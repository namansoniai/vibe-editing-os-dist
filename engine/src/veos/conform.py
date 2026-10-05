"""veos conform: constant-30-fps H.264 working copies + mono 48 kHz wav per source."""
from __future__ import annotations

import time
from pathlib import Path

from . import media
from .core import FPS, VeosError, need_project, r3, read_json, run, tools, write_json

BT601 = {"smpte170m", "bt470bg", "smpte240m"}


def add_args(p, cmd):
    p.add_argument("--id", default=None, help="conform only this source id")
    p.add_argument("--force", action="store_true", help="redo even if outputs are up to date")


def _fresh(out: Path, src: Path) -> bool:
    return out.exists() and out.stat().st_size > 0 and out.stat().st_mtime >= src.stat().st_mtime


def _count_frames(path: Path) -> int:
    r = run([tools().ffprobe, "-v", "error", "-count_packets", "-select_streams", "v:0",
             "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0", str(path)])
    return int(r.stdout.decode().strip().split(",")[0])


def _colorspace(path: Path) -> str:
    r = run([tools().ffprobe, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=color_space",
             "-of", "csv=p=0", str(path)], check=False)
    return r.stdout.decode().strip()


def main(args, project) -> dict:
    proj = need_project(project)
    sp = proj.work / "sources.json"
    if not sp.exists():
        raise VeosError("NO_SOURCES", "work/sources.json not found", "Run `veos ingest <files>` first.")
    data = read_json(sp)
    todo = [s for s in data["sources"] if args.id in (None, s["id"])]
    if not todo:
        raise VeosError("NO_SUCH_ID", f"no source with id {args.id}", "See work/sources.json for the ids.")
    ff = tools().ffmpeg
    out_summary, warnings = [], []
    for s in todo:
        t0 = time.time()
        src = proj.abs(s["path"])
        if not src.exists():
            raise VeosError("SOURCE_MISSING", f"source file not found: {src}", "Move it back or re-run `veos ingest`.")
        pr = media.probe(src)
        v = pr["video"]
        vid = proj.path("work", "src", f"{s['id']}.mp4")
        wav = proj.path("work", "audio", f"{s['id']}.wav")
        a_idx = (s.get("audio") or {}).get("stream", 0)
        notes = [n for n in s.get("notes", []) if not n.startswith("conform:")]
        status = []
        if v is not None:
            if not args.force and _fresh(vid, src):
                status.append("video cached")
            else:
                vf = [f"fps={FPS}"]
                if _colorspace(src) in BT601:
                    vf.append("scale=in_color_matrix=bt601:out_color_matrix=bt709:out_range=tv")
                cmd = [ff, "-v", "error", "-y", "-i", str(src), "-map", "0:v:0", "-vf", ",".join(vf), "-fps_mode", "cfr",
                       "-c:v", "libx264", "-crf", "16", "-preset", "veryfast", "-pix_fmt", "yuv420p",
                       "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv"]
                if pr["audio"]:
                    a = pr["audio"][a_idx]
                    cmd += ["-map", f"0:a:{a_idx}", "-c:a", "copy" if a["codec"] == "aac" else "aac", "-b:a", "192k"]
                cmd += ["-movflags", "+faststart", str(vid)]
                tmp = vid.with_suffix(".tmp.mp4")
                cmd[-1] = str(tmp)
                run(cmd, proj, "conform")
                tmp.replace(vid)
                status.append("video done")
        if pr["audio"]:
            if not args.force and _fresh(wav, src):
                status.append("audio cached")
            else:
                if len(pr["audio"]) > 1:
                    notes.append(f"conform: used audio stream {a_idx} of {len(pr['audio'])} (loudest non-silent)")
                tmp = wav.with_suffix(".tmp.wav")
                run([ff, "-v", "error", "-y", "-i", str(src), "-map", f"0:a:{a_idx}", "-ac", "1", "-ar", "48000",
                     "-c:a", "pcm_s16le", "-f", "wav", str(tmp)], proj, "conform")
                tmp.replace(wav)
                status.append("audio done")
        else:
            warnings.append(f"{s['id']}: no audio stream")
        info: dict = {"fps": FPS}
        if v is not None:
            frames = _count_frames(vid)
            info.update(video=proj.rel(vid), frames=frames)
            s["frames"] = frames
            s["duration"] = r3(frames / FPS)
        if pr["audio"]:
            info["audio"] = proj.rel(wav)
        s["conformed"] = info
        s["notes"] = notes
        cached = all("cached" in x for x in status) and bool(status)
        out_summary.append({"id": s["id"], "frames": info.get("frames"), "fps": FPS,
                            "lufs": (s.get("audio") or {}).get("lufs"), "status": "cached" if cached else ", ".join(status),
                            "s": round(time.time() - t0, 1)})
    write_json(sp, data)
    return {"sources": out_summary, "warnings": warnings}
