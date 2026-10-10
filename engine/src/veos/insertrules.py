"""V-INSERTS and V-CITE (E-10; structure §12.5, §19, NC-7, NC-13).

Blocking (facts): someone's words or a headline not verbatim, highlight words that aren't in the headline, media of
unknown origin (NC-7: the creator's own file, a file fetched from the web with its source, or a created visual). Everything else here is advice (validate's
levels). Made-up cards carry no label and nothing needs a credit line (Naman, 8 Oct 2026).

V-INSERTS (always on; nothing to check -> no findings)
  - plan/inserts.json is valid (veos.inserts.record_problems): ids, kinds, origins (creator | created | fetched),
    `origin: creator` / `fetched` points to a plan/assets entry added with `veos asset add` (`--origin creator`, or
    `--source <url>` for a file fetched from the web), created inserts name
    a recipe and what they stand in for, quote_text is verbatim from the script / transcript / the creator's own text.
  - every moment in plan/inserts.scan.json has a record or a `dismissed` reason;
  - every third-party pattern beat (beat `pattern` in tokens.inserts.patterns or the default list, or a beat with
    `insert` / `third_party`) has an insert record overlapping it;
  - every record is shown: a scene (`scene` field or a scene declaring `insert: <id>`) active within its time range;
    a creator record's scene shows its asset (scene `asset`, when declared); a quote / headline scene shows exactly the
    record's quote_text;
  - any scene that declares `quote_text` (any quote card, even without a record) quotes verbatim (NC-13);
  - scenes that show a plan/assets file declare it (`asset`) and that asset has origin creator, created or fetched.
V-CITE (always on; runs on `source` beats and scenes)
  - every source has masthead + date + headline; highlight spans exist in the headline text;
  - a created source card quotes the headline exactly from the script / transcript / creator text;
  - FIG. numbers increase when `citations.figure_numbering`.
"""
from __future__ import annotations

from .core import read_json
from .inserts import (QUOTE_RECIPES, THIRD_PARTY_PATTERNS, asset_name, asset_origins, corpus, fact_problem, is_verbatim,
                      norm_tokens, record_problems)
from .vcommon import advice, fail, get_path


def _load(ctx, name):
    proj = getattr(ctx, "project", None)
    if proj is None:
        return None, False
    p = proj.root / "plan" / name
    if not p.exists():
        return None, False
    try:
        return read_json(p), True
    except ValueError:
        ctx.warnings.append(f"plan/{name} is not valid JSON; ignored")
        return None, True


def _corpus(ctx, data):
    proj = getattr(ctx, "project", None)
    cache = getattr(ctx, "_ins_corpus", None)
    if cache is None:
        cache = corpus(proj, ctx.words, data) if (proj is not None or ctx.words) else []
        ctx._ins_corpus = cache
    return cache


def _scenes_of(ctx, rec) -> list[dict]:
    want = rec.get("scene")
    want = [want] if isinstance(want, str) else list(want or [])
    return [s for s in ctx.scenes if s.get("id") in want or (rec.get("id") and s.get("insert") == rec.get("id"))]


def _overlaps(a0, a1, b0, b1) -> bool:
    return float(a0) < float(b1) - 1e-6 and float(b0) < float(a1) - 1e-6


def rule_inserts(c, p: dict) -> list:
    out = []
    data, present = _load(c, "inserts.json")
    scan, _ = _load(c, "inserts.scan.json")
    scan_ids = [m.get("id") for m in (scan or {}).get("moments", []) if isinstance(m, dict)]
    patterns = set(p.get("patterns") or get_path(c.style, "inserts.patterns") or THIRD_PARTY_PATTERNS)
    tp_beats = [b for b in c.beats if b.get("pattern") in patterns or b.get("insert") or b.get("third_party")]
    proj = getattr(c, "project", None)
    docs = _corpus(c, data if isinstance(data, dict) else None)

    if not present:
        if scan_ids:
            out.append(advice(fail("V-INSERTS", None, 0, f"{len(scan_ids)} third-party moment(s) were scanned but plan/inserts.json is missing",
                            "Ask the creator once (reel-inputs), then record every moment in plan/inserts.json (creator file or created card).")))
        for b in tp_beats:
            out.append(advice(fail("V-INSERTS", b.get("id"), b.get("t0", 0), f"beat {b.get('id')} shows third-party material "
                            f"({b.get('pattern') or 'insert'}) but there is no plan/inserts.json record",
                            "Record the insert (origin creator with the creator's file, or origin created with a card).")))
    recs = [r for r in (data or {}).get("inserts", []) if isinstance(r, dict)] if isinstance(data, dict) else []
    if present:
        for rid, msg, fix in record_problems(data, proj, docs, c.style, scan_ids):
            r = next((x for x in recs if x.get("id") == rid), None)
            t = float((r or {}).get("t0") or 0) if r else 0
            f = fail("V-INSERTS", c.beat_id(t) if r else None, t, msg, fix)
            out.append(f if fact_problem(msg) else advice(f))
        for b in tp_beats:
            b0, b1 = b.get("t0", 0), b.get("t1", 0)
            want = b.get("insert")
            hit = [r for r in recs if (want and r.get("id") == want) or (not want and _overlaps(r.get("t0", 0), r.get("t1", 0), b0, b1))]
            if not hit:
                out.append(advice(fail("V-INSERTS", b.get("id"), b0, f"beat {b.get('id')} ({b.get('pattern') or 'insert'}) has no insert record"
                                + (f" with id {want}" if want else " in its time range"),
                                "Add the record to plan/inserts.json (creator file or created card) and link it with the beat's `insert`.")))
    origins = asset_origins(proj) if proj is not None else {}
    for r in recs:
        rid, t0, t1 = r.get("id"), r.get("t0", 0), r.get("t1", 0)
        try:
            float(t0), float(t1)
        except (TypeError, ValueError):
            continue
        scs = _scenes_of(c, r)
        if not scs:
            out.append(advice(fail("V-INSERTS", c.beat_id(t0), t0, f"insert {rid} is not shown by any scene",
                            f"Give its scene `insert: \"{rid}\"` (the VEOS.fx insert factories take `insert`), or set the record's `scene`.")))
            continue
        if not any(_overlaps(s.get("t_in", 0), s.get("t_out", 0), t0, t1) for s in scs):
            out.append(advice(fail("V-INSERTS", c.beat_id(t0), t0, f"insert {rid}'s scene ({', '.join(s['id'] for s in scs)}) is not on screen "
                            f"during its moment {float(t0):.2f}-{float(t1):.2f} s", "Move the scene onto the moment's words.")))
        if r.get("origin") in ("creator", "fetched") and r.get("file"):
            nm = asset_name(r["file"])
            shown = [s.get("asset") for s in scs if s.get("asset")]
            if shown and nm not in {asset_name(a) for a in shown}:
                out.append(advice(fail("V-INSERTS", c.beat_id(t0), t0, f"insert {rid} is the creator's '{nm}' but its scene shows '{shown[0]}'",
                                f"Show the creator's asset `{nm}` in the scene.")))
        if r.get("quote_text") and r.get("recipe") in QUOTE_RECIPES:
            want = norm_tokens(r["quote_text"])
            if not any(norm_tokens(s.get("quote_text") or "") == want for s in scs):
                out.append(fail("V-INSERTS", c.beat_id(t0), t0, f"insert {rid}: the card does not show the record's quote_text exactly",
                                "Show exactly the record's quote_text (scene `quote_text` / the factory's `quote`)."))
    for s in c.scenes:
        q = s.get("quote_text")
        if q and s.get("origin") not in ("creator", "fetched") and not is_verbatim(q, docs):
            out.append(fail("V-INSERTS", c.beat_id(s.get("t_in", 0)), s.get("t_in", 0),
                            f"scene {s.get('id')} quotes \"{str(q)[:60]}\", which is not in the script, transcript or the creator's text (NC-13)",
                            "Quote only the script's or transcript's words, verbatim."))
        a = s.get("asset")
        if a and proj is not None:
            o = (origins.get(asset_name(a)) or {}).get("origin")
            if o not in ("creator", "created", "fetched"):
                out.append(fail("V-INSERTS", c.beat_id(s.get("t_in", 0)), s.get("t_in", 0),
                                f"scene {s.get('id')} shows asset '{a}', which has no recorded origin (creator | created | fetched)",
                                f"Add it with `veos asset add <file> --name {asset_name(a)}` (with `--source <url>` for a file from the web)."))
    c.stats_extra["inserts"] = {"records": len(recs), "creator": sum(1 for r in recs if r.get("origin") == "creator"),
                                "created": sum(1 for r in recs if r.get("origin") == "created"),
                                "fetched": sum(1 for r in recs if r.get("origin") == "fetched"),
                                "scanned": len(scan_ids), "third_party_beats": len(tp_beats)}
    return out


def rule_cite(c, p: dict) -> list:
    out = []
    data, _ = _load(c, "inserts.json")
    recs = {r.get("id"): r for r in (data or {}).get("inserts", []) if isinstance(r, dict)} if isinstance(data, dict) else {}
    cit = c.style.get("citations") or {}
    docs = _corpus(c, data if isinstance(data, dict) else None)
    items = []   # (where, t, beat id, source, spans, credit, origin, scenes)
    for b in c.beats:
        src = b.get("source")
        if not isinstance(src, dict):
            continue
        rec = recs.get(b.get("insert")) if b.get("insert") else None
        layer = [s for s in c.scenes if s.get("id") in (b.get("layers") or [])]
        spans = b.get("highlight_spans") if b.get("highlight_spans") is not None else src.get("highlight_spans")
        origin = (rec or {}).get("origin") or next((s.get("origin") for s in layer if s.get("origin")), None)
        items.append((f"beat {b.get('id')}", b.get("t0", 0), b.get("id"), src, spans, b.get("credit"), origin, layer))
    in_beats = {s.get("id") for it in items for s in it[7]}
    for s in c.scenes:
        src = s.get("source")
        if isinstance(src, dict) and s.get("id") not in in_beats:
            items.append((f"scene {s.get('id')}", s.get("t_in", 0), c.beat_id(s.get("t_in", 0)), src, src.get("highlight_spans"),
                          s.get("credit"), s.get("origin"), [s]))
    for where, t, bid, src, spans, credit, origin, scs in items:
        miss = [k for k in ("masthead", "date", "headline") if not str(src.get(k) or "").strip()]
        if miss:
            out.append(advice(fail("V-CITE", bid, t, f"{where}: the source has no {', '.join(miss)}",
                            "A source card usually shows the outlet (set in type), the date and the exact headline.")))
        head = " ".join(str(src.get("headline") or "").split())
        for sp in spans or []:
            sp_txt = " ".join(str(sp.get("text") if isinstance(sp, dict) else sp).split())
            if head and sp_txt not in head:
                out.append(fail("V-CITE", bid, t, f"{where}: highlight span \"{sp_txt[:40]}\" is not in the headline",
                                "Highlight words that are in the headline text, exactly."))
        if head and origin != "creator" and not is_verbatim(head, docs):
            out.append(fail("V-CITE", bid, t, f"{where}: headline \"{head[:60]}\" is not quoted exactly from the script, transcript or creator",
                            "Headlines are quoted exactly, never paraphrased: copy it from the script or the creator's text."))
    if cit.get("figure_numbering"):
        figs = sorted(((s.get("t_in", 0), s.get("figure"), s.get("id")) for s in c.scenes if s.get("figure") is not None),
                      key=lambda x: x[0])
        last = None
        for t, f, sid in figs:
            try:
                f = int(f)
            except (TypeError, ValueError):
                continue
            if last is not None and f <= last:
                out.append(advice(fail("V-CITE", c.beat_id(t), t, f"scene {sid}: FIG. {f:02d} does not increase (previous FIG. {last:02d})",
                                "Number figures in order of appearance.")))
            last = f
    c.stats_extra["citations"] = {"sources": len(items)}
    return out
