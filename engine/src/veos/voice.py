"""`veos voice`: the edit's voice track (work/voice.wav) built from work/cutmap.json and work/audio/<src>.wav."""
from __future__ import annotations

import wave
from pathlib import Path

import numpy as np

from .core import FPS, VeosError, need_project, r3, read_json, run, tools

SR = 48000
XFADE_S = 0.008       # total crossfade length at a join (equal power)


def add_args(p, cmd):
    p.add_argument("--out", default="work/voice.wav", help="output wav, relative to the project (default work/voice.wav)")


def _load(project, src: str, cache: dict) -> np.ndarray:
    if src not in cache:
        wav = project.work / "audio" / f"{src}.wav"
        if not wav.exists():
            raise VeosError("AUDIO_MISSING", f"missing {wav}", "Run `veos conform` first.")
        r = run([tools().ffmpeg, "-v", "error", "-i", str(wav), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                project, "voice")
        cache[src] = np.frombuffer(r.stdout, dtype="<f4").astype(np.float32)
    return cache[src]


def stretch(x: np.ndarray, speed: float) -> np.ndarray:
    """Play `x` (mono float, SR) `speed` times faster with the pitch kept (ffmpeg atempo, as the cut proxy)."""
    if len(x) == 0:
        return x
    r = run([tools().ffmpeg, "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
             "-af", f"atempo={speed:.2f}", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-"],
            input=np.ascontiguousarray(x, dtype="<f4").tobytes())
    return np.frombuffer(r.stdout, dtype="<f4").astype(np.float32)


def _take(src: np.ndarray, s0: int, n: int) -> np.ndarray:
    """src[s0 : s0 + n], zero-filled outside the source."""
    idx = np.arange(s0, s0 + n)
    ok = (idx >= 0) & (idx < len(src))
    chunk = np.zeros(n, dtype=np.float32)
    chunk[ok] = src[idx[ok]]
    return chunk


def assemble(cutmap: dict, load, stretch_fn=None) -> np.ndarray:
    """Place each segment at round(t0*SR); equal-power crossfade (sin/cos) at non-contiguous joins.
    The fade straddles the join (h samples of extra source audio each side), so timing is unchanged.
    A segment with `speed` > 1 is time-stretched (pitch kept) so it fills exactly its edit span."""
    from .cut import seg_speed, src_frames
    stretch_fn = stretch_fn or stretch
    n_total = int(round(cutmap["duration"] * SR))
    segs = cutmap["segments"]
    h = int(round(XFADE_S * SR / 2))
    out = np.zeros(n_total, dtype=np.float32)
    for k, sg in enumerate(segs):
        src = load(sg["src"])
        p0 = int(round(sg["t0"] * SR))
        p1 = n_total if k == len(segs) - 1 else int(round(sg["t1"] * SR))
        s0 = int(round(sg["in"] * SR))
        fade_in = k > 0 and not _contiguous(segs[k - 1], sg)
        fade_out = k < len(segs) - 1 and not _contiguous(sg, segs[k + 1])
        a, b = p0 - (h if fade_in else 0), p1 + (h if fade_out else 0)
        sp = seg_speed(sg)
        if sp == 1.0:
            chunk = _take(src, s0 + (a - p0), b - a)
        else:  # source span (+ margins for the fades and the stretcher's edges) -> stretched -> this edit span
            m = int(round(0.05 * SR))
            pre = int(round((p0 - a) * sp)) + m
            ns = int(round(src_frames(sg) / FPS * SR))
            y = stretch_fn(_take(src, s0 - pre, pre + ns + int(round((b - p1) * sp)) + m), sp)
            off = int(round(pre / sp)) - (p0 - a)
            chunk = _take(y, off, b - a)
        ramp = np.linspace(0.0, np.pi / 2, 2 * h, endpoint=False) + np.pi / 4 / h  # centred sample positions
        if fade_in:
            chunk[:2 * h] *= np.sin(ramp).astype(np.float32)
        if fade_out:
            chunk[-2 * h:] *= np.cos(ramp).astype(np.float32)
        lo, hi = max(a, 0), min(b, n_total)
        out[lo:hi] += chunk[lo - a:hi - a]
    return out


def _contiguous(a: dict, b: dict) -> bool:
    from .cut import seg_speed, src_frames
    if seg_speed(a) != 1.0 or seg_speed(b) != 1.0:  # sped segments join on source frames
        return a["src"] == b["src"] and a["in_frame"] + src_frames(a) == b["in_frame"]
    return a["src"] == b["src"] and abs((a["in"] + (a["t1"] - a["t0"])) - b["in"]) < 1.0 / SR


def write_wav(path: Path, x: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pcm = (np.clip(x, -1.0, 1.0) * 32767.0).round().astype("<i2")
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


def build_voice_wav(project, out: Path | None = None) -> dict:
    cm = project.work / "cutmap.json"
    if not cm.exists():
        raise VeosError("NO_CUTMAP", "work/cutmap.json missing", "Run `veos cut` first.")
    cutmap = read_json(cm)
    out = out or project.work / "voice.wav"
    from .novoice import build_bed, is_no_voice
    if is_no_voice(project):  # nobody speaks: the reel's sound is the cut's music bed (or the clips' own sound)
        x, info = build_bed(project, cutmap)
        write_wav(out, x)
        return {"file": project.rel(out), "segments": len(cutmap["segments"]), "duration": r3(len(x) / SR),
                "bed": info}
    cache: dict = {}
    x = assemble(cutmap, lambda s: _load(project, s, cache))
    write_wav(out, x)
    return {"file": project.rel(out), "segments": len(cutmap["segments"]), "duration": r3(len(x) / SR),
            "sources": sorted(cache)}


def main(args, project) -> dict:
    pr = need_project(project)
    return build_voice_wav(pr, pr.abs(args.out))
