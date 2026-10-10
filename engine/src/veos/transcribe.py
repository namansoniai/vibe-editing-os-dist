"""`veos transcribe`: word-level transcript (source time) with silence-aligned chunks, onset snap and glossary pass.

The audio decides what is silence (speechmap.py: voice detector + level), and the transcript is cleaned against it:
  * a word lying (almost) wholly inside a real silence (>= 0.25 s) is a hallucination ("you." over a look-away): it
    keeps its place in words/<id>.json with `suspect: "in_silence"`, and `veos cut` leaves it out of words.edit.json
    (so out of the captions) unless `--keep-suspect`;
  * a word that runs into or across a silence is trimmed to its voiced part (`orig` keeps the model's times).
Language, script or confidence never make a word suspect: regional speech must survive.

Language: --language, else the playbook's speech language (profile.language.speech / creator.language; a code-mix maps
to its regional language: "telugu-english" -> te), else hi. Model (speechmodel.py): --model, else VEOS_WHISPER_MODEL,
else the playbook's profile.language.model, else large-v3 for te / ta / kn / ml / bn / gu / pa / mr speech (downloaded
once, ~3 GB, on the first such reel; turbo with a warning when that fails), else large-v3-turbo.
"""
from __future__ import annotations

import difflib
import os
import re
import time
from pathlib import Path

import numpy as np

from . import speechmap, speechmodel
from .core import VeosError, need_project, r3, read_json, tools, write_json
from .glossary import apply_glossary, load_glossary, term_list
from .langs import script_of

SR = 16000
HOP = 0.02            # 20 ms RMS hop
SIL_DB, SIL_MIN = speechmap.SIL_DB, speechmap.SIL_MIN
MODEL = "large-v3-turbo"
IN_SIL_FRAC = 0.8     # a word with >= 80 % of it inside real silence ...
VOICED_MIN = 0.12     # ... and less than this much outside it lies in the silence (suspect "in_silence")
ABUT_S = 0.05         # a neighbour this close counts as touching the word


def add_args(p, cmd):
    p.add_argument("--id", help="source id (default: all sources in sources.json)")
    p.add_argument("--script", help="script file; its first ~200 characters become the initial prompt")
    p.add_argument("--glossary", help="extra glossary JSON merged over the default one")
    p.add_argument("--fast", action="store_true", help="greedy decoding and longer chunks (same model)")
    p.add_argument("--language", default=None,
                   help="speech language, a code or a name (te, ta, telugu-english, ...; default: the playbook's speech "
                        "language, else hi)")
    p.add_argument("--audio", help="standalone: wav/audio file to transcribe instead of work/audio/<id>.wav")
    p.add_argument("--model", default=None,
                   help="speech model (default: VEOS_WHISPER_MODEL, else the playbook's profile.language.model, else "
                        "large-v3 for Telugu / Tamil / Kannada / Malayalam / Bengali / Gujarati / Punjabi / Marathi "
                        "speech, else large-v3-turbo)")
    p.add_argument("--no-vad", action="store_true", help="speech map from the sound level only (no voice detector)")


# ---------------------------------------------------------------- audio helpers
def load_audio(path: str | Path) -> np.ndarray:
    from faster_whisper.audio import decode_audio
    return decode_audio(str(path), sampling_rate=SR)


def rms_envelope(audio: np.ndarray, hop: float = HOP) -> np.ndarray:
    h = int(round(hop * SR))
    n = len(audio) // h
    if n == 0:
        return np.zeros(0, np.float32)
    x = audio[: n * h].reshape(n, h)
    return np.sqrt((x ** 2).mean(axis=1)).astype(np.float32)


def find_silences(audio: np.ndarray) -> list[list[float]]:
    """Runs of >= 0.18 s below -42 dB (20 ms RMS frames), like ffmpeg silencedetect n=-42dB:d=0.18."""
    env = rms_envelope(audio)
    quiet = 20 * np.log10(env + 1e-9) < SIL_DB
    out, i, n = [], 0, len(quiet)
    while i < n:
        if quiet[i]:
            j = i
            while j < n and quiet[j]:
                j += 1
            if (j - i) * HOP >= SIL_MIN:
                out.append([r3(i * HOP), r3(j * HOP)])
            i = j
        else:
            i += 1
    return out


def make_chunks(audio: np.ndarray, silences: list[list[float]], maxlen: float) -> list[tuple[float, float]]:
    dur = len(audio) / SR
    cuts = [(s + e) / 2 for s, e in silences]
    chunks, s0 = [], 0.0
    while s0 < dur - 0.05:
        lim = s0 + maxlen
        if lim >= dur:
            chunks.append((s0, dur))
            break
        cand = [x for x in cuts if s0 + 1.0 < x <= lim]
        if cand:
            e0 = cand[-1]
        else:  # no pause: quietest 20 ms in the last 3 s, never mid-word
            hop = int(HOP * SR)
            i0 = max(0, int((lim - 3) * SR))
            i1 = int(lim * SR) - hop
            rms = [np.sqrt((audio[i:i + hop] ** 2).mean()) for i in range(i0, max(i0 + hop, i1), hop)]
            e0 = (i0 + int(np.argmin(rms)) * hop + hop / 2) / SR
        chunks.append((s0, e0))
        s0 = e0
    return chunks


def snap_onsets(words: list[dict], audio: np.ndarray, window: float = 0.12) -> int:
    """Move each word start to the nearest rising RMS onset within +-120 ms. Returns how many moved/confirmed."""
    env = rms_envelope(audio)
    if len(env) < 6:
        return 0
    db = 20 * np.log10(env + 1e-9)
    floor = np.percentile(db, 10)
    onsets = []
    for k in range(2, len(db)):
        rise = db[k] - db[k - 2]
        if rise >= 6.0 and db[k] > floor + 10 and db[k - 1] < db[k]:
            # walk back to the foot of the rise so the onset is where the energy starts
            f = k - 1
            while f > 0 and db[f - 1] < db[f] and db[f] - db[f - 1] > 0.5:
                f -= 1
            onsets.append(f * HOP)
    if not onsets:
        return 0
    on = np.array(sorted(set(onsets)))
    n, prev = 0, 0.0
    for w in words:
        j = int(np.argmin(np.abs(on - w["s"])))
        if abs(on[j] - w["s"]) <= window:
            s = max(float(on[j]), prev)
            if s < w["e"] - 0.02:
                w["s"] = r3(s)
                w["onset_snapped"] = True
                n += 1
        prev = w["s"]
    return n


def script_kind(word: str) -> str:
    """devanagari | telugu | tamil | kannada | malayalam | bengali | gujarati | gurmukhi | odia | arabic | latin | other"""
    return script_of(word)


# ---------------------------------------------------------------- clean-up against the audio
def silence_fix(words: list[dict], silences: list, min_sil: float = speechmap.LIST_MIN) -> dict:
    """Mark words lying in real silence `suspect: "in_silence"` and trim words that run into / across one to their
    voiced part (`orig` = the model's times). Only the audio decides. Returns {"in_silence": n, "trimmed": n}."""
    sil = sorted([float(a), float(b)] for a, b in silences if b - a >= min_sil - 1e-9)
    n_in = n_trim = 0
    for k, w in enumerate(words):
        s, e = float(w["s"]), float(w["e"])
        d = e - s
        if d <= 0:
            continue
        hit = [(a, b) for a, b in sil if speechmap.overlap(s, e, a, b) > 0.01]
        if not hit:
            continue
        inside = sum(speechmap.overlap(s, e, a, b) for a, b in hit)
        if inside >= IN_SIL_FRAC * d and d - inside < VOICED_MIN:
            w["suspect"] = "in_silence"
            n_in += 1
            continue
        prev = next((x for x in reversed(words[:k]) if not x.get("suspect")), None)
        nxt = words[k + 1] if k + 1 < len(words) else None
        for a, b in sorted(hit, key=lambda x: x[0] - x[1]):  # the longest silence first
            if speechmap.overlap(s, e, a, b) <= 0.01:
                continue
            if a <= s + 0.01:            # starts in the silence: the word starts when it ends
                s = b
            elif b >= e - 0.01:          # ends in the silence: the word ends when it starts
                e = a
            else:                        # the silence is inside the word: keep the side that is the word
                before, after = a - s, e - b
                prev_touch = prev is not None and prev["e"] >= s - ABUT_S
                next_touch = nxt is not None and nxt["s"] <= e + ABUT_S
                if prev_touch and not next_touch:
                    keep_after = True    # the start was pulled back onto the previous word ("Team" + "aur")
                elif next_touch and not prev_touch:
                    keep_after = False   # the end was stretched up to the next word
                else:
                    keep_after = after >= before
                s, e = (b, e) if keep_after else (s, a)
        if e - s < 0.02:
            e = s + 0.02
        if (r3(s), r3(e)) != (r3(w["s"]), r3(w["e"])):
            w.setdefault("orig", [r3(w["s"]), r3(w["e"])])
            w["s"], w["e"] = r3(s), r3(e)
            n_trim += 1
    return {"in_silence": n_in, "trimmed": n_trim}


# ---------------------------------------------------------------- script alignment
_DEV = {**dict(zip("अआइईउऊऋएऐओऔ", ["a", "aa", "i", "ee", "u", "oo", "ri", "e", "ai", "o", "au"])),
        **dict(zip("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह",
                   ["k", "kh", "g", "gh", "n", "ch", "chh", "j", "jh", "n", "t", "th", "d", "dh", "n", "t", "th", "d",
                    "dh", "n", "p", "f", "b", "bh", "m", "y", "r", "l", "v", "sh", "sh", "s", "h"])),
        **dict(zip("ािीुूृेैोौ", ["a", "i", "ee", "u", "oo", "ri", "e", "ai", "o", "au"])),
        "ं": "n", "ँ": "n", "ः": "h", "़": "", "्": "", "ॅ": "e", "ॉ": "o", "ज़": "z"}


def romanise(word: str) -> str:
    """Crude Devanagari -> Latin, only good enough for fuzzy comparison with romanised Hinglish."""
    out = [_DEV.get(c, c.lower()) for c in word]  # schwa left out on purpose: spelling noise
    return "".join(out)


def _tok(s: str) -> str:
    s = s.lower()
    if re.search(r"[ऀ-ॿ]", s):
        s = romanise(s)
    s = re.sub(r"[^a-z0-9]", "", s)
    return re.sub(r"(.)\1+", r"\1", s)  # collapse doubled letters (aa/ee spelling noise)


def script_tokens(script_text: str) -> list[str]:
    return [t for t in re.findall(r"[\wऀ-ॿ'.+#]+", script_text) if re.search(r"\w", t)]


def clean_script(text: str) -> str:
    """Spoken lines only: the '## Script' section without [stage directions], quotes, rules, headings."""
    if "## Script" in text:
        text = text.split("## Script", 1)[1]
        text = re.split(r"\n## ", text, maxsplit=1)[0]
    lines = [l.strip() for l in text.splitlines()]
    lines = [l for l in lines if l and not l.startswith((">", "---", "#", "- ")) and not re.match(r"^\*\*\[.*\]\*\*$", l)]
    s = " ".join(lines)
    s = re.sub(r"\*\*\[.*?\]\*\*", " ", s)
    return re.sub(r"[*_`]", "", s)


def align_script(words: list[dict], script_text: str, min_ratio: float = 0.75) -> list[str | None]:
    """Per-word suggested caption text from the script (None where there's no confident match).

    Needleman-Wunsch over normalised tokens: Latin words match by string similarity, Devanagari words are compared
    through a rough romanisation and act as positional wildcards (confident only when the neighbours matched).
    Spoken words are never changed here; callers store the result as "caption".
    """
    stoks = script_tokens(script_text)
    sn = [_tok(t) for t in stoks]
    wn = [_tok(w["w"]) for w in words]
    wdev = [script_kind(w["w"]) == "devanagari" for w in words]
    n, m = len(words), len(stoks)
    if n == 0 or m == 0:
        return [None] * n

    def sim(i: int, j: int) -> float:
        if not wn[i] or not sn[j]:
            return 0.0
        return difflib.SequenceMatcher(None, wn[i], sn[j]).ratio()

    GAP = -0.4
    S = np.zeros((n + 1, m + 1), np.float32)
    S[:, 0] = np.arange(n + 1) * GAP
    S[0, :] = np.arange(m + 1) * GAP
    sc = np.zeros((n, m), np.float32)
    for i in range(n):
        for j in range(m):
            r = sim(i, j)
            if wdev[i]:
                sc[i, j] = 0.35 if r < 0.5 else 1.0 * r
            else:
                sc[i, j] = (2.0 * r) if r >= min_ratio else -1.0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i, j] = max(S[i - 1, j - 1] + sc[i - 1, j - 1], S[i - 1, j] + GAP, S[i, j - 1] + GAP)
    pairs: dict[int, int] = {}
    i, j = n, m
    while i > 0 and j > 0:
        if S[i, j] == S[i - 1, j - 1] + sc[i - 1, j - 1]:
            pairs[i - 1] = j - 1
            i, j = i - 1, j - 1
        elif S[i, j] == S[i - 1, j] + GAP:
            i -= 1
        else:
            j -= 1
    solid = {i for i, j in pairs.items() if not wdev[i] and sim(i, j) >= min_ratio}
    out: list[str | None] = [None] * n
    for i, j in pairs.items():
        if i in solid:
            out[i] = stoks[j]
        elif wdev[i]:  # wildcard: need a solid neighbour on both sides and a plausible romanisation
            near = any(k in solid for k in (i - 1, i - 2)) and any(k in solid for k in (i + 1, i + 2))
            adjacent = pairs.get(i - 1) == j - 1 or pairs.get(i + 1) == j + 1
            if near and adjacent and sim(i, j) >= 0.5:
                out[i] = stoks[j]
    return out


# ---------------------------------------------------------------- main
def _prompt(script: str | None, gloss: dict) -> str:
    if script:
        return clean_script(script)[:200].strip()
    return ", ".join(term_list(gloss))


_MODELS: dict = {}


def _load(name: str):
    from faster_whisper import WhisperModel
    return WhisperModel(name, device="cpu", compute_type="int8", cpu_threads=min(os.cpu_count() or 4, 16))


def get_model(name: str):
    if name not in _MODELS:
        tools()  # sets HF_HOME under VEOS_HOME
        try:
            _MODELS[name] = _load(name)
        except Exception as e:  # noqa: BLE001
            raise VeosError("MODEL_UNAVAILABLE", f"could not load {name}: {e}",
                            "Run `veos doctor` to check the speech model is installed (it downloads once, ~1.6 GB).")
    return _MODELS[name]


def load_model(args, warnings: list) -> None:
    """Make sure args.model can be loaded: large-v3 is downloaded on first use; a model that can't be fetched or loaded
    falls back to large-v3-turbo with a warning (a reel never fails on the bigger model)."""
    args.model = speechmodel.ensure(args.model, args.language, warnings)
    if args.model == speechmodel.TURBO:
        return
    try:
        get_model(args.model)
    except VeosError as e:
        warnings.append(f"could not load {args.model} ({e.message}); transcribed with {speechmodel.TURBO}")
        speechmodel.say(f"warning: {warnings[-1]}")
        args.model = speechmodel.TURBO


def transcribe_audio(audio: np.ndarray, *, language: str | None = "hi", prompt: str = "", fast: bool = False,
                     model_name: str = MODEL, silences: list | None = None) -> tuple[list[dict], list, float]:
    """Core: chunked transcription -> (words in source time, silences, wall seconds excluding model load)."""
    model = get_model(model_name)
    silences = find_silences(audio) if silences is None else silences
    pad_s, maxlen = 0.8, (20.0 if fast else 11.0)
    chunks = make_chunks(audio, silences, maxlen)
    pad = np.zeros(int(pad_s * SR), np.float32)
    words: list[dict] = []
    t0 = time.perf_counter()
    for cs, ce in chunks:
        x = np.concatenate([pad, audio[int(cs * SR):int(ce * SR)], pad])
        segs, _ = model.transcribe(x, language=language or None, word_timestamps=True, beam_size=1 if fast else 5,
                                   vad_filter=False, condition_on_previous_text=False,
                                   initial_prompt=prompt or None)
        for sg in segs:
            for wd in sg.words or []:
                s, e = wd.start - pad_s + cs, wd.end - pad_s + cs
                if s >= ce or e <= cs:  # decoded from the padding: hallucination
                    continue
                words.append({"w": wd.word.strip(), "s": max(cs, s), "e": min(ce, e), "p": round(wd.probability, 3)})
    wall = time.perf_counter() - t0
    words = [w for w in words if w["w"]]
    for w in words:  # a word that starts inside a pause really starts when the pause ends
        for s, e in silences:
            if s - 0.01 <= w["s"] <= e + 0.01 and w["e"] > e:
                w["s"] = e
    return words, silences, wall


def process_source(sid: str, wav: Path, args, project=None, glossary: dict | None = None,
                   script_text: str | None = None) -> tuple[dict, dict]:
    gloss = glossary or load_glossary(args.glossary)
    audio = load_audio(wav)
    dur = len(audio) / SR
    prompt = _prompt(script_text, gloss)
    smap = speechmap.build(audio, vad=not getattr(args, "no_vad", False))
    words, silences, wall = transcribe_audio(audio, language=args.language, prompt=prompt, fast=args.fast,
                                             model_name=getattr(args, "model", None) or MODEL,
                                             silences=smap["silences"])
    for w in words:
        w["s"], w["e"] = r3(min(w["s"], dur)), r3(min(w["e"], dur))
        if w["e"] <= w["s"]:
            w["e"] = r3(min(dur, w["s"] + 0.02))
    snapped = snap_onsets(words, audio)
    for w in words:  # keep order sane: a start never before the previous start; ends not past the next start
        w.setdefault("onset_snapped", False)
    for a, b in zip(words, words[1:]):
        if b["s"] < a["s"]:
            b["s"] = a["s"]
        if a["e"] > b["s"] and b["s"] > a["s"]:
            a["e"] = b["s"]
        b["e"] = max(b["e"], r3(b["s"] + 0.02)) if b["e"] <= b["s"] else b["e"]
    cleaned = silence_fix(words, smap["silences"])
    for w in words:
        w["script"] = script_kind(w["w"])
    for i, w in enumerate(words):
        w["i"] = i
    fixes = apply_glossary(words, gloss)
    match_rate = None
    if script_text:
        caps = align_script(words, clean_script(script_text))
        for w, c in zip(words, caps):
            if c:
                w["caption"] = c
        match_rate = round(sum(1 for c in caps if c) / max(1, len(words)), 3)
    ordered = [{"i": w["i"], "w": w["w"], "s": w["s"], "e": w["e"], "p": w["p"], "script": w["script"],
                "onset_snapped": w["onset_snapped"], **({"caption": w["caption"]} if "caption" in w else {}),
                **{k: w[k] for k in ("suspect", "orig") if k in w}}
               for w in words]
    doc = {"version": 1, "source": sid, "model": getattr(args, "model", None) or MODEL, "language": args.language,
           "prompt_used": bool(prompt), "words": ordered, "silences": silences, "speech": smap["speech"],
           "speech_method": smap["method"], "speech_threshold_db": smap["threshold_db"], "glossary_fixes": fixes}
    summary = {"id": sid, "words": len(ordered), "language": args.language, "rtf": round(wall / max(dur, 1e-6), 2),
               "glossary_fixes": len(fixes), "low_confidence": sum(1 for w in ordered if w["p"] < 0.5),
               "onset_snapped": snapped, "duration": r3(dur), "in_silence": cleaned["in_silence"],
               "trimmed_to_speech": cleaned["trimmed"], "speech_map": smap["method"]}
    if match_rate is not None:
        summary["script_match_rate"] = match_rate
    return doc, summary


def resolve_language(args, project) -> str:
    """--language (a code or a name), else the playbook's speech language, else hi; the model likewise. Sets
    args.language / args.language_from / args.model."""
    from . import langs
    tok = langs.playbook_tokens(project)
    if args.language:
        code = langs.whisper_code(args.language) or args.language
        args.language_from = "--language"
    else:
        code, why = langs.speech_language(project, tok)
        args.language_from = why if code else "default hi (no speech language in the playbook)"
        code = code or "hi"
    args.language = code
    args.model, args.model_from = speechmodel.choose(code, getattr(args, "model", None), langs.speech_model(project, tok))
    return code


def main(args, project) -> dict:
    resolve_language(args, project)
    script_text = None
    if args.script:
        sp = Path(args.script)
        if not sp.exists():
            raise VeosError("SCRIPT_MISSING", f"script file not found: {sp}", "Check the --script path.")
        script_text = sp.read_text(encoding="utf-8-sig")
    gloss = load_glossary(args.glossary)
    jobs: list[tuple[str, Path]] = []
    if args.audio:
        a = Path(args.audio)
        if not a.exists():
            raise VeosError("AUDIO_MISSING", f"audio file not found: {a}", "Check the --audio path.")
        jobs.append((args.id or a.stem, a))
    else:
        proj = need_project(project)
        sj = proj.work / "sources.json"
        if not sj.exists():
            raise VeosError("NO_SOURCES", "work/sources.json not found",
                            "Run `veos ingest` and `veos conform` first (or pass --audio FILE --id X).")
        sdoc = read_json(sj)
        ids = [s["id"] for s in sdoc["sources"] if s.get("kind") in (None, "talking-head", "audio-only", "voiceover")]
        if script_text is None and sdoc.get("script"):  # the script stored by `veos ingest --script` (voice-over reels)
            sp = Path(sdoc["script"])
            if sp.exists():
                script_text = sp.read_text(encoding="utf-8-sig")
        if args.id:
            ids = [i for i in ids if i == args.id] or [args.id]
        for sid in ids:
            wav = proj.work / "audio" / f"{sid}.wav"
            if not wav.exists():
                raise VeosError("NO_AUDIO", f"missing {proj.rel(wav)}", "Run `veos conform` first.")
            jobs.append((sid, wav))
    warnings: list = []
    load_model(args, warnings)
    results = []
    for sid, wav in jobs:
        doc, summ = process_source(sid, wav, args, project, gloss, script_text)
        if project is not None:
            out = project.path("work", "words", f"{sid}.json")
            write_json(out, doc)
            summ["file"] = project.rel(out)
            project.log("transcribe", f"{sid}: {summ}")
        elif args.audio:
            out = Path(args.audio).with_suffix(".words.json")
            write_json(out, doc)
            summ["file"] = out.as_posix()
        results.append(summ)
    out = {"sources": results, "language": args.language, "language_from": args.language_from, "model": args.model,
           "model_from": args.model_from}
    if warnings:
        out["warnings"] = warnings
    return out
