"""`veos sfx` (place library sound effects on a timeline) and `veos mix` (voice chain + beds + -14 LUFS stereo master).

Also exposes helpers used by other modules: decode_mono, loudness, measure, balance.
"""
from __future__ import annotations

import hashlib
import json
import re
import tempfile
from pathlib import Path

import numpy as np

from .core import VeosError, r3, read_json, run, tools

SR = 48000
CHAIN = "highpass=f=80,deesser=i=0.35,acompressor=threshold=-21dB:ratio=2.5:attack=8:release=120:makeup=2"
TARGET_I, TARGET_TP, TARGET_LRA = -14.0, -1.5, 11


# --------------------------------------------------------------------------- helpers
def _cache_dir() -> Path:
    d = tools().scratch / "sfxcache"
    d.mkdir(parents=True, exist_ok=True)
    return d


def decode_mono(path: str | Path, sr: int = SR) -> np.ndarray:
    """Decode any audio/video file to float32 mono at `sr` through ffmpeg."""
    r = run([tools().ffmpeg, "-v", "error", "-i", str(path), "-vn", "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
            check=False)
    if r.returncode != 0:
        raise VeosError("AUDIO_DECODE_FAILED", f"could not decode {Path(path).name}",
                        "Check the file exists and is a valid audio/video file.")
    return np.frombuffer(r.stdout, np.float32).copy()


def _decode_cached(path: Path) -> np.ndarray:
    st = path.stat()
    key = hashlib.sha1(f"{path.resolve()}|{st.st_size}|{st.st_mtime_ns}".encode("utf-8")).hexdigest()[:20]
    f = _cache_dir() / f"{key}.npy"
    if f.exists():
        try:
            return np.load(f)
        except Exception:  # noqa: BLE001 - corrupt cache entry, re-decode
            pass
    a = decode_mono(path)
    np.save(f, a)
    return a


def loudness(path: str | Path, extra_af: str = "") -> dict:
    """Integrated loudness (LUFS) and true peak (dBTP) of the file as stereo/as-is, via ebur128."""
    af = (extra_af + "," if extra_af else "") + "ebur128=peak=true"
    r = run([tools().ffmpeg, "-nostats", "-hide_banner", "-i", str(path), "-vn", "-af", af, "-f", "null", "-"], check=False)
    err = (r.stderr or b"").decode("utf-8", "replace")
    k = err.rfind("Summary")
    if k < 0:
        raise VeosError("LOUDNESS_FAILED", f"could not measure loudness of {Path(path).name}", "Does the file have an audio stream?")
    s = err[k:]
    i = re.search(r"I:\s+(-?[\d.]+|-inf)\s+LUFS", s)
    p = re.search(r"Peak:\s+(-?[\d.]+|-inf)\s+dBFS", s)
    f = lambda m: float(m.group(1)) if m and m.group(1) != "-inf" else -120.0  # noqa: E731
    return {"lufs": r3(f(i)), "tp": r3(f(p))}


def _env_db(a: np.ndarray, hop: int) -> np.ndarray:
    n = len(a) // hop
    if n == 0:
        return np.full(1, -180.0)
    x = a[: n * hop].reshape(n, hop).astype(np.float64)
    return 20 * np.log10(np.sqrt((x ** 2).mean(1)) + 1e-9)


def measure(path: str | Path, sr: int = SR) -> dict:
    """Appendix J step 2: peak time, onset and end (s) of a sound file on a 10 ms RMS envelope (30 dB window)."""
    a = decode_mono(path, sr)
    env = _env_db(a, sr // 100)
    act = np.where(env > env.max() - 30)[0]
    return {"dur": r3(len(a) / sr), "peak_t": r3(int(np.argmax(env)) / 100), "onset": r3(act[0] / 100), "end": r3(act[-1] / 100)}


def balance(voice: str | Path, sfx: str | Path) -> dict:
    """Appendix J step 5: SFX level relative to the voice over 400 ms windows (only where the voice is above -40 dB)."""
    v, x = decode_mono(voice), decode_mono(sfx)
    n, win = min(len(v), len(x)), int(0.4 * SR)
    db = lambda s: 20 * np.log10(np.sqrt((s.astype(np.float64) ** 2).mean()) + 1e-9)  # noqa: E731
    d = [db(x[i:i + win]) - db(v[i:i + win]) for i in range(0, n - win, win // 2) if db(v[i:i + win]) > -40]
    if not d:
        return {"median_db": None, "p90_db": None, "max_db": None}
    d = np.array(d)
    return {"median_db": r3(np.median(d)), "p90_db": r3(np.percentile(d, 90)), "max_db": r3(d.max())}


def _write_wav(path: Path, x: np.ndarray) -> None:
    from scipy.io import wavfile
    path.parent.mkdir(parents=True, exist_ok=True)
    wavfile.write(str(path), SR, (np.clip(x, -1, 1) * 32767).round().astype("<i2"))


# --------------------------------------------------------------------------- sfx
def _sfx(args, project) -> dict:
    cues_path = Path(args.cues)
    if not cues_path.exists():
        raise VeosError("CUES_MISSING", f"cue file not found: {cues_path}", "Pass the path of the sfx-cues.json file.")
    C = read_json(cues_path)
    if isinstance(C, list):
        C = {"cues": C}
    aliases = C.get("aliases", {})
    root = Path(args.root) if args.root else Path(C["root"]) if C.get("root") else cues_path.resolve().parent
    mix = np.zeros(int((args.dur + 1) * SR), np.float64)
    ledger: dict[str, int] = {}
    warnings: list[str] = []
    n = 0
    for c in C.get("cues", []):
        name = aliases.get(c["f"], c["f"])
        p = Path(name) if Path(name).is_absolute() else root / name
        if not p.exists():
            raise VeosError("SFX_FILE_MISSING", f"sound file not found: {p}",
                            "Check the SFX folder (--root) and the file names/aliases in the cue sheet.")
        x = _decode_cached(p)
        fr = float(c.get("from", 0.0))
        to = float(c.get("to", len(x) / SR))
        seg = x[int(fr * SR):int(to * SR)].astype(np.float64)
        if len(seg) == 0:
            raise VeosError("BAD_CUE", f"cue at t={c.get('t')} trims '{name}' to nothing", "Check its from/to values.")
        if c.get("fi"):
            k = min(len(seg), int(c["fi"] * SR))
            seg[:k] *= np.linspace(0, 1, k) ** 2
        if c.get("fo"):
            k = min(len(seg), int(c["fo"] * SR))
            seg[len(seg) - k:] *= np.linspace(1, 0, k) ** 2
        pk = np.abs(seg).max() or 1.0
        seg *= 10 ** (float(c["db"]) / 20) / pk
        st = int(round((float(c["t"]) - (float(c.get("a", 0.0)) - fr)) * SR))
        if st < 0:
            seg = seg[-st:]
            st = 0
        e = min(len(mix), st + len(seg))
        if e > st:
            mix[st:e] += seg[:e - st]
        n += 1
        ledger[name] = ledger.get(name, 0) + 1
    mix = mix[: int(args.dur * SR)]
    pk = float(np.abs(mix).max())
    if pk > 0.9:
        mix *= 0.9 / pk
        warnings.append(f"bus peak {20 * np.log10(pk):.1f} dBFS was scaled down to -0.9 dBFS")
    out = Path(args.out)
    _write_wav(out, mix)
    over = sorted(f for f, u in ledger.items() if u > 2)
    return {"out": out.as_posix(), "cues": n, "files": len(ledger),
            "bus_peak_db": r3(20 * np.log10(float(np.abs(mix).max()) + 1e-12)), "dur": r3(len(mix) / SR),
            "ledger": dict(sorted(ledger.items(), key=lambda kv: -kv[1])), "over_2_uses": over, "warnings": warnings}


# --------------------------------------------------------------------------- mix
def _loudnorm_two_pass(ff: str, src: str, dst: str, dur: float) -> None:
    ln = f"loudnorm=I={TARGET_I}:TP={TARGET_TP}:LRA={TARGET_LRA}"
    r = run([ff, "-nostats", "-hide_banner", "-i", src, "-af", ln + ":print_format=json", "-f", "null", "-"], check=False)
    e = (r.stderr or b"").decode("utf-8", "replace")
    try:
        j = json.loads(e[e.rindex("{"):e.rindex("}") + 1])
    except ValueError as ex:
        raise VeosError("LOUDNORM_FAILED", "loudness analysis failed", "The mix input may be silent or corrupt.") from ex
    f = (f"{ln}:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:"
         f"measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true,"
         f"aresample={SR},apad=whole_dur={dur},atrim=0:{dur}")
    run([ff, "-y", "-v", "error", "-i", src, "-af", f, "-ar", str(SR), "-ac", "2", "-c:a", "pcm_s16le", dst])


def _mix(args, project) -> dict:
    t = tools()
    ff = t.ffmpeg
    for p in (args.voice, args.sfx, args.music):
        if p and not Path(p).exists():
            raise VeosError("AUDIO_MISSING", f"file not found: {p}", "Check the path.")
    dur = float(args.dur)
    chain = f"[0:a]aformat=channel_layouts=mono,{CHAIN},apad"
    with tempfile.TemporaryDirectory(dir=_scratch_dir()) as td:
        pre = str(Path(td) / "pre.wav")
        ins = ["-i", str(args.voice)]
        mixin, n = "[vm]", 1
        fc = chain + (",asplit=2[vm][vk];" if args.music else "[vm];")
        if args.sfx:
            ins += ["-i", str(args.sfx)]
            fc += f"[{n}:a]aformat=channel_layouts=mono[s{n}];"
            mixin += f"[s{n}]"
            n += 1
        if args.music:
            # music gain so the bed sits (music_db + 14) LU relative to the voice, before ducking
            vl = loudness(args.voice, CHAIN)["lufs"]
            ml = loudness(args.music)["lufs"]
            gain = (vl + (args.music_db - TARGET_I)) - ml if ml > -90 else 0.0
            ins += ["-stream_loop", "-1", "-i", str(args.music)]
            fc += (f"[{n}:a]aformat=channel_layouts=mono,volume={gain:.2f}dB[m0];"
                   f"[m0][vk]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=300[m1];")
            mixin += "[m1]"
            n += 1
        n_in = n
        fc += (f"{mixin}amix=inputs={n_in}:normalize=0:duration=longest,atrim=0:{dur},"
               f"alimiter=limit=0.84:attack=2:release=40:level=false,pan=stereo|c0=c0|c1=c0[o]")
        run([ff, "-y", "-v", "error", *ins, "-filter_complex", fc, "-map", "[o]", "-ar", str(SR), "-c:a", "pcm_f32le", pre],
            project, "mix")
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        _loudnorm_two_pass(ff, pre, str(out), dur)
    res = loudness(out)
    got = len(decode_mono(out)) / SR
    warns = []
    if abs(res["lufs"] - TARGET_I) > 0.5:
        warns.append(f"loudness {res['lufs']} LUFS is off target {TARGET_I}")
    if res["tp"] > TARGET_TP + 0.05:
        warns.append(f"true peak {res['tp']} dBTP is above {TARGET_TP}")
    return {"out": out.as_posix(), "lufs": res["lufs"], "tp": res["tp"], "dur": r3(got), "channels": 2,
            "sfx": bool(args.sfx), "music": bool(args.music), "warnings": warns}


def _scratch_dir() -> str:
    d = tools().scratch / "mix"
    d.mkdir(parents=True, exist_ok=True)
    return str(d)


# --------------------------------------------------------------------------- interface
def add_args(p, cmd: str) -> None:
    if cmd == "sfx":
        p.add_argument("cues", help="sfx-cues.json (aliases + cues)")
        p.add_argument("out", help="output 48 kHz mono WAV")
        p.add_argument("--dur", type=float, required=True, help="timeline length in seconds")
        p.add_argument("--root", default=None, help="folder holding the SFX files (default: the cue sheet's folder)")
    else:
        p.add_argument("voice", help="voice WAV (any audio file)")
        p.add_argument("out", help="output stereo WAV master")
        p.add_argument("--dur", type=float, required=True, help="exact output length in seconds")
        p.add_argument("--sfx", default=None, help="SFX bus WAV from `veos sfx`")
        p.add_argument("--music", default=None, help="optional music bed")
        p.add_argument("--music-db", type=float, default=-26.0, help="music bed loudness (LUFS) when the master is -14")


def main(args, project) -> dict:
    return _sfx(args, project) if args.cmd == "sfx" else _mix(args, project)
