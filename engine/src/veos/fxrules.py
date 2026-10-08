"""Footage blur, built-in transitions, blur pulses and the end fade (Package A): V-FX for `veos validate`.

The renderer side is renderer/transitions.js (`check()` there is mirrored here exactly; the player boot fails on the same
problems). Runs only when the timeline uses one of these fields, so older reels validate exactly as before.

V-FX     the fields are well formed: timeline.transitions[] entries with a `type` (built-in transitions), timeline.blur[],
         camera[].blur / camera[].p.blur / camera_presets.<id>.blur, timeline.grades[].blur / .frame, timeline.end_fade.
         Two built-in transitions may not overlap in time (advice; a malformed field blocks: it breaks the render).
Flashes are free: there is no flash limit (Naman, 8 Oct 2026). A style that uses rapid flashes uses them.
"""
from __future__ import annotations

from typing import Any

from .vcommon import advice, fail

FPS = 30
TYPES = {"flash": (7, 2), "leak": (16, 9), "blur-through": (10, 5), "zoom-blur": (8, 4), "whip": (8, 4),
         "glitch": (6, 3), "burn": (14, 2), "iris": (10, 0), "curtain": (12, 0), "push": (12, 0)}  # (frames, pre)
LUMINOUS = ("flash", "leak", "burn")
KINDS = ("defocus", "directional", "radial")
SHAPES = ("pulse", "decay", "rise", "hold")
LAYERS = ("picture", "stage", "all")
DIRS = ("left", "right", "up", "down")
BLENDS = ("light", "normal", "screen", "add")  # flash: how it lights the picture (light: exposure + soft veil)
CLEARS = ("fade", "wipe")                      # flash: a uniform decay, or a top -> bottom (dir) reveal
NUM = {
    "common": {"frames": (1, 90), "pre": (0, 90)},
    "flash": {"peak": (0, 1), "decay": (0.2, 6), "clear_frames": (1, 90), "feather": (0, 960)},
    "leak": {"peak": (0, 1), "angle": (-360, 360)},
    "blur-through": {"px": (0, 80)},
    "zoom-blur": {"amount": (0, 0.6), "punch": (0, 0.4)},
    "whip": {"angle": (-360, 360), "px": (0, 200), "travel": (0, 1080), "blend": (0, 6)},
    "glitch": {"slices": (0, 16), "offset": (0, 300), "rgb": (0, 60), "posterize": (0, 16), "seed": (-1e9, 1e9)},
    "burn": {"peak": (0, 1), "ring": (0, 400)},
    "iris": {"ring": (0, 240), "feather": (0, 200)},
    "curtain": {},
    "push": {},
}
ENV_NUM = {"px": (0, 80), "angle": (-360, 360), "amount": (0, 0.6), "frames": (1, 300)}
STAGE_TYPES = ("blur-through", "zoom-blur", "whip")


def _num(v: Any) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and v == v and abs(v) != float("inf")


def _n(v: float) -> str:  # numbers as JS prints them
    return str(int(v)) if float(v).is_integer() else repr(v)


def _fr(t: float) -> int:
    return int(round(float(t) * FPS))


def _at_ok(v: Any) -> bool:
    return v in ("face", "centre") or (isinstance(v, list) and len(v) == 2 and all(_num(x) for x in v))


def check_env(b: Any, where: str) -> list[str]:
    """A blur envelope {kind, px, angle, amount, at, frames, shape, keys} -> problems."""
    if not isinstance(b, dict):
        return [f"{where} must be an object {{kind, px | amount, frames, shape | keys}}"]
    out = []
    if b.get("kind") is not None and b["kind"] not in KINDS:
        out.append(f"{where}.kind '{b['kind']}' is not one of {' | '.join(KINDS)}")
    if b.get("shape") is not None and b["shape"] not in SHAPES:
        out.append(f"{where}.shape '{b['shape']}' is not one of {' | '.join(SHAPES)}")
    for k, (lo, hi) in ENV_NUM.items():
        if b.get(k) is not None and not (_num(b[k]) and lo <= b[k] <= hi):
            out.append(f"{where}.{k} must be a number {_n(lo)}..{_n(hi)}")
    if b.get("at") is not None and not _at_ok(b["at"]):
        out.append(f'{where}.at must be "face", "centre" or [x, y]')
    ks = b.get("keys")
    if ks is not None and not (isinstance(ks, list) and ks and all(
            isinstance(k, list) and len(k) == 2 and _num(k[0]) and k[0] >= 0 and _num(k[1]) and 0 <= k[1] <= 1 for k in ks)):
        out.append(f"{where}.keys must be [[frame >= 0, 0..1], ...]")
    return out


def check_transition(tr: Any, i: int) -> list[str]:
    w = f"timeline.transitions[{i}]"
    if not isinstance(tr, dict) or tr.get("type") is None:
        return []  # a marker
    ty = tr["type"]
    if ty not in TYPES:
        return [f"{w}.type '{ty}' is not a built-in transition ({' | '.join(TYPES)})"]
    out = []
    if not (_num(tr.get("t")) and tr["t"] >= 0):
        out.append(f"{w} needs t (the cut, edit seconds >= 0)")
    lim = {**NUM["common"], **NUM[ty]}
    for k, (lo, hi) in lim.items():
        if tr.get(k) is not None and not (_num(tr[k]) and lo <= tr[k] <= hi):
            out.append(f"{w}.{k} must be a number {_n(lo)}..{_n(hi)}")
    frames = tr.get("frames", TYPES[ty][0])
    if _num(tr.get("pre")) and _num(frames) and tr["pre"] > frames:
        out.append(f"{w}.pre ({tr['pre']}) must not exceed frames ({frames})")
    if tr.get("layers") is not None and tr["layers"] not in LAYERS:
        out.append(f"{w}.layers '{tr['layers']}' is not one of {' | '.join(LAYERS)}")
    if tr.get("layers") == "stage" and ty not in STAGE_TYPES:
        out.append(f'{w}.layers "stage" only applies to blur-through, zoom-blur and whip')
    for k in ("colour", "color"):
        if tr.get(k) is not None and not isinstance(tr[k], str):
            out.append(f"{w}.{k} must be a hex colour or a colour role")
    cs = tr.get("colours")
    if cs is not None and not (isinstance(cs, list) and 2 <= len(cs) <= 5 and all(isinstance(c, str) for c in cs)):
        out.append(f"{w}.colours must be 2-5 hex colours or roles")
    if tr.get("dir") is not None and tr["dir"] not in DIRS:
        out.append(f"{w}.dir '{tr['dir']}' is not one of {' | '.join(DIRS)}")
    if ty == "flash" and tr.get("blend") is not None and tr["blend"] not in BLENDS:
        out.append(f"{w}.blend '{tr['blend']}' is not one of {' | '.join(BLENDS)}")
    if ty == "flash" and tr.get("clear") is not None and tr["clear"] not in CLEARS:
        out.append(f"{w}.clear '{tr['clear']}' is not one of {' | '.join(CLEARS)}")
    if ty == "iris" and tr.get("reveal") is not None and tr["reveal"] not in ("next", "open"):
        out.append(f'{w}.reveal must be "next" (the old shot collapses in a circle) or "open"')
    if tr.get("at") is not None and not _at_ok(tr["at"]):
        out.append(f'{w}.at must be "face", "centre" or [x, y]')
    if tr.get("slide") is not None and not isinstance(tr["slide"], bool):
        out.append(f"{w}.slide must be true or false")
    return out


def check(tl: dict, style: dict | None) -> list[str]:
    """The same list as transitions.js check(TL, T) (T.camera_presets from the style)."""
    out: list[str] = []
    for i, tr in enumerate(tl.get("transitions") or []):
        out += check_transition(tr, i)
    if tl.get("blur") is not None:
        if not isinstance(tl["blur"], list):
            out.append("timeline.blur must be a list [{t, kind, px | amount, frames, ...}]")
        else:
            for i, b in enumerate(tl["blur"]):
                if not (isinstance(b, dict) and _num(b.get("t"))):
                    out.append(f"timeline.blur[{i}] needs t (edit seconds)")
                out += check_env(b, f"timeline.blur[{i}]")
    for i, c in enumerate(tl.get("camera") or []):
        if not isinstance(c, dict):
            continue
        b = c.get("blur") if c.get("blur") is not None else (c.get("p") or {}).get("blur")
        if b is not None:
            out += check_env(b, f"timeline.camera[{i}].blur")
    for pid, spec in ((style or {}).get("camera_presets") or {}).items():
        if isinstance(spec, dict) and spec.get("blur") is not None:
            out += check_env(spec["blur"], f"camera_presets.{pid}.blur")
    for i, g in enumerate(tl.get("grades") or []):
        if not isinstance(g, dict):
            continue
        if g.get("blur") is not None and not (_num(g["blur"]) and 0 <= g["blur"] <= 60):
            out.append(f"timeline.grades[{i}].blur must be px 0..60")
        if g.get("frame") is not None and not isinstance(g["frame"], bool):
            out.append(f"timeline.grades[{i}].frame must be true or false")
    ef = tl.get("end_fade")
    if ef is not None:
        fr = ef if _num(ef) else (ef.get("frames") if isinstance(ef, dict) else None)
        if not (_num(fr) and int(fr) == fr and 1 <= fr <= 300):
            out.append("timeline.end_fade must be frames 1..300 (or {frames, colour})")
        if isinstance(ef, dict) and ef.get("colour") is not None and not isinstance(ef["colour"], str):
            out.append("timeline.end_fade.colour must be a hex colour or a role")
    return out


def uses_fx(tl: dict, style: dict | None = None) -> bool:
    """True when the timeline (or the style's camera presets) uses any Package A field."""
    if any(isinstance(tr, dict) and tr.get("type") is not None for tr in tl.get("transitions") or []):
        return True
    if tl.get("blur") is not None or tl.get("end_fade") is not None:
        return True
    if any(isinstance(g, dict) and (g.get("blur") is not None or g.get("frame") is not None) for g in tl.get("grades") or []):
        return True
    cams = [c for c in tl.get("camera") or [] if isinstance(c, dict)]
    if any(c.get("blur") is not None or (c.get("p") or {}).get("blur") is not None for c in cams):
        return True
    presets = (style or {}).get("camera_presets") or {}
    return any(isinstance(presets.get(c.get("preset")), dict) and presets[c.get("preset")].get("blur") is not None for c in cams)


def windows(tl: dict) -> list[dict]:
    """Built-in transitions as frame windows {i, type, c, a, b} (b exclusive), like transitions.js compile()."""
    out = []
    for i, tr in enumerate(tl.get("transitions") or []):
        if not (isinstance(tr, dict) and tr.get("type") in TYPES and _num(tr.get("t"))):
            continue
        frames, pre0 = TYPES[tr["type"]]
        frames = int(round(tr["frames"])) if _num(tr.get("frames")) else frames
        pre = int(round(min(max(tr["pre"] if _num(tr.get("pre")) else min(pre0, frames), 0), frames)))
        c = _fr(tr["t"])
        out.append({"i": i, "type": tr["type"], "t": float(tr["t"]), "c": c, "a": c - pre, "b": c - pre + frames, "p": tr})
    return sorted(out, key=lambda x: x["a"])


def rule_fx(c) -> list[dict]:
    """V-FX over the validate Ctx (c.tl, c.style, c.beat_id)."""
    tl, style = c.tl, c.style
    out = []
    probs = check(tl, style)
    for m in probs:
        out.append(fail("V-FX", None, 0, m, "fix the field (renderer/SCENES-API.md section 4c lists every field and its range)"))
    ws = windows(tl)
    for x, y in zip(ws, ws[1:]):
        if y["a"] < x["b"]:
            out.append(advice(fail("V-FX", c.beat_id(y["t"]), y["t"],
                            f"built-in transitions {x['type']} at {x['t']:.2f} s and {y['type']} at {y['t']:.2f} s overlap "
                            f"(frames {x['a']}-{x['b'] - 1} and {y['a']}-{y['b'] - 1})",
                            "consider moving one of them, or shortening its `frames`")))
    return out
