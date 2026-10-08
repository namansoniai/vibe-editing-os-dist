"""Text measurement for `veos measure` (E-06, E-21) -> plan/measure.text.json; read by V-TYPE and V-EXC.

For every text element on the sampled frames (scene text and the caption chunks, which the renderer paints under a
`__`-prefixed scene id such as `__subtitles`) the renderer's `window.measureText(n)` reports the rendered font size (CSS size
x the accumulated transform scale), weight, fill / stroke / shadows, effective opacity, the nearest painted container, the
rect, lines and characters per line, and glyph clipping. This module adds, per element:

  contrast   WCAG ratio of the text against the sampled background: the frame is screenshotted with every glyph made
             transparent (containers, footage and worlds stay), the background under the text rect is read and the
             worst-side percentile is used (p90 for light text, p10 for dark text). A text stroke >= 1.5 px is a full halo;
             text shadows count as a partial halo (combined alpha, at most 0.85), and a halo counts only when it raises the
             contrast (a same-colour glow is decoration). Opacity blends the fill with the background. Text inside its own
             painted container (chip, pill, bubble, card) is read against that container: its flat colour when opaque,
             else the pixels inside the container rect only.
  occlusion  E1 behind-subject text only: the person cut-out alpha (work/frames/c*.webp, placed with the footage->screen
             transform of that frame) sampled over each character box -> visible glyph ratio (area-weighted) and whether the
             first and last letters are visible (>= 0.5).

Sampled frames: every scene's mid-hold frame plus one every 2 s of its settled hold, and every caption chunk's mid frame
(work/captions.json when present, else the renderer's own subtitle cards). E6 scenes add a layout-only frame every 2 frames
of their hold (slot rects); E4 scenes add frame n+1 after each sample (item speed). Only the contrast frames take a
screenshot (~0.1 s each).
"""
from __future__ import annotations

import io
import time
from pathlib import Path
from urllib.parse import unquote, urlparse
from urllib.request import url2pathname

import numpy as np

from .core import FPS, read_json, write_json

W, H = 1080, 1920
HIDE_TEXT_CSS = ("#root [data-scene], #root [data-scene] * { color: transparent !important; "
                 "-webkit-text-fill-color: transparent !important; -webkit-text-stroke-color: transparent !important; "
                 "text-shadow: none !important; caret-color: transparent !important; }")
HOLD_STEP = 60       # frames between extra samples of one scene's hold (2 s)
SETTLE_F = 10        # skip the entry
EXIT_F = 6
STROKE_HALO_PX = 1.5
SHADOW_HALO_MAX = 0.85


# --------------------------------------------------------------------------- colour maths
def _lin(c):
    c = np.asarray(c, dtype=np.float64) / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def luminance(rgb) -> np.ndarray:
    """Relative luminance (WCAG) of an (..., 3) sRGB 0-255 array."""
    l = _lin(rgb)
    return 0.2126 * l[..., 0] + 0.7152 * l[..., 1] + 0.0722 * l[..., 2]


def ratio(a: float, b: float) -> float:
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def container_colour(rec: dict):
    """The text's own painted container as a solid colour [r, g, b] (a chip, pill, bubble or card with an opaque flat
    fill), else None (no container, a gradient / image fill, or a see-through fill)."""
    box = rec.get("box")
    if not isinstance(box, dict) or box.get("image"):
        return None
    col = box.get("colour")
    if not col or len(col) < 3 or (col[3] if len(col) > 3 else 1) < 0.95:
        return None
    return col[:3]


def sample_rect(rec: dict):
    """Where the background is read: the text rect, clipped to its painted container when it has one (the em boxes of
    a chip's text overhang the chip, and the worst-side percentile then read the scene behind the chip)."""
    r = rec["rect"]
    box = rec.get("box")
    br = box.get("rect") if isinstance(box, dict) else None
    if br and len(br) >= 4:
        x0, y0, x1, y1 = max(r[0], br[0]), max(r[1], br[1]), min(r[2], br[2]), min(r[3], br[3])
        if x1 - x0 >= 2 and y1 - y0 >= 2:
            return [x0, y0, x1, y1]
    return r


def text_contrast(rec: dict, bg_lums: np.ndarray) -> dict | None:
    """Contrast of one measured text element against background luminances sampled under it (see module doc).

    A solid container (chip, pill, bubble) is the background itself: its colour is used, not the pixels around it.
    A stroke / shadow halo counts only when it raises the contrast: a glow in the text's own colour (or a dark drop
    shadow under dark text) is decoration, not the background the glyphs are read against."""
    cc = container_colour(rec)
    if cc is not None:
        bg_lums = np.array([float(luminance(np.array(cc, dtype=np.float64)))])
    if bg_lums.size == 0:
        return None
    col = rec.get("colour") or [0, 0, 0, 1]
    lt = float(luminance(np.array(col[:3], dtype=np.float64)))
    at = max(0.0, min(1.0, float(col[3] if len(col) > 3 else 1) * float(rec.get("opacity", 1))))
    med = float(np.median(bg_lums))
    lb = float(np.percentile(bg_lums, 90 if lt >= med else 10))
    h, lh = 0.0, 0.0
    sc = rec.get("stroke_colour")
    if float(rec.get("stroke") or 0) >= STROKE_HALO_PX and sc and (sc[3] if len(sc) > 3 else 1) >= 0.5:
        h, lh = 1.0, float(luminance(np.array(sc[:3], dtype=np.float64)))
    elif rec.get("shadows"):
        keep, wsum, lsum = 1.0, 0.0, 0.0
        for s in rec["shadows"]:
            if not s:
                continue
            a = max(0.0, min(1.0, float(s[3] if len(s) > 3 else 1)))
            keep *= 1 - a
            wsum += a
            lsum += a * float(luminance(np.array(s[:3], dtype=np.float64)))
        if wsum > 0:
            h, lh = min(SHADOW_HALO_MAX, 1 - keep), lsum / wsum
    plain = ratio(at * lt + (1 - at) * lb, lb)
    lb2 = (1 - h) * lb + h * lh
    lt2 = at * lt + (1 - at) * lb2
    haloed = ratio(lt2, lb2)
    if haloed < plain:
        h, haloed = 0.0, plain
    return {"contrast": round(haloed, 2), "bg_lum": round(lb, 4), "halo": round(h, 2),
            **({"bg": "container"} if cc is not None else {})}


def region_lums(img: np.ndarray, rect, step: int = 2) -> np.ndarray:
    x0, y0, x1, y1 = (int(round(v)) for v in rect)
    x0, y0, x1, y1 = max(0, x0), max(0, y0), min(img.shape[1], x1), min(img.shape[0], y1)
    if x1 <= x0 or y1 <= y0:
        return np.zeros(0)
    return luminance(img[y0:y1:step, x0:x1:step, :3].astype(np.float64)).ravel()


# --------------------------------------------------------------------------- E1 occlusion
def occlusion(chars: list, geo: dict | None, alpha: np.ndarray | None) -> dict | None:
    """Visible glyph ratio of behind text: 1 - cut-out alpha over each character box (5x5 samples, 15% inset).

    geo: {m: [a,b,c,d,e,f] (CSS matrix: footage group -> screen), win: [x,y,w,h] (the footage window clip)}; alpha: the
    cut-out alpha (0..1) of the frame, drawn at 1080x1920 in group space."""
    if not chars or not geo or alpha is None:
        return None
    a, b, c, d, e, f = (float(v) for v in geo["m"])
    det = a * d - b * c
    if abs(det) < 1e-9:
        return None
    wx, wy, ww, wh = (float(v) for v in geo["win"])
    ih, iw = alpha.shape[:2]
    vis, areas = [], []
    for x0, y0, x1, y1 in chars:
        dx, dy = (x1 - x0) * 0.15, (y1 - y0) * 0.15
        xs = np.linspace(x0 + dx, x1 - dx, 5)
        ys = np.linspace(y0 + dy, y1 - dy, 5)
        gx, gy = np.meshgrid(xs, ys)
        inwin = (gx >= wx) & (gx < wx + ww) & (gy >= wy) & (gy < wy + wh)
        X = (d * (gx - e) - c * (gy - f)) / det
        Y = (-b * (gx - e) + a * (gy - f)) / det
        ix = np.clip((X * iw / W).astype(int), 0, iw - 1)
        iy = np.clip((Y * ih / H).astype(int), 0, ih - 1)
        inimg = (X >= 0) & (X < W) & (Y >= 0) & (Y < H)
        al = np.where(inwin & inimg, alpha[iy, ix], 0.0)
        vis.append(float(1 - al.mean()))
        areas.append(max(0.1, (x1 - x0) * (y1 - y0)))
    tot = sum(areas)
    return {"visible": round(sum(v * w for v, w in zip(vis, areas)) / tot, 3),
            "first": round(vis[0], 3), "last": round(vis[-1], 3)}


def _url_path(url: str) -> Path | None:
    try:
        u = urlparse(url)
        if u.scheme != "file":
            return None
        return Path(url2pathname(unquote(u.path)))
    except (ValueError, TypeError):
        return None


def load_alpha(url: str | None) -> np.ndarray | None:
    p = _url_path(url) if url else None
    if p is None or not p.exists():
        return None
    from PIL import Image
    im = Image.open(p)
    if "A" in im.getbands():
        return np.asarray(im.getchannel("A"), dtype=np.float64) / 255.0
    return np.asarray(im.convert("L"), dtype=np.float64) / 255.0


# --------------------------------------------------------------------------- frames
def scene_exception(s: dict) -> str | None:
    from .tokens import EXC_BY_NAME, EXC_REGISTRY
    e = s.get("exception")
    if not isinstance(e, str):
        return None
    return e if e in EXC_REGISTRY else EXC_BY_NAME.get(e, e)


def caption_chunks(pr) -> tuple[list[dict] | None, str]:
    p = Path(pr.work) / "captions.json"
    if not p.exists():
        return None, "renderer"
    try:
        d = read_json(p)
        raw = d.get("chunks") if isinstance(d, dict) else d
        out = [x for x in raw or [] if isinstance(x, dict) and "t0" in x and "t1" in x]
        return sorted(out, key=lambda x: float(x["t0"])), "captions.json"
    except (ValueError, TypeError, KeyError, AttributeError):
        return None, "renderer"


def plan_frames(scenes: list[dict], nframes: int, chunk_spans: list[tuple[int, int]]) -> tuple[set, set]:
    """(contrast frames, extra layout-only frames)."""
    pix, lay = set(), set()
    for s in scenes:
        fin = int(round(float(s.get("t_in", 0)) * FPS))
        fout = max(int(round(float(s.get("t_out", 0)) * FPS)), fin + 1)
        mid = (fin + fout) // 2
        pix.add(mid)
        pix.update(range(min(fin + SETTLE_F, mid), max(fout - EXIT_F, mid), HOLD_STEP))
        exc = scene_exception(s)
        if exc == "E6":
            lay.update(range(fin + 12, fout - 10, 2))
    for f0, f1 in chunk_spans:
        if f1 > f0:
            pix.add((f0 + f1) // 2)
    pix = {n for n in pix if 0 <= n < nframes}
    for s in scenes:
        if scene_exception(s) == "E4" or s.get("ambient"):
            fin, fout = round(float(s.get("t_in", 0)) * FPS), round(float(s.get("t_out", 0)) * FPS)
            lay.update(n + 1 for n in pix if fin <= n < fout - 1)
    lay = {n for n in lay if 0 <= n < nframes} - pix
    return pix, lay


def _chunk_at(chunks: list[dict] | None, n: int) -> dict | None:
    t = n / FPS
    for ch in chunks or []:
        if float(ch["t0"]) - 1e-6 <= t < float(ch["t1"]) - 1e-6:
            return ch
    return None


def measure_text(pr, url: str, scenes: list[dict], nframes: int, pixels: bool = True) -> dict:
    """Run the text pass headless and write plan/measure.text.json; returns a summary."""
    from PIL import Image

    from .core import VeosError
    from .scenes import _open
    chunks, src = caption_chunks(pr)
    chars_for = [s["id"] for s in scenes if s.get("behind") and (s.get("text") or scene_exception(s) == "E1")]
    items_for = [s["id"] for s in scenes if scene_exception(s) == "E4" or s.get("ambient")]
    t0 = time.perf_counter()
    pw, br, pg, logs = _open(url)
    frames: dict[str, dict] = {}
    shots = 0
    try:
        boot = pg.evaluate("window.VEOS_BOOT_ERROR || null")
        if boot:
            raise VeosError("SCENES_BOOT", "player failed to load: " + str(boot)[:1200],
                            "Fix plan/scenes.js (run `veos scenes-meta` for per-scene errors).")
        if not pg.evaluate("typeof window.measureText === 'function'"):
            raise VeosError("RENDERER_OLD", "renderer/core.js has no measureText", "Update the renderer.")
        if chunks is not None:
            spans = [(int(round(float(c["t0"]) * FPS)), int(round(float(c["t1"]) * FPS))) for c in chunks]
        else:
            spans = [(int(c["f0"]), int(c["f1"])) for c in (pg.evaluate("VEOS.cards ? VEOS.cards() : []") or [])]
            chunks = [{"t0": a / FPS, "t1": b / FPS} for a, b in spans]
        pix, lay = plan_frames(scenes, nframes, spans)
        alpha_cache: dict[str, np.ndarray | None] = {}
        for n in sorted(pix | lay):
            want = pixels and n in pix
            try:
                d = pg.evaluate("([n, o]) => window.measureText(n, o)", [n, {"pixels": want, "chars": chars_for, "items": items_for}])
            except Exception as e:  # noqa: BLE001
                msg = str(e).splitlines()[0][:400]
                raise VeosError("SCENE_RENDER_FAILED", f"frame {n}: {msg}", "Fix the scene named in the message.") from None
            img = None
            if want and d.get("texts"):
                h = pg.add_style_tag(content=HIDE_TEXT_CSS)
                img = np.asarray(Image.open(io.BytesIO(pg.screenshot(type="png"))).convert("RGB"))
                h.evaluate("e => e.remove()")
                shots += 1
            geo = d.get("geo")
            for rec in d.get("texts") or []:
                if str(rec.get("scene", "")).startswith("__"):
                    ch = _chunk_at(chunks, n)
                    if ch is not None:
                        rec["chunk"] = {k: ch[k] for k in ("text", "class", "size", "weight", "profile", "exception") if k in ch}
                if img is not None:
                    c = text_contrast(rec, region_lums(img, sample_rect(rec)))
                    if c:
                        rec.update(c)
                chars = rec.pop("chars", None)
                if chars is not None:
                    cut = (geo or {}).get("cut")
                    if cut not in alpha_cache:
                        alpha_cache[cut] = load_alpha(cut)
                    occ = occlusion(chars, geo, alpha_cache[cut])
                    rec["occlusion"] = occ if occ else {"visible": None, "why": "no cut-out frame (stage hidden or c*.webp missing)"}
            frames[str(n)] = {"pixels": img is not None, "texts": d.get("texts") or [],
                              **({"geo": {"m": geo["m"], "win": geo["win"]}} if geo and geo.get("m") else {}),
                              **({"items": d["items"]} if d.get("items") else {}),
                              **({"slots": d["slots"]} if d.get("slots") else {})}
    finally:
        br.close()
        pw.stop()
    dt = time.perf_counter() - t0
    data = {"version": 1, "size": [W, H], "fps": FPS, "pixels": bool(pixels), "captions": src, "frames": frames}
    write_json(pr.path("plan", "measure.text.json"), data, indent=None)
    n_text = sum(len(v["texts"]) for v in frames.values())
    return {"text_file": "plan/measure.text.json", "text_frames": len(frames), "text_elements": n_text,
            "text_screenshots": shots, "text_seconds": round(dt, 1)}
