# Tech Countdown: evidence map (App. B)

**Source.** `vibe-editing-os-research/analysis/short/vaibhav.md` and the frame sheets in `evidence/short/vaibhav/v01–v03/sheets/` (hook sheets at 6 fps, body sheets at 1 fps). Every sheet was inspected for this template (v01 hook + s_01–s_10, v02 hook + s_01–s_05, v03 hook + s_01–s_10). Sources are 720 × 1280; all positions below are scaled to 1080 × 1920 (× 1.5) and measured on the sheet cells (300 × 534 px per cell = × 3.6 to 1080 × 1920).

| Video | Topic | Duration | Format here |
|---|---|---|---|
| v01 | A keynote recap: numbered features #01…#10 (ascending) | 178.7 s | F-A, TH-studio |
| v02 | "Day 60 of future tech updates": one product story | 89.4 s | F-B, TH-studio |
| v03 | "Week 09 of the AI tools": tools #10…#01 (descending) | 163.0 s | F-A, TH-lime |

## 1. DNA rules → evidence

| Rule / value | Evidence (vNN @ m:ss) | Notes |
|---|---|---|
| Pill caption, small plain sans | v01 @0:02 "Apple just launched one", @0:21 "I could just ask", @0:57 "like 500 times Now"; v02 @0:00 "One image gen AI company just" | Plain text measured 38–42 px (v01 seam caption 479 px wide for 23 characters); black translucent pill in v01, bare white with shadow on the dark fade in v02 → CS-1 42 px pill (E3) |
| Lime pill skin (CS-2) | v03 @0:25–2:29 every tool-card caption ("YouTube link", "Zapier charges", "$22 a month for this.") | Black text on solid lime; one skin per reel → themes `per_reel` |
| Italic-serif emphasis, split around the plain words | v01 @0:05 "This is / *exciting part* / not the most", @0:09 "which / *nobody is talking*"; v02 @0:02 "One image gen AI company just / *announced a full body ultrasound scanner*", @0:44 "But here's / *where you slow down*", @0:48 "So why / *does an AI company want it?*", @1:14 "It can't / *diagnose anything yet*"; v03 @0:09 "*Mr. Beast* / is literal", @0:18 "I went through / *100 of launches this week*" | Italic measured 80–120 px (v02 split ≈ 80 px, v01 full ≈ 100–120 px) → 92 px tier; one phrase per 4–8 s |
| Blur-in of emphasis | v02 @0:06 "*are shocked*" (smeared/blurred on entry) | Caption fade swap 3 f + scenes' 6 f blur-in |
| `#NN` numeral, white `#` + lime digits (SM-NUM-A) | v01 @0:10–0:12 #01, @0:29–0:30 #02, @0:45–0:47 #03, @1:26–1:28 #05, @1:41–1:42 #06, @1:53–1:55 #07, @2:00–2:07 #08, @2:16–2:17 #10 | Numeral ≈ 590 px wide, cap ≈ 216 px, centre y ≈ 1060–1075; captions hidden while up |
| Lime hash + white condensed digits (SM-NUM-B) | v03 @0:23–0:24 #10, @0:32–0:33 #09, @0:45 #08, @0:55–0:56 #07, @1:05–1:06 #06, @1:17 #05, @1:29–1:30 #04, @1:43–1:44 #03, @1:55 #02 | Centre y ≈ 1100–1120 |
| Label chip above the numeral | v01 @0:11 "Personal Context", @0:30 "Actions", @0:46 "Notify Me", @1:26 "Phone App Intelligence", @1:41 "Siri On Camera", @1:53 "Dictation" | White box, black italic serif ≈ 54 px, centre y ≈ 866 |
| Teaser chip | v01 @2:00–2:07 "Wait for the Next 02 >>>" on #08 | Two items left (#09, #10) |
| Recap chip | v01 @2:16–2:17 "Recap Feature" on #10 | |
| Numbering asc / desc | v01 ascending #01 → #10; v03 descending #10 → #02 (#01 off-sheet) | `numbering` VAR, default desc |
| Item cadence 10–20 s | v01 items at 0:10, 0:29, 0:45, 1:26, 1:41, 1:53, 2:00, 2:16; v03 at 0:23, 0:32, 0:45, 0:55, 1:05, 1:17, 1:29, 1:43, 1:55 | → re-hook every ≤ 25 s (V-REHOOK) |
| Tool card over the dimmed presenter | v03 @0:25–0:31 TubeTutor, @0:34–0:44 Screencap, @0:46–0:54 Mubert, @0:57–1:04 Open Generative AI, @1:07–1:15 Halo, @1:18–1:27 Meetily, @1:31–1:42 Qwen, @1:45–1:54 MiniMax, @1:56–2:08 Voicebox, @2:10–2:29 NVIDIA | Brand row y ≈ 673–690 (logo ≈ 80 px + name ≈ 50 px); window x 54–1008, y ≈ 738–1303 (16:9); lime pill cy ≈ 1342–1350; presenter blurred ≈ 10–14 px and darkened ≈ 50 % |
| White frame on the window (TH-lime) | v03 @2:10–2:29 (NVIDIA cards), @1:23 | Dark windows without a frame in the earlier v03 items; the frame is the TH-lime default here |
| Logo behind the head at item start | v03 @0:24 (red tile), @0:45 (Mubert), @0:56 (Open Generative AI "M"), @1:06 (Halo), @1:17 (Meetily), @1:29 (Qwen), @1:44 (MiniMax), @1:55 (mic), @2:09 (NVIDIA) | Logo ≈ 400 px at y ≈ 144–560; behind the matte; stays dimmed through the card |
| Screen swaps every 2–3 s inside a card | v03 @0:57–1:04 (4 screens), @1:31–1:41 (6 screens), @2:10–2:23 | `max_gap_s` 2.5 |
| Cursor highlight on a named element | v03 @0:53 "Add to my downloads" (yellow outline + cursor), @2:02–2:03 cursor hand | → P-CURSOR-BOX (lime role) |
| Paid vs free | v03 @2:02–2:05 "elevanlabs charges / $22 a month for this. / This one is open / source, free forever" | → P-PRICE-STRIKE (the reels show it in captions only; the chip is this template's visual for D1) |
| 50/50 split, caption on the seam | v01 @0:02–0:03, @0:06–0:08, @0:13–0:19, @0:25–0:28, @0:40–0:44, @0:50–0:56, @1:19–1:22, @1:33–1:37, @1:50–1:52, @1:56–1:59, @2:08–2:12, @2:24–2:27, @2:30–2:33; v02 @0:00–0:05 | Seam measured y 953–960; caption pill centred on it; v02 adds a black gradient fade above the seam (≈ 140 px) |
| Lower split variant | v02 @0:21–0:30, @0:38–0:47, @0:51–0:58, @1:02–1:08, @1:17–1:22 | Graphic ≈ y 0–1000, caption ≈ cy 1180, presenter from ≈ y 1240; not adopted as a second layout (one seam keeps the caption band constant); TUNE range 900–1060 covers part of it |
| Full-screen graphic boards | v01 @1:14–1:17 (phone on an orange gradient), @1:33–1:37 (blue gradient phone); v02 @0:18–0:20, @1:11–1:13 (black world, framed clip, italic lines) | → L-board, W-board warm/cool, P-PHONE-BOARD, P-FRAMED-CLIP |
| Words on full-bleed B-roll | v02 @0:33–0:35 "No radiation" / "No magnet" / "No tube" | → P-RENDER-WORDS |
| Note card with an orb (assistant request) | v01 @0:21–0:24 "Hey, my teammates sent…", @1:03–1:06 "keep checking this page…", @2:24–2:27 "Hey Siri, what was spoken…"; @2:56–2:58 "Comment below" | The reels use a real assistant's orb; this template uses a generic gradient orb (N8, NC-7) |
| Logo pop / cluster at chest | v01 @1:09–1:12 (three round badges), @1:29–1:31 (one app tile) | → P-LOGO-CLUSTER, P-LOGO-POP |
| Feature icon grid | v01 @0:08 (health icons in circles) | → P-FEATURE-GRID |
| HUD marks + readout on B-roll | v02 @0:02–0:03 (corner brackets, "284" gauge) | Readout only for spoken numbers here (NC-6) |
| Dot-matrix figure | v02 @0:00–0:03 | → P-DOT-REVEAL / T-9 |
| Hook: plate + proof card | v01 @0:00.17–0:01.67: "The most exciting part" (white on black) / "of WWDC-26" (white on red) at cy ≈ 1000/1080; white card "This not the / exciting part" + image at y ≈ 1100–1590 | Moved up to cy 960/1036 and card y 1084–1484 to respect NC-5 (no meaning text below 1500) |
| First proof cut ≤ 2 s | v01 @0:01.83 cut to split (phone UI) | payoff ≤ 2.5 s |
| Hook: post header + clip (HA-18) | v03 @0:00–0:08: header y ≈ 324–432, clip band y ≈ 461–1397, emoji-avatar progress bar at the band's bottom, presenter absent 8 s | `max_absence_s` 8 |
| Hook: split thesis (HA-12) | v02 @0:00–0:03: B-roll top + seam caption @0:33, italic @1:67, HUD @2:17–2:83 | |
| Teaser lockup + tiles (HA-05) | v03 @0:11–0:13 "*#02, #03 and #08* / do the whole job for ₹0" + three tool tiles | |
| Warm wash transition | v02 @0:07; v03 @0:08, @0:44 (red), @1:16, @2:09, @2:33 | ≤ 85 % peak opacity here (NC-11) |
| Vortex burst | v03 @0:17 (radial burst into the first item) | once per reel |
| Lime swipe into a numeral | v03 @1:28 (lime bars before #04) | |
| Series card | v02 @0:08–0:09 "Welcome to / *Day 60* / Of future tech updates"; v03 @0:15–0:16 "Welcome to / *Week 09* / of the AI tools" | Number ≈ 150–180 px italic serif; kicker/sub ≈ 50 px sans; at 8–15 s |
| Re-crop on jump cuts | v01 @0:57–0:58, @1:12–1:13, @2:13–2:15, @2:28–2:29, @2:36 (wide ↔ tight framing) | No visible zoom moves anywhere → `crop_on_cut` |
| End stack | v03 @2:30–2:32 Save (red bookmark badge behind the head) + "Save this now / *because 90% of you will forget*", @2:34–2:35 "And follow / *because I do this every single week*", @2:36–2:38 "And if you want / *all 10 with the links and the GitHub repos*" + tile behind the head, @2:39–2:42 community card | Community card ≈ 3.7 s; v02 @1:26–1:28 and v01 @2:45–2:48 same card |
| Community card | v01 @2:45–2:48; v02 @1:26–1:28; v03 @2:39–2:42 | Dark green dot grid, italic "Join the free", heavy lime headline with glow, phone mock, "Link in Bio" pill tapped by a 3-D cursor, floating chat glyphs |
| Calm, no comedy | all three reels: no stickers, stamps, shakes or meme moments | comedy off |
| Brand spelling QA | v03 @2:02 "elevanlabs" (a visible typo) | H11 |

## 2. Inferred values (not directly measurable)

| Value | Inference |
|---|---|
| Motion frame counts (numeral pop 8 f, card rise 10 f, dim 8 f, chip 6 f) | Read from 6 fps hook sheets and 1 fps body sheets: entries complete within one 1 fps step; exact frames chosen inside G3 limits |
| Dim amount (blur 12 px, luma −0.5) | Visual estimate of v03's dimmed presenter (face recognisable, background near-dark) |
| Cadence 4–8 SC per 10 s | Caption swaps every 1–1.5 s (weight 0.5) + 2–4 picture changes per 10 s counted on the 1 fps sheets |
| P-PRICE-STRIKE, P-STAT-LINE, P-CURSOR-BOX in lime | Built to satisfy D1 from moments the reels show in captions or with a yellow outline; colours mapped to this template's roles |
| The count-card fallback for buyers without a series | Same recipe as the series card; no evidence (buyer need) |
| Generic orb, monogram tiles, created community screen | Required by NC-7 (no fetched brand marks); the reels use real brand assets |

## 3. Unverified (default to TUNE / VAR)

| Path | Why |
|---|---|
| `profile.language.speech` | No transcript existed; on-screen text is English in all three reels. The template supports en/en (default), hinglish/en, hinglish/hinglish and hi/hi |
| `profile.language.captions.transform` | Depends on the real speech language (verbatim for English, translate for Hinglish) |
| `sound.bed.on` | Sound is not observable; the bed choice follows the bundled pack's defaults |

## 4. Known gaps and engine requests

| Gap | Today's handling |
|---|---|
| The caption engine puts the whole emphasis phrase on one line; the reels wrap 4–7-word italic phrases over two staggered lines (v02 @1:15 "said they'll / sell your data") | Emphasis phrases are capped at 2–4 words / 22 characters (§5.3); longer questions emphasise their last ≤ 22 characters. **Engine request:** `tiers.keyword_wrap: 2` with a stagger offset (−40 / +40 px) |
| ~~`connector_container` puts a pill on plain lines~~ | Resolved by the 2026-10 audit: full-frame captions never have a pill (CS-1 bare); the pill lives only in CS-1S (seam) and CS-2 (card), routed by `captions.by_layout` |
| The reels align the plain line before the italic phrase to its left edge and the line after it to its right edge (v01 @0:05) | Centred lines. **Engine request:** `tiers.align: stagger` |
| Theme packs cannot pick a caption profile, and the PV-8 cross-pack contrast check compares a pack's role against the *other* pack's resolved `text_on` role | Two profiles CS-1/CS-2; the reel header sets `captions.profile` from the theme (§4.3). **Engine request:** `themes.<id>.captions.default` and a per-pack contrast check |
| Third-party cinematic renders (v02 medical renders) | Creator-supplied only (SH-5); otherwise FB-5 created diagrams |
| A second split variant with a lower seam (v02) | Folded into the seam TUNE range (900–1060) |

## 5. Fidelity audit 2026-10 (full-resolution frames, 720×1280 sources scaled ×1.5 to 1080×1920)

| Measure | Evidence | Value → token |
|---|---|---|
| Full-frame captions have **no pill** | v01 @0:05.0 "This is / *exciting part* / not the most", @0:09.0 "which"; v03 @2:31 "Save this now / *because 90% of you will forget*" | `CS-1.tiers.connector_container: null` |
| Full-frame plain size | v01 @0:05.0: "This is" ascender-to-baseline 48 px, "not the most" 46 px → ≈ 62–66 px | `CS-1.skin.size` 60 |
| Full-frame italic size | v01 @0:05.0 "exciting part" 123 px (asc+desc), 724 px wide; v03 @2:31 79 px per line | `keyword_px` 116 |
| Full-frame caption centre | v01 @0:05.0 block 995–1247 (centre 1121); @0:09.0 "which" ≈ 1047 | `CS-1.position.cy` 1080 |
| Seam caption | v01 @0:02.5: text 923–965 (≈ 44 px font), 539 px wide; pill sampled `#5A5A5A` over white B-roll → black ≈ 65 %; seam line y 950–955 | CS-1S 42 px, opacity 0.65, seam 952 |
| Split italic | v02 @0:02.0: connector 37 px span (≈ 40 px font), italic lines 71 / 56 px (≈ 76 px font), bare white on the dark fade | CS-1S keyword 80 |
| Italic entry | v02 @0:01.567–0:01.767: the italic line arrives smeared (horizontal blur) for 2+ frames, sharp by 1.70 | swap `blur` 4 f |
| Lime | v01 @0:11 digits `#C7FF0C`/`#C8FF0B`; v03 @0:27 pill `#B9FC0E` | `primary` `#C6FF0C` |
| Plate red | v01 @0:00.6 line-2 plate `#E60005` | `accent` `#E60005` |
| Plate geometry | v01 @0:00.6: black plate y 955–1038, red y 1042–1114 (cy 997 / 1078); text 974–1036 | unchanged (cy 1000/1078 in tokens) |
| SM-NUM-A | v01 @0:11: `#` x 202–488, digits x 494–820, y 930–1182 (cap 252 px), centre 1056; Montserrat 900 matches the round `0` and flagged `1` (Inter Tight's `0` is too narrow) | `display` Montserrat, size 330–360, cy 1056 |
| SM-NUM-B | v03 @0:24: lime `#` x 342–738, y 1002–1396; white digits x 434–646, y 1086–1320; centre ≈ 1200 | hash 540, digits 330, cy 1200 |
| CS-2 pill | v03 @0:27, @0:50: pill x 321–755, y 1312–1374 (h 62, cy 1343) | L-card caption cy 1343 |
| Logo behind head | v03 @0:24: red tile x 377–701, y 211–523 | consistent with P-LOGO-BEHIND |

## 6. Motion audit 2026-10 (full frame rate, 30 fps)

Method: ffmpeg scene scores (> 0.08, multi-frame clusters = transitions) on all three reels; 17 bursts of 10–28 consecutive frames; ORB + `estimateAffinePartial2D` per frame pair for scale; jump-cut pairs for re-crops. Strips: `docs/audit/tech-countdown/strip-*.jpg`.

| Measure | Evidence | Value → token / section |
|---|---|---|
| Shot lengths | v01 107 shots, median 1.33 s, p90 3.07, max 5.2; v02 42 shots, 1.67 / 4.0 / 4.3; v03 45 shots, 3.03 / 8.5 / 12.6 (cards) | `cadence.median_shot_s` 3.5; §7.6 |
| Warm leak wash (T-2) | v01 @0:10.13–0:10.57 (6 f leak, 1 f white @0:10.30, residue to 0:10.57); v02 @0:07.02–0:07.58 (white @0:07.25); v03 @0:08.33–0:08.80 (white @0:08.50), @0:22.67–0:23.0, @0:44.5, @0:54.7, @1:04.9, @1:16.1, @1:28.03–1:28.40, @1:42.5, @1:54.5, @2:09.1, @2:29.5, @2:33.20–2:33.57 (red-yellow field, no white) | §9.1 T-2; TH-lime door on every item. Now built-in: `leak` `frames` 15, `pre` 6 (6 f build, 9 f residue) + `fx.flash` up 1 / hold 0 / decay 2 for the 1 f white (was a 12 f gradient capped at 85 %) |
| Rush-in after the wash | v03 @0:22.97–0:23.37 per-frame scale 1.20, 1.15, 1.07, 1.05, 1.035, 1.025, 1.015 … (≈ ×1.7); @1:28.27–1:28.67 ≈ ×1.69; @2:33.47–2:33.77 ≈ ×1.6; after the hook wash @0:08.73–0:08.93 ≈ ×1.12 | `camera_presets.snap-punch` / `crash-zoom` `from_wide` 0.59 (×1.7) → base, 12 f, `expoOut` (Z-1 / Z-2); hook wash `p.from_wide` 0.89, 8 f. Now built-in (was 1.0 → 1.25 from the base) |
| Jump cuts keep the crop | full → full pairs v01 @0:39.8 (s 0.98), 0:44.5 (0.98), 0:57.1 (1.00), 1:01.2 (1.01); v02 @1:08.3 (1.00) | old Z-1/Z-2 alternation removed |
| Slow drift | v01 @2:48.9 → 2:53.9 one shot, s 1.096; v02 @0:48.0 → 0:50.7 s 0.974 | Z-3 1.0 → 1.08 linear |
| Hook plate entry | v01 @0:00.00–0:00.07 bare pre-roll; @0:00.07–0:00.27 plate + card group zooms ≈ 2× → 1 with motion blur (ORB 0.76 → 0.83 per frame); prop strobe red/black every 2–3 f @0:00.33–0:00.67+ | §5.2 f0 / Life |
| First proof cut | v01 @0:01.85 hard cut, split complete on the cut frame | G-1 |
| SM-NUM-A entry | v01 @0:10.33 (under the white), @0:29.37 one-frame horizontal smear-stretch, settled @0:29.40, constant size after | §7.3, P-NUMERAL-A |
| SM-NUM-B entry | v03 @0:23.03–0:23.07 lime bars swipe (2 f), numeral full size @0:23.10, digits flicker @0:23.17–0:23.37; same @1:28.43–1:28.67 | T-6, P-NUMERAL-B |
| Logo behind the head | v03 @0:23.55 cut-on at full size, 14 f after the numeral | P-LOGO-BEHIND |
| Card entry | v03 @0:24.55–0:24.62 horizontal streak wipe (3 f) carrying the numeral out; card + brand row complete @0:24.65; dim ramps luma 53 → 36 over 12 f | T-11, G-3, `stage_morphs.dim` 12 |
| Board in / out | v01 @1:14.20 hard cut onto the phone board; @1:17.68–1:17.80 phone pushes ×1.03–1.06/f, @1:17.82–1:17.92 rushes into the white screen, hard cut @1:17.95 | G-5, T-12 |
| Board caption | v01 @1:14.3 "You can just explain", @1:17.6 pill at cy ≈ 960 over the phone | L-board caption cy 960 |
| TH-studio plain caption | v01 @1:13.95 "It's called shortcuts": cap height 32 px (≈ 44 px font), `ink` pill y 928–992, hard swap (also @0:01.85, @1:17.95) | `captions.by_theme.TH-studio`; pill only on plain-only chunks: `tiers.connector_container_when: "plain_only"` (now built-in; emphasis chunks no longer pill their plain lines) |
| TH-lime typing captions | v03 @0:17.67–0:17.95 "I went through" types ≈ 1.5–2 chars/f; @2:33.67–2:33.77 "And follow"; italic phrase pops in 1–2 f @0:17.92 | `by_theme.TH-lime` `reveal: "char"`, `cps` 50. Now built-in (was `reveal: word` + blur 2 f) |
| Italic / word-group smear | v02 @0:34.77–0:34.93 "No magnet" smears out 2 f, "No tube" smears in 3 f on the B-roll cut | CS-1 swap `smear` 3 f in / 2 f out (`smear_px` 24, angle 0, `stretch` 1.6); P-RENDER-WORDS `ctx.blur(px, 0)`. Now built-in (was isotropic `blur` 3 f) |
| Dot dissolve | v02 @0:00.17–0:00.33 (6 f); first caption blur-in @0:00.37 | T-9, HA-12 |
| Series kicker types on | v02 @0:07.45–0:07.58 "Welcome to", 1 char/f | P-SERIES-CARD |
| Vortex into the tool wheel | v03 @0:17.12–0:17.38 leak; @0:17.42–0:17.60 zoom-through into a radial wheel world (×1.19, 1.13, 1.08, 1.05 per frame); presenter matted over it until @0:22.6; radial white speed lines @0:22.60–0:22.63 | T-5, W-wheel, P-WHEEL-STAGE |

## 7. Engine built-ins pass 2026-10
Now built-in (the workaround recipes are deleted from the playbook):
- Captions: TH-studio pill only on plain-only chunks (`tiers.connector_container_when: "plain_only"`, v01 @1:13.95 vs @0:05); TH-lime per-character type-on (`reveal: "char"`, `cps` 50 = the measured 1.5–2 chars/f, v03 @0:17.67); base CS-1 swap `smear` 3 f in / 2 f out (v02 @0:34.77–0:34.93).
- Camera: the rush-in starts wide via `from_wide` 0.59 (= ×1.7, v03 @0:22.97, 1:28.27, 2:33.47) with `ease: expoOut`, landing on the base framing; the old 1.0 → 1.25 cap and the Z-2 `pull-out` reset are gone (Z-2 is now the same rush-in under `crash-zoom`, so doors alternate presets). Hook wash: `p.from_wide` 0.89, 8 f (×1.12, v03 @0:08.73).
- Transitions: T-2 is a core `leak` (15 f, `pre` 6, the wash ramp + white stop, `peak` 1.0) plus a 1 f `fx.flash` on the cut at section breaks; TH-lime doors use a red-yellow leak without the flash. T-5's leak and its blur, T-12's motion blur (`zoom-blur`) are built-in; T-6 and T-11 are `fx.streak`; the series kicker and HUD readout use `fx.typeOn`.
- Still scene-driven: the T-5 wheel zoom-through and the T-12 phone push (the scenes scale themselves; only their blur is built-in). The leak alone cannot hold a pure-white frame, hence the separate `fx.flash`. No glitch device was measured in v01–v03, so none is added.
