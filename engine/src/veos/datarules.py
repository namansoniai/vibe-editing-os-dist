"""V-DATA and V-NUMFMT (E-08; structure §18, SW-08, §5.5, NC-6). Registered in validate.REGISTRY.

V-DATA (runs when the reel has plan/figures.json, a scene bound to a figure, or the style's `modules.data_figures`):
  - figures.json resolves: provenance on every input (script + said, creator, spoken@t, source:<id>), known formulas
    (and allowed by `data.formulas`), no literal claims, scale maxima >= the data;
  - every stated value (step / figure `value`) equals the recomputed formula at display precision (+- round_to / 2);
  - every number in a bound scene's `text_content` is a value of its figures (inputs, steps, outputs, axis x) and a
    data-kind scene (counter, bar, ...) that shows numbers is bound to a figure (provenance);
  - every spoken number in a data beat (a beat whose layers include a bound scene) is in figures.json;
  - `spoken@t` inputs are really spoken near t;
  - scenes that draw one `scale_id` declare the same axis max (= the resolved scale), and compared figures in one
    scene share a scale_id;
  - counters (`lands: [{t, value | figure + step}]`) land within +-land_frames (5) of the spoken number word.
  Blocking (facts): figures.json errors, stated vs recomputed values, numbers in bound / data scenes that are not
  their figures' values, `spoken@t` inputs that were not spoken. Advice (validate's levels): incidental numbers on
  screen ("2025", "10x"), shared scales, counters on the word, spoken numbers missing from figures.json. Made-up
  (illustrative) figures need no label.
V-NUMFMT: every number written in a scene (text_content, and the measured texts when plan/measure.text.json exists)
  follows the profile's numbers: grouping (a wrong rupee grouping fails), currency glyph (₹, not Rs / INR), compact
  system (no K/M/B on ₹ amounts in a lakh/crore style; no lakh/crore in a K/M/B style), decimals, units (dual shows
  both); figure-bound numbers are written exactly as fmt_num(value, figure format) writes them (ctx.fmtNum does).
  Verbatim text is exempt: a scene with `verbatim: true`, and numbers inside its `quote_text` / `headline` / `quote`
  (a headline that says "Rs 500 crore" is shown as published).
Scene meta fields: figure | figures, lands, scale {id, max} | scales [...], kind, text_content, verbatim, quote_text,
headline.
"""
from __future__ import annotations

import re

from .figures import KINDS, load_resolved, numbers_profile, stated_mismatch
from .numfmt import KMB_SUF, LAKH_SUF, UNITS, PAIR, fmt_num, group, parse_numbers, resolve_spec, same_number, spoken_numbers
from .vcommon import advice, fail, get_path

DATA_KINDS = set(KINDS) | {"chart", "data", "figure"}
VERBATIM_KEYS = ("quote_text", "headline", "quote")  # scene fields holding verbatim third-party text (V-NUMFMT skips it)
COMPARE_KINDS = {"bar", "bar_race", "line"}
_UNSET = object()


def _figures(c):
    figs = c.__dict__.get("figures", _UNSET)
    if figs is _UNSET:
        proj = getattr(c, "project", None)
        figs = load_resolved(proj, c.style, c.warnings) if proj is not None else None
        c.figures = figs
    return figs


def bound_ids(s: dict) -> list[str]:
    ids = []
    if s.get("figure"):
        ids.append(str(s["figure"]))
    for x in s.get("figures") or []:
        if str(x) not in ids:
            ids.append(str(x))
    return ids


def _words(c) -> list[dict]:
    w = c.words
    if isinstance(w, dict):
        w = w.get("words")
    return [x for x in (w or []) if isinstance(x, dict)]


def _cands(figs: dict, ids: list[str] | None) -> list[tuple[float, float, str]]:
    """(value, extra tolerance, source) of figures `ids` (None = every figure) + every input."""
    out = []
    for name, inp in (figs.get("inputs") or {}).items():
        if isinstance(inp.get("value"), (int, float)):
            out.append((float(inp["value"]), 0.0, f"input {name}"))
    for fid, r in (figs.get("figures") or {}).items():
        if ids is not None and fid not in ids:
            continue
        tol = float(r.get("round_to") or 0) / 2
        for st in r["steps"]:
            for k in ("shown", "computed", "value", "x"):
                v = st.get(k)
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    out.append((float(v), tol, f"figure {fid}"))
        for k, v in (r.get("outputs") or {}).items():
            if isinstance(v, (int, float)):
                out.append((float(v), tol, f"figure {fid}.{k}"))
    return out


def _match(val: float, half: float, cands) -> bool:
    return any(same_number(val, cv, half, tol) or same_number(cv, val, half, tol) for cv, tol, _ in cands)


def _nearest(val: float, cands):
    return min(cands, key=lambda x: abs(x[0] - val)) if cands else None


def _active(c) -> bool:
    return bool(get_path(c.style, "profile.modules.data_figures", False))


# --------------------------------------------------------------------------- V-DATA
def rule_data(c, p: dict):
    figs = _figures(c)
    bound = [s for s in c.scenes if bound_ids(s)]
    datak = [s for s in c.scenes if s.get("kind") in DATA_KINDS and parse_numbers(s.get("text_content", ""))]
    if figs is None and not bound and not (_active(c) and datak) and not p.get("require"):
        return []
    out = []
    fps = c.fps or 30
    land_f = float(p.get("land_frames", 5))
    if figs is None:
        for s in bound + [s for s in datak if s not in bound]:
            out.append(fail("V-DATA", c.beat_id(s.get("t_in", 0)), s.get("t_in", 0),
                            f"scene {s.get('id')} shows data numbers but the reel has no plan/figures.json",
                            "write plan/figures.json: each number as an input with provenance or a formula over inputs (§18)"))
        return out
    recs = figs.get("figures") or {}
    for e in figs.get("errors") or []:
        fid = e.get("figure")
        t = _fig_t(recs.get(fid)) if fid else 0.0
        out.append(fail("V-DATA", c.beat_id(t), t, e["msg"], e["fix"]))
    # stated values vs the recomputed formula
    for fid, r in recs.items():
        if r.get("illustrative"):
            continue
        for st in r["steps"]:
            comp_txt = stated_mismatch(r, st)
            if comp_txt:
                t = float(st.get("at") or _fig_t(r))
                said = fmt_num(st["value"], r["format"])
                where = f" (step {st['i']}" + (f", x={st['x']}" if st.get("x") is not None else "") + ")" if len(r["steps"]) > 1 else ""
                out.append(fail("V-DATA", c.beat_id(t), t,
                                f"figure {fid}{where} states {said} but {r['formula']} recomputes {comp_txt}",
                                f"show {comp_txt} (or fix the inputs); if the creator rounds, declare round_to on the figure"))
    words = _words(c)
    spoken_all = spoken_numbers(words) if words else []
    all_c = _cands(figs, None)
    # bound scenes: text numbers, illustrative label, scales
    scale_seen: dict[str, list[tuple[str, float]]] = {}
    for s in c.scenes:
        ids = bound_ids(s)
        t = float(s.get("t_in", 0))
        if not ids:
            toks = parse_numbers(s.get("text_content", ""))
            if s.get("kind") in DATA_KINDS and toks:
                out.append(fail("V-DATA", c.beat_id(t), t,
                                f"{s.get('kind')} scene {s.get('id')} shows numbers ('{str(s.get('text_content'))[:60]}') "
                                "with no figure behind them (no provenance)",
                                f"bind it to a figure (figure: '<id>' in the scene) declared in plan/figures.json"))
            elif s.get("text_class") != "TC-decorative":
                # any other number on screen traces to figures.json or to the words (script provenance), NC-6
                for tok in toks:
                    small = not tok["currency"] and not tok["compact"] and not tok["percent"] and abs(tok["value"]) <= 12                         and tok["decimals"] == 0
                    if small or _match(tok["value"], tok["half"], all_c) or any(
                            same_number(sp["value"], tok["value"], sp["half"]) or same_number(tok["value"], sp["value"], tok["half"])
                            for sp in spoken_all):
                        continue
                    out.append(advice(fail("V-DATA", c.beat_id(t), t,
                                    f"scene {s.get('id')} shows {tok['raw']}, which is neither in figures.json nor spoken",
                                    "if it is a claim, add it to plan/figures.json with provenance; an incidental number is fine")))
            continue
        unknown = [i for i in ids if i not in recs]
        for i in unknown:
            out.append(fail("V-DATA", c.beat_id(t), t, f"scene {s.get('id')} is bound to figure '{i}', which figures.json does not declare",
                            f"add figure '{i}' to plan/figures.json or fix the id"))
        known = [i for i in ids if i in recs]
        cands = _cands(figs, known)
        text = str(s.get("text_content", "") or "")
        toks = parse_numbers(text)
        for tok in toks:
            if not _match(tok["value"], tok["half"], cands):
                nb = _nearest(tok["value"], cands)
                hint = f"; nearest is {fmt_num(nb[0], recs[known[0]]['format'] if known else None)} ({nb[2]})" if nb else ""
                out.append(fail("V-DATA", c.beat_id(t), t,
                                f"scene {s.get('id')} shows {tok['raw']}, which is not a value of {', '.join(known) or 'its figures'}{hint}",
                                "show the figure's value (ctx.fmtNum(ctx.fig(id).shown, id)), or add the number to figures.json with provenance"))
        comp = [i for i in known if recs[i].get("kind") in COMPARE_KINDS]
        if len(comp) >= 2 and len({recs[i].get("scale_id") for i in comp}) > 1:
            out.append(advice(fail("V-DATA", c.beat_id(t), t,
                            f"scene {s.get('id')} compares {', '.join(comp)} on different scales "
                            f"({', '.join(str(recs[i].get('scale_id')) for i in comp)})",
                            "consider one scale_id for compared figures (same axes, §8.5)")))
        decl = s.get("scales") or ([s["scale"]] if isinstance(s.get("scale"), dict) else [])
        for sc in decl:
            if isinstance(sc, dict) and sc.get("id") is not None and isinstance(sc.get("max"), (int, float)):
                scale_seen.setdefault(str(sc["id"]), []).append((str(s.get("id")), float(sc["max"])))
    for sid, rows in scale_seen.items():
        ref = (figs.get("scales") or {}).get(sid)
        want = float(ref["max"]) if ref and isinstance(ref.get("max"), (int, float)) else rows[0][1]
        for scid, mx in rows:
            if abs(mx - want) > max(1e-6, 0.005 * abs(want)):
                sc = next((x for x in c.scenes if str(x.get("id")) == scid), {})
                t = float(sc.get("t_in", 0))
                out.append(advice(fail("V-DATA", c.beat_id(t), t,
                                f"scene {scid} draws scale {sid} with axis max {mx:g}; the shared max is {want:g}",
                                f"consider ctx.figScale('{sid}').max (= {want:g}) so compared bars share one axis")))
    # counters land on the spoken number
    spoken = spoken_all
    n_lands = 0
    for s in c.scenes:
        for L in s.get("lands") or []:
            if not isinstance(L, dict) or not isinstance(L.get("t"), (int, float)):
                continue
            n_lands += 1
            val, rec, st = _land_value(L, s, recs)
            if val is None:
                continue
            tol = float((rec or {}).get("round_to") or 0) / 2
            lt = float(L["t"])
            ref_t, said = None, None
            if spoken:
                hits = [sp for sp in spoken if abs(sp["s"] - lt) <= 3.0 and same_number(sp["value"], val, sp["half"], tol)]
                if hits:
                    h = min(hits, key=lambda sp: (abs(sp["value"] - val) > 0.5 + tol, abs(sp["s"] - lt)))  # exact words first
                    ref_t, said = h["s"], h["text"]
            if ref_t is None and st is not None and isinstance(st.get("at"), (int, float)):
                ref_t, said = float(st["at"]), None  # no matching number word: the step's declared word time
            if ref_t is None:
                if spoken:
                    c.warnings.append(f"V-DATA: counter {s.get('id')} lands on {fmt_num(val, (rec or {}).get('format'))} "
                                      f"at {lt:.2f} s but no matching spoken number is within 3 s")
                continue
            off = (lt - ref_t) * fps
            if abs(off) > land_f + 1e-6:
                out.append(advice(fail("V-DATA", c.beat_id(lt), lt,
                                f"counter {s.get('id')} lands on {fmt_num(val, (rec or {}).get('format'))} at {lt:.2f} s, "
                                f"{off:+.0f} frames from " + (f"the spoken '{said}'" if said else "its step's word time `at`")
                                + f" ({ref_t:.2f} s)",
                                f"consider landing the count at {ref_t:.2f} s (the step's `at` = the word time)")))
    # spoken numbers in data beats are in figures.json
    n_spoken = 0
    if spoken:
        bound_ids_set = {str(s.get("id")) for s in bound}
        for b in c.beats:
            if not ({str(x) for x in (b.get("layers") or [])} & bound_ids_set or b.get("figures")):
                continue
            t0, t1 = float(b.get("t0", 0)), float(b.get("t1", 0))
            for sp in spoken:
                if not (t0 - 1e-6 <= sp["s"] < t1 - 1e-6):
                    continue
                n_spoken += 1
                if sp["by_words"] and sp["value"] <= float(p.get("ignore_word_counts_upto", 3)):
                    continue
                if not _match(sp["value"], sp["half"], all_c):
                    out.append(advice(fail("V-DATA", b.get("id"), sp["s"],
                                    f"'{sp['text']}' is spoken in data beat {b.get('id')} but is not in figures.json",
                                    "if the screen shows it, add it as an input (from: spoken@t or script) or a figure value")))
    # spoken@t inputs
    if words:
        for name, inp in (figs.get("inputs") or {}).items():
            src = str(inp.get("from") or "")
            if not src.startswith("spoken@") or not isinstance(inp.get("value"), (int, float)):
                continue
            try:
                t = float(src.split("@", 1)[1])
            except ValueError:
                continue
            if not any(abs(sp["s"] - t) <= 0.75 and same_number(sp["value"], float(inp["value"]), sp["half"]) for sp in spoken):
                out.append(fail("V-DATA", c.beat_id(t), t, f"input '{name}' = {inp['value']:g} is declared spoken@{t:g}, "
                                "but no matching number word is spoken within 0.75 s",
                                "fix the time or the value, or change `from` to script / creator"))
    c.stats_extra["data"] = {"figures": len(recs), "steps": sum(len(r["steps"]) for r in recs.values()),
                             "bound_scenes": len(bound), "counters": n_lands, "spoken_in_data_beats": n_spoken,
                             "scales": {k: v.get("max") for k, v in (figs.get("scales") or {}).items()}}
    return out


def _fig_t(r) -> float:
    if not r:
        return 0.0
    ats = [st.get("at") for st in r.get("steps") or [] if isinstance(st.get("at"), (int, float))]
    return float(ats[0]) if ats else 0.0


def _land_value(L: dict, s: dict, recs: dict):
    fid = L.get("figure") or s.get("figure") or ((s.get("figures") or [None])[0])
    rec = recs.get(str(fid)) if fid is not None else None
    st = None
    if rec is not None:
        i = L.get("step")
        if isinstance(i, int) and 0 <= i < len(rec["steps"]):
            st = rec["steps"][i]
        elif i is None and len(rec["steps"]) == 1:
            st = rec["steps"][0]
    val = L.get("value")
    if not isinstance(val, (int, float)) or isinstance(val, bool):
        val = st.get("shown") if st else (rec.get("shown") if rec else None)
    return (float(val) if isinstance(val, (int, float)) else None), rec, st


# --------------------------------------------------------------------------- V-NUMFMT
def _texts(c, include_captions: bool):
    seen, out = set(), []
    for s in c.scenes:
        t = str(s.get("text_content", "") or "")
        if t and (s.get("id"), t) not in seen:
            seen.add((s.get("id"), t))
            out.append((s, t, "text_content"))
    by_id = {str(s.get("id")): s for s in c.scenes}
    for n, fr in sorted((c.text_measure or {}).items()):
        for e in (fr or {}).get("texts") or []:
            sid, t = str(e.get("scene", "")), str(e.get("text", "") or "")
            if not t or (sid.startswith("__") and not include_captions) or (sid, t) in seen:
                continue
            seen.add((sid, t))
            out.append((by_id.get(sid, {"id": sid, "t_in": int(n) / (c.fps or 30)}), t, f"measured frame {n}"))
    return out


def rule_numfmt(c, p: dict):
    prof = resolve_spec({k: v for k, v in p.items() if k not in ("from", "captions", "legacy")}, numbers_profile(c.style))
    grouping, currency, compact = prof.get("grouping"), str(prof.get("currency") or ""), prof.get("compact")
    decimals = int(prof.get("decimals") or 0)
    figs = _figures(c) or {}
    recs = figs.get("figures") or {}
    out, seen = [], set()

    def add(s, key, msg, fix):
        if (s.get("id"), key) in seen:
            return
        seen.add((s.get("id"), key))
        t = float(s.get("t_in", 0) or 0)
        out.append(fail("V-NUMFMT", c.beat_id(t), t, msg, fix))

    texts = _texts(c, bool(p.get("captions")))
    for s, text, src in texts:
        sid = s.get("id")
        if s.get("verbatim"):  # a verbatim headline / quote card: its words are someone else's (NC-13), not ours to format
            continue
        quoted = [t["raw"] for k in VERBATIM_KEYS if s.get(k) for t in parse_numbers(str(s[k]))]
        for tok in parse_numbers(text):
            raw, g = tok["raw"], tok["grouping"]
            if raw in quoted:  # this number is inside the verbatim headline / quote
                quoted.remove(raw)
                continue
            if grouping in ("indian", "international") and g in ("invalid", "indian" if grouping == "international" else "international"):
                good = _regroup(raw, grouping)
                add(s, ("group", raw), f"scene {sid} writes {raw} ({src}): {'international' if g == 'international' else g + ' (broken)' if g == 'invalid' else g} "
                                       f"digit grouping; this style groups the {grouping} way ({good})",
                    f"write {good} (ctx.fmtNum formats it)")
            elif grouping in ("indian", "international") and g == "none" and tok["int_digits"] >= 5 and not tok["compact"] and not tok["percent"]:
                good = _regroup(raw, grouping)
                add(s, ("nogroup", raw), f"scene {sid} writes {raw} ({src}) with no digit grouping", f"write {good}")
            cur = tok["currency"]
            if currency == "₹" and cur and cur.rstrip(".").lower() in ("rs", "inr"):
                add(s, ("cur", raw), f"scene {sid} writes {raw} ({src}); this style writes the rupee glyph ₹", f"write {raw.replace(cur, '₹').replace('₹ ', '₹')}")
            if compact == "lakh_crore" and tok["compact"] in KMB_SUF and (cur or currency and _bound_money(s, recs)):
                add(s, ("kmb", raw), f"scene {sid} writes {raw} ({src}): K/M/B on a money amount in a lakh/crore style",
                    f"write {fmt_num(tok['value'], 'short', prof)} (lakh / crore)")
            if compact == "k_m_b" and tok["compact"] in LAKH_SUF:
                add(s, ("lakh", raw), f"scene {sid} writes {raw} ({src}): lakh/crore in a K/M/B style",
                    f"write {fmt_num(tok['value'], 'short', prof)}")
            if cur and not tok["compact"] and not tok["percent"] and tok["decimals"] > decimals:
                add(s, ("dec", raw), f"scene {sid} writes {raw} ({src}) with {tok['decimals']} decimals (style: {decimals})",
                    f"write {fmt_num(tok['value'], {'currency': cur}, prof)}")
        # figure-bound numbers are written the way the figure's format writes them (the nearest bound value decides)
        bvals = [(fid, st["shown"]) for fid in bound_ids(s) if recs.get(fid) and src == "text_content"
                 for st in recs[fid]["steps"] if isinstance(st.get("shown"), (int, float))]
        if bvals:
            for tok in parse_numbers(text):
                fid, v = min(bvals, key=lambda x: abs(x[1] - tok["value"]))
                r = recs[fid]
                if not same_number(tok["value"], v, tok["half"], float(r.get("round_to") or 0) / 2):
                    continue
                want = fmt_num(v, r["format"])
                if tok["raw"] != want and want not in text:
                    add(s, ("fmt", fid, tok["raw"]), f"scene {sid} writes {tok['raw']} for figure {fid}; its format writes {want}",
                        f"format it with ctx.fmtNum(value, '{fid}')")
        for fid in bound_ids(s):
            r = recs.get(fid)
            if not r or src != "text_content":
                continue
            vals = [st["shown"] for st in r["steps"] if isinstance(st.get("shown"), (int, float))]
            unit = str(r["format"].get("unit") or "").lower()
            if prof.get("units") == "dual" and unit in UNITS and unit in PAIR and vals:
                other = UNITS[PAIR[unit]][3]
                if other not in text:
                    add(s, ("dual", fid), f"scene {sid} shows figure {fid} in {UNITS[unit][3]} only; this style shows dual units",
                        f"show both ({fmt_num(vals[-1], {**r['format'], 'units': 'dual'})})")
    c.stats_extra["numfmt"] = {"grouping": grouping, "currency": currency, "compact": compact, "texts": len(texts)}
    return out


def _regroup(raw: str, grouping: str) -> str:
    """The same written number with its integer digits grouped the given way (1,31,190 <-> 131,190)."""
    def sub(m):
        ip, dot, fr = m.group(0).partition(".")
        return group(int(ip.replace(",", "")), grouping) + (dot + fr if dot else "")
    return re.sub(r"\d[\d,]*(?:\.\d+)?", sub, raw, count=1)


def _bound_money(s, recs) -> bool:
    return any((recs.get(f) or {}).get("format", {}).get("currency") for f in bound_ids(s))
