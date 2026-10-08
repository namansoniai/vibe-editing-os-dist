# Renderer contract v2 (scenes): timeline.json + scenes.js

**Owner:** Opus. Implementations follow this document.

**Architecture decision:** there is **no component library**. The renderer is a skeleton (core.js). For every reel Claude writes bespoke visual code, *scenes*, in `plan/scenes.js`, guided by the creator's playbook (`playbooks/<id>/`). This is the original procedure (PROC Appendix E: reuse the core, write new scenes per reel). The ctx toolkit and scene fields are in `SCENES-API.md`.

## 1. Pipeline
```
engine outputs (cutmap.json, words.edit.json, face/*.json, matte/*.mp4, sources.json)
   + plan/timeline.json   (planner: beats, stage, world, camera, captions, sfx, audio)
   + plan/scenes.js       (planner: VEOS.scene({...}) calls; classic script)
   + plan/assets/*        (optional images for scenes: ctx.asset("<stem>"))
   → veos tokens          (playbooks/<id>/tokens.json [+ plan/tokens.override.json] → work/tokens.json)
   → veos scenes-meta     (headless: registered scenes' metadata → plan/scenes.meta.json)
   → veos measure         (headless: per-scene rendered rects, sampled → plan/measure.json)
   → veos validate        (timeline + scenes.meta [+ measure] + playbook rules → failures with beat ids and fix hints)
   → veos prep-frames     (per edit frame n: work/frames/f%05d.jpg footage + c%05d.webp RGBA cut-out; face boxes)
   → veos bundle          (node --check plan/scenes.js; work/render/bundle.js)
   → veos render --html renderer/player.html --query bundle=<url>
```
- `player.html` loads `core.js`, the bundle (timeline, resolved tokens, words, face, asset URLs) and then `plan/scenes.js`.
- Every frame is a pure function of `n`: `t = n / 30`.
- `timeline.inputs.{cutmap,words,face,frames}` may be project-relative or absolute paths.

## 2. timeline.json (top level; no `layers`)
```json
{
  "version": 2,
  "meta": {"size": [1080,1920], "fps": 30, "out_fps": 30, "duration": 52.4, "frames": 1572, "playbook": "naman", "title": "…", "keyword": "SCALE", "count": 3},
  "inputs": {"cutmap": "work/cutmap.json", "words": "work/words.edit.json", "frames": "work/frames/", "face": "work/face.edit.json"},
  "assets": {"logo_claude": {"type": "image", "src": "assets/logos/claude.svg"}},
  "beats": [ {"id": 1, "section": "HOOK", "t0": 0.0, "t1": 1.55, "spoken": "…", "trigger": {"word": "website", "at": 0.62},
              "tone": "mock", "mode": "HOOK", "line_type": "roast", "layers": ["banner", "slop-card"],
              "visual": "Slab banner 'Your site vs MINE'; garbage browser card behind the speaker, shatters on 'website'", "notes": ""} ],
  "stage":   [ {"t": 0.0, "layout": "full"}, {"t": 7.4, "layout": "panel", "via": "panel-drop"} ],
  "world":   [ {"t": 0.0, "world": "studio"}, {"t": 7.4, "world": "canvas"} ],
  "camera":  [ {"t": 0.2, "preset": "rotation-snap"}, {"t": 1.62, "preset": "shake", "p": {"amp": 10}} ],
  "captions": {"subtitles": "auto", "hide": [[0.0, 7.4]], "overrides": []},
  "transitions": [ {"t": 2.10, "id": "light-sweep"} ],
  "sfx":     [ {"t": 1.62, "id": "impact-cinematic-03", "db": -14, "beat": 1, "on": "camera@1.62", "why": "crash-zoom on the roast"} ],
  "audio":   {"bed": null, "bed_db": -22, "dropouts": [[31.2, 31.9]]}
}
```
**Rules:**
- All times are **edit time in seconds**; the renderer converts to frames with `round(t * 30)`.
- `beats[].layers` = the **scene ids** shown in that beat. `beats[].visual` = one human sentence describing what the viewer sees (the storyboard shows it; the beat table is the human review surface).
- `stage.layout` is an engine layout (`full | low | panel | inset | slide-aside | bubble | hidden`, and E-07 `card | stack | pip | letterbox | blurfill`) or a `tokens.layouts` id whose `engine` is one of them. `low` = full-frame footage lowered by `offset` px (default 380) to make room above the head; the revealed top shows the frame scaled x1.15, blurred 40 px at 45% brightness. `behind` scenes are NOT lowered. `via` names the morph (`cut | panel-drop | pop-back | slide-aside | bubble-shrink | bubble-grow`, E-07 `shrink-to-card | grow-from-card | slide-down | slide-up | pip-shrink | pip-grow | morph | dim | fade-through`); the stage interpolates between consecutive layouts over the `via` duration (`dur` frames, `ease` optional, `overshoot` 0-0.3: a back-out peaking that far past the target). Layout params (card rect/radius/crop/border, stack seam/top/bottom/hairline/fade, pip shape/d/corner/ring, letterbox/blurfill band, `dim {blur_px, luma}`) come from the token layout, `p` and inline keys; table and default moves: SCENES-API section 4a. Unknown layout ids fail the player boot with the known ids listed. Validator: V-LAYOUT.
- `world` is any `tokens.worlds` id (or the v1 `studio | canvas | data`, always defined); it decides what is drawn behind a non-full stage. `{"t", "world", "fade": s}` cross-fades. Theme packs recolour worlds at `veos tokens` time. Unknown ids fail the boot.
- **`canvas_camera`** `[{t, move, to?, dur?, ease?, p?}]` (E-14, structure §21): a camera over the graphics world: moves `C-1 push`, `C-2 pull`/`settle`, `C-3 pan`/`drift`/`dolly`, `C-4 zoom-through`, `C-5 orbit`; targets are `canvas_nodes` (`{id: {x, y, w, h}}`, world px), scene `nodes`, or `{x, y, s}`; `canvas_home` sets the resting view. It transforms scenes z1-6 by their `parallax` and never captions, chrome, z7+ or `behind` scenes. The maths is `renderer/canvascam.js` (mirrored in `engine/src/veos/canvascam.py`); the validator rule is V-CANVAS. Details and examples: SCENES-API section 4b.
- **Voice-over reels** (E-12): when every cut-map span comes from a voice-over source, the bundle carries `footage: false`, the stage is `hidden` throughout (core forces it), no footage frames or face boxes exist and `ctx.face()` is `null`. Write `"stage": [{"t": 0, "layout": "hidden"}]` anyway; build every frame from scenes (SCENES-API section 10).
- `camera.preset` is a playbook camera preset id (snap-punch, crash-zoom, pull-out, push-drift, shake, zoom-through, rotation-snap, reset). It transforms the footage group, cut-out included, around the face point. Validator: no identical preset twice in a row. Camera v2 (SCENES-API 4c): `ease`, `rotate [from, to]` / `from_rotate`, `origin` / `toward`, `from` (`inherit`), `from_wide`, `land`, `crop` (an event may be `{t, crop}` alone: an instant re-crop on a cut), `target: all`; front scenes with `follow_footage` ride the camera. Canvas camera: `p.roll`, `p.snap`, eases `expoInOut` / `expoOut`.
- **Captions** are generated by the caption profile engine (E-05: `engine/src/veos/capengine.py` -> `work/captions.json` and the bundle's `captions`, drawn by `renderer/captions.js`) from `words.edit.json` and the playbook's caption profiles (tokens.schema §3.8). A v1 playbook gets the legacy profile: 2-3 words per card, exactly as before. Hidden inside `hide` ranges, during stage morphs and, per profile, under z8 scenes, in the hook, around transitions or E2 bursts. `captions.profile` picks the reel's profile; `captions.overrides` fix text (`{from, to}`, `{t, text}`), force breaks, switch emphasis on or off, switch the profile, or hide or set the caption centre (`{t: [a, b], cy}`) for a time range; `captions.hide_on_morph: false` keeps captions through stage morphs for one reel. Swap types (`flicker`, `wipe`, `smear`), `reveal: char`, `line_fit` and `connector_container_when`: SCENES-API section 4 (caption swaps, reveals and placement). **The planner never writes caption cards by hand** (V-CAPTION fails `captions.cards` / `captions.chunks`).
- **Grades** (E-16, `renderer/grades.js`): optional `timeline.grade` (this reel's base grade: a `tokens.grades.scene` id, a CSS filter list, a grade object or `"off"`) and `timeline.grades: [{t, t1 | dur, grade, fade, freeze}]` (events over the base). The grade is part of the footage layer (frame, cut-out, breakout, backdrop copies), never the graphics. Precedence: scene `grade` > world `grade` > `timeline.grade` > theme `grade` > `tokens.grades.footage`. Unknown ids fail the boot.
- **Framing** (E-16b, `engine/src/veos/framing.py`): `veos bundle` computes one base reframe per reel from `tokens.footage.setups[].framing` and the face boxes (`bundle.framing: {s, tx, ty, setup, face, ranges, capped, residual_px}`); core applies it on `full` / `low`. `timeline.framing: "off" | {"setup": id} | {ranges}`. Multi-camera reels (`shots`) are not reframed.
- `transitions` without a `type` are markers only (timeline events for M7 and storyboard strips). **With a `type`** (`flash | leak | blur-through | zoom-blur | whip | glitch | burn | iris | curtain | push`; `{t, type, frames, pre, layers, ...}`) core draws a built-in transition over the composited picture (`renderer/transitions.js`; captions stay on top unless `layers: "all"`). Also drawn by core: the **footage blur** (`timeline.blur[]`, camera `blur`, preset `blur`: defocus / directional / radial envelopes on the stage only), grade-event **blur pulses** (`timeline.grades[].blur`, `frame: true` = the whole picture) and **`end_fade`** (frames to black). Fields and examples: SCENES-API section 4c. Validator: V-FX (no flash limit).
- **`sfx` cues** `{t, id, db?, beat, on, why}`: `id` is a sound from the shipped `assets/sfx/catalog.json` (`veos paths` -> `sfx_catalog`; the audio itself is downloaded on demand into `sfx_pack`); `t` is the **edit second where the sound's anchor** (peak for hits/whooshes, onset for clicks/pops, end for risers) **lands**; `db` is the peak dBFS (default by role: impact -14, sub-hit -16, whoosh -22, pop/click -26, shine/chime -24, riser -20, meme -12); `on` ties it to a real visual moment: `"<scene id>@<local s>"` (a scene start/end or a declared `events` time), `"stage@<t>"`, `"camera@<t>"` or `"transition@<t>"`; `why` is a short reason shown on the storyboard card. Every sound must match the playbook's vibe and sit on a picture event (validator S1-S6, section 5). The renderer ignores `sfx`; `veos sfx --project P` builds `work/sfx.wav` from it and `veos mix --sfx` mixes it. Legacy `{"t", "file", "role", "beat"}` cues still validate through M10/M9.
- **`shots`** (multi-speaker reels only; engine SPEC §7): which camera/crop shows each span. The engine composes them into the footage frames (`veos shots render` → `prep-frames`), so the stage stays `full`; core reads `shots` only to put captions on the seam of `stack` shots. Such reels have no cut-out layer (no `behind` scenes).
- **`captions.speakers`** `{<speaker id or role>: {colour (hex or role), style: upright|italic}}`: per-speaker caption styles; words carry `speaker`/`role` (`veos speakers`). Cards never mix speakers.
- `beats` carry the planning semantics (tone, trigger, line type) used by the validator and the storyboard; the renderer ignores them.

## 3. Scene API (`plan/scenes.js`)
**Classic script, not an ES module** (Chrome blocks module imports over `file://`). Top-level helper functions are allowed; each visual is one `VEOS.scene({...})` call. Fields:

| field | meaning |
|---|---|
| `id` (required, unique) | referenced from `beats[].layers` |
| `t_in`, `t_out` (required) | edit-time seconds; the scene is gone at `t_out` |
| `z` (required, 1-11) | 1 background, 2 glow, 3 cards/data, 4 speaker, 5 labels, 6 markers/badges, 7 subtitles, 8 big captions, 9 comedy, 10 banner, 11 light passes |
| `behind` | between footage and the person cut-out (depth sandwich); only valid when the stage shows footage |
| `in`, `out` | core presets: `settle \| pop \| squash \| rise \| drop \| blur \| stamp \| slide-l \| slide-r \| rocket \| none` (default in `settle`, out `none`) |
| `box` | declared footprint `{x,y,w,h}` in 1080x1920 px (also the preset transform origin, and the rect for canvas-only scenes) |
| `roles` | bright colour roles used (validator: at most `max_bright_per_frame` per frame) |
| `events` | local seconds (after `t_in`) of internal visual changes; counted for M7 and M6 |
| `text`, `text_content` | `text: true` if it carries text (safe-zone check); `text_content` = the text shown, one string |
| `may_overlap_face` | exempt from the face-clearance check |
| `overlaps` | `["B", ...]` scene ids (or `"__subtitles"`) this scene is deliberately nested on; exempts the pair from global check G1 |
| `cuts` | `[s, ...]` LOCAL seconds of deliberate hard cuts; exempts them from global check G3 |
| `ian_frames`, `chout_frames`, `step_frames` / `step_fps`, `smear` | per-sPacenkage pE: `{treack, offset, lepoingths (0-60 frames), scale_witeppedh, "smonoth, twlos" drawing (1-6t, frames per posde, min_cornf, 5-3max_lost, clip_t0, fsps; G3 jueedges, placer pose), directional smear on}`: the pbox centreset follows a `plan/tracks/<id>.json` track (fx-h`velpeos trsack`; SCENES-API section 213). Needs `box`; exclusive with `follow_footage` |
| `smear_px`, `in_fade` | fix-visual: the velocity smear's cap (0-48 px; default the style's `motion.smear_push.motion_blur_px`, else 24). Travel presets (`slide-l` / `slide-r` / `rocket`) arrive opaque by default; `in_fade` is a rare override. SCENES-API section 2 |
| `parallax`, `nodes`, `text_px`, `text_class` | canvas camera: how much the scene moves with it (0..1 / false), the camera targets it provides, and its smallest font-size + text class (V-CANVAS) |
| `kind` | optional: `"banner"` (M1, M4, M13 headline), `"cta-keyword"` (M13 keyword check), `"meme"` (M9) |
| `chips`, `lines` | banner only: `[{text, role}]` keyword chips, number of lines (M4) |
| `render(ctx, lt, dur)` | returns an HTML string (`return ctx.html(...)`) or draws on `ctx.canvas()` and returns `""`. `lt` = seconds since `t_in`, `dur` = `t_out - t_in` |

**Rules for scenes:** pure functions of `(ctx, lt, dur)`. No `Math.random`, `Date`, timers, `<video>` or network fetches (use `ctx.rng(seed)`). Use `ctx.tokens` colours/fonts, never hard-coded hexes for role colours. Registration errors (bad fields, duplicate id, syntax) are reported with the scene id by `veos scenes-meta` and fail the player boot.

Core wraps each scene's output in `<div data-scene="ID">` (position 0,0, 1080x1920) and applies the enter/exit preset to that wrapper.

## 4. Built into core.js (+ canvascam.js before it, fx.js after it)
- `canvascam.js`: the canvas-camera maths (`window.VEOS_CANVASCAM`; also `require()`-able by node). `fx.js`: the `VEOS.fx` toolkit (kinetic type, diagrams, cards, clips, morphs, ambient worlds; SCENES-API section 10). `inserts.js` (after fx.js): the created-substitute toolkit for third-party moments (quote, headline and citation cards, recreated generic UI, logo plates set in type, silhouettes, the creator's screenshot frame, credit lines; SCENES-API section 11). `fx3d.js` (after fx.js, on `vendor/three.min.js` = three.js r186, MIT, global `THREE`) provides `VEOS.fx.three`: lit 3D objects rendered with WebGL (SwiftShader in headless Chromium) into a transparent canvas scene (SCENES-API section 13). All ship with the renderer and load from `player.html`.
- `layouts.js` (`window.VEOS_LAYOUTS`, `require()`-able): stage layout resolution, geometry, morph interpolation and `ctx.layout()` info. `worlds.js` (`window.VEOS_WORLDS`): world markup from `tokens.worlds` + the v1 mapping. Both load before `core.js` in `player.html`.
- The stage (7 v1 layouts + card, stack, pip, letterbox, blurfill, the dim treatment, morphs) and the camera presets (+ shake, banner clamp). v1 reels render byte-identically.
- Worlds (`tokens.worlds`; v1 studio/canvas/data), auto-subtitles, the footage + cut-out layers, vertical motion blur.
- `ctx.layout()` / `VEOS.layout(n)`: `{id, engine, morph, rects {presenter, card, pip, band, top, bottom, cells, graphic}, seam_y, anchors {seam, below_card, above_card, inside_footage}, caption}` for scenes and the caption engine (anchors `seam`, `below_card`, `inside_footage` by layout id).
- Font loading and the glyph/emoji warm-up, `READY`. `window.measureFrame(n)` for `veos measure` (layout only: no footage decode, no paint wait; the auto-subtitles are wrapped in `data-scene="__subtitles"` and measured under that id). `window.measureText(n, {pixels, chars, items})` for the text pass (E-06): every painted text element of the frame at its resting position (rendered size incl. transform scale, weight, colours, container, lines, clipping, `data-tc` / `data-redundant` / `data-slot` / `data-item` markers) plus the footage->screen geometry; with `pixels` the footage and cut-out are decoded so the engine can screenshot the frame with glyphs hidden (contrast) and sample the cut-out alpha (E1 occlusion).
- `ctx.videoFrame(name, seconds)` for video assets (bundle key `videos: {name: {frames, fps, w, h, duration, base_url}}`; frames are `base_url + f%05d.jpg`, zero-based, decoded before the frame is ready). `plan/assets/<name>/` with a `meta.json` is a video asset (made by `veos asset add`).
- The cut-out is only decoded when a `behind` scene is visible.
- `tracks.js` (`window.VEOS_TRACKS`, `require()`-able; loads before core.js): object tracks from `bundle.tracks` (`veos bundle` compacts `plan/tracks/*.json`, edit tracks in footage px) and the scene-anchor maths (mirrored in `engine/src/veos/anchors.py`). Core wraps an anchored scene in a translate + scale about its box centre (opacity for `lost: fade`), mapping edit tracks through the live footage->screen transform; `ctx.track(id)`. `follow_footage` on a front scene wraps it in the footage matrix. An unknown `anchor.track` fails the boot.

## 5. Validator (`veos validate`)
- **Inputs:** timeline, `plan/scenes.meta.json` (auto-rebuilt when missing or older than scenes.js), `plan/measure.json` (preferred over declared boxes), face boxes, playbook tokens (`budgets`, `layout`, `rules_v0`).
- **Two levels** (directions, not limits; `playbooks/_global/GLOBAL-RULES.md`): `failures` are facts and block the reel (G1, G3, the face, readable text, true numbers and quotes, the promise count, the plan, broken fields, an unknown sound, a missing cut-out); `advice` (same shape) is direction for the Director and never blocks.
- **Output:** `{"ok": true, "passed": false, "advice": [...], "failures": [{"rule": "V-CADENCE", "playbook_rule": "M7", "beat": 12, "t": 18.4, "msg": "...", "fix": "..."}], "warnings": [...], "stats": {...}}`. `rule` is the stable registry id (engine/SPEC.md section 7); `playbook_rule` is the playbook's own id when it cites the rule.
- **Sound rules S1-S6** run whenever `timeline.sfx` holds cues with an `id` (not part of `rules_v0`): S1 tied to picture (`on` resolves to a real event, cue within +-3 frames of it), S2 vibe match (catalogue vibe vs playbook palette and beat tone; meme only on mock beats with `tone.meme_sfx`), S3 palette (`sound.allowed_roles` / `banned_roles`), S4 restraint (`budgets.sfx_per_10s`, 0.25 s spacing, silence before the CTA, `sound.dry_hook`), S5 ledger (replaces M10: max 2 uses per file, one list-cue exception, no consecutive repeats), S6 catalogue (id exists and is not excluded; draft tags warn). Details: `engine/SPEC.md` section 6.
- **Global checks G1 no overlap, G2 no clutter, G3 smooth motion** run for every playbook (not part of `rules_v0`), from `plan/measure.json` + `plan/measure.motion.json` (details in SCENES-API section 7b). `stats.global_checks` counts their failures. G3 compares rects with the canvas camera removed (camera travel is V-CANVAS's job).
- **V-ANCHOR** runs whenever a scene declares `anchor` (`veos.anchors.rule_v_anchor`; counted in `stats.global_checks["V-ANCHOR"]`): track exists, covers the scene, confidence (`max_lost`, no long `hold` on a lost object), no anchored overlay on the face. Anchored scenes are exempt from G3.
- **V-PLAN** (`veos.sceneplan`; counted in `stats.global_checks["V-PLAN"]`): `veos validate --plan` judges `plan/scenes.plan.json` + `plan/scene-briefs.md` before any code (completeness, plus every rule on the declared boxes); plain `veos validate` with a scene plan present fails every difference between the registered scenes and the plan.
- **V-CANVAS** runs whenever the timeline has `canvas_camera` moves (`veos.canvascam.rule_v_canvas`; counted in `stats.global_checks["V-CANVAS"]`).
- Playbook rules come from the rule registry v2 (V-F0, V-CADENCE, V-TITLE, V-ONWORD, V-SAFE, V-FACE, V-CAMERA, V-HUES, V-LEDGER, V-COMEDY, V-PROMISE, V-PRESENCE, V-PROFILE). The reference playbook's ten rules M1, M7, M4, M6, M12, N5-zoom, N6, M10, M9, M13 are aliases of them and behave exactly as before. Component ids are not referenced anywhere; scene `kind`s with meaning: `banner` and the other headline kinds, `cta-keyword`, `meme`, `end-card`, and the hook-archetype kinds listed in `engine/src/veos/hookrules.py` (or `satisfies: [...]`).
- M12 uses **measured** rects per sampled frame (the safe zone for `text` scenes, the face clearance for z>=5 non-behind scenes); without `measure.json` it falls back to declared boxes.

## 6. Tokens
`veos tokens --project P` resolves `playbooks/<id>/tokens.json` (the creator's colours by role, font slots, type, layout, motion, camera_presets, stage_morphs, budgets, tone) plus optional `plan/tokens.override.json` (`{colours, fonts, tone, patch}`) into `work/tokens.json`. The playbook id comes from `project.json` `playbook` (set by `veos project init` from the folder workspace, no default; old `style`/`brand` keys are ignored).
- Only `brandable` roles may be overridden; fixed-meaning roles (`bad`, `good`, `comedy`) are ignored with a warning.
- Brandable colours are contrast-checked against `text_on` (>= 4.5:1, or 3:1 for large-text-only roles) and nudged in OKLCH lightness if they fail; adjustments are listed in `warnings`.
- Patches touching safe zones, fixed meanings or loudness are rejected.
- Output: `{"version": 2, "playbook", "creator", "colours", "text_on", "fonts", "type", "layout", "motion", "camera_presets", "stage_morphs", "tone", "budgets", ..., "warnings"}`.
