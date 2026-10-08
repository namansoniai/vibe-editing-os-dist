"""Speaker labels without gated models or tokens: everything runs locally on CPU through onnxruntime.

Two modes, one output (a speaker activity matrix on a 10 ms grid -> turns -> per-word labels):

* **mics** (mode 1, preferred whenever each person has a mic): per-mic level envelopes on the session timeline; a mic's
  talker is active when the mic is above its own noise floor AND louder than the bleed expected from the other mics
  (the bleed ratio is calibrated per mic pair from moments where only one person talks). Overlap = 2+ active.
* **diarize** (mode 2, one mixed track): pyannote segmentation-3.0 (powerset, up to 3 local speakers and overlap per
  10 s window) -> one CAM++ speaker embedding per (window, local speaker) -> agglomerative clustering (to the known
  cast size, or by threshold) with a per-window cannot-link assignment (Hungarian) -> windows aggregated per frame,
  the per-frame speaker count decides how many speakers are active (overlap).

Models (downloaded once into VEOS_HOME/models/diarize, no account, no token; both from the sherpa-onnx GitHub
releases): pyannote segmentation-3.0 ONNX (5.7 MB, MIT, CNRS) and 3D-Speaker CAM++ VoxCeleb ONNX (28 MB, Apache-2.0).
"""
from __future__ import annotations

import hashlib
import math
import tarfile
import urllib.request
from pathlib import Path

import numpy as np

from .core import VeosError, veos_home

SR = 16000
HOP = 0.01
SEG_URL = ("https://github.com/k2-fsa/sherpa-onnx/releases/download/speaker-segmentation-models/"
           "sherpa-onnx-pyannote-segmentation-3-0.tar.bz2")
SEG_TAR_SHA = "24615ee884c897d9d2ba09bb4d30da6bb1b15e685065962db5b02e76e4996488"
SEG_SHA = "220ad67ca923bef2fa91f2390c786097bf305bceb5e261d4af67b38e938e1079"
EMB_URL = ("https://github.com/k2-fsa/sherpa-onnx/releases/download/speaker-recongition-models/"
           "3dspeaker_speech_campplus_sv_en_voxceleb_16k.onnx")
EMB_SHA = "357a834f702b80161e5b981182c038e18553c1f2ca752ed6cec2052365d4129b"
SEG_NAME, EMB_NAME = "pyannote-segmentation-3.0.onnx", "campplus_sv_en_voxceleb_16k.onnx"
MODELS_MB = {"segmentation": 5.7, "embedding": 28.2}
BACKCHANNEL = {"yeah", "yes", "yep", "yup", "right", "true", "exactly", "ok", "okay", "hmm", "mm", "mhm", "uh-huh",
               "wow", "nice", "sure", "haan", "ha", "accha", "achha", "acha", "sahi", "bilkul", "correct", "absolutely",
               "totally", "really", "oh", "ah", "haha", "lol", "great", "cool", "amazing", "interesting", "hmm.", "ji"}
LAUGH = {"haha", "hahaha", "[laughter]", "(laughs)", "[laughs]", "lol", "hehe"}


# ======================================================================= models
def models_dir() -> Path:
    return veos_home() / "models" / "diarize"


def _sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def _download(url: str, dest: Path, sha: str) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    part = dest.with_name(dest.name + ".part")
    try:
        urllib.request.urlretrieve(url, part)
        if sha and _sha(part) != sha:
            raise ValueError("sha256 mismatch")
        part.replace(dest)
    except Exception as e:  # noqa: BLE001
        part.unlink(missing_ok=True)
        raise VeosError("MODEL_MISSING", f"speaker model {dest.name} missing and the download failed ({e})",
                        "Check the internet connection and run `veos doctor` (or /vibe-editing-os:setup update).") from e


def model_paths(fetch: bool = True) -> dict:
    """{'segmentation': Path, 'embedding': Path}; downloads (and verifies) what is missing when `fetch`."""
    d = models_dir()
    seg, emb = d / SEG_NAME, d / EMB_NAME
    if fetch and not seg.exists():
        tar = d / "segmentation-3.0.tar.bz2"
        _download(SEG_URL, tar, SEG_TAR_SHA)
        with tarfile.open(tar, "r:bz2") as tf:
            for m in tf.getmembers():
                name = Path(m.name).name
                if name in ("model.onnx", "LICENSE") and m.isfile():
                    data = tf.extractfile(m).read()
                    (d / (SEG_NAME if name == "model.onnx" else "pyannote-segmentation-3.0.LICENSE.txt")).write_bytes(data)
        tar.unlink(missing_ok=True)
        if _sha(seg) != SEG_SHA:
            seg.unlink(missing_ok=True)
            raise VeosError("MODEL_MISSING", "speaker segmentation model failed its checksum", "Re-run `veos doctor`.")
    if fetch and not emb.exists():
        _download(EMB_URL, emb, EMB_SHA)
    return {"segmentation": seg, "embedding": emb}


def models_present() -> bool:
    p = model_paths(fetch=False)
    return p["segmentation"].exists() and p["embedding"].exists()


def _session(path: Path, threads: int = 0):
    import onnxruntime as ort
    o = ort.SessionOptions()
    o.intra_op_num_threads = threads or max(1, min(8, (__import__("os").cpu_count() or 2) // 2))
    o.inter_op_num_threads = 1
    o.log_severity_level = 3
    return ort.InferenceSession(str(path), sess_options=o, providers=["CPUExecutionProvider"])


# ======================================================================= features
_MEL_CACHE: dict = {}


def _mel_banks(n_mels: int = 80, nfft: int = 512, sr: int = SR, low: float = 20.0, high: float = -400.0) -> np.ndarray:
    key = (n_mels, nfft, sr, low, high)
    if key in _MEL_CACHE:
        return _MEL_CACHE[key]
    hi = sr / 2 + high if high <= 0 else high
    mel = lambda f: 1127.0 * np.log1p(np.asarray(f, np.float64) / 700.0)  # noqa: E731
    mlo, mhi = mel(low), mel(hi)
    dm = (mhi - mlo) / (n_mels + 1)
    freqs = np.arange(nfft // 2) * sr / nfft
    m = mel(freqs)
    W = np.zeros((n_mels, nfft // 2 + 1), np.float32)
    for b in range(n_mels):
        l, c, r = mlo + b * dm, mlo + (b + 1) * dm, mlo + (b + 2) * dm
        up = (m - l) / (c - l)
        dn = (r - m) / (r - c)
        W[b, : nfft // 2] = np.maximum(0.0, np.minimum(up, dn)) * ((m > l) & (m < r))
    _MEL_CACHE[key] = W
    return W


def fbank(x: np.ndarray, sr: int = SR, n_mels: int = 80) -> np.ndarray:
    """Kaldi-compatible log mel filterbank (25 ms povey window, 10 ms shift, pre-emphasis 0.97, DC removal, 512-pt
    power spectrum, mel 20 Hz..Nyquist-400 Hz, no dither, snip_edges). Input float in [-1, 1]. -> [T, n_mels]."""
    fl, fs, nfft = int(0.025 * sr), int(0.010 * sr), 512
    x = np.asarray(x, np.float32)
    if len(x) < fl:
        x = np.pad(x, (0, fl - len(x)))
    n = 1 + (len(x) - fl) // fs
    idx = np.arange(fl)[None, :] + fs * np.arange(n)[:, None]
    fr = x[idx].astype(np.float32)
    fr -= fr.mean(1, keepdims=True)
    fr[:, 1:] -= 0.97 * fr[:, :-1].copy()
    fr[:, 0] *= 1 - 0.97
    win = (0.5 - 0.5 * np.cos(2 * np.pi * np.arange(fl) / (fl - 1))) ** 0.85
    spec = np.abs(np.fft.rfft(fr * win.astype(np.float32), nfft)) ** 2
    mel = spec @ _mel_banks(n_mels, nfft, sr).T
    return np.log(np.maximum(mel, 1.1920929e-07)).astype(np.float32)


class Embedder:
    """CAM++ speaker embedding (512-d, L2-normalised) from 16 kHz audio."""

    def __init__(self, path: Path | None = None):
        self.sess = _session(path or model_paths()["embedding"])
        self.inp = self.sess.get_inputs()[0].name

    def __call__(self, x: np.ndarray) -> np.ndarray:
        f = fbank(x)
        f = f - f.mean(0, keepdims=True)          # feature_normalize_type: global-mean
        e = self.sess.run(None, {self.inp: f[None]})[0][0].astype(np.float64)
        return e / (np.linalg.norm(e) + 1e-12)


# ======================================================================= segmentation (pyannote 3.0, powerset)
class Segmenter:
    def __init__(self, path: Path | None = None):
        self.sess = _session(path or model_paths()["segmentation"])
        meta = self.sess.get_modelmeta().custom_metadata_map
        self.window = int(meta.get("window_size", 160000))
        self.rf_shift = int(meta.get("receptive_field_shift", 270))
        self.rf_size = int(meta.get("receptive_field_size", 991))
        self.nspk = int(meta.get("num_speakers", 3))
        self.inp = self.sess.get_inputs()[0].name
        # powerset class -> speakers (class 0 = silence, then singles, then pairs)
        rows = [[0] * self.nspk]
        rows += [[1 if j == i else 0 for j in range(self.nspk)] for i in range(self.nspk)]
        rows += [[1 if j in (a, b) else 0 for j in range(self.nspk)] for a in range(self.nspk) for b in range(a + 1, self.nspk)]
        self.mapping = np.array(rows, np.float32)

    def __call__(self, audio: np.ndarray, step_s: float = 1.5, batch: int = 16) -> tuple[np.ndarray, np.ndarray, int]:
        """-> (labels [chunks, frames, nspk] binary, chunk start samples, frames per chunk)."""
        W = self.window
        step = int(step_s * SR)
        n = len(audio)
        starts = list(range(0, max(1, n - W + 1), step))
        if not starts or starts[-1] + W < n:
            starts.append(max(0, n - W) if n > W else 0)
        starts = sorted(set(starts))
        out = []
        for i in range(0, len(starts), batch):
            seg = np.zeros((len(starts[i:i + batch]), 1, W), np.float32)
            for k, s in enumerate(starts[i:i + batch]):
                chunk = audio[s:s + W]
                seg[k, 0, :len(chunk)] = chunk
            y = self.sess.run(None, {self.inp: seg})[0]
            out.append(y)
        y = np.concatenate(out, 0)
        labels = self.mapping[np.argmax(y, -1)]
        return labels, np.array(starts), y.shape[1]

    def frame_time(self, start_sample: int, k: np.ndarray | int) -> np.ndarray:
        return (start_sample + np.asarray(k) * self.rf_shift + self.rf_size / 2) / SR


# ======================================================================= clustering
def cluster(E: np.ndarray, k: int | None = None, threshold: float = 0.62, min_share: float = 0.05,
            weights: np.ndarray | None = None, merge_sim: float = 0.6) -> np.ndarray:
    """Agglomerative clustering (average linkage, cosine). k known -> exactly k clusters (then 3 centroid refinement
    passes); else cut at cosine distance `threshold` and merge clusters holding < min_share of the speech weight."""
    from scipy.cluster.hierarchy import fcluster, linkage
    n = len(E)
    if n == 0:
        return np.zeros(0, int)
    if n == 1 or k == 1:
        return np.zeros(n, int)
    w = np.ones(n) if weights is None else np.asarray(weights, float)
    Z = linkage(E, method="average", metric="cosine")
    lab = fcluster(Z, t=threshold, criterion="distance") - 1
    # merge clusters that hold too little speech into their nearest neighbour
    while True:
        ids = np.unique(lab)
        share = np.array([w[lab == c].sum() for c in ids]) / w.sum()
        if len(ids) <= 1 or share.min() >= min_share:
            break
        C = _cent(E, lab, w, ids)
        small = int(np.argmin(share))
        sim = C @ C[small]
        sim[small] = -9
        lab[lab == ids[small]] = ids[int(np.argmax(sim))]
    if not k:  # unknown cast size: clusters whose centroids are this alike are one voice
        while len(np.unique(lab)) > 1:
            ids = np.unique(lab)
            C = _cent(E, lab, w, ids)
            S = C @ C.T
            np.fill_diagonal(S, -9)
            a, b = np.unravel_index(int(np.argmax(S)), S.shape)
            if S[a, b] < merge_sim:
                break
            lab[lab == ids[b]] = ids[a]
    if k:
        # exactly k: merge the closest pair of centroids, or split the largest cluster in two (farthest-pair seeds)
        while len(np.unique(lab)) > k:
            ids = np.unique(lab)
            C = _cent(E, lab, w, ids)
            S = C @ C.T
            np.fill_diagonal(S, -9)
            a, b = np.unravel_index(int(np.argmax(S)), S.shape)
            lab[lab == ids[b]] = ids[a]
        guard = 0
        while len(np.unique(lab)) < k and guard < k:
            guard += 1
            ids = np.unique(lab)
            big = ids[int(np.argmax([w[lab == c].sum() for c in ids]))]
            m = np.flatnonzero(lab == big)
            if len(m) < 2:
                break
            S = E[m] @ E[m].T
            i, j = np.unravel_index(int(np.argmin(S)), S.shape)
            seeds = np.stack([E[m[i]], E[m[j]]])
            for _ in range(5):
                part = np.argmax(E[m] @ seeds.T, axis=1)
                if part.min() == part.max():
                    break
                seeds = np.stack([np.average(E[m][part == q], axis=0, weights=w[m][part == q]) for q in (0, 1)])
                seeds /= np.linalg.norm(seeds, axis=1, keepdims=True) + 1e-12
            lab[m[part == 1]] = lab.max() + 1
    # weighted spherical k-means refinement
    for _ in range(5):
        ids = np.unique(lab)
        C = _cent(E, lab, w, ids)
        new = np.argmax(E @ C.T, axis=1)
        if k and len(np.unique(new)) < len(ids):
            break
        lab = ids[new]
    _, lab = np.unique(lab, return_inverse=True)
    return lab


def _cent(E: np.ndarray, lab: np.ndarray, w: np.ndarray, ids) -> np.ndarray:
    C = np.stack([np.average(E[lab == c], axis=0, weights=w[lab == c]) for c in ids])
    return C / (np.linalg.norm(C, axis=1, keepdims=True) + 1e-12)


def centroids(E: np.ndarray, lab: np.ndarray, w: np.ndarray | None = None) -> np.ndarray:
    w = np.ones(len(E)) if w is None else w
    C = np.stack([np.average(E[lab == c], axis=0, weights=w[lab == c]) for c in range(lab.max() + 1)])
    return C / (np.linalg.norm(C, axis=1, keepdims=True) + 1e-12)


# ======================================================================= mode 2: diarise one track
def speech_count(audio: np.ndarray, seg: Segmenter, step_s: float = 1.5) -> np.ndarray:
    """[T] number of simultaneous talkers per 10 ms (0 = silence), from the segmentation model aggregated over windows."""
    labels, starts, nf = seg(audio, step_s)
    T = int(math.ceil(len(audio) / SR / HOP)) + 1
    cover, cnt = np.zeros(T), np.zeros(T)
    k_idx = np.arange(nf)
    for c in range(len(starts)):
        gi = np.clip(np.round(seg.frame_time(int(starts[c]), k_idx) / HOP).astype(int), 0, T - 1)
        n_on = labels[c].sum(1)
        for off in (0, 1):
            g = np.clip(gi + off, 0, T - 1)
            np.add.at(cover, g, 1)
            np.add.at(cnt, g, n_on)
    return np.round(cnt / np.maximum(cover, 1)).astype(int)


def viterbi(score: np.ndarray, switch: float) -> np.ndarray:
    """Best label path through per-frame scores [K, T] with a constant penalty per label change."""
    K, T = score.shape
    back = np.zeros((K, T), np.int32)
    v = score[:, 0].copy()
    for t in range(1, T):
        stay = v
        best = int(np.argmax(v))
        move = v[best] - switch
        take_move = move > stay
        back[:, t] = np.where(take_move, best, np.arange(K))
        v = np.where(take_move, move, stay) + score[:, t]
    path = np.zeros(T, np.int32)
    path[-1] = int(np.argmax(v))
    for t in range(T - 1, 0, -1):
        path[t - 1] = back[path[t], t]
    return path


def diarize(audio: np.ndarray, num_speakers: int | None = None, step_s: float = 1.5, threshold: float = 0.62,
            seg: Segmenter | None = None, emb: Embedder | None = None, win_s: float = 1.0, hop_s: float | None = None,
            switch: float = 6.0, max_cluster: int = 1500, progress=None) -> dict:
    """Diarise 16 kHz mono float audio. -> {hop, act [K,T] bool, score [K,T], count [T], centroids [K,512], quality}.

    1. speech + overlap count per 10 ms from pyannote segmentation-3.0 (its local speaker split is NOT trusted for
       identity: on fast handovers it often lumps two voices into one local speaker);
    2. identity from CAM++ embeddings of short sliding windows (1.0 s, hop 0.25 s; 0.5 s over 10 min) on speech;
    3. clustering of the clean windows (one talker, mostly speech) to the known cast size, or by threshold;
    4. per-frame similarity to each centroid (triangular weighting of the covering windows), Viterbi with a switch
       penalty (no flicker), overlap frames add the runner-up speaker as a second active talker."""
    seg = seg or Segmenter()
    emb = emb or Embedder()
    dur = len(audio) / SR
    hop_s = hop_s or (0.25 if dur <= 600 else 0.5)
    count = speech_count(audio, seg, step_s)
    T = len(count)
    speech = count > 0
    wf, hf = int(round(win_s / HOP)), int(round(hop_s / HOP))
    starts = [s for s in range(0, max(1, T - wf), hf) if speech[s:s + wf].mean() >= 0.6]
    if not starts:
        return {"hop": HOP, "act": np.zeros((0, T), bool), "score": np.zeros((0, T)), "count": count,
                "centroids": np.zeros((0, 512)), "quality": {"embeddings": 0, "note": "no speech found"}}
    E = np.array([emb(audio[int(s * HOP * SR): int((s + wf) * HOP * SR)]) for s in starts])
    clean = np.array([(count[s:s + wf] <= 1).all() and speech[s:s + wf].mean() >= 0.8 for s in starts])
    pick = np.flatnonzero(clean) if clean.sum() >= max(4, 0.2 * len(starts)) else np.arange(len(starts))
    if len(pick) > max_cluster:
        pick = pick[np.linspace(0, len(pick) - 1, max_cluster).astype(int)]
    lab = cluster(E[pick], num_speakers, threshold)
    K = int(lab.max()) + 1
    Cn = centroids(E[pick], lab)
    sim = E @ Cn.T                                     # [windows, K]
    tri = 1.0 - np.abs(np.linspace(-1, 1, wf)) * 0.8   # centre-weighted
    acc, wsum = np.zeros((K, T)), np.zeros(T)
    for i, s in enumerate(starts):
        e = min(T, s + wf)
        acc[:, s:e] += sim[i][:, None] * tri[: e - s]
        wsum[s:e] += tri[: e - s]
    has = wsum > 0
    score = np.zeros((K, T))
    score[:, has] = acc[:, has] / wsum[has]
    # fill frames with speech but no window (edges) from the nearest scored frame
    idx = np.flatnonzero(has)
    if len(idx):
        near = idx[np.clip(np.searchsorted(idx, np.arange(T)), 0, len(idx) - 1)]
        score[:, ~has] = score[:, near[~has]]
    path = viterbi(score - score.mean(0, keepdims=True), switch * HOP * 10) if K > 1 else np.zeros(T, np.int32)
    act = np.zeros((K, T), bool)
    act[path[speech], np.flatnonzero(speech)] = True
    if K > 1:
        second = np.argsort(-score, axis=0)[1]
        ov = count >= 2
        act[second[ov], np.flatnonzero(ov)] = True
    soft = np.clip((score + 1) / 2, 0, 1) * act
    own = sim[np.arange(len(sim)), np.argmax(sim, 1)]
    if K > 1:
        srt = np.sort(sim, 1)
        margin = float(np.mean(srt[:, -1] - srt[:, -2]))
        csim = float(np.max(Cn @ Cn.T - 2 * np.eye(K)))
    else:
        margin, csim = None, None
    return {"hop": HOP, "act": act, "score": soft, "count": count, "centroids": Cn,
            "quality": {"embeddings": len(E), "clustered": int(len(pick)), "speakers": K,
                        "cluster_margin": None if margin is None else round(margin, 3),
                        "centroid_similarity": None if csim is None else round(csim, 3),
                        "own_similarity": round(float(own.mean()), 3), "window_s": win_s, "hop_s": hop_s}}


# ======================================================================= mode 1: per-mic voice activity
def _env_db(x: np.ndarray, sr: int, hop: float = HOP) -> np.ndarray:
    h = int(round(hop * sr))
    n = len(x) // h
    e = np.sqrt((x[: n * h].reshape(n, h).astype(np.float64) ** 2).mean(1) + 1e-12)
    return 20 * np.log10(e + 1e-9)


def _smooth_bool(b: np.ndarray, hold: int, min_on: int) -> np.ndarray:
    """Hangover of `hold` frames after activity, then drop bursts shorter than `min_on` frames."""
    out = b.copy()
    last = -10 ** 9
    for i in range(len(b)):
        if b[i]:
            last = i
        elif i - last <= hold:
            out[i] = True
    edges = np.flatnonzero(np.diff(np.concatenate([[0], out.astype(int), [0]])) != 0).reshape(-1, 2)
    for a, z in edges:
        if z - a < min_on:
            out[a:z] = False
    return out


def mic_activity(tracks: list[np.ndarray], sr: int, hop: float = HOP, margin_db: float = 6.0) -> dict:
    """Time-aligned mic tracks (one per person) -> activity [K, T].

    Mic i's talker is active when (a) mic i is 12+ dB over its noise floor (or 40% of its floor-to-speech range) and
    (b) it is louder than the bleed predicted from every other active mic j: L_i > L_j + bleed_ji + margin, where
    bleed_ji = median(L_i - L_j) over frames in which j clearly dominates (calibrated per pair; default -15 dB)."""
    n = min(len(t) for t in tracks)
    L = np.array([_env_db(t[:n], sr, hop) for t in tracks])
    K, T = L.shape
    floor = np.percentile(L, 10, axis=1)
    speech = np.percentile(L, 97, axis=1)
    thr = floor + np.maximum(12.0, 0.4 * (speech - floor))
    loud = L > thr[:, None]
    bleed = np.full((K, K), -15.0)
    rel = L - speech[:, None]
    for j in range(K):
        for i in range(K):
            if i == j:
                continue
            dom_j = loud[j] & (rel[j] > (np.delete(rel, j, 0).max(0) + 8.0))
            if dom_j.sum() > 50:
                bleed[j, i] = float(np.median(L[i, dom_j] - L[j, dom_j]))
    act = np.zeros((K, T), bool)
    for i in range(K):
        ok = loud[i].copy()
        for j in range(K):
            if j != i:
                ok &= ~(loud[j] & (L[i] <= L[j] + bleed[j, i] + margin_db))
        act[i] = _smooth_bool(ok, hold=int(0.25 / hop), min_on=int(0.12 / hop))
    score = np.clip((L - floor[:, None]) / np.maximum(speech - floor, 1)[:, None], 0, 1) * act
    return {"hop": hop, "act": act, "score": score, "count": act.sum(0),
            "quality": {"bleed_db": np.round(bleed, 1).tolist(), "floor_db": np.round(floor, 1).tolist(),
                        "speech_db": np.round(speech, 1).tolist()}}


# ======================================================================= shared post-processing
def dominant(res: dict) -> np.ndarray:
    """[T] index of the dominant active speaker, -1 where nobody speaks."""
    act, sc = res["act"], res["score"]
    if act.shape[0] == 0:
        return np.full(act.shape[1], -1)
    s = np.where(act, sc + 1.0, -1.0)
    d = np.argmax(s, axis=0)
    d[~act.any(0)] = -1
    return d


def turns_from(res: dict, ids: list[str], min_gap: float = 0.35, min_len: float = 0.15) -> list[dict]:
    """Dominant-speaker runs merged across short gaps -> [{speaker, t0, t1, overlap_s}]."""
    hop = res["hop"]
    d = dominant(res)
    runs = []
    i, T = 0, len(d)
    while i < T:
        if d[i] < 0:
            i += 1
            continue
        j = i
        while j < T and d[j] == d[i]:
            j += 1
        runs.append([int(d[i]), i, j])
        i = j
    merged: list[list] = []
    for r in runs:
        if merged and merged[-1][0] == r[0] and (r[1] - merged[-1][2]) * hop <= min_gap:
            merged[-1][2] = r[2]
        else:
            merged.append(r)
    # absorb very short runs sandwiched by the same speaker
    out: list[list] = []
    for k, r in enumerate(merged):
        if (r[2] - r[1]) * hop < min_len and out and k + 1 < len(merged) and merged[k + 1][0] == out[-1][0]:
            continue
        if out and out[-1][0] == r[0] and (r[1] - out[-1][2]) * hop <= min_gap:
            out[-1][2] = r[2]
        else:
            out.append(r)
    ov = res["act"].sum(0) >= 2
    return [{"speaker": ids[s], "t0": round(a * hop, 3), "t1": round(b * hop, 3),
             "overlap_s": round(float(ov[a:b].sum()) * hop, 2)} for s, a, b in out if (b - a) * hop >= min_len]


def label_words(words: list[dict], res: dict, ids: list[str], max_snap: float = 1.0) -> dict:
    """Write `speaker` (dominant over the word), `spk_conf` (0..1) and `overlap` (another speaker active >= 40% of the
    word) into each word in place. Words with no detected activity take the nearest active speaker within `max_snap` s,
    else the previous word's speaker. Returns counts."""
    hop = res["hop"]
    act, sc = res["act"], res["score"]
    K, T = act.shape
    d = dominant(res)
    stats = {"labelled": 0, "snapped": 0, "carried": 0, "overlap": 0, "unlabelled": 0}
    prev = None
    act_idx = np.flatnonzero(d >= 0)
    for w in words:
        a, b = int(math.floor(w["s"] / hop)), int(math.ceil(w["e"] / hop))
        a, b = max(0, min(a, T - 1)), max(a + 1, min(b, T))
        if K == 0:
            w.pop("speaker", None)
            stats["unlabelled"] += 1
            continue
        tot = (act[:, a:b] * (1.0 + sc[:, a:b])).sum(1)
        if tot.max() > 0:
            k = int(np.argmax(tot))
            srt = np.sort(tot)[::-1]
            if K > 1 and prev in ids and srt[1] >= 0.95 * srt[0] and tot[ids.index(prev)] >= 0.95 * srt[0]:
                k = ids.index(prev)          # a tie in overlapped speech: the floor stays with the current speaker
            w["speaker"] = ids[k]
            w["spk_conf"] = round(float((srt[0] - (srt[1] if K > 1 else 0)) / (srt[0] + 1e-9)), 2)
            frac_other = (act[np.arange(K) != k, a:b].any(0)).mean() if K > 1 else 0.0
            if frac_other >= 0.4:
                w["overlap"] = True
                stats["overlap"] += 1
            else:
                w.pop("overlap", None)
            stats["labelled"] += 1
        elif len(act_idx):
            c = (a + b) // 2
            p = int(np.searchsorted(act_idx, c))
            cand = [act_idx[q] for q in (p - 1, p) if 0 <= q < len(act_idx)]
            near = min(cand, key=lambda q: abs(q - c))
            if abs(near - c) * hop <= max_snap:
                w["speaker"], w["spk_conf"] = ids[int(d[near])], 0.3
                stats["snapped"] += 1
            elif prev:
                w["speaker"], w["spk_conf"] = prev, 0.2
                stats["carried"] += 1
            else:
                stats["unlabelled"] += 1
        elif prev:
            w["speaker"], w["spk_conf"] = prev, 0.2
            stats["carried"] += 1
        # a turn's first word that starts in silence (a stretched ASR word): start it at the speaker's voice onset
        if w.get("speaker") and w["speaker"] != prev and w["e"] - w["s"] > 0.45:
            k = ids.index(w["speaker"])
            on = np.flatnonzero(act[k, a:b])
            if len(on) and on[0] > 0 and (a + on[0]) * hop < w["e"] - 0.1:
                w["s"] = round((a + on[0]) * hop, 3)
                w["onset_from"] = "speaker"
                stats["onsets_fixed"] = stats.get("onsets_fixed", 0) + 1
        prev = w.get("speaker", prev)
    return stats


def is_backchannel(text_words: list[str], dur: float) -> bool:
    toks = [t.strip(".,!?…\"'").lower() for t in text_words if t.strip()]
    return 0 < len(toks) <= 3 and dur <= 1.6 and all(t in BACKCHANNEL for t in toks)


def is_laugh(text_words: list[str]) -> bool:
    return any(t.strip(".,!?").lower() in LAUGH for t in text_words)


# ======================================================================= evaluation (used by tests and the proof)
def frame_labels(turns: list[dict], ids: list[str], dur: float, hop: float = HOP) -> np.ndarray:
    T = int(math.ceil(dur / hop))
    y = np.full(T, -1)
    for t in turns:
        if t["speaker"] in ids:
            y[int(t["t0"] / hop): int(t["t1"] / hop)] = ids.index(t["speaker"])
    return y


def best_mapping(ref: np.ndarray, hyp: np.ndarray, n_ref: int, n_hyp: int) -> dict:
    """Optimal hyp->ref label mapping (Hungarian on co-occurrence)."""
    from scipy.optimize import linear_sum_assignment
    M = np.zeros((n_hyp, n_ref))
    both = (ref >= 0) & (hyp >= 0)
    np.add.at(M, (hyp[both], ref[both]), 1)
    r, c = linear_sum_assignment(-M)
    return {int(a): int(b) for a, b in zip(r, c)}


def speaker_error(ref: np.ndarray, hyp: np.ndarray, n_ref: int, n_hyp: int, collar: int = 25) -> dict:
    """Frame-level scores with a +-collar (frames) around reference boundaries excluded (standard 0.25 s collar).
    -> {der, confusion, miss, false_alarm, mapping}."""
    keep = np.ones(len(ref), bool)
    edges = np.flatnonzero(np.diff(ref) != 0)
    for e in edges:
        keep[max(0, e - collar + 1): e + collar + 1] = False
    m = best_mapping(ref, hyp, n_ref, n_hyp)
    hm = np.array([m.get(int(h), -2) if h >= 0 else -1 for h in hyp])
    r, h = ref[keep], hm[keep]
    speech = (r >= 0).sum()
    miss = ((r >= 0) & (h == -1)).sum()
    fa = ((r == -1) & (h != -1)).sum()
    conf = ((r >= 0) & (h != -1) & (h != r)).sum()
    return {"der": round(float((miss + fa + conf) / max(speech, 1)), 4), "confusion": round(float(conf / max(speech, 1)), 4),
            "miss": round(float(miss / max(speech, 1)), 4), "false_alarm": round(float(fa / max(speech, 1)), 4),
            "mapping": m}
