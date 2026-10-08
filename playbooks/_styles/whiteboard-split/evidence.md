# Whiteboard Split: evidence map (App. B)

**Sources.** `vibe-editing-os-research/analysis/short/kallaway.md`; frame sheets `evidence/short/kallaway/v01` (74.0 s), `v02` (107.6 s), `v03` (62.7 s): `hook_01.jpg` (0–3 s at 6 fps) and `s_01…s_06.jpg` (1 fps); `meta.json`, `cuts.json`. All sheets were read for this template, including the three the analysis skipped (v01 s_03, v02 s_02, v02 s_04). Sources are 720×1280; every measurement below is converted to 1080×1920 (tile px × 3.6 on the 300×534 sheet tiles).

## DNA rules → evidence
| DNA element | Value in the template | Evidence |
|---|---|---|
| Three-band split | Card band y 150–1160; caption cy 1245; window from y 1400 | v01 @ 0:00–0:01.7 (caption y ≈ 1240, window top ≈ 1402); v02 @ 0:00–0:16 (caption ≈ 1287); v03 @ 0:00–0:02 (≈ 1240) |
| Window rect | x 64–1016, radius 30, bleeds off the bottom | v01 hook tiles: window x 65–1011, top corners only; v03 @ 0:19 x 72–1008 |
| Window shows the wide master | face 0.24 of the window | All split tiles: waist-up wide shot of the room |
| Head breaks the window edge | ER-1 (not implemented; head kept inside) | v01 @ 0:00 cap top ≈ y 1325 vs window 1402; v02 @ 0:00; v03 @ 0:00 |
| Full-face punch | L-full, face 0.26, eyes ≈ y 690 | v01 @ 0:01.8–0:03.9 ("is / because / you're / using"); v03 @ 0:03 ("don't") |
| Mode cuts are hard cuts | `via: cut`, `stage_morphs.cut: 0` | cuts.json v01 [1.75, 3.96, 11.42, 12.25, 18.96, …]; no intermediate frames in the 6 fps hook sheets |
| Run lengths | L-full 0.8–4.0 s; L-split 1.5–12 s | v01 full 1.75–3.96 (2.2), 11.42–12.25 (0.83 "But"), 32.08–34.96 (2.9); v01 first split 0–1.75; v02 splits 18.2–30.4 and 34.7–52.5 (long, card changes every 2–3 s); v02 full 30.4–34.7 (4.4) |
| Switch words | claim / but / number / sentence / pause | v01 @ 0:01.8 "is", 0:11.4 "But", 0:19 "instead,", 0:24 "zero.", 0:32 "Then"; v03 @ 0:03 "don't", 0:15 "information" |
| Full-face share 26–42% | `layouts.L-full.share` | analysis §6: ≈ 38% (v01), 30% (v02), 35% (v03) |
| One-word captions | CS-1/CS-2 unit word | v01 @ 0:04–0:11 "what / school, / story arc. / Initial conflict, / rising action, / climax, / falling action,"; v03 @ 0:00 "This / how you / turn / Claude" |
| Caption case as spoken, punctuation kept | `case: as_spoken`, `punct: keep` | "The reason", "But", "Then", "Now,", "Claude,", "YouTube", "I'll", "done." |
| Caption colour flips with the world | ink on paper, white on stage and footage | v01 @ 0:00 (black on paper) vs 0:04 (white on stage); v03 paper throughout |
| Caption sizes | CS-1 56 px, CS-2 66 px | measured ≈ 46–53 px split ("falling action," 360 px wide / 15 chars), ≈ 59–75 px full ("because" 288 px / 7 chars; "information" 374 px / 11 chars) |
| Caption pop swap | `swap: pop 3 f` | v01 @ 0:38 "contrast" caught tiny mid-pop |
| Italic-serif caption keyword | `emphasis: font_swap`, ≤ 1 per 5 s | v01 @ 0:03 "*story*" (full face); v01 @ 0:43 "*dopamine*" (on a clip) |
| Lockup recipes | LK-1…LK-5 | LK-1 v01 @ 0:00 "This Is The Reason / Why Your Video Fails" (crimson), v03 @ 0:19, 0:29; LK-2 v02 @ 0:01 "How to make your / *Storytelling addictive*" (underline); LK-3 v01 @ 0:14 "No Longer Works" slab; LK-4 v01 @ 0:04 "Traditional *Story Arc*", v02 @ 1:05 "Art of *Contrast*", 1:36 "Super Addicting *Story*"; LK-5 v01 @ 1:12 "Comment *"Story"* / To Get The Doc", v02 @ 1:40, v03 @ 1:01 |
| Lockup arrives with a blur build; underline first | f0 / body entrance | v02 @ 0:00–0:00.83 word by word with blur; v03 @ 0:00 underline drawn before the words fade in; v01 @ 0:00.17–0:00.5 fade with blur |
| Crimson | `primary` #B0122A | v01 "Video Fails", "No Longer Works" slab, "Storytelling Principles"; v03 "Social Media Forever" underline, "Every Secret", follower chip |
| Worlds | W-paper #EEEDEA + 40 px grid; W-stage #050505 | v01 @ 0:00 and 1:04 (paper), 0:04–1:01 (stage); v02 all stage; v03 all paper |
| Neon diagram, white nodes, callout tags | P-CURVE-DRAW, P-NODE-CALLOUT | v01 @ 0:04–0:11 |
| Old → new on the same axes | P-ARC-SWAP | v01 @ 0:14–0:25 (red arc fades; "Modern Story Arc" white spikes) |
| Magenta reading + stat chips | P-CURVE-OVERLAY, P-STAT-CHIP, P-AREA-FILL | v01 @ 0:16–0:18 ("832", "101"), 0:47–1:01 (magenta curve + fill) |
| Threshold bars + serif annotation | P-THRESHOLD-BAR | v01 @ 0:27–0:31 (yellow bars, "HOOK" + curl arrow), 0:48–1:01 |
| In-band diagram push | P-DIAGRAM-PUSH | v01 @ 0:26–0:31 (title pushed off, chart enlarged), 0:36–0:41 (pan right) |
| Grey bevel chip stack | P-CHIP-STACK | v01 @ 0:38–0:41 ("Contrast Moment / Contrarian Take / Shocking Stat") |
| Recurring motif with visits and numerals | §23, P-MOTIF-* , SM-NUM | v02 @ 0:04–0:06 (loop built, 1–4), 0:35–0:36 ("2 Big Question"), 0:51 ("3"), 1:15–1:17 ("3 Headfake", "1 Stakes", "4"), 1:31–1:36 (recap with 4 labels) |
| Numbered tokens | P-TOKEN-LIST | v02 @ 0:18–0:23 (chips 1–3 "A character someone can root for / Something at risk / Urgency") |
| Script page highlight | P-DOC-HIGHLIGHT | v02 @ 0:24–0:29 |
| Road fork | P-ROAD-FORK | v02 @ 0:54–1:07 ("The Headfake", A/B) |
| Mini frames | P-MINI-FRAMES | v02 @ 1:25–1:30 ("Good Stories / Great Stories") |
| Object pulse, linked objects | P-OBJECT-PULSE, P-CONCEPT-LINK | v02 @ 0:01–0:03 (brain + red disc), 0:06–0:09 (brain → loop → slot machine) |
| Tile wall + tint flip | P-TILE-WALL | v02 @ 0:01.8–0:03 (column slides up, tints red on "impossible") |
| Mini player montage | P-MINI-PLAYER | v02 @ 0:00–0:01 (4 clips, 0.17 s each) |
| Clip card + outline tags | P-CLIP-CARD, P-CLIP-TAG | v02 @ 0:37–0:46 ("10K followers" green box, "17 days ago", dotted leaders "Stakes", "Big Question") |
| Card flip | P-TILE-FLIP | v02 @ 0:46–0:51 |
| Full-bleed example clips | L-clip, P-CLIP-INTERCUT | v01 @ 0:42–0:43; v02 @ 1:12–1:15, 1:18–1:22 (third-party films: creator-supplied only in this template) |
| Recreated UI, phone, chat typing | P-UI-POPULATE, P-PHONE-MOCK, P-CHAT-TYPE | v01 @ 0:00–0:01 (insights panel); v02 @ 0:12–0:15 (phone); v03 @ 0:04–0:08 ("/analyze" typed) |
| Counter ticking with a tile grid | P-COUNTER-TICK, E6 | v03 @ 0:01.7–0:02.9 (2K → 19K, ≈ every 0.17 s) |
| Output sections, hand labels, tile grid | P-RESULT-SECTIONS, P-HAND-LABELS, P-TILE-GRID | v03 @ 0:10–0:14, 0:35–0:37, 0:29–0:31 |
| Logo link, settings list, converge | P-LOGO-LINK, P-SETTINGS-LIST, P-CONVERGE | v03 @ 0:39–0:42, 0:44–0:47, 0:54–0:56 |
| Doc grid CTA, video card CTA | P-DOC-GRID, P-CTA-ASSET | v01 @ 1:04–1:13; v02 @ 1:40–1:47; v03 @ 1:01–1:02 |
| Ends on the split CTA, no end card | N11 | v01 @ 1:13, v02 @ 1:47, v03 @ 1:02 |
| Collage flip | P-COLLAGE-FLIP | v01 @ 0:12–0:13 |
| Structure variants | FW-1 / FW-2 / FW-3 | v02 / v01 / v03 |
| Hook archetypes | HA-06 default; HA-02, HA-07 alternates | v01, v02 (title + build); v03 (headline + proof, live counter) |
| Hook change count | `hook_sc_3s` 9 (captions 0.34) | v01 0–3 s: 6 graphic/stage events + 11 caption words |
| Pace | ≈ 3.2 words/s | analysis §11 (caption cadence) |

## Inferred (not measured)
- Card/scale-in frame counts, blur amounts, push durations: estimated from 6 fps hook sheets and 1 fps body sheets; set to the nearest standard motion token.
- Colours beyond the analysis' hexes (`good` #2BD96B, `mute`, `grid` #D4D2CC): sampled by eye from the sheets.
- Lockup sizes: from rendered string widths (Inter Tight ExtraBold average advance ≈ 0.53 em).
- `caption_weight` 0.34 and the cadence windows: derived (Part E #2), not observed.

## (unverified)
- **Speech language:** English, read from the burnt-in captions; no transcript.
- **Sound:** not observable; §11 is the minimal contract (silent mode cuts is a decision, not evidence).
- **Camera setup:** one 4K camera cropped vs a second tight angle is not provable from the sheets (prior knowledge says one 4K camera).
- **Head pop-out:** the head clearly breaks the window edge; whether this is a matte cut-out or a window placed under the head is inferred (matte).

## Known gaps
- 1 fps body sheets cannot show sub-second card events between samples; card-event spacing (≤ 2.5 s) is a template decision consistent with the samples.
- The v02 film clips and other creators' reels are third-party: the template only uses them when the creator supplies them, otherwise the created substitutes in playbook §12.5.

## Fidelity audit (6 Oct 2026, full-resolution frames; sources are 720×1280, upscaled ×1.5)
Report: `vibe-editing-os/docs/audit/whiteboard-split/audit.md` (17 frames, v01–v03).
| Corrected value | Evidence |
|---|---|
| Hook lockup not on f0; readable ≤ 1.0 s; band zoom ≈ 0.65 → 1.0 over 1.5 s | v01 @ 0.0 / 0.5 / 1.5 s (no lockup at 0.0; card 313 → 504 px wide); v02 @ 0.0 / 1.0 s; v03 @ 0.0 / 1.5 s |
| CS-2 cy 1160 | v01 @ 0:03 "wrong", v01 @ 0:20 "social" (white band y 1131–1181) |
| Paper `#E4E4E0`, grid `#DADAD6` (faint) | v01 @ 1:12 pixel row y 1100: paper `#E1E2DD`–`#E4E4E4`, lines ≈ 6 levels darker |

## Completeness pass (7 Oct 2026, full frame rate, 24 fps sources)
Report: `vibe-editing-os/docs/audit/whiteboard-split/completeness.md`; strips `strip-*.jpg` beside it. Method: scene detection (thr 0.2) on v01–v03; 15 bursts × 0.7 s at 24 fps; YuNet face boxes at 4 fps over every run.
| Value | Evidence |
|---|---|
| Mode cuts v01 | 1.75, 3.96, 11.42, 12.25, 18.96, 20.5, 22.5, 24.71, 32.08, 34.96, 41.67 (clip), 44.46, 46.54, 52.54, 56.0, 61.17, 63.54, 67.58, 71.71 |
| Mode cuts v02 | 16.39, 18.23, 30.36, 34.74, 52.47, 53.85, 67.86, 71.61 (clip), 75.28, 78.41 (clip), 82.33, 84.88, 96.68, 100.06 |
| Mode cuts v03 | 2.96, 3.79, 8.29, 9.92, 15.08, 18.75, 25.54, 28.96, 38.0, 39.25, 42.54, 44.08, 48.29, 51.46, 56.67, 60.67 |
| Punch rate / L-full share | v01 9 in 74 s, 29%; v02 6 in 108 s, 16%; v03 8 in 63 s, 31% |
| Static L-full entry (no land) | strip-punch-v01 (1.758 s: f5–f8 identical scale); v02 @ 0:30.36 same |
| Punch-in step inside L-full | face box 560 → 700 px at v01 @ 0:02.75; 560 → 630 @ 0:23.75; 575 → 702 @ 0:55.25; v03 580 → 700 @ 0:17.25, 560 → 670 @ 0:50.0; strip-jumpcut-punchin-v03 (0:15.76) |
| Push-drift | v02 @ 1:07.9–1:11.3 face 543 → 585 px, gradual |
| Window face | face box 200–265 px, centre y 1440–1545 (all split samples) |
| Caption hard swap, 2-word chunks | every strip ("The reason" → "your" v01 @ 0:00.29; "of a" v01 @ 0:26.46) |
| Lockup line build | strip-hook-v01 (lines fade 0.13–0.33 s); v01 @ 1:03.7–1:04.0 (line 2 5 f after line 1); LK-2 word build strip-hook-miniplayer-v02 |
| Mini player swap 4 f @ 24 fps | strip-hook-miniplayer-v02 (clips change at f4, f8, f12) |
| Motif pan expo-out | strip-motif-pan-v02 (loop travels ≈ 78 px/f → 12 px/f over 16 f; numeral fades 6 f) |
| Smear push | strip-smear-swap-v03 (0:32.38–0:32.47 out, 0:32.72–0:32.84 back); v03 @ 0:01.6. **Now built-in:** `slide-l` / `slide-r` with `smear: true`, `out_frames: 3` / `in_frames: 4`, 700 px travel (was a scene-side CSS blur, ER-5) |
| Detail cut-zoom | strip-cta-cutzoom-v02 (1:42.47, blur-in 4 f) |
| Clip montage in L-clip | strip-clip-in-v02 (1:18.41 cut in, 1:18.66 next shot) |
| Clip pull-out to phone | strip-clip-pullout-v01 (0:43.55–0:43.9) |
| Collage orbit | v01 @ 0:12.27–0:13.5 (continuous 3D orbit of 5 playing tiles) |
| Paper grid radial fade | v01 @ 1:03.55 (grid only in the centre). **Now built-in:** W-paper `grid.fade {x: 540, y: 770, inner: 0.1, outer: 0.3}` (was a uniform faint grid, ER-6) |

## Engine built-ins (template pass, 2026-10-07)
- **Now built-in:** smear push (ER-5), paper grid radial fade (ER-6), see the rows above.
- **Already built-in:** CS-1 ink on paper / paper on stage: `position.colour_by_bg {light: ink, dark: paper}` (capengine).
- **Still a workaround:** head pop-out above the window (`breakout: 120`, ER-1), clip → phone pull-out (bespoke scale into `fx.device`, ER-7), in-band camera (canvas camera inside one scene, ER-2), punch-rate check (reviewer, ER-4): no engine field for any of these yet.
