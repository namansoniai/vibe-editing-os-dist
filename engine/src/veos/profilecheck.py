"""Style profile checks: PV-1...PV-12 (V-PROFILE) and the presenter presence rule (V-PRESENCE).

Structure Part A §0.2 (profile validity) and SW-02 (presenter). `violations(style)` works on a resolved style dict
(`tokens.effective_style`), so `veos tokens` (warnings) and `veos validate` (V-PROFILE failures) share one implementation.
"""
from __future__ import annotations

import copy

from .vcommon import FRAME_H, fail, get_path, norm_box, taste

ENUMS = {
    "source_type": ("talking_head", "voiceover_only", "narrated_footage", "multi_speaker", "edited_master",
                    "stunt_footage", "animated_plates", "no_voice"),
    "presenter.presence": ("anchor", "host", "guest", "flash", "none"),
    "spine": ("talking_head", "audio", "footage", "hybrid"),
    "captions.mode": ("off", "keywords", "full"),
    "captions.role": ("support", "primary"),
    "captions.mute_policy": ("mute_safe", "sound_on"),
    "graphics": ("passthrough", "minimal", "support", "primary"),
    "duration.class": ("micro", "short", "standard", "long"),
    "tone.energy": ("calm", "balanced", "hype"),
    "tone.comedy": ("off", "light", "roast"),
    "themes.policy": ("single", "per_reel", "per_topic", "per_section"),
    "footage_dependency": ("none", "low", "medium", "high", "total"),
}
REQUIRED = ("source_type", "presenter", "spine", "captions", "graphics", "duration", "tone", "themes", "formats",
            "footage_dependency", "cta", "modules")
MODULES = ("chrome", "running_state", "anchors", "data_figures", "citations", "dialogue", "canvas_camera", "ink",
           "continuity", "series", "brand")
CTA_DEVICES = ("comment_keyword", "dm", "link_bio", "qr", "subscribe", "follow_save_stack", "product_card", "end_card",
               "cross_promo", "post_only", "none")
FOOTAGE_LEVEL = {"none": 0, "low": 1, "medium": 2, "high": 3, "total": 4}
NO_PRESENTER_SOURCES = ("voiceover_only", "narrated_footage", "animated_plates", "edited_master", "no_voice")
PRESENCE_FACE_FRAC = 0.06            # SW-02: the face counts as visible at >= 6 % of frame height
COVER_FRAC = 0.9                     # a scene covering >= 90 % of the frame hides the presenter when opaque
FULLFRAME_FOOTAGE = ("broll", "footage", "clip", "archive", "video")


def _v(pid, msg, fix, where=None):
    return {"id": pid, "msg": msg if not where else f"{where}: {msg}", "fix": fix}


def presence_of(style: dict) -> str:
    return str(get_path(style, "profile.presenter.presence", "anchor") or "anchor")


def _check_profile(prof: dict, style: dict, where: str | None = None) -> list[dict]:
    """PV-1...PV-11 (and the switch vocabulary) for one resolved profile."""
    out: list[dict] = []
    g = lambda p, d=None: get_path(prof, p, d)  # noqa: E731
    for k in REQUIRED:
        if k not in prof:
            out.append(_v("PV-0", f"profile.{k} is missing", f"add profile.{k} (structure §0.1)", where))
    for path, allowed in ENUMS.items():
        val = g(path)
        if val is not None and val not in allowed:
            out.append(_v("PV-0", f"profile.{path} = {val!r} is not one of {', '.join(allowed)}",
                          f"set profile.{path} to one of {', '.join(allowed)}", where))
    for d in g("cta.devices", []) or []:
        if d not in CTA_DEVICES:
            out.append(_v("PV-0", f"profile.cta.devices has unknown device {d!r}", f"use devices from {', '.join(CTA_DEVICES)}", where))
    for m in (g("modules") or {}):
        if m not in MODULES:
            out.append(_v("PV-0", f"profile.modules.{m} is not a known module", f"use modules from {', '.join(MODULES)}", where))
    mods = g("modules") or {}
    presence, src, spine = g("presenter.presence"), g("source_type"), g("spine")
    excs = {k for k, v in (style.get("exceptions") or {}).items() if v not in (None, False)}
    # PV-1 (V-PRESENCE and the face rules are switched off by the validator itself when presence is none)
    if presence == "none":
        if src not in NO_PRESENTER_SOURCES:
            out.append(_v("PV-1", f"presence: none needs source_type in {', '.join(NO_PRESENTER_SOURCES)} (is {src})",
                          "change source_type, or give the style a presenter", where))
        if spine == "talking_head":
            out.append(_v("PV-1", "presence: none cannot have spine: talking_head", "set spine to audio, footage or hybrid", where))
        if "E1" in excs:
            out.append(_v("PV-1", "presence: none but exception E1 (behind-subject type) is declared", "remove exceptions.E1", where))
    # PV-2
    if src == "multi_speaker":
        if not mods.get("dialogue"):
            out.append(_v("PV-2", "source_type: multi_speaker needs modules.dialogue = true", "turn modules.dialogue on", where))
        if not get_path(style, "captions.speakers"):
            out.append(_v("PV-2", "source_type: multi_speaker needs a caption speaker map (captions.speakers)",
                          "add captions.speakers with a colour per cast member", where))
    # PV-3
    if src == "voiceover_only":
        if g("footage_dependency") not in ("none", "low", "medium"):
            out.append(_v("PV-3", f"voiceover_only needs footage_dependency none/low/medium (is {g('footage_dependency')})",
                          "lower footage_dependency", where))
        if g("graphics") not in ("support", "primary"):
            out.append(_v("PV-3", f"voiceover_only needs graphics support or primary (is {g('graphics')})",
                          "set graphics to support or primary", where))
    # PV-4
    if g("graphics") == "passthrough":
        if g("footage_dependency") != "total":
            out.append(_v("PV-4", "graphics: passthrough needs footage_dependency: total", "set footage_dependency: total", where))
        if mods.get("canvas_camera"):
            out.append(_v("PV-4", "graphics: passthrough cannot use the canvas camera", "turn modules.canvas_camera off", where))
    # PV-5
    if mods.get("canvas_camera") and g("graphics") != "primary":
        out.append(_v("PV-5", "modules.canvas_camera needs graphics: primary", "set graphics: primary or turn the canvas camera off", where))
    # PV-6
    if g("captions.mode") == "off":
        if g("captions.mute_policy") != "sound_on":
            out.append(_v("PV-6", "captions.mode: off needs captions.mute_policy: sound_on", "set mute_policy: sound_on", where))
        if not g("language.on_screen"):
            out.append(_v("PV-6", "captions.mode: off needs language.on_screen declared", "set profile.language.on_screen", where))
    # PV-7
    if g("duration.class") in ("standard", "long") and not get_path(style, "structure.rehook_every_s"):
        out.append(_v("PV-7", f"duration class {g('duration.class')} needs a re-hook interval (structure.rehook_every_s)",
                      "set structure.rehook_every_s (standard: one mid-reel re-hook; long: every 20-30 s)", where))
    # PV-8
    if g("themes.policy") not in (None, "single"):
        packs = list(g("themes.packs") or [])
        if len(packs) < 2:
            out.append(_v("PV-8", f"themes.policy {g('themes.policy')} needs >= 2 packs (has {len(packs)})",
                          "add theme packs or set policy: single", where))
        defined = style.get("_theme_packs") or style.get("themes") or {}
        for p in packs:
            if p not in defined:
                out.append(_v("PV-8", f"theme pack {p} is listed in profile.themes.packs but not defined in themes",
                              f"add themes.{p}", where))
        for msg in style.get("_theme_contrast_fail") or []:
            out.append(_v("PV-8", msg, "pick a theme colour that reaches 4.5:1 against its text colour", where))
    # PV-9 (E1 behind-subject type needs a presenter and the matte; E5 edge bleed works for faceless styles too)
    if "E1" in excs:
        if presence == "none":
            out.append(_v("PV-9", "exception E1 needs presenter footage (presence is none)", "remove exceptions.E1", where))
        elif get_path(style, "footage.matte") in (None, "none"):
            out.append(_v("PV-9", "exception E1 needs the matte step (footage.matte optional or required)",
                          "set footage.matte to optional or required", where))
    # PV-10
    comedy = g("tone.comedy")
    if comedy == "roast" and "mock" not in (style.get("tones") or []):
        out.append(_v("PV-10", "tone.comedy: roast needs the 'mock' tone in tones", "add 'mock' to tones", where))
    if get_path(style, "sound.meme_cues") is True and comedy != "roast":
        out.append(_v("PV-10", f"sound.meme_cues is true but tone.comedy is {comedy}", "set sound.meme_cues: false (meme cues need comedy: roast)", where))
    # PV-11
    if FOOTAGE_LEVEL.get(g("footage_dependency"), 0) >= FOOTAGE_LEVEL["high"]:
        fbs = {f.get("id") for f in (get_path(style, "footage.fallbacks") or []) if isinstance(f, dict)}
        for sh in get_path(style, "footage.shots") or []:
            if not isinstance(sh, dict):
                continue
            fb = sh.get("fallback")
            if fb == "no_fallback" or sh.get("no_fallback"):
                continue
            if not fb or fb not in fbs:
                out.append(_v("PV-11", f"shot {sh.get('id')} has no fallback (footage_dependency {g('footage_dependency')})",
                              f"give {sh.get('id')} a fallback FB-... from footage.fallbacks, or mark it no_fallback", where))
    return out


def format_view(style: dict, f: dict) -> dict:
    """The resolved style as format `f` alone would make it: the blocks formats override go back to the style's own
    values (`_resolved.base_blocks`), then f's overrides apply (structure, cadence, ... are read per format)."""
    from .tokens import FORMAT_META_KEYS, deep_merge
    res = style.get("_resolved") or {}
    out = dict(style)
    for k, v in (res.get("base_blocks") or {}).items():
        if v is None:
            out.pop(k, None)
        else:
            out[k] = copy.deepcopy(v)
    out["profile"] = deep_merge(copy.deepcopy(res.get("base_profile") or {}), f.get("profile") or {})
    for k, v in f.items():
        if k in FORMAT_META_KEYS or k == "profile":
            continue
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(copy.deepcopy(out[k]), v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def violations(style: dict) -> list[dict]:
    """PV-1...PV-12 for a resolved style (the chosen format applied). Empty list = valid."""
    prof = style.get("profile") or {}
    out = _check_profile(prof, style)
    base = (style.get("_resolved") or {}).get("base_profile")
    chosen = (style.get("_resolved") or {}).get("format")
    if base is not None:  # PV-12: every other format must be valid on its own
        for fid, f in (style.get("formats") or {}).items():
            if fid == chosen or not isinstance(f, dict):
                continue
            fstyle = format_view(style, f)
            for v in _check_profile(fstyle["profile"], fstyle, where=f"format {fid}"):
                if v["id"] != "PV-0" or "missing" not in v["msg"]:
                    out.append({**v, "id": "PV-12", "msg": f"({v['id']}) {v['msg']}"})
    return out


# --------------------------------------------------------------------------- validator rules
def rule_profile(c, p) -> list[dict]:
    """V-PROFILE: PV-1...PV-12 on the resolved tokens."""
    return [fail("V-PROFILE", None, 0, f"{v['id']}: {v['msg']}", v["fix"]) for v in violations(c.style)]


def presenter_visible(c, n: int, need_face: bool = True) -> bool:
    """Presenter visible at frame n: stage not hidden, not under an opaque full-frame scene, and (when face boxes are
    loaded and need_face) a face box at >= 6 % of frame height."""
    t = n / c.fps if c.fps else n / 30
    if c.stage_engine_at(t) == "hidden":
        return False
    for s in c.scenes:
        if not c.active(s, n) or s.get("behind") or s.get("z", 0) < 3 or s.get("z") == 11:
            continue
        if not (s.get("opaque") or s.get("covers_presenter") or s.get("kind") in FULLFRAME_FOOTAGE):
            continue
        b = c.rect(s, n)
        if b is not None and (b[2] - b[0]) * (b[3] - b[1]) >= COVER_FRAC * 1080 * 1920:
            return False
        if s.get("covers_presenter"):
            return False
    if need_face and c.face is not None:
        fb = c.face[n] if n < len(c.face) else None
        fb = norm_box(fb) if fb else None
        if fb is None or (fb[3] - fb[1]) < PRESENCE_FACE_FRAC * FRAME_H:
            return False
    return True


def rule_presence(c, p) -> list[dict]:
    """V-PRESENCE: presenter share within profile.presenter.share and longest absence <= max_absence_s.
    Off when presence is none. The share is taste (vcommon.taste): validate leaves it out (stats.presence keeps it)."""
    pres = get_path(c.style, "profile.presenter", {}) or {}
    if pres.get("presence") == "none" or c.frames < 1:
        return []
    share = p.get("share", pres.get("share"))
    max_abs = p.get("max_absence_s", pres.get("max_absence_s"))
    vis = [presenter_visible(c, n) for n in range(c.frames)]
    pct = 100.0 * sum(vis) / len(vis)
    longest, cur, start, best_start = 0, 0, 0, 0
    for n, v in enumerate(vis + [True]):
        if not v:
            if cur == 0:
                start = n
            cur += 1
        else:
            if cur > longest:
                longest, best_start = cur, start
            cur = 0
    c.stats_extra["presence"] = {"share_pct": round(pct, 1), "longest_absence_s": round(longest / c.fps, 2),
                                 "face_checked": c.face is not None}
    out = []
    if isinstance(share, (list, tuple)) and len(share) == 2:
        lo, hi = (float(share[0]), float(share[1]))
        if hi <= 1.0:  # written as fractions
            lo, hi = lo * 100, hi * 100
        if pct < lo - 1e-6:
            out.append(taste(fail("V-PRESENCE", None, 0, f"the presenter is visible {pct:.0f}% of the reel (style range {lo:.0f}-{hi:.0f}%)",
                                  "shorten full-frame cutaways or hidden-stage spans, or use a layout that keeps the presenter visible (panel, card, pip)")))
        elif pct > hi + 1e-6:
            from .layoutrules import library, missing_footage
            lay = list((c.style.get("_resolved") or {}).get("layouts") or []) or list(library(c.style))
            missing = missing_footage(c, lay)
            msg = f"the presenter is visible {pct:.0f}% of the reel (style range {lo:.0f}-{hi:.0f}%)"
            if missing:  # the cutaways that would lower it are creator footage this project does not have
                msg += ("; the range assumes creator footage this project does not have: "
                        + "; ".join(f"{w} for {lid}" for lid, w in missing))
            out.append(taste(fail("V-PRESENCE", None, 0, msg,
                                  "add the style's cutaways (graphics full-frame, B-roll or hidden-stage spans) to reach the range")))
    if max_abs is not None and longest / c.fps > float(max_abs) + 1e-6:
        t = best_start / c.fps
        out.append(fail("V-PRESENCE", c.beat_id(t), t,
                        f"the presenter is absent for {longest / c.fps:.1f} s from {t:.1f} s (max {max_abs} s)",
                        f"bring the presenter back (stage layout or a smaller cutaway) before {t + float(max_abs):.1f} s"))
    return out
