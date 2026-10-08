# Lesson Frame: evidence map (App. B)

Source: `vibe-editing-os-research/analysis/short/editing-explained.md` and the frame sheets in `evidence/short/editing-explained/v01–v04/sheets` (hook sheets at 6 fps, body sheets at 1 fps). All four sources are native 1080 × 1920, so px values are direct (sheet tiles are 300 px wide = 1/3.6 scale; key frames were re-enlarged to 1080 × 1920 and measured). No transcripts exist: speech is read from the burned-in captions. Sound is not observable.

| Source | Topic | Duration |
|---|---|---|
| v01 | Embedded vs separate subtitles | 34.1 s |
| v02 | Codec vs format | 46.5 s |
| v03 | Render settings for social media | 32.5 s |
| v04 | The bitrate mistake | 47.2 s |

## DNA rules → evidence

| Rule (playbook) | Value | Evidence |
|---|---|---|
| Persistent lockup (D1, D2, §5.2) | 2 lines, held to the last frame | v02 @ 0:00.83–0:46; v04 @ 0:00.67–0:46 |
| Lockup build order (P-01) | line 2 + hairline at 0.17 s, line 1 at 0.33 s, complete 0.67–0.83 s | v02 hook @ 0.167 / 0.333 / 0.5 / 0.833; v04 hook @ 0.167 / 0.333 / 0.667; v01 hook @ 0.167 / 0.333 / 0.667 |
| Lockup sizes | line 1 ≈ 86 px (442 px wide "95% Editor", cap ≈ 65 px), cy 378; line 2 ≈ 72 px italic serif, cy 466 | v02 @ 0:10 (enlarged frame) |
| Hairline | y 518, x ≈ 125–935, core ≈ #D89D36 with orange glow, fading ends | v02 @ 0:06 pixel samples (216,157,54 core) |
| Card rect | x 72–1008, y 568–1288, radius ≈ 40 | v02 @ 0:06, 0:10; v04 @ 0:18; v03 @ 0:09 (same rect without a title) |
| Empty top / bottom | nothing above y ≈ 330; nothing below y ≈ 1580 | all sheets; template keeps y ≥ 1536 empty for NC-5 |
| Dark page | ≈ #050505, dot grid ≈ #1C1C1C at pitch ≈ 28 px | v02 / v04 background samples (mean luma 2.7; dot max 23; autocorrelation 7–8 tile px) |
| Light page (TH-light) | ≈ #FBF3F1, 1 px lines at ≈ 180 px pitch | v03 @ 0:03–0:31 samples (249,241,239; line spacing 50 tile px) |
| Captions (CS-1) | Space-Grotesk-like 500, ≈ 48 px, ALL CAPS, wide tracking, 2–4 words, 1 line, cy ≈ 1345, hard swaps ≈ every 0.6 s | v02 hook (CHAHE TUM → KOI BHI SOFTWARE → USE KARTE HO → TUMNE HAMESHA → DEKHA HOGA); v02 @ 0:10 enlarged (cap height 34 px); v04 hook |
| Caption box | black box behind the caption on footage (F-mode) and on the light page | v01 @ 0:04–0:17 (box at y ≈ 1170–1250 in full-bleed); v03 @ 0:02.67–0:31 |
| Hinglish romanised, English terms verbatim, digits ungrouped in captions | "CODEC H. 264", "50000 KBPS PE", "FRAME REORDERING AAPNE" | v03 @ 0:04, v04 @ 0:18, v03 @ 0:13 |
| Term card, light + presenter in the corner (P-06) | white card, condensed charcoal word ≈ 170–180 px with drop shadow, presenter at the bottom-right | v02 @ 0:02.83–0:08 (CODEC) |
| Variant chips (P-07) | plain text ≈ 56 px, one per spoken variant, two-tone "Apple Pro Res" | v02 @ 0:04 (H.264), 0:05 (H.265), 0:07 (Apple Pro Res) |
| Dark term card (P-08) | charcoal card, white condensed; orange + white two-line variant | v02 @ 0:24 (FORMAT); v04 @ 0:08 (AUTOMATIC / HOTA HAY), 0:37 (THIS IS WRONG); v01 @ 0:18 (LADIES & GENTELMEN) |
| Marker term card + Essential pill + panel strip (P-09, P-10) | brush "Bit Rate", grey pill "Essential #3", settings strip with orange box | v04 @ 0:03–0:05, 0:38–0:39 |
| Question card (P-11) | "Why Automatic is good then?" on white with the presenter | v04 @ 0:15–0:16 |
| Number on card (P-12) | "50,000KB/S" ≈ 200 px condensed white at the card bottom | v04 @ 0:18–0:19; "100,000KB/S" @ 0:32 |
| Number beside the head (P-13) | "10,000KB/S" + "BHI NI CHAHIE" | v04 @ 0:23–0:24 |
| Keyword on card (P-14) | ".MOV", "APPLE PRO RES 4444" | v02 @ 0:28, 0:43–0:45 |
| Dialog card + orange box (P-15, P-16) | dark export panel inset on a white card, box moving Format → Codec | v02 @ 0:09–0:17, 0:29–0:31 |
| White box + cursor on recordings (P-16, P-19) | white rectangle around Format/Codec, Resolution, Quality on the light page | v03 @ 0:03–0:09 |
| Chevron pointer (P-17) | white « and ⌄ chevrons on settings | v01 @ 0:11, 0:20 |
| Value pick (P-21) | bit-depth dropdown 24 → 32 | v03 @ 0:22–0:29 |
| Insert hook (H-3, P-23, P-24) | 16:9 film clip above the lockup with the face card below; phone mock looping clips | v01 @ 0:00–0:04.27; v03 @ 0:00–0:02.67 |
| Composition cut (G-2) | whole layout changes by hard cut after the hook | v03 @ 0:02.67; v01 @ 0:04.27 |
| Full-bleed face + boxed caption (P-28) | caption box at y ≈ 1170–1250, credit under it | v01 @ 0:04–0:06, 0:09–0:17, 0:30–0:33 |
| Card only, no title (P-29) | same card rect with an empty page above | v01 @ 0:18–0:29 |
| Re-crop jump (P-05, Z-1/Z-2) | scale alternation ≈ 1.0 / 1.25 on jump cuts | v02 @ 0:18–0:24; v04 @ 0:01–0:03 |
| Hard cuts only (D4) | no whips, flashes or slides | cuts.json + all sheets |
| Credit chip (P-04) | arrow + handwritten "Captions made using" + green chip, y ≈ 1420–1580 | v02 @ 0:07–0:14, 0:35–0:45; v04 @ 0:05–0:09, 0:37–0:46; v03 @ 0:07–0:14, 0:24–0:31; v01 @ 0:06–0:10, 0:24–0:33 |
| Credit windows (two, not persistent) | absent mid-reel | v02 @ 0:15–0:34; v04 @ 0:10–0:36; v03 @ 0:15–0:23; v01 @ 0:11–0:23 |
| One accent | orange only (+ the chip) | all sheets |
| Hook question (H-2) | "MERA EK QUESTION HAI… SEARCH NA KARNA GOOGLE PE" → Bit Rate at 0:03 | v04 hook + s_01 |
| Durations | 32.5–47.2 s | meta.json |
| Gestures as the face card's only "graphics" | OK sign, finger at the lens | v02 hook @ 0.33–1.0; v04 hook @ 1.33–2.67 |

## Inferred (not directly observable at 1–6 fps)
- Sub-second motion: the lockup's blur amount, the term-word settle, chip and callout scale-ins (10 f), the highlight-box draw (6 f) and slide (7 f), the credit chip's entry. Values are set from the 6 fps hook sheets and the style's restraint.
- The H-4 term-first hook (moved from the 2.8–3.0 s term card to f0).
- Exact caption chunk timing (lead, holds): read from 6 fps hook sheets.
- Fonts: closest bundled faces (Inter Tight for Inter; EB Garamond italic for a Newsreader-like italic; Anton for a Bebas-like condensed; Permanent Marker for both the brush term and, as a stand-in, the thin handwriting).
- The presenter on term cards is a matte cut-out in the evidence; the template uses a rounded tile until the engine supports a cut-out PiP.

## Unverified
- `profile.language.speech` (no transcripts; captions show romanised Hinglish).
- Caption timing tokens, the lockup's f0 recipe, the credit chip's entry, the marker and caption font families (listed in `tokens.json → style.unverified`).

## Fidelity audit (6 Oct 2026, full-resolution frames)
Report: `vibe-editing-os/docs/audit/lesson-frame/audit.md` (18 frames, v01–v04, pixel-measured).
| Corrected value | Evidence |
|---|---|
| Lockup build: line 2 f3, hairline L → R, line 1 f12 (5 f stagger), readable 0.9 s | v02 @ 0.25 / 0.5 / 0.8 / 1.1 s title crops |
| Hairline x 170–900 | v02 @ 0:03: amber pixels y 514–521, x 175–892 |
| CS-1 44 px | v02 @ 0:01.5 "USE KARTE HO" cap y 1328–1359; v01 @ 0:10 boxed caption |
| TH-dark page `#000000`, dots `#131313` r 4 pitch 27 | v02 @ 0:03 pixel rows: `#000000` ground, `#121212` dashes 14 × 7 px, pitch 29.5 × 24.7 |

## Completeness audit (7 Oct 2026, full frame rate)
Report: `vibe-editing-os/docs/audit/lesson-frame/completeness.md`. Method: per-frame band diffs on all four videos (180 × 320 gray, every frame), background-registered ORB / LK scale per frame, 16 bursts at 30 fps (≈ 340 frames).
| Corrected value | Evidence |
|---|---|
| Lockup: line 2 L→R soft wipe + blur, 6 f from f2–3; hairline L→R with it; line 1 per-character L→R blur reveal from f11–12; settled f22–24 | v02 @ 0.05–0.85 s (strip-lockup) |
| Jump cuts keep the framing (scale 1.00 ± 2 %); no 1.00 / 1.25 re-crop alternation | 30+ cuts: v04 @ 1.20, 11.57, 13.63, 14.33, 15.0, 18.1, 19.67, 21.47, 27.63–35.67; v02 @ 19.9, 22.27, 32.87; v01 @ 4.53, 4.8, 12.33, 16.93, 30.1 |
| Z-2 push 1.00 → 1.28 over 18 f, accelerating; small pushes +7–9 % / 14 f | v02 @ 0:41.20–0:41.77 (strip-push); 0:31.8, 0:34.7 (LK) |
| Z-3 pull-out −14 % over 33 f, near-linear | v02 @ 0:38.77–0:39.8 |
| No camera moves in v01, v03, v04 (full-bleed growth in v01 is the presenter leaning in, scale/frame ≤ 1.006) | v01 @ 4.3–4.87, 14.35–15.05 |
| Term card + word cut on together, static (no settle) | v02 @ 0:02.817 (strip-termcard) |
| Variant chip: L→R character reveal + blur, 8 f, no rise, 2 f before the caption | v02 @ 0:03.95–4.22 (H.264) |
| Dark term card static, 0.73 s, caption stays on with the same words | v04 @ 0:36.97–0:37.70 |
| Number callout hard on with a jump cut, hard off on the next | v04 @ 0:18.10 on; 0:33.30 off (100,000KB/S) |
| Dialog screenshot settles 1.02 → 1.00 in 7 f, then drifts +0.1 %/f | v02 @ 0:09.02–0:09.55 |
| Highlight box traces from the top-right, leftwards then down, 14–16 f | v02 @ 0:09.15–0:09.55 (strip-dialog-box) |
| Credit chip flicker-on 6 f (on 3, off 1, on 1, off 1, on), hard off | v04 @ 0:05.43 on, 0:10.20 off (strip-credit); v02 @ 6.7/6.87; v03 @ 6.1–6.6 |
| Captions swap hard, 1 f after the card cut; ≈ 1 swap per 0.62 s | v02 74 swaps / 46 s; v02 @ 2.85, v04 @ 1.233 |
| Longest talking run without a weight-1 change: 3.4 s | v04 @ 0:21.47–0:24.83 |

## Engine built-ins pass 2026-10-07
- Now built-in: Z-2 `push-drift` accelerates (`ease: "in"`), 1.00 → 1.28 over 18 f as measured (v02 @ 0:41.20–0:41.77); it ran linear before.
- Now built-in: Z-3 `pull-out` is `ease: "linear"` (measured −0.4 %/f, v02 @ 0:38.77–0:39.8; the engine default eased out) and starts mid-shot from the crop on screen with `p.from: "inherit"` (no 1.15 snap hidden on a jump cut).
- Still a workaround: the highlight box trace starts at word −2 f, not ≈ 12 f early (V-ONWORD has no early-start mark; not in this engine pass). Matte cut-out PiP is still the rounded presenter tile.

## Template values pass 2026-10-07 (defaults, no switches)
- P-16 highlight box starts tracing ≈ 12 f before its field word and closes on it (v02 @ 0:09.15–0:09.55). V-ONWORD accepts a lead of up to 15 f by default, so this is just the scene time (`hilite_lead_frames: 12`).
