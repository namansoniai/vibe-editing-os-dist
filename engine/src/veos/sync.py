"""`veos sync`: line up several clips, camera angles and mic tracks of one recording session by their audio.

Model (SPEC section 7): every synced source X maps its own time onto **session time** with
    t_session = offset + t_X * (1 + drift)          (drift = drift_ppm * 1e-6; the inverse is used to fetch frames)
Session time 0 is the earliest start of any synced source. Different start times, different lengths, different
frame rates and resolutions are all fine: sync uses the sound only, frames are fetched by time.

Method (robust to gain, mic colour and room differences):
  1. coarse: cross-correlate band-wise spectral-flux onset envelopes (100 Hz) over every possible lag -> offset to
     ~10 ms + a peak z-score and a peak ratio (the best peak against the best peak more than 1 s away);
  2. fine + drift: GCC-PHAT on 12 s windows spread over the overlap (8 kHz, +-0.6 s around the coarse lag, parabolic
     sub-sample peak), then a deterministic RANSAC line fit (inliers within 4 ms) -> offset, drift (ppm), residual;
  3. confidence 0..1 from the coarse peak and the share of agreeing windows. A source whose sync is not reliable is a
     hard failure (SYNC_UNRELIABLE) unless the creator gives its offset (`--offset ID=SECONDS`).

Session master: with 2+ synced sources `veos sync` also writes source `MIX` (kind "session"): work/audio/MIX.wav on the
session timeline (a gain-sharing automix of the mic tracks, or the best camera audio when there are no mics) plus a
small work/src/MIX.mp4 proxy of the main camera, so `transcribe --id MIX`, the rough cut, `cut` and `voice` work on the
whole session unchanged. `veos shots render` maps MIX time to each camera through the sync blocks.
"""
from __future__ import annotations

import math
import time
import wave
from pathlib import Path

import numpy as np

from .core import FPS, VeosError, need_project, r3, read_json, run, tools, write_json

SR = 8000                 # analysis rate for sync
HOP = 0.01                # envelope hop (s)
BANDS = ((100, 300), (300, 800), (800, 2000), (2000, 3800))
WIN_S = 12.0              # fine window length
SEARCH_S = 0.6            # fine search +- around the coarse/predicted lag
INLIER_S = 0.004          # RANSAC inlier band
MIN_Z = 8.0               # coarse peak z-score needed when fine windows can't decide
MIN_RATIO = 1.25
MIX_SR = 48000
MIX_ID = "MIX"
EXCLUDE_KINDS = {"broll", "screen-recording", "session"}
PROXY_W = 540


def add_args(p, cmd):
    p.add_argument("--ids", help="comma list of source ids to sync (default: every camera/mic source with audio)")
    p.add_argument("--ref", help="reference source id (default: the longest video source with audio)")
    p.add_argument("--mics", help="comma list of ids that are per-person mic tracks (default: audio-only sources)")
    p.add_argument("--offset", action="append", default=[], metavar="ID=SECONDS",
                   help="manual offset of a source against the reference (its t=0 lands at SECONDS of the reference)")
    p.add_argument("--no-mix", action="store_true", help="do not write the MIX session master")
    p.add_argument("--min-confidence", type=float, default=0.5, help="below this a source fails (default 0.5)")


# ======================================================================= signal helpers (pure, tested)
def _sos_bandpass(lo: float, hi: float, sr: int):
    from scipy.signal import butter
    return butter(4, [lo / (sr / 2), min(hi / (sr / 2), 0.99)], btype="band", output="sos")


def onset_envelope(x: np.ndarray, sr: int = SR, hop: float = HOP) -> np.ndarray:
    """Band-wise log-energy spectral flux at `hop` (s), summed over bands, then high-passed and unit-normalised.

    Insensitive to gain and to moderate EQ differences between mics: only *changes* in each band's log energy count.
    """
    from scipy.signal import sosfilt
    h = int(round(hop * sr))
    n = len(x) // h
    if n < 4:
        return np.zeros(max(n, 1), np.float32)
    out = np.zeros(n, np.float64)
    for lo, hi in BANDS:
        y = sosfilt(_sos_bandpass(lo, hi, sr), x.astype(np.float64))
        e = np.sqrt((y[: n * h].reshape(n, h) ** 2).mean(1) + 1e-12)
        le = np.log(e + 1e-4 * (np.median(e) + 1e-9))
        out += np.maximum(0.0, np.diff(le, prepend=le[0]))
    # remove slow trends (1 s moving average) and normalise
    k = max(1, int(round(1.0 / hop)))
    ma = np.convolve(out, np.ones(k) / k, mode="same")
    env = out - ma
    sd = env.std()
    return (env / sd if sd > 1e-12 else env).astype(np.float32)


def _next_pow2(n: int) -> int:
    return 1 << max(1, int(math.ceil(math.log2(max(n, 2)))))


def xcorr_full(ref: np.ndarray, x: np.ndarray) -> tuple[np.ndarray, int]:
    """Linear cross-correlation c[k] = sum_n ref[n + k] * x[n] for k in [-(len(x)-1), len(ref)-1].
    Returns (c, k0) where c[i] is lag k = i + k0."""
    n = len(ref) + len(x) - 1
    N = _next_pow2(n)
    R = np.fft.rfft(ref.astype(np.float64), N)
    X = np.fft.rfft(x.astype(np.float64), N)
    c = np.fft.irfft(R * np.conj(X), N)
    # lags >= 0 at c[0:len(ref)], negative lags wrap to the end
    pos = c[: len(ref)]
    neg = c[N - (len(x) - 1):] if len(x) > 1 else np.zeros(0)
    return np.concatenate([neg, pos]), -(len(x) - 1)


def coarse_offset(env_ref: np.ndarray, env_x: np.ndarray, hop: float = HOP, min_overlap_s: float = 3.0) -> dict:
    """Best lag (s) so that env_ref[t + lag] ~ env_x[t]; z = (peak - median) / robust sigma; ratio = peak / best other peak
    more than 1 s away. Lags with less than `min_overlap_s` of overlap are ignored."""
    c, k0 = xcorr_full(env_ref, env_x)
    lags = np.arange(len(c)) + k0
    ov = np.minimum(len(env_ref), lags + len(env_x)) - np.maximum(0, lags)
    valid = ov >= max(2, int(min_overlap_s / hop))
    if not valid.any():
        return {"lag": 0.0, "z": 0.0, "ratio": 1.0, "overlap_s": 0.0}
    cv = np.where(valid, c, -np.inf)
    i = int(np.argmax(cv))
    peak = float(c[i])
    vals = c[valid]
    med = float(np.median(vals))
    mad = float(np.median(np.abs(vals - med))) * 1.4826 + 1e-12
    excl = int(round(1.0 / hop))
    other = cv.copy()
    other[max(0, i - excl): i + excl + 1] = -np.inf
    p2 = float(np.max(other)) if np.isfinite(np.max(other)) else med
    ratio = (peak - med) / max(p2 - med, 1e-9)
    # parabolic refinement
    frac = 0.0
    if 0 < i < len(c) - 1 and np.isfinite(cv[i - 1]) and np.isfinite(cv[i + 1]):
        a, b, d = c[i - 1], c[i], c[i + 1]
        den = a - 2 * b + d
        frac = 0.5 * (a - d) / den if abs(den) > 1e-12 else 0.0
    return {"lag": float((lags[i] + frac) * hop), "z": (peak - med) / mad, "ratio": float(ratio),
            "overlap_s": float(ov[i] * hop)}


def gcc_phat_lag(ref_seg: np.ndarray, x_seg: np.ndarray, max_k: int, beta: float = 0.8) -> tuple[float, float]:
    """Lag k in [0, max_k] (samples, sub-sample) maximising sum ref_seg[n + k] x_seg[n] with PHAT-beta weighting.
    Returns (k, quality) where quality = (peak - mean) / std of the searched correlation."""
    N = _next_pow2(len(ref_seg) + len(x_seg))
    R = np.fft.rfft(ref_seg.astype(np.float64), N)
    X = np.fft.rfft(x_seg.astype(np.float64), N)
    G = R * np.conj(X)
    G /= np.abs(G) ** beta + 1e-12
    c = np.fft.irfft(G, N)[: max_k + 1]
    i = int(np.argmax(c))
    frac = 0.0
    if 0 < i < len(c) - 1:
        a, b, d = c[i - 1], c[i], c[i + 1]
        den = a - 2 * b + d
        frac = 0.5 * (a - d) / den if abs(den) > 1e-12 else 0.0
    sd = float(c.std()) + 1e-12
    return i + float(np.clip(frac, -0.5, 0.5)), float((c[i] - c.mean()) / sd)


def _active(x: np.ndarray) -> bool:
    return float(np.sqrt(np.mean(x.astype(np.float64) ** 2))) > 1e-4


def fine_fit(ref: np.ndarray, x: np.ndarray, sr: int, coarse_lag: float, win_s: float = WIN_S,
             search_s: float = SEARCH_S, max_windows: int = 24) -> dict:
    """Windows over the overlap -> local lags -> RANSAC line lag(t) = a + b*t (t = source time at window centre)."""
    L, M = int(win_s * sr), int(search_s * sr)
    t_lo = max(0.0, -coarse_lag) + search_s
    t_hi = min(len(x) / sr, (len(ref) / sr) - coarse_lag) - win_s - search_s
    pts = []
    if t_hi > t_lo:
        n = int(np.clip((t_hi - t_lo) / 20.0, 1, max_windows))
        starts = np.linspace(t_lo, t_hi, n) if n > 1 else np.array([t_lo])
        for s in starts:
            i0 = int(round(s * sr))
            xs = x[i0: i0 + L]
            r0 = int(round((s + coarse_lag) * sr)) - M
            if r0 < 0 or r0 + L + 2 * M > len(ref) or len(xs) < L or not _active(xs):
                continue
            rs = ref[r0: r0 + L + 2 * M]
            if not _active(rs):
                continue
            k, q = gcc_phat_lag(rs, xs, 2 * M)
            lag = (r0 + k) / sr - s
            pts.append((s + win_s / 2, lag, q))
    if len(pts) < 2:
        return {"n": len(pts), "inliers": len(pts), "a": coarse_lag if not pts else pts[0][1], "b": 0.0,
                "residual_ms": None, "points": pts}
    P = np.array(pts)
    good = P[:, 2] >= 6.0     # PHAT peaks below this are noise
    Q = P[good] if good.sum() >= 2 else P
    best = None
    for i in range(len(Q)):
        for j in range(i, len(Q)):
            if i == j:
                a, b = Q[i, 1], 0.0
            else:
                dt = Q[j, 0] - Q[i, 0]
                if abs(dt) < 1e-6:
                    continue
                b = (Q[j, 1] - Q[i, 1]) / dt
                if abs(b) > 500e-6:   # > 500 ppm is not a clock drift
                    continue
                a = Q[i, 1] - b * Q[i, 0]
            inl = np.abs(Q[:, 1] - (a + b * Q[:, 0])) <= INLIER_S
            score = (int(inl.sum()), -float(np.abs(Q[inl, 1] - (a + b * Q[inl, 0])).sum()))
            if best is None or score > best[0]:
                best = (score, inl)
    inl = best[1]
    T, Y = Q[inl, 0], Q[inl, 1]
    if len(T) >= 2 and np.ptp(T) > 1.0:
        b, a = np.polyfit(T, Y, 1)
    else:
        a, b = float(Y.mean()), 0.0
    res = Y - (a + b * T)
    return {"n": int(len(P)), "valid": int(len(Q)), "inliers": int(inl.sum()), "a": float(a), "b": float(b),
            "residual_ms": float(np.sqrt(np.mean(res ** 2)) * 1000) if len(res) else None, "points": pts}


def align(ref: np.ndarray, x: np.ndarray, sr: int = SR) -> dict:
    """Align source audio `x` to reference audio `ref` (same rate). Result: t_ref = offset + t_x * (1 + drift)."""
    er, ex = onset_envelope(ref, sr), onset_envelope(x, sr)
    co = coarse_offset(er, ex)
    ff = fine_fit(ref, x, sr, co["lag"])
    valid = ff.get("valid", ff["n"])
    fine_q = ff["inliers"] / valid if valid else 0.0
    coarse_q = float(np.clip((co["z"] - 6.0) / 10.0, 0, 1)) * float(np.clip((co["ratio"] - 1.0) / 0.5, 0, 1))
    if valid >= 3:
        conf = 0.35 * coarse_q + 0.65 * fine_q
        offset, drift = ff["a"], ff["b"]
        if ff["inliers"] < 2:
            offset, drift = co["lag"], 0.0
    elif valid >= 1:
        conf = 0.6 * coarse_q + 0.4 * fine_q
        offset, drift = (ff["a"] if ff["inliers"] else co["lag"]), 0.0
    else:
        conf = coarse_q * 0.8
        offset, drift = co["lag"], 0.0
    # a fine estimate far from the coarse one means the windows locked onto something else
    if abs(offset - co["lag"]) > 0.05 and valid < 3:
        offset, conf = co["lag"], conf * 0.7
    return {"offset": float(offset), "drift": float(drift), "confidence": round(float(conf), 3),
            "coarse": {"lag": r3(co["lag"]), "z": round(co["z"], 1), "ratio": round(co["ratio"], 2),
                       "overlap_s": round(co["overlap_s"], 1)},
            "fine": {"windows": ff["n"], "valid": valid, "inliers": ff["inliers"],
                     "residual_ms": None if ff["residual_ms"] is None else round(ff["residual_ms"], 2)}}


def reliable(res: dict, min_conf: float) -> bool:
    c, f = res["coarse"], res["fine"]
    if res["confidence"] < min_conf:
        return False
    if f["valid"] >= 3:
        return f["inliers"] >= max(2, math.ceil(0.5 * f["valid"]))
    return c["z"] >= MIN_Z and c["ratio"] >= MIN_RATIO


# ======================================================================= automix (Dugan gain sharing)
def automix(tracks: list[np.ndarray], sr: int, hop: float = 0.01, attack: float = 0.01, release: float = 0.25) -> np.ndarray:
    """Gain-sharing automix of time-aligned mic tracks: each mic's gain = its share of the total (smoothed) energy, so
    the open mic is the one with the talker and bleed/comb filtering from the others is suppressed. Tracks are first
    matched to the same speech level (95th percentile of their 10 ms RMS)."""
    n = max(len(t) for t in tracks)
    h = int(round(hop * sr))
    nf = (n + h - 1) // h
    lv = []
    norm = []
    for t in tracks:
        t = np.pad(t.astype(np.float32), (0, n - len(t)))
        e = np.sqrt((np.pad(t, (0, nf * h - n)).reshape(nf, h).astype(np.float64) ** 2).mean(1) + 1e-12)
        ref = np.percentile(e, 95) + 1e-9
        g = 0.1 / ref                                   # bring every mic's loud speech to ~-20 dBFS RMS
        norm.append(t * np.float32(g))
        lv.append(e * g)
    E = np.array(lv) ** 2
    sm = np.zeros_like(E)
    aa, ar = math.exp(-hop / attack), math.exp(-hop / release)
    cur = E[:, 0].copy()
    for k in range(nf):
        up = E[:, k] > cur
        cur = np.where(up, aa * cur + (1 - aa) * E[:, k], ar * cur + (1 - ar) * E[:, k])
        sm[:, k] = cur
    G = sm / (sm.sum(0, keepdims=True) + 1e-12)
    out = np.zeros(n, np.float32)
    xs = (np.arange(nf) + 0.5) * h
    idx = np.arange(n)
    for t, g in zip(norm, G):
        out += t * np.interp(idx, xs, g).astype(np.float32)
    pk = float(np.max(np.abs(out))) if len(out) else 0.0
    return out * np.float32(0.89 / pk) if pk > 0.89 else out


def warp_to_session(x: np.ndarray, sr: int, offset: float, drift: float, n_out: int) -> np.ndarray:
    """Resample source audio onto session time: out[i] = x((i/sr - offset) / (1 + drift)); zeros outside."""
    out = np.zeros(n_out, np.float32)
    CH = sr * 60
    for a in range(0, n_out, CH):
        b = min(n_out, a + CH)
        ts = (np.arange(a, b) / sr - offset) / (1.0 + drift)
        pos = ts * sr
        ok = (pos >= 0) & (pos <= len(x) - 1)
        if ok.any():
            out[a:b][ok] = np.interp(pos[ok], np.arange(len(x)), x).astype(np.float32)
    return out


# ======================================================================= project helpers
def _decode(path: Path, sr: int) -> np.ndarray:
    r = run([tools().ffmpeg, "-v", "error", "-i", str(path), "-vn", "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
            check=False)
    if r.returncode != 0 or not r.stdout:
        raise VeosError("AUDIO_DECODE_FAILED", f"could not decode the audio of {path.name}",
                        "Check the file has a sound track.")
    return np.frombuffer(r.stdout, np.float32).copy()


def source_audio(proj, s: dict, sr: int) -> np.ndarray:
    wav = proj.work / "audio" / f"{s['id']}.wav"
    return _decode(wav if wav.exists() else proj.abs(s["path"]), sr)


def write_wav(path: Path, x: np.ndarray, sr: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp.wav")
    pcm = (np.clip(x, -1.0, 1.0) * 32767.0).round().astype("<i2")
    with wave.open(str(tmp), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(pcm.tobytes())
    tmp.replace(path)


def to_session(sync: dict, t_src: float) -> float:
    return sync["offset"] + t_src * (1.0 + sync.get("drift_ppm", 0.0) * 1e-6)


def from_session(sync: dict, t_session: float) -> float:
    return (t_session - sync["offset"]) / (1.0 + sync.get("drift_ppm", 0.0) * 1e-6)


def session_map(sources: list[dict]) -> dict:
    """{id: sync block} for every source with a sync block; a source without one maps identically (single camera)."""
    return {s["id"]: (s.get("sync") or {"offset": 0.0, "drift_ppm": 0.0}) for s in sources}


def _parse_offsets(items: list[str]) -> dict:
    out = {}
    for it in items:
        if "=" not in it:
            raise VeosError("BAD_ARG", f"--offset {it}: use ID=SECONDS", "Example: --offset B=-3.25")
        k, v = it.split("=", 1)
        try:
            out[k.strip()] = float(v)
        except ValueError as e:
            raise VeosError("BAD_ARG", f"--offset {it}: {v} is not a number", "Example: --offset B=-3.25") from e
    return out


def _session_proxy(proj, ref: dict, sync: dict, dur: float, wav: Path, out: Path) -> None:
    """A small CFR proxy of the main camera on the session timeline, with the session audio (rough-cut review)."""
    vid = proj.work / "src" / f"{ref['id']}.mp4"
    src = vid if vid.exists() else proj.abs(ref["path"])
    off = sync["offset"]
    w = PROXY_W if (ref.get("width") or 1080) <= (ref.get("height") or 1920) else 960
    vf = [f"fps={FPS}", f"scale={w}:-2"]
    pre = []
    if off > 0:
        vf.append(f"tpad=start_duration={off:.4f}:start_mode=add:color=black")
    elif off < 0:
        pre = ["-ss", f"{-off:.4f}"]
    vf.append(f"tpad=stop_duration={dur + 1:.3f}:stop_mode=add:color=black")
    tmp = out.with_suffix(".tmp.mp4")
    run([tools().ffmpeg, "-v", "error", "-y", *pre, "-i", str(src), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0",
         "-vf", ",".join(vf), "-t", f"{dur:.4f}", "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "26",
         "-pix_fmt", "yuv420p", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
         "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(tmp)], proj, "sync")
    tmp.replace(out)


# ======================================================================= command
def main(args, project) -> dict:
    proj = need_project(project)
    sp = proj.work / "sources.json"
    if not sp.exists():
        raise VeosError("NO_SOURCES", "work/sources.json not found", "Run `veos ingest <files>` first.")
    data = read_json(sp)
    srcs = [s for s in data["sources"] if s["id"] != MIX_ID]
    want = [x.strip() for x in args.ids.split(",")] if args.ids else None
    group = [s for s in srcs if (want is None and s.get("audio") and s.get("kind") not in EXCLUDE_KINDS)
             or (want is not None and s["id"] in want)]
    if want:
        missing = sorted(set(want) - {s["id"] for s in group})
        if missing:
            raise VeosError("NO_SUCH_ID", f"unknown source id(s): {', '.join(missing)}", "See work/sources.json for ids.")
    no_audio = [s["id"] for s in group if not s.get("audio")]
    if no_audio:
        raise VeosError("NO_AUDIO", f"{', '.join(no_audio)} ha{'s' if len(no_audio) == 1 else 've'} no sound to sync by",
                        "Every camera needs at least scratch audio, or give its offset with --offset ID=SECONDS.")
    if not group:
        raise VeosError("NOTHING_TO_SYNC", "no camera or mic source with audio", "Ingest the session's clips first.")
    videos = [s for s in group if s.get("width")]
    if args.ref:
        ref = next((s for s in group if s["id"] == args.ref), None)
        if ref is None:
            raise VeosError("NO_SUCH_ID", f"--ref {args.ref} is not in the sync group", "Pick one of the synced ids.")
    else:
        ref = max(videos or group, key=lambda s: s.get("duration") or 0)
    manual = _parse_offsets(args.offset)
    mic_ids = ([x.strip() for x in args.mics.split(",")] if args.mics
               else [s["id"] for s in group if s.get("kind") == "audio-only"])
    t0 = time.time()
    audio = {s["id"]: source_audio(proj, s, SR) for s in group}
    results, failures, warnings = {}, [], []
    for s in group:
        sid = s["id"]
        if sid == ref["id"]:
            results[sid] = {"offset": 0.0, "drift": 0.0, "confidence": 1.0, "reference": True}
            continue
        if sid in manual:
            results[sid] = {"offset": manual[sid], "drift": 0.0, "confidence": 1.0, "manual": True}
            continue
        res = align(audio[ref["id"]], audio[sid], SR)
        res["reliable"] = reliable(res, args.min_confidence)
        results[sid] = res
        if not res["reliable"]:
            failures.append(sid)
        elif abs(res["drift"]) * 1e6 > 200:
            warnings.append(f"{sid}: clock drift {res['drift'] * 1e6:.0f} ppm is unusually large; check the sync")
    # session time: shift so the earliest source starts at 0
    spans = {}
    for s in group:
        r = results[s["id"]]
        dur = len(audio[s["id"]]) / SR
        spans[s["id"]] = (r["offset"], r["offset"] + dur * (1 + r["drift"]))
    t_start = min(a for a, _ in spans.values())
    session_dur = max(b for _, b in spans.values()) - t_start
    summary = []
    for s in group:
        r = results[s["id"]]
        blk = {"group": "G1", "ref": ref["id"], "offset": round(r["offset"] - t_start, 4),
               "drift_ppm": round(r["drift"] * 1e6, 2), "confidence": r["confidence"],
               "method": "reference" if r.get("reference") else ("manual" if r.get("manual") else "audio-xcorr"),
               "role": "mic" if s["id"] in mic_ids else ("camera" if s.get("width") else "audio"),
               "span": [round(spans[s["id"]][0] - t_start, 3), round(spans[s["id"]][1] - t_start, 3)]}
        if "coarse" in r:
            blk["coarse"], blk["fine"] = r["coarse"], r["fine"]
        s["sync"] = blk
        summary.append({"id": s["id"], "role": blk["role"], "offset": blk["offset"], "drift_ppm": blk["drift_ppm"],
                        "confidence": blk["confidence"], **({"fine": f"{r['fine']['inliers']}/{r['fine']['valid']} windows agree",
                                                             "residual_ms": r["fine"]["residual_ms"]} if "fine" in r else {}),
                        "fps_in": s.get("fps_in"), "size": [s.get("width"), s.get("height")] if s.get("width") else None})
    if failures:
        detail = "; ".join(f"{sid} (confidence {results[sid]['confidence']:.2f}, coarse z {results[sid]['coarse']['z']}, "
                           f"{results[sid]['fine']['inliers']}/{results[sid]['fine']['valid']} windows agree)" for sid in failures)
        proj.log("sync", "UNRELIABLE: " + detail)
        raise VeosError("SYNC_UNRELIABLE", f"could not line up {', '.join(failures)} with {ref['id']} by sound: {detail}",
                        "Make sure these clips are from the same conversation and recorded sound (a clap on camera at "
                        "the start helps), or give the offset with --offset ID=SECONDS (where that clip's start lands "
                        f"on {ref['id']}'s timeline).")
    data["session"] = {"version": 1, "group": "G1", "ref": ref["id"], "duration": round(session_dur, 3),
                       "members": [s["id"] for s in group], "mics": [m for m in mic_ids if m in {s["id"] for s in group}],
                       "cameras": [s["id"] for s in group if s.get("width")], "master": None}
    data["sources"] = [s for s in data["sources"] if s["id"] != MIX_ID]
    mix_info = None
    if len(group) >= 2 and not args.no_mix:
        n_out = int(round(session_dur * MIX_SR))
        mics = [s for s in group if s["id"] in mic_ids]
        if len(mics) >= 2 or (len(mics) == 1 and not videos):
            tracks = [warp_to_session(source_audio(proj, s, MIX_SR), MIX_SR, s["sync"]["offset"],
                                      s["sync"]["drift_ppm"] * 1e-6, n_out) for s in mics]
            mix = automix(tracks, MIX_SR) if len(tracks) > 1 else tracks[0]
            how = f"automix of mics {', '.join(s['id'] for s in mics)}"
        else:
            best = max(group, key=lambda s: ((s.get("audio") or {}).get("lufs") or -99))
            mix = warp_to_session(source_audio(proj, best, MIX_SR), MIX_SR, best["sync"]["offset"],
                                  best["sync"]["drift_ppm"] * 1e-6, n_out)
            how = f"audio of {best['id']} (no mic tracks)"
        wav = proj.path("work", "audio", f"{MIX_ID}.wav")
        write_wav(wav, mix, MIX_SR)
        frames = int(round(session_dur * FPS))
        entry = {"id": MIX_ID, "path": proj.rel(wav), "kind": "session", "duration": r3(frames / FPS), "frames": frames,
                 "audio": {"stream": 0, "channels": 1, "lufs": None, "tp": None},
                 "sync": {"group": "G1", "ref": ref["id"], "offset": 0.0, "drift_ppm": 0.0, "confidence": 1.0,
                          "method": "session", "role": "session", "span": [0.0, round(session_dur, 3)]},
                 "segments": [], "face_ratio": 0.0, "notes": [f"session master: {how}"],
                 "conformed": {"fps": FPS, "audio": proj.rel(wav), "frames": frames}}
        if videos:
            pv = proj.path("work", "src", f"{MIX_ID}.mp4")
            _session_proxy(proj, ref, ref["sync"], session_dur, wav, pv)
            entry["conformed"]["video"] = proj.rel(pv)
            entry.update(width=PROXY_W if (ref.get("width") or 1080) <= (ref.get("height") or 1920) else 960)
        data["sources"].append(entry)
        data["session"]["master"] = MIX_ID
        mix_info = {"id": MIX_ID, "audio": proj.rel(wav), "how": how, "duration": r3(session_dur)}
    elif len(group) == 1:
        data["session"]["master"] = group[0]["id"]
    else:
        data["session"]["master"] = ref["id"]
    write_json(sp, data)
    write_json(proj.path("work", "sync.json"), {"version": 1, "ref": ref["id"], "session": data["session"],
                                                "sources": {s["id"]: s["sync"] for s in group}})
    proj.log("sync", f"synced {len(group)} sources in {time.time() - t0:.1f}s: {summary}")
    return {"ref": ref["id"], "session_s": r3(session_dur), "master": data["session"]["master"], "sources": summary,
            "mix": mix_info, "warnings": warnings}
