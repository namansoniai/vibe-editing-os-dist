"""One face detector interface with a self-healing backend chain.

    detect(rgb) -> [(x, y, w, h, score), ...]   source pixels, best first, never raises on backend failure

Chain (chosen once per process): MediaPipe BlazeFace -> OpenCV YuNet -> OpenCV Haar cascade.
A backend is "working" when import + model load + one detection on a built-in synthetic frame succeed.
Any exception from a backend (also mid-clip) permanently switches this process to the next one and logs a
warning. `VEOS_FACE_BACKEND=mediapipe|yunet|haar` puts a backend first (the others stay as fallbacks).
Self-test results (each run in a subprocess, so a native crash is survivable) are recorded in
VEOS_HOME/state/facedet.json by the doctor / first use; backends recorded as broken are skipped.
"""
from __future__ import annotations

import hashlib
import json
import logging
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np

from .core import VeosError, veos_home

log = logging.getLogger("veos.facedet")

ORDER = ("mediapipe", "yunet", "haar")
MP_URL = ("https://storage.googleapis.com/mediapipe-models/face_detector/"
          "blaze_face_short_range/float16/1/blaze_face_short_range.tflite")
YUNET_URL = "https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx"
YUNET_SHA256 = "8f2383e4dd3cfbb4553ea8718107fc0423210dc964f9f4280604804ed2552fa4"
MIN_SCORE = 0.4
YUNET_SIDE = 640   # YuNet runs on a frame downscaled to this max side
HAAR_SIDE = 800


# ------------------------------------------------------------------ models
def mediapipe_model_path() -> Path:
    p = veos_home() / "models" / "mediapipe" / "blaze_face_short_range.tflite"
    if not p.exists():
        _fetch(MP_URL, p)
    return p


def yunet_model_path() -> Path:
    p = veos_home() / "models" / "yunet" / "face_detection_yunet_2023mar.onnx"
    if p.exists() and _sha(p) != YUNET_SHA256:
        p.unlink()
    if not p.exists():
        _fetch(YUNET_URL, p, YUNET_SHA256)
    return p


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _fetch(url: str, dest: Path, sha: str = "") -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    part = dest.with_name(dest.name + ".part")
    try:
        urllib.request.urlretrieve(url, part)
        if sha and _sha(part) != sha:
            raise ValueError("sha256 mismatch")
        part.replace(dest)
    except Exception as e:  # noqa: BLE001
        part.unlink(missing_ok=True)
        raise VeosError("MODEL_MISSING", f"face model {dest.name} missing and download failed ({e})",
                        "Run `veos doctor` / /reel-setup to download the models.") from e


# ------------------------------------------------------------------ backends (raw: no fallback logic)
class _MediaPipe:
    name = "mediapipe"

    def __init__(self):
        import mediapipe as mp
        from mediapipe.tasks import python as mpt
        from mediapipe.tasks.python import vision
        self.mp = mp
        self.det = vision.FaceDetector.create_from_options(vision.FaceDetectorOptions(
            base_options=mpt.BaseOptions(model_asset_path=str(mediapipe_model_path())),
            running_mode=vision.RunningMode.IMAGE, min_detection_confidence=MIN_SCORE))

    def _run(self, rgb, oy=0):
        r = self.det.detect(self.mp.Image(image_format=self.mp.ImageFormat.SRGB, data=np.ascontiguousarray(rgb)))
        out = []
        for d in r.detections:
            b = d.bounding_box
            out.append((int(b.origin_x), int(b.origin_y + oy), int(b.width), int(b.height),
                        round(float(d.categories[0].score), 3)))
        return out

    def detect(self, rgb, tiled=False):
        H, W = rgb.shape[:2]
        if not tiled or H <= W:
            return self._run(rgb)
        # BlazeFace squashes its input to 128 px: tile tall frames into up to three full-width squares
        out = []
        for y0 in sorted({0, int((H - W) * 0.4), H - W}):
            out += self._run(rgb[y0:y0 + W], y0)
        return out


class _YuNet:
    name = "yunet"

    def __init__(self):
        import cv2
        self.cv2 = cv2
        self.det = cv2.FaceDetectorYN.create(str(yunet_model_path()), "", (320, 320), MIN_SCORE, 0.3, 50)

    def detect(self, rgb, tiled=False):
        cv2 = self.cv2
        H, W = rgb.shape[:2]
        s = min(1.0, YUNET_SIDE / max(H, W))
        w, h = max(1, round(W * s)), max(1, round(H * s))
        img = cv2.cvtColor(np.ascontiguousarray(rgb), cv2.COLOR_RGB2BGR)
        if s < 1.0:
            img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
        self.det.setInputSize((w, h))
        _, faces = self.det.detect(img)
        out = []
        for f in (faces if faces is not None else []):
            out.append((int(round(f[0] / s)), int(round(f[1] / s)), int(round(f[2] / s)), int(round(f[3] / s)),
                        round(float(f[14]), 3)))
        return out


class _Haar:
    name = "haar"

    def __init__(self):
        import cv2
        self.cv2 = cv2
        name = "haarcascade_frontalface_default.xml"
        # opencv-python 4.x ships the cascade in cv2.data; 5.x wheels do not, so a copy is bundled with veos
        cands = [Path(getattr(getattr(cv2, "data", None), "haarcascades", "") or "") / name,
                 Path(__file__).parent / "data" / name]
        self.cc = None
        for c in cands:
            if c.is_file():
                cc = cv2.CascadeClassifier(str(c))
                if not cc.empty():
                    self.cc = cc
                    break
        if self.cc is None:
            raise RuntimeError("haar cascade file not found")

    def detect(self, rgb, tiled=False):
        cv2 = self.cv2
        H, W = rgb.shape[:2]
        s = min(1.0, HAAR_SIDE / max(H, W))
        g = cv2.cvtColor(np.ascontiguousarray(rgb), cv2.COLOR_RGB2GRAY)
        if s < 1.0:
            g = cv2.resize(g, (max(1, round(W * s)), max(1, round(H * s))), interpolation=cv2.INTER_AREA)
        g = cv2.equalizeHist(g)
        r = self.cc.detectMultiScale(g, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))
        boxes = [(int(round(x / s)), int(round(y / s)), int(round(w / s)), int(round(h / s)), 1.0) for x, y, w, h in r]
        return sorted(boxes, key=lambda b: -b[2] * b[3])


_CLASSES = {"mediapipe": _MediaPipe, "yunet": _YuNet, "haar": _Haar}


def selftest_backend(name: str) -> tuple[bool, str]:
    """import + model load + one detection on a synthetic gray frame, in this process."""
    try:
        r = _CLASSES[name]().detect(np.full((480, 640, 3), 128, np.uint8))
        if not isinstance(r, list):
            raise TypeError("detect did not return a list")
        return True, "ok"
    except Exception as e:  # noqa: BLE001
        return False, f"{type(e).__name__}: {str(e)[:160]}"


def selftest_isolated(name: str, timeout: float = 120.0) -> tuple[bool, str]:
    """Same, in a subprocess: survives a native crash (segfault) inside the backend."""
    try:
        p = subprocess.run([sys.executable, "-m", "veos.facedet", "--selftest", name], capture_output=True,
                           timeout=timeout, text=True)
        for line in reversed((p.stdout or "").strip().splitlines()):
            if line.startswith("{"):
                j = json.loads(line)
                return bool(j["ok"]), str(j["detail"])
        return False, f"crashed (exit code {p.returncode}) {(p.stderr or '').strip()[-120:]}"
    except subprocess.TimeoutExpired:
        return False, "self-test timed out"
    except Exception as e:  # noqa: BLE001
        return False, f"{type(e).__name__}: {str(e)[:160]}"


# ------------------------------------------------------------------ state file
def state_path() -> Path:
    return veos_home() / "state" / "facedet.json"


def _sig() -> str:
    from importlib import metadata
    v = []
    for pkg in ("mediapipe", "opencv-python-headless"):
        try:
            v.append(metadata.version(pkg))
        except Exception:  # noqa: BLE001
            v.append("-")
    return "|".join(v)


def read_state() -> dict | None:
    try:
        return json.loads(state_path().read_text(encoding="utf-8-sig"))
    except Exception:  # noqa: BLE001
        return None


def run_selftests(write: bool = True) -> dict:
    """Self-test every backend (isolated), record and return {backend, results, ...}."""
    results = {}
    for n in ORDER:
        ok, detail = selftest_isolated(n)
        results[n] = {"ok": ok, "detail": detail}
    active = next((n for n in ORDER if results[n]["ok"]), None)
    st = {"backend": active, "results": results, "sig": _sig(), "time": int(time.time())}
    if write:
        try:
            state_path().parent.mkdir(parents=True, exist_ok=True)
            state_path().write_text(json.dumps(st, indent=1), encoding="utf-8")
        except Exception as e:  # noqa: BLE001
            log.warning("could not write %s: %s", state_path(), e)
    return st


# ------------------------------------------------------------------ chain
_dead: set[str] = set()
_active = None  # backend instance
_state_checked = False


def _wanted_order() -> list[str]:
    forced = os.environ.get("VEOS_FACE_BACKEND", "").strip().lower()
    order = list(ORDER)
    if forced in ORDER:
        order.remove(forced)
        order.insert(0, forced)
    elif forced:
        log.warning("VEOS_FACE_BACKEND=%s is not one of %s; ignored", forced, "/".join(ORDER))
    return order


def _skip_from_state() -> set[str]:
    """Backends recorded as broken by the doctor / an earlier first-use test (none when one is forced)."""
    global _state_checked
    if os.environ.get("VEOS_FACE_BACKEND") or _state_checked:
        return set()
    _state_checked = True
    st = read_state()
    if not st or st.get("sig") != _sig():
        st = run_selftests()
    return {n for n, r in st.get("results", {}).items() if not r.get("ok")}


def _activate() -> None:
    """Pick the first loadable backend of the chain (once per process)."""
    global _active
    if _active is not None:
        return
    skip = _skip_from_state()
    order = [n for n in _wanted_order() if n not in _dead and n not in skip] or \
            [n for n in _wanted_order() if n not in _dead]
    for n in order:
        try:
            _active = _CLASSES[n]()
            return
        except Exception as e:  # noqa: BLE001
            _dead.add(n)
            log.warning("face backend %s unavailable (%s: %s); trying the next one", n, type(e).__name__, str(e)[:160])
    raise VeosError("FACE_DETECTOR_MISSING", "no face detector backend works (mediapipe, yunet and haar all failed)",
                    "Run `veos doctor` and follow the hint on the face detector check.")


def backend_name() -> str:
    _activate()
    return _active.name


def reset() -> None:
    """Forget the process-wide choice (tests)."""
    global _active, _state_checked
    _active = None
    _state_checked = False
    _dead.clear()


def detect(rgb: np.ndarray, tiled: bool = False, min_score: float = MIN_SCORE) -> list[tuple]:
    """rgb: HxWx3 uint8. -> [(x, y, w, h, score)] in the pixels of `rgb`, best first.
    tiled=True: MediaPipe tiles tall frames into full-width squares (small faces in downscaled frames).
    A backend failure switches to the next backend instead of raising."""
    global _active
    while True:
        _activate()
        try:
            r = _active.detect(rgb, tiled=tiled)
            return sorted((b for b in r if b[4] >= min_score), key=lambda b: -b[4])
        except Exception as e:  # noqa: BLE001
            log.warning("face backend %s failed at runtime (%s: %s); switching to the next backend",
                        _active.name, type(e).__name__, str(e)[:160])
            _dead.add(_active.name)
            _active = None


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--selftest":
        ok, detail = selftest_backend(sys.argv[2])
        print(json.dumps({"ok": ok, "detail": detail}))
