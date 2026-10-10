"""Sound-effects pack tooling: catalogue (`veos sfx catalog`), tag merge (`veos sfx tag`), and the timeline -> bus build
(`veos sfx --project P`). The validator rules S1-S6 live in sfxrules.py. Vocabulary and formats: engine/SPEC.md section 6."""
from __future__ import annotations

import csv
import hashlib
import re
import time
import urllib.request
from urllib.parse import quote
from pathlib import Path

import numpy as np

from .core import VeosError, read_json, r3, write_json
from . import audio
from .audio import SR

EXTS = {".wav", ".mp3", ".ogg", ".m4a", ".aif", ".aiff"}
ROLES = ["whoosh", "swish", "impact", "sub-hit", "riser", "downlifter", "pop", "click", "tap", "typing", "shine", "chime",
         "ding", "sparkle", "glitch", "alarm", "camera", "cash", "meme", "ambient"]
VIBES = ["calm", "premium", "playful", "hype", "tense", "comedic", "techy", "organic"]
USES = ["transition", "text-pop", "reveal", "card-in", "card-out", "data", "number", "warning", "success", "cta",
        "hook-stop", "list-cue", "comedy"]
ANCHORS = ("peak", "onset", "end")
# which instant of the file lands on the visual moment: hits and whooshes on the peak, risers on their end, the rest on the onset
ANCHOR_BY_ROLE = {"impact": "peak", "sub-hit": "peak", "whoosh": "peak", "swish": "peak", "riser": "end"}
DEFAULT_DB = {"impact": -14, "sub-hit": -16, "whoosh": -22, "swish": -22, "pop": -26, "click": -26, "shine": -24,
              "chime": -24, "riser": -20, "meme": -12}
FALLBACK_DB = -24
REVIEWED = "reviewed"


# --------------------------------------------------------------------------- pack / catalogue io
# Audio is NOT shipped with the app. The app carries catalog.json (small); sounds are fetched one by one into the local
# cache (`pack_dir()` = VEOS_HOME/sfx) from the remote store named by catalog.json "base_url" / per-entry "url".
DEFAULT_BASE_URL = "https://raw.githubusercontent.com/namansoniai/vibe-editing-os-sfx/main/"


def pack_dir(arg: str | None = None) -> Path:
    """Folder holding sound FILES: --pack DIR, else the local cache."""
    if arg:
        return Path(arg)
    from .paths import sfx_pack
    return sfx_pack()


def catalog_file(arg: str | None = None) -> Path:
    """catalog.json location: <--pack DIR>/catalog.json, else the app's assets/sfx/catalog.json."""
    if arg:
        return Path(arg) / "catalog.json"
    from .paths import sfx_catalog
    return sfx_catalog()


def read_catalog_doc(src: Path | None = None) -> dict | None:
    """{"version", "base_url", "sounds": [...]} from a catalog.json path (or its folder); None when it does not exist."""
    f = Path(src) if src else catalog_file()
    if f.is_dir():
        f = f / "catalog.json"
    if not f.exists():
        return None
    try:
        data = read_json(f)
    except ValueError as e:
        raise VeosError("BAD_CATALOG", f"{f} is not valid JSON: {e}", "Re-run `veos sfx catalog --pack DIR`.") from e
    if isinstance(data, list):
        data = {"sounds": data}
    data.setdefault("sounds", [])
    return data


def load_catalog(src: Path | None = None) -> list[dict] | None:
    doc = read_catalog_doc(src)
    return None if doc is None else doc["sounds"]


def write_catalog_doc(path: Path, doc: dict) -> None:
    write_json(path, {"version": 1, "base_url": doc.get("base_url") or DEFAULT_BASE_URL, "sounds": doc["sounds"]}, indent=1)


def entry_url(entry: dict, base_url: str | None) -> str | None:
    if entry.get("url"):
        return entry["url"]
    base = base_url or DEFAULT_BASE_URL
    return base.rstrip("/") + "/" + quote(entry["file"], safe="/") if base else None


def default_anchor(role: str | None, attack_ms: float | None = None) -> str:
    if role in ANCHOR_BY_ROLE:
        return ANCHOR_BY_ROLE[role]
    if role:
        return "onset"
    return "peak" if (attack_ms is not None and attack_ms > 15) else "onset"


# --------------------------------------------------------------------------- features
def features(path: Path) -> dict:
    a = audio.decode_mono(path)
    if len(a) < 16 or float(np.abs(a).max()) < 1e-6:
        raise VeosError("SFX_SILENT", f"{path.name} is empty or silent", "Remove it from the pack or replace the file.")
    m = audio.measure_array(a)
    from scipy.signal import resample_poly
    tp = 20 * np.log10(float(np.abs(resample_poly(a, 4, 1)).max()) + 1e-12)
    i0, i1 = int(m["onset"] * SR), min(len(a), int((m["end"] + 0.01) * SR) + 1)
    seg = a[i0:max(i1, i0 + 16)].astype(np.float64)
    lufs = -0.691 + 10 * np.log10(float((seg ** 2).mean()) + 1e-12)
    spec = np.abs(np.fft.rfft(seg * np.hanning(len(seg))))
    freqs = np.fft.rfftfreq(len(seg), 1 / SR)
    centroid = float((freqs * spec).sum() / (spec.sum() + 1e-12))
    # 1 ms peak envelope: attack = 10% -> 90% rise time; rise = last third vs first third level (dB)
    hop = SR // 1000
    n = len(a) // hop
    env = np.abs(a[: n * hop]).reshape(n, hop).max(1)
    pk = int(np.argmax(env))
    i10 = int(np.argmax(env >= 0.1 * env[pk]))
    i90 = int(np.argmax(env >= 0.9 * env[pk]))
    attack_ms = float(max(i90 - i10, 0) + 1)
    act = env[int(m["onset"] * 1000):int(m["end"] * 1000) + 1]
    third = max(len(act) // 3, 1)
    rise = float(20 * np.log10((np.sqrt((act[-third:] ** 2).mean()) + 1e-9) / (np.sqrt((act[:third] ** 2).mean()) + 1e-9)))
    return {**m, "tp_db": r3(tp), "lufs": r3(lufs), "centroid_hz": round(centroid), "attack_ms": round(attack_ms, 1),
            "rise_db": r3(rise)}


# --------------------------------------------------------------------------- draft guesses
KEYWORDS: list[tuple[str, str]] = [  # first match wins; patterns match at a word start
    (r"(?<![a-z])(meme|vine|bruh|airhorn|air-horn|scratch|trombone|fail|laugh|sitcom)", "meme"),
    (r"(?<![a-z])(downlift|down-lift|downshift|fall)", "downlifter"),
    (r"(?<![a-z])(riser|rise|uplift|build[- ]?up|tension)", "riser"),
    (r"(?<![a-z])sub(?![a-z])|(?<![a-z])(boom|808)", "sub-hit"),
    (r"(?<![a-z])(whoosh|woosh|swoosh|swosh)", "whoosh"),
    (r"(?<![a-z])(swish|swipe|flick)", "swish"),
    (r"(?<![a-z])(impact|hit|slam|punch|thud|stomp|cinematic|drop)", "impact"),
    (r"(?<![a-z])(typing|typewriter|keyboard|keystroke)", "typing"),
    (r"(?<![a-z])(camera|shutter)", "camera"),
    (r"(?<![a-z])(cash|coin|money|register|kaching|ka-ching)", "cash"),
    (r"(?<![a-z])(alarm|siren|buzzer|warning|beep|timer|countdown)", "alarm"),
    (r"(?<![a-z])(glitch|static|error|corrupt|digital)", "glitch"),
    (r"(?<![a-z])(sparkle|glitter|magic)", "sparkle"),
    (r"(?<![a-z])(shine|shimmer|glint|twinkle)", "shine"),
    (r"(?<![a-z])(chime|bell)", "chime"),
    (r"(?<![a-z])(ding|ping|notification|success|correct|level-?up)", "ding"),
    (r"(?<![a-z])(tap|knock)", "tap"),
    (r"(?<![a-z])(click|key|switch|button|tick)", "click"),
    (r"(?<![a-z])(pop|bubble|blip|bloop)", "pop"),
    (r"(?<![a-z])(ambient|ambience|drone|atmos|room-?tone)", "ambient"),
]
ROLE_VIBE = {"whoosh": ["hype", "techy"], "swish": ["playful", "techy"], "impact": ["hype", "premium"],
             "sub-hit": ["hype", "premium", "tense"], "riser": ["tense", "hype"], "downlifter": ["tense", "calm"],
             "pop": ["playful", "techy"], "click": ["techy", "calm"], "tap": ["calm", "organic"], "typing": ["techy"],
             "shine": ["premium", "calm"], "chime": ["calm", "premium"], "ding": ["playful", "premium"],
             "sparkle": ["premium", "playful"], "glitch": ["techy", "tense"], "alarm": ["tense"],
             "camera": ["organic", "playful"], "cash": ["playful"], "meme": ["comedic", "playful"],
             "ambient": ["calm", "organic"]}
NAME_VIBE = [(r"\b(soft|gentle|calm|smooth)", "calm"), (r"\b(cinematic|premium|luxury|epic)", "premium"),
             (r"\b(cartoon|funny|comic|silly)", "comedic"), (r"\b(tech|digital|ui|cyber|robot|data)", "techy"),
             (r"\b(wood|nature|organic|paper|cloth)", "organic"), (r"\b(tense|dark|horror|scary|suspense)", "tense")]
ROLE_USE = {"whoosh": ["transition", "card-in", "card-out"], "swish": ["transition", "card-out"],
            "impact": ["hook-stop", "reveal", "number"], "sub-hit": ["hook-stop", "reveal"],
            "riser": ["reveal", "transition"], "downlifter": ["transition"], "pop": ["text-pop", "card-in", "list-cue"],
            "click": ["text-pop", "data", "list-cue"], "tap": ["data", "list-cue"], "typing": ["data", "text-pop"],
            "shine": ["reveal", "success"], "chime": ["success", "cta"], "ding": ["success", "list-cue"],
            "sparkle": ["reveal", "success", "cta"], "glitch": ["warning", "transition"], "alarm": ["warning"],
            "camera": ["reveal"], "cash": ["number", "success"], "meme": ["comedy"], "ambient": ["reveal"]}
ROLE_ENERGY = {"whoosh": 3, "swish": 2, "impact": 4, "sub-hit": 5, "riser": 3, "downlifter": 2, "pop": 2, "click": 1,
               "tap": 1, "typing": 1, "shine": 2, "chime": 2, "ding": 2, "sparkle": 2, "glitch": 3, "alarm": 4,
               "camera": 2, "cash": 3, "meme": 4, "ambient": 1}


# category (owner's SFX_Descriptions.csv) -> (default role, roles the name/description keywords may refine it to)
CATEGORY_ROLE = {
    "whoosh/transition": ("whoosh", {"whoosh", "swish", "riser", "downlifter"}),
    "glitch/digital": ("glitch", {"glitch", "typing", "click", "pop", "alarm"}),
    "impact/hit": ("impact", {"impact", "sub-hit"}),
    "ding/shine/magic": ("ding", {"ding", "shine", "chime", "sparkle"}),
    "ui/click/pop": ("click", {"click", "pop", "tap", "typing"}),
    "typing/keyboard": ("typing", {"typing"}),
    "cartoon/comedy": ("meme", {"meme"}),
    "camera": ("camera", {"camera"}),
    "music sting/logo": ("impact", {"impact", "sub-hit", "riser", "whoosh"}),
    "riser/build": ("riser", {"riser", "downlifter"}),
    "texture/ambience": ("ambient", {"ambient"}),
    "voice/meme": ("meme", {"meme"}),
    "other": (None, None),
}
USE_WORDS = [(r"transition|slide|swipe|sweep|pan\b|whip|cut between", "transition"), (r"\b(text|title|caption|label|word)", "text-pop"),
             (r"reveal|logo|intro|unveil|opener", "reveal"), (r"\bcard|\bui\b|button|pop-?up|window", "card-in"),
             (r"\bdata\b|typing|code|terminal|digital|download|loading", "data"), (r"number|price|money|profit|cash|sales|count", "number"),
             (r"warning|error|alarm|danger|countdown|time pressure|crash|fail", "warning"), (r"success|win\b|correct|level.?up|achiev|done|complete", "success"),
             (r"\bcta\b|subscribe|follow|comment|outro|end card", "cta"), (r"hook|slam|punch|big (?:hit|moment)|stop|impact", "hook-stop"),
             (r"\blist\b|\bitem\b|\bstep\b|each point|next", "list-cue"), (r"funny|comed|meme|joke|fail\b|gag|laugh|cartoon", "comedy")]


def guess_role(text: str, f: dict | None, category: str | None = None) -> str | None:
    name = text.lower().replace("_", "-").replace(" ", "-")
    allowed = None
    if category:
        default, allowed = CATEGORY_ROLE.get(category.strip().lower(), (None, None))
        if allowed is not None:
            for pat, role in KEYWORDS:
                if role in allowed and re.search(pat, name):
                    return role
            return default
    for pat, role in KEYWORDS:
        if re.search(pat, name):
            return role
    if f is None:
        return None
    d, atk, cen, rise = f["dur"], f["attack_ms"], f["centroid_hz"], f["rise_db"]
    if d >= 1.0 and rise >= 6:
        return "riser"
    if d >= 0.8 and rise <= -6 and cen < 1500:
        return "downlifter"
    if d < 0.3 and atk <= 4 and cen >= 2500:
        return "click"
    if d < 0.3:
        return "pop"
    if atk <= 8 and cen < 400:
        return "sub-hit"
    if atk <= 12 and d < 2.5:
        return "impact"
    if 0.3 <= d <= 1.6 and cen >= 1200:
        return "whoosh"
    return None


def draft_tags(text: str, f: dict | None, category: str | None = None, best_use: str = "") -> dict:
    role = guess_role(text, f, category)
    if role is None:
        return {"role": None, "vibe": [], "energy": None, "use": []}
    low = (text + " " + best_use).lower()
    vibe = list(ROLE_VIBE[role])
    for pat, v in NAME_VIBE:
        if re.search(pat, low) and v not in vibe:
            vibe.insert(0, v)
    energy = ROLE_ENERGY[role]
    if f is not None:
        energy += 1 if f["lufs"] > -16 else -1 if f["lufs"] < -32 else 0
    else:
        energy += 1 if re.search(r"\b(loud|heavy|big|huge|hard|massive|epic|deep)", low) else -1 if re.search(r"\b(quiet|soft|subtle|gentle|needs gain)", low) else 0
    use = list(ROLE_USE[role])
    for pat, u in USE_WORDS:
        if u not in use and re.search(pat, (best_use or low).lower()):
            use.append(u)
    return {"role": role, "vibe": vibe[:3], "energy": int(min(5, max(1, energy))), "use": use[:4]}


def slug(rel: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", Path(rel).with_suffix("").as_posix().lower())).strip("-") or "sfx"


# --------------------------------------------------------------------------- descriptions (owner's SFX_Descriptions.csv)
EXCLUDE_RE = re.compile(r"do\s*n[o']?t\s+use|don.?t\s+use|never\s+use|not\s+for\s+use|exclude|unusable", re.I)
DUP_RE = re.compile(r"\b(?:mp3|wav|aiff?)\s+copy\b|\bduplicate\b|^\s*same as\b", re.I)
COPYRIGHT_RE = re.compile(r"\bfrom\s+'[^']+'|(?<!no )(?<!no-)\bcopyright(?:ed)?\b(?!.free)", re.I)
SONG_RE = re.compile(r"\bsong\b|\btrack\b|music bed|\bbackground music\b", re.I)
MAX_STING_S = 20.0


def _hdr_slug(h: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", h.lower()).strip("_") or "col"


def _key(x: str) -> str:
    return x.replace("\\", "/").strip().lower()


def _noext(x: str) -> str:
    return re.sub(r"\.(wav|mp3|ogg|m4a|aif|aiff|flac)$", "", x)


def read_descriptions(path: Path) -> tuple[list[dict], dict]:
    """Flexible CSV reader. Detects the filename/path column by header keywords (file, path, name, sound, sfx) and keeps every
    other column as desc_<header> (e.g. desc_category, desc_length, desc_description, desc_best_use). Returns (rows, index):
    rows = [{"file": name, "desc": {...}}], index maps the lower-cased path, basename, and the same without extension to a row."""
    raw = path.read_text(encoding="utf-8-sig", errors="replace")
    try:
        dialect = csv.Sniffer().sniff(raw[:4096], delimiters=",;\t|")
    except csv.Error:
        dialect = csv.excel
    table = [r for r in csv.reader(raw.splitlines(), dialect) if any(c.strip() for c in r)]
    if len(table) < 2:
        raise VeosError("BAD_DESCRIPTIONS", f"{path.name} has no data rows", "Pass the owner's SFX_Descriptions.csv (header row + one row per sound).")
    hdr = [h.strip() for h in table[0]]
    low = [h.lower() for h in hdr]
    fcol = next((i for k in ("file", "path", "filename", "name", "sound", "sfx") for i, h in enumerate(low) if k in h), 0)
    rows, index = [], {}
    for r in table[1:]:
        r = r + [""] * (len(hdr) - len(r))
        name = r[fcol].strip().replace("\\", "/")
        if not name:
            continue
        row = {"file": name, "desc": {f"desc_{_hdr_slug(h)}": r[i].strip() for i, h in enumerate(hdr) if i != fcol and r[i].strip()}}
        rows.append(row)
        k = _key(name)
        index.setdefault(k, row)
    for row in rows:  # weaker keys only after every exact path is registered (so a .wav and its .mp3 never swap)
        k = _key(row["file"])
        for alt in (k.rsplit("/", 1)[-1], _noext(k), _noext(k.rsplit("/", 1)[-1])):
            index.setdefault("~" + alt, row)
    return rows, index


def _lookup(rel: str, index: dict) -> dict | None:
    k = _key(rel)
    return index.get(k) or index.get("~" + k) or index.get("~" + k.rsplit("/", 1)[-1]) or index.get("~" + _noext(k)) \
        or index.get("~" + _noext(k.rsplit("/", 1)[-1]))


def _csv_dur(d: dict) -> float | None:
    m = re.search(r"([\d.]+)\s*s", d.get("desc_length", ""))
    return float(m.group(1)) if m else None


def exclusion_reason(rel: str, d: dict, dur: float | None) -> str | None:
    """Why a sound must not be used, from the owner's description (None = usable)."""
    text = " ".join(v for k, v in d.items() if k in ("desc_description", "desc_best_use")) or " ".join(d.values())
    cat = d.get("desc_category", "")
    if DUP_RE.search(text):
        return "duplicate"
    if EXCLUDE_RE.search(text):
        return "do_not_use"
    if COPYRIGHT_RE.search(text):
        return "copyrighted"
    if SONG_RE.search(text) or ("music" in cat.lower() and dur is not None and dur > MAX_STING_S):
        return "song"
    return None


# --------------------------------------------------------------------------- veos sfx catalog
MEASURE_KEYS = ("peak_t", "onset", "end", "tp_db", "lufs", "centroid_hz", "attack_ms")


def catalog(args) -> dict:
    """Build/refresh catalog.json. Sources: the pack folder (--pack: measured), the descriptions CSV (--descriptions), or both.
    Descriptions-only works without any audio (measured: false; the numbers are measured on demand after `veos sfx fetch`).
    Writes <pack>/catalog.json, or the app catalogue (assets/sfx/catalog.json) when there is no --pack or with --update."""
    pack_arg, update = getattr(args, "pack", None), bool(getattr(args, "update", False))
    pack = Path(pack_arg) if pack_arg else None
    if pack is not None and not pack.is_dir():
        raise VeosError("PACK_MISSING", f"SFX pack folder not found: {pack}",
                        "Pass the full pack folder (the SFX folder with the audio), or catalogue from --descriptions CSV alone.")
    if pack is None and not getattr(args, "descriptions", None):
        raise VeosError("NOTHING_TO_CATALOG", "give --pack DIR and/or --descriptions FILE.csv",
                        "e.g. veos sfx catalog --descriptions assets/sfx/SFX_Descriptions.csv")
    dest = catalog_file(None) if (update or pack is None) else catalog_file(pack_arg)
    old_doc = read_catalog_doc(dest) or {}
    old = {e["file"]: e for e in old_doc.get("sounds", [])}
    rows, index = read_descriptions(Path(args.descriptions)) if getattr(args, "descriptions", None) else ([], {})
    want_draft = bool(args.draft or rows)
    items: dict[str, tuple[Path | None, dict | None]] = {}
    used_rows: set[int] = set()
    if pack is not None:
        for p in sorted(p for p in pack.rglob("*") if p.is_file() and p.suffix.lower() in EXTS):
            rel = p.relative_to(pack).as_posix()
            row = _lookup(rel, index) if index else None
            if row is not None:
                used_rows.add(id(row))
            items[rel] = (p, row)
    missing_audio = 0
    for row in rows:
        if id(row) not in used_rows:
            rel = row["file"]
            if rel not in items:
                items[rel] = (None, row)
                missing_audio += 1
    ids_used: set[str] = {e["id"] for r, e in old.items() if r in items and e.get("id")}
    out, warnings = [], []
    for rel in sorted(items, key=lambda r: (r.lower().endswith(".mp3"), r.lower())):
        p, row = items[rel]
        prev = old.get(rel) or {}
        d = dict(row["desc"]) if row else {k: v for k, v in prev.items() if k.startswith("desc_")}
        f = None
        if p is not None:
            try:
                f = features(p)
            except VeosError as e:
                warnings.append(e.message)
                continue
        reviewed = prev.get("tags_from") == REVIEWED
        cid = prev.get("id")
        if not cid:
            cid = slug(rel)
            if cid in ids_used:
                cid = f"{cid}-{Path(rel).suffix.lstrip('.').lower()}"
            if cid in ids_used:
                cid = f"{cid}-{hashlib.sha1(rel.encode('utf-8')).hexdigest()[:4]}"
        ids_used.add(cid)
        measured = f is not None or bool(prev.get("measured", prev.get("peak_t") is not None))
        dur = f["dur"] if f else prev.get("dur") if prev.get("dur") is not None else _csv_dur(d)
        if reviewed:
            tags = prev
        elif want_draft:
            tags = draft_tags(rel + " " + d.get("desc_description", ""), f, d.get("desc_category"), d.get("desc_best_use", ""))
        else:
            tags = prev
        tags = {"role": tags.get("role"), "vibe": tags.get("vibe") or [], "energy": tags.get("energy"), "use": tags.get("use") or []}
        anchor = prev["anchor"] if reviewed and prev.get("anchor") in ANCHORS else default_anchor(tags["role"], (f or {}).get("attack_ms"))
        meas = {k: (f[k] if f else prev.get(k)) for k in MEASURE_KEYS}
        reason = exclusion_reason(rel, d, dur) if (rows or not prev) else prev.get("excluded_reason")
        e = {"file": rel, "id": cid, "dur": dur, "peak_t": meas["peak_t"], "onset": meas["onset"], "end": (f or prev).get("end"),
             "anchor": anchor, "role": tags["role"], "vibe": tags["vibe"], "energy": tags["energy"], "use": tags["use"],
             "tags_from": REVIEWED if reviewed else "draft",
             "tp_db": meas["tp_db"], "lufs": meas["lufs"], "centroid_hz": meas["centroid_hz"], "attack_ms": meas["attack_ms"],
             "size": p.stat().st_size if p is not None else prev.get("size"), "measured": measured,
             "excluded": reason is not None, "excluded_reason": reason}
        if prev.get("url"):
            e["url"] = prev["url"]
        e.update(d)
        out.append(e)
    doc = {"base_url": old_doc.get("base_url"), "sounds": out}
    base = doc["base_url"] or DEFAULT_BASE_URL
    for e in out:
        e.setdefault("url", entry_url(e, base))
    write_catalog_doc(dest, doc)
    gone = sorted(set(old) - set(items))
    if gone:
        warnings.append(f"{len(gone)} catalogued file(s) are no longer in the pack/descriptions and were dropped")
    if rows and pack is not None and missing_audio:
        warnings.append(f"{missing_audio} described file(s) were not found in the pack (kept unmeasured)")
    if pack is not None and index:
        nodesc = sum(1 for rel, (p, row) in items.items() if row is None and p is not None)
        if nodesc:
            warnings.append(f"{nodesc} audio file(s) have no row in the descriptions file")
    reasons: dict[str, int] = {}
    for e in out:
        if e["excluded"]:
            reasons[e["excluded_reason"]] = reasons.get(e["excluded_reason"], 0) + 1
    return {"catalog": dest.as_posix(), "sounds": len(out), "measured": sum(1 for e in out if e["measured"]),
            "excluded": sum(reasons.values()), "excluded_by_reason": reasons,
            "mb": round(sum(e["size"] or 0 for e in out) / 1e6, 1),
            "reviewed": sum(1 for e in out if e["tags_from"] == REVIEWED), "untagged": sum(1 for e in out if not e["role"]),
            "by_role": {r: sum(1 for e in out if e["role"] == r and not e["excluded"]) for r in ROLES
                        if any(e["role"] == r and not e["excluded"] for e in out)},
            "warnings": warnings}


# --------------------------------------------------------------------------- veos sfx tag
def tag(args) -> dict:
    dest = catalog_file(getattr(args, "pack", None))
    doc = read_catalog_doc(dest)
    if doc is None:
        raise VeosError("NO_CATALOG", f"{dest} not found", "Run `veos sfx catalog --pack DIR` first.")
    cat = doc["sounds"]
    tf = Path(args.out) if getattr(args, "out", None) else None
    if tf is None or not tf.exists():
        raise VeosError("TAGS_MISSING", f"tags file not found: {tf}", "Pass the tags.json path: veos sfx tag --pack DIR tags.json")
    tags = read_json(tf)
    by_id = {e["id"]: e for e in cat}
    n = 0
    for cid, t in tags.items():
        e = by_id.get(cid)
        if e is None:
            raise VeosError("UNKNOWN_ID", f"tags.json has id '{cid}' which is not in the catalogue", "Use ids from catalog.json.")
        role = t.get("role", e.get("role"))
        vibe, use, energy = t.get("vibe", e.get("vibe") or []), t.get("use", e.get("use") or []), t.get("energy", e.get("energy"))
        bad = []
        if role is not None and role not in ROLES:
            bad.append(f"role '{role}' (allowed: {', '.join(ROLES)})")
        bad += [f"vibe '{v}' (allowed: {', '.join(VIBES)})" for v in vibe if v not in VIBES]
        bad += [f"use '{u}' (allowed: {', '.join(USES)})" for u in use if u not in USES]
        if energy is not None and (not isinstance(energy, int) or isinstance(energy, bool) or not 1 <= energy <= 5):
            bad.append(f"energy {energy!r} (must be an integer 1-5)")
        if t.get("anchor") is not None and t["anchor"] not in ANCHORS:
            bad.append(f"anchor '{t['anchor']}' (peak, onset or end)")
        if bad:
            raise VeosError("BAD_TAGS", f"{cid}: invalid " + "; ".join(bad), "Use only the vocabulary in engine/SPEC.md section 6.")
        e.update({"role": role, "vibe": list(vibe), "energy": energy, "use": list(use), "tags_from": REVIEWED})
        e["anchor"] = t.get("anchor") or (default_anchor(role, e.get("attack_ms")) if "role" in t else e.get("anchor", "onset"))
        n += 1
    write_catalog_doc(dest, doc)
    return {"catalog": dest.as_posix(), "tagged": n, "reviewed": sum(1 for e in cat if e["tags_from"] == REVIEWED),
            "still_draft": sum(1 for e in cat if e.get("tags_from") != REVIEWED)}


# --------------------------------------------------------------------------- fetch (on-demand download into the cache)
def _download(url: str, dst: Path, size: int | None) -> int:
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_name(dst.name + ".part")
    last = ""
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r, open(tmp, "wb") as fh:
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    fh.write(b)
            got = tmp.stat().st_size
            if size and got != size:
                raise OSError(f"size {got} != expected {size}")
            tmp.replace(dst)
            return got
        except Exception as e:  # noqa: BLE001 - retry, then report
            last = str(e)
            time.sleep(0.5 * (attempt + 1))
    tmp.unlink(missing_ok=True)
    raise VeosError("SFX_DOWNLOAD_FAILED", f"could not download {dst.name} after 3 tries ({last[:120]})",
                    "Check the internet connection and run `veos sfx fetch` again.")


def fetch_entries(entries: list[dict], pack: Path, base_url: str | None, tolerant: bool = False) -> dict:
    """Download only what is missing (or the wrong size) into `pack`/<relpath>. `tolerant`: a sound that cannot be
    downloaded (no URL, 404, offline) is skipped and listed in `failed` [{id, file, why}] instead of raising."""
    got, skipped, nbytes, failed = [], 0, 0, []
    for e in entries:
        dst = pack / e["file"]
        if dst.exists() and (not e.get("size") or dst.stat().st_size == e["size"]):
            skipped += 1
            continue
        try:
            url = entry_url(e, base_url)
            if not url:
                raise VeosError("NO_SFX_URL", f"no download url for '{e['id']}' and the file is not in {pack}",
                                "The catalogue needs base_url (tools/publish_sfx.py writes it).")
            nbytes += _download(url, dst, e.get("size"))
        except VeosError as err:
            if not tolerant:
                raise
            failed.append({"id": e["id"], "file": Path(e["file"]).name, "why": err.message})
            continue
        got.append(e["id"])
    out = {"downloaded": len(got), "already_cached": skipped, "mb_downloaded": round(nbytes / 1e6, 2), "ids": got}
    if tolerant:
        out["failed"] = failed
    return out


def ensure_cached(cat_doc_or_list, ids, pack: Path, tolerant: bool = False) -> dict:
    doc = cat_doc_or_list if isinstance(cat_doc_or_list, dict) else {"sounds": cat_doc_or_list}
    by_id = {e["id"]: e for e in doc["sounds"]}
    miss = [i for i in ids if i not in by_id]
    if miss:
        raise VeosError("UNKNOWN_SFX", f"sound id(s) not in the catalogue: {', '.join(sorted(set(miss)))}",
                        "Pick ids from the app's assets/sfx/catalog.json.")
    bad = [i for i in dict.fromkeys(ids) if by_id[i].get("excluded")]
    if bad:
        raise VeosError("SFX_EXCLUDED", f"sound(s) marked do-not-use ({by_id[bad[0]].get('excluded_reason')}): {', '.join(bad)}",
                        "Pick other sounds; excluded ones are never fetched or used.")
    return fetch_entries([by_id[i] for i in dict.fromkeys(ids)], pack, doc.get("base_url"), tolerant)


def fetch(args, project=None) -> dict:
    pack = pack_dir(getattr(args, "pack", None))
    doc = read_catalog_doc(catalog_file(getattr(args, "pack", None)))
    if doc is None:
        raise VeosError("NO_CATALOG", "no catalog.json found", "Reinstall/update the plugin (it ships assets/sfx/catalog.json).")
    ids: list[str] = [i for i in (getattr(args, "ids", None) or "").split(",") if i.strip()]
    ids = [i.strip() for i in ids]
    pb = getattr(args, "playbook", None)
    if pb:
        from .tokens import load_playbook
        snd = load_playbook(pb).get("sound") or {}
        ids += list(snd.get("preferred") or []) + list(snd.get("palette_ids") or [])
    if project is not None:
        tlp = project.root / "plan" / "timeline.json"
        if not tlp.exists():
            raise VeosError("NO_TIMELINE", f"{tlp} not found", "Write plan/timeline.json first.")
        ids += [c["id"] for c in read_json(tlp).get("sfx") or [] if c.get("id")]
    if not ids:
        raise VeosError("NOTHING_TO_FETCH", "no sound ids given", "Use --ids a,b,c, --playbook ID or --project P.")
    r = ensure_cached(doc, ids, pack, tolerant=True)
    out = {"pack": pack.as_posix(), "requested": len(set(ids)), **{k: v for k, v in r.items() if k != "ids"}}
    if r.get("failed"):
        out["warnings"] = [skip_note(f) for f in r["failed"]]
    return out


def skip_note(f: dict, t: float | None = None) -> str:
    """One warning line for a sound that could not be downloaded and was left out."""
    at = f" (cue at {t:.2f} s)" if t is not None else ""
    return (f"skipped sound '{f['id']}' ({f['file']}){at}: it could not be downloaded ({f['why'][:120]}); "
            "the rest plays. Swap it for another catalogue id or drop the cue.")


# --------------------------------------------------------------------------- timeline -> bus
def cue_db(cue: dict, entry: dict) -> float:
    if cue.get("db") is not None:
        return float(cue["db"])
    return float(DEFAULT_DB.get(entry.get("role"), FALLBACK_DB))


def anchor_time(entry: dict) -> float:
    return float(entry.get({"peak": "peak_t", "onset": "onset", "end": "end"}.get(entry.get("anchor") or "onset", "onset"), 0.0))


def voice_reference_db(voice_wav: Path) -> float | None:
    """Median 400 ms RMS (dB) of the voice where it is speaking (> -40 dB); None when there is no speech."""
    v = audio.decode_mono(voice_wav)
    win = int(0.4 * SR)
    db = [20 * np.log10(np.sqrt((v[i:i + win].astype(np.float64) ** 2).mean()) + 1e-9) for i in range(0, len(v) - win, win // 2)]
    db = [d for d in db if d > -40]
    return float(np.median(db)) if db else None


REF_VOICE_DB = -18.0   # cue dB defaults assume a voice whose speaking RMS is -18 dBFS; the bus is shifted to the real voice


def build_cuesheet(tl: dict, cat: list[dict], offset_db: float = 0.0, skip=()) -> list[dict]:
    """The bus cue sheet; cues whose id is in `skip` (sounds that could not be downloaded) are left out."""
    by_id = {e["id"]: e for e in cat}
    sheet = []
    for c in sorted(tl.get("sfx") or [], key=lambda x: x.get("t", 0)):
        if c.get("id") in skip:
            continue
        if "id" not in c:
            raise VeosError("LEGACY_CUE", f"sfx cue at {c.get('t')} s uses 'file', not a catalogue 'id'",
                            "Rewrite the cue as {t, id, on, why} (renderer/CONTRACT.md section 2).")
        e = by_id.get(c["id"])
        if e is None:
            raise VeosError("UNKNOWN_SFX", f"sfx id '{c['id']}' (cue at {c.get('t')} s) is not in the catalogue",
                            "Pick an id from the pack's catalog.json (or re-run `veos sfx catalog`).")
        if e.get("excluded"):
            raise VeosError("SFX_EXCLUDED", f"sound '{c['id']}' is marked do-not-use in the pack description",
                            "Pick another sound (S6 reports this too).")
        a = anchor_time(e)
        sheet.append({"t": float(c["t"]), "f": e["file"], "a": a, "db": r3(cue_db(c, e) + offset_db), "id": e["id"],
                      "role": e.get("role"), "beat": c.get("beat"),
                      "span": [r3(float(c["t"]) - (a - e["onset"])), r3(float(c["t"]) + (e["end"] - a))]})
    return sheet


def build_bus(tl: dict, cat, pack: Path, voice_wav: Path | None, out: Path) -> dict:
    """Timeline sfx -> mono bus WAV `out` (+ `<out>.cues.json` next to it for the mix gate). Missing sound files are downloaded
    into `pack` first; a sound that cannot be downloaded is skipped and named in `warnings` / `skipped` (the bus, the
    storyboard and the mix still build). `cat` is the catalogue doc (or its list of sounds)."""
    doc = cat if isinstance(cat, dict) else {"sounds": cat}
    cat = doc["sounds"]
    want = [c["id"] for c in tl.get("sfx") or [] if c.get("id")]
    fetched = ensure_cached(doc, want, pack, tolerant=True)
    failed = {f["id"]: f for f in fetched.get("failed") or []}
    skipped_notes = []
    for c in sorted(tl.get("sfx") or [], key=lambda x: x.get("t", 0)):
        if c.get("id") in failed:
            skipped_notes.append(skip_note(failed[c["id"]], float(c.get("t", 0) or 0)))
    for e in cat:  # descriptions-only entries have no measurements yet: measure the downloaded file now
        if e["id"] in want and e["id"] not in failed and e.get("peak_t") is None:
            f = features(pack / e["file"])
            e.update({k: f[k] for k in MEASURE_KEYS if k in f} | {"dur": f["dur"], "end": f["end"], "measured": True})
            e["anchor"] = e.get("anchor") or default_anchor(e.get("role"), f["attack_ms"])
    dur = float(tl["meta"]["duration"])
    offset, ref = 0.0, None
    if voice_wav is not None and voice_wav.exists():
        ref = voice_reference_db(voice_wav)
        if ref is not None:
            offset = ref - REF_VOICE_DB
    sheet = build_cuesheet(tl, cat, offset, skip=set(failed))
    mix, ledger, warnings, n = audio.place(sheet, pack, {}, dur)
    warnings = skipped_notes + warnings
    audio._write_wav(out, mix)
    write_json(out.with_suffix(".cues.json"), {"voice_offset_db": r3(offset), "cues": sheet}, indent=1)
    by_id = {e["id"]: e for e in cat}
    draft = sorted({c["id"] for c in sheet if by_id[c["id"]].get("tags_from") != REVIEWED})
    if draft:
        warnings.append(f"{len(draft)} sound(s) still have draft tags: {', '.join(draft)}")
    return {"cues": n, "files": len(ledger), "bus_peak_db": r3(20 * np.log10(float(np.abs(mix).max()) + 1e-12)),
            "dur": r3(len(mix) / SR), "voice_ref_db": None if ref is None else r3(ref), "voice_offset_db": r3(offset),
            "downloaded": fetched["downloaded"], "mb_downloaded": fetched["mb_downloaded"], "warnings": warnings,
            "skipped": sorted(failed)}


def build_project_bus(project, args=None) -> dict:
    tl_path = project.root / "plan" / "timeline.json"
    if not tl_path.exists():
        raise VeosError("NO_TIMELINE", f"{tl_path} not found", "Write plan/timeline.json first.")
    tl = read_json(tl_path)
    pack = pack_dir(getattr(args, "pack", None))
    cat = read_catalog_doc(catalog_file(getattr(args, "pack", None)))
    if cat is None:
        raise VeosError("NO_CATALOG", "no catalog.json found (see `veos paths` sfx_catalog)",
                        "Update the plugin, or run `veos sfx catalog --pack DIR` if you own the pack.")
    out = project.work / "sfx.wav"
    res = build_bus(tl, cat, pack, project.work / "voice.wav", out)
    return {"out": project.rel(out), "cues_file": project.rel(out.with_suffix(".cues.json")), **res}


# --------------------------------------------------------------------------- balance gate (used by `veos mix --sfx`)
MEDIAN_MIN_UNDER_DB = 20.0
CUE_MIN_UNDER_DB = 6.0


def check_balance(voice: Path, sfx: Path) -> dict:
    """Median SFX level vs the voice, and (when `<sfx>.cues.json` exists) every non-sub cue vs the voice while speech is present."""
    bal = audio.balance(voice, sfx)
    problems = []
    if bal["median_db"] is not None and bal["median_db"] > -MEDIAN_MIN_UNDER_DB:
        problems.append(f"the median sound-effect level is only {-bal['median_db']:.1f} dB under the voice (needs at least "
                        f"{MEDIAN_MIN_UNDER_DB:.0f} dB)")
    cf = Path(sfx).with_suffix(".cues.json")
    if cf.exists():
        v, x = audio.decode_mono(voice), audio.decode_mono(sfx)
        win = int(0.4 * SR)
        db = lambda s: 20 * np.log10(np.sqrt((s.astype(np.float64) ** 2).mean()) + 1e-9)  # noqa: E731
        for c in read_json(cf).get("cues", []):
            if c.get("role") == "sub-hit":
                continue
            a, b = int(max(c["span"][0], 0) * SR), int(c["span"][1] * SR)
            gap = None
            for i in range(a, max(b - win // 2, a + 1), win // 2):
                vs, xs = v[i:i + win], x[i:i + win]
                if len(vs) < win // 2 or db(vs) <= -40:
                    continue
                d = db(xs) - db(vs)
                gap = d if gap is None else max(gap, d)
            if gap is not None and gap > -CUE_MIN_UNDER_DB:
                problems.append(f"'{c.get('id')}' at {c['t']:.2f} s is only {-gap:.1f} dB under the voice (needs at least "
                                f"{CUE_MIN_UNDER_DB:.0f} dB while someone is speaking)")
    return {**bal, "problems": problems}
