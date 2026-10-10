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
  * pauses longer than MAX_PAUSE (0.35 s), from the AUDIO (speechmap.py): `kind: "audio"` = a real silence, with the
    word it hides in (`inside_word`) or the words lying on it (`under_words`, e.g. a hallucinated "you."), `dead_air`
    when >= 0.6 s; `kind: "words"` = a gap between words where the audio still hears something (`sound: true`:
    untranscribed speech, a breath, noise). Without a speech map: word gaps, as before. Plus filler runs (um, uh, ...);
  * per clip (`sources[]`): the audio's `speech` regions and `silences` (>= 0.25 s);
  * `suspect_words`: words the transcript found lying in a silence (left out of everything here);
  * suggested_edl: those rules applied mechanically (story order = clip order, then time). It splits at real silences
    (every silence >= 0.6 s, and a silence > 0.35 s at a gap between words) and never inside speech, keeping the
    style's pause (playbook `cut.pause_s`, default 0.12 s: a third before the speech, two thirds after); a cut edge on a
    loose word edge moves onto the audio; a clean single take = the whole clip. It is a starting point for the cutter,
    not a decision: nothing is cut until work/edl.json is written and `veos cut` runs.
"""
from __future__ import annotations

import difflib

from .core import FPS, VeosError, need_project, r3, read_json
from .cut import LEAD_S, TAIL_S
from .look import _text, norm, sentences, write_look
from .speechmap import DEAD_AIR, LIST_MIN, overlap

SIM = 0.72           # token similarity that makes two sentences takes of one line
MIN_TOKENS = 3       # shorter sentences never group (too little to compare)
PREFIX_FRAC = 0.6    # an abandoned take: >= 3 tokens and >= 60 % of the shorter sentence equal the other's start
COMPLETE_FRAC = 0.8  # a complete take has >= 80 % of the group's longest take
MAX_PAUSE = 0.35     # s: longer pauses between words are listed (and tightened in the suggestion)
MAX_RESTART = 6      # words: a restart begins at most this many words after the abandoned phrase began
WHOLE_SILENCE = 0.5  # s: a clean take keeps the whole clip when the silence before/after its words is at most this
FILLERS = set("um umm ummm uh uhh uhm hmm hm mm mmm erm er ah aah eh अं उम्म हम्म".split())
SKIP_KINDS = ("screen-recording", "broll")
SPLIT_S = DEAD_AIR    # s: a silence this long is always cut out of a kept run (tightened to the style's pause)
EDGE_SLACK = 0.08     # s: speech starting / ending this much beyond a word edge moves the cut point onto the audio
EDGE_MAX = 0.6        # s: ... but never further than this from the word


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


def _audio_pauses(sid: str, ws: list[dict], sil: list, speech: list, suspect: list[dict]) -> list[dict]:
    """Pauses inside the clip's speech (between its first and last word), from the audio, plus word gaps the audio
    hears sound in."""
    if not ws:
        return []
    lo, hi = ws[0]["s"], ws[-1]["e"]
    out = []
    for a, b in sil:
        if b - a <= MAX_PAUSE or not lo < (a + b) / 2 < hi:
            continue
        p = {"src": sid, "at": [r3(a), r3(b)], "d": r3(b - a), "kind": "audio"}
        host = next((w for w in ws if w["s"] < a - 0.01 and w["e"] > b + 0.01), None)
        if host:
            p["inside_word"] = _text(host) or host.get("w", "")
        under = [w for w in ws + suspect if overlap(w["s"], w["e"], a, b) >= 0.5 * max(w["e"] - w["s"], 1e-6)]
        if under:
            p["under_words"] = " ".join(_text(w) or w.get("w", "") for w in sorted(under, key=lambda w: w["s"]))
        if b - a >= DEAD_AIR:
            p["dead_air"] = True
        out.append(p)
    for x, y in zip(ws, ws[1:]):
        a, b = x["e"], y["s"]
        if b - a > MAX_PAUSE and not any(overlap(a, b, *p["at"]) > 0.05 for p in out):
            heard = any(overlap(a, b, s0, s1) > 0.05 for s0, s1 in speech)
            out.append({"src": sid, "at": [r3(a), r3(b)], "d": r3(b - a), "kind": "words", "sound": heard})
    return sorted(out, key=lambda p: p["at"][0])


def candidates(sources: list[dict], words: dict[str, list[dict]], speech: dict[str, dict] | None = None,
               pause: float = TAIL_S + LEAD_S) -> dict:
    """Pure: sources (sources.json entries, in order) + {id: source-time words} (+ {id: speech map}) -> the candidates
    document. `pause`: the silence a tightened cut keeps (the style's pause)."""
    speech = speech or {}
    order = [s["id"] for s in sources if s["id"] in words and s.get("kind") not in SKIP_KINDS]
    sents, toks, wsof, fs_all, pauses, fillers, suspect_all = [], [], [], [], [], [], []
    kept_words: dict[str, list[dict]] = {}
    for sid in order:
        valid = [dict(w) for w in words[sid] if isinstance(w.get("s"), (int, float)) and isinstance(w.get("e"), (int, float))]
        susp = sorted((w for w in valid if w.get("suspect")), key=lambda w: w["s"])
        suspect_all += [{"src": sid, "w": w.get("w"), "s": r3(w["s"]), "e": r3(w["e"]), "why": w["suspect"]} for w in susp]
        ws = sorted((w for w in valid if not w.get("suspect")), key=lambda w: (w["s"], w["e"]))
        kept_words[sid] = ws
        for k, w in enumerate(ws):
            w["i"] = k
        m = speech.get(sid)
        if m is not None:
            pauses += _audio_pauses(sid, ws, m.get("silences") or [], m.get("speech") or [], susp)
        else:
            for a, b in zip(ws, ws[1:]):
                if b["s"] - a["e"] > MAX_PAUSE:
                    pauses.append({"src": sid, "at": [r3(a["e"]), r3(b["s"])], "d": r3(b["s"] - a["e"]), "kind": "words"})
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
    lead, tail = round(pause / 3, 3), round(pause * 2 / 3, 3)
    edl = suggested_edl(sources, order, kept_words, sents, groups, fs_all, fillers, pauses, speech=speech,
                        lead=lead, tail=tail)
    srcs = []
    for s in sources:
        if s["id"] not in order:
            continue
        row = {"id": s["id"], "kind": s.get("kind"), "duration": s.get("duration"), "words": len(kept_words.get(s["id"]) or [])}
        m = speech.get(s["id"])
        if m is not None:
            row["speech"] = m.get("speech") or []
            row["silences"] = [x for x in m.get("silences") or [] if x[1] - x[0] >= LIST_MIN - 1e-9]
            row["speech_map"] = m.get("method")
        srcs.append(row)
    return {"version": 1, "max_pause": MAX_PAUSE, "dead_air": DEAD_AIR, "pause": r3(pause), "lead": lead, "tail": tail,
            "note": ("source seconds per clip; groups = takes of one line (pick = the default rule: the last complete, fluent "
                     "take); false_starts kind restart = cut [abandoned start, restart start), kind repeat = a word said "
                     "twice (stutter or deliberate); pauses kind audio = a real silence (dead_air when >= 0.6 s; the "
                     "words on it are the speech model hearing things), kind words + sound = something audible between "
                     "the words; sources[].speech / silences = the audio's own map; suggested_edl = these rules applied "
                     "mechanically, in clip order, cut on real silences and never inside speech"),
            "sources": srcs, "sentences": sents, "groups": groups, "false_starts": fs_all, "pauses": pauses,
            "fillers": fillers, "suspect_words": suspect_all, "suggested_edl": edl}


def _containing(iv: list, t: float):
    return next(((a, b) for a, b in iv if a <= t <= b), None)


def _edges(ws: list[dict], run: list[int], sil: list, speech: list, lead: float, tail: float) -> tuple[float, float]:
    """Cut points of a run of kept words: `lead` before its first word and `tail` after its last, with a loose word
    edge moved onto the audio (a word starting in a silence starts when it ends) and speech the word edges miss kept
    (when it belongs to no other word)."""
    s, e = ws[run[0]]["s"], ws[run[-1]]["e"]
    S = _containing(sil, s)
    if S and S[1] < e:
        s = S[1]
    S = _containing(sil, e)
    if S and S[0] > s:
        e = S[0]
    a, b = s - lead, e + tail
    prev_e = ws[run[0] - 1]["e"] if run[0] > 0 else 0.0
    next_s = ws[run[-1] + 1]["s"] if run[-1] + 1 < len(ws) else float("inf")
    R = _containing(speech, a)
    if R and R[0] < a - EDGE_SLACK and R[0] >= prev_e - 0.01 and a - R[0] <= EDGE_MAX:
        a = R[0]
    R = _containing(speech, b)
    if R and R[1] > b + EDGE_SLACK and R[1] <= next_s + 0.01 and R[1] - b <= EDGE_MAX:
        b = R[1]
    return a, b


def _splits(ws: list[dict], run: list[int], sil: list) -> list[tuple[float, float]]:
    """Real silences inside a run to cut out: every one >= SPLIT_S, and one > MAX_PAUSE that sits at a gap between
    words (not inside a word)."""
    lo, hi = ws[run[0]]["s"], ws[run[-1]]["e"]
    out = []
    for a, b in sil:
        if not (lo < a and b < hi) or b - a <= MAX_PAUSE:
            continue
        inside_word = any(ws[k]["s"] < a - 0.01 and ws[k]["e"] > b + 0.01 for k in run)
        if b - a >= SPLIT_S or not inside_word:
            out.append((a, b))
    return out


def suggested_edl(sources, order, words, sents, groups, fs_all, fillers, pauses, speech=None,
                  lead: float = LEAD_S, tail: float = TAIL_S) -> dict:
    by_id = {s["id"]: s for s in sources}
    dropped_sent = {t for g in groups for t in g["takes"] if t != g["pick"]}
    speech = speech or {}
    segs = []
    for sid in order:
        ws = sorted((w for w in words[sid] if isinstance(w.get("s"), (int, float))), key=lambda w: (w["s"], w["e"]))
        n = len(ws)
        m = speech.get(sid)
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
            if m is None and cur and ws[k]["s"] - ws[cur[-1]]["e"] > MAX_PAUSE:  # no audio map: word gaps, as before
                runs.append(cur)
                cur = []
            cur.append(k)
        if cur:
            runs.append(cur)
        last_out = -1.0
        sil = (m or {}).get("silences") or []
        spm = (m or {}).get("speech") or []
        for run in runs:
            if m is None:
                pieces = [(ws[run[0]]["s"] - LEAD_S, ws[run[-1]]["e"] + TAIL_S)]
            else:  # cut on the audio: real silences out (the style's pause kept), never inside speech
                a0, b0 = _edges(ws, run, sil, spm, lead, tail)
                cuts = [a0]
                for x, y in _splits(ws, run, sil):
                    if x + tail > cuts[-1] and y - lead < b0:
                        cuts += [x + tail, y - lead]
                cuts.append(b0)
                pieces = list(zip(cuts[0::2], cuts[1::2]))
            for a, b in pieces:
                a = max(0.0, a, last_out)
                b = min(dur, b)
                if b - a < 1.0 / FPS:
                    continue
                ks = [k for k in run if a - 0.01 <= ws[k]["s"] < b] or run
                ids = sorted({s["id"] for s in sents if s["src"] == sid and s["i"][0] <= ks[-1] and s["i"][1] >= ks[0]},
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
    from . import langs, speechmap
    maps = {}
    for s in sources:
        if s["id"] in words:
            try:
                m = speechmap.for_source(pr, s["id"], s.get("duration"))
            except Exception:  # noqa: BLE001 - without a map the word gaps decide, as before
                m = None
            if m is not None:
                maps[s["id"]] = m
    doc = candidates(sources, words, maps, pause=langs.cut_settings(pr)["pause_s"])
    out = pr.path("work", "roughcut.candidates.json")
    write_look(out, doc)
    return {"file": pr.rel(out), "sources": {s["id"]: s["duration"] for s in doc["sources"]},
            "sentences": len(doc["sentences"]), "take_groups": len(doc["groups"]),
            "false_starts": sum(1 for f in doc["false_starts"] if f["kind"] == "restart"),
            "repeats": sum(1 for f in doc["false_starts"] if f["kind"] == "repeat"),
            "pauses_gt_035": len(doc["pauses"]), "dead_air": sum(1 for p in doc["pauses"] if p.get("dead_air")),
            "suspect_words": len(doc["suspect_words"]), "fillers": len(doc["fillers"]),
            "suggested": {"segments": len(doc["suggested_edl"]["segments"]), "kept_s": doc["suggested_edl"]["kept_s"]}}
