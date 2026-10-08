"""Small helpers shared by the validator modules (validate, hookrules, cadence, profilecheck, sfxrules).

Kept free of imports from those modules so any of them can import it without a cycle.
"""
from __future__ import annotations

from typing import Any

from .core import FPS

FRAME_W, FRAME_H = 1080, 1920
SUBTITLE_Z = (7, 8)
# Headline devices (structure Definitions "Headline element"); `banner` is the reference playbook's slab.
HEADLINE_KINDS = ("banner", "pill", "lockup", "chip", "plate", "title_card", "headline")


def fr(t: float) -> int:
    return int(round(float(t) * FPS))


def fail(rule, beat, t, msg, fix):
    return {"rule": rule, "beat": beat, "t": round(float(t), 3), "msg": msg, "fix": fix}


def advice(f: dict) -> dict:
    """Mark a finding as advice: reported to the Director, never blocks a reel (validate's two levels)."""
    f["advice"] = True
    return f


def norm_box(b: Any) -> tuple[float, float, float, float] | None:
    """Return (x0, y0, x1, y1) from {x,y,w,h} or [x,y,w,h]."""
    try:
        if isinstance(b, dict):
            x, y, w, h = (float(b[k]) for k in ("x", "y", "w", "h"))
        elif isinstance(b, (list, tuple)) and len(b) >= 4:
            x, y, w, h = (float(v) for v in b[:4])
        else:
            return None
    except (KeyError, TypeError, ValueError):
        return None
    return (x, y, x + w, y + h)


def overlap(a, b) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def expand(b, m):
    return (b[0] - m, b[1] - m, b[2] + m, b[3] + m)


def area(r) -> float:
    return max(0.0, r[2] - r[0]) * max(0.0, r[3] - r[1])


def get_path(d: Any, path: str, default=None):
    """d['a']['b'] for 'a.b'; `default` when any step is missing or not a dict."""
    cur = d
    for k in path.split("."):
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def as_range(v, default=None):
    """[lo, hi] from a 2-list, or (v, None) from a single number; `default` otherwise."""
    if isinstance(v, (list, tuple)) and len(v) == 2 and all(isinstance(x, (int, float)) or x is None for x in v):
        return (v[0], v[1])
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        return (v, None)
    return default


# Entrance / exit windows (V-SAFE, V-TYPE, G1, G3 judge a scene's settled state, not its entrance animation).
# `veos measure` neutralises the enter/exit presets, but a scene's own render() entrance (a slam, a slide, a blur-in)
# is measured as drawn. A scene may declare its windows in LOCAL seconds: `enter_s` (alias `settle_s`) after t_in and
# `exit_s` before t_out; the default is the preset's length (core.js IN_F / OUT_F) and at least ENTER_MIN_F / EXIT_MIN_F.
IN_F = {"settle": 8, "pop": 7, "squash": 6, "rise": 8, "drop": 8, "blur": 6, "stamp": 5, "slide-l": 8, "slide-r": 8,
        "rocket": 10, "none": 0}
OUT_F = {"rocket": 8, "none": 0}
ENTER_MIN_F, EXIT_MIN_F = 6, 4


def _win_f(s: dict, keys, preset_f: int, floor: int) -> int:
    for k in keys:
        v = s.get(k)
        if isinstance(v, (int, float)) and not isinstance(v, bool) and v >= 0:
            return int(round(float(v) * FPS))
    return max(preset_f, floor)


def _frames_field(s: dict, key: str):
    v = s.get(key)
    return int(v) if isinstance(v, (int, float)) and not isinstance(v, bool) and v >= 0 else None


def enter_frames(s: dict) -> int:
    pf = _frames_field(s, "in_frames")  # fx-helpers: a per-scene preset length replaces core.js IN_F
    return _win_f(s, ("enter_s", "settle_s"), pf if pf is not None else IN_F.get(str(s.get("in") or "settle"), 8), ENTER_MIN_F)


def exit_frames(s: dict) -> int:
    pf = _frames_field(s, "out_frames")
    return _win_f(s, ("exit_s",), pf if pf is not None else OUT_F.get(str(s.get("out") or "none"), 5), EXIT_MIN_F)


def step_of(s: dict) -> float:
    """Frames per drawn pose of a stepped scene (core.js stepN): `step_frames` (2 = on twos), else 30 / `step_fps`
    (12 fps -> 2.5: poses held 2 and 3 frames), else 1 (every frame drawn)."""
    k = s.get("step_frames")
    if isinstance(k, (int, float)) and not isinstance(k, bool) and k >= 1:
        return float(int(k))
    f = s.get("step_fps")
    if isinstance(f, (int, float)) and not isinstance(f, bool) and 0 < f <= FPS:
        return FPS / float(f)
    return 1.0


def settled_at(s: dict, n: int) -> bool:
    """Frame n is in the scene's settled hold (past its entrance window, before its exit window). A scene too short to
    have a settled hold counts as settled throughout (there is nothing else to judge)."""
    fin, fout = fr(s.get("t_in", 0)), fr(s.get("t_out", 0))
    a, b = fin + enter_frames(s), fout - exit_frames(s)
    if b <= a:
        return True
    return a <= n < b
