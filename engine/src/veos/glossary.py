"""Brand/tool glossary post-pass for transcripts (data lives in assets-default/glossary.json)."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .core import read_json

DEFAULT_PATH = Path(__file__).resolve().parents[2] / "assets-default" / "glossary.json"
SENT_END = re.compile(r"[.?!।]$")
_STRIP = re.compile(r"^([^\w]*)(.*?)([^\w]*)$", re.S)


def load_glossary(extra: str | Path | None = None) -> dict[str, Any]:
    """Default glossary, with the user's file merged over it (same term -> aliases unioned, new terms appended)."""
    g = read_json(DEFAULT_PATH) if DEFAULT_PATH.exists() else {"terms": []}
    g = {"context_aliases": list(g.get("context_aliases", [])), "context_words": list(g.get("context_words", [])),
         "terms": [dict(t, aliases=list(t.get("aliases", []))) for t in g.get("terms", [])]}
    if extra:
        u = read_json(extra)
        if isinstance(u, list):  # a bare list of terms is fine too
            u = {"terms": [{"term": t} if isinstance(t, str) else t for t in u]}
        for k in ("context_aliases", "context_words"):
            g[k] += [x for x in u.get(k, []) if x not in g[k]]
        by = {t["term"].lower(): t for t in g["terms"]}
        for t in u.get("terms", []):
            t = {"term": t} if isinstance(t, str) else t
            if t["term"].lower() in by:
                cur = by[t["term"].lower()]
                cur["aliases"] += [a for a in t.get("aliases", []) if a not in cur["aliases"]]
                if "ambiguous" in t:
                    cur["ambiguous"] = t["ambiguous"]
            else:
                t = dict(t, aliases=list(t.get("aliases", [])))
                g["terms"].append(t)
                by[t["term"].lower()] = t
    return g


def term_list(g: dict[str, Any]) -> list[str]:
    return [t["term"] for t in g["terms"]]


def _norm(w: str) -> str:
    return _STRIP.match(w).group(2).lower()


def _split(w: str) -> tuple[str, str, str]:
    m = _STRIP.match(w)
    return m.group(1), m.group(2), m.group(3)


def apply_glossary(words: list[dict], g: dict[str, Any]) -> list[dict]:
    """Fix mis-heard brand names in place-ish: returns the fix log [{"i","from","to"}].

    Words are re-indexed ("i") after the pass because a multi-word alias ("next js") may merge into one word.
    Ambiguous matches (like "cloud") are only fixed when a neighbouring word is a context word or the sentence
    already contains an unambiguous glossary term.
    """
    ctx_alias = {a.lower() for a in g.get("context_aliases", [])}
    ctx_words = {c.lower() for c in g.get("context_words", [])}
    rules: list[tuple[list[str], str, bool, bool]] = []  # alias tokens, canonical, always-needs-context, is canonical self-match
    for t in g["terms"]:
        amb = bool(t.get("ambiguous"))
        for a in [t["term"]] + list(t.get("aliases", [])):
            toks = a.lower().split()
            if toks:
                rules.append((toks, t["term"], amb or a.lower() in ctx_alias, a == t["term"]))
    rules.sort(key=lambda r: -len(r[0]))
    n = len(words)
    norm = [_norm(w["w"]) for w in words]
    hits: list[tuple[int, int, str, bool]] = []  # start, length, canonical, needs_context
    i = 0
    while i < n:
        for toks, canon, needs, _ in rules:
            k = len(toks)
            if i + k <= n and norm[i:i + k] == toks:
                hits.append((i, k, canon, needs))
                i += k
                break
        else:
            i += 1

    def sentence_bounds(pos: int) -> tuple[int, int]:
        a = pos
        while a > 0 and not SENT_END.search(words[a - 1]["w"]) and pos - a < 12:
            a -= 1
        b = pos
        while b < n - 1 and not SENT_END.search(words[b]["w"]) and b - pos < 12:
            b += 1
        return a, b

    sure = [h for h in hits if not h[3]]
    accepted = []
    for st, k, canon, needs in hits:
        ok = not needs
        if needs:
            nb = [norm[j] for j in (st - 1, st + k, st + k + 1) if 0 <= j < n]
            if any(x in ctx_words for x in nb):
                ok = True
            else:
                a, b = sentence_bounds(st)
                ok = any(a <= s2 <= b and s2 != st for s2, _, _, _ in sure)
        if ok:
            accepted.append((st, k, canon))

    fixes: list[dict] = []
    out: list[dict] = []
    amap = {st: (k, canon) for st, k, canon in accepted}
    i = 0
    while i < n:
        w = words[i]
        if i in amap:
            k, canon = amap[i]
            seg = words[i:i + k]
            orig = " ".join(x["w"] for x in seg)
            lead, _, _ = _split(seg[0]["w"])
            _, _, trail = _split(seg[-1]["w"])
            ctoks = canon.split()
            if len(ctoks) == k:  # same token count: keep per-word timing
                new = []
                for j, x in enumerate(seg):
                    x = dict(x)
                    x["w"] = (lead if j == 0 else "") + ctoks[j] + (trail if j == k - 1 else "")
                    new.append(x)
            else:  # merge into one word spanning the group
                x = dict(seg[0])
                x["w"] = lead + canon + trail
                x["e"] = seg[-1]["e"]
                x["p"] = round(sum(s["p"] for s in seg) / k, 3)
                new = [x]
            if " ".join(x["w"] for x in new) != orig:
                fixes.append({"i": len(out), "from": " ".join(_split(x["w"])[1] for x in seg), "to": canon})
            out.extend(new)
            i += k
        else:
            out.append(w)
            i += 1
    words[:] = out
    for j, w in enumerate(words):
        w["i"] = j
    return fixes
