"""V-CAPTION (E-05, with the E-20 glossary spelling): caption sync, chunk limits, speaker colour, emphasis budget,
glossary spelling and no hand-written cards.

Source: work/captions.json (the caption engine's export; rebuilt by `veos bundle` / `veos captions build`). When it is
missing, the chunks are built in memory from work/tokens.json + words. Params (`validator.rules.V-CAPTION`):
max_lead_s (0.15), max_lag_s (0.1), cut_tol_s (0.05), spelling (true), brand_case (true).
"""
from __future__ import annotations

from pathlib import Path

from . import captext as X
from .core import read_json
from .vcommon import fail

DEF = {"max_lead_s": 0.15, "max_lag_s": 0.10, "cut_tol_s": 0.05, "spelling": True, "brand_case": True}


def load_export(c) -> tuple[dict | None, str]:
    proj = getattr(c, "project", None)
    if proj is not None:
        p = Path(proj.work) / "captions.json"
        if p.exists():
            try:
                d = read_json(p)
                wp = Path(proj.work) / "words.edit.json"
                if wp.exists() and wp.stat().st_mtime > p.stat().st_mtime + 1:
                    c.warnings.append("work/captions.json is older than work/words.edit.json; run `veos captions build` "
                                      "(or `veos bundle`) so V-CAPTION checks the current captions")
                return d, "captions.json"
            except ValueError:
                c.warnings.append("work/captions.json is not valid JSON; V-CAPTION rebuilds the chunks in memory")
    if c.tokens and c.words:
        from . import capengine
        try:
            return capengine.build(c.tokens, c.tl, c.words), "built"
        except Exception as e:  # noqa: BLE001
            c.warnings.append(f"V-CAPTION could not build the caption chunks ({e})")
    return None, "none"


def _profile_rules(c, exp: dict, profs: dict, chunks: list) -> list:
    """Package C fields: bad swap / reveal / line-fit / tier values, caption cy overrides inside the safe zone and a
    boolean hide_on_morph. Flicker swaps are free: there is no flash limit."""
    from . import capengine as E
    out = []
    for pid, pf in sorted(profs.items()):
        for msg in pf.get("problems") or []:
            out.append(fail("V-CAPTION", None, 0.0, f"caption profile {pid}: {msg}",
                            "fix the profile in the playbook's captions.profiles (SCENES-API: caption swaps and reveals)"))
    tok = getattr(c, "tokens", None) or {}
    safe = ((tok.get("layout") or {}).get("safe") or {}).get("y") or [110, 1500]
    for o in ((c.tl.get("captions") or {}).get("overrides") or []):
        if isinstance(o, dict) and "cy" in o:
            cy = o["cy"]
            if not isinstance(o.get("t"), list) or len(o["t"]) != 2:
                out.append(fail("V-CAPTION", None, 0.0, f"captions override {o} sets cy without a time range",
                                "write it as {\"t\": [a, b], \"cy\": y}"))
            elif not E._num(cy) or not safe[0] <= cy <= safe[1]:
                out.append(fail("V-CAPTION", None, float(o["t"][0]), f"captions override cy {cy!r} is outside the "
                                f"safe zone {list(safe)}", "pick a caption centre inside layout.safe.y"))
    for where, v in (("timeline captions", (c.tl.get("captions") or {}).get("hide_on_morph")),
                     ("captions", (tok.get("captions") or {}).get("hide_on_morph") if isinstance(tok.get("captions"), dict) else None)):
        if v is not None and not isinstance(v, bool):
            out.append(fail("V-CAPTION", None, 0.0, f"{where}.hide_on_morph {v!r} must be true or false",
                            "set hide_on_morph: false to keep captions through stage morphs"))
    return out


def rule_caption(c, p: dict) -> list:
    prm = {**DEF, **{k: v for k, v in (p or {}).items() if k in DEF}}
    out = []
    tc = c.tl.get("captions") or {}
    for k in ("cards", "chunks"):
        if tc.get(k):
            out.append(fail("V-CAPTION", None, 0.0, f"timeline.captions.{k} hand-writes caption cards",
                            "delete it: the caption engine builds the chunks; use captions.overrides for text fixes, "
                            "breaks, emphasis or a profile switch"))
    exp, src = load_export(c)
    if not exp or exp.get("mode") == "off":
        c.stats_extra["captions"] = {"source": src, "chunks": 0}
        return out
    chunks = exp.get("chunks") or []
    profs = exp.get("profiles") or {}
    speakers = exp.get("speakers") or {}
    legacy = bool(exp.get("legacy"))
    out += _profile_rules(c, exp, profs, chunks)
    gl = None
    if prm["spelling"]:
        from .glossary import load_glossary
        try:
            proj = getattr(c, "project", None)
            gp = proj.root / "plan" / "glossary.json" if proj is not None else None
            gl = X.Glossary(list(load_glossary(gp if gp is not None and gp.exists() else None).get("terms") or [])
                            + list(exp.get("glossary") or []))
        except Exception:  # noqa: BLE001
            gl = None
    counts = {"sync": 0, "limits": 0, "speaker": 0, "emphasis": 0, "spelling": 0}
    emph_t: dict[str, list] = {}
    for ch in chunks:
        ws = ch.get("words") or []
        t0, t1 = float(ch.get("t0", 0)), float(ch.get("t1", 0))
        bid = c.beat_id(t0) if hasattr(c, "beat_id") else None
        pf = profs.get(ch.get("profile")) or {}
        if not ws:
            continue
        s0 = min(float(w.get("s", 0)) for w in ws)
        # sync: on screen at most max_lead_s before the first word, never late; not cut before the last word ends
        if not legacy and s0 - t0 > prm["max_lead_s"] + 1e-3 and float(ch.get("t0", 0)) == round(ch.get("f0", 0) / 30, 4):
            counts["sync"] += 1
            out.append(fail("V-CAPTION", bid, t0, f"caption '{ch.get('text')}' appears {round((s0 - t0) * 1000)} ms before "
                            f"its first word (max {int(prm['max_lead_s'] * 1000)} ms)", "lower the profile's lead_frames (≤ 4)"))
        if t0 - s0 > prm["max_lag_s"] + 1e-3 and float(ch.get("t0", 0)) == round(ch.get("f0", 0) / 30, 4):
            counts["sync"] += 1
            out.append(fail("V-CAPTION", bid, t0, f"caption '{ch.get('text')}' appears {round((t0 - s0) * 1000)} ms after its "
                            "first word is spoken", "check the word timings (veos captions build) or the previous chunk's hold"))
        last_e = max(float(w.get("e", 0)) for w in ws)
        if not legacy and not ch.get("stack") and t1 < last_e - prm["cut_tol_s"] - 0.034:
            nxt = next((d for d in chunks if d is not ch and float(d.get("t0", 0)) >= t1 - 1e-6), None)
            if nxt is None or float(nxt.get("t0", 0)) > t1 + 1e-6:
                counts["sync"] += 1
                out.append(fail("V-CAPTION", bid, t1, f"caption '{ch.get('text')}' leaves the screen while its last word is "
                                "still spoken", "raise tail_s / pause_hold_s in the profile"))
        # chunk limits
        if not legacy:
            wr = pf.get("words") or [1, 99]
            n_words = len(ws)
            glued = n_words > 1 and all(X.is_number(w.get("t", "")) or X.is_unit(w.get("t", "")) or X.is_currency(w.get("t", ""))
                                        or str(w.get("t", ""))[:1].isupper() for w in ws)
            if n_words > int(wr[1]) and not glued and not ch.get("variant") == "stack":
                counts["limits"] += 1
                out.append(fail("V-CAPTION", bid, t0, f"caption '{ch.get('text')}' has {n_words} words (max {wr[1]})",
                                "add a break override or lower the profile's word limit"))
            lines = ch.get("lines") or [list(range(n_words))]
            if pf.get("lines") and len(lines) > int(pf["lines"]):
                counts["limits"] += 1
                out.append(fail("V-CAPTION", bid, t0, f"caption '{ch.get('text')}' runs {len(lines)} lines (max {pf['lines']})",
                                "shorten the chunk"))
            mcl = pf.get("max_chars_line")
            if mcl and ch.get("variant") not in ("tiers", "duet"):
                for ln in lines:
                    txt = " ".join(ws[k].get("t", "") for k in ln if k < len(ws))
                    if len(txt) > int(mcl) and len(ln) > 1:
                        counts["limits"] += 1
                        out.append(fail("V-CAPTION", bid, t0, f"caption line '{txt}' is {len(txt)} characters "
                                        f"(max {mcl})", "add a break override or shorten the words"))
            # speaker colour = speaker
            spk = {w.get("spk") for w in ws if w.get("spk") is not None}
            if len(spk) > 1:
                counts["speaker"] += 1
                out.append(fail("V-CAPTION", bid, t0, f"caption '{ch.get('text')}' mixes speakers {sorted(spk)}",
                                "one chunk per speaker turn (check the word speaker labels)"))
            sp = ch.get("speaker")
            if sp is not None and sp in speakers and speakers[sp].get("colour"):
                want = str(speakers[sp]["colour"]).lower()
                if str(ch.get("colour", "")).lower() != want:
                    counts["speaker"] += 1
                    out.append(fail("V-CAPTION", bid, t0, f"caption '{ch.get('text')}' is {ch.get('colour')} but speaker "
                                    f"'{sp}' is {want}", "speaker colours come from captions.speakers; rebuild the captions"))
            # emphasis budget
            emc = (pf.get("emphasis") or {})
            if emc.get("span") == "phrase":  # one emphasis = one phrase: a run of up to PHRASE_MAX adjacent words
                from .capengine import PHRASE_MAX
                em, run = [], 0
                for k, w in enumerate(ws):
                    run = run + 1 if w.get("emph") and k and ws[k - 1].get("emph") else (1 if w.get("emph") else 0)
                    if w.get("emph") and (run - 1) % PHRASE_MAX == 0:
                        em.append(w)
            else:
                em = [w for w in ws if w.get("emph")]
            mpc = int(emc.get("max_per_chunk") or 1) if emc.get("mechanism", "none") != "none" else None
            if em and pf.get("emphasis", {}).get("mechanism", "none") != "none":
                emph_t.setdefault(ch.get("profile"), []).extend(float(w.get("s", 0)) for w in em)
                if mpc is not None and len(em) > mpc:
                    counts["emphasis"] += 1
                    out.append(fail("V-CAPTION", bid, t0, f"caption '{ch.get('text')}' emphasises {len(em)} words (max {mpc})",
                                    "drop an emphasis override"))
        # glossary spelling (E-20) and brand case
        if gl:
            case = ((pf.get("skin") or {}).get("case")) or "sentence"
            for w in ws:
                t = str(w.get("t", ""))
                miss = gl.near_miss(t)
                if miss:
                    counts["spelling"] += 1
                    out.append(fail("V-CAPTION", bid, float(w.get("s", t0)), f"'{X.core(t)}' looks like a misspelling of "
                                    f"'{miss}'", f"fix it with a captions override {{\"from\": \"{X.core(t)}\", \"to\": \"{miss}\"}} "
                                    "or add the word to plan/glossary.json"))
                elif prm["brand_case"] and case in ("sentence", "as_spoken", "title") and not legacy:
                    canon = gl.canon(t)
                    if canon and " " not in canon and X.core(t) != canon and X.core(t).lower() == canon.lower():
                        counts["spelling"] += 1
                        out.append(fail("V-CAPTION", bid, float(w.get("s", t0)), f"brand '{X.core(t)}' should read '{canon}'",
                                        "brand names are written exactly (glossary)"))
    # emphasis rate per profile
    for pid, ts in emph_t.items():
        rate = ((profs.get(pid) or {}).get("emphasis") or {}).get("max_per_s")
        if not rate:
            continue
        gap = 1.0 / float(rate)
        ts = sorted(ts)
        for a, b in zip(ts, ts[1:]):
            if b - a < gap - 0.05 and b - a > 0.0:
                counts["emphasis"] += 1
                out.append(fail("V-CAPTION", c.beat_id(b) if hasattr(c, "beat_id") else None, b,
                                f"emphasis {b - a:.2f} s after the previous one (budget: one per {gap:.1f} s)",
                                "drop an emphasis override (the engine keeps its own picks inside the budget)"))
    c.stats_extra["captions"] = {"source": src, "chunks": len(chunks), "legacy": legacy, "failures": counts,
                                 "emphasis": sum(len(v) for v in emph_t.values()),
                                 "profiles": sorted({ch.get("profile") for ch in chunks})}
    return out
