# Edit reference: the mechanics

Look things up here; the creative decisions live in SKILL.md and the playbook. `P` = the project folder (`.../vibe-edit`).
Every `veos` command takes `--project "P"`. Times are edit seconds; frame = round(t × 30); the canvas is 1080×1920 at 30 fps.

**Shell.** Commands work in PowerShell and in Bash: quote every path, and nothing else is shell-specific unless shown
twice. Setup puts `veos` on the user PATH (terminals opened after the install know it). If `veos` isn't recognised,
call the wrapper by its full path: `<plugin root>/bin/veos.cmd` on Windows (in
PowerShell: `& "<plugin root>\bin\veos.cmd" ...`), `bash "<plugin root>/bin/veos" ...` elsewhere (works even if the file lost its run permission). The plugin root is two folders
above this skill's base directory. Long jobs (matte, storyboard, render) go in the background with the shell tool's
background option; you're told when they finish.

**Files.** Write and change every file with the Write and Edit tools, not PowerShell `Out-File`, `Set-Content` or
`ConvertTo-Json`: you see exactly what lands on disk. Never write helper scripts to patch the plan; edit the file.

## 1. See and hear the cut
- `veos look` → `P/review/look/sheet_NN.jpg` (frames picked by meaning, labelled with time and words) + `look.json`
  (shot size, face box, motion per second, cuts). Close looks: `veos look --at 12.4-13.6` (≤ 2 s) or `--at 3.1,7.9,15.2`.
- `veos context --part all` → setups, face ranges and the free bands per setup, and the words in edit time as
  `i:word@t` (`?` = low confidence) with pauses ≥ 0.3 s marked.
- Footage frames and face boxes (the reel skill makes them after the cut; re-run if missing or the cut changed):
  `veos faces`, then `veos prep-frames`. Both are cached and quick.

## 2. Captions
Captions are automatic: the engine builds them from the words and the playbook's caption profile, avoids the face where
the profile says so, and hides them during stage morphs. You fix the text, never draw caption cards.
- `veos captions status` → words, how many have a caption, Devanagari and low-confidence words without one.
- Write `P/work/captions.map.json` = `{"<i>": "text"}` for the words that need it (index from `veos context`), then
  `veos captions apply "P/work/captions.map.json"`. `""` hides a word (a duplicated fragment). Never merge or split
  indices; fix spelling, never what was said; brand and tool names exact; case and script as the playbook says.
- Romanised Hinglish: every Devanagari word gets its romanised caption, one-to-one.
- Telugu, Tamil and other non-Devanagari words keep their own script; for romanised captions write a `{i: text}` map and
  `veos captions apply`; `captions status` shows `regional_script_no_caption`.
- Hinglish speech with English captions (`captions.transform: translate` in the tokens): write
  `P/plan/captions.script.md`, the English of what they say, one sentence per line in spoken order.
- Placement per moment: `timeline.captions.hide: [[t0, t1]]`, `captions.overrides: [{"t": [t0, t1], "cy": 1300}]`, or a
  scene's `caption_cy` (SCENES-API §4).

## 3. Things from the web
- Find with WebSearch, read a page with WebFetch (the exact headline or post text, the image URLs on it).
- Download straight into the project: `curl -L -o "P/plan/assets/<name>.<ext>" "<url>"` (in Windows PowerShell type
  `curl.exe`; `curl` there is another command). PNG, JPG, WEBP, SVG. Read the image afterwards to check it's the right
  thing and not an error page.
- Every image in `P/plan/assets/` is available as `ctx.asset("<name>")` (file stem or full name). A video clip: download
  it anywhere in `P`, then `veos asset add "<file>" --name <name>` → `ctx.videoFrame("<name>", lt)`.
- Record where a fetched file came from: `veos asset add "<file>" --name <n> --source "<url>"` (origin `fetched`). A line
  per file in `P/plan/fetched.md` (`<name> ← <url> (what it is)`) is optional.
- A screenshot of a web page: `veos capture "<url>" --out "P/plan/assets/<name>.png" [--selector "<css>"] [--full-page]`
  (`--selector` frames one element: the post, the headline, the pricing table), then `asset add` it with `--source`. Or
  rebuild the post or page in a scene from its exact text and its fetched images (`fx.quoteCard`, `fx.headlineCard`,
  `fx.shot` on an image; SCENES-API §12).
- The creator's own files: `veos asset add "<file>" --name <name>`.

## 4. `P/plan/timeline.json`
Full contract: `CONTRACT.md` §2 (next to `SCENES-API.md`) and SCENES-API §4. The skeleton:
```json
{"version": 2,
 "meta": {"size": [1080, 1920], "fps": 30, "out_fps": 30, "duration": 41.37, "frames": 1241, "playbook": "<id>",
          "title": "<the hook title>", "title_alternatives": ["<2nd>", "<3rd>"], "keyword": null, "count": 3},
 "inputs": {"cutmap": "work/cutmap.json", "words": "work/words.edit.json", "frames": "work/frames/", "face": "work/face.edit.json"},
 "assets": {},
 "beats": [{"id": 1, "section": "HOOK", "t0": 0.0, "t1": 2.4, "spoken": "…", "trigger": {"word": "website", "at": 0.62},
            "tone": "mock", "layers": ["hook-slab", "bad-site"], "visual": "Their sad site under a red marker; the slab slams in"}],
 "stage": [{"t": 0, "layout": "full"}],
 "world": [{"t": 0, "world": "studio"}],
 "camera": [], "transitions": [], "captions": {"subtitles": "auto", "hide": [], "overrides": []},
 "sfx": [], "audio": {"bed": null}}
```
- `meta.duration` and `meta.frames` are the cut's (`P/work/cutmap.json` → `duration`, `frames`), exactly.
- Beats tile 0 → duration with integer ids; `layers` = the scene ids on screen in that beat; `visual` = one sentence of
  what the viewer sees (the storyboard shows it). Section names are yours (`HOOK`, `ITEM-1`…, `PAYOFF`, `CTA`); a `CTA`
  section gets its own storyboard strip.
- Stage layouts, worlds and camera presets are ids from the playbook (its tables) and its `tokens.json` (`layouts`,
  `worlds`, `camera_presets`), or the engine's own (SCENES-API §4, §4a, §4c). An unknown id fails the player.
- Every `transitions[]` entry has an `id` (`{"t": 7.4, "id": "t-shatter", "type": "flash", ...}`); the storyboard needs it.
- Moves the engine draws for you: stage `via` morphs, `transitions[].type`, footage `camera`, `canvas_camera`, `blur`,
  `grades`, `end_fade` (SCENES-API §4–4c). Moves inside the graphics are scenes (`fx.morphShape`, `fx.handoff`,
  `fx.shatter`, `fx.streak`, or your own).
- Per-reel token tweaks (a caption centre, a colour): `P/plan/tokens.override.json`, same shape as the playbook's tokens.

## 5. `P/plan/scenes.js`
SCENES-API is the whole reference. The points that bite:
- A classic script: helpers at the top, then one `VEOS.scene({...})` (or `VEOS.fx.*` / `VEOS.data.*` factory) per scene.
  Every scene id appears in some beat's `layers`.
- Pure functions of `lt` / `ctx.n`: no `Math.random`, `Date`, timers, CSS animations, `<video>` or `fetch`. Colours
  through `ctx.col(role)` / `ctx.hexA`, fonts through `ctx.fam(slot)`, images through `ctx.asset`.
- `behind: true` puts a scene between the footage and the person (it needs the cut-out, §7). Declare every visible change
  in `events` (local seconds): sounds anchor to them. `text: true` + `text_content` on every scene with words (the
  storyboard lists it).
- Write it in steps: the first Write holds the helpers and the hook's scenes and ends with the line
  `// ==== next section ====`; each later section is one Edit that replaces that line with the new scenes followed by
  the same line again. The file on disk is always valid up to the marker, so an interrupted edit resumes from it.
- When every section is in: `veos scenes-meta` loads the file in the real player and names the scene behind any syntax
  or registration error. Fix and run it again until it's clean. Numbers drawn by `VEOS.data` helpers need
  `P/plan/figures.json` (SCENES-API §11) and `veos figures`; your own counters don't.

## 6. Sound
- What exists: `SOUNDS.md` in this folder (every usable sound: id, length, vibe, what it sounds like, best use). The
  playbook's sound section and `tokens.json` → `sound` (`preferred` ids per use, vibes, roles) are its own palette.
- A cue in `timeline.sfx`: `{"t": 3.27, "id": "<id>", "beat": 2, "on": "<scene id>@<local s>", "why": "card lands"}`.
  `on` is a scene's start (`@0`), an `events` time, its end (`@out`), or `stage@t`, `camera@t`, `transition@t`.
  `t` is where the sound's own anchor lands (the peak of a hit or whoosh, the onset of a click or pop, the end of a riser):
  put it on the frame the picture lands.
- Levels default by role (impact −14 dB, sub-hit −16, riser −20, whoosh −22, shine/chime −24, pop/click −26, meme −12);
  `"db"` overrides one cue. The final mix fails `SFX_TOO_LOUD` when cues crowd the voice: lower those cues.
- An unknown id, a do-not-use id, or `SFX_DOWNLOAD_FAILED` for one file: swap in another sound of the same role.

## 7. The person cut-out (talking head)
Needed only when a scene is `behind: true` or a card / pip layout lets the head break out (`breakout`). If the playbook's
`tokens.json` says `"matte": "required"` the reel skill already started `veos matte` after the cut. Otherwise, after
`veos scenes-meta`: `veos matte --if-needed` (it answers `skipped` with the reason when nothing needs it; when it runs it
takes minutes, so run it in the background and tell the user in one line). When it's done, `veos prep-frames` adds the
cut-out frames. Never two heavy jobs at once: no storyboard or render while a matte runs.

## 8. The storyboard and looking at it
1. A `veos matte` still running in the background: wait for it. Then delete the old animatic frames: PowerShell
   `if (Test-Path "P\review\mockup\anim") { Remove-Item -Recurse -Force "P\review\mockup\anim" }`, Bash
   `rm -rf "P/review/mockup/anim"`.
2. `veos prep-frames` (cached; adds the cut-out frames when a matte exists), then `veos storyboard` (it refreshes the
   tokens and the bundle itself; a minute or two) → `P/review/mockup.html`, `review/mockup/anim/a_NNNN.jpg` (5 fps), `still_NNNN.jpg` (a key frame per beat, 540×960),
   `strip_NNNN.jpg` (frame-by-frame strips of every move; which frames belong to which move: `P/plan/storyboard.config.json`
   → `strips`).
3. Watch sheets: `veos sheet "P/review/mockup/anim" "P/review/watch/reel" --per 25 --cols 5 --tile 216` →
   `review/watch/reel_0.jpg`, `reel_1.jpg`… Each row is one second, each sheet five.
4. A moment at full size: `veos stills --at 4.9,14.9` (or `--scenes a,b` for those scenes' moments) →
   `review/stills/sheet_NN.jpg`.
5. Open the page for the user: PowerShell `Start-Process "P\review\mockup.html"`, macOS `open "<path>"`, Bash on Windows
   `powershell -NoProfile -Command "Start-Process '<path>'"`. If it won't open, give the path.

## 9. Tools for when something looks broken (never a gate, never a loop)
- `veos measure --every 10` then `veos validate`. It blocks only a broken build (`failures`: V-PLAN, V-FX, S6,
  V-CUTOUT); everything else is advice (overlaps, jumps, unreadable text and more: 3 per rule in the summary, all of
  them in `P/plan/validate.json`). Fix a failure; read the advice for what explains the problem you saw and ignore the
  rest. Never loop on it.
- `veos track` for a graphic that must follow a moving object (SCENES-API §13).
- Engine crash or missing tool: `veos doctor` once, say plainly what failed, suggest `/vibe-editing-os:setup update`,
  stop. Never patch the engine or re-encode video yourself.

## 10. Other kinds of reel
- **Faceless (voice-over):** `"stage": [{"t": 0, "layout": "hidden"}]`, no faces, no cut-out; every second is built from
  scenes on a world (`fx.ambient`, `fx.typeStack`, `fx.diagram` with the `canvas_camera`, `fx.card`, `fx.clip` for their
  own B-roll; SCENES-API §10).
- **Conversation (2+ people, `P/work/angles.json` exists):** once the timeline is written, `veos shots plan --apply` adds
  `timeline.shots` (camera / crop per moment; edit them, never rewrite the file without them), and `veos shots render`
  composes the footage before `prep-frames`. Set `timeline.captions.speakers` per role so each voice looks different; no
  `behind` scenes.
- **No voice (`no_voice`):** `"stage": [{"t": 0, "layout": "full"}]` (the footage is the picture),
  `"captions": {"subtitles": "off"}`, no faces, no cut-out. `veos context` → `music` gives `beats`, `bars`, `sections`,
  `hits` and `bar_energy` in edit seconds: key `beats[].t0/t1`, text `at` times, camera moves and transitions to them.
  `work/voice.wav` is the music bed: the render skill's `veos voice` / `veos mix` handle it as music (no voice chain, the
  same −14 LUFS); timeline `sfx` are optional. The three kinds:
  - **B-roll montage:** the footage fills the stage; the cut is the rhythm. Text lands on the beat, in the playbook's
    type; footage `camera` pushes and `transitions` on bar starts; a photo held long gets a slow push. Sounds sparingly:
    the music is already the sound.
  - **Screen-recording walkthrough:** the recording is the picture. Guide the eye: zoom into the part that matters
    (footage `camera` / `canvas_camera` push, then settle), highlight it (a box, an underline, a cursor ring), callouts
    that name each step ("1. Open settings"), blur what's private. A step per bar or two; the result shown big at the
    payoff.
  - **Slides/photos to music:** each photo or slide held for its `dur`, moving (a slow push or pan so nothing is ever
    still), text building on it on the beat; slides keep their own text readable (`fit: blur` in the cut). Transitions
    on bar starts; the last slide holds for the CTA.

## 11. Phases (`veos project set ...`)
`phase=captions` after the captions; `phase=plan` once scenes.js is clean; `phase=storyboard` when the user has the page;
on approval `approved_at=now phase=approved`. On a failure: `last_error="edit: <reason>"`.
