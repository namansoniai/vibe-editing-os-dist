"""veos ingest: register source files, classify them and detect camera-setup segments."""
from __future__ import annotations

import urllib.request
from pathlib import Path

import numpy as np

from . import media
from .core import FPS, VeosError, need_project, r3, read_json, tools, write_json

MODEL_NAME = "blaze_face_short_range.tflite"
MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/face_detector/blaze_face_short_range/float16/1/"
             "blaze_face_short_range.tflite")
SPEECH_LUFS = -45.0       # quieter than this is treated as "no speech"
FACE_TH = 0.5             # face_ratio needed for talking-head
SELFIE_W = 0.35           # face width / frame width at or above this = selfie
WIDE_W = 0.10             # below this = wide
MIN_SEG_S = 2.0


def add_args(p, cmd):
    p.add_argument("inputs", nargs="*", help="video/audio files and/or folders (searched recursively); "
                   "default: the clips stored in project.json")


# ---------------------------------------------------------------- face detection
def _model_path() -> Path:
    path = tools().models / "mediapipe" / MODEL_NAME
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            urllib.request.urlretrieve(MODEL_URL, path)
        except Exception as e:  # noqa: BLE001
            path.unlink(missing_ok=True)
            raise VeosError("MODEL_MISSING", f"face model missing and download failed ({e})",
                            f"Download {MODEL_URL} to {path}.") from e
    return path


class FaceFinder:
    """BlazeFace short-range on up to three full-width square windows (the model squashes its input to 128 px,
    so a small face in a tall frame is only found when the frame is tiled)."""

    def __init__(self):
        import mediapipe as mp
        from mediapipe.tasks.python import BaseOptions, vision
        self.mp = mp
        self.det = vision.FaceDetector.create_from_options(vision.FaceDetectorOptions(
            base_options=BaseOptions(model_asset_path=str(_model_path())), min_detection_confidence=0.5))

    def find(self, gray: np.ndarray):
        """-> (w, h, cx, cy, score) as fractions of the frame, or None."""
        import cv2
        H, W = gray.shape
        offs = [0] if H <= W else sorted({0, int((H - W) * 0.4), H - W})
        best = None
        for y0 in offs:
            rgb = cv2.cvtColor(np.ascontiguousarray(gray[y0:y0 + W]), cv2.COLOR_GRAY2RGB)
            res = self.det.detect(self.mp.Image(image_format=self.mp.ImageFormat.SRGB, data=rgb))
            for d in res.detections:
                sc = d.categories[0].score
                if best is None or sc > best[0]:
                    b = d.bounding_box
                    best = (sc, b.width / W, b.height / H, (b.origin_x + b.width / 2) / W,
                            (b.origin_y + y0 + b.height / 2) / H)
        return None if best is None else (best[1], best[2], best[3], best[4], best[0])


# ---------------------------------------------------------------- analysis
def _flatness(g: np.ndarray) -> tuple[float, float]:
    """(edge density, flat-pixel fraction) of a gray frame."""
    import cv2
    e = cv2.Canny(g, 60, 160)
    gi = g.astype(np.int16)
    gx = np.abs(np.diff(gi, axis=1))[:-1]
    gy = np.abs(np.diff(gi, axis=0))[:, :-1]
    return float((e > 0).mean()), float(((gx < 2) & (gy < 2)).mean())


def analyse_video(path: Path, duration: float, finder: FaceFinder | None) -> dict:
    step = max(0.5, duration / 360)
    ts, faces, motion, edge, flat = [], [], [], [], []
    prev = None
    for t, g in media.iter_gray_frames(path, step, width=288):
        ts.append(t)
        faces.append(finder.find(g) if finder else None)
        gi = g.astype(np.int16)
        motion.append(0.0 if prev is None else float(np.abs(gi - prev).mean()))
        prev = gi
        e, f = _flatness(g)
        edge.append(e)
        flat.append(f)
    return {"t": ts, "face": faces, "motion": motion, "edge": edge, "flat": flat, "step": step}


def _label(face_w: float | None, motion: float) -> str:
    if face_w is None:
        return "other"
    if face_w >= SELFIE_W:
        return "selfie"
    if face_w >= WIDE_W:
        return "selfie" if (face_w >= 0.26 and motion > 20) else "tripod"
    return "wide"


def segment_setups(an: dict, cuts: list[float], duration: float) -> list[dict]:
    """Per-sample label from smoothed face width (+ camera motion); boundaries snap to nearby scene cuts."""
    ts, n = an["t"], len(an["t"])
    if n == 0:
        return [{"start": 0.0, "end": r3(duration), "setup": "other"}]
    w = np.array([f[0] if f else np.nan for f in an["face"]])
    mot = np.array(an["motion"])
    k = 2
    labels = []
    for i in range(n):
        lo, hi = max(0, i - k), min(n, i + k + 1)
        ww = w[lo:hi]
        ww = ww[~np.isnan(ww)]
        fw = float(np.median(ww)) if len(ww) >= max(1, (hi - lo) // 3) else None
        labels.append(_label(fw, float(np.median(mot[lo:hi]))))
    runs: list[list] = []  # [label, first_idx, last_idx]
    for i, lab in enumerate(labels):
        if runs and runs[-1][0] == lab:
            runs[-1][2] = i
        else:
            runs.append([lab, i, i])
    min_n = max(2, int(round(MIN_SEG_S / an["step"])))
    changed = True
    while changed and len(runs) > 1:
        changed = False
        for j, r in enumerate(runs):
            if r[2] - r[1] + 1 < min_n:
                if j == 0:
                    nb = 1
                elif j == len(runs) - 1:
                    nb = j - 1
                else:
                    nb = j - 1 if (runs[j - 1][2] - runs[j - 1][1]) >= (runs[j + 1][2] - runs[j + 1][1]) else j + 1
                runs[nb][1], runs[nb][2] = min(runs[nb][1], r[1]), max(runs[nb][2], r[2])
                runs.pop(j)
                changed = True
                break
        merged: list[list] = []
        for r in runs:
            if merged and merged[-1][0] == r[0]:
                merged[-1][2] = r[2]
            else:
                merged.append(r)
        runs = merged
    bounds = [0.0]
    for a, b in zip(runs, runs[1:]):
        lo, hi = ts[a[2]], ts[b[1]]
        near = [c for c in cuts if lo - 1.0 <= c <= hi + 1.0]
        bounds.append(min(near, key=lambda c: abs(c - (lo + hi) / 2)) if near else (lo + hi) / 2)
    bounds.append(duration)
    return [{"start": r3(s), "end": r3(e), "setup": r[0]} for r, s, e in zip(runs, bounds, bounds[1:])]


def classify(an: dict, lufs: float | None, has_audio: bool) -> tuple[str, float, list[str]]:
    faces = an["face"]
    ratio = sum(1 for f in faces if f) / max(1, len(faces))
    notes: list[str] = []
    speech = has_audio and lufs is not None and lufs > SPEECH_LUFS
    if ratio >= FACE_TH and speech:
        return "talking-head", ratio, notes
    if ratio >= FACE_TH:
        notes.append("face present but no speech-level audio")
        return "broll", ratio, notes
    edge, flat = float(np.mean(an["edge"])), float(np.mean(an["flat"]))
    if flat > 0.55 and edge > 0.012:
        return "screen-recording", ratio, notes
    return "broll", ratio, notes


# ---------------------------------------------------------------- command
def _collect(inputs: list[str]) -> list[Path]:
    out, seen = [], set()
    exts = media.VIDEO_EXT | media.AUDIO_EXT
    for s in inputs:
        p = Path(s).expanduser()
        if not p.exists():
            raise VeosError("INPUT_MISSING", f"not found: {s}", "Check the path (quote paths that contain spaces).")
        if p.is_dir():
            files = sorted((q for q in p.rglob("*") if q.is_file() and q.suffix.lower() in exts),
                           key=lambda q: [c.lower() for c in q.parts])
        else:
            files = [p]
        for f in files:
            r = f.resolve()
            if r not in seen:
                seen.add(r)
                out.append(r)
    if not out:
        raise VeosError("NO_MEDIA", "no video or audio files found", "Pass video files or a folder that contains them.")
    return out


def _talking_id(n: int) -> str:
    return chr(ord("A") + n) if n < 26 else f"A{n - 25}"


def main(args, project) -> dict:
    proj = need_project(project)
    inputs = args.inputs
    if not inputs:  # default to the clips registered by `veos project init`
        pj = proj.root / "project.json"
        inputs = (read_json(pj).get("clips") or []) if pj.exists() else []
        if not inputs:
            raise VeosError("NO_INPUT", "no files given and project.json has no clips",
                            "Pass files/folders, or run `veos project init <clips> --project P` first.")
    files = _collect(inputs)
    finder = None
    sources, summary, warnings = [], [], []
    nth, ns = 0, 0
    for f in files:
        pr = media.probe(f)
        v = pr["video"]
        notes: list[str] = []
        audio = None
        if pr["audio"]:
            best = None
            for a in pr["audio"]:
                lufs, tp = media.loudness(f, a["stream"])
                if best is None or (lufs if lufs is not None else -999) > (best[1] if best[1] is not None else -999):
                    best = (a, lufs, tp)
            a, lufs, tp = best
            audio = {"stream": a["stream"], "channels": a["channels"], "lufs": lufs, "tp": tp}
            if len(pr["audio"]) > 1:
                notes.append(f"{len(pr['audio'])} audio streams; stream {a['stream']} is the loudest")
            if lufs is None:
                notes.append("audio is silent")
        entry: dict = {"path": proj.rel(f)}
        if v is None:
            kind, ratio, segs = "audio-only", 0.0, []
            entry.update(duration=r3(pr["duration"]), frames=int(round(pr["duration"] * FPS)))
        else:
            if finder is None:
                finder = FaceFinder()
            dur = v["duration"] or pr["duration"]
            an = analyse_video(f, dur, finder)
            kind, ratio, n2 = classify(an, audio["lufs"] if audio else None, audio is not None)
            notes += n2
            if kind == "talking-head":
                segs = segment_setups(an, media.scene_cuts(f, 0.3), dur)
            else:
                segs = [{"start": 0.0, "end": r3(dur), "setup": "screen" if kind == "screen-recording" else "other"}]
            frames = v["frames"] or int(round(dur * (v["fps"] or FPS)))
            entry.update(duration=r3(dur), frames=frames, width=v["disp_w"], height=v["disp_h"],
                         rotation=v["rotation"], fps_in=v["fps_in"], vfr=v["vfr"])
            if v["vfr"]:
                warnings.append(f"{f.name}: variable frame rate (conform makes it a constant 30 fps)")
        if kind == "talking-head":
            sid = _talking_id(nth)
            nth += 1
        else:
            ns += 1
            sid = f"S{ns}"
        src = {"id": sid, **entry, "kind": kind, "audio": audio, "segments": segs,
               "face_ratio": round(ratio, 2), "notes": notes}
        order = ["id", "path", "kind", "duration", "frames", "width", "height", "rotation", "fps_in", "vfr",
                 "audio", "segments", "face_ratio", "notes"]
        sources.append({k: src[k] for k in order if k in src})
        summary.append({"id": sid, "file": f.name, "kind": kind, "duration": entry["duration"],
                        "segments": [[s["start"], s["end"], s["setup"]] for s in segs],
                        "vfr": entry.get("vfr", False)})
    write_json(proj.path("work", "sources.json"), {"version": 1, "fps": FPS, "sources": sources})
    proj.log("ingest", f"ingested {len(sources)} sources")
    return {"sources": summary, "warnings": warnings}
