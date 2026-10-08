"""`veos tokens`: resolve playbooks/<id>/tokens.json (+ optional <project>/plan/tokens.override.json) into work/tokens.json.

One source: the creator's playbook tokens (colours by role, font slots, type, layout, motion, camera presets, stage
morphs, budgets, tone). Hard rules are re-checked after the merge: fixed-meaning roles can't be recoloured, brandable
colours get an OKLCH lightness auto-fix when contrast against their `text_on` fails, override patches that touch safe
zones / fixed meanings / loudness are rejected.

v3 (`"schema": "veos.tokens/3"`, playbooks/_styles/tokens.schema.md): `effective_style` resolves style -> format ->
theme -> override patch (through `locks`), enforces the exception registry and `inserts.fetch: false`, maps a v1 file's
`rules_v0` / budgets to the v3 blocks (the v1 file itself loads unchanged), and PV-1...PV-12 are checked by
profilecheck.py. engine/SPEC.md section 7.
"""
from __future__ import annotations

import copy
import math
import os
import re
from pathlib import Path
from typing import Any

from .core import VeosError, need_project, r3, read_json, write_json

REPO = Path(__file__).resolve().parents[3]
DEFAULT_PLAYBOOK = "naman"
PROTECTED_PREFIXES = ("roles.bad", "roles.good", "roles.comedy", "fixed_meaning", "layout.safe", "layout.ig_ui",
                      "layout.size")
PROTECTED_WORDS = ("loudness", "lufs", "truepeak", "true_peak")
PASSTHROUGH = ("budgets", "gradients", "max_bright_per_frame", "fixed_meaning", "tones", "tone_treatment", "sound")


def add_args(p, cmd):
    p.add_argument("--playbook", help="playbook id (default: project.json `playbook`, else naman)")
    p.add_argument("--format", default=None, help="v3 playbooks: format id (default: override `format`, timeline meta.format, profile default)")
    p.add_argument("--theme", default=None, help="v3 playbooks: theme pack id (default: override `theme`, timeline meta.theme, profile default)")


# ------------------------------------------------------------------ colour maths
def _hex_rgb(h: str) -> tuple[float, float, float]:
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))  # type: ignore[return-value]


def _rgb_hex(rgb) -> str:
    return "#" + "".join(f"{max(0, min(255, round(c * 255))):02X}" for c in rgb)


def _lin(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _unlin(c: float) -> float:
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def luminance(h: str) -> float:
    r, g, b = (_lin(c) for c in _hex_rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def _to_oklch(h: str):
    r, g, b = (_lin(c) for c in _hex_rgb(h))
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    bb = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return L, math.hypot(a, bb), math.atan2(bb, a)


def _from_oklch(L, C, hue):
    """OKLCH -> (r,g,b) linear-gamma-encoded floats, reducing chroma until inside the sRGB gamut."""
    for _ in range(40):
        a, b = C * math.cos(hue), C * math.sin(hue)
        l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
        m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
        s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
        r = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
        g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
        bl = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
        if min(r, g, bl) >= -1e-4 and max(r, g, bl) <= 1 + 1e-4:
            break
        C *= 0.96
    return tuple(_unlin(max(0.0, min(1.0, c))) for c in (r, g, bl))


def fix_contrast(colour: str, text: str, need: float):
    """Move OKLCH lightness of `colour` until contrast(colour, text) >= need. Returns (hex, changed, ok)."""
    if contrast(colour, text) >= need:
        return colour, False, True
    L, C, h = _to_oklch(colour)
    lighten = luminance(text) < luminance(colour) or luminance(text) < 0.18  # dark text -> lighter bg
    step = 0.01 if lighten else -0.01
    best = colour
    for i in range(1, 101):
        L2 = L + step * i
        if L2 > 1 or L2 < 0:
            break
        cand = _rgb_hex(_from_oklch(L2, C, h))
        best = cand
        if contrast(cand, text) >= need:
            return cand, True, True
    if not lighten:  # darkening failed -> try the other direction before giving up
        for i in range(1, 101):
            L2 = L + 0.01 * i
            if L2 > 1:
                break
            cand = _rgb_hex(_from_oklch(L2, C, h))
            if contrast(cand, text) >= need:
                return cand, True, True
    return best, True, False


# ------------------------------------------------------------------ helpers
def _norm_hex(v) -> str | None:
    if isinstance(v, str) and re.fullmatch(r"#?[0-9a-fA-F]{6}|#?[0-9a-fA-F]{3}", v.strip()):
        v = v.strip().lstrip("#")
        if len(v) == 3:
            v = "".join(c * 2 for c in v)
        return "#" + v.upper()
    return None


def _weights(spec: str) -> str:
    m = re.search(r"(\d{3})\s*-\s*(\d{3})", spec or "")
    if m:
        return f"{m.group(1)} {m.group(2)}"
    m = re.search(r"\d{3}", spec or "")
    return m.group(0) if m else "400"


FONT_REF_SKIP = ("evidence", "notes", "note", "unverified", "inspired_by", "lineage", "desc", "warnings", "locks")


def referenced_families(obj, fonts_json: dict, text: str | None = None) -> list[str]:
    """Bundled families (assets/fonts/fonts.json) named anywhere in a resolved style (string values: "Archivo Black",
    "Montserrat 800", "'Jost', sans-serif"; explanation keys like notes / evidence skipped) or in `text` (plan/scenes.js).
    Longest names first, so "Barlow Semi Condensed" is not also read as "Barlow Condensed"."""
    fams = sorted((k for k in fonts_json if not k.startswith("_")), key=len, reverse=True)
    pats = {f: re.compile(r"(?<![\w-])" + re.escape(f) + r"(?![\w-])") for f in fams}
    found: set[str] = set()

    def scan(s: str):
        for f in fams:
            if f in s and pats[f].search(s):
                found.add(f)
                s = pats[f].sub(" ", s)

    def walk(v, key=""):
        if key in FONT_REF_SKIP:
            return
        if isinstance(v, str):
            scan(v)
        elif isinstance(v, dict):
            for k, x in v.items():
                walk(x, str(k))
        elif isinstance(v, list):
            for x in v:
                walk(x, key)

    walk(obj)
    if text:
        scan(text)
    return sorted(found)


def font_entry(family: str, fonts_json: dict, warnings: list[str]):
    meta = fonts_json.get(family)
    if not meta:
        warnings.append(f"font '{family}' not in assets/fonts/fonts.json; falls back to the system font")
        return []
    w = _weights(meta.get("weights", ""))
    out = []
    for f in meta.get("files", []):
        p = REPO / "assets" / "fonts" / f
        if not p.exists():
            warnings.append(f"font file missing: {p}")
            continue
        italic = "italic" in f.lower() or ("italic" in meta.get("weights", "").lower() and len(meta["files"]) == 1)
        fw = (meta.get("file_weights") or {}).get(f, w)  # static families (Poppins...): one weight per file
        out.append({"src": p.as_uri(), "weight": fw, "style": "italic" if italic else "normal"})
    return out


def _set_path(d: dict, path: str, value) -> bool:
    keys = path.split(".")
    cur = d
    for k in keys[:-1]:
        if isinstance(cur, list) and k.isdigit() and int(k) < len(cur):
            cur = cur[int(k)]
        elif isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return False
    last = keys[-1]
    if isinstance(cur, list) and last.isdigit() and int(last) < len(cur):
        cur[int(last)] = value
        return True
    if isinstance(cur, dict) and last in cur:
        cur[last] = value
        return True
    return False


# ------------------------------------------------------------------ v3 loader (schema veos.tokens/3)
SCHEMA_V3 = "veos.tokens/3"
V3_PASSTHROUGH = ("schema", "kind", "style", "lineage", "profile", "formats", "worlds", "captions", "layouts", "slots", "camera_crops",
                  "zoom_policy", "canvas_camera", "grades", "hooks", "structure", "cadence", "exceptions",
                  "running_state", "anchors", "data", "citations", "inserts", "footage", "dialogue", "ink", "continuity",
                  "series", "brand", "validator")
FORMAT_META_KEYS = ("name", "when", "shared_dna", "layouts", "profile")
THEME_META_KEYS = ("name", "when", "roles", "worlds", "gradients", "grade", "captions")
V1_SOUND_KEYS = ("palette_vibes", "allowed_roles", "banned_roles", "preferred")

# Part C.2 exception registry: limit -> (direction, registry bound). ">=" limits are floors (a style may only raise
# them), "<=" limits are caps (a style may only lower them). Looser values are clamped with a warning.
EXC_REGISTRY: dict[str, dict] = {
    "E1": {"name": "behind_text", "limits": {"min_visible": (">=", 0.65), "max_at_once": ("<=", 1), "min_hold_s": (">=", 0.6)}},
    "E2": {"name": "chaos_burst", "limits": {"max_s": ("<=", 1.5), "max_per_60s": ("<=", 1), "max_per_reel": ("<=", 2),
                                             "max_snippets": ("<=", 6), "clean_after_s": (">=", 1.0)}},
    "E3": {"name": "quiet_type", "limits": {"subtitle_min_px": (">=", 36), "label_min_px": (">=", 28),
                                            "contrast_min": (">=", 7.0), "pill_contrast_min": (">=", 4.5),
                                            "weight_min": (">=", 500), "max_lines": ("<=", 2), "max_chars_line": ("<=", 44)}},
    "E4": {"name": "ambient_field", "limits": {"max_items": ("<=", 30), "max_item_area": ("<=", 0.12),
                                               "max_speed_px_s": ("<=", 60), "dim_under_text": (">=", 0.4),
                                               "blur_px": (">=", 6), "max_s": ("<=", 5)}},
    "E5": {"name": "edge_bleed", "limits": {"min_display_px": (">=", 180), "min_margin": (">=", 24), "max_at_once": ("<=", 1)}},
    "E6": {"name": "hard_swap", "limits": {"slot_tolerance_px": ("<=", 4)}},
}
EXC_BY_NAME = {v["name"]: k for k, v in EXC_REGISTRY.items()}

# v1 rules_v0 -> v2 registry ids (tokens.schema §4). Order follows rules_v0.
V1_RULE_MAP = {"M1": ("V-F0",), "M7": ("V-CADENCE",), "M4": ("V-TITLE",), "M6": ("V-ONWORD",), "M12": ("V-SAFE", "V-FACE"),
               "N5-zoom": ("V-CAMERA",), "N6": ("V-HUES",), "M10": ("V-LEDGER",), "M9": ("V-COMEDY",), "M13": ("V-PROMISE",)}

# Default lock level per path when the file's `locks` block says nothing (structure Part D.2, tokens.schema §2).
# (pattern, level, range). `*` matches one path segment; a pattern also covers every path below it.
DEFAULT_LOCKS: list[tuple] = [
    ("schema", "DNA", None), ("kind", "DNA", None), ("style", "DNA", None), ("lineage", "DNA", None),
    ("locks", "DNA", None), ("validator", "DNA", None), ("formats", "DNA", None),
    ("profile", "DNA", None), ("profile.presenter.share", "TUNE", "±10"), ("profile.presenter.max_absence_s", "TUNE", "±15%"),
    ("profile.duration", "TUNE", None), ("profile.language", "VAR", None), ("profile.numbers", "VAR", None),
    ("profile.tone", "TUNE", None), ("profile.themes.packs", "VAR", None), ("profile.themes.default", "VAR", None),
    ("profile.formats", "VAR", None), ("profile.cta", "VAR", None), ("profile.cta.devices", "DNA", None),
    ("profile.modules.series", "VAR", None), ("profile.modules.brand", "VAR", None),
    ("creator", "VAR", None), ("tone", "TUNE", None), ("roles", "DNA", None), ("roles.*.default", "VAR", None),
    ("fixed_meaning", "DNA", None), ("max_bright_per_frame", "TUNE", [2, 4]), ("gradients", "TUNE", None),
    ("themes", "VAR", None), ("worlds", "DNA", None), ("font_slots", "DNA", None), ("font_slots.*.family", "TUNE", None),
    ("type", "DNA", None), ("type.*.size", "TUNE", None), ("captions", "DNA", None),
    ("captions.profiles.*.skin.size", "TUNE", None), ("captions.profiles.*.position.cy", "TUNE", "±5%"),
    ("layout", "TUNE", None), ("layouts", "DNA", None), ("layouts.*.presenter", "TUNE", "±5%"),
    ("layouts.*.graphic", "TUNE", "±5%"), ("layouts.*.caption", "TUNE", "±5%"), ("slots", "DNA", None),
    ("motion", "TUNE", "±15%"), ("camera_presets", "DNA", None), ("zoom_policy", "DNA", None),
    ("canvas_camera", "DNA", None), ("stage_morphs", "DNA", None), ("grades", "TUNE", None),
    ("hooks", "DNA", None), ("structure", "DNA", None), ("cadence", "TUNE", "±15%"), ("budgets", "TUNE", None),
    ("exceptions", "DNA", None), ("running_state", "DNA", None), ("anchors", "DNA", None), ("data", "DNA", None),
    ("citations", "DNA", None), ("inserts", "DNA", None), ("footage", "DNA", None), ("dialogue", "DNA", None),
    ("ink", "DNA", None), ("continuity", "DNA", None), ("series", "DNA", None), ("series.name", "VAR", None),
    ("series.number", "VAR", None), ("brand", "DNA", None), ("sound", "VAR", None), ("tones", "DNA", None),
    ("tone_treatment", "DNA", None),
]


def schema_version(pb: dict) -> int:
    """3 for `"schema": "veos.tokens/3"`, 1 for a file without `schema` (the reference v1 format)."""
    s = pb.get("schema")
    if s is None:
        return 1
    if s == SCHEMA_V3:
        return 3
    raise VeosError("BAD_TOKENS", f"unknown tokens schema {s!r}", f"Use \"schema\": \"{SCHEMA_V3}\" or omit it for a v1 file.")


def deep_merge(base: dict, over: dict) -> dict:
    """Merge `over` into `base` in place (dicts recurse, everything else replaces) and return `base`."""
    for k, v in (over or {}).items():
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            deep_merge(base[k], v)
        else:
            base[k] = copy.deepcopy(v)
    return base


def _get_path(d, path: str):
    cur = d
    for k in path.split("."):
        if isinstance(cur, list) and k.isdigit() and int(k) < len(cur):
            cur = cur[int(k)]
        elif isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return None
    return cur


def find_misplaced_sound(pb: dict) -> list[str]:
    """Dotted paths of every `sound` key that is not top-level (the reference bug: camera_presets.snap-punch.sound)."""
    out: list[str] = []

    def walk(node, path):
        if isinstance(node, dict):
            for k, v in node.items():
                p = f"{path}.{k}" if path else k
                if k == "sound" and path:
                    out.append(p)
                walk(v, p)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}.{i}")
    for k, v in pb.items():
        walk(v, k)
    return out


def check_exceptions(exc: dict | None, warnings: list[str], errors: list[str]) -> dict:
    """Closed registry (structure Part C.2): unknown ids rejected; looser limits clamped; missing limits filled."""
    out: dict = {}
    for key, val in (exc or {}).items():
        eid = key if key in EXC_REGISTRY else EXC_BY_NAME.get(key)
        if eid is None:
            errors.append(f"exceptions.{key} is not in the exception registry (E1-E6); add it to structure Part C.2 first")
            continue
        if val in (None, False):  # switched off (buyers may do this at VAR level)
            continue
        reg = EXC_REGISTRY[eid]["limits"]
        lim = {k: v for k, (_, v) in reg.items()}
        if isinstance(val, dict):
            for k, v in val.items():
                if k not in reg:
                    warnings.append(f"exceptions.{eid}.{k} is not a registry limit; ignored")
                    continue
                if not isinstance(v, (int, float)) or isinstance(v, bool):
                    warnings.append(f"exceptions.{eid}.{k} = {v!r} is not a number; registry value {reg[k][1]} used")
                    continue
                direction, bound = reg[k]
                if (direction == ">=" and v < bound) or (direction == "<=" and v > bound):
                    warnings.append(f"exceptions.{eid}.{k} = {v} is looser than the registry ({direction} {bound}); clamped to {bound}")
                    v = bound
                lim[k] = v
        elif val is not True:
            warnings.append(f"exceptions.{eid} = {val!r} should be an object of limits or true; registry limits used")
        out[eid] = lim
    return out


def _v1_profile(pb: dict) -> dict:
    cr, tone, budgets = pb.get("creator") or {}, pb.get("tone") or {}, pb.get("budgets") or {}
    lang = cr.get("language") or "en"
    indian = str(lang).lower() in ("hinglish", "hi", "ta", "te", "mr", "bn", "kn", "ml", "gu", "pa")
    cta = cr.get("cta") or {}
    return {
        "source_type": "talking_head",
        "presenter": {"presence": "anchor", "share": [80, 100],
                      "max_absence_s": budgets.get("max_full_screen_without_speaker_s", 3)},
        "spine": "talking_head",
        "captions": {"mode": "full", "role": "support", "mute_policy": "mute_safe"},
        "graphics": "primary",
        "duration": {"class": "short", "target_s": [30, 60]},
        "language": {"speech": lang, "captions": {"lang": cr.get("caption_language") or lang, "script": "Latn",
                                                  "transform": "verbatim"},
                     "on_screen": cr.get("banner_language") or "en", "post_title": lang},
        "numbers": {"grouping": "indian" if indian else "international", "currency": "₹" if indian else "$",
                    "compact": "lakh_crore" if indian else "k_m_b", "units": "metric", "decimals": 0},
        "tone": {"energy": tone.get("energy") if tone.get("energy") in ("calm", "balanced", "hype") else "balanced",
                 "comedy": "roast" if tone.get("roast") else "off"},
        "themes": {"policy": "single", "packs": [], "default": None},
        "formats": {"list": ["F-A"], "default": "F-A"},
        "footage_dependency": "medium",
        "cta": {"devices": ["comment_keyword"] if cta.get("pattern") else ["none"], "placement": "end"},
        "modules": {m: False for m in ("chrome", "running_state", "anchors", "data_figures", "citations", "dialogue",
                                       "canvas_camera", "ink", "continuity", "series", "brand")},
    }


def _v1_cadence(budgets: dict) -> dict:
    return {"sc_per_10s": None, "hook_sc_3s": budgets.get("hook_changes_first_3s"),
            "max_gap_s": budgets.get("change_every_s", 1.5), "hook_max_gap_s": budgets.get("hook_change_every_s", 1.0),
            "max_static_s": budgets.get("max_static_s", 2.5), "caption_weight": 0.5, "cuts_per_min": None,
            "median_shot_s": None, "continuous_motion_required": False}


def _v1_rules(pb: dict) -> dict:
    enabled = pb.get("rules_v0") or list(V1_RULE_MAP)
    rules, aliases = {}, {}
    for m in enabled:
        for vid in V1_RULE_MAP.get(m, ()):
            rules[vid] = {"legacy": True}
            aliases[vid] = m
        if m not in V1_RULE_MAP:
            rules[m] = True  # unknown legacy id: reported as not implemented by the validator
    return {"rules": rules, "aliases": aliases}


def v1_view(pb: dict) -> dict:
    """The v3 blocks synthesised for a v1 file (tokens.schema §4). The v1 keys themselves are not touched."""
    roles = pb.get("roles") or {}
    col = lambda r, d: (roles.get(r) or {}).get("default", d)  # noqa: E731
    sub = (pb.get("type") or {}).get("subtitle") or {}
    wpc = sub.get("words_per_card") or [2, 3]
    budgets = pb.get("budgets") or {}
    return {
        "profile": _v1_profile(pb),
        "formats": {"F-A": {"name": "default", "profile": {}}},
        "worlds": {"studio": {"kind": "footage"}, "canvas": {"kind": "canvas", "bg": col("canvas", "#FCFCFC"),
                                                             "grid": {"colour": col("grid", "#C5C5C5")}},
                   "data": {"kind": "stage", "bg": col("night", "#07070C")}},
        "captions": {"default": "CS-1", "by_layout": {}, "speakers": {}, "profiles": {"CS-1": {
            "unit": "group", "words": list(wpc), "case": sub.get("case", "lower"),
            "skin": {"slot": sub.get("slot", "body"), "weight": sub.get("weight", 800), "size": sub.get("size", 54),
                     "text_class": "TC-subtitle"},
            "position": {"anchor": "fixed_y", "cy": ((pb.get("layout") or {}).get("caption_cy") or {}).get("full", 1300)}}}},
        "hooks": {"default": "HA-01", "allowed": ["HA-01"],
                  "stopper": {"payoff_by_s": budgets.get("result_by_s"), "hook_sc_3s": budgets.get("hook_changes_first_3s")},
                  "f0": {"require": [], "forbid": []}},
        "structure": {"type": "list", "rehook_every_s": None, "intro_max_ratio": 0.15},
        "cadence": _v1_cadence(budgets),
        "exceptions": {},
        "validator": _v1_rules(pb),
    }


def _lock_match(pattern: str, path: str):
    """Specificity (segments, literal segments) when `pattern` covers `path` (equal or ancestor), else None."""
    pp, sp = pattern.split("."), path.split(".")
    if len(pp) > len(sp):
        return None
    for a, b in zip(pp, sp):
        if a != "*" and a != b:
            return None
    return (len(pp), sum(1 for a in pp if a != "*"))


def lock_for(path: str, locks: dict | None) -> tuple[str, Any, str]:
    """(level, range, source pattern) of the most specific lock covering `path`; the file's locks win ties."""
    best, best_key = ("VAR", None, "(none)"), (-1, -1, -1)
    for pat, lv in (locks or {}).items():
        if pat.startswith("§") or not isinstance(lv, dict):
            continue
        m = _lock_match(pat, path)
        if m is not None and (m[0], m[1], 1) > best_key:
            best, best_key = (str(lv.get("level", "DNA")).upper(), lv.get("range"), pat), (m[0], m[1], 1)
    for pat, level, rng in DEFAULT_LOCKS:
        m = _lock_match(pat, path)
        if m is not None and (m[0], m[1], 0) > best_key:
            best, best_key = (level, rng, f"default:{pat}"), (m[0], m[1], 0)
    return best


def _relative(rng) -> tuple[float, bool] | None:
    m = re.fullmatch(r"\s*±\s*(\d+(?:\.\d+)?)\s*(%?)\s*", str(rng)) if isinstance(rng, str) else None
    return (float(m.group(1)), m.group(2) == "%") if m else None


def _clamp_num(v, lo, hi):
    return max(lo, min(hi, v))


def apply_lock(path: str, old, new, locks: dict | None, warnings: list[str]) -> tuple[bool, Any]:
    """Classify an override patch against `locks` (structure Part D): DNA rejected; TUNE clamped or checked against its
    range; VAR / NICHE applied. Returns (accept, value)."""
    level, rng, src = lock_for(path, locks)
    if level in ("VAR", "NICHE"):
        return True, new
    if level == "DNA":
        warnings.append(f"override patch '{path}' changes DNA (lock {src}); rejected - record it as a deviation in the "
                        "playbook's lineage instead")
        return False, old
    # TUNE
    isnum = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool)  # noqa: E731
    rel = _relative(rng)
    if rel is not None and old is not None:
        amt, pct = rel

        def clamp_rel(o, n):
            if not (isnum(o) and isnum(n)):
                return n
            d = abs(o) * amt / 100 if pct else amt
            return _clamp_num(n, o - d, o + d)
        if isinstance(new, list) and isinstance(old, list) and len(new) == len(old):
            val = [clamp_rel(o, n) for o, n in zip(old, new)]
        else:
            val = clamp_rel(old, new)
        if val != new:
            warnings.append(f"override patch '{path}' = {new} is outside its TUNE range ({rng} of {old}); clamped to {val}")
        return True, val
    if isinstance(rng, list) and len(rng) == 2 and all(isnum(x) for x in rng) and isnum(new):
        val = _clamp_num(new, min(rng), max(rng))
        if val != new:
            warnings.append(f"override patch '{path}' = {new} is outside its TUNE range {rng}; clamped to {val}")
        return True, val
    if isinstance(rng, list) and rng and not all(isnum(x) for x in rng):
        if new in rng:
            return True, new
        warnings.append(f"override patch '{path}' = {new!r} is not in its TUNE range {rng}; rejected")
        return False, old
    if isinstance(rng, str) and rng:
        warnings.append(f"override patch '{path}' is TUNE: keep it within \"{rng}\"")
    return True, new


def _apply_theme(eff: dict, theme_id: str, warnings: list[str]) -> dict:
    """Theme pack: brandable role hex, world colours, gradients, grade. Returns the resolved theme record."""
    th = (eff.get("themes") or {}).get(theme_id) or {}
    roles = eff.get("roles") or {}
    fixed = set(eff.get("fixed_meaning") or [])
    for r, hx in (th.get("roles") or {}).items():
        h = _norm_hex(hx)
        if r not in roles:
            warnings.append(f"theme {theme_id}: role '{r}' is not a playbook role; ignored")
        elif r in fixed or roles[r].get("brandable") is False:
            warnings.append(f"theme {theme_id}: role '{r}' has a fixed meaning; a theme may only change brandable roles")
        elif not h:
            warnings.append(f"theme {theme_id}: role '{r}' = {hx!r} is not a hex colour; ignored")
        else:
            roles[r]["default"] = h
    if th.get("worlds"):
        eff["worlds"] = deep_merge(eff.get("worlds") or {}, th["worlds"])
    if th.get("gradients"):
        eff["gradients"] = deep_merge(eff.get("gradients") or {}, th["gradients"])
    # captions per theme (A21 / A26): `captions.by_theme.<theme>` and a pack's own `captions` patch merge into captions
    # (by_layout, default, profiles.<id>.position.cy, ...), so a light theme can switch profiles or move the caption y
    caps = eff.get("captions")
    if isinstance(caps, dict):
        bt = caps.get("by_theme")
        if isinstance(bt, dict) and isinstance(bt.get(theme_id), dict):
            deep_merge(caps, {k: v for k, v in bt[theme_id].items() if k != "by_theme"})
        if isinstance(th.get("captions"), dict):
            deep_merge(caps, {k: v for k, v in th["captions"].items() if k != "by_theme"})
    elif isinstance(th.get("captions"), dict):
        eff["captions"] = copy.deepcopy(th["captions"])
    return {"id": theme_id, "name": th.get("name"), "grade": th.get("grade")}


def _theme_contrast(eff: dict, base_roles: dict | None = None) -> list[str]:
    """PV-8: every pack's role overrides must reach 4.5:1 (3:1 large-text-only) against their text colour, the text
    colour as THAT pack resolves it (its own override of the text role, else the style's default; never the text
    colour of the theme the reel happens to use)."""
    out = []
    roles = eff.get("roles") or {}
    base = base_roles if base_roles is not None else roles
    for tid, th in (eff.get("_theme_packs") or {}).items():
        own = (th or {}).get("roles") or {}
        for r, hx in own.items():
            spec = roles.get(r) or {}
            h = _norm_hex(hx)
            if not h or "text_on" not in spec:
                continue
            to = spec["text_on"]
            t = own.get(to) or ((base.get(to) or {}).get("default") if isinstance(base.get(to), dict) else None) or to
            t = _norm_hex(t)
            if not t:
                continue
            need = 3.0 if spec.get("large_text_only") else 4.5
            if contrast(h, t) < need:
                _, _, ok = fix_contrast(h, t, need)
                if not ok:
                    out.append(f"theme {tid}: role '{r}' {h} cannot reach {need}:1 against {spec['text_on']}")
    return out


def _pick(kind: str, requested, allowed: list, default, warnings: list[str]):
    if requested and requested in allowed:
        return requested
    if requested:
        warnings.append(f"{kind} '{requested}' is not available in this playbook ({', '.join(allowed) or 'none'}); "
                        f"using {default}")
    return default


def effective_style(pb: dict, *, fmt: str | None = None, theme: str | None = None, override: dict | None = None,
                    warnings: list[str] | None = None, errors: list[str] | None = None) -> dict:
    """The playbook as the validator and renderer see it for one reel.

    v1 (no `schema`): the file unchanged plus synthesised v3 blocks (profile, cadence, hooks, validator...) that are
    absent from v1; `override` is NOT applied (v1 behaviour: overrides only reach work/tokens.json colours/fonts/patch).
    v3: style -> format -> theme -> override patch (with `locks`), exceptions registry, `inserts.fetch` rejected.
    `_resolved` records {schema, format, theme, base_profile, layouts}.
    """
    warnings = [] if warnings is None else warnings
    errors = [] if errors is None else errors
    for p in find_misplaced_sound(pb):
        warnings.append(f"`sound` found at {p}; it must be a top-level block (tokens.schema §3.22), so it is ignored there")
    ver = schema_version(pb)
    eff = copy.deepcopy(pb)
    if ver == 1:
        for k, v in v1_view(pb).items():
            eff.setdefault(k, v)
        eff["_resolved"] = {"schema": 1, "format": "F-A", "theme": None, "base_profile": None, "layouts": []}
        return eff

    override = override or {}
    # blocks every v3 reader can rely on
    for k, d in (("profile", {}), ("formats", {}), ("themes", {}), ("exceptions", {}), ("cadence", {}), ("hooks", {}),
                 ("validator", {}), ("locks", {}), ("budgets", {}), ("layout", {}), ("type", {}), ("roles", {})):
        if not isinstance(eff.get(k), dict):
            eff[k] = copy.deepcopy(d)
    snd = eff.get("sound")
    if isinstance(snd, dict) and any(k in snd for k in V1_SOUND_KEYS):
        warnings.append("sound carries v1 palette keys (palette_vibes/allowed_roles/...); v3 templates carry no per-style "
                        "palette (tokens.schema §3.22)")
    if "sound" not in eff:
        warnings.append("no top-level `sound` block; the sound rules run on the SFX pack defaults")
    eff["exceptions"] = check_exceptions(eff.get("exceptions"), warnings, errors)

    prof = eff["profile"]
    base_profile = copy.deepcopy(prof)
    # format
    flist = list(get_list(prof, "formats.list") or list(eff["formats"]) or [])
    fdefault = (prof.get("formats") or {}).get("default") or (flist[0] if flist else None)
    fid = _pick("format", fmt or override.get("format"), flist, fdefault, warnings)
    layouts_sel: list = []
    # the blocks any format overrides, as the style has them before a format applies (PV-12 checks each format alone)
    fkeys = {k for f in eff["formats"].values() if isinstance(f, dict) for k in f if k not in FORMAT_META_KEYS}
    base_blocks = {k: copy.deepcopy(eff.get(k)) for k in fkeys}
    if fid and fid in eff["formats"]:
        f = eff["formats"][fid] or {}
        deep_merge(prof, f.get("profile") or {})
        layouts_sel = list(f.get("layouts") or [])
        for k, v in f.items():
            if k in FORMAT_META_KEYS:
                continue
            if isinstance(v, dict) and isinstance(eff.get(k), dict):
                deep_merge(eff[k], v)
            else:
                eff[k] = copy.deepcopy(v)
        for lid in layouts_sel:
            if lid not in (eff.get("layouts") or {}):
                warnings.append(f"format {fid} uses layout '{lid}', which is not defined in layouts")
    elif fid:
        warnings.append(f"format '{fid}' is listed in profile.formats but not defined in formats")
    # theme
    eff["_theme_packs"] = copy.deepcopy(eff.get("themes") or {})
    base_roles = copy.deepcopy(eff.get("roles") or {})
    packs = list(get_list(prof, "themes.packs") or list(eff["themes"]) or [])
    tdefault = (prof.get("themes") or {}).get("default") or (packs[0] if packs else None)
    tid = _pick("theme", theme or override.get("theme"), packs, tdefault, warnings)
    theme_rec = None
    if tid and tid in eff["themes"]:
        theme_rec = _apply_theme(eff, tid, warnings)
    elif tid:
        warnings.append(f"theme '{tid}' is listed in profile.themes but not defined in themes")
    eff["_theme_contrast_fail"] = _theme_contrast(eff, base_roles)
    # per-reel override patch, through the locks (colours / fonts / tone are applied by resolve())
    locks = eff.get("locks") or {}
    for path, val in (override.get("patch") or {}).items():
        low = path.lower()
        if path.startswith(PROTECTED_PREFIXES) or any(w in low for w in PROTECTED_WORDS):
            warnings.append(f"override patch '{path}' touches a hard rule; rejected")
            continue
        old = _get_path(eff, path)
        if old is None and not _set_path(copy.deepcopy(eff), path, val):
            warnings.append(f"override patch: unknown path '{path}'; rejected")
            continue
        ok, v = apply_lock(path, old, val, locks, warnings)
        if ok:
            _set_path(eff, path, v)
    if (eff.get("inserts") or {}).get("fetch") is True:
        errors.append("inserts.fetch is true: the engine never fetches third-party media (NC-7); set it to false")
    # v1 budgets are fallbacks for the v3 cadence / hooks / presenter numbers (tokens.schema §4)
    b, cad = eff.get("budgets") or {}, eff["cadence"]
    for bk, ck in (("change_every_s", "max_gap_s"), ("hook_change_every_s", "hook_max_gap_s"),
                   ("max_static_s", "max_static_s"), ("hook_changes_first_3s", "hook_sc_3s")):
        if ck not in cad and bk in b:
            cad[ck] = b[bk]
    stopper = eff["hooks"].setdefault("stopper", {}) if isinstance(eff["hooks"].get("stopper", {}), dict) else {}
    if "hook_sc_3s" not in cad and stopper.get("hook_sc_3s") is not None:
        cad["hook_sc_3s"] = stopper["hook_sc_3s"]
    if stopper.get("payoff_by_s") is None and "result_by_s" in b:
        stopper["payoff_by_s"] = b["result_by_s"]
    pres = prof.get("presenter")
    if isinstance(pres, dict) and pres.get("max_absence_s") is None and "max_full_screen_without_speaker_s" in b:
        pres["max_absence_s"] = b["max_full_screen_without_speaker_s"]
    # validator: legacy rules_v0 only when there is no validator.rules
    if not (eff["validator"].get("rules")) and eff.get("rules_v0"):
        eff["validator"] = {**_v1_rules(eff), **{k: v for k, v in eff["validator"].items() if k != "rules"}}
    eff["_resolved"] = {"schema": 3, "format": fid, "theme": tid, "theme_record": theme_rec,
                        "base_profile": base_profile, "base_blocks": base_blocks, "layouts": layouts_sel}
    return eff


def get_list(d, path: str) -> list | None:
    v = _get_path(d, path)
    return v if isinstance(v, list) else None


def load_effective(playbook_id: str, *, fmt=None, theme=None, override=None) -> tuple[dict, list[str]]:
    """load_playbook + effective_style; tokens errors raise BAD_TOKENS."""
    warnings: list[str] = []
    errors: list[str] = []
    eff = effective_style(load_playbook(playbook_id), fmt=fmt, theme=theme, override=override,
                          warnings=warnings, errors=errors)
    if errors:
        raise VeosError("BAD_TOKENS", f"playbook {playbook_id} tokens are invalid: " + "; ".join(errors),
                        "Fix the listed keys in tokens.json (see playbooks/_styles/tokens.schema.md).")
    return eff, warnings


# ------------------------------------------------------------------ main
def playbooks_dir() -> Path:
    """Folder that holds user playbooks/<id>/tokens.json (see paths.py; env VEOS_PLAYBOOKS overrides)."""
    from . import paths
    return paths.playbooks_dir()


def load_playbook(playbook_id: str) -> dict:
    """A user playbook (or the shipped reference); else a shipped style template by id (VEOS_STYLES /
    paths.styles_dir()), so `veos tokens --playbook <template-id>` resolves a template directly."""
    from . import paths
    d = paths.find_playbook_dir(playbook_id)
    if d is None and playbook_id and not playbook_id.startswith(("_", ".")) and \
            (paths.styles_dir() / playbook_id / "tokens.json").is_file():
        d = paths.styles_dir() / playbook_id
    if d is None:
        pp = playbooks_dir() / playbook_id / "tokens.json"
        have = sorted(x.name for x in playbooks_dir().iterdir() if (x / "tokens.json").exists()) if playbooks_dir().exists() else []
        raise VeosError("PLAYBOOK_MISSING", f"playbook not found: {pp}",
                        f"Use one of: {', '.join(have) or '(none)'}; or create playbooks/<id>/tokens.json.")
    return read_json(d / "tokens.json")


def project_playbook(pr, explicit: str | None = None, timeline_meta: dict | None = None) -> str:
    """playbook id: explicit > timeline meta.playbook > project.json `playbook` > (old) project.json `brand` if such a playbook exists > naman."""
    if explicit:
        return explicit
    if timeline_meta and timeline_meta.get("playbook"):
        return str(timeline_meta["playbook"])
    pj = pr.root / "project.json"
    st = read_json(pj) if pj.exists() else {}
    if st.get("playbook"):
        return str(st["playbook"])
    for old in (st.get("brand"), (st.get("meta") or {}).get("brand")):  # v1 project.json compat
        if old and __import__("veos.paths", fromlist=["x"]).find_playbook_dir(str(old)):
            return str(old)
    return DEFAULT_PLAYBOOK


def resolve(playbook_id: str, override: dict | None = None, fmt: str | None = None, theme: str | None = None) -> dict:
    raw = load_playbook(playbook_id)
    warnings: list[str] = []
    override = override or {}
    v3 = schema_version(raw) == 3
    if v3:  # style -> format -> theme -> override patch (locks); colours / fonts / tone below as for v1
        errors: list[str] = []
        pb = effective_style(raw, fmt=fmt, theme=theme, override=override, warnings=warnings, errors=errors)
        if errors:
            raise VeosError("BAD_TOKENS", f"playbook {playbook_id} tokens are invalid: " + "; ".join(errors),
                            "Fix the listed keys in tokens.json (see playbooks/_styles/tokens.schema.md).")
    else:
        pb = raw
        for p in find_misplaced_sound(raw):
            warnings.append(f"`sound` found at {p}; it must be a top-level block (tokens.schema §3.22), so it is ignored there")
    fonts_json = read_json(REPO / "assets" / "fonts" / "fonts.json")
    roles = pb["roles"]
    fixed = set(pb.get("fixed_meaning", [])) | {r for r, v in roles.items() if v.get("brandable") is False and
                                                r in ("bad", "good", "comedy")}
    colours = {r: v["default"] for r, v in roles.items()}

    # optional per-reel override: colours (brandable roles only), fonts, tone, patch (dotted paths)
    for r, v in (override.get("colours") or {}).items():
        hx = _norm_hex(v)
        if r not in roles:
            warnings.append(f"override colour '{r}' is not a playbook role; ignored")
        elif r in fixed:
            warnings.append(f"override tried to set fixed-meaning role '{r}'; ignored")
        elif not roles[r].get("brandable"):
            warnings.append(f"role '{r}' is not brandable; ignored")
        elif v3 and lock_for(f"roles.{r}.default", pb.get("locks"))[0] == "DNA":
            warnings.append(f"override colour '{r}' is locked (DNA) in this style; ignored")
        elif not hx:
            warnings.append(f"override colour '{r}' = {v!r} is not a hex colour; ignored")
        else:
            colours[r] = hx
    for path, val in ((override.get("patch") or {}) if not v3 else {}).items():  # v3: applied with the locks above
        low = path.lower()
        if path.startswith(PROTECTED_PREFIXES) or any(w in low for w in PROTECTED_WORDS):
            warnings.append(f"override patch '{path}' touches a hard rule; rejected")
        elif not _set_path(pb, path, val):
            warnings.append(f"override patch: unknown path '{path}'; rejected")

    # contrast re-check on every role that has text_on
    text_on = {}
    for r, v in roles.items():
        if "text_on" not in v:
            continue
        t = colours.get(v["text_on"], v["text_on"])
        text_on[r] = t
        need = 3.0 if v.get("large_text_only") else 4.5
        if r in fixed or not v.get("brandable"):
            if contrast(colours[r], t) < need:
                warnings.append(f"fixed role '{r}' has contrast {contrast(colours[r], t):.2f} < {need} on {v['text_on']} (not adjusted)")
            continue
        fixed_hex, changed, ok = fix_contrast(colours[r], t, need)
        if changed:
            warnings.append(f"contrast: '{r}' {colours[r]} -> {fixed_hex} (OKLCH lightness, "
                            f"{'now ' + format(contrast(fixed_hex, t), '.2f') + ':1' if ok else 'could NOT reach ' + str(need)})")
            colours[r] = fixed_hex

    # fonts
    fonts = {}
    over = override.get("fonts") or {}
    for slot, v in pb["font_slots"].items():
        fam = over.get(slot, v["family"])
        files = font_entry(fam, fonts_json, warnings)
        if not files and fam != v["family"]:
            warnings.append(f"override font '{fam}' for slot '{slot}' unavailable; using '{v['family']}'")
            fam = v["family"]
            files = font_entry(fam, fonts_json, warnings)
        fonts[slot] = {"family": fam, "files": files, "use": v.get("use", "")}
        for k in ("weight", "tracking"):  # optional slot defaults (fx.card grow: "fit-text" reads them)
            if isinstance(v.get(k), (int, float)) and not isinstance(v.get(k), bool):
                fonts[slot][k] = v[k]
    for slot in over:
        if slot not in pb["font_slots"]:
            warnings.append(f"override font slot '{slot}' does not exist in the playbook; ignored")
    emoji = font_entry("Noto Color Emoji", fonts_json, warnings)
    fonts["emoji"] = {"family": "Noto Color Emoji", "files": emoji, "use": "emoji fallback"}
    # every other bundled family the resolved style names (a caption profile's family, a type spec "Archivo Black 900",
    # a playbook-allowed alternative): loaded too, so a scene that uses it never falls back to a system font
    slot_fams = {v["family"] for v in fonts.values()}
    fonts_extra = {fam: font_entry(fam, fonts_json, warnings) for fam in referenced_families(pb, fonts_json)
                   if fam not in slot_fams}

    tone = {"energy": "hype", "meme_sfx": False, "roast": False}
    tone.update(pb.get("tone") or {})
    tone.update(override.get("tone") or {})
    out = {"version": 2, "playbook": playbook_id, "creator": copy.deepcopy(pb.get("creator", {})), "colours": colours,
           "text_on": text_on, "fonts": fonts, "fonts_extra": {k: v for k, v in fonts_extra.items() if v},
           "type": copy.deepcopy(pb.get("type", {})), "layout": copy.deepcopy(pb.get("layout", {})),
           "motion": copy.deepcopy(pb.get("motion", {})), "camera_presets": copy.deepcopy(pb.get("camera_presets", {})),
           "stage_morphs": copy.deepcopy(pb.get("stage_morphs", {})), "tone": tone, "warnings": warnings}
    for k in PASSTHROUGH:
        if k in pb:
            out[k] = copy.deepcopy(pb[k])
    if v3:
        from .profilecheck import violations
        for k in V3_PASSTHROUGH:
            if k in pb:
                out[k] = copy.deepcopy(pb[k])
        res = pb["_resolved"]
        out.update({"format": res["format"], "theme": res["theme_record"], "format_layouts": res["layouts"]})
        pv = violations(pb)
        out["profile_check"] = pv
        warnings.extend(f"V-PROFILE {v['id']}: {v['msg']}" for v in pv)
    return out


SOURCE_FILE = "tokens.source.json"  # work/: what work/tokens.json was built from (playbook id, explicit args, hashes)


def _resolve_project(pr, args) -> tuple[str, dict, bool]:
    """(playbook id, resolved tokens, override used) for a project, exactly as `veos tokens` builds work/tokens.json."""
    pid = project_playbook(pr, getattr(args, "playbook", None))
    op = pr.root / "plan" / "tokens.override.json"
    override = read_json(op) if op.exists() else None
    tp = pr.root / "plan" / "timeline.json"
    meta = {}
    if tp.exists():
        try:
            meta = (read_json(tp) or {}).get("meta") or {}
        except ValueError:
            meta = {}
    fmt = getattr(args, "format", None) or (override or {}).get("format") or meta.get("format")
    theme = getattr(args, "theme", None) or (override or {}).get("theme") or meta.get("theme")
    return pid, resolve(pid, override, fmt=fmt, theme=theme), bool(override)


def _source_files(pr, pid: str) -> list[Path]:
    """The files work/tokens.json is built from: the linked playbook's (or style copy's) tokens.json and playbook.md,
    and plan/tokens.override.json."""
    from . import paths
    d = paths.find_playbook_dir(pid)
    if d is None and (paths.styles_dir() / pid / "tokens.json").is_file():
        d = paths.styles_dir() / pid
    files = [d / "tokens.json", d / "playbook.md"] if d is not None else []
    files.append(pr.root / "plan" / "tokens.override.json")
    return [f for f in files if f.is_file()]


def _digests(pr, pid: str) -> dict[str, str]:
    import hashlib
    return {f.as_posix(): hashlib.sha256(f.read_bytes()).hexdigest() for f in _source_files(pr, pid)}


def refresh(pr) -> str | None:
    """Rebuild work/tokens.json when it is stale and return the warning line to print (None when it is fresh or missing,
    or when the playbook cannot be resolved: the caller's own checks report that). Stale = a source file (the linked
    playbook's or style copy's tokens.json / playbook.md, plan/tokens.override.json) hashes differently from when
    `veos tokens` built it (work/tokens.source.json), or the project now links another playbook; without that record
    (built by an older engine) = a source file is newer than work/tokens.json. The rebuild reuses the explicit
    arguments of the last `veos tokens`. A hand-written work/tokens.json whose sources did not change is left alone.
    `bundle`, `storyboard` and `render` call it so a reel never renders with stale style settings."""
    from argparse import Namespace
    tk = pr.work / "tokens.json"
    if not tk.exists():
        return None
    sp = pr.work / SOURCE_FILE
    try:
        rec = read_json(sp) if sp.exists() else None
    except ValueError:
        rec = None
    rec = rec if isinstance(rec, dict) else None
    given = (rec or {}).get("args") or {}
    args = Namespace(**{k: given.get(k) for k in ("playbook", "format", "theme")})
    try:
        pid = project_playbook(pr, args.playbook)
        now = _digests(pr, pid)
    except (VeosError, OSError, ValueError):
        return None
    if not now:
        return None
    rel = lambda f: pr.rel(f) if pr.root in Path(f).parents else Path(f).as_posix()  # noqa: E731
    if rec is not None:
        if rec.get("playbook") != pid:
            why = f"it was built from playbook '{rec.get('playbook')}', the project now uses '{pid}'"
        else:
            old = rec.get("sources") or {}
            changed = [f for f in sorted(set(now) | set(old)) if now.get(f) != old.get(f)]
            if not changed:
                return None
            why = ", ".join(rel(f) for f in changed) + " changed since it was built"
    else:
        newer = [f for f in now if Path(f).stat().st_mtime > tk.stat().st_mtime]
        if not newer:
            return None
        why = ", ".join(rel(f) for f in newer) + " is newer than it"
    try:
        main(args, pr)
    except VeosError as e:
        return f"work/tokens.json is stale ({why}) but `veos tokens` failed: {e.message}"
    return f"work/tokens.json was stale ({why}); re-ran `veos tokens`"


def main(args, project):
    pr = need_project(project)
    pid, out, has_override = _resolve_project(pr, args)
    dest = pr.path("work", "tokens.json")
    write_json(dest, out)
    explicit = {k: getattr(args, k, None) for k in ("playbook", "format", "theme") if getattr(args, k, None)}
    write_json(pr.work / SOURCE_FILE, {"version": 1, "playbook": pid, "args": explicit, "sources": _digests(pr, pid)})
    return {"playbook": pid, "out": pr.rel(dest), "roles": len(out["colours"]),
            "fonts": {k: len(v["files"]) for k, v in out["fonts"].items()}, "override": has_override,
            **({"schema": out["schema"], "format": out.get("format"), "theme": (out.get("theme") or {}).get("id")}
               if out.get("schema") else {}),
            "warnings": out["warnings"]}
