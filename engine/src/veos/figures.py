"""`veos figures`: the data contract (E-08; structure §18). Resolve plan/figures.json with the safe formula library.

Every displayed number of a data beat is a declared **input** with provenance or a **formula** over inputs:

plan/figures.json
{
  "version": 1,
  "inputs": {                                   # named values; provenance `from` is required
    "loan":  {"value": 250000, "unit": "INR", "from": "script", "said": "₹2.5 lakhs"},
    "years": {"value": 10, "from": "spoken@4.1"},             # a number word in the transcript near t (V-DATA checks it)
    "rate":  {"value": 8, "unit": "%", "from": "creator"}      # the creator gave it when asked
  },                                            # from: script (+ said) | creator | spoken@<t> | source:<citation id>
  "scales": {"S-int": {"max": 200000}},         # optional fixed axis maxima (else the max of the figures' values)
  "figures": [
    {"id": "flat", "kind": "bar", "label": "8% flat",
     "formula": "flat_rate_interest", "args": {"principal": "loan", "rate_pct": "rate", "years": "years"},
     "output": "interest_paid",                 # which output of the formula is shown (default: the formula's main one)
     "steps": [{"x": 2, "args": {"elapsed_years": 2}, "value": 40000, "at": 7.1}, ...],
     "value": 200000,                           # the stated (shown) value when there are no steps
     "round_to": 10,                            # the creator rounds shown values to 10 (tolerance +-5)
     "scale_id": "S-int", "format": {"style": "full"}, "illustrative": false}
  ]
}

An arg is an input name, `fig:<id>` / `fig:<id>.<output>` (another figure's final computed value), an inline input
`{"value", "from", "said"?}`, a list of those (sum, stacked_discount), or a literal number for a **setting** parameter
(per_year, elapsed_years, periods, from, to). A literal for a **claim** parameter (principal, rate_pct, ...) has no
provenance and is an error. `value` on a step / figure is what the reel says and shows; the engine recomputes it
(`computed`) and V-DATA compares the two at display precision (+- round_to / 2). Shown = value when stated, else computed.

Writes work/figures.json (what the bundle carries as `figures`; `ctx.fig(id)` in a scene):
{version, numbers, inputs {name: {value, unit, from, said}}, figures {id: {id, kind, label, formula, output, format,
 scale_id, illustrative, round_to, steps: [{i, x, at, value, computed, shown, text}], value, computed, shown, text,
 outputs}}, scales {id: {max, min, figures}}, errors [{figure, msg, fix}]}
"""
from __future__ import annotations

import math
import re

from .core import VeosError, need_project, read_json, write_json
from .numfmt import convert, fmt_num, parse_numbers, resolve_spec, same_number

KINDS = ("bar", "bar_race", "counter", "slider", "ledger", "donut", "grid_fill", "line", "hero_number", "table")
PROVENANCE = ("script", "creator", "buyer", "spoken@", "source:", "figure:")


# ------------------------------------------------------------------ the safe formula library (pure, no eval)
def _pow(base: float, e: float) -> float:
    return math.pow(base, e)


def f_sum(a):
    return {"value": float(sum(a["values"]))}


def f_diff(a):
    return {"value": a["a"] - a["b"], "abs": abs(a["a"] - a["b"])}


def f_ratio(a):
    return {"value": a["a"] / a["b"], "pct": a["a"] / a["b"] * 100.0}


def f_percent_change(a):
    return {"value": (a["new"] - a["old"]) / a["old"] * 100.0, "delta": a["new"] - a["old"]}


def f_stacked_discount(a):
    keep = 1.0
    for d in a["discounts_pct"]:
        keep *= 1.0 - d / 100.0
    out = {"value": (1.0 - keep) * 100.0, "pay_pct": keep * 100.0}
    if a.get("price") is not None:
        out["final"] = a["price"] * keep
        out["saved"] = a["price"] - out["final"]
    return out


def f_simple_interest(a):
    i = a["principal"] * a["rate_pct"] / 100.0 * a["years"]
    return {"interest": i, "total": a["principal"] + i}


def f_flat_rate_interest(a):
    """Flat rate: interest on the full principal every year. EMI = (P + P*r*years) / (years * per_year)."""
    p, r, y, k = a["principal"], a["rate_pct"] / 100.0, a["years"], a.get("per_year") or 12
    total_i = p * r * y
    el = a.get("elapsed_years")
    el = y if el is None else min(float(el), y)
    return {"interest": total_i, "interest_paid": p * r * el, "emi": (p + total_i) / (y * k), "total_paid": p + total_i}


def f_reducing_balance_emi(a):
    """Reducing balance: interest each period on what is still owed. EMI = P i (1+i)^n / ((1+i)^n - 1), i = r / per_year.

    elapsed_years -> interest_paid (cumulative interest after that many years) and balance."""
    p, r, y, k = a["principal"], a["rate_pct"] / 100.0, a["years"], a.get("per_year") or 12
    n = int(round(y * k))
    i = r / k
    emi = p / n if i == 0 else p * i * _pow(1 + i, n) / (_pow(1 + i, n) - 1)
    el = a.get("elapsed_years")
    m = n if el is None else min(int(round(float(el) * k)), n)
    bal = p - emi * m if i == 0 else p * _pow(1 + i, m) - emi * (_pow(1 + i, m) - 1) / i
    if m == n:
        bal = 0.0  # paid off (removes the float residue)
    paid_i = emi * m - (p - bal)
    return {"emi": emi, "total_interest": emi * n - p, "total_paid": emi * n, "interest_paid": paid_i, "balance": bal}


def f_compound(a):
    """Future value with compounding per_year times a year, plus an optional contribution each period (SIP, end of period)."""
    p, r, y, k = a["principal"], a["rate_pct"] / 100.0, a["years"], a.get("per_year") or 1
    c = a.get("contribution") or 0.0
    n, i = y * k, r / k
    g = _pow(1 + i, n)
    fv = p * g + (c * (g - 1) / i if i else c * n)
    inv = p + c * n
    return {"value": fv, "invested": inv, "gain": fv - inv}


def f_cagr(a):
    return {"value": (_pow(a["end"] / a["start"], 1.0 / a["years"]) - 1.0) * 100.0}


def f_per_period(a):
    return {"value": a["total"] / a["periods"]}


def f_unit_convert(a):
    if a.get("rate") is not None:  # currency or any declared rate: value x rate (the rate needs provenance)
        return {"value": a["value"] * a["rate"]}
    return {"value": convert(a["value"], str(a["from"]).lower(), str(a["to"]).lower())}


def f_none(a):
    return {"value": a["value"]}


# name -> (function, claim params (need provenance), setting params (literals allowed), optional params, main output)
FORMULAS = {
    "sum": (f_sum, ("values",), (), (), "value"),
    "diff": (f_diff, ("a", "b"), (), (), "value"),
    "ratio": (f_ratio, ("a", "b"), (), (), "value"),
    "percent_change": (f_percent_change, ("old", "new"), (), (), "value"),
    "stacked_discount": (f_stacked_discount, ("discounts_pct",), (), ("price",), "value"),
    "simple_interest": (f_simple_interest, ("principal", "rate_pct", "years"), (), (), "interest"),
    "flat_rate_interest": (f_flat_rate_interest, ("principal", "rate_pct", "years"), ("per_year", "elapsed_years"), (), "interest"),
    "reducing_balance_emi": (f_reducing_balance_emi, ("principal", "rate_pct", "years"), ("per_year", "elapsed_years"), (), "emi"),
    "compound": (f_compound, ("principal", "rate_pct", "years"), ("per_year",), ("contribution",), "value"),
    "cagr": (f_cagr, ("start", "end", "years"), (), (), "value"),
    "per_period": (f_per_period, ("total",), ("periods",), (), "value"),
    "unit_convert": (f_unit_convert, ("value",), ("from", "to"), ("rate",), "value"),
    "none": (f_none, ("value",), (), (), "value"),
}
SETTING_LISTS = {"discounts_pct"}  # lists whose items are refs too


def compute(formula: str, args: dict) -> dict:
    """Run one formula on plain numbers (unit tests, the planner's own checks). Raises KeyError / ValueError."""
    fn = FORMULAS[formula][0]
    return fn(args)


# ------------------------------------------------------------------ resolution
def _provenance_error(name: str, inp: dict) -> str | None:
    src = str(inp.get("from") or "")
    if not src:
        return f"input '{name}' has no provenance (`from`: script | creator | spoken@<t> | source:<id>)"
    if not any(src == p or (p.endswith(("@", ":")) and src.startswith(p) and len(src) > len(p)) for p in PROVENANCE):
        return f"input '{name}' has an unknown provenance '{src}'"
    if src.startswith("spoken@"):
        try:
            float(src.split("@", 1)[1])
        except ValueError:
            return f"input '{name}': spoken@ needs the edit-time seconds of the number word (spoken@4.1)"
    if src == "script":
        said = str(inp.get("said") or "").strip()
        if not said:
            return f"input '{name}' comes from the script but has no `said` (the words that state it)"
        got = parse_numbers(said)
        val = inp.get("value")
        if got and isinstance(val, (int, float)) and not any(same_number(g["value"], float(val), g["half"]) for g in got):
            return f"input '{name}' = {val} but the script words '{said}' say {got[0]['raw']}"
    return None


class _Resolver:
    def __init__(self, doc: dict, base_numbers: dict, allowed: list | None):
        self.doc, self.base, self.allowed = doc, base_numbers or {}, allowed
        self.inputs = {k: v for k, v in (doc.get("inputs") or {}).items() if isinstance(v, dict)}
        self.figs = {}
        for f in doc.get("figures") or []:
            if isinstance(f, dict) and f.get("id") is not None:
                self.figs[str(f["id"])] = f
        self.out: dict[str, dict] = {}
        self.errors: list[dict] = []
        self.busy: set[str] = set()

    def err(self, fig, msg, fix):
        self.errors.append({"figure": fig, "msg": msg, "fix": fix})

    def ref(self, fid: str, pname: str, v, claim: bool):
        """An arg value -> float (None on error)."""
        if isinstance(v, bool):
            v = None
        if isinstance(v, (int, float)):
            if claim:
                self.err(fid, f"figure {fid}: '{pname}' is the literal {v}, which has no provenance",
                         f"declare it in figures.json `inputs` with `from` (script + said, creator, spoken@t) and refer to it by name")
                return None
            return float(v)
        if isinstance(v, dict):
            pe = _provenance_error(f"{fid}.{pname}", v)
            if pe:
                self.err(fid, pe, "give the inline input a `from` (and `said` for script numbers)")
                return None
            try:
                return float(v["value"])
            except (KeyError, TypeError, ValueError):
                self.err(fid, f"figure {fid}: inline input '{pname}' has no numeric value", "set `value`")
                return None
        if isinstance(v, str):
            if v.startswith("fig:"):
                tid, _, outk = v[4:].partition(".")
                r = self.figure(tid)
                if r is None:
                    self.err(fid, f"figure {fid}: '{pname}' refers to unknown or broken figure '{tid}'", "fix the figure id")
                    return None
                val = r["outputs"].get(outk) if outk else r["computed"]
                if not isinstance(val, (int, float)):
                    self.err(fid, f"figure {fid}: '{pname}' refers to {v}, which has no numeric output", "pick an output name")
                    return None
                return float(val)
            if v in self.inputs:
                return float(self.inputs[v]["value"]) if isinstance(self.inputs[v].get("value"), (int, float)) else None
            if pname in ("from", "to"):
                return v  # unit ids
            self.err(fid, f"figure {fid}: '{pname}' refers to unknown input '{v}'", f"add '{v}' to figures.json `inputs`")
            return None
        if v is None:
            return None
        self.err(fid, f"figure {fid}: '{pname}' has an unsupported value {v!r}", "use an input name, fig:<id>, or an inline input")
        return None

    def args(self, fid, formula, raw: dict):
        fn, claims, settings, optional, _ = FORMULAS[formula]
        out = {}
        for k, v in raw.items():
            claim = k in claims or k in optional
            if k not in claims and k not in settings and k not in optional:
                self.err(fid, f"figure {fid}: {formula} has no parameter '{k}'",
                         f"{formula} takes {', '.join(claims + settings + optional)}")
                continue
            if isinstance(v, list):
                vals = [self.ref(fid, k, x, True) for x in v]
                out[k] = None if any(x is None for x in vals) else vals
            else:
                out[k] = self.ref(fid, k, v, claim)
        miss = [k for k in claims if out.get(k) is None]
        return out, miss

    def figure(self, fid: str):
        if fid in self.out:
            return self.out[fid]
        f = self.figs.get(fid)
        if f is None or fid in self.busy:
            if fid in self.busy:
                self.err(fid, f"figure {fid} refers to itself through fig: references", "break the cycle")
            return None
        self.busy.add(fid)
        try:
            return self._figure(fid, f)
        finally:
            self.busy.discard(fid)

    def _figure(self, fid, f):
        formula = str(f.get("formula") or "none")
        if formula not in FORMULAS:
            self.err(fid, f"figure {fid}: unknown formula '{formula}'", "use one of: " + ", ".join(k for k in FORMULAS if k != "none"))
            return None
        if self.allowed is not None and formula != "none" and formula not in self.allowed:
            self.err(fid, f"figure {fid}: formula '{formula}' is not in this style's data.formulas", "use one of: " + ", ".join(self.allowed))
        kind = f.get("kind")
        if kind not in KINDS:
            self.err(fid, f"figure {fid}: kind '{kind}' is not a figure kind", "use one of: " + ", ".join(KINDS))
        raw_args = dict(f.get("args") or {})
        if formula == "none" and "value" not in raw_args:
            if f.get("from"):  # a stated value with its own provenance
                raw_args["value"] = {"value": f.get("value"), "from": f.get("from"), "said": f.get("said")}
            elif f.get("input"):
                raw_args["value"] = f.get("input")
        output = str(f.get("output") or FORMULAS[formula][4])
        fmt = resolve_spec(f.get("format"), self.base)
        round_to = float(f.get("round_to") or 0)
        steps_in = f.get("steps") if isinstance(f.get("steps"), list) and f.get("steps") else [None]
        steps, outputs = [], {}
        ok = True
        for i, st in enumerate(steps_in):
            a = dict(raw_args)
            if isinstance(st, dict):
                a.update(st.get("args") or {})
            vals, miss = self.args(fid, formula, a)
            comp = None
            if miss:
                self.err(fid, f"figure {fid}{f' step {i}' if st else ''}: {formula} is missing {', '.join(miss)}",
                         f"give {', '.join(miss)} in `args` (input names with provenance)")
                ok = False
            else:
                try:
                    res = FORMULAS[formula][0]({k: v for k, v in vals.items() if v is not None})
                    outputs = res
                    comp = res.get(output)
                    if output not in res:
                        self.err(fid, f"figure {fid}: {formula} has no output '{output}'", "outputs: " + ", ".join(res))
                        ok = False
                except (ZeroDivisionError, ValueError, KeyError, OverflowError) as e:
                    self.err(fid, f"figure {fid}: {formula} failed ({e})", "check the inputs")
                    ok = False
            stated = (st or {}).get("value") if st else f.get("value")
            if formula == "none" and stated is None:
                stated = None
            stated = float(stated) if isinstance(stated, (int, float)) and not isinstance(stated, bool) else None
            shown = stated if stated is not None else comp
            steps.append({"i": i, "x": (st or {}).get("x"), "label": (st or {}).get("label"), "at": (st or {}).get("at"),
                          "value": stated, "computed": comp, "shown": shown,
                          "text": fmt_num(shown, fmt) if isinstance(shown, (int, float)) else None})
        last = steps[-1]
        rec = {"id": fid, "kind": kind, "label": f.get("label"), "formula": formula, "output": output,
               "format": fmt, "scale_id": f.get("scale_id"), "illustrative": bool(f.get("illustrative")),
               "round_to": round_to, "steps": steps, "value": last["value"], "computed": last["computed"],
               "shown": last["shown"], "text": last["text"], "outputs": outputs, "ok": ok}
        self.out[fid] = rec
        return rec

    def run(self) -> dict:
        for name, inp in self.inputs.items():
            pe = _provenance_error(name, inp)
            if pe:
                self.err(None, pe, "add `from` (script with `said`, creator, spoken@t, source:<id>) to the input")
            if not isinstance(inp.get("value"), (int, float)) or isinstance(inp.get("value"), bool):
                self.err(None, f"input '{name}' has no numeric value", "set `value` to a number")
        for fid in self.figs:
            self.figure(fid)
        scales: dict[str, dict] = {}
        for fid, r in self.out.items():
            sid = r.get("scale_id")
            if not sid:
                continue
            s = scales.setdefault(str(sid), {"max": None, "min": None, "data_max": 0.0, "figures": []})
            s["figures"].append(fid)
            for st in r["steps"]:
                for v in (st["shown"], st["computed"]):
                    if isinstance(v, (int, float)):
                        s["data_max"] = max(s["data_max"], abs(v))
        for sid, s in scales.items():
            fixed = ((self.doc.get("scales") or {}).get(sid) or {}).get("max")
            if isinstance(fixed, (int, float)):
                if fixed < s["data_max"] - 1e-9:
                    self.err(None, f"scale {sid}: max {fixed} is below the largest value {s['data_max']:g}",
                             f"raise scales.{sid}.max to at least {s['data_max']:g}")
                s["max"] = float(fixed)
            else:
                s["max"] = s["data_max"]
            s["min"] = 0.0
        return {"version": 1, "numbers": self.base,
                "inputs": {k: {kk: v.get(kk) for kk in ("value", "unit", "from", "said", "label")} for k, v in self.inputs.items()},
                "figures": self.out, "scales": scales, "errors": self.errors}


def resolve(doc: dict, numbers: dict | None = None, allowed: list | None = None) -> dict:
    """plan/figures.json (dict) -> the resolved figures (see the module doc)."""
    if not isinstance(doc, dict):
        return {"version": 1, "numbers": numbers or {}, "inputs": {}, "figures": {}, "scales": {},
                "errors": [{"figure": None, "msg": "figures.json is not an object", "fix": "write {inputs, figures}"}]}
    return _Resolver(doc, numbers or {}, allowed).run()


def numbers_profile(style: dict | None) -> dict:
    """The style's numbers block: profile.numbers (v3, and synthesised for v1 by tokens.effective_style)."""
    p = ((style or {}).get("profile") or {}).get("numbers")
    if isinstance(p, dict):
        return dict(p)
    lang = str(((style or {}).get("creator") or {}).get("language") or "en").lower()
    ind = lang in ("hinglish", "hi", "ta", "te", "mr", "bn", "kn", "ml", "gu", "pa")
    return {"grouping": "indian" if ind else "international", "currency": "₹" if ind else "$",
            "compact": "lakh_crore" if ind else "k_m_b", "units": "metric", "decimals": 0}


def allowed_formulas(style: dict | None):
    d = (style or {}).get("data")
    return list(d.get("formulas")) if isinstance(d, dict) and isinstance(d.get("formulas"), list) else None


def load_resolved(proj, style: dict | None, warnings: list | None = None) -> dict | None:
    """Resolve <project>/plan/figures.json for this style (None when the file is missing)."""
    fp = proj.root / "plan" / "figures.json"
    if not fp.exists():
        return None
    try:
        doc = read_json(fp)
    except ValueError as e:
        res = resolve({}, numbers_profile(style))
        res["errors"] = [{"figure": None, "msg": f"plan/figures.json is not valid JSON ({e})", "fix": "fix the JSON syntax"}]
        return res
    return resolve(doc, numbers_profile(style), allowed_formulas(style))


def for_bundle(proj, tl: dict, warnings: list) -> tuple[dict | None, dict]:
    """(resolved figures or None, numbers profile) for the render bundle (`ctx.fig`, `ctx.fmtNum`)."""
    style = None
    try:
        from .validate import load_style
        style = load_style(proj, tl, [])
    except Exception as e:  # noqa: BLE001 - the bundle still builds; fmtNum falls back to tokens
        warnings.append(f"figures: could not resolve the style ({getattr(e, 'message', e)})")
    res = load_resolved(proj, style, warnings)
    if res is not None:
        write_json(proj.path("work", "figures.json"), res)
        warnings += [f"figures: {e['msg']}" for e in res["errors"][:5]]
    return res, numbers_profile(style)


# ------------------------------------------------------------------ command
def add_args(p, cmd):
    p.add_argument("--file", default=None, help="figures file (default <project>/plan/figures.json)")


def main(args, project):
    from pathlib import Path
    pr = need_project(project)
    fp = Path(args.file) if getattr(args, "file", None) else pr.root / "plan" / "figures.json"
    if not fp.exists():
        raise VeosError("NO_FIGURES", f"{fp} not found", "Write plan/figures.json (engine/src/veos/figures.py has the format).")
    try:
        doc = read_json(fp)
    except ValueError as e:
        raise VeosError("BAD_FIGURES", f"figures file is not valid JSON: {e}", "Fix the JSON syntax.")
    style = None
    tl = {}
    tp = pr.root / "plan" / "timeline.json"
    if tp.exists():
        try:
            tl = read_json(tp)
        except ValueError:
            tl = {}
    try:
        from .validate import load_style
        style = load_style(pr, tl, [])
    except Exception:  # noqa: BLE001 - no playbook yet: default numbers
        style = None
    res = resolve(doc, numbers_profile(style), allowed_formulas(style))
    dest = pr.path("work", "figures.json")
    write_json(dest, res)
    rows = {}
    for fid, r in res["figures"].items():
        rows[fid] = [(st["text"], fmt_num(st["computed"], r["format"]) if isinstance(st["computed"], (int, float)) else None)
                     for st in r["steps"]][:12]
    return {"out": pr.rel(dest), "figures": len(res["figures"]), "inputs": len(res["inputs"]),
            "scales": {k: v["max"] for k, v in res["scales"].items()}, "shown_vs_computed": rows,
            "errors": res["errors"][:10], "warnings": []}


def stated_mismatch(rec: dict, st: dict) -> str | None:
    """None when the stated value displays the same as the recomputed one (+- round_to / 2), else the computed text."""
    if st.get("value") is None or not isinstance(st.get("computed"), (int, float)):
        return None
    fmt = rec["format"]
    a, b = fmt_num(st["value"], fmt), fmt_num(st["computed"], fmt)
    if a == b or abs(st["value"] - st["computed"]) <= rec.get("round_to", 0) / 2 + 1e-9:
        return None
    return b


def is_number_text(s: str) -> bool:
    return bool(re.search(r"\d", str(s or "")))
