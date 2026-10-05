"""`veos render` and `veos assemble`: drive an HTML page (window.renderFrame(n)) in headless Chromium and encode frames.

Page contract: the page sets `window.READY === true` once fonts/assets are loaded and exposes
`async window.renderFrame(n)` (a pure function of n). One Chromium + one ffmpeg per worker; frames are piped as
JPEG q95 into libx264 and the chunks are later concatenated with stream copy (`assemble`).
"""
from __future__ import annotations

import multiprocessing as mp
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .core import FPS, Project, VeosError, r3, run, tools

COLOR = ["-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv"]
VF = "scale=out_color_matrix=bt709:out_range=tv:flags=bicubic,format=yuv420p"
BSF = "h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1:video_full_range_flag=0"
CHROME_ARGS = ["--force-color-profile=srgb", "--font-render-hinting=none", "--hide-scrollbars", "--mute-audio",
               "--allow-file-access-from-files",
               "--disable-background-timer-throttling", "--disable-renderer-backgrounding",
               "--disable-backgrounding-occluded-windows"]
RETRIES = 3


def add_args(p, cmd):
    if cmd == "assemble":
        p.add_argument("--out", required=True, help="final MP4 to write")
        p.add_argument("--chunks", required=True, help="folder with chunk_KK.mp4 (+ list.txt) from `veos render`")
        p.add_argument("--audio", help="audio file (WAV/AAC) to mux")
        p.add_argument("--frames", type=int, help="expected frame count (default: sum of the chunks)")
        return
    p.add_argument("--html", required=True, help="page exposing window.READY and async window.renderFrame(n)")
    p.add_argument("--frames", type=int, required=True, help="total frame count N (frames 0..N-1)")
    p.add_argument("--test", help="comma list of frames to render as PNG, e.g. 0,30,60")
    p.add_argument("--range", nargs=2, type=int, metavar=("A", "B"), help="render frames A..B-1 into one chunk (patching)")
    p.add_argument("--workers", type=int, default=None, help="parallel browsers (default min(8, max(1, cpus//2)))")
    p.add_argument("--out", help="output folder (default <project>/work/render or VEOS_HOME/scratch/render)")
    p.add_argument("--size", default="1080x1920", help="viewport WxH")
    p.add_argument("--query", action="append", help="k=v appended to the page URL (repeatable)")
    p.add_argument("--preset", default="medium", help="x264 preset (default medium)")
    p.add_argument("--crf", default="14")


# ---------------------------------------------------------------- helpers
def _log(path: str, text: str) -> None:
    with open(path, "a", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")


def _page_url(html: str, query: str) -> str:
    return Path(html).resolve().as_uri() + (("?" + query) if query else "")


def _nframes(ffprobe: str, path: Path) -> int:
    r = subprocess.run([ffprobe, "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
                        "stream=nb_read_frames", "-of", "csv=p=0", str(path)], capture_output=True, text=True)
    first = (r.stdout.split() or [""])[0].strip(",")
    return int(first) if first.isdigit() else 0


def _probe(ffprobe: str, path: Path, entries: str, stream: str | None = None) -> list[str]:
    cmd = [ffprobe, "-v", "error"]
    if stream:
        cmd += ["-select_streams", stream]
    cmd += ["-show_entries", entries, "-of", "default=nw=1:nk=1", str(path)]
    return subprocess.run(cmd, capture_output=True, text=True).stdout.split()


# ---------------------------------------------------------------- worker (runs in a spawned process)
def _new_page(br, job):
    pg = br.new_page(viewport={"width": job["w"], "height": job["h"]}, device_scale_factor=1)
    pg.goto(job["url"])
    pg.wait_for_function("window.READY===true || !!window.VEOS_BOOT_ERROR", timeout=60000)
    err = pg.evaluate("window.VEOS_BOOT_ERROR || null")
    if err:
        raise RuntimeError("page failed to boot: " + str(err)[:1500])
    return pg


def _shot(pg, n, kind):
    pg.evaluate("n => window.renderFrame(n)", n)
    if kind == "png":
        return pg.screenshot(type="png")
    return pg.screenshot(type="jpeg", quality=95)


def worker(job: dict) -> dict:
    from playwright.sync_api import sync_playwright
    t0 = time.perf_counter()
    res = {"k": job["k"], "done": 0, "error": None, "retries": 0}
    enc = None
    try:
        with sync_playwright() as pw:
            br = pw.chromium.launch(headless=True, args=CHROME_ARGS)
            pg = _new_page(br, job)
            if job["mode"] == "video":
                cmd = [job["ffmpeg"], "-y", "-v", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                       "-vf", VF, "-c:v", "libx264", "-crf", job["crf"], "-preset", job["preset"], "-pix_fmt", "yuv420p",
                       "-g", "60", *COLOR, "-r", str(FPS), job["path"]]
                errf = open(job["path"] + ".err", "wb")
                enc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=errf)
            for i, n in enumerate(job["frames"]):
                for attempt in range(RETRIES + 1):
                    try:
                        data = _shot(pg, n, "png" if job["mode"] == "png" else "jpeg")
                        break
                    except Exception as e:  # noqa: BLE001 - reopen the page and retry
                        if attempt == RETRIES:
                            raise
                        res["retries"] += 1
                        _log(job["log"], f"w{job['k']} frame {n} retry {attempt + 1}: {e!r}")
                        try:
                            pg.close()
                        except Exception:  # noqa: BLE001
                            pass
                        pg = _new_page(br, job)
                if enc:
                    enc.stdin.write(data)
                else:
                    (Path(job["dir"]) / f"t_{n:04d}.png").write_bytes(data)
                res["done"] += 1
                if i % 50 == 0:
                    _log(job["log"], f"w{job['k']} {i}/{len(job['frames'])}")
            br.close()
    except Exception as e:  # noqa: BLE001
        res["error"] = f"{type(e).__name__}: {e}"
        _log(job["log"], f"w{job['k']} FAILED {res['error']}")
    finally:
        if enc:
            try:
                enc.stdin.close()
            except Exception:  # noqa: BLE001
                pass
            enc.wait()
            if enc.returncode:
                res["error"] = res["error"] or f"ffmpeg exited {enc.returncode}"
    res["total_s"] = time.perf_counter() - t0
    return res


# ---------------------------------------------------------------- render
def _render(args, project: Project | None) -> dict:
    t = tools()
    html = Path(args.html)
    if not html.exists():
        raise VeosError("HTML_MISSING", f"page not found: {html}", "Check the --html path.")
    try:
        w, h = (int(x) for x in args.size.lower().split("x"))
    except ValueError:
        raise VeosError("BAD_SIZE", f"bad --size {args.size!r}", "Use WxH, e.g. 1080x1920.") from None
    out = Path(args.out) if args.out else (project.work / "render" if project else t.scratch / "render")
    out.mkdir(parents=True, exist_ok=True)
    if project and project.root.exists():
        (project.root / "logs").mkdir(exist_ok=True)
        log = str(project.root / "logs" / "render.log")
    else:
        log = str(out / "render.log")
    query = "&".join(args.query or [])
    workers = args.workers or min(8, max(1, (os.cpu_count() or 2) // 2))
    base = {"url": _page_url(str(html), query), "w": w, "h": h, "log": log, "ffmpeg": t.ffmpeg,
            "crf": str(args.crf), "preset": args.preset}

    if args.test:
        fl = [int(x) for x in args.test.split(",") if x.strip()]
        k = max(1, min(workers, 4, len(fl)))
        groups = [fl[i::k] for i in range(k)]
        jobs = [{**base, "k": i, "frames": g, "mode": "png", "dir": str(out)} for i, g in enumerate(groups) if g]
        mode = "test"
    else:
        if args.range:
            a, b = args.range
            if b <= a:
                raise VeosError("BAD_RANGE", f"--range {a} {b} is empty", "Use --range A B with B > A.")
            ranges = [(a, b)]
        else:
            if args.frames < 1:
                raise VeosError("BAD_FRAMES", "--frames must be >= 1", "")
            k = max(1, min(workers, args.frames))
            step = -(-args.frames // k)
            ranges = [(s, min(args.frames, s + step)) for s in range(0, args.frames, step)]
            for old in out.glob("chunk_*.mp4"):
                old.unlink()
        jobs = [{**base, "k": i, "frames": list(range(a, b)), "mode": "video", "path": str(out / f"chunk_{i:02d}.mp4")}
                for i, (a, b) in enumerate(ranges)]
        mode = "range" if args.range else "full"
    _log(log, f"render {mode}: {len(jobs)} workers, url={base['url']}")

    t0 = time.perf_counter()
    if len(jobs) == 1:
        results = [worker(jobs[0])]
    else:
        with mp.get_context("spawn").Pool(len(jobs)) as pool:
            results = pool.map(worker, jobs)
    wall = time.perf_counter() - t0
    done = sum(r["done"] for r in results)
    errors = [f"worker {r['k']}: {r['error']}" for r in results if r["error"]]
    for j in jobs:
        if j.get("path"):
            Path(j["path"] + ".err").unlink(missing_ok=True)
    summary = {"mode": mode, "frames": done, "workers": len(jobs), "ms_per_frame": r3(1000 * wall / max(done, 1)),
               "effective_fps": r3(done / wall) if wall else 0.0, "retries": sum(r["retries"] for r in results),
               "out": project.rel(out) if project else out.as_posix()}
    if mode == "test":
        summary["pngs"] = len(list(out.glob("t_*.png")))
        if errors:
            raise VeosError("RENDER_FAILED", "; ".join(errors),
                            "See logs/render.log; check the page sets window.READY and renderFrame.")
        return summary

    with ThreadPoolExecutor(max_workers=len(jobs)) as ex:
        counts = list(ex.map(lambda j: _nframes(t.ffprobe, Path(j["path"])) if Path(j["path"]).exists() else 0, jobs))
    bad = []
    for j, got in zip(jobs, counts):
        if got != len(j["frames"]):
            a, b = j["frames"][0], j["frames"][-1] + 1
            bad.append({"chunk": j["k"], "got": got, "expected": len(j["frames"]), "rerender": f"--range {a} {b}"})
    if mode == "full":
        lst = out / "list.txt"
        lst.write_text("".join(f"file '{Path(j['path']).as_posix()}'\n" for j in jobs), encoding="utf-8")
        summary["list"] = project.rel(lst) if project else lst.as_posix()
    summary["chunks"] = {"ok": len(jobs) - len(bad), "bad": len(bad)}
    if errors or bad:
        raise VeosError("CHUNK_MISMATCH", f"{len(bad)} chunk(s) wrong: {bad}; worker errors: {errors or 'none'}",
                        "Re-render each listed --range into another folder and splice it into list.txt in order.")
    return summary


# ---------------------------------------------------------------- assemble
def _assemble(args, project: Project | None) -> dict:
    t = tools()
    chunks = Path(args.chunks)
    lst = chunks / "list.txt"
    if not lst.exists():
        files = sorted(chunks.glob("chunk_*.mp4"))
        if not files:
            raise VeosError("NO_CHUNKS", f"no chunk_*.mp4 in {chunks}", "Run `veos render` first.")
        lst.write_text("".join(f"file '{f.resolve().as_posix()}'\n" for f in files), encoding="utf-8")
    listed = [Path(ln.strip()[6:-1]) for ln in lst.read_text(encoding="utf-8").splitlines() if ln.startswith("file '")]
    with ThreadPoolExecutor(max_workers=8) as ex:
        counts = list(ex.map(lambda f: _nframes(t.ffprobe, f), listed))
    expected = args.frames if args.frames is not None else sum(counts)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    cmd = [t.ffmpeg, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst)]
    audio_dur = None
    if args.audio:
        a = Path(args.audio)
        if not a.exists():
            raise VeosError("AUDIO_MISSING", f"audio not found: {a}", "Check --audio.")
        codec = (_probe(t.ffprobe, a, "stream=codec_name", "a:0") or [""])[0]
        ad = _probe(t.ffprobe, a, "format=duration")
        audio_dur = float(ad[0]) if ad else None
        acodec = ["-c:a", "copy"] if codec == "aac" else ["-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-ac", "2"]
        cmd += ["-i", str(a), "-map", "0:v:0", "-map", "1:a:0", *acodec]
    else:
        cmd += ["-map", "0:v:0"]
    cmd += ["-c:v", "copy", "-bsf:v", BSF, "-movflags", "+faststart", str(out)]
    run(cmd, project, "render")

    got = _nframes(t.ffprobe, out)
    tags = _probe(t.ffprobe, out, "stream=color_space,color_primaries,color_transfer,color_range,pix_fmt", "v:0")
    vdur = got / FPS
    summary = {"out": project.rel(out) if project else out.as_posix(), "frames": got, "expected": expected,
               "fps": FPS, "duration": r3(vdur), "tags": tags}
    if audio_dur is not None:
        summary["audio_duration"] = r3(audio_dur)
    problems = []
    if got != expected:
        problems.append(f"frame count {got} != expected {expected}")
    if audio_dur is not None and abs(audio_dur - vdur) > 1.0 / FPS + 1e-3:
        problems.append(f"audio {audio_dur:.3f}s vs video {vdur:.3f}s differ by more than one frame")
    if sum(1 for x in tags if x == "bt709") < 3:
        problems.append(f"BT.709 tags missing: {tags}")
    if problems:
        raise VeosError("ASSEMBLE_MISMATCH", "; ".join(problems),
                        "Re-render the short chunks (see CHUNK_MISMATCH --range hints) or trim/pad the audio to the "
                        "video length; do not ship this file.")
    return summary


def main(args, project):
    return _assemble(args, project) if args.cmd == "assemble" else _render(args, project)
