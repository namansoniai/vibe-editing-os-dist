"""Per-reel base reframe from a template's framing tokens (E-16b, audit A22: "the presenter sits too low").

Templates declare where the face should sit on a full 1080x1920 stage in `footage.setups[].framing`:
`head_top_y`, `chin_y`, `eye_y` / `eyes_y` (screen px ranges), `face_cx` / `face_x`, `face_h_ratio` / `face_h_frac`
(face height / frame height), `head_top_frac` / `face_cx_frac` (fractions of the frame), and optionally
`punch_in: [min, max]` (the base punch-in a wide take usually needs; only its max caps the scale here).

From the reel's face boxes (median over the reel) this module picks ONE base crop for the whole reel: a scale
`s` in [1, cap] (cap = 2.0 upscale, or `punch_in` max, or `footage.base_reframe.max_up`) and offsets `tx, ty` (screen =
s * footage + t; the footage always covers the frame) so the face lands in the declared ranges with the least punch-in.
Without a size range (chin / face height) only "too low" is corrected: the solver never zooms in just to push a head
down. The renderer applies it to the `full` and `low` stages (footage and cut-out together); the caption engine and the
validator move the face boxes the same way (`apply_boxes`), so chest captions, avoid_face and V-FACE agree with the
picture. Per reel: `timeline.framing` = "off" | {"setup": "B"} | explicit ranges (merged over the setup's framing);
`timeline.meta.setup` also picks the setup. Multi-camera reels (`timeline.shots`) are never reframed here.

Which setup (when the reel names none): the footage is classified from its face boxes (`footage_kind`): a face taller
than CLOSE_SEL of the frame is a close selfie, anything smaller a tripod / desk take. Setups whose `desc` says selfie /
handheld / arm's length are selfie setups; tripod / locked-off / static / seated / desk ones are tripod setups. The first
setup of the footage's kind wins (a tripod take never gets the selfie setup A just because it is listed first); with no
match, the first setup with framing ranges. A setup whose desc names formats (F-A, F-B) is only used for those formats.

Never enlarge an already-close face: the base reframe can only punch in, so a face already CLOSE of the frame height
(or more) is left as shot (`close: true`, identity), and an unsized spec never punches a face past CLOSE.
"""
from __future__ import annotations

import re
import statistics

W, H = 1080, 1920
HEAD_UP = 0.35   # head top = face box y - 0.35 * h (context.HEAD_UP)
EYE_K = 0.38     # eye line = y + 0.38 * h
MAX_UP = 2.0
STEP = 0.01
INNER = 0.1      # target the inner 80 % of each declared range
CLOSE = 0.30     # face box height / frame height at which a face is already close: never punch in further
CLOSE_SEL = 0.20  # face height fraction above which the footage reads as an arm's-length selfie (setup choice only)
SELFIE_WORDS = ("selfie", "handheld", "hand-held", "arm's length", "arm’s length", "front camera", "gimbal")
TRIPOD_WORDS = ("tripod", "locked-off", "locked off", "static", "fixed camera", "seated", "desk", "webcam")
KEYS = ("head_top_y", "chin_y", "eye_y", "eyes_y", "face_cx", "face_x", "face_h_ratio", "face_h_frac",
        "head_top_frac", "face_cx_frac")


def _rng(v):
    if isinstance(v, (list, tuple)) and len(v) == 2 and all(isinstance(x, (int, float)) for x in v):
        a, b = float(v[0]), float(v[1])
        return (min(a, b), max(a, b))
    return None


def setup_kind(setup: dict) -> str | None:
    """'selfie' | 'tripod' | None from a footage setup's description."""
    d = str((setup or {}).get("desc") or "").lower()
    sel = any(w in d for w in SELFIE_WORDS)
    tri = any(w in d for w in TRIPOD_WORDS)
    if sel and not tri:
        return "selfie"
    if tri and not sel:
        return "tripod"
    if sel and tri:  # "selfie ... seated": whichever comes first in the description
        i = min(d.find(w) for w in SELFIE_WORDS if w in d)
        j = min(d.find(w) for w in TRIPOD_WORDS if w in d)
        return "selfie" if i < j else "tripod"
    return None


def footage_kind(boxes) -> str | None:
    """'selfie' (a close, arm's-length face) | 'tripod' (a smaller, set-up take) | None (no faces)."""
    med = face_median(boxes)
    if not med:
        return None
    return "selfie" if med[3] / H >= CLOSE_SEL else "tripod"


def _formats_of(setup: dict) -> set:
    return set(re.findall(r"\bF-[A-Z]\b", str((setup or {}).get("desc") or "")))


def pick_setup(setups: list, tl: dict, boxes=None) -> dict | None:
    """The default setup for a reel that names none (module doc: footage kind, formats)."""
    cands = [s for s in setups if isinstance(s.get("framing"), dict) and any(_rng(s["framing"].get(k)) for k in KEYS)]
    if not cands:
        return None
    fmt = str((tl.get("meta") or {}).get("format") or "")
    if fmt:
        fit = [s for s in cands if not _formats_of(s) or fmt in _formats_of(s)]
        cands = fit or cands
    kind = footage_kind(boxes)
    if kind:
        same = [s for s in cands if setup_kind(s) == kind]
        if same:
            return same[0]
        other = "tripod" if kind == "selfie" else "selfie"
        neutral = [s for s in cands if setup_kind(s) != other]
        if neutral:
            return neutral[0]
    return cands[0]


def spec_for(tokens: dict | None, tl: dict | None, boxes=None) -> dict | None:
    """The framing ranges this reel should follow (screen px), or None (no framing / turned off / multi-camera).
    `boxes` (the reel's face boxes) pick the default setup by footage kind."""
    tl = tl or {}
    tokens = tokens or {}
    fr = tl.get("framing")
    if fr is False or fr in ("off", "none") or (isinstance(fr, dict) and (fr.get("off") or fr.get("enabled") is False)):
        return None
    if tl.get("shots"):
        return None
    foot = tokens.get("footage") or {}
    br = foot.get("base_reframe") if isinstance(foot.get("base_reframe"), dict) else {}
    if br.get("enabled") is False and not isinstance(fr, dict):
        return None
    setups = [s for s in (foot.get("setups") or []) if isinstance(s, dict)]
    want = (fr.get("setup") if isinstance(fr, dict) else None) or (tl.get("meta") or {}).get("setup")
    pick = None
    if want:
        pick = next((s for s in setups if str(s.get("id")) == str(want)), None)
    if pick is None:
        pick = pick_setup(setups, tl, boxes)
    raw = dict((pick or {}).get("framing") or {})
    if isinstance(fr, dict):
        raw.update({k: v for k, v in fr.items() if k not in ("setup", "off", "enabled")})
    out = {}
    for k, scale in (("head_top_y", 1), ("chin_y", 1), ("eye_y", 1), ("eyes_y", 1), ("face_cx", 1), ("head_top_frac", H),
                     ("face_cx_frac", W)):
        r = _rng(raw.get(k))
        if r:
            key = {"eyes_y": "eye_y", "head_top_frac": "head_top_y", "face_cx_frac": "face_cx"}.get(k, k)
            out.setdefault(key, (r[0] * scale, r[1] * scale))
    fx = _rng(raw.get("face_x"))
    if fx and "face_cx" not in out:
        out["face_cx"] = ((fx[0] + fx[1]) / 2 - 40, (fx[0] + fx[1]) / 2 + 40)
    for k in ("face_h_ratio", "face_h_frac"):
        r = _rng(raw.get(k))
        if r and "face_h" not in out:
            out["face_h"] = (r[0] * H, r[1] * H)
    if not out:
        return None
    cap = MAX_UP
    pi = _rng(raw.get("punch_in")) or _rng(br.get("punch_in"))
    if pi:
        cap = min(cap, max(1.0, pi[1]))
    if isinstance(br.get("max_up"), (int, float)):
        cap = min(cap, max(1.0, float(br["max_up"])))
    out["cap"] = cap
    out["setup"] = (pick or {}).get("id")
    return out


def face_median(boxes) -> tuple | None:
    bs = [b for b in (boxes or []) if b and len(b) >= 4 and b[2] > 0 and b[3] > 0]
    if not bs:
        return None
    return tuple(float(statistics.median(b[k] for b in bs)) for k in range(4))


def _features(box):
    x, y, w, h = box
    return {"head_top_y": y - HEAD_UP * h, "chin_y": y + h, "eye_y": y + EYE_K * h, "face_cx": x + w / 2, "face_h": h}


def _dist(v, r):
    return r[0] - v if v < r[0] else (v - r[1] if v > r[1] else 0.0)


def _best_t(vals: list[tuple[float, tuple, bool]], s: float, size: float, low_only: bool):
    """1-D: offset t in [size * (1 - s), 0] minimising sum dist(s * v + t, range); `low_only` counts only v' > hi."""
    lo, hi = size * (1 - s), 0.0
    if not vals:
        return None, 0.0
    cands = {lo, hi}
    for v, r, _ in vals:
        cands.update({r[0] - s * v, r[1] - s * v, (r[0] + r[1]) / 2 - s * v})
    best = None
    for t in sorted(cands):
        t = min(hi, max(lo, t))
        cost = 0.0
        for v, r, _ in vals:
            vv = s * v + t
            d = _dist(vv, r)
            if low_only and vv < r[0]:
                d = 0.0
            cost += d
        # prefer the range middles among equal costs (stable, centred placement)
        mid = sum(abs(s * v + t - (r[0] + r[1]) / 2) for v, r, _ in vals) * 1e-4
        key = (round(cost, 3), mid)
        if best is None or key < best[0]:
            best = (key, t, cost)
    return best[1], best[2]


def solve(box, spec: dict) -> dict:
    """Base reframe for a median face box [x, y, w, h] (footage px = screen px at s=1)."""
    f = _features(box)
    sized = "face_h" in spec or ("chin_y" in spec and ("head_top_y" in spec or "eye_y" in spec))
    if box[3] >= CLOSE * H:  # already a close face: punching in only makes it bigger (and a pull-out is impossible)
        f0 = _features(box)
        return {"s": 1.0, "tx": 0.0, "ty": 0.0, "residual_px": 0.0, "capped": False, "cap": float(spec.get("cap", MAX_UP)),
                "close": True, "before": {k: round(v, 1) for k, v in f0.items()},
                "face": {"x": round(box[0], 1), "y": round(box[1], 1), "w": round(box[2], 1), "h": round(box[3], 1),
                         "cx": round(f0["face_cx"], 1), "cy": round(box[1] + box[3] / 2, 1), "head_top": round(f0["head_top_y"], 1),
                         "eye": round(f0["eye_y"], 1), "chin": round(f0["chin_y"], 1)}}
    # aim inside the inner 80 % of each range: the median face sits clear of the edges, so per-frame motion stays in range
    inner = {k: (r[0] + INNER * (r[1] - r[0]), r[1] - INNER * (r[1] - r[0])) for k, r in spec.items() if isinstance(r, tuple)}
    vy = [(f[k], inner[k], True) for k in ("head_top_y", "eye_y", "chin_y") if k in spec]
    vx = [(f["face_cx"], inner["face_cx"], True)] if "face_cx" in spec else []
    cap = float(spec.get("cap", MAX_UP))
    if not sized:  # an unsized spec never punches a face past CLOSE of the frame height
        cap = max(1.0, min(cap, CLOSE * H / max(box[3], 1.0)))
    best = None
    n = int(round((cap - 1.0) / STEP))
    for i in range(n + 1):
        s = 1.0 + i * STEP
        ty, cy = _best_t(vy, s, H, low_only=not sized)
        tx, cx = _best_t(vx, s, W, low_only=False)
        cost = cy + cx
        if "face_h" in spec:
            cost += _dist(s * f["face_h"], inner["face_h"])
        if best is None or cost < best[0] - 0.5:
            best = (cost, s, tx, ty)
    cost, s, tx, ty = best
    if ty is None:   # no vertical range: keep the face's height on screen while scaling about it
        ty = min(0.0, max(H * (1 - s), (box[1] + box[3] / 2) * (1 - s)))
    if tx is None:   # no horizontal range: zoom about the face centre
        tx = min(0.0, max(W * (1 - s), f["face_cx"] * (1 - s)))
    x, y, w, h = box
    sx, sy = s * x + tx, s * y + ty
    after = {"x": round(sx, 1), "y": round(sy, 1), "w": round(s * w, 1), "h": round(s * h, 1),
             "cx": round(sx + s * w / 2, 1), "cy": round(sy + s * h / 2, 1), "head_top": round(sy - HEAD_UP * s * h, 1),
             "eye": round(sy + EYE_K * s * h, 1), "chin": round(sy + s * h, 1)}
    return {"s": round(s, 3), "tx": round(tx, 2), "ty": round(ty, 2), "residual_px": round(cost, 1),
            "capped": bool(cost > 0.5 and s >= cap - 1e-6), "cap": cap,
            "before": {k: round(v, 1) for k, v in f.items()}, "face": after}


def for_reel(tokens: dict | None, tl: dict | None, boxes) -> dict | None:
    """The bundle's `framing` record, or None when nothing should move (no ranges, no faces, already in range)."""
    spec = spec_for(tokens, tl, boxes)
    if not spec:
        return None
    med = face_median(boxes)
    if not med:
        return None
    r = solve(med, spec)
    r["setup"] = spec.get("setup")
    r["ranges"] = {k: list(v) for k, v in spec.items() if isinstance(v, tuple)}
    if r["s"] == 1.0 and abs(r["tx"]) < 0.5 and abs(r["ty"]) < 0.5:
        r["identity"] = True
    return r


def apply_box(b, rf: dict | None):
    if not b or not rf or rf.get("identity"):
        return b
    s, tx, ty = rf["s"], rf["tx"], rf["ty"]
    return [s * b[0] + tx, s * b[1] + ty, s * b[2], s * b[3], *b[4:]]


def apply_boxes(boxes, rf: dict | None):
    """Face boxes as they appear on a full stage after the base reframe (None entries kept)."""
    if not boxes or not rf or rf.get("identity"):
        return boxes
    return [apply_box(b, rf) if b else b for b in boxes]


def for_project(pr, tl: dict | None, boxes) -> dict | None:
    """framing record from the project's work/tokens.json (None when missing)."""
    from .core import read_json
    tp = pr.work / "tokens.json"
    if not tp.exists():
        return None
    try:
        return for_reel(read_json(tp), tl, boxes)
    except (ValueError, OSError):
        return None
