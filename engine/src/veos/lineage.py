"""Buyer-copy lineage (structure Part D.4, tokens.schema §3.2): classify a change against a style copy's `locks`, apply
it, and keep `lineage` (tuned / deviations / fidelity) plus the human log in playbook.md in step.

Buyers can change anything in their copy (structure D.4): every change is applied at once and logged; only the
global quality guarantees are refused. Classes (worst wins when one rule carries several changes):
  VAR   a buyer variable: applied, appended to lineage.tuned
  TUNE  inside its allowed range: applied, appended to lineage.tuned
  DNA   a DNA path, or a TUNE value outside its range: applied, recorded as DV-n in lineage.deviations (no confirmation,
        no warning; the record is only for template upgrades and support)
  NC    breaks the never-bendable core (structure C.1) or a hard engine rule: refused in one friendly line, with the
        nearest allowed alternative

`lineage.fidelity` (faithful / derived) is still computed as an internal note; it never renames the copy and is not
shown to the buyer.

Used by `veos learn add --change` (feedback while editing, "change my playbook") and by `veos templates copy` (the
brand variables). engine/SPEC.md section 8.
"""
from __future__ import annotations

import copy
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

from .core import VeosError, read_json, write_json
from .tokens import EXC_BY_NAME, EXC_REGISTRY, PROTECTED_WORDS, _get_path, _relative, lock_for, schema_version

RANK = {"VAR": 0, "TUNE": 1, "DNA": 2, "NC": 3}
# internal note only: a deviation on any of these marks the copy `derived` (structure D.4); never shown to the buyer
CORE_SWITCHES = ("profile.source_type", "profile.spine", "profile.captions.role", "profile.graphics")
DERIVED_AT = 3
# TUNE enums whose range is "one step" / "adjacent class" (structure D.2)
ORDINALS = {
    "profile.tone.energy": ["calm", "balanced", "hype"], "tone.energy": ["calm", "balanced", "hype"],
    "profile.duration.class": ["micro", "short", "standard", "long"],
}
COMEDY = ["off", "light", "roast"]
# absolute floors per text class (NC-4; structure §0 Definitions)
NC4_FLOOR = {"TC-display": 40, "TC-subtitle": 36, "TC-label": 28, "TC-legal": 22}

ALTERNATIVES = {
    "NC-1": "keep the element beside or below the face (a side card, the chest line, or above the head)",
    "NC-2": "show the two texts one after the other, or nest one inside the other as a declared overlap",
    "NC-3": "ease the move over at least 6 frames, or make it a declared cut",
    "NC-4": "use the smallest legal size for that text class, or put the text on a pill or box for contrast",
    "NC-5": "keep meaning text inside the safe box (y 110-1540, clear of the right button column)",
    "NC-6": "label it as an example, or use a number the script actually says",
    "NC-7": "supply the clip yourself (veos asset add), or let the editor build a created card instead",
    "NC-8": "turn the music bed down or off instead; the mix stays at -14 LUFS with the bed 18 dB under the voice",
    "NC-9": "use a seeded variation instead of true randomness",
    "NC-10": "keep at most 4 bright hues per frame: recolour one role instead of adding a hue",
    "NC-11": "use one soft flash, or a colour pulse without a full-frame luminance jump",
    "NC-12": "keep the disclosure, and change its wording (BV-14) instead",
    "NC-13": "show the quote verbatim, or paraphrase it in the narrator's own caption",
    "NC-14": "keep the blur; crop the screenshot tighter so less of it needs hiding",
    "fixed-meaning": "bad / good / comedy colours keep their meaning; brand your primary or accent colour instead",
    "registry": "stay within the approved exception limits (structure Part C.2)",
}
NC_WHY = {
    "NC-1": "nothing may cover the presenter's face", "NC-2": "meaning texts may not overlap",
    "NC-3": "motion must stay smooth", "NC-4": "text must stay legible (size floors and contrast)",
    "NC-5": "Instagram's UI covers those areas", "NC-6": "no invented facts, numbers or UIs",
    "NC-7": "the editor never fetches other people's media", "NC-8": "the loudness and voice-over-bed limits are fixed",
    "NC-9": "renders must be repeatable", "NC-10": "at most 4 bright hues per frame",
    "NC-11": "flash safety", "NC-12": "sponsors must be disclosed", "NC-13": "quotes stay verbatim",
    "NC-14": "personal identifiers stay blurred", "fixed-meaning": "these colours carry a fixed meaning in every style",
    "registry": "the exception goes beyond the approved registry",
}

LINEAGE_START, LINEAGE_END = "<!-- veos:lineage -->", "<!-- /veos:lineage -->"
APPC_HEAD = "## App. C Lineage & deviations"
APPC_START, APPC_END = "<!-- veos:appc -->", "<!-- /veos:appc -->"


# ------------------------------------------------------------------ paths
def set_path(d: dict, path: str, value) -> None:
    """Set a dotted path, creating missing dicts (list indices must exist)."""
    keys = path.split(".")
    cur = d
    for k in keys[:-1]:
        if isinstance(cur, list) and k.isdigit() and int(k) < len(cur):
            cur = cur[int(k)]
            continue
        if not isinstance(cur, dict):
            raise VeosError("BAD_PATH", f"cannot set '{path}': '{k}' is not an object", "Check the path in tokens.json.")
        if not isinstance(cur.get(k), (dict, list)):
            cur[k] = {}
        cur = cur[k]
    last = keys[-1]
    if isinstance(cur, list) and last.isdigit() and int(last) < len(cur):
        cur[int(last)] = value
    elif isinstance(cur, dict):
        cur[last] = value
    else:
        raise VeosError("BAD_PATH", f"cannot set '{path}'", "Check the path in tokens.json.")


def parse_change(spec: str) -> tuple[str, Any]:
    """'captions.profiles.CS-1.skin.size=42' -> (path, 42). The value is JSON when it parses, else a string."""
    if "=" not in spec:
        raise VeosError("BAD_CHANGE", f"--change '{spec}' needs PATH=VALUE", "Example: --change captions.profiles.CS-1.skin.size=42")
    path, raw = spec.split("=", 1)
    path = path.strip()
    if not path:
        raise VeosError("BAD_CHANGE", f"--change '{spec}' has no path", "Example: --change profile.tone.energy=balanced")
    try:
        val = json.loads(raw)
    except ValueError:
        val = raw.strip()
    return path, val


def fmt(v) -> str:
    if isinstance(v, str):
        return v
    return json.dumps(v, ensure_ascii=False)


# ------------------------------------------------------------------ classification
def _isnum(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _nc(rule: str, path: str, old, new, alt_value=None) -> dict:
    alt = ALTERNATIVES.get(rule, "keep the rule as it is")
    if alt_value is not None:
        alt = f"set it to {fmt(alt_value)} instead ({alt})"
    return {"path": path, "from": old, "to": new, "class": "NC", "lock": "NC", "rule": rule,
            "why": NC_WHY.get(rule, "a never-bendable rule"), "alternative": alt, "alternative_value": alt_value}


def refusal(rec: dict) -> str:
    """The one friendly line for a refused change: why, then the nearest allowed alternative."""
    return f"I can't do that one: {rec['why']}. Nearest option: {rec['alternative']}."


def _text_class_of(tokens: dict, path: str) -> str | None:
    if path.startswith("captions.profiles.") and path.endswith(".skin.size"):
        prof = _get_path(tokens, path.rsplit(".", 1)[0]) or {}
        return prof.get("text_class") or "TC-subtitle"
    m = re.fullmatch(r"type\.([^.]+)\.size", path)
    if m:
        return ((tokens.get("type") or {}).get(m.group(1)) or {}).get("text_class") or "TC-label"
    return None


def _nc_check(tokens: dict, path: str, old, new) -> dict | None:
    """The never-bendable core and the engine's hard rules, judged on the token value."""
    low = path.lower()
    if path.startswith(("roles.bad", "roles.good", "roles.comedy", "fixed_meaning")):
        return _nc("fixed-meaning", path, old, new)
    if path.startswith(("layout.ig_ui", "layout.size")):
        return _nc("NC-5", path, old, new)
    if path.startswith("layout.safe"):
        safe = copy.deepcopy(_get_path(tokens, "layout.safe") or {})
        probe = {"layout": {"safe": safe}}
        try:
            set_path(probe, path, new)
        except VeosError:
            return _nc("NC-5", path, old, new)
        s = probe["layout"]["safe"]
        y, x = s.get("y") or [110, 1540], s.get("x") or [64, 1016]
        if not (isinstance(y, list) and isinstance(x, list) and len(y) == 2 and len(x) == 2):
            return _nc("NC-5", path, old, new)
        if y[0] < 110 or y[1] > 1540 or x[0] < 0 or x[1] > 1080:
            fixed = {"x": [max(0, x[0]), min(1080, x[1])], "y": [max(110, y[0]), min(1540, y[1])]}
            return _nc("NC-5", path, old, new, _get_path({"layout": {"safe": fixed}}, path) if path != "layout.safe" else fixed)
        return None
    if any(w in low for w in PROTECTED_WORDS):
        if new != old:
            return _nc("NC-8", path, old, new, old)
        return None
    if low.endswith("duck_db") and _isnum(new) and new > -18:
        return _nc("NC-8", path, old, new, -18)
    if path == "max_bright_per_frame" and _isnum(new) and new > 4:
        return _nc("NC-10", path, old, new, 4)
    if path == "inserts.fetch" and new is True:
        return _nc("NC-7", path, old, new, False)
    cls = _text_class_of(tokens, path)
    if cls and cls in NC4_FLOOR:
        floor = NC4_FLOOR[cls]
        vals = new if isinstance(new, list) else [new]
        if any(_isnum(v) and v < floor for v in vals):
            alt = [max(floor, v) for v in new] if isinstance(new, list) else floor
            return _nc("NC-4", path, old, new, alt)
    m = re.fullmatch(r"exceptions\.([^.]+)\.([^.]+)", path)
    if m:
        eid = EXC_BY_NAME.get(m.group(1), m.group(1))
        lim = (EXC_REGISTRY.get(eid) or {}).get("limits", {}).get(m.group(2))
        if lim and _isnum(new):
            op, bound = lim
            if (op == ">=" and new < bound) or (op == "<=" and new > bound):
                return _nc("registry", path, old, new, bound)
    return None


def _template_value(template_tokens: dict | None, path: str, fallback):
    if template_tokens is not None:
        v = _get_path(template_tokens, path)
        if v is not None:
            return v
    return fallback


def _tune_in_range(path: str, base, new, rng, tokens: dict) -> tuple[bool, str]:
    """(in range, range text) for a TUNE change measured from the template value `base`."""
    rel = _relative(rng)
    if rel is not None:
        amt, pct = rel
        pairs = list(zip(base, new)) if isinstance(base, list) and isinstance(new, list) and len(base) == len(new) else [(base, new)]
        ok = True
        for b, n in pairs:
            if _isnum(b) and _isnum(n):
                d = abs(b) * amt / 100 if pct else amt
                ok = ok and (b - d - 1e-9 <= n <= b + d + 1e-9)
        return ok, f"{rng} of {fmt(base)}"
    if isinstance(rng, list) and len(rng) == 2 and all(_isnum(x) for x in rng):
        vals = new if isinstance(new, list) else [new]
        return all(_isnum(v) and min(rng) <= v <= max(rng) for v in vals), f"{rng[0]}-{rng[1]}"
    if isinstance(rng, list) and rng:
        return new in rng, " / ".join(fmt(x) for x in rng)
    if isinstance(rng, str) and rng:
        return True, rng
    scale = ORDINALS.get(path)
    if scale and base in scale and new in scale:
        return abs(scale.index(new) - scale.index(base)) <= 1, f"one step from {base}"
    if path.endswith("tone.comedy") and new in COMEDY:
        cmax = _get_path(tokens, "profile.tone.comedy_max") or base
        if cmax in COMEDY:
            return COMEDY.index(new) <= COMEDY.index(cmax), f"up to {cmax}"
    return True, "any"


def classify(tokens: dict, path: str, new, template_tokens: dict | None = None) -> dict:
    """One change against the copy's locks: {path, from, to, class, lock, range, in_range, rule?, why?, alternative?}."""
    old = _get_path(tokens, path)
    nc = _nc_check(tokens, path, old, new)
    if nc:
        return nc
    locks = tokens.get("locks") or {}
    base = _template_value(template_tokens, path, old)
    # exceptions: switching one off is stricter (VAR); adding one the template doesn't declare is DNA (structure C.3.5)
    m = re.fullmatch(r"exceptions\.([^.]+)", path)
    if m:
        if new in (False, None):
            return {"path": path, "from": old, "to": new, "class": "VAR", "lock": "VAR", "range": "off", "in_range": True}
        return {"path": path, "from": old, "to": new, "class": "DNA", "lock": "DNA", "range": None, "in_range": False,
                "note": "adds or changes a declared exception"}
    level, rng, src = lock_for(path, locks)
    rec = {"path": path, "from": old, "to": new, "lock": level, "lock_source": src, "range": rng}
    if level in ("VAR", "NICHE"):
        return {**rec, "class": "VAR", "in_range": True}
    if level == "DNA":
        return {**rec, "class": "DNA", "in_range": False}
    ok, rtext = _tune_in_range(path, base, new, rng, tokens)
    return {**rec, "class": "TUNE" if ok else "DNA", "in_range": ok, "range_text": rtext, "template_value": base}


def worst(recs: list[dict]) -> str:
    return max((r["class"] for r in recs), key=lambda c: RANK[c], default="VAR")


# ------------------------------------------------------------------ fidelity + playbook.md
def style_name(tokens: dict) -> str:
    return (tokens.get("style") or {}).get("name") or (tokens.get("lineage") or {}).get("template", {}).get("id") or "this style"


def buyer_name(tokens: dict) -> str:
    cr = tokens.get("creator") or {}
    return cr.get("name") or (cr.get("handle") or "").lstrip("@") or "My"


def fidelity(lin: dict) -> str:
    devs = [d for d in (lin.get("deviations") or []) if d.get("confirmed", True) and d.get("active", True)]
    if len(devs) >= DERIVED_AT or any(str(d.get("path", "")).startswith(CORE_SWITCHES) for d in devs):
        return "derived"
    return "faithful"


def copy_title(tokens: dict) -> str:
    """The copy's title. It keeps the template's name however far the buyer tweaks it (fidelity is internal)."""
    lin = tokens.get("lineage") or {}
    t = lin.get("template") or {}
    return f"{buyer_name(tokens)} · {style_name(tokens)} (from template {t.get('id')} v{t.get('version')})"


def lineage_block(tokens: dict) -> str:
    lin = tokens.get("lineage") or {}
    t = lin.get("template") or {}
    var = lin.get("variables") or {}
    tuned, devs = lin.get("tuned") or [], lin.get("deviations") or []
    lines = [LINEAGE_START,
             f"> **Lineage.** From template `{t.get('id')}` v{t.get('version')} on {lin.get('created')}. "
             f"Variables set: {', '.join(sorted(var)) or 'none'}. Tuned values: {len(tuned)}. "
             f"Deviations: {len(devs)}. Full log: App. C.",
             LINEAGE_END]
    return "\n".join(lines)


def _log_line(kind: str, rec: dict) -> str:
    src = rec.get("source", "buyer")
    if kind == "DV":
        why = f" Reason: {rec['reason']}." if rec.get("reason") else ""
        return (f"- **{rec['id']}** · {rec['date']} · `{rec['path']}` {fmt(rec['from'])} → {fmt(rec['to'])} "
                f"(changed from the style; source {src}).{why}")
    return (f"- {rec['date']} · `{rec['path']}` {fmt(rec['template'])} → {fmt(rec['value'])} "
            f"({rec.get('level', 'TUNE')}, range {fmt(rec.get('range'))}; source {src})")


def update_playbook_md(pbdir: Path, tokens: dict, new_lines: list[str] | None = None) -> None:
    """Title, the header lineage block and the App. C log (engine-managed marker regions)."""
    f = pbdir / "playbook.md"
    if not f.exists():
        return
    text = f.read_text(encoding="utf-8")
    title = copy_title(tokens)
    if re.search(r"^# .*$", text, flags=re.M):
        text = re.sub(r"^# .*$", lambda _m: f"# {title}", text, count=1, flags=re.M)
    else:
        text = f"# {title}\n\n" + text
    block = lineage_block(tokens)
    if LINEAGE_START in text and LINEAGE_END in text:
        a, b = text.index(LINEAGE_START), text.index(LINEAGE_END) + len(LINEAGE_END)
        text = text[:a] + block + text[b:]
    else:
        m = re.search(r"^# .*$", text, flags=re.M)
        text = text[:m.end()] + "\n\n" + block + text[m.end():]
    if APPC_START not in text:
        text = text.rstrip("\n") + f"\n\n{APPC_HEAD}\n\n{APPC_START}\n{APPC_END}\n"
    if new_lines:
        b = text.index(APPC_END)
        text = text[:b] + "".join(ln + "\n" for ln in new_lines) + text[b:]
    f.write_text(text, encoding="utf-8", newline="\n")


# ------------------------------------------------------------------ apply
def is_style_copy(tokens: dict) -> bool:
    return schema_version(tokens) == 3 and tokens.get("kind") == "style_copy"


def load_template_tokens(tokens: dict) -> dict | None:
    """The template this copy came from (for TUNE ranges measured from the template value), when still shipped."""
    from . import paths
    tid = ((tokens.get("lineage") or {}).get("template") or {}).get("id")
    if not tid:
        return None
    f = paths.styles_dir() / tid / "tokens.json"
    try:
        return read_json(f) if f.is_file() else None
    except ValueError:
        return None


def apply_changes(pbdir: Path, changes: list[tuple[str, Any]], *, source: str = "buyer", reason: str | None = None,
                  confirm: bool = False, nc: str | None = None) -> dict:
    """Classify and apply `changes` to the style copy in `pbdir` (buyers can change anything).

    status: applied | refused (NC only; nothing is written). `confirm` is accepted for old callers and ignored."""
    tf = pbdir / "tokens.json"
    tokens = read_json(tf)
    if not is_style_copy(tokens):
        raise VeosError("NOT_A_STYLE_COPY", f"{pbdir.name} is not a template copy (kind: {tokens.get('kind')})",
                        "Lock classification applies to playbooks made from a template (path A).")
    if nc:
        rule = nc.upper()
        rec = _nc(rule, "(rule)", None, None)
        return {"status": "refused", "class": "NC", "changes": [rec], "rule": rule, "why": rec["why"],
                "alternative": rec["alternative"],
                "message": refusal(rec)}
    tmpl = load_template_tokens(tokens)
    recs = [classify(tokens, p, v, tmpl) for p, v in changes]
    cls = worst(recs)
    if cls == "NC":
        bad = next(r for r in recs if r["class"] == "NC")
        return {"status": "refused", "class": "NC", "changes": recs, "rule": bad["rule"], "why": bad["why"],
                "alternative": bad["alternative"],
                "message": refusal(bad)}
    today = date.today().isoformat()
    lin = tokens.setdefault("lineage", {})
    lin.setdefault("tuned", [])
    lin.setdefault("deviations", [])
    log, dv_ids = [], []
    for r in recs:
        set_path(tokens, r["path"], r["to"])
        if r["class"] == "DNA":
            n = 1 + max([int(str(d.get("id", "DV-0"))[3:]) for d in lin["deviations"] if str(d.get("id", ""))[3:].isdigit()] or [0])
            dv = {"id": f"DV-{n}", "path": r["path"], "from": r["from"], "to": r["to"], "reason": reason, "source": source,
                  "date": today, "confirmed": True, "lock": r.get("lock")}
            lin["deviations"].append(dv)
            dv_ids.append(dv["id"])
            r["dv"] = dv["id"]
            log.append(_log_line("DV", dv))
        else:
            t = {"path": r["path"], "template": r.get("template_value", r["from"]), "value": r["to"],
                 "range": r.get("range") if r["class"] == "TUNE" else "VAR", "level": r["class"], "source": source,
                 "date": today}
            lin["tuned"].append(t)
            log.append(_log_line("T", t))
    lin["fidelity"] = fidelity(lin)  # internal note (template upgrades); never shown, never renames the copy
    tokens["version"] = int(tokens.get("version") or 1) + 1
    write_json(tf, tokens, indent=2)
    update_playbook_md(pbdir, tokens, log)
    return {"status": "applied", "class": cls, "changes": recs, "deviations": dv_ids, "version": tokens["version"]}
