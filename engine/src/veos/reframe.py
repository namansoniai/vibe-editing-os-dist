"""Reframing geometry for multi-camera / faux-angle shots (pure functions; used by angles, shots and compose).

A *cell* is the screen rectangle a shot fills (the whole 1080x1920 frame, or one half of a `stack`). For each shot
the engine picks a crop window in source pixels with the cell's aspect ratio:

* `single`  one subject, chest-up: the face is `face_frac` of the cell height (x step for jump re-crops), the face
            centre sits at `eye_y` of the crop height, horizontally centred; the crop never upsamples more than
            `max_up` (it widens instead) and never leaves the source (it slides/shrinks instead);
* `group`   two or more subjects (two-shot): the union of the faces plus margins must fit; when it cannot fit the
            cell's aspect inside the source (two people side by side never fit a 9:16 crop), the shot falls back;
* `wide`    the whole source frame; on a cell of a different aspect it always falls back.

Fallback (`fit`): `blurfill` (the content band, scaled to the cell width, over a blurred, darkened cover copy of the
same band) or `letterbox` (the band on a flat fill). `cover` = a normal crop.

Subject follow: per-sample ideal crop centres -> a virtual operator with a dead zone (it holds still until the face
drifts out of the middle band), critically damped easing, then Ramer-Douglas-Peucker simplification -> keyframes
[[t, x, y], ...] (crop size is constant within a shot, so a follow never zooms).
"""
from __future__ import annotations

import math

import numpy as np

FACE_FRAC = {"full": 0.17, "stack": 0.27}      # face height / cell height for a single
EYE_Y = 0.36
MAX_UP = 2.0                                    # max upsampling for 9:16 shorts (Hormozi delivers 720p from 1080p)
GROUP_MARGIN = 0.9                              # x face width added on each side of a group union


def _clamp_rect(x, y, w, h, W, H):
    w, h = min(w, W), min(h, H)
    return float(np.clip(x, 0, W - w)), float(np.clip(y, 0, H - h)), float(w), float(h)


def size_single(face_h: float, src: tuple, cell: tuple, face_frac: float, step: float = 1.0,
                max_up: float = MAX_UP) -> tuple[float, float, dict]:
    """Crop (w, h) for a single. Returns (w, h, info{scale, limited})."""
    W, H = src
    cw, ch = cell
    asp = cw / ch
    h = face_h / max(1e-6, face_frac * step)
    info = {"limited": None}
    h_min = ch / max_up                     # no more upsampling than max_up
    if h < h_min:
        h, info["limited"] = h_min, "upscale"
    if h > H:
        h, info["limited"] = H, "source"
    if h * asp > W:
        h, info["limited"] = W / asp, "source"
    info["scale"] = round(ch / h, 3)
    return h * asp, h, info


def place_single(face: list, wh: tuple, src: tuple, eye_y: float = EYE_Y, lead: float = 0.0) -> tuple:
    """Crop rect (x, y, w, h) for a face box [x, y, w, h] with the crop size `wh`."""
    w, h = wh
    fx, fy = face[0] + face[2] / 2, face[1] + face[3] / 2
    return _clamp_rect(fx - w / 2 + lead * w, fy - eye_y * h, w, h, *src)


def group_rect(faces: list[list], src: tuple, cell: tuple, max_up: float = MAX_UP) -> dict:
    """Two-shot: {'fit': 'cover', 'crop': rect} or {'fit': 'blurfill', 'band': rect (content), 'crop': None}."""
    W, H = src
    cw, ch = cell
    asp = cw / ch
    x0 = min(f[0] - GROUP_MARGIN * f[2] for f in faces)
    x1 = max(f[0] + (1 + GROUP_MARGIN) * f[2] for f in faces)
    y0 = min(f[1] - 0.8 * f[3] for f in faces)
    y1 = max(f[1] + 2.6 * f[3] for f in faces)
    uw, uh = x1 - x0, y1 - y0
    w = max(uw, uh * asp)
    h = w / asp
    if h <= H and w <= W:
        h = max(h, ch / max_up)
        w = h * asp
        if h <= H and w <= W:
            cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
            return {"fit": "cover", "crop": _clamp_rect(cx - w / 2, cy - h / 2, w, h, W, H)}
    # cannot fill the cell: show a band that holds the group (at least 16:9-ish, never taller than the source)
    bw = min(W, max(uw, 1.0))
    bh = min(H, max(uh, bw * 9 / 16))
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return {"fit": "blurfill", "crop": None, "band": _clamp_rect(cx - bw / 2, cy - bh / 2, bw, bh, W, H)}


def wide_rect(src: tuple, cell: tuple) -> dict:
    W, H = src
    if abs(W / H - cell[0] / cell[1]) < 0.02:
        return {"fit": "cover", "crop": (0.0, 0.0, float(W), float(H))}
    return {"fit": "blurfill", "crop": None, "band": (0.0, 0.0, float(W), float(H))}


def band_layout(band: tuple, cell: tuple, y_frac: float = 0.5) -> tuple:
    """Where the band lands inside the cell for blurfill/letterbox: (dx, dy, dw, dh) in cell px (fit to width)."""
    bw, bh = band[2], band[3]
    s = min(cell[0] / bw, cell[1] / bh)
    dw, dh = bw * s, bh * s
    return (cell[0] - dw) / 2, (cell[1] - dh) * y_frac, dw, dh


# ======================================================================= follow
def _rdp(pts: np.ndarray, eps: float) -> list[int]:
    if len(pts) < 3:
        return list(range(len(pts)))
    out = [0, len(pts) - 1]   # pts rows: [t, x, y]; distance measured in (x, y) against the time-linear interpolation

    def rec(i, j):
        if j <= i + 1:
            return
        seg = pts[i:j + 1]
        f = (seg[:, 0] - pts[i, 0]) / max(pts[j, 0] - pts[i, 0], 1e-9)
        lin = pts[i, 1:] + f[:, None] * (pts[j, 1:] - pts[i, 1:])
        d = np.linalg.norm(seg[:, 1:] - lin, axis=1)
        k = int(np.argmax(d))
        if d[k] > eps:
            out.append(i + k)
            rec(i, i + k)
            rec(i + k, j)

    rec(0, len(pts) - 1)
    return sorted(set(out))


def follow(times: list[float], centres: list[tuple | None], wh: tuple, src: tuple, dead: float = 0.12,
           smooth_s: float = 0.6, eps_px: float = 2.0) -> list[list[float]]:
    """Ideal crop top-left per sample (None = no face: hold) -> keyframes [[t, x, y]] of a calm virtual operator.

    The operator holds until the ideal position is more than `dead` x crop size away, then eases there with a
    critically damped spring (time constant `smooth_s`)."""
    W, H = src
    w, h = wh
    if not times:
        return []
    ideal = []
    last = None
    for c in centres:
        if c is None:
            ideal.append(last)
        else:
            last = (float(np.clip(c[0], 0, W - w)), float(np.clip(c[1], 0, H - h)))
            ideal.append(last)
    first = next((p for p in ideal if p is not None), ((W - w) / 2, (H - h) / 2))
    ideal = [p if p is not None else first for p in ideal]
    # start on the median of the first second (no initial lurch)
    k0 = max(1, sum(1 for t in times if t - times[0] < 1.0))
    pos = np.median(np.array(ideal[:k0]), axis=0)
    vel = np.zeros(2)
    tgt = pos.copy()
    out = [[times[0], *pos]]
    omega = 2.0 / max(smooth_s, 1e-3)
    for i in range(1, len(times)):
        dt = max(1e-3, times[i] - times[i - 1])
        p = np.array(ideal[i])
        if abs(p[0] - tgt[0]) > dead * w or abs(p[1] - tgt[1]) > dead * h:
            tgt = p
        # critically damped spring step
        x = pos - tgt
        e = math.exp(-omega * dt)
        new = tgt + (x + (vel + omega * x) * dt) * e
        vel = (vel - omega * (vel + omega * x) * dt) * e
        pos = new
        out.append([times[i], float(pos[0]), float(pos[1])])
    arr = np.array(out)
    keep = _rdp(arr, eps_px)
    return [[round(float(arr[i, 0]), 3), round(float(arr[i, 1]), 1), round(float(arr[i, 2]), 1)] for i in keep]


def at(keys: list[list[float]], t: float) -> tuple[float, float]:
    """Crop top-left at time t from follow keyframes (linear between keys, held outside)."""
    if not keys:
        return 0.0, 0.0
    if t <= keys[0][0]:
        return keys[0][1], keys[0][2]
    for a, b in zip(keys, keys[1:]):
        if t <= b[0]:
            f = (t - a[0]) / max(b[0] - a[0], 1e-9)
            return a[1] + f * (b[1] - a[1]), a[2] + f * (b[2] - a[2])
    return keys[-1][1], keys[-1][2]
