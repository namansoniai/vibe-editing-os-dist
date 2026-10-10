"""Caption profile engine (E-05): words + caption profile -> the chunk list (`work/captions.json`) that the renderer
(`renderer/captions.js`), V-CADENCE, V-F0, V-CAPTION, V-TYPE and the storyboard read.

Pipeline (`build`):
  1. resolve the caption config (tokens v3 `captions` + `profile.captions`; a v1 playbook gets the `legacy` profile
     that reproduces the old 2-3-word auto-subtitles exactly);
  2. caption words: per-word `caption` fields, `captions.transform` (transliterate / translate from the script text),
     clean, glossary spellings, profanity mask, speaker labels (overlapping back-channels dropped);
  3. profile per word (timeline overrides, then `by_layout` from the stage), then chunking per profile run:
     unit word | group | phrase | line | sentence with word limits, characters per line, lines, no-split classes
     (names, numbers + units), punctuation and pauses (dynamic programming over break costs);
  4. emphasis selection (numbers, glossary terms, names, topic nouns, key verbs; never stop-words; budget per chunk and
     per second; planner overrides), then the variant arrangement (plain, karaoke, two-tier, duet, kinetic stack) into
     lines with per-word font, size, colour and effect;
  5. timing (lead frames, min hold, pause hold, swaps), hide ranges, position anchors and an estimated rect.

The planner never writes caption cards: `timeline.captions.overrides` can only nudge this engine (text fixes, breaks,
emphasis on/off, a profile for a time range, hide, speaker).
"""
from __future__ import annotations

import copy
import json
import math
import re
from pathlib import Path

from . import captext as X

ENGINE = "veos.captions/1"
FPS = 30
W, H = 1080, 1920
REPO = Path(__file__).resolve().parents[3]
LIB_PATH = Path(__file__).resolve().parent / "data" / "caption_profiles.json"
DEV_FALLBACK = "Noto Sans Devanagari"
# Indic scripts -> the bundled Noto Sans family that renders them (assets/fonts/fonts.json); Devanagari goes through
# deva_family (a style may pick Noto Serif Devanagari). Marathi is Devanagari, Punjabi is Gurmukhi.
INDIC_FAMILY = {"devanagari": DEV_FALLBACK, "bengali": "Noto Sans Bengali", "gurmukhi": "Noto Sans Gurmukhi",
                "gujarati": "Noto Sans Gujarati", "tamil": "Noto Sans Tamil", "telugu": "Noto Sans Telugu",
                "kannada": "Noto Sans Kannada", "malayalam": "Noto Sans Malayalam"}
# a few letters per family so the renderer loads the font before it measures (document.fonts.load)
SCRIPT_SAMPLE = {DEV_FALLBACK: "कार", "Noto Sans Bengali": "বাংলা", "Noto Sans Gurmukhi": "ਪੰਜਾਬੀ",
                 "Noto Sans Gujarati": "ગુજરાતી", "Noto Sans Tamil": "தமிழ்", "Noto Sans Telugu": "తెలుగు",
                 "Noto Sans Kannada": "ಕನ್ನಡ", "Noto Sans Malayalam": "മലയാളം"}


def deva_family(prof: dict, cfg=None) -> str:
    """The family Devanagari words use: the profile's `language.devanagari_family`, else the style's
    `captions.devanagari_family` (e.g. Noto Serif Devanagari for a serif style), else Noto Sans Devanagari."""
    return ((prof.get("language") or {}).get("devanagari_family") or getattr(cfg, "deva", None) or DEV_FALLBACK)


def script_family(text: str, prof: dict, cfg=None) -> str | None:
    """The bundled family an Indic-script word is drawn in (Telugu -> Noto Sans Telugu, ...; Devanagari ->
    deva_family); None for Latin and scripts without a bundled font."""
    from .langs import script_of
    sc = script_of(str(text or ""))
    if sc == "devanagari":
        return deva_family(prof, cfg)
    return INDIC_FAMILY.get(sc)


def regional_script_notes(texts: list[str]) -> list[str]:
    """Captions in an Indic script other than Devanagari keep their original words (nothing is dropped or garbled);
    say which scripts appear, the bundled font that draws them (or that none ships, so the browser falls back to a
    system font such as Nirmala UI on Windows), and how to show them romanised instead."""
    from .langs import script_of
    found: dict[str, int] = {}
    for t in texts:
        for part in str(t or "").split():
            sc = script_of(part)
            if sc not in ("latin", "devanagari", "other"):
                found[sc] = found.get(sc, 0) + 1
    out = []
    for sc, n in sorted(found.items()):
        fam = INDIC_FAMILY.get(sc)
        how = f"in {fam}" if fam else f"in a system font (no {sc.title()} font ships in assets/fonts)"
        out.append(f"captions: {n} word(s) in {sc.title()} script, shown as spoken {how}. For romanised captions "
                   f"write a map and run `veos captions apply`.")
    return out

UNIT_DEFAULTS = {
    "word": {"words": [1, 1], "max_chars_line": 18, "lines": 1, "pause_split_s": 0.25, "min_hold_s_per_word": 0.3},
    "group": {"words": [2, 3], "max_chars_line": 24, "lines": 1, "pause_split_s": 0.3},
    "phrase": {"words": [2, 6], "max_chars_line": 28, "lines": 2, "pause_split_s": 0.35},
    "line": {"words": [3, 8], "max_chars_line": 32, "lines": 1, "pause_split_s": 0.45},
    "sentence": {"words": [4, 12], "max_chars_line": 32, "lines": 2, "pause_split_s": 0.6},
}
DEFAULT_PROFILE = {
    "unit": "group", "no_split": ["names", "numbers", "units"], "punct_break": True, "hard_pause_s": 0.9,
    "lead_frames": 2, "min_hold_s_per_word": 0.25, "tail_s": 0.12, "max_hold_s": None,
    "swap": {"type": "hard", "frames": 0, "out_frames": 0, "blur_px": 10, "rise_px": 24},
    "reveal": "chunk", "cps": None, "pause_hold_s": 0, "punct": "keep",
    "skin": {"slot": "body", "weight": 700, "size": 56, "text_class": "TC-subtitle", "case": "sentence", "tracking": 0,
             "line_height": 1.15, "colour": "paper", "stroke": 0, "stroke_colour": "ink",
             "shadow": "0 2 8 rgba(0,0,0,.55)", "style": "normal",
             "container": {"type": "none", "fill": "ink", "opacity": 0.85, "radius": 14, "padding": [14, 24], "shadow": None}},
    "position": {"anchor": "fixed_y", "cy": 1300, "offset": 40, "align": "center", "max_w": 952, "colour_by_bg": None,
                 "by_layout": {}, "hide_on_morph": True},
    "emphasis": {"mechanism": "none", "slot": None, "style": None, "weight": None, "colour": None, "ratio": 1.0,
                 "select": ["number", "glossary", "name", "topic_noun"], "max_per_chunk": 1, "max_per_s": 0.5,
                 "never": ["stopwords"], "span": "word", "glow_px": 14, "min_score": 1.2},
    "karaoke": None, "tiers": None, "duet": None, "stack": None,
    "hide": [],
    "language": {"script": "Latn", "transliteration": "keep_english_terms", "normalise_spelling": False,
                 "profanity_mask": False, "glossary": []},
}
TEXT_CLASS = "TC-subtitle"

# swap / reveal vocabulary (captions.js swapState). flicker, wipe and smear are the Package C swaps: an opacity strobe,
# a feathered mask wipe (in and out) and a directional-blur + x-stretch smear.
SWAP_TYPES = ("hard", "fade", "blur", "rise", "pop", "flicker", "wipe", "smear")
SWAP_DEFAULT_FRAMES = {"wipe": 6, "smear": 3}           # flicker defaults to its pattern's length
FLICKER_PATTERN = [1, 0, 0, 1, 0, 1]                   # per-frame opacity: 3 flashes in 6 f
FLASH_MAX_PER_S = 3   # kept for old callers; flicker captions are free (no flash limit, Naman 8 Oct 2026)
WIPE_DIRS = ("right", "left", "down", "up")
REVEALS = ("chunk", "word", "char")
CPS_RANGE = (1.0, 120.0)                               # reveal: char, characters per second
LINE_FIT = ("block", "max_w")
CONNECTOR_WHEN = ("plain_lines", "plain_only")


def flash_rises(pattern) -> list[int]:
    """Frame offsets where a flicker pattern turns on (opacity crosses 0.5 upward; the chunk starts from hidden)."""
    out, prev = [], 0.0
    for k, v in enumerate(pattern or []):
        v = float(v)
        if prev < 0.5 <= v:
            out.append(k)
        prev = v
    return out


def _num(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def profile_problems(p: dict) -> list[str]:
    """Bad values of the swap / reveal / line-fit / tier fields of one (completed) profile, as readable messages.
    `complete_profile` warns and falls back; V-CAPTION fails on the same list."""
    out = []
    sw = p.get("swap") or {}
    t = sw.get("type") or "hard"
    if t not in SWAP_TYPES:
        out.append(f"swap.type {t!r} is not one of {', '.join(SWAP_TYPES)}")
    for k, hi in (("frames", 30), ("out_frames", 30)):
        v = sw.get(k)
        if v is not None and (not _num(v) or not 0 <= v <= hi):
            out.append(f"swap.{k} {v!r} must be 0-{hi} frames")
    if t == "flicker":
        pat = sw.get("pattern", FLICKER_PATTERN)
        if not isinstance(pat, list) or not pat or len(pat) > 30 or not all(_num(x) and 0 <= x <= 1 for x in pat):
            out.append("swap.pattern must be a list of 1-30 opacities in 0..1 (one per frame)")
    for k in ("dir", "out_dir"):
        if sw.get(k) is not None and sw[k] not in WIPE_DIRS:
            out.append(f"swap.{k} {sw[k]!r} is not one of {', '.join(WIPE_DIRS)}")
    for k, lo, hi in (("feather_px", 0, 400), ("smear_px", 0, 120), ("stretch", 1, 4), ("travel_px", -400, 400),
                      ("angle", -360, 360)):
        if sw.get(k) is not None and (not _num(sw[k]) or not lo <= sw[k] <= hi):
            out.append(f"swap.{k} {sw[k]!r} must be a number in {lo}..{hi}")
    rv = p.get("reveal") or "chunk"
    if rv not in REVEALS:
        out.append(f"reveal {rv!r} is not one of {', '.join(REVEALS)}")
    cps = p.get("cps")
    if cps is not None and (not _num(cps) or not CPS_RANGE[0] <= cps <= CPS_RANGE[1]):
        out.append(f"cps {cps!r} must be {CPS_RANGE[0]:g}-{CPS_RANGE[1]:g} characters per second")
    lf = (p.get("skin") or {}).get("line_fit")
    if lf is not None:
        lf_to = lf.get("to", "block") if isinstance(lf, dict) else lf
        if lf_to not in LINE_FIT:
            out.append(f"skin.line_fit {lf!r} is not one of {', '.join(LINE_FIT)} (or {{to, max_scale}})")
        ms = lf.get("max_scale") if isinstance(lf, dict) else None
        if ms is not None and (not _num(ms) or not 1 <= ms <= 3):
            out.append(f"skin.line_fit.max_scale {ms!r} must be 1-3")
    cw = (p.get("tiers") or {}).get("connector_container_when")
    if cw is not None and cw not in CONNECTOR_WHEN:
        out.append(f"tiers.connector_container_when {cw!r} is not one of {', '.join(CONNECTOR_WHEN)}")
    hom = (p.get("position") or {}).get("hide_on_morph")
    if hom is not None and not isinstance(hom, bool):
        out.append(f"position.hide_on_morph {hom!r} must be true or false")
    return out


def _normalise_swaps(p: dict, warnings: list, pid: str) -> None:
    """Warn about bad swap / reveal values and fall back to safe ones (hard swap, chunk reveal, no line fit)."""
    probs = profile_problems(p)
    for msg in probs:
        warnings.append(f"captions profile {pid}: {msg}; ignored")
    if probs:
        p["problems"] = probs  # exported with the profile: V-CAPTION fails on them
    sw = p.setdefault("swap", {})
    t = sw.get("type") or "hard"
    if t not in SWAP_TYPES:
        sw["type"] = "hard"
    if t == "flicker":
        pat = sw.get("pattern", FLICKER_PATTERN)
        ok = isinstance(pat, list) and pat and len(pat) <= 30 and all(_num(x) and 0 <= x <= 1 for x in pat)
        sw["pattern"] = list(pat) if ok else list(FLICKER_PATTERN)
        if not sw.get("frames"):
            sw["frames"] = len(sw["pattern"])
    elif t in SWAP_DEFAULT_FRAMES and not sw.get("frames"):
        sw["frames"] = SWAP_DEFAULT_FRAMES[t]
    for k in ("dir", "out_dir"):
        if sw.get(k) is not None and sw[k] not in WIPE_DIRS:
            sw.pop(k)
    if (p.get("reveal") or "chunk") not in REVEALS:
        p["reveal"] = "chunk"
    cps = p.get("cps")
    if cps is not None and (not _num(cps) or not CPS_RANGE[0] <= cps <= CPS_RANGE[1]):
        p["cps"] = None
    sk = p.get("skin") or {}
    lf = sk.get("line_fit")
    if lf is not None and (lf.get("to", "block") if isinstance(lf, dict) else lf) not in LINE_FIT:
        sk.pop("line_fit")
    tiers = p.get("tiers") or {}
    if tiers.get("connector_container_when") not in (None,) + CONNECTOR_WHEN:
        tiers.pop("connector_container_when")


# ================================================================================================ helpers
def f_of(t: float) -> int:
    """Seconds -> frame, rounding half up like the renderer's Math.round."""
    return int(math.floor(float(t) * FPS + 0.5))


def deep_merge(base: dict, over: dict) -> dict:
    for k, v in (over or {}).items():
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            deep_merge(base[k], v)
        else:
            base[k] = copy.deepcopy(v)
    return base


def get(d, path, default=None):
    cur = d
    for k in path.split("."):
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return default
    return cur


def load_library() -> dict:
    try:
        return json.loads(LIB_PATH.read_text(encoding="utf-8-sig")).get("profiles", {})
    except (OSError, ValueError):
        return {}


def hex_of(colour, colours: dict, default="#FFFFFF"):
    """Role name or hex (or rgba()) -> CSS colour."""
    if colour in (None, ""):
        return default
    c = str(colour)
    if c.startswith(("#", "rgb", "hsl")):
        return c
    return colours.get(c, default)


def luma_hex(c: str) -> float:
    c = (c or "").lstrip("#")
    if len(c) == 3:
        c = "".join(x * 2 for x in c)
    try:
        r, g, b = (int(c[k:k + 2], 16) / 255 for k in (0, 2, 4))
    except ValueError:
        return 0.0
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


# ================================================================================================ config
class Config:
    """The caption setup one reel sees."""

    def __init__(self):
        self.mode = "full"
        self.role = "support"
        self.legacy = False
        self.default = "CS-1"
        self.profiles: dict[str, dict] = {}
        self.by_layout: dict[str, str] = {}
        self.speakers: dict[str, dict] = {}
        self.cast: dict[str, str] = {}
        self.transform = "verbatim"
        self.colours: dict[str, str] = {}
        self.fonts: dict[str, dict] = {}
        self.deva: str | None = None
        self.layouts: dict = {}
        self.layout: dict = {}
        self.worlds: dict = {}
        self.safe = {"x": [64, 1016], "y": [110, 1500]}
        self.motion: dict = {}
        self.subtitle: dict = {}
        self.warnings: list[str] = []
        self.latin = False                  # captions are written in Latin script (English / Hinglish)


LATIN_LANGS = ("en", "eng", "english", "hinglish", "hi-latn", "en-in")


def latin_captions(lang: dict) -> bool:
    """profile.language.captions says the captions are Latin script: `script: Latn`, or an English / Hinglish `lang`
    with no other script named."""
    script = str(lang.get("script") or "").lower()
    if script:
        return script in ("latn", "latin", "roman")
    return str(lang.get("lang") or lang.get("language") or "").lower() in LATIN_LANGS


def legacy_profile(tokens: dict) -> dict:
    """The v1 mapping profile: today's auto-subtitles (core.js buildCards + subtitleHTML), reproduced exactly."""
    sub = (tokens.get("type") or {}).get("subtitle") or {}
    size = sub.get("size")
    size0 = ((size[0] + size[1]) / 2 if isinstance(size, list) else size) or 58
    wpc = sub.get("words_per_card") or [2, 3]
    return {"legacy": True, "unit": "group", "words": [wpc[0] if len(wpc) > 1 else 1, (wpc[1] if len(wpc) > 1 else wpc[0]) or 3],
            "max_chars_line": 999, "lines": 1, "lead_frames": (tokens.get("motion") or {}).get("lead_frames") or 2,
            "swap": {"type": "hard", "frames": 0}, "reveal": "chunk",
            "skin": {"slot": sub.get("slot") or "body", "weight": sub.get("weight") or 800, "size": size0,
                     "text_class": TEXT_CLASS, "case": "lower", "tracking": 0},
            "position": {"anchor": "fixed_y", "cy": (((tokens.get("layout") or {}).get("caption_cy") or {}).get("full") or 1300)},
            "emphasis": {"mechanism": "none"}, "hide": ["under_z8", "morph"]}


def complete_profile(p: dict, lib: dict, warnings: list, pid: str = "") -> dict:
    """Defaults + library base (`extends: "lib:<id>"`) + unit defaults under the given profile."""
    p = copy.deepcopy(p or {})
    base = copy.deepcopy(DEFAULT_PROFILE)
    ext = p.pop("extends", None)
    if ext:
        lid = str(ext).split(":", 1)[-1]
        if lid in lib:
            deep_merge(base, copy.deepcopy(lib[lid]))
        else:
            warnings.append(f"captions profile {pid}: extends {ext!r} is not in the caption library; ignored")
    unit = p.get("unit") or base.get("unit") or "group"
    if unit not in UNIT_DEFAULTS:
        warnings.append(f"captions profile {pid}: unit {unit!r} unknown; using group")
        unit = "group"
    for k, v in UNIT_DEFAULTS[unit].items():
        if k not in p and (k not in base or ext is None):
            base[k] = copy.deepcopy(v)
    # schema shorthands: case/tracking may sit at the top level
    for k in ("case", "tracking", "colour", "weight", "size", "slot"):
        if k in p and not isinstance(p[k], dict):
            p.setdefault("skin", {})[k] = p.pop(k)
    if isinstance(p.get("swap"), str):
        t, _, fr = p["swap"].partition(":")
        p["swap"] = {"type": t, "frames": int(fr or 0)}
    deep_merge(base, p)
    base["unit"] = unit
    sel = base["emphasis"].get("select")
    if isinstance(sel, str):
        base["emphasis"]["select"] = [x.strip() for x in re.split(r"[|,]", sel) if x.strip()]
    if not isinstance(base.get("words"), list) or len(base["words"]) != 2:
        w = base.get("words")
        base["words"] = [int(w), int(w)] if isinstance(w, (int, float)) else list(UNIT_DEFAULTS[unit]["words"])
    if base.get("pause_hold_s") and base["pause_hold_s"] > 2:
        warnings.append(f"captions profile {pid}: pause_hold_s {base['pause_hold_s']} > 2 s; clamped to 2")
        base["pause_hold_s"] = 2.0
    if base.get("lead_frames", 0) > 4:
        warnings.append(f"captions profile {pid}: lead_frames {base['lead_frames']} > 4 (150 ms); clamped to 4")
        base["lead_frames"] = 4
    _normalise_swaps(base, warnings, pid)
    return base


def apply_profanity(cfg: Config, caps: dict) -> None:
    """`captions.profanity: {mask: true|false, style: inner|vowel|full}`, the style-wide switch (every template ships it
    on, style inner). mask false turns masking off in every profile; mask true sets it on every profile that doesn't
    choose its own `language.profanity_mask`."""
    pf = caps.get("profanity")
    if isinstance(pf, bool):
        pf = {"mask": pf}
    if not isinstance(pf, dict) or "mask" not in pf:
        return
    style = pf.get("style") or "inner"
    if style not in ("inner", "vowel", "full"):
        cfg.warnings.append(f"captions.profanity.style {style!r} is not inner, vowel or full; using inner")
        style = "inner"
    raw = caps.get("profiles") or {}
    for pid, p in cfg.profiles.items():
        lang = p.setdefault("language", {})
        if not pf["mask"]:
            lang["profanity_mask"] = False
        elif "profanity_mask" not in ((raw.get(pid) or {}).get("language") or {}):
            lang["profanity_mask"] = style


def apply_hide_on_morph(cfg: Config, caps: dict, tcaps: dict) -> None:
    """`captions.hide_on_morph: false` (style-wide, a per-template flag) keeps every profile's captions on screen through
    stage morphs unless the profile sets its own `position.hide_on_morph`; the timeline's `captions.hide_on_morph`
    (one reel) wins over both."""
    tv, sv = tcaps.get("hide_on_morph"), caps.get("hide_on_morph")
    for where, v in (("timeline captions", tv), ("captions", sv)):
        if v is not None and not isinstance(v, bool):
            cfg.warnings.append(f"{where}.hide_on_morph {v!r} must be true or false; ignored")
    tv = tv if isinstance(tv, bool) else None
    sv = sv if isinstance(sv, bool) else None
    raw = caps.get("profiles") or {}
    for pid, p in cfg.profiles.items():
        own = "hide_on_morph" in (((raw.get(pid) or {}).get("position")) or {})
        if tv is not None:
            p.setdefault("position", {})["hide_on_morph"] = tv
        elif sv is not None and not own:
            p.setdefault("position", {})["hide_on_morph"] = sv


def resolve_config(tokens: dict, tl: dict | None = None) -> Config:
    tl = tl or {}
    cfg = Config()
    lib = load_library()
    cfg.colours = dict(tokens.get("colours") or {})
    cfg.fonts = dict(tokens.get("fonts") or {})
    cfg.layout = tokens.get("layout") or {}
    cfg.layouts = tokens.get("layouts") or {}
    cfg.worlds = tokens.get("worlds") or {}
    cfg.motion = tokens.get("motion") or {}
    cfg.subtitle = (tokens.get("type") or {}).get("subtitle") or {}
    if isinstance(cfg.layout.get("safe"), dict):
        cfg.safe = cfg.layout["safe"]
    caps = tokens.get("captions")
    pc = get(tokens, "profile.captions") or {}
    cfg.mode = pc.get("mode", "full")
    cfg.role = pc.get("role", "support")
    lang = get(tokens, "profile.language.captions") or {}
    cfg.transform = lang.get("transform") or "verbatim"
    cfg.latin = latin_captions(lang)
    tcaps = tl.get("captions") or {}
    if tcaps.get("subtitles") in ("off", False):
        cfg.mode = "off"
    if not isinstance(caps, dict) or not caps.get("profiles"):
        cfg.legacy = True
        cfg.profiles = {"CS-1": legacy_profile(tokens)}
        cfg.default = "CS-1"
        if isinstance(caps, dict):  # a v3 style on the legacy mapping (template 0) still takes the profanity switch
            apply_profanity(cfg, caps)
        # ... and the keep-captions-through-morphs flag (style-wide, or this reel's timeline)
        apply_hide_on_morph(cfg, caps if isinstance(caps, dict) else {}, tcaps)
        return cfg
    for pid, p in caps["profiles"].items():
        cfg.profiles[pid] = complete_profile(p, lib, cfg.warnings, pid)
    cfg.default = caps.get("default") or next(iter(cfg.profiles))
    if tcaps.get("profile"):
        if tcaps["profile"] in cfg.profiles:
            cfg.default = tcaps["profile"]
        else:
            cfg.warnings.append(f"timeline captions.profile {tcaps['profile']!r} is not a profile of this style; "
                                f"using {cfg.default}")
    if tcaps.get("transform"):
        cfg.transform = tcaps["transform"]
    if cfg.default not in cfg.profiles:
        cfg.warnings.append(f"captions.default {cfg.default!r} is not a profile; using the first one")
        cfg.default = next(iter(cfg.profiles))
    apply_profanity(cfg, caps)
    apply_hide_on_morph(cfg, caps, tcaps)
    cfg.deva = caps.get("devanagari_family") or None
    cfg.by_layout = {k: v for k, v in (caps.get("by_layout") or {}).items() if v in cfg.profiles}
    for k, v in (caps.get("by_layout") or {}).items():
        if v not in cfg.profiles:
            cfg.warnings.append(f"captions.by_layout.{k} -> {v!r} is not a profile; ignored")
    cfg.speakers = dict(caps.get("speakers") or {})
    for c in get(tokens, "dialogue.cast") or []:
        if isinstance(c, dict) and c.get("id"):
            cfg.cast[str(c["id"])] = str(c.get("caption") or c.get("role") or c["id"])
    return cfg


# ================================================================================================ fonts / measuring
class Measurer:
    """Advance widths from the bundled font files (fontTools; variable fonts via HVAR at the requested weight).
    Kerning is ignored (a few px). Without fontTools, an average-width estimate is used."""

    def __init__(self, fonts: dict):
        self.fonts = fonts
        self.cache: dict = {}
        self.adv: dict = {}
        try:
            import fontTools  # noqa: F401
            self.ok = True
        except ImportError:
            self.ok = False

    def _face(self, family: str, italic: bool):
        key = (family, italic)
        if key in self.cache:
            return self.cache[key]
        face = None
        files = []
        for slot in self.fonts.values():
            if slot.get("family") == family:
                files = slot.get("files") or []
                break
        if not files:
            meta = _fonts_json().get(family) or {}
            files = [{"src": (REPO / "assets" / "fonts" / f).as_uri(), "style": "italic" if "italic" in f.lower() else "normal"}
                     for f in meta.get("files", [])]
        pick = [f for f in files if (f.get("style") == "italic") == italic] or files
        if pick and self.ok:
            from urllib.parse import unquote, urlparse
            from fontTools.ttLib import TTFont
            try:
                u = urlparse(pick[0]["src"])
                path = unquote(u.path.lstrip("/")) if re.match(r"^/[A-Za-z]:", u.path) else unquote(u.path)
                faces = []
                for f in pick:
                    uu = urlparse(f["src"])
                    pp = unquote(uu.path.lstrip("/")) if re.match(r"^/[A-Za-z]:", uu.path) else unquote(uu.path)
                    faces.append((f.get("weight", "400"), TTFont(pp, lazy=True)))
                face = faces
                del path
            except Exception:  # noqa: BLE001 - unreadable font: estimate
                face = None
        self.cache[key] = face
        return face

    def _advances(self, family, weight, italic):
        key = (family, int(weight), italic)
        if key in self.adv:
            return self.adv[key]
        faces = self._face(family, italic)
        res = None
        if faces:
            # static families: the file whose weight is closest; variable: HVAR deltas at the weight
            def wnum(s):
                m = re.findall(r"\d{3}", str(s))
                return [int(x) for x in m] or [400]
            best = min(faces, key=lambda fw: min(abs(x - int(weight)) for x in wnum(fw[0])))
            ft = best[1]
            try:
                cmap = ft.getBestCmap()
                hm = ft["hmtx"]
                upm = ft["head"].unitsPerEm
                delta = None
                if "fvar" in ft and "HVAR" in ft:
                    from fontTools.varLib.models import normalizeLocation, piecewiseLinearMap
                    from fontTools.varLib.varStore import VarStoreInstancer
                    axes = {a.axisTag: (a.minValue, a.defaultValue, a.maxValue) for a in ft["fvar"].axes}
                    loc = {"wght": max(axes["wght"][0], min(axes["wght"][2], int(weight)))} if "wght" in axes else {}
                    nl = normalizeLocation(loc, axes)
                    if "avar" in ft:
                        for tag, m in ft["avar"].segments.items():
                            if tag in nl:
                                nl[tag] = piecewiseLinearMap(nl[tag], m)
                    hv = ft["HVAR"].table
                    inst = VarStoreInstancer(hv.VarStore, ft["fvar"].axes, nl)
                    amap = hv.AdvWidthMap.mapping if hv.AdvWidthMap else None
                    delta = (inst, amap)
                res = (cmap, hm, upm, delta, ft)
            except Exception:  # noqa: BLE001
                res = None
        self.adv[key] = res
        return res

    def width(self, text: str, family: str, weight=400, size=56.0, italic=False, tracking_em=0.0) -> float:
        if not text:
            return 0.0
        a = self._advances(family, weight, italic) if self.ok else None
        if a is None:
            return len(text) * size * (0.5 + (int(weight) - 400) / 4000) + len(text) * tracking_em * size
        cmap, hm, upm, delta, ft = a
        tot = 0.0
        for ch in text:
            g = cmap.get(ord(ch))
            if g is None:
                tot += 0.55 * upm
                continue
            adv = hm[g][0]
            if delta is not None:
                inst, amap = delta
                try:
                    vi = amap[g] if amap is not None else ft.getGlyphID(g)
                    adv += inst[vi]
                except (KeyError, IndexError, AttributeError):
                    pass
            tot += adv
        return tot / upm * size + len(text) * tracking_em * size


_FJ = None


def _fonts_json() -> dict:
    global _FJ
    if _FJ is None:
        try:
            _FJ = json.loads((REPO / "assets" / "fonts" / "fonts.json").read_text(encoding="utf-8-sig"))
        except (OSError, ValueError):
            _FJ = {}
    return _FJ


def family_of(cfg: Config, slot: str | None) -> str:
    if not slot:
        slot = "body"
    f = cfg.fonts.get(slot)
    if f and f.get("family"):
        return f["family"]
    return slot  # an unknown slot is used as a family name (warned in build)


def font_files(family: str) -> list[dict]:
    meta = _fonts_json().get(family) or {}
    out = []
    for f in meta.get("files", []):
        p = REPO / "assets" / "fonts" / f
        if p.exists():
            w = (meta.get("file_weights") or {}).get(f)
            if w is None:
                m = re.search(r"(\d{3})\s*-\s*(\d{3})", meta.get("weights", ""))
                w = f"{m.group(1)} {m.group(2)}" if m else (re.search(r"\d{3}", meta.get("weights", "")) or [None])[0] or "400"
            out.append({"src": p.as_uri(), "weight": w, "style": "italic" if "italic" in f.lower() else "normal"})
    return out


# ================================================================================================ words
class Word:
    __slots__ = ("i", "text", "raw", "s", "e", "spk", "dev", "num", "unit", "cur", "name", "gloss", "send", "soft",
                 "gap", "syn", "emph", "force", "score", "tier", "prof", "brk", "glue", "hidden", "case_start", "masked")

    def __init__(self, i, text, s, e, raw=None):
        self.i, self.text, self.s, self.e = i, text, float(s), float(e)
        self.raw = raw if raw is not None else text
        self.spk = None
        self.dev = X.is_devanagari(text)
        self.num = self.unit = self.cur = self.name = False
        self.gloss = None
        self.send = self.soft = False
        self.gap = 9.0
        self.syn = False
        self.emph = False
        self.force = None   # planner override: True / False
        self.score = 0.0
        self.tier = 0
        self.prof = None
        self.brk = None     # "before" / "after" (planner)
        self.glue = False   # no break after this word (no-split class)
        self.hidden = False
        self.case_start = False
        self.masked = False


def speaker_key(w: dict, cfg: Config):
    for k in ("role", "speaker_name", "speaker"):
        v = w.get(k)
        if v is not None and v != "":
            v = str(v)
            if v in cfg.cast:
                return cfg.cast[v]
            if not cfg.speakers or v in cfg.speakers:
                return v
    sp = w.get("speaker")
    return cfg.cast.get(str(sp), str(sp)) if sp not in (None, "") else None


def caption_words(raw: list[dict], cfg: Config, *, script: list[str] | None = None, glossary=None,
                  warnings: list | None = None) -> list[Word]:
    """Transcript words -> caption words (text per the transform, cleaned, glossary-spelled, masked, speaker-labelled)."""
    warnings = warnings if warnings is not None else []
    tr = cfg.transform or "verbatim"
    ws = [w for w in raw if isinstance(w, dict) and "s" in w and "e" in w]
    out: list[Word] = []
    if tr == "translate":
        if not script:
            warnings.append("captions.transform is translate but no script text was given; captions show the speech")
        else:
            syn = X.align_translate(ws, script)
            for k, sw in enumerate(syn):
                w = Word(None, sw["w"], sw["s"], sw["e"])
                w.syn = True
                srcs = [ws[x] for x in sw.get("src") or []]
                if srcs:
                    w.spk = speaker_key(srcs[0], cfg)
                out.append(w)
            if out:
                return _finish_words(out, cfg, glossary)
    rom = [None] * len(ws)
    # Latin-script captions (English / Hinglish) never show Devanagari: Whisper's Devanagari words are romanised
    # before chunking, from the script text when one is given, else by the Hinglish transliteration (captext).
    latin = bool(getattr(cfg, "latin", False))
    if (tr == "transliterate" or latin) and script:
        need = [k for k, w in enumerate(ws) if "caption" not in w
                and (tr == "transliterate" or X.is_devanagari(str(w.get("w", ""))))]
        if need:
            al = X.align_transliterate([ws[k] for k in need], X.script_tokens(script))
            for k, a in zip(need, al):
                rom[k] = a
    prev_spk = None
    for k, w in enumerate(ws):
        if w.get("overlap") and prev_spk is not None and speaker_key(w, cfg) != prev_spk:
            continue  # a back-channel spoken over the main speaker: only the dominant speaker is captioned
        if "caption" in w:
            txt = w.get("caption")
            if txt in ("", None):
                continue
        elif rom[k]:
            txt = rom[k]
        elif tr in ("transliterate",) and X.is_devanagari(str(w.get("w", ""))):
            txt = X.hinglish(str(w.get("w", "")))
        else:
            txt = str(w.get("w", ""))
        txt = str(txt).strip()
        if latin and X.is_devanagari(txt):
            txt = " ".join(X.hinglish(p) if X.is_devanagari(p) else p for p in txt.split())
        if not txt:
            continue
        if tr == "clean" and X.norm(txt) in ("um", "uh", "umm", "uhh", "hmm", "er", "erm", "ah"):
            continue
        cw = Word(w.get("i", k), txt, w["s"], w["e"], raw=str(w.get("w", "")))
        cw.spk = speaker_key(w, cfg)
        prev_spk = cw.spk if cw.spk is not None else prev_spk
        out.append(cw)
    return _finish_words(out, cfg, glossary)


def _finish_words(out: list[Word], cfg: Config, glossary) -> list[Word]:
    for k, w in enumerate(out):
        nxt = out[k + 1] if k + 1 < len(out) else None
        w.gap = (nxt.s - w.e) if nxt else 9.0
        w.dev = X.is_devanagari(w.text)
        w.num = X.is_number(w.text)
        w.unit = X.is_unit(w.text)
        w.cur = X.is_currency(w.text)
        w.send = X.sentence_end(w.text)
        w.soft = X.soft_break(w.text)
        if glossary:
            g = glossary.canon(w.text)
            if g and " " not in g:
                lead, c, trail = X.split_edges(w.text)
                w.text = lead + g + trail
                w.gloss = g
    for k, w in enumerate(out):  # names: capitalised words not at a sentence start, glossary terms
        prev = out[k - 1] if k else None
        c = X.core(w.text)
        w.name = bool(w.gloss) or (bool(c[:1].isupper()) and prev is not None and not prev.send and not X.is_stop(c)
                                    and not w.dev)
        w.case_start = prev is None or prev.send
    return out


# ================================================================================================ chunking
def _glue(a: Word, b: Word, ns: list) -> bool:
    if a.spk != b.spk:
        return False
    if "numbers" in ns and a.num and b.num:
        return True
    if "units" in ns and ((a.num and b.unit) or (a.cur and b.num)):
        return True
    if "names" in ns and a.name and b.name and not a.send and not a.soft:
        return True
    if "numbers" in ns and a.num and X.norm(b.text) in ("lakh", "crore", "thousand", "million", "billion", "hundred", "k"):
        return True
    return False


def _line_chars(ws: list[Word]) -> int:
    return sum(len(w.text) for w in ws) + max(0, len(ws) - 1)


def chunk_words(ws: list[Word], prof: dict) -> list[list[Word]]:
    """Dynamic-programming chunker for one profile run of words."""
    if not ws:
        return []
    unit = prof["unit"]
    lo, hi = int(prof["words"][0]), int(prof["words"][1])
    lo = max(1, min(lo, hi))
    mcl = int(prof.get("max_chars_line") or 32)
    lines = int(prof.get("lines") or 1)
    cap_chars = mcl * lines
    pause = float(prof.get("pause_split_s") or 0.3)
    hard_pause = float(prof.get("hard_pause_s") or 0.9)
    ns = prof.get("no_split") or []
    for k in range(len(ws) - 1):
        ws[k].glue = _glue(ws[k], ws[k + 1], ns)
    # hard segments
    segs, cur = [], []
    for k, w in enumerate(ws):
        cur.append(w)
        nxt = ws[k + 1] if k + 1 < len(ws) else None
        hard = (nxt is None or w.brk == "after" or nxt.brk == "before" or nxt.spk != w.spk or nxt.prof != w.prof
                or w.gap >= hard_pause or (w.send and (prof.get("punct_break", True) or unit == "sentence")))
        if hard:
            w.glue = False
            segs.append(cur)
            cur = []
    if cur:
        segs.append(cur)
    target = {"word": 1.0, "group": (lo + hi) / 2, "phrase": (lo + hi) / 2 + 0.5, "line": hi * 0.8,
              "sentence": hi * 0.85}[unit]
    out = []
    for seg in segs:
        n = len(seg)
        INF = 1e18
        best = [INF] * (n + 1)
        back = [0] * (n + 1)
        best[0] = 0.0
        for j in range(1, n + 1):
            if j < n and seg[j - 1].glue:
                continue  # may not break after a glued word
            for i in range(max(0, j - max(hi * 2, hi + 4)), j):
                if best[i] >= INF:
                    continue
                k = j - i
                chunk = seg[i:j]
                chars = _line_chars(chunk)
                c = 0.0
                if k > hi:
                    # only allowed when glue forces it (a long name / number group)
                    if any(not seg[x].glue for x in range(i, j - 1)):
                        continue
                    c += 3.0 * (k - hi)
                if chars > cap_chars:
                    if k == 1 or all(seg[x].glue for x in range(i, j - 1)):
                        c += 2.0
                    else:
                        c += 6.0 + (chars - cap_chars) * 0.5
                c += 1.2 * ((k - target) / max(target, 1)) ** 2
                if k < lo and n >= lo:
                    c += 1.5 * (lo - k)
                if unit in ("line", "sentence"):
                    c += 0.8 * (1 - min(chars, cap_chars) / cap_chars) ** 2
                if k == 1 and unit != "word" and n > 1:
                    c += 1.2
                # break quality after word j-1 (inside a segment)
                if j < n:
                    a, b = seg[j - 1], seg[j]
                    if a.soft:
                        c -= 1.0
                    if a.gap >= pause:
                        c -= 0.8 + min(0.6, (a.gap - pause))
                    elif a.gap >= 0.15:
                        c -= 0.3
                    if X.norm(b.text) in X.CONNECTORS_START:
                        c -= 0.45 if unit in ("phrase", "sentence", "line") else 0.25
                    if X.norm(a.text) in X.DANGLING_END and not a.soft:
                        c += 0.9
                    if unit == "sentence":
                        c += 0.6  # sentences break mid-way only when they must
                dur = chunk[-1].e - chunk[0].s
                min_dur = 0.25 if unit == "word" else 0.45
                if dur < min_dur and n > k:
                    c += (min_dur - dur) * 3
                max_dur = {"word": 1.6, "group": 2.6, "phrase": 3.6, "line": 4.0, "sentence": 5.5}[unit]
                if dur > max_dur:
                    c += (dur - max_dur) * 0.8
                if best[i] + c < best[j]:
                    best[j], back[j] = best[i] + c, i
        if best[n] >= INF:  # glue made it impossible: fall back to greedy max chunks
            for x in range(0, n, hi):
                out.append(seg[x:x + hi])
            continue
        cuts, j = [], n
        while j > 0:
            cuts.append((back[j], j))
            j = back[j]
        for i, j in reversed(cuts):
            out.append(seg[i:j])
    return out


def legacy_cards(raw_words: list[dict], cfg: Config, tl: dict) -> list[dict]:
    """core.js buildCards, ported line by line (the v1 mapping profile renders exactly as before)."""
    p = cfg.profiles["CS-1"]
    lead = int(p.get("lead_frames") or 2)
    ws = []
    for w in raw_words:
        if "caption" in w:
            txt = w["caption"]
            if txt == "" or txt is None:
                continue
        else:
            txt = re.sub(r"[.,;:!…]+$", "", str(w.get("w") or "").lower())
        if not txt:
            continue
        pm = (p.get("language") or {}).get("profanity_mask")
        if pm:
            txt = X.mask_word(str(txt), pm if isinstance(pm, str) else "inner")
        ws.append({"txt": str(txt), "s": w["s"], "e": w["e"], "i": w.get("i")})
    per = (cfg.subtitle.get("words_per_card") and cfg.subtitle["words_per_card"][1]) or 3
    cards = []
    i = 0
    while i < len(ws):
        j = i + 1
        while j < len(ws) and j - i < per and ws[j]["s"] - ws[j - 1]["e"] <= 0.25:
            j += 1
        if j - i == per and j < len(ws) and len(ws) - j == 1 and ws[j]["s"] - ws[j - 1]["e"] <= 0.25:
            j -= 1
        cards.append({"f0": max(0, f_of(ws[i]["s"]) - lead), "last": ws[j - 1]["e"],
                      "text": " ".join(x["txt"] for x in ws[i:j]), "s": ws[i]["s"], "ws": ws[i:j]})
        i = j
    for c in range(len(cards)):
        nx = cards[c + 1] if c + 1 < len(cards) else None
        hold = f_of(cards[c]["last"]) + 7
        cards[c]["f1"] = min(nx["f0"], max(hold, cards[c]["f0"] + 4)) if nx else max(hold, cards[c]["f0"] + 4)
        if cards[c]["f1"] <= cards[c]["f0"]:
            cards[c]["f1"] = cards[c]["f0"] + 1
    for o in ((tl.get("captions") or {}).get("overrides") or []):
        if not isinstance(o, dict):
            continue
        if o.get("from") is not None and o.get("to") is not None:
            for c in cards:
                c["text"] = " ".join(o["to"] if w.lower() == str(o["from"]).lower() else w for w in c["text"].split(" "))
        else:
            t = o.get("t") if o.get("t") is not None else o.get("at")
            if t is None or isinstance(t, list) or "text" not in o:
                continue
            f = f_of(t)
            for c in cards:
                if c["f0"] <= f < c["f1"]:
                    c["text"] = o["text"]
    return cards


# ================================================================================================ emphasis
def word_score(w: Word, sel: list, freq: dict) -> float:
    c = X.norm(w.text)
    if not c or (X.is_stop(c) and not w.num):
        return 0.0
    s = 0.0
    if "number" in sel and w.num:
        s = max(s, 3.0)
    if ("glossary" in sel or "brand" in sel) and w.gloss:
        s = max(s, 2.6)
    if "name" in sel and w.name:
        s = max(s, 2.2)
    if "topic_noun" in sel and len(c) >= 4 and c not in X.COMMON_VERBS and not c.endswith(("ly",)) and not w.dev:
        s = max(s, 1.0 + 0.08 * min(len(c), 10) + (0.4 if freq.get(c, 0) >= 2 else 0) + (0.3 if w.soft or w.send else 0))
    if "key_verb" in sel and (c in X.COMMON_VERBS or c.endswith(("ing", "ed"))) and len(c) >= 4:
        s = max(s, 1.3)
    if "content" in sel and len(c) >= 3:
        s = max(s, 1.0)
    return s


PHRASE_MAX = 3  # span "phrase": the seed word + at most 2 adjacent content words (one emphasis event for the budget)


def select_emphasis(chunks: list[list[Word]], profiles: dict, allw: list[Word]):
    """Budgeted emphasis: candidates by score; at most `max_per_chunk` per chunk and one per 1/max_per_s seconds;
    planner overrides force words on (counted) or off. A phrase span (seed + up to 2 adjacent content words) is ONE
    emphasis event: the budget counts runs, never the words inside a phrase (V-CAPTION counts the same way)."""
    freq: dict[str, int] = {}
    for w in allw:
        freq[X.norm(w.text)] = freq.get(X.norm(w.text), 0) + 1
    cand = []
    for ci, ch in enumerate(chunks):
        prof = profiles[ch[0].prof]
        em = prof["emphasis"]
        sel = em.get("select") or []
        never = em.get("never") or []
        for w in ch:
            w.score = word_score(w, sel, freq)
            if "stopwords" in never and X.is_stop(w.text) and not w.num:
                w.score = 0.0
            if any(X.norm(w.text) == X.norm(str(n)) for n in never if n != "stopwords"):
                w.score = 0.0
            if w.force is True:
                w.emph = True
            elif w.force is None and em.get("mechanism", "none") not in ("none", None) and w.score >= float(em.get("min_score", 1.2)):
                cand.append((w.score, -w.s, ci, w))
    cand.sort(key=lambda x: (-x[0], -x[1]))
    taken: list[float] = [w.s for w in allw if w.emph]
    per_chunk: dict[int, int] = {}
    for ci, ch in enumerate(chunks):
        per_chunk[ci] = sum(1 for w in ch if w.emph)
    for score, _, ci, w in cand:
        em = profiles[w.prof]["emphasis"]
        mpc = int(em.get("max_per_chunk") or 1)
        rate = em.get("max_per_s")
        gap = 1.0 / float(rate) if rate else 0.0
        if per_chunk[ci] >= mpc:
            continue
        if gap and any(abs(w.s - t) < gap - 1e-6 for t in taken):
            continue
        w.emph = True
        taken.append(w.s)
        per_chunk[ci] += 1
    # phrase spans (promoted emphasis): extend to adjacent content words in the chunk. The run's first word is when the
    # emphasis lands, so a left extension may not bring it closer than the budget gap to the previous emphasis.
    prev_start: float | None = None
    for ch in chunks:
        em = profiles[ch[0].prof]["emphasis"]
        rate = em.get("max_per_s")
        gap = 1.0 / float(rate) if rate else 0.0
        if em.get("span") != "phrase":
            for k, w in enumerate(ch):
                if w.emph and (k == 0 or not ch[k - 1].emph):
                    prev_start = w.s
            continue
        seeds = [k for k, w in enumerate(ch) if w.emph and w.force is not False]
        for k in seeds:  # a phrase is the seed + adjacent content words, PHRASE_MAX words in all, right side first
            lo = hi = k
            while lo > 0 and ch[lo - 1].emph:
                lo -= 1
            while hi + 1 < len(ch) and ch[hi + 1].emph:
                hi += 1
            for d in (1, -1):
                j = hi + 1 if d == 1 else lo - 1
                while (0 <= j < len(ch) and hi - lo + 1 < PHRASE_MAX and not ch[j].emph and not X.is_stop(ch[j].text)
                       and ch[j].force is not False
                       and (d == 1 or prev_start is None or not gap or ch[j].s - prev_start >= gap - 1e-6)):
                    ch[j].emph = True
                    lo, hi = min(lo, j), max(hi, j)
                    j += d
            prev_start = ch[lo].s


# ================================================================================================ arrangement
def _word_style(w: Word, prof: dict, cfg: Config, colour_hex: str, speaker: dict | None) -> dict:
    sk = prof["skin"]
    st = {"slot": sk.get("slot") or "body", "wt": int(sk.get("weight") or 700), "it": sk.get("style") == "italic",
          "sz": float(sk.get("size") or 56), "c": colour_hex, "fx": None}
    if speaker:
        if speaker.get("style") == "italic":
            st["it"] = True
        if speaker.get("slot"):
            st["slot"] = speaker["slot"]
        if speaker.get("weight"):
            st["wt"] = int(speaker["weight"])
    if w.emph:
        em = prof["emphasis"]
        mech = em.get("mechanism") or "none"
        ecol = hex_of(em.get("colour"), cfg.colours, colour_hex) if em.get("colour") else colour_hex
        ratio = float(em.get("ratio") or 1.0)
        if mech == "bold":
            st["wt"] = int(em.get("weight") or min(900, st["wt"] + 200))
            if em.get("colour"):
                st["c"] = ecol
        elif mech == "colour":
            st["c"] = ecol
            if em.get("weight"):
                st["wt"] = int(em["weight"])
        elif mech == "font_swap":
            st["slot"] = em.get("slot") or "serif"
            st["it"] = (em.get("style") or "italic") == "italic"
            st["wt"] = int(em.get("weight") or 400)
            st["c"] = ecol
        elif mech == "size_tier":
            st["c"] = ecol
            if em.get("weight"):
                st["wt"] = int(em["weight"])
        elif mech == "glow":
            st["c"] = ecol
            st["fx"] = {"glow": {"c": ecol, "r": float(em.get("glow_px") or 14)}}
        elif mech == "chip":
            fill = hex_of(em.get("colour") or "primary", cfg.colours, "#FCF700")
            st["c"] = hex_of(em.get("text_colour") or "ink", cfg.colours, "#0B0B0B")
            st["fx"] = {"chip": {"fill": fill, "r": 10, "pad": [2, 12]}}
        elif mech == "box":  # A18: a box / pill behind the emphasised word (fill, radius, padding, glow from the profile)
            fill = hex_of(em.get("fill") or em.get("colour") or "primary", cfg.colours, "#2AAEEB")
            st["c"] = hex_of(em.get("text_colour") or "paper", cfg.colours, "#FFFFFF")
            pad = em.get("padding") if isinstance(em.get("padding"), list) and len(em["padding"]) == 2 else [6, 16]
            box = {"fill": fill, "r": float(em["radius"]) if em.get("radius") is not None else 8, "pad": pad}
            if em.get("glow"):
                box["glow"] = float(em["glow"])
            st["fx"] = {"chip": box}
        elif mech == "underline":
            st["fx"] = {"underline": {"c": ecol, "h": max(4, round(st["sz"] * 0.09))}}
        if mech != "none":
            st["sz"] = st["sz"] * ratio
    return st


def _case_text(w: Word, prof: dict, first_in_chunk: bool) -> str:
    sk = prof["skin"]
    case = sk.get("case") or "sentence"
    txt = w.text
    pm = prof.get("punct") or "keep"
    if pm == "strip":
        lead, c, trail = X.split_edges(txt)
        txt = c if c else txt
    elif pm == "strip_end":
        txt = re.sub(r"[.,;:!…।]+$", "", txt) or txt
    if w.gloss and case in ("sentence", "as_spoken", "title"):
        return txt
    return X.apply_case(txt, case, sentence_start=w.case_start)


def arrange(ch: list[Word], prof: dict, cfg: Config, meas: Measurer, colour_hex: str, speaker: dict | None) -> dict:
    """Words -> styled word records + line breaks (indices) for one chunk."""
    sk = prof["skin"]
    trk = float(sk.get("tracking") or 0)
    recs = []
    variant = None
    line_box = None
    tiers, duet = prof.get("tiers"), prof.get("duet")
    for k, w in enumerate(ch):
        st = _word_style(w, prof, cfg, colour_hex, speaker)
        recs.append({"t": _case_text(w, prof, k == 0), "i": w.i, "s": round(w.s, 3), "e": round(w.e, 3),
                     "f": None, "emph": bool(w.emph), "tier": 0, "dev": w.dev, "spk": w.spk, **st})
        fam = script_family(recs[-1]["t"], prof, cfg)
        if fam:   # an Indic-script word: drawn in its own Noto family, no italic, no tracking (renderer `dev`)
            recs[-1]["dev"], recs[-1]["dfam"] = True, fam
    if duet:
        variant = "duet"
        jump = duet.get("size_jump") or [1.0, 1.6, 2.5]
        base = float(sk.get("size") or 56)
        mid = float(duet.get("mid_score") or 1.0)
        for k, w in enumerate(ch):
            r = recs[k]
            tier = 2 if w.emph else (1 if (w.score >= mid or w.num) else 0)
            r["tier"] = tier
            r["sz"] = base * float(jump[min(tier, len(jump) - 1)])
            if tier == 2:
                r["slot"] = duet.get("keyword_slot") or "display"
                r["it"] = (duet.get("keyword_style") or "normal") == "italic"
                r["wt"] = int(duet.get("keyword_weight") or r["wt"])
            elif tier == 1:
                r["slot"] = duet.get("mid_slot") or duet.get("keyword_slot") or r["slot"]
                r["it"] = (duet.get("mid_style") or duet.get("keyword_style") or "normal") == "italic"
                r["wt"] = int(duet.get("mid_weight") or duet.get("keyword_weight") or r["wt"])
            else:
                r["slot"] = duet.get("connector_slot") or r["slot"]
                r["it"] = (duet.get("connector_style") or "normal") == "italic"
                r["wt"] = int(duet.get("connector_weight") or r["wt"])
                if duet.get("tier0_container"):
                    tc = duet["tier0_container"]
                    r["fx"] = {"chip": {"fill": hex_of(tc.get("fill"), cfg.colours, "#2D3CF0"), "r": tc.get("radius", 4),
                                        "pad": tc.get("padding", [2, 8])}}
            if tier == 2 and duet.get("keyword_colour"):
                r["c"] = hex_of(duet["keyword_colour"], cfg.colours, r["c"])
    if tiers:
        variant = "tiers"
        kw = [k for k, w in enumerate(ch) if w.emph]
        if not kw:
            best = max(range(len(ch)), key=lambda k: ch[k].score) if ch else None
            if best is not None and ch[best].score >= float(tiers.get("min_score", 1.2)):
                kw = [best]
        cpx, kpx = float(tiers.get("connector_px") or 48), float(tiers.get("keyword_px") or 120)
        if kpx / max(cpx, 1) < float(tiers.get("min_ratio") or 2.2):
            kpx = cpx * float(tiers.get("min_ratio") or 2.2)
        for k, r in enumerate(recs):
            if k in kw:
                r["tier"] = 2
                r["sz"] = kpx
                if tiers.get("keyword_slot"):
                    r["slot"] = tiers["keyword_slot"]
                if tiers.get("keyword_style"):
                    r["it"] = tiers["keyword_style"] == "italic"
                if tiers.get("keyword_weight"):
                    r["wt"] = int(tiers["keyword_weight"])
                if tiers.get("keyword_colour"):
                    r["c"] = hex_of(tiers["keyword_colour"], cfg.colours, r["c"])
                r["fx"] = None if prof["emphasis"].get("mechanism") in ("size_tier", "none") else r["fx"]
            else:
                r["tier"] = 0
                r["sz"] = cpx if kw else float(tiers.get("plain_px") or round(cpx * 1.25))
                if tiers.get("connector_weight"):
                    r["wt"] = int(tiers["connector_weight"])
        lines = _tier_lines(len(ch), kw, tiers.get("stack") or "split")
        if tiers.get("connector_container"):
            # plain_lines (default): every all-plain line gets the box; plain_only: only chunks with no keyword at all
            if (tiers.get("connector_container_when") or "plain_lines") == "plain_only" and kw:
                line_box = [False for _ in lines]
            else:
                line_box = [all(recs[k]["tier"] == 0 for k in ln) for ln in lines]
    else:
        lines = _break_lines(recs, prof, cfg, meas)
    if prof.get("karaoke"):
        variant = variant or "karaoke"
    if prof.get("stack"):
        variant = "stack"
    for r in recs:
        r["sz"] = round(r["sz"], 1)
        r["fam"] = family_of(cfg, r["slot"])
        if r["dev"] and not r.get("dfam"):
            r["dfam"] = deva_family(prof, cfg)
        r["w"] = round(meas.width(r["t"], r["fam"] if not r["dev"] else r["dfam"], r["wt"], r["sz"], r["it"],
                                  0 if r["dev"] else trk), 1)
    if sk.get("line_fit") and (len(lines) > 1 or _line_fit_to(sk) == "max_w"):
        _line_fit(recs, lines, prof, meas, trk)
    return {"words": recs, "lines": lines, "variant": variant, "line_box": line_box}


def _line_fit_to(sk: dict) -> str:
    lf = sk.get("line_fit")
    return (lf.get("to") or "block") if isinstance(lf, dict) else str(lf)


def _line_fit(recs: list[dict], lines: list[list[int]], prof: dict, meas: Measurer, trk: float) -> None:
    """skin.line_fit (block justify): each line's words grow so the line is as wide as the widest line (`block`) or
    as `position.max_w` minus the container padding (`max_w`), at most `max_scale` (1.6) x. Lines only grow, so the
    caption floor (TC-subtitle) still holds; captions.js re-measures with the loaded fonts and evens out the rest."""
    sk = prof["skin"]
    lf = sk.get("line_fit")
    ms = float(lf.get("max_scale") or 1.6) if isinstance(lf, dict) else 1.6

    def lw(ln):
        ws = [recs[k] for k in ln]
        return sum(r["w"] for r in ws) + sum(meas.width(" ", r["fam"], r["wt"], r["sz"]) for r in ws[:-1])
    widths = [lw(ln) for ln in lines]
    if _line_fit_to(sk) == "max_w":
        cont = sk.get("container") or {}
        pad = (cont.get("padding") or [0, 0])[1] if cont.get("type") not in (None, "none") else 0
        target = float((prof.get("position") or {}).get("max_w") or 952) - 2 * float(pad)
    else:
        target = max(widths or [0])
    for ln, w in zip(lines, widths):
        if w <= 0:
            continue
        k = max(1.0, min(ms, target / w))
        if k <= 1.0005:
            continue
        for i in ln:
            r = recs[i]
            r["sz"] = round(r["sz"] * k, 1)
            r["w"] = round(meas.width(r["t"], r["fam"] if not r["dev"] else r["dfam"], r["wt"], r["sz"], r["it"],
                                      0 if r["dev"] else trk), 1)
            r["lf"] = round(k, 3)  # the line-fit scale (kept for the storyboard / debugging)


def _tier_lines(n: int, kw: list[int], mode: str) -> list[list[int]]:
    if not kw:
        return [list(range(n))]
    a, b = min(kw), max(kw)
    before, key, after = list(range(0, a)), list(range(a, b + 1)), list(range(b + 1, n))
    if mode == "below":
        return [x for x in (key, before + after) if x]
    if mode == "above":
        return [x for x in (before + after, key) if x]
    if mode == "right":
        return [before + key + after]
    return [x for x in (before, key, after) if x]


def _break_lines(recs: list[dict], prof: dict, cfg: Config, meas: Measurer) -> list[list[int]]:
    """Balanced line breaks within max_chars_line and the max width (px)."""
    n = len(recs)
    lines_max = int(prof.get("lines") or 1)
    mcl = int(prof.get("max_chars_line") or 32)
    sk = prof["skin"]
    trk = float(sk.get("tracking") or 0)
    pad = (prof["skin"].get("container") or {}).get("padding") or [0, 0]
    maxw = float((prof.get("position") or {}).get("max_w") or 952) - (2 * float(pad[1]) if (prof["skin"].get("container") or {}).get("type") not in (None, "none") else 0)
    if n <= 1 or lines_max <= 1:
        return [list(range(n))]

    def wpx(k):
        r = recs[k]
        return meas.width(r["t"], family_of(cfg, r["slot"]) if not r["dev"] else (r.get("dfam") or deva_family(prof, cfg)), r["wt"], r["sz"],
                          r["it"], trk)

    widths = [wpx(k) for k in range(n)]
    space = [meas.width(" ", family_of(cfg, recs[k]["slot"]), recs[k]["wt"], recs[k]["sz"]) for k in range(n)]

    def line_w(a, b):
        return sum(widths[a:b]) + sum(space[a:b - 1])

    def line_c(a, b):
        return sum(len(recs[k]["t"]) for k in range(a, b)) + (b - a - 1)
    full_c, full_w = line_c(0, n), line_w(0, n)
    if full_c <= mcl and full_w <= maxw:
        return [list(range(n))]
    best, best_c = None, 1e18
    if lines_max >= 2:
        for c in range(1, n):
            l1, l2 = (0, c), (c, n)
            cost = abs(line_w(*l1) - line_w(*l2)) / 100
            for a, b in (l1, l2):
                if line_c(a, b) > mcl:
                    cost += 5 + (line_c(a, b) - mcl)
                if line_w(a, b) > maxw:
                    cost += 5 + (line_w(a, b) - maxw) / 40
            last = X.norm(recs[c - 1]["t"])
            if last in X.DANGLING_END:
                cost += 0.8
            if re.search(r"[,;:]$", recs[c - 1]["t"]):
                cost -= 0.6
            if line_w(*l1) > line_w(*l2) * 1.15:
                cost += 0.2  # slight preference for a bottom-heavy pyramid
            if cost < best_c:
                best, best_c = [list(range(0, c)), list(range(c, n))], cost
    if lines_max >= 3 and n >= 3:
        for c1 in range(1, n - 1):
            for c2 in range(c1 + 1, n):
                parts = [(0, c1), (c1, c2), (c2, n)]
                ws = [line_w(a, b) for a, b in parts]
                cost = (max(ws) - min(ws)) / 100 + 0.5
                for a, b in parts:
                    if line_c(a, b) > mcl:
                        cost += 5 + (line_c(a, b) - mcl)
                    if line_w(a, b) > maxw:
                        cost += 5 + (line_w(a, b) - maxw) / 40
                if cost < best_c:
                    best, best_c = [list(range(a, b)) for a, b in parts], cost
    return best or [list(range(n))]


# ================================================================================================ geometry
def stage_at(tl: dict, t: float) -> dict:
    st = sorted([s for s in (tl.get("stage") or []) if isinstance(s, dict)], key=lambda s: s.get("t", 0))
    cur = {"t": 0, "layout": "full"}
    for s in st:
        if f_of(s.get("t", 0)) <= f_of(t):
            cur = s
    return cur


def world_at(tl: dict, t: float) -> str:
    cur = "studio"
    for w in sorted([w for w in (tl.get("world") or []) if isinstance(w, dict)], key=lambda w: w.get("t", 0)):
        if f_of(w.get("t", 0)) <= f_of(t):
            cur = w.get("world", cur)
    return cur


def swap_frames_for(frames: int, dur: int) -> int:
    """Swap-in frames a chunk (or a revealed word) of `dur` frames really gets: a fast Hinglish chunk never spends most
    of its life mid-swap. At most a third of its frames (rounded down, after the first), at least 1: a 4-5 frame chunk
    is fully opaque and sharp from the frame after it enters; long chunks keep the profile's full swap."""
    frames = max(0, int(frames or 0))
    if frames <= 1:
        return frames
    return max(1, min(frames, (int(dur) - 1) // 3))


def _span_pick(changes: list[tuple[int, str]], first: str, f0: int, f1: int) -> str:
    """The value that holds the most frames of [f0, f1) given (frame, value) switches (sorted); ties go to the later one,
    so a chunk that starts on a switch (its lead frames still on the old state) takes the new state."""
    cur, segs, a = first, [], f0
    for f, v in changes:
        if f <= f0:
            cur = v
            continue
        if f >= f1:
            break
        segs.append((a, f, cur))
        cur, a = v, f
    segs.append((a, max(f1, a + 1), cur))
    best = None
    for k, (a, b, v) in enumerate(segs):
        key = (b - a, k)
        if best is None or key >= best[0]:
            best = (key, v)
    return best[1]


def layout_for_span(tl: dict, f0: int, f1: int) -> str:
    """Stage layout id that covers most of a chunk's frames [f0, f1)."""
    st = sorted([s for s in (tl.get("stage") or []) if isinstance(s, dict)], key=lambda s: s.get("t", 0))
    return _span_pick([(f_of(s.get("t", 0)), str(s.get("layout", "full"))) for s in st], "full", f0, f1)


def world_for_span(tl: dict, f0: int, f1: int) -> str:
    """World id that covers most of a chunk's frames [f0, f1) (caption colour: ink / paper flip, colour_by_bg)."""
    ws = sorted([w for w in (tl.get("world") or []) if isinstance(w, dict)], key=lambda w: w.get("t", 0))
    ch, cur = [], "studio"
    for w in ws:
        cur = w.get("world", cur)
        ch.append((f_of(w.get("t", 0)), cur))
    return _span_pick(ch, "studio", f0, f1)


def layout_keys(cfg: Config, name: str) -> list[str]:
    keys = [name]
    lay = cfg.layouts.get(name)
    if isinstance(lay, dict) and lay.get("engine"):
        keys.append(lay["engine"])
    for lid, l in cfg.layouts.items():
        if isinstance(l, dict) and l.get("engine") == name and lid not in keys:
            keys.append(lid)
    if name in ("full", "low") and "L-full" not in keys:
        keys.append("L-full")
    return keys


def stage_rect(cfg: Config, name: str, ev: dict | None = None):
    """Approximate footage window (x, y, w, h) of a stage layout (the renderer computes it exactly per frame)."""
    lay = cfg.layouts.get(name) if isinstance(cfg.layouts.get(name), dict) else None
    if lay and isinstance(lay.get("presenter"), dict) and all(k in lay["presenter"] for k in ("x", "y", "w", "h")):
        p = lay["presenter"]
        return (p["x"], p["y"], p["w"], p["h"])
    eng = (lay or {}).get("engine") or name
    L = cfg.layout
    P = L.get("panel") or {}
    ix = (P.get("inset") or {}).get("x") or [12, 1068]
    iy = (P.get("inset") or {}).get("y") or [1008, 1881]
    bt = P.get("bleed_top") or 1135
    if eng == "panel":
        return (ix[0], bt, ix[1] - ix[0], H - bt)
    if eng in ("inset", "card"):
        return (ix[0], iy[0], ix[1] - ix[0], iy[1] - iy[0])
    if eng == "slide-aside":
        sw = ((L.get("slide_aside") or {}).get("x") or [0, 450])[1]
        return (0, 0, sw, H)
    if eng == "stack":
        sy = (lay or {}).get("seam_y") or 960
        return (0, sy, W, H - sy)
    if eng in ("bubble", "pip"):
        b = L.get("bubble") or {"cx": 210, "cy": 1560, "d": 300}
        return (b["cx"] - b["d"] / 2, b["cy"] - b["d"] / 2, b["d"], b["d"])
    if eng == "hidden":
        return None
    return (0, 0, W, H)


def position_for(cfg: Config, prof: dict, layout: str) -> dict:
    pos = {k: v for k, v in (prof.get("position") or {}).items() if k != "by_layout"}
    keys = layout_keys(cfg, layout)
    for k in keys:  # the layout's own caption block, then the profile's per-layout position
        lc = (cfg.layouts.get(k) or {}).get("caption") if isinstance(cfg.layouts.get(k), dict) else None
        if isinstance(lc, dict):
            pos.update(lc)
            break
    for k in keys:
        bl = (prof.get("position") or {}).get("by_layout") or {}
        if isinstance(bl.get(k), dict):
            pos.update(bl[k])
            break
    return pos


# ================================================================================================ build
def _overrides(tl: dict) -> list[dict]:
    return [o for o in ((tl.get("captions") or {}).get("overrides") or []) if isinstance(o, dict)]


def _apply_word_overrides(ws: list[Word], tl: dict, cfg: Config, warnings: list):
    by_i = {w.i: w for w in ws if w.i is not None}
    for o in _overrides(tl):
        targets: list[Word] = []
        if o.get("i") is not None:
            ids = o["i"] if isinstance(o["i"], list) else [o["i"]]
            targets = [by_i[x] for x in ids if x in by_i]
            if not targets:
                warnings.append(f"captions override {o}: word index not found")
        elif o.get("word") is not None:
            targets = [w for w in ws if X.norm(w.text) == X.norm(str(o["word"]))]
        elif o.get("t") is not None and not isinstance(o.get("t"), list) and ("emph" in o or "break" in o or "speaker" in o):
            t = float(o["t"])
            near = [w for w in ws if w.s - 0.05 <= t <= w.e + 0.05]
            targets = near[:1]
        if o.get("from") is not None and o.get("to") is not None:
            for w in ws:
                if X.norm(w.text) == X.norm(str(o["from"])):
                    lead, c, trail = X.split_edges(w.text)
                    w.text = lead + str(o["to"]) + trail
            continue
        for w in targets:
            if "emph" in o:
                w.force = bool(o["emph"])
            if o.get("break") in ("before", "after", True):
                w.brk = "before" if o["break"] in ("before", True) else "after"
            if "speaker" in o:
                w.spk = str(o["speaker"])
            if "text" in o and o.get("i") is not None:
                w.text = str(o["text"])
        if isinstance(o.get("t"), list) and len(o["t"]) == 2:
            a, b = float(o["t"][0]), float(o["t"][1])
            for w in ws:
                if a - 1e-6 <= w.s < b - 1e-6:
                    if o.get("profile"):
                        if o["profile"] in cfg.profiles:
                            w.prof = o["profile"]
                    if o.get("hide"):
                        w.hidden = True
            if o.get("profile") and o["profile"] not in cfg.profiles:
                warnings.append(f"captions override profile {o['profile']!r} is not a profile of this style; ignored")


def hide_ranges(cfg: Config, tl: dict, scenes: list | None, prof_hide: set) -> list[tuple[int, int, str]]:
    out = []
    for h in (tl.get("captions") or {}).get("hide") or []:
        try:
            out.append((f_of(h[0]), f_of(h[1]), "timeline"))
        except (TypeError, ValueError, IndexError):
            continue
    if "hook" in prof_hide:
        hook = [b for b in tl.get("beats") or [] if str(b.get("section", "")).upper() == "HOOK"]
        if hook:
            out.append((f_of(min(b.get("t0", 0) for b in hook)), f_of(max(b.get("t1", 0) for b in hook)), "hook"))
    if "transitions" in prof_hide:
        for tr in tl.get("transitions") or []:
            if isinstance(tr, dict) and tr.get("t") is not None:
                d = float(tr.get("dur", 0.33))
                out.append((f_of(tr["t"]), f_of(float(tr["t"]) + d), "transition"))
    # a layout whose caption block says `hide: true` shows no captions (its own type carries the words, e.g. a hook
    # layout with a lockup line and the face window where the caption band would be)
    st = sorted([e for e in (tl.get("stage") or []) if isinstance(e, dict)], key=lambda e: float(e.get("t", 0) or 0))
    for i, e in enumerate(st):
        lay = cfg.layouts.get(str(e.get("layout", "full"))) if isinstance(cfg.layouts, dict) else None
        cap = lay.get("caption") if isinstance(lay, dict) else None
        if isinstance(cap, dict) and cap.get("hide") is True:
            a = f_of(e.get("t", 0) or 0)
            b = f_of(st[i + 1].get("t", 0) or 0) if i + 1 < len(st) else 10 ** 7
            if b > a:
                out.append((a, b, "layout"))
    for s in scenes or []:
        try:
            a, b = f_of(s["t_in"]), max(f_of(s["t_out"]), f_of(s["t_in"]) + 1)
        except (KeyError, TypeError, ValueError):
            continue
        if s.get("z") == 8 and ("under_z8" in prof_hide or cfg.legacy):
            out.append((a, b, "z8"))
        if "E2" in prof_hide and str(s.get("exception", "")).upper() in ("E2", "CHAOS_BURST"):
            out.append((a, b, "E2"))
    return out


def caption_cy_at(tl: dict, scenes: list | None, f0: int, f1: int):
    """The caption centre y that holds for the chunk [f0, f1): a timeline override `{t: [a, b], cy}` covering the
    chunk's middle (the last one wins), else a scene's `caption_cy` (scene meta; the highest z, then the later one),
    else None. Lets one template put its caption pill at a different height per card / scene."""
    m = (f0 + f1 - 1) / 2 / FPS
    cy = None
    for o in _overrides(tl):
        t = o.get("t")
        if isinstance(t, list) and len(t) == 2 and _num(o.get("cy")):
            try:
                if float(t[0]) - 1e-6 <= m < float(t[1]) - 1e-6:
                    cy = float(o["cy"])
            except (TypeError, ValueError):
                continue
    if cy is not None:
        return cy
    best = None
    for s in scenes or []:
        if not isinstance(s, dict) or not _num(s.get("caption_cy")):
            continue
        try:
            if float(s["t_in"]) - 1e-6 <= m < float(s["t_out"]):
                key = (int(s.get("z") or 0), float(s["t_in"]))
                if best is None or key >= best[0]:
                    best = (key, float(s["caption_cy"]))
        except (KeyError, TypeError, ValueError):
            continue
    return best[1] if best else None


def _flicker_seq(pattern, frames: int) -> list:
    """The opacities a flicker swap really shows: the pattern cut to the swap frames, then settled (1)."""
    return list((pattern or FLICKER_PATTERN)[:max(0, int(frames))]) + [1]


def flash_frames(chunks: list[dict], profiles: dict) -> list[tuple[int, dict, str]]:
    """Every flicker flash (off -> on) the captions show: (frame, chunk, word index or "") sorted by frame. Reads the
    export (chunk `swap_type` / word `st` overrides, profile `swap` and `reveal`), so V-CAPTION uses it too."""
    out = []
    for c in chunks:
        p = profiles.get(c.get("profile")) or {}
        sw = p.get("swap") or {}
        pat = sw.get("pattern") or FLICKER_PATTERN
        rv = p.get("reveal") or "chunk"
        if rv == "char" or c.get("stack"):  # type-on and kinetic stacks never use the swap
            continue
        if rv == "word":
            for k, r in enumerate(c.get("words") or []):
                if (r.get("st") or sw.get("type")) == "flicker" and r.get("f") is not None:
                    fr = r.get("sf") if r.get("sf") is not None else (sw.get("frames") or 3)
                    out += [(int(r["f"]) + x, c, str(k)) for x in flash_rises(_flicker_seq(pat, fr))]
            continue
        if (c.get("swap_type") or sw.get("type")) != "flicker":
            continue
        fr = c.get("swap_frames") if c.get("swap_frames") is not None else int(sw.get("frames") or 0)
        fr = min(int(fr), max(0, int(c["f1"]) - int(c["f0"]) - 1))
        out += [(int(c["f0"]) + x, c, "") for x in flash_rises(_flicker_seq(pat, fr))]
    return sorted(out, key=lambda x: x[0])


def flash_overload(frames: list[int]) -> int | None:
    """The first frame where more than FLASH_MAX_PER_S flashes fall inside one second (NC-11), else None."""
    fs = sorted(frames)
    for i in range(len(fs) - FLASH_MAX_PER_S):
        if fs[i + FLASH_MAX_PER_S] - fs[i] < FPS:
            return fs[i + FLASH_MAX_PER_S]
    return None


def _flicker_budget(chunks: list[dict], cfg: Config, warnings: list) -> None:
    """Retired (no flash limit): would turn flicker swaps past 3 flashes a second into fades. Not called; kept so an
    old caller still imports it."""
    accepted: list[int] = []
    n_down = 0
    for c in chunks:
        p = cfg.profiles[c["profile"]]
        units = [("", c)] if (p.get("reveal") or "chunk") != "word" else [(str(k), r) for k, r in enumerate(c["words"])]
        for key, u in units:
            mine = [f for f, cc, k in flash_frames([c], {c["profile"]: p}) if k == key]
            if not mine:
                continue
            if flash_overload(accepted + mine) is not None:
                u["swap_type" if key == "" else "st"] = "fade"
                n_down += 1
            else:
                accepted += mine
    if n_down:
        warnings.append(f"{n_down} flicker caption swap(s) became fades: more than {FLASH_MAX_PER_S} flashes in one "
                        "second (NC-11)")


def _visible_span(f0: int, f1: int, hides: list) -> tuple[int, int] | None:
    """The first and last visible frames of [f0, f1) given hide ranges (None when fully hidden)."""
    fr = [f for f in range(f0, f1) if not any(a <= f < b for a, b, _ in hides)]
    if not fr:
        return None
    return fr[0], fr[-1] + 1


def build(tokens: dict, tl: dict | None, words_doc, *, face=None, scenes=None, frames_dir: Path | None = None,
          script: list[str] | None = None, glossary_terms=None) -> dict:
    """The full caption export for one reel (pure apart from optional frame sampling). `face`: the face boxes as a full
    stage shows them (after the E-16b base reframe)."""
    tl = tl or {}
    warnings: list[str] = []
    cfg = resolve_config(tokens, tl)
    warnings += cfg.warnings
    raw = (words_doc or {}).get("words") if isinstance(words_doc, dict) else (words_doc or [])
    raw = [w for w in raw or [] if isinstance(w, dict) and "s" in w and "e" in w]
    base = {"version": 1, "engine": ENGINE, "mode": cfg.mode, "role": cfg.role, "legacy": cfg.legacy,
            "default": cfg.default, "transform": cfg.transform}
    if cfg.mode == "off":
        return {**base, "profiles": {}, "chunks": [], "hide": [], "fallback_fonts": [], "stats": {"chunks": 0},
                "warnings": warnings}
    if any(k in (tl.get("captions") or {}) for k in ("cards", "chunks")):
        warnings.append("timeline.captions has hand-written cards/chunks; they are ignored (the caption engine builds "
                        "chunks; use captions.overrides)")
    if cfg.legacy:
        cards = legacy_cards(raw, cfg, tl)
        p = cfg.profiles["CS-1"]
        lm = Measurer(cfg.fonts)
        chunks = []
        for k, c in enumerate(cards):
            sz = p["skin"]["size"]
            chunks.append({"id": f"c{k}", "profile": "CS-1", "text": c["text"], "f0": c["f0"], "f1": c["f1"],
                           "t0": round(c["f0"] / FPS, 4), "t1": round(c["f1"] / FPS, 4),
                           "s0": round(float(c["s"]), 3), "s1": round(float(c["last"]), 3),
                           "words": [{"t": x["txt"], "i": x.get("i"), "s": x["s"], "e": x["e"]} for x in c["ws"]],
                           "class": TEXT_CLASS, "size": sz, "weight": p["skin"]["weight"],
                           "font": family_of(cfg, p["skin"]["slot"]), "anchor": "fixed_y",
                           "layout": stage_at(tl, c["f0"] / FPS).get("layout", "full"),
                           "rect": _legacy_rect(c["text"], cfg, p, lm, tl, c["f0"])})
        hides = hide_ranges(cfg, tl, scenes, set(p.get("hide") or []))
        vis, hid = [], []
        shown = bool(tl.get("captions"))  # the old renderer drew no subtitles without a timeline captions block
        for c in chunks:
            (vis if shown and _visible_span(c["f0"], c["f1"], hides) else hid).append(c)
        prof_out = {"CS-1": _profile_payload(p, cfg)}
        return {**base, "profiles": prof_out, "chunks": vis, "hidden_chunks": hid, "all_chunks": len(chunks),
                "legacy_cards": [[c["f0"], c["f1"], c["text"]] for c in cards],
                "hide": [[round(a / FPS, 4), round(b / FPS, 4), r] for a, b, r in hides], "fallback_fonts": [],
                "stats": _stats(vis, cfg), "warnings": warnings}

    glossary = X.Glossary(list(glossary_terms or []) + [t for p in cfg.profiles.values()
                                                        for t in (get(p, "language.glossary") or [])])
    ws = caption_words(raw, cfg, script=script, glossary=glossary, warnings=warnings)
    warnings.extend(regional_script_notes([w.text for w in ws]))
    # profile per word: by_layout from the stage, then planner overrides
    for w in ws:
        w.prof = cfg.default
        lay = stage_at(tl, w.s).get("layout", "full")
        for k in layout_keys(cfg, lay):
            if k in cfg.by_layout:
                w.prof = cfg.by_layout[k]
                break
    _apply_word_overrides(ws, tl, cfg, warnings)
    for k, w in enumerate(ws):  # masks + glossary after overrides
        lang = cfg.profiles[w.prof].get("language") or {}
        pm = lang.get("profanity_mask")
        if pm:
            m = X.mask_word(w.text, pm if isinstance(pm, str) else "inner", set(lang.get("mask_words") or []))
            if m != w.text:
                w.text, w.masked = m, True
    ws = [w for w in ws if not w.hidden]
    for k, w in enumerate(ws):
        nxt = ws[k + 1] if k + 1 < len(ws) else None
        w.gap = (nxt.s - w.e) if nxt else 9.0
    # chunk per profile run
    runs, cur = [], []
    for w in ws:
        if cur and w.prof != cur[-1].prof:
            runs.append(cur)
            cur = []
        cur.append(w)
    if cur:
        runs.append(cur)
    chunks_w: list[list[Word]] = []
    for run in runs:
        chunks_w += chunk_words(run, cfg.profiles[run[0].prof])
    if cfg.mode == "keywords":
        select_emphasis(chunks_w, cfg.profiles, ws)
        chunks_w = [[w] for ch in chunks_w for w in ch if w.emph]
    else:
        select_emphasis(chunks_w, cfg.profiles, ws)
    meas = Measurer(cfg.fonts)
    prof_hide = set(h for p in cfg.profiles.values() for h in (p.get("hide") or []))
    hides = hide_ranges(cfg, tl, scenes, prof_hide)
    chunks = []
    prev_f1 = 0
    for ci, ch in enumerate(chunks_w):
        pid = ch[0].prof
        prof = cfg.profiles[pid]
        spk = ch[0].spk
        sp_style = cfg.speakers.get(spk) if spk is not None else None
        skin_col = hex_of(prof["skin"].get("colour"), cfg.colours, "#FFFFFF")
        colour = hex_of(sp_style.get("colour"), cfg.colours, skin_col) if sp_style and sp_style.get("colour") else skin_col
        ar = arrange(ch, prof, cfg, meas, colour, sp_style)
        lead = int(prof.get("lead_frames") or 0)
        f0 = max(0, f_of(ch[0].s) - lead)
        if chunks and not prof.get("stack"):
            f0 = max(f0, prev_f1)
        if chunks and f0 <= chunks[-1]["f0"]:
            f0 = chunks[-1]["f0"] + 1
        nwords = len(ch)
        min_hold = max(float(prof.get("min_hold_s_per_word") or 0.25) * nwords, 0.3 if prof["unit"] == "word" else 0.25)
        f1 = max(f_of(ch[-1].e + float(prof.get("tail_s") or 0.12)), f0 + max(4, f_of(min_hold)))
        nxt = chunks_w[ci + 1] if ci + 1 < len(chunks_w) else None
        nxt_f0 = max(0, f_of(nxt[0].s) - int(cfg.profiles[nxt[0].prof].get("lead_frames") or 0)) if nxt else None
        ph = float(prof.get("pause_hold_s") or 0)
        if ph and nxt is not None:
            f1 = max(f1, min(nxt_f0, f_of(ch[-1].e + ph)))
        elif ph and nxt is None:
            f1 = max(f1, f_of(ch[-1].e + ph))
        if prof.get("max_hold_s"):
            f1 = min(f1, max(f0 + 4, f_of(ch[-1].e + float(prof["max_hold_s"]))))
        if nxt_f0 is not None and not prof.get("stack"):
            f1 = min(f1, max(nxt_f0, f0 + 1))
        f1 = max(f1, f0 + 1)
        for r in ar["words"]:
            r["f"] = max(f0, f_of(r["s"]) - lead)
        sw = prof.get("swap") or {}
        if prof.get("reveal") == "word":  # each word's own swap-in, shortened for fast words
            wfr = int(sw.get("frames") or 3)
            for k, r in enumerate(ar["words"]):
                nxt_f = ar["words"][k + 1]["f"] if k + 1 < len(ar["words"]) else f1
                r["sf"] = swap_frames_for(wfr, nxt_f - r["f"])
        elif prof.get("reveal") == "char":  # per-character type-on: each word types from its onset at `cps`
            cps = float(prof.get("cps") or 30)
            for k, r in enumerate(ar["words"]):
                nxt_f = ar["words"][k + 1]["f"] if k + 1 < len(ar["words"]) else f1
                # frames to type the word: its length at cps, but always finished before the next word starts
                r["tf"] = max(1, min(math.ceil(len(r["t"]) * FPS / cps), max(1, nxt_f - r["f"])))
        layout = layout_for_span(tl, f0, f1)  # the layout / world that holds most of the chunk (a chunk starting on a switch takes the new one)
        pos = position_for(cfg, prof, layout)
        cyo = caption_cy_at(tl, scenes, f0, f1)
        if cyo is not None:  # a per-scene / per-range caption height: a fixed_y caption at that centre
            if not cfg.safe["y"][0] <= cyo <= cfg.safe["y"][1]:
                warnings.append(f"caption cy {cyo:g} at {f0 / FPS:.2f} s is outside the safe zone "
                                f"{cfg.safe['y']}; the caption is clamped into it")
            pos = {**pos, "anchor": "fixed_y", "cy": cyo}
        rec = {"id": f"c{ci}", "profile": pid, "text": " ".join(r["t"] for r in ar["words"]), "f0": f0, "f1": f1,
               "t0": round(f0 / FPS, 4), "t1": round(f1 / FPS, 4), "s0": round(ch[0].s, 3), "s1": round(ch[-1].e, 3),
               "words": ar["words"], "lines": ar["lines"], "variant": ar["variant"], "line_box": ar["line_box"],
               "class": prof["skin"].get("text_class") or TEXT_CLASS,
               "size": round(min(r["sz"] for r in ar["words"]), 1), "size_max": round(max(r["sz"] for r in ar["words"]), 1),
               "weight": int(prof["skin"].get("weight") or 700), "font": family_of(cfg, prof["skin"].get("slot")),
               "speaker": spk, "colour": colour, "layout": layout, "world": world_for_span(tl, f0, f1),
               "anchor": pos.get("anchor", "fixed_y"), "cy": pos.get("cy"), "offset": pos.get("offset", 40),
               "emphasis": [r["t"] for r in ar["words"] if r["emph"]],
               "swap_frames": 0 if (sw.get("type") or "hard") == "hard" else swap_frames_for(int(sw.get("frames") or 0), f1 - f0)}
        _place(rec, prof, pos, cfg, tl, face)
        chunks.append(rec)
        prev_f1 = f1
    _stacks(chunks, cfg)
    stuck =[c["id"] for c in chunks if c.get("face_overlap")]
    if stuck:
        warnings.append(f"{len(stuck)} caption chunk(s) cannot clear the face inside the safe zone ({', '.join(stuck[:6])}"
                        f"{'...' if len(stuck) > 6 else ''}): set position.face_fallback_cy or a smaller caption, or reframe")
    _bg_colours(chunks, cfg, frames_dir)
    vis, hid = [], []
    for c in chunks:
        span = _visible_span(c["f0"], c.get("stack_f1", c["f1"]), hides)
        if span is None:
            hid.append(c)
            continue
        if span[0] != c["f0"]:
            c["t0"] = round(span[0] / FPS, 4)
        vis.append(c)
    fb = extra_fonts(cfg, vis, warnings)
    return {**base, "profiles": {pid: _profile_payload(p, cfg) for pid, p in cfg.profiles.items()},
            "by_layout": cfg.by_layout, "speakers": {k: {**v, "colour": hex_of(v.get("colour"), cfg.colours, "#FFFFFF")}
                                                     for k, v in cfg.speakers.items()},
            "glossary": sorted({str(t if isinstance(t, str) else t.get("term")) for p in cfg.profiles.values()
                                for t in (get(p, "language.glossary") or []) if t}),
            "chunks": vis, "hidden_chunks": hid, "all_chunks": len(chunks),
            "hide": [[round(a / FPS, 4), round(b / FPS, 4), r] for a, b, r in hides], "fallback_fonts": fb,
            "stats": _stats(vis, cfg), "warnings": warnings}


def extra_fonts(cfg: Config, chunks: list[dict], warnings: list) -> list[dict]:
    """Families the captions use that the playbook's font slots don't load (a profile may name a bundled family
    directly, e.g. a library profile), plus the Devanagari fallback when a Devanagari word is shown."""
    have = {v.get("family") for v in cfg.fonts.values()}
    fams = sorted({r["fam"] for c in chunks for r in c["words"]} - have)
    for r in (r for c in chunks for r in c["words"] if r.get("dev")):
        if r.get("dfam", DEV_FALLBACK) not in have:
            fams.append(r.get("dfam", DEV_FALLBACK))
    out = []
    for f in dict.fromkeys(fams):
        files = font_files(f)
        if files:
            out.append({"family": f, "files": files, **({"sample": SCRIPT_SAMPLE[f]} if f in SCRIPT_SAMPLE else {})})
        else:
            warnings.append(f"caption font {f!r} is neither a font slot of the playbook nor a bundled family "
                            "(assets/fonts/fonts.json); the browser falls back to a system font")
    return out


def _legacy_rect(text, cfg, p, meas, tl, f0):
    size = float(p["skin"]["size"])
    fam = family_of(cfg, p["skin"]["slot"])
    w0 = meas.width(text, fam, p["skin"]["weight"], size)
    size2 = math.floor(size * 960 / w0) if w0 > 960 else size
    w = min(w0, 960)
    cy = p["position"]["cy"]
    lay = stage_at(tl, f0 / FPS).get("layout", "full")
    lt = cfg.layouts.get(lay) if isinstance(cfg.layouts, dict) else None
    if isinstance(lt, dict) and lt.get("engine") in ("panel", "inset"):
        lay = lt["engine"]  # the renderer's v1 subtitles go by the stage's engine (core.js subtitleHTML: st.name)
    L = cfg.layout
    P = L.get("panel") or {}
    if lay == "panel":
        cy = (P.get("bleed_top") or 1135) - 60
    elif lay == "inset":
        cy = (((P.get("inset") or {}).get("y") or [1008])[0]) - 60
    h = size2 * 1.1
    return {"x": round(540 - w / 2, 1), "y": round(cy - h / 2, 1), "w": round(w, 1), "h": round(h, 1)}


def avoid_face(top: float, bh: float, bw: float, fb, pos: dict, cfg: Config, off: float, anchor: str, rec: dict) -> float:
    """The caption block's top after moving it off the face box fb (x, y, w, h); see the NC-1 note in _place."""
    ylo, yhi = cfg.safe["y"][0], cfg.safe["y"][1]
    clear = float(cfg.layout.get("face_clearance") or 40) * 0.5
    fx0, fy0, fx1, fy1 = fb[0] - clear, fb[1] - clear, fb[0] + fb[2] + clear, fb[1] + fb[3] + clear
    x0 = (cfg.safe["x"][0] if (anchor == "top_left" or pos.get("align") == "left") else float(pos.get("cx") or W / 2) - bw / 2)
    hits = lambda t: x0 < fx1 and x0 + bw > fx0 and t < fy1 and t + bh > fy0  # noqa: E731
    if not hits(top):
        return top
    rec["avoided"] = True
    gap = max(off, clear)
    if top + bh / 2 >= fb[1] + fb[3] / 2:  # at or below the face centre: below the chin
        below = fb[1] + fb[3] + gap
        if below + bh <= yhi:
            return below
        fcy = pos.get("face_fallback_cy")
        band = (float(fcy) - bh / 2) if isinstance(fcy, (int, float)) and not isinstance(fcy, bool) else yhi - bh
        band = max(ylo, min(band, yhi - bh))
        if not hits(band):
            return band
        rec["face_overlap"] = True  # nowhere below clears the face: stay as low as the safe zone allows
        return max(top, yhi - bh)
    above = fb[1] - gap - bh  # above the face centre: above the head
    if above >= ylo:
        return above
    rec["face_overlap"] = True
    return min(top, ylo)


def _place(rec: dict, prof: dict, pos: dict, cfg: Config, tl: dict, face):
    """Estimated rect (the renderer positions live; anchors needing the footage window use the stage estimate)."""
    sk = prof["skin"]
    lh = float(sk.get("line_height") or 1.15)
    cont = sk.get("container") or {}
    boxed = cont.get("type") not in (None, "none")
    pad = cont.get("padding") or [0, 0]
    trk = float(sk.get("tracking") or 0)
    widths, heights = [], []
    for line in rec["lines"]:
        ws = [rec["words"][k] for k in line]
        if not ws:
            continue
        sp = sum(0.27 * w["sz"] for w in ws[:-1])
        widths.append(sum(w["w"] for w in ws) + sp + (2 * pad[1] if cont.get("type") == "box_per_line" else 0))
        heights.append(max(w["sz"] for w in ws) * lh + (2 * pad[0] if cont.get("type") == "box_per_line" else 0))
    del trk
    bw = max(widths or [0]) + (2 * pad[1] if boxed and cont.get("type") != "box_per_line" else 0)
    bh = sum(heights) + (2 * pad[0] if boxed and cont.get("type") != "box_per_line" else 0)
    maxw = float(pos.get("max_w") or 952)
    scale = min(1.0, maxw / bw) if bw > 0 else 1.0
    bw, bh = bw * scale, bh * scale
    rec["fit"] = round(scale, 3)
    anchor = pos.get("anchor", "fixed_y")
    off = float(pos.get("offset", 40) or 0)
    cy = pos.get("cy")
    sr = stage_rect(cfg, rec["layout"])
    ev = stage_at(tl, rec["f0"] / FPS)
    top = None
    if anchor == "chest" and _face_at(face, rec["f0"], rec["layout"], cfg, ev) is not None:
        fb0 = _face_at(face, rec["f0"], rec["layout"], cfg, ev)
        top = fb0[1] + fb0[3] + off
    elif anchor == "seam" and sr:
        cy = sr[1] if sr[1] > 1 else sr[1] + sr[3]
        cy += float(pos.get("dy", 0) or 0)
    elif anchor == "seam_above" and sr:  # the block's bottom edge `offset` px above the seam: clear of the head below it
        top = (sr[1] if sr[1] > 1 else sr[1] + sr[3]) - off - bh
    elif anchor == "below_card" and sr:
        top = sr[1] + sr[3] + off
    elif anchor == "inside_footage" and sr:
        top = sr[1] + sr[3] - off - bh
    elif anchor == "top_left":
        top = cfg.safe["y"][0] + off
    if top is None:
        cy = float(cy if cy is not None else 1300)
        top = cy - bh / 2
    ylo, yhi = cfg.safe["y"][0], cfg.safe["y"][1]
    top = max(ylo, min(top, yhi - bh))
    # never cover the face (NC-1): a caption that would sit on the face moves AWAY from it, never across it: one that
    # sits at or below the face centre goes below the chin, else down to the fallback band (`position.face_fallback_cy`,
    # default the lowest caption line of the safe zone); one above the face centre goes above the head. If neither
    # clears the face, the caption keeps the position furthest from the face on its own side and is flagged.
    # Full-frame stages only (full, low): on a window (card, pip, stack, split) the caption stays where the layout puts
    # it; the Director decides whether it may touch the person there (Naman, 10 Oct 2026: captions on the face are okay).
    fb = _face_at(face, rec["f0"], rec["layout"], cfg, ev)
    if fb is not None and pos.get("avoid_face", True) and anchor not in ("top_left",):
        top = avoid_face(top, bh, bw, fb, pos, cfg, off, anchor, rec)
    if anchor == "top_left" or pos.get("align") == "left":
        x = cfg.safe["x"][0] + (float(pos.get("x", 0)) if pos.get("x") is not None else 0)
    else:
        cx = float(pos.get("cx") or W / 2)
        x = cx - bw / 2
    rec["rect"] = {"x": round(x, 1), "y": round(top, 1), "w": round(bw, 1), "h": round(bh, 1)}
    if anchor == "chest" or rec.get("avoided"):
        rec["top"] = round(top, 1)
    rec["cy"] = round(top + bh / 2, 1) if anchor in ("fixed_y", "chest") else rec.get("cy")


def _face_engine(cfg: Config | None, layout: str) -> str | None:
    """'full' / 'low' when the footage fills the frame on this layout (by name, or a token layout whose engine is
    full / low), else None."""
    if layout in ("full", "L-full"):
        return "full"
    if layout == "low":
        return "low"
    lay = (cfg.layouts.get(layout) if cfg is not None else None) or {}
    eng = lay.get("engine") if isinstance(lay, dict) else None
    if eng in ("full", "low") and not isinstance(lay.get("presenter"), dict):
        return eng
    return None


LOW_OFFSET = 380  # core.js geom "low": the footage drops by the stage entry's `offset`, else 380 px


def _face_at(face, f0: int, layout: str, cfg: Config | None = None, ev: dict | None = None):
    """Smoothed face box (x, y, w, h) in screen space around frame f0 when the footage fills the frame, else None.
    On `low` the footage is lowered by the stage entry's `offset` (what the renderer uses), else LOW_OFFSET."""
    eng = _face_engine(cfg, layout)
    if not face or eng is None:
        return None
    n = min(max(f0, 0), len(face) - 1)
    bs = [b for b in face[max(0, n - 6):min(len(face), n + 7)] if b]
    if not bs:
        return None
    dy = 0.0
    if eng == "low":
        off = (ev or {}).get("offset")
        dy = float(off) if isinstance(off, (int, float)) and not isinstance(off, bool) else LOW_OFFSET
    return tuple(sum(b[k] for b in bs) / len(bs) + (dy if k == 1 else 0) for k in range(4))


def _stacks(chunks: list[dict], cfg: Config):
    """Kinetic stack: consecutive line chunks accumulate until max_lines, a sentence end + pause, or a speaker /
    profile change; every line stays until the stack clears (all at once)."""
    sid, cur = 0, []

    def close(group):
        nonlocal sid
        if not group:
            return
        p = cfg.profiles[group[0]["profile"]]["stack"]
        clear = int(p.get("clear_frames") or 6)
        end = max(c["f1"] for c in group)
        alt = p.get("alternate") or []
        for k, c in enumerate(group):
            c["stack"] = {"id": sid, "pos": k, "n": len(group), "f_end": end, "clear": clear}
            c["stack_f1"] = end
            if alt:
                slot = alt[k % len(alt)]
                for r in c["words"]:
                    r["slot"] = slot if isinstance(slot, str) else slot.get("slot", r["slot"])
                    if isinstance(slot, dict):
                        r["it"] = slot.get("style") == "italic"
                        if slot.get("weight"):
                            r["wt"] = int(slot["weight"])
                        if slot.get("size"):
                            r["sz"] = float(slot["size"])
                    r["fam"] = family_of(cfg, r["slot"])
        sid += 1

    for c in chunks:
        p = cfg.profiles[c["profile"]].get("stack")
        if not p:
            close(cur)
            cur = []
            continue
        if cur:
            prev = cur[-1]
            gap = (c["s0"] - prev["s1"])
            ended = prev["words"] and re.search(r"[.?!।]$", prev["words"][-1]["t"] or "")
            if (len(cur) >= int(p.get("max_lines") or 5) or prev["profile"] != c["profile"] or prev["speaker"] != c["speaker"]
                    or gap >= float(p.get("clear_gap_s") or 1.0) or (ended and gap >= 0.3)):
                close(cur)
                cur = []
        cur.append(c)
    close(cur)
    # a stack's lines share the rect column; extend each stack's last line to the next stack's start
    for k, c in enumerate(chunks):
        if "stack" in c and c["stack"]["pos"] == c["stack"]["n"] - 1:
            nxt = next((d for d in chunks[k + 1:]), None)
            end = c["stack"]["f_end"]
            if nxt is not None:
                end = min(end, nxt["f0"])
            for d in chunks:
                if d.get("stack", {}).get("id") == c["stack"]["id"]:
                    d["stack"]["f_end"] = max(end, d["f0"] + 1)
                    d["stack_f1"] = d["stack"]["f_end"]
                    d["f1"] = d["stack_f1"]
                    d["t1"] = round(d["f1"] / FPS, 4)


def _world_lum(c: dict, cfg: Config) -> float:
    wd = cfg.worlds.get(c["world"]) if isinstance(cfg.worlds.get(c["world"]), dict) else None
    bg = (wd or {}).get("bg") or {"canvas": cfg.colours.get("canvas", "#FCFCFC"),
                                  "data": cfg.colours.get("night", "#07070C")}.get(c["world"])
    if not bg and (wd or {}).get("light"):
        return 0.9
    return luma_hex(hex_of(bg, cfg.colours, "#000000")) if bg else 0.15


def _shadow_is_dark(shadow) -> bool:
    s = str(shadow or "").lower()
    if not s or s == "none":
        return False
    m = re.findall(r"rgba?\(([^)]*)\)", s)
    if m:
        vals = [float(x) for x in re.split(r"[ ,/]+", m[0].strip()) if x][:3]
        return len(vals) == 3 and sum(vals) / 3 < 110
    return "#000" in s or "black" in s


def _bg_colours(chunks: list[dict], cfg: Config, frames_dir: Path | None):
    """colour_by_bg: the background under each chunk (world colour off the footage window, else the sampled footage
    luma at the chunk's rect) picks the light/dark text colour once per chunk (no flicker inside a chunk).

    The ink / paper flip also runs without colour_by_bg: a chunk off the footage window whose world matches the text
    (light text on a light world such as paper, dark text on a dark one) switches to `ink` / `paper`. Dark text on a
    light world drops a dark drop shadow (chunk `shadow: "none"`): ink with a black shadow reads as a grey smear."""
    for c in chunks:
        prof = cfg.profiles[c["profile"]]
        cb = (prof.get("position") or {}).get("colour_by_bg")
        r = c["rect"]
        cx, cy = r["x"] + r["w"] / 2, r["y"] + r["h"] / 2
        sr = stage_rect(cfg, c["layout"])
        on_foot = sr is not None and sr[0] <= cx <= sr[0] + sr[2] and sr[1] <= cy <= sr[1] + sr[3]
        fixed = bool(c.get("speaker") and cfg.speakers.get(c["speaker"], {}).get("colour"))
        boxed = ((prof.get("skin") or {}).get("container") or {}).get("type") not in (None, "none")
        if cb:
            lum = None
            if not on_foot:
                lum = _world_lum(c, cfg)
            elif frames_dir is not None:
                lum = _sample_luma(frames_dir, (c["f0"] + c["f1"]) // 2, r)
            kind = "light" if (lum if lum is not None else 0.2) > 0.55 else "dark"
            col = hex_of(cb.get(kind), cfg.colours, c["colour"])
        elif not on_foot and not boxed and not fixed:
            lum = _world_lum(c, cfg)
            kind = "light" if lum > 0.55 else "dark"
            tl_ = luma_hex(c["colour"])
            if kind == "light" and tl_ > 0.55:
                col = hex_of("ink", cfg.colours, "#0B0B0B")
            elif kind == "dark" and tl_ < 0.45:
                col = hex_of("paper", cfg.colours, "#FFFFFF")
            else:
                continue
        else:
            continue
        c["bg"] = kind
        if fixed:
            continue
        base = c["colour"]
        c["colour"] = col
        for w in c["words"]:
            if w["c"] == base:
                w["c"] = col
        if kind == "light" and luma_hex(col) < 0.45 and _shadow_is_dark((prof.get("skin") or {}).get("shadow")):
            c["shadow"] = "none"


def _sample_luma(frames_dir: Path, f: int, r: dict) -> float | None:
    p = Path(frames_dir) / f"f{f:05d}.jpg"
    if not p.exists():
        return None
    try:
        from PIL import Image
        with Image.open(p) as im:
            im = im.convert("L")
            sx, sy = im.width / W, im.height / H
            box = (int(max(0, r["x"]) * sx), int(max(0, r["y"]) * sy), int(min(W, r["x"] + r["w"]) * sx),
                   int(min(H, r["y"] + r["h"]) * sy))
            if box[2] <= box[0] or box[3] <= box[1]:
                return None
            reg = im.crop(box).resize((16, 4))
            px = list(reg.getdata())
            return sum(px) / len(px) / 255
    except Exception:  # noqa: BLE001
        return None


def _profile_payload(p: dict, cfg: Config) -> dict:
    """What the renderer needs from a profile, colours resolved to hex."""
    sk = copy.deepcopy(p.get("skin") or {})
    sk["colour"] = hex_of(sk.get("colour"), cfg.colours, "#FFFFFF")
    sk["stroke_colour"] = hex_of(sk.get("stroke_colour"), cfg.colours, "#0B0B0B")
    sk["fam"] = family_of(cfg, sk.get("slot"))
    cont = sk.get("container") or {}
    if cont:
        cont["fill"] = hex_of(cont.get("fill"), cfg.colours, "#0B0B0B")
        if cont.get("border"):
            cont["border_colour"] = hex_of(cont.get("border_colour"), cfg.colours, "#FFFFFF")
    kar = copy.deepcopy(p.get("karaoke"))
    if kar:
        kar["active"] = hex_of(kar.get("active"), cfg.colours, "#111111")
        kar["queued"] = hex_of(kar.get("queued"), cfg.colours, "#9B9B9B")
    pos = {k: v for k, v in (p.get("position") or {}).items()}
    tiers = copy.deepcopy(p.get("tiers"))
    if tiers and tiers.get("connector_container"):
        tiers["connector_container"]["fill"] = hex_of(tiers["connector_container"].get("fill"), cfg.colours, "#000000")
    extra = {"problems": list(p["problems"])} if p.get("problems") else {}
    return {**extra, "legacy": bool(p.get("legacy")), "unit": p.get("unit"), "skin": sk, "position": pos,
            "swap": p.get("swap") or {}, "reveal": p.get("reveal") or "chunk", "cps": p.get("cps"), "karaoke": kar,
            "stack": p.get("stack"), "tiers": tiers, "duet": p.get("duet"), "hide": p.get("hide") or [],
            "emphasis": {k: (p.get("emphasis") or {}).get(k) for k in ("mechanism", "max_per_chunk", "max_per_s", "span")},
            "lines": p.get("lines"), "words": p.get("words"), "max_chars_line": p.get("max_chars_line"),
            "lead_frames": p.get("lead_frames")}


def _stats(chunks: list[dict], cfg: Config) -> dict:
    if not chunks:
        return {"chunks": 0}
    nw = [len(c.get("words") or []) for c in chunks]
    dur = [(c["f1"] - c["f0"]) / FPS for c in chunks]
    return {"chunks": len(chunks), "words_per_chunk": round(sum(nw) / len(nw), 2), "max_words": max(nw),
            "mean_hold_s": round(sum(dur) / len(dur), 2),
            "emphasis": sum(len(c.get("emphasis") or []) for c in chunks),
            "profiles": sorted({c["profile"] for c in chunks}), "legacy": cfg.legacy}
