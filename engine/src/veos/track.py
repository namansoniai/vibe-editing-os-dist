"""`veos track`: follow an object (box) or a point through a clip on the CPU (Package E, ER-2 / E-15).

    veos track --project P --at T (--box x,y,w,h | --point x,y) [--from A] [--to B] [--clip ID|FILE|ASSET] [--id NAME]

Two spaces:
* **edit** (default; `--clip` omitted or a source id of the cut map): times are EDIT seconds, the seed box / point is in
  edit-frame pixels (1080x1920, the pixels of work/frames/f%05d.jpg; double the cut_proxy.mp4 coordinates). Frames are
  decoded from work/src/<id>.mp4 through the cut map, so jump cuts inside one take are followed and other sources are
  left out (`--clip A` keeps only source A's spans).
* **clip** (`--clip` = a video file or a `plan/assets/<name>` video asset): times are the clip's own seconds (30 fps),
  coordinates are the clip's pixels (an asset's JPEG frames, or the file's frames). A scene that shows the clip maps
  them onto the screen (`anchor.clip_t0` / `anchor.place`, SCENES-API section 13).

Cheap by design: frames are decoded once by ffmpeg (2 threads) into a small proxy (`--proxy` px on the long side,
default 640) and tracked every `--step` frames (default 2, ~15 fps); in-between frames are interpolated. A span is
capped at `--max-span` seconds (default 10). Trackers: OpenCV CSRT or KCF when the build has them (opencv-contrib),
else the built-in `flow` tracker (pyramidal Lucas-Kanade on corner features + a template search), which works on the
plain opencv-python-headless wheel. Points always use Lucas-Kanade with a forward-backward check.

Confidence is the same for every tracker: the normalised cross-correlation of the tracked patch with the seed template
and with the most recent confident template (0..1). A sample below `--min-conf` (default 0.5) is **lost**; while lost the
last confident template is searched over the whole proxy frame and the tracker restarts when it is found again.

Writes plan/tracks/<id>.json (TRACK FORMAT below) and plan/tracks/<id>.preview.jpg (six frames with the box drawn: look
at it before anchoring anything). `--look` writes plan/tracks/look_<t>.jpg (the frame at --at with a 100 px grid in the
seed's coordinates) and exits: use it to read off the box.

TRACK FORMAT (version 1)
    {"version": 1, "id", "space": "edit" | "clip", "clip", "source", "mode": "box" | "point", "method", "fps": 30,
     "size": [W, H] (the coordinate space), "at", "from", "to", "seed": {"f", "box" | "point"},
     "reframe": {"s", "tx", "ty"} | null, "min_conf",
     "frames": [{"f", "x", "y", "w", "h", "conf", "lost"?}], "stats": {...}}
  Edit space: `f` is the edit frame and x, y, w, h are OUTPUT-frame pixels on a full stage after the reel's base reframe
  (E-16b framing; identity when the reel has none). The camera, a stage layout (card, pip, low ...) and the canvas camera
  are applied live by the renderer, through the same footage->screen transform as ctx.face(). Clip space: `f` is the clip
  frame and the pixels are the clip's. A point track has w = h = 0. Lost frames keep the last confident position.
"""
from __future__ import annotations

import math
import re
import subprocess
import time
from pathlib import Path

import numpy as np

from .core import FPS, VeosError, need_project, r3, read_json, tools, write_json

PROXY = 640          # proxy long side (px)
STEP = 2             # track every 2nd frame (~15 fps at 30 fps), interpolate the rest
MAX_SPAN = 10.0      # seconds per run (CPU guard)
MIN_CONF = 0.5       # below: lost
REACQ = 0.72         # template score that re-acquires a lost object
KEEP = 0.75          # a sample this confident refreshes the "recent" template
TPL = 48             # template side (px) for the confidence score
METHODS = ("auto", "csrt", "kcf", "flow")
ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,40}$")


def add_args(p, cmd):
    p.add_argument("--at", type=float, required=True, help="seconds where the seed box / point is (edit time; clip time with a clip)")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--box", help="x,y,w,h of the object at --at (edit-frame px 1080x1920, or clip px)")
    g.add_argument("--point", help="x,y of the point at --at")
    p.add_argument("--from", dest="t_from", type=float, default=None, help="track backwards from --at to here (default: --at)")
    p.add_argument("--to", type=float, default=None, help="track forwards from --at to here (default: --at + 4 s, clamped)")
    p.add_argument("--clip", default=None, help="source id of the cut map (edit time), or a video file / plan/assets video name (clip time)")
    p.add_argument("--id", default=None, help="track id (default track1, track2, ...): plan/tracks/<id>.json")
    p.add_argument("--method", choices=METHODS, default="auto", help="box tracker (auto: csrt when available, else flow)")
    p.add_argument("--min-conf", type=float, default=MIN_CONF, help="confidence below which a frame is lost (0..1)")
    p.add_argument("--step", type=int, default=STEP, help="track every Nth frame (1 = every frame)")
    p.add_argument("--proxy", type=int, default=PROXY, help="proxy long side in px")
    p.add_argument("--max-span", type=float, default=MAX_SPAN, help="maximum seconds tracked in one run")
    p.add_argument("--look", action="store_true", help="only write plan/tracks/look_<t>.jpg (the frame at --at with a grid)")


# ------------------------------------------------------------------------------------------------ parsing
def parse_nums(s: str, n: int, what: str) -> list[float]:
    try:
        v = [float(x) for x in re.split(r"[,\s]+", str(s).strip()) if x != ""]
    except ValueError:
        v = []
    if len(v) != n or not all(math.isfinite(x) for x in v):
        raise VeosError("BAD_TRACK_ARGS", f"--{what} needs {n} numbers separated by commas (got '{s}')",
                        f"Example: --{what} " + ("400,700,240,420" if n == 4 else "540,960"))
    if n == 4 and (v[2] < 4 or v[3] < 4):
        raise VeosError("BAD_TRACK_ARGS", f"--box is too small ({v[2]:g}x{v[3]:g} px)", "Give the object's whole box, at least 4x4 px.")
    return v


# ------------------------------------------------------------------------------------------------ confidence
def _gray(img: np.ndarray) -> np.ndarray:
    import cv2
    return img if img.ndim == 2 else cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def _patch(gray: np.ndarray, box, side: int = TPL) -> np.ndarray | None:
    """The box's pixels resized to side x side (None when the box is mostly outside the frame)."""
    import cv2
    h, w = gray.shape[:2]
    x, y, bw, bh = box
    x0, y0, x1, y1 = int(round(x)), int(round(y)), int(round(x + bw)), int(round(y + bh))
    cx0, cy0, cx1, cy1 = max(0, x0), max(0, y0), min(w, x1), min(h, y1)
    if cx1 - cx0 < 3 or cy1 - cy0 < 3 or (cx1 - cx0) * (cy1 - cy0) < 0.5 * max(1, (x1 - x0) * (y1 - y0)):
        return None
    return cv2.resize(gray[cy0:cy1, cx0:cx1], (side, side), interpolation=cv2.INTER_AREA)


def ncc(a: np.ndarray | None, b: np.ndarray | None) -> float:
    """Normalised cross-correlation of two equal-size patches, clipped to 0..1 (flat patches score 0)."""
    if a is None or b is None:
        return 0.0
    a = a.astype(np.float32) - a.mean()
    b = b.astype(np.float32) - b.mean()
    d = float(np.sqrt((a * a).sum() * (b * b).sum()))
    return 0.0 if d < 1e-6 else max(0.0, min(1.0, float((a * b).sum()) / d))


def _search(gray: np.ndarray, tpl_img: np.ndarray, wh) -> tuple[float, tuple] | None:
    """Template search over the whole proxy frame: (score, box) of the best match of `tpl_img` resized to wh."""
    import cv2
    w, h = max(4, int(round(wh[0]))), max(4, int(round(wh[1])))
    if w >= gray.shape[1] or h >= gray.shape[0]:
        return None
    t = cv2.resize(tpl_img, (w, h), interpolation=cv2.INTER_AREA)
    if float(t.std()) < 1e-3:
        return None
    r = cv2.matchTemplate(gray, t, cv2.TM_CCOEFF_NORMED)
    _, mx, _, loc = cv2.minMaxLoc(r)
    return float(mx), (float(loc[0]), float(loc[1]), float(w), float(h))


# ------------------------------------------------------------------------------------------------ trackers
def available_method(method: str) -> str:
    import cv2
    have = {"csrt": hasattr(cv2, "TrackerCSRT_create") or hasattr(getattr(cv2, "legacy", None), "TrackerCSRT_create"),
            "kcf": hasattr(cv2, "TrackerKCF_create") or hasattr(getattr(cv2, "legacy", None), "TrackerKCF_create")}
    if method == "auto":
        return "csrt" if have["csrt"] else "flow"
    if method in have and not have[method]:
        return "flow"
    return method


class _CvTracker:
    """OpenCV CSRT / KCF (opencv-contrib)."""

    def __init__(self, method: str, img: np.ndarray, box):
        import cv2
        name = {"csrt": "TrackerCSRT_create", "kcf": "TrackerKCF_create"}[method]
        mk = getattr(cv2, name, None) or getattr(cv2.legacy, name)
        self.t = mk()
        self.t.init(img, tuple(int(round(v)) for v in box))

    def update(self, img: np.ndarray):
        ok, b = self.t.update(img)
        return tuple(float(v) for v in b) if ok and b[2] > 1 and b[3] > 1 else None


class _FlowTracker:
    """Built-in box tracker: Lucas-Kanade on corner features inside the box (forward-backward checked); the median
    displacement moves the box, the median change of pairwise distances scales it (clamped per step)."""

    LK = dict(winSize=(21, 21), maxLevel=3, criteria=(3, 20, 0.03))  # cv2.TERM_CRITERIA_EPS | COUNT == 3

    def __init__(self, img: np.ndarray, box):
        self.prev = _gray(img)
        self.box = tuple(float(v) for v in box)

    def _features(self, gray, box):
        import cv2
        h, w = gray.shape
        x, y, bw, bh = box
        m = np.zeros_like(gray)
        x0, y0 = max(0, int(x)), max(0, int(y))
        x1, y1 = min(w, int(x + bw)), min(h, int(y + bh))
        if x1 - x0 < 3 or y1 - y0 < 3:
            return None
        m[y0:y1, x0:x1] = 255
        pts = cv2.goodFeaturesToTrack(gray, maxCorners=80, qualityLevel=0.01, minDistance=3, mask=m)
        if pts is None or len(pts) < 6:  # a flat object: a regular grid still carries its texture
            gx, gy = np.meshgrid(np.linspace(x0 + 2, x1 - 2, 6), np.linspace(y0 + 2, y1 - 2, 6))
            pts = np.stack([gx.ravel(), gy.ravel()], 1).astype(np.float32).reshape(-1, 1, 2)
        return pts.astype(np.float32)

    def update(self, img: np.ndarray):
        import cv2
        gray = _gray(img)
        p0 = self._features(self.prev, self.box)
        if p0 is None:
            return None
        p1, st, _ = cv2.calcOpticalFlowPyrLK(self.prev, gray, p0, None, **self.LK)
        if p1 is None:
            return None
        pb, st2, _ = cv2.calcOpticalFlowPyrLK(gray, self.prev, p1, None, **self.LK)
        fb = np.linalg.norm((p0 - pb).reshape(-1, 2), axis=1)
        good = (st.ravel() == 1) & (st2.ravel() == 1) & (fb < 1.5)
        if good.sum() < 4:
            return None
        a, b = p0.reshape(-1, 2)[good], p1.reshape(-1, 2)[good]
        d = np.median(b - a, axis=0)
        s = 1.0
        if len(a) >= 6:
            i, j = np.triu_indices(len(a), 1)
            da = np.linalg.norm(a[i] - a[j], axis=1)
            db = np.linalg.norm(b[i] - b[j], axis=1)
            ok = da > 4
            if ok.sum() >= 5:
                s = float(np.clip(np.median(db[ok] / da[ok]), 0.85, 1.18))
        x, y, w, h = self.box
        cx, cy = x + w / 2 + d[0], y + h / 2 + d[1]
        w, h = w * s, h * s
        self.box = (cx - w / 2, cy - h / 2, w, h)
        self.prev = gray
        return self.box


def _make_box_tracker(method: str, img, box):
    return _FlowTracker(img, box) if method == "flow" else _CvTracker(method, img, box)


def track_sequence(frames: list[tuple[int, np.ndarray]], seed, mode: str = "box", method: str = "flow",
                   min_conf: float = MIN_CONF) -> list[dict]:
    """Track through `frames` [(frame index, proxy BGR image)] in the given order, starting from frames[0] where the
    object is `seed` (proxy px: [x, y, w, h], or [x, y] for a point). Returns one sample per frame:
    {f, box [x, y, w, h] | None, conf, lost}. Pure: no I/O; the same input gives the same output."""
    import cv2
    if not frames:
        return []
    f0, img0 = frames[0]
    g0 = _gray(img0)
    pt_half = max(8.0, 0.035 * max(g0.shape))  # a point's confidence patch (half side, proxy px)
    if mode == "point":
        box = (seed[0] - pt_half, seed[1] - pt_half, 2 * pt_half, 2 * pt_half)
    else:
        box = tuple(float(v) for v in seed)
    tpl0 = _patch(g0, box)
    if tpl0 is None:
        raise VeosError("BAD_TRACK_ARGS", "the seed box / point is outside the frame", "Check the coordinates with --look.")
    tpl_recent, last_good_wh = tpl0, box[2:]
    seed_crop = g0[max(0, int(box[1])):int(box[1] + box[3]), max(0, int(box[0])):int(box[0] + box[2])].copy()
    recent_crop = seed_crop
    out = [{"f": f0, "box": list(box), "conf": 1.0, "lost": False}]
    tracker = _make_box_tracker(method, img0, box) if mode == "box" else None
    prev_g, pt = g0, np.array([[seed[0], seed[1]]], np.float32).reshape(-1, 1, 2)
    lost = False
    for f, img in frames[1:]:
        g = _gray(img)
        nb = None
        if not lost:
            if mode == "box":
                nb = tracker.update(img)
            else:
                lk = _FlowTracker.LK
                p1, st, _ = cv2.calcOpticalFlowPyrLK(prev_g, g, pt, None, **lk)
                if p1 is not None and st.ravel()[0] == 1:
                    pb, st2, _ = cv2.calcOpticalFlowPyrLK(g, prev_g, p1, None, **lk)
                    if st2.ravel()[0] == 1 and float(np.linalg.norm(pb - pt)) < 2.0:
                        pt = p1
                        nb = (float(p1[0, 0, 0]) - pt_half, float(p1[0, 0, 1]) - pt_half, 2 * pt_half, 2 * pt_half)
        conf = 0.0
        if nb is not None:
            p = _patch(g, nb)
            conf = max(ncc(p, tpl0), ncc(p, tpl_recent))
        if nb is None or conf < min_conf:
            # lost (or never found): search the whole proxy frame for the recent, then the seed template
            best = None
            for crop in (recent_crop, seed_crop):
                if crop.size and crop.shape[0] >= 4 and crop.shape[1] >= 4:
                    r = _search(g, crop, last_good_wh)
                    if r and (best is None or r[0] > best[0]):
                        best = r
            if best and best[0] >= REACQ:
                nb, conf, lost = best[1], best[0], False
                if mode == "box":
                    tracker = _make_box_tracker(method, img, nb)
                else:
                    pt = np.array([[nb[0] + nb[2] / 2, nb[1] + nb[3] / 2]], np.float32).reshape(-1, 1, 2)
            else:
                lost = True
                if nb is None and best:
                    conf = max(conf, best[0])
        if not lost and nb is not None:
            out.append({"f": f, "box": [float(v) for v in nb], "conf": round(float(conf), 3), "lost": False})
            if conf >= KEEP:
                tpl_recent = _patch(g, nb)
                x0, y0 = max(0, int(nb[0])), max(0, int(nb[1]))
                c = g[y0:int(nb[1] + nb[3]), x0:int(nb[0] + nb[2])]
                if c.shape[0] >= 4 and c.shape[1] >= 4:
                    recent_crop = c.copy()
                last_good_wh = nb[2:]
        else:
            out.append({"f": f, "box": None, "conf": round(float(conf), 3), "lost": True})
        prev_g = g
    if mode == "point":
        for s in out:
            if s["box"]:
                b = s["box"]
                s["box"] = [b[0] + b[2] / 2, b[1] + b[3] / 2, 0.0, 0.0]
    return out


def smooth_samples(samples: list[dict]) -> list[dict]:
    """3-tap median over consecutive confident samples (never across a lost one): kills single-sample jitter."""
    out = [dict(s, box=list(s["box"]) if s["box"] else None) for s in samples]
    for i in range(1, len(samples) - 1):
        a, b, c = samples[i - 1], samples[i], samples[i + 1]
        if a["box"] and b["box"] and c["box"]:
            out[i]["box"] = [float(np.median([a["box"][k], b["box"][k], c["box"][k]])) for k in range(4)]
    return out


def densify(samples: list[dict], frames: list[int]) -> list[dict]:
    """Per-frame records for every index in `frames` (sorted) from sparse samples: linear between two confident samples,
    lost between a confident and a lost one; lost frames hold the last confident box (or the next one before any)."""
    by = sorted(samples, key=lambda s: s["f"])
    fs = [s["f"] for s in by]
    out = []
    last = next((s["box"] for s in by if s["box"]), None)
    hold = None
    import bisect
    for f in frames:
        j = bisect.bisect_left(fs, f)
        if j < len(fs) and fs[j] == f:
            s = by[j]
            box, conf, lost = s["box"], s["conf"], s["lost"]
        elif 0 < j < len(fs):
            a, b = by[j - 1], by[j]
            if a["box"] and b["box"]:
                p = (f - a["f"]) / (b["f"] - a["f"])
                box = [a["box"][k] + (b["box"][k] - a["box"][k]) * p for k in range(4)]
                conf, lost = round(min(a["conf"], b["conf"]), 3), False
            else:
                box, conf, lost = None, round(min(a["conf"], b["conf"]), 3), True
        else:
            continue  # outside the tracked span
        if box:
            hold = box
        out.append({"f": f, "box": box if box else (hold or last), "conf": conf, "lost": bool(lost or not box)})
    return out


# ------------------------------------------------------------------------------------------------ decoding
def _probe_wh(ffprobe: str, path: Path) -> tuple[int, int]:
    r = subprocess.run([ffprobe, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                        "-of", "csv=p=0:s=x", str(path)], capture_output=True, text=True)
    try:
        w, h = r.stdout.strip().splitlines()[0].split("x")[:2]
        return int(w), int(h)
    except (ValueError, IndexError):
        raise VeosError("BAD_CLIP", f"cannot read the video size of {path}", "Check the file plays; re-run veos conform.")


def proxy_size(w: int, h: int, long_side: int) -> tuple[int, int]:
    k = min(1.0, long_side / max(w, h))
    pw, ph = max(16, int(round(w * k / 2)) * 2), max(16, int(round(h * k / 2)) * 2)
    return pw, ph


def decode_run(ffmpeg: str, path: Path, start: int, count: int, pw: int, ph: int, keep) -> dict[int, np.ndarray]:
    """Decode `count` frames of `path` from frame `start` (30 fps) into pw x ph BGR; keep only offsets i with keep(i)."""
    seek = max(0.0, (start - 0.5) / FPS)
    cmd = [ffmpeg, "-v", "error", "-threads", "2", "-ss", f"{seek:.4f}", "-i", str(path), "-an", "-frames:v", str(count),
           "-vf", f"fps={FPS},scale={pw}:{ph}:flags=area", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    size, out, i = pw * ph * 3, {}, 0
    try:
        while i < count:
            buf = p.stdout.read(size)
            if not buf or len(buf) < size:
                break
            if keep(i):
                out[i] = np.frombuffer(buf, np.uint8).reshape(ph, pw, 3).copy()
            i += 1
    finally:
        p.stdout.close()
        p.wait()
    return out


def _cover(sw: int, sh: int, W: int = 1080, H: int = 1920) -> tuple[float, float, float]:
    s = max(W / sw, H / sh)
    return s, (W - sw * s) / 2, (H - sh * s) / 2


# ------------------------------------------------------------------------------------------------ planning the frames
def _edit_plan(pr, clip: str | None, fa: int, fb: int) -> list[dict]:
    """Edit frames fa..fb (inclusive) -> [{f, src, sf}] through work/cutmap.json (frames of other sources dropped)."""
    cp = pr.work / "cutmap.json"
    if not cp.exists():
        raise VeosError("NO_CUTMAP", "work/cutmap.json missing", "Run `veos cut` first (edit-time tracks follow the cut map).")
    cm = read_json(cp)
    out = []
    for seg in cm.get("segments", []):
        if clip and seg.get("src") != clip:
            continue
        for n in range(max(fa, seg["f0"]), min(fb + 1, seg["f1"])):
            out.append({"f": n, "src": seg["src"], "sf": seg["in_frame"] + (n - seg["f0"])})
    return out


def _runs(plan: list[dict]) -> list[list[dict]]:
    """Split into runs of consecutive source frames of one source (one ffmpeg decode each)."""
    runs: list[list[dict]] = []
    for e in plan:
        if runs and runs[-1][-1]["src"] == e["src"] and runs[-1][-1]["sf"] + 1 == e["sf"] and runs[-1][-1]["f"] + 1 == e["f"]:
            runs[-1].append(e)
        else:
            runs.append([e])
    return runs


def _resolve_clip(pr, clip: str | None):
    """-> ("edit", source id | None, None) or ("clip", name, {"kind": "file"|"asset", "path", "w", "h", "frames"})."""
    if clip is None:
        return "edit", None, None
    sp = pr.work / "sources.json"
    ids = {s.get("id") for s in (read_json(sp).get("sources") or [])} if sp.exists() else set()
    cp = pr.work / "cutmap.json"
    if cp.exists():
        ids |= {s.get("src") for s in read_json(cp).get("segments", [])}
    if clip in ids:
        return "edit", clip, None
    meta = pr.root / "plan" / "assets" / clip / "meta.json"
    if meta.exists():
        m = read_json(meta)
        return "clip", clip, {"kind": "asset", "path": meta.parent, "w": int(m["w"]), "h": int(m["h"]), "frames": int(m["frames"])}
    p = Path(clip).expanduser()
    if not p.is_absolute():
        p = pr.root / p if (pr.root / p).exists() else p
    if p.is_file():
        return "clip", p.stem, {"kind": "file", "path": p.resolve()}
    if re.match(r"^[a-z][a-z0-9+.-]*://", clip, re.I):
        raise VeosError("NO_FETCH", "tracks are made from local footage only", "Pass a source id, a local video file or an asset name.")
    raise VeosError("BAD_CLIP", f"--clip '{clip}' is not a source id, a plan/assets video or a video file",
                    f"Known sources: {', '.join(sorted(i for i in ids if i)) or 'none'}.")


def _next_id(pr) -> str:
    d = pr.root / "plan" / "tracks"
    k = 1
    while (d / f"track{k}.json").exists():
        k += 1
    return f"track{k}"


def _frame_reframe(pr):
    """The reel's base reframe {s, tx, ty} (E-16b) on a full stage, or None (identity / no tokens / no faces)."""
    try:
        from .framing import for_project
        tl = read_json(pr.root / "plan" / "timeline.json") if (pr.root / "plan" / "timeline.json").exists() else {}
        fp = pr.work / "face.edit.json"
        boxes = read_json(fp).get("boxes") if fp.exists() else None
        rf = for_project(pr, tl, boxes) if boxes else None
    except (ValueError, OSError, KeyError, TypeError):
        rf = None
    if not rf or rf.get("identity"):
        return None
    return {"s": rf["s"], "tx": rf["tx"], "ty": rf["ty"]}


# ------------------------------------------------------------------------------------------------ preview
def _preview(path: Path, shots: list[tuple[int, np.ndarray, list | None, bool]]) -> None:
    import cv2
    tiles = []
    for f, img, box, lost in shots:
        im = img.copy()
        if box:
            x, y, w, h = box
            col = (0, 0, 255) if lost else (0, 230, 0)
            if w > 0:
                cv2.rectangle(im, (int(x), int(y)), (int(x + w), int(y + h)), col, 2)
            else:
                cv2.circle(im, (int(x), int(y)), 8, col, 2)
        cv2.putText(im, f"f{f}{' LOST' if lost else ''}", (6, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        tiles.append(im)
    hmax = max(t.shape[0] for t in tiles)
    tiles = [cv2.copyMakeBorder(t, 0, hmax - t.shape[0], 0, 4, cv2.BORDER_CONSTANT) for t in tiles]
    path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(path), np.hstack(tiles), [cv2.IMWRITE_JPEG_QUALITY, 85])


# ------------------------------------------------------------------------------------------------ main
def main(args, project):
    import cv2
    pr = need_project(project)
    t0 = time.perf_counter()
    if not args.look and not args.box and not args.point:
        raise VeosError("BAD_TRACK_ARGS", "give the object with --box x,y,w,h or --point x,y", "Run with --look first to read the coordinates.")
    seed = parse_nums(args.box, 4, "box") if args.box else (parse_nums(args.point, 2, "point") if args.point else None)
    mode = "box" if args.box else "point"
    tid = args.id or _next_id(pr)
    if not ID_RE.match(tid):
        raise VeosError("BAD_TRACK_ARGS", f"track id '{tid}' must be letters, digits, - or _ (max 40)", "Example: --id phone")
    if not 0 < args.min_conf < 1:
        raise VeosError("BAD_TRACK_ARGS", "--min-conf must be between 0 and 1", "The default 0.5 suits most objects.")
    step = max(1, int(args.step))
    space, clip, info = _resolve_clip(pr, args.clip)
    tt = tools()
    f_at = int(round(args.at * FPS))
    f_from = int(round((args.t_from if args.t_from is not None else args.at) * FPS))
    f_to = int(round((args.to if args.to is not None else args.at + 4.0) * FPS))
    if f_from > f_at or f_to < f_at:
        raise VeosError("BAD_TRACK_ARGS", "--from must be <= --at <= --to", "Example: --from 1.0 --at 1.5 --to 4.0")
    span = (f_to - f_from) / FPS
    if span > args.max_span + 1e-6:
        raise VeosError("TRACK_TOO_LONG", f"{span:.1f} s asked; one run tracks at most {args.max_span:g} s",
                        "Track only the span the anchored scene is on screen (or raise --max-span knowingly).")

    # --- what to decode: [{f, src, sf}] and per-source (path, size, proxy, mapping to the output coordinates)
    srcs: dict[str, dict] = {}
    if space == "edit":
        plan = _edit_plan(pr, clip, f_from, f_to)
        if not plan or not any(e["f"] == f_at for e in plan):
            raise VeosError("BAD_TRACK_ARGS", f"edit time {args.at:g} s is not in the cut map{' for source ' + clip if clip else ''}",
                            "Pick --at inside the reel (and inside the --clip source's spans).")
        for sid in {e["src"] for e in plan}:
            p = pr.work / "src" / f"{sid}.mp4"
            if not p.exists():
                raise VeosError("NO_CONFORM", f"work/src/{sid}.mp4 missing", "Run `veos conform` first.")
            sw, sh = _probe_wh(tt.ffprobe, p)
            pw, ph = proxy_size(sw, sh, args.proxy)
            cs, ox, oy = _cover(sw, sh)
            k = sw / pw  # proxy -> source px
            srcs[sid] = {"path": p, "pw": pw, "ph": ph, "to_out": (cs * k, ox, oy), "size": (1080, 1920)}
        size = [1080, 1920]
    else:
        if info["kind"] == "asset":
            w, h, nfr = info["w"], info["h"], info["frames"]
        else:
            w, h = _probe_wh(tt.ffprobe, info["path"])
            nfr = None
        f_to = min(f_to, nfr - 1) if nfr else f_to
        plan = [{"f": n, "src": clip, "sf": n} for n in range(f_from, f_to + 1)]
        pw, ph = proxy_size(w, h, args.proxy)
        srcs[clip] = {"path": info["path"], "pw": pw, "ph": ph, "to_out": (w / pw, 0.0, 0.0), "size": (w, h), "asset": info["kind"] == "asset"}
        size = [w, h]

    # coordinates in -> proxy: the seed is in output px (edit: after the cover crop, before the reframe)
    at = next(e for e in plan if e["f"] == f_at)
    k_out, ox, oy = srcs[at["src"]]["to_out"]
    to_proxy = (lambda x, y: ((x - ox) / k_out, (y - oy) / k_out))
    to_out = (lambda s: (lambda x, y: (x * srcs[s]["to_out"][0] + srcs[s]["to_out"][1], y * srcs[s]["to_out"][0] + srcs[s]["to_out"][2])))

    # --- decode (sampled frames only), one ffmpeg run per contiguous span
    sampled = {e["f"] for e in plan if (e["f"] - f_at) % step == 0}
    runs = _runs(plan)
    for r in runs:  # always keep each run's first and last frame (cuts are tracking boundaries)
        sampled |= {r[0]["f"], r[-1]["f"]}
    imgs: dict[int, np.ndarray] = {}
    for r in runs:
        need = [e for e in r if e["f"] in sampled]
        if args.look:
            need = [e for e in r if e["f"] == f_at]
            if not need:
                continue
        s = srcs[r[0]["src"]]
        if s.get("asset"):
            for e in need:
                im = cv2.imread(str(s["path"] / f"f{e['sf']:05d}.jpg"))
                if im is not None:
                    imgs[e["f"]] = cv2.resize(im, (s["pw"], s["ph"]), interpolation=cv2.INTER_AREA)
            continue
        first = need[0]["sf"]
        offs = {e["sf"] - first: e["f"] for e in need}
        got = decode_run(tt.ffmpeg, s["path"], first, need[-1]["sf"] - first + 1, s["pw"], s["ph"], lambda i: i in offs)
        for i, im in got.items():
            imgs[offs[i]] = im
    if f_at not in imgs:
        raise VeosError("BAD_CLIP", f"could not decode the frame at {args.at:g} s", "Check the time is inside the clip.")

    tdir = pr.root / "plan" / "tracks"
    if args.look:
        import cv2 as _cv
        im = imgs[f_at].copy()
        for i in range(1, int(max(size) / 100) + 1):
            x, y = (i * 100 - ox) / k_out, (i * 100 - oy) / k_out
            thick = 2 if i % 5 == 0 else 1
            _cv.line(im, (int(x), 0), (int(x), im.shape[0]), (255, 255, 0), thick)
            _cv.line(im, (0, int(y)), (im.shape[1], int(y)), (255, 255, 0), thick)
            if i % 2 == 0:
                _cv.putText(im, str(i * 100), (int(x) + 2, 12), _cv.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)
                _cv.putText(im, str(i * 100), (2, int(y) - 2), _cv.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)
        out = tdir / f"look_{args.at:g}.jpg"
        tdir.mkdir(parents=True, exist_ok=True)
        _cv.imwrite(str(out), im, [_cv.IMWRITE_JPEG_QUALITY, 88])
        return {"look": pr.rel(out), "space": space, "size": size, "frame": f_at,
                "note": "grid lines every 100 px of the seed coordinates (thick every 500)"}

    # --- track forwards from --at, and backwards to --from
    method = available_method(args.method) if mode == "box" else "lk"
    if mode == "box":
        x, y, w, h = seed
        px0, py0 = to_proxy(x, y)
        seed_p = [px0, py0, w / k_out, h / k_out]
    else:
        seed_p = list(to_proxy(*seed))
    fwd = [(f, imgs[f]) for f in sorted(imgs) if f >= f_at]
    bwd = [(f, imgs[f]) for f in sorted((f for f in imgs if f <= f_at), reverse=True)]
    samples = smooth_samples(track_sequence(fwd, seed_p, mode, method, args.min_conf))
    if len(bwd) > 1:
        samples = smooth_samples(track_sequence(bwd, seed_p, mode, method, args.min_conf))[1:] + samples
    src_of = {e["f"]: e["src"] for e in plan}
    for s in samples:  # proxy -> output coordinates (edit: footage px of the 1080x1920 frame)
        if s["box"]:
            m = to_out(src_of[s["f"]])
            x0, y0 = m(s["box"][0], s["box"][1])
            k = srcs[src_of[s["f"]]]["to_out"][0]
            s["box"] = [x0, y0, s["box"][2] * k, s["box"][3] * k]
    dense = densify(samples, [e["f"] for e in plan])
    rf = _frame_reframe(pr) if space == "edit" else None
    frames = []
    for d in dense:
        b = d["box"] or [0, 0, 0, 0]
        if rf:  # output frame on a full stage after the base reframe (framing.apply_box)
            b = [rf["s"] * b[0] + rf["tx"], rf["s"] * b[1] + rf["ty"], rf["s"] * b[2], rf["s"] * b[3]]
        rec = {"f": d["f"], "x": round(b[0], 1), "y": round(b[1], 1), "w": round(b[2], 1), "h": round(b[3], 1), "conf": d["conf"]}
        if d["lost"]:
            rec["lost"] = True
        frames.append(rec)
    nl = sum(1 for r in frames if r.get("lost"))
    runs_lost, cur = [], 0
    for r in frames:
        if r.get("lost"):
            cur += 1
        elif cur:
            runs_lost.append(cur)
            cur = 0
    if cur:
        runs_lost.append(cur)
    confs = [r["conf"] for r in frames if not r.get("lost")]
    el = time.perf_counter() - t0
    doc = {"version": 1, "id": tid, "space": space, "clip": clip, "mode": mode, "method": method, "fps": FPS,
           "source": pr.rel(srcs[at["src"]]["path"]) if space == "edit" else pr.rel(info["path"]),
           "size": size, "at": r3(args.at), "from": r3(f_from / FPS), "to": r3(frames[-1]["f"] / FPS if frames else f_to / FPS),
           "seed": {"f": f_at, mode: [round(v, 1) for v in seed]}, "reframe": rf, "min_conf": args.min_conf,
           "proxy": {"w": srcs[at["src"]]["pw"], "h": srcs[at["src"]]["ph"], "step": step},
           "frames": frames,
           "stats": {"frames": len(frames), "tracked": len(samples), "lost": nl, "longest_lost": max(runs_lost or [0]),
                     "mean_conf": round(sum(confs) / len(confs), 3) if confs else 0.0, "seconds": round(el, 2),
                     "ms_per_frame": round(1000 * el / max(1, len(frames)), 1)}}
    tdir.mkdir(parents=True, exist_ok=True)
    out = tdir / f"{tid}.json"
    write_json(out, doc, indent=None)
    # preview: six frames spread over the span, the box drawn in proxy px
    keys = sorted(imgs)
    pick = sorted({keys[int(round(i * (len(keys) - 1) / 5))] for i in range(6)}) if len(keys) > 1 else keys
    sm = {s["f"]: s for s in samples}
    shots = []
    for f in pick:
        s = sm.get(f)
        b = None
        if s and s["box"]:
            kk, ox2, oy2 = srcs[src_of[f]]["to_out"]
            b = [(s["box"][0] - ox2) / kk, (s["box"][1] - oy2) / kk, s["box"][2] / kk, s["box"][3] / kk]
        shots.append((f, imgs[f], b, bool(s and s["lost"])))
    prev = tdir / f"{tid}.preview.jpg"
    _preview(prev, shots)
    warnings = []
    if nl:
        warnings.append(f"{nl} of {len(frames)} frames lost (confidence < {args.min_conf}); longest run {max(runs_lost)} frames: "
                        "anchors hold or fade there (anchor.lost)")
    if method == "flow" and args.method in ("csrt", "kcf"):
        warnings.append(f"{args.method} is not in this OpenCV build; the built-in flow tracker was used")
    return {"track": pr.rel(out), "preview": pr.rel(prev), "id": tid, "space": space, "mode": mode, "method": method,
            "frames": len(frames), "from": doc["from"], "to": doc["to"], "lost": nl, "mean_conf": doc["stats"]["mean_conf"],
            "ms_per_frame": doc["stats"]["ms_per_frame"], "warnings": warnings}
