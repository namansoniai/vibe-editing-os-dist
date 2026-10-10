"""`veos beats`: the music's beat map for no-voice reels -> work/beats.json.

A no-voice reel (B-roll / screen recording / photos + music + on-screen text) is cut and planned to the music, the way a
speech reel is cut and planned to the words. This module finds, for the project's music track (sources.json kind `music`,
else the cut's own sound, else `--file`):
  - tempo (BPM) and every beat time,
  - downbeats (bar starts, 4/4 assumed; `downbeat_confidence` says how clear the accent was),
  - energy per bar and over time (0..1, 2 Hz), section changes (bars where the energy or the sound clearly changes: a
    drop, a build, a break), and the strongest hits (accents that are worth a cut or a word).

Method (numpy/scipy only, no new dependency): mono 22.05 kHz decode -> STFT (1024 / hop 256) -> 48 log-spaced bands in
dB -> spectral flux = the onset envelope (and a low-band flux for the downbeat). Tempo = autocorrelation of the onset
envelope weighted by a log-normal prior around 120 BPM (as librosa does); beats = Ellis' dynamic-programming tracker;
each beat is then refined to the sharp energy rise near it (5 ms envelope), so times are good to about a frame at 30 fps.

beats.json times are in `time` units: "music" = seconds into the music file (`source.id`), "edit" = edit seconds (the
cut's own sound was analysed), "file" = seconds into `--file`. `edit_map(doc, cut_audio, duration)` maps them into edit
time for a cut (music `in` offset and loops applied); `veos context` and `veos cut --snap-beats` use it.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

from .core import FPS, VeosError, need_project, r3, read_json, write_json

SR = 22050
NFFT = 1024
HOP = 256
BANDS = 48
FMIN, FMAX = 30.0, 11000.0
LOW_HZ = 160.0                    # bands below this feed the downbeat (kick / bass) flux
TOP_DB = 80.0
BPM_PRIOR, BPM_STD = 120.0, 1.0   # log-normal prior on tempo (octaves), librosa's default
BPM_MIN, BPM_MAX = 40.0, 240.0
TIGHTNESS = 100.0                 # Ellis DP: how hard beats are held to the tempo
METER = 4
ENERGY_HOP = 0.5
REFINE_S = 0.015                  # a beat moves at most this much to the sharp attack next to it
MIN_SECTION_BARS = 4


def add_args(p, cmd):
    p.add_argument("--src", default=None, help="analyse this source id (default: the music source, else the cut's sound)")
    p.add_argument("--file", default=None, help="analyse any audio/video file instead (times are file seconds)")
    p.add_argument("--out", default="work/beats.json", help="output, relative to the project (default work/beats.json)")


# ------------------------------------------------------------------ analysis
def _frames(y: np.ndarray) -> np.ndarray:
    """Power spectrum of centred, Hann-windowed frames (n_frames x NFFT/2+1), computed in chunks."""
    pad = NFFT // 2
    y = np.pad(y.astype(np.float32), (pad, pad))
    if len(y) < NFFT:
        y = np.pad(y, (0, NFFT - len(y)))
    view = np.lib.stride_tricks.sliding_window_view(y, NFFT)[::HOP]
    win = np.hanning(NFFT).astype(np.float32)
    out = np.empty((len(view), NFFT // 2 + 1), np.float32)
    for a in range(0, len(view), 2048):
        spec = np.fft.rfft(view[a:a + 2048] * win, axis=1)
        out[a:a + 2048] = (spec.real ** 2 + spec.imag ** 2).astype(np.float32)
    return out


def _band_matrix() -> tuple[np.ndarray, np.ndarray]:
    """Triangular log-spaced filterbank (BANDS x bins) and the band centre frequencies."""
    freqs = np.fft.rfftfreq(NFFT, 1.0 / SR)
    edges = np.geomspace(FMIN, FMAX, BANDS + 2)
    fb = np.zeros((BANDS, len(freqs)), np.float32)
    for b in range(BANDS):
        lo, c, hi = edges[b], edges[b + 1], edges[b + 2]
        up = (freqs - lo) / max(c - lo, 1e-9)
        down = (hi - freqs) / max(hi - c, 1e-9)
        fb[b] = np.clip(np.minimum(up, down), 0, None)
        if not fb[b].any():  # a band narrower than a bin: take the nearest bin
            fb[b, int(np.argmin(np.abs(freqs - c)))] = 1.0
    return fb, edges[1:-1]


def analyse(y: np.ndarray) -> dict:
    """Onset envelopes and band energies of a mono signal at SR."""
    P = _frames(y)
    fb, centres = _band_matrix()
    bands = P @ fb.T                                         # power per band
    db = 10 * np.log10(np.maximum(bands, 1e-10))
    db = np.maximum(db, db.max() - TOP_DB)
    flux = np.maximum(0.0, np.diff(db, axis=0, prepend=db[:1]))
    onset = flux.mean(axis=1)
    edge = NFFT // (2 * HOP) + 1  # frames whose window runs past the end of the file: an abrupt end is not an onset
    onset[-edge:] = 0.0
    low = flux[:, centres < LOW_HZ].mean(axis=1) if (centres < LOW_HZ).any() else onset
    # remove the slow trend (a crescendo is not an onset), keep it non-negative
    k = max(3, int(round(0.4 * SR / HOP)) | 1)
    trend = np.convolve(onset, np.ones(k) / k, mode="same")
    onset = np.maximum(0.0, onset - trend)
    # level-adaptive: a quiet verse's beats count as much as a loud chorus's (divide by the local RMS over ~4 s)
    w = max(3, int(round(4.0 * SR / HOP)) | 1)
    local_rms = np.sqrt(np.convolve(onset ** 2, np.ones(w) / w, mode="same"))
    onset = onset / (local_rms + 0.1 * (np.sqrt(np.mean(onset ** 2)) + 1e-9))
    total_db = 10 * np.log10(np.maximum(bands.sum(axis=1), 1e-10))
    return {"onset": onset, "low": low, "band_db": db, "total_db": total_db, "fps": SR / HOP}


def estimate_tempo(onset: np.ndarray, fps: float) -> float:
    """BPM from the onset autocorrelation weighted by a log-normal prior around 120 BPM."""
    x = onset - onset.mean()
    n = len(x)
    if n < 8 or not np.any(x):
        return BPM_PRIOR
    size = 1 << int(np.ceil(np.log2(2 * n)))
    f = np.fft.rfft(x, size)
    ac = np.fft.irfft(f * np.conj(f), size)[:n]
    lag_min = max(1, int(np.floor(60.0 * fps / BPM_MAX)))
    lag_max = min(n - 2, int(np.ceil(60.0 * fps / BPM_MIN)))
    if lag_max <= lag_min + 1:
        return BPM_PRIOR
    lags = np.arange(lag_min, lag_max + 1)
    bpm = 60.0 * fps / lags
    prior = np.exp(-0.5 * (np.log2(bpm / BPM_PRIOR) / BPM_STD) ** 2)
    score = np.maximum(ac[lags], 0) * prior
    k = int(np.argmax(score))
    lag = float(lags[k])
    if 0 < k < len(lags) - 1:  # parabolic refinement of the peak lag
        a, b, c = ac[lags[k] - 1], ac[lags[k]], ac[lags[k] + 1]
        den = a - 2 * b + c
        if den < 0:
            lag += 0.5 * (a - c) / den
    return 60.0 * fps / lag


def track_beats(onset: np.ndarray, fps: float, bpm: float) -> np.ndarray:
    """Ellis (2007) dynamic-programming beat tracker; returns beat frame indices."""
    n = len(onset)
    sd = onset.std()
    if n == 0 or sd <= 0:
        return np.array([], int)
    period = 60.0 * fps / bpm
    g = np.arange(-int(period), int(period) + 1)
    local = np.convolve(onset / sd, np.exp(-0.5 * (g * 32.0 / period) ** 2), mode="same")
    window = np.arange(-int(round(2 * period)), -int(round(period / 2)) + 1)
    txwt = -TIGHTNESS * np.log(-window / period) ** 2
    cum = np.zeros(n)
    back = np.full(n, -1, int)
    first = True
    for i in range(n):
        z = i + window
        ok = z >= 0
        if not ok.any():
            cum[i] = local[i]
            continue
        cand = txwt[ok] + cum[z[ok]]
        j = int(np.argmax(cand))
        if first and local[i] < 0.01 * local.max():
            cum[i] = local[i]
            continue
        first = False
        if cand[j] <= 0:  # nothing worth following: a chain starts here
            cum[i] = local[i]
            continue
        cum[i] = local[i] + cand[j]
        back[i] = int(z[ok][j])
    # the last beat: the last local maximum of the cumulative score above half their median
    peaks = [i for i in range(1, n - 1) if cum[i] >= cum[i - 1] and cum[i] >= cum[i + 1]]
    if not peaks:
        return np.array([], int)
    med = float(np.median(cum[peaks]))
    tail = max(i for i in peaks if cum[i] >= 0.5 * med)
    beats = [tail]
    while back[beats[-1]] >= 0:
        beats.append(int(back[beats[-1]]))
    beats = np.array(beats[::-1], int)
    # trim weak beats at the edges (fade-in / fade-out, silence)
    strength = local[beats]
    thr = 0.5 * np.sqrt(np.mean(strength ** 2)) if len(strength) else 0
    keep = np.where(strength >= thr)[0]
    if len(keep):
        beats = beats[keep[0]:keep[-1] + 1]
    return beats


def _snap_peaks(onset: np.ndarray, bf: np.ndarray, period: float) -> np.ndarray:
    """Each tracked beat moves to the onset peak within +-12 % of a beat (the DP may lag where the music thins out),
    then to a sub-frame time by parabolic interpolation of that peak. Returns beat times in frames (float)."""
    if not len(bf):
        return bf.astype(float)
    r = max(1, int(round(0.12 * period)))
    med = float(np.median(onset[bf])) if len(bf) else 0.0
    out = []
    for b in bf:
        a, c = max(0, b - r), min(len(onset), b + r + 1)
        j = a + int(np.argmax(onset[a:c]))
        if onset[j] < 0.3 * med:
            j = int(b)
        off = 0.0
        if 0 < j < len(onset) - 1:
            l, m, n = onset[j - 1], onset[j], onset[j + 1]
            den = l - 2 * m + n
            if den < 0:
                off = float(np.clip(0.5 * (l - n) / den, -0.5, 0.5))
        out.append(j + off)
    return np.array(out)


def _refine(y: np.ndarray, times: np.ndarray) -> np.ndarray:
    """Move each beat to the steepest rise of a 5 ms log-energy envelope within +-REFINE_S (when there is a clear one)."""
    hop = int(SR * 0.005)
    m = len(y) // hop
    if m < 4 or not len(times):
        return times
    e = (y[: m * hop].astype(np.float64).reshape(m, hop) ** 2).mean(axis=1)
    le = 10 * np.log10(e + 1e-10)
    rise = np.maximum(0.0, np.diff(le, prepend=le[:1]))
    out = times.copy()
    w = int(REFINE_S / 0.005)
    floor = np.median(rise) + 3 * (np.median(np.abs(rise - np.median(rise))) + 1e-9)
    for k, t in enumerate(times):
        c = int(round(t / 0.005))
        a, b = max(0, c - w), min(m, c + w + 1)
        if b - a < 3:
            continue
        j = a + int(np.argmax(rise[a:b]))
        if rise[j] > max(floor, 6.0):  # a sharp attack (>= 6 dB in 5 ms) near the beat: that's where it lands
            out[k] = (j - 0.5) * 0.005  # the rise is between frame j-1 and j
    return np.maximum(out, 0.0)


def _near_max(env: np.ndarray, f: int, r: int = 2) -> float:
    a, b = max(0, f - r), min(len(env), f + r + 1)
    return float(env[a:b].max()) if b > a else 0.0


def downbeats(an: dict, beat_frames: np.ndarray) -> tuple[int, float]:
    """(phase, confidence): which beat of every METER starts a bar. Score = low-band (kick / bass) flux plus the
    harmonic change across the beat; confidence = best / second best phase score (1.0 = no preference)."""
    if len(beat_frames) < METER * 2:
        return 0, 1.0
    low = np.array([_near_max(an["low"], f) for f in beat_frames])
    ons = np.array([_near_max(an["onset"], f) for f in beat_frames])
    db = an["band_db"]
    change = np.zeros(len(beat_frames))
    for i in range(1, len(beat_frames) - 1):
        a = db[beat_frames[i - 1]:beat_frames[i]].mean(axis=0)
        b = db[beat_frames[i]:beat_frames[i + 1]].mean(axis=0)
        change[i] = float(np.abs(a - b).mean())

    def z(v):
        s = v.std()
        return (v - v.mean()) / s if s > 0 else v * 0
    score = z(low) + 0.5 * z(ons) + 0.5 * z(change)
    ph = np.array([score[k::METER].mean() for k in range(METER)])
    order = np.argsort(ph)[::-1]
    best, second = ph[order[0]], ph[order[1]]
    spread = float(ph.max() - ph.min()) or 1.0
    conf = 1.0 + max(0.0, float(best - second)) / spread
    return int(order[0]), round(conf, 2)


def _energy(an: dict, fps: float, duration: float) -> tuple[list[float], np.ndarray]:
    """Energy at ENERGY_HOP steps, 0..1 (0 = 30 dB under the loudest step, or silence)."""
    tdb = an["total_db"]
    step = max(1, int(round(ENERGY_HOP * fps)))
    vals = []
    for a in range(0, len(tdb), step):
        seg = 10 ** (tdb[a:a + step] / 10)
        vals.append(10 * np.log10(seg.mean() + 1e-10))
    v = np.array(vals) if vals else np.zeros(1)
    top = v.max()
    norm = np.clip((v - (top - 30.0)) / 30.0, 0, 1)
    return [round(float(x), 2) for x in norm], v


def sections(bars: list[float], duration: float, an: dict, fps: float) -> tuple[list[dict], list[float]]:
    """Per-bar energy (0..1) and the bars where the music clearly changes (energy step or a new sound)."""
    if len(bars) < 2:
        return [], []
    bar_len = float(np.median(np.diff(bars))) if len(bars) > 1 else duration
    edges = list(bars) + [min(duration, bars[-1] + bar_len)]  # the last bar is one bar long, not the tail of the file
    tdb, bdb = an["total_db"], an["band_db"]
    lv, prof = [], []
    for a, b in zip(edges, edges[1:]):
        fa, fb_ = int(a * fps), max(int(a * fps) + 1, int(b * fps))
        lv.append(10 * np.log10((10 ** (tdb[fa:fb_] / 10)).mean() + 1e-10))
        prof.append(bdb[fa:fb_].mean(axis=0))
    lv = np.array(lv)
    prof = np.array(prof)
    top = lv.max()
    bar_energy = [round(float(x), 2) for x in np.clip((lv - (top - 30.0)) / 30.0, 0, 1)]
    k = 2  # compare the 2 bars before a bar line with the 2 after
    out = []
    nov = np.zeros(len(lv))
    full = len(lv) - (1 if edges[-1] - edges[-2] < 0.75 * bar_len else 0)  # a last partial bar is not a section
    for i in range(k, full - 1):
        prev, nxt = slice(i - k, i), slice(i, min(full, i + k))
        d_db = float(lv[nxt].mean() - lv[prev].mean())
        d_tone = float(np.abs(prof[nxt].mean(axis=0) - prof[prev].mean(axis=0)).mean())
        nov[i] = abs(d_db) + 0.5 * d_tone
    if not nov.any():
        return [], bar_energy
    thr = max(3.0, float(nov[nov > 0].mean() + 1.0 * nov[nov > 0].std()))
    last = -MIN_SECTION_BARS
    for i in range(len(nov)):
        if nov[i] < thr or i - last < MIN_SECTION_BARS:
            continue
        if i + 1 < len(nov) and nov[i + 1] > nov[i]:
            continue
        d_db = float(lv[i:min(full, i + k)].mean() - lv[max(0, i - k):i].mean())
        kind = "up" if d_db >= 3 else "down" if d_db <= -3 else "change"
        out.append({"t": r3(bars[i]), "bar": i, "kind": kind, "delta_db": round(d_db, 1)})
        last = i
    return out, bar_energy


def hits(an: dict, fps: float, max_per_s: float = 2.0) -> list[float]:
    """The strongest onsets (accents): local maxima of the onset envelope well above its level, at most 2 per second."""
    o = an["onset"]
    if len(o) < 3 or o.max() <= 0:
        return []
    thr = o.mean() + 2.0 * o.std()
    r = max(1, int(0.1 * fps))
    cand = [i for i in range(1, len(o) - 1) if o[i] >= thr and o[i] == o[max(0, i - r):i + r + 1].max()]
    cand.sort(key=lambda i: -o[i])
    picked: list[int] = []
    gap = fps / max_per_s
    for i in cand:
        if all(abs(i - j) >= gap for j in picked):
            picked.append(i)
    return sorted(r3(i / fps) for i in picked)


def beat_map(y: np.ndarray) -> dict:
    """The full beat map of a mono signal at SR (times in the signal's own seconds)."""
    duration = len(y) / SR
    if duration < 1.0 or float(np.abs(y).max() if len(y) else 0) < 1e-4:
        return {"duration": r3(duration), "tempo": None, "beats": [], "downbeats": [], "bars": [], "bar_energy": [],
                "sections": [], "hits": [], "energy": {"hop": ENERGY_HOP, "values": []},
                "note": "too short or silent: no beats"}
    an = analyse(y)
    fps = an["fps"]
    bpm = estimate_tempo(an["onset"], fps)
    bf = track_beats(an["onset"], fps, bpm)
    bpos = _snap_peaks(an["onset"], bf, 60.0 * fps / bpm)
    if len(bpos) > 2:  # no beat on the silence or the release at either end
        st = np.array([_near_max(an["onset"], int(round(b)), 1) for b in bpos])
        good = np.where(st >= 0.25 * float(np.median(st)))[0]
        if len(good):
            bpos, bf = bpos[good[0]:good[-1] + 1], bf[good[0]:good[-1] + 1]
    times = _refine(y, bpos / fps)
    if len(times) >= 4:  # the tempo the tracked beats actually keep: a line through them (robust to per-beat jitter)
        ibi = np.diff(times)
        med = float(np.median(ibi))
        if np.all(np.abs(ibi - med) < 0.25 * med):  # one steady grid: fit it
            slope = float(np.polyfit(np.arange(len(times)), times, 1)[0])
            bpm = 60.0 / slope if slope > 0 else 60.0 / med
        else:  # tempo changes / dropped beats: the typical interval
            bpm = 60.0 / med
    phase, conf = downbeats(an, bf)
    beats_t = [r3(t) for t in times]
    downs = beats_t[phase::METER]
    secs, bar_energy = sections(downs, duration, an, fps)
    energy, _ = _energy(an, fps, duration)
    return {"duration": r3(duration), "tempo": round(float(bpm), 1), "beat_period": r3(60.0 / bpm), "meter": METER,
            "beats": beats_t, "downbeats": downs, "downbeat_phase": phase, "downbeat_confidence": conf,
            "first_beat": beats_t[0] if beats_t else None, "bar_energy": bar_energy, "sections": secs,
            "hits": hits(an, fps), "energy": {"hop": ENERGY_HOP, "values": energy}}


# ------------------------------------------------------------------ edit-time mapping
def edit_map(doc: dict, cut_audio: dict | None, duration: float) -> dict:
    """Beats, downbeats, sections and hits of a beats.json in edit time for a cut of `duration` seconds.

    "edit" maps 1:1. "music": edit t = music t - music_in, repeated every loop when the bed loops (cut_audio from
    cutmap.json `audio`). Anything else (a file, or a cut whose sound is not this music) gives empty lists."""
    t = doc.get("time")
    keys = ("beats", "downbeats", "hits")
    if t == "edit":
        shift, span, loops = 0.0, None, 1
    elif t == "music" and cut_audio and cut_audio.get("mode") == "music" and \
            cut_audio.get("src") == (doc.get("source") or {}).get("id"):
        shift = float(cut_audio.get("in") or 0.0)
        span = float(cut_audio.get("loop_len") or 0.0) or None
        loops = int(np.ceil(duration / span)) if span else 1
    else:
        return {k: [] for k in keys} | {"sections": [], "mapped": False}
    out: dict = {"mapped": True}

    half = 0.5 / FPS  # a beat detected a hair before the music's `in` point is the cut's first beat

    def place(ts):
        res = []
        for k in range(loops):
            for x in ts:
                e = x - shift + (k * span if span else 0.0)
                if span and not (-half <= x - shift < span - half):
                    continue
                if -half <= e <= duration + half:
                    res.append(r3(min(duration, max(0.0, e))))
        return sorted(set(res))
    for k in keys:
        out[k] = place(doc.get(k) or [])
    secs = []
    for s in doc.get("sections") or []:
        for e in place([s["t"]]):
            secs.append({**s, "t": e})
    out["sections"] = secs
    return out


# ------------------------------------------------------------------ command
def _cut_sound(pr) -> np.ndarray:
    """The cut's own sound (the bed `veos voice` builds) at SR, for a reel with no music."""
    from .novoice import build_bed
    cm = read_json(pr.work / "cutmap.json")
    x, _ = build_bed(pr, cm)
    from scipy.signal import resample_poly
    return resample_poly(x.astype(np.float64), SR, 48000).astype(np.float32)


def main(args, project) -> dict:
    from .audio import decode_mono
    pr = need_project(project)
    src_doc: dict
    if args.file:
        f = Path(args.file).expanduser()
        if not f.exists():
            raise VeosError("INPUT_MISSING", f"not found: {args.file}", "Check the --file path.")
        y = decode_mono(f, SR)
        src_doc, time = {"file": f.resolve().as_posix()}, "file"
    else:
        sp = pr.work / "sources.json"
        if not sp.exists():
            raise VeosError("NO_SOURCES", "work/sources.json not found", "Run `veos ingest` first.")
        sources = read_json(sp).get("sources") or []
        pick = [s for s in sources if s["id"] == args.src] if args.src else [s for s in sources if s.get("kind") == "music"]
        if args.src and not pick:
            raise VeosError("NO_SUCH_ID", f"no source with id {args.src}", "See work/sources.json for the ids.")
        if pick:
            s = pick[0]
            wav = pr.work / "audio" / f"{s['id']}.wav"
            f = wav if wav.exists() else pr.abs(s["path"])
            y = decode_mono(f, SR)
            src_doc, time = {"id": s["id"], "file": s["path"]}, "music"
        elif (pr.work / "cutmap.json").exists():
            y = _cut_sound(pr)
            src_doc, time = {"id": None, "file": "the cut's own sound"}, "edit"
        else:
            raise VeosError("NO_MUSIC", "no music track in this project and no cut yet",
                            "Give the music with `veos project init ... --no-voice --music <file>` (then ingest), "
                            "pass --file <audio>, or cut first to map the clips' own sound.")
    doc = {"version": 1, "time": time, "source": src_doc, **beat_map(y)}
    out = pr.abs(args.out)
    write_json(out, doc)
    res = {"file": pr.rel(out), "time": time, "tempo": doc.get("tempo"), "beats": len(doc["beats"]),
           "bars": len(doc["downbeats"]), "downbeat_confidence": doc.get("downbeat_confidence"),
           "sections": [[s["t"], s["kind"]] for s in doc["sections"]], "first_beat": doc.get("first_beat"),
           "duration": doc["duration"]}
    if doc.get("note"):
        res["warnings"] = [doc["note"]]
    if doc.get("downbeat_confidence") is not None and doc["downbeat_confidence"] < 1.15 and doc["beats"]:
        res.setdefault("warnings", []).append("the bar starts are a guess (no clear accent on beat 1)")
    return res
