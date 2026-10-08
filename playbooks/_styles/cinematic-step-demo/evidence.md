# Cinematic Step Demo: evidence map (template v1, inspired by Peter McKinnon)

**Sources.** `vibe-editing-os-research/analysis/short/peter-mckinnon.md`; frame sheets `evidence/short/peter-mckinnon/v01` (5-step notebook system, 109.9 s, 34 cuts) and `v02` (podcast clip, 47.4 s, 15 cuts), `meta.json`, `cuts.json`. Sources are 720 × 1280; positions are measured on the sheets (one cell = 300 px wide = 1080 / 3.6) and given on 1080 × 1920. No transcripts existed; speech was read from the burned-in subtitles. Sound is not observable.

## 1. DNA rules → evidence

| Rule (playbook id) | Value in the template | Evidence |
|---|---|---|
| Gold italic serif keyword inside a white grotesk caption (P-KEYWORD-SWAP, CS-1/2 emphasis `font_swap`) | Instrument Serif italic, `#D9A441` (F-A) / `#F5C518` (F-B), 1.3×, F-A span phrase | v01 @0:01.0 "system", @0:03 "Track habits", @0:05 "track everything", @0:12 "habit", @0:19 "September", @0:40 "index page", @1:00 "sticky", @1:11-1:13 "peel", "fresh", @1:28 "Double", @1:47 "notes"; v02 @0:01.33 "printing", @0:01.83 "photos", @0:04 "photographer" / "content", @0:10 "causing emotion", @0:19 "Instagram's", @0:27 "photos", @0:28 "Lightroom", @0:36 "lost", @0:41 "awful", @0:42 "buried", @0:45 "house" |
| Gold frequency ≈ 1 per 4 s (`max_per_s 0.25`) | ≤ 1 per chunk, ≤ 0.25/s | v01 ≈ 30 keywords / 110 s (16/min); v02 ≈ 12 / 46 s (15/min) |
| Gold is larger than the white words (`ratio 1.3`) | 1.3× (italic serif reads smaller at equal size) | v02 @0:01.33 "printing" cap height ≈ 1.3× "like,"; v01 @0:03 "Track habits" visibly larger than the white line |
| Gold colour | F-A `#D9A441`, F-B `#F5C518` (audit) | full-res audit: v01 glyph cores `#D9A441`-`#DDAE5A` (@0:01.2, @0:04, @0:06.6, @1:32); v02 `#F5C518`-`#FAD109` with a faint glow (@0:01.5, @0:04.4) |
| Word-by-word reveal (`reveal: word`) | each word appears on its onset | v01 hook sheet 0:00.17 "This" → 0:00.33 "This" → 0:00.83 "This is my" → 1.0 "This is my system"; v02 hook sheet "I'm wondering" → "I'm wondering sometimes" → "…sometimes if," |
| New word briefly dimmer (fade-in) | swap fade 2 f (unverified per-word fade) | v02 @0:19 "gone," grey; @0:42 "alive." grey; v01 @1:04 "forget" grey |
| Caption chunk 2-5 words, ≤ 2 lines | CS-1 3-5 words, CS-2 2-5 | v01 "Now I'll just / add whatever" (@0:21), "I found these / sheets here" (@0:42); v02 "What's interesting / about that is" (@0:18) |
| Caption size | CS-1 56 px 600 tracking −5%, CS-2 76 px | full-res audit (1080 × 1920): v01 cap height 37-42 px → 52-57 px (@0:01.2, @0:02.6, @0:08.5, @1:32), semibold, word spaces almost closed; v02 cap height ≈ 55 px → 76-80 px (@0:01.5, @0:09) |
| Caption position | CS-1 cy 1440 max_w 560, CS-2 cy 1385 | full-res audit: v01 blocks y 1490-1645 (cy ≈ 1565), block width 300-360 px, centred → lifted to the lowest compliant cy; v02 y 1300-1470 (cy ≈ 1385) |
| STEP tape (P-STEP-TAPE, TX-1) | black tape, square corners, JetBrains Mono 600 60 px caps, tracking 0.18 em, top 165, h 100, ≈ 300 px wide, centred | full-res audit v01 @0:08.5 "STEP 1": tape x 386-687, y 165-264 (pure `#000000`), letters cap height 44 px (y 194-238), x 396-664; hand-inked typewriter face; @1:32 recap the same; @0:38 STEP 2; @0:47 STEP 3; @1:07 STEP 4; @1:25 STEP 5 |
| Tape hold 2.0-3.5 s, gone before the step ends | default 2.5 s | STEP 1 visible @0:08-0:10, gone @0:11 (still overhead); STEP 2 @0:38-0:39; STEP 3 @0:47-0:49; STEP 4 @1:07-1:08; STEP 5 @1:25-1:27 |
| Tape never over the desk A-roll | H6 | STEP 2 exits before the desk shot @0:40; no tape on any desk frame |
| Recap strip with tape swaps (P-RECAP-STRIP, E6) | 1.2-2.0 s per step | v01 @1:31-1:43: STEP 1 (1:31-1:32), 2 (1:33-1:34), 3 (1:35-1:38), 4 (1:39-1:40), 5 (1:41-1:43), caption "You've got your *tracker*, … *index* page, … adhesive on the back, … long *form Post-it*, … *custom*" |
| Overhead hand demo on a patterned rug (P-OVERHEAD-PLATE, L-overhead) | 45-80% of F-A | v01 ≈ 70%: @0:00-0:02, @0:08-0:37, @0:44-0:49, @1:07-1:16, @1:22-1:29, @1:31-1:43; rug red ≈ `#8C1C22`, navy ≈ `#233A5E` |
| Object zone above the caption band | y 200-1250 | v01 notebook spans cell y ≈ 80-430 (≈ 290-1550) in close passes; the caption sits on the rug or fingers @0:13, @0:20-0:24 |
| Desk A-roll (L-desk) | head top 220-360, face centre x 420-660 | v01 @0:06 head top ≈ 238, @0:57 ≈ 270, @1:17 ≈ 250; face centred |
| Presence F-A 20-50%, max absence 30 s | share [20, 50], `max_absence_s 30` | face ≈ 30% of v01; the longest face-free run @0:08-0:39 (31 s) |
| Held-to-camera / angled inserts (P-HELD-TO-CAMERA, P-ANGLED-HERO) | SH-4 | v01 @0:02.8-0:05 (angled notebook, dark background, rack), @0:38-0:39 (index page held), @0:53-0:56 (sticker sheet), @1:31-1:43 |
| Desk show (P-DESK-SHOW) | in the A-roll | v01 @0:41 (sheet held up), @1:05 (red sticky note), @1:48 (notebook) |
| State jump (P-STATE-JUMP) | same framing, later state | v01 @0:34 → 0:35 (empty grid → filled grid, "It starts to fill") |
| Hidden cuts on hand motion (T-02/T-03, R-1) | ≥ 60% of overhead cuts | v01 cut 0.1 (notebook flip), hand swipes @0:01.5-0:02.0, cut @0:34.57-0:34.73 (three cuts inside one swipe), @1:12 (flip) |
| Hook F-A (HA-14 result in hand) | §6.2 | v01 @0:00 result flip (cut 0.1) → 0:00.33 filled tracker sharp → 1.0 gold "system" → cut 2.77 angled notebook → 0:03-0:05 benefit run with gold words → 0:06 desk → 0:08 STEP 1 |
| Hook F-B (HA-14 cold open) | §6.2b | v02 @0:00 Peter mid-sentence, first word 0.17, gold "printing" 1.33, first cut 5.03 |
| Cadence | cuts/min 14-26; median 1.8-3.6 (F-A), 2.0-4.2 (F-B); max gap 5.0 / 6.0 | `meta.json`: 18.6 / 19.0 cuts/min; median 2.60 / 2.77 s; longest gaps v01 24.67-31.33 (6.7 s, continuous writing), 57.0-66.9 (9.9 s, desk monologue with gestures); v02 15.77-21.7 (5.9 s) |
| F-B speaker cuts, reactions (§20, R-6/R-7) | handover ±3 f, reactions 1.0-2.6 s | v02 cuts 5.03, 8.2, 11.07, 15.77, 21.7, 24.47, 28.6, 29.67, 35.3, 36.77, 38.47, 40.13, 41.3, 43.57, 46.13; reaction-length shots 28.6-29.67 (1.1 s), 35.3-36.77 (1.5 s), 40.13-41.3 (1.2 s) |
| F-B framing | tight singles, eyes ≈ y 600, mic in frame | v02 all frames |
| F-B ends on a reaction | P-BUTTON-END | v02 @0:43 "Yeah, yeah." smile, @0:46 face-palm laugh |
| Tungsten grade (GR-tungsten) | warm, contrasty, slightly desaturated, vignette | every frame of v01 and v02: crushed blacks, amber practicals, skin warm, background falls off |
| No headline, no emoji, no banner | H4, N1 | none in either video |

## 2. Inferred (not observed; added for hands-on niches)
- **P-TOOL-TAPE, P-MEASURE-TAPE, P-WAIT-TAPE, P-NAME-TAPE, P-CTA-TAPE:** extensions of the STEP tape (the style's only label device). v01 never labels a tool on screen.
- **Created inserts (P-SCREEN-INSERT, P-PHOTO-PRINT, P-PRODUCT-TAPE, P-QUOTE-CARD):** required by the ask-then-create policy; styled on the warm-black desk world to stay in the look. v02 mentions Lightroom and Instagram (@0:19, @0:28) without showing them; the template keeps that as caption-only by default.
- **P-RESULT-FLASH re-hook:** the structure's `standard` class needs one mid-reel re-hook; v01 has none (its 110 s run relies on the step count).
- **CTA devices:** neither video has an on-screen CTA; the default is `none`.
- **F-B guest caption cream:** v02 uses white for both speakers; the engine's speaker check needs distinct styles.

## 3. Unverified values (default to TUNE)
| Path | Why |
|---|---|
| `profile.language.speech` | No transcript; English read from the burned-in subtitles |
| `sound.bed` | Sound not observable |
| `captions.profiles.CS-1.swap` (per-word fade length) | Sheets at 6 fps show a grey new word; the exact frames are unknown |
| `grades.footage` numbers | Estimated from graded frames, not from a LUT |

## 4. Known gaps (engine)
- **Now built-in: E-16 grades.** The engine applies `grades.footage` (GR-tungsten, vignette 0.50, bloom 0.12) to the stage footage; the z4 `backdrop-filter` grade-pass scene is retired. Core leaves video assets natural, so z1 plates set `ctx.grade(ctx.gradeId || "GR-tungsten", {spatial: true})` themselves (P-GRADE-PASS). Drawn graphics (W-desk card chrome, tapes) are no longer darkened by a pass; their palette is already tungsten.
- **Now built-in: per-line caption fit.** CS-1 and CS-3 `skin.line_fit: "block"`: lines grow to the widest line (v01 @0:02, both lines x 363-717), replacing "both lines at 56 px".
- **Now built-in: T-08 white flash.** `timeline.transitions[]` `type: "flash"` (7 f, pre 2, peak 1.0, decay 0.4, white, `layers: picture` so it covers the z1 plates; NC-11 enforced by V-FLASH) replaces the bespoke z5 flash scene. Still approximated: the measured 2 f top → bottom reveal clears uniformly (a `curtain` on the same cut would overlap the flash, which V-FX rejects).
- **E-24 motion-matched cut points:** hand-swipe frames are picked by reading contact sheets; no detector exists.
- **Overhead clips as assets:** `veos asset add` scales videos to 1080 px wide, so overhead clips must be shot vertical; a horizontal overhead falls back to P-PLATE-BAND.

## 5. Fidelity audit (full-resolution frames, 2026-10)
Frames pulled one at a time from the 720 × 1280 originals and measured on a 1080 × 1920 upscale (`docs/audit/cinematic-step-demo/`).

| Ref | What it settled |
|---|---|
| v01 @0:01.2, @0:02.6 | caption block x 363-717, y 1534-1626; line 1 cap height 37 px, semibold, tracking ≈ −5%; line 2 size-fitted to line 1's width (block justify); gold `system` glyph cores `#D7BA6E`/`#C9923C` |
| v01 @0:04.0, @0:06.6, @1:32 | gold runs over 2-word phrases ("Track habits,", "track everything"); gold `#D9A441`-`#DDAE5A`; white line cap ≈ 40 px |
| v01 @0:08.5, @0:38.6, @1:32 | STEP tape x 386-687, y 165-264, `#000000`, square corners, letters cap 44 px |
| v01 @0:06.6, @1:47.5 | A-roll head top ≈ y 248, face y ≈ 380-820; frame mean `#28201B`, above-head `#0F100F` (darker grade) |
| v02 @0:01.5, @0:04.4, @0:09, @0:29 | caption cy ≈ 1385, 76-80 px; gold `#F5C518`-`#FAD109` with faint glow; two gold words in one chunk; face y ≈ 450-1170 |

## 6. Completeness audit (motion at full frame rate, 2026-10)
Every frame of v01 (3297) and v02 (1421) measured: ORB + `estimateAffinePartial2D` per frame pair (scale, rotation, translation), a tape-band and caption-band pixel timeline, scene detection at threshold 0.2; bursts tiled in `docs/audit/cinematic-step-demo/strip-*.jpg`.

| Ref | What it settled |
|---|---|
| v01 7.73, 37.77, 46.80, 66.90, 84.93, 91.13 (tape band, strip-step-entry) | The STEP tape pops on complete on the cut frame (letter pixels constant from frame 1) and goes off hard on the next cut: 11.10 (cut 11.23), 40.43, 49.90, 69.03, 87.70, 104.17. Holds 2.1-3.4 s (mean 2.8) |
| v01 91.1-104.2 (strip-recap) | Recap = one hand-held overhead flip-through (1 hidden cut at 93.33); tape STEP 1 → 5 at ≈ 91.1, 93.1, 95.0, 98.6, 101.3, each after the spoken ordinal ("…tracker, one."); 13.0 s for 5 steps |
| v01 34.57-34.77, 37.57-37.77 (strip-flash) | White flash transition: 2 f bluish bloom, 3 f solid white, 2 f top-to-bottom reveal; at the state jump "It starts to fill" and into STEP 2. No other flash in v01; none in v02 |
| v01 f30-35, f86-100; v02 f37-42 (strip-captions) | Each caption word fades in over 3 f with a slight blur; the chunk clears hard (f90 full → f91 empty); the gold word enters the same way; v02 gold has a faint glow |
| v01 0.0-3.0 (strip-hook) | f0-f2 a blurred flip, cut f3, notebook swings open f4-f9, sharp f10; scene-detector hits 1.7-2.7 are hand passes inside one shot; the 2nd real cut is 2.77 |
| v01 2.77-4.57 | Angled hero insert pushes 1.00 → 1.22 (ease-out, ×1.13 by 3.3 s) and racks soft → sharp by ≈ 4.3 s (≈ 40 f) |
| v01 60.9, 80.8, 89.7, 107.8 / 90.2 (strip-jump) | Desk jump cuts: same framing (scale 1.00) in 4 of 5; one re-crop 1.07 |
| v01 57.0-66.9 | Desk camera drift 1.00 → 1.024 over 9.9 s; all other scale changes trace to hands or subject motion; no rotation or shake anywhere (v02 per-shot drift ≤ ±7%, subject motion) |
| v01 / v02 cut lists | v01 43 real cuts (false hand-pass hits removed, desk jump cuts added): 23.5/min, median 1.98 s, p90 4.7 s, longest 10.8 s (the recap, carried by tape swaps); v02 15 cuts, 19.0/min, median 2.67 s, p90 5.3 s, longest 5.9 s |

## Template values pass 2026-10-07 (defaults, no switches)
- T-08 flash now clears as measured: `clear: "wipe"`, `clear_frames: 2`, `dir: "down"` (the 2 f top → bottom reveal, v01 34.57 / 37.57). The uniform-clear approximation is gone.
