"""Canvas camera (E-14, structure §21): the Python mirror of renderer/canvascam.js, and the V-CANVAS rule.

The renderer moves the graphics world (scenes z1-6 by their `parallax`) with `timeline.canvas_camera`; captions, z7+
and `behind` scenes never move. This module computes exactly the same camera per frame (same moves, same easing
curves, same rounding) so the validator can check what is actually drawn:

* ``rule_v_canvas(c, params=None)``: V-CANVAS. Self-contained rule ``(validate.Ctx) -> [failure]``; the foundation's
  V-rule registry can register it as is (its params default to ``PARAMS``; a playbook may set ``canvas_camera`` in
  tokens.json to override them). Checks: known moves, duration and easing, move spacing (G3: never two camera moves
  within 0.4 s), camera speed, and text size after camera scale against its text-class floor.
* ``uncam_rect(c, scene, n, rect)``: maps a measured screen rect back to the scene's own (camera-free) space, so the
  global smooth-motion check G3 judges what the scene does, not what the camera does (the camera has V-CANVAS).
"""
from __future__ import annotations

import math
from typing import Any

W, H, FPS = 1080, 1920, 30
CX, CY = W / 2, H / 2

# ------------------------------------------------------------------ easing (identical to canvascam.js)


def _cl(x: float, a: float = 0.0, b: float = 1.0) -> float:
    return a if x < a else b if x > b else x


def _bez(x1: float, y1: float, x2: float, y2: float):
    def f(x: float) -> float:
        if x <= 0:
            return 0.0
        if x >= 1:
            return 1.0
        t = x
        for _ in range(12):
            u = 1 - t
            fx = 3 * x1 * t * u * u + 3 * x2 * t * t * u + t * t * t - x
            if abs(fx) < 1e-9:
                break
            d = 3 * x1 * u * u + 6 * (x2 - x1) * t * u + 3 * (1 - x2) * t * t
            if abs(d) < 1e-9:
                break
            t = _cl(t - fx / d)
        u = 1 - t
        return 3 * y1 * t * u * u + 3 * y2 * t * t * u + t * t * t
    return f


def _expo_in_out(x: float) -> float:
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    return 2 ** (20 * x - 10) / 2 if x < 0.5 else (2 - 2 ** (10 - 20 * x)) / 2


def _expo_out(x: float) -> float:
    return 0.0 if x <= 0 else 1.0 if x >= 1 else 1 - 2 ** (-10 * x)


EASE = {"inOut": _bez(0.65, 0, 0.35, 1), "out": _bez(0.25, 0.46, 0.45, 0.94), "in": _bez(0.55, 0.055, 0.675, 0.19),
        "sine": _bez(0.37, 0, 0.63, 1), "linear": lambda x: _cl(x),
        # camera v2: exponential curves (snap push, expo settle)
        "expoInOut": _expo_in_out, "expoOut": _expo_out}
MOVES = {
    "C-1": ("C-1", "push"), "push": ("C-1", "push"), "zoom-in": ("C-1", "push"),
    "C-2": ("C-2", "pull"), "pull": ("C-2", "pull"), "zoom-out": ("C-2", "pull"), "settle": ("C-2", "settle"),
    "C-3": ("C-3", "pan"), "pan": ("C-3", "pan"), "drift": ("C-3", "drift"), "dolly": ("C-3", "dolly"),
    "C-4": ("C-4", "zoom-through"), "zoom-through": ("C-4", "zoom-through"),
    "C-5": ("C-5", "orbit"), "orbit": ("C-5", "orbit"),
}
DEF = {"push": (0.8, "inOut"), "pull": (0.7, "inOut"), "settle": (0.6, "out"), "pan": (0.8, "inOut"),
       "dolly": (1.0, "inOut"), "drift": (3.0, "sine"), "zoom-through": (0.8, "in"), "orbit": (2.0, "sine")}


def _num(v, default=0.0) -> float:
    try:
        f = float(v)
        return f if math.isfinite(f) else default
    except (TypeError, ValueError):
        return default


def _jround(x: float) -> int:
    """JavaScript Math.round (halves round up), so frame numbers match the renderer."""
    return int(math.floor(x + 0.5))


# ------------------------------------------------------------------ compile + evaluate
def node_map(timeline: dict | None, scenes: list[dict] | None) -> dict:
    out: dict = {}
    for s in scenes or []:
        for nd in (s or {}).get("nodes") or []:
            if isinstance(nd, dict) and nd.get("id") is not None:
                out[str(nd["id"])] = nd
    for k, v in ((timeline or {}).get("canvas_nodes") or {}).items():
        out[str(k)] = v
    return out


def home_of(timeline: dict | None) -> dict:
    h = (timeline or {}).get("canvas_home") or {}
    return {"x": _num(h.get("x"), CX) if h.get("x") is not None else CX,
            "y": _num(h.get("y"), CY) if h.get("y") is not None else CY,
            "s": _num(h.get("s"), 1.0) if h.get("s") is not None else 1.0, "r": 0.0}


def _roll_to(mv: dict) -> float:
    """Camera v2 roll (deg) a move ends on: p.roll (number, or [from, to]) or to.r; 0 otherwise (rolls back level)."""
    p, to = mv.get("p") or {}, mv.get("to")
    if isinstance(p.get("roll"), list):
        return _num(p["roll"][1]) if len(p["roll"]) > 1 else 0.0
    if p.get("roll") is not None:
        return _num(p["roll"])
    if isinstance(to, dict) and to.get("r") is not None:
        return _num(to["r"])
    return 0.0


def _target(mv: dict, st: dict, nodes: dict, home: dict) -> dict:
    to, p = mv.get("to"), mv.get("p") or {}
    kind = mv.get("kind")
    if kind == "settle" or to == "home" or (to is None and kind == "pull" and not p.get("by") and p.get("scale") is None):
        return dict(home)
    x, y, s = st["x"], st["y"], st["s"]
    if isinstance(to, dict):
        if to.get("node") is not None:
            nd = nodes.get(str(to["node"]))
            if nd:
                x0, y0 = _num(nd.get("x")), _num(nd.get("y"))
                x1, y1 = x0 + _num(nd.get("w")), y0 + _num(nd.get("h"))
                for k in to.get("keep") if isinstance(to.get("keep"), list) else []:   # neighbours that must stay in frame
                    kn = nodes.get(str(k))
                    if kn:
                        kx, ky = _num(kn.get("x")), _num(kn.get("y"))
                        x0, y0, x1, y1 = min(x0, kx), min(y0, ky), max(x1, kx + _num(kn.get("w"))), max(y1, ky + _num(kn.get("h")))
                nw, nh = x1 - x0, y1 - y0
                x, y = (x0 + x1) / 2, (y0 + y1) / 2
                fill = _num(to["fill"]) if to.get("fill") is not None else (_num(p["fill"]) if p.get("fill") is not None else 0.7)
                keep = kind in ("pan", "drift") and to.get("fill") is None and p.get("fill") is None
                if to.get("s") is None and not keep:
                    s = fill * min(W / max(nw or 1, 1), H / max(nh or 1, 1))
        if to.get("x") is not None:
            x = _num(to["x"])
        if to.get("y") is not None:
            y = _num(to["y"])
        if to.get("s") is not None:
            s = _num(to["s"])
        if to.get("by"):
            x, y = st["x"] + _num(to["by"].get("x")), st["y"] + _num(to["by"].get("y"))
    if p.get("by") and not (isinstance(to, dict) and to.get("by")):
        x, y = st["x"] + _num(p["by"].get("x")), st["y"] + _num(p["by"].get("y"))
    if p.get("scale") is not None and not (isinstance(to, dict) and to.get("s") is not None) and kind != "zoom-through":
        s = st["s"] * _num(p["scale"], 1.0)
    if (to is None or (isinstance(to, dict) and to.get("s") is None and to.get("node") is None)) and p.get("scale") is None:
        if kind == "push":
            s = st["s"] * 1.5
        if kind == "pull":
            s = st["s"] / 1.5
    return {"x": x, "y": y, "s": max(0.05, s), "r": _roll_to(mv)}


def compile_camera(timeline: dict | None, scenes: list[dict] | None = None) -> dict:
    tl = timeline or {}
    raw = [dict(m, i=i) for i, m in enumerate(tl.get("canvas_camera") or []) if isinstance(m, dict)]
    raw.sort(key=lambda m: (_num(m.get("t")), m["i"]))
    moves = []
    for m in raw:
        code, kind = MOVES.get(str(m.get("move")), (None, None))
        d = DEF.get(kind, (0.8, "inOut"))
        dur = _num(m["dur"], d[0]) if m.get("dur") is not None else d[0]
        t = _num(m.get("t"))
        moves.append({"code": code, "kind": kind, "name": str(m.get("move")), "t": t, "f0": _jround(t * FPS),
                      "F": max(1, _jround(dur * FPS)), "dur": dur, "ease": m.get("ease") or d[1], "to": m.get("to"),
                      "p": m.get("p") or {}, "i": m["i"]})
    return {"moves": moves, "nodes": node_map(tl, scenes), "home": home_of(tl), "active": bool(moves)}


def _lerp(a: float, b: float, p: float) -> float:
    return a + (b - a) * p


def _eval_move(m: dict, n: int) -> dict:
    st, tg, P = m["start"], m["target"], m.get("p") or {}
    q = _cl((n - m["f0"]) / m["F"])
    e = EASE.get(m["ease"], EASE["inOut"])(q)
    kind = m["kind"]
    if kind == "zoom-through":
        if n >= m["f0"] + m["F"]:
            return dict(m["after"])
        k = _num(P.get("scale"), 6.0) if P.get("scale") is not None else 6.0
        return {"x": _lerp(st["x"], tg["x"], e), "y": _lerp(st["y"], tg["y"], e), "s": st["s"] * k ** e, "r": st["r"]}
    if kind == "orbit":
        R = _num(P.get("radius"), 60.0) if P.get("radius") is not None else 60.0
        deg = _num(P.get("deg"), 3.0) if P.get("deg") is not None else 3.0
        a = 2 * math.pi * e
        return {"x": st["x"] + R * math.sin(a), "y": st["y"] + R * 0.5 * (1 - math.cos(a)), "s": st["s"],
                "r": st["r"] + deg * math.sin(a)}
    if kind in ("push", "pull", "settle", "pan", "dolly", "drift"):
        s = math.exp(_lerp(math.log(st["s"]), math.log(tg["s"]), e))
        if kind == "dolly":
            s *= 1 - (_num(P.get("arc"), 0.18) if P.get("arc") is not None else 0.18) * math.sin(math.pi * e)
        return {"x": _lerp(st["x"], tg["x"], e), "y": _lerp(st["y"], tg["y"], e), "s": s, "r": _lerp(st["r"], tg["r"], e)}
    return dict(st)


def state_at(cam: dict, n: int) -> dict:
    """Camera at edit frame n: {x, y, s, r, moving, move (C-code) or None, kind}."""
    prev = None
    for mv in cam["moves"]:
        if n < mv["f0"]:
            break
        start = _eval_move(prev, mv["f0"]) if prev else dict(cam["home"])
        roll = (mv.get("p") or {}).get("roll")
        if isinstance(roll, list) and roll:
            start = dict(start, r=_num(roll[0]))  # roll [from, to]: starts at from
        tg = _target(mv, start, cam["nodes"], cam["home"])
        after = None
        if mv["kind"] == "zoom-through":
            then = (mv.get("p") or {}).get("then")
            after = _target({"kind": "push", "to": then, "p": {}}, start, cam["nodes"], cam["home"]) if then else dict(cam["home"])
        prev = dict(mv, start=start, target=tg, after=after)
    st = _eval_move(prev, n) if prev else dict(cam["home"])
    moving = bool(prev) and n < prev["f0"] + prev["F"] and prev["kind"] is not None
    return {"x": st["x"], "y": st["y"], "s": st["s"], "r": st.get("r", 0.0) or 0.0, "moving": moving,
            "move": prev["code"] if moving else None, "kind": prev["kind"] if moving else None}


def layer(st: dict, k: float, home: dict) -> dict:
    k = _cl(_num(k))
    return {"x": home["x"] + (st["x"] - home["x"]) * k, "y": home["y"] + (st["y"] - home["y"]) * k,
            "s": st["s"] ** k, "r": (st.get("r") or 0.0) * k}


def matrix(v: dict) -> list[float]:
    rad = (v.get("r") or 0.0) * math.pi / 180
    a, b = v["s"] * math.cos(rad), v["s"] * math.sin(rad)
    c, d = -b, a
    return [a, b, c, d, CX - (a * v["x"] + c * v["y"]), CY - (b * v["x"] + d * v["y"])]


def apply(M, x, y):
    return M[0] * x + M[2] * y + M[4], M[1] * x + M[3] * y + M[5]


def invert(M):
    det = (M[0] * M[3] - M[1] * M[2]) or 1e-12
    a, b, c, d = M[3] / det, -M[1] / det, -M[2] / det, M[0] / det
    return [a, b, c, d, -(a * M[4] + c * M[5]), -(b * M[4] + d * M[5])]


def map_rect(M, r) -> tuple[float, float, float, float]:
    pts = [apply(M, r[0], r[1]), apply(M, r[2], r[1]), apply(M, r[2], r[3]), apply(M, r[0], r[3])]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return (min(xs), min(ys), max(xs), max(ys))


def parallax_of(scene: dict | None) -> float:
    """Default parallax: z1 0 (backgrounds are pinned and follow ctx.camera themselves), z2 0.8, z3-6 1; z>=7 and
    `behind` never move. A scene's `parallax` (0..1, or false) overrides it."""
    if not scene or scene.get("behind") or _num(scene.get("z")) >= 7:
        return 0.0
    v = scene.get("parallax")
    if v is False:
        return 0.0
    if isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v):
        return _cl(float(v))
    z = _num(scene.get("z"))
    return 0.0 if z <= 1 else 0.8 if z == 2 else 1.0


# ------------------------------------------------------------------ validator glue
def camera_for(c) -> dict:
    """Compiled camera for a validate.Ctx (cached on the ctx)."""
    cam = getattr(c, "_canvascam", None)
    if cam is None:
        cam = compile_camera(getattr(c, "tl", {}) or {}, getattr(c, "scenes", []) or [])
        try:
            c._canvascam = cam
        except AttributeError:
            pass
    return cam


def uncam_rect(c, scene: dict, n: int, rect):
    """A measured screen rect at frame n mapped back to the scene's own space (identity when the camera is off or the
    scene is pinned). Used by the G3 hook so camera moves are not reported as scene jumps."""
    cam = camera_for(c)
    if not cam["active"]:
        return rect
    k = parallax_of(scene)
    if k <= 0:
        return rect
    M = matrix(layer(state_at(cam, n), k, cam["home"]))
    if abs(M[0] - 1) < 1e-9 and abs(M[1]) < 1e-9 and abs(M[4]) < 1e-9 and abs(M[5]) < 1e-9:
        return rect
    return map_rect(invert(M), rect)


TEXT_FLOORS = {"TC-display": 40, "TC-subtitle": 54, "TC-label": 40, "TC-legal": 22, "TC-decorative": 0}
PARAMS: dict[str, Any] = {
    "min_gap_s": 0.4,          # G3: never two canvas-camera moves within 0.4 s (end of one -> start of the next)
    "min_dur_s": 0.5,          # §21: every move eases over at least 0.5 s
    "min_dur_s_c4": 0.25,      # camera v2: a zoom-through (push-through) may be as short as 0.25 s
    "min_dur_s_snap": 0.25,    # camera v2: a single snap push / pull (`p.snap: true`) too
    "max_scale_step_snap": 0.35,  # ... and may zoom up to 35 % per frame (one isolated accent, never two snaps in a row)
    "max_pan_px_snap": 220,
    "max_roll_deg": 20,        # camera v2 roll (`p.roll`): at most 20 deg off level, 2 deg per frame
    "max_roll_step": 2.0,
    "max_scale_step": 0.12,    # max |ln s| change per frame (12 %); zoom-through may use `max_scale_step_c4`
    "max_scale_step_c4": 0.20,
    "max_pan_px": 110,         # max screen travel of the frame centre per frame (px; G3 lets scenes move 90)
    "min_scale": 0.25, "max_scale": 12.0,
    "text_floors": TEXT_FLOORS,
    "linear_ok": ["drift"],    # kinds that may use linear easing
    "sample_every": 2,         # frames sampled for the text-floor check
}


def _params(c, params: dict | None) -> dict:
    out = dict(PARAMS)
    style = getattr(c, "style", None) or {}
    over = style.get("canvas_camera") if isinstance(style, dict) else None
    if isinstance(over, dict):
        out.update({k: v for k, v in over.items() if k in PARAMS})
    if params:
        out.update(params)
    floors = dict(TEXT_FLOORS)
    floors.update(out.get("text_floors") or {})
    out["text_floors"] = floors
    return out


def _fail(c, t: float, msg: str, fix: str) -> dict:
    beat = c.beat_id(t) if hasattr(c, "beat_id") else None
    return {"rule": "V-CANVAS", "beat": beat, "t": round(float(t), 3), "msg": msg, "fix": fix}


def text_class(scene: dict) -> str:
    tc = scene.get("text_class")
    if isinstance(tc, str) and tc in TEXT_FLOORS:
        return tc
    if scene.get("kind") == "banner":
        return "TC-display"
    return "TC-label"


def rule_v_canvas(c, params: dict | None = None) -> list[dict]:
    """V-CANVAS on a validate.Ctx-like object (needs .tl, .scenes, .frames, .beat_id; .style optional)."""
    P = _params(c, params)
    cam = camera_for(c)
    if not cam["active"]:
        return []
    out: list[dict] = []
    moves = cam["moves"]
    dur_total = getattr(c, "duration", None)
    frames = int(getattr(c, "frames", 0) or 0)
    snap_kinds = ("push", "pull", "zoom-through")
    for m in moves:
        if m["kind"] is None:
            out.append(_fail(c, m["t"], f"canvas camera move '{m['name']}' at {m['t']:.2f} s is not a known move",
                             "use C-1 push, C-2 pull (or settle), C-3 pan / drift / dolly, C-4 zoom-through or C-5 orbit"))
            continue
        snap = m["p"].get("snap")
        if snap is not None and not isinstance(snap, bool):
            out.append(_fail(c, m["t"], f"canvas camera {m['code']} at {m['t']:.2f} s: p.snap must be true or false",
                             "set p.snap to true (a single snap push) or remove it"))
        elif snap and m["kind"] not in snap_kinds:
            out.append(_fail(c, m["t"], f"canvas camera {m['code']} {m['kind']} at {m['t']:.2f} s: only push, pull and "
                             "zoom-through can snap", "remove p.snap"))
        roll = m["p"].get("roll")
        if roll is not None:
            vals = roll if isinstance(roll, list) else [roll]
            if not (all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in vals)
                    and (len(roll) == 2 if isinstance(roll, list) else True)):
                out.append(_fail(c, m["t"], f"canvas camera {m['code']} at {m['t']:.2f} s: p.roll must be degrees or [from, to]",
                                 'e.g. "p": {"roll": -4} or {"roll": [6, 0]}'))
            elif max(abs(float(v)) for v in vals) > P["max_roll_deg"] + 1e-9:
                out.append(_fail(c, m["t"], f"canvas camera {m['code']} at {m['t']:.2f} s rolls {max(abs(float(v)) for v in vals):g} deg; "
                                 f"keep the roll within {P['max_roll_deg']} deg of level", "use a smaller p.roll"))
        if snap is True and m["kind"] in snap_kinds:
            lim_dur = P["min_dur_s_snap"]
        elif m["kind"] == "zoom-through":
            lim_dur = P["min_dur_s_c4"]
        else:
            lim_dur = P["min_dur_s"]
        if m["dur"] < lim_dur - 1e-9:
            out.append(_fail(c, m["t"], f"canvas camera {m['code']} {m['kind']} at {m['t']:.2f} s lasts {m['dur']:.2f} s; "
                             f"camera moves ease over at least {lim_dur} s"
                             + ("" if lim_dur < P["min_dur_s"] else " (a single snap push or a zoom-through may take 0.25 s)"),
                             f"set dur to {lim_dur} s or more"))
        if m["ease"] not in EASE:
            out.append(_fail(c, m["t"], f"canvas camera {m['code']} at {m['t']:.2f} s uses unknown easing '{m['ease']}'",
                             "use inOut, out, in, sine, expoInOut or expoOut"))
        elif m["ease"] == "linear" and m["kind"] not in P["linear_ok"]:
            out.append(_fail(c, m["t"], f"canvas camera {m['code']} {m['kind']} at {m['t']:.2f} s is linear; camera moves are eased",
                             "use ease inOut (or out for a settle)"))
        if dur_total is not None and m["t"] > float(dur_total) + 1e-6:
            out.append(_fail(c, m["t"], f"canvas camera {m['code']} starts at {m['t']:.2f} s, after the reel ends",
                             "remove it or move it inside the reel"))
    for a, b in zip(moves, moves[1:]):
        if a["kind"] is None or b["kind"] is None:
            continue
        if a["p"].get("snap") is True and b["p"].get("snap") is True:
            out.append(_fail(c, b["t"], f"canvas camera {b['code']} at {b['t']:.2f} s snaps right after the snap at {a['t']:.2f} s; "
                             "a snap push is a single accent", "ease one of them over 0.5 s or more (remove p.snap)"))
        end = a["t"] + a["dur"]
        gap = b["t"] - end
        if gap < P["min_gap_s"] - 1e-6:
            what = "starts before the previous move ends" if gap < -1e-6 else f"starts {gap:.2f} s after the previous one ends"
            out.append(_fail(c, b["t"], f"canvas camera {b['code']} {b['kind']} at {b['t']:.2f} s {what} "
                             f"({a['code']} {a['kind']} {a['t']:.2f}-{end:.2f} s); keep {P['min_gap_s']} s between camera moves",
                             f"start it at {end + P['min_gap_s']:.2f} s or later, or shorten the previous move"))
    # speed + scale range, per frame
    last = frames or (max(m["f0"] + m["F"] for m in moves) + 1)
    prev = None
    spd_hit = None
    rng_hit = None
    roll_hit = None
    for n in range(0, last):
        st = state_at(cam, n)
        if not (P["min_scale"] - 1e-9 <= st["s"] <= P["max_scale"] + 1e-9) and rng_hit is None:
            rng_hit = (n, st["s"])
        if prev is not None and st["moving"]:
            step = abs(math.log(st["s"] / prev["s"]))
            pan = math.hypot(st["x"] - prev["x"], st["y"] - prev["y"]) * st["s"]
            act = next((m for m in moves if m["f0"] <= n < m["f0"] + m["F"]), None)
            snap = bool(act) and act["kind"] in snap_kinds and (act["p"].get("snap") is True or (act["kind"] == "zoom-through" and act["dur"] < P["min_dur_s"] - 1e-9))  # a short push-through is a snap
            lim = P["max_scale_step_snap"] if snap else P["max_scale_step_c4"] if st["kind"] == "zoom-through" else P["max_scale_step"]
            lim_pan = P["max_pan_px_snap"] if snap else P["max_pan_px"]
            m_end = act["f0"] + act["F"] if act else None
            if (step > lim + 1e-9 or pan > lim_pan + 1e-9) and spd_hit is None and not (m_end and m_end - n <= 1 and st["kind"] == "zoom-through"):
                spd_hit = (n, step, pan, st, lim)
            roll_cut = bool(act) and act["f0"] == n and isinstance(act["p"].get("roll"), list)  # roll [from, to] starts on a cut
            if abs(st["r"] - prev["r"]) > P["max_roll_step"] + 1e-9 and roll_hit is None and st["kind"] != "orbit" and not roll_cut:
                roll_hit = (n, abs(st["r"] - prev["r"]))
        prev = st
    if rng_hit:
        n, s = rng_hit
        out.append(_fail(c, n / FPS, f"canvas camera zoom {s:.2f}x at {n / FPS:.2f} s is outside {P['min_scale']}-{P['max_scale']}x",
                         "keep the canvas camera between those zooms (lay the canvas out larger or smaller instead)"))
    if roll_hit:
        n, dr = roll_hit
        out.append(_fail(c, n / FPS, f"canvas camera rolls {dr:.1f} deg in one frame at {n / FPS:.2f} s "
                         f"(max {P['max_roll_step']} deg per frame)", "give the move a longer dur or a smaller p.roll"))
    if spd_hit:
        n, step, pan, st, lim = spd_hit
        what = f"zooms {round(100 * (math.exp(step) - 1))}% in one frame" if step > lim \
            else f"travels {int(round(pan))} px in one frame"
        out.append(_fail(c, n / FPS, f"canvas camera {st['move']} {st['kind']} {what} at {n / FPS:.2f} s (too fast to read)",
                         "give the move a longer dur, or a shorter distance / smaller zoom"))
    # text floors after camera scale
    every = max(1, int(P["sample_every"]))
    for s in getattr(c, "scenes", []) or []:
        if not s.get("text"):
            continue
        k = parallax_of(s)
        if k <= 0:
            continue
        cls = text_class(s)
        floor = float(P["text_floors"].get(cls, 40))
        if floor <= 0:
            continue
        px = s.get("text_px")
        if not isinstance(px, (int, float)) or isinstance(px, bool) or px <= 0:
            ws = getattr(c, "warnings", None)
            if isinstance(ws, list):
                ws.append(f"V-CANVAS: scene '{s.get('id')}' moves with the canvas camera but declares no text_px; "
                          "its text size after zoom was not checked (fx factories set it; bespoke scenes add text_px)")
            continue
        f0, f1 = _jround(_num(s.get("t_in")) * FPS), _jround(_num(s.get("t_out")) * FPS)
        worst = None
        for n in range(f0, max(f0 + 1, f1), every):
            sk = layer(state_at(cam, n), k, cam["home"])["s"]
            size = float(px) * sk
            if size < floor - 1e-6 and (worst is None or size < worst[1]):
                worst = (n, size, sk)
        if worst:
            n, size, sk = worst
            out.append(_fail(c, n / FPS, f"'{s.get('id')}' text is {size:.0f} px on screen at {n / FPS:.2f} s "
                             f"({px:g} px x camera {sk:.2f}); {cls} needs at least {floor:g} px",
                             f"make its text at least {math.ceil(floor / max(sk, 1e-6)):d} px, pull the camera out less, "
                             "or pin the label to the screen (parallax: 0) and track the node with ctx.camera.toScreen"))
    return out


def stats(c) -> dict:
    cam = camera_for(c)
    return {"moves": len(cam["moves"]), "codes": sorted({m["code"] for m in cam["moves"] if m["code"]})}
