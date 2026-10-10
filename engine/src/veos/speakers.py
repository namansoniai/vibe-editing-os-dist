"""`veos speakers`: who speaks when (word -> speaker labels) for multi-speaker sessions.

    veos speakers [--mode auto|mics|diarize] [--num N] [--names "S1=Naman:host,S2=Priya:guest"]
    veos speakers name "S1=Naman:host" "S2=Priya:guest"     (name / re-name the speakers; roles: host, guest, ...)
    veos speakers show

Reads the session master (sources.json `session.master`: MIX after `veos sync`, else the single talking-head source).
Mode `mics` (auto when the session has 2+ mic tracks) uses per-mic voice activity; mode `diarize` runs the local
diarisation models on the master track. Writes:
  work/speakers.json   {mode, master, speakers[{id, name, role, role_guess, mic, talk_s, turns}], turns[], overlaps[],
                        segments{id: [[t0, t1], ...]}, quality}
  `speaker` (+ `spk_conf`, `overlap`, and `role`/`speaker_name` once named) on every word of work/words/<master>.json,
  and on work/words.edit.json when it already exists (so captions pick the colours up without re-cutting).
Times are master-source seconds (= session seconds when the master is MIX).
"""
from __future__ import annotations

import re
import time

import numpy as np

from . import diarize as D
from .core import VeosError, need_project, r3, read_json, write_json
from .cut import seg_speed, src_frames
from .sync import source_audio, to_session

QWORDS = {"what", "how", "why", "when", "who", "which", "where", "do", "does", "did", "is", "are", "can", "could",
          "would", "should", "will", "kya", "kaise", "kyun", "kyon", "kab", "kaun", "kahan", "kitna", "kitne"}


def add_args(p, cmd):
    p.add_argument("action", nargs="?", default="label", choices=["label", "name", "show"])
    p.add_argument("pairs", nargs="*", help="for `name`: S1=Name:role ...")
    p.add_argument("--mode", default="auto", choices=["auto", "mics", "diarize"])
    p.add_argument("--num", type=int, default=None, help="number of people talking (when known)")
    p.add_argument("--names", default=None, help="S1=Name:role,S2=Name:role (same as `name` after labelling)")
    p.add_argument("--master", default=None, help="source id to label (default: the session master)")
    p.add_argument("--step", type=float, default=None, help="diarisation window step in s (default 1.5; 3.0 over 30 min)")


# ======================================================================= helpers
def session_master(sources: dict, data: dict, want: str | None = None) -> str:
    if want:
        if want not in sources:
            raise VeosError("NO_SUCH_ID", f"no source {want}", "See work/sources.json.")
        return want
    m = (data.get("session") or {}).get("master")
    if m and m in sources:
        return m
    th = [s for s in sources.values() if s.get("kind") == "talking-head"]
    if not th:  # a wide two-shot has small faces, so ingest may call it b-roll: a lone video with sound is the source
        th = [s for s in sources.values() if s.get("width") and s.get("audio") and s.get("kind") != "session"]
    if len(th) == 1:
        return th[0]["id"]
    if not th:
        raise VeosError("NO_MASTER", "no talking-head source to label", "Ingest the conversation footage first.")
    raise VeosError("NEEDS_SYNC", f"{len(th)} camera/mic sources but no session master",
                    "Run `veos sync --project P` first so the clips share one timeline.")


def warp_to_master(proj, src: dict, master: dict, sr: int) -> np.ndarray:
    """Source audio resampled onto the master's timeline (via session time)."""
    x = source_audio(proj, src, sr)
    n = int(round((master.get("duration") or 0) * sr)) or len(x)
    ms, ss = master.get("sync") or {"offset": 0.0}, src.get("sync") or {"offset": 0.0}
    out = np.zeros(n, np.float32)
    CH = sr * 60
    for a in range(0, n, CH):
        b = min(n, a + CH)
        t_m = np.arange(a, b) / sr
        t_s = to_session(ms, 0.0) + t_m * (1 + ms.get("drift_ppm", 0.0) * 1e-6)
        pos = ((t_s - ss["offset"]) / (1 + ss.get("drift_ppm", 0.0) * 1e-6)) * sr
        ok = (pos >= 0) & (pos <= len(x) - 1)
        if ok.any():
            out[a:b][ok] = np.interp(pos[ok], np.arange(len(x)), x).astype(np.float32)
    return out


def parse_names(items: list[str]) -> dict:
    """["S1=Naman:host", "S2=Priya"] -> {"S1": {"name": "Naman", "role": "host"}, "S2": {"name": "Priya", "role": None}}"""
    out = {}
    for it in items:
        for part in [x for x in re.split(r",(?=\s*\w+\s*=)", it) if x.strip()]:
            if "=" not in part:
                raise VeosError("BAD_ARG", f"'{part}': use S1=Name:role", "Example: S1=Naman:host S2=Priya:guest")
            k, v = part.split("=", 1)
            name, _, role = v.partition(":")
            out[k.strip()] = {"name": name.strip() or None, "role": (role.strip().lower() or None)}
    return out


def role_guesses(turns: list[dict], words: list[dict], ids: list[str]) -> dict:
    """host = the one who asks (question marks / question openers, per turn), with a nudge for speaking first."""
    if len(ids) < 2:
        return {ids[0]: "host"} if ids else {}
    score = {i: 0.0 for i in ids}
    nturn = {i: 0 for i in ids}
    by_w = sorted(words, key=lambda w: w["s"])
    k = 0
    for t in turns:
        ws = []
        while k < len(by_w) and by_w[k]["s"] < t["t1"]:
            if by_w[k]["s"] >= t["t0"] - 0.05:
                ws.append(by_w[k]["w"])
            k += 1
        if not ws:
            continue
        nturn[t["speaker"]] += 1
        q = ws[-1].strip().endswith("?") or ws[0].strip(".,!?¿").lower() in QWORDS
        score[t["speaker"]] += 1.0 if q else 0.0
    rate = {i: score[i] / max(nturn[i], 1) for i in ids}
    if turns:
        rate[turns[0]["speaker"]] += 0.15
    host = max(ids, key=lambda i: rate[i])
    return {i: ("host" if i == host else "guest") for i in ids}


def _segments(res: dict, ids: list[str]) -> dict:
    hop = res["hop"]
    out = {}
    for k, sid in enumerate(ids):
        a = res["act"][k].astype(int)
        e = np.flatnonzero(np.diff(np.concatenate([[0], a, [0]])) != 0).reshape(-1, 2)
        out[sid] = [[round(x * hop, 2), round(y * hop, 2)] for x, y in e]
    return out


def _overlaps(res: dict, ids: list[str], min_s: float = 0.2) -> list:
    hop = res["hop"]
    ov = res["act"].sum(0) >= 2
    e = np.flatnonzero(np.diff(np.concatenate([[0], ov.astype(int), [0]])) != 0).reshape(-1, 2)
    out = []
    for a, b in e:
        if (b - a) * hop >= min_s:
            who = [ids[k] for k in range(len(ids)) if res["act"][k, a:b].any()]
            out.append([round(a * hop, 2), round(b * hop, 2), who])
    return out


def apply_cast(words: list[dict], cast: dict) -> None:
    for w in words:
        c = cast.get(w.get("speaker"))
        if c:
            if c.get("role"):
                w["role"] = c["role"]
            if c.get("name"):
                w["speaker_name"] = c["name"]


def _patch_edit_words(proj, master: str, src_words: list[dict], cast: dict) -> int:
    p = proj.work / "words.edit.json"
    if not p.exists():
        return 0
    doc = read_json(p)
    cm = proj.work / "cutmap.json"
    segs = read_json(cm)["segments"] if cm.exists() else []
    by_i = {w["i"]: w for w in src_words}
    n = 0
    for w in doc.get("words", []):
        if w.get("src") != master or w.get("si") not in by_i:
            continue
        sw = by_i[w["si"]]
        if sw.get("onset_from") == "speaker" and segs:   # carry the voice-onset start fix into edit time
            for sg in segs:
                lo = sg["in_frame"] / 30.0
                if sg["src"] == master and lo <= sw["s"] < lo + src_frames(sg) / 30.0:
                    w["s"] = round(sg["t0"] + (sw["s"] - lo) / seg_speed(sg), 3)
                    w["onset_from"] = "speaker"
                    break
        for k in ("speaker", "spk_conf", "overlap", "role", "speaker_name"):
            if k in sw:
                w[k] = sw[k]
            else:
                w.pop(k, None)
        n += 1
    write_json(p, doc)
    return n


# ======================================================================= actions
def _label(args, proj) -> dict:
    sp = proj.work / "sources.json"
    if not sp.exists():
        raise VeosError("NO_SOURCES", "work/sources.json not found", "Run `veos ingest` (and `veos sync`) first.")
    data = read_json(sp)
    sources = {s["id"]: s for s in data["sources"]}
    master_id = session_master(sources, data, args.master)
    master = sources[master_id]
    sess = data.get("session") or {}
    mics = [m for m in sess.get("mics", []) if m in sources]
    mode = args.mode
    if mode == "auto":
        mode = "mics" if len(mics) >= 2 else "diarize"
    if mode == "mics" and len(mics) < 2:
        raise VeosError("NO_MICS", "mode mics needs 2+ synced mic tracks",
                        "Pass the mic files to `veos ingest`, then `veos sync --mics ID,ID`; or use --mode diarize.")
    cast_in = parse_names([args.names]) if args.names else {}
    num = args.num or (len(cast_in) if cast_in else None)
    t0 = time.time()
    warnings = []
    dur = float(master.get("duration") or 0)
    if mode == "mics":
        tracks = [warp_to_master(proj, sources[m], master, 16000) for m in mics]
        res = D.mic_activity(tracks, 16000)
        ids = [f"S{k + 1}" for k in range(len(mics))]
        mic_of = dict(zip(ids, mics))
    else:
        if not D.models_present():
            D.model_paths(fetch=True)   # one-time ~34 MB download; raises MODEL_MISSING with a hint on failure
        audio = source_audio(proj, master, 16000)
        dur = len(audio) / 16000
        step = args.step or (3.0 if dur > 1800 else 1.5)
        res = D.diarize(audio, num_speakers=num, step_s=step)
        # order speakers by first appearance
        first = [int(np.argmax(res["act"][k])) if res["act"][k].any() else 10 ** 9 for k in range(res["act"].shape[0])]
        order = np.argsort(first)
        res = {**res, "act": res["act"][order], "score": res["score"][order]}
        ids = [f"S{k + 1}" for k in range(len(order))]
        mic_of = {}
        q = res["quality"]
        if num and q.get("speakers", 0) < num:
            warnings.append(f"found {q.get('speakers')} voice(s) but {num} people were expected")
        if q.get("centroid_similarity") is not None and q["centroid_similarity"] >= 0.6:
            warnings.append("the voices sound very alike, so voice-only labels are unreliable here; per-person mic "
                            "tracks fix this (pass them to `veos ingest` + `veos sync`), else check who-is-who on the storyboard")
            res.setdefault("quality", {})["reliable"] = False
    turns = D.turns_from(res, ids)
    wpath = proj.work / "words" / f"{master_id}.json"
    words_doc = read_json(wpath) if wpath.exists() else None
    wstats = None
    if words_doc:
        wstats = D.label_words(words_doc["words"], res, ids)
    else:
        warnings.append(f"no transcript for {master_id} yet: speaker turns saved; run `veos transcribe --id {master_id}` "
                        "and then `veos speakers` again to label the words")
    guesses = role_guesses(turns, words_doc["words"] if words_doc else [], ids)
    old = read_json(proj.work / "speakers.json") if (proj.work / "speakers.json").exists() else {}
    old_cast = {s["id"]: {"name": s.get("name"), "role": s.get("role")} for s in old.get("speakers", [])
                if old.get("mode") == mode and len(old.get("speakers", [])) == len(ids)}
    cast = {**old_cast, **cast_in}
    hop = res["hop"]
    spk = []
    for k, sid in enumerate(ids):
        talk = float(res["act"][k].sum()) * hop
        c = cast.get(sid, {})
        spk.append({"id": sid, "name": c.get("name"), "role": c.get("role"), "role_guess": guesses.get(sid),
                    **({"mic": mic_of[sid]} if sid in mic_of else {}), "talk_s": round(talk, 1),
                    "turns": sum(1 for t in turns if t["speaker"] == sid)})
    if words_doc:
        apply_cast(words_doc["words"], {s["id"]: {"name": s["name"], "role": s["role"]} for s in spk})
        words_doc["speakers"] = {"mode": mode, "ids": ids, "file": "work/speakers.json"}
        write_json(wpath, words_doc)
    doc = {"version": 1, "mode": mode, "master": master_id, "hop": hop, "duration": r3(dur),
           "speakers": spk, "turns": turns, "overlaps": _overlaps(res, ids), "segments": _segments(res, ids),
           "quality": res.get("quality", {}), "words": wstats, "seconds": round(time.time() - t0, 1)}
    write_json(proj.path("work", "speakers.json"), doc)
    patched = _patch_edit_words(proj, master_id, words_doc["words"], {}) if words_doc else 0
    if patched:
        from .shots import write_words_json
        write_words_json(proj)
    proj.log("speakers", f"{mode}: {len(ids)} speakers, {len(turns)} turns, {doc['seconds']}s")
    return {"mode": mode, "master": master_id, "speakers": [{k: s[k] for k in ("id", "name", "role", "role_guess",
                                                                                 "talk_s", "turns") if s.get(k) is not None}
                                                            for s in spk],
            "turns": len(turns), "overlap_s": round(sum(o[1] - o[0] for o in doc["overlaps"]), 1),
            "words": wstats, "edit_words_patched": patched, "quality": doc["quality"] if mode == "diarize" else None,
            "file": "work/speakers.json", "warnings": warnings}


def _name(args, proj) -> dict:
    p = proj.work / "speakers.json"
    if not p.exists():
        raise VeosError("NO_SPEAKERS", "work/speakers.json not found", "Run `veos speakers` first.")
    doc = read_json(p)
    cast = parse_names(args.pairs + ([args.names] if args.names else []))
    known = {s["id"] for s in doc["speakers"]}
    bad = sorted(set(cast) - known)
    if bad:
        raise VeosError("NO_SUCH_SPEAKER", f"unknown speaker id(s) {', '.join(bad)}", f"Known: {', '.join(sorted(known))}.")
    for s in doc["speakers"]:
        if s["id"] in cast:
            s["name"] = cast[s["id"]]["name"] or s.get("name")
            s["role"] = cast[s["id"]]["role"] or s.get("role")
    write_json(p, doc)
    full = {s["id"]: {"name": s.get("name"), "role": s.get("role")} for s in doc["speakers"]}
    wpath = proj.work / "words" / f"{doc['master']}.json"
    patched = 0
    if wpath.exists():
        wd = read_json(wpath)
        apply_cast(wd["words"], full)
        write_json(wpath, wd)
        patched = _patch_edit_words(proj, doc["master"], wd["words"], full)
        if patched:
            from .shots import write_words_json
            write_words_json(proj)
    return {"speakers": [{k: s.get(k) for k in ("id", "name", "role")} for s in doc["speakers"]],
            "edit_words_patched": patched}


def _show(args, proj) -> dict:
    p = proj.work / "speakers.json"
    if not p.exists():
        raise VeosError("NO_SPEAKERS", "work/speakers.json not found", "Run `veos speakers` first.")
    doc = read_json(p)
    return {"mode": doc["mode"], "master": doc["master"], "speakers": doc["speakers"], "turns": len(doc["turns"]),
            "first_turns": doc["turns"][:8]}


def main(args, project) -> dict:
    proj = need_project(project)
    return {"label": _label, "name": _name, "show": _show}[args.action](args, proj)
