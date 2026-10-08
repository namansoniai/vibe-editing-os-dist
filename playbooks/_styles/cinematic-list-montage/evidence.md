# Evidence map: Cinematic List / Montage (inspired by ant.lon)

Sources: `vibe-editing-os-research/analysis/short/ant-lon.md`; frame sheets `evidence/short/ant-lon/v01–v05/sheets/*.jpg` (hook at 6 fps, whole video at 1 fps, all sheets read); `meta.json` and `cuts.json` per video. Sources are 720×1280 at 24–25 fps; every px value below is converted to the 1080×1920 frame (sheet cell 300×534 → ×3.6; 720 p → ×1.5). Transcripts were unavailable for all five videos: spoken content is read from the captions.

| Video | Topic (from captions) | Duration | Cuts/min | Median shot | Format |
|---|---|---|---|---|---|
| v01 | "Picture this: 2 editors improving over 6 months" (parable) | 66.7 s | 28.8 | 1.32 s | F-B |
| v02 | "Creating banger videos in 2026 isn't hard" (7 steps) | 55.0 s | 26.2 | 1.04 s | F-B |
| v03 | "10/10 video editing habits" (list) | 34.3 s | 0.0 | 34.25 s | F-A |
| v04 | "10 ways to earn money as a video editor" (list) | 28.8 s | 0.0 | 28.84 s | F-A |
| v05 | "Editing better videos 101" (3 things) | 75.7 s | 26.1 | 1.56 s | F-B |

## DNA rule → evidence
| Rule (playbook id) | Value in the template | Evidence (video @ time, measurement) |
|---|---|---|
| Two formats (§0.4) | F-A 0 cuts; F-B 26–29 cuts/min, median 1.0–1.6 s | `meta.json`: v03/v04 0 cuts; v01 28.8, v02 26.2, v05 26.1; medians 1.32 / 1.04 / 1.56 |
| Burst / breath rhythm (§7.5, H5) | bursts of 3–6 plates at 0.4–1.0 s, breaths of 2–6 s | `cuts.json` v01: 16.08–18.84 (7 cuts in 2.8 s), 39.36–40.28 (4 cuts in 0.9 s), then 40.28 → 48.48 (8.2 s on the face with graphic events); v02: 33.4–35.4 (6 cuts in 2 s); v05: 6.32–8.24 (7 cuts) |
| Cobalt chip title (§5.2, P-01) | `#2B35E8`, cy 400, 104 px serif (F-A) / 88 px grotesk (F-B), radius 4 | v03 @0:00–0:02.8 chip centre y ≈ 112/534 → 403 px, chip ≈ 220/300 wide → ≈ 790 px, glyph height ≈ 28 cell px → ≈ 100–110 px condensed serif; v04 @0:00.17–0:04 same chip, sweeping in rotated from top-left and settling (cy 288 → 396 by 2 s); v05 @0:00.17–0:04.5 grotesk chip typed L→R, tilted, settling at cy ≈ 420 |
| Sub-line (P-03) | serif 56 px, cy 515, built word by word | v03 @0:00.17–0:01.3 "you need to lock in" at cell y 143 → 515 px, ≈ 16 cell px glyphs; v04 @0:00.67–0:01.7 "as a video editor" |
| Behind-head numeral (P-04, E1) | ≤ 1 per reel, hook | v05 @0:00–0:04 translucent italic "101" behind the head; v02 @0:04–0:05 "BY STEP" occluded by the head |
| Micro captions CS-1 (E3) | 44 px, cy 1130, one word | v03 @0:00.17–0:33 one word at cell y 310 → 1116 px, x-height ≈ 7 cell px → ≈ 44–48 px font; v04 @0:00–0:28 cell y 316 → 1138 px |
| Keyword slam F-A (P-12) | tier 2 grotesk 800, 110 px, ≈ 1 per 6–10 s | v03 @0:08 "anything", @0:20 "edit", @0:32–0:33 "build", "earn" |
| Duet tiers F-B CS-2 (§5.3) | 64 / 102 / 160 px; tier 2 italic didone | v02 @0:00–0:03 "Creating", "banger", "videos" grotesk ≈ 100–170 px, "isn't" italic serif at the chin; v01 @0:19–0:21 "earn" italic, "key difference" italic; v05 @0:12–0:15 "everything", "without" grotesk ≈ 100 px; small connectors ≈ 44 px ("start", "result", "aside", "First") |
| Blur-in swap (P-11) | 4 f blur | v02 @0:00.0 "Creating" blurred → sharp by 0.17 s; v05 @0:00 "You" blurred; v01 @0:12–0:13 "still" / "started." ghosted then sharp |
| Positions F-B (§3.2) | plates cy 960; face cy 1150; split seam + 72 | v01 @0:00–0:03 words at cell y 267 → 960 px (split seam); v01 @0:19–0:20 "earn" y ≈ 970; v05 @0:12–0:15 chest y ≈ 1160; v02 @0:18–0:22 screen recording top band 0–880 px, caption at ≈ 963 px |
| Chip duet CS-3 (P-13) | connector words on cobalt chips, hook only | v01 @0:01.17–0:03 "are", "improving", "their", "craft", "over", "period", "of", "6" each on a cobalt chip |
| List title row (P-10, SM-1) | italic serif 92 px, cy 250 | v03 @0:03–0:33 "1. Edit with purpose" … "10. Follow for more" at cell y ≈ 65 → 234 px, ≈ 26 cell px glyphs; v04 @0:04–0:28 at y ≈ 274 px |
| Hover thumbnail (P-05) | 500×440 at x 290–790, y 320–760, radius 10 | v03 @0:03 eye still cell x 80–218, y 83–210 → 288–785 × 300–756 px; v04 @0:07 desk photo 270–810 × 292–778 px; @0:18 meeting grid 288–774 px. The evidence reaches the eyebrows (v04 @0:11–0:13); the template clamps the bottom 24 px above the face box (NC-1) |
| Logo card (P-06) | white card, name in type | v04 @0:04–0:07 white rounded logo cards (platform names); template sets the name in type unless the creator supplies the logo file |
| Counter ring (P-30) | Ø 430 gradient ring above the head | v03 @0:24–0:26 magenta→violet ring, centre ≈ (540, 508) px, Ø ≈ 430, values rolling 152,565 → 242,409 "Views"; v01 @0:42–0:44; v05 @0:27 on white with "+51,353 Followers" |
| Profile pill / tile (P-31, P-32) | glass pill at (540, 500); tilted glass tile | v03 @0:30–0:31 dark pill with avatar + name at y ≈ 493 px; v01 @0:45–0:47 tilted profile tile straightening |
| Notification pill (P-33) | accent pill with counts | v01 @0:07–0:08 red pill with comment / like / follow counts (template uses `accent`; `bad` is reserved) |
| Toggle compare (P-34) | Original / Enhanced toggle with a cursor | v02 @0:09–0:11 |
| Card wall (P-35) | curved wall of own work above the head | v02 @0:00.67–0:02.3 |
| File float (P-36) | file labels on paper | v02 @0:31–0:32 sound-file labels on off-white |
| Polaroid grid (P-37) | 3×2 stills on paper + cobalt word | v01 @0:17 "portfolio" |
| Tilt phone card (P-38) | tilted phone card on cobalt + didone word | v01 @0:16 "FAST" |
| Level panel (P-39) | green meter with "step n" | v02 @0:12, v05 @0:28 (template sets the text in `ink`) |
| Section numerals (P-08, SM-2) | "No.n" cream upright didone 300 px, cy 480; sub-line cy 720 | v01 @0:37–0:38 "No.2" (cell y 118 → 425 px); v05 @0:10–0:11 "No.1 / the technical foundation" (numeral y ≈ 525, sub-line ≈ 755), @0:21 "No.2", @0:34–0:35 "No.3 / learn from people ahead" |
| Step numerals (P-09, SM-3) | "step" italic 72 px + numeral italic 260–320 px at chest | v02 @0:08 "step 1", @0:16 "step 3", @0:23 "step 4", @0:28 "step 5", @0:31 "step 6" (on paper), @0:37 "step 7" |
| Paper frames (P-14) | `#F2F2F2`, cobalt grotesk or italic word | v01 @0:12–0:13, @0:25–0:26; v05 @0:06–0:09 ("comes down / to 3 things" with a cobalt chip), @0:30–0:31 |
| Cobalt frames (P-15) | small white word + underline | v01 @0:27–0:28 "managed", "timeline"; v05 @0:19–0:20 "that's", "to"; v01 @0:56–0:57 "towards", "goal." italic |
| Void frame (P-16) | navy black + word | v01 @0:55 "putting" |
| Split twin (P-23) | blue top / red bottom, caption on the seam | v01 @0:00–0:08 |
| Mono accent (P-24) | B&W plate + red word | v01 @0:10–0:11 "closer", "goal" |
| Colour wash (P-25) | red / blue / amber | v01 @0:48–0:54 red room wash; v01 @0:18–0:20 amber haze |
| Macro (P-26) | eye macro + big word | v01 @0:39 "went"; v02 @0:33 "emphasize" |
| Crop punch (P-27) | 1.35–1.6× on a cut | v02 @0:02.44 cut to a ≈ 160 % close face |
| Split screen (P-28) | screen top, face bottom, seam caption | v02 @0:16–0:22, @0:37–0:40 |
| Own B-roll plates (B-4, SH-1…SH-6) | back of head, hands, profiles, silhouettes, macro, tripod | v01 @0:00–0:11, @0:18–0:20, @0:23–0:24, @0:29–0:36, @0:48–0:54; v02 @0:24–0:27; v05 @0:05, @0:07, @0:10–0:11, @0:21–0:22, @0:29, @0:34–0:35 |
| Rack-focus open (P-22) | 14 → 0 px over 12 f | v01 @0:00–0:00.5 |
| Stacked pair (P-17) | two heavy grotesk words above the head | v01 @1:02–1:03 "private / community"; v02 @0:29–0:30 "animate / your captions", "and make / alive." |
| Keyword over plate (P-18) | big didone word + micro next word under it | v01 @0:23–0:24 "Editor 1" + "sat" / "paper"; @0:19–0:20 "earn" + "like" / "before." |
| Community card (P-45) | white card with name + promise + collage | v04 @0:25–0:27 (item "10. Join …"); v05 @0:58–1:00 |
| Keyword quote (P-46) | curly-quoted didone 220–300 px, cream → white, glow, cy ≈ 450 | v04 @0:28 'JOIN' (≈ 720 px wide, cy ≈ 454); v01 @1:04–1:06 'JOIN' cream-sage → white; v02 @0:51–0:54 'ELITE' teal → white with glow |
| Room look (W-room, §12.1) | dark top, practicals, teal-green / warm grade, head top 560–660 (F-A) | v03 cap top ≈ 650 px, v04 hair top ≈ 560 px, eyes ≈ 780–790 px; v02 head top ≈ 360 px, v05 ≈ 500 px (F-B) |
| Presence (SW-02) | F-A 95–100 %; F-B 20–50 %, absence ≤ 10 s | v03/v04 face 100 %; v01 face ≈ 20 % (first face @0:14), v05 ≈ 35 %, v02 ≈ 50 % |
| Fonts (§5.1) | Inter Tight + Instrument Serif | closest bundled matches to the observed condensed didone (italic list titles, upright chip / numerals / keyword) and tight grotesque |

## Known gaps and inferences
| Item | Status |
|---|---|
| Speech language | `(unverified)`: no transcripts; captions read as English |
| Sound (bed, cues on cuts) | `(unverified)`: not observable; §11 uses the pack contract only |
| F-B voice source | `(unverified)`: inferred as the desk take (lip movement and continuity at v01 @0:14, v02, v05); a separate VO is not supported |
| E1 occlusion | inferred from 2 instances (v05 "101", v02 "BY STEP"); limited to 1 per reel in the hook |
| Captions over the chin / face | observed (v02 @0:02.5 "isn't", v05 @0:34 "actually"); **not adopted** (NC-1) |
| Thumbnails down to the eyebrows | observed (v04 @0:11–0:13); **clamped** 24 px above the face box |
| Stock / famous art stills | observed (v02 card wall, v03, v04 Michelangelo, coins, handshake); **not adopted**: creator-owned or created type cards only (NC-7) |
| Brand logo stack | observed (v01 @0:06); replaced by logo plates set in type unless the creator supplies files |
| Notification pill red | observed (v01 @0:07); recoloured to `accent` |
| White text on the green panel | observed (v02 @0:12); set in `ink` for contrast |
| Grade events on A-roll | observed (v02 @0:07 magenta solarise of the A-roll); **not adopted**: grades only on B-roll plates (no engine footage-grade layer) |
| Exact easing curves | inferred from 6 fps hook sheets (blur-in ≈ 4 f for captions, ≈ 8 f for titles) |

## Fidelity audit 2026-10 (full-resolution frames, 720×1280 ×1.5)
Frames: v01 @0:00.1, 0:00.6, 0:01.5, 0:02.5, 0:27.5, 1:05.0; v02 @0:00.3, 0:01.2, 0:02.6, 0:09.0; v03 @0:00.3, 0:02.0, 0:10.0, 0:25.0; v04 @0:00.0, 0:00.5, 0:01.5, 0:03.0, 0:08.0, 0:20.0, 0:28.4; v05 @0:00.3, 0:01.0, 0:09.0, 1:15.0. Report: `vibe-editing-os/docs/audit/cinematic-list-montage/audit.md`.

| Claim | Measured | Where |
|---|---|---|
| F-A chip confirmed: fill #2534E9 (≈ #2B35E8), rect x 90–978, y 316–476 (cy 396), Instrument Serif ≈ 102 px (38.9 px/char) | — | v04 @0:03 |
| Sub-line ≈ 56 px at cy ≈ 514 confirmed | band 484–543 | v04 @0:03, v03 @0:02 |
| List title row cy ≈ 233, ≈ 86–92 px italic serif confirmed | "2. Local businesses" 590 px wide | v04 @0:08, @0:20; v03 @0:10, @0:25 |
| Hover thumbnail x 272–812, top y 288 (was x 290–790, y 320) | scans | v04 @0:08 |
| CS-1 micro caption bold ≈ 46 px at cy ≈ 1130–1136 (was 600, 44 px) | ascender band 34 px | v04 @0:03, @0:08; v03 @0:25; v05 @0:01 |
| F-B A-roll caption cy ≈ 960–1000 under the chin, ≈ 160 px heavy grotesk (was cy 1150) | "videos" ascender band 898–1020 | v02 @0:00.3, @0:01.2 |
| L-split seam at y ≈ 955, a hard edge; caption centred on it (was seam 900, caption +72, 60 px fade) | colour step 950 → 960 | v01 @0:00.6, @0:01.5, @0:02.5 |
| CTA 'JOIN' = condensed didone, letters nearly touching, cap ≈ 237 px, width ≈ 700 px, cy 450–510 → Instrument Serif (was Bodoni Moda 220–300) | — | v04 @0:28.4, v01 @1:05 |
| A-roll is low-key → `grades.footage` gain 0.82 / sat 0.85 / vignette 0.3 (was null) | walls #1C2214, shirt #030E0A | v04 @0:08 |

## Completeness audit 2026-10 (motion at full frame rate)
Method: scene detection on all 5 videos (`select='gt(scene,0.2)'`, 0.1 for v03/v04), 17 bursts read every frame (cv2, 360 px), ORB + `estimateAffinePartial2D` per frame for zoom. Strips and the full report: `vibe-editing-os/docs/audit/cinematic-list-montage/completeness.md`.

| Claim (playbook id) | Measured | Where |
|---|---|---|
| Z-3 pull-out 2.0 → 1.0 / 50 f, expo-out, blurred open | cumulative scale 0.51 by f19 then 0.83 more by 2.2 s (≈ 2.3×); sharpness 73 → 400 over f0–f19 | v04 @0:00.00–0:02.2; v02 @0:00–0:01.9 (2.1×); v05 @0:00–0:02.0 (1.6×) |
| P-01 swing-in typed chip | enters top-left rotated, rests by f12–14, types ≈ 1 char/f | v04 @0:00.08–0:00.76; v05 @0:00.12–0:00.68; static alternate v03 @0:00.00 |
| P-03 typed sub-line | "y" → "you need" over f2–f12 (≈ 0.8 char/f) | v03 @0:00.08–0:00.50 |
| H3 hidden cut into item 1 | posture/prop change, same framing, under a 4 f blur + 5 f de-blur (v04) or hard (v03) | v03 @0:02.83; v04 @0:03.58–0:03.90 |
| T-06 hard title swap + 1 flicker | old/new on the same frame; title 1 → 0.35 → 1 | v04 @0:09.12, @0:13.92; v03 @0:09.09, @0:15.16 |
| F-A camera locked | scale 1.0000 ± 0.0001 per frame | v03 @0:00–0:00.54, @0:02.5–0:03.0; v04 @0:03.5–0:04.06 |
| CS-2 flicker-in swap | blurred → 0.4 → 0.8 → 0.4 → 0.8 → 1 over 5 f | v02 @0:00.64–0:00.84 |
| T-11 blur pulse | full-frame sharpness drops to 5–35 for 1–4 f | v01 @0:00.00, 0:00.16, 0:00.56, 0:41.7, 1:04.34; v02 @0:00.60; v04 @0:03.62, 0:27.68 |
| Z-1 = cut-in + de-blur | hard cut to ≈ 1.9× tighter, sharpness 156 → 205 over 5 f | v02 @0:02.44 |
| Z-2 push-in | 1.0 → 1.14 (41.6–42.7), 1.0 → 1.12 (45.4–46.3); CTA 1.0 → 1.06 / 12 f | v01; v04 @0:27.68–0:28.16 |
| P-08 / P-09 flicker-in | "No.2", "step 3" land on the cut frame and flicker 5–6 f | v01 @0:37.12; v02 @0:16.08–0:16.44; de-blur 4 f v05 @0:09.82 |
| P-15 resizing underline | the line width follows each word over ≈ 3 f | v01 @0:27.16–0:27.40 |
| P-28 split by hard cut | no slide | v02 @0:16.08 |
| P-29 framed take on paper; P-38 3 f swing | card exits with a 2 f 3D flick; phone card edge-on → −18° in 3 f | v01 @0:16.08–0:16.44 |
| P-30 odometer ring | 8 → 152,565 in 13 f, gradient rotating ≈ 30°/f | v03 @0:23.90–0:24.44 |
| P-46 keyword entry | 1 f empty blur frame, then cobalt → teal → white in 3 f; v01 cream fade 4–6 f | v04 @0:27.68–0:27.80; v01 @1:04.34–1:04.46 |
| Pacing F-B | shots 38 / 31 / 43, median 1.32 / 1.04 / 1.28 s, p90 3.56 / 3.68 / 3.84 s, longest 9.2 / 11.6 / 9.0 s (face + graphics) | v01 / v02 / v05 scene lists |
| Pacing F-A | graphic swaps every 2.0–2.6 s (v04), 3.0–3.7 s (v03) | scene 0.1 lists |

Observed, not adopted: the 1-frame white type flash "you need to" (v01 @0:16.72, NC-11 flash safety); stock art on paper ("TASTE", v01 @0:16.76, NC-7).

## Engine built-ins 2026-10 (workarounds replaced)
| Device | Was (workaround) | Now built-in | Value (measured) |
|---|---|---|---|
| CS-2 flicker-in swap | caption swap `blur` 5 f 12 px | caption `swap: {type: "flicker", pattern: [0.4, 0.8, 0.4, 0.8, 1], frames: 5}` (2 flashes, NC-11 ≤ 3) | 0.4 / 0.8 / 0.4 / 0.8 / 1 over 5 f, v02 @0:00.64–0:00.84 (the first-frame motion blur is not reproduced: a flicker has no blur) |
| T-11 blur pulse | `GR-pulse` grade (`blur(14px)`) on the footage only; graphics entered after it | `timeline.grades {t, blur: 14, dur: 0.04–0.16, frame: true}`: whole picture incl. graphics z1–6, captions sharp; `GR-pulse` removed from `grades.scene` | ≈ 14 px, 1–4 f, v01 @0:00.16, 0:00.56, 1:04.34; v04 @0:03.62, 0:27.68 |
| T-02 blur-through | two clip scenes with filter ramps | `transitions {type: "blur-through", px: 16, frames: 9, pre: 4}` | 0 → 16 px over 4 f, cut, 16 → 0 over 5 f, v04 @0:03.58–0:03.90 |
| Z-2 push-in ease | push-drift eased linearly by the engine | preset `ease: "expoOut"` | 1.0 → 1.12 / 28 f (1.12–1.14 measured), v01 @0:41.6, 0:45.4 |
| Z-3 pull-out | engine default ease-out, no blur | preset `ease: "expoOut"` + `blur` radial 0.15 at the face, 12 f decay | 2.0 → 1.0 / 50 f, half the travel by f6, blurred f0–f12, v04 @0:00.0–0:02.2 |
| Z-1 crop punch de-blur | a separate GR-pulse event | preset `blur` defocus 14 px, 5 f decay | 5 f de-blur, v02 @0:02.44 |

Still not built in: Z-1 stays at 1.35× (the measured ≈ 1.9× needs a 4K take: a resolution limit, not an engine gap).
