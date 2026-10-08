# Archive Explainer: evidence map (App. B)

**Sources.** `vibe-editing-os-research/analysis/short/johnny-harris.md`; frame sheets `evidence/short/johnny-harris/v01–v03/sheets/*.jpg` (hook at 6 fps, the rest at 1 fps), `meta.json`, `cuts.json`. All three sources are 720 × 1280; every measurement below is converted to the 1080 × 1920 frame (×1.5; sheet tiles are 300 × 534 px, so ×3.6 from tile pixels). Colours were sampled from the sheets (JPEG, ±6 per channel). No transcripts: the spoken words were read from the burnt-in captions. Sound is not observable.

| Video | What | Duration | Cuts/min | Median shot |
|---|---|---|---|---|
| v01 | Archive explainer (sports-business story), Search Party branding | 80.25 s | 24.7 | 1.08 s |
| v02 | Archive explainer (sport/culture history) | 59.48 s | 19.2 | 1.64 s |
| v03 | Two-camera podcast clip | 42.80 s | 11.2 | 3.10 s |

## DNA rule → evidence
| Rule / token | Value | Evidence |
|---|---|---|
| CS-A font | JetBrains Mono 700 (monospaced, slab-free) | every caption v01 0:00–1:12, v02 0:00–0:54 |
| CS-A size | 58 px | v01 0:01 "The King of FIFA" spans 164 tile px = 590 px for 16 chars → 37 px advance → 61 px at 0.6 em; v01 0:14 "One is reported" 554 px / 15 chars → 61 px; v02 "Japanese baseball" 34.7 px advance → 58 px. Chosen 58 (TUNE 54–64) |
| CS-A container | one box per chunk, as wide as the longest line; black ≈ 70 % | v01 0:14, 0:24, 0:43; v02 0:16, 0:54 (crops: one rectangle, short line centred inside); sampled #090E36 on blue (#1A2EA6 × 0.3 ≈ #080E32), #4D5353 on a light photo |
| CS-A position | block centre y 1415 | v01 first line centre 1379, 2-line block 1343–1487; v02 first line 1429, block to ≈ 1530; engine centring (no top/bottom anchor) → 1415 keeps the box ≤ 1500 |
| CS-A chunking | 2–5 words, ≤ 2 lines, ≤ 18 chars/line, punctuation kept, hard swaps | v01 0:08–0:24 (≈ 1 chunk/s, "Donald Trump.", "each to start,"); no fades seen between consecutive 6 fps frames (hook sheets) |
| CS-B font / size | Inter Tight 800, 60 px, soft shadow | v03 0:01 "thing it teaches me" 670 px wide; cap height ≈ 41–45 px; line pitch ≈ 96 px; the face is a tight grotesk (unverified family) |
| CS-B container | one box per chunk, bright blue, translucent ≈ 85 % | v03 0:22 "I yeah, / more and more," (sweater texture visible through the box); sampled #1940D9 |
| CS-B position | bottom line at y ≈ 1483, block centre ≈ 1435 → 1405 | v03 0:01–0:40 (all chunks; single lines sit on the second-line row) |
| W-blue | #1A2FAA (sampled #112595 v01, #1C33A5 v02), 1–3 % grain | v01 0:08–0:22, v02 0:07–0:20 |
| Card rect | x 43–1037, y 511–1130, radius ≈ 40 (template: x 64–1016 for the 64 px margin) | v01 0:25 (green card), 0:46 (photo card), 0:48–0:52 (maps); v02 0:07–0:12 |
| Tall card | ≈ 994 × 987 at y 324–1318 | v02 0:17–0:20 (square map), 0:25–0:44 (comparison cards) |
| Receipt recipe | outlet small lime-grey, headline wide grotesk white → key span lime, others dimmed lavender; lime dot + thin leader with a rounded corner off the left edge; decorative body copy; square-cornered photo thumbs; the block moves up as thumbs arrive | v01 0:08–0:22 (Financial Times), 0:34–0:38 (same card, new body highlight), 0:39–0:41 (Guardian swap), 1:02–1:09 (Yahoo Sports, 3 thumbs) |
| Receipt colours | lime ≈ #CAF689 (sampled; analysis #D7F45A) → #D4F56A; dim words ≈ lavender → #A6B1F0 (raised to 5 : 1) | same |
| Type-on | letters missing mid-reveal ("Financ al T mes") | v01 0:08 |
| Green figures | world #1B473A, card #19613B, seat arc + avatar ring + flying tokens; bars timeline | v01 0:25–0:33, 1:12 |
| Maps | navy sea #16225B / #121B3A, grey land #7D8381, focus white #E1E6E0, label chips, pins, faces on map, dashed routes with a red ×, token migration | v01 0:46–0:52, 1:13; v02 0:07–0:20, 0:49–0:55 |
| Comparison | darker-blue card, framed clip, chip at the frame bottom: red + flag "CONSISTENCY" vs white + flag "POWER"; next card peeks left; horizontal swipe | v02 0:25–0:44 (sampled red #BA3221, white #DBE2DA) |
| Hook HA-11 | f0 tight face + chunk 1; re-crop cut 0.42; bills wipe 1.17–2.33 covering by 1.83; confetti over picture 2; twist chunk 2.83 | v01 hook sheet 0:00–0:03 |
| Hook flurry | colour card 0.00, B&W 0.33, sepia halftone 0.50, live clip 1.00, punch 1.83 | v02 hook sheet |
| HA-14 | cold open mid-sentence, first chunk 0.5 s, no cut until 11.5 s | v03 hook sheet, s_01 |
| F-B cuts | 11.53 (guest reaction 1.5 s), 13.03 (host, re-framed), 19.07 (guest speaks), 22.07 (host), 31.57 (wide of guest), 35 (wide of host), 36 (guest) | v03 s_01–s_03 |
| Re-hook | "Now why is Infantino…" over a hard cut to a face | v01 0:24 |
| Roll-by | a football rolls across the frame as a wipe | v01 0:04 |
| Archive treatments | B&W, sepia halftone, VHS colour | v02 0:00–0:06, 0:13–0:16, 0:45–0:48 |
| Cross-promo | white world, video card, cursor click, grey caption box | v01 1:14–1:16 |
| End card (tagline) | #0A1314 ground, 4-line heavy wide sans, words in cyan #35CFD2 and red #C64D3C, round logo + Subscribe → Subscribed + Join, fades in | v01 1:17–1:19, v02 0:56–0:58 |
| End card (QR) | bright blue #0847F4, 3 mono lines, URL in a white box, white QR ≈ 620 px | v03 0:41–0:42 |
| Cadence F-A | 15–30 cuts/min, median 0.9–2.2 s, ≈ 1 caption chunk/s | meta.json v01/v02; sheets |
| Cadence F-B | 7–16 cuts/min, median 2–5 s | meta.json v03 |

## Inferred (not in the evidence)
- P-TIMELINE-RAIL, P-SPONSOR-SOURCE, P-B-NAME-PLATE, P-B-QUESTION-PLATE, P-B-STACK and the HA-03 alternate: designed to fit the system; none appears in the three videos.
- Created plates (silhouette, object, date) and the schematic locator card: substitutes required by the ask-then-create policy and the missing geo bundle.
- The F-B guest italic: required by V-SPEAKER (the source uses one style for both speakers).
- The music bed from f0 (F-A): sound is not observable.

## (unverified)
- `profile.language.speech` (no transcript; captions are English).
- `sound.bed.on` (not observable).
- `captions.profiles.CS-B.skin.slot` (the podcast caption face is a tight grotesk; Inter Tight is the closest bundled face).
- `type.end_tagline.slot` (the end-card face is a wide rounded heavy sans; Montserrat 800 is the closest bundled face).
- `type.src_headline.slot` (the receipt headline face is a wide geometric grotesk; Space Grotesk 700 is the closest bundled face).
- `dialogue.stack.share` (no stack in the evidence).
- `captions.speakers.guest.style`.

## Known gaps
- Geo maps (E-18): P-MAP-CARD is unavailable; P-LOCATOR-CARD is the fallback.
- Caption vertical anchoring: the evidence top-anchors F-A (1-line chunks sit on the first-line row) and bottom-anchors F-B; the engine centres the block on `cy`.
- The source reel's caption typo ("lenghts", v01 0:54) is treated as a QA failure, not DNA.

## Fidelity audit 2026-10 (full-resolution frames, 720×1280 ×1.5)
Frames: v01 @0:00.0, 0:00.5, 0:01.00, 0:01.08, 0:01.17, 0:01.25, 0:01.5, 0:02.5, 0:10.0, 0:15.0, 0:28.0, 0:48.0, 1:16.6, 1:18.0, 1:20.0; v02 @0:00.0, 0:00.4, 0:01.0, 0:02.0, 0:10.0, 0:30.0, 0:52.0, 0:57.0, 0:59.2; v03 @0:01.0, 0:20.0, 0:41.5. Report: `vibe-editing-os/docs/audit/archive-explainer/audit.md`.

| Claim | Measured | Where |
|---|---|---|
| CS-A size 58 px confirmed (not ≈ 40 px) | "The King of FIFA" 16 chars span x 246–834 = 36.8 px/char → ≈ 61 px mono; 2-line pitch 72 px (= 58 × 1.24) | v01 @0:00, @0:15; v01 @0:28 |
| CS-A box = one rect per chunk, black ≈ 60 % (was 70 %) | 2-line box y 1336–1490, x 320–760; #060D37 over #132595 and #0D1A51 over #1C33A5 → 50–68 % black | v01 @0:15, v02 @0:10 |
| CS-A block centre 1413 (cy 1415 confirmed); v02 sits lower (box to y 1534; kept above 1500) | — | v01 @0:15, v02 @0:10 |
| Chunk swap is a hard swap of the whole chunk (no word build) | new chunk complete at 1.00; unchanged at 1.08–1.25 while the bills wipe rises under it | v01 @0:01.00–0:01.25 |
| Lime `accent` #CCF852 (was #D4F56A) | #C8F848–#C8F860 | v01 @0:15 "$20bn commercial vehicle" |
| Muted headline words #6478BC in source (2.4 : 1) → #8C9AD8 (3.8 : 1) | #6078B8–#6078C0 | v01 @0:15 "Fifa plans" |
| T-HEAD ≈ 72 px, line height ≈ 1.04 (was 64 px, 1.12) | ascender band 53 px; baseline pitch 75 px | v01 @0:15 |
| T-OUTLET ≈ 40–44 px (was 30 px) | "Financial Times" ≈ 425 px wide | v01 @0:15 |
| End tagline ≈ 138 px, tracking ≈ −0.04, x 93, cap top 151, off-white #E4ECE6; lines brighten from grey; "sports" cyan first, "geopolitics" red last | #707474 at 1:18, #E4ECE6 / #30D0D0 / #C85040 at 1:20 | v01 @1:18, @1:20; v02 @0:57, @0:59.2 |
| Logo disc Ø ≈ 295 at y 925–1220 | — | v01 @1:20 |
| Card rect x 44–1036, y 510–1130, r 40 (template x 64–1016 kept) | — | v01 @0:48 |
| T-HEAD family = the end-card family (Montserrat 700, tracking −0.03) | wide heavy grotesk with tight spacing in both | v01 @0:15, @1:20 |

## Completeness audit 2026-10 (motion at full frame rate)
Method: scene detection (scale 270, threshold 0.2) on v01–v03; full-rate bursts; cv2 ORB + `estimateAffinePartial2D` for scale / rotation / translation. Strips: `vibe-editing-os/docs/audit/archive-explainer/strip-*.jpg`. Report: `docs/audit/archive-explainer/completeness.md`.

| Claim | Measured | Where |
|---|---|---|
| Stinger: block rises accelerating, covers at 1.63, holds ≈ 6 f, lifts off decelerating to 2.43; picture 2 revealed underneath; caption stays visible on top | ≈ 1.35 s total (38–40 f at 30 fps) | v01 @1.09–2.43 (strip-hook-stinger) |
| Roll-by: ball Ø ≈ 1.1 × frame width, bottom → top, 7 f at 23.98 (≈ 9 f at 30); cut under it; caption on top | — | v01 @4.43–4.72 (strip-rollby) |
| Receipt: 4 f empty blue, then word-by-word type-on (a word every 2–3 f, each dim → white in 4 f); outlet letters random over ≈ 14 f | — | v01 @7.93–8.80 (strip-receipt-typeon) |
| Receipt follow-push ×1.145 and translate (−110, −300 px at 1080) over ≈ 22 f at 23.98; thumb fades in (no scale) | ORB scale 1.000 → 1.146 | v01 @14.52–15.40 (strip-receipt-settle) |
| Graphics animated on twos (consecutive identical frames in pairs) | ORB diff 0.0 between pairs | v01 @8.43–8.76, @14.52–15.40, @29.6 |
| Figure card hard-cuts in built; avatar rises 10 f from behind the arc | — | v01 @25.37–26.03 (strip-figure-card-entry) |
| Inner punch ×1.8 inside the seat-arc card, then pull-out ≈ 0.15 %/f | ORB per-frame s 0.998–0.999 after the punch | v01 @29.97–30.47 (strip-figure-push) |
| Map: inner punch ×1.52 (rot 0.9°), then pan ≈ 2.4 px/f at 270 w (≈ 9 px/f at 1080); new region = hard cut to a new map | — | v01 @49.14–49.48 (strip-map-fly), @51.6 |
| Archive still: settle −3.8 % in ≤ 5 f then static; hook face drift 0.4 %/s | ORB 0.962 / 0.998 | v02 @45.15–45.95; v01 @0.45–1.05 |
| Comparison: card hard-cuts in, previous card peeks left; media fades up from blue-tinted over ≈ 0.6 s; chip grows from a sliver ≈ 6 f; trait letters resolve ≈ 0.5 s; media hard-cuts inside the frame | — | v02 @25.36–25.96, @28.60–30.12 (strip-compare-entry, strip-compare-swipe) |
| Side change: chips / card push up off the top in ≈ 4 f | — | v02 @34.16–34.32 (strip-compare-flip) |
| Clip punch = cut to a tighter shot of the same action | ORB: no shared transform across the cut | v02 @1.88 (strip-v02-punch) |
| End card: hard cut; logo row rises ≈ 180 px over 8–10 f; tagline resolves dim → bright | — | v01 @76.80, v02 @56.00 (strip-endcard) |
| CS-B boxes are per line (two widths) | — | v03 @11.40–11.83 (strip-podcast-cut) |
| Pacing: picture changes / 10 s 4.2, 4.0, 1.9; median shot 1.08, 1.24, 3.10 s; p90 4.7, 4.7, 9.9 s; longest stretch without a cut 17.1 s (v01 receipt + figure), 19.2 s (v02 comparison deck), 11.5 s (v03) | scene threshold 0.2, changes < 0.2 s apart merged | v01–v03 |

## Engine built-ins (2026-10-07, engine cc324ec+)
| Device | Before (workaround) | Now built-in | Measured value now used |
|---|---|---|---|
| Graphics on twos | each scene rounded its own local time to 1/12 s by hand | scene field `step_fps: 12` (G3 judges per pose) on every graphic scene; clips stay at full rate | receipt, push and figure frames repeat in pairs: 12 poses/s (v01 @8.43–8.76, @14.52–15.40) |
| Letter resolve (outlet, chip trait word, end tagline) | a seeded per-letter reveal written in each scene | `VEOS.fx.resolve(text, lt, {at, dur, every, order: "random", seed, ctx, font})` | outlet 16 f (14–18 f, v01 @8.09–8.80); chip word ≈ 12 f (v02 compare strips); tagline over ≈ 1.5 s (v01 @1:16.6–1:20) |
| Side change push-up (G-3 / T-04) | the scene animated the old card off the top | built-in transition `push`, `dir: "up"`, `frames: 4` | cards push up off the top in ≈ 4 f (v02 @34.24). The built-in also carries the incoming card up from below, where the evidence has it already underneath |
| Label on a moving object in an archive clip | not available (static chips only) | optional `veos track --clip` + scene `anchor` (§17), with a caption-only fallback | — (no tracked labels in v01–v03; offered for buyers' clips) |

Still not built-in: **geo maps** (E-18; P-LOCATOR-CARD stays the fallback) and the **receipt follow-push as a camera** (canvas_camera stays off in this style; G-4 is the scene's own scale + translate, at the measured ×1.14 over 24–27 f).
