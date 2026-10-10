"""`veos playbook index`: a one-page reading guide to a playbook, generated from its own markdown. Directions, not rules.

    veos playbook index --project P            the project's playbook -> P/work/playbook-index.md
    veos playbook index --playbook ID [--out F] any playbook or style template -> VEOS_HOME/cache/playbook-index/ID.md

Contents, all taken from the playbook's own text (deterministic; nothing is invented or re-worded):
  * a short "how to read this playbook" header with plain directions: start from what you saw and heard in each beat,
    look candidates up in the groups, open the recipes and the worked examples at their lines, follow the playbook's own
    variety and budget guidance;
  * the section map: headings with line ranges (sub-headings with their first line);
  * the device directory grouped by purpose: hooks, graphics / B-roll patterns, the line -> pattern lookup, transitions,
    camera, worlds and layouts, caption profiles, structure devices. Each entry keeps the playbook's own "use when"
    wording (shortened, never rewritten) and the line of its full recipe.
It is neither a menu nor a check: nothing validates a plan against it. Any section, id or device the parser does not
recognise is still in the playbook, reachable from the section map.

Robust: a parsing problem never fails the command; it falls back to the section map alone. Grouping comes from the
section a device sits in (a "Transitions" heading, a "Camera / zoom" heading, ...) and its id prefix (P-, T-, Z-, W-,
L-, G-, CS-, SM-, HA-, ...); table rows, ids in headings and bold paragraph leads ("**HA-01 Result pair** ...") count.

Cached; rebuilt when playbook.md changes (sha256), the project links another playbook, or INDEX_VERSION changes, the
same freshness approach as tokens.source.json (record: <out>.source.json next to the index).
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

from .core import VeosError, read_json, veos_home, write_json

INDEX_VERSION = 1
USE_W, NAME_W = 78, 34

# purpose groups: (key, title, heading pattern, id prefixes). Order = the order they print in.
GROUPS = [
    ("hooks", "Hooks", r"(?<!re-)(?<!re)hooks?\b|stopper|archetype|opening|\bcta\b", {"HA", "HF", "VS", "O", "H", "HK"}),
    ("patterns", "Graphics and B-roll patterns", r"pattern|visual system|b-roll|graphics?\b|famil", {"P"}),
    ("lookup", "Line -> pattern lookup", r"line\s*(?:→|->|to)\s*(?:pattern|device|visual)|\blookup\b|line types?\b", set()),
    ("transitions", "Transitions", r"transition", {"T", "TR"}),
    ("camera", "Camera", r"camera|zoom|reframe|\bcrop", {"Z", "C", "RF", "CAM"}),
    ("worlds", "Worlds and layouts", r"world|layout|stage move|scene move|screen mode|shot type|\bmodes?\b", {"W", "L", "G", "SHOT"}),
    ("captions", "Caption profiles", r"caption|subtitle|^type\b", {"CS", "CAP"}),
    ("structure", "Structure devices", r"structure|marker|ritual|open loop|re-?hooks?\b|chapter|series furniture", {"SM", "RS", "FW", "RH", "U", "R", "M"}),
]
# the order a section's heading is tested in (most specific first); a heading in a SKIP section never yields devices
MATCH_ORDER = ["lookup", "transitions", "camera", "captions", "structure", "hooks", "worlds", "patterns"]
SKIP = re.compile(r"worked example|\bqa\b|checklist|output contract|ids used|evidence map|deviation|personali[sz]ation|"
                  r"exceptions?\b|hard rules|procedure|appendix|^app\.|\bbank\b|quick index|starter prompt|v1 → v2", re.I)
GUIDE = re.compile(r"density|variety|budget|cadence|rhythm", re.I)
CORE = re.compile(r"style dna|directive|hard rules|procedure", re.I)
EXAMPLES = re.compile(r"worked example", re.I)

HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
ID_RE = re.compile(r"(?<![\w-])([A-Z][A-Z0-9]{0,5}(?:-[A-Za-z0-9]+)+(?:\.[A-Za-z0-9]+)?)(?![\w-])")
SECNUM_RE = re.compile(r"^(?:§\s*)?\d+(?:\.\d+)*\.?\s+")
USE_KEYS = [r"^use when", r"^use\b|^use for|when to use|^purpose", r"^when\b|^carries|^job\b|\bfor$",
            r"^recipe|^what|on screen|^look\b|^meaning|^effect"]
NAME_KEYS = r"^name|^device|^pattern|^transition|^preset|^marker|^formula|^archetype|^title|^world|^mode|^profile|^layout|^move"
DASHES = {"", "—", "–", "-", "n/a"}


# ---------------------------------------------------------------- text helpers
def strip_md(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", str(s))
    s = s.replace("**", "").replace("__", "")
    return re.sub(r"\s+", " ", s).strip()


def clean_heading(h: str) -> str:
    h = re.sub(r"`\[[^`]*\]`", "", h)
    h = re.sub(r"\[(?:REQ|DNA|VAR|TUNE|NICHE|COND)[^\]]*\]", "", h)
    return strip_md(h).strip(" -—:")


def short(s: str, n: int = USE_W) -> str:
    s = strip_md(s).strip(" ,;:—–-")
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0] if " " in s[:n] else s[:n]
    return cut.rstrip(",;:—–-( ") + "…"


def first_sentence(s: str) -> str:
    s = strip_md(s)
    m = re.search(r"\b(Use (?:only )?when\b[^.]*\.)", s)
    if m:
        return m.group(1)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"“(])", s, maxsplit=1)
    return parts[0]


def cells(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    out, cur, tick, i = [], [], False, 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur.append("|")
            i += 2
            continue
        if ch == "`":
            tick = not tick
        if ch == "|" and not tick:
            out.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
        i += 1
    out.append("".join(cur).strip())
    if tick:  # unbalanced backticks: a plain split is the better guess
        return [c.strip() for c in s.split("|")]
    return out


def lead_id(text: str) -> tuple[str | None, str]:
    """(id, rest) when the cleaned text starts with an id, else (None, text)."""
    t = strip_md(text).replace("`", "").strip()
    m = ID_RE.match(t)
    if not m:
        return None, t
    return m.group(1), t[m.end():].strip(" :–—-·.")


def prefix(i: str) -> str:
    return i.split("-", 1)[0]


def first_id(text: str, allowed: set):
    """The first id in `text` whose prefix belongs to the group ("F-A: SM-FIG" -> SM-FIG for structure)."""
    return next((m for m in ID_RE.finditer(text) if prefix(m.group(1)) in allowed), None)


# ---------------------------------------------------------------- parsing
def headings(lines: list[str]) -> list[tuple[int, int, str]]:
    """[(line no (1-based), level, raw text)] outside code fences."""
    out, fence = [], False
    for n, ln in enumerate(lines, 1):
        if ln.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = HEAD_RE.match(ln)
        if m:
            out.append((n, len(m.group(1)), m.group(2)))
    return out


def section_map(lines: list[str], heads: list) -> dict:
    """{level, sections: [{line, end, title, subs: [(line, title)]}], front: {...} | None}."""
    total = len(lines)
    levels = [lv for _, lv, _ in heads]
    sec = 2 if levels.count(2) >= 2 else 1 if levels.count(1) >= 2 else (min(levels) if levels else 2)
    tops = [(n, t) for n, lv, t in heads if lv == sec]
    secs = []
    for k, (n, t) in enumerate(tops):
        end = (tops[k + 1][0] - 1) if k + 1 < len(tops) else total
        nxt_higher = next((m for m, lv, _ in heads if m > n and lv < sec), None)
        if nxt_higher and nxt_higher - 1 < end:
            end = nxt_higher - 1
        subs = [(m, clean_heading(st)) for m, lv, st in heads if n < m <= end and lv == sec + 1]
        secs.append({"line": n, "end": end, "title": clean_heading(t), "subs": subs})
    front = None
    first = tops[0][0] if tops else total + 1
    if first > 1:
        subs = [(m, clean_heading(st)) for m, lv, st in heads if m < first and lv > sec]
        front = {"line": 1, "end": first - 1, "title": "Front matter", "subs": subs}
    return {"level": sec, "sections": secs, "front": front, "total": total}


def _groups_of(stack: list[str]) -> list[str]:
    """Every group a heading stack matches, the deepest heading first ([] inside a SKIP section). The first is the
    section's own group; an id joins the first one whose prefixes include its own ("5.3 CAP-CHUNKY (hook, ...)" under
    "§5 Type tokens" is a caption style, not a hook)."""
    if any(SKIP.search(t) for t in stack):
        return []
    out: list[str] = []
    for t in reversed(stack):
        t2 = SECNUM_RE.sub("", t)
        out += [k for k in MATCH_ORDER if k not in out and re.search(RULES[k], t2, re.I)]
    return out


def _group_for(ident: str | None, groups: list[str]) -> str | None:
    if not ident:
        return None
    return next((g for g in groups if prefix(ident) in PREFIXES[g]), None)


def _first_id_in(text: str, groups: list[str]):
    """(match, group) of the first id in `text` that belongs to one of `groups`."""
    for m in ID_RE.finditer(text):
        g = _group_for(m.group(1), groups)
        if g:
            return m, g
    return None, None


RULES = {k: rx for k, _, rx, _ in GROUPS}
PREFIXES = {k: px for k, _, _, px in GROUPS}
TITLES = {k: t for k, t, _, _ in GROUPS}


def _pick_cols(header: list[str]) -> tuple[int | None, int | None]:
    h = [strip_md(x).lower() for x in header]
    name = next((i for i in range(1, len(h)) if re.search(NAME_KEYS, h[i])), None)
    use = None
    for rx in USE_KEYS:
        use = next((i for i in range(1, len(h)) if i != name and re.search(rx, h[i])), None)
        if use is not None:
            break
    return name, use


def _paragraph_after(lines: list[str], n: int, limit: int = 8) -> str:
    """The first prose line after line n (1-based): no heading, table, fence or blank."""
    for ln in lines[n:n + limit]:
        s = ln.strip()
        if not s or s.startswith(("|", "#", "```", "<")):
            if s.startswith(("#", "|")):
                return ""
            continue
        return s
    return ""


def devices(lines: list[str], heads: list) -> dict:
    """{group: [{id, name, note, use, line}]} plus {"lookup": [{line_type, primary, alt, line}]}."""
    out: dict[str, list] = {k: [] for k, *_ in GROUPS}
    seen: set = set()
    head_at = {n: (lv, t) for n, lv, t in heads}
    # the document title ("# Evidence Explainer Style Playbook") names the style, not a section: never a group or a skip
    title_line = heads[0][0] if heads and heads[0][1] == 1 and sum(1 for _, lv, _ in heads if lv == 1) == 1 else None
    stack: list[tuple[int, str]] = []
    heading_entries: list[dict] = []
    fence, i, N = False, 0, len(lines)

    def add(group, ident, name, use, line, note=""):
        key = (group, ident or name)
        if not (ident or name) or key in seen:
            return None
        seen.add(key)
        e = {"id": ident or "", "name": short(name, NAME_W) if name else "", "note": note, "use": short(use) if use else "",
             "line": line}
        out[group].append(e)
        return e

    while i < N:
        n, ln = i + 1, lines[i]
        s = ln.strip()
        if s.startswith("```"):
            fence = not fence
            i += 1
            continue
        if fence:
            i += 1
            continue
        if n in head_at:
            lv, raw = head_at[n]
            while stack and stack[-1][0] >= lv:
                stack.pop()
            stack.append((lv, "" if n == title_line else clean_heading(raw)))
            gs = _groups_of([t for _, t in stack])
            if gs and gs[0] != "lookup":
                text = SECNUM_RE.sub("", clean_heading(raw)).replace("`", "")
                m, g = _first_id_in(text, gs)
                if m:
                    name = text[m.end():].strip(" :–—-")
                    note = "default" if re.search(r"\bdefault\b", text, re.I) and "default" not in name.lower() else ""
                    add(g, m.group(1), name, first_sentence(_paragraph_after(lines, n)), n, note)
                elif gs[0] == "hooks" and re.search(r"\bdefault\b", text, re.I) and lv > 2:
                    g = "hooks"
                    e = add(g, "", text, first_sentence(_paragraph_after(lines, n)), n, "")
                    if e is not None:
                        end = next((m2 for m2, lv2, _ in heads if m2 > n and lv2 <= lv), N + 1)
                        heading_entries.append({"e": e, "end": end})
            i += 1
            continue
        gs = _groups_of([t for _, t in stack]) if stack else []
        if not gs:
            i += 1
            continue
        if s.startswith("|") and i + 1 < N and SEP_RE.match(lines[i + 1]):
            header = cells(s)
            j = i + 2
            rows = []
            while j < N and lines[j].strip().startswith("|"):
                rows.append((j + 1, cells(lines[j])))
                j += 1
            if gs[0] == "lookup":
                _lookup(out, header, rows)
            else:
                _table(header, rows, gs, add)
            i = j
            continue
        mb = re.match(r"^\s*(?:[-*]\s+)?([^*|`#]{0,12}?)\*\*(.+?)\*\*(.*)$", ln)
        if mb and gs[0] != "lookup":
            lead, bold, rest = mb.group(1).strip(" :"), strip_md(mb.group(2)).replace("`", ""), mb.group(3)
            m, g = _first_id_in(bold, gs)
            if m:
                before = (lead + " " + bold[:m.start()]).strip(" :–—-")
                name = bold[m.end():].strip(" :–—-.")
                para = rest
                k = i + 1
                while k < N and lines[k].strip() and not lines[k].lstrip().startswith(("|", "#", "**", "```")):
                    para += " " + lines[k].strip()
                    k += 1
                use = first_sentence(para.strip().lstrip(":,.;—– "))
                note = before if before and len(before) <= 24 and before.lower() not in name.lower() else ""
                add(g, m.group(1), name, use, n, note)
        i += 1
    # an id-less "default ..." hook heading that holds id'd hooks is a container, not a device
    for he in heading_entries:
        e = he["e"]
        inner = [x for x in out["hooks"] if x is not e and x["id"] and e["line"] < x["line"] < he["end"]]
        if inner:
            out["hooks"].remove(e)
    return out


def _table(header: list[str], rows: list, gs: list[str], add) -> None:
    name_col, use_col = _pick_cols(header)
    # caption profiles laid out as columns: "| Field | CS-1 **Chest** (default) | CS-2 ... |"
    col_ids = [(c, lead_id(header[c])) for c in range(1, len(header))]
    col_ids = [(c, x, _group_for(x[0], gs)) for c, x in col_ids]
    col_ids = [(c, x, g) for c, x, g in col_ids if g]
    if col_ids and not lead_id(header[0])[0]:
        for c, (ident, rest), g in col_ids:
            m = re.match(r"^(.*?)\s*\((.*)\)\s*$", rest)
            name, use = (m.group(1), m.group(2)) if m else (rest, "")
            add(g, ident, name, use, rows[0][0] - 2 if rows else 0)
        return
    for line, cs in rows:
        if not cs or not cs[0]:
            continue
        ident, rest = lead_id(cs[0])
        g = _group_for(ident, gs)
        if ident and not g:
            continue
        if not ident:  # a named world or screen mode without an id ("**Studio**", "`HOOK`")
            raw = cs[0].strip()
            if not (gs[0] == "worlds" and (raw.startswith("**") or raw.startswith("`")) and len(strip_md(raw)) <= 24):
                continue
            ident, rest, g = strip_md(raw).replace("`", ""), "", "worlds"
        name = rest or (strip_md(cs[name_col]) if name_col is not None and name_col < len(cs) else "")
        if use_col is not None and use_col < len(cs):
            use = cs[use_col]
        else:
            others = [(k, c) for k, c in enumerate(cs[1:], 1) if k != name_col and strip_md(c) not in DASHES]
            use = " · ".join((f"{strip_md(header[k])}: " if k < len(header) and len(strip_md(c)) <= 14 else "") + strip_md(c)
                             for k, c in others[:2])
        add(g, ident, name, first_sentence(use) if use_col is not None else use, line)


def _lookup(out: dict, header: list[str], rows: list) -> None:
    h = [strip_md(x).lower() for x in header]
    lt = next((k for k, x in enumerate(h) if x.startswith("line") or "type" in x), 0)
    pr = next((k for k, x in enumerate(h) if x.startswith("primary")), 1 if len(h) > 1 else None)
    al = next((k for k, x in enumerate(h) if x.startswith("altern")), None)
    for line, cs in rows:
        if lt >= len(cs) or not strip_md(cs[lt]):
            continue
        out["lookup"].append({"line_type": short(cs[lt], 48),
                              "primary": short(cs[pr], 44) if pr is not None and pr < len(cs) else "",
                              "alt": short(cs[al], 36) if al is not None and al < len(cs) and strip_md(cs[al]) not in DASHES else "",
                              "line": line})


# ---------------------------------------------------------------- rendering
def _range(a: int, b: int) -> str:
    return f"L{a}–{b}" if b > a else f"L{a}"


def _sec_label(t: str) -> str:
    return short(t, 46)


def render(md: str, pid: str, source: str) -> tuple[str, dict]:
    lines = md.splitlines()
    heads = headings(lines)
    sm = section_map(lines, heads)
    title = next((clean_heading(t) for _, lv, t in heads if lv == 1), pid)
    stats = {"sections": len(sm["sections"]), "map_only": False, "devices": {}}
    dev, err = None, ""
    try:
        dev = devices(lines, heads)
        if not any(dev.values()):
            dev, err = None, "no device tables or ids found"
    except Exception as e:  # noqa: BLE001 - never fail: the section map alone still guides the reading
        dev, err = None, f"{type(e).__name__}"
    if dev is None:
        stats["map_only"] = True

    def find(rx):
        return [(n, clean_heading(t)) for n, lv, t in heads if rx.search(clean_heading(t))]

    def owner(n):  # the top-level section holding line n
        return next((s for s in sm["sections"] if s["line"] <= n <= s["end"]), None)

    out = [f"# Playbook index: {title}",
           f"`{pid}` · `{source}` · {sm['total']} lines · built by `veos playbook index` from the playbook's own text. "
           "Directions, not rules: the playbook text and your judgement decide.", "",
           "## How to read this playbook"]
    ex = find(EXAMPLES)
    ex_sec = owner(ex[0][0]) if ex else None
    lk = (dev or {}).get("lookup") or []
    lk_head = next(((n, t) for n, t in find(re.compile(RULES["lookup"], re.I))), None)
    out.append("1. Start from what you saw and heard in each beat (`plan/look.md`, `review/look/look.json`, the words): "
               "framing, props, screens, gestures on key words, pauses, energy.")
    step2 = "2. Look candidates up in the device groups below"
    lk_end = 0
    if lk_head:
        lk_sec = next((s for s in sm["sections"] + [x for x in [sm["front"]] if x] if s["line"] <= lk_head[0] <= s["end"]), None)
        lk_end = next((m - 1 for m, lv, _ in heads if m > lk_head[0] and lv <= sm["level"] + 1), lk_sec["end"] if lk_sec else lk_head[0])
        step2 += f": what is said → the line → pattern lookup ({_range(lk_head[0], lk_end)}); what is seen → the group that fits"
    out.append(step2 + ".")
    s3 = "3. Open the recipes you will use (Read playbook.md at the line shown) and the worked examples"
    if ex_sec:
        subs = [f"{short(t, 30)} L{m}" for m, t in ex_sec["subs"]][:5]
        s3 += f": {_sec_label(ex_sec['title'])} {_range(ex_sec['line'], ex_sec['end'])}" + (f" ({' · '.join(subs)})" if subs else "")
    out.append(s3 + ".")
    sub_lines = {n for n, lv, _ in heads if lv > sm["level"]}
    gd = [f"{short(t, 34)} L{n}" for n, t in find(GUIDE) if n in sub_lines and not EXAMPLES.search(t)][:6]
    out.append("4. Follow the playbook's own variety and budget guidance" + (": " + " · ".join(gd) if gd else " (see the section map)") + ".")
    core = [f"{short(t, 30)} L{n}" for n, t in find(CORE)][:5]
    if core:
        out.append("Always in force: " + " · ".join(core) + ".")
    out.append("Anything not listed here is still in the playbook: use the section map.")
    out += ["", "## Section map"]
    for s in ([sm["front"]] if sm["front"] else []) + sm["sections"]:
        subs = " · ".join(f"{short(t, 32)} {m}" for m, t in s["subs"])
        out.append(f"- {_sec_label(s['title'])} {_range(s['line'], s['end'])}" + (f": {subs}" if subs else ""))
    out += ["", "## Devices by purpose (id, name: the playbook's own use-when, shortened · line of the full recipe)"]
    if dev is None:
        out.append(f"(Device directory unavailable: {err}. Use the section map.)")
    else:
        for key, ttl, _, _ in GROUPS:
            items = dev.get(key) or []
            stats["devices"][key] = len(items)
            if not items:
                continue
            secs = []
            for it in items:
                o = owner(it["line"])
                if o and o not in secs:
                    secs.append(o)
            where = " · ".join(f"{_sec_label(o['title'])} {_range(o['line'], o['end'])}" for o in secs[:3])
            if key == "lookup" and lk_head:
                where = f"{_sec_label(lk_head[1])} {_range(lk_head[0], lk_end)}"
            out.append(f"### {ttl}" + (f" ({where})" if where else ""))
            if key == "lookup":
                for it in items:
                    alt = f"; alt {it['alt']}" if it["alt"] else ""
                    out.append(f"- {it['line_type']} → {it['primary']}{alt} · L{it['line']}")
                continue
            for it in items:
                head = " ".join(x for x in (it["id"], it["name"]) if x)
                if it["note"]:
                    head += f" ({it['note']})"
                out.append(f"- {head}" + (f": {it['use']}" if it["use"] else "") + f" · L{it['line']}")
    return "\n".join(out) + "\n", stats


# ---------------------------------------------------------------- playbook files, cache
def playbook_md(pid: str) -> Path:
    from . import paths
    d = paths.find_playbook_dir(pid)
    if d is None and (paths.styles_dir() / pid / "tokens.json").is_file():
        d = paths.styles_dir() / pid
    if d is None or not (d / "playbook.md").is_file():
        raise VeosError("PLAYBOOK_MISSING", f"no playbook.md for playbook '{pid}'",
                        "Check the playbook id (`veos workspace get` lists them) or create the playbook first.")
    return d / "playbook.md"


def ensure(pid: str, out: Path, force: bool = False) -> dict:
    """Write `out` (and its .source.json record) unless it is fresh. Returns {file, rebuilt, why, lines, stats}."""
    md_path = playbook_md(pid)
    raw = md_path.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    rec_path = out.with_name(out.stem + ".source.json")
    want = {"version": 1, "index_version": INDEX_VERSION, "playbook": pid, "source": md_path.resolve().as_posix(), "sha256": sha}
    try:
        rec = read_json(rec_path) if rec_path.exists() else None
    except ValueError:
        rec = None
    why = None
    if force:
        why = "--force"
    elif not out.exists() or not isinstance(rec, dict):
        why = "no index yet"
    elif rec.get("playbook") != pid:
        why = f"the project now uses playbook '{pid}' (was '{rec.get('playbook')}')"
    elif rec.get("sha256") != sha or rec.get("source") != want["source"]:
        why = "playbook.md changed"
    elif rec.get("index_version") != INDEX_VERSION:
        why = "index format updated"
    if why is None:
        stats = rec.get("stats") or {}
        return {"file": out, "rebuilt": False, "why": "fresh", "lines": rec.get("lines"), "stats": stats}
    text, stats = render(raw.decode("utf-8-sig", "replace"), pid, md_path.resolve().as_posix())
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8", newline="\n")
    n = text.count("\n")
    write_json(rec_path, {**want, "lines": n, "stats": stats})
    return {"file": out, "rebuilt": True, "why": why, "lines": n, "stats": stats}


def main(args, project) -> dict:
    from .tokens import project_playbook
    if project is None and not args.playbook:
        raise VeosError("NO_PLAYBOOK", "playbook index needs --project P or --playbook ID",
                        "Example: veos playbook index --project P")
    pid = project_playbook(project, args.playbook) if project is not None else args.playbook
    if args.out:
        out = Path(args.out)
    elif project is not None:
        out = project.root / "work" / "playbook-index.md"
    else:
        out = veos_home() / "cache" / "playbook-index" / f"{pid}.md"
    r = ensure(pid, out.resolve(), force=bool(getattr(args, "force", False)))
    f = project.rel(r["file"]) if project is not None else r["file"].as_posix()
    st = r["stats"] or {}
    return {"playbook": pid, "file": f, "rebuilt": r["rebuilt"], "why": r["why"], "lines": r["lines"],
            "map_only": st.get("map_only", False), "sections": st.get("sections"), "devices": st.get("devices", {})}
