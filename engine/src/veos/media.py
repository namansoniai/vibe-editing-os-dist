"""Shared media helpers: ffprobe parsing, loudness, scene cuts, frame sampling."""
from __future__ import annotations

import json
import re
import subprocess
from fractions import Fraction
from pathlib import Path

import numpy as np

from .core import VeosError, tools

VIDEO_EXT = {".mp4", ".mov", ".m4v", ".mkv", ".webm", ".avi", ".mts", ".mxf", ".wmv", ".flv"}
AUDIO_EXT = {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".opus", ".aif", ".aiff"}


def _frac(s: str | None) -> float:
    try:
        f = Fraction(s or "0/0")
        return float(f)
    except (ZeroDivisionError, ValueError):
        return 0.0


def probe(path: str | Path) -> dict:
    """Parse ffprobe. Returns {duration, video: {...}|None, audio: [{stream, index, codec, channels, sample_rate, duration}]}.

    video: index, codec, width, height (stored, before rotation), disp_w/disp_h (after rotation), rotation (0/90/180/270),
    fps_in (str of r_frame_rate), fps (float, avg), vfr (bool), frames (int|None), duration.
    `audio[i]["stream"]` is the audio-relative index (0:a:N). Data/subtitle streams are ignored.
    """
    r = subprocess.run([tools().ffprobe, "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)],
                       capture_output=True)
    if r.returncode != 0:
        raise VeosError("PROBE_FAILED", f"ffprobe could not read {Path(path).name}",
                        "The file may be corrupt or not a media file.")
    j = json.loads(r.stdout.decode("utf-8", "replace") or "{}")
    streams = j.get("streams", [])
    fmt_dur = float(j.get("format", {}).get("duration") or 0)
    video = None
    for s in streams:
        if s.get("codec_type") != "video" or s.get("disposition", {}).get("attached_pic"):
            continue
        rot = 0
        if "rotation" in s.get("tags", {}):
            rot = int(float(s["tags"]["rotation"]))
        for sd in s.get("side_data_list", []) or []:
            if "rotation" in sd:
                rot = int(round(float(sd["rotation"])))
        rot %= 360
        w, h = int(s["width"]), int(s["height"])
        rfr, afr = _frac(s.get("r_frame_rate")), _frac(s.get("avg_frame_rate"))
        vfr = bool(rfr and afr and abs(rfr - afr) / rfr > 0.01)
        dur = float(s.get("duration") or fmt_dur or 0)
        nb = int(s["nb_frames"]) if str(s.get("nb_frames", "")).isdigit() else None
        video = {"index": s["index"], "codec": s.get("codec_name"), "width": w, "height": h,
                 "disp_w": h if rot in (90, 270) else w, "disp_h": w if rot in (90, 270) else h,
                 "rotation": rot, "fps_in": s.get("r_frame_rate", "0/0"), "fps": afr or rfr, "vfr": vfr,
                 "frames": nb, "duration": dur}
        break
    audio = []
    for s in streams:
        if s.get("codec_type") == "audio":
            audio.append({"stream": len(audio), "index": s["index"], "codec": s.get("codec_name"),
                          "channels": int(s.get("channels", 0)), "sample_rate": int(s.get("sample_rate", 0) or 0),
                          "duration": float(s.get("duration") or fmt_dur or 0)})
    duration = video["duration"] if video else (audio[0]["duration"] if audio else fmt_dur)
    if video and fmt_dur:
        duration = max(duration, 0) or fmt_dur
    return {"duration": duration, "format_duration": fmt_dur, "video": video, "audio": audio}


def loudness(path: str | Path, stream: int = 0) -> tuple[float | None, float | None]:
    """Integrated LUFS and true peak (dBTP) of audio stream `stream` (audio-relative). None, None if silent/none."""
    r = subprocess.run([tools().ffmpeg, "-hide_banner", "-nostats", "-i", str(path), "-map", f"0:a:{stream}",
                        "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True)
    txt = r.stderr.decode("utf-8", "replace")
    tail = txt[txt.rfind("Summary:"):] if "Summary:" in txt else ""
    m = re.search(r"\bI:\s+(-?[\d.]+|-inf)\s+LUFS", tail)
    p = re.search(r"True peak:.*?Peak:\s+(-?[\d.]+|-inf)\s+dBFS", tail, re.S)

    def num(g):
        if g is None or g.group(1) == "-inf":
            return None
        return round(float(g.group(1)), 1)
    return num(m), num(p)


def scene_cuts(path: str | Path, threshold: float = 0.3, scale_w: int = 320) -> list[float]:
    """Times (s) of hard scene changes, via ffmpeg select(scene)."""
    vf = f"scale={scale_w}:-2,select='gt(scene,{threshold})',showinfo"
    r = subprocess.run([tools().ffmpeg, "-hide_banner", "-nostats", "-i", str(path), "-an", "-vf", vf, "-f", "null", "-"],
                       capture_output=True)
    txt = r.stderr.decode("utf-8", "replace")
    return [round(float(x), 3) for x in re.findall(r"pts_time:\s*(-?[\d.]+)", txt)]


def sample_frames(path: str | Path, times: list[float], width: int = 360) -> list[np.ndarray]:
    """RGB uint8 frames at `times`, resized to `width` (aspect kept; rotation applied by the decoder)."""
    import cv2
    cap = cv2.VideoCapture(str(path))
    out = []
    try:
        for t in times:
            cap.set(cv2.CAP_PROP_POS_MSEC, max(0.0, t) * 1000.0)
            ok, f = cap.read()
            if not ok:
                f = out[-1] if out else None
                if f is None:
                    raise VeosError("DECODE_FAILED", f"cannot decode frame at {t:.2f}s of {Path(path).name}")
                out.append(f)
                continue
            h, w = f.shape[:2]
            if w != width:
                f = cv2.resize(f, (width, max(1, round(h * width / w))), interpolation=cv2.INTER_AREA)
            out.append(cv2.cvtColor(f, cv2.COLOR_BGR2RGB))
    finally:
        cap.release()
    return out


def iter_gray_frames(path: str | Path, step: float, width: int = 160, t0: float = 0.0, t1: float | None = None):
    """Yield (t, gray uint8 array) at a fixed step using ffmpeg's fps filter (fast sequential decode)."""
    pr = probe(path)
    v = pr["video"]
    if not v:
        return
    w = width - width % 2
    h = max(2, round(v["disp_h"] * w / v["disp_w"] / 2) * 2)
    cmd = [tools().ffmpeg, "-v", "error", "-ss", str(t0)]
    if t1 is not None:
        cmd += ["-t", str(t1 - t0)]
    cmd += ["-i", str(path), "-an", "-vf", f"fps=1/{step},scale={w}:{h}", "-pix_fmt", "gray", "-f", "rawvideo", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    n = 0
    try:
        while True:
            buf = p.stdout.read(w * h)
            if len(buf) < w * h:
                break
            yield t0 + n * step, np.frombuffer(buf, np.uint8).reshape(h, w)
            n += 1
    finally:
        p.stdout.close()
        p.kill()
        p.wait()
