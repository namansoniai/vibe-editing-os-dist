"""`veos templates list|copy|gallery|check`: path A of the playbook setup (pick a style -> brand it -> edit).

list                       the shipped templates (playbooks/_styles/<id>/, TEMPLATE-PACKAGE.md) with name, inspired_by,
                           needs, readiness, tier (core / full), section, languages, CTA devices, brandable roles and
                           preview paths. Templates that need an engine capability this install doesn't have are hidden
                           (`--all` shows them).
copy <id> --name N [--handle @h] [--colors ...] [--language english|hinglish|hinglish-en|hindi] [--currency X]
          [--cta device[:value]] [--id ID]
                           the buyer's branded copy in the user playbooks folder: brand variables (BV-01/02/05/06/08)
                           applied (buyers can change anything; only the never-bendable core is refused), a silent
                           contrast nudge, `kind: style_copy`, `lineage`, profile.md. Link it to a folder afterwards
                           with `veos workspace set --playbook <id>`.
gallery [--out F] [--faceless-first]
                           writes the picker page (default `<styles>/index.html`): a card per visible template;
                           `section: brands` templates go in a "For brands & agencies" section at the end.
check [ID ...]             validates template packages against TEMPLATE-PACKAGE.md (for template authors).

engine/SPEC.md section 8; playbooks/_styles/TEMPLATE-PACKAGE.md; structure Part D.
"""
from __future__ import annotations

import copy
import hashlib
import html
import importlib.util
import inspect
import os
import re
import shutil
from datetime import date, datetime, timezone
from pathlib import Path

from . import lineage, paths
from .core import VeosError, read_json, write_json
from .tokens import SCHEMA_V3, _get_path, _norm_hex, contrast, effective_style, fix_contrast, lock_for, schema_version
from .workspace import slug

PACKAGE = "veos.template/1"
STATUSES = ("draft", "released", "fixture")
READINESS = {
    "R1": "Ready",
    "R2": "Ready",  # shown only once its engine capability is installed
    "R4": "Ready · best with your own footage",
}
NOT_COPIED = {"template.json", "evidence.md", "index.html"}
FRAME_EXT = (".webp", ".png", ".jpg", ".jpeg", ".gif", ".avif")

LANG_NAMES = {"en": "English", "hi": "Hindi", "hinglish": "Hinglish", "ta": "Tamil", "te": "Telugu", "mr": "Marathi",
              "bn": "Bengali", "gu": "Gujarati", "kn": "Kannada", "ml": "Malayalam", "pa": "Punjabi", "ur": "Urdu",
              "es": "Spanish", "fr": "French", "de": "German", "pt": "Portuguese", "ar": "Arabic"}
SCRIPT_NAMES = {"Latn": "Latin script", "Deva": "Devanagari"}
INDIAN = {"hi", "hinglish", "ta", "te", "mr", "bn", "gu", "kn", "ml", "pa"}
# the three setup answers every template offers (structure D.3 BV-05); English is the default
LANG_OPTIONS = {"en/en/Latn": "English", "hinglish/hinglish/Latn": "Hinglish", "hinglish/en/Latn": "Hinglish speech, English captions",
                "hi/hi/Deva": "Hindi"}
LANG_LABELS = {"en/en/Latn": "English (English speech, English captions)",
               "hinglish/en/Latn": "Hinglish speech, English captions (translated)",
               "hinglish/hinglish/Latn": "Hinglish (Hinglish speech, captions in romanised Hinglish)",
               "hi/hi/Deva": "Hindi (Hindi speech, Devanagari captions)"}
LANG_ALIASES = {"english": "en/en/Latn", "en": "en/en/Latn", "hinglish": "hinglish/hinglish/Latn",
                "hinglish-en": "hinglish/en/Latn", "hinglish-english": "hinglish/en/Latn", "hinglish_en": "hinglish/en/Latn",
                "hinglish>en": "hinglish/en/Latn",
                "hindi": "hi/hi/Deva", "hi": "hi/hi/Deva"}
DEFAULT_LANG = "en/en/Latn"
HINGLISH_EN = "hinglish/en/Latn"  # BV-05 4th answer: Hinglish speech, English captions (transform translate)
NUMBERS_INTL = {"grouping": "international", "currency": "$", "compact": "k_m_b"}
NUMBERS_INDIAN = {"grouping": "indian", "currency": "₹", "compact": "lakh_crore"}
TIERS = ("core", "full")
SECTIONS = ("main", "brands")
ROTATION_NOTE = "Your brand colour replaces the per-reel colour rotation."

CTA_ALIASES = {"comment": "comment_keyword", "keyword": "comment_keyword", "link": "link_bio", "bio": "link_bio",
               "link_in_bio": "link_bio", "follow": "follow_save_stack", "save": "follow_save_stack",
               "subscribe": "subscribe", "dm": "dm", "none": "none", "no": "none"}
CTA_WORDS = {"comment_keyword": "comment keyword", "dm": "DM keyword", "link_bio": "link in bio", "qr": "QR code",
             "subscribe": "subscribe", "follow_save_stack": "follow / save", "product_card": "product card",
             "end_card": "end card", "cross_promo": "cross-promo", "post_only": "in the post text", "none": "no CTA"}

NEEDS = {  # source_type -> footage_dependency -> what the buyer has to shoot (the card's "needs:" line)
    "talking_head": {"none": "just you talking", "low": "just you talking", "medium": "you + screen recordings",
                     "high": "you + your own B-roll", "total": "you + the props and shots this style is built on"},
    "voiceover_only": "a voice-over only",
    "narrated_footage": "a voice-over + your own B-roll",
    "multi_speaker": "a conversation (two or more people on camera)",
    "edited_master": "an edited long video to re-cut",
    "stunt_footage": "raw event footage from several cameras",
    "animated_plates": "animation plates + a voice-over",
}


def add_args(p, cmd):
    p.add_argument("action", choices=["list", "copy", "gallery", "check"])
    p.add_argument("template", nargs="*", help="copy: the template id; check: template ids (default: all)")
    p.add_argument("--all", action="store_true", help="list: also show templates hidden for missing engine capabilities")
    p.add_argument("--name", help="copy BV-01: the buyer's name (or brand)")
    p.add_argument("--handle", help="copy BV-01: the buyer's handle, e.g. @riya.money")
    p.add_argument("--colors", "--colours", dest="colors",
                   help="copy BV-02: one or two hex colours for the brandable roles in order ('#FFFFFF,#7C5CFF'), "
                        "or role=hex pairs ('accent=#7C5CFF')")
    p.add_argument("--language", help="copy BV-05: english (default), hinglish, hinglish-en (Hinglish speech, English captions) or hindi; or a speech/captions/script "
                                      "entry of the template's `languages` (e.g. hinglish/hinglish/Latn)")
    p.add_argument("--currency", help="copy BV-06: the currency on screen (INR / Rs / the rupee glyph, or $ / EUR / GBP). "
                                      "Default: $ for English, rupees in lakh / crore for Hinglish and Hindi")
    p.add_argument("--cta", help="copy BV-08: device[:value], e.g. comment_keyword:BUDGET, link_bio:Free sheet, none")
    p.add_argument("--id", dest="new_id", help="copy: the new playbook id (default: a unique id from the name)")
    p.add_argument("--out", help="gallery: output file (default <styles>/index.html)")
    p.add_argument("--faceless-first", action="store_true", help="gallery: faceless (voice-over) templates first")


# ------------------------------------------------------------------ engine capabilities
def _module(name: str):
    return lambda: importlib.util.find_spec(f"veos.{name}") is not None


def _rule(vid: str):
    def probe():
        from .validate import REGISTRY
        return vid in REGISTRY
    return probe


def _file(rel: str):
    return lambda: (paths.app_root() / rel).exists()


def _vo_only() -> bool:
    try:
        from . import ingest
        return "--audio" in inspect.getsource(ingest.add_args)
    except (ImportError, OSError, TypeError):
        return False


# name -> (ENGINE-IMPLICATIONS item, probe). A template lists what it needs in template.json `requires`; a few are
# derived from its profile (derived_requires). Unknown names count as missing.
CAPABILITIES = {
    "tokens_v3": ("E-01", lambda: True),
    "caption_profiles": ("E-05", _module("capengine")),
    "type_floors": ("E-06", _rule("V-TYPE")),
    "layouts_v3": ("E-07", _file("renderer/layouts.js")),
    "worlds_v3": ("E-07", _file("renderer/worlds.js")),
    "chrome_slots": ("E-07", _rule("V-CHROME")),
    "data_figures": ("E-08", _rule("V-DATA")),
    "number_format": ("E-08", _rule("V-NUMFMT")),
    "running_state": ("E-09", _rule("V-STATE")),
    "inserts_flow": ("E-10", _rule("V-INSERTS")),
    "citations": ("E-10", _rule("V-CITE")),
    "vo_only": ("E-12", _vo_only),
    "multi_speaker": ("E-13", _rule("V-SPEAKER")),
    "diarisation": ("E-13", _module("speakers")),
    "canvas_camera": ("E-14", lambda: _module("canvascam")() and _file("renderer/canvascam.js")()),
    "anchors": ("E-15", _module("anchors")),
    "grades": ("E-16", _rule("V-GRADE")),
    "broll_bank": ("E-17", _module("broll")),
    "geo_maps": ("E-18", _file("assets/geo")),
    "continuity": ("E-19", _rule("V-CONTINUITY")),
}


def capabilities() -> dict[str, bool]:
    out = {}
    for name, (_item, probe) in CAPABILITIES.items():
        try:
            out[name] = bool(probe())
        except Exception:  # noqa: BLE001 - a broken probe means the capability is not usable
            out[name] = False
    return out


def derived_requires(profile: dict) -> list[str]:
    """Capabilities a profile needs whatever the author wrote: the engine can't even take the input without them."""
    req = []
    st = profile.get("source_type")
    if st == "voiceover_only":
        req.append("vo_only")
    if st == "multi_speaker" or (profile.get("modules") or {}).get("dialogue"):
        req += ["multi_speaker", "diarisation"]
    if (profile.get("modules") or {}).get("canvas_camera"):
        req.append("canvas_camera")
    return req


# ------------------------------------------------------------------ reading a package
def needs_line(profile: dict) -> str:
    st = profile.get("source_type") or "talking_head"
    v = NEEDS.get(st, "your own footage")
    if isinstance(v, dict):
        v = v.get(profile.get("footage_dependency") or "low", v["low"])
    return v


def is_faceless(profile: dict) -> bool:
    return (profile.get("presenter") or {}).get("presence") == "none" or profile.get("source_type") == "voiceover_only"


def _merged_profile(base: dict, fmt: dict) -> dict:
    p = copy.deepcopy(base)
    for k, v in ((fmt or {}).get("profile") or {}).items():
        if isinstance(v, dict) and isinstance(p.get(k), dict):
            p[k] = {**p[k], **v}
        else:
            p[k] = copy.deepcopy(v)
    return p


def lang_key(combo) -> str:
    speech, cap, script = (list(combo) + [None, None, None])[:3]
    return f"{speech}/{cap}/{script or ('Deva' if cap == 'hi' else 'Latn')}"


def lang_label(key: str) -> str:
    speech, cap, script = key.split("/")
    if key in LANG_LABELS:
        return LANG_LABELS[key]
    s = f"{LANG_NAMES.get(speech, speech)} speech → {LANG_NAMES.get(cap, cap)} captions"
    return s + (f" ({SCRIPT_NAMES.get(script, script)})" if script != "Latn" or cap in ("hi", "hinglish") else "")


def languages(profile: dict) -> tuple[str, list[str]]:
    lang = profile.get("language") or {}
    cap = lang.get("captions") or {}
    default = lang_key([lang.get("speech"), cap.get("lang"), cap.get("script")])
    keys = [lang_key(c) for c in (lang.get("supported") or []) if isinstance(c, (list, tuple)) and len(c) >= 2]
    if default not in keys:
        keys.insert(0, default)
    # Hinglish speech with English (translated) captions: every template with English Latin captions can do it (the
    # caption engine's `translate` transform); offered right after Hinglish
    if HINGLISH_EN not in keys and any(k.split("/")[1:] == ["en", "Latn"] for k in keys):
        at = keys.index("hinglish/hinglish/Latn") + 1 if "hinglish/hinglish/Latn" in keys else len(keys)
        keys.insert(at, HINGLISH_EN)
    return default, keys


def brandable_roles(tokens: dict) -> list[dict]:
    out = []
    fixed = set(tokens.get("fixed_meaning") or [])
    for r, v in (tokens.get("roles") or {}).items():
        if not isinstance(v, dict) or not v.get("brandable") or r in fixed:
            continue
        if lock_for(f"roles.{r}.default", tokens.get("locks"))[0] == "DNA":
            continue
        out.append({"role": r, "default": v.get("default"), "meaning": v.get("meaning")})
    return out


def _display_names(meta: dict, style: dict) -> list[str]:
    if meta.get("inspired_by_display"):
        return list(meta["inspired_by_display"])
    return [" ".join(w.capitalize() for w in re.split(r"[-_]", s)) for s in (style.get("inspired_by") or [])]


def _frames(d: Path, meta: dict) -> list[Path]:
    pv = meta.get("preview") or {}
    fr = [d / f for f in (pv.get("frames") or [])]
    if not fr and (d / "preview" / "frames").is_dir():
        fr = sorted(p for p in (d / "preview" / "frames").iterdir() if p.suffix.lower() in FRAME_EXT)
    return [f for f in fr if f.is_file()]


def read_package(d: Path, caps: dict[str, bool] | None = None) -> dict:
    """One template folder -> its card record (raises VeosError when the package is unreadable)."""
    caps = capabilities() if caps is None else caps
    try:
        meta = read_json(d / "template.json")
        tokens = read_json(d / "tokens.json")
    except (OSError, ValueError) as e:
        raise VeosError("BAD_TEMPLATE", f"template '{d.name}' is unreadable: {e}", "See TEMPLATE-PACKAGE.md.")
    style = tokens.get("style") or {}
    prof = tokens.get("profile") or {}
    fmts = []
    flist = (prof.get("formats") or {}).get("list") or list(tokens.get("formats") or {})
    for fid in flist:
        f = (tokens.get("formats") or {}).get(fid) or {}
        fp = _merged_profile(prof, f)
        need = derived_requires(fp)
        fmts.append({"id": fid, "name": f.get("name"), "when": f.get("when"), "needs": needs_line(fp),
                     "faceless": is_faceless(fp), "requires": need,
                     "available": all(caps.get(c, False) for c in need)})
    requires = sorted(set(meta.get("requires") or []) | set(derived_requires(prof)))
    missing = [c for c in requires if not caps.get(c, False)]
    readiness = meta.get("readiness") or "R1"
    available = not missing and readiness != "R3" and (not fmts or any(f["available"] for f in fmts))
    default_lang, langs = languages(prof)
    needs = meta.get("needs") or needs_line(prof)
    extra = sorted({f["needs"] for f in fmts if f["needs"] != needs})
    devices = list((prof.get("cta") or {}).get("devices") or [])
    page = d / ((meta.get("preview") or {}).get("page") or "preview/index.html")
    return {
        "id": d.name, "name": style.get("name") or d.name, "version": style.get("template_version") or tokens.get("version"),
        "status": style.get("status") or "draft", "order": meta.get("order", 50),
        "inspired_by": _display_names(meta, style), "own_style": not style.get("inspired_by"),
        "tagline": meta.get("tagline"), "needs": needs,
        "needs_by_format": {f["id"]: f["needs"] for f in fmts} if extra else {},
        "faceless": is_faceless(prof), "faceless_formats": [f["id"] for f in fmts if f["faceless"]],
        "readiness": readiness, "readiness_label": READINESS.get(readiness, readiness),
        "readiness_note": meta.get("readiness_note"),
        "formats": fmts, "languages": langs, "default_language": default_lang, "ask_language": True,
        "tier": meta.get("tier") or "full", "section": meta.get("section") or "main",
        "cta_devices": devices, "brandable": brandable_roles(tokens),
        "requires": requires, "missing": missing, "available": available,
        "preview": {"page": page.as_posix() if page.is_file() else None, "frames": [f.as_posix() for f in _frames(d, meta)],
                    "captions": list((meta.get("preview") or {}).get("captions") or [])},
        "path": d.as_posix(),
    }


def _template_dirs(base: Path) -> list[Path]:
    if not base.is_dir():
        return []
    return sorted(d for d in base.iterdir() if d.is_dir() and not d.name.startswith(("_", ".")) and
                  (d / "template.json").is_file())


def _tier_lock(rec: dict, access: dict) -> dict:
    """Mark a card locked when the buyer's licence tier doesn't include its template tier (licence.TEMPLATE_ACCESS)."""
    from .licence import unlock_plan
    rec["locked"] = rec["tier"] not in access["allowed"]
    rec["unlock_with"] = unlock_plan(rec["tier"]) if rec["locked"] else None
    return rec


def list_templates(include_hidden: bool = False, _locked_recs: bool = False) -> dict:
    from .licence import template_access
    base = paths.styles_dir()
    caps = capabilities()
    access = template_access()
    shown, hidden, locked, problems = [], [], [], []
    for d in _template_dirs(base):
        try:
            rec = _tier_lock(read_package(d, caps), access)
        except VeosError as e:
            problems.append({"id": d.name, "error": e.message})
            continue
        (locked if rec["available"] and rec["locked"] else shown if rec["available"] else hidden).append(rec)
    if include_hidden:
        shown += hidden
    shown.sort(key=lambda r: (r["order"], r["name"].lower()))
    locked.sort(key=lambda r: (r["order"], r["name"].lower()))
    idx = base / "index.html"
    return {"styles": base.as_posix(), "templates": shown, "count": len(shown),
            "hidden": [{"id": h["id"], "name": h["name"], "missing": h["missing"], "readiness": h["readiness"]} for h in hidden],
            "locked": locked if _locked_recs else [{"id": r["id"], "name": r["name"], "tier": r["tier"],
                                                    "unlock_with": r["unlock_with"]} for r in locked],
            "plan": access["tier_name"], "template_tiers": access["allowed"],
            "problems": problems, "gallery": idx.as_posix() if idx.is_file() else None,
            "capabilities": caps}


def find_template(tid: str, caps: dict | None = None) -> dict:
    d = paths.styles_dir() / tid
    if not (d / "template.json").is_file() or tid.startswith(("_", ".")):
        have = ", ".join(x.name for x in _template_dirs(paths.styles_dir())) or "(none yet)"
        raise VeosError("TEMPLATE_MISSING", f"template '{tid}' does not exist", f"Use one of: {have} (veos templates list).")
    return read_package(d, caps)


# ------------------------------------------------------------------ copy (brand it)
def template_hash(d: Path) -> str:
    h = hashlib.sha256()
    for name in ("playbook.md", "tokens.json"):
        f = d / name
        if f.is_file():
            h.update(f.read_bytes())
    return "sha256:" + h.hexdigest()


def _parse_colors(spec: str, brandable: list[dict]) -> dict[str, str]:
    out: dict[str, str] = {}
    names = [b["role"] for b in brandable]
    parts = [p.strip() for p in re.split(r"[,\s]+", spec.strip()) if p.strip()]
    pos = 0
    for p in parts:
        if "=" in p:
            r, v = p.split("=", 1)
            r = r.strip()
            if r not in names:
                raise VeosError("BAD_COLORS", f"'{r}' is not a brandable colour in this template",
                                f"Brandable roles: {', '.join(names) or '(none)'}.")
        else:
            if pos >= len(names):
                raise VeosError("BAD_COLORS", f"too many colours: this template brands {len(names)} ({', '.join(names)})",
                                "Pass one or two hex colours.")
            r, v = names[pos], p
            pos += 1
        hx = _norm_hex(v)
        if not hx:
            raise VeosError("BAD_COLORS", f"'{v}' is not a hex colour", "Use #RRGGBB, e.g. #7C5CFF.")
        out[r] = hx.upper()
    return out


def _parse_cta(spec: str, devices: list[str]) -> dict:
    """Any CTA device the engine knows (buyers can change anything); the style's own devices are only suggestions."""
    from .profilecheck import CTA_DEVICES
    dev, _, val = spec.partition(":")
    dev = dev.strip().lower().replace("-", "_").replace(" ", "_")
    dev = CTA_ALIASES.get(dev, dev)
    if dev not in CTA_DEVICES:
        raise VeosError("BAD_CTA", f"'{dev}' isn't a call to action the editor knows",
                        f"Choose one of: {', '.join(dict.fromkeys(list(devices) + list(CTA_DEVICES)))}.")
    val = val.strip() or None
    if dev in ("comment_keyword", "dm") and val:
        val = val.upper()
    return {"device": dev, "value": val}


def _resolve_text_on(roles: dict, colours: dict, v: dict) -> str | None:
    t = v.get("text_on")
    if not t:
        return None
    return colours.get(t) or _norm_hex(t)


def _contrast_pass(tokens: dict, branded: dict[str, str]) -> list[dict]:
    """Nudge the buyer's colours (OKLCH lightness) until text on them reads (tokens.resolve uses the same rule). Only
    roles the buyer branded, or whose text colour is a branded role, are touched."""
    roles = tokens.get("roles") or {}
    colours = {r: (v.get("default") if isinstance(v, dict) else None) for r, v in roles.items()}
    nudges = []
    for r, v in roles.items():
        if not isinstance(v, dict) or not v.get("brandable") or r in set(tokens.get("fixed_meaning") or []):
            continue
        if r not in branded and v.get("text_on") not in branded:  # the template's own colours are its author's call
            continue
        t = _resolve_text_on(roles, colours, v)
        if not t or not colours.get(r):
            continue
        need = 3.0 if v.get("large_text_only") else 4.5
        hx, changed, ok = fix_contrast(colours[r], t, need)
        if changed:
            nudges.append({"role": r, "from": colours[r], "to": hx.upper(), "contrast": round(contrast(hx, t), 2),
                           "need": need, "ok": ok, "asked": r in branded})
            v["default"] = hx.upper()
            colours[r] = hx.upper()
    return nudges


PLACEHOLDER = re.compile(r"\{\{\s*(BV-\d\d)\.([A-Za-z_]+)\s*(?:\|([^}]*))?\}\}")


def fill_placeholders(text: str, values: dict) -> str:
    def sub(m):
        v = (values.get(m.group(1)) or {}).get(m.group(2))
        return str(v) if v not in (None, "") else (m.group(3) or "").strip()
    return PLACEHOLDER.sub(sub, text)


def _apply_var(tokens: dict, path: str, value, applied: list, skipped: list) -> None:
    """A setup answer: applied whatever the template's lock says; only the never-bendable core (NC) is refused."""
    rec = lineage.classify(tokens, path, value)
    if rec["class"] != "NC":
        lineage.set_path(tokens, path, value)
        applied.append(path)
    else:
        skipped.append({"path": path, "class": "NC", "rule": rec.get("rule"), "message": lineage.refusal(rec)})


def resolve_language(language: str, offered: list[str]) -> str:
    """'english' / 'hinglish' / 'hindi' (or a speech/captions/script key) -> one of the template's language keys."""
    want = language.strip().replace(" ", "")
    key = LANG_ALIASES.get(want.lower()) or lang_key(re.split(r"[/>,]", want))
    match = next((k for k in offered if k.lower() == key.lower()), None)
    if not match:
        raise VeosError("LANGUAGE_NOT_SUPPORTED", f"'{language}' isn't a language this template offers",
                        f"Choose one of: {', '.join(LANG_OPTIONS.get(k, k) for k in offered)}.")
    return match


def numbers_for(speech: str, currency: str | None, base: dict | None = None) -> dict:
    """BV-06: numbers follow the language. English -> international ($, 1.2M) unless the buyer picks rupees; Hinglish
    and Hindi -> rupees in lakh / crore (unless the buyer picks another currency). A style that never compacts
    (`compact: none`, the numbers are the picture) keeps that."""
    cur = (currency or "").strip()
    if cur.upper() in ("₹", "INR", "RS", "RS.", "RUPEE", "RUPEES"):
        out = dict(NUMBERS_INDIAN)
    elif cur:
        out = {**NUMBERS_INTL, "currency": {"USD": "$", "EUR": "€", "GBP": "£"}.get(cur.upper(), cur)}
    else:
        out = dict(NUMBERS_INDIAN if speech in INDIAN else NUMBERS_INTL)
    if (base or {}).get("compact") == "none":
        out["compact"] = "none"
    return out


def _unique_id(name: str | None, handle: str | None, tid: str) -> str:
    base = slug(name or "") or slug((handle or "").lstrip("@")) or "my"
    base = f"{base}-{tid}"
    taken = set()
    for b in {paths.playbooks_dir(), paths.app_root() / "playbooks"}:
        if b.is_dir():
            taken |= {d.name.lower() for d in b.iterdir()}
    cand, i = base, 1
    while cand in taken:
        i += 1
        cand = f"{base}-{i}"
    return cand


def copy_template(tid: str, *, name: str | None = None, handle: str | None = None, colors: str | None = None,
                  language: str | None = None, cta: str | None = None, new_id: str | None = None,
                  currency: str | None = None) -> dict:
    caps = capabilities()
    info = find_template(tid, caps)
    from .licence import template_access
    if _tier_lock(info, template_access())["locked"]:
        raise VeosError("TEMPLATE_LOCKED", f"'{info['name']}' is part of the {info['unlock_with']} plan and up; "
                        "your plan doesn't include it",
                        f"Upgrade to {info['unlock_with']} to unlock it, or pick a style from `veos templates list`, "
                        "or build your own style (path B).")
    if not info["available"]:
        raise VeosError("TEMPLATE_UNAVAILABLE", f"template '{tid}' needs engine features this install doesn't have: "
                        f"{', '.join(info['missing']) or info['readiness']}",
                        "Run /vibe-editing-os:setup update, then pick it again; or pick another template.")
    src = Path(info["path"])
    tokens = read_json(src / "tokens.json")
    if schema_version(tokens) != 3 or tokens.get("kind") != "style_template":
        raise VeosError("BAD_TEMPLATE", f"template '{tid}' tokens are not a v3 style_template", "See TEMPLATE-PACKAGE.md.")
    errors: list[str] = []
    effective_style(tokens, warnings=[], errors=errors)
    if errors:
        raise VeosError("BAD_TEMPLATE", f"template '{tid}' tokens are invalid: " + "; ".join(errors), "See tokens.schema.md.")

    # inputs
    brandable = info["brandable"]
    branded = _parse_colors(colors, brandable) if colors else {}
    lang_key_ = resolve_language(language, info["languages"]) if language else None
    cta_rec = _parse_cta(cta, info["cta_devices"]) if cta else None

    pid = new_id or _unique_id(name, handle, tid)
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", pid):
        raise VeosError("BAD_ID", f"'{pid}' is not a valid playbook id", "Use lowercase letters, digits and dashes.")
    dest = paths.playbooks_dir() / pid
    if dest.exists() or paths.find_playbook_dir(pid):
        raise VeosError("PLAYBOOK_EXISTS", f"playbook '{pid}' already exists", "Never overwrite a playbook: pick another --id.")

    applied: list[str] = []
    skipped: list[dict] = []
    variables: dict = {}
    notes: list[str] = []
    # BV-01 name and handle
    if name or handle:
        variables["BV-01"] = {"name": name, "handle": handle}
        if name:
            _apply_var(tokens, "creator.name", name, applied, skipped)
        if handle:
            _apply_var(tokens, "creator.handle", handle if handle.startswith("@") else "@" + handle, applied, skipped)
            variables["BV-01"]["handle"] = tokens["creator"]["handle"]
    # BV-02 brand colours -> brandable roles, then the contrast nudge
    nudges: list[dict] = []
    if branded:
        for r, hx in branded.items():
            _apply_var(tokens, f"roles.{r}.default", hx, applied, skipped)
        policy = ((tokens.get("profile") or {}).get("themes") or {}).get("policy") or "single"
        packs = tokens.get("themes") or {}
        touched = [t for t, p in packs.items() if isinstance(p, dict) and set((p.get("roles") or {})) & set(branded)]
        if touched and policy in ("single", "per_reel"):
            for t in touched:
                for r in set(packs[t]["roles"]) & set(branded):
                    packs[t]["roles"][r] = branded[r]
        if policy == "per_reel" and len(packs) > 1:
            notes.append(ROTATION_NOTE)
        elif touched and policy != "single":
            notes.append(f"Each topic theme keeps its own {', '.join(sorted({r for t in touched for r in packs[t]['roles']} & set(branded)))} "
                         f"(that colour carries meaning in this style); your colour is the base everywhere else.")
    nudges = _contrast_pass(tokens, branded)
    if branded:
        variables["BV-02"] = {r: (tokens["roles"][r]["default"]) for r in branded}
        asked = {n["role"]: n for n in nudges if n["asked"]}
        if asked:
            variables["BV-02"]["asked"] = {r: branded[r] for r in asked}
        # theme packs follow the nudged colour too
        for t, p in (tokens.get("themes") or {}).items():
            for r in set((p or {}).get("roles") or {}) & set(asked):
                if p["roles"][r] == branded[r]:
                    p["roles"][r] = tokens["roles"][r]["default"]
    # BV-05 language (+ BV-06 numbers follow it)
    chosen = lang_key_ or info["default_language"]
    speech, cap, script = chosen.split("/")
    if lang_key_ and lang_key_ != info["default_language"]:
        lang = tokens["profile"].setdefault("language", {})
        transform = (lang.get("captions") or {}).get("transform") or "verbatim"
        if cap == "hinglish":
            transform = "transliterate"  # romanised Hinglish captions, whatever script the transcript comes in
        elif speech == cap:
            transform = "clean" if transform == "clean" else "verbatim"
        elif cap == "en" and speech != "en":
            transform = "translate"
        for path, v in (("profile.language.speech", speech), ("profile.language.captions.lang", cap),
                        ("profile.language.captions.script", script), ("profile.language.captions.transform", transform),
                        ("creator.language", speech), ("creator.caption_language", cap)):
            _apply_var(tokens, path, v, applied, skipped)
        variables["BV-05"] = {"speech": speech, "captions": cap, "script": script, "transform": transform}
    elif lang_key_:
        variables["BV-05"] = dict(zip(("speech", "captions", "script"), lang_key_.split("/")))
    have = (tokens.get("profile") or {}).get("numbers") or {}
    nums = numbers_for(speech, currency, have)
    if any(have.get(k) != v for k, v in nums.items()):
        for k, v in nums.items():
            _apply_var(tokens, f"profile.numbers.{k}", v, applied, skipped)
        variables["BV-06"] = nums
        notes.append(f"Numbers follow your language: {nums['grouping']} grouping, {nums['currency']}"
                     f"{' (lakh / crore)' if nums['compact'] == 'lakh_crore' else ''}.")
    # BV-08 call to action
    if cta_rec:
        dev, val = cta_rec["device"], cta_rec["value"]
        _apply_var(tokens, "profile.cta.chosen", dev, applied, skipped)
        devs = list(((tokens.get("profile") or {}).get("cta") or {}).get("devices") or [])
        if dev not in devs:
            _apply_var(tokens, "profile.cta.devices", devs + [dev], applied, skipped)
        cr = tokens.setdefault("creator", {})
        c = cr.get("cta") if isinstance(cr.get("cta"), dict) else {}
        c = {**c, "device": dev, "keyword": val if dev in ("comment_keyword", "dm") else None,
             "deliverable": val if dev not in ("comment_keyword", "dm", "none") else c.get("deliverable"),
             "pattern": (f"Comment {val}" if dev == "comment_keyword" and val else
                         f"DM me {val}" if dev == "dm" and val else
                         "Link in bio" if dev == "link_bio" else None if dev == "none" else CTA_WORDS.get(dev))}
        _apply_var(tokens, "creator.cta", c, applied, skipped)
        variables["BV-08"] = cta_rec
    for sk in skipped:
        notes.append(sk["message"])

    # the copy
    today = date.today().isoformat()
    tokens["kind"] = "style_copy"
    tokens["playbook"] = pid
    tokens["version"] = 1
    tokens["lineage"] = {
        "template": {"id": tid, "version": info["version"], "hash": template_hash(src)},
        "created": today, "variables": variables, "tuned": [], "deviations": [],
        "niche": {"topics": [], "updated": None}, "fidelity": "faithful", "upgrades": [],
    }
    shutil.copytree(src, dest, ignore=lambda d, names: [n for n in names if n == "__pycache__" or
                                                        (Path(d) == src and n in NOT_COPIED)])
    write_json(dest / "tokens.json", tokens, indent=2)
    pm = dest / "playbook.md"
    if pm.is_file():
        bv = {"BV-01": {"name": (tokens.get("creator") or {}).get("name"), "handle": (tokens.get("creator") or {}).get("handle")},
              "BV-02": {r: v.get("default") for r, v in (tokens.get("roles") or {}).items() if isinstance(v, dict)},
              "BV-05": variables.get("BV-05") or dict(zip(("speech", "captions", "script"), info["default_language"].split("/"))),
              "BV-08": {"device": (cta_rec or {}).get("device"), "keyword": (cta_rec or {}).get("value"),
                        "value": (cta_rec or {}).get("value")}}
        pm.write_text(fill_placeholders(pm.read_text(encoding="utf-8"), bv), encoding="utf-8", newline="\n")
        lineage.update_playbook_md(dest, tokens, [f"- {today} · created from template `{tid}` v{info['version']} "
                                                  f"(variables: {', '.join(sorted(variables)) or 'none'})"])
    (dest / "profile.md").write_text(_profile_md(info, tokens, variables, nudges, notes, lang_key_), encoding="utf-8",
                                     newline="\n")
    # the copy must load like any playbook
    w2: list[str] = []
    e2: list[str] = []
    effective_style(read_json(dest / "tokens.json"), warnings=w2, errors=e2)
    if e2:
        raise VeosError("BAD_COPY", "the branded copy does not load: " + "; ".join(e2), "Report this template to its author.")
    nudge_line = None
    asked = [n for n in nudges if n["asked"]]
    if asked:
        req = variables["BV-02"].get("asked", {})
        moved = "; ".join(f"your {n['role']} {req.get(n['role'], n['from'])} → {n['to']}" for n in asked)
        nudge_line = f"Adjusted {moved} so text on it stays readable (contrast {max(n['need'] for n in asked):g}:1)."
    return {"id": pid, "path": dest.as_posix(), "template": tid, "title": lineage.copy_title(tokens),
            "variables": variables, "applied": applied, "kept": skipped, "nudges": nudges, "nudge_line": nudge_line,
            "notes": notes, "faceless": info["faceless"],
            "next": f"veos workspace set --playbook {pid}"}


def _numbers_line(tokens: dict) -> str:
    n = (tokens.get("profile") or {}).get("numbers") or {}
    lc = " (lakh / crore)" if n.get("compact") == "lakh_crore" else ""
    return f"{n.get('currency') or '-'}, {n.get('grouping') or '-'} grouping{lc}"


def _profile_md(info: dict, tokens: dict, variables: dict, nudges: list, notes: list, lang: str | None) -> str:
    cr = tokens.get("creator") or {}
    insp = "Naman's own style" if info["own_style"] else "inspired by " + ", ".join(info["inspired_by"])
    b1 = variables.get("BV-01")
    b2 = variables.get("BV-02")
    b8 = variables.get("BV-08")
    a1 = f"{cr.get('name') or '-'} ({cr.get('handle') or 'no handle'})" if b1 else "template default (no name on screen)"
    a2 = (", ".join(f"{r} {v}" for r, v in b2.items() if r != "asked") +
          (f" (asked {', '.join(f'{r} {v}' for r, v in b2['asked'].items())}; nudged for contrast)" if b2.get("asked") else "")) \
        if b2 else "template default"
    a5 = lang_label(lang) if lang else f"template default ({lang_label(info['default_language'])})"
    a8 = (f"{CTA_WORDS.get(b8['device'], b8['device'])}" + (f": {b8['value']}" if b8.get("value") else "")) if b8 else "template default"
    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    lines = [
        f"# Profile: {lineage.copy_title(tokens)}", "",
        f"Made with path A (pick a template) on {date.today().isoformat()}. No interview, no inspiration videos:"
        " the template is the style, these answers brand it.", "",
        f"confirmed_at: {now}", "",
        "## Template", "",
        f"- **{info['name']}** (`{info['id']}` v{info['version']}), {insp}.",
        f"- Needs: {info['needs']}." + (" Faceless: no face on camera." if info["faceless"] else ""),
        f"- Formats: {', '.join((f['id'] + ' ' + (f['name'] or '')).strip() for f in info['formats']) or 'one'}.", "",
        "## Branding answers (structure D.3)", "",
        "| BV | Question | Answer |", "|---|---|---|",
        f"| BV-01 | Name and handle | {a1} |",
        f"| BV-02 | Brand colours | {a2} |",
        f"| BV-05 | Spoken and caption language | {a5} |",
        f"| BV-06 | Numbers | {_numbers_line(tokens)} |",
        f"| BV-08 | Call to action | {a8} |", "",
        "## Everything else", "",
        "Template defaults (structure D.3): fonts, formats, theme packs, humour level, series, sponsor wording, duration."
        " Change any of them later with \"change my playbook\". Niche slots (hook pairs, the line → pattern lookup,"
        " worked examples, the headline bank) adapt per reel from your transcript (D.6).",
    ]
    if notes or nudges:
        lines += ["", "## Notes", ""] + [f"- {n}" for n in notes]
        lines += [f"- Contrast: {n['role']} {n['from']} → {n['to']} ({n['contrast']}:1)." for n in nudges]
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------ gallery page
def _rel(target: Path, out_dir: Path) -> str:
    try:
        return Path(os.path.relpath(target, out_dir)).as_posix()
    except ValueError:  # another drive (Windows)
        return target.resolve().as_uri()


def _placeholder_frame(tokens: dict) -> str:
    roles = tokens.get("roles") or {}
    col = lambda r, d: ((roles.get(r) or {}).get("default") if isinstance(roles.get(r), dict) else None) or d  # noqa: E731
    worlds = tokens.get("worlds") or {}
    w = next(iter(worlds.values()), {}) if worlds else {}
    themes = tokens.get("themes") or {}
    tdef = ((tokens.get("profile") or {}).get("themes") or {}).get("default")
    tw = next(iter(((themes.get(tdef) or {}).get("worlds") or {}).values()), {}) if tdef else {}
    top = tw.get("top") or w.get("top") or w.get("bg") or col("night", "#14161A")
    bot = tw.get("bottom") or w.get("bottom") or top
    accent = col("accent", col("primary", "#FFD400"))
    return (f'<div class="ph" style="background:linear-gradient(180deg,{html.escape(top)},{html.escape(bot)})">'
            f'<span class="ph-bar" style="background:{html.escape(accent)}"></span>'
            f'<span class="ph-cap">your words appear here</span></div>')


GALLERY_CSS = """
:root{--bg:#EDEAE3;--ink:#1E2622;--muted:#55605A;--card:#FFFFFF;--line:#DDD6CA;--pill:#B7D3B0;--pill2:#F5D77E;--face:#8DB3D4;
  --draft:#F2896B;--e-in:cubic-bezier(.16,1,.3,1);--sh:0 10px 30px rgba(30,38,34,.16)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#16211C;--ink:#F3F1EC;--muted:#B5BDB8;--card:#1F2B25;
  --line:#2F3D36;--sh:0 10px 30px rgba(0,0,0,.45)}}
:root[data-theme="dark"]{--bg:#16211C;--ink:#F3F1EC;--muted:#B5BDB8;--card:#1F2B25;--line:#2F3D36;--sh:0 10px 30px rgba(0,0,0,.45)}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font-family:"Plus Jakarta Sans",system-ui,sans-serif;padding:40px 16px 80px}
header{max-width:1180px;margin:0 auto 30px}
header h1{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400;font-size:clamp(34px,6vw,48px);letter-spacing:-.01em}
header p{font-size:15px;line-height:1.55;max-width:760px;margin-top:8px;color:var(--muted)}
header .how{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.tag{display:inline-block;background:var(--pill);color:#1E2622;border-radius:99px;padding:3px 12px;font-family:Jost,sans-serif;font-weight:600;font-size:13px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,270px),300px));justify-content:center;gap:28px;max-width:1180px;margin:0 auto}
.card{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:14px 14px 18px;box-shadow:var(--sh);display:flex;flex-direction:column}
.frames{position:relative;width:100%;aspect-ratio:9/16;border-radius:16px;overflow:hidden;background:#111;isolation:isolate}
.frames img,.frames .ph{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0}
.frames.n1 img,.frames.n1 .ph{opacity:1;animation:drift 7s ease-in-out infinite alternate}
.frames.n2 img{animation:show2 5.2s var(--e-in) infinite;animation-delay:calc(var(--i)*2.6s)}
.frames.n3 img{animation:show3 7.8s var(--e-in) infinite;animation-delay:calc(var(--i)*2.6s)}
@keyframes show2{0%{opacity:0;transform:scale(1.04)}5%{opacity:1}50%{opacity:1;transform:scale(1)}55%,100%{opacity:0;transform:scale(1)}}
@keyframes show3{0%{opacity:0;transform:scale(1.04)}4%{opacity:1}33%{opacity:1;transform:scale(1)}37%,100%{opacity:0;transform:scale(1)}}
@keyframes drift{from{transform:scale(1)}to{transform:scale(1.05)}}
.dots{position:absolute;left:0;right:0;bottom:10px;display:flex;justify-content:center;gap:6px;z-index:3}
.dots i{width:6px;height:6px;border-radius:50%;background:rgba(255,255,255,.45)}
.n2 .dots i{animation:dot2 5.2s linear infinite;animation-delay:calc(var(--i)*2.6s)}
.n3 .dots i{animation:dot3 7.8s linear infinite;animation-delay:calc(var(--i)*2.6s)}
@keyframes dot2{0%,49%{background:#fff}50%,100%{background:rgba(255,255,255,.45)}}
@keyframes dot3{0%,33%{background:#fff}34%,100%{background:rgba(255,255,255,.45)}}
.ph{display:flex;align-items:flex-end;justify-content:center;padding-bottom:30%}
.ph-bar{position:absolute;left:12%;right:12%;top:14%;height:9%;border-radius:12px;opacity:.9}
.ph-cap{font-weight:800;font-size:15px;color:#fff;text-shadow:0 2px 6px rgba(0,0,0,.6)}
.pills{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 8px}
.pill{font-family:Jost,sans-serif;font-weight:600;font-size:12px;border-radius:99px;padding:2px 10px;background:var(--pill);color:#1E2622}
.pill.r4{background:var(--pill2)}.pill.face{background:var(--face)}.pill.draft{background:var(--draft);color:#fff}
.card h2{font-family:"Instrument Serif",Georgia,serif;font-weight:400;font-size:30px;line-height:1.05}
.insp{font-size:13px;color:var(--muted);margin-top:3px;font-style:italic}
.tagline{font-size:14px;line-height:1.45;margin-top:10px}
.needs{font-size:14px;line-height:1.45;margin-top:10px;padding:8px 12px;border-radius:12px;background:rgba(183,211,176,.28)}
.needs b{font-family:Jost,sans-serif;font-weight:600}
.meta{font-size:12.5px;line-height:1.5;color:var(--muted);margin-top:10px}
.pick{margin-top:auto;padding-top:14px;font-size:13px;line-height:1.5}
.pick code{font-family:"JetBrains Mono",monospace;font-size:12px;background:rgba(127,127,127,.14);border-radius:6px;padding:1px 6px}
.pick a{color:inherit;font-weight:600}
.empty{max-width:640px;margin:40px auto;text-align:center;color:var(--muted);font-size:15px;line-height:1.6}
footer{max-width:1180px;margin:36px auto 0;font-size:12px;color:var(--muted)}
.brands{max-width:1180px;margin:56px auto 0;border-top:1px solid var(--line);padding-top:28px}
.sec{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400;font-size:clamp(28px,5vw,38px);margin-bottom:6px}
.sec-note{font-size:14px;color:var(--muted);margin-bottom:22px}
@media (prefers-reduced-motion:reduce){.frames img,.frames .ph,.dots i{animation:none!important}.frames img:first-child,.frames .ph:first-child{opacity:1}}
"""


def _fonts_css(out_dir: Path) -> str:
    fd = paths.app_root() / "assets" / "fonts"
    faces = [("Plus Jakarta Sans", "PlusJakartaSans-VF.ttf", "font-weight:200 800"), ("Jost", "Jost-VF.ttf", "font-weight:100 900"),
             ("Instrument Serif", "InstrumentSerif-Regular.ttf", ""),
             ("Instrument Serif", "InstrumentSerif-Italic.ttf", "font-style:italic"),
             ("JetBrains Mono", "JetBrainsMono-VF.ttf", "font-weight:100 800")]
    return "".join(f'@font-face{{font-family:"{n}";src:url("{_rel(fd / f, out_dir)}");{extra}}}\n'
                   for n, f, extra in faces if (fd / f).exists())


def _card(rec: dict, out_dir: Path) -> str:
    e = html.escape
    frames = [Path(f) for f in rec["preview"]["frames"]][:3]
    n = max(1, len(frames))
    if frames:
        alts = rec["preview"]["captions"] + [""] * 3
        inner = "".join(f'<img style="--i:{i}" src="{e(_rel(f, out_dir))}" alt="{e(alts[i] or rec["name"])}">'
                        for i, f in enumerate(frames))
    else:
        try:
            inner = _placeholder_frame(read_json(Path(rec["path"]) / "tokens.json"))
        except (OSError, ValueError):
            inner = '<div class="ph"><span class="ph-cap">preview coming</span></div>'
    dots = "".join(f'<i style="--i:{i}"></i>' for i in range(n)) if n > 1 else ""
    pills = [f'<span class="pill {"r4" if rec["readiness"] == "R4" else ""}">{e(rec["readiness_label"])}</span>']
    if rec["faceless"]:
        pills.append('<span class="pill face">Faceless · no face on camera</span>')
    elif rec["faceless_formats"]:
        pills.append(f'<span class="pill face">Faceless option ({e(", ".join(rec["faceless_formats"]))})</span>')
    if rec["status"] != "released":
        pills.append(f'<span class="pill draft">{e(rec["status"])}</span>')
    if rec.get("locked"):
        pills.insert(0, f'<span class="pill lock">Upgrade to {e(rec["unlock_with"])} to unlock</span>')
    insp = "Naman's own style" if rec["own_style"] else "inspired by " + ", ".join(rec["inspired_by"])
    needs = e(rec["needs"])
    if rec["needs_by_format"]:
        needs += "".join(f'<br><small>{e(k)}: {e(v)}</small>' for k, v in rec["needs_by_format"].items())
    meta = []
    if rec["formats"]:
        meta.append(f"{len(rec['formats'])} format{'s' if len(rec['formats']) > 1 else ''}: " +
                    " · ".join(e(f["name"] or f["id"]) for f in rec["formats"]))
    meta.append(e(lang_label(rec["default_language"])) + (f" · {len(rec['languages']) - 1} more language options"
                                                           if rec["ask_language"] else ""))
    if rec["readiness_note"]:
        meta.append(e(rec["readiness_note"]))
    page = rec["preview"]["page"]
    full = f' · <a href="{e(_rel(Path(page), out_dir))}" target="_blank">Full preview →</a>' if page else ""
    pick = (f'<p class="pick">Not in your plan: upgrade to {e(rec["unlock_with"])} to unlock this style{full}</p>'
            if rec.get("locked") else f'<p class="pick">To use it, tell Claude <code>{e(rec["name"])}</code>{full}</p>')
    return (f'<article class="card{" locked" if rec.get("locked") else ""}" id="{e(rec["id"])}"><div class="frames n{n}">{inner}'
            f'<div class="dots">{dots}</div></div>'
            f'<div class="pills">{"".join(pills)}</div><h2>{e(rec["name"])}</h2><p class="insp">{e(insp)}</p>'
            + (f'<p class="tagline">{e(rec["tagline"])}</p>' if rec["tagline"] else "")
            + f'<p class="needs"><b>needs:</b> {needs}</p><p class="meta">{"<br>".join(meta)}</p>{pick}</article>')


def gallery(out: str | None = None, faceless_first: bool = False) -> dict:
    data = list_templates(_locked_recs=True)
    recs = data["templates"]
    locked = data["locked"]
    if faceless_first:
        recs = sorted(recs, key=lambda r: (not (r["faceless"] or r["faceless_formats"]), r["order"], r["name"].lower()))
    dest = Path(out) if out else paths.styles_dir() / "index.html"
    if dest.suffix.lower() != ".html":
        dest = dest / "index.html"
    out_dir = dest.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    main = [r for r in recs if r.get("section") != "brands"]
    brands = [r for r in recs if r.get("section") == "brands"]
    cards = "\n".join(_card(r, out_dir) for r in main)
    extra = ""
    if brands:
        extra = ('<section class="brands"><h2 class="sec">For brands &amp; agencies</h2>'
                 '<p class="sec-note">Made for product and brand ads rather than a creator\'s own channel.</p>'
                 f'<div class="grid">{"".join(_card(r, out_dir) for r in brands)}</div></section>')
    if locked:  # tier-locked styles stay visible, marked "upgrade to unlock" (licence.TEMPLATE_ACCESS)
        extra += ('<section class="brands locked-sec"><h2 class="sec">Unlock with an upgrade</h2>'
                  f'<p class="sec-note">Your {html.escape(data["plan"] or "current")} plan doesn\'t include these styles. '
                  'Upgrade your plan to use them.</p>'
                  f'<div class="grid">{"".join(_card(r, out_dir) for r in locked)}</div></section>')
    body = (f'<main class="grid">{cards}</main>{extra}' if recs else
            '<p class="empty">Your plan includes building your own editing style: run /vibe-editing-os:playbook. '
            'Ready-made styles come with an upgrade (below).</p>' + extra if locked else
            '<p class="empty">No editing styles are installed yet. They arrive with an app update '
            '(/vibe-editing-os:setup update). Until then, build your own style with /vibe-editing-os:playbook.</p>')
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pick a Style</title>
<style>
{_fonts_css(out_dir)}{GALLERY_CSS}{LOCK_CSS}</style>
</head>
<body>
<header>
<h1>Pick an editing style</h1>
<p>Each style is a complete, ready-to-use editing playbook. Pick the one you like for this folder. Claude then asks
four quick branding questions (name, colours, language, call to action) and you can edit your first reel right away.
You can change anything in your copy any time.</p>
<div class="how"><span class="tag">{len(recs)} style{'s' if len(recs) != 1 else ''}</span><span class="tag">"needs" = what you shoot</span>
<span class="tag">Faceless styles work from a voice-over</span></div>
</header>
{body}
<footer>Vibe Editing OS · generated {date.today().isoformat()} by veos templates gallery. Styles are inspired by creators'
editing; they're not affiliated with or endorsed by them.</footer>
</body>
</html>
"""
    dest.write_text(page, encoding="utf-8", newline="\n")
    return {"out": dest.as_posix(), "cards": len(recs), "ids": [r["id"] for r in main + brands],
            "brands": [r["id"] for r in brands], "hidden": data["hidden"],
            "locked": [{"id": r["id"], "name": r["name"], "unlock_with": r["unlock_with"]} for r in locked],
            "plan": data["plan"]}


LOCK_CSS = """
.card.locked{opacity:.62;filter:grayscale(.85)}
.card.locked:hover{opacity:.85}
.pill.lock{background:#2a2a2a;color:#fff}
"""


# ------------------------------------------------------------------ check (template authors)
REQUIRED_FILES = ("template.json", "tokens.json", "playbook.md", "preview/index.html")


def check_package(d: Path) -> dict:
    problems, warnings = [], []
    for f in REQUIRED_FILES:
        if not (d / f).is_file():
            problems.append(f"missing {f}")
    if problems:
        return {"id": d.name, "ok": False, "problems": problems, "warnings": warnings}
    try:
        meta, tokens = read_json(d / "template.json"), read_json(d / "tokens.json")
    except ValueError as e:
        return {"id": d.name, "ok": False, "problems": [f"invalid JSON: {e}"], "warnings": []}
    style = tokens.get("style") or {}
    if meta.get("package") != PACKAGE:
        problems.append(f'template.json "package" must be "{PACKAGE}"')
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", d.name):
        problems.append("the folder name must be a kebab-case id (no leading underscore)")
    for k, v in (("template.json id", meta.get("id")), ("tokens.playbook", tokens.get("playbook")), ("tokens.style.id", style.get("id"))):
        if v != d.name:
            problems.append(f"{k} is {v!r}; it must equal the folder name '{d.name}'")
    if tokens.get("schema") != SCHEMA_V3:
        problems.append(f'tokens.schema must be "{SCHEMA_V3}"')
    if tokens.get("kind") != "style_template":
        problems.append('tokens.kind must be "style_template"')
    if style.get("status") not in STATUSES:
        problems.append(f"tokens.style.status must be one of {', '.join(STATUSES)}")
    if not style.get("name"):
        problems.append("tokens.style.name is missing")
    if "inspired_by" not in style:
        problems.append("tokens.style.inspired_by is missing ([] for a creator's own style)")
    if meta.get("readiness") not in ("R1", "R2", "R4"):
        problems.append("template.json readiness must be R1, R2 or R4 (R3 styles are not packaged)")
    for c in meta.get("requires") or []:
        if c not in CAPABILITIES:
            problems.append(f"requires '{c}' is not a known engine capability ({', '.join(CAPABILITIES)})")
    if not tokens.get("locks"):
        problems.append("tokens.locks is empty: path A needs the lock map to brand and tweak copies")
    errs: list[str] = []
    warns: list[str] = []
    try:
        eff = effective_style(tokens, warnings=warns, errors=errs)
        from .profilecheck import violations
        warnings += [f"V-PROFILE {v['id']}: {v['msg']}" for v in violations(eff)]
    except Exception as e:  # noqa: BLE001
        errs.append(f"tokens do not resolve: {e}")
    problems += errs
    warnings += warns
    frames = _frames(d, meta)
    if len(frames) < 3:
        problems.append(f"preview needs 3 card frames (found {len(frames)}): preview/frames/01..03 (TEMPLATE-PACKAGE §3)")
    for f in frames:
        try:
            from PIL import Image
            with Image.open(f) as im:
                w, h = im.size
            if abs(w / h - 9 / 16) > 0.02:
                problems.append(f"{f.name} is {w}x{h}; card frames are 9:16")
        except Exception:  # noqa: BLE001
            warnings.append(f"could not read {f.name}")
    text = (d / "playbook.md").read_text(encoding="utf-8")
    first = next((ln for ln in text.splitlines() if ln.startswith("# ")), "")
    if not re.fullmatch(r"# .+ Style Playbook \(template v\d+\)", first.strip()):
        warnings.append("the title should read '# <Style name> Style Playbook (template v<N>)'")
    bad = [m.group(0) for m in re.finditer(r"\{\{[^}]*\}\}", text) if not PLACEHOLDER.fullmatch(m.group(0))]
    if bad:
        problems.append(f"malformed placeholders: {', '.join(sorted(set(bad))[:5])}")
    if not brandable_roles(tokens):
        warnings.append("no brandable role: the colour question (BV-02) will be skipped")
    if meta.get("tier") is not None and meta.get("tier") not in TIERS:
        problems.append(f"template.json tier must be one of {', '.join(TIERS)}")
    if meta.get("section") is not None and meta.get("section") not in SECTIONS:
        problems.append(f"template.json section must be one of {', '.join(SECTIONS)}")
    if style.get("status") == "released" and not (d / "evidence.md").is_file():
        warnings.append("released templates ship evidence.md (App. B)")
    return {"id": d.name, "ok": not problems, "problems": problems, "warnings": warnings}


def main(args, project) -> dict:
    a = args.action
    if a == "list":
        return list_templates(include_hidden=args.all)
    if a == "gallery":
        return gallery(args.out, args.faceless_first)
    if a == "check":
        base = paths.styles_dir()
        dirs = [base / t for t in args.template] if args.template else _template_dirs(base)
        res = [check_package(d) for d in dirs]
        return {"styles": base.as_posix(), "results": res, "all_ok": all(r["ok"] for r in res)}
    if len(args.template) != 1:
        raise VeosError("MISSING_ARGS", "templates copy needs exactly one template id",
                        "Example: veos templates copy ledger-explainer --name Riya --handle @riya.money")
    return copy_template(args.template[0], name=args.name, handle=args.handle, colors=args.colors, language=args.language,
                         cta=args.cta, new_id=args.new_id, currency=args.currency)
