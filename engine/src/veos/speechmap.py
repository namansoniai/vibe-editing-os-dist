"""The speech map: where the AUDIO has someone speaking and where it is silent (source seconds per clip).

The cut follows the sound, not the transcript: Whisper can lay a word over a silence ("you." hallucinated over a 2 s
look-away) or stretch one across it ("और" over 1.1 s), so word gaps alone hide dead air (09-silences.md).

    speech   = Silero VAD speech (the model bundled with faster-whisper; any language, robust to room tone)
               UNION the frames louder than an energy threshold (20 ms RMS)
    silences = the gaps between speech (>= SIL_MIN)

The union is deliberately conservative: a stretch is silent only when neither the VAD nor the level hears anything, so
regional speech, soft endings and breaths are never called silence. The energy threshold is -42 dB, raised with the
noise floor (floor + 10 dB, at most -30 dB) only when the VAD is there to guard the speech. Without the VAD (older
faster-whisper, model missing) it is the plain -42 dB rule the engine always used.

Where the maps live: `veos transcribe` writes `speech` / `silences` into work/words/<id>.json. `for_source` reads them
from there, else from a cache (work/speech/<id>.json), else measures work/audio/<id>.wav (a second or two per minute),
else falls back to an older transcript's `silences`.

Edit-time views over a cut map (`veos cut`): `dead_air` (every silence >= DEAD_AIR in edit seconds, joins merged) and
`dropped_speech` (speech the EDL leaves out, with the words there; `clipped` = a cut point inside speech).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

from .core import FPS, r3, read_json, write_json

SR = 16000
HOP = 0.02            # 20 ms RMS frames
SIL_DB = -42.0        # quieter than this is silence (the engine's long-standing rule)
SIL_MAX_DB = -30.0    # the noise-adapted threshold never goes above this
FLOOR_MARGIN = 10.0   # noise floor (10th percentile) + this = the adapted threshold
SIL_MIN = 0.18        # shortest silence in the map (transcribe chunking, start fix)
LIST_MIN = 0.25       # shortest silence listed for the cutter / used by the transcript clean-up
DEAD_AIR = 0.6        # a silence this long in the cut is dead air
DROP_MIN = 0.10       # dropped speech shorter than this is not reported (clicks)
VAD = {"threshold": 0.4, "min_speech_duration_ms": 0, "min_silence_duration_ms": 150, "speech_pad_ms": 60}


# ---------------------------------------------------------------- interval helpers
def merge(iv: list, join: float = 0.0) -> list[list[float]]:
    """Sorted union of [a, b] intervals; intervals closer than `join` are merged."""
    out: list[list[float]] = []
    for a, b in sorted([float(a), float(b)] for a, b in iv if b > a):
        if out and a <= out[-1][1] + join:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def gaps(speech: list, dur: float, min_len: float = SIL_MIN) -> list[list[float]]:
    """The silences of [0, dur] not covered by `speech`, at least `min_len` long."""
    out, t = [], 0.0
    for a, b in merge(speech):
        if a - t >= min_len - 1e-9:
            out.append([r3(t), r3(a)])
        t = max(t, b)
    if dur - t >= min_len - 1e-9:
        out.append([r3(t), r3(dur)])
    return out


def overlap(a0: float, a1: float, b0: float, b1: float) -> float:
    return max(0.0, min(a1, b1) - max(a0, b0))


def subtract(iv: list, cut: list) -> list[list[float]]:
    """Parts of the intervals `iv` outside the intervals `cut`."""
    cut = merge(cut)
    out = []
    for a, b in merge(iv):
        cur = a
        for c0, c1 in cut:
            if c1 <= cur or c0 >= b:
                continue
            if c0 > cur:
                out.append([cur, c0])
            cur = max(cur, c1)
        if b > cur:
            out.append([cur, b])
    return out


# ---------------------------------------------------------------- measuring
def rms_db(audio: np.ndarray, hop: float = HOP) -> np.ndarray:
    h = int(round(hop * SR))
    n = len(audio) // h
    if n == 0:
        return np.zeros(0, np.float32)
    x = audio[: n * h].astype(np.float32).reshape(n, h)
    return (20 * np.log10(np.sqrt((x ** 2).mean(axis=1)) + 1e-9)).astype(np.float32)


def threshold_db(db: np.ndarray, guarded: bool) -> float:
    """-42 dB; raised with the noise floor (at most -30 dB) only when the VAD guards the speech."""
    if not guarded or len(db) == 0:
        return SIL_DB
    floor = float(np.percentile(db, 10))
    return float(min(SIL_MAX_DB, max(SIL_DB, floor + FLOOR_MARGIN)))


def energy_speech(db: np.ndarray, thr: float, min_sil: float = SIL_MIN) -> list[list[float]]:
    """Frames at or above `thr` are sound; quiet runs shorter than `min_sil` stay inside the sound around them."""
    quiet = db < thr
    n = len(quiet)
    sil, i = [], 0
    while i < n:
        if quiet[i]:
            j = i
            while j < n and quiet[j]:
                j += 1
            if (j - i) * HOP >= min_sil - 1e-9:
                sil.append([i * HOP, j * HOP])
            i = j
        else:
            i += 1
    return subtract([[0.0, n * HOP]], sil)


def vad_speech(audio: np.ndarray) -> list[list[float]] | None:
    """Silero VAD speech regions (seconds), or None when the VAD can't run here."""
    try:
        from faster_whisper.vad import VadOptions, get_speech_timestamps
        try:
            opts = VadOptions(**VAD)
        except TypeError:  # an older faster-whisper with fewer fields
            opts = VadOptions(threshold=VAD["threshold"], min_silence_duration_ms=VAD["min_silence_duration_ms"],
                              speech_pad_ms=VAD["speech_pad_ms"])
        ts = get_speech_timestamps(np.ascontiguousarray(audio, dtype=np.float32), opts)
        return [[t["start"] / SR, t["end"] / SR] for t in ts]
    except Exception:  # noqa: BLE001 - the VAD is a guard; the energy rule still works without it
        return None


def build(audio: np.ndarray, *, vad: bool = True) -> dict:
    """16 kHz mono float audio -> {"speech", "silences", "method", "threshold_db", "duration"} (seconds)."""
    dur = len(audio) / SR
    db = rms_db(audio)
    v = vad_speech(audio) if vad else None
    thr = threshold_db(db, v is not None)
    speech = energy_speech(db, thr)
    if v is not None:
        speech = merge(speech + v)
    speech = [[r3(max(0.0, a)), r3(min(dur, b))] for a, b in speech if min(dur, b) > max(0.0, a)]
    end = len(db) * HOP  # the last whole 20 ms frame (as the energy rule has always measured)
    return {"speech": speech, "silences": gaps(speech, end), "method": "vad+energy" if v is not None else "energy",
            "threshold_db": round(thr, 1), "duration": r3(dur)}


def load_audio(path: str | Path) -> np.ndarray:
    from faster_whisper.audio import decode_audio
    return decode_audio(str(path), sampling_rate=SR)


# ---------------------------------------------------------------- per source
def for_source(proj, sid: str, duration: float | None = None) -> dict | None:
    """The speech map of one source: transcript > cache > measured from work/audio/<id>.wav > an older transcript's
    silences. None when there is nothing to go on."""
    wp = proj.work / "words" / f"{sid}.json"
    wd = None
    if wp.exists():
        try:
            wd = read_json(wp)
        except ValueError:
            wd = None
    if wd and isinstance(wd.get("speech"), list):
        return {"speech": wd["speech"], "silences": wd.get("silences") or [], "method": wd.get("speech_method") or "transcribe"}
    wav = proj.work / "audio" / f"{sid}.wav"
    if wav.exists():
        cp = proj.work / "speech" / f"{sid}.json"
        stamp = [wav.stat().st_size, wav.stat().st_mtime_ns]
        if cp.exists():
            try:
                c = read_json(cp)
                if c.get("stamp") == stamp:
                    return c
            except ValueError:
                pass
        try:
            m = build(load_audio(wav))
        except Exception:  # noqa: BLE001 - informational only: fall back to the transcript
            m = None
        if m is not None:
            m["stamp"] = stamp
            write_json(proj.path("work", "speech", f"{sid}.json"), m, indent=None)
            return m
    if wd and isinstance(wd.get("silences"), list) and duration:
        return {"speech": gaps(wd["silences"], float(duration), 0.0), "silences": wd["silences"],
                "method": "older transcript silences"}
    return None


# ---------------------------------------------------------------- edit-time views over a cut map
def _span(seg: dict) -> tuple[float, float, float]:
    """(source start s, source end s, speed) of a cut-map segment."""
    from .cut import seg_speed, src_frames
    lo = seg["in_frame"] / FPS
    return lo, lo + src_frames(seg) / FPS, seg_speed(seg)


def to_edit(cutmap: dict, per_src: dict[str, list], join: float = 1e-3) -> list[list[float]]:
    """Source intervals per source id -> edit-time intervals (merged across segment joins)."""
    out = []
    for seg in cutmap.get("segments") or []:
        iv = per_src.get(seg["src"])
        if not iv:
            continue
        lo, hi, sp = _span(seg)
        for a, b in iv:
            a2, b2 = max(a, lo), min(b, hi)
            if b2 - a2 > 1e-3:
                out.append([seg["t0"] + (a2 - lo) / sp, min(seg["t1"], seg["t0"] + (b2 - lo) / sp)])
    return [[r3(a), r3(b)] for a, b in merge(out, join)]


def dead_air(cutmap: dict, maps: dict[str, dict], min_len: float = DEAD_AIR) -> list[dict]:
    """Every silence of at least `min_len` edit seconds in the cut (a silence ending one segment and the one opening
    the next count as one)."""
    sil = to_edit(cutmap, {k: (m or {}).get("silences") or [] for k, m in maps.items()}, join=0.011)
    return [{"t0": a, "t1": b, "dur": r3(b - a)} for a, b in sil if b - a >= min_len - 1e-9]


def dropped_speech(cutmap: dict, maps: dict[str, dict], words: dict[str, list] | None = None,
                   min_len: float = DROP_MIN) -> list[dict]:
    """Speech (per the audio) in the sources the cut uses that the cut leaves out. `clipped`: the dropped speech runs
    straight into a kept segment, so that cut point is inside speech (`cut_at` = its edit time)."""
    words = words or {}
    segs = cutmap.get("segments") or []
    out = []
    for sid in dict.fromkeys(s["src"] for s in segs):
        m = maps.get(sid)
        if not m:
            continue
        kept = []
        for s in segs:
            if s["src"] == sid:
                lo, hi, _ = _span(s)
                kept.append([lo, hi, s])
        for a, b in subtract(m.get("speech") or [], [[x, y] for x, y, _ in kept]):
            if b - a < min_len - 1e-9:
                continue
            item = {"src": sid, "at": [r3(a), r3(b)], "dur": r3(b - a)}
            ws = [w for w in words.get(sid) or [] if not w.get("suspect")
                  and overlap(w["s"], w["e"], a, b) >= min(0.05, 0.5 * (w["e"] - w["s"]))]
            item["words"] = " ".join(str(w.get("w", "")) for w in ws[:14]) + (" …" if len(ws) > 14 else "")
            for lo, hi, s in kept:  # the speech runs on into a kept segment: that cut point is inside speech
                if abs(b - lo) < 0.02:
                    item["clipped"], item["cut_at"] = True, r3(s["t0"])
                elif abs(a - hi) < 0.02:
                    item["clipped"], item["cut_at"] = True, r3(s["t1"])
            out.append(item)
    return out
