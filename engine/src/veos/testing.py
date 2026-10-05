"""Test helpers: short fixture clips cut from the local test footage (never committed)."""
from __future__ import annotations

import os
from pathlib import Path

from .core import run, tools, veos_home

FOOTAGE = Path(os.environ.get("VEOS_FOOTAGE", r"C:\namansoni.ai\vibe-editing-os-footage"))
RAW = {"reel7": FOOTAGE / "Reel 7" / "reel 7.mp4", "reel9": FOOTAGE / "Reel 9" / "raw.mp4"}


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
