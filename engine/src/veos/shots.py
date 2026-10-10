"""`veos shots`: multi-camera / multi-speaker shot planning and composition for shorts (E-13, E-13b).

    veos shots mine   [--min 60 --max 150]   candidate 60-150 s clips (self-contained Q&A arcs) in a long recording
    veos shots plan   [--apply] [--no-stack] [--seam Y]   turn-rule generator -> plan/shots.json (+ timeline.shots)
    veos shots render [--fallback blurfill|letterbox]      compositor -> work/multicam/footage.mp4 (+ face, compose.json)
    veos shots check                                       V-SPEAKER on the timeline -> plan/dialogue.check.json

`plan` needs work/cutmap.json, work/words.edit.json with speaker labels (`veos speakers` before or after `veos cut`)
and work/angles.json. It also writes **work/words.json**, the caption engine's input: the edit-time words with
`speaker` (+ `role`, `speaker_name`, `overlap`) and the cast `{id: {name, role}}`.
Shots live in `timeline.shots[]` (edit time); see turnrules.py for the fields. A `stack` shot uses the layout
primitive's field names: `seam_y`, `top`/`bottom` = "source:<angle id>", `hairline`.
"""
from __future__ import annotations

import time

from . import compose, turnrules
from .core import SIZE, VeosError, need_project, r3, read_json, write_json
from .cut import seg_speed, src_frames
from .dialoguerules import DialogueCtx, rule_speaker
from .speakers import QWORDS


def add_args(p, cmd):
    p.add_argument("action", choices=["mine", "plan", "render", "check"])
    p.add_argument("--apply", action="store_true", help="plan: also write the shots into plan/timeline.json")
    p.add_argument("--no-stack", action="store_true", help="plan: never use the 50/50 stack")
    p.add_argument("--seam", type=int, default=None, help="plan: stack seam y in px (default 960)")
    p.add_argument("--fallback", default=None, choices=["blurfill", "letterbox"],
                   help="render: how uncroppable shots are shown (default: tokens dialogue.fallback, else blurfill)")
    p.add_argument("--min", type=float, default=60.0, help="mine: shortest clip (s)")
    p.add_argument("--max", type=float, default=150.0, help="mine: longest clip (s)")


# ======================================================================= tokens
def dialogue_tokens(proj) -> dict:
    """`dialogue` / `captions` / `camera` blocks: work/tokens.json (resolved) over the raw playbook tokens."""
    out: dict = {}
    try:
        from .tokens import load_playbook, project_playbook
        raw = load_playbook(project_playbook(proj))
        out.update({k: raw[k] for k in ("dialogue", "captions", "camera", "type") if k in raw})
    except Exception:  # noqa: BLE001 - no playbook: defaults
        pass
    tp = proj.work / "tokens.json"
    if tp.exists():
        res = read_json(tp)
        out.update({k: res[k] for k in ("dialogue", "captions", "camera", "type") if res.get(k)})
    return out


# ======================================================================= words.json (caption engine input)
def write_words_json(proj) -> dict | None:
    p = proj.work / "words.edit.json"
    if not p.exists():
        return None
    doc = read_json(p)
    sp = proj.work / "speakers.json"
    cast = {}
    if sp.exists():
        cast = {s["id"]: {"name": s.get("name"), "role": s.get("role") or s.get("role_guess"),
                          "role_guess": s.get("role_guess")} for s in read_json(sp)["speakers"]}
    keep = ("i", "w", "s", "e", "p", "src", "si", "caption", "script", "speaker", "role", "speaker_name", "overlap",
            "spk_conf")
    words = [{k: w[k] for k in keep if k in w} for w in doc.get("words", [])]
    out = {"version": 1, "time": "edit", "source": "work/words.edit.json + work/speakers.json", "cast": cast,
           "speakers": sorted({w["speaker"] for w in words if w.get("speaker")}), "words": words}
    write_json(proj.path("work", "words.json"), out)
    return {"file": "work/words.json", "words": len(words), "labelled": sum(1 for w in words if w.get("speaker"))}


# ======================================================================= actions
def _mine(args, proj) -> dict:
    """Candidate clips: start on a turn start (preferably a question by the asker), end on the end of an answer turn,
    duration in [min, max]; scored by question start, complete answer, few dead seconds, 2+ speakers."""
    sp = proj.work / "speakers.json"
    if not sp.exists():
        raise VeosError("NO_SPEAKERS", "work/speakers.json not found", "Run `veos speakers` first.")
    spk = read_json(sp)
    wp = proj.work / "words" / f"{spk['master']}.json"
    words = read_json(wp)["words"] if wp.exists() else []
    floor, _ = turnrules.turns(words)
    if not floor:
        raise VeosError("NO_WORDS", "no labelled words to mine", f"Run `veos transcribe --id {spk['master']}` and `veos speakers`.")
    cand = []
    for i, a in enumerate(floor):
        first = a["words"][0]["w"].strip(".,!?¿").lower()
        q_start = a["words"][-1]["w"].strip().endswith("?") or first in QWORDS
        for j in range(i + 1, len(floor)):
            b = floor[j]
            d = b["t1"] - a["t0"]
            if d > args.max:
                break
            if d < args.min:
                continue
            spoken = sum(w["e"] - w["s"] for t in floor[i:j + 1] for w in t["words"])
            whos = {t["speaker"] for t in floor[i:j + 1]}
            ends_answer = b["speaker"] != a["speaker"] and (b["t1"] - b["t0"]) >= 6.0
            score = (2.0 if q_start else 0) + (1.5 if ends_answer else 0) + 2.0 * spoken / d + (1.0 if len(whos) >= 2 else 0)
            text = " ".join(w["w"] for w in a["words"][:14])
            cand.append({"t0": r3(max(0.0, a["t0"] - 0.15)), "t1": r3(b["t1"] + 0.25), "dur": round(d, 1),
                         "score": round(score, 2), "turns": j - i + 1, "starts_with": a["speaker"], "opening": text,
                         "ending": " ".join(w["w"] for w in b["words"][-10:])})
    cand.sort(key=lambda c: -c["score"])
    picked = []
    for c in cand:  # non-overlapping best
        if all(c["t1"] <= p["t0"] or c["t0"] >= p["t1"] for p in picked):
            picked.append(c)
        if len(picked) >= 8:
            break
    write_json(proj.path("plan", "clip_candidates.json"), {"version": 1, "master": spk["master"], "candidates": picked})
    return {"master": spk["master"], "candidates": picked[:5], "file": "plan/clip_candidates.json"}


def _edit_onsets(proj, cm: dict) -> dict:
    """Voice onsets per speaker (work/speakers.json segment starts, master time) mapped to edit time."""
    sp = proj.work / "speakers.json"
    if not sp.exists():
        return {}
    out: dict = {}
    for sid, segs in read_json(sp).get("segments", {}).items():
        for a, _ in segs:
            for s in cm["segments"]:
                lo = s["in_frame"] / 30.0
                if lo <= a < lo + src_frames(s) / 30.0:
                    out.setdefault(sid, []).append(round(s["t0"] + (a - lo) / seg_speed(s), 3))
    return out


def _plan(args, proj) -> dict:
    for f in ("cutmap.json", "words.edit.json", "angles.json"):
        if not (proj.work / f).exists():
            raise VeosError("MISSING_INPUT", f"work/{f} not found",
                            {"cutmap.json": "Run `veos cut` first.", "words.edit.json": "Run `veos transcribe` and `veos cut`.",
                             "angles.json": "Run `veos angles` first."}[f])
    cm = read_json(proj.work / "cutmap.json")
    words = read_json(proj.work / "words.edit.json")["words"]
    if not any(w.get("speaker") for w in words):
        raise VeosError("NO_SPEAKER_LABELS", "the edit's words carry no speaker labels",
                        "Run `veos speakers` (it updates work/words.edit.json), then plan again.")
    ang = read_json(proj.work / "angles.json")
    tok = dialogue_tokens(proj)
    cfg = turnrules.config(tok)
    if args.no_stack:
        cfg["stack"] = False
    if args.seam:
        cfg["seam_y"] = args.seam
    shots = turnrules.generate(words, ang["preferred"], cm["duration"], cfg, onsets=_edit_onsets(proj, cm))
    if not shots:
        raise VeosError("NO_SHOTS", "no speech in the edit to plan shots from", "Check the rough cut.")
    kinds = {a["id"]: a["kind"] for a in ang["angles"]}
    for s in shots:
        if s["layout"] == "full":
            s["angle_kind"] = kinds.get(s["angle"])
    st = turnrules.stats(shots)
    doc = {"version": 1, "canvas": list(SIZE), "rules": cfg, "stats": st, "shots": shots}
    write_json(proj.path("plan", "shots.json"), doc)
    ww = write_words_json(proj)
    applied = False
    tlp = proj.root / "plan" / "timeline.json"
    if args.apply or tlp.exists():
        tl = read_json(tlp) if tlp.exists() else {"version": 2, "meta": {"size": list(SIZE), "fps": 30,
                                                                          "duration": cm["duration"], "frames": cm["frames"]}}
        tl["shots"] = shots
        write_json(tlp, tl)
        applied = True
    fails = rule_speaker(DialogueCtx({"shots": shots}, words, tok), {})
    return {"shots": st["shots"], "stats": st, "file": "plan/shots.json", "timeline_updated": applied, "words_json": ww,
            "v_speaker": [f"{f['check']} @{f['t']}: {f['msg']}" for f in fails][:6], "warnings": []}


def _shots_of(proj) -> list[dict]:
    tlp = proj.root / "plan" / "timeline.json"
    if tlp.exists():
        tl = read_json(tlp)
        if tl.get("shots"):
            return tl["shots"]
    sp = proj.root / "plan" / "shots.json"
    if sp.exists():
        return read_json(sp)["shots"]
    raise VeosError("NO_SHOTS", "no shots in plan/timeline.json or plan/shots.json", "Run `veos shots plan` first.")


def _render(args, proj) -> dict:
    shots = _shots_of(proj)
    tok = dialogue_tokens(proj)
    fb = args.fallback or (tok.get("dialogue") or {}).get("fallback") or "blurfill"
    t0 = time.time()
    res = compose.render(proj, shots, SIZE, fallback=fb, blur_dim=compose.blur_dim_of(tok),
                         progress=lambda f: proj.log("shots", f"render {f:.0%}"))
    write_words_json(proj)
    proj.log("shots", f"render: {res} in {time.time() - t0:.1f}s")
    return {**res, "footage": "work/multicam/footage.mp4", "compose": "work/multicam/compose.json",
            "next": "veos prep-frames uses the composed footage", "seconds": round(time.time() - t0, 1)}


def _check(args, proj) -> dict:
    tlp = proj.root / "plan" / "timeline.json"
    tl = read_json(tlp) if tlp.exists() else {"shots": _shots_of(proj)}
    if not tl.get("shots"):
        tl["shots"] = _shots_of(proj)
    wp = proj.work / "words.edit.json"
    words = read_json(wp)["words"] if wp.exists() else []
    fails = rule_speaker(DialogueCtx(tl, words, dialogue_tokens(proj)), {})
    out = {"passed": not fails, "failures": fails}
    write_json(proj.path("plan", "dialogue.check.json"), out)
    return {"passed": not fails, "failures": fails[:12], "file": "plan/dialogue.check.json"}


def main(args, project) -> dict:
    proj = need_project(project)
    return {"mine": _mine, "plan": _plan, "render": _render, "check": _check}[args.action](args, proj)
