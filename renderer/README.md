# Renderer core v2

Follows `CONTRACT.md`. Pages are classic scripts (no modules), opened over `file://`. There is no component library: Claude writes `plan/scenes.js` per reel (`SCENES-API.md`).

## Run
```
source engine/dev-env.sh
veos tokens       --project P            # playbooks/<id>/tokens.json (+ plan/tokens.override.json) -> work/tokens.json
veos scenes-meta  --project P            # plan/scenes.js -> plan/scenes.meta.json (errors name the scene id)
veos prep-frames  --project P [--range A B]   # -> work/frames/f%05d.jpg + c%05d.webp, work/face.edit.json (cached)
veos measure      --project P [--every 10]    # -> plan/measure.json (rendered rect per scene per sampled frame)
veos validate     --project P
veos bundle       --project P            # node --check scenes.js, then work/render/bundle.js (prints "url")
veos render --project P --html renderer/player.html --query bundle=<url> --frames N [--test 0,30,...]
veos assemble --project P --chunks P/work/render --out out.mp4 --frames N [--audio W]
```

## Demo
`renderer/demo/` is a tiny project: `timeline.json` + `scenes.js` with four bespoke scenes (slab banner, caption pop, painted-canvas phone card, CTA chip). To run it, make a scratch project, copy both into `plan/`, point `inputs.frames` at any prepped frames folder (absolute paths are supported) and copy cutmap/words/face jsons into `work/`. It is an API proof, not a styled reel, so `veos validate` on it reports some rule failures (e.g. M7 gaps, M13 count).

## bundle.js
`window.VEOS_BUNDLE = {timeline, tokens, words, face, frames_url, frames, cuts, scenes:[scenes.js file URL], assets:{id:{type,url}}}`.
`words` = words.edit.json words (a `caption` field, when present, is rendered verbatim; `""` hides the word).
`face` = face.edit.json (1080x1920 px boxes per edit frame). `cuts` = edit frames where a segment starts.
`assets` = `timeline.assets` plus every file in `plan/assets/` (by stem and by file name).

## Files
`player.html` loads `canvascam.js` (canvas-camera maths, shared with the engine's `canvascam.py`), `core.js`, `fx.js` (the `VEOS.fx` faceless toolkit), `inserts.js` (created substitutes for third-party moments, E-10), `vendor/three.min.js` + `fx3d.js` (`VEOS.fx.three`, lit 3D objects; three.js r186, MIT), then the reel's `plan/scenes.js`.

## Built into core.js
- Stage: full / low / panel / inset / slide-aside / bubble / hidden, plus (E-07, `layouts.js`) card / stack / pip / letterbox / blurfill and the dim treatment, by engine name or `tokens.layouts` id; eased morphs over `stage_morphs[via]` frames (`stage[].dur` overrides; the new morphs size themselves to stay G3-smooth). Behind scenes stay un-lowered in `low`. `ctx.layout()` / `VEOS.layout(n)` expose the resolved rects and caption anchors.
- Grades (`grades.js`, E-16): the footage grade (tokens, theme, world, scene, `timeline.grade`) and `timeline.grades[]` events as one SVG filter on every footage image (frame, cut-out, head breakout), under the graphics. Base reframe (E-16b): `bundle.framing` punches `full` / `low` in so the face sits in the template's framing ranges.
- Worlds (`worlds.js`): `tokens.worlds` (solid, gradients, grid, dot grid, glow, texture, noise, vignette, footage backdrop) with optional cross-fades; without them the v1 studio, canvas (token + dashed grid) and data (night + dot grid + drifting glow), which render exactly as before.
- Camera: all `camera_presets` + `reset`, around the smoothed face centre; seeded decaying shake; banner clamp.
- Canvas camera (`timeline.canvas_camera`): C-1..C-5 over the graphics world (z1-6 by `parallax`), `ctx.camera`, motion blur on fast moves; measured rects are on-screen.
- Voice-over reels: `footage: false` in the bundle forces the stage hidden and skips footage frames.
- Auto-subtitles (2-3 words, pause break 250 ms, overrides; the fallback when the bundle has no `captions`), enter/exit presets, `V()`, the ctx API, fonts + glyph/emoji warm-up, `READY`.
- `captions.js` (loaded before core.js): the caption renderer (E-05). It draws the bundle's `captions` chunk list: layout, stage anchors, swaps, word reveal, karaoke, two-tier, duet, kinetic stack, hide rules; the legacy profile reproduces the old subtitles exactly. Hook in core.js: `VEOS_CAPTIONS.init` at boot and `.html(n, {st, world, g, face})` in place of `subtitleHTML`.
- A scene's exit plays in the last frames of `[t_in, t_out)`. The cut-out is only decoded when a `behind` scene is visible.
- Debug: `?bundle=<url>&meta=1` registers scenes only (used by `scenes-meta`); `window.measureFrame(n)` returns `{sceneId: [x0,y0,x1,y1]}` at the resting position (presets neutralised).
