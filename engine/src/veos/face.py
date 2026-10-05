"""Face boxes: MediaPipe BlazeFace short-range, full frame first, then a 640 px crop around the last box.

Used by `veos matte` in the same decode pass. Boxes are [x, y, w, h, score] in source pixels.
"""
from __future__ import annotations

import urllib.request
from pathlib import Path

import numpy as np

from .core import VeosError, tools

MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/face_detector/"
             "blaze_face_short_range/float16/1/blaze_face_short_range.tflite")
CROP = 640
MAX_GAP = 6


def model_path() -> Path:
    p = tools().models / "mediapipe" / "blaze_face_short_range.tflite"
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        try:
            urllib.request.urlretrieve(MODEL_URL, p)
        except Exception as e:  # noqa: BLE001
            raise VeosError("MODEL_MISSING", f"face model not found and download failed ({e})",
                            "Run `veos doctor` / /reel-setup to download the models.") from e
    return p


class FaceTracker:
    def __init__(self):
        import mediapipe as mp
        from mediapipe.tasks import python as mpt
        from mediapipe.tasks.python import vision
        self._mp = mp
        self._det = vision.FaceDetector.create_from_options(vision.FaceDetectorOptions(
            base_options=mpt.BaseOptions(model_asset_path=str(model_path())),
            running_mode=vision.RunningMode.IMAGE, min_detection_confidence=0.4))
        self.last: tuple[float, float] | None = None  # centre of the last box
        self.fallback_frames = 0

    def reset(self) -> None:
        self.last = None

    def _run(self, rgb: np.ndarray):
        r = self._det.detect(self._mp.Image(image_format=self._mp.ImageFormat.SRGB, data=np.ascontiguousarray(rgb)))
        if not r.detections:
            return None
        d = max(r.detections, key=lambda d: d.categories[0].score)
        return d.bounding_box, float(d.categories[0].score)

    def detect(self, rgb: np.ndarray) -> list | None:
        """rgb: HxWx3 uint8 at source size. Returns [x, y, w, h, score] or None."""
        h, w = rgb.shape[:2]
        res = self._run(rgb)
        ox = oy = 0
        if res is None:
            self.fallback_frames += 1
            cx, cy = self.last if self.last else (w / 2, h * 0.4)
            cw, ch = min(CROP, w), min(CROP, h)
            ox = int(np.clip(cx - cw / 2, 0, w - cw))
            oy = int(np.clip(cy - ch / 2, 0, h - ch))
            res = self._run(rgb[oy:oy + ch, ox:ox + cw])
        if res is None:
            return None
        b, score = res
        box = [int(b.origin_x + ox), int(b.origin_y + oy), int(b.width), int(b.height), round(score, 3)]
        self.last = (box[0] + box[2] / 2, box[1] + box[3] / 2)
        return box


def finalize(boxes: list) -> list:
    """Interpolate gaps <= 6 frames, then 3-frame median on the coordinates. Longer gaps stay None."""
    n = len(boxes)
    out = [list(b) if b else None for b in boxes]
    valid = [i for i, b in enumerate(out) if b]
    for a, b in zip(valid, valid[1:]):
        gap = b - a - 1
        if 0 < gap <= MAX_GAP:
            A, B = np.array(out[a], float), np.array(out[b], float)
            for k in range(1, gap + 1):
                v = A + (B - A) * k / (gap + 1)
                out[a + k] = [int(round(x)) for x in v[:4]] + [round(float(v[4]), 3)]
    sm = [None] * n
    for i in range(n):
        if out[i] is None:
            continue
        win = [out[j] for j in (i - 1, i, i + 1) if 0 <= j < n and out[j]]
        med = np.median(np.array([w[:4] for w in win], float), axis=0)
        sm[i] = [int(round(x)) for x in med] + [out[i][4]]
    return sm
