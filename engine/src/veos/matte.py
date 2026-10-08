"""`veos faces` and `veos matte`: face boxes, and the person cut-out (RVM mobilenetv3 ONNX) only where a reel needs it.

    veos faces --project P              face boxes for every talking-head source (prep; fast: no cut-out model)
    veos matte --project P              the person cut-out of the frames the cut keeps (+ a margin); the rest of the
                                        source is written transparent, so the alpha video keeps the source's frame count
    veos matte --if-needed --project P  the same, only when the plan needs the cut-out (cutout.needs_cutout): a scene
                                        behind the presenter or a head breakout; otherwise it reports why it skipped
    veos matte --all                    every frame of every source (the old prep behaviour; also with no cut map)

Outputs (per talking-head source id):
  work/face/<id>.json   SPEC section 3 face format (`veos faces`; `veos matte` writes it too when it is missing)
  work/matte/<id>.mp4   gray H.264 alpha, same frame count as the source
  work/matte/<id>.json  which source frame ranges were cut out ("all" or [[a, b], ...]); a matte without it covers all
A source whose matte already covers the wanted frames is skipped (`--force` redoes it).

HOW A BROWSER MUST READ matte/<id>.mp4
  The file is yuv420p H.264 with the FULL-RANGE flag set (color_range=pc, x264 fullrange=1) and neutral chroma, so
  alpha = the luma plane: 0 = transparent, 255 = fully opaque. Draw each frame (requestVideoFrameCallback /
  WebCodecs VideoFrame) to a canvas or WebGL texture and take the RED channel (R == G == B == luma). A decoder that
  honours the range flag gives 0..255 directly. If a browser ignores the flag (treats it as limited range, so
  transparent reads 16 and opaque 235), correct with  a = clamp((v - 16) / 219).
  Check once: a background pixel must read 0 and the chest 255.
  ffmpeg: `-i matte.mp4 -vf format=gray` returns the same values (flag honoured).

Pipeline per frame: decode (ffmpeg rgb24 pipe) -> face box (BlazeFace + 640 px crop fallback) -> RVM (state carried,
reset on hard cuts) -> keep only the components near the face / the previous mask (drops chair-back fragments) -> EMA
-> bilinear upscale + guided-filter edge refinement -> gray frame piped to ffmpeg.
"""
from __future__ import annotations

import json
import os
import queue
import subprocess
import threading
import time
import urllib.request
from pathlib import Path

import numpy as np

from .core import FPS, Project, VeosError, need_project, r3, read_json, tools, write_json
from . import face as facemod

RVM_URL = "https://github.com/PeterL1n/RobustVideoMatting/releases/download/v1.0.0/rvm_mobilenetv3_fp32.onnx"
FACE_EXPAND = (0.25, 0.25)       # dilate the face box by this fraction of w / h each side for component selection
KEEP_PREV_OVERLAP = 0.30
EMA_PREV = 0.30                  # weight of the previous alpha
EMA_MAX_DELTA = 0.20             # only smooth where |alpha - prev| is below this (no lag on fast hands)
CUT_DIFF = 28.0                  # mean abs thumbnail difference (0-255) that counts as a hard cut ...
CUT_RATIO = 5.0                  # ... and must exceed this multiple of the recent median difference
WARMUP_F = 12                    # frames cut out before each kept range: the recurrent state settles before it shows
TAIL_F = 3                       # frames cut out after each kept range
JOIN_F = 30                      # kept ranges closer than this are cut out as one (a new warm-up would cost more)


def add_args(p, cmd):
    p.add_argument("--id", default=None, help="source id (default: every talking-head source)")
    p.add_argument("--input", default=None, help="standalone video file (use with --id; no sources.json needed)")
    p.add_argument("--threads", type=int, default=min(14, os.cpu_count() or 4))
    p.add_argument("--out", default=None, help="output folder when no --project is given")
    p.add_argument("--force", action="store_true", help="redo sources that are already done")
    if cmd == "matte":
        p.add_argument("--quality", action="store_true", help="full-resolution RVM, downsample_ratio 0.25 (slower)")
        p.add_argument("--all", action="store_true", help="cut out every frame of the source, not only what the cut keeps")
        p.add_argument("--if-needed", action="store_true",
                       help="only when the plan needs the cut-out (a scene behind the presenter or a head breakout)")


# ---------------------------------------------------------------- helpers
def _probe(path: Path) -> dict:
    r = subprocess.run([tools().ffprobe, "-v", "error", "-select_streams", "v:0", "-show_streams", "-of", "json", str(path)],
                       capture_output=True)
    try:
        s = json.loads(r.stdout.decode("utf-8", "replace"))["streams"][0]
    except Exception as e:  # noqa: BLE001
        raise VeosError("PROBE_FAILED", f"ffprobe could not read {path.name}", "The file may be corrupt.") from e
    w, h = int(s["width"]), int(s["height"])
    rot = int(float(s.get("tags", {}).get("rotation", 0) or 0))
    for sd in s.get("side_data_list", []) or []:
        if "rotation" in sd:
            rot = int(round(float(sd["rotation"])))
    if abs(rot) % 180 == 90:
        w, h = h, w
    num, _, den = (s.get("avg_frame_rate") or "30/1").partition("/")
    d = float(den or 1)
    fps = float(num) / d if d else float(FPS)
    return {"w": w, "h": h, "fps": fps or float(FPS)}


def _count_frames(path: Path) -> int:
    r = subprocess.run([tools().ffprobe, "-v", "error", "-select_streams", "v:0", "-count_frames",
                        "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", str(path)], capture_output=True)
    try:
        return int(r.stdout.decode().strip().split()[0])
    except Exception:  # noqa: BLE001
        return -1


def _rvm_session(threads: int):
    import onnxruntime as ort
    p = tools().models / "rvm" / "rvm_mobilenetv3_fp32.onnx"
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        try:
            urllib.request.urlretrieve(RVM_URL, p)
        except Exception as e:  # noqa: BLE001
            raise VeosError("MODEL_MISSING", f"RVM model not found and download failed ({e})",
                            "Run `veos doctor` / /reel-setup to download the models.") from e
    so = ort.SessionOptions()
    so.intra_op_num_threads = threads
    so.inter_op_num_threads = 1
    return ort.InferenceSession(str(p), so, providers=["CPUExecutionProvider"])


# ---------------------------------------------------------------- clean-up
def keep_components(alpha: np.ndarray, box: list | None, prev_kept: np.ndarray | None, scale: float):
    """alpha float [0,1] at processing size. Returns (soft alpha with stray components removed, kept binary mask)."""
    import cv2
    binary = (alpha > 0.5).astype(np.uint8)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(binary, connectivity=8)
    if n <= 1:
        return alpha, binary
    keep = np.zeros(n, bool)
    H, W = binary.shape
    if box is not None:
        x, y, w, h = [v * scale for v in box[:4]]
        x0, x1 = int(max(0, x - FACE_EXPAND[0] * w)), int(min(W, x + w * (1 + FACE_EXPAND[0])))
        y0, y1 = int(max(0, y - FACE_EXPAND[1] * h)), int(min(H, y + h * (1 + FACE_EXPAND[1])))
        if x1 > x0 and y1 > y0:
            keep[np.unique(lab[y0:y1, x0:x1])] = True
    if prev_kept is not None and prev_kept.any():
        ov = np.bincount(lab[prev_kept > 0], minlength=n).astype(np.float64)
        keep |= (ov / np.maximum(stats[:, cv2.CC_STAT_AREA], 1)) > KEEP_PREV_OVERLAP
    keep[0] = False
    if not keep.any():  # no face and no history: keep the biggest blob
        keep[1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))] = True
    kept = keep[lab].astype(np.uint8)
    halo = cv2.dilate(kept, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))
    return alpha * halo, kept


def refine_up(alpha: np.ndarray, rgb: np.ndarray, size: tuple[int, int], guided: bool) -> np.ndarray:
    """Upscale float alpha to (w, h) with bilinear and refine edges with a guided filter inside the edge band."""
    import cv2
    w, h = size
    a = alpha if alpha.shape == (h, w) else cv2.resize(alpha, (w, h), interpolation=cv2.INTER_LINEAR)
    if guided and hasattr(cv2, "ximgproc"):
        ys, xs = np.where(a[::4, ::4] > 0.02)
        if len(ys):
            pad = 24
            y0, y1 = max(0, ys.min() * 4 - pad), min(h, ys.max() * 4 + pad)
            x0, x1 = max(0, xs.min() * 4 - pad), min(w, xs.max() * 4 + pad)
            sub = np.ascontiguousarray(a[y0:y1, x0:x1])
            guide = cv2.cvtColor(rgb[y0:y1, x0:x1], cv2.COLOR_RGB2GRAY)
            gf = cv2.ximgproc.guidedFilter(guide, sub, 6, 40.0)
            band = ((sub > 0.03) & (sub < 0.97)).astype(np.uint8)
            band = cv2.dilate(band, np.ones((9, 9), np.uint8)).astype(bool)
            a = a.copy()
            a[y0:y1, x0:x1] = np.where(band, np.clip(gf, 0, 1), sub)
    return a


# ---------------------------------------------------------------- one source
def kept_ranges(cut: dict, sid: str, n_src: int) -> list[list[int]]:
    """The source frames of `sid` the cut map keeps, widened by the warm-up / tail margins and joined when close:
    [[a, b), ...] in source frames, inside [0, n_src)."""
    spans = []
    for seg in cut.get("segments") or []:
        if seg.get("src") != sid:
            continue
        a = int(seg["in_frame"])
        b = a + int(seg["f1"]) - int(seg["f0"])
        spans.append([max(0, a - WARMUP_F), min(n_src, b + TAIL_F)])
    spans.sort()
    out: list[list[int]] = []
    for a, b in spans:
        if out and a - out[-1][1] < JOIN_F:
            out[-1][1] = max(out[-1][1], b)
        elif b > a:
            out.append([a, b])
    return out


def covers(done, want) -> bool:
    """Does an existing cut-out ("all", ranges, or None = none yet) cover the wanted ranges ("all" or ranges)?"""
    if done is None:
        return False
    if done == "all":
        return True
    if want == "all":
        return False
    return all(any(a >= x and b <= y for x, y in done) for a, b in want)


def process(src: Path, W: int, H: int, fps: float, out_mp4: Path | None, out_face: Path | None, quality: bool,
            threads: int, cuts: set, expect_frames, source_id: str, log, faces: bool = True,
            ranges: list | None = None, known_boxes: list | None = None) -> dict:
    """One decode pass over a source.
    faces False (animated plates): no face tracking; the face file is written with empty boxes.
    out_mp4 None: the face-only pass of `veos faces` (no cut-out model at all).
    ranges: the source frame ranges to cut out (None = every frame); frames outside are written transparent.
    known_boxes: the boxes of an earlier `veos faces` pass, used instead of tracking again (the face file is kept)."""
    import cv2
    cv2.setNumThreads(4)
    ff = tools().ffmpeg
    cutout = out_mp4 is not None
    t_load = time.time()
    sess = _rvm_session(threads) if cutout else None
    tracker = facemod.FaceTracker() if faces and known_boxes is None else None
    log(f"models loaded in {time.time() - t_load:.1f}s")

    if quality:
        PW, PH, ds = W, H, 0.25
    else:
        s = 960.0 / max(W, H)
        PW, PH, ds = max(2, int(round(W * s))), max(2, int(round(H * s))), 0.5
    scale = PW / W
    dsr = np.array([ds], dtype=np.float32)
    inside = (lambda i: True) if ranges is None else (lambda i: any(a <= i < b for a, b in ranges))
    starts = {a for a, _ in ranges} if ranges else set()

    def zero():
        return [np.zeros((1, 1, 1, 1), np.float32) for _ in range(4)]

    dec = subprocess.Popen([ff, "-v", "error", "-i", str(src), "-an", "-fps_mode", "passthrough", "-f", "rawvideo",
                            "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=W * H * 3 * 2)
    enc = None
    if cutout:
        out_mp4.parent.mkdir(parents=True, exist_ok=True)
        enc = subprocess.Popen([ff, "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "gray", "-s", f"{W}x{H}",
                                "-framerate", f"{fps:.6f}", "-i", "-",
                                "-vf", "scale=in_range=full:out_range=full,format=yuv420p",
                                "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-x264-params", "fullrange=1",
                                "-color_range", "pc", "-colorspace", "bt709", "-color_primaries", "bt709",
                                "-color_trc", "bt709", "-movflags", "+faststart", str(out_mp4)],
                               stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    err: list = []
    q1: queue.Queue = queue.Queue(6)
    q2: queue.Queue = queue.Queue(6)
    nbytes = W * H * 3
    blank = bytes(W * H)

    def reader():
        try:
            while True:
                buf = dec.stdout.read(nbytes)
                if len(buf) < nbytes:
                    break
                q1.put(np.frombuffer(buf, np.uint8).reshape(H, W, 3))
        except BaseException as e:  # noqa: BLE001
            err.append(e)
        finally:
            q1.put(None)

    def post():
        prev_kept = None
        prev_a = None
        try:
            while True:
                item = q2.get()
                if item is None:
                    break
                if item == "blank":  # a frame the reel never shows: transparent, and the smoothing starts afresh
                    prev_kept = prev_a = None
                    enc.stdin.write(blank)
                    continue
                rgb, a, box, reset = item
                if reset:
                    prev_kept = prev_a = None
                a, kept = keep_components(a, box, prev_kept, scale)
                if prev_a is not None:
                    d = np.abs(a - prev_a)
                    a = np.where(d < EMA_MAX_DELTA, (1 - EMA_PREV) * a + EMA_PREV * prev_a, a)
                prev_kept, prev_a = kept, a
                full = refine_up(a, rgb, (W, H), guided=(PW != W))
                enc.stdin.write(np.clip(full * 255 + 0.5, 0, 255).astype(np.uint8).tobytes())
        except BaseException as e:  # noqa: BLE001
            err.append(e)
            while q2.get() is not None:  # drain so the producer never blocks
                pass

    tr = threading.Thread(target=reader, daemon=True)
    tp = threading.Thread(target=post, daemon=True) if cutout else None
    tr.start()
    if tp:
        tp.start()

    boxes: list = []
    states = zero()
    last_box = None
    prev_thumb = None
    diffs: list = []
    n = 0
    cut_frames: list = []
    cut_out = 0
    t0 = time.time()
    try:
        while True:
            rgb = q1.get()
            if rgb is None or err:
                break
            here = cutout and inside(n)
            if tracker is None and not here:  # nothing to look at in this frame
                prev_thumb = None
                if cutout:
                    q2.put("blank")
                if known_boxes is None:
                    boxes.append(None)
                n += 1
                continue
            small = rgb if (PW, PH) == (W, H) else cv2.resize(rgb, (PW, PH), interpolation=cv2.INTER_AREA)
            thumb = cv2.cvtColor(cv2.resize(small, (48, 84), interpolation=cv2.INTER_AREA), cv2.COLOR_RGB2GRAY).astype(np.float32)
            reset = n == 0 or n in starts
            if prev_thumb is not None:
                d = float(np.abs(thumb - prev_thumb).mean())
                base = max(float(np.median(diffs[-15:])) if diffs else 0.0, 2.0)
                if n in cuts or (d > CUT_DIFF and d > CUT_RATIO * base):
                    reset = True
                    cut_frames.append(n)
                diffs.append(d)
            prev_thumb = thumb
            if reset:
                states = zero()
                if tracker:
                    tracker.reset()
                last_box = None
            if known_boxes is not None:
                box = known_boxes[n] if n < len(known_boxes) else None
            else:
                box = tracker.detect(rgb) if tracker else None
                boxes.append(box)
            if box:
                last_box = box
            if cutout:
                if here:
                    src_t = np.ascontiguousarray((small.astype(np.float32) * (1 / 255.0)).transpose(2, 0, 1)[None])
                    o = sess.run(None, dict(src=src_t, r1i=states[0], r2i=states[1], r3i=states[2], r4i=states[3],
                                            downsample_ratio=dsr))
                    states = o[2:]
                    q2.put((rgb, o[1][0, 0].copy(), last_box, reset))
                    cut_out += 1
                else:
                    q2.put("blank")
            n += 1
            if n % 150 == 0:
                log(f"{n} frames, {n / (time.time() - t0):.1f} fps")
    finally:
        q2.put(None)
        if tp:
            tp.join()
        enc_err = ""
        if enc:
            try:
                enc.stdin.close()
            except Exception:  # noqa: BLE001
                pass
        dec.stdout.close()
        dec.wait()
        if enc:
            enc_err = enc.stderr.read().decode("utf-8", "replace")
            enc.wait()
    wall = time.time() - t0
    if err:
        raise VeosError("MATTE_FAILED", f"{type(err[0]).__name__}: {err[0]}", "See logs/matte.log.")
    if enc and enc.returncode != 0:
        raise VeosError("TOOL_FAILED", "ffmpeg alpha encode failed: " + enc_err.strip()[-300:], "See logs/matte.log.")

    want = expect_frames if expect_frames else n
    if n != want:
        raise VeosError("FRAME_MISMATCH", f"decoded {n} frames but the source has {want}", "Conform the source first (`veos conform`).")
    res = {"id": source_id, "frames": n, "fps_achieved": round(n / wall, 2), "s_per_60s": round(60 * FPS / (n / wall), 1),
           "seconds": round(wall, 1), "faces": faces}
    if cutout:
        out_frames = _count_frames(out_mp4)
        if out_frames != n:
            raise VeosError("FRAME_MISMATCH", f"alpha video has {out_frames} frames, expected {n}", "Re-run `veos matte`.")
        write_json(out_mp4.with_suffix(".json"), {"version": 1, "source": source_id, "frames": n,
                                                  "ranges": "all" if ranges is None else ranges}, indent=None)
        res.update({"cut_out_frames": cut_out, "mode": "quality" if quality else "default", "proc_size": [PW, PH],
                    "ds": ds, "matte_mb": round(out_mp4.stat().st_size / 2**20, 2)})
    if known_boxes is None and out_face is not None:
        fb = facemod.finalize(boxes)
        write_json(out_face, {"version": 1, "source": source_id, "fps": FPS if abs(fps - FPS) < 0.01 else r3(fps),
                              "frames": n, "boxes": fb}, indent=None)
        cov = sum(1 for b in fb if b) / max(n, 1)
        res.update({"face_coverage_pct": round(100 * cov, 1),
                    "face_fallback_frames": tracker.fallback_frames if tracker else 0,
                    "hard_cuts": cut_frames, "face_kb": round(out_face.stat().st_size / 1024, 1)})
    return res


def _matte_done(proj: Project, sid: str):
    """What an existing cut-out of `sid` covers: "all", [[a, b], ...], or None (no cut-out)."""
    mp4 = proj.work / "matte" / f"{sid}.mp4"
    if not mp4.exists():
        return None
    meta = proj.work / "matte" / f"{sid}.json"
    if not meta.exists():
        return "all"  # made before the per-range cut-out: every frame
    try:
        return read_json(meta).get("ranges") or "all"
    except ValueError:
        return None


def _known_boxes(proj: Project, sid: str, frames) -> list | None:
    fp = proj.work / "face" / f"{sid}.json"
    if not fp.exists():
        return None
    try:
        d = read_json(fp)
    except ValueError:
        return None
    boxes = d.get("boxes")
    return boxes if isinstance(boxes, list) and (not frames or len(boxes) == frames) else None


# ---------------------------------------------------------------- command
def main(args, project: Project | None) -> dict:
    tools()
    faces_only = getattr(args, "cmd", "matte") == "faces"
    force = bool(getattr(args, "force", False))
    every = bool(getattr(args, "all", False))
    quality = bool(getattr(args, "quality", False))
    jobs: list = []
    need = None
    if args.input:
        if not args.id:
            raise VeosError("BAD_ARGS", "--input needs --id", "Pass e.g. --id A.")
        inp = Path(args.input)
        if not inp.exists():
            raise VeosError("NO_INPUT", f"input not found: {inp}", "Check the path.")
        jobs.append({"id": args.id, "src": inp, "cuts": set(), "frames": None})
    else:
        proj = need_project(project)
        sj = proj.work / "sources.json"
        if not sj.exists():
            raise VeosError("NO_SOURCES", "work/sources.json not found", "Run `veos ingest` first, or pass --input FILE --id X.")
        sdoc = read_json(sj)
        plates = sdoc.get("source_type") == "animated_plates"
        if sdoc.get("source_type") == "voiceover_only" and not args.id:  # E-12: no presenter, nothing to cut out
            return {"skipped": True, "reason": "voice-over reel: no presenter footage, so no matte and no face boxes",
                    "sources": []}
        if getattr(args, "if_needed", False):
            from .cutout import needs_cutout
            need = needs_cutout(proj)
            if not need["needed"]:
                return {"skipped": True, "needed": False, "why": need["why"], "sources": []}
        for s in sdoc["sources"]:
            if s.get("kind") != "talking-head" or (args.id and s["id"] != args.id):
                continue
            conf = proj.work / "src" / f"{s['id']}.mp4"
            cuts = {int(round(g["start"] * FPS)) for g in s.get("segments", [])[1:]}
            jobs.append({"id": s["id"], "src": conf if conf.exists() else proj.abs(s["path"]), "cuts": cuts,
                         "frames": s.get("frames") if conf.exists() else None, "plates": plates})
        if not jobs:
            raise VeosError("NO_SOURCE", f"no talking-head source{' with id ' + args.id if args.id else ''} in sources.json",
                            "Check work/sources.json (kind must be talking-head).")
    base = project.root if project else (Path(args.out) if args.out else tools().scratch / "matte-out")
    cut = None
    if project and not faces_only and not every and (project.work / "cutmap.json").exists():
        cut = read_json(project.work / "cutmap.json")
    log_lines: list = []

    def log(s):
        log_lines.append(f"{time.strftime('%H:%M:%S')} {s}")
        if project:
            project.log("faces" if faces_only else "matte", log_lines[-1])

    results, skipped = [], []
    for j in jobs:
        info = _probe(j["src"])
        prefix = "work" if project else ""
        out_mp4 = base / prefix / "matte" / f"{j['id']}.mp4"
        out_face = base / prefix / "face" / f"{j['id']}.json"
        if faces_only:
            if project and not force and _known_boxes(project, j["id"], j["frames"]) is not None:
                skipped.append({"id": j["id"], "why": "face boxes already found"})
                continue
            log(f"{j['id']}: faces {j['src']} {info['w']}x{info['h']} {info['fps']:.3f} fps")
            res = process(Path(j["src"]), info["w"], info["h"], info["fps"], None, out_face, False, args.threads,
                          j["cuts"], j["frames"], j["id"], log, faces=not j.get("plates"))
        else:
            n_src = (j["frames"] or _count_frames(Path(j["src"]))) if cut is not None else 0
            ranges = kept_ranges(cut, j["id"], n_src) if cut is not None else None
            if cut is not None and not ranges:
                skipped.append({"id": j["id"], "why": "the cut keeps none of this source"})
                continue
            if project and not force and covers(_matte_done(project, j["id"]), ranges or "all"):
                skipped.append({"id": j["id"], "why": "the cut-out already covers the frames the cut keeps"})
                continue
            known = _known_boxes(project, j["id"], j["frames"]) if project else None
            log(f"{j['id']}: {j['src']} {info['w']}x{info['h']} {info['fps']:.3f} fps; cut-out "
                + ("every frame" if ranges is None else f"{sum(y - x for x, y in ranges)} of {n_src} frames in {len(ranges)} ranges"))
            res = process(Path(j["src"]), info["w"], info["h"], info["fps"], out_mp4, out_face, quality, args.threads,
                          j["cuts"], j["frames"], j["id"], log, faces=not j.get("plates"), ranges=ranges, known_boxes=known)
            res["matte"] = project.rel(out_mp4) if project else out_mp4.as_posix()
        res["face"] = project.rel(out_face) if project else out_face.as_posix()
        results.append(res)
        log(json.dumps(res))
    warnings = [f"{r['id']}: face found in only {r['face_coverage_pct']}% of frames" for r in results
                if r.get("faces", True) and "face_coverage_pct" in r and r["face_coverage_pct"] < 80]
    out = {"sources": results, "warnings": warnings}
    if skipped:
        out["skipped_sources"] = skipped
    if need is not None:
        out["needed"], out["why"] = True, need["why"]
    return out
