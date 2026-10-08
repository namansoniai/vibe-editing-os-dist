# Evidence: Long-form Re-cut (inspired by Veritasium)

Sources: `vibe-editing-os-research/analysis/short/veritasium.md` and the frame sheets `evidence/short/veritasium/v01–v03/sheets/*.jpg` (hook at 6 fps, whole video at 1 fps), `meta.json`, `cuts.json`. All three are 720 × 1280 re-encodes; every position and size below is measured on the sheets and scaled ×1.5 (720 → 1080, sheet cell 300 px → ×3.6). No transcripts exist; speech is read from the burnt-in captions. Sound is not observable.

| Video | Topic | Duration | Cuts (detector) | Median shot | fps |
|---|---|---|---|---|---|
| v01 | Antiproton decelerator (CAD renders, CERN interview) | 115.09 s | 26 (13.6/min) | 2.27 s | 29.97 |
| v02 | Portable antimatter trap (host, video-call guest, letterbox renders, map) | 153.32 s | 30 (11.7/min) | 3.07 s | 29.97 |
| v03 | Falling into a black hole (painted animation, HUD bands, host outro) | 110.02 s | 6 (3.3/min) | 4.63 s | 23.98 |

## DNA rule → evidence

| Rule (playbook id) | Evidence | How measured / note |
|---|---|---|
| `source_type: edited_master`, passthrough graphics (§0) | v01 @ 0:00–0:11 CAD fly-over with baked 3D text "ELENA" (0:33) and "16,200,000 km/h" (0:41); v02 @ 0:21–0:29 animated p̄ / CPT graphics; v03 painted animation throughout | All visuals are source-made; the re-cut layer is reframing + captions |
| CS-1 serif, 1 line, 1–3 words, hard swap (§5.3, E6) | v02 hook sheet 0:00–2.83 ("One thing" / "that makes" / "this research" / "so tricky" / "and also"); v01 hook sheet ("Strong electric" / "fields in the" / "accelerator" / "slow down" / "the antiprotons") | Chunks change between consecutive 6 fps samples with no intermediate fade |
| Caption size ≈ 70 px, weight ≈ 600 (CS-1 skin) | v02 s_01: "One thing" 320 px wide, "there is only one" 544 px, "another experiment" 652 px | Widths compared with Source Serif 4 at weight 600, opsz 20: 70.0–72.1 px. The caption library default (62 px) is replaced |
| Caption centre y 1380 (CS-1 position) | v01/v02 sheets: text centre at cell y 384/534 → y 1384; v03: 374/534 → y 1345 | Range 1345–1384; template 1380, TUNE 1300–1460 |
| Caption stays at the same y in every layout | v02 @ 0:58–1:11 (letterbox), v03 @ 1:09–1:29 (blur-fill), v01 full-bleed | Caption under the band at the same y |
| Stroke + shadow | v01 @ 0:29–0:33 white text on light CAD shows a dark edge; v02 @ 2:24 on a bright map | Inferred 2 px dark stroke + soft shadow; exact values unverified |
| Guest colour gold `#EDD462` (roles.accent) | v02 s_06 @ 1:31, s_08 @ 2:12, s_03 @ 0:45; v01 s_05 @ 1:25 | Brightest-quartile median of gold glyph pixels: #E9D462, #EBD560, #E6D66A, #E7D565 → #EDD462. Library default #F2C14E (more orange) replaced |
| Colour follows the voice, not the face (R-3) | v02 @ 1:29–1:30 gold "This is one of these / Penning traps." over the host's face; v02 @ 2:10–2:15 gold over the host in profile; v02 @ 2:21 gold "will get" over the host; v01 @ 1:23–1:24 white "because you can't have perfect vacuum." over the guest's back; v01 @ 0:54–0:57 gold over B-roll details | — |
| Cold open, no graphic, caption at f0 (HA-14, H1) | v01 @ 0:00 "Strong electric" on a moving CAD orbit; v02 @ 0:00 "One thing" on the host mid-gesture; v03 @ 0:00 "You can" on a drifting ship | Captions present at 0.000 in all three hook sheets |
| First shot held long (P-RENDER-HOLD, §6.2 table) | v01 first cut 11.51 s; v02 17.75 s; v03 4.63 s then 85 s uncut | `cuts.json` |
| Hook change count ≈ 5 in 0–3 s (`hook_sc_3s: 4`) | v01 5, v02 5, v03 6 caption swaps in 0–3 s | Hook sheets |
| Cadence from captions (`caption_weight 1.0`, sc_per_10s 6–15) | A new chunk every 0.6–1.0 s; ≈ 2.4 words/s | Hook and 1 fps sheets |
| Band geometry y 656–1264, caption under (RF-3, L-band-*) | v02 @ 0:58–1:11 and 1:46–1:50 (black); v03 @ 1:09–1:29, 1:32–1:34, 1:45–1:46 (blur-fill) | v03 s_04/s_05: band 662–1255 (cell px 184–349); equals the compositor's centred 1080 × 608 band |
| Band share ≤ 25 % (SS-6) | v02 ≈ 22 s / 153 s = 14 %; v03 ≈ 24 s / 110 s = 22 % | — |
| Full-bleed face crops, head top y 150–260 (RF-1) | v02 @ 0:00–0:17, 1:40–2:06; v01 @ 0:12–0:28 | — |
| Baked labels kept whole in crops (P-BAKED-TEXT-SAFE) | v01 @ 0:33–0:44 "ELENA", "16,200,000 km/h"; v03 @ 1:37–1:40 vertical credit lines at the left edge kept in frame | — |
| Blank-caption pauses ≤ 2 s (P-PAUSE-BREATH, H8) | v03 @ 0:49–0:51, 1:06–1:08 (black, no caption) | — |
| Splice across shoots (P-DIP-SPLICE) | v03 @ 1:30 and 1:44: the host from a different shoot (night, grey tee) after the animation | Measured 2026-10-07 at 24 fps: a hard cut (0 f) at 1:29.87; the dip was withdrawn |
| Dissolves rare | v03 @ 1:12–1:29 cross-dissolves inside the HUD sequence; v02 @ 0:54 blink | — |
| No zoom added (`zoom_policy: source_only`) | Camera motion is inside the source (dolly, orbit, handheld); v02 @ 1:40–1:46 push likely source | — |
| No CTA / end card (cta none) | v01 ends @ 1:54 on CAD "from normal matter."; v02 @ 2:32 map "research institutions."; v03 @ 1:49 wormhole render | — |
| Explainer arc, re-hooks ≤ 26 s (§7) | v02: problem 0:00–0:17 → mechanism 0:18–0:58 → proof 1:08–1:47 → implication 2:06–2:32; world changes ≈ 0:18, 0:32, 0:58, 1:12, 1:23, 1:40, 2:00, 2:07 | — |
| Italic serif object title (P-OBJECT-TITLE) | v02 @ 1:08–1:11 "Antimatter Trap" at y ≈ 720 | At 1:08 the object passes in front of the title, so it is probably baked into the master's render. Kept as a rare (≤ 3) editor device for masters that show an object unnamed |

## Unverified / inferred
- Speech = caption text (verbatim transform): no transcripts.
- Caption lead (1 frame) and exact stroke/shadow values.
- Sound (music bed, effects): not observable; the template keeps the master's mix and adds nothing.
- The italic object title may be source-baked (see above).
- v03's caption face is a lighter Computer-Modern-like serif; v01/v02 use a semibold transitional serif. The template ships the semibold (Source Serif 4 600); EB Garamond is the TUNE alternative.
- Whether the re-cuts reorder sentences: only the v03 outro splice is visible.
- Presence shares (≈ 40 / 55 / 5 %) are estimates from the 1 fps sheets.

## Fidelity audit 2026-10-06 (full-resolution frames, 720 × 1280 → × 1.5)
Frames: v01 @ 0.0, 0.5, 12.5, 30, 60, 90, 114; v02 @ 0.0, 0.3, 0.6, 1.0, 1.1, 1.2, 40, 90, 120, 152.5; v03 @ 0.0, 1.0, 30, 50, 80, 109. Report: `docs/audit/long-form-recut/audit.md`.
| Measure | Value | Frame |
|---|---|---|
| Caption face / size | Source Serif 4 600 match; "One thing" 321 × 67 px → ≈ 70-72 px; cy 1377 | v02 @ 0.0, 2:00 |
| Caption swap | hard, 2-word chunks, ≈ 0.4 s ("One thing" → "that makes" → "this research") | v02 @ 0.6-1.2 |
| Gold | #E8CC28 (232,204,40) | v01 @ 1:00, 1:30; v02 @ 1:30 |
| Gold on host | host on location in gold | v02 @ 1:30 |
| Animation reel | lighter LaTeX-like serif, cy 1341 | v03 @ 0:30, 1:49 |
| Framing | full-bleed 9:16 in every sampled frame | all |


## Completeness audit 2026-10-07 (every frame, 30 / 24 fps; ORB camera measure)
Bursts (strips in `docs/audit/long-form-recut/`): v01 @ 0:00, 0:11.3, 0:44.4, 1:19.3, 1:54.45; v02 @ 0:00, 0:17.55, 0:20.7, 0:35.05, 0:54.4, 2:32.6; v03 @ 0:04.45, 1:29.7, 1:33.2, 1:49.4. Report: `docs/audit/long-form-recut/completeness.md`.
| Measure | Value | Evidence |
|---|---|---|
| Editor camera | none: max frame-to-frame background change 1.9 % scale / 1.7 % shift (gestures); crops static per shot | ORB v02 0:00–0:17.7, 1:40–1:46; stills v01 0:11.6–0:28.5 |
| Transitions | all hard cuts (0 f), incl. the cross-shoot splice and band ↔ full | v03 @ 1:29.87, 1:33.37; v01 @ 0:11.50; v02 @ 0:17.75 |
| Caption swap | hard, 0 f; chunks 0.4–0.6 s in fast speech | v01 @ 1:19.70, 1:20.20; v02 @ 0:54.80 |
| Captions vs cuts | voice-timed: outlive a cut by 3–4 f; a J-cut guest goes gold 2 f before his picture | v02 @ 0:20.83, 0:35.28; v01 @ 0:44.57 |
| Host on location | white (no `field` gold) | v01 @ 1:19.3–1:20.3 |
| Band backdrop | blurred copy, undimmed (surround luma ≥ band) | v03 @ 1:29.7 (150 / 104), 1:33.5 (69 / 50) |
| Endings | hard end with caption on (v01, v02); 5 f fade to black after the last word (v03) | v01 @ 1:55.05; v02 @ 2:33.27; v03 @ 1:49.73–1:49.94 |
| Pacing | median shot 2.5 / 2.8 / 1.9 s; p90 11.9 / 8.8 / 5.8 s; longest 17.1 / 17.8 / 79.5 s | scene detection at 0.2 |
| Master-made motion | handheld pans (v01 1:19–1:25), defocus-to-sharp graphic reveal over 8 f (v02 @ 0:20.83) | keep as the master made them |

## Engine built-ins pass 2026-10-07
- Now built-in: blur-fill backdrop brightness. `dialogue.blur_dim: 1.0` (was the compositor's hard-coded 0.45, ER-7): the backdrop is undimmed, as measured (v03 @ 1:29.7 surround 150 vs band 104).
- Now built-in: T-END-FADE is `timeline.end_fade: 5` (5 f linear to `#000000`, v03 @ 1:49.73–1:49.94); the bespoke full-frame black scene is gone (ER-8).
- Still a workaround: near-static per-shot crop uses the compositor's dead-zone follow (ER-1, explicit per-shot crop override, is not part of this engine pass).

## Template values pass 2026-10-07 (defaults, no switches)
- No overlays → an empty `plan/scenes.js`. The validator no longer needs a placeholder scene, so the stills' dummy scene is not part of the recipe.
