"""Languages and per-playbook cut settings the prep and cut steps read.

* `whisper_code("telugu-english")` -> "te": a playbook's speech language (a name, a code-mix or a code) -> the speech
  model's language code. A code-mix maps to its regional language (Hinglish -> hi, Tanglish -> ta), because that is
  what the model hears; English stays "en".
* `speech_language(project)` -> (code, why): playbook `profile.language.speech`, else `creator.language`.
* `cut_settings(project)` -> the playbook's `cut` block: `speed` (1.0-1.5, the creator's choice) and `pause_s` (the
  pause a tightened cut keeps, default 0.12 s).
* `script_of(word)` -> the writing system of a word (devanagari, telugu, tamil, ... latin, other).

The playbook is read from work/tokens.json (made by `veos tokens`), else from the playbook named in project.json. A
missing or broken playbook never blocks: the callers fall back to their defaults.
"""
from __future__ import annotations

import re

from .core import read_json

NAMES = {
    "english": "en", "hinglish": "hi", "hindi": "hi", "telugu": "te", "tenglish": "te", "tamil": "ta", "tanglish": "ta",
    "kannada": "kn", "kanglish": "kn", "malayalam": "ml", "manglish": "ml", "marathi": "mr", "bengali": "bn",
    "bangla": "bn", "banglish": "bn", "gujarati": "gu", "punjabi": "pa", "panjabi": "pa", "urdu": "ur",
    "assamese": "as", "nepali": "ne", "sinhala": "si", "sindhi": "sd", "sanskrit": "sa",
}
# languages the speech model knows (Whisper); Odia is not one of them
WHISPER = set("en hi te ta kn ml mr bn gu pa ur as ne si sd sa zh de es ru ko fr ja pt tr pl ca nl ar sv it id vi he uk "
              "el ms cs ro da hu no th fa fi sk hr bg lt la mi cy lv sl az gl mk br et ka is hy eu so af oc be tg mn "
              "sw yi sr kk sq lb bs".split())
SCRIPTS = (("devanagari", "ऀ-ॿ"), ("bengali", "ঀ-৿"), ("gurmukhi", "਀-੿"),
           ("gujarati", "઀-૿"), ("odia", "଀-୿"), ("tamil", "஀-௿"),
           ("telugu", "ఀ-౿"), ("kannada", "ಀ-೿"), ("malayalam", "ഀ-ൿ"),
           ("arabic", "؀-ۿ"))
_SCRIPT_RE = [(name, re.compile(f"[{rng}]")) for name, rng in SCRIPTS]
SPEED_RANGE = (1.0, 1.5)
DEFAULT_PAUSE = 0.12


def whisper_code(value) -> str | None:
    """'telugu-english' -> 'te', 'Hinglish' -> 'hi', 'en-IN' -> 'en', 'te' -> 'te'; None when unknown."""
    if not isinstance(value, str) or not value.strip():
        return None
    s = value.strip().lower().replace("_", "-")
    if s in NAMES:
        return NAMES[s]
    m = re.fullmatch(r"([a-z]{2})(-[a-z]{2,4})?", s)
    if m and m.group(1) in WHISPER:
        return m.group(1)
    codes = [whisper_code(t) for t in re.split(r"[\s\-+/&,()]+|\band\b|\bmix\b|\bmixed\b", s) if t and t != s]
    codes = [c for c in codes if c]
    regional = [c for c in codes if c != "en"]
    return regional[0] if regional else (codes[0] if codes else None)


def script_of(word: str) -> str:
    for name, rx in _SCRIPT_RE:
        if rx.search(word):
            return name
    return "latin" if re.search(r"[A-Za-z]", word) or not re.search(r"[^\W\d_]", word) else "other"


def playbook_tokens(proj) -> dict:
    """work/tokens.json, else the tokens of the playbook named in project.json; {} when neither can be read."""
    if proj is None:
        return {}
    tp = proj.work / "tokens.json"
    if tp.exists():
        try:
            return read_json(tp)
        except ValueError:
            pass
    try:
        pj = proj.root / "project.json"
        pid = read_json(pj).get("playbook") if pj.exists() else None
        if pid:
            from .tokens import load_playbook
            return load_playbook(str(pid))
    except Exception:  # noqa: BLE001 - a missing playbook never blocks prep or the cut
        pass
    return {}


def _get(d, path: str):
    for k in path.split("."):
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


def speech_language(proj, tokens: dict | None = None) -> tuple[str | None, str]:
    """(whisper code, where it came from) from the playbook, or (None, why not)."""
    tok = playbook_tokens(proj) if tokens is None else tokens
    for path in ("profile.language.speech", "creator.language"):
        v = _get(tok, path)
        code = whisper_code(v) if isinstance(v, str) else None
        if code:
            return code, f"playbook {path} = {v!r}"
    return None, "no speech language in the playbook"


def speech_model(proj, tokens: dict | None = None) -> str | None:
    """The playbook's speech model (`profile.language.model`, e.g. "large-v3" for a regional language), if set."""
    tok = playbook_tokens(proj) if tokens is None else tokens
    v = _get(tok, "profile.language.model")
    return v.strip() if isinstance(v, str) and v.strip() else None


def cut_settings(proj, tokens: dict | None = None) -> dict:
    """The playbook's `cut` block, checked: {"speed": float | None, "pause_s": float, "warnings": [...]}."""
    tok = playbook_tokens(proj) if tokens is None else tokens
    c = tok.get("cut") if isinstance(tok.get("cut"), dict) else {}
    out: dict = {"speed": None, "pause_s": DEFAULT_PAUSE, "warnings": []}
    sp = c.get("speed")
    if sp is not None:
        try:
            sp = float(sp)
        except (TypeError, ValueError):
            sp = None
        if sp is None or not SPEED_RANGE[0] <= sp <= SPEED_RANGE[1]:
            out["warnings"].append(f"playbook cut.speed {c.get('speed')!r} ignored (allowed {SPEED_RANGE[0]}-{SPEED_RANGE[1]})")
        else:
            out["speed"] = sp
    ps = c.get("pause_s")
    if isinstance(ps, (int, float)) and 0.0 <= ps <= 1.0:
        out["pause_s"] = float(ps)
    return out
