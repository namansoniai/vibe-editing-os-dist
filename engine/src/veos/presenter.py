"""Where the presenter's face is on screen, for V-FACE (and anything else that needs the face in screen space).

work/face.edit.json holds the face box per frame in footage space (1080x1920). The stage layout places the footage:
`full` shows it as is, `low` lowers it by its offset, the legacy windows (panel, inset, slide-aside, bubble) and the E-07
layouts (card, pip, stack, letterbox, blurfill) scale it into a presenter window around the face, and `hidden` shows no
footage at all. A layout with a `dim` treatment blurs and darkens the footage (the face is not a reading surface there).

`screen_face(c, n, box)` returns the face box (x0, y0, x1, y1) in screen space at frame n, clipped to the presenter
window, or None when no face is visible (hidden stage, dimmed footage, an opaque full-frame cover, a stack whose cells
show other sources, or the box falls outside the window). The geometry is the renderer's (core.js `geom`, layouts.js
`geom` / `frameRect`) without camera presets; when `veos measure` recorded the frame's footage transform
(plan/measure.text.json `geo`), that exact transform is used instead.

`screen_head(c, n, box, raw, sil)` returns the presenter's head region the same way (face, hair, room above the head:
`head_box`, from the cut-out silhouette when `silhouette()` could read one, else the face box grown by HAIR_UP / SIDES),
clipped to the window plus its head-breakout strip. `map_region` is the Ctx-free core the caption engine uses too.
"""
from __future__ import annotations

from .vcommon import FRAME_H as H, FRAME_W as W

LEGACY = ("full", "low", "panel", "inset", "slide-aside", "bubble", "hidden")
DEFAULTS = {
    "card": {"face": None, "eye": 0.42, "crop": "4:3"},
    "pip": {"d": 380, "corner": "br", "face": 0.62, "eye": 0.5, "margin": 0},
    "letterbox": {"band_h": 608, "cy": 960, "face": 0.42, "eye": 0.45},
    "blurfill": {"band_h": 608, "cy": 960, "face": 0.42, "eye": 0.45},
    "stack": {"seam_y": 960, "top": "graphic", "bottom": "footage"},
}
ASPECT = {"16:9": 16 / 9, "4:3": 4 / 3, "1:1": 1.0, "4:5": 4 / 5, "3:4": 3 / 4, "9:16": 9 / 16}
CORNER_X, CORNER_Y = {"l": 64, "r": 1016, "c": 540}, {"t": 150, "b": 1500, "c": 960}


def _cl(x, a, b):
    return a if x < a else b if x > b else x


def _cov(a, lo, hi):
    return _cl(a, lo, hi) if lo <= hi else (lo + hi) / 2


def _num(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def layout_token(style: dict, lid: str) -> dict:
    lay = (style.get("layouts") or {}).get(lid)
    return lay if isinstance(lay, dict) else {}


def dimmed(style: dict, lid: str, ev: dict | None = None) -> bool:
    """The stage layout blurs / darkens the footage (`treatment.dim`, or a `dim` on the stage entry)."""
    tr = layout_token(style, lid).get("treatment")
    if isinstance(tr, dict) and tr.get("dim"):
        return True
    return bool((ev or {}).get("dim"))


FR_FRAC = {"head_top_frac": "head_top_y", "eye_frac": "eye_y", "eyes_frac": "eye_y", "chin_frac": "chin_y",
           "face_h_frac": "face_h", "face_cx_frac": "face_cx"}
FR_PX = ("head_top_y", "eye_y", "chin_y", "face_cx", "face_h")


def _rng2(v):
    if isinstance(v, (list, tuple)) and len(v) == 2 and all(_num(x) for x in v):
        return (float(min(v)), float(max(v)))
    return None


def win_framing(R, own=None, base=None) -> dict | None:
    """layouts.js winFraming: screen-px framing ranges for a presenter window R (x, y, w, h) from the layout's own
    `framing` (fractions of the window, or screen px) or the reel's base framing ranges when every vertical range lies
    inside the window; None when neither applies."""
    rx, ry, rw, rh = R
    if isinstance(own, dict):
        o = {}
        for k, key in FR_FRAC.items():
            r = _rng2(own.get(k))
            if not r or key in o:
                continue
            o[key] = ((rx + r[0] * rw, rx + r[1] * rw) if key == "face_cx" else (r[0] * rh, r[1] * rh) if key == "face_h"
                      else (ry + r[0] * rh, ry + r[1] * rh))
        for k in FR_PX:
            r = _rng2(own.get(k))
            if r and k not in o:
                o[k] = r
        return o or None
    if not isinstance(base, dict):
        return None
    vk = [k for k in ("head_top_y", "eye_y", "chin_y") if _rng2(base.get(k))]
    if not vk or not all(_rng2(base[k])[0] >= ry - 1 and _rng2(base[k])[1] <= ry + rh + 1 for k in vk):
        return None
    o = {k: _rng2(base[k]) for k in vk}
    fx = _rng2(base.get("face_cx"))
    if fx and fx[0] >= rx - 1 and fx[1] <= rx + rw + 1:
        o["face_cx"] = fx
    fh = _rng2(base.get("face_h"))
    if fh and fh[1] <= rh:
        o["face_h"] = fh
    return o


def _frame_rect(R, F, face=None, eye=0.42, framing=None):
    """layouts.js frameRect: (s, ax, ay, Fx, Fy) that frame a 1080x1920 source with face F (x, y, w, h) into rect R
    (`framing`: win_framing ranges)."""
    rx, ry, rw, rh = R
    fx, fy, fw, fh = F
    cx, cy, fs = fx + fw / 2, fy + fh / 2, max(1.0, (fw + fh) / 2)
    cover = max(rw / W, rh / H)
    if framing:
        h = max(1.0, fh)
        mid = lambda r: (r[0] + r[1]) / 2  # noqa: E731
        fr = framing
        s = None
        if fr.get("face_h"):
            s = mid(fr["face_h"]) / h
        elif fr.get("head_top_y") and fr.get("chin_y"):
            s = (mid(fr["chin_y"]) - mid(fr["head_top_y"])) / (1.35 * h)
        elif fr.get("eye_y") and fr.get("chin_y"):
            s = (mid(fr["chin_y"]) - mid(fr["eye_y"])) / (0.62 * h)
        elif fr.get("head_top_y") and fr.get("eye_y"):
            s = (mid(fr["eye_y"]) - mid(fr["head_top_y"])) / (0.73 * h)
        if s is None:
            s = face * rh / fs if face else cover
        s = min(max(cover, s), max(cover, 3))
        ys = []
        if fr.get("head_top_y"):
            ys.append(mid(fr["head_top_y"]) + 0.85 * s * h)
        if fr.get("eye_y"):
            ys.append(mid(fr["eye_y"]) + 0.12 * s * h)
        if fr.get("chin_y"):
            ys.append(mid(fr["chin_y"]) - 0.5 * s * h)
        ay = sum(ys) / len(ys) if ys else ry + (0.42 if eye is None else eye) * rh
        ax = mid(fr["face_cx"]) if fr.get("face_cx") else rx + rw / 2
        ax = _cov(ax, rx + rw - s * (W - cx), rx + s * cx)
        ay = _cov(ay, ry + rh - s * (H - cy), ry + s * cy)
        return s, ax, ay, cx, cy
    s = min(max(cover, face * rh / fs if face else 0), max(cover, 3))
    ax = _cov(rx + rw / 2, rx + rw - s * (W - cx), rx + s * cx)
    ay = _cov(ry + (0.42 if eye is None else eye) * rh, ry + rh - s * (H - cy), ry + s * cy)
    return s, ax, ay, cx, cy


def _legacy(style: dict, eng: str, ev: dict, F):
    """core.js geom for the v1 engines: (window (x, y, w, h), s, ax, ay, Fx, Fy)."""
    L = style.get("layout") or {}
    P = L.get("panel") or {}
    ix, iy = (P.get("inset") or {}).get("x") or [12, 1068], (P.get("inset") or {}).get("y") or [1008, 1881]
    bt = P.get("bleed_top") or 1135
    bub = L.get("bubble") or {"cx": 210, "cy": 1560, "d": 300}
    fx, fy, fw, fh = F
    cx, cy, fs = fx + fw / 2, fy + fh / 2, max(1.0, (fw + fh) / 2)
    smin = lambda w, h: max(w / W, min(h, H) / H)  # noqa: E731
    if eng == "full":
        return (0, 0, W, H), 1.0, cx, cy, cx, cy
    if eng == "low":
        off = ev.get("offset")
        off = float(off) if _num(off) else 380.0
        return (0, 0, W, H), 1.0, cx, cy + off, cx, cy
    if eng == "panel":
        x, y, w, h = ix[0], bt, ix[1] - ix[0], H - bt + 12
        s = _cl(max(smin(w, h - 12), 0.52 * (h - 12) / fs), 0, 1.6)
        ax, ay = x + w / 2, y + 0.46 * (h - 12)
    elif eng == "inset":
        x, y, w, h = ix[0], iy[0], ix[1] - ix[0], iy[1] - iy[0]
        s = _cl(max(smin(w, h), 0.5 * h / fs), 0, 1.6)
        ax, ay = x + w / 2, y + 0.46 * h
    elif eng == "slide-aside":
        w = ((L.get("slide_aside") or {}).get("x") or [0, 450])[1]
        x, y, h = 0, 0, H
        s = _cl(max(smin(w, h), 0.7 * w / fs), 0, 1.6)
        ax, ay = w / 2, cy
    elif eng == "bubble":
        d = bub.get("d", 300)
        x, y, w, h = bub.get("cx", 210) - d / 2, bub.get("cy", 1560) - d / 2, d, d
        s = _cl(max(smin(d, d), 0.8 * d / fs), 0, 1.6)
        ax, ay = bub.get("cx", 210), bub.get("cy", 1560)
    else:
        return None
    yb = min(y + h, H)
    ax = _cov(ax, x + w - s * (W - cx), x + s * cx)
    ay = _cov(ay, yb - s * (H - cy), y + s * cy)
    return (x, y, w, h), s, ax, ay, cx, cy


def _params(style: dict, lid: str, eng: str, ev: dict) -> dict:
    """layouts.js resolve: engine defaults <- the token layout (its `presenter` block) <- the stage entry."""
    p = dict(DEFAULTS.get(eng) or {})
    for src in (layout_token(style, lid), {k: v for k, v in ev.items() if k not in ("t", "layout", "via", "dur", "ease", "overshoot")}):
        for k, v in src.items():
            if k in ("engine", "presenter", "graphic", "caption", "treatment", "share", "safe", "name", "notes"):
                continue
            p[k] = v
        pr = src.get("presenter")
        if isinstance(pr, dict):
            rect = {k: pr.get(k) for k in ("x", "y", "w", "h")} if any(pr.get(k) is not None for k in ("x", "y", "w", "h")) else None
            for k, v in pr.items():
                if k not in ("x", "y", "w", "h", "fade_to"):
                    p[k] = v
            if rect:
                if eng == "card":
                    p["rect"] = rect
                elif eng == "pip" and pr.get("d") is None:
                    p["d"] = min(rect.get("w") or 0, rect.get("h") or 0) or p.get("d")
                    if rect.get("x") is not None:
                        p["corner"] = {"cx": rect["x"] + (rect.get("w") or 0) / 2, "cy": rect["y"] + (rect.get("h") or 0) / 2}
                elif eng in ("letterbox", "blurfill"):
                    if rect.get("h") is not None:
                        p["band_h"] = rect["h"]
                    if rect.get("y") is not None:
                        p["cy"] = rect["y"] + (rect.get("h") or 0) / 2
                elif eng == "stack" and rect.get("y") is not None and "seam_y" not in src:
                    top = (rect.get("y") or 0) <= 1
                    p["seam_y"] = rect["y"] + (rect.get("h") or 0) if top else rect["y"]
                    p["top"], p["bottom"] = ("footage", "graphic") if top else ("graphic", "footage")
    return p


def _new(style: dict, lid: str, eng: str, ev: dict, F, base_framing=None):
    """layouts.js geom for the E-07 engines: (window, s, ax, ay, Fx, Fy) or None when the presenter's footage is not shown.
    `base_framing`: the reel's base framing ranges (framing.for_reel()["ranges"]) for window framing."""
    p = _params(style, lid, eng, ev)
    wf = lambda R, own: win_framing(R, own, base_framing)  # noqa: E731
    if eng == "card":
        asp = ASPECT.get(p.get("crop"), p.get("crop") if _num(p.get("crop")) else 4 / 3)
        r = dict(p.get("rect") or {})
        if not _num(r.get("w")) and not _num(r.get("h")):
            r["w"] = 936
        if not _num(r.get("w")):
            r["w"] = r["h"] * asp
        if not _num(r.get("h")):
            r["h"] = r["w"] / asp
        if not _num(r.get("x")):
            r["x"] = (W - r["w"]) / 2
        if not _num(r.get("y")):
            r["y"] = (H - r["h"]) / 2
        face = p.get("face")
        if face is None:
            face = 0 if abs(r["w"] / r["h"] - W / H) < 0.02 else 0.3
        R = (r["x"], r["y"], r["w"], r["h"])
        return (R, *_frame_rect(R, F, face, p.get("eye", 0.42), wf(R, p.get("framing"))))
    if eng == "pip":
        d = float(p.get("d") or 380)
        c = p.get("corner")
        if isinstance(c, dict):
            ccx, ccy = float(c.get("cx", 540)), float(c.get("cy", 960))
        else:
            s = str(c or "br")
            v, hz = (s[0], s[1]) if len(s) == 2 else ("c", "c") if s == "c" else (s[0], "c")
            m = float(p.get("margin") or 0)
            ccx = CORNER_X["l"] + m + d / 2 if hz == "l" else CORNER_X["r"] - m - d / 2 if hz == "r" else CORNER_X["c"]
            ccy = CORNER_Y["t"] + m + d / 2 if v == "t" else CORNER_Y["b"] - m - d / 2 if v == "b" else CORNER_Y["c"]
        R = (ccx - d / 2, ccy - d / 2, d, d)
        return (R, *_frame_rect(R, F, p.get("face", 0.62), p.get("eye", 0.5), wf(R, p.get("framing"))))
    if eng in ("letterbox", "blurfill"):
        if p.get("src") not in (None, "footage"):
            return None
        bh = float(p.get("band_h") or 608)
        R = (0, float(p.get("cy") or 960) - bh / 2, W, bh)
        return (R, *_frame_rect(R, F, p.get("face", 0.42), p.get("eye", 0.45)))
    if eng == "stack":
        sy = _cl(float(p.get("seam_y") or 960) if _num(p.get("seam_y")) else 960, 120, H - 120)
        for key, R in (("top", (0, 0, W, sy)), ("bottom", (0, sy, W, H - sy))):
            cell = p.get(key)
            src = cell if isinstance(cell, str) else (cell.get("src") or "footage") if isinstance(cell, dict) else "graphic"
            if src == "footage":
                o = cell if isinstance(cell, dict) else {}
                if o.get("crop"):
                    return None  # an explicit crop window (multicam reframe): not modelled, judged by measure geo only
                return (R, *_frame_rect(R, F, o.get("face", 0.3), o.get("eye", 0.4),
                                        wf(R, o.get("framing") if o.get("framing") is not None else p.get("framing"))))
        return None
    return None


def stage_entry_at(c, t: float) -> dict:
    from .vcommon import fr
    cur = {"t": 0, "layout": "full"}
    for e in c.stage:
        if fr(e.get("t", 0)) <= fr(t):
            cur = e
    return cur


def _geo_at(c, n: int):
    tm = getattr(c, "text_measure", None) or {}
    g = (tm.get(n) or {}).get("geo") if isinstance(tm.get(n), dict) else None
    return g if isinstance(g, dict) and g.get("m") and g.get("win") else None


def screen_face(c, n: int, box, raw=None) -> tuple | None:
    """Face box (x0, y0, x1, y1) on screen at frame n (see module doc). `box` is [x, y, w, h, ...] as a full stage shows
    it (after the E-16b base reframe, framing.apply_boxes: what `full` / `low` draw); `raw` the same box in footage space
    (before the reframe: the card / pip / stack windows and the measured transform map from it; default `box`)."""
    return _screen(c, n, box, raw, None)


def screen_head(c, n: int, box, raw=None, sil=None) -> tuple | None:
    """The presenter's HEAD REGION (x0, y0, x1, y1) on screen at frame n: face, hair and a little room above the head
    (head_box: the cut-out silhouette `sil` when known, else the face box expanded), clipped to the presenter window
    extended upward by the layout's head `breakout` (the strip [window.y - bo, window.y] where the cut-out head rises
    over a card / pip window). None when no presenter shows (the same cases as screen_face)."""
    return _screen(c, n, box, raw, sil if sil is not None else False)


def screen_window_fit(c, n: int, box, raw=None, sil=None) -> dict | None:
    """window_fit at frame n (see window_fit): None on a full-frame stage, or when no presenter shows (the same cases as
    screen_face). `sil`: the cut-out silhouette tuple, or None for the face box grown for the hair."""
    if not box or len(box) < 4:
        return None
    F = tuple(float(v) for v in box[:4])
    R0 = tuple(float(v) for v in (raw or box)[:4]) if (raw or box) and len(raw or box) >= 4 else F
    t = n / (c.fps or 30)
    ev = stage_entry_at(c, t)
    lid = str(ev.get("layout", "full"))
    eng = c.stage_engine_at(t)
    if eng in ("hidden", "full", "low") or dimmed(c.style, lid, ev):
        return None
    from .profilecheck import presenter_visible
    if not presenter_visible(c, n, need_face=False):
        return None
    got = window_fit(c.style, lid, eng, ev, F, R0, (getattr(c, "framing", None) or {}).get("ranges"),
                     geo=_geo_at(c, n), sil=sil)
    if got is not None:
        got["layout"] = lid
    return got


def _screen(c, n: int, box, raw, head) -> tuple | None:
    """screen_face (head None) / screen_head (head False: the expanded face box, or a silhouette tuple)."""
    if not box or len(box) < 4:
        return None
    F = tuple(float(v) for v in box[:4])
    R0 = tuple(float(v) for v in (raw or box)[:4]) if (raw or box) and len(raw or box) >= 4 else F
    t = n / (c.fps or 30)
    ev = stage_entry_at(c, t)
    lid = str(ev.get("layout", "full"))
    eng = c.stage_engine_at(t)
    if eng == "hidden" or dimmed(c.style, lid, ev):
        return None
    from .profilecheck import presenter_visible
    if not presenter_visible(c, n, need_face=False):
        return None
    return map_region(c.style, lid, eng, ev, F, R0, (getattr(c, "framing", None) or {}).get("ranges"),
                      geo=_geo_at(c, n), head=head)


# ------------------------------------------------------------------------------------------------ the head region
# The person comes first (Naman, 9 Oct 2026): nothing drawn above the presenter may cover the face, the hair or the
# top of the head. Face boxes run brow to chin, so the head region grows them: up by HAIR_UP face heights (skull and
# hair) plus HEADROOM, sideways by SIDES face widths each side. When the cut-out (work/frames/c*.webp) exists for the
# frame, the real silhouette above the chin line replaces the guess (silhouette()).
HAIR_UP = 0.75
HEADROOM = 0.10
SIDES = 0.15
SIL_UP_MAX = 1.6     # the silhouette search window above the face box (face heights) ...
SIL_SIDE_MAX = 0.6   # ... and beside it (face widths): hair, not a raised hand at arm's length
SIL_ALPHA = 128


def head_box(box, sil=None) -> tuple:
    """Head region (x, y, w, h) in the same space as the face box (x, y, w, h). `sil` = (left, up, right): how far the
    cut-out silhouette above the chin reaches past the face box, in face widths / heights (silhouette()); without it the
    face box grows by SIDES each side and HAIR_UP up. HEADROOM is always added above. The bottom stays at the chin."""
    x, y, w, h = (float(v) for v in box[:4])
    if sil:
        left, up, right = (max(0.0, float(v)) for v in sil)
    else:
        left, up, right = SIDES, HAIR_UP, SIDES
    up += HEADROOM
    return (x - left * w, y - up * h, w * (1 + left + right), h * (1 + up))


def silhouette(path, box) -> tuple | None:
    """(left, up, right) extents of the person cut-out above the chin line around the face box (footage space), read
    from a cut-out frame (RGBA, alpha = the person); None when the file is missing / unreadable / shows no person."""
    try:
        import numpy as np
        from PIL import Image
        with Image.open(path) as im:
            if "A" not in im.getbands():
                return None
            a = np.asarray(im.getchannel("A"))
    except Exception:  # noqa: BLE001 - a broken frame is "no silhouette"
        return None
    x, y, w, h = (float(v) for v in box[:4])
    if w < 2 or h < 2:
        return None
    H_, W_ = a.shape[:2]
    cx0, cx1 = max(0, int(x - SIL_SIDE_MAX * w)), min(W_, int(x + w + SIL_SIDE_MAX * w) + 1)
    cy0, cy1 = max(0, int(y - SIL_UP_MAX * h)), min(H_, int(y + h))  # rows above the chin line only
    if cx1 - cx0 < 2 or cy1 - cy0 < 2:
        return None
    m = a[cy0:cy1, cx0:cx1] >= SIL_ALPHA
    rows, cols = np.nonzero(m.any(axis=1))[0], np.nonzero(m.any(axis=0))[0]
    if not len(rows) or not len(cols):
        return None
    top, left, right = cy0 + rows[0], cx0 + cols[0], cx0 + cols[-1] + 1
    return ((x - left) / w, (y - top) / h, (right - (x + w)) / w)


def breakout_px(v) -> float:
    """layouts.js normBreakout: true = 160 px, a number = px, {px} = px."""
    if isinstance(v, dict):
        v = v.get("px", True)
    if v is True:
        return 160.0
    if _num(v) and v > 0:
        return float(v)
    return 0.0


def _project(style: dict, lid: str, eng: str, ev: dict, F, R0, base_framing=None, geo=None, head=None):
    """The unclipped screen rect (x0, y0, x1, y1) of the face box / head region, the footage window (x, y, w, h) and
    the head breakout px (card / pip, head regions only); None when nothing shows. See map_region."""
    ev = ev or {}
    if head is not None:
        sil = head or None
        EF, ER = head_box(F, sil), head_box(R0, sil)
    else:
        EF, ER = F, R0
    bo = 0.0
    if geo:
        a, b, cc, d, e, f = (float(v) for v in geo["m"])
        pts = [(a * x + cc * y + e, b * x + d * y + f) for x, y in ((ER[0], ER[1]), (ER[0] + ER[2], ER[1]),
                                                                     (ER[0], ER[1] + ER[3]), (ER[0] + ER[2], ER[1] + ER[3]))]
        win = tuple(float(v) for v in geo["win"])
        x0, y0 = min(p[0] for p in pts), min(p[1] for p in pts)
        x1, y1 = max(p[0] for p in pts), max(p[1] for p in pts)
    else:
        full = eng in ("full", "low")
        B, E = (F, EF) if full else (R0, ER)  # the base reframe only applies to the full and low stages
        g = (_legacy(style, eng, ev, B) if eng in LEGACY else _new(style, lid, eng, ev, B, base_framing))
        if g is None:
            return None
        win, s, ax, ay, fx, fy = g
        x0, y0 = ax + s * (E[0] - fx), ay + s * (E[1] - fy)
        x1, y1 = ax + s * (E[0] + E[2] - fx), ay + s * (E[1] + E[3] - fy)
    if head is not None and eng in ("card", "pip"):
        bo = breakout_px(_params(style, lid, eng, ev).get("breakout"))
    return (x0, y0, x1, y1), win, bo


def map_region(style: dict, lid: str, eng: str, ev: dict, F, R0, base_framing=None, geo=None, head=None):
    """Screen rect (x0, y0, x1, y1) of the face box (head None) or of the head region (head False / a silhouette) given
    the stage layout. F: the face box as a full stage shows it (after the base reframe); R0: the same box in footage
    space. The window's transform is computed from the face box itself; the head region rides the same transform and
    is clipped to the window, extended upward by the layout's head breakout (card / pip). None when nothing shows."""
    got = _project(style, lid, eng, ev, F, R0, base_framing, geo, head)
    if got is None:
        return None
    (x0, y0, x1, y1), win, bo = got
    wx0, wy0, wx1, wy1 = win[0], win[1] - bo, win[0] + win[2], win[1] + win[3]
    x0, y0, x1, y1 = max(x0, wx0, 0), max(y0, wy0, 0), min(x1, wx1, W), min(y1, wy1, H)
    if x1 - x0 < 4 or y1 - y0 < 4:
        return None
    return (x0, y0, x1, y1)


# ------------------------------------------------------------------------------------------------ window crops (advice)
# Does a window crop the creator's head? When the footage shows inside a rect smaller than the frame (card, pip, split /
# stack cell, letterbox band, the legacy panels), the head region (head_box: the cut-out silhouette, else the face box
# grown for the hair, plus headroom) is compared with the visible window plus a card / pip `breakout` strip. Full-frame
# stages (full, low, a 1080x1920 card) are exempt. V-FACE reports it as advice only, and the renderer frames every
# window with the style's own face / eye (Naman, 10 Oct 2026: no automatic head-safe framing).
FIT_TOL = 2.0  # px: rounding between this model and the renderer


def full_frame(win) -> bool:
    """The footage window covers the whole frame (core.js: the world shows through no window)."""
    x, y, w, h = (float(v) for v in win[:4])
    return x <= 0.5 and y <= 0.5 and x + w >= W - 0.5 and y + h >= H - 0.5


def window_fit(style: dict, lid: str, eng: str, ev: dict, F, R0, base_framing=None, geo=None, sil=None) -> dict | None:
    """Does the head region fit the presenter's window? None for a full-frame stage or when nothing shows; else
    {"head": unclipped screen head region (x0, y0, x1, y1), "win": the visible window (clipped to the frame, its top
    raised by the breakout strip), "bo": breakout px, "cut": {side: px the head reaches past that edge} (empty: fits)}.
    `sil`: a silhouette tuple (presenter.silhouette) or None for the face box grown for the hair."""
    if eng in ("full", "low"):
        return None
    got = _project(style, lid, eng, ev, F, R0, base_framing, geo, sil or False)
    if got is None:
        return None
    (x0, y0, x1, y1), win, bo = got
    if full_frame(win):
        return None
    wx0, wy0 = max(0.0, win[0]), max(0.0, win[1] - bo)
    wx1, wy1 = min(float(W), win[0] + win[2]), min(float(H), win[1] + win[3])
    cut = {k: v for k, v in (("top", wy0 - y0), ("left", wx0 - x0), ("right", x1 - wx1), ("bottom", y1 - wy1))
           if v > FIT_TOL}
    return {"head": (x0, y0, x1, y1), "win": (wx0, wy0, wx1, wy1), "bo": bo, "cut": cut}
