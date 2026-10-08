# Monochrome Metaphor: evidence map (App. B)

**Sources.** `vibe-editing-os-research/analysis/short/dan-koe.md` and the frame sheets in `evidence/short/dan-koe/v01–v03/sheets` (hook at 6 fps, the whole video at 1 fps), plus `meta.json` / `cuts.json`. No transcripts exist: spoken words were read from the burned-in captions. Sound is not observable.

| id | What | Duration | Cuts | Notes |
|---|---|---|---|---|
| v01 | Text-only black card (0–5.12 s), then a seated talking head with gold serif captions | 38.1 s, 24 fps | 1 (@ 5.12) | F-A |
| v02 | Voice-over metaphor animation (dots, megaphones, hammer, phone, dot grid, progress bar, globe) | 50.3 s, 29.97 fps | 0 | F-B |
| v03 | Voice-over metaphor animation (icon swirl, eye-clock, lighthouse, hourglass, spiral spotlight) + book end card | 25.1 s, 30 fps | 0 | F-B + product card |

## Measurements (taken on this template's behalf)
Sheets are 300 px-wide cells, so 1 cell px = 3.6 px on 1080 × 1920. Text widths were matched to the bundled fonts with PIL (`getlength`).

| Value | Measured | Method | Template value |
|---|---|---|---|
| F-A caption size | "and extremely uncomfortable" 691 px → 62 px; "to fit the environment" 515 px → 62 px; "as you grow into that" 490 px → 61 px (EB Garamond 400) | v01 s_02 cells r1c0, r0c2, r2c2 | 60 px (CS-A) |
| F-A caption centre y | 1366–1381 | same cells | 1372 |
| Cold-open size / y | "is to rip yourself out" 518 px and "and digital environment" 630 px → 68 px; centre y 959 | v01 s_01 r0c1, r0c4 | 68 px at y 960 (CS-A0) |
| F-B caption size | "with endless scrolling" 454 px → 43–44 px; "Numb your mind" 360 px → 44 px (Poppins 400) | v03 s_01 r0c5, r0c4 | 44 px, weight 500 (E3 floor) |
| F-B caption centre y | ≈ 1543 (in the IG bottom band) | v03 s_01 row 0 | 1470 (NC-5 lift) |
| Split title | "INTO A VIDEO GAME" 515 px → ≈ 46–50 px Montserrat 400 with tracking; lines at y ≈ 746 and ≈ 1160 | v02 s_01 r0c0; full-res v02 @ 0:00.5: cap 37 px, 425 px wide → Montserrat 500 ≈ 50 px | 50 px, y 746 / 1160 |
| Motif dot | Ø ≈ 43 px at (540, 960); stays centred 0:01.5–0:02.83 | v02 hook_01 rows 2–3 | Ø 40 (TUNE 30–48), centre (540, 960) |
| Object sizes | hammer ≈ 180 px tall (17% width); phone 450 × 846 (42%); dot field 612 px (57%); progress bar 864 × 80 (80%); screen 864 × 432; globe ≈ 396 px (37%); eye ≈ 420 px (39%) | v02 s_01–s_03, v03 hook_01 | 35–55% typical, 15–80% limits |
| End card | line at y 180–263; cover ≈ x 170–912, y 403–1512 | v03 s_02 r0c4–5, r1c0 | line y 230; cover x 220–860, y 360–1320 (kept inside the safe box) |
| Caption chunk rate | v01 ≈ 1 chunk / 1.2–2.0 s, 3–5 words; v03 ≈ 1 chunk / s, 1–4 words | 1 fps sheets | CS-A 3–5 words; CS-B 1–4 words |
| Scenes per minute | v02 ≈ 13; v03 ≈ 22 | sheets | 12–24 per 60 s |

## DNA rule → evidence
| Rule | Evidence |
|---|---|
| Black void, greyscale light; the only chroma is the F-A caption gold (D3, §4, H8) | v02 all frames; v03 0:00–0:20; v01 captions 0:05–0:37 gold #FCC31E (full-res sample 2026-10-06; the 1 fps sheet read #E8A83C) |
| Zero hard cuts in F-B, scenes morph (D2, §9, §23, H4) | `cuts.json` v02 [] and v03 []; morphs: v02 @ 0:16–0:17 (dot → bar), 0:33–0:41 (bar → screen); v03 @ 0:01.83–0:02.5 (push into the pupil → lighthouse) |
| The dot as "you", recurring (D4, §23.2, H5) | v02 @ 0:01.5, 0:03–0:09 (grows), 0:17, 0:18–0:25 (hops in the phone); v03 @ 0:00 (swirl centre), 0:11–0:20 (light source) |
| One literal object per idea (D1, §8.3) | v02 hammer and nail 0:10–0:15; phone feed 0:18–0:25; v03 eye-clock 0:00.67–0:01.67; lighthouse 0:02.5–0:06; hourglass 0:07–0:09 |
| Quiet type, no emphasis (D5, §5.3) | v01 all chunks lowercase, gold, no bold; v03 all chunks plain sentence case, no colour change |
| Chunk wipe captions (CS-B) | v03 @ 0:00.13–0:00.27 "You weren't born" revealed L → R in 5 f; @ 0:01.77–0:01.90 "to work 40" erased R → L in 4 f; @ 0:06.05–0:06.57 erase, 3 f gap, "and wake up one day" reveal in 7 f (full-rate bursts) |
| Cold-open card, then one cut (HA-12 F-A, T-CARD-CUT) | v01 hook_01 0:00–0:02.83 and s_01 0:00–0:04; cut @ 5.12 |
| Static seated framing, no zoom (H12, `zoom_policy: none`) | v01 s_01–s_03: identical framing at every 1 fps sample |
| Atmosphere hook (HA-15) | v03 hook_01 0:00–0:03; v02 hook_01 0:00–0:03 |
| Split title over the motif row (HA-12 alternate, P-SPLIT-TITLE, T-BREATH) | v02 hook_01 0:00 (blurred), 0:00.17 (near-black), 0:00.33–0:01.17 (sharp), 0:01.33–0:01.5 (fading) |
| Light burst ≤ 50% of the frame (P-FLARE-BOWTIE) | v03 @ 0:00.67 bow-tie flare |
| E4 ambient field | v03 @ 0:00–0:00.5 icon swirl; v02 @ 0:26–0:32 dot field |
| Lit objects (engine 3D, `VEOS.fx.three`) | v03 lighthouse 0:02.5–0:06, hourglass bulbs 0:07–0:09; v02 sphere 0:41, globe 0:42–0:49 |
| Product end card (§25) | v03 @ 0:21–0:25 |
| Spotlight wedge + X strike (P-SPIRAL-SPOTLIGHT, P-STRIKE-X) | v03 @ 0:12–0:20 |

## Unverified (default TUNE / VAR)
- `profile.language.speech` (en): read from captions; no transcript.
- Sound (bed, cue moments): not observable; the calm pack defaults are used.
- `formats.F-A.cadence.max_gap_s` (none): one reel of evidence only (v01).
- F-A grade and set: one reel (cool slate wall with two light strips, black tee).

## Inferred, not seen
- The motif states `seed`, `dim` and `source`, and the invented patterns (P-LADDER-CLIMB, P-SCALE-TIP, P-DOOR-SPILL, P-CHAIN-BREAK, P-MAZE-THREAD, P-ROAD-VANISH, P-WAVE-SETTLE, P-SEED-TREE, P-MIRROR-HORIZON, P-DOT-AMONG, P-DOT-ORBIT): built from the same grammar so the style covers any niche.
- The light curve (cost = dim, turn = brightest): generalised from v03's spiral → light source and v02's dimming between scenes.
- The keyword and handle end cards: quiet variants of v03's product card.

## Known gaps / engine requests
1. **E3 weight floor 500** forces Poppins Medium where the evidence is Regular (400). Request: allow weight ≥ 400 under E3 when contrast ≥ 10:1.
2. **V-CONTINUITY / E-19 is not built** (capability `continuity` false): the morph chain and the dot's presence are checked by review only.
3. ~~Lit-object recipes and 3D~~ now built-in (`VEOS.fx.three`); the globe still has no landmasses (no geo bundle).
4. **`fx.ambient` is not marked as continuous motion**: it sets `fx: "ambient"` and passes its `kind` ("void") as the scene kind, so V-CADENCE / V-F0 don't count it. The playbook works around this with `extra: {continuous: true}`.
5. ~~No `wipe` caption swap~~ now built-in (CS-B `swap.type: "wipe"`).
6. ~~V-CANVAS minimum move 0.5 s~~ now built-in: a zoom-through may take 0.25 s (the push-through is 9 f).
7. **Canvas-camera roll** exists now but stops at 20° and 2°/frame; C-6's 50° roll in 20 f stays the scene's own scale + rotate (at the measured values).
8. **No displacement / lens-warp filter** for the end card's un-warp entrance (shipped as scale + blur).

## Motion (completeness audit 2026-10-07, every frame)
Method: ffmpeg scene detection (threshold 0.2: v01 one cut @ 5.125, v02 none, v03 one change @ 0.77 = the flare); per-frame luma / lit-area / ORB affine (`estimateAffinePartial2D`) on all frames at 270 px; full-rate bursts at 360 px. Strips: `docs/audit/monochrome-metaphor/strip-*.jpg`.

| Device | Measured | Where |
|---|---|---|
| F-A camera | scale 1.000/frame, p95 translation 0.7 px/frame on the wall strips: locked off | v01 @ 5.3–38 |
| F-A card swaps | hard, 0 f; card pixel-still between swaps (frame diff 0.000); phrases @ 0, 0.71, 1.38, 2.96, 3.75; cut @ 5.083 | v01 @ 0–5.1 |
| F-A caption swaps | hard, 0 f | v01 @ 6.06 |
| CS-B | chunk wipe L → R 5–7 f, erase R → L 4–6 f, gap 3–4 f | v03 @ 0.13, 1.77, 6.05 |
| Hook snap | dots → clock gauge in 4 f; bloom swell wipes icon field in 2 f | v03 @ 0.20–0.30, 0.47–0.50 |
| Flare reveal | slit → bow-tie → wash in 3 f, peak frame mean luma 96/255, lit area 32%; decay 8 f | v03 @ 0.67–1.0 |
| Push-through | object contracts ~0.65× over 12 f, pupil-clock → dot; push ≥ 4× in 9 f ease-in; 2 f dissolve; ground widens 3 f, tower rises from 2.57 | v03 @ 1.70–2.57 |
| T-SINK | beam swings to lens 4 f, off 1 f, tower sinks 8 f, ground fades 4 f, lamp left as the dot | v03 @ 6.12–6.72 |
| Cost dimming | hourglass scene frame mean luma 1–4/255 (dimmest stretch of the reel) | v03 @ 6.7–9.9 |
| Zoom-out with roll | scene ~3× → 1×, roll −5° → +45° over ~20 f on "zoom out"; comet streak settles as the dot | v03 @ 9.97–10.67 |
| Camera creep | spotlight scene +0.3–0.8% per 0.5 s; lit tower and end card still (scale 1.000) | v03 @ 12.5–20, 3–6, 22–25 |
| T-COLLAPSE-DOT | wedge narrows to a line 6 f, scene retracts to the dot, 2 f dark; cover un-warps from a lens/whirl distortion over 8–10 f | v03 @ 20.68–21.25 |
| End line | letters flicker on in place, random order, 21.83 → 23.0 | v03 |
| T-FLICKER (hook on) | 2 black f, then dim/dim/dim/off/dim/full over 9 f | v02 @ 0–0.33 |
| Chomper | lit row shrinks 15.3 px/f → one 118 px dot per ~7.7 f | v02 @ 0.67–1.33 |
| T-FLICKER (off) | title + row off in 8 f with one 1 f flash back | v02 @ 1.33–1.57 |
| Held still | lone dot, frame diff < 0.05 for 26 f (0.87 s) | v02 @ 1.64–2.5 |
| Emitters | pop on within 2 f; group rotates 13°/s (0.43°/f), scale 0.97 per 0.5 s @ 5–7 | v02 @ 2.74–9.5 |
| T-FLICKER-SWAP | old/new scenes alternate 7 f; grown dot shrinks into the nail head | v02 @ 9.53–9.77 |
| Dot falls | nail head falls y 1058 → 1355 over ~35 f (ease-in), phone rises at 17.3 | v02 @ 16.0–17.6 |
| T-FLICKER (off/on) | phone dims, out, back dim, out (12 f); black 0.43 s; field flickers on 10 f | v02 @ 25.8–26.6 |
| Bar fills | fill ~0.9 s, reset in 1 f, ×3; bar → screen height 84 → 436 px over 48 f | v02 @ 33.0–37.8 |
| T-CRT-OFF | screen flickers, squashes to a 4 px line in 5 f, black 4 f, globe flickers on 8 f | v02 @ 41.9–42.6 |
| Pacing | F-B scenes median ~4 s (v03 2.4, v02 5.9), p90 ~8.5 s; frames with visible change v03 89%, v02 49% | all |

## Fidelity audit 2026-10-06 (full-resolution frames, 1080 × 1920 native)
Frames: v01 @ 0.0, 2.0, 5.5, 6.4-6.7 (4), 9.0, 14.0, 30.0, 37.5; v02 @ 0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 8.0, 17.0, 30.0, 45.0, 49.5; v03 @ 0.0, 0.3, 0.6, 1.0, 1.07, 2.0, 3.0, 4.0, 12.0, 15.0, 22.0, 24.8. Report: `docs/audit/monochrome-metaphor/audit.md`.
| Measure | Value | Frame |
|---|---|---|
| F-B ground | #000000 at corners and centre | v02 @ 17, 30; v03 @ 12 |
| CS-B | Poppins 400, "You weren't born" 354 × 35 px → 43 px; colour 242-255 grey; cy ≈ 1537 | v03 @ 0.3, 4.0 |
| CS-A0 card | EB Garamond ≈ 66 px white, cy 960 | v01 @ 2.0 |
| CS-A gold | #FCC31E core, cy 1374, ≈ 62 px | v01 @ 9.0, 14.0 |
| Dot | Ø 40 core, glow falls to 0 over ≈ 24 px | v02 @ 2.0 |
| Dot row | 9 dots Ø 46, cy 961, x 42-1034 | v02 @ 0.5 |
| Outline art | ≈ 4 px white core + bloom | v02 @ 3.0 (megaphones) |
| End line | Montserrat 500 caps, cap 48 px → ≈ 60 px, cy 180 / 262 | v03 @ 24.8 |

## Engine built-ins (2026-10-07, engine cc324ec+)
| Device | Before (workaround) | Now built-in | Measured value now used |
|---|---|---|---|
| CS-B chunk wipe | `blur` swap 6 f in / 5 f out | caption `swap: {type: "wipe", frames: 6, out_frames: 5, dir: "right", out_dir: "left", feather_px: 40}` | L → R in 5–7 f, R → L out 4–6 f (v03 @ 0:00.13, 0:01.77, 0:06.05) |
| T-PUSH-THROUGH push (C-4) | 15 f zoom-through (V-CANVAS 0.5 s floor) | zoom-through may take 0.25 s (snap speed) | 9 f, ×5, ease in (v03 @ 0:02.13–0:02.43) |
| Lit tower, globe, sphere (B-4) | flat 2D gradient + rim + bloom (`lit_cylinder`, `lit_sphere`) | `VEOS.fx.three` (`cylinder` + emissive lamp, `globe`, `sphere`), one 3D scene at a time | tower 420 px tall, rises 18 f, sinks 8 f (v03 @ 0:02.47–0:06.72); globe Ø 400, 0.6°/f (v02 @ 0:42–0:49); sphere rises 24 f (v02 @ 0:41) |

Still not built-in: **C-6 zoom-out roll** (50° in ≈ 20 f; the canvas camera's roll stops at 20° and 2°/frame, so the scene keeps its own scale + rotate at the measured values) and the **lens / whirl un-warp** card entrance (no displacement filter; still scale 1.25 → 1 + blur + fade).

## Template values pass 2026-10-07 (defaults, no switches)
- P-LIT-TOWER: the rim light moves to the right and slightly behind (pos [6, 2.5, −1.5], intensity 4.5, was [5, 2, −3] at 2.4), so the column's right edge reads as the measured bright rim (v03 @ 2.5–6; stills v3 showed no visible rim).
- The tower camera is z 15 (was 11): the column renders ≈ 420 px tall as measured (z 11 gave ≈ 630 px).
