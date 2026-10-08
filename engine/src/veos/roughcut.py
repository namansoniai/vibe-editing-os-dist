"""`veos roughcut-candidates`: the transcript as a compact, sentence-level list for the rough cut.

    veos roughcut-candidates --project P      -> work/roughcut.candidates.json (+ a small summary on stdout)

Source time, per clip (words from work/words/<id>.json), before any cut:
  * sentences (the same splitter as `veos look`: . ? ! । … or a pause >= 0.5 s; longer than 5 s split at a comma /
    the longest pause), each with its clip, times, text and the pause after it;
  * take groups: sentences that say the same thing (token similarity >= SIM), or where one is the start of another (an
    abandoned take), across clips. Each group lists its takes in recording order, which are complete (>= 80 % of the
    longest take and ending on a full stop or a pause) and fluent (no false start or filler inside), and the default
    pick: the last complete, fluent take (the reel-roughcut rule; an earlier take may still be clearly better);
  * false starts inside a sentence: a phrase restarted within MAX_RESTART words ("so the first, so the first thing";
    kind "restart", with the cut [start of the abandoned phrase, start of the restart]) and single-word doubles
    (kind "repeat": a stutter, or deliberate reduplication like "alag alag"; judge them);
  * pauses longer than MAX_PAUSE (0.35 s) between words, and filler runs (um, uh, hmm, ...);
  * suggested_edl: those rules applied mechanically (story order = clip order, then time; pauses > 0.35 s tightened to
    about 0.12 s; cut points 0.04 s before a word and 0.08 s after one; a clean single take = the whole clip). It is a
    starting point for the rough-cutter, not a decision: nothing is cut until work/edl.json is written and `veos cut` runs.
"""
from __future__ import annotations

import difflib

from .core import FPS, VeosError, need_project, r3, read_json
from .cut import LEAD_S, TAIL_S
from .look import _text, norm, sentences, write_look

SIM = 0.72           # token similarity that makes two sentences takes of one line
MIN_TOKENS = 3       # shorter sentences never group (too little to compare)
PREFIX_FRAC = 0.6    # an abandoned take: >= 3 tokens and >= 60 % of the shorter sentence equal the other's start
COMPLETE_FRAC = 0.8  # a complete take has >= 80 % of the group's longest take
MAX_PAUSE = 0.35     # s: longer pauses between words are listed (and tightened in the suggestion)
MAX_RESTART = 6      # words: a restart begins at most this many words after the abandoned phrase began
WHOLE_SILENCE = 0.5  # s: a clean take keeps the whole clip when the silence before/after its words is at most this
FILLERS = set("um umm ummm uh uhh uhm hmm hm mm mmm erm er ah aah eh अं उम्म हम्म".split())
SKIP_KINDS = ("screen-recording", "broll")


def add_args(p, cmd):
    pass


def _tokens(ws: list[dict]) -> list[str]:
    return [t for t in (norm(_text(w) or w.get("w", "")) for w in ws) if t and t not in FILLERS]


def similar(a: list[str], b: list[str]) -> tuple[bool, str]:
    """(same line?, how): 'similar' (token ratio >= SIM) or 'prefix' (one is an abandoned start of the other)."""
    if len(a) < MIN_TOKENS or len(b) < MIN_TOKENS:
        return False, ""
    if difflib.SequenceMatcher(None, a, b, autojunk=False).ratio() >= SIM:
        return True, "similar"
    k = 0
    for x, y in zip(a, b):
        if x != y:
            break
        k += 1
    if k >= MIN_TOKENS and k >= PREFIX_FRAC * min(len(a), len(b)):
        return True, "prefix"
    return False, ""


def false_starts(ws: list[dict]) -> list[dict]:
    """Restarts inside one sentence's words: tokens (t[i], t[i+1]) said again at j (i+2 <= j <= i+MAX_RESTART) ->
    kind restart, cut [s_i, s_j); a word said twice in a row -> kind repeat, cut [s_i, s_i+1)."""
    from .look import STOP
    toks = [norm(_text(w) or w.get("w", "")) for w in ws]
    out, i = [], 0
    while i < len(ws) - 1:
        hit = None
        for j in range(i + 2, min(len(ws) - 1, i + MAX_RESTART) + 1):
            m = 0
            while i + m < j and j + m < len(toks) and toks[i + m] and toks[i + m] == toks[j + m]:
                m += 1
            # the restart repeats >= 3 words, or 2 when one carries content ("kar ke ... kar ke" is grammar, not a flub)
            if m >= 3 or (m == 2 and any(t not in STOP for t in toks[i:i + 2])):
                hit = ("restart", j)
                break
        if hit is None and toks[i] and toks[i] == toks[i + 1] and toks[i] not in FILLERS:
            hit = ("repeat", i + 1)
        if hit is None:
            i += 1
            continue
        kind, j = hit
        out.append({"kind": kind, "cut": [r3(ws[i]["s"]), r3(ws[j]["s"])], "i": [i, j],
                    "dropped": " ".join(_text(w) or w.get("w", "") for w in ws[i:j]),
                    "restart": " ".join(_text(w) or w.get("w", "") for w in ws[j:j + 4])})
        i = j
    return out


def _complete(sent: dict, ws: list[dict], nxt_s: float | None, longest: int, ntok: int) -> bool:
    raw = str(ws[-1].get("w") or "")
    ends = raw.rstrip("\"'”’)").endswith((".", "?", "!", "।", "॥", "…"))
    pause = nxt_s is None or nxt_s - ws[-1]["e"] >= 0.5
    return ntok >= COMPLETE_FRAC * longest and (ends or pause)


def candidates(sources: list[dict], words: dict[str, list[dict]]) -> dict:
    """Pure: sources (sources.json entries, in order) + {id: source-time words} -> the candidates document."""
    order = [s["id"] for s in sources if s["id"] in words and s.get("kind") not in SKIP_KINDS]
    sents, toks, wsof, fs_all, pauses, fillers = [], [], [], [], [], []
    for sid in order:
        ws = sorted((dict(w) for w in words[sid] if isinstance(w.get("s"), (int, float)) and isinstance(w.get("e"), (int, float))),
                    key=lambda w: (w["s"], w["e"]))
        for k, w in enumerate(ws):
            w["i"] = k
        for a, b in zip(ws, ws[1:]):
            if b["s"] - a["e"] > MAX_PAUSE:
                pauses.append({"src": sid, "at": [r3(a["e"]), r3(b["s"])], "d": r3(b["s"] - a["e"])})
        k = 0
        while k < len(ws):
            if norm(_text(ws[k]) or ws[k].get("w", "")) in FILLERS:
                j = k
                while j + 1 < len(ws) and norm(_text(ws[j + 1]) or ws[j + 1].get("w", "")) in FILLERS:
                    j += 1
                fillers.append({"src": sid, "cut": [r3(ws[k]["s"]), r3(ws[j]["e"])], "i": [k, j],
                                "text": " ".join(_text(w) or w.get("w", "") for w in ws[k:j + 1])})
                k = j + 1
            else:
                k += 1
        for s in sentences(ws):
            sw = ws[s["i0"]:s["i1"] + 1]
            fs = false_starts(sw)
            for f in fs:
                f["i"] = [sw[0]["i"] + f["i"][0], sw[0]["i"] + f["i"][1]]
            sents.append({"id": f"{sid}{len([x for x in sents if x['src'] == sid])}", "src": sid, "s": s["t0"], "e": s["t1"],
                          "text": s["text"], "pause_after": s["pause_after"], "i": [s["i0"], s["i1"]]})
            toks.append(_tokens(sw))
            wsof.append(sw)
            for f in fs:
                f.update({"src": sid, "sentence": sents[-1]["id"]})
                fs_all.append(f)
    # take groups (union-find over similar pairs, across clips)
    parent = list(range(len(sents)))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    how: dict[tuple, str] = {}
    for a in range(len(sents)):
        for b in range(a + 1, len(sents)):
            ok, why = similar(toks[a], toks[b])
            if ok:
                parent[root(b)] = root(a)
                how[(a, b)] = why
    members: dict[int, list[int]] = {}
    for k in range(len(sents)):
        members.setdefault(root(k), []).append(k)
    groups = []
    rank = {sid: n for n, sid in enumerate(order)}
    for ms in members.values():
        if len(ms) < 2:
            continue
        ms.sort(key=lambda k: (rank[sents[k]["src"]], sents[k]["s"]))
        longest = max(len(toks[k]) for k in ms)
        info = []
        for k in ms:
            nxt = next((x["s"] for x in sents if x["src"] == sents[k]["src"] and x["s"] > sents[k]["e"]), None)
            comp = _complete(sents[k], wsof[k], nxt, longest, len(toks[k]))
            flu = not any(f["sentence"] == sents[k]["id"] for f in fs_all) and \
                not any(f["src"] == sents[k]["src"] and sents[k]["s"] <= f["cut"][0] <= sents[k]["e"] for f in fillers)
            info.append((k, comp, flu))
        pick = next((k for k, c, f in reversed(info) if c and f), None)
        why = "the last complete, fluent take"
        if pick is None:
            pick = next((k for k, c, _ in reversed(info) if c), None)
            why = "the last complete take (it has a false start or filler: check it)"
        if pick is None:
            pick = max(ms, key=lambda k: (len(toks[k]), sents[k]["s"]))
            why = "no complete take: the longest one"
        gid = f"g{len(groups) + 1}"
        for k, c, f in info:
            sents[k].update({"group": gid, "complete": c, "fluent": f})
        groups.append({"id": gid, "takes": [sents[k]["id"] for k in ms], "complete": [sents[k]["id"] for k, c, _ in info if c],
                       "pick": sents[pick]["id"], "why": why,
                       "how": sorted({how.get((min(a, b), max(a, b)), "") for a in ms for b in ms if a < b} - {""})})
    for s in sents:
        s.setdefault("group", None)
    edl = suggested_edl(sources, order, words, sents, groups, fs_all, fillers, pauses)
    return {"version": 1, "max_pause": MAX_PAUSE, "lead": LEAD_S, "tail": TAIL_S,
            "note": ("source seconds per clip; groups = takes of one line (pick = the default rule: the last complete, fluent "
                     "take); false_starts kind restart = cut [abandoned start, restart start), kind repeat = a word said "
                     "twice (stutter or deliberate); suggested_edl = these rules applied mechanically, in clip order"),
            "sources": [{"id": s["id"], "kind": s.get("kind"), "duration": s.get("duration"),
                         "words": len(words.get(s["id"]) or [])} for s in sources if s["id"] in order],
            "sentences": sents, "groups": groups, "false_starts": fs_all, "pauses": pauses, "fillers": fillers,
            "suggested_edl": edl}


def suggested_edl(sources, order, words, sents, groups, fs_all, fillers, pauses) -> dict:
    by_id = {s["id"]: s for s in sources}
    dropped_sent = {t for g in groups for t in g["takes"] if t != g["pick"]}
    segs = []
    for sid in order:
        ws = sorted((w for w in words[sid] if isinstance(w.get("s"), (int, float))), key=lambda w: (w["s"], w["e"]))
        n = len(ws)
        if not n:
            continue
        keep = [True] * n
        for s in sents:
            if s["src"] == sid and s["id"] in dropped_sent:
                for k in range(s["i"][0], s["i"][1] + 1):
                    keep[k] = False
        for f in fs_all:
            if f["src"] == sid and f["kind"] == "restart":
                for k in range(f["i"][0], f["i"][1]):
                    keep[k] = False
        for f in fillers:
            if f["src"] == sid:
                for k in range(f["i"][0], f["i"][1] + 1):
                    keep[k] = False
        dur = float(by_id[sid].get("duration") or ws[-1]["e"] + TAIL_S)
        clean = all(keep) and not any(p["src"] == sid for p in pauses)
        if clean and ws[0]["s"] <= WHOLE_SILENCE and dur - ws[-1]["e"] <= WHOLE_SILENCE:
            segs.append({"src": sid, "in": 0.0, "out": r3(dur), "note": "single clean take: whole clip"})
            continue
        runs, cur = [], []
        for k in range(n):
            if not keep[k]:
                if cur:
                    runs.append(cur)
                    cur = []
                continue
            if cur and ws[k]["s"] - ws[cur[-1]]["e"] > MAX_PAUSE:
                runs.append(cur)
                cur = []
            cur.append(k)
        if cur:
            runs.append(cur)
        last_out = -1.0
        for run in runs:
            a = max(0.0, ws[run[0]]["s"] - LEAD_S, last_out)
            b = min(dur, ws[run[-1]]["e"] + TAIL_S)
            if b - a < 1.0 / FPS:
                continue
            ids = sorted({s["id"] for s in sents if s["src"] == sid and s["i"][0] <= run[-1] and s["i"][1] >= run[0]},
                         key=lambda x: int(x[len(sid):]))
            segs.append({"src": sid, "in": r3(a), "out": r3(b), "note": " ".join(ids)})
            last_out = b
    kept = sum(s["out"] - s["in"] for s in segs)
    return {"version": 1, "fps": FPS, "auto": "roughcut-candidates", "kept_s": r3(kept), "segments": segs}


def main(args, project) -> dict:
    pr = need_project(project)
    sp = pr.work / "sources.json"
    if not sp.exists():
        raise VeosError("NO_SOURCES", "work/sources.json missing", "Run `veos ingest` (prep) first.")
    sources = read_json(sp).get("sources") or []
    words = {}
    for s in sources:
        wp = pr.work / "words" / f"{s['id']}.json"
        if wp.exists() and s.get("kind") not in SKIP_KINDS:
            words[s["id"]] = read_json(wp).get("words") or []
    if not words:
        raise VeosError("NO_WORDS", "no transcripts in work/words/", "Run `veos transcribe` (prep) first.")
    doc = candidates(sources, words)
    out = pr.path("work", "roughcut.candidates.json")
    write_look(out, doc)
    return {"file": pr.rel(out), "sources": {s["id"]: s["duration"] for s in doc["sources"]},
            "sentences": len(doc["sentences"]), "take_groups": len(doc["groups"]),
            "false_starts": sum(1 for f in doc["false_starts"] if f["kind"] == "restart"),
            "repeats": sum(1 for f in doc["false_starts"] if f["kind"] == "repeat"),
            "pauses_gt_035": len(doc["pauses"]), "fillers": len(doc["fillers"]),
            "suggested": {"segments": len(doc["suggested_edl"]["segments"]), "kept_s": doc["suggested_edl"]["kept_s"]}}
