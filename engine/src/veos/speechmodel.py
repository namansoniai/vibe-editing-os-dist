"""Which speech model `veos transcribe` uses, and the one-time download of the larger one (engine/SPEC.md section 5).

The installer downloads large-v3-turbo (~1.6 GB). Indian regional languages transcribe much better with the full
large-v3 (~3 GB), so it is chosen automatically for them and downloaded once, on the first reel that needs it, into the
same Hugging Face cache the installer fills (HF_HOME = VEOS_HOME/models/hf). If the download or the load fails (offline,
disk full, low memory) the reel goes on with large-v3-turbo and a warning: a missing model never stops a reel.

Choice (first that applies): `--model`, `VEOS_WHISPER_MODEL`, the playbook's `profile.language.model`, large-v3 when the
speech language is one of BIG_LANGS, else large-v3-turbo.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

TURBO = "large-v3-turbo"
LARGE = "large-v3"
# the faster-whisper (CTranslate2) repos faster_whisper.utils maps these names to; the installer fetches TURBO's
REPOS = {TURBO: "mobiuslabsgmbh/faster-whisper-large-v3-turbo", LARGE: "Systran/faster-whisper-large-v3"}
SIZE = {TURBO: "~1.6 GB", LARGE: "~3 GB"}
FILES = ["config.json", "preprocessor_config.json", "model.bin", "tokenizer.json", "vocabulary.*"]
# languages that turbo hears noticeably worse than large-v3
BIG_LANGS = {"te": "Telugu", "ta": "Tamil", "kn": "Kannada", "ml": "Malayalam", "bn": "Bengali", "gu": "Gujarati",
             "pa": "Punjabi", "mr": "Marathi"}


def choose(language: str | None, explicit: str | None = None, playbook: str | None = None) -> tuple[str, str]:
    """(model name, why) for a speech language."""
    if explicit:
        return explicit, "--model"
    env = os.environ.get("VEOS_WHISPER_MODEL")
    if env:
        return env, "VEOS_WHISPER_MODEL"
    if playbook:
        return playbook, "playbook profile.language.model"
    if language in BIG_LANGS:
        return LARGE, f"{BIG_LANGS[language]} speech (large-v3 hears it better)"
    return TURBO, "default"


def hf_home() -> Path:
    """The Hugging Face cache the installer fills (the `veos` wrapper and core.tools set HF_HOME to it)."""
    from .core import veos_home
    os.environ.setdefault("HF_HOME", str(veos_home() / "models" / "hf"))
    return Path(os.environ["HF_HOME"])


def is_present(name: str) -> bool:
    """True when the model's weights are in the local cache (a known repo), or for names we can't map (a local path or
    another model faster-whisper resolves itself)."""
    repo = REPOS.get(name)
    if not repo:
        return True
    d = hf_home() / "hub" / ("models--" + repo.replace("/", "--"))
    return any(d.glob("snapshots/*/model.bin"))


def _download(repo: str) -> None:
    from huggingface_hub import snapshot_download
    try:
        from huggingface_hub.utils import disable_progress_bars
        disable_progress_bars()   # one clear line instead of a 3 GB progress bar in the agent's output
    except Exception:  # noqa: BLE001
        pass
    snapshot_download(repo, allow_patterns=FILES)


def say(msg: str) -> None:
    print(f"veos: {msg}", file=sys.stderr, flush=True)


def ensure(name: str, language: str | None = None, warnings: list | None = None) -> str:
    """The model to load: `name` once it is present (large-v3 is downloaded here the first time), else turbo with a
    warning. Never raises."""
    warnings = warnings if warnings is not None else []
    if name != LARGE or is_present(name):
        return name
    who = BIG_LANGS.get(language or "", "this language")
    say(f"Downloading the larger speech model for {who} ({SIZE[LARGE]}, once)...")
    try:
        _download(REPOS[LARGE])
    except Exception as e:  # noqa: BLE001 - offline, disk full, interrupted: the reel goes on with turbo
        warnings.append(f"could not download the larger speech model {LARGE} ({type(e).__name__}: {e}); transcribed "
                        f"with {TURBO}. It downloads by itself on the next {who} reel once the internet is back.")
        say(f"warning: {warnings[-1]}")
        return TURBO
    if not is_present(name):
        warnings.append(f"the {LARGE} download finished but its files are incomplete; transcribed with {TURBO}")
        say(f"warning: {warnings[-1]}")
        return TURBO
    say(f"Speech model {LARGE} ready.")
    return name
