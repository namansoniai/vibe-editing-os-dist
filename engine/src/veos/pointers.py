"""Verbal pointing: moments where the speaker points with words ("this, this and this", "from this to this",
"like this", "ye dekho") and so means for the viewer to SEE something.

Runs inside `veos inserts scan` (plan/inserts.scan.json -> `pointers`). The reel-inputs skill asks the creator what each
moment should show (with a suggested picture), and the planner depicts every moment: the creator's answer, or, with no
answer, the most likely referent inferred from the sentence and the reel's topic. `veos validate` gives advice (V-POINT)
when a pointing moment has nothing but words on screen.

Deliberately conservative (a pointer word is ordinary grammar most of the time). A word counts only when it stands
alone (punctuation, a breath, a connector like "and" / "to" / "aur", or another pointer after it: a pronoun pointing
at something, not a determiner as in "this week" or "at this point") and:
  * it repeats within a few words ("this, this and this", "ye, ye aur ye"; the moment spans every repeat);
  * or it follows from / to / like / see / at / into ("from this to this", "like this");
  * or "this / these / here" ends a clause (punctuation or a pause of PAUSE_S after it);
or when a look-word sits next to it, even before a noun ("look at this graph", "check this out", "watch this",
"ye dekho", "isko dekho", "dekho yahan").
Hits closer than MERGE_S merge into one moment. Pure function of the edit-time words.

POINTER FORMAT: {"id": "P1", "t0", "t1", "phrase", "context", "why": ["repeat"|"lead"|"look"|"clause_end", ...]}
"""
from __future__ import annotations

import re

POINT_EN = {"this", "these", "that", "those", "here"}
POINT_HI = {"ye", "yeh", "yah", "yeh", "isko", "isse", "inko", "aisa", "aise", "aisi", "yahan", "yaha", "idhar"}
POINTS = POINT_EN | POINT_HI
LEAD = {"from", "to", "like", "at", "into", "see", "check", "watch", "look", "vs", "versus", "se", "jaisa", "jaise"}
LOOK = {"dekho", "dekhiye", "dekh", "dekhna", "dekhte", "look", "see", "watch"}
SHOW_VERBS = {"check", "watch"}  # "check this (out)", "watch this", and "look at this": pointing even before a noun
CLAUSE_END_WORDS = {"this", "these", "here", "ye", "yeh", "yahan", "idhar"}
CONNECT = {"and", "or", "to", "vs", "versus", "then", "aur", "ya", "se", "toh", "tak"}
REPEAT_WINDOW = 5     # words: the same pointer word again within this many words = a repeat
PAUSE_S = 0.3         # s: a pointer word followed by this much silence ends a clause
STANDALONE_GAP_S = 0.15  # s: a shorter breath after it still marks the word as standing alone
MERGE_S = 2.5         # s: hits closer than this are one moment
CONTEXT = 5           # words of context on each side
_PUNCT_END = re.compile(r"[.,!?;:…]+[\"'”’)]*$")


def _norm(w: str) -> str:
    return re.sub(r"[^\w]+", "", str(w).lower())


def _text(w: dict) -> str:
    return str(w.get("w") or w.get("word") or "").strip()


def find_pointers(words: list[dict]) -> list[dict]:
    """The pointing moments in time order (see the module doc)."""
    ws = [w for w in words if isinstance(w, dict) and "s" in w and "e" in w and _text(w)]
    toks = [_norm(_text(w)) for w in ws]
    hits: list[tuple[int, str]] = []
    for i, t in enumerate(toks):
        if t not in POINTS:
            continue
        prev = toks[i - 1] if i > 0 else ""
        prev2 = toks[i - 2] if i > 1 else ""
        nxt = toks[i + 1] if i + 1 < len(toks) else ""
        gap = float(ws[i + 1]["s"]) - float(ws[i]["e"]) if i + 1 < len(ws) else 1.0
        ends = bool(_PUNCT_END.search(_text(ws[i]))) or gap >= PAUSE_S
        # a pointer standing alone (a pronoun pointing at something), not a determiner ("this week", "at this point")
        alone = ends or gap >= STANDALONE_GAP_S or nxt in CONNECT or nxt in POINTS or nxt in LOOK
        why = []
        if alone and (any(toks[j] == t for j in range(max(0, i - REPEAT_WINDOW), i)) or any(
                toks[j] == t for j in range(i + 1, min(len(toks), i + 1 + REPEAT_WINDOW)))):
            why.append("repeat")
        if alone and prev in LEAD:
            why.append("lead")
        if t in POINT_HI and (prev in LOOK or nxt in LOOK) or (t in POINT_EN and prev in {"dekho", "dekhiye"}) or (
                t in POINT_EN and (prev in SHOW_VERBS or (prev2 == "look" and prev == "at"))):
            why.append("look")
        if t in CLAUSE_END_WORDS and ends:
            why.append("clause_end")
        if why:
            hits.append((i, ",".join(why)))
    # the other half of a repeat belongs to the moment ("this to THIS", "ye, ye aur YE") even when it isn't alone
    marked = {i for i, _ in hits}
    for i, why in list(hits):
        if "repeat" not in why:
            continue
        for j in range(max(0, i - REPEAT_WINDOW), min(len(toks), i + 1 + REPEAT_WINDOW)):
            if toks[j] == toks[i] and j not in marked:
                marked.add(j)
                hits.append((j, ""))
    hits.sort()
    moments: list[dict] = []
    for i, why in hits:
        w = ws[i]
        if moments and float(w["s"]) - moments[-1]["_t1"] <= MERGE_S:
            m = moments[-1]
            m["_last"], m["_t1"] = i, float(w["e"])
            m["why"] = list(dict.fromkeys(m["why"] + [x for x in why.split(",") if x]))
            continue
        moments.append({"_first": i, "_last": i, "_t0": float(w["s"]), "_t1": float(w["e"]),
                        "why": [x for x in why.split(",") if x]})
    out = []
    for k, m in enumerate(moments, 1):
        a, b = m["_first"], m["_last"]
        lo, hi = max(0, a - CONTEXT), min(len(ws), b + 1 + CONTEXT)
        out.append({"id": f"P{k}", "t0": round(m["_t0"], 3), "t1": round(m["_t1"], 3),
                    "phrase": " ".join(_text(x) for x in ws[a:b + 1]).rstrip(",.;:!?…"),
                    "context": " ".join(_text(x) for x in ws[lo:hi]), "why": m["why"]})
    return out


def pointer_question(ptrs: list[dict]) -> str:
    """The plain-words lines the reel-inputs skill turns into its question (it adds a suggested picture to each)."""
    from .inserts import fmt_t
    return "\n".join(f"{fmt_t(p['t0'])} · you say \"…{p['context']}…\": what should viewers see here?" for p in ptrs)
