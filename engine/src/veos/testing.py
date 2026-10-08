"""Test helpers: short fixture clips cut from the local test footage (never committed)."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path

from .core import run, tools, veos_home

FOOTAGE = Path(os.environ.get("VEOS_FOOTAGE", r"C:\namansoni.ai\vibe-editing-os-footage"))
RAW = {"reel7": FOOTAGE / "Reel 7" / "reel 7.mp4", "reel9": FOOTAGE / "Reel 9" / "raw.mp4"}


def scratch_tests(*parts: str) -> Path:
    """Per-checkout scratch folder for tests: <VEOS_HOME>/scratch/tests/<checkout tag>/<parts>.

    Tests rmtree and rebuild their folder; two checkouts (git worktrees) running the suite at once on one machine used to
    share <VEOS_HOME>/scratch/tests/<name> and delete each other's project mid-test (random failures in test_scenes /
    test_render). The tag is a hash of this checkout's path, so each worktree gets its own folder."""
    tag = hashlib.sha1(str(Path(__file__).resolve().parents[3]).encode("utf-8")).hexdigest()[:8]
    return veos_home() / "scratch" / "tests" / tag / Path(*parts)


def fixture_clip(seconds: float = 5.0, which: str = "reel7", start: float = 20.0) -> Path:
    """Return a cached short clip (CFR 30 fps) cut from a raw test video; pytest should skip if missing."""
    src = RAW[which]
    if not src.exists():
        raise FileNotFoundError(f"test footage missing: {src}")
    out = veos_home() / "scratch" / "fixtures" / f"{which}_{start:g}_{seconds:g}.mp4"
    if not out.exists():
        out.parent.mkdir(parents=True, exist_ok=True)
        run([tools().ffmpeg, "-v", "error", "-y", "-ss", str(start), "-t", str(seconds), "-i", str(src),
             "-r", "30", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "aac", str(out)])
    return out
