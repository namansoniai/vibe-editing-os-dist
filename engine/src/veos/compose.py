"""Multi-camera compositor: timeline shots -> work/multicam/footage.mp4 (the reel's footage layer, frame-exact).

For every edit frame n: edit time -> master time (cutmap) -> session time -> each camera's own time (sync blocks),
then each cell of the shot (`full`, or the two halves of a `stack`) gets its angle's crop of that camera frame:
  * single  : crop size fixed per shot (median face height over the shot), position from the subject-follow
              keyframes (reframe.follow) -> the "reframe keyframes" of E-13;
  * group / wide : a cover crop when it fits the cell, else `blurfill` (the content band fitted to the cell width
              over a blurred copy darkened to tokens `dialogue.blur_dim`, 0.45) or `letterbox` (band on black), per `dialogue.fallback`.
Cameras are decoded once each through ffmpeg pipes (sequential reads; re-opened on a backwards/long jump), so two
cells of the same wide camera (E-13b faux angles) cost one decode.

Writes work/multicam/footage.mp4 (1080x1920, 30 fps, BT.709, CRF 16), work/multicam/face.edit.json (the shown
speaker's face box per frame in canvas px; same format as work/face.edit.json) and work/multicam/compose.json
(frames, per-shot geometry incl. the reframe keyframes). `veos prep-frames` uses footage.mp4 instead of src+matte
when compose.json matches the cutmap (no cut-out layer: `behind` scenes are not available on multi-camera reels).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import numpy as np

from . import reframe as RF
from .core import FPS, SIZE, VeosError, read_json, run, tools, write_json
from .sync import from_session, to_session

BLUR_DIM = 0.45  # default brightness of the blurfill backdrop; tokens `dialogue.blur_dim` (0..1, 1 = undimmed) overrides it


def blur_dim_of(tokens: dict | None) -> float:
    """The blurfill backdrop brightness from tokens `dialogue.blur_dim` (a number 0..1), else BLUR_DIM. Bad values fail."""
    v = ((tokens or {}).get("dialogue") or {}).get("blur_dim")
    if v is None:
        return BLUR_DIM
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not 0 <= v <= 1:
        raise VeosError("BAD_TOKENS", f"dialogue.blur_dim must be a number 0-1 (the blurfill backdrop brightness), got {v!r}",
                        "Use 0.45 for the default darkened backdrop, 1.0 for an undimmed one.")
    return float(v)


# ======================================================================= decoding
class Reader:
    """Sequential BGR frame reader for a CFR file; get(k) returns frame k (clamped), re-opening on jumps."""

    def __init__(self, path: Path, w: int, h: int, frames: int, fps: float = FPS):
        self.path, self.w, self.h, self.frames, self.fps = path, w, h, max(1, frames), fps
        self.proc, self.pos, self.last, self.last_k = None, -1, None, None

    def _open(self, k: int):
        self.close()
        t = max(0.0, k / self.fps)
        cmd = [tools().ffmpeg, "-v", "error", "-ss", f"{t:.5f}", "-i", str(self.path), "-map", "0:v:0",
               "-f", "rawvideo", "-pix_fmt", "bgr24", "-"]
        self.proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=self.w * self.h * 3 * 2)
        self.pos = k - 1

    def get(self, k: int) -> np.ndarray:
        k = int(np.clip(k, 0, self.frames - 1))
        if k == self.last_k:
            return self.last
        if self.proc is None or k < self.pos or k > self.pos + 90:   # backwards or a long jump: seek
            self._open(k)
        n = self.w * self.h * 3
        while self.pos < k:
            b = self.proc.stdout.read(n)
            if len(b) < n:          # past the end: hold the last frame
                self.frames = self.pos + 1
                break
            self.last = np.frombuffer(b, np.uint8).reshape(self.h, self.w, 3)
            self.pos += 1
        self.last_k = k
        if self.last is None:
            self.last = np.zeros((self.h, self.w, 3), np.uint8)
        return self.last

    def close(self):
        if self.proc:
            self.proc.stdout.close()
            self.proc.kill()
            self.proc.wait()
            self.proc = None


# ======================================================================= time mapping
class TimeMap:
    """edit frame -> master seconds (cutmap) -> session -> camera seconds."""

    def __init__(self, cutmap: dict, sources: dict, master: str):
        self.segs = cutmap["segments"]
        self.sources, self.master = sources, master
        self.msync = sources[master].get("sync") or {"offset": 0.0}

    def master_t(self, n: int) -> float:
        for s in self.segs:
            if s["f0"] <= n < s["f1"]:
                return (s["in_frame"] + n - s["f0"]) / FPS
        s = self.segs[-1]
        return (s["in_frame"] + n - s["f0"]) / FPS

    def cam_t(self, cam: str, t_master: float) -> float:
        cs = self.sources[cam].get("sync") or {"offset": 0.0}
        return float(from_session(cs, to_session(self.msync, t_master)))


# ======================================================================= faces
class Faces:
    def __init__(self, proj, cam: str):
        p = proj.work / "faces" / f"{cam}.json"
        self.doc = read_json(p) if p.exists() else {"fps": 10, "tracks": {}}
        self.fps = self.doc["fps"]

    def box(self, track: str, t: float):
        tr = self.doc["tracks"].get(track) or []
        if not tr:
            return None
        i = int(round(t * self.fps))
        for d in range(0, 31):
            for j in (i - d, i + d):
                if 0 <= j < len(tr) and tr[j] is not None:
                    return tr[j]
        return None

    def median(self, track: str):
        tr = [b for b in (self.doc["tracks"].get(track) or []) if b is not None]
        return np.median(np.array(tr), axis=0).tolist() if tr else None


# ======================================================================= geometry per shot cell
def cell_geometry(angle: dict, faces: Faces, src: tuple, cell: tuple, cam_times: list[float], step: float,
                  kind: str, fallback: str = "blurfill") -> dict:
    if angle["framing"] == "single":
        bx = [faces.box(angle["track"], t) for t in cam_times]
        hs = [b[3] for b in bx if b]
        med = faces.median(angle["track"])
        face_h = float(np.median(hs)) if hs else (med[3] if med else src[1] * 0.12)
        frac = RF.FACE_FRAC[kind]
        if abs(src[0] / src[1] - cell[0] / cell[1]) < 0.05:
            frac = min(frac, face_h / src[1])     # same aspect: keep the camera's own framing; steps punch in from it
        w, h, info = RF.size_single(face_h, src, cell, frac, step)
        tops = [None if b is None else RF.place_single(b, (w, h), src)[:2] for b in bx]
        keys = RF.follow(cam_times, tops, (w, h), src)
        if not keys:
            x, y, _, _ = RF.place_single(med or [src[0] / 2 - 50, src[1] / 3, 100, 100], (w, h), src)
            keys = [[cam_times[0] if cam_times else 0.0, x, y]]
        return {"fit": "cover", "wh": [round(w, 1), round(h, 1)], "keys": keys, "scale": info["scale"],
                "limited": info["limited"]}
    if angle["framing"] == "group":
        fs = [faces.median(t) for t in angle.get("tracks", [])]
        g = RF.group_rect([f for f in fs if f], src, cell)
    else:
        g = RF.wide_rect(src, cell)
    if g["fit"] == "cover":
        x, y, w, h = g["crop"]
        return {"fit": "cover", "wh": [w, h], "keys": [[0.0, x, y]], "scale": round(cell[1] / h, 3)}
    return {"fit": fallback, "band": [round(v, 1) for v in g["band"]]}


def _blur_cover(img: np.ndarray, cell: tuple, dim: float = BLUR_DIM) -> np.ndarray:
    import cv2
    cw, ch = cell
    h, w = img.shape[:2]
    s = max(cw / w, ch / h)
    small = cv2.resize(img, (max(2, int(w * s / 16)), max(2, int(h * s / 16))), interpolation=cv2.INTER_AREA)
    small = cv2.GaussianBlur(small, (0, 0), 3)
    big = cv2.resize(small, (int(w * s) + 2, int(h * s) + 2), interpolation=cv2.INTER_LINEAR)
    oy, ox = (big.shape[0] - ch) // 2, (big.shape[1] - cw) // 2
    return np.clip(big[oy:oy + ch, ox:ox + cw].astype(np.float32) * dim, 0, 255).astype(np.uint8)


def draw_cell(frame: np.ndarray, geo: dict, cell: tuple, t_cam: float, dim: float = BLUR_DIM) -> tuple[np.ndarray, tuple | None]:
    """-> (cell image, (x, y, s) mapping source px to cell px)."""
    import cv2
    cw, ch = cell
    if geo["fit"] == "cover":
        w, h = geo["wh"]
        x, y = RF.at(geo["keys"], t_cam)
        s = cw / w
        if s < 0.7:
            xi, yi = int(round(x)), int(round(y))
            crop = frame[yi:yi + int(round(h)), xi:xi + int(round(w))]
            return cv2.resize(crop, (cw, ch), interpolation=cv2.INTER_AREA), (x, y, s)
        M = np.array([[s, 0, -x * s], [0, s, -y * s]], np.float32)
        return cv2.warpAffine(frame, M, (cw, ch), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE), (x, y, s)
    bx, by, bw, bh = geo["band"]
    band = frame[int(by):int(by + bh), int(bx):int(bx + bw)]
    dx, dy, dw, dh = RF.band_layout((bx, by, bw, bh), cell)
    out = _blur_cover(band, cell, dim) if geo["fit"] == "blurfill" else np.zeros((ch, cw, 3), np.uint8)
    fit = cv2.resize(band, (int(round(dw)), int(round(dh))), interpolation=cv2.INTER_AREA)
    y0, x0 = int(round(dy)), int(round(dx))
    out[y0:y0 + fit.shape[0], x0:x0 + fit.shape[1]] = fit[: ch - y0, : cw - x0]
    s = dw / bw
    return out, (bx - dx / s, by - dy / s, s)


# ======================================================================= main entry
def shots_hash(shots: list[dict], cutmap: dict) -> str:
    return hashlib.sha1(json.dumps([shots, cutmap.get("segments")], sort_keys=True).encode()).hexdigest()[:16]


def render(proj, shots: list[dict], canvas: tuple = SIZE, fallback: str = "blurfill", progress=None,
           blur_dim: float = BLUR_DIM) -> dict:
    import cv2
    W, H = canvas
    cm = read_json(proj.work / "cutmap.json")
    data = read_json(proj.work / "sources.json")
    sources = {s["id"]: s for s in data["sources"]}
    ang_doc = read_json(proj.work / "angles.json")
    angles = {a["id"]: a for a in ang_doc["angles"]}
    master = cm["segments"][0]["src"]
    tm = TimeMap(cm, sources, master)
    N = int(cm["frames"])
    faces: dict = {}
    readers: dict = {}

    def angle_of(ref: str) -> dict:
        aid = ref.split(":", 1)[1] if ref.startswith("source:") else ref
        if aid not in angles:
            raise VeosError("BAD_SHOT", f"shot uses unknown angle '{aid}'", f"Known angles: {', '.join(angles)}.")
        return angles[aid]

    def cells_of(sh: dict) -> list[tuple]:
        if sh["layout"] == "stack":
            sy = int(sh.get("seam_y", H // 2))
            return [(angle_of(sh["top"]), (W, sy), (0, 0), "stack", sh.get("top_subject")),
                    (angle_of(sh["bottom"]), (W, H - sy), (0, sy), "stack", sh.get("bottom_subject"))]
        return [(angle_of(sh["angle"]), (W, H), (0, 0), "full", sh.get("subject"))]

    # geometry per shot cell (source-time samples every 0.1 s)
    plan = []
    for sh in shots:
        f0, f1 = int(round(sh["t0"] * FPS)), min(N, int(round(sh["t1"] * FPS)))
        cells = []
        for ang, cell, org, kind, subj in cells_of(sh):
            cam = ang["source"]
            faces.setdefault(cam, Faces(proj, cam))
            src = (sources[cam]["width"], sources[cam]["height"])
            ns = list(range(f0, max(f0 + 1, f1), 3))
            ts = [tm.cam_t(cam, tm.master_t(n)) for n in ns]
            geo = cell_geometry(ang, faces[cam], src, cell, ts, float(sh.get("step", 1.0)), kind, fallback)
            cells.append({"angle": ang["id"], "cam": cam, "cell": list(cell), "org": list(org), "subject": subj,
                          "track": ang.get("track"), **geo})
        plan.append({"t0": sh["t0"], "t1": sh["t1"], "f0": f0, "f1": f1, "layout": sh["layout"], "cells": cells,
                     **({"hairline": sh.get("hairline", 0), "seam_y": sh.get("seam_y")} if sh["layout"] == "stack" else {})})
    out_dir = proj.work / "multicam"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "footage.mp4"
    tmp = out_dir / "footage.tmp.mp4"
    enc = subprocess.Popen([tools().ffmpeg, "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",
                            "-pix_fmt", "yuv420p", "-colorspace", "bt709", "-color_primaries", "bt709",
                            "-color_trc", "bt709", "-color_range", "tv", "-movflags", "+faststart", str(tmp)],
                           stdin=subprocess.PIPE)
    boxes: list = [None] * N
    t0 = time.time()
    pi = 0
    try:
        for n in range(N):
            while pi + 1 < len(plan) and n >= plan[pi]["f1"]:
                pi += 1
            p = plan[pi]
            canvas_img = np.zeros((H, W, 3), np.uint8)
            tmast = tm.master_t(n)
            for c in p["cells"]:
                cam = c["cam"]
                s = sources[cam]
                if cam not in readers:
                    vid = proj.work / "src" / f"{cam}.mp4"
                    readers[cam] = Reader(vid if vid.exists() else proj.abs(s["path"]), s["width"], s["height"],
                                          int(s.get("frames") or round(s["duration"] * FPS)))
                tc = tm.cam_t(cam, tmast)
                fr = readers[cam].get(int(round(tc * FPS)))
                img, mp = draw_cell(fr, c, tuple(c["cell"]), tc, blur_dim)
                ox, oy = c["org"]
                canvas_img[oy:oy + img.shape[0], ox:ox + img.shape[1]] = img
                if boxes[n] is None and c.get("track") and c.get("subject") and mp:
                    b = faces[cam].box(c["track"], tc)
                    if b:
                        x, y, sc = mp
                        bb = [ox + (b[0] - x) * sc, oy + (b[1] - y) * sc, b[2] * sc, b[3] * sc]
                        if 0 <= bb[0] + bb[2] / 2 <= W and oy <= bb[1] + bb[3] / 2 <= oy + c["cell"][1]:
                            boxes[n] = [round(v, 1) for v in bb] + [1.0]
            if p["layout"] == "stack" and p.get("hairline"):
                sy = int(p.get("seam_y") or H // 2)
                hl = int(p["hairline"])
                canvas_img[max(0, sy - hl // 2): sy + (hl + 1) // 2] = 0
            enc.stdin.write(canvas_img.tobytes())
            if progress and n % 300 == 0:
                progress(n / N)
    finally:
        enc.stdin.close()
        enc.wait()
        for r in readers.values():
            r.close()
    if enc.returncode != 0:
        raise VeosError("COMPOSE_FAILED", "encoding the multi-camera footage failed", "See logs/shots.log.")
    tmp.replace(out)
    got = int(run([tools().ffprobe, "-v", "error", "-count_packets", "-select_streams", "v:0", "-show_entries",
                   "stream=nb_read_packets", "-of", "csv=p=0", str(out)]).stdout.decode().strip().split(",")[0])
    if got != N:
        raise VeosError("FRAME_MISMATCH", f"composed footage has {got} frames, cutmap says {N}", "This is a bug.")
    write_json(out_dir / "face.edit.json", {"version": 1, "fps": FPS, "size": [W, H], "frames": N, "boxes": boxes},
               indent=None)
    doc = {"version": 1, "frames": N, "canvas": [W, H], "hash": shots_hash(shots, cm), "footage": "work/multicam/footage.mp4",
           "face": "work/multicam/face.edit.json", "shots": plan, "blur_dim": blur_dim, "seconds": round(time.time() - t0, 1)}
    write_json(out_dir / "compose.json", doc)
    return {"frames": N, "fps_render": round(N / max(time.time() - t0, 1e-6), 1),
            "fallbacks": sorted({c["fit"] for p in plan for c in p["cells"] if c["fit"] != "cover"}),
            "max_upscale": max([c.get("scale", 1.0) for p in plan for c in p["cells"] if c.get("scale")] or [1.0])}


# ======================================================================= prep-frames hook
def composed_ready(proj) -> bool:
    cj, cm = proj.work / "multicam" / "compose.json", proj.work / "cutmap.json"
    if not (cj.exists() and cm.exists() and (proj.work / "multicam" / "footage.mp4").exists()):
        return False
    return int(read_json(cj).get("frames", -1)) == int(read_json(cm)["frames"])


def prep_frames(proj, args) -> dict:
    """`veos prep-frames` for multi-camera reels: frames come from the composed footage (no matte / cut-out)."""
    import shutil
    t0 = time.time()
    N = int(read_json(proj.work / "cutmap.json")["frames"])
    a, b = (args.range if getattr(args, "range", None) else (0, N))
    a, b = max(0, a), min(N, b)
    fdir = proj.work / "frames"
    fdir.mkdir(parents=True, exist_ok=True)
    have = all((fdir / f"f{n:05d}.jpg").exists() for n in range(a, b))
    fresh = have and (fdir / f"f{a:05d}.jpg").stat().st_mtime >= (proj.work / "multicam" / "footage.mp4").stat().st_mtime
    if not fresh or getattr(args, "force", False):
        run([tools().ffmpeg, "-v", "error", "-y", "-i", str(proj.work / "multicam" / "footage.mp4"),
             "-vf", f"select=between(n\\,{a}\\,{b - 1})", "-fps_mode", "passthrough", "-q:v", "3",
             "-start_number", str(a), str(fdir / "f%05d.jpg")], proj, "prep-frames")
    missing = [n for n in range(a, b) if not (fdir / f"f{n:05d}.jpg").exists()]
    if missing:
        raise VeosError("PREP_INCOMPLETE", f"{len(missing)} frames missing (first {missing[0]})", "Re-run `veos shots render`.")
    shutil.copyfile(proj.work / "multicam" / "face.edit.json", proj.work / "face.edit.json")
    with_box = sum(1 for x in read_json(proj.work / "face.edit.json")["boxes"] if x)
    return {"frames": b - a, "written": 0 if fresh else b - a, "cached": (b - a) if fresh else 0, "source": "multicam",
            "face": {"file": "work/face.edit.json", "with_box": with_box, "of": N}, "frames_dir": proj.rel(fdir),
            "seconds": round(time.time() - t0, 2),
            "warnings": ["multi-camera reel: footage from work/multicam/footage.mp4; no cut-out layer (no `behind` scenes)"]}
