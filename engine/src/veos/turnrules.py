"""Turn-rule generator for multi-speaker shorts (30-150 s conversation clips; Hormozi-style grammar, structure §20/§9.3).

Input: edit-time words with `speaker`, the angle registry's preferred angles, the clip duration and the playbook's
dialogue cut rules. Output: `shots[]` (edit time) that pick the source and crop per span:

  {"t0", "t1", "layout": "full", "angle": "<angle id>", "subject": "S1", "step": 1.0, "speaker": "S1",
   "cut_reason": "open|handover|reaction|recrop|stack"}
  {"t0", "t1", "layout": "stack", "seam_y": 960, "top": "source:<angle id>", "bottom": "source:<angle id>",
   "top_subject": "S1", "bottom_subject": "S2", "hairline": 0, "speaker": "S1", "cut_reason": ...}

Rules (defaults from the Hormozi analysis; every number is a playbook token under `dialogue.cut_rules`):
  R-SPK   cut on the first word of a new speaker (`handover_tol_f` 3 frames), never inside a word;
  R-OPEN  the clip opens on the 50/50 stack (asker + answerer) for `open_s` (≈ 2.7-4.4 s observed);
  R-HOLD  no shot holds longer than `max_hold_s` (4 s; the stack may hold `stack_max_s` 8 s): a long turn rotates
          speaker single -> stack (speaker top, listener bottom) -> listener reaction -> jump re-crop -> ...;
  R-REACT listener cutaway `reaction_s` (1.5-3 s), never in the first 1 s of a turn or the last 1 s before a handover;
          a listener back-channel ("yeah", "haan") inside the speaker's turn is shown as a reaction on that person;
  R-JZ    jump re-crop on the same angle (x1.25) instead of a hard repeat;
  R-TOP   a stack puts the speaker on top; with `dialogue.stack.top: "host"` the host (the speaker whose words carry
          role "host") stays on top whoever talks, the other person below;
  stack share aims at `stack_share` (≈ 35%); identical framings are never cut together.
Overlapping speech: words carry the dominant speaker, so the cut follows the dominant speaker.
Deterministic (no randomness): the rotation is driven by position in the turn and a running counter.
"""
from __future__ import annotations

from .diarize import is_backchannel

DEFAULTS = {"handover_tol_f": 3, "lead_f": 1, "open_s": [2.7, 4.4], "max_hold_s": 4.0, "stack_max_s": 8.0,
            "reaction_s": [1.5, 3.0], "recrop_step": 1.25, "stack_share": 0.35, "min_shot_s": 0.8,
            "stack": True, "seam_y": 960, "hairline": 0, "backchannel_max_s": 1.6, "stack_top": "speaker"}
FPS = 30


def config(tokens: dict | None) -> dict:
    """Merge playbook tokens (`dialogue.cut_rules`, `dialogue.stack`) over the defaults."""
    cfg = dict(DEFAULTS)
    d = (tokens or {}).get("dialogue") or {}
    cr = d.get("cut_rules") or {}
    for k in DEFAULTS:
        if k in cr:
            cfg[k] = cr[k]
    if "reaction_s" in cr:
        cfg["reaction_s"] = list(cr["reaction_s"])
    st = d.get("stack")
    if st is False:
        cfg["stack"] = False
    elif isinstance(st, dict):
        cfg["seam_y"] = st.get("seam_y", cfg["seam_y"])
        cfg["hairline"] = st.get("hairline", cfg["hairline"])
        cfg["stack_share"] = st.get("share", cfg["stack_share"])
        if str(st.get("top") or "").lower() == "host":
            cfg["stack_top"] = "host"
    return cfg


# ======================================================================= turns
def turns(words: list[dict], bc_max_s: float = 1.6) -> tuple[list[dict], list[dict]]:
    """-> (floor turns [{speaker, t0, t1, words}], back-channels [{speaker, t0, t1}]) from labelled edit-time words.
    A short back-channel by the listener in the middle of the other's turn does not take the floor."""
    ws = [w for w in sorted(words, key=lambda w: w["s"]) if w.get("speaker")]
    runs: list[dict] = []
    for w in ws:
        if runs and runs[-1]["speaker"] == w["speaker"]:
            runs[-1]["t1"] = w["e"]
            runs[-1]["words"].append(w)
        else:
            runs.append({"speaker": w["speaker"], "t0": w["s"], "t1": w["e"], "words": [w]})
    floor, bcs = [], []
    for i, r in enumerate(runs):
        prev = floor[-1] if floor else None
        nxt = runs[i + 1] if i + 1 < len(runs) else None
        short = is_backchannel([w["w"] for w in r["words"]], r["t1"] - r["t0"]) or \
            (r["t1"] - r["t0"] <= min(bc_max_s, 1.0) and len(r["words"]) <= 2)
        if prev and nxt and short and prev["speaker"] == nxt["speaker"] != r["speaker"]:
            bcs.append({"speaker": r["speaker"], "t0": r["t0"], "t1": r["t1"]})
            continue
        if prev and prev["speaker"] == r["speaker"]:
            prev["t1"] = r["t1"]
            prev["words"] += r["words"]
        else:
            floor.append(dict(r, words=list(r["words"])))
    return floor, bcs


def snap(t: float, words: list[dict], lo: float, hi: float) -> float:
    """Nearest legal cut time in [lo, hi]: a word onset or a point inside a pause, never inside a word."""
    best, bd = None, 1e9
    for w in words:
        for c in (w["s"],):
            if lo <= c <= hi and abs(c - t) < bd:
                best, bd = c, abs(c - t)
    for a, b in zip(words, words[1:]):
        if b["s"] - a["e"] > 0.06:
            c = min(max(t, a["e"] + 0.02), b["s"])
            if lo <= c <= hi and abs(c - t) < bd:
                best, bd = c, abs(c - t)
    inside = any(w["s"] + 1e-3 < t < w["e"] - 1e-3 for w in words)
    if best is None:
        return t if not inside else lo
    return best


def _fr(t: float) -> float:
    return round(round(t * FPS) / FPS, 4)


# ======================================================================= generator
def generate(words: list[dict], pref: dict, duration: float, cfg: dict | None = None,
             onsets: dict | None = None) -> list[dict]:
    """`onsets` {speaker: [edit-time voice onsets]} (from work/speakers.json): a handover cut may land on the new
    speaker's voice onset in the pause before their first transcribed word (ASR sometimes drops the first words)."""
    cfg = cfg or dict(DEFAULTS)
    onsets = onsets or {}
    floor, bcs = turns(words, cfg["backchannel_max_s"])
    spk = pref.get("speakers", {})
    people = [s for s in spk if spk[s].get("single")]
    two = pref.get("two_shot")
    if not floor:
        return []

    def single(s):
        a = (spk.get(s) or {}).get("single")
        return a or two or pref.get("wide")

    def other(s):
        cands = [p for p in people if p != s]
        return cands[0] if cands else None

    can_stack = cfg["stack"] and len(people) >= 2
    hosts = [p for p in people if any(w.get("speaker") == p and str(w.get("role") or "").lower() == "host" for w in words)]
    host = hosts[0] if cfg.get("stack_top") == "host" and len(hosts) == 1 else None
    lead = cfg["lead_f"] / FPS
    # floor segments: the cut lands on the new speaker's first word (minus a lead of `lead_f` frames)
    segs = []
    for i, t in enumerate(floor):
        a = 0.0 if i == 0 else max(t["t0"] - lead, floor[i - 1]["words"][-1]["e"])
        if i > 0:
            pe = floor[i - 1]["words"][-1]["e"]
            early = [o for o in onsets.get(t["speaker"], []) if pe + 0.25 <= o < t["t0"] - 0.2 and t["t0"] - o <= 1.0]
            if early:
                a = max(pe, min(early) - lead)
        segs.append({"speaker": t["speaker"], "t0": _fr(a), "words": t["words"]})
    for i, s in enumerate(segs):
        s["t1"] = segs[i + 1]["t0"] if i + 1 < len(segs) else _fr(duration)
    all_words = sorted(words, key=lambda w: w["s"])
    shots: list[dict] = []
    stack_time = 0.0
    k = 0                                    # rotation counter across the clip

    def add(shot):
        nonlocal stack_time
        if shot["t1"] - shot["t0"] < 1e-3:
            return
        if shots and _same(shots[-1], shot):
            shots[-1]["t1"] = shot["t1"]
        else:
            shots.append(shot)
        if shot["layout"] == "stack":
            stack_time += shot["t1"] - shot["t0"]

    def full(s, t0, t1, reason, step=1.0, speaker=None):
        return {"t0": t0, "t1": t1, "layout": "full", "angle": single(s), "subject": s, "step": step,
                "speaker": speaker or s, "cut_reason": reason}

    def stack(s, o, t0, t1, reason):
        speaker = s
        if host is not None and o == host:  # R-TOP host: the host on top, the speaker below
            s, o = o, s
        return {"t0": t0, "t1": t1, "layout": "stack", "seam_y": cfg["seam_y"], "hairline": cfg["hairline"],
                "top": f"source:{single(s)}", "bottom": f"source:{single(o)}", "top_subject": s, "bottom_subject": o,
                "speaker": speaker, "cut_reason": reason}

    for si, sg in enumerate(segs):
        s, o = sg["speaker"], other(sg["speaker"])
        t, end = sg["t0"], sg["t1"]
        reason = "open" if si == 0 else "handover"
        seg_bcs = [b for b in bcs if t < b["t0"] < end and b["speaker"] != s]
        # opener: the stack
        if si == 0 and can_stack and o:
            ot = min(end, cfg["open_s"][1])
            if ot - t >= cfg["open_s"][0] or ot >= end:
                cut = _fr(snap(min(end, (cfg["open_s"][0] + cfg["open_s"][1]) / 2), all_words, t + cfg["open_s"][0], ot)) if ot < end else end
                add(stack(s, o, t, cut, "open"))
                t, reason = cut, "recrop"
        while end - t > 1e-3:
            remain = end - t
            # a listener back-channel coming up: show the speaker until it, then the reaction on the back-channeler
            bc = next((b for b in seg_bcs if b["t0"] >= t + cfg["min_shot_s"] and b["t0"] < end - cfg["min_shot_s"]), None)
            if bc and bc["t0"] - t <= cfg["max_hold_s"]:
                c0 = _fr(snap(bc["t0"], all_words, t + cfg["min_shot_s"], bc["t0"] + 0.5))
                c1 = _fr(snap(max(bc["t1"] + 0.6, c0 + cfg["reaction_s"][0]), all_words, c0 + cfg["min_shot_s"],
                              min(end - 1.0, c0 + cfg["reaction_s"][1])))
                if c1 - c0 >= cfg["min_shot_s"] and end - c1 >= cfg["min_shot_s"]:
                    add(full(s, t, c0, reason))
                    add(full(bc["speaker"], c0, c1, "reaction", speaker=s))
                    seg_bcs.remove(bc)
                    t, reason, k = c1, "recrop", k + 1
                    continue
                seg_bcs.remove(bc)
            if remain <= cfg["max_hold_s"] + cfg["min_shot_s"]:
                prev_same = bool(shots) and shots[-1]["layout"] == "full" and shots[-1].get("subject") == s                     and shots[-1].get("step", 1.0) == 1.0
                add(full(s, t, end, reason, step=cfg["recrop_step"] if prev_same else 1.0))
                break
            phase = k % 4
            want_stack = can_stack and o and stack_time < cfg["stack_share"] * max(t, 1.0) + 2.0
            if phase == 1 and want_stack and remain >= 4.0:
                L = min(cfg["stack_max_s"], max(3.0, remain * 0.45))
                c = _fr(snap(t + L, all_words, t + 3.0, min(end - cfg["min_shot_s"], t + cfg["stack_max_s"])))
                add(stack(s, o, t, c, "stack"))
            elif phase == 2 and o and t - sg["t0"] >= 1.0 and end - t >= cfg["reaction_s"][0] + 1.0 + cfg["min_shot_s"]:
                L = min(cfg["reaction_s"][1], max(cfg["reaction_s"][0], (end - t - 1.0) * 0.3))
                c = _fr(snap(t + L, all_words, t + cfg["reaction_s"][0], min(t + cfg["reaction_s"][1], end - 1.0)))
                add(full(o, t, c, "reaction", speaker=s))
            else:
                step = cfg["recrop_step"] if (shots and shots[-1].get("subject") == s and shots[-1]["layout"] == "full"
                                              and shots[-1].get("step", 1.0) == 1.0) else 1.0
                L = min(cfg["max_hold_s"], max(2.0, remain / 2))
                c = _fr(snap(t + L, all_words, t + cfg["min_shot_s"] + 0.6, min(t + cfg["max_hold_s"], end - cfg["min_shot_s"])))
                add(full(s, t, c, reason, step=step))
            t, reason, k = c, "recrop", k + 1
    return _tidy(shots, cfg)


def _same(a: dict, b: dict) -> bool:
    if a["layout"] != b["layout"]:
        return False
    if a["layout"] == "stack":
        return a["top"] == b["top"] and a["bottom"] == b["bottom"]
    return a["angle"] == b["angle"] and a.get("step", 1.0) == b.get("step", 1.0)


def _tidy(shots: list[dict], cfg: dict) -> list[dict]:
    """Merge too-short shots into their neighbour and identical neighbours; round to frames."""
    out: list[dict] = []
    for s in shots:
        s = dict(s, t0=_fr(s["t0"]), t1=_fr(s["t1"]))
        if s["t1"] <= s["t0"]:
            continue
        if out and (_same(out[-1], s) or (s["t1"] - s["t0"] < cfg["min_shot_s"] and s["cut_reason"] != "handover")):
            out[-1]["t1"] = s["t1"]
            continue
        out.append(s)
    for a, b in zip(out, out[1:]):
        b["t0"] = a["t1"]
    return out


def stats(shots: list[dict]) -> dict:
    dur = sum(s["t1"] - s["t0"] for s in shots) or 1.0
    lens = sorted(s["t1"] - s["t0"] for s in shots)
    by = {}
    for s in shots:
        by[s["cut_reason"]] = by.get(s["cut_reason"], 0) + 1
    return {"shots": len(shots), "stack_share": round(sum(s["t1"] - s["t0"] for s in shots if s["layout"] == "stack") / dur, 2),
            "median_s": round(lens[len(lens) // 2], 2) if lens else 0, "longest_s": round(lens[-1], 2) if lens else 0,
            "reasons": by}
