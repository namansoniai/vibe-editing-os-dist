"""Track anchors (Package E): plan/tracks/*.json for the bundle, the anchor maths (mirrors renderer/tracks.js) and V-ANCHOR.

A scene follows a track with `anchor: {track, offset: [dx, dy], point, scale_with, smooth, lost, fade, min_conf, max_lost,
clip_t0, speed, place}` (SCENES-API section 13). Core translates the scene so the centre of its declared `box` lands on
the track point (+ offset) and, with `scale_with`, scales it about that centre by the object's size change since the
scene's first frame. The renderer applies the live footage->screen transform (stage layout, camera presets) to edit-space
tracks; this module predicts the rect on a full stage at rest (what the track file stores), which is what V-ANCHOR judges.

V-ANCHOR (runs whenever a scene declares `anchor`):
  * the anchor is well formed, the scene has a `box`, the track file exists and is a version-1 track;
  * the track covers every frame of the scene span (edit tracks: edit frames; clip tracks: the clip frames the scene plays);
  * confidence (advice): at most `max_lost` (default 0.2) of the span is lost (conf < min_conf), and a `lost: "hold"`
    anchor never holds still for more than HOLD_MAX frames while the object is lost (use `lost: "fade"` or track again);
  * NC-1: an anchored overlay never covers the face itself (no clearance margin), on full / low stages, every other
    frame.
"""
from __future__ import annotations

import math
from pathlib import Path

from .core import FPS, read_json
from .vcommon import advice, expand, fail, fr, overlap  # noqa: F401 (expand re-exported)

POINTS = ("center", "top", "bottom", "left", "right")
LOSTS = ("hold", "fade")
SMOOTH = 2          # default half-window (frames) of the anchor's moving average
FADE = 6            # frames to fade out / in around lost frames (lost: "fade")
MAX_LOST = 0.2
HOLD_MAX = 15       # frames a "hold" anchor may sit still on a lost object (0.5 s)
SCALE_LIM = (0.25, 4.0)


def _num(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def anchor_errors(a) -> list[str]:
    """Shape problems of a scene's `anchor` (same checks as VEOS.scene in core.js)."""
    if not isinstance(a, dict):
        return ["anchor must be an object {track, offset, ...}"]
    e = []
    if not isinstance(a.get("track"), str) or not a.get("track"):
        e.append("anchor.track must be a track id (plan/tracks/<id>.json)")
    off = a.get("offset")
    if off is not None and not (isinstance(off, (list, tuple)) and len(off) == 2 and all(_num(v) for v in off)):
        e.append("anchor.offset must be [dx, dy] px")
    if a.get("point") is not None and a.get("point") not in POINTS:
        e.append(f"anchor.point must be one of {'|'.join(POINTS)}")
    if a.get("lost") is not None and a.get("lost") not in LOSTS:
        e.append("anchor.lost must be hold | fade")
    for k, lo, hi in (("smooth", 0, 15), ("fade", 1, 30)):
        v = a.get(k)
        if v is not None and not (_num(v) and lo <= v <= hi and int(v) == v):
            e.append(f"anchor.{k} must be an integer {lo}..{hi} (frames)")
    for k in ("min_conf", "max_lost"):
        v = a.get(k)
        if v is not None and not (_num(v) and 0 <= v <= 1):
            e.append(f"anchor.{k} must be a number 0..1")
    if a.get("scale_with") is not None and not isinstance(a.get("scale_with"), bool):
        e.append("anchor.scale_with must be true or false")
    if a.get("clip_t0") is not None and not (_num(a["clip_t0"]) and a["clip_t0"] >= 0):
        e.append("anchor.clip_t0 must be clip seconds >= 0")
    if a.get("speed") is not None and not (_num(a["speed"]) and a["speed"] > 0):
        e.append("anchor.speed must be > 0")
    pl = a.get("place")
    if pl is not None and not (isinstance(pl, dict) and all(_num(pl.get(k)) for k in ("x", "y", "w")) and pl["w"] > 0):
        e.append("anchor.place must be {x, y, w}: where the clip is drawn on screen (left, top, width px)")
    return e


# ------------------------------------------------------------------------------------------------ loading
def track_path(pr, tid: str) -> Path:
    return pr.root / "plan" / "tracks" / f"{tid}.json"


def load_track(pr, tid: str) -> dict | None:
    p = track_path(pr, tid)
    if not p.exists():
        return None
    try:
        t = read_json(p)
    except (ValueError, OSError):
        return None
    return t if isinstance(t, dict) and t.get("version") == 1 and isinstance(t.get("frames"), list) else None


def for_bundle(pr, warnings: list | None = None) -> dict:
    """Every plan/tracks/*.json, compacted for renderer/tracks.js: {id: {space, mode, size, f0, n, x, y, w, h, c, lost}}.
    Edit tracks are given in FOOTAGE px (the base reframe the file was written with is undone), so the renderer maps them
    through the live footage->screen transform exactly like the face boxes."""
    out = {}
    d = pr.root / "plan" / "tracks"
    if not d.is_dir():
        return out
    for p in sorted(d.glob("*.json")):
        t = load_track(pr, p.stem)
        if not t or not t["frames"]:
            if warnings is not None:
                warnings.append(f"plan/tracks/{p.name} is not a version-1 track; ignored")
            continue
        fr_ = sorted(t["frames"], key=lambda r: r["f"])
        f0, f1 = fr_[0]["f"], fr_[-1]["f"]
        n = f1 - f0 + 1
        rf = t.get("reframe") if t.get("space") == "edit" else None
        s, tx, ty = (rf["s"], rf["tx"], rf["ty"]) if rf else (1.0, 0.0, 0.0)
        arr = {k: [None] * n for k in ("x", "y", "w", "h", "c", "lost")}
        for r in fr_:
            i = r["f"] - f0
            arr["x"][i] = round((r["x"] - tx) / s, 1)
            arr["y"][i] = round((r["y"] - ty) / s, 1)
            arr["w"][i] = round(r["w"] / s, 1)
            arr["h"][i] = round(r["h"] / s, 1)
            arr["c"][i] = r.get("conf", 1.0)
            arr["lost"][i] = 1 if r.get("lost") else 0
        for i in range(n):  # holes (frames of another source): lost
            if arr["x"][i] is None:
                for k in ("x", "y", "w", "h"):
                    arr[k][i] = 0
                arr["c"][i], arr["lost"][i] = 0, 1
        out[t.get("id") or p.stem] = {"space": t.get("space", "edit"), "mode": t.get("mode", "box"), "size": t.get("size") or [1080, 1920],
                                      "min_conf": t.get("min_conf", 0.5), "f0": f0, "n": n, **arr}
    return out


# ------------------------------------------------------------------------------------------------ anchor maths (= tracks.js)
def _good(T: dict, i: int, min_conf: float) -> bool:
    return 0 <= i < T["n"] and not T["lost"][i] and (T["c"][i] or 0) >= min_conf


def sample(T: dict, f: int, smooth: int = SMOOTH, min_conf: float | None = None) -> dict | None:
    """The track at frame f: centred moving average over confident frames within +-smooth; on a lost frame the nearest
    confident one before it (else after it). {x, y, w, h, conf, lost, gap} (gap = frames to the nearest confident frame)."""
    mc = T.get("min_conf", 0.5) if min_conf is None else min_conf
    i = f - T["f0"]
    if T["n"] <= 0:
        return None
    ic = min(max(i, 0), T["n"] - 1)
    lost = not _good(T, i, mc)
    gap = 0
    if lost:
        j = next((k for d in range(1, T["n"] + 1) for k in (ic - d, ic + d) if _good(T, k, mc)), None)
        if j is None:
            return None
        back = next((ic - d for d in range(0, T["n"]) if _good(T, ic - d, mc)), None)
        gap = abs(j - ic)
        ic = back if back is not None else j
    acc, c = [0.0, 0.0, 0.0, 0.0], 0
    for k in range(ic - smooth, ic + smooth + 1):
        if _good(T, k, mc):
            for q, key in enumerate(("x", "y", "w", "h")):
                acc[q] += T[key][k]
            c += 1
    if not c:
        return None
    x, y, w, h = (v / c for v in acc)
    return {"x": x, "y": y, "w": w, "h": h, "conf": T["c"][min(max(i, 0), T["n"] - 1)] or 0, "lost": lost or not (0 <= i < T["n"]), "gap": gap}


def point_of(sm: dict, point: str = "center") -> tuple[float, float]:
    x, y, w, h = sm["x"], sm["y"], sm["w"], sm["h"]
    return {"center": (x + w / 2, y + h / 2), "top": (x + w / 2, y), "bottom": (x + w / 2, y + h),
            "left": (x, y + h / 2), "right": (x + w, y + h / 2)}.get(point or "center", (x + w / 2, y + h / 2))


def track_frame(a: dict, T: dict, fin: int, n: int) -> int:
    """The track frame a scene shows at edit frame n (edit tracks: n; clip tracks: clip_t0 + lt * speed)."""
    if T.get("space") == "clip":
        return int(round(((a.get("clip_t0") or 0) + (n - fin) / FPS * (a.get("speed") or 1)) * FPS))
    return n


def predicted_rect(scene: dict, T: dict, n: int, reframe: dict | None = None) -> tuple | None:
    """The anchored scene's box on screen at frame n on a full stage at rest (footage px -> + base reframe), or None."""
    a, b = scene.get("anchor") or {}, scene.get("box")
    if not b:
        return None
    fin = fr(scene.get("t_in", 0))
    sm = sample(T, track_frame(a, T, fin, n), int(a.get("smooth", SMOOTH)), a.get("min_conf"))
    if sm is None:
        return None
    px, py = point_of(sm, a.get("point"))
    k = 1.0
    if T.get("space") == "clip":
        pl = a.get("place") or {"x": 0, "y": 0, "w": T["size"][0]}
        k = pl["w"] / T["size"][0]
        px, py = pl["x"] + px * k, pl["y"] + py * k
    elif reframe:
        px, py, k = reframe["s"] * px + reframe["tx"], reframe["s"] * py + reframe["ty"], reframe["s"]
    s = 1.0
    if a.get("scale_with") and T.get("mode") != "point":
        ref = sample(T, track_frame(a, T, fin, fin), int(a.get("smooth", SMOOTH)), a.get("min_conf"))
        if ref and ref["w"] > 0 and ref["h"] > 0 and sm["w"] > 0 and sm["h"] > 0:
            s = min(SCALE_LIM[1], max(SCALE_LIM[0], math.sqrt(sm["w"] * sm["h"] / (ref["w"] * ref["h"]))))
    dx, dy = (a.get("offset") or [0, 0])
    cx, cy = px + dx * s, py + dy * s
    w, h = b["w"] * s, b["h"] * s
    return (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)


# ------------------------------------------------------------------------------------------------ V-ANCHOR
def rule_v_anchor(c) -> list[dict]:
    pr = getattr(c, "project", None)
    out = []
    tracks = None
    for s in c.scenes:
        a = s.get("anchor")
        if not isinstance(a, dict):  # a string anchor ("top") is a text helper's layout option, not a track
            continue
        sid, t_in = s.get("id"), float(s.get("t_in", 0))
        beat = c.beat_id(t_in)
        errs = anchor_errors(a)
        if not s.get("box"):
            errs.append("an anchored scene needs a `box` (its centre is what lands on the track point)")
        if errs:
            out.append(fail("V-ANCHOR", beat, t_in, f"scene {sid}: " + "; ".join(errs), "fix the anchor fields (SCENES-API section 13)"))
            continue
        if tracks is None:
            tracks = for_bundle(pr) if pr else {}
        T = tracks.get(a["track"])
        if not T:
            out.append(fail("V-ANCHOR", beat, t_in, f"scene {sid}: track '{a['track']}' not found (plan/tracks/{a['track']}.json)",
                            f"run `veos track --project P --id {a['track']} --at <t> --box x,y,w,h` for the span the scene is on screen"))
            continue
        if T["space"] == "clip" and a.get("place") is None:
            out.append(fail("V-ANCHOR", beat, t_in, f"scene {sid}: track '{a['track']}' is in clip space but the anchor has no `place`",
                            "add place: {x, y, w} (where the scene draws the clip) and clip_t0 (clip seconds at t_in)"))
            continue
        fin, fout = fr(t_in), fr(s.get("t_out", 0))
        mc = a.get("min_conf", T.get("min_conf", 0.5))
        missing, lost, run, worst = [], 0, 0, 0
        for n in range(fin, fout):
            i = track_frame(a, T, fin, n) - T["f0"]
            if not 0 <= i < T["n"]:
                missing.append(n)
                continue
            if T["lost"][i] or (T["c"][i] or 0) < mc:
                lost += 1
                run += 1
                worst = max(worst, run)
            else:
                run = 0
        span = max(1, fout - fin)
        if missing:
            out.append(fail("V-ANCHOR", beat, missing[0] / FPS,
                            f"scene {sid}: track '{a['track']}' does not cover {len(missing)} of its {span} frames "
                            f"(first uncovered {missing[0] / FPS:.2f} s)",
                            f"track again with --from/--to spanning {t_in:.2f}-{float(s.get('t_out', 0)):.2f} s, or shorten the scene"))
            continue
        ml = a.get("max_lost", MAX_LOST)
        if lost / span > ml:
            out.append(advice(fail("V-ANCHOR", beat, t_in, f"scene {sid}: track '{a['track']}' is lost on {lost} of {span} frames "
                            f"({100 * lost / span:.0f}% > {100 * ml:.0f}%, confidence < {mc})",
                            "track again from a clearer frame (--at where the object is sharp, a tighter --box), or end the scene earlier")))
        elif worst > HOLD_MAX and (a.get("lost") or "hold") == "hold":
            out.append(advice(fail("V-ANCHOR", beat, t_in, f"scene {sid}: holds still for {worst} frames while '{a['track']}' is lost",
                            "set anchor.lost: \"fade\" (the overlay fades out while the object is lost) or track again")))
        elif lost:
            c.warnings.append(f"V-ANCHOR: scene {sid}: {lost} lost frame(s) on track '{a['track']}' ({a.get('lost') or 'hold'})")
        # NC-1: an anchored overlay never covers the face
        if s.get("behind") or c.face is None or T["space"] != "edit" or s.get("z", 0) >= 11:
            continue
        rf = (getattr(c, "framing", None) or None)
        rf = rf if rf and not rf.get("identity") else None
        for n in range(fin, fout, 2):
            if c.stage_engine_at(n / FPS) not in ("full", "low") or n >= len(c.face) or not c.face[n]:
                continue
            fb = c.face[n]
            zone = (fb[0], fb[1], fb[0] + fb[2], fb[1] + fb[3])  # the face itself: no clearance margin
            r = predicted_rect(s, T, n, rf)
            if r and overlap(r, zone):
                out.append(fail("V-ANCHOR", c.beat_id(n / FPS), n / FPS,
                                f"scene {sid} follows '{a['track']}' onto the face at {n / FPS:.2f} s (NC-1)",
                                "change anchor.offset so the overlay sits on the far side of the object, shrink the box, "
                                "or end the scene before the object reaches the face"))
                break
    return out
