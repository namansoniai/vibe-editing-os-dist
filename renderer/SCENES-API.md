# SCENES-API: how to write `plan/scenes.js`

You write the visuals of each reel as **scenes**: bespoke code on top of the renderer skeleton. There is no component library to pick from; the playbook says *what* to show and when, you decide *how it looks* and paint it. Canvas is 1080x1920 px, 30 fps, every frame a pure function of `n`.

Files: `plan/timeline.json` (beats, stage, world, camera, captions, sfx, audio; no layers), `plan/scenes.js` (this), optional `plan/assets/*` (images; `ctx.asset("<file stem>")` returns a URL). Contract details: `CONTRACT.md`.

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
| `behind: true` | depth sandwich: between the footage and the person cut-out (text/objects appear behind the speaker). Only when the stage shows footage |
| `in`, `out` | enter/exit presets (section 5). Default in `settle`, out `none`. Use `in: "none"` when you animate the entrance yourself |
| `box: {x,y,w,h}` | declared footprint (also the preset transform origin; the rect used for canvas-drawn scenes) |
| `roles: [...]` | bright colour roles you use (`primary accent bad good data concept comedy`); at most 3 bright roles on screen at once; `comedy` only in mock beats |
| `events: [s, ...]` | LOCAL seconds (after `t_in`) when something visibly changes inside the scene (word swap, pulse, bar grows). Declare every one: they count for the "something changes every 1.5 s" rule (M7) and for "starts on the trigger word" (M6) |
| `text: true`, `text_content: "..."` | set when it carries text; `text_content` is that text as one string (storyboard + checks) |
| `overlaps: ["B", ...]` | scene ids this scene is *intentionally* nested on (a chip pinned on its card). Exempts the pair from the global G1 no-overlap check (use `"__subtitles"` for the auto-subtitles) |
| `cuts: [s, ...]` | LOCAL seconds of deliberate hard cuts (position/size snaps). Exempts those moments (+-2 frames) from the global G3 smooth-motion check |
| `may_overlap_face` | allowed to cover the face (captions, a label on the chest). Default: z>=5, non-behind scenes must stay 40 px clear of the face |
| `kind` | `"banner"` (the headline slab: exactly one chip, or a bad+good pair; <=9 words; <=2 lines; <=2 emoji; needs `chips: [{text, role}]`, `lines`), `"cta-keyword"` (the CTA keyword chip; `text_content` must contain `meta.keyword`), `"meme"` (comedy sticker/stamp; mock beats only) |
| `render(ctx, lt, dur)` | `lt` = seconds since `t_in`, `dur` = `t_out - t_in`. Return `ctx.html("<div ...>")`, or draw on `ctx.canvas()` and `return ""` |

Output of `render` is placed in a 1080x1920 absolutely-positioned layer at (0,0): position your elements with `position:absolute; left/top` in screen pixels.

## 3. The ctx toolkit
- Frame: `ctx.n`, `ctx.t` (edit seconds), `ctx.fps`, `ctx.W`, `ctx.H`, `ctx.scene` (your scene object), `ctx.stageName`, `ctx.world`.
- Tokens: `ctx.tokens` = `{colours, text_on, fonts, type, layout, motion, camera_presets, stage_morphs, tone, creator, ...}`. `ctx.col(role)` -> hex, `ctx.hexA(role, alpha)` -> rgba(), `ctx.tokens.text_on[role]` = readable text colour on that role, `ctx.fam(slot)` -> CSS font-family (`display chunky body numeric serif marker kinetic ui pixel mono`, with emoji fallback; use inside `font:` shorthand or `g.font`), `ctx.tokens.type.banner/chunky/subtitle/...` (weights, sizes, stroke, shadow, radius), `ctx.safe` = `{x:[64,1016], y:[110,1500]}` (text stays inside), `ctx.tokens.layout` (`banner_top`, `banner_x`, `caption_cy`, `card_zone`, `face_clearance`, ...).
- Face: `ctx.face()` -> `{x,y,w,h,cx,cy}` in output pixels after stage + camera transform, or `null` (stage hidden). Use it to place things clear of the head.
- Animation: `ctx.V(lt, inDur, outAt, {in, out, dout, op})` returns an inline `style` string (opacity/transform/filter) for a built-in enter/exit on one element, or `null` when it is not visible (`outAt` null = never exits). `ctx.ease.out | in | inOut | back | elastic` (each `p in 0..1` -> eased 0..1, `back` overshoots), `ctx.lerp(a,b,p)`, `ctx.clamp(x,lo=0,hi=1)`.
- Text: `ctx.measure(text, "800 60px 'Inter Tight'")` -> width px (use `ctx.fam` in the font string); `ctx.esc(s)` HTML-escapes.
- Assets/words: `ctx.asset(id)` -> URL (id = `timeline.assets` key or a `plan/assets` file stem/name; preloaded before READY; for a video asset it is its first frame), `ctx.videoFrame(name, seconds)` -> URL of the frame of a video asset (`veos asset add <video>`) at that LOCAL time: 30 fps, frame-exact (`floor(seconds*30)`), clamped to the first/last frame, decoded before the frame is captured, like footage (`""` for an unknown name). Use it in `<img src>` or `background:url(...)`, `ctx.word(i)`, `ctx.wordsBetween(t0, t1)` -> `[{w,s,e,caption?}]` in edit time for word-synced pops.
- Randomness: `ctx.rng(seed)` -> seeded PRNG that is stable per (scene, seed, frame): same frame, same numbers. `ctx.rngStable(seed)` is the same for every frame (static scatter).
- Output: `ctx.html(str)` (identity, marks intent), `ctx.canvas()` -> 2D context of a 1080x1920 canvas owned by this scene, cleared each frame (`ctx.canvasEl()` for the element, e.g. to set a CSS filter), `ctx.blur(px)` -> `url(#id)` for a vertical motion-blur filter (`filter:${ctx.blur(12)}`).

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
- `stage[].layout`: `full | low | panel | inset | slide-aside | bubble | hidden`; `via`: `cut | panel-drop | pop-back | slide-aside | bubble-shrink | bubble-grow`. `low` lowers the footage (`offset` default 380 px) to make room above the head for banner + caption + card.
- `world[].world`: `studio | canvas | data` (what is behind a non-full stage).
- `camera[].preset`: `snap-punch | crash-zoom | pull-out | push-drift | shake | zoom-through | rotation-snap | reset` (see `ctx.tokens.camera_presets` for tones and limits). Never the same preset twice in a row.
- Subtitles are automatic (hidden during `captions.hide` and while a z8 scene is active). Never write subtitle cards.

### Sound cues (timeline.json `sfx`, tied to your scenes)
Every sound is anchored to a visual moment you wrote here: `{"t": <edit s>, "id": "<catalog id>", "beat": N, "on": "<scene id>@<local s>", "why": "..."}`. `on` may name a scene's start (`L4@0`, `L4@in`), its end (`L4@out`) or any time you declared in that scene's `events` (`L4@0.5`); the cue `t` must be within 3 frames of that moment (`t_in + local`). So when you want a sound at an internal beat of a scene (a counter landing, a stamp), declare that time in `events`. Other anchors: `stage@t`, `camera@t`, `transition@t`. Contract: `CONTRACT.md` section 2; rules S1-S6: `engine/SPEC.md` section 6.

## 5. Enter/exit presets (`in` / `out`)
`settle` (scale 1.08->1 + blur, 8 f), `pop` (overshoot, 7 f), `squash`, `rise`, `drop`, `blur`, `stamp` (big -> 1, slight rotate), `slide-l`, `slide-r`, `rocket` (from below / off the top, vertical motion blur), `none`. Exit default is `none`; `rocket` is 8 f, others 5 f.

## 6. Determinism and safety
- A scene is a pure function of `(ctx, lt, dur)`. **No `Math.random`, `Date`, `performance.now`, timers, `fetch`, `<video>`, CSS animations/transitions.** Everything animates from `lt` (or `ctx.n`).
- Never hard-code role colours; use `ctx.col(role)` / `ctx.tokens`. Neutral black/white/shadows via `rgba()` are fine.
- Text uses `ctx.fam(slot)`; keep text inside `ctx.safe`; the banner uses `layout.banner_x`/`banner_top`.
- Do not rely on `document`/DOM state between frames. Preload nothing yourself; use `plan/assets`.
- Do not make a scene full-frame opaque unless it is z1-2.

## 7. Performance budget
Core + all scenes must render in **<= 30 ms per frame** (typical frame: 3-4 active scenes). Keep DOM under ~150 nodes per scene, avoid large `filter: blur()` / `backdrop-filter` stacks and `box-shadow` blurs on many elements, cap canvas paths per frame (~500), and do not build big strings or arrays each frame (hoist constants to top-level). `veos measure` reports `ms_per_frame` of the sampled frames.

## 7b. Global quality checks (`veos validate`, always on, every playbook)
They use the measured rects (`veos measure`; `veos validate` runs the per-frame motion measure itself when `plan/scenes.js` exists). Messages are plain English with the scene ids, the time and a fix.
- **G1 no overlap.** At every measured frame, text-bearing scenes, z>=5 non-`behind` scenes and the auto-subtitles (`"__subtitles"`) may not intersect by more than 2% of the smaller rect, unless one of the two declares `overlaps: ["<other id>"]` (deliberate nesting) or is z11. Fix: move the later scene (the hint says by how many px) or declare `overlaps`.
- **G2 no clutter.** At most 4 active scenes with z 3-10 (`behind` and z11 not counted) and at most 3 text elements (subtitles count). Fix: drop or merge one.
- **G3 smooth motion.** A scene's rect centre may not jump more than 90 px, nor its width/height change more than 25%, between two consecutive frames, except within 2 frames of its `t_in`/`t_out`, of a declared `events` time, or of a declared `cuts` time. Counters/typewriters whose text width changes every frame must declare their `events`. z11 and subtitles are exempt.

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
