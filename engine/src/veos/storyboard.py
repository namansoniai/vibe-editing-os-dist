"""`veos storyboard`: build the review page (review/mockup.html) from plan/timeline.json.

Frames are real renderer frames (veos render test mode). Layout and page format follow reference/Storyboard-Template.md.
The hook title the reel uses (`meta.title`) and the next two best (`meta.title_alternatives`, written by reel-plan with
every candidate and its scores in plan/ideas.md) head the page, so the creator can swap with "use the second title".
"""
from __future__ import annotations

import argparse
import hashlib
import html
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from .core import FPS, VeosError, need_project, r3, read_json, run, tools, write_json

REPO = Path(__file__).resolve().parents[3]
MORPH_FRAMES = 12          # assumed length of a stage morph (via != cut)
NEAR = 4                   # a focus frame must be > NEAR frames from a transition / stage / camera change
MAX_STRIPS = 12
E = lambda x: html.escape(str(x)) if x is not None else ""


def add_args(p, cmd):
    p.add_argument("--html", help="renderer page (default <repo>/renderer/player.html)")
    p.add_argument("--query", action="append", help="k=v appended to the page URL (repeatable)")
    p.add_argument("--anim-fps", type=float, default=5, help="animatic frame rate (default 5)")
    p.add_argument("--workers", type=int, default=None, help="parallel browsers")


# ------------------------------------------------------------------ frame selection
def f_of(t: float) -> int:
    return int(round(t * FPS))


def _change_frames(tl: dict) -> list[int]:
    out = [f_of(t["t"]) for t in tl.get("transitions") or []]
    for i, s in enumerate(tl.get("stage") or []):
        if i == 0 and s["t"] <= 0:
            continue
        out.append(f_of(s["t"]))
    out += [f_of(c["t"]) for c in tl.get("camera") or []]
    out += [f_of(c.get("t", 0)) for c in tl.get("canvas_camera") or []]
    return out


def focus_frame(b: dict, changes: list[int], nframes: int) -> int:
    a = max(0, f_of(b["t0"]))
    z = max(a, min(nframes, f_of(b["t1"])) - 1)
    want = min(z, max(a, f_of(((b.get("trigger") or {}).get("at", b["t0"])) + 0.5)))
    dist = lambda f: min((abs(f - c) for c in changes), default=999)
    if dist(want) > NEAR:
        return want
    cands = sorted(range(a, z + 1), key=lambda f: (abs(f - want), f))
    for f in cands:
        if dist(f) > NEAR:
            return f
    return max(cands, key=lambda f: (dist(f), -abs(f - want)))


def _rng(a, b, step=1):
    return list(range(a, b + 1, step))


def pick_strips(tl: dict, nframes: int) -> list[dict]:
    cand: list[dict] = []

    def add(title, desc, frames):
        cand.append({"title": title, "desc": desc, "frames": sorted({min(nframes - 1, max(0, f)) for f in frames})})

    add("Frame 0 (opening)", "Frames 0-7, every frame: what the viewer sees first.", _rng(0, 7))
    for tr in sorted(tl.get("transitions") or [], key=lambda x: x["t"]):
        c = f_of(tr["t"])
        add(f"Transition: {tr['id']}", f"{tr['t']:.2f} s (frame {c}), every frame from -6 to +6.", _rng(c - 6, c + 6))
    prev = None
    for s in tl.get("stage") or []:
        if prev is not None and s.get("via", "cut") != "cut":
            a = f_of(s["t"])
            add(f"Stage: {prev} to {s['layout']} ({s['via']})",
                f"{s['t']:.2f} s: the stage morphs from {prev} to {s['layout']}, every frame.", _rng(a, a + MORPH_FRAMES + 3))
        prev = s["layout"]
    cta = [b for b in tl.get("beats") or [] if str(b.get("section", "")).upper() == "CTA"]
    if cta:
        a = f_of(cta[0]["t0"])
        add("CTA opening", f"{cta[0]['t0']:.2f}-{cta[0]['t0'] + 1.2:.2f} s: first 1.2 s of the CTA, every 3rd frame.",
            _rng(a, a + 35, 3))
    seen = set()
    for c in tl.get("camera") or []:
        pr = c.get("preset") or f"crop {c.get('crop', (c.get('p') or {}).get('crop'))}"  # camera v2: preset-less crop
        if pr in seen:
            continue
        seen.add(pr)
        a = f_of(c["t"])
        add(f"Camera: {pr}", f"{c['t']:.2f} s: first use of the {pr} camera move, frames -2 to +8.", _rng(a - 2, a + 8))
    for c in tl.get("canvas_camera") or []:  # E-14: the first use of each canvas-camera move, every 2nd frame
        name = str(c.get("move"))
        if ("cc", name) in seen:
            continue
        seen.add(("cc", name))
        a, d = f_of(c.get("t", 0)), f_of(c.get("dur") or 0.8)
        add(f"Canvas camera: {name}", f"{c.get('t', 0):.2f} s: the {name} move across the canvas, every 2nd frame.",
            _rng(a - 2, a + d + 4, 2))
    out, used = [], []
    for s in cand:
        fs = set(s["frames"])
        if any(fs <= u for u in used):
            continue
        used.append(fs)
        out.append(s)
        if len(out) == MAX_STRIPS:
            break
    return out


# ------------------------------------------------------------------ text for the cards
def _nice(s: str) -> str:
    s = str(s).replace("-", " ").replace("_", " ")
    return s[:1].upper() + s[1:]


def load_scenes(project) -> list[dict]:
    f = project.root / "plan" / "scenes.meta.json"
    try:
        data = read_json(f) if f.exists() else []
    except ValueError:
        data = []
    return data if isinstance(data, list) else []


def beat_scenes(scenes: list[dict], b: dict) -> list[dict]:
    ids = b.get("layers")
    if ids:
        return [s for s in scenes if s.get("id") in ids]
    return [s for s in scenes if s.get("t_in", 0) < b["t1"] and s.get("t_out", 0) > b["t0"]]


def _texts(scenes: list[dict]) -> list[str]:
    out = []
    for s in scenes:
        v = s.get("text_content")
        if isinstance(v, str) and v.strip():
            out.append(v.strip())
    return out


def _within(items, b, key="t"):
    return [x for x in items or [] if b["t0"] - 1e-6 <= x[key] < b["t1"] - 1e-6]


def visual_line(tl: dict, b: dict, scenes: list[dict] | None = None) -> str:
    base = str(b.get("visual") or "").strip() or " · ".join(str(x) for x in (b.get("layers") or []))         or " · ".join(str(s.get("id")) for s in beat_scenes(scenes or [], b))
    parts = [base] if base else []
    for s in _within(tl.get("stage"), b):
        if s.get("via") is None and s["t"] <= 0:
            continue
        parts.append(f"stage to {s['layout']}" + (f" ({s['via']})" if s.get("via") not in (None, "cut") else ""))
    for c in _within(tl.get("camera"), b):
        parts.append(f"{c['preset'].replace('-', ' ')} camera")
    return " · ".join(parts) or "Speaker only"


def in_out(tl: dict, b: dict) -> str:
    items = []
    for s in _within(tl.get("stage"), b):
        if s.get("via") not in (None, "cut"):
            items.append(f"{s['via']} @ {s['t']:.2f}s")
    for t in _within(tl.get("transitions"), b):
        items.append(f"{t['id']} @ {t['t']:.2f}s")
    return ", ".join(items) or "none"


def sfx_names(tl: dict, b: dict) -> str:
    """The beat's sounds as 'id - why' (catalogue cues), never file paths; legacy {"file"} cues show the file name."""
    names = []
    for s in tl.get("sfx") or []:
        if s.get("beat") == b["id"] or (s.get("beat") is None and b["t0"] <= s["t"] < b["t1"]):
            if s.get("id"):
                names.append(f"{s['id']} — {s['why']}" if s.get("why") else str(s["id"]))
            else:
                names.append(Path(str(s.get("file", ""))).name)
    return "; ".join(n for n in names if n)


# ------------------------------------------------------------------ config
def build_config(tl: dict, project, anim_fps: float) -> dict:
    meta = tl["meta"]
    beats = tl["beats"]
    nframes = int(meta.get("frames") or f_of(meta["duration"]))
    changes = _change_frames(tl)
    stills = [focus_frame(b, changes, nframes) for b in beats]
    secs: dict[str, list] = {}
    for b in beats:
        secs.setdefault(b["section"], []).append(b)
    legend = []
    for k, bs in secs.items():
        first = " ".join(str(bs[0].get("spoken", "")).split()[:7])
        legend.append([_nice(k), f"{bs[0]['t0']:.1f}-{bs[-1]['t1']:.1f} s · {first}"])
    w, h = meta.get("size", [1080, 1920])
    facts = [f"{w}×{h} · {meta.get('fps', FPS)} fps", f"{meta['duration']:.2f} s · {nframes} frames"]
    if meta.get("playbook"):
        facts.append(f"Playbook: {meta['playbook']}")
    if meta.get("keyword"):
        facts.append(f"Keyword: {meta['keyword']}")
    title = meta.get("title") or project.root.name
    alts = [str(a) for a in meta.get("title_alternatives") or [] if str(a).strip()][:2]
    return {
        "page_title": f"{project.root.name} Storyboard", "title_main": project.root.name, "title_em": title,
        "subtitle": "Storyboard for review. Every image is a real frame from the renderer; nothing has been rendered to video yet.",
        "facts": facts, "titles": [str(meta["title"])] + alts if meta.get("title") and alts else [],
        "audio": "mockup/voice.m4a", "size": [w, h], "fps": FPS, "frames": nframes,
        "duration": meta["duration"], "anim_fps": anim_fps,
        "sections": {k: _nice(k) for k in secs}, "modes": {str(b.get("mode")): str(b.get("mode")) for b in beats},
        "legend": legend, "stills": stills, "strips": pick_strips(tl, nframes),
        "footer": "Source plan: plan/timeline.json · Frames come from the real renderer · Final audio mix is applied in the full render.",
    }


def anim_list(C: dict) -> tuple[list[int], int]:
    step = max(1, round(C["fps"] / C["anim_fps"]))
    return list(range(0, C["frames"], step)), step


def all_frames(C: dict):
    st = list(C["stills"])
    sp = [n for s in C["strips"] for n in s["frames"]]
    an, _ = anim_list(C)
    return st, sp, an, sorted(set(st + sp + an))


# ------------------------------------------------------------------ page
def cards_html(C: dict, tl: dict, scenes: list[dict]) -> str:
    out, cur = [], None
    for b, n in zip(tl["beats"], C["stills"]):
        if b["section"] != cur:
            cur = b["section"]
            out.append(f'<h2 class="sec" id="{E(cur)}">{E(C["sections"].get(cur, cur))}</h2>')
        ost = " · ".join(E(x) for x in dict.fromkeys(_texts(beat_scenes(scenes, b)))) or "—"
        sfx = E(sfx_names(tl, b)) or "—"
        tr = b.get("trigger") or {}
        tags = "".join(f'<span class="tag">{E(x)}</span>' for x in (C["modes"].get(str(b.get("mode")), b.get("mode")), b.get("tone"),
                                                                    b.get("line_type")) if x)
        notes = str(b.get("notes") or "")
        dev = f'<p class="dev"><b>Deviation:</b> {E(notes[4:].strip())}</p>' if notes.startswith("dev:") else ""
        out.append(f'''<article class="beat"><button class="th" data-src="mockup/still_{n:04d}.jpg" aria-label="Enlarge beat {b['id']}"><img loading="lazy" src="mockup/still_{n:04d}.jpg" alt="Beat {b['id']} key frame"></button>
<div class="info"><div class="top"><span class="id">{int(b['id']):02d}</span><span class="tc">{b['t0']:.2f}–{b['t1']:.2f}s</span>{tags}</div>
<p class="spoken">“{E(b.get('spoken', ''))}”</p><p class="vis">{E(visual_line(tl, b, scenes))}</p>
<dl><dt>On screen</dt><dd>{ost}</dd><dt>Trigger</dt><dd>“{E(tr.get('word', ''))}” @ {float(tr.get('at', b['t0'])):.2f}s</dd><dt>In / out</dt><dd>{E(in_out(tl, b))}</dd><dt>Sound</dt><dd>{sfx}</dd></dl>{dev}
<button class="jump" data-t="{b['t0']}">▶ Play from {b['t0']:.2f}s</button></div></article>''')
    return "\n".join(out)


ORDINAL = ("first", "second", "third")


def titles_html(titles: list[str]) -> str:
    """The hook title in the reel and the next two best, numbered so the creator can say "use the second title"."""
    if len(titles) < 2:
        return ""
    rows = "".join(f'<li{" class=on" if i == 0 else ""}><b>{i + 1}</b> {E(t)}'
                   + (' <span>in the reel</span>' if i == 0 else "") + "</li>" for i, t in enumerate(titles))
    return (f'<section class="titles" aria-label="Hook title options"><h2>Hook title</h2><ol>{rows}</ol>'
            f'<p>To swap, say "use the {ORDINAL[1]} title" (or write your own).</p></section>')


def strips_html(C: dict) -> str:
    fps = C["fps"]
    return "".join(
        f'''<section class="strip"><h3>{E(s['title'])}</h3><p>{E(s['desc'])}</p><div class="row">{''.join(f'<figure><button class="th" data-src="mockup/strip_{n:04d}.jpg" aria-label="Enlarge frame {n}"><img loading="lazy" src="mockup/strip_{n:04d}.jpg" alt="frame {n}"></button><figcaption>f{n} · {n / fps:.2f}s</figcaption></figure>' for n in s['frames'])}</div></section>'''
        for s in C["strips"])


def build_page(C: dict, tl: dict, png_dir: Path, review: Path, scenes: list[dict]) -> dict:
    from PIL import Image
    st, sp, an, al = all_frames(C)
    mk = review / "mockup"
    (mk / "anim").mkdir(parents=True, exist_ok=True)
    for n in al:
        with Image.open(png_dir / f"t_{n:04d}.png") as im:
            im = im.convert("RGB")
            if n in st:
                im.resize((540, 960), Image.LANCZOS).save(mk / f"still_{n:04d}.jpg", quality=86)
            if n in sp:
                im.resize((216, 384), Image.LANCZOS).save(mk / f"strip_{n:04d}.jpg", quality=84)
            if n in an:
                im.resize((360, 640), Image.LANCZOS).save(mk / "anim" / f"a_{n:04d}.jpg", quality=78)
    _, step = anim_list(C)
    nav = "".join(f'<a href="#{E(k)}">{E(v)}</a>' for k, v in C["sections"].items()) + '<a href="#motion">Motion strips</a>'
    rep = {"%%TITLE%%": E(C["page_title"]), "%%H1%%": E(C["title_main"]), "%%H1EM%%": E(C["title_em"]), "%%SUB%%": E(C["subtitle"]),
           "%%FACTS%%": "".join(f"<span>{E(f)}</span>" for f in C["facts"]), "%%NAV%%": nav,
           "%%TITLES%%": titles_html(C.get("titles") or []),
           "%%LEGEND%%": "".join(f"<div><b>{E(a)}</b> {E(b)}</div>" for a, b in C["legend"]),
           "%%CARDS%%": cards_html(C, tl, scenes), "%%STRIPS%%": strips_html(C), "%%DUR%%": f"{C['duration']:.2f}",
           "%%NANIM%%": str(len(an)), "%%STEP%%": str(step), "%%AFPS%%": f"{C['anim_fps']:g}",
           "%%AUDIO%%": E(C["audio"]), "%%FOOT%%": E(C["footer"])}
    page = TEMPLATE
    for k, v in rep.items():
        page = page.replace(k, v)
    out = review / "mockup.html"
    out.write_text(page, encoding="utf-8", newline="\n")
    return {"page": out, "stills": len(st), "strip_frames": len(set(sp)), "anim": len(an), "frames": len(al)}


def check_script(page: Path) -> None:
    src = page.read_text(encoding="utf-8")
    scripts = re.findall(r"<script>(.*?)</script>", src, re.S)
    if not scripts:
        raise VeosError("NO_SCRIPT", "page has no inline script", "This is a bug in the generator.")
    node = shutil.which("node")
    if not node:
        return
    with tempfile.TemporaryDirectory() as d:
        js = Path(d) / "page.js"
        js.write_text(scripts[-1], encoding="utf-8")
        r = subprocess.run([node, "--check", str(js)], capture_output=True, text=True)
    if r.returncode:
        raise VeosError("PAGE_JS_INVALID", f"inline script failed node --check: {r.stderr.strip()[:300]}",
                        "This is a bug in the generator; report it.")


# ------------------------------------------------------------------ voice
def build_voice(project, tl: dict, out: Path) -> None:
    t = tools()
    dur = float(tl["meta"]["duration"])
    cm_path = project.work / "cutmap.json"
    audio_dir = project.work / "audio"
    if cm_path.exists():
        from .voice import build_voice_wav  # one implementation of the edit's voice track
        vw = project.work / "voice.wav"
        if not vw.exists() or vw.stat().st_mtime < cm_path.stat().st_mtime:
            build_voice_wav(project, vw)
        inputs = ["-i", str(vw)]
        graph = "[0:a]asetpts=PTS-STARTPTS[c]"
    else:
        wavs = sorted(audio_dir.glob("*.wav")) if audio_dir.exists() else []
        if not wavs:
            raise VeosError("AUDIO_MISSING", "no cutmap.json and no work/audio/*.wav", "Run `veos conform` (and `veos cut`).")
        inputs = ["-i", str(wavs[0])]
        graph = "[0:a]asetpts=PTS-STARTPTS[c]"
    graph += f";[c]highpass=f=80,loudnorm=I=-14:TP=-1.5,apad,atrim=end={dur:.4f}[o]"
    out.parent.mkdir(parents=True, exist_ok=True)
    bus = _sfx_bus(project, tl, inputs, graph, dur)
    if bus is not None:  # the creator hears the sounds before approving: voice + SFX bus
        inputs = inputs + ["-i", str(bus)]
        graph = graph.replace("[o]", "[v]") + (";[1:a]aformat=channel_layouts=mono[s];[v]aresample=48000,aformat=channel_layouts=mono[vm];"
                                               "[vm][s]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.89:level=false[o]")
    run([t.ffmpeg, "-y", "-v", "error", *inputs, "-filter_complex", graph, "-map", "[o]", "-ac", "2", "-ar", "48000",
         "-c:a", "aac", "-b:a", "128k", str(out)], project, "storyboard")


def _sfx_bus(project, tl: dict, inputs: list, graph: str, dur: float):
    """Bus WAV for the animatic, or None when the timeline has no catalogue cues / no catalogue (then voice only)."""
    if not any(c.get("id") for c in tl.get("sfx") or []):
        return None
    from .sfxlib import pack_dir, read_catalog_doc
    pack = pack_dir()
    cat = read_catalog_doc()
    if cat is None:
        project.log("storyboard", "sfx: no catalog.json; animatic is voice only")
        return None
    sc = tools().scratch / "sb"
    sc.mkdir(parents=True, exist_ok=True)
    vref = sc / "animatic_voice.wav"  # the loudness-normalised voice, so cue levels sit where the final mix puts them
    run([tools().ffmpeg, "-y", "-v", "error", *inputs, "-filter_complex", graph, "-map", "[o]", "-ac", "1", "-ar", "48000",
         str(vref)], project, "storyboard")
    return _build_bus_file(tl, cat, pack, vref, sc / "animatic_sfx.wav")


def _build_bus_file(tl, cat, pack, vref, out):
    from .sfxlib import build_bus
    build_bus(tl, cat, pack, vref, out)
    return out


# ------------------------------------------------------------------ main
def main(args, project):
    from . import render
    project = need_project(project)
    tlp = project.root / "plan" / "timeline.json"
    if not tlp.exists():
        raise VeosError("NO_TIMELINE", f"{tlp} not found", "Write plan/timeline.json first (planner step).")
    tl = read_json(tlp)
    C = build_config(tl, project, args.anim_fps)
    write_json(project.root / "plan" / "storyboard.config.json", C)
    st, sp, an, al = all_frames(C)

    html_path = Path(args.html) if args.html else REPO / "renderer" / "player.html"
    query = list(args.query or [])
    warnings: list[str] = []  # a stale work/tokens.json rebuilt on the way (tokens.refresh)
    if not any(q.startswith(("bundle=", "timeline=")) for q in query) and not args.html:
        from .prep import ensure_bundle
        query.append("bundle=" + ensure_bundle(project, warnings))
    scenes = load_scenes(project)
    scratch = tools().scratch / "sb" / hashlib.sha1(str(project.root).encode("utf-8")).hexdigest()[:12]
    shutil.rmtree(scratch, ignore_errors=True)
    scratch.mkdir(parents=True)
    w, h = C["size"]
    ns = argparse.Namespace(html=str(html_path), frames=C["frames"], test=",".join(map(str, al)), range=None,
                            workers=args.workers, out=str(scratch), size=f"{w}x{h}", query=query, preset="medium", crf="14")
    review = project.root / "review"
    try:
        render._render(ns, project)
        build_voice(project, tl, review / "mockup" / "voice.m4a")
        res = build_page(C, tl, scratch, review, scenes)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    check_script(res["page"])
    mb = sum(f.stat().st_size for f in (review / "mockup").rglob("*") if f.is_file()) + res["page"].stat().st_size
    return {"beats": len(tl["beats"]), "strips": len(C["strips"]), "strip_frames": res["strip_frames"],
            "animatic_frames": res["anim"], "page": project.rel(res["page"]), "mb": r3(mb / 1e6),
            "config": "plan/storyboard.config.json", **({"warnings": warnings} if warnings else {})}


TEMPLATE = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%%TITLE%%</title>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;700;800&family=Instrument+Serif:ital@1&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
:root{--bg:#0a0a0a;--panel:#141414;--line:rgba(255,255,255,.1);--text:#f2f2f2;--mute:#a3a3a3;--acc:#FF8B1F;--blue:#116CD4}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.5 'Inter Tight',system-ui,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:28px 16px 80px}
header h1{font-size:clamp(28px,5vw,44px);font-weight:800;letter-spacing:-.02em;margin:0 0 6px}
header h1 em{font-family:'Instrument Serif',serif;font-weight:400;color:var(--acc)}
.sub{color:var(--mute);margin:0 0 18px;max-width:780px}
.facts{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:22px}
.facts span{font:500 13px 'JetBrains Mono',monospace;border:1px solid var(--line);border-radius:999px;padding:5px 12px;color:#ddd}
.titles{background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:14px 18px;margin:0 0 22px;max-width:780px}
.titles h2{margin:0 0 8px;font-size:18px}.titles ol{list-style:none;margin:0 0 8px;padding:0;display:grid;gap:6px}
.titles li{font-size:17px;color:#ddd}.titles li b{display:inline-block;min-width:26px;color:var(--mute)}
.titles li.on{color:var(--text);font-weight:700}.titles li.on b{color:var(--acc)}
.titles li span{font:500 12px 'JetBrains Mono',monospace;border:1px solid var(--acc);color:var(--acc);border-radius:999px;padding:1px 8px;margin-left:6px}
.titles p{margin:0;color:var(--mute);font-size:14px}
nav{position:sticky;top:0;z-index:5;background:rgba(10,10,10,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);display:flex;gap:6px;overflow-x:auto;padding:10px 0;margin-bottom:8px}
nav a{white-space:nowrap;color:var(--text);text-decoration:none;font-weight:700;font-size:14px;padding:6px 12px;border-radius:999px;border:1px solid var(--line)}
nav a:hover{border-color:var(--acc)}
.player{display:grid;grid-template-columns:minmax(0,360px) 1fr;gap:28px;align-items:start;background:var(--panel);border:1px solid var(--line);border-radius:22px;padding:20px;margin:18px 0 10px}
.screen{position:relative;aspect-ratio:9/16;width:100%;border-radius:16px;overflow:hidden;background:#000}
.screen img{width:100%;height:100%;object-fit:cover;display:block}
.ctrl{display:flex;flex-direction:column;gap:14px}
.ctrl h2{margin:0;font-size:22px}
.ctrl p{margin:0;color:var(--mute)}
.btns{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
button{font:inherit;cursor:pointer}
.pp{background:var(--acc);color:#0a0a0a;border:0;border-radius:999px;padding:10px 22px;font-weight:800;font-size:16px}
.tm{font:500 15px 'JetBrains Mono',monospace;color:#ddd}
input[type=range]{width:100%;accent-color:var(--acc)}
.legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:8px;font-size:14px;color:#cfcfcf}
.legend div{border:1px solid var(--line);border-radius:12px;padding:8px 12px}
.legend b{color:var(--text)}
h2.sec{font-size:26px;margin:44px 0 14px;padding-top:8px;border-top:1px solid var(--line);scroll-margin-top:60px}
.beat{display:grid;grid-template-columns:200px 1fr;gap:20px;background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:14px;margin-bottom:14px}
.th{padding:0;border:0;background:none;display:block;width:100%;border-radius:12px;overflow:hidden}
.th img{width:100%;display:block;aspect-ratio:9/16;object-fit:cover;transition:transform .2s}
.th:hover img{transform:scale(1.02)}
.top{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:6px}
.id{font-weight:800;background:var(--acc);color:#0a0a0a;border-radius:8px;padding:1px 9px}
.tc{font:500 14px 'JetBrains Mono',monospace;color:#ddd}
.tag{font:500 12px 'JetBrains Mono',monospace;border:1px solid var(--line);border-radius:999px;padding:2px 10px;color:#cfcfcf}
.spoken{font-family:'Instrument Serif',serif;font-style:italic;font-size:24px;line-height:1.25;margin:4px 0 8px}
.vis{margin:0 0 10px;color:#e6e6e6}
dl{display:grid;grid-template-columns:110px 1fr;gap:4px 12px;margin:0 0 12px;font-size:14px}
dt{color:var(--mute)}dd{margin:0;color:#ddd}
.dev{font-size:14px;color:#ffcf9e;margin:0 0 10px}
.jump{background:none;border:1px solid var(--line);color:var(--text);border-radius:999px;padding:6px 14px;font-weight:700;font-size:14px}
.jump:hover{border-color:var(--acc)}
.strip{background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:16px;margin-bottom:14px}
.strip h3{margin:0 0 4px;font-size:19px}.strip p{margin:0 0 12px;color:var(--mute);font-size:15px}
.row{display:flex;gap:8px;overflow-x:auto;padding-bottom:6px}
.row figure{margin:0;flex:0 0 108px}
.row figcaption{font:500 11px 'JetBrains Mono',monospace;color:var(--mute);margin-top:4px;text-align:center}
.lb{position:fixed;inset:0;background:rgba(0,0,0,.9);display:none;align-items:center;justify-content:center;z-index:20;padding:16px}
.lb.on{display:flex}.lb img{max-height:94vh;max-width:100%;border-radius:14px}
.foot{color:var(--mute);font-size:14px;margin-top:40px}
@media (max-width:720px){.player{grid-template-columns:1fr}.beat{grid-template-columns:120px 1fr;gap:12px}.spoken{font-size:19px}dl{grid-template-columns:84px 1fr}}
</style></head>
<body><div class="wrap">
<header><h1>%%H1%% · <em>%%H1EM%%</em></h1>
<p class="sub">%%SUB%%</p>
<div class="facts">%%FACTS%%</div>%%TITLES%%</header>
<nav>%%NAV%%</nav>
<section class="player" aria-label="Animatic">
<div class="screen"><img id="af" src="mockup/anim/a_0000.jpg" alt="Animatic frame"></div>
<div class="ctrl"><h2>Animatic with voice (%%AFPS%% fps)</h2>
<p>Steps through the storyboard at %%AFPS%% frames per second, synced to the cleaned-up voice, so you can judge pacing and timing. Motion between frames isn't shown here; the strips below show it frame by frame.</p>
<div class="btns"><button class="pp" id="pp">▶ Play</button><span class="tm" id="tm">0.00 / %%DUR%% s</span></div>
<input type="range" id="sc" min="0" max="%%DUR%%" step="0.04" value="0" aria-label="Scrub timeline">
<div class="legend">%%LEGEND%%</div>
</div></section>
<audio id="au" src="%%AUDIO%%" preload="auto"></audio>
%%CARDS%%
<h2 class="sec" id="motion">Motion strips</h2>
%%STRIPS%%
<p class="foot">%%FOOT%%</p>
</div>
<div class="lb" id="lb" role="dialog" aria-label="Enlarged frame"><img id="lbi" alt="Enlarged frame"></div>
<script>
const au=document.getElementById('au'),af=document.getElementById('af'),pp=document.getElementById('pp'),sc=document.getElementById('sc'),tm=document.getElementById('tm');
const DUR=%%DUR%%,NA=%%NANIM%%,STEP=%%STEP%%,AFPS=%%AFPS%%;let last=-1;
const src=k=>'mockup/anim/a_'+String(k*STEP).padStart(4,'0')+'.jpg';
function show(t){const k=Math.min(NA-1,Math.max(0,Math.floor(t*AFPS)));if(k!==last){last=k;af.src=src(k);}sc.value=t;tm.textContent=t.toFixed(2)+' / '+DUR.toFixed(2)+' s';}
function loop(){show(au.currentTime);if(!au.paused&&!au.ended)requestAnimationFrame(loop);else pp.textContent='▶ Play';}
pp.onclick=()=>{if(au.paused){au.play();pp.textContent='❚❚ Pause';loop();}else{au.pause();pp.textContent='▶ Play';}};
sc.oninput=()=>{au.currentTime=parseFloat(sc.value);show(au.currentTime);};
au.onended=()=>{pp.textContent='▶ Play';};
for(let k=0;k<NA;k+=10){const i=new Image();i.src=src(k);}
document.querySelectorAll('.jump').forEach(b=>b.onclick=()=>{au.currentTime=parseFloat(b.dataset.t);show(au.currentTime);window.scrollTo({top:0,behavior:'smooth'});au.play();pp.textContent='❚❚ Pause';loop();});
const lb=document.getElementById('lb'),lbi=document.getElementById('lbi');
document.querySelectorAll('.th').forEach(b=>b.onclick=()=>{lbi.src=b.dataset.src;lb.classList.add('on');});
lb.onclick=()=>lb.classList.remove('on');document.addEventListener('keydown',e=>{if(e.key==='Escape')lb.classList.remove('on');});
</script></body></html>
'''
