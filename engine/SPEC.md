# `veos` engine: spec (contract v2: scenes, no component library)

This is the single source of truth for the engine's commands and data files. Modules must follow it exactly. A change to this file needs Opus review.

## 1. Conventions
- **Invocation:** `veos <command> [args] --project DIR` (the project folder for one video). It runs as `python -m veos` or through the `veos` console script.
- **Output:** **stdout gets exactly one compact JSON object** (one line):
  `{"ok": true, "cmd": "probe", ...command-specific summary..., "warnings": [], "elapsed_s": 1.23}`
  On failure: `{"ok": false, "cmd": "...", "error": {"code": "FFMPEG_MISSING", "message": "...", "hint": "plain-language fix"}}` and exit code 1.
  Keep summaries small (≤ ~40 lines when pretty-printed). Detail goes to files, never stdout.
- **Module interface:** each module exposes `add_args(parser, cmd)` and `main(args, project) -> dict`. The dict is the summary that `cli.py` prints.
  - `project` is `None` when `--project` isn't given. Project commands call `veos.core.need_project(project)`.
  - Raise `veos.core.VeosError(code, message, hint)` for expected failures.
  - Use `veos.core.run()` for subprocesses and `read_json`/`write_json` for JSON.
  - Don't print to stdout yourself.
- **Logs:** `<project>/logs/<command>.log` (full tool output, timings).
- **Paths:**
  - Every path stored in JSON is relative to the project folder when it's inside it, absolute otherwise.
  - Use `pathlib`, `encoding="utf-8"` everywhere, and `Path.as_uri()` for browser URLs.
  - Paths with spaces must work.
- **Tools:** resolve ffmpeg/ffprobe/models/browsers through `veos.core.tools()`. That means `VEOS_HOME` (env, default `%LOCALAPPDATA%\VibeEditingOS` or `~/Library/Application Support/VibeEditingOS`), then `tools/ffmpeg/bin`, then PATH. Never hard-code.
- **Determinism:** no unseeded randomness. Every time is in **seconds (float, 3 decimals)** plus **frames at 30 fps** where useful. The project fps is 30 (`FPS = 30`).
- **Heavy files:** decoded frames, alpha and renders go to `<project>/work` or `VEOS_HOME/scratch`, never the repo.
- **Tests:** pytest in `engine/tests/`. Fixtures come from `veos.testing.fixture_clip(seconds)`, which cuts a short clip from `$VEOS_FOOTAGE` (default `C:\namansoni.ai\vibe-editing-os-footage`). Skip with a reason if it's missing.

## 2. Project folder
```
<project>/
  project.json            (orchestrator state; engine only reads "fps" / "size" if present)
  raw/                    (optional; sources may live anywhere)
  work/
    sources.json          (veos ingest)
    src/<id>.mp4          (veos conform: CFR 30 fps, 1080x1920 or source size, BT.709)
    audio/<id>.wav        (veos conform: mono 48 kHz, pre-normalisation)
    words/<id>.json       (veos transcribe, source time)
    edl.json              (written by the rough-cut skill / Claude)
    cutmap.json           (veos cut)
    words.edit.json       (veos cut: words remapped to edit time)
    cut_proxy.mp4         (veos cut: 540x960 review proxy)
    matte/<id>.mp4        (veos matte: gray H.264 alpha, same frame count as src)
    face/<id>.json        (veos matte)
    captures/             (veos capture)
  plan/ review/ out/ logs/
```

## 3. Data formats

**sources.json**
```json
{"version": 1, "fps": 30, "sources": [
  {"id": "A", "path": "C:/…/reel 7.mp4", "kind": "talking-head", "duration": 57.984, "frames": 1740,
   "width": 1080, "height": 1920, "rotation": 0, "fps_in": "30/1", "vfr": false,
   "audio": {"stream": 0, "channels": 2, "lufs": -19.2, "tp": -1.1},
   "segments": [{"start": 0.0, "end": 14.2, "setup": "selfie"}, {"start": 14.2, "end": 57.984, "setup": "tripod"}],
   "face_ratio": 0.97, "notes": []}]}
```
- `kind` is one of `talking-head | screen-recording | broll | audio-only`.
- `setup` is one of `selfie | tripod | wide | screen | other`.
- Segment boundaries come from scene detection plus a face-size and camera-motion heuristic.
- Ids are `A, B, C…` for talking heads and `S1, S2…` for screens/B-roll, in file order.

**words/<id>.json** (source time)
```json
{"version": 1, "source": "A", "model": "large-v3-turbo", "language": "hi", "prompt_used": true,
 "words": [{"i": 0, "w": "Haan", "s": 0.412, "e": 0.655, "p": 0.93, "script": "devanagari|latin", "onset_snapped": true}],
 "silences": [[3.21, 3.65]], "glossary_fixes": [{"i": 14, "from": "cloud", "to": "Claude"}]}
```

**edl.json** (input to `veos cut`, written by Claude)
```json
{"version": 1, "fps": 30, "segments": [{"src": "A", "in": 0.41, "out": 3.21, "note": "hook take 2"}, {"src": "A", "in": 3.65, "out": 9.8}]}
```

**cutmap.json** (output of `veos cut`; edit time → source)
```json
{"version": 1, "fps": 30, "duration": 52.4, "frames": 1572,
 "segments": [{"t0": 0.0, "t1": 2.8, "f0": 0, "f1": 84, "src": "A", "in": 0.41, "in_frame": 12}]}
```
- Segment boundaries snap to whole frames.
- For edit frame `n` in `[f0, f1)`, the source frame is `in_frame + (n - f0)`.
- The `words.edit.json` format is the same as `words/<id>.json`, plus `"src"` per word and edit-time `s`/`e`. Words in cut regions are dropped.

**face/<id>.json**
```json
{"version": 1, "source": "A", "fps": 30, "frames": 1740, "boxes": [[412, 380, 300, 360, 0.97], null]}
```
- Each box is `[x, y, w, h, score]` in source pixels, or `null`.
- Gaps of ≤ 6 frames are interpolated. Longer gaps stay `null`.

## 4. Commands (owner module → `veos/<module>.py`)
| Command | Args | Writes | stdout summary |
|---|---|---|---|
| `doctor [--quick]` | — | — | tools found + versions, VEOS_HOME, disk free, fonts present, models present, problems[] with hints |
| `ingest <files/folders…>` | `--project` | `work/sources.json` | per source: id, kind, duration, setup segments, vfr |
| `conform [--id X]` | | `work/src/*.mp4`, `work/audio/*.wav` | per source: frames, fps, loudness |
| `transcribe [--id X] [--script FILE] [--glossary FILE] [--fast]` | | `work/words/*.json` | per source: words, language, rtf, glossary fixes count, low-confidence count |
| `cut <edl.json>` | | `cutmap.json`, `words.edit.json`, `cut_proxy.mp4` | duration, segments, removed seconds, gaps ≥ 150 ms remaining |
| `matte [--id X] [--quality]` | | `work/matte/*.mp4`, `work/face/*.json` | fps achieved, frames, face coverage % |
| `capture <url> [--scroll S] [--name N]` | | `work/captures/<name>.png` (+ `.mp4` if scrolling) | size, path |
| `render --html F --frames N [--test 0,30,…] [--range A B] [--workers K] [--out DIR]` | | test PNGs or chunk MP4s + `list.txt` | frames done, ms/frame, chunk check |
| `assemble --out FILE [--audio WAV]` | | final MP4 | frames == expected?, duration, colour tags |
| `sheet <dir> <out_prefix> [--per 28] [--cols 7]` | | contact sheets | paths |
| `sfx <cues.json> <out.wav> --dur D` | | wav | cues placed, bus peak |
| `mix <voice.wav> <out.wav> --dur D [--sfx W] [--music W]` | | stereo master | LUFS, TP |
| `qa <final.mp4> [--expect-frames N] [--ref-audio W]` | | `out/qa-report.md` + contact sheet | pass/fail per check |
| `tokens [--playbook ID]` | `--project` | `work/tokens.json` | merges `playbooks/<id>/tokens.json` (+ `plan/tokens.override.json`), contrast-checks; roles, fonts, warnings |
| `scenes-meta` | `--project` | `plan/scenes.meta.json` (list) | headless load of the bundle; scene ids; registration errors are reported with the scene id |
| `measure [--every 10] [--range A B]` | `--project` | `plan/measure.json` `{frames:{n:{scene_id:[x0,y0,x1,y1]}}}` | rendered rect per active scene (1080x1920 px, resting position); ms/frame |
| `validate` | `--project` | `plan/validate.json` | `passed`, failures `{rule, beat, t, msg, fix}`; reads timeline + scenes.meta (+ measure) + playbook rules |
| `prep-frames`, `bundle` | `--project` | `work/frames/*`, `work/render/bundle.js` | bundle `node --check`s `plan/scenes.js` and includes it plus `plan/assets/*` |
| `project init\|show\|set\|latest [--playbook ID]` | | `project.json` | state (`playbook`, default `naman`) |
| `paths` | | — | `repo_root, playbooks, renderer_player, renderer_core, veos_home` |

Per-reel files in `<project>/plan/`: `timeline.json` (no `layers`; beats list scene ids and carry a `visual` sentence), `scenes.js` (Claude-written `VEOS.scene({...})` calls), optional `assets/`, `tokens.override.json`; generated `scenes.meta.json`, `measure.json`, `validate.json`. See `renderer/CONTRACT.md` and `renderer/SCENES-API.md`.

## 5. Rules carried over from PROC / playbook (must hold)
- Frame count of the output = `round(duration × 30)`. Verify every chunk; never ship a mismatch.
- Rendering runs one Chromium per worker, frames piped as JPEG q95 into libx264 (CRF 14, yuv420p, BT.709 tags, `-r 30`). **No grain, no vignette.** Chunks are concatenated with stream copy and the `h264_metadata` colour tags restored.
- Audio: voice chain `highpass=f=80, deesser, acompressor`; two-pass loudnorm to **−14 LUFS, TP ≤ −1.5 dBTP**, measured on the final stereo file.
- Matte: RVM mobilenetv3 ONNX with recurrent state carried across frames, reset at hard cuts.
  - Default: 540×960 input, ds 0.5.
  - `--quality`: full resolution, ds 0.25.
  - Clean-up: keep the largest connected component touching the face box, plus components overlapping the previous frame's mask, to drop chair fragments.
  - Light temporal smoothing.
  - Output is gray H.264 (full-range flag set correctly) with the same frame count as the source.
- Transcription: large-v3-turbo int8, `language="hi"`, initial prompt = the first ~200 characters of the script, or else the glossary terms.
  - Chunks ≤ 11 s cut at pauses, with the quietest-20 ms fallback.
  - Word starts snap to the RMS onset (20 ms hop) within ±120 ms.
  - Glossary post-pass.
  - Pass audio as numpy arrays (a PyAV workaround).
- Never modify input files. Never write inside OneDrive.
