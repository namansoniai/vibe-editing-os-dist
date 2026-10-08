"""`veos angles`: who is on which camera, and the angle registry the shot planner chooses from (E-13, E-13b).

    veos angles [--ids A,B,W] [--assign "A:T1=S1,W:T2=S2"] [--fps 10]

For every camera source (a video source of the session, or the single wide source):
  1. face tracks: faces detected at 5 fps (YuNet on landscape frames, where faces are small; the MediaPipe chain on
     portrait frames), linked into tracks, fragments merged; boxes interpolated at 10 fps;
  2. who is who (active-speaker matching): mouth-region motion of each track (minus upper-face motion, so head moves
     and camera shake cancel) correlated with each speaker's voice activity from work/speakers.json; per camera a
     Hungarian assignment (two faces in one frame are two people). `--assign` overrides it;
  3. the registry (work/angles.json):
       real angle   a camera that shows one person            id = source id     kind host_single|guest_single|single
       faux angles  from a camera that shows 2+ people (E-13b) id = <src>:<S>    tight single per person (faux: true)
                                                                 <src>:2S       two-shot (group framing)
                                                                 <src>:W        the wide
     Each angle stores its subjects, framing, the max upsampling a 9:16 crop needs, and the allowed jump re-crop
     steps. Face tracks go to work/faces/<src>.json (source time, source px) for the reframe pass.
"""
from __future__ import annotations

import subprocess
import time

import numpy as np

from . import facedet, reframe
from .core import SIZE, VeosError, need_project, read_json, tools, write_json
from .sync import from_session, to_session

DET_EVERY = 2
STEPS = (1.0, 1.25, 1.5)


def add_args(p, cmd):
    p.add_argument("--ids", help="camera source ids (default: every video source of the session)")
    p.add_argument("--assign", default=None, help='override who is who: "A:T1=S1,W:T2=S2"')
    p.add_argument("--fps", type=float, default=10.0, help="analysis frame rate (default 10)")


# ======================================================================= detection + tracking
_yunet = None


def nms(boxes: list[tuple], iou: float = 0.3) -> list[tuple]:
    """Drop duplicate detections of one face (overlapping tiles): IoU above `iou`, or a centre inside a kept box."""
    keep: list[tuple] = []
    for b in sorted(boxes, key=lambda b: -b[4]):
        cx, cy = b[0] + b[2] / 2, b[1] + b[3] / 2
        if any(_iou(b, k) > iou or (k[0] <= cx <= k[0] + k[2] and k[1] <= cy <= k[1] + k[3]) for k in keep):
            continue
        keep.append(b)
    return keep


def detect_faces(rgb: np.ndarray) -> list[tuple]:
    """All faces [(x, y, w, h, score)] in rgb pixels, de-duplicated. Landscape frames use YuNet (small faces)."""
    return nms(_detect_raw(rgb))


def _detect_raw(rgb: np.ndarray) -> list[tuple]:
    global _yunet
    H, W = rgb.shape[:2]
    if W > H * 1.1:
        try:
            if _yunet is None:
                _yunet = facedet._YuNet()
            return sorted([b for b in _yunet.detect(rgb) if b[4] >= 0.6], key=lambda b: -b[4])
        except Exception:  # noqa: BLE001 - fall back to the self-healing chain
            _yunet = False if _yunet is None else _yunet
    return facedet.detect(rgb, tiled=True, min_score=0.5)


def _iou(a, b) -> float:
    x0, y0 = max(a[0], b[0]), max(a[1], b[1])
    x1, y1 = min(a[0] + a[2], b[0] + b[2]), min(a[1] + a[3], b[1] + b[3])
    inter = max(0, x1 - x0) * max(0, y1 - y0)
    return inter / max(1e-9, a[2] * a[3] + b[2] * b[3] - inter)


def link_tracks(dets: list[list], max_gap: int = 20) -> list[dict]:
    """dets[i] = boxes at sample i -> tracks [{first, boxes{i: box}}] (greedy IoU / centre-distance association)."""
    tracks: list[dict] = []
    for i, boxes in enumerate(dets):
        used = set()
        live = [t for t in tracks if i - t["last"] <= max_gap]
        pairs = []
        for ti, t in enumerate(live):
            lb = t["boxes"][t["last"]]
            for bi, b in enumerate(boxes):
                d = np.hypot((lb[0] + lb[2] / 2) - (b[0] + b[2] / 2), (lb[1] + lb[3] / 2) - (b[1] + b[3] / 2))
                score = _iou(lb, b) + max(0.0, 1.0 - d / (0.8 * max(lb[2], b[2])))
                if score > 0.3:
                    pairs.append((score, ti, bi))
        for score, ti, bi in sorted(pairs, reverse=True):
            t = live[ti]
            if bi in used or t["last"] == i:
                continue
            t["boxes"][i] = list(boxes[bi][:4])
            t["last"] = i
            used.add(bi)
        for bi, b in enumerate(boxes):
            if bi not in used:
                tracks.append({"first": i, "last": i, "boxes": {i: list(b[:4])}})
    return tracks


def merge_fragments(tracks: list[dict], n: int, min_presence: float = 0.15) -> list[dict]:
    """Join tracks that never overlap in time and sit at the same place (a static camera's face that was lost)."""
    tracks = sorted(tracks, key=lambda t: -len(t["boxes"]))
    out: list[dict] = []
    for t in tracks:
        mt = np.median(np.array(list(t["boxes"].values())), axis=0)
        for o in out:
            mo = np.median(np.array(list(o["boxes"].values())), axis=0)
            if set(o["boxes"]) & set(t["boxes"]):
                continue
            if np.hypot(mo[0] + mo[2] / 2 - mt[0] - mt[2] / 2, mo[1] + mo[3] / 2 - mt[1] - mt[3] / 2) < 0.7 * max(mo[2], mt[2]):
                o["boxes"].update(t["boxes"])
                break
        else:
            out.append({"boxes": dict(t["boxes"])})
    keep = [t for t in out if len(t["boxes"]) >= min_presence * n]
    keep.sort(key=lambda t: np.median([b[0] + b[2] / 2 for b in t["boxes"].values()]))   # left to right
    return keep


def _interp(boxes: dict, n: int, max_gap: int = 30) -> list:
    out = [None] * n
    ks = sorted(boxes)
    for k in ks:
        out[k] = boxes[k]
    for a, b in zip(ks, ks[1:]):
        if 1 < b - a <= max_gap:
            A, B = np.array(boxes[a], float), np.array(boxes[b], float)
            for k in range(a + 1, b):
                out[k] = list(A + (B - A) * (k - a) / (b - a))
    return out


def mouth_motion(prev: np.ndarray, cur: np.ndarray, box) -> float:
    x, y, w, h = [float(v) for v in box]
    H, W = cur.shape

    def reg(y0, y1):
        a, b = int(np.clip(x + 0.2 * w, 0, W - 1)), int(np.clip(x + 0.8 * w, 1, W))
        c, d = int(np.clip(y + y0 * h, 0, H - 1)), int(np.clip(y + y1 * h, 1, H))
        if b <= a or d <= c:
            return 0.0
        return float(np.abs(cur[c:d, a:b].astype(np.int16) - prev[c:d, a:b].astype(np.int16)).mean())

    return max(0.0, reg(0.62, 1.05) - 0.6 * reg(0.05, 0.45))


# ======================================================================= per camera analysis
def analyse_camera(path, src_w: int, src_h: int, fps: float = 10.0, max_w: int = 1280) -> dict:
    """-> {fps, n, scale, tracks: [{boxes: [box|None]*n (source px), mouth: [float|nan]*n}]}"""
    s = min(1.0, max_w / src_w) if src_w > src_h else min(1.0, 720 / src_w)
    w, h = int(round(src_w * s / 2) * 2), int(round(src_h * s / 2) * 2)
    cmd = [tools().ffmpeg, "-v", "error", "-i", str(path), "-vf", f"fps={fps},scale={w}:{h}", "-f", "rawvideo",
           "-pix_fmt", "rgb24", "-"]
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    frames_gray, dets = [], []
    fsz = w * h * 3
    i = 0
    while True:
        b = pr.stdout.read(fsz)
        if len(b) < fsz:
            break
        rgb = np.frombuffer(b, np.uint8).reshape(h, w, 3)
        g = (rgb[..., 0] * 0.299 + rgb[..., 1] * 0.587 + rgb[..., 2] * 0.114).astype(np.uint8)
        frames_gray.append(g)
        dets.append([d for d in detect_faces(rgb)] if i % DET_EVERY == 0 else [])
        i += 1
    pr.wait()
    n = len(frames_gray)
    det_idx = [k for k in range(n) if k % DET_EVERY == 0]
    raw = link_tracks([dets[k] for k in det_idx])
    tracks = merge_fragments(raw, len(det_idx))
    out = []
    for t in tracks:
        boxes = _interp({det_idx[k]: v for k, v in t["boxes"].items()}, n)
        mouth = [float("nan")] * n
        for k in range(1, n):
            if boxes[k] is not None:
                mouth[k] = mouth_motion(frames_gray[k - 1], frames_gray[k], boxes[k])
        out.append({"boxes": [None if b is None else [round(v / s, 1) for v in b] for b in boxes], "mouth": mouth,
                    "presence": round(sum(b is not None for b in boxes) / max(n, 1), 3)})
    return {"fps": fps, "n": n, "scale": s, "tracks": out}


def activity_on_grid(segments: dict, ids: list[str], times_master: np.ndarray) -> np.ndarray:
    A = np.zeros((len(ids), len(times_master)))
    for k, sid in enumerate(ids):
        for a, b in segments.get(sid, []):
            A[k, (times_master >= a) & (times_master < b)] = 1.0
    return A


def match_speakers(tracks: list[dict], A: np.ndarray, ids: list[str], min_corr: float = 0.1) -> list[tuple]:
    """[(speaker id | None, corr)] per track: correlation of smoothed mouth motion with each speaker's activity,
    one speaker per face within a camera (Hungarian)."""
    from scipy.optimize import linear_sum_assignment
    if not tracks or not ids:
        return [(None, 0.0)] * len(tracks)
    C = np.zeros((len(tracks), len(ids)))
    for i, t in enumerate(tracks):
        m = np.array(t["mouth"], float)
        ok = ~np.isnan(m)
        if ok.sum() < 10:
            continue
        mm = np.where(ok, m, 0.0)
        mm = np.convolve(mm, np.ones(5) / 5, mode="same")
        for k in range(len(ids)):
            a = A[k]
            if a[ok].std() < 1e-6 or mm[ok].std() < 1e-9:
                continue
            C[i, k] = float(np.corrcoef(mm[ok], a[ok])[0, 1])
    r, c = linear_sum_assignment(-C)
    out = [(None, 0.0)] * len(tracks)
    for a, b in zip(r, c):
        out[a] = (ids[b], round(float(C[a, b]), 3)) if C[a, b] >= min_corr else (None, round(float(C[a, b]), 3))
    return out


# ======================================================================= registry
def build_registry(cams: dict, cast: dict, canvas: tuple = SIZE) -> list[dict]:
    """cams: {src: {size: [w, h], tracks: [{id, subject, median}]}} -> angle list (see module doc)."""
    angles = []
    full, half = (canvas[0], canvas[1]), (canvas[0], canvas[1] // 2)

    def kind_of(sid):
        role = (cast.get(sid) or {}).get("role")
        return f"{role}_single" if role in ("host", "guest") else "single"

    def scale_for(face, src):
        out = {}
        for nm, cell in (("full", full), ("stack", half)):
            w, h, info = reframe.size_single(face[3], src, cell, reframe.FACE_FRAC[nm], 1.0, max_up=99)
            out[nm] = info["scale"]
        return out

    for sid_src, cam in cams.items():
        src = tuple(cam["size"])
        subs = [t for t in cam["tracks"] if t.get("subject")]
        if len(subs) == 1:
            t = subs[0]
            sc = scale_for(t["median"], src)
            angles.append({"id": sid_src, "kind": kind_of(t["subject"]), "source": sid_src, "subjects": [t["subject"]],
                           "track": t["id"], "framing": "single", "faux": False, "scale": sc,
                           "steps": [s for s in STEPS if sc["full"] * s <= reframe.MAX_UP * 1.4 or s == 1.0]})
        elif len(subs) >= 2:
            for t in subs:
                sc = scale_for(t["median"], src)
                angles.append({"id": f"{sid_src}:{t['subject']}", "kind": kind_of(t["subject"]), "source": sid_src,
                               "subjects": [t["subject"]], "track": t["id"], "framing": "single", "faux": True,
                               "scale": sc, "steps": [s for s in STEPS if sc["full"] * s <= reframe.MAX_UP * 1.4 or s == 1.0],
                               "fidelity": "degraded"})
            g = reframe.group_rect([t["median"] for t in subs], src, full)
            angles.append({"id": f"{sid_src}:2S", "kind": "two_shot", "source": sid_src,
                           "subjects": [t["subject"] for t in subs], "tracks": [t["id"] for t in subs],
                           "framing": "group", "faux": True, "fit_9x16": g["fit"], "steps": [1.0]})
            angles.append({"id": f"{sid_src}:W", "kind": "wide", "source": sid_src, "subjects": [t["subject"] for t in subs],
                           "framing": "wide", "faux": False, "fit_9x16": reframe.wide_rect(src, full)["fit"], "steps": [1.0]})
    return angles


def best_angles(angles: list[dict], ids: list[str]) -> dict:
    """Per speaker: preferred single (real over faux, larger face first), plus the session's two-shot and wide."""
    out = {}
    for sid in ids:
        singles = [a for a in angles if a["framing"] == "single" and a["subjects"] == [sid]]
        singles.sort(key=lambda a: (a["faux"], a["scale"]["full"]))
        out[sid] = {"single": singles[0]["id"] if singles else None, "singles": [a["id"] for a in singles]}
    two = [a["id"] for a in angles if a["framing"] == "group"]
    wide = [a["id"] for a in angles if a["framing"] == "wide"]
    return {"speakers": out, "two_shot": two[0] if two else None, "wide": wide[0] if wide else None}


# ======================================================================= command
def _parse_assign(s: str | None) -> dict:
    out = {}
    for part in [p.strip() for p in (s or "").split(",") if p.strip()]:
        try:
            cam_tr, spk = part.split("=")
            cam, tr = cam_tr.split(":")
        except ValueError as e:
            raise VeosError("BAD_ARG", f"--assign {part}: use CAM:T1=S1", 'Example: --assign "A:T1=S1,W:T2=S2"') from e
        out[(cam.strip(), tr.strip())] = spk.strip()
    return out


def main(args, project) -> dict:
    proj = need_project(project)
    sp = proj.work / "sources.json"
    if not sp.exists():
        raise VeosError("NO_SOURCES", "work/sources.json not found", "Run `veos ingest` first.")
    data = read_json(sp)
    sources = {s["id"]: s for s in data["sources"]}
    spk_p = proj.work / "speakers.json"
    if not spk_p.exists():
        raise VeosError("NO_SPEAKERS", "work/speakers.json not found", "Run `veos speakers` first.")
    spk = read_json(spk_p)
    ids = [s["id"] for s in spk["speakers"]]
    cast = {s["id"]: {"name": s.get("name"), "role": s.get("role") or s.get("role_guess")} for s in spk["speakers"]}
    master = sources[spk["master"]]
    sess = data.get("session") or {}
    want = [x.strip() for x in args.ids.split(",")] if args.ids else (
        sess.get("cameras") or [s["id"] for s in data["sources"] if s.get("width") and s.get("kind") == "talking-head"]
        or ([spk["master"]] if sources[spk["master"]].get("width") else []))
    cams = [sources[c] for c in want if c in sources and sources[c].get("width") and c != "MIX"]
    if not cams:
        raise VeosError("NO_CAMERAS", "no camera source to analyse", "Ingest the camera files of the conversation.")
    assign = _parse_assign(args.assign)
    t0 = time.time()
    reg_cams, summary, warnings = {}, [], []
    for c in cams:
        vid = proj.work / "src" / f"{c['id']}.mp4"
        path = vid if vid.exists() else proj.abs(c["path"])
        an = analyse_camera(path, c["width"], c["height"], args.fps)
        times = np.arange(an["n"]) / args.fps
        t_master = from_session(master.get("sync") or {"offset": 0.0},
                                np.array([to_session(c.get("sync") or {"offset": 0.0}, t) for t in times]))
        A = activity_on_grid(spk["segments"], ids, np.asarray(t_master))
        match = match_speakers(an["tracks"], A, ids)
        tracks = []
        for k, (t, (who, corr)) in enumerate(zip(an["tracks"], match)):
            tid = f"T{k + 1}"
            if (c["id"], tid) in assign:
                who, corr = assign[(c["id"], tid)], None
            elif who is None and t["presence"] > 0.5:
                warnings.append(f"{c['id']} {tid}: a face whose lips do not follow any voice (corr {corr}); "
                                "pass --assign if this person talks")
            elif who is not None and corr < 0.2:
                warnings.append(f"{c['id']} {tid}: weak lip/voice match ({corr}); check who-is-who or pass --assign")
            med = np.median(np.array([b for b in t["boxes"] if b is not None]), axis=0).round(1).tolist()
            tracks.append({"id": tid, "subject": who, "corr": corr, "presence": t["presence"], "median": med})
        write_json(proj.path("work", "faces", f"{c['id']}.json"),
                   {"version": 1, "source": c["id"], "fps": args.fps, "n": an["n"], "size": [c["width"], c["height"]],
                    "tracks": {f"T{k + 1}": t["boxes"] for k, t in enumerate(an["tracks"])}}, indent=None)
        reg_cams[c["id"]] = {"size": [c["width"], c["height"]], "tracks": tracks}
        summary.append({"camera": c["id"], "faces": len(tracks),
                        "who": {t["id"]: f"{t['subject']} ({t['corr']})" for t in tracks}})
    angles = build_registry(reg_cams, cast)
    # two people on one face? the same speaker on two faces of one camera is impossible (Hungarian), across
    # cameras it is normal (a single + the wide)
    pref = best_angles(angles, ids)
    missing = [s for s in ids if not pref["speakers"][s]["single"]]
    if missing:
        warnings.append(f"no camera shows {', '.join(missing)}: shots of them fall back to the two-shot/wide")
    doc = {"version": 1, "canvas": list(SIZE), "master": spk["master"], "cameras": reg_cams, "angles": angles,
           "preferred": pref, "cast": cast}
    write_json(proj.path("work", "angles.json"), doc)
    proj.log("angles", f"{len(angles)} angles from {len(cams)} cameras in {time.time() - t0:.1f}s")
    return {"cameras": summary, "angles": [{"id": a["id"], "kind": a["kind"], "faux": a["faux"]} for a in angles],
            "file": "work/angles.json", "warnings": warnings}
