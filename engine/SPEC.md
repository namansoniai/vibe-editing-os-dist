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
| `sfx <cues.json> <out.wav> --dur D [--root DIR]` | | wav | legacy cue sheet (`{t, f, a, db}`): cues placed, bus peak |
| `sfx` (no positionals) | `--project`, `[--pack DIR]` | `work/sfx.wav` + `work/sfx.cues.json` | **auto-fetches missing cue files**, then builds the bus from `timeline.sfx` + the catalogue: each cue's file anchor (peak/onset/end) lands on `t`; peak dB = cue `db` or the role default (section 6); shifted so a voice at -18 dBFS speaking RMS is the reference (the real `work/voice.wav` level is used when present). cues, files, bus peak, voice offset, draft-tag warnings |
| `sfx catalog` | `[--pack DIR] [--descriptions CSV] [--draft] [--update]` | `<pack>/catalog.json`, or the app catalogue `assets/sfx/catalog.json` when there is no `--pack` or with `--update` | walks the pack (wav/mp3/ogg/m4a/aif) and measures every file, and/or reads the owner's `SFX_Descriptions.csv` (flexible columns; every column kept as `desc_*`). **Works without audio**: descriptions-only entries have `measured: false` and null measurements (they are measured when first fetched). Keeps `reviewed` tags, ids and urls on re-runs; descriptions or `--draft` fill role/vibe/energy/use guesses (Category gives the default role). Marks `excluded` + `excluded_reason` (duplicate, do_not_use, copyrighted, song). sounds, measured, excluded_by_reason, by_role |
| `sfx fetch` | `--ids a,b,c` or `--playbook ID` (its `sound.preferred` + `sound.palette_ids`) or `--project P` (every cue id in the timeline) | `VEOS_HOME/sfx/<relpath>` | downloads only missing/wrong-size files from `url` (else `base_url` + url-encoded relpath), 3 tries, verifies `size`; refuses excluded ids. requested, downloaded, already_cached, mb_downloaded |
| `sfx tag <tags.json>` | `--pack DIR` | `<pack>/catalog.json` | merges `{id: {role, vibe, energy, use[, anchor]}}`, validates the vocabulary, sets `tags_from: "reviewed"` |
| `mix <voice.wav> <out.wav> --dur D [--sfx W] [--music W] [--no-balance-check]` | | stereo master | LUFS, TP. With `--sfx` it then runs the balance gate and fails (`SFX_TOO_LOUD`, ok:false) when the median SFX level is not >= 20 dB under the voice, or (with `<sfx>.cues.json` next to the bus) any non-sub-hit cue is within 6 dB of the voice while speech is present |
| `qa <final.mp4> [--expect-frames N] [--ref-audio W]` | | `out/qa-report.md` + contact sheet | pass/fail per check |
| `tokens [--playbook ID]` | `--project` | `work/tokens.json` | merges `playbooks/<id>/tokens.json` (+ `plan/tokens.override.json`), contrast-checks; roles, fonts, warnings |
| `scenes-meta` | `--project` | `plan/scenes.meta.json` (list) | headless load of the bundle; scene ids; registration errors are reported with the scene id |
| `measure [--every 10] [--range A B] [--motion]` | `--project` | `plan/measure.json` `{frames:{n:{scene_id:[x0,y0,x1,y1]}}}`; `--motion`: `plan/measure.motion.json` (every frame where a z3-10 scene is active) | rendered rect per active scene, plus `"__subtitles"` (1080x1920 px, resting position); layout only, no screenshots (`--every 1` is cheap: ~17-20 ms/frame); ms/frame |
| `validate [--skip-motion]` | `--project` | `plan/validate.json` | `passed`, failures `{rule, beat, t, msg, fix}`; reads timeline + scenes.meta (+ measure, measure.motion) + playbook rules; **always runs global checks G1 no overlap, G2 no clutter, G3 smooth motion** (SCENES-API 7b) and builds `measure.motion.json` itself when scenes.js exists and it is stale; **always runs the sound rules S1-S6 when `timeline.sfx` has cues with an `id`** (section 6) |
| `prep-frames`, `bundle` | `--project` | `work/frames/*`, `work/render/bundle.js` | bundle `node --check`s `plan/scenes.js` and includes it plus `plan/assets/*` |
| `project init|show|set|latest [--playbook ID]` | | `project.json` | state. `init` without `--playbook` uses the clips' folder workspace playbook (an existing project.json's playbook on `--force`), else error `PLAYBOOK_REQUIRED` (hint: choose a playbook first). Phases: init, prep, roughcut, captions, **inputs**, plan, storyboard, approved, render, done. `set inputs=@file.json` stores free JSON in the `inputs` key (the creator's per-reel inputs: screen recordings, links, numbers) |
| `workspace get\|set [--dir D] [--playbook ID]` | | `<D>/.vibe-editing-os.json` `{version:1, playbook, created, updated}` | `get` walks up from D for the marker and lists `playbooks` (id, name, handle, updated; user playbooks dir, `_*` excluded); `set` errors `PLAYBOOK_MISSING` if the playbook does not exist |
| `playbook new-id --name N [--handle @x]` | | none | a unique kebab id (`aria-mehta`, `aria-mehta-2`, ...) that collides with no playbook folder |
| `learn add\|list\|remove --playbook ID` | `--text --area plan\|visuals\|captions\|sound\|cut\|pacing\|other [--reel P] [--quote Q]`; `--id L3` | `<playbook>/learned.md` + `learned.json` | numbered `L<n> · date · area · text (from: reel; said: "quote")`; `remove` sets `active:false` (history kept). Learned rules override the playbook body, never the global rules |
| `asset add <file> [--name N]` / `asset list` | `--project` | `plan/assets/<name>.<ext>` or `plan/assets/<name>/f%05d.jpg` + `meta.json {frames, fps, w, h, duration}` | images copied; videos conformed to 30 fps, JPEG frames scaled to fit 1080 px wide (q ~90); returns name, kind, frames/size |
| `paths` | | — | `repo_root, playbooks, renderer_player, renderer_core, veos_home, sfx_pack, sfx_catalog, sfx_catalog_exists` (`sfx_pack` = `VEOS_HOME/sfx`, the download cache; `sfx_catalog` = `<app>/assets/sfx/catalog.json`; env `VEOS_SFX=DIR` overrides both with a full pack folder, used by tests) |

The bundle carries `videos: {name: {frames, fps, w, h, duration, base_url}}` for video assets (`ctx.videoFrame`).

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

## 6. Sound effects (bundled pack, catalogue, cues, rules S1-S6)
**The audio is NOT in the app.** The app ships only `assets/sfx/catalog.json` (committed, with the owner's descriptions `SFX_Descriptions.csv`/`.md`). The audio lives in the public repo `namansoniai/vibe-editing-os-sfx` (one file per sound, published by `tools/publish_sfx.py PACK_DIR`: skips excluded files and files over 95 MB, pushes in batches, writes `base_url` + per-file `url` into the catalogue) and is downloaded on demand into `VEOS_HOME/sfx/<relpath>` (`veos sfx fetch`; `veos sfx --project` fetches what its cues need). `tools/make_dist.py` copies only `assets/sfx/catalog.json`; the installers just create `VEOS_HOME/sfx`. Every sound in a reel must **match the reel's vibe and land on a real visual moment**.

**Vocabulary** (the only allowed values)
- `role`: whoosh, swish, impact, sub-hit, riser, downlifter, pop, click, tap, typing, shine, chime, ding, sparkle, glitch, alarm, camera, cash, meme, ambient
- `vibe` (subset): calm, premium, playful, hype, tense, comedic, techy, organic
- `energy`: integer 1-5
- `use` (subset): transition, text-pop, reveal, card-in, card-out, data, number, warning, success, cta, hook-stop, list-cue, comedy

**catalog.json**: `{"version": 1, "base_url": "https://raw.githubusercontent.com/namansoniai/vibe-editing-os-sfx/main/", "sounds": [...]}`; each sound: `{"file": "relpath", "id": "stable-slug", "dur", "peak_t", "onset", "end" (s; 10 ms RMS envelope, 30 dB window), "anchor": "peak|onset|end", "role": null, "vibe": [], "energy": null, "use": [], "tags_from": "draft|reviewed", "tp_db", "lufs" (unweighted, active part), "centroid_hz", "attack_ms" (10-90% rise; lower is sharper), "size" (bytes), "url", "measured": bool, "excluded": bool, "excluded_reason": null|duplicate|do_not_use|copyrighted|song|too_large, "desc_category", "desc_length", "desc_description", "desc_best_use" (the owner's columns, as `desc_<header>`)}`. Measurements are null while `measured` is false.
- **Exclusion** (from Description / Best use): "same as ... (MP3 copy)" or "duplicate" -> `duplicate`; "do not use" -> `do_not_use`; a quoted source title ("from '...'") or "copyright" -> `copyrighted`; "song", "track", "music bed", or a Music sting/Logo longer than 20 s -> `song`. Excluded sounds are never published, fetched or used.
- `id` = slug of the relative path without extension, kept stable across re-runs. Default anchor: hits and whooshes `peak`, risers `end`, everything else (clicks, pops, chimes, ...) `onset`.
- `--draft` (implied by `--descriptions`) guesses from the CSV Category (default role: Whoosh/Transition whoosh, Glitch/Digital glitch, Impact/Hit impact, Ding/Shine/Magic ding, UI/Click/Pop click, Typing/Keyboard typing, Cartoon/Comedy and Voice/Meme meme, Camera camera, Music sting/Logo impact, Riser/Build riser, Texture/Ambience ambient), refined by file-name/description keywords, `use` from Best use, then (Other, or no CSV) from features (long rising energy: riser; short broadband transient: click/pop; low sharp thump: sub-hit; ...). Guesses stay `tags_from: "draft"` until Claude corrects them with `veos sfx tag`.

**Timeline cue**: `{"t": edit s where the anchor lands, "id": catalogue id, "db"?: peak dBFS (default by role: impact -14, sub-hit -16, whoosh/swish -22, pop/click -26, shine/chime -24, riser -20, meme -12, others -24), "beat": id, "on": "<scene id>@<local s>|stage@<t>|camera@<t>|transition@<t>", "why": "short reason"}`. Cues with only `file` are legacy (checked by M10/M9 only).

**Playbook tokens** (all optional): `sound.palette_vibes` (default from `tone.energy`: calm -> calm, premium, organic; premium -> premium, calm, techy; playful -> playful, comedic, premium, techy; hype -> hype, premium, techy, playful, tense; plus comedic when `tone.meme_sfx`), `sound.allowed_roles`, `sound.banned_roles`, `sound.silence_before_cta` (default true), `sound.dry_hook` (default false), `budgets.sfx_per_10s` (default 6), `budgets.sfx_max_uses_per_file` (default 2).

**Rules** (`sfxrules.py`; plain-English message + `fix`):
- **S1 tied to picture.** `on` must resolve to a real event: a scene's `t_in` / `t_out` (`@0`, `@in`, `@out`) or a declared `events` time (`<scene>@<local s>`), or a `stage`, `camera` or `transition` entry; the cue `t` must be within +-3 frames of that event. No orphan sounds.
- **S2 vibe match.** The sound's `vibe` must intersect the playbook palette AND suit the beat tone: mock -> comedic/playful; warn -> tense; awe -> premium/calm; explain -> techy/calm/premium; hype -> hype/premium; win -> premium/playful; cta -> premium/calm. A `meme` role (or `use: comedy`) needs `tone.meme_sfx` and a mock beat.
- **S3 palette.** `sound.allowed_roles` / `sound.banned_roles`.
- **S4 restraint.** At most `sfx_per_10s` in any 10 s window; no two cues within 0.25 s unless a sub-hit under an impact; nothing in the 1.0 s before the first word of the CTA section (`silence_before_cta`); nothing in the hook when `dry_hook`.
- **S5 ledger.** No file more than `sfx_max_uses_per_file` times, except one list-cue file (tagged `use: list-cue`, at most one use per ITEM section); never the same file on consecutive cues. (Replaces M10 for catalogue cues; M10 and M9 keep working for legacy `file` cues.)
- **S6 catalogue.** Every id exists in `catalog.json` and is not `excluded` (failures); draft tags give a warning only.

**Mix gate.** `veos sfx --project P` then `veos mix voice.wav out.wav --dur D --sfx work/sfx.wav` (as before). The mix fails with `SFX_TOO_LOUD` when the median SFX level (400 ms windows where the voice is above -40 dB) is not at least 20 dB under the voice, or any non-sub-hit cue is within 6 dB of the voice while speech is present. `veos storyboard` mixes the SFX into the animatic voice (`review/mockup/voice.m4a`) so the creator hears them before approving; the beat cards list them as `id - why`.
