# SCENES-API: how to write `plan/scenes.js`

You write the visuals of each reel as **scenes**: bespoke code on top of the renderer skeleton. There is no component library to pick from; the playbook says *what* to show and when, you decide *how it looks* and paint it. Canvas is 1080x1920 px, 30 fps, every frame a pure function of `n`.

Files: `plan/timeline.json` (beats, stage, world, camera, captions, sfx, audio; no layers), `plan/scenes.js` (this), `plan/inserts.json` (third-party moments, section 11), optional `plan/assets/*` (images; `ctx.asset("<file stem>")` returns a URL). Contract details: `CONTRACT.md`.

## 1. scenes.js layout
Classic script (no `import`/`export`). Helpers first, then scenes. Every beat's `layers: [...]` lists scene ids, and beats get a human `visual` sentence.
```js
function chip(ctx, text, role, size) { /* returns an HTML string */ }
VEOS.scene({ id, t_in, t_out, z, render(ctx, lt, dur) { return ctx.html(`...`); } });
```

## 2. Scene fields
| field | |
|---|---|
| `id` | unique string; used in `beats[].layers` |
| `t_in`, `t_out` | edit seconds. Gone at `t_out`; the exit preset plays in the last frames before it |
| `z` | 1 background, 2 glow, 3 cards/data, 4 speaker, 5 labels, 6 markers/badges, 7 subtitles, 8 big captions, 9 comedy, 10 banner, 11 light passes (momentary) |
| `behind: true` | depth sandwich: between the footage and the person cut-out (text/objects appear behind the speaker). Only when the stage shows footage. Drawn in **screen space** (clipped to the presenter window): the base reframe, camera punches and the `low` offset never move it, so a card declared at y 450 lands at y 450. Exception: a camera event with `p.target: "all"` (a composition zoom) carries it with the picture, like the z1-6 scenes |
| `follow_footage: true` | behind scenes: ride the footage transform instead: the base reframe, camera presets and the `low` offset move and scale it with the picture (an object pinned to a spot in the room). Front scenes (camera v2, section 4c): ride the camera's punches, rolls and shakes (not the base reframe), e.g. a plate that scales with a 1.19 punch |

| `follow_footage: true` | ride the footage transform: the base reframe, camera presets and the `low` offset move and scale it with the picture (an object pinned to a spot in the room). Behind scenes, and (Package E) front scenes, drawn in footage px |
| `anchor: {track, offset, scale_with, lost}` | follow an object track (`veos track`), section 13 |
| `in`, `out` | enter/exit presets (section 5). Default in `settle`, out `none`. Use `in: "none"` when you animate the entrance yourself |
| `in_frames`, `out_frames` | the enter / exit preset's length in frames (0-60), instead of the preset default (section 5): `in: "blur", in_frames: 3` is a 3-frame blur-in, `in: "stamp", in_frames: 4` a slam. G3 / V-SAFE use it as the entrance / exit window |
| `step_frames` / `step_fps` | animate "on twos": the scene draws a new pose every `step_frames` frames (1-6), or at `step_fps` (5-30; `12` = poses held 3 and 2 frames). `lt`, `ctx.n`, `ctx.t` and the presets are held; the canvas camera stays smooth. G3 judges a stepped scene per pose (k x 90 px). `step_frames: 2` |
| `smear: true` | the enter / exit presets get a directional motion blur along their own travel (a `slide-r` smears horizontally, `rise` vertically) instead of their uniform blur. `in: "slide-r", smear: true` |
| `smear_px` | the smear's largest blur in px (0-48). Default: the style's `motion.smear_push.motion_blur_px`, else 24. `in: "slide-r", smear: true, smear_px: 40` |
| `in_fade` | rarely needed. Travel presets (`slide-l`, `slide-r`, `rocket`) arrive opaque: the scene keeps its motion but has no fade-in, from its first frame (an incoming screen over the held frame). The other presets fade in. `in_fade: true` / `false` overrides either. `in: "slide-r", in_frames: 4` |
| `box: {x,y,w,h}` | declared footprint (also the preset transform origin; the rect used for canvas-drawn scenes) |
| `roles: [...]` | bright colour roles you use (`primary accent bad good data concept comedy`); at most 3 bright roles on screen at once; `comedy` only in mock beats |
| `events: [s, ...]` | LOCAL seconds (after `t_in`) when something visibly changes inside the scene (word swap, pulse, bar grows). Declare every one: they count for the "something changes every 1.5 s" rule (M7) and for "starts on the trigger word" (M6) |
| `text: true`, `text_content: "..."` | set when it carries text; `text_content` is that text as one string (storyboard + checks) |
| `overlaps: ["B", ...]` | scene ids this scene is *intentionally* nested on (a chip pinned on its card). Exempts the pair from the global G1 no-overlap check (use `"__subtitles"` for the auto-subtitles) |
| `onword_lead` | not needed: V-ONWORD accepts a scene (or event) that starts up to 15 f before its trigger word by default (a lead-in, e.g. a highlight box that starts tracing about 12 f early and closes on the word). Still accepted: frames this scene (its start and every `events` time) starts before its word, or `[{at: local s, frames}]` for single events; each 1..15 (or the style's `onword_lead_max`). `t_in: word_s - 12 / 30` |
| `handoff: "<id>"` | declared push out to the scene `<id>` (in / out presets overlapping <= 3 f, like a smear push): G2 does not count this outgoing scene during the overlap. Two scenes that both set `smear: true` are a declared push without it. `out: "slide-l", out_frames: 3, handoff: "output"` |
| `cuts: [s, ...]` | LOCAL seconds of deliberate hard cuts (position/size snaps). Exempts those moments (+-2 frames) from the global G3 smooth-motion check |
| `may_overlap_face` | allowed to cover the face (captions, a label on the chest). Default: z>=5, non-behind scenes must stay 40 px clear of the face |
| `kind` | `"banner"` (the headline slab: exactly one chip, or a bad+good pair; <=9 words; <=2 lines; <=2 emoji; needs `chips: [{text, role}]`, `lines`), `"cta-keyword"` (the CTA keyword chip; `text_content` must contain `meta.keyword`), `"meme"` (comedy sticker/stamp; mock beats only) |
| `render(ctx, lt, dur)` | `lt` = seconds since `t_in`, `dur` = `t_out - t_in`. Return `ctx.html("<div ...>")`, or draw on `ctx.canvas()` and `return ""` |
| `parallax` | canvas camera (section 4b): how much this scene moves with it, 0..1 or `false`. Default z1 0 (backgrounds follow `ctx.camera` themselves), z2 0.8, z3-6 1; z7+ and `behind` never move |
| `nodes` | `[{id, x, y, w, h}]` world px: canvas-camera targets this scene provides (`canvas_camera[].to.node`) |
| `text_px`, `text_class` | smallest font-size (px, before camera zoom) and its class (`TC-display`, `TC-subtitle`, `TC-label`, `TC-legal`, `TC-decorative`); V-CANVAS checks `text_px x zoom` against the class floor. The `VEOS.fx` factories set both. Every text scene sets `text_class`: V-TYPE measures the rendered text against its floor (display 40 px, captions 54, labels 40, legal 22, decorative none), contrast >= 4.5:1 (3:1 for display >= 96 px) and clipping. Inside a scene, mark a node of another class with `data-tc="TC-legal"` (a credit line in a card), and a small label that repeats spoken or larger words with `data-redundant` (28-39 px labels need E3) |
| `exception` | one declared exception id the scene relies on (`"E1"`...`"E6"`; structure Part C, the playbook's `exceptions`): E1 behind-subject display text (`behind: true`, the word stays readable around the head), E2 chaos burst (<= 1.5 s, <= 6 snippets, captions hidden, a clean second after), E3 quiet type, E4 ambient field (texture items, no text; mark items `data-item`), E5 edge bleed (display >= 180 px, 24 px margin), E6 hard swap (content changes inside a fixed container: mark it `data-slot`). Undeclared or unknown ids and `ambient` scenes at z3-10 without E4 are V-EXC advice. Text behind the speaker needs no exception |
| `figure`, `figures`, `lands`, `scale` | data scenes (section 11): the `plan/figures.json` figure(s) this scene shows; `lands: [{t, figure, step}]` the edit seconds where a counter lands on a value (V-DATA: within +-5 frames of the spoken number word); `scale: {id, max}` the shared axis it draws (`ctx.figScale(id).max`). The `VEOS.data` helpers fill all of them |
| `grade` | E-16: while this scene is on screen the FOOTAGE takes this grade (a `tokens.grades.scene` id such as `"GR-mono"`, a CSS filter list, a grade object, or `"off"` for natural footage). It never touches the graphics: the grade is drawn on the footage, cut-out and breakout images under every scene. The latest / highest-z graded scene wins |
| `redundant`, `snippets`, `ambient`, `items`, `item_area`, `speed_px_s`, `dim_under_text` | E3 labels (`redundant: true`); the E2 snippet count when it cannot be measured; the E4 field flag and declared item numbers (used when the items cannot be measured); a declared dim under text when a mask does it |

Output of `render` is placed in a 1080x1920 absolutely-positioned layer at (0,0): position your elements with `position:absolute; left/top` in screen pixels.

## 3. The ctx toolkit
- Frame: `ctx.n`, `ctx.t` (edit seconds), `ctx.fps`, `ctx.W`, `ctx.H`, `ctx.scene` (your scene object), `ctx.stageName`, `ctx.world`.
- Tokens: `ctx.tokens` = `{colours, text_on, fonts, type, layout, motion, camera_presets, stage_morphs, tone, creator, ...}`. `ctx.col(role)` -> hex, `ctx.hexA(role, alpha)` -> rgba(), `ctx.tokens.text_on[role]` = readable text colour on that role, `ctx.fam(slot)` -> CSS font-family (`display chunky body numeric serif marker kinetic ui pixel mono`, with emoji fallback; use inside `font:` shorthand or `g.font`), `ctx.tokens.type.banner/chunky/subtitle/...` (weights, sizes, stroke, shadow, radius), `ctx.safe` = `{x:[64,1016], y:[110,1500]}` (text stays inside), `ctx.tokens.layout` (`banner_top`, `banner_x`, `caption_cy`, `card_zone`, `face_clearance`, ...).
- Face: `ctx.face()` -> `{x,y,w,h,cx,cy}` in output pixels after stage + camera transform, or `null` (stage hidden). Use it to place things clear of the head.
- Tracks (section 13): `ctx.track(id)` -> `{x,y,w,h,cx,cy,conf,lost}` of a tracked object on screen at this frame, or `null`.
- Face-relative bands (E-16b): `ctx.faceRef()` -> the reel-level face on a `full` / `low` stage after the base reframe (median of the reel, steady: no per-frame jitter) `{x,y,w,h,cx,cy,head_top,eye,chin}`, or `null` on other stages; `ctx.faceBand(edge, dy)` -> the y of `head_top | eye | chin | cy | top | bottom` + dy (a banner at `ctx.faceBand("chin", 180)`, a hero-word band above `ctx.faceBand("head_top", -40)`). `ctx.framing` is the base reframe itself (`{s, tx, ty, setup, face, ranges, capped}` or `null`).
- Grades (E-16): `ctx.grade(spec)` -> a `filter:...;` declaration for your own clip or image (a `tokens.grades.scene` id, a CSS list or a grade object; colour only), e.g. a B-roll clip in `GR-amber`: `<img style="${ctx.grade("GR-amber")}" ...>`. `ctx.gradeId` is the footage's grade id at this frame (or `null`).
- Fit to width (A11): `ctx.fitText(text, {width, slot | family, weight, italic, tracking, min, max, line_height})` -> `{size, width, font, css, html}`: the font size that sets one line at `width` px (duo keyword blocks, title lockups). `ctx.worldHTML(id)` returns a world's markup (a `behind` scene can paint W-poster's disc behind the cut-out).
- Layout: `ctx.layout()` -> the stage layout at this frame, resolved (and interpolated mid-morph): `{id, engine, morph, p, from, dim, rects: {presenter, card, pip, band, top, bottom, cells, graphic}, seam_y, anchors: {seam: {y}, below_card: {y}, above_card: {y}, inside_footage: {x,y,w,h}}, caption}` (rects `{x,y,w,h,r}` in output px, `null` when absent). Anchor graphics and captions to it instead of hard-coding y values: a chip at `anchors.seam.y` rides the seam through a morph, a card in `rects.graphic` fills the graphic band. `caption` is the token layout's caption spec (`{anchor, cy}`). `VEOS.layout(n)` returns the same outside a scene.
- Canvas camera: `ctx.camera` -> `{x, y, s, r, k, moving, move, kind, speed, full, home, matrix, view(k), toScreen(wx, wy[, k]), toWorld(sx, sy[, k]), node(id)}`: the view this scene sees (its parallax `k`). `ctx.camera.full` is the camera itself; `view(k)` the view at another parallax (backgrounds use it to slide their pattern); `toScreen` places a pinned label on a world node. Identity when the timeline has no `canvas_camera`. `ctx.footage` is false in a voice-over reel.
- Animation: `ctx.V(lt, inDur, outAt, {in, out, dout, op})` returns an inline `style` string (opacity/transform/filter) for a built-in enter/exit on one element, or `null` when it is not visible (`outAt` null = never exits). `ctx.ease.out | in | inOut | back | elastic` (each `p in 0..1` -> eased 0..1, `back` overshoots), `ctx.lerp(a,b,p)`, `ctx.clamp(x,lo=0,hi=1)`.
- Text: `ctx.measure(text, "800 60px 'Inter Tight'")` -> width px (use `ctx.fam` in the font string); `ctx.esc(s)` HTML-escapes.
- Assets/words: `ctx.asset(id)` -> URL (id = `timeline.assets` key or a `plan/assets` file stem/name; preloaded before READY; for a video asset it is its first frame), `ctx.videoFrame(name, seconds)` -> URL of the frame of a video asset (`veos asset add <video>`) at that LOCAL time: 30 fps, frame-exact (`floor(seconds*30)`), clamped to the first/last frame, decoded before the frame is captured, like footage (`""` for an unknown name). Use it in `<img src>` or `background:url(...)`, `ctx.word(i)`, `ctx.wordsBetween(t0, t1)` -> `[{w,s,e,caption?}]` in edit time for word-synced pops.
- Numbers and figures (section 11): `ctx.fmtNum(value, figureIdOrFormat, override)` writes a number the style's way (₹1,23,45,678, ₹12.5 L, $3.2M, 8.5%, 12 km (7.5 mi)); `ctx.fig(id)` -> the resolved figure `{steps: [{x, at, value, computed, shown, text}], shown, outputs, format, scale_id}`; `ctx.figScale(id)` -> `{max}`; `ctx.figAt(id, t?, {roll, from})` -> the value on screen at t (rolls into each step and lands on its `at`). `VEOS.fmtNum` / `VEOS.fig` work at load time (for `text_content`).
- Randomness: `ctx.rng(seed)` -> seeded PRNG that is stable per (scene, seed, frame): same frame, same numbers. `ctx.rngStable(seed)` is the same for every frame (static scatter).
- Output: `ctx.html(str)` (identity, marks intent), `ctx.canvas()` -> 2D context of a 1080x1920 canvas owned by this scene, cleared each frame (`ctx.canvasEl()` for the element, e.g. to set a CSS filter), `ctx.blur(px)` -> `url(#id)` for a vertical motion-blur filter (`filter:${ctx.blur(12)}`);. `ctx.blurassetImage(px,id)` -> the decoded `<img>` of an imagle) asset (for canvas `drawImage` blurs along any direction (degrees: 0 = horizontal smear, 90 = vertical, 45 = diagonal): `filter:${ctx.blur(14, 0)}` for a WebGL texture; `null` if unknowhn). `ctx.measuripng` onis a`true` sliduring the layout-only `veos measure` pass: a heavy canvas scene may skip painting then, and its declared `box` is used as its rect.

### Assets of one reel (screen recordings, images, logos)
`veos asset add <file> --project P [--name N]`: images (png/jpg/webp/svg) go to `plan/assets/<name>.<ext>` (`ctx.asset("<name>")`). Videos (screen recordings, B-roll; mp4/mov/mkv/webm/gif) are conformed to 30 fps, scaled to fit 1080 px wide and extracted as `plan/assets/<name>/f%05d.jpg` + `meta.json {frames, fps, w, h, duration}` (`ctx.videoFrame("<name>", lt)`). `veos asset list --project P` shows what is there. Never use `<video>`: a recording plays by picking the frame for the scene's local time (`lt`, `lt * speed`, or `lt + offset` to start mid-clip):
```js
VEOS.scene({ id: "rec", t_in: 2, t_out: 6, z: 5, in: "pop", box: { x: 140, y: 420, w: 800, h: 1000 },
  render(ctx, lt) {
    return ctx.html(`<div style="position:absolute;left:140px;top:420px;width:800px;height:1000px;border-radius:48px;overflow:hidden;
      border:6px solid ${ctx.col("ink")};background:url(${ctx.videoFrame("demo", lt)}) center/cover"></div>`);
  } });
```

## 4. Stage, world, camera (timeline.json, not scenes)
- `stage[].layout`: a **token layout id** from the playbook (`tokens.layouts`, e.g. `"L-split"`; preferred in v3 styles) or an engine layout: `full | low | panel | inset | slide-aside | bubble | hidden` (v1) and `card | stack | pip | letterbox | blurfill` (E-07, section 4a). `low` lowers the footage (`offset` default 380 px) to make room above the head for banner + caption + card.
- `stage[].via`: `cut | panel-drop | pop-back | slide-aside | bubble-shrink | bubble-grow` (v1) and `shrink-to-card | grow-from-card | slide-down | slide-up | pip-shrink | pip-grow | morph | dim | fade-through` (E-07). Leave it out and the stage picks the move (section 4a); `dur` (frames) and `ease` (`inOut | out | in | back | elastic | linear | card | slide | pip`) override. `overshoot` (0-0.3) replaces the ease with a back-out that peaks exactly that far past the target and settles: `{"t": 18.78, "layout": "full", "via": "pop-back", "dur": 5, "overshoot": 0.1}` (V-LAYOUT rejects other values).
- `world` tokens: a world's `grid` (or dot grid) takes `fade: true | outer | {x, y, inner, outer, min}` to fade the pattern out radially from a centre (x / y in px or fractions of the frame, inner / outer in px or fractions of the frame height, `min` the edge opacity): `"grid": {"pitch": 72, "colour": "grid", "fade": {"y": 0.45, "outer": 0.5}}`.
- `world[].world`: any world id of the playbook (`tokens.worlds`, e.g. `"W-paper"`), or the v1 `studio | canvas | data` (always available). `fade` (seconds) cross-fades from the previous world.

### 4a. Layouts (E-07)
Params come from engine defaults < `tokens.layouts[id]` < the entry's `p` < inline keys on the entry (`{"t": 3, "layout": "L-split", "seam_y": 1000}`).

| engine | params | looks like |
|---|---|---|
| `card` | `rect {x,y,w,h}` (or `presenter` in tokens), `radius`, `crop: 16:9 \| 4:3 \| 1:1 \| 9:16` (derives a missing w/h), `border: px \| {px, colour}`, `shadow` (0-1), `glow {colour, px}`, `face` (face height / window height), `eye` | lesson card, face window, 16:9 inset, glass card |
| `stack` | `seam_y`, `top`, `bottom` = `footage \| graphic \| source:<id>` or `{src, crop {x,y,w,h} (source px), face, eye, fit: cover \| contain \| blurfill}`, `hairline: px \| {px, colour}`, `fade: px \| {px, colour, side: top \| bottom \| both}` | 50/50 split, seam caption, two live sources |
| `pip` | `shape: circle \| square`, `d`, `corner: tl \| tr \| bl \| br \| tc \| bc \| c \| {cx, cy}`, `ring: px \| {px, colour, gradient: [...]}`, `radius` (square), `margin`, `shadow` | ringed PiP over full-frame evidence |
| `letterbox` | `band_h` (608 = 16:9), `cy`, `fill`, `src` | 16:9 band on black |
| `blurfill` | `band_h`, `cy`, `blur_px`, `luma`, `scale`, `src` | band over a blurred copy of itself |
| treatment | `dim: {blur_px, luma}` or `dim: true` on any layout (also `tokens.layouts[id].treatment.dim`), `full` included | presenter dimmed under a card |
| breakout | `card` / `pip`: `breakout: px` or `true` (= 160): the cut-out head may rise up to px above the window's top edge (drawn over the frame, clipped to the window's columns; needs the matte) | Kallaway face window with the head over the edge |
| seam blend | `stack`: `fade: {px, mode: "blend"}`: instead of a colour band, each footage band reaches px/2 past the seam and fades in over px (a mask), so the face melts into the panel / world behind it | Warikoo F-B face-bottom |

- A stack cell may carry its own `grade` (`top: {src: "footage", crop: {...}, grade: "GR-bw"}`): one shot in two grades (A5).

- `graphic` cells are empty: the world shows there and your scenes paint it (`ctx.layout().rects.graphic`). `source:<id>` plays a second synced source (bundle `sources[id]`: `{base_url, frames, w, h, offset_f, face}`) or a video asset (`plan/assets/<name>`, from the layout's start); the main footage is always `footage`.
- **Default moves**: into `card` `shrink-to-card`, into `stack` `slide-down` (the graphic band and seam ride in from the top), into `pip` `pip-shrink`, into `letterbox`/`blurfill` and between two layouts of one engine `morph`, a `dim` change `dim`; back to a v1 layout `grow-from-card` / `pip-grow` / `slide-up` / `morph`. Their length adapts to the travel so every window moves at most ~84 px and 22% per frame (G3-safe, 8-30 frames); a jump the window cannot make smoothly (bottom window to top inset) becomes `fade-through` (A settles out, B settles in). `tokens.stage_morphs[via]` or `dur` fixes the length instead.
- Auto-subtitles sit at the layout's `caption.cy`, on the seam of a `stack`, or under a `card` / band; they hide during morphs (the caption engine, E-05, reads `ctx.layout()` anchors).
- `ctx.stageName` is the engine (`card`, `stack`...); `ctx.layout().id` is the token id.
- **Base reframe (E-16b)**: on `full` and `low` the footage (and cut-out) is punched in once per reel so the face lands in the template's `footage.setups[].framing` ranges (head top, chin, eye line, face x / height), at most 2.0x (or the setup's `punch_in` max). `timeline.framing: "off"` keeps the raw framing; `{"setup": "B"}` (or `meta.setup`) picks another setup; explicit ranges override. Captions (chest, avoid_face) and V-FACE use the same moved face boxes. The bundle's `framing` record says what was applied.
  - **Which setup:** without `{"setup"}` / `meta.setup` the footage picks it: a face taller than 20 % of the frame reads as an arm's-length selfie, smaller as a tripod / desk take, and the first setup whose `desc` says so (selfie / handheld vs tripod / seated / desk) wins; setups whose desc names formats (F-A, F-B) only serve those formats.
  - **Never enlarge a close face:** a face already ≥ 30 % of the frame height is left as shot (`close: true`; a pull-out is impossible), and a spec without a size range never punches a face past 30 %.
  - **Windows (card / pip / stack):** a layout's `presenter.framing` (fractions of the window: `head_top_frac`, `eye_frac`, `chin_frac`, `face_h_frac`, `face_cx_frac`; or screen px `head_top_y`…) frames the face inside the window (size from the face height or head-to-chin, position from the ranges). Without one, the reel's base ranges apply to a window when every vertical range lies inside it (lesson-frame's 4:3 face card: setup A head top y 610–720). Otherwise `face` / `eye` as before. V-FACE (presenter.py) uses the same geometry.
- **Fonts:** every bundled family the resolved tokens name (`tokens.fonts_extra`: a caption profile, a type spec "Archivo Black 900", a playbook alternative) and every family `plan/scenes.js` names (`bundle.fonts_extra`, e.g. `ctx.fitText({family: "Archivo Black"})`) is loaded at boot, not only the slot fonts. Canvas `fillText` cannot set `font-variation-settings`: use the static-axes instance **Fraunces Soft** (SOFT 100, WONK 0, opsz 9 baked in, weight still variable) for a soft Fraunces on canvas.
- **Grades (E-16)**: the footage grade is `tokens.grades.footage`, replaced by the theme's `grade`, then `timeline.grade` (`"off"` = natural), then the world's `grade`, then a scene's `grade`. `timeline.grades: [{t, t1 | dur, grade, fade, freeze: true}]` are momentary looks over the base (a B&W freeze, a tint flash); without t1/dur an event lasts the grade's `frames`. Graphics are never graded.
- `camera[].preset`: `snap-punch | crash-zoom | pull-out | push-drift | shake | zoom-through | rotation-snap | reset` (see `ctx.tokens.camera_presets` for tones and limits). Never the same preset twice in a row. Easing, roll, pivot, start scale, crop levels and graphics-follow: section 4c.
- Captions are automatic (caption profile engine, E-05; hidden during `captions.hide`, stage morphs and, per profile, z8 scenes). Never write caption cards; nudge them with `captions.overrides`. They are drawn in screen space, so neither camera presets nor the canvas camera move them.

**Caption swaps, reveals and placement (profile fields, `tokens.captions.profiles.<id>`; drawn by `renderer/captions.js`, built by `capengine.py`, checked by V-CAPTION).** Bad values warn at build time, fall back (hard swap, chunk reveal, no fit) and fail V-CAPTION with the field named.

| Field | Values | Example |
|---|---|---|
| `swap.type` | `hard \| fade \| blur \| rise \| pop` and: `flicker` (opacity strobe, one value per frame in `swap.pattern`, default `[1,0,0,1,0,1]`, `frames` = pattern length), `wipe` (feathered mask: `dir` in `right \| left \| down \| up`, default right; `out_dir` for the exit, default the opposite, so L->R in and R->L out; `feather_px` 40; default 6 f; a wiping chunk without a pill gets 48 px of padding above and below (cancelled by a negative margin) so the mask never cuts descenders), `smear` (directional blur `smear_px` 24 at `angle` 0 (deg, 90 = vertical), x-stretch `stretch` 1.6, `travel_px` 40 along `dir` right \| left; default 3 f) | `"swap": {"type": "wipe", "frames": 6, "out_frames": 5, "feather_px": 40}` |
| `swap.out_frames` | with `wipe` / `smear` the exit uses the same swap (wipe erases in `out_dir`, smear leaves along its direction); other types fade out as before. Only when a gap follows | `"swap": {"type": "smear", "frames": 3, "out_frames": 2}` |
| flicker | a pattern flashes (off -> on, at 0.5) as often as the style wants: there is no flash limit | `"swap": {"type": "flicker", "pattern": [1, 0, 1, 1, 0, 1]}` |
| `reveal` | `chunk` (default) \| `word` \| `char`: per-character type-on at `cps` characters/s (default 30), each word types from its onset and is finished before the next word starts (word `tf` frames); untyped letters keep their place (hidden); Devanagari words appear whole | `"reveal": "char", "cps": 45` |
| `skin.line_fit` | `block` (every line grows to the widest line: block justify) \| `max_w` (to `position.max_w`) \| `{to, max_scale}` (default 1.6). Lines only grow, never below the caption floor | `"skin": {"line_fit": "block"}` |
| `tiers.connector_container_when` | `plain_lines` (default: every all-plain line gets the connector pill) \| `plain_only` (only chunks with no keyword) | `"tiers": {"connector_container_when": "plain_only"}` |
| `captions.hide_on_morph` | style-wide (per template) `false` keeps captions on screen through stage morphs (they ride the moving anchors); a profile's own `position.hide_on_morph` wins over it; the timeline's `captions.hide_on_morph` wins over both | `"captions": {"hide_on_morph": false, ...}` |
| caption cy per scene | timeline `captions.overrides` `{t: [a, b], cy}` (the chunk's middle decides) or a scene's `caption_cy` (scene meta; highest z wins): the chunk becomes a `fixed_y` caption centred there; face avoidance and the safe zone still apply; V-CAPTION fails a cy outside `layout.safe.y` | `{"t": [4.0, 7.5], "cy": 1075}` / `VEOS.scene({id: "card2", caption_cy: 1408, ...})` |

The smear's directional blur is a local SVG `feGaussianBlur` (stdDeviation split by angle) emitted with the captions; the shared `ctx.blur` (fx helpers) is separate.

## 4c. Footage blur, built-in transitions, blur pulses, end fade (timeline.json; `renderer/transitions.js`)
Core draws these; **do not write them as bespoke z11 scenes any more**. Validator: V-FX (fields and ranges block; two built-in transitions overlapping is advice). Flashes, leaks and burns are free: no flash limit, every one is drawn at full strength. All are pure functions of the frame; measure passes ignore them.

**Footage blur** (the stage only: footage window, cut-out, breakout, second sources, band backdrop and z1 plate scenes; graphics z2+ and captions stay sharp). A *blur envelope* is `{kind: "defocus" | "directional" | "radial", px (defocus / directional smear, default 12, max 80), angle (directional, degrees, 0 = horizontal), amount (radial zoom spread, default 0.12, max 0.6), at: "face" | "centre" | [x, y] (radial centre), frames (default 8), shape: "pulse" | "decay" | "rise" | "hold", keys: [[frame, 0..1], ...] (per-frame multiplier; replaces frames + shape)}`. Where it goes:
- `timeline.blur: [{t, ...envelope}]`: e.g. `{"t": 6.46, "kind": "defocus", "px": 14, "frames": 5, "shape": "decay"}` (T-02 defocus).
- a camera event `blur` (or `p.blur`), or the preset's own `camera_presets.<id>.blur`: frames default to the move's frames, shape `pulse`. E.g. `{"t": 7.27, "preset": "crash-zoom", "blur": {"kind": "radial", "amount": 0.18, "at": "face"}}`.
- a transition with `layers: "stage"` (blur-through, zoom-blur, whip): only its blur part, on the stage.
- `timeline.grades[]` `blur: px`: a defocus pulse on the grade event's fade envelope (no `grade` needed; 4 f by default): `{"t": 3.62, "blur": 14, "dur": 0.1}`. With **`frame: true`** it blurs the whole picture, graphics z1-6 included (the frame-level blur pulse); captions stay sharp.

**Built-in transitions**: a `timeline.transitions[]` entry **with a `type`** (without one it stays a marker, as before; both count for cadence, storyboards and `transition@t` sound anchors). Common fields: `t` (the cut, edit s), `frames`, `pre` (frames before the cut), `layers`: `picture` (default: world, footage, scenes z1-6, under the captions) | `all` (captions and z7+ too) | `stage`. Two-source types show the outgoing frame frozen on its last frame (`t` minus 1 frame).

| type | default frames / pre | what it does | params (defaults) | example |
|---|---|---|---|---|
| `flash` | 7 / 2 | a colour fill over the picture: rises over `pre`, peak on the cut, decays (a flash that ends on the cut, `pre` = `frames`, reaches `peak` on its last frame) | `colour` (#FFFFFF, or a role), `peak` (0.85, max 1), `decay` exponent (1.6), `blend` (`light` for a white / near-white hex: an exposure lift + soft veil that reads as light, full white at peak 1; else `normal`, the flat veil; also `screen`, `add`), `clear` (`fade`; `wipe`: the flash is full on the cut, then clears in a `dir` (down = top -> bottom) reveal over the next `clear_frames` (default: the rest of the flash), edge `feather` 160 px) | `{"t": 34.57, "type": "flash", "peak": 0.4, "frames": 5}`, `{"t": 12.1, "type": "flash", "peak": 1, "frames": 4, "pre": 2, "clear": "wipe", "clear_frames": 2}` |
| `leak` | 16 / 9 | light-leak burn: a warm wash + a diagonal colour band sweeping across (screen blend), peak on the cut | `colours` (2-5 stops; orange, yellow, cream, red), `angle` (35), `peak` (0.9) | `{"t": 19.25, "type": "leak"}` |
| `blur-through` | 10 / 5 | defocus out, cut, defocus in | `px` (24) | `{"t": 6.0, "type": "blur-through", "px": 18}` |
| `zoom-blur` | 8 / 4 | radial blur + a small scale punch through the cut | `amount` (0.15), `punch` (0.06), `at` | `{"t": 4.42, "type": "zoom-blur", "at": "face"}` |
| `whip` | 8 / 4 | directional smear + travel out, a `blend`-frame cross-blend of the old shot, smear in from the other side | `dir` left/right/up/down or `angle`, `px` (60), `travel` (160), `blend` (2) | `{"t": 21.3, "type": "whip", "dir": "left", "px": 90}` |
| `glitch` | 6 / 3 | seeded slices shifted sideways, RGB split, posterise (composited frame) | `slices` (7), `offset` (60), `rgb` (12), `posterize` (4 levels; 0 off), `seed` | `{"t": 37.42, "type": "glitch"}` |
| `burn` | 14 / 2 | the old frame burns (hot, posterised) and a hole with a glowing edge opens onto the new one | `colour` (#FF6A00), `ring` (140), `at`, `peak` (1) | `{"t": 3.71, "type": "burn", "at": "face"}` |
| `iris` | 10 / 0 | circle mask: `reveal: "next"` (default) the old shot collapses in a shrinking circle over the new one (orb collapse); `"open"` the new one grows in a circle. The frozen old shot keeps the `flash` / `leak` that lit it on its last frame (a bloom-out flash ending on the cut gives a glowing orb) | `reveal`, `at`, `feather` (2), `ring` (0 = none, max 240) px + `colour` | `{"t": 7.08, "type": "iris", "ring": 8}`, `{"t": 7.6, "type": "iris", "reveal": "open", "ring": 200, "colour": "primary"}` |
| `curtain` | 12 / 0 | the new shot enters with an eased clip rect | `dir` (down), `slide` (true: it also travels; false: a wipe) | `{"t": 22.0, "type": "curtain"}` |
| `push` | 12 / 0 | the old frame and the new one (footage window and world together) move along `dir` | `dir` (left) | `{"t": 53.8, "type": "push", "dir": "right"}` |

**End fade**: `timeline.end_fade: 5` (or `{"frames": 5, "colour": "#000000"}`): the last frames fade to black over everything.

### 4c. Camera v2 (timeline.json `camera[]`: footage camera fields)
Each field may sit in the event's `p` or in the preset (`tokens.camera_presets.<id>`); `p` wins. Without them a reel renders exactly as before (ease out, push-drift linear, zoom-through in; zoom about the face; graphics stay put).

| field | values | example |
|---|---|---|
| `ease` | `out` (default) \| `in` \| `inOut` \| `linear` \| `expoInOut` \| `expoOut` | `{"t": 4.1, "preset": "push-drift", "p": {"ease": "in"}}` accelerating push |
| `rotate` | degrees (end roll, from the current roll) or `[from, to]`; `from_rotate` sets only the start | `{"t": 9.0, "preset": "pull-out", "p": {"rotate": [5, 0]}}` roll settling level on a cut-in |
| `origin` (alias `toward`) | `face` (default) \| `center` (window centre) \| `free_side` (the side of the window away from the face) \| `device` (node `device`, else `tokens.layout.device {x, y}`) \| `{x, y}` screen px \| `{node: id}` (scene `nodes` / `canvas_nodes`) | `{"t": 1.3, "preset": "crash-zoom", "p": {"origin": "device"}}` zoom about the phone |
| `from` | `"inherit"` (start from the current crop, no snap) or a start scale | `{"t": 38.77, "preset": "pull-out", "p": {"from": "inherit"}}` |
| `from_wide` | `true` (the raw footage: 1 / base reframe) or a scale 0..1, never wider than the raw footage; the footage still covers the window | `{"t": 22.97, "preset": "snap-punch", "p": {"from_wide": true, "scale": 1.0}}` rush in from wide |
| `land` | `true` (flag) or the start scale: an eased settle to 1.0. Under `zoom_policy: slow_push` a landing that starts on a cut / f0, ends at 1.0 and starts at most 1.5x away is exempt (V-CAMERA) | `{"t": 0, "preset": "settle-out", "p": {"land": 1.22, "ease": "expoOut"}}` |
| `crop` | `wide` \| `mid` \| `tight` (or a scale), about the face: the preset's `levels` midpoint, else `tokens.camera_crops`, else 1.0 / 1.18 / 1.35. On the event itself (`"crop"`) or in `p`; with no `preset` it is an instant re-crop on the cut that holds | `{"t": 6.0, "crop": "tight"}` |
| `target` | `footage` (default) \| `all`: graphics z1-6 and `behind` scenes (never captions or z7+) ride the camera too, blended in and out by the event's ease | `{"t": 4.3, "preset": "crash-zoom", "p": {"target": "all"}}` composition zoom |

- A front scene with `follow_footage: true` always rides the camera (any z). Measure (`veos measure`) records graphics at rest (like enter/exit presets), so G1/G3 judge the layout, not the punch.
- Pivots: a new `origin` re-centres smoothly (the previous pivot's offset fades out over the move); `reset` returns everything to 1.0, level, centred.
- V-CAMERA rejects bad values with the event time and the field (`p.ease 'bouncy' is not one of ...`); the renderer fails the boot on the same values.

## 4b. Canvas camera (timeline.json `canvas_camera`, structure §21)
A camera that moves over the **graphics world**, not over footage: peter.visuals' hub visits, Dan Koe's push-throughs, a flow of stations the viewer travels along. It transforms scenes z1-6 by their `parallax`; **captions (z7/8, auto-subtitles), chrome and z9-11 never move**.
```json
"canvas_nodes": {"keys": {"x": 1510, "y": 3600, "w": 660, "h": 160}},
"canvas_camera": [
  {"t": 11.75, "move": "zoom-through", "to": {"node": "hub"}, "dur": 0.6, "p": {"scale": 4, "then": {"x": 540, "y": 2900, "s": 1}}},
  {"t": 12.75, "move": "push", "to": {"node": "s1-title", "fill": 0.8}, "dur": 0.7},
  {"t": 14.1,  "move": "pull", "to": {"x": 540, "y": 2900, "s": 1}},
  {"t": 20.55, "move": "dolly", "to": {"x": 1840, "y": 2900, "s": 1}, "dur": 1.1, "p": {"arc": 0.12}},
  {"t": 31.2,  "move": "orbit", "dur": 2.0, "p": {"radius": 50, "deg": 2.5}}]
```
- The camera looks at world point `(x, y)` at zoom `s`; that point lands on the frame centre (540, 960). Home is the frame itself (540, 960, 1), or `canvas_home`. A scene drawn at screen coordinates and never moved stays where it is drawn.
- **Moves** (each eases over `dur`, default in brackets): `C-1 push` / `zoom-in` (0.8 s), `C-2 pull` / `zoom-out` (0.7 s) and `settle` (back to home, 0.6 s), `C-3 pan` (keeps the zoom), `drift` (slow, `p.by`, 3 s, sine), `dolly` (between nodes, pulls back mid-way by `p.arc`, 1.0 s), `C-4 zoom-through` (zooms `p.scale`x into the target, then cuts to `p.then` (default home): the object fills the frame and becomes the next scene, 0.8 s), `C-5 orbit` (a small circle of `p.radius` px and `p.deg` roll that returns; with mixed parallax it shows depth, 2 s).
- **Targets** `to`: `{node: id, fill?, keep?: [ids]}` frames a node (`timeline.canvas_nodes` or a scene's `nodes`) at `fill` (0.7) of the frame; `keep` adds neighbouring nodes to the framed box, so a settled push never cuts their text at the frame edge (a push to `s2-doc` with `keep: ["s2-title"]` shows the step title too); `{x, y, s?}` a world point; `{by: {x, y}}` relative; `"home"`.
- `ease`: `inOut` (default), `out`, `in`, `sine`, `expoInOut`, `expoOut`; `linear` only for `drift`. Fast moves get a little motion blur automatically.
- **Roll** (camera v2): `p.roll` = the roll (deg) the move ends on, or `[from, to]` (starts at `from`, a cut); `to.r` works too. Without it a move rolls back level. `{"t": 9.97, "move": "pull", "to": {"x": 540, "y": 960, "s": 1}, "p": {"roll": [-6, 0]}}`
- **Snap** (camera v2): `p.snap: true` on one push / pull / zoom-through: it may last 0.25 s and zoom up to 35 % per frame (220 px travel), e.g. `{"t": 2.27, "move": "push", "to": {"node": "hub"}, "dur": 0.3, "ease": "expoInOut", "p": {"snap": true}}`. Two snaps in a row fail. A zoom-through may last 0.25 s (a short one gets the snap speed limit).
- **V-CANVAS** (`veos validate`): moves known, at least 0.5 s (0.25 s for a zoom-through or a single `snap`), eased, roll within 20 deg and 2 deg per frame, **0.4 s between the end of one move and the start of the next (G3)**, no faster than 12 % zoom (20 % for zoom-through) or 110 px travel per frame, zoom 0.25-12x, and **every moving text scene stays at or above its class floor after zoom** (`text_px x s`). The global G3 check compares each scene's rects with the camera removed, so camera travel is judged by V-CANVAS and a scene's own jumps by G3.
- Measured rects (`veos measure`) are on-screen rects, so G1/G2 see what the viewer sees: when you push in, keep the zoomed content out of the caption band or hide the captions for that span.

### Sound cues (timeline.json `sfx`, tied to your scenes)
Every sound is anchored to a visual moment you wrote here: `{"t": <edit s>, "id": "<catalog id>", "beat": N, "on": "<scene id>@<local s>", "why": "..."}`. `on` may name a scene's start (`L4@0`, `L4@in`), its end (`L4@out`) or any time you declared in that scene's `events` (`L4@0.5`); the cue `t` must be within 3 frames of that moment (`t_in + local`). So when you want a sound at an internal beat of a scene (a counter landing, a stamp), declare that time in `events`. Other anchors: `stage@t`, `camera@t`, `transition@t`. Contract: `CONTRACT.md` section 2; rules S1-S6: `engine/SPEC.md` section 6.

## 5. Enter/exit presets (`in` / `out`)
`settle` (scale 1.08->1 + blur, 8 f), `pop` (overshoot, 7 f), `squash`, `rise`, `drop`, `blur`, `stamp` (big -> 1, slight rotate), `slide-l`, `slide-r`, `rocket` (from below / off the top, vertical motion blur), `none`. Exit default is `none`; `rocket` is 8 f, others 5 f. A scene's `in_frames` / `out_frames` set its own lengths, and `smear: true` turns the preset's blur into a directional smear along its travel.

## 6. Determinism and safety
- A scene is a pure function of `(ctx, lt, dur)`. **No `Math.random`, `Date`, `performance.now`, timers, `fetch`, `<video>`, CSS animations/transitions.** Everything animates from `lt` (or `ctx.n`).
- Never hard-code role colours; use `ctx.col(role)` / `ctx.tokens`. Neutral black/white/shadows via `rgba()` are fine.
- Text uses `ctx.fam(slot)`; keep text inside `ctx.safe`; the banner uses `layout.banner_x`/`banner_top`.
- Do not rely on `document`/DOM state between frames. Preload nothing yourself; use `plan/assets`.
- Do not make a scene full-frame opaque unless it is z1-2.

## 7. Performance budget
Core + all scenes must render in **<= 30 ms per frame** (typical frame: 3-4 active scenes). Keep DOM under ~150 nodes per scene, avoid large `filter: blur()` / `backdrop-filter` stacks and `box-shadow` blurs on many elements, cap canvas paths per frame (~500), and do not build big strings or arrays each frame (hoist constants to top-level). `veos measure` reports `ms_per_frame` of the sampled frames. **Exception: `fx.three` 3D scenes** (section 13) cost 45-150 ms per frame on SwiftShader at about 900x900 px, plus 300-500 ms once on their first frame (build and shader compile). Keep at most one on screen at a time and size its `box` to the object.

## 7b. Global quality checks (`veos validate`, always on, every playbook)
They use the measured rects (`veos measure`; `veos validate` runs the per-frame motion measure itself when `plan/scenes.js` exists). Messages are plain English with the scene ids, the time and a fix. **Two levels** (directions, not limits; `playbooks/_global/GLOBAL-RULES.md`): `failures` are facts and block (G1, G3, the face, readable text, true numbers and quotes, the promise count, the plan, broken fields); `advice` is direction for the Director and never blocks (G2 and every taste rule).
- **G1 no overlap.** At every measured frame, text-bearing scenes, z>=5 non-`behind` scenes and the auto-subtitles (`"__subtitles"`) may not intersect by more than 2% of the smaller rect, unless one of the two declares `overlaps: ["<other id>"]` (deliberate nesting) or is z11. A `kind: "transition"` scene without text lasting <= 1 s (`fx.shatter` shards, streaks) is exempt from G1 and G3. Fix: move the later scene (the hint says by how many px) or declare `overlaps`.
- **G2 no clutter (advice).** At most 4 active scenes with z 3-10 (`behind`, `ambient` and z11 not counted) and at most 3 text elements (subtitles count; `TC-legal`, `TC-decorative` and `ambient` items do not). A declared E2 chaos burst suspends G1/G2 for its own span (V-EXC checks its limits). During a declared push overlap (the outgoing scene in its exit window, the incoming one in its entrance window and started <= 3 f before the outgoing ends; both `smear: true`, or the outgoing `handoff: "<incoming id>"`) the outgoing scene is not counted. Fix: drop or merge one.
- **G3 smooth motion.** A scene's rect centre may not jump more than 90 px, nor its width/height change more than 25%, between two consecutive frames, except within 2 frames of its `t_in`/`t_out`, of a declared `events` time, or of a declared `cuts` time. Counters/typewriters whose text width changes every frame must declare their `events` (or, for content swaps in a fixed container, `exception: "E6"` with the container marked `data-slot`: G3 then accepts the swaps and V-EXC holds the container to +-4 px). z11 and subtitles are exempt. A stepped scene (`step_frames` / `step_fps`, poses held k frames) is judged per pose: up to k x 90 px and 1.25^k size on the frame its pose changes.
- **V-TYPE** (blocks) / **V-EXC** (advice), always on, every playbook: `veos measure` also writes `plan/measure.text.json` (each text element's rendered size, weight, contrast against the real background, clipping, E1 occlusion); see the `text_class` and `exception` rows in section 2 and `engine/SPEC.md` section 7.

Cost: G3 measures every frame where a z3-10 scene is active, headless, with no screenshots and no footage decode (about 17-20 ms/frame, so a 60 s reel with scenes on screen all the time is ~1800 frames, roughly 35 s once, including browser start-up). The result is cached in `plan/measure.motion.json` and only redone when `scenes.js` or `timeline.json` changed (`veos measure --motion` does it explicitly; `veos validate --skip-motion` reuses what exists; capped at 2700 frames = 90 s, with a warning beyond).

## 8. Workflow
1. Write `plan/timeline.json` (beats with `visual`, stage, camera, ...) and `plan/scenes.js`.
2. `veos scenes-meta --project P` (registration errors name the scene) -> `veos measure --project P --every 10` -> `veos validate --project P`.
3. Fix with the `fix` hints (they name beat, time, scene), re-run. `validate` prefers measured rects over declared boxes.
4. Look at frames (`veos render --test ...` + `veos sheet`) before the storyboard.

## 9. Examples
**A. Slab banner with a keyword chip (z10, `kind: "banner"`)**
```js
VEOS.scene({
  id: "banner", t_in: 0, t_out: 3.0, z: 10, in: "settle", out: "rocket", kind: "banner", text: true, roles: ["primary"],
  text_content: "3 Claude skills that kill AI slop 🔥", chips: [{ text: "AI slop", role: "primary" }], lines: 2,
  box: { x: 40, y: 150, w: 1000, h: 260 }, events: [1.2],
  render(ctx, lt) {
    const ty = ctx.tokens.type.banner, k = Math.round(lt * ctx.fps);
    const pulse = k >= 36 && k < 42 ? 1 + 0.12 * Math.sin(Math.PI * (k - 35.5) / 6) : 1;   // = events [1.2]
    const chip = `<span style="display:inline-block;padding:2px 22px 4px;background:${ctx.col("primary")};color:${ctx.tokens.text_on.primary};
      border:4px solid ${ctx.col("ink")};border-radius:14px;transform:scale(${pulse})">AI slop</span>`;
    return ctx.html(`<div style="position:absolute;left:40px;top:150px;width:1000px;box-sizing:border-box;padding:26px 30px;background:${ctx.col("paper")};
      border:${ty.stroke}px solid ${ctx.col("ink")};border-radius:${ty.radius}px;box-shadow:${ty.shadow[0]}px ${ty.shadow[1]}px 0 ${ctx.col("ink")};
      transform:rotate(${ty.rotate}deg);font:${ty.weight} 74px/1.1 ${ctx.fam(ty.slot)};color:${ctx.col("ink")}">3 Claude skills that<br>kill ${chip} 🔥</div>`);
  },
});
```
**B. Word-synced caption pop with its own spring (z8; time it with `ctx.wordsBetween` or the transcript)**
```js
VEOS.scene({
  id: "pop-build", t_in: 12.40, t_out: 13.30, z: 8, in: "none", out: "none", text: true, text_content: "BUILD",
  may_overlap_face: true, roles: [], box: { x: 140, y: 1120, w: 800, h: 220 },
  render(ctx, lt, dur) {
    const s = 0.55 + 0.45 * ctx.ease.back(ctx.clamp(lt / 0.2)), a = ctx.clamp((dur - lt) / 0.12);
    return ctx.html(`<div style="position:absolute;left:140px;top:1120px;width:800px;text-align:center;opacity:${a};transform:scale(${s});
      font:400 150px/1.1 ${ctx.fam("chunky")};color:${ctx.col("paper")};-webkit-text-stroke:6px ${ctx.col("ink")};paint-order:stroke fill">BUILD</div>`);
  },
});
```
**C. Painted card on canvas (z3): you paint bespoke art, no art library**
```js
VEOS.scene({
  id: "stats-card", t_in: 1.0, t_out: 5.0, z: 3, in: "rise", out: "slide-r", roles: ["data"],
  box: { x: 640, y: 330, w: 380, h: 640 }, events: [1.0, 2.2],
  render(ctx, lt) {
    const g = ctx.canvas();                                   // 1080x1920 canvas, cleared each frame
    g.fillStyle = ctx.col("night"); g.beginPath(); g.roundRect(640, 330, 380, 640, 52); g.fill();
    const n = Math.round(ctx.lerp(0, 5000, ctx.ease.out(ctx.clamp(lt / 1.2))));
    g.font = `400 96px ${ctx.fam("numeric")}`; g.fillStyle = ctx.col("data"); g.fillText(n.toLocaleString("en-US"), 680, 545);
    return "";
  },
});
```

## 10. Faceless reels and the `VEOS.fx` toolkit
**Voice-over reels** (`source_type: voiceover_only`): there is no presenter. The engine registers the VO as source `V`, the cut map is the VO's own timeline, and the bundle says `footage: false`, so the **stage is hidden throughout** (core forces it) and `ctx.face()` is `null`. Every frame is built from scenes: **one scene per sentence, no gaps**, on an ambient world. The whole safe box is free (no face), the caption band (around `layout.caption_cy`) is the only reserved strip. The creator's own clips (B-roll, screen recordings, photos) still work: `veos asset add` them and show them with `VEOS.fx.clip`.

`renderer/fx.js` (loaded by `player.html` before your scenes) gives you building blocks for the faceless families seen in the reference styles. They are **building blocks, not a template**: style every one through the playbook's roles and font slots, mix them with bespoke scenes, and keep the global rules. Each factory registers a normal `VEOS.scene` (same fields; pass `in`, `out`, `parallax`, `overlaps`, `roles`, `kind`, `extra: {...}` through) and fills in `box`, `text`, `text_content`, `text_px`, `text_class`, `events` and `nodes` honestly, so validation works without extra declarations.

| Factory | Family | Key options |
|---|---|---|
| `fx.typeStack(o)` | **kinetic type**: lines rise with a vertical blur and stack, alternating bold sans / italic serif (P-STACK-TEXT); `maxLines: 1` = replace mode (Dan Koe captions) | `lines: [{text, at (edit s), style sans\|serif\|cond\|mono\|small, size, color}]`, `x, y, anchor top|center|bottom, align, maxW, maxLines (5), rise, blurPx, inFrames, glide, color, alternate, styles`, `blurAngle` (smear direction, degrees; default vertical), `keepTween: true` (a line finishes its own rise when the next arrives instead of snapping to rest).\|center\|bottom, align, maxW, maxLines (5), rise, blurPx, inFrames, glide, color, alternate, styles`. Markup in `text`: `**bold**`, `_serif italic_`, `~ghost~`, `{word\|role}` |
| `fx.linesFromWords(t0, t1, o)` | load-time helper: transcript words (caption text) -> `lines` of ≤ `maxWords` (3), breaking on pauses ≥ `breakGap` (0.22 s) and punctuation | |
| `fx.diagram(o)` | **node / diagram canvas** in world px: hubs, flows, lists, keycaps; the camera travels across it (P-HUB-DIAGRAM, P-REDACT-REVEAL) | `nodes: [{id, x, y, w, h, shape hex\|circle\|pill\|rect\|bar\|diamond\|none, label, sub, icon, size (52), at, label_at, reveal pop\|fade\|type\|redact, fill, ink, outline, label_pos, active: [[t0,t1]], nodim}]`, `edges: [{from, to, at, dur, style line\|arrow\|dashed, dot}]`, `dimInactive`. Node ids become camera targets |
| `fx.card(o)` | **icon / illustration card** (light, dark, glass, outline, glow) | `x, y, w, h, theme, icon, accent, kicker, number, title, sub, layout row\|stack, device: {kind browser\|terminal\|phone\|doc\|chat\|note, lines, title}, body(ctx, lt, dur)`, `grow: "fit-text"` (the card widens with its title as it types: `typeAt`, `cps` (18), `minW`; `w` is the final width; a title wider than `w` wraps by words and the card grows taller line by line, `h` being the one-line height), `titleWeight` / `titleTracking` (em) (default the font slot's `weight` / `tracking` in `font_slots`, else 800 / -0.02): `{title: "what if it fails?", grow: "fit-text", typeAt: 0.2, cps: 12}`, `{title: "what would you build first?", grow: "fit-text", w: 520, titleFont: "body", titleWeight: 600, titleTracking: 0.04}` |
| `fx.clip(o)` | **creator B-roll, screen recording or photo** over the VO, card or full-bleed (P-REF-CARD, P-EXAMPLE-CLIP) | `asset, x, y, w, h (default full frame), radius, speed, offset, kenburns: [from, to], focus, chip ('6.7M' view chip), dim, border`, `land: {from, frames, ease}` (P-LAND: eased pull-back from `from` (1.2) over `frames` (14), then a hold; `in` defaults to `none`), `rotate: [from, to]` (a dolly roll in degrees, eased with `land` or over the scene; the image is scaled to keep covering unless `cover: false`): `{land: {from: 1.25, frames: 14}, rotate: [-4, 0]}` |
| `fx.morphShape(o)` | **morph / continuity hand-off**: one object that changes shape across beats (Dan Koe's morph chain; a card that becomes the next diagram) | `keys: [{at, shape: {kind circle\|dot\|rect\|hex\|tri\|diamond\|poly\|star\|line, ...}, fill, stroke, width, glow, opacity}], dur (0.5)` |
| `fx.ambient(o)` | **ambient backgrounds** (z1, pinned, they slide with the canvas camera at `follow`): `paper` (dot grid), `grid`, `void` (dark with slow bloom), `aurora`, `particles`, `cards` (P-CARD-RAIN, exception E4: no text; tiles drift at 24 / 40 / 56 px/s, within E4's 60, are marked `data-item`, and keep half their opacity under live captions and `text_rects` + 40 px). The registered scene is `kind: "ambient"`, `continuous: true`, with the pattern in `ambient`, so cadence and hook checks count it as continuous motion | `kind, bg, ink, glow, spacing, dot, follow, drift: [vx, vy], count, seed, assets, text_rects: [{x, y, w, h}]` |
| `fx.flash(o)` | **light flash** (z11, `kind: "flash"`): up, hold, decay | `at, up (2), hold (1), decay (6) frames, color (#FFFFFF or a role), peak (0.85), blend`. Any number of flashes, any length (a strobing style strobes): `fx.flash({id: "fl", at: 4.87, peak: 0.8})` |
| `fx.streak(o)` | **light streaks** sweeping across the frame (T-20, whip accents; z11, `kind: "sweep"`). Even by default: the lead lane starts on `at` at full strength, every lane holds full strength for the whole sweep (a short end fade: none up to 9 f, 2 f from 10 f, 3 f from 20 f) and travels near-linearly; a short streak (<= 4 f) is just short. A coloured streak gets a white hot core | `at, frames (8), y, angle (deg), color, width (16, thickness px), length (0.7 of W), count (3), spread (140 px), seed, glow (24 px), opacity (0.9), core (white on a coloured streak; a colour, or `"none"`)`. Rare overrides: `fade` (end-fade frames), `ease` (`soft` default, `expo`, `linear`, `sine`), `bar: true` (a light bar across the travel spanning the frame, `width` px thick): `fx.streak({id: "st", at: 46.1, y: 900, angle: -10, color: "primary"})`, `fx.streak({id: "t01", at: 4.25, frames: 9, width: 60, angle: 20, count: 1, spread: 0, color: "accent", glow: 100})` |
| `fx.shatter(o)` | **shard break**: whatever sits under the box breaks into seeded shards that fly from an impact point, spin and fall (T-19; `kind: "transition"`). By default the source is the topmost visible scene overlapping the box at the break frame (`at + hold`; flashes, streaks, shatters and ambient backgrounds skipped): its own live markup shatters, each shard a clone clipped to a polygon, drawn as it was on the break frame; the source ends on the break frame by itself and the shards take its z (else 10). Nothing under the box: a `paper` plate breaks | `at, hold (frames intact), frames (14), x, y, w, h, cx, cy, cols (5), rows (8), spread (700), spin (90), gravity (900), seed, z`. Rare overrides: `scene` (a scene id or the object a factory returned; the rect defaults to its `box`), `html` (string or `(ctx, lt) -> html`, frame px), `asset` (an image, shown like `fx.clip` in the rect) or `fill` (a colour plate): `fx.shatter({id: "sh", at: 4.87, hold: 2, frames: 9, x: 100, y: 400, w: 880, h: 420, cols: 3, rows: 3})`, `fx.shatter({id: "sh", at: 4.87, asset: "plate", cols: 4, rows: 6})` |

Render helpers for bespoke scenes: `fx.icon(name, {size, color, stroke, glow})` (46 line icons drawn for VEOS: `fx.icons()` lists them), `fx.device(kind, {...})` (recreated generic UI frames: never a look-alike of a real brand), `fx.typewriter(text, lt, {at, cps, flare})` (`flare: true | {color, px, frames, scale}`: the newest letter lands as a bright blurred glyph and cools), `fx.typeOn(text, lt, {at, cps (20), frames (6), drop (0.45 em), stretch (0.4), blur})` (per-glyph drop-in with a stretch; untyped glyphs keep their place), `fx.resolve(text, lt, {at, dur (0.6), every (2 f), order ltr|rtl|random|center, seed, charset, ghost, color, ctx, font})` (seeded letter scramble that locks letter by letter; pass `ctx` + `font` to hold each glyph width; `fx.resolvedAt(text, o)` is the lock-in second for `events`), `fx.shape(kind, o)` / `fx.morph(a, b, p)` / `fx.path(points)`, `fx.handoff(rectA, rectB, p)` (shared-object rect between two scenes), `fx.mix(hex1, hex2, p)`, `fx.rgba(ctx, role, a)`, `fx.parseMarks(text)`.

**Recipes**
- *Peter-style framework reel:* `fx.ambient({kind: "paper"})` -> a `typeStack` hook built from `fx.linesFromWords` -> a `diagram` hub whose bars `reveal: "redact"` -> per item, `canvas_camera` push to the node, its label types, a creator `clip` or a `card` as proof -> pull out. World flips (paper <-> dark) are hard cuts between `ambient` scenes at section starts (declare them as `transitions`).
- *Dan Koe-style metaphor chain:* `fx.ambient({kind: "void", glow: "paper"})`, one `morphShape` that carries the motif (dot -> ring -> card) through every beat, `typeStack({maxLines: 1, styles: {sans: {slot: "display", weight: 400, size: 48}}})` as quiet captions, a `zoom-through` into the object to hand off to the next scene. No hard cuts.
- *Stations on one canvas:* lay each item out at screen coordinates plus an offset (`station k = layout + [dx_k, dy_k]`), give each a `diagram`, and `dolly` between them; the paper `ambient` with `follow` < 1 adds depth while the camera travels. See `renderer/demo/faceless/` for a complete 33 s reel (kinetic type, number cards, morph hand-off, a hub with redacted bars, three stations, zoom-through, push, pull, dolly and orbit) that validates clean.
- *Creator clips on a faceless reel:* a full-bleed `clip` for ≤ 2.5 s as proof, or a 9:16 card (`w: 430-760`) with a view chip next to the kinetic stack.

**Legible text by default.** `fx` text (stack lines, card kicker / title marks / sub, diagram labels and sublabels) is passed through `fx.legible(colour, ground, min)`: a role colour that is too light for the ground under it (the orange accent on cream or white) is deepened in lightness, same hue, until it reaches V-TYPE contrast (4.5:1, or 3:1 for display text of 96 px and up, plus a small margin); colours that already pass are untouched. The ground is the card fill, the node fill, or the `fx.ambient` world active at that time (`fx.bgAt`). Sublabels are a solid tint of the label colour, never opacity. Use `fx.textColour(ctx, role, ground, px)` in your own scenes.

**Rules that matter most here:** G2 counts a diagram as one element (its labels are internal), so prefer one diagram per screen to many cards; captions and kinetic stacks are both text: hide the auto-subtitles (`captions.hide`) while a stack shows the same words; zoomed world text must stay above its floor (V-CANVAS); never let zoomed content run into the caption band.

**Example: a faceless hook and a canvas station (from the proof reel)**
```js
VEOS.fx.ambient({ id: "paper", t_in: 0, t_out: 33.5, kind: "paper", follow: 0.7 });
VEOS.fx.typeStack({ id: "hook", t_in: 0, t_out: 3.45, z: 5, y: 640, anchor: "top", roles: ["primary"],
  lines: [{ text: "tum jo **prompts**", at: 0 }, { text: "app banane ke liye", at: 0.6 }, { text: "usse {ghanta|primary}", at: 1.95 }] });
// or: lines: VEOS.fx.linesFromWords(0, 3.45, { maxWords: 3 })
VEOS.fx.card({ id: "num-4", t_in: 6.13, t_out: 7.42, z: 4, x: 570, y: 700, w: 400, h: 460, theme: "glass",
  layout: "stack", align: "center", number: "4", title: "apps shipped" });
VEOS.fx.morphShape({ id: "card-to-hub", t_in: 7.4, t_out: 8.05, z: 3, in: "none", out: "none", keys: [
  { at: 7.4, shape: { kind: "rect", x: 570, y: 700, w: 400, h: 460, radius: 40 }, fill: "#2E2C2B" },
  { at: 7.5, shape: { kind: "hex", cx: 540, cy: 900, r: 160 }, fill: "#2B2421" }] });
const S1 = (x, y, w, h) => ({ x, y: y + 1940, w, h });   // station 1 sits one screen below home
VEOS.fx.diagram({ id: "st1", t_in: 12.35, t_out: 22.2, z: 3, out: "none", nodes: [
  { id: "s1-title", ...S1(250, 300, 600, 120), shape: "pill", fill: "ink", label: "/init", size: 72, reveal: "type", at: 12.45, label_at: 13.15 },
  { id: "s1-mem", ...S1(96, 860, 888, 250), shape: "rect", fill: "paper", outline: "ink", ink: "ink", icon: "file",
    label: "CLAUDE.md", sub: "a memory file", size: 64, at: 15.28, active: [[16.4, 20.6]] }] });
```
with `"canvas_camera": [{"t": 11.75, "move": "zoom-through", "to": {"node": "hub"}, "dur": 0.6, "p": {"scale": 4, "then": {"x": 540, "y": 2900, "s": 1}}}, {"t": 12.75, "move": "push", "to": {"node": "s1-title", "fill": 0.8}, "dur": 0.7}, {"t": 14.1, "move": "pull", "to": {"x": 540, "y": 2900, "s": 1}}]` and `"stage": [{"t": 0, "layout": "hidden"}]`.

## 11. Numbers and figures (E-08, structure §18)
**Never type a number into a data scene.** Every chart, counter, comparison and hero number comes from `plan/figures.json` (the planner writes it from the script and transcript; `veos figures --project P` resolves it and prints shown vs recomputed values) and is written by `ctx.fmtNum`, so `veos validate` can recompute it:
- **V-DATA** recomputes every formula and compares the stated values at display precision (`round_to` when the creator rounds); every number in a bound scene's `text_content` must be a value of its figures, and any other number on screen must be in figures.json or spoken; spoken numbers in data beats must be in figures.json; scenes sharing a `scale_id` draw the same axis max; counters land within +-5 frames of the spoken number word (else of the step's `at`).
- **V-NUMFMT** checks the style's `profile.numbers`: grouping (a wrong rupee grouping like ₹131,190 fails), the ₹ glyph (not Rs / INR), the compact system (no K/M/B on ₹ amounts in a lakh/crore style), decimals, dual units; figure-bound numbers must be written exactly as the figure's format writes them.

`ctx.fmtNum(v, spec)`: `spec` is a figure id (its `format`), a format object, or `"full"` (₹1,63,250) | `"short"` (₹1.6 L, ₹3.2 Cr, $3.2M) | `"long"` (₹1.6 lakh, $3.2 million) | `"percent"`. Format keys: `grouping`, `currency`, `compact`, `style`, `decimals`, `compact_decimals`, `percent_decimals`, `unit` (`%`, `km`, `kg`, `l`, `c`...), `units` (`metric | imperial | dual`), `lang` (`en | hinglish | hi`: lakh / लाख), `plural`, `sign`, `prefix`, `suffix`. It is the same function as the engine's `numfmt.fmt_num` (a test keeps them identical).

**`VEOS.data` helpers** (`renderer/data.js`): each registers a scene bound to its figures with honest metadata (`figure(s)`, `lands`, `scale`, `events` at each landing, `text_content` of every value it will show).

| Helper | Shows | Key options |
|---|---|---|
| `VEOS.data.counter(o)` | a number that rolls into each step and lands on the step's `at` (hero number, ledger) | `figure, x, y, w, size, font, color, glow, label, labelSize, roll (frames, 12), from (0), steps, format` |
| `VEOS.data.bars(o)` | horizontal bars for several figures on ONE shared scale, value roll-ups, a leader chip | `figures, scale, labels, colors, card, track, rowH, gap, valueSize, labelSize, leader {text, role, by: max or min}, roll` |
| `VEOS.data.slider(o)` | a parameter axis (years 2/4/6/8/10) whose handle moves to the step being spoken | `figure, x, y, w, label, size, color, handle, roll` |

**Example A: an animated counter** (lands on the spoken "₹36,750"; `gap` is the diff of two figures)
```js
VEOS.data.counter({ id: "gap-counter", figure: "gap", t_in: 11.44, t_out: 15.5, z: 4, x: 64, y: 860, w: 900, size: 200,
  font: "numeric", color: "paper", glow: "bad", label: "more interest on the 8% flat loan", labelSize: 48, roll: 54 });
```
**Example B: bars from figures with a shared scale** (both figures have `scale_id: "S-int"`; a bar's length is value / the scale's max, so ₹1,63,250 is drawn against the same ₹2,00,000 axis as the flat loan)
```js
VEOS.data.slider({ id: "year-slider", figure: "flat", t_in: 3.5, t_out: 11.44, x: 130, y: 790, w: 800, label: "Year" });
VEOS.data.bars({ id: "interest-bars", figures: ["flat", "red"], t_in: 3.5, t_out: 11.44, x: 64, y: 960, w: 900,
  labels: { flat: "8%", red: "11%" }, colors: { flat: "data", red: "ink" }, card: "paper", leader: { text: "Costs more", role: "bad" } });
```
with `plan/figures.json`:
```json
{"inputs": {"loan": {"value": 250000, "from": "script", "said": "₹2.5 lakhs"}, "years": {"value": 10, "from": "spoken@4.1"},
            "flat_rate": {"value": 8, "from": "script", "said": "an 8% loan"}, "red_rate": {"value": 11, "from": "script", "said": "an 11% loan"}},
 "figures": [
  {"id": "flat", "kind": "bar", "label": "8%", "formula": "flat_rate_interest", "output": "interest_paid", "scale_id": "S-int",
   "args": {"principal": "loan", "rate_pct": "flat_rate", "years": "years"},
   "steps": [{"x": 2, "args": {"elapsed_years": 2}, "value": 40000, "at": 7.1}, {"x": 10, "args": {"elapsed_years": 10}, "value": 200000, "at": 27.9}]},
  {"id": "red", "kind": "bar", "label": "11%", "formula": "reducing_balance_emi", "output": "interest_paid", "scale_id": "S-int", "round_to": 10,
   "args": {"principal": "loan", "rate_pct": "red_rate", "years": "years"},
   "steps": [{"x": 2, "args": {"elapsed_years": 2}, "value": 51880, "at": 8.6}, {"x": 10, "args": {"elapsed_years": 10}, "value": 163250, "at": 30.1}]},
  {"id": "gap", "kind": "counter", "formula": "diff", "args": {"a": "fig:flat", "b": "fig:red"}, "steps": [{"value": 36750, "at": 13.74}]}]}
```
**Example C: a loan comparison card** (a bespoke scene: bind it with `figures`, write every number with `ctx.fmtNum`, roll with `ctx.figAt`)
```js
const EMI = [{ id: "flat_emi", title: "8% flat", role: "bad", x: 64 }, { id: "red_emi", title: "11% reducing", role: "good", x: 534 }];
VEOS.scene({ id: "loan-card", t_in: 0, t_out: 3.5, z: 4, kind: "figure", in: "rise", out: "blur", text: true, text_class: "TC-label",
  roles: ["bad", "good"], figures: EMI.map(e => e.id), box: { x: 64, y: 700, w: 900, h: 680 },
  lands: EMI.map(e => ({ t: VEOS.fig(e.id).steps[0].at, figure: e.id })), events: EMI.map(e => VEOS.fig(e.id).steps[0].at),
  text_content: [...EMI.map(e => e.title), "EMI", ...EMI.map(e => VEOS.fmtNum(VEOS.fig(e.id).shown, e.id)), "per month"].join(" "),
  render(ctx) {
    return ctx.html(EMI.map(e => {
      const at = ctx.fig(e.id).steps[0].at, v = ctx.figAt(e.id, ctx.t, { roll: 10 }).value;
      return `<div style="position:absolute;left:${e.x}px;top:820px;width:430px;height:420px;border-radius:28px;background:${ctx.col("paper")};padding:34px 36px;box-sizing:border-box">
        <span style="padding:6px 20px;border-radius:14px;background:${ctx.col(e.role)};color:${ctx.tokens.text_on[e.role]};font:800 46px/1.1 ${ctx.fam("display")}">${e.title}</span>
        <div style="margin-top:34px;font:600 40px/1 ${ctx.fam("display")};color:#4a4a4a">EMI</div>
        <div style="height:118px;font:400 108px/1.08 ${ctx.fam("numeric")};font-variant-numeric:tabular-nums">${ctx.t >= at - 10 / 30 ? ctx.fmtNum(v, e.id) : ""}</div>
        <div style="font:600 40px/1 ${ctx.fam("display")};color:#4a4a4a">per month</div></div>`;
    }).join(""));
  } });
```
(`flat_emi` / `red_emi` are the same two formulas with `"output": "emi"`: ₹3,750 flat vs ₹3,444 reducing.) Keep counter text inside a fixed-width box (G3), and put `figure` / `figures` on every scene that shows figure numbers.

## 12. Third-party moments: the created-substitute toolkit (E-10)
**Claude never fetches anyone else's media** (no web tools, no URLs in scenes; `veos` has no download command). A post, headline, clip, product, app screen, chart, event or person appears only as the creator's own file (`veos asset add <file> --origin creator`) or as a visual you create here. Every moment is a record in `plan/inserts.json` (engine/SPEC.md section 7, Inserts); pass its id as `insert` so V-INSERTS finds the scene. `renderer/inserts.js` (loaded after fx.js) holds premium, unbranded recipes; each sets `box`, `text_content`, `text_px`, `text_class` and the insert metadata (`insert, recipe, origin, label, synthetic, quote_text, credit, asset, source`). Common options: `id, t_in, t_out, z (4), x, y, w, insert, theme (light | paper | dark)`; `credit` and `label` draw a small line only when you pass them (made-up cards need neither). Entrances are built in (rise + de-blur over 10 f; exit fade over 6 f). Text classes: card text TC-label >= 40 px; an optional label or credit line TC-legal 24 px.

| Factory | Stands in for | Key options |
|---|---|---|
| `fx.quoteCard(o)` | a post or quote read aloud (generic card: avatar initials, name, a neutral post glyph, never a platform logo) | `quote` (verbatim script words), `name`, `handle?` (only if the script says it), `size` (54), `reveal` (word by word, `wps` 9), `highlight: [phrases]`, `hlRole` |
| `fx.headlineCard(o)` | a news article | `masthead` (set in type), `date`, `headline` (exact), `highlight: [phrases]` (Dhruv-style bars wiping word by word from `hlAt`, 0.5 s per span; the bar colour is darkened until its text reads >= 4.6:1), `hlRole` ('bad'), `kicker`, `body` (decorative lines, 3) |
| `fx.appUI(o)` | an app screen, a screen recording, or another creator's clip | `kind: terminal \| list \| chat \| settings \| browser \| video`, `title`, `lines: [str \| {text, out, who: "me", on}]`, `at: [local s]` (typing / row times; terminal typing declares an event every 0.9 s), `accent`, `size` (>= 40), `caption` (video) |
| `fx.logoPlate(o)` | a product, company or event (never a logo) | `name`, `kicker`, `sub`, `monogram` (initials, decorative), `accent`, `pulses: [local s]` (the tile pulses on words). No label: it is type, not a reconstruction |
| `fx.silhouette(o)` | a person's photo | `name`, `role` (from the script), `accent` |
| `fx.citationStrip(o)` | evidence (Dhruv): SOURCE strip, masthead, date | created: `headline`, `highlight`; creator: `asset` (+ `aspect`, `highlights: [{x, y, w, h (0..1 of the image), at, role}]`) |
| `fx.shot(o)` | the creator's own screenshot or clip, framed | `asset`, `aspect` (image w/h; used for the cover crop), `chrome` (window bar title, or false), `push` ([1, 1.06]; no painted element grows, so G1/V-SAFE see the card), `focus`, `highlights`, `credit` |
| `fx.creditLine(o)` | an optional small source line (never required) | `text`, `x`, `y`, `size` (>= 22), `config` (tokens `citations.credit_line`) |

**Recipes**
- *Dhruv-style evidence:* the creator's article screenshot in `citationStrip({asset, highlights})`; without one, `headlineCard` or `citationStrip({headline, highlight})` with the exact headline from the script and red bars on the spoken phrase. The beat carries `source {masthead, date, headline}` and `highlight_spans` (V-CITE: the headline word for word).
- *100x-style tool beats:* `appUI({kind: "list" | "terminal"})` for a product's screen, `logoPlate` for the product's name.
- *peter.visuals-style proof:* `quoteCard` for a post read aloud (a light card on the paper world), `appUI({kind: "video", caption})` for another creator's reel; with the creator's own clip, `fx.shot` / `fx.clip` instead.
- *Talking head (Vaibhav / Naman):* switch the stage to `stack` and put the insert in the graphic band (`y` 200-860 clears a 980 seam and its captions).

```js
VEOS.fx.shot({ id: "ins-site", insert: "I1", asset: "inspo-site", t_in: 6.0, t_out: 9.4, x: 70, y: 214, w: 940, aspect: 1.6,
  chrome: "the site you like", highlights: [{ x: 0.035, y: 0.21, w: 0.41, h: 0.25, at: 0.65, role: "primary" }] });
VEOS.fx.logoPlate({ id: "ins-flow", insert: "I2", t_in: 9.6, t_out: 13.9, y: 330, name: "Google Flow", kicker: "photo se video",
  sub: "5-6 second ka loop", accent: "data", pulses: [1.08, 2.0] });
VEOS.fx.appUI({ id: "ins-cc", insert: "I3", kind: "terminal", t_in: 14.1, t_out: 19.0, y: 236, title: "claude code · my-site",
  lines: [{ text: "yahi website Claude Design se directly de do" }, { text: "✓ design received", out: true }], at: [0.3, 1.44] });
```

## 13. Object tracking and anchors (Package E: `veos track`, `anchor`, `ctx.track`)
A graphic that stays on a moving object (a ring around a device the presenter whips round, a price tag on a product, an X on a hand) follows a **track**: per-frame boxes made on the CPU from the footage, never hand-written keyframes.

**When to ask for one (plan / storyboard stage):** as soon as a beat's visual says "on the phone", "follows the product", "circle the device" and the object moves. Track only the span the scene is on screen (≤ 10 s per run).
1. `veos track --project P --at 3.2 --look` writes `plan/tracks/look_3.2.jpg`: the edit frame at 3.2 s with a grid every 100 px (1080x1920 edit-frame px, the pixels of `work/frames/`; double the `cut_proxy.mp4` coordinates). Read the object's box off it.
2. `veos track --project P --id phone --at 3.2 --box 820,560,200,300 --from 2.8 --to 7.5` (or `--point x,y` for a fingertip / a spot). It tracks forwards to `--to` and backwards to `--from` on a 640 px proxy every 2nd frame (OpenCV CSRT when the build has it, else the built-in optical-flow tracker; points use Lucas-Kanade), interpolates the rest, and writes `plan/tracks/phone.json` + `plan/tracks/phone.preview.jpg` (six frames, box drawn green, red = lost). **Look at the preview.** Jump cuts inside one take are followed; spans from other sources are left out (`--clip A` keeps only source A).
3. A B-roll clip or video asset: `--clip <plan/assets name | file>`; times and pixels are then the clip's own (`space: "clip"`), and the anchor says where the scene draws it (`place`, `clip_t0`).

Track file: `{version: 1, id, space: edit|clip, mode: box|point, method, size, frames: [{f, x, y, w, h, conf, lost?}], stats}`; edit tracks hold output-frame px on a full stage after the base reframe (engine/src/veos/track.py has the full format). Confidence is the patch correlation with the seed / recent template (0..1); below `min_conf` (0.5) a frame is **lost** and keeps the last confident box; the tracker searches the whole frame and resumes when the object comes back.

**Scene field `anchor`** (needs a `box`; its centre lands on the track point):
| key | |
|---|---|
| `track` | track id (`plan/tracks/<id>.json`) |
| `offset: [dx, dy]` | px from the track point to the box centre (scaled with the object when `scale_with`) |
| `point` | `center` (default) `top bottom left right` of the tracked box |
| `scale_with` | scale the scene about its box centre by the object's size change since `t_in` (camera punches included) |
| `smooth` | half-window in frames of the moving average (default 2; 0 = raw) |
| `lost`, `fade` | `hold` (default: stay at the last confident spot) or `fade` (fade out over `fade` frames, default 6, before the lost frames and back in after) |
| `min_conf`, `max_lost` | lost threshold (default the track's 0.5) and the share of lost frames V-ANCHOR accepts (default 0.2) |
| `clip_t0`, `speed`, `place: {x, y, w}` | clip-space tracks only: clip seconds at `t_in`, playback speed, and the screen rect where the scene draws the clip (left, top, width) |

```js
VEOS.scene({ id: "ring", t_in: 3.2, t_out: 7.4, z: 6, in: "pop", box: { x: 340, y: 760, w: 400, h: 400 },
  anchor: { track: "phone", scale_with: true, lost: "fade" }, render(ctx, lt) { /* a ring drawn inside the box */ } });
```
The edit-space anchor rides the live footage->screen transform (base reframe, stage layout, camera presets, like `ctx.face()`); anchored scenes ignore the canvas camera and are exempt from G3 (the motion is the object's). `follow_footage: true` now also works on front scenes (z>=1, not `behind`): the scene is drawn in footage px and rides the footage transform, without a track. `anchor` and `follow_footage` are exclusive.

**`ctx.track(id, o)`** -> `{x, y, w, h, cx, cy, conf, lost}` on screen at this frame (o: `{smooth, min_conf}`; clip tracks `{t: clip seconds, place}`), or `null` (no track, or the footage window is hidden). For bespoke drawing: a leader line from a fixed label to the device, a highlight that grows with it.

**V-ANCHOR** (`veos validate`, whenever a scene has `anchor`): the anchor is well formed and the scene has a box; the track exists; it covers every frame of the scene; at most `max_lost` of the span is lost; a `hold` anchor never sits still on a lost object for more than 15 frames; and the predicted rect never covers the face (40 px clearance, `may_overlap_face` relaxes only the clearance) on full / low stages. Fixes name the scene, the time and the `veos track` call.

## 13. Lit 3D objects: `VEOS.fx.three` (Package F)
`renderer/fx3d.js` runs on the vendored **three.js r186** (`renderer/vendor/three.min.js`: npm three@0.186.1 plus the SVGLoader and RoundedBoxGeometry addons, bundled as one classic-script IIFE with the global `THREE`; MIT licence in `vendor/three.LICENSE`). Nothing loads from a CDN or the network: textures are plan/assets images, and 3D text is traced from the playbook's own font slots. One factory, `VEOS.fx.three(o)`, registers a normal scene (z 3 by default, `in`/`out` `none`). It renders a lit 3D scene into its `box` with a **transparent background**, so it composites over worlds, footage and other scenes like any canvas scene.

**Determinism.** The scene graph is built once, at the scene's first frame. After that, every transform, the camera and the fades are set from `lt` on every frame: no clock, no requestAnimationFrame, no AnimationMixer. Headless Chromium renders WebGL2 on SwiftShader (software, bit-stable), so every render worker paints the same frame. `veos doctor` reports the WebGL renderer. `VEOS.fx.three.info()` returns `{ok, renderer, version}` and `VEOS.fx.three.stats()` returns `{frames, ms_last, ms_max, ms_avg}`. Without WebGL the scene fails the render with a clear message instead of rendering blank.

| option | |
|---|---|
| `id, t_in, t_out, z, in, out, behind, parallax, overlaps, kind, roles, events, extra` | same as every fx factory. **Every other standard scene key passes through to the scene** like `VEOS.scene` (`text_class`, `insert`, `exception`, `anchor`, `follow_footage`, `may_overlap_face`, `cuts`, `grade`, ...), so V-TYPE / V-INSERTS read them directly (no `extra` needed). A scene with 3D text defaults to `text_class: "TC-display"` |
| `box` | `{x, y, w, h}` px: the render region (and the measured rect). Default: the full frame. A smaller box renders faster |
| `objects` | `[{kind, ...}]` (kinds below). Common fields: `pos [x,y,z]`, `rot [deg x,y,z]`, `scale` (a number or [x,y,z]), `spin` (deg/s turntable around the object's own y), `color` / `side` (role or hex), `metal`, `rough`, `material: "chrome"` (preset: bright polished chrome, a white -> ice-blue face (`grad ["#FFFFFF", "#9FC2FF"]`), side `#AFC2DC`, metal 1, rough 0.12; your `color` / `side` / `metal` / `rough` / `grad` still win), `grad: [top, bottom]` (text / svg: a vertical face gradient, multiplied with `color`), `env_k` (this object's reflection strength, 0..4), `emissive` (role), `emissive_k`, `glow: {color, size, strength, behind, y}` (an additive halo kept behind the object), `opacity`, `shadow` (casts a shadow, default true), `receive`, `keys: [{at (local s), pos?, rot?, scale?, opacity?, ease?}]` (absolute values, eased from the previous key; ease `out` by default, or `linear in inOut expoOut back sine`) |
| `camera` | `{fov (35), pos [0,0.6,8], target [0,0,0], roll, fit, keys: [{at, pos?, target?, fov?, ease?}]}` or `orbit: {radius (8), height (1.5), from, to}` (degrees, eased over the scene with ease inOut) or `orbit: {from, speed}` (deg/s). `fit` (0.2..1): a fixed camera moves along its `pos` -> `target` direction (target: the objects' centre unless given) until the objects' rest pose fills that share of the box height or width. **A scene with a `device` and no `camera.pos` / `keys` / `orbit` fits at 0.9 by default**, so the phone fills its `box` |
| `env` | reflections from a built-in procedural studio environment (a graded dome plus HDR softboxes, one behind the camera so flat faces read bright; pre-filtered once with PMREM, no file or download). Default: on for metal materials only (`metal` >= 0.5, `material: "chrome"`, the device frame), so a metal title is never black. `true` / `{intensity (1, 0..4), tint (the softboxes' lower colour, role or hex, default ice blue #B9D3FF)}` lights every material; `false` switches it off |
| `lights` | key (casts the shadow), fill, rim and ambient (hemisphere). `{key: {color, intensity, pos}, rim: {...}, fill: false, ...}` overrides the studio defaults |
| `ground` | `{y (0), size (8, the shadow camera half-extent), shadow (0.35 opacity), soft}`: an invisible plane that shows only the shadow |
| `quality` | `{scale (1 = render px / box px, 0.25..2), aa (false; MSAA costs about 1.4x the GL time), shadow (1024 map px, 256..2048)}` |
| `update(THREE, scene, lt, dur, ctx)` | optional bespoke per-frame posing (must stay a pure function of `lt`) |

Object kinds:
- `text`: `text, slot (display), weight (800), italic, size (world height, 1), depth, bevel, res (trace px, 220)`. The playbook font's glyphs are traced, then extruded and bevelled. `color` is the face, `side` the extrusion.
- `svg`: `svg` markup, or `path` as a d string or array. The logo is extruded the same way. Never use a real brand's logo unless the creator supplied it.
- `globe`: `radius`, `texture` (an equirect image asset). Without a texture you get a procedural graticule: `sea, line, land` (false = no dots), plus an `atmosphere` role.
- `sphere`.
- `tower`: `width, height, depth, floors, lines`. Its base sits at y 0, so keying `scale` from `[1,0,1]` to 1 grows it out of the ground. `shape: "cyl"` makes it round.
- `cylinder`: `radius, radius_top, height`, base at y 0.
- `box`: `dims [w,h,d]`, `radius` (rounded corners).
- `device`: `dims [1, 2.05, 0.09]`, `radius` (corner radius in the screen plane, 0.14 x width), `bezel` (body edge to screen, 0.045 x width), `notch` (`"island"` default for a phone-shaped slab, `"notch"`, `"none"`), and `screen` (an image asset shown on the screen, with rounded corners). The frame is metal with rounded edges under a black glass front. Size it by `box`: with no camera position the camera fits the phone to 90 % of the box.
- `custom`: `build(THREE, ctx)` returns an Object3D. THREE is the full r186 API.

Validation: bad kinds, empty text, malformed vectors, keys or eases, and out-of-range `quality` or `camera.fov` values are registration errors that name the scene id (`veos scenes-meta`). Scene meta carries `fx: "three"` and `three: {objects, camera, shadow, scale}`. 3D words count as `text` for the safe zone and G2, and face clearance is checked through `box`.

**Recipes** (from the fixture `engine/tests/data/three/scenes.js`; stills in `docs/audit/_engine-proof/3d-objects/`)
```js
// logo slam: the word drops in, overshoots and lands with a ground shadow
VEOS.fx.three({ id: "slam", t_in: 0, t_out: 1.4, z: 5, box: { x: 0, y: 360, w: 1080, h: 900 }, ground: { size: 6, shadow: 0.45 },
  camera: { fov: 30, pos: [0, 1.6, 9], target: [0, 0.9, 0] },
  objects: [{ kind: "text", text: "SHIP IT", slot: "display", size: 1.3, color: "paper", side: "primary", pos: [0, 0.9, 0],
    keys: [{ at: 0, pos: [0, 5, 2], rot: [-35, 0, 0], scale: 1.4 }, { at: 0.35, pos: [0, 0.9, 0], rot: [0, 0, 0], scale: 1, ease: "back" }] }] });
// globe spin: a procedural data globe (or texture: "<equirect asset>"), rim-lit, with a halo
VEOS.fx.three({ id: "globe", t_in: 2, t_out: 5, box: { x: 90, y: 460, w: 900, h: 900 }, camera: { fov: 30, pos: [0, 0.4, 7.5] },
  lights: { rim: { color: "data", intensity: 3 } },
  objects: [{ kind: "globe", radius: 1.6, rot: [12, 0, -18], spin: 40, atmosphere: "data", glow: { color: "data", size: 4.4, strength: 0.5 } }] });
// tower rise: staggered growth out of the ground while the camera orbits 35 degrees
VEOS.fx.three({ id: "towers", t_in: 5, t_out: 7, box: { x: 0, y: 300, w: 1080, h: 1200 }, ground: { size: 5 },
  camera: { fov: 32, target: [0, 1.6, 0], orbit: { radius: 10, height: 3, from: -25, to: 10 } },
  objects: [0, 1, 2].map(i => ({ kind: "tower", width: 0.9, height: 1.5 + i * 1.2, floors: 3 + i * 3, pos: [(i - 1) * 1.5, 0, 0],
    color: i === 2 ? "primary" : "paper", keys: [{ at: 0.12 + i * 0.12, scale: [1, 0, 1] }, { at: 0.5 + i * 0.12, scale: 1, ease: "expoOut" }] })) });
// chrome title: bright chrome (built-in studio reflections), a shadow, a violet halo
VEOS.fx.three({ id: "chrome", t_in: 0, t_out: 2, z: 8, kind: "lockup", text_class: "TC-display", box: { x: 0, y: 830, w: 1080, h: 660 },
  camera: { fov: 30, pos: [0, 0, 9] }, objects: [{ kind: "text", text: "4 APPS", slot: "display", weight: 900, italic: true, size: 1.05, depth: 0.35, material: "chrome", glow: { color: "primary", size: 5, strength: 0.35 } }] });
// phone hero: fills its box (camera fit), island, rounded screen; insert record passes straight through
VEOS.fx.three({ id: "hero", t_in: 2, t_out: 5, insert: "I2", box: { x: 220, y: 300, w: 640, h: 1100 },
  objects: [{ kind: "device", screen: "my-app-shot", rot: [0, -24, -6], keys: [{ at: 0, rot: [0, -40, -6], scale: 0.9 }, { at: 0.4, rot: [0, -24, -6], scale: 1, ease: "expoOut" }] }] });
// product turntable: a phone slab with the creator's screenshot on its screen, on a glowing plinth
VEOS.fx.three({ id: "phone", t_in: 7, t_out: 10, box: { x: 140, y: 380, w: 800, h: 1100 }, ground: { y: -1.15, size: 4 },
  camera: { fov: 30, pos: [0, 0.5, 7] },
  objects: [{ kind: "device", screen: "my-app-shot", rot: [0, -30, 0], spin: 60 },
    { kind: "cylinder", radius: 1.25, height: 0.04, pos: [0, -1.15, 0], color: "night", emissive: "primary", glow: { color: "primary", size: 2.6, strength: 0.35 } }] });
```
**Budget** (SwiftShader, measured on the fixture): steady frames take 45-150 ms. Text with a shadow at 1080x900 takes about 50-85 ms, the globe at 900x900 about 70-95 ms, three towers with a shadow about 100-150 ms, and the device with its plinth about 70-95 ms. The first frame of each scene takes 300-500 ms (geometry, text trace, shader compile). `quality.scale: 0.75` roughly halves the cost, and `aa: true` adds about 40%. Keep the halo's `glow.size` inside the box: a sprite larger than the view is cut off at the box edge.
