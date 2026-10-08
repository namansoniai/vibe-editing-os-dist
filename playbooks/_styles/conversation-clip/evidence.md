# Conversation Clip: evidence map (App. B)

**Sources:** `vibe-editing-os-research/analysis/short/alex-hormozi.md`; frame sheets `evidence/short/alex-hormozi/v01..v03/sheets/` (hook_01 at 6 fps, s_* at 1 fps, every sheet read), `meta.json`, `cuts.json`. All three are 720×1280 30 fps audience-Q&A clips (112.9 / 150.8 / 146.9 s). Positions are measured on the sheet tiles and scaled to 1080×1920 (tile 300 × 533 → ×3.6). No transcripts: speech is read from the burned-in captions. Sound is not observable.

## DNA rules → evidence
| Rule (playbook) | Value | Evidence |
|---|---|---|
| Stack opener, seam y 960, no line or gap (§3.2 SHOT-STACK, P-14) | 50/50, seam at tile y 268 → 965 | v01 hook 0:00–4.37; v02 0:00–4.0; v03 0:00–2.67 |
| Host always on top of a stack (§20.6, H7) | host top even when the asker speaks | v01 @ 0:00 (asker speaking), 0:54–1:06, 1:27–1:51; v02 @ 0:00, 0:22–0:36, 0:54–1:05 (asker speaking), 1:36–1:52; v03 @ 0:00, 1:10–1:30 |
| Pill: red per-line boxes, white caps, 2 lines (§5.2) | fill ≈ #E4001B; text ≈ 64–70 px; rect x 126–954, y 659–825 (v01) / x 144–943, y 666–882 (v03) | v01 hook "YOU NEED TO MAKE / BIGGER BETS"; v02 "“SHOULD I SELL MY / COMPANY?”"; v03 "“WHY DO MY / EMPLOYEES LEAVE?”" |
| Pill on f0, no entrance (H1) | fully drawn at 0:00.000 in all three | hook_01 sheets, first tile |
| Quotes only on the asker's question (§6.5) | v01 verdict without quotes; v02/v03 questions with curly quotes | as above |
| Pill held while the question is asked, hard out where it ends (P-03) | v01 out f115 = 3.83 s mid-stack (first cut 4.37); v02 out f142 = 4.73 s mid-shot (carried across the 4.0 cut); v03 out f346 = 11.53 s (carried across 2.7, 4.1, 5.77, 7.37, 9.93; 2 f before the 11.6 cut) | 30 fps bursts `strip-v01-pillout.jpg`, `strip-v02-pillout.jpg` |
| Captions: 1–4 words, one line, ≈ 1 chunk/s, hard swaps (CS-1, E6) | mean ≈ 2.4 words; no in-between frames at 6 fps | hook_01 sheets (v01 "I sell" → "the most effective" → "noninvasive alternative") |
| Caption size / font (CS-1) | Montserrat-like 600, ≈ 60 px ("you're playing too small" ≈ 790 px wide) | v01 @ 0:57 |
| Caption position cy 940 full, on the seam in stacks (CS-1) | full shots y 872–968 regardless of shot size; stacks y ≈ 960 | v01 @ 0:07, 0:12, 0:51; v02 @ 0:16; v03 @ 0:06, 0:21; stacks v01 @ 0:54 |
| Speaker colours: host white upright, asker yellow italic (H4) | asker ≈ #FFE600 italic | v01 @ 0:00–0:36 vs 0:54–1:05; v02, v03 throughout |
| Colour follows the voice, not the face (H4) | the asker's "thank you!" in yellow on the host's shot | v02 @ 2:30; v02 @ 2:00–2:05 host words on the asker's wide |
| Bold emphasis on numbers / key nouns, ≤ 1 per chunk (P-07) | 800 weight | v01 @ 0:07 "$44M", 0:21 "greatest", 0:57 "small"; v03 @ 0:55 "$70K", 2:14 "best talent" |
| Punch size (CS-2) | ≈ 1.4× | v02 @ 0:26–0:27 "you're gonna / work again" |
| The word (CS-3) | ≈ 2× single word | v03 @ 1:06 "role" |
| Voiced quotes, italic, curly quotes, voiced person's colour (§5.3.2) | host voicing the asker in yellow; host voicing others in white italic | v02 @ 0:33–0:35; v01 @ 1:23–1:25, 1:31; v02 @ 1:42–1:52 |
| Back-channels as the listener's own chunk (P-13) | "yeah yeah", "mmh", "okay", "nope", "uhm.." | v02 @ 0:23, 0:28–0:29, 0:39, 2:28–2:29; v03 @ 1:16 |
| Cut-off hyphen hold (P-12) | "where you're-" held 2 s | v01 @ 1:44–1:45; v02 @ 2:19 |
| Profanity vowel mask (CS-1 language) | "f*ck" | v02 @ 1:41 |
| One emoji per reel max (N1) | "perfect ✨" | v03 @ 0:02.7 (the only emoji in 410 s) |
| Action captions only with comedy light (P-11) | "*alex approves*", "*boop*" | v01 @ 0:15; v03 @ 1:31 |
| Hard cuts only (T-00, N2) | 26 / 44 / 39 cuts, all straight | cuts.json; every sheet |
| Cuts per minute 12–18, median shot 1.8–3.2 s (H6) | 13.8 / 17.5 / 15.9; 2.2 / 2.0 / 2.9 s | meta.json |
| Handover cut (R-SPK) | cut on the new speaker's first word | v02 @ 0:36–0:37, 0:38–0:39 |
| Listener cutaways 1.0–3 s (R-REACT) | 1.17–3.0 s measured | v01 @ 0:06.9–0:09.9 (3.0 s), 0:15.43–0:16.6 (1.17 s, "*alex approves*"); v02 @ 1:13–1:14, 1:20–1:21 |
| Same-speaker angle switch (R-JZ) | host front medium ↔ side/podium ↔ full-body wide; v01 0:14–0:18 is host/asker/wide alternation, not re-crops | v01 @ 0:51.3; v02 @ 0:16.2, 1:09.3 (`strip-v01-recrop.jpg`) |
| Wide establish ≤ 4 s (R-WIDE) | — | v01 @ 0:37–0:38, 1:08–1:09; v02 @ 1:27–1:29, 2:18–2:22; v03 @ 0:21–0:26 |
| Set-piece at a flip chart (P-21) | full while writing, stack while explaining | v03 @ 1:03–1:42 |
| Max full 10 s / max stack 20 s (R-HOLD) | full > 6 s: 10.5, 7.3, 10.8 (v01), 8.6 (v02), 8.2 (v03); stacks 12.1, 23.7 (v01), 14.4, 13.2, 16.5 (v02), 12.5, 9.7 (v03); no in-stack cut (per-cell scene detection) | scene detection at 30 fps, threshold 0.2 |
| Clip ends on "thank you" (R-END, CTA none) | no CTA, no end card | v01 @ 1:52; v02 @ 2:30; v03 ends mid-advice at 2:26 |
| No B-roll, stickers, logos, lower-thirds, zooms, SFX graphics (N1–N3) | 0% B-roll | all sheets |
| No grade added; source vignette kept (§4.4) | soft corner vignette baked in some angles | v01 @ 0:54–1:00 bottom cell |

## Inferred (no direct evidence)
- **F-B "Solo answer"** has no reference clip. It follows STYLE-COVERAGE row 2 ("face top, screen/graphic bottom") and the analysis §5 single-speaker fallback; the question card replacing the asker's face and the board (Permanent Marker, after v03's flip chart) are design decisions.
- **CTA devices** other than `none`, and the CTA pill reprise.
- **Duration of F-B** (45–90 s, standard class).
- **Pill and caption sub-frame motion:** no tween is visible at 6 fps, so both are treated as hard (f0 present, hard swaps).
- **`hook_sc_3s` = 3** (coverage said 4; the sheets show 3 in v01).

## (unverified) list
| Path | Value used | Why unverified |
|---|---|---|
| `sound.bed` | on, from f0, −26 dB | audio not observable |
| `formats.F-B` | whole format | no solo evidence |
| `profile.cta.devices` | none + buyer options | only `none` observed |

## Fidelity audit 2026-10 (full-resolution frames; 720×1280 sources scaled ×1.5)

| Measure | Evidence | Value → token |
|---|---|---|
| Caption size/weight | v01 @0:50 "okay so you're doing" 66 px tall asc→desc, 681 px wide; Montserrat rendered at 70 px = 66 px tall, 715–729 px wide (400–500) → ≈ 67–68 px, medium weight, −1 % tracking; v03 @0:20 "medium-skilled labor" ascender height 57 px | CS-1 68 px, weight 500, tracking −1 % (was 60 / 600) |
| Caption centre | v01 @0:01 925–980, @0:03 931–985 (seam), @0:20 934–985, @0:50 934–1000; v02 @0:10 958–1020; v03 @0:20 935–992 | `fixed_y` 960 (was 940) |
| Guest yellow | most common text colour (240, 222, 24–36) in v01 @0:01, @0:03, @0:20 and v02 @0:10 | `accent` `#F2DF1A` (was `#FFE600`) |
| Emphasis | "*the most* ***effective***", "***noninvasive*** *alternative*", "**medium-skilled** labor", "people who **don't**": 800 weight, same size, same colour | unchanged |
| Pill | red `#E80001`; v02 @0:00 y 680–886, v03 @0:00 y 661–888, v01 @0:00 y 656–914; cap height 48 px (= Montserrat 800 68 px); carried over the first cut (v02 @0:04.5 full shot) and gone by 5 s (v01) | `primary` `#E80001`; pill geometry confirmed |
| Caption swap | v01 @0:01.600–0:01.933 (6 consecutive frames) shows one chunk held with no tween; no change caught in that window | hard swap not contradicted |

## Completeness pass 2026-10 (motion at 30 fps)
Full report: `docs/audit/conversation-clip/completeness.md`.

| Measure | Evidence | Value → token |
|---|---|---|
| Pill entry | v01 f0–f3 identical, fully drawn | `type.headline.f0` verified (removed from unverified) |
| Caption swap | v01 "I sell" appears full size on f4 (0.133 s), next chunk on f29; CS-2 "you're gonna" static f785–f795 (v02) | `CS-1.swap` hard 0 f verified |
| Pill exit | v01 f115 3.83 s (mid-shot), v02 f142 4.73 s (mid-shot), v03 f346 11.53 s | `type.headline.exit` = end of the question sentence |
| Cuts | 27 / 44 / 42 at 30 fps (threshold 0.2, full frame and each half), all 0 f; cut frame = chunk swap frame (v01 4.367, 54.067) | T-00 only; §9.2 chunk-boundary rule |
| Shot lengths | median 2.3 s, p75 4.2 s, p90 6.7 s; shots > 6 s = 37% of runtime | `dialogue.cut_rules.max_hold_s` 10, `stack_max_s` 20 |
| Camera | ORB similarity first vs last frame of long shots: v01 0:17.9/0:28.2 scale 1.000 (414 inliers), 1:15.1/1:25.7 0.991; per-frame motion = live operator pans and gestures only | `zoom_policy: crop_on_cut` confirmed |
| Angles | host: front medium, side/podium, full-body wide from the crowd; asker: medium, wider with foreground, crowd wide | SHOT-ALT, P-18, R-JZ |
| End | v02 last cut 150.03 s, hard end at f4524, no fade | R-END |

## Engine built-ins pass 2026-10-07
- No change: the measured style is hard cuts only, no editor camera, no fades or blurs (completeness audit), so no new engine built-in applies. The open gaps (same-speaker angle switch in `veos angles` / the planner, host-on-top stacks) are planner work, not this engine pass.
