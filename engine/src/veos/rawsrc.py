"""Frames of an original clip on the conform grid, without converting the whole clip first.

`veos conform` makes a constant 30 fps copy with ffmpeg's fps filter and `-fps_mode cfr`: frame k of the copy is the
input frame nearest grid slot k, in 1/30 s units of the clip's own timeline (which starts at the file's start_time; a
video stream that starts later than the file is padded from slot 0 with its first frame). Every frame index the engine
stores (cut map `in_frame`, face boxes, cut-out ranges, tracks) is an index into that grid.

To get frames [a, a + n) of that grid straight from the original: seek to a grid-aligned point T = k0 / 30 a little
before `a` (an accurate seek drops the frames before T and shifts timestamps by exactly k0 slots), run the same fps
filter anchored at T (start_time=0), and trim to [a - k0, ...). The fps filter's choice for a slot depends only on the
input frames around it, so from PRE_F frames after the seek point on it picks the same frames as one pass over the
whole clip (tests compare decoded pixels). Only the stretch around the wanted frames is decoded.

Used by `veos cut` (the review proxy, before anything is converted), `veos look --src` (retake stills) and
`veos conform` after the cut (only the kept ranges are converted at full quality).
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path

from .core import FPS, VeosError, run, tools

PRE_F = 60       # frames decoded before the first wanted one (2 s): the fps filter's choice there has settled
TAIL_F = 3       # frames read past the last wanted one (the fps filter looks one frame ahead)
BT601 = {"smpte170m", "bt470bg", "smpte240m"}
# conform writes BT.709-tagged limited-range yuv420p, so ffmpeg converts any other (or unknown) colour space into it on
# the way to the encoder. Encoders given the same tags (the kept-range conform, the review proxy) get that for free;
# a reader that decodes to RGB (retake stills) appends this to see the colours the conformed copy has.
AS_CONFORMED = ("scale=out_color_matrix=bt709:out_range=tv,format=yuv420p,"
                "setparams=colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv")


@dataclass
class Grid:
    path: Path
    start: float          # the file's start_time (seconds): the timeline origin ffmpeg uses when not seeking
    a0: int               # the first video frame's slot on the 1/30 s grid (slots before it repeat that frame)
    frames: int           # how many frames the conformed copy has
    width: int            # displayed size (rotation applied, as the decoder outputs it)
    height: int
    bt601: bool           # convert BT.601 colour to BT.709, as conform does

    def color_filter(self) -> str:
        return "scale=in_color_matrix=bt601:out_color_matrix=bt709:out_range=tv" if self.bt601 else ""


def _probe(path: Path) -> dict:
    r = run([tools().ffprobe, "-v", "error", "-show_entries",
             "format=start_time,duration:stream=codec_type,width,height,duration,start_time,color_space"
             ":stream_side_data=rotation:stream_tags=rotate", "-of", "json", str(path)])
    return json.loads(r.stdout.decode("utf-8", "replace") or "{}")


def _first_pts(path: Path) -> float | None:
    r = run([tools().ffprobe, "-v", "error", "-select_streams", "v:0", "-read_intervals", "%+#1", "-show_entries",
             "frame=pts_time,best_effort_timestamp_time", "-of", "json", str(path)], check=False)
    try:
        fr = (json.loads(r.stdout.decode("utf-8", "replace") or "{}").get("frames") or [{}])[0]
    except ValueError:
        return None
    for k in ("pts_time", "best_effort_timestamp_time"):
        try:
            return float(fr[k])
        except (KeyError, TypeError, ValueError):
            continue
    return None


def _end_pts(path: Path, approx_end: float) -> float | None:
    """When the last shown frame ends (its pts + its duration), read from the packets of the last few seconds; this is
    the end-of-stream time ffmpeg hands the fps filter (a stream's own duration can be one frame short of it)."""
    pk: list[tuple[float, float]] = []
    for back in (3.0, 12.0, None):  # a seek that reads nothing (seen once, not reproducible) falls back to further back
        iv = ["-read_intervals", f"{max(0.0, approx_end - back):.3f}%"] if back is not None else []
        r = run([tools().ffprobe, "-v", "error", "-select_streams", "v:0", *iv,
                 "-show_entries", "packet=pts_time,duration_time", "-of", "csv=p=0", str(path)], check=False)
        for line in r.stdout.decode("utf-8", "replace").splitlines():
            p = line.strip().split(",")
            try:
                pk.append((float(p[0]), float(p[1]) if len(p) > 1 and p[1] not in ("", "N/A") else 0.0))
            except (ValueError, IndexError):
                continue
        if pk:
            break
    if not pk:
        return None
    pk.sort()
    pts, dur = pk[-1]
    if dur <= 0 and len(pk) > 1:  # no packet duration: ffmpeg repeats the last gap between frames
        dur = pts - pk[-2][0]
    return pts + dur


def _round_near(x: float) -> int:
    """av_rescale_q_rnd(..., AV_ROUND_NEAR_INF): halves away from zero."""
    return int(math.floor(x + 0.5)) if x >= 0 else -int(math.floor(-x + 0.5))


def grid(path: str | Path) -> Grid:
    """The conform grid of a clip (cheap: two ffprobe calls, one decoded frame)."""
    path = Path(path)
    if not path.is_file():
        raise VeosError("SOURCE_MISSING", f"source file not found: {path}", "Move it back or re-run `veos ingest`.")
    j = _probe(path)
    fmt = j.get("format") or {}
    v = next((s for s in j.get("streams") or [] if s.get("codec_type") == "video"), None)
    if not v:
        raise VeosError("NO_PICTURE", f"{path.name} has no video stream", "Pass a clip with picture.")
    start = float(fmt.get("start_time") or 0.0)
    first = _first_pts(path)
    if first is None:
        first = float(v.get("start_time") or start)
    a0 = _round_near((first - start) * FPS)
    vdur = float(v.get("duration") or fmt.get("duration") or 0.0)
    vstart = float(v.get("start_time") or first)
    end = _end_pts(path, vstart + vdur) or vstart + vdur
    # conform's frame count: slots 0 .. the end of the last frame on the same timeline (the fps filter stops there)
    frames = max(1, _round_near((end - start) * FPS))
    w, h = int(v.get("width") or 0), int(v.get("height") or 0)
    rot = 0
    for sd in v.get("side_data_list") or []:
        if "rotation" in sd:
            rot = int(round(float(sd["rotation"])))
    if not rot and (v.get("tags") or {}).get("rotate"):
        rot = int(float(v["tags"]["rotate"]))
    if abs(rot) % 180 == 90:
        w, h = h, w
    return Grid(path, start, a0, frames, w, h, (v.get("color_space") or "") in BT601)


def seek(g: Grid, a: int, n: int) -> tuple[list[str], str]:
    """Input options and the filter chain that yield exactly grid frames [a, a + n) of `g` (fewer only past the end).

    The chain starts with the fps filter and ends with the trim; append scaling etc. after it."""
    if a < 0 or n < 1:
        raise ValueError(f"bad frame range {a}+{n}")
    k0 = a - PRE_F
    if k0 <= 0:  # near the start: one pass from the top, padded from slot 0 exactly as conform's cfr output is
        pre = ["-t", f"{(a + n + TAIL_F + 1) / FPS:.6f}"]
        return pre, f"fps={FPS}:start_time=0,trim=start_frame={a}:end_frame={a + n}"
    pre = ["-ss", f"{k0 / FPS:.6f}", "-t", f"{(n + PRE_F + TAIL_F + 1) / FPS:.6f}"]
    return pre, f"fps={FPS}:start_time=0,trim=start_frame={a - k0}:end_frame={a - k0 + n}"


def chain(g: Grid, a: int, n: int, *extra: str) -> tuple[list[str], str]:
    """`seek` plus conform's colour conversion and any further filters, as one comma-joined chain."""
    pre, base = seek(g, a, n)
    parts = [base, g.color_filter(), *extra]
    return pre, ",".join(p for p in parts if p)
