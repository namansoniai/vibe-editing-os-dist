"""`veos paths`: where the repo assets live. Skills never hard-code paths; they ask this.

Two layouts:
  dev       running from the git repo: playbooks live in <repo>/playbooks.
  installed running from VEOS_HOME/app (made by plugin/setup/install.*): USER playbooks live in VEOS_HOME/playbooks
            (never overwritten by app updates); the shipped reference playbook + template stay read-only in app/.
"""
from __future__ import annotations

import os
from pathlib import Path

from .core import veos_home


def app_root() -> Path:
    """Root that holds playbooks/, renderer/, assets/. Dev: the repo. Installed: veos_home() / "app"."""
    return Path(__file__).resolve().parents[3]


def is_installed() -> bool:
    try:
        return app_root().resolve() == (veos_home() / "app").resolve()
    except OSError:
        return False


def playbooks_dir() -> Path:
    """Where USER playbooks live (env VEOS_PLAYBOOKS overrides; used by tests)."""
    env = os.environ.get("VEOS_PLAYBOOKS")
    if env:
        return Path(env)
    return veos_home() / "playbooks" if is_installed() else app_root() / "playbooks"


def playbook_template() -> Path:
    return app_root() / "playbooks" / "_template"


def reference_playbook() -> Path:
    """The read-only quality reference for the playbook builder: `_reference` in the distribution, else Naman's (dev repo)."""
    for name in ("_reference", "naman"):
        p = app_root() / "playbooks" / name / "playbook.md"
        if p.exists():
            return p
    return app_root() / "playbooks" / "_reference" / "playbook.md"


def find_playbook_dir(playbook_id: str) -> Path | None:
    """User dir first, then the shipped app/playbooks (so the reference `naman` always resolves)."""
    for base in (playbooks_dir(), app_root() / "playbooks"):
        if (base / playbook_id / "tokens.json").exists():
            return base / playbook_id
    return None


def sfx_pack() -> Path:
    """Local cache of downloaded sound files: VEOS_HOME/sfx/<relpath> (filled by `veos sfx fetch`). Env VEOS_SFX overrides it
    (a full pack folder, with its catalog.json; used by tests and by the pack owner)."""
    env = os.environ.get("VEOS_SFX")
    return Path(env) if env else veos_home() / "sfx"


def sfx_catalog() -> Path:
    """The small catalogue that ships with the app: <app_root>/assets/sfx/catalog.json (no audio ships with the app)."""
    env = os.environ.get("VEOS_SFX")
    return Path(env) / "catalog.json" if env else app_root() / "assets" / "sfx" / "catalog.json"


def add_args(p, cmd):
    pass


def resolve() -> dict:
    root = app_root()
    return {"repo_root": root.as_posix(), "installed": is_installed(), "playbooks": playbooks_dir().as_posix(),
            "playbook_template": playbook_template().as_posix(),
            "reference_playbook": reference_playbook().as_posix(),
            "renderer_player": (root / "renderer" / "player.html").as_posix(),
            "renderer_core": (root / "renderer" / "core.js").as_posix(), "veos_home": veos_home().as_posix(),
            "sfx_pack": sfx_pack().as_posix(), "sfx_catalog": sfx_catalog().as_posix(),
            "sfx_catalog_exists": sfx_catalog().exists()}


def main(args, project) -> dict:
    return resolve()
