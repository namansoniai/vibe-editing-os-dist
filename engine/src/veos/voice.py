"""`veos voice`: the edit's voice track (work/voice.wav) built from work/cutmap.json and work/audio/<src>.wav."""
from __future__ import annotations

import wave
from pathlib import Path

import numpy as np

from .core import VeosError, need_project, r3, read_json, run, tools

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


def assemble(cutmap: dict, load) -> np.ndarray:
    """Place each segment at round(t0*SR); equal-power crossfade (sin/cos) at non-contiguous joins.
    The fade straddles the join (h samples of extra source audio each side), so timing is unchanged."""
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
        idx = np.arange(a - p0, b - p0) + s0
        ok = (idx >= 0) & (idx < len(src))
        chunk = np.zeros(len(idx), dtype=np.float32)
        chunk[ok] = src[idx[ok]]
        ramp = np.linspace(0.0, np.pi / 2, 2 * h, endpoint=False) + np.pi / 4 / h  # centred sample positions
        if fade_in:
            chunk[:2 * h] *= np.sin(ramp).astype(np.float32)
        if fade_out:
            chunk[-2 * h:] *= np.cos(ramp).astype(np.float32)
        lo, hi = max(a, 0), min(b, n_total)
        out[lo:hi] += chunk[lo - a:hi - a]
    return out


def _contiguous(a: dict, b: dict) -> bool:
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
    cache: dict = {}
    x = assemble(cutmap, lambda s: _load(project, s, cache))
    out = out or project.work / "voice.wav"
    write_wav(out, x)
    return {"file": project.rel(out), "segments": len(cutmap["segments"]), "duration": r3(len(x) / SR),
            "sources": sorted(cache)}


def main(args, project) -> dict:
    pr = need_project(project)
    return build_voice_wav(pr, pr.abs(args.out))
