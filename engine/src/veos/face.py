"""Face boxes via facedet (MediaPipe -> YuNet -> Haar chain), full frame first, then a 640 px crop around the last box.

Used by `veos matte` in the same decode pass. Boxes are [x, y, w, h, score] in source pixels.
"""
from __future__ import annotations

import numpy as np

from . import facedet

CROP = 640
MAX_GAP = 6


class FaceTracker:
    def __init__(self):
        facedet.backend_name()  # pick the backend now (raises FACE_DETECTOR_MISSING if none works)
        self.last: tuple[float, float] | None = None  # centre of the last box
        self.fallback_frames = 0

    def reset(self) -> None:
        self.last = None

    @staticmethod
    def _best(rgb: np.ndarray):
        r = facedet.detect(rgb)
        return r[0] if r else None

    def detect(self, rgb: np.ndarray) -> list | None:
        """rgb: HxWx3 uint8 at source size. Returns [x, y, w, h, score] or None."""
        h, w = rgb.shape[:2]
        res = self._best(rgb)
        ox = oy = 0
        if res is None:
            self.fallback_frames += 1
            cx, cy = self.last if self.last else (w / 2, h * 0.4)
            cw, ch = min(CROP, w), min(CROP, h)
            ox = int(np.clip(cx - cw / 2, 0, w - cw))
            oy = int(np.clip(cy - ch / 2, 0, h - ch))
            res = self._best(rgb[oy:oy + ch, ox:ox + cw])
        if res is None:
            return None
        x, y, bw, bh, score = res
        box = [int(x + ox), int(y + oy), int(bw), int(bh), round(score, 3)]
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
