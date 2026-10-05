"""`veos tokens`: resolve playbooks/<id>/tokens.json (+ optional <project>/plan/tokens.override.json) into work/tokens.json.

One source: the creator's playbook tokens (colours by role, font slots, type, layout, motion, camera presets, stage
morphs, budgets, tone). Hard rules are re-checked after the merge: fixed-meaning roles can't be recoloured, brandable
colours get an OKLCH lightness auto-fix when contrast against their `text_on` fails, override patches that touch safe
zones / fixed meanings / loudness are rejected.
"""
from __future__ import annotations

import copy
import math
import os
import re
from pathlib import Path

from .core import VeosError, need_project, r3, read_json, write_json

REPO = Path(__file__).resolve().parents[3]
DEFAULT_PLAYBOOK = "naman"
PROTECTED_PREFIXES = ("roles.bad", "roles.good", "roles.comedy", "fixed_meaning", "layout.safe", "layout.ig_ui",
                      "layout.size")
PROTECTED_WORDS = ("loudness", "lufs", "truepeak", "true_peak")
PASSTHROUGH = ("budgets", "gradients", "max_bright_per_frame", "fixed_meaning", "tones", "tone_treatment", "sound")


def add_args(p, cmd):
    p.add_argument("--playbook", help="playbook id (default: project.json `playbook`, else naman)")


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
        out.append({"src": p.as_uri(), "weight": w, "style": "italic" if italic else "normal"})
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


# ------------------------------------------------------------------ main
def playbooks_dir() -> Path:
    """Folder that holds user playbooks/<id>/tokens.json (see paths.py; env VEOS_PLAYBOOKS overrides)."""
    from . import paths
    return paths.playbooks_dir()


def load_playbook(playbook_id: str) -> dict:
    from . import paths
    d = paths.find_playbook_dir(playbook_id)
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


def resolve(playbook_id: str, override: dict | None = None) -> dict:
    pb = load_playbook(playbook_id)
    warnings: list[str] = []
    override = override or {}
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
        elif not hx:
            warnings.append(f"override colour '{r}' = {v!r} is not a hex colour; ignored")
        else:
            colours[r] = hx
    for path, val in (override.get("patch") or {}).items():
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
    for slot in over:
        if slot not in pb["font_slots"]:
            warnings.append(f"override font slot '{slot}' does not exist in the playbook; ignored")
    emoji = font_entry("Noto Color Emoji", fonts_json, warnings)
    fonts["emoji"] = {"family": "Noto Color Emoji", "files": emoji, "use": "emoji fallback"}

    tone = {"energy": "hype", "meme_sfx": False, "roast": False}
    tone.update(pb.get("tone") or {})
    tone.update(override.get("tone") or {})
    out = {"version": 2, "playbook": playbook_id, "creator": copy.deepcopy(pb.get("creator", {})), "colours": colours,
           "text_on": text_on, "fonts": fonts,
           "type": copy.deepcopy(pb.get("type", {})), "layout": copy.deepcopy(pb.get("layout", {})),
           "motion": copy.deepcopy(pb.get("motion", {})), "camera_presets": copy.deepcopy(pb.get("camera_presets", {})),
           "stage_morphs": copy.deepcopy(pb.get("stage_morphs", {})), "tone": tone, "warnings": warnings}
    for k in PASSTHROUGH:
        if k in pb:
            out[k] = copy.deepcopy(pb[k])
    return out


def main(args, project):
    pr = need_project(project)
    pid = project_playbook(pr, getattr(args, "playbook", None))
    op = pr.root / "plan" / "tokens.override.json"
    override = read_json(op) if op.exists() else None
    out = resolve(pid, override)
    dest = pr.path("work", "tokens.json")
    write_json(dest, out)
    return {"playbook": pid, "out": pr.rel(dest), "roles": len(out["colours"]),
            "fonts": {k: len(v["files"]) for k, v in out["fonts"].items()}, "override": bool(override),
            "warnings": out["warnings"]}
