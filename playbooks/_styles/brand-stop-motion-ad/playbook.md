# Brand Stop-motion Ad Style Playbook (template v1)

**Purpose.** You (Claude) receive a brand's own finished stop-motion or animated **plates** (shots), their mixed audio, a wordmark file and, for the product broadcast format, pack shots and an approved claims list. Use this playbook to **select, order and cut the plates on action, time small dialogue captions, run the product spot inside the world, close on the wordmark, and keep the sound contract**, so that a 10–30 s ad plays like a handmade sketch: the characters act first, the product turns the story, and the brand signs it at the end.

**Input (SW-01 `animated_plates`).** Plates are the picture. The engine never makes the characters, sets, lighting or depth of field; it makes the edit, the type, the in-world product spot, the iris, the end card and the timing. **Who can use it:** brands and agencies that already own stop-motion, claymation, felt, puppet, paper-cut or 3D-animated shots (or are commissioning them). A creator with only a phone camera cannot use this template.

**Inspired by:** Chamberlain Coffee stop-motion ads (claymation and needle-felt). See App. B.

### Style DNA `[DNA]`
A miniature handmade world, lit warm, shot on a macro lens, plays out with **no title and no banner**: a character is already doing something on frame 0. Shots are calm (1.4–7.8 s, median ≈ 4 s) and joined by hard cuts on the action. The world moves on its own frame cadence (characters on twos, pose-to-pose bursts with held poses, camera moves on ones), and anything the engine animates inside the world steps on that cadence too. When characters talk, **small pale-yellow two-line captions** sit low in the frame and cut on with the first word; when they don't, there is no text at all. The product appears **inside the world**, held by a character, waiting at the end of a journey, or playing on an in-world TV between bursts of static, with one or two red condensed label words. A last character beat (the **button**) lands after the product, then a soft **iris** closes on the characters (or a hard cut to black) and the brand's **wordmark sits alone on black** for about two seconds. Comedy comes from the characters' acting and the timing, never from stickers or meme sounds.

**Copy these 5 things:**
1. **Plate-first open, zero added text before the first spoken word** (HA-16 diegetic hook) → §6.2, H1.
2. **Small pale-yellow two-line captions, 64 px, block centre y 1420, hard on/off (0 f), only for speech** (CS-1) → §5.3.
3. **Calm hard cuts on action, plates on their own cadence** (shots 1.4–7.8 s; characters on twos; never retimed) → §9, §10.2.
4. **The product lives inside the world** (prop, journey's end, or the in-world screen spot) → §8.3 P-PRODUCT-IN-HAND, P-REVEAL-WIDE, P-SCREEN-*.
5. **Button beat, then iris or cut to black, then the wordmark alone on black 1.8–2.4 s** → §7.1, §25.

### Directives (the style's laws) `[DNA]`
| # | Directive | Where |
|---|---|---|
| D1 | **Characters act before anything is written.** No headline, banner, title card or label in the hook; the first text on screen is the first spoken line's caption | §6.2, H1 |
| D2 | **The plates are the look.** Never retime, interpolate, regrade, punch in, stabilise or speed-ramp a plate. The only engine change to a plate is a trim, a ≤ 12 f end-frame hold, or a declared fallback crop | §10.2, H11 |
| D3 | **Captions are small and quiet:** pale yellow `#F6FA8C`, 64 px, ≤ 2 lines × ≤ 24 characters, block centre y 1420, one character line per caption, cut on and off with no fade, no coloured or bold emphasis | §5.3, H5 |
| D4 | **The product lives inside the world.** It is a prop, the place the journey ends, or a broadcast on an in-world screen. Never a full-frame pack shot pasted over the plates | §8.3, H12 |
| D5 | **Calm rhythm, hard cuts on action.** Shots 1.4–7.8 s; no dissolves, whips, zoom transitions, light leaks or glitches. The in-screen static, the sensory-trip glow and the closing iris are the only designed transitions | §9, H4 |
| D6 | **Every sketch has a button:** a last character beat (reaction, non-sequitur, a satisfied sip, the masked punch line) between the product turn and the wordmark | §7.1, H10 |
| D7 | **The wordmark closes alone on black** (y 960, 600–700 px wide, 1.8–2.4 s), then a hard end. Nothing else on the card except an optional link line | §25, H10 |
| D8 | **Every word on screen is approved:** captions verbatim from the brand's script, label words only from the approved claims list, profanity masked inner-style (`F**k`) | §5.5, §8.5, H6, H9 |

Buyer directives `BD1…` `[VAR]` go here; they may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile | ON |
| §1 | Procedure | ON |
| §2 | Hard rules, exceptions | ON |
| §3 | Worlds, layouts, safe zones | ON (§3.6 OFF: no presenter) |
| §4 | Colour | ON (§4.3 OFF: single theme; §4.4 OFF: plates are never regraded) |
| §5 | Type & captions | ON |
| §6 | Hook system | ON |
| §7 | Structure & cadence | ON |
| §8 | Visual system & patterns (34) | ON |
| §9 | Transitions & shot grammar | ON (§9.3 ON: footage spine) |
| §10 | Motion, camera, layers, finishing | ON |
| §11 | Sound contract | ON |
| §12 | Plates, shot list, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (F-A, F-B, F-C) | ON |
| §15 | QA | ON |
| §16 Chrome · §18 Data · §19 Citations · §20 Dialogue · §21 Canvas camera · §22 Ink · §23 Continuity · §24 Series | modules | OFF |
| §17 | Anchors (screen rect, iris centre, face band) | ON in F-B; anchor pass used in every format |
| §25 | Sponsor, brand & end cards | ON |
| Formats | F-A Dialogue sketch (default) · F-B Product broadcast · F-C Vignette | |

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile
  source_type: animated_plates
  presenter: {presence: none, share: [0, 0], max_absence_s: 999}
  spine: footage
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: minimal              # F-B overrides to support
  duration: {class: micro, target_s: [12, 30]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: none, units: metric, decimals: 0}
  tone: {energy: calm, comedy: light, comedy_max: light}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A, F-B, F-C], default: F-A}
  footage_dependency: total
  cta: {devices: [end_card, link_bio, post_only, none], placement: end, chosen: end_card}
  modules: {chrome: false, running_state: false, anchors: false, data_figures: false, citations: false,
            dialogue: false, canvas_camera: false, ink: false, continuity: false, series: false, brand: true}
```

Why each switch has its value:
- **source_type: animated_plates**, because every evidence clip is a pre-produced stop-motion ad (claymation v01/v02, needle-felt v03); the editor assembles plates, it films nothing.
- **presenter: none**: no human presenter appears in any frame; the "faces" are puppets. V-PRESENCE and V-FACE are off; the character-face rule is H7 (review).
- **spine: footage**: picture moments are the timeline; dialogue follows the picture (v03's lines sit on the shots made for them).
- **captions: full / support / mute_safe**: v03 captions every spoken line (≈80% of runtime); v01/v02 have no speech, so they have no captions. Captions never carry the ad; the plates do. Mode is TUNE `full ↔ off` (a brand may run silent cuts).
- **graphics: minimal**: added graphics are the captions, the end card and the iris (v01 0%, v03 ≈ 8% beyond captions). F-B is `support` because the engine builds the screen spot (v02 @0:05–0:17, ≈ 40% of runtime).
- **duration: micro 12–30 s**: evidence 12.0 / 28.3 / 32.2 s; v03's 32.2 s includes a 2.3 s black hold that this template trims to ≤ 2.4 s total card time, landing it ≤ 30 s. Adjacent class `short` (≤ 45 s) is a TUNE step.
- **language: en**: the evidence captions and labels are English. Speech in the plates is the brand's; the buyer picks the caption language at setup (BV-05).
- **numbers**: ads in this style show no figures; prices or numbers only appear if they are in the claims list (H9).
- **tone: calm / light**: character comedy, no meme sounds, no stickers (§8.6).
- **themes: single**: the plates set the colour; the engine's two colours (label red, screen sky) are the brand's.
- **formats F-A / F-B / F-C**: v03 dialogue sketch, v02 silent product broadcast, v01 vignette. They share all five "Copy these" traits except that F-C has no captions by nature.
- **footage_dependency: total**: the style *is* the plates (FB-1 has no fallback).
- **cta: end_card** (wordmark), the only device in the evidence (v02 @0:15, v03 @0:30). `link_bio` adds one link line under the wordmark.
- **modules: brand** (end card + paid-partnership disclosure). **anchors** is switched on by F-B for the screen rect; every format still runs the anchor pass for the iris centre and the caption band (§17).

### 0.4 Formats `[DNA set; VAR enable]`

| Field | F-A Dialogue sketch (default) | F-B Product broadcast | F-C Vignette |
|---|---|---|---|
| `when` | Plates with character dialogue: a two-character mini story that turns on the product | Silent or music-only plates with a locked-off in-world screen (TV, phone, billboard, shop window) | One short character moment, no dialogue |
| Evidence | v03 | v02 | v01 |
| Profile overrides | duration 20–30 s | graphics `support`; duration 18–30 s; `modules.anchors: true` | duration 10–16 s |
| Layouts | L-plate, L-endcard (+ fallbacks L-plate-band, L-plate-blur) | same | same |
| Default hook | HA-16 | HA-16 | HA-16 |
| Structure | sketch: setup → gag/journey → product turn → button → logo | sketch: setup → product broadcast → reactions → wide hold → logo | sketch: action → wide → button → logo |
| Cadence `sc_per_10s` | 2.5–6.0 (captions count 0.5) | 2.0–6.0 (screen swaps count) | 1.5–4.0 |
| End | T-IRIS → wordmark card | T-CUT-BLACK → wordmark card | T-CUT-BLACK → wordmark card |
| Captions | CS-1 (CS-2 on bright plates, CS-3 for low faces) | only if a plate has speech | none (no speech) |

**Shared DNA (one line):** plates open mid-action with no added text, small pale-yellow two-line captions only when someone speaks, hard cuts on action, the product inside the world, a button beat, the wordmark alone on black last.

**Format pick rule (decided):** dialogue in the plate mix → F-A. No dialogue and a locked-off in-world screen plate of ≥ 6 s exists (SH-8) → F-B. No dialogue, no screen, total plate time < 18 s → F-C. No dialogue, no screen, ≥ 18 s → F-A structure without captions (the sketch reads as pantomime; FB-3).

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

The craft step of this style is **P4b, the plate cut pass**: choosing in and out points on the action inside each plate, so that every cut lands on a completed or matched motion and the sketch keeps a calm, patient rhythm.

1. **P1 Inventory.** `ffprobe` every plate: resolution, aspect, fps, duration, audio channels. Conform to 30 fps CFR with frame duplication only (`veos conform` uses `fps=30`, which repeats frames: a 24 fps plate gets a 2-2-2-3 cadence, and a 12 fps "on twos" plate keeps its stutter). **Never** use optical-flow or blended frame-rate conversion. Register every plate, the wordmark and the pack shots in `plan/assets.json` with `origin: creator` (they are the brand's own files).
   - **P1b Plate log.** One row per plate: `id`, setting, characters, action (one sentence), shot size (`W` wide · `M` medium · `CU` close-up · `INS` insert), camera (locked · push · pan · rack), the frame where the action starts and ends, usable in/out, an in-world screen present (y/n, locked-off y/n), the plate's dominant luminance under y 1340–1500 (dark · mid · bright), and where the characters' eyes sit (y range). Read 1 frame per second plus the first and last frame of each plate.
2. **P2 Prepare:** skipped. No matte (the engine never draws behind a puppet). Pick the format by the §0.4 rule.
3. **P3 Transcribe** only when the plate mix has speech (F-A; or F-B/F-C plates with a line). Word timestamps from the plate audio. Caption text comes from the brand's dialogue script (SH-4) aligned to the words (`captions.transform: verbatim`, the script's casing kept: "you've **GOT** to try this"). Apply the profanity mask `inner` ("F**k that's good") and the glossary (brand and product names). Without a script, FB-4 applies.
4. **P4 Segment** into the sketch beats (§7.1): `setup`, `gag` (or `journey` / `broadcast`), `product`, `button`, `logo`. Assign every plate to a beat.
   - **P4b Plate cut pass (the craft step).** For every plate pick the in point on the first frame of a motion (or 2–4 f into it) and the out point on the frame a motion completes, or on the matching moment of the next plate's action (R-1). Hold rules §9.3. Write each cut's reason (`action_end`, `match`, `line_end`, `reaction`).
5. **P5 Classify** every plate and every spoken line with a line type (§8.4) and its trigger (the word or the action frame the visual change lands on).
6. **P6 Tone-tag** every beat: `setup` · `gag` · `awe` (the product turn) · `button` · `cta` (the wordmark).
7. **P7 Hook plan.** Pick the archetype (§6.2 HA-16 default; alternates §6.3). Write **3 hook variants**, each a different opener plate and first cut, and run the stopper tests ST-1, ST-3, ST-6 (§6.1).
8. **P8 Visual plan (overlays only).**
   - Captions: CS-1 by default; CS-2 for every shot whose caption band is bright (P1b luminance `bright`); CS-3 for every shot where a character's eyes or mouth fall in y 1330–1520 (§5.3).
   - F-B: the screen spot plan (§7.3 ritual) and its labels from the claims list.
   - The end: T-IRIS (F-A) or T-CUT-BLACK (F-B, F-C), the end card, the link line if `link_bio`.
   - The disclosure line when the post is paid (§25).
   - **P8b Anchor pass** (§17): the screen rect of every F-B screen plate, the iris centre on the button plate, and each shot's face band for CS-3.
   - **P8c Claims pass:** every label word, every number and every product name on screen is matched to the claims list or the script (H9). Unmatched words are dropped and listed at the checkpoint.
9. **P9 Beat sheet** (§13): one beat per plate (and per line inside a long plate), meeting §7.6 cadence and §9.3 shot grammar.
10. **P10 SFX ledger** (§11, from the bundled pack only on the allowed moments) and the transition map (§9).
11. **P11 Assets:** wordmark (SH-5), pack shots (SH-6), screen show content (§12.5); resolve fallbacks (§12.3) and record which were used.
12. **P12 Checkpoint** (§13.5), then **wait for approval.**
13. **P13 Build:** cut list → `plan/timeline.json` + `plan/scenes.js` (screen spot, iris, end card, legal lines) → `veos validate` → preview and QA (§15, at most 3 passes) → render.

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| E-id | Use in this style | Limits (≤ registry) | DNA reason | Evidence |
|---|---|---|---|---|
| **E6** Hard swap | Content changes inside the in-world screen rect (label → pack → label → lineup → static) are hard cuts, like a channel change | The screen rect stays constant ±4 px for the whole spot (it is the plate's TV, locked off); only the content inside changes; the static comes on and goes off hard (v02 @5.43, @16.97); never used for an element appearing outside the screen | The TV broadcast reads as television because its content cuts, not slides | v02 @0:07–0:17 |

No other exception is declared. Captions are 64 px (≥ the 54 px subtitle floor), labels ≥ 52 px, legal lines 24 px TC-legal: E3 is not needed.

### 2.3 Style MUST rules
- **H1 Frame 0 (HA-16):** frame 0 is a plate already in motion (a character mid-gesture, something entering the frame, a screen already playing). No headline, banner, title, label or logo on f0. A caption may be on f0 only when the first spoken word starts at 0.00–0.10 s (HA-14 alternate). The disclosure line (TC-legal) is allowed. `check: V-F0`
- **H2 Subject by 5.0 s:** by 5.0 s the viewer knows who the sketch is about and where they are (the subject full in frame ≥ 20% of frame height for ≥ 1 s). F-B: the in-world screen is on screen by 3.0 s and the product is on it by 8.0 s. F-C: the product is in a character's hand or in the frame by 5.0 s. `check: V-F0` (payoff) + review
- **H3 Cadence:** weighted state changes per 10 s within the format's band (F-A 2.5–6.0, F-B 2.0–6.0, F-C 1.5–4.0); the first cut at 1.2–3.0 s (`hook_sc_3s` ≥ 1); no gap > 8.0 s between weight-1 changes; nothing static > 3.0 s in F-A/F-C or > 4.5 s in F-B (a plate's own held pose of up to 1.6 s is a beat, never trimmed below 12 f; v01 @7.5–9.08, v02 @20.0–22.0). `check: V-CADENCE`
- **H4 Shot lengths and cut points:** every plate shot 1.4–7.8 s (F-A median ≈ 4 s); a character's close-up holds its whole line plus 8–15 f; cuts land on a completed motion or a matched motion ±2 f; at most two long shots of 4.0–7.8 s per reel, each carrying a camera move or travel (P-PATIENT-HOLD); a locked-off screen shot in F-B may run up to 14 s while its screen content changes at least every 2.0 s. `check: review`
- **H5 Captions (CS-1):** one character line per caption (1–8 words), ≤ 2 lines, ≤ 24 characters per line, Plus Jakarta Sans 500 64 px pale yellow `#F6FA8C`, block centre y 1420 (CS-3: 1180), hard on 2 f before the first word, hard off (0 f fades; v03 @1.17, @28.98, @30.23), held ≥ 0.3 s per word, the script's casing kept, no colour, weight or size emphasis. `check: V-CAPTION`
- **H6 Profanity:** every listed profanity is masked `inner` (first and last letter kept: "F**k", "S**t"); the plate audio is left as the brand mixed it. `check: V-CAPTION`
- **H7 Character faces stay clear:** no caption, label or legal line covers a character's eyes or mouth. When a shot's face band (anchor pass) reaches y 1330–1520, that shot's captions use CS-3 (y 1180); if the face also covers y 1100–1260, the line is moved to the previous or next shot (never placed on the face). `check: review`
- **H8 Contrast:** every caption measures ≥ 4.5:1 against the plate under it; shots logged `bright` use CS-2 (2 px warm-dark stroke + deeper shadow). Label words on the screen sky measure ≥ 4.5:1 (`#9C0012` on `#C9D9EE` ≈ 6:1). `check: V-TYPE`
- **H9 Product truth:** every label word and every product claim on screen is in the approved claims list (SH-7) or the script; pack shots are the brand's own files, shown unaltered; no invented claims, prices, ratings, awards, "new", "best" or "#1". Numbers appear only when the claims list states them. `check: review` (NC-6)
- **H10 The end:** every reel ends: button beat → T-IRIS (F-A) or T-CUT-BLACK (F-B, F-C) → wordmark card on `ink` black, wordmark centred at y 960, 600–700 px wide, in over 5 f (F-A: under the iris snap, no black gap), held 1.8–2.4 s (F-C 1.6–2.0 s), hard end. Card total ≤ 2.5 s. `check: V-PROMISE` (`brand.endcard.max_s`) + V-LAYOUT
- **H11 Plates untouched:** no engine zoom, punch, shake, speed change, reverse, frame blending, regrade, blur or stabilisation on any plate (the measured sensory-trip transitions T-GLOW-IN / T-BLOOM-OUT excepted, once per reel); trims only, plus ≤ 12 f end-frame holds (P-FRAME-HOLD) and the declared fallback crop/band (FB-2). The plate's frame cadence (ones, twos, held poses) is kept exactly: 24 → 30 fps by frame duplication only. `check: V-CAMERA` (`zoom_policy: source_only`) + review
- **H12 Graphics stay out of the story:** during `setup`, `gag` and `button` beats the only engine elements on screen are captions (and the disclosure line in the first 2.5 s). Overlay graphics beyond captions ≤ 15% of runtime in F-A and F-C, ≤ 50% in F-B (the screen spot). `check: review`
- **H13 Disclosure:** when the post is paid (an agency or creator posting for the brand), the `TC-legal` line "Paid partnership" (BV-14 wording) shows at x 64, y 150 from 0.0 s for ≥ 2.0 s, plus the platform's own label. `check: review` (NC-12)
- **H14 Third-party material:** real shows, matches, logos of other companies, celebrities or retailers that would appear on an in-world screen, sign or line are creator-supplied, or Claude creates its own visual (§12.5). Nothing is fetched. `check: V-INSERTS`
- **H15 Spelling:** brand, product and character names are spelled exactly as in the glossary and the script. `check: V-CAPTION`
- **H16 Audio:** the plate mix is kept as the brand delivered it; SFX-pack cues only on the §11 moments; −14 LUFS integrated, true peak ≤ −1.5 dBTP; the last sound ends ≤ 6 f after the wordmark hold ends. `check: review` (NC-8)
- **H17 Determinism:** static noise, cloud drift and every animated element are functions of the frame index (seeded). `check: review` (NC-9)
- **H18 Safe zones:** captions, labels, links and legal lines sit inside x 64–1016, y 110–1500; nothing that carries meaning in y > 1500 or the right 110 px between y 900 and 1540. `check: V-SAFE`

Subjects covered with this style's value:

| Subject | Value | Rule |
|---|---|---|
| Frame-0 stopper | a plate in motion, no added text | H1 |
| Cadence | F-A 2.5–6 · F-B 2–6 · F-C 1.5–4 SC/10 s; first cut ≤ 3.0 s; max gap 8.0 s (F-A) / 6.5 s; static ≤ 3.0 s (F-B 4.5 s) | H3 |
| Payoff by | subject by 5.0 s; product by the turn (F-A 55–75% of runtime, F-B ≤ 8.0 s, F-C ≤ 5.0 s) | H2 |
| Headline limits | n/a: no headline exists in this style | type.headline `none` |
| Dead air (spine footage) | picture-led gaps are allowed while the plate's action continues; a silent, motionless stretch > 3.0 s is trimmed | H3 |
| On-the-word visuals | screen label words land 2 f before their spoken word when the word is spoken, else on the hard swap ±2 f | V-ONWORD |
| Face rule | character eyes and mouth never covered | H7 |
| Presenter presence | n/a (presence `none`) | — |
| Promise integrity | the product promised in the setup is the product shown; the wordmark ends every reel | H2, H10 |
| Truth | claims list only; pack shots unaltered | H9 |
| Spelling and glossary | exact | H15 |
| Audio targets | NC-8 | H16 |
| Determinism | NC-9 | H17 |

### 2.4 NEVER list
- **N1** A title, banner, "NEW!", product name card or logo bug in the hook or over the story beats.
- **N2** A full-frame pack shot, product turntable or price card pasted over or between plates (the product stays in the world; FB-8 is the only exception path).
- **N3** Engine zooms, punch-ins, shakes, speed ramps, reverse, freeze-frames longer than 12 f, motion blur, frame blending or optical-flow retiming on plates.
- **N4** Dissolves, cross-fades between plates, whip pans, zoom transitions, light leaks, film burns, flash frames, glitches or RGB splits.
- **N5** Coloured, bold, stroked (except CS-2), boxed or karaoke caption words; ALL-CAPS captions unless the script writes the word in caps.
- **N6** Meme sounds, cartoon boings, record scratches, laugh tracks or any SFX-pack cue over a character's line.
- **N7** Stickers, emoji, arrows, circles, marker notes or reaction GIF-style overlays.
- **N8** White captions on a bright plate without CS-2 (the honey-yellow and sky-white failure, v03 @0:06).
- **N9** Label words that are not in the claims list, or more than 2 words per label, or more than 3 labels per spot.
- **N10** A wordmark on anything but black, a wordmark smaller than 600 px wide, a tagline or URL card longer than the wordmark's own hold, or a black tail after the card > 0.2 s.
- **N11** Grain, vignette, bloom, LUTs or "film look" added on top of the plates.
- **N12** A fetched logo, show, match or celebrity image on an in-world screen; a look-alike of a real broadcaster's graphics.

Buyer additions `BN1…` `[VAR]` go here.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-plate** | `footage` | The brand's plates, full frame, untouched (warm tungsten key, shallow depth of field, miniature sets: evidence peach `#F7D7B5`, warm skin `#E8A46A`, teal fills `#2FA39A`, honey `#F6D21B`) | Every story beat; the in-world screen spot is drawn into a plate | Hard cuts between plates |
| **W-black** | `void` | `#000000` (`ink`), no texture, no noise | The iris surround, the cut to black, the wordmark card | T-IRIS closes into it; T-CUT-BLACK cuts into it; the reel ends on it |

The in-world screen's content (sky, labels, packs, static) is **not a world**: it is a scene clipped to the screen rect inside W-plate (P-SCREEN-*).

### 3.2 Layout library
| ID | Name | Engine | Rects | Caption | Share (per format) |
|---|---|---|---|---|---|
| **L-plate** | Full plate | `full` | the plate fills 1080×1920 | CS-1 block centre y 1420 (CS-3 y 1180) | F-A 85–94%, F-B 85–94%, F-C 80–88% |
| **L-endcard** | Wordmark on black | `hidden` (stage hidden, W-black shows) | graphic x 64–1016, y 640–1280 | none (captions hidden) | 5–20% (1.6–2.4 s) |
| **L-plate-band** | 16:9 plate band (fallback FB-2) | `letterbox` | band_h 608, centre y 860 → band y 556–1164, fill `#000000` | CS-1 at y 1290 (under the band) | only when the plate is 16:9 |
| **L-plate-blur** | 4:5 or 1:1 plate band (fallback FB-2) | `blurfill` | band_h 1350, centre y 900 → band y 225–1575, blur 48 px, luma −0.35, scale 1.15 | CS-1 at y 1420 (inside the band) | only when the plate is 4:5 or 1:1 |

**Layout rule:** one layout per plate, decided by the plate's aspect in P1; a reel mixes L-plate and a fallback layout only when the brand's plates are mixed (each fallback shot is listed at the checkpoint).

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-CUT** | Plate to plate | `via: cut`, 0 f | Every shot change |
| **G-IRIS-END** | Plate to end card | The P-IRIS-OUT scene closes to r 0 on the plate (§9.1 T-IRIS); on the frame it reaches 0 the stage switches to `L-endcard` (`via: cut`) and the world is W-black | F-A ending |
| **G-BLACK-END** | Plate to end card | `via: cut` straight to `L-endcard` on the frame after the button plate's out point | F-B, F-C ending |
| **G-BAND** | Plate to a fallback band | `via: cut` (never a morph: the band appears with its plate) | FB-2 plates only |

### 3.4 Layout diagrams
```
L-plate (F-A dialogue shot)                 L-endcard
┌─────────────────────────┐ 0               ┌─────────────────────────┐ 0
│ (IG top UI, keep clear) │ ← y 0–110        │                         │
│ Paid partnership        │ ← legal y 150    │                         │
│                         │   (paid only,    │                         │
│     [character eyes     │    0–2.5 s)      │                         │
│      y 480–1300]        │                  │   ╭╮ wordmark (image)   │ ← centre y 960
│                         │                  │  ╰──╯ 600–700 px wide   │   ≈ 250 px tall
│   CS-3 line y 1180 ─ ─  │ ← only when a    │                         │
│                         │   face is low    │  link in bio            │ ← link line y 1180
│   Dude, you've GOT      │ ← CS-1 block     │                         │   (link_bio only)
│   to try this           │   centre y 1420  │                         │
│ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │ ← y 1500 safe    │                         │
│ (IG caption / UI band)  │   floor          │ (black to the edges)    │
└─────────────────────────┘ 1920            └─────────────────────────┘ 1920

L-plate (F-B screen shot, v02 geometry)      L-plate-band (16:9 fallback)
┌─────────────────────────┐ 0               ┌─────────────────────────┐ 0
│   framed pictures       │                 │        black            │
│ ┌─────────────────────┐ │ ← screen rect   │┌───────────────────────┐│ ← y 556
│ │     ORGANIC         │ │   ≈ x 198–864,  ││   16:9 plate band     ││
│ │  (label cy = top    │ │     y 709–1141  ││                       ││
│ │   + 0.21·h)         │ │                 │└───────────────────────┘│ ← y 1164
│ │   [pack 0.62·h]     │ │                 │   caption y 1290        │
│ └─────────────────────┘ │                 │        black            │
│   TV cabinet, books     │                 │                         │
└─────────────────────────┘ 1920            └─────────────────────────┘ 1920
```

### 3.5 Safe zones and bands
- **Meaning text box:** x 64–1016, y 110–1500 (TUNE ±5% inside NC-5).
- **Caption band:** y 1348–1496 for a two-line CS-1 block (centre 1420, 64 px × 1.25 line height; the source pitch is 79 px); single lines sit on y 1420. CS-3 band y 1108–1252.
- **Legal band:** y 136–164 (24 px line at y 150), left-aligned at x 64.
- **Screen band (F-B):** wherever the plate's screen is; label words stay ≥ 24 px inside the screen rect and inside the meaning box.
- **End card band:** wordmark y 835–1085 (centre 960), link line y 1160–1200.

### 3.6 Presenter rules
OFF (`presenter.presence: none`). Character faces are protected by H7 and the anchor pass (§17).

---

## §4 Colour `[REQ] [roles' meanings DNA; brandable hex VAR]`

### 4.1 Role palette
| Role | Hex | Its one job | `text_on` | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` | `{{BV-02.primary|#9C0012}}` (label colour; default red, audit sampled `#980014`-`#9F000D` on the TV sky) | Label words on the in-world screen; the link line's accent dot | `paper` | 7.9:1 (white on it); 5.6:1 as text on `accent` | yes (BV-02 colour 1) |
| `accent` | `{{BV-02.accent|#C9D9EE}}` (screen sky; default pale blue) | The ground of engine-built screen content: a pale sky with soft clouds | `primary` | 5.6:1 | yes (BV-02 colour 2) |
| `paper` | `#FFFFFF` | Captions, the type-set wordmark fallback, the link line, legal lines | `ink` | 21:1 on black | no (fixed) |
| `ink` | `#000000` | The end card, the iris surround, the cut to black | `paper` | 21:1 | no (fixed) |
| `shade` | `#2A1E14` | CS-2 caption stroke and shadow tint on bright plates | — | — | no (TUNE: warm near-black) |
| `static` | `#8E8E8E` | Mid grey of the in-world screen static | — | — | no (TUNE: neutral grey) |

### 4.2 Meanings
- **The plates own colour.** Every hue in the story is the brand's set design; the engine adds no colour to a plate.
- **White = words someone says** (captions) and the brand's signature (wordmark).
- **Red label words = what the brand claims**, shown only inside a screen in the world.
- **Black = the story is over;** only the wordmark lives there.
- Brand colours appear only on brand elements: label words, screen sky, wordmark (in its own file colours).

### 4.3 Theme packs
OFF (`themes.policy: single`).

### 4.4 Grades
OFF. Plates are never regraded (H11, N11). If plates from two shoots differ in white balance, the brand fixes it in their grade; the engine reports it at the checkpoint.

### 4.5 Rules
- `max_bright_per_frame` = 2 for engine elements (label red + screen sky); plate colours do not count.
- Label words sit only on the `accent` sky inside the screen, never directly on a plate.
- The BV-02 colours are contrast-nudged at setup: `primary` keeps ≥ 4.5:1 with white, `accent` keeps ≥ 4.5:1 with `primary`.
- Captions are always `paper`; never brand-coloured.

**Must match `tokens.json`.**

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within the class]`
| Slot | Family | Weight | Class (TUNE boundary) | Uses |
|---|---|---|---|---|
| `caption` | **Plus Jakarta Sans** | 500 (CS-2 600) | friendly geometric-humanist sans 400–600 (Plus Jakarta Sans, Inter Tight, Poppins, Jost) | Captions, link line, legal lines |
| `label` | **Barlow Condensed** | 700 | condensed grotesque caps 600–700 (Barlow Condensed, Anton) | Screen label words |
| `wordmark` | **Fraunces Soft** (Fraunces with SOFT 100 / opsz 9 baked in, so canvas text gets the soft shapes too) | 800 | soft chunky serif 700–900 (Fraunces Soft, Fraunces, EB Garamond, Instrument Serif, Lilita One, Source Serif 4) | The type-set wordmark fallback only (FB-5) |

The brand's wordmark and pack shots are **image assets**, never fonts. Devanagari captions fall back to Noto Sans Devanagari 500 (no italic exists; none is used).

### 5.2 Headline element
OFF (`type.headline.kind: none`). This style has no headline, banner, pill or title card. The wordmark card (§25) is the only "title", and it comes last.

### 5.3 Caption system profiles

**CS-1 "Soft dialogue"** (default; `extends: lib:chamberlain`):

| Group | Value |
|---|---|
| Mode | `full` / `support` / `mute_safe`; only spoken lines get captions |
| Chunking | `unit: sentence`: one character line per chunk (split at the line's own sentence end); words 1–8; ≤ 24 characters per line; ≤ 2 lines; break at the most natural phrase boundary closest to the middle (evidence: "Dude, you've GOT / to try this", "Told ya! I can show you / where it came from"); never split a name, number or unit; a new chunk on every new speaker and every sentence end; a line longer than 8 words or 48 characters splits into two chunks at its comma |
| Timing | lead 2 f before the first word; **hard on, hard off (0 f)**: the evidence caption is full on its first frame (v03 @1.167) and vanishes on one frame (@30.23); a line spoken across a cut stays on through it (@1.42); min hold 0.3 s per word; tail 0.25 s after the last word; hold through pauses up to 0.6 s, then fade out; a pause ≥ 0.9 s always ends the chunk |
| Skin | Plus Jakarta Sans 500, **64 px**, `TC-subtitle`, case `as_spoken` (the script's casing: "GOT" stays caps), tracking 0, **pale yellow `#F6FA8C`** (audit, v03 @0:01.5 and @0:08: glyph cores `#F5FF7C`-`#F7FF7C`, reading `#F1FFD1` over yellow felt @0:20; not white), no stroke, shadow `0 2 10 rgba(0,0,0,.55)`, line height 1.25 (line pitch 79 px; cap height 44 px, so ≈ 63 px Plus Jakarta Sans), no container |
| Position | `fixed_y`, block centre **y 1420**, centred at x 540, max width 860; the same y in every plate shot (evidence first line ≈ 1444, lifted to keep a two-line block above y 1500) |
| Speakers | none: every character's line is the same white (v03 frog and bee share one style) |
| Emphasis | `none`. Emphasis exists only where the brand's script writes caps |
| Karaoke / two-tier / duet / kinetic stack | none |
| Hide rules | hidden on the wordmark card (`captions.hide` over L-endcard); shown over the iris (white on its black surround, v03 @0:29) |
| Language | script Latn; English terms kept verbatim; spelling not normalised (the script wins); profanity mask `inner`; glossary = brand, product and character names |

**CS-2 "Bright plate"** (same as CS-1 except): weight 600, stroke 2 px `shade` `#2A1E14`, shadow `0 2 14 rgba(42,30,20,.75)`. **Use rule:** every shot logged `bright` in P1b (sky, white walls, honey, snow, light fabric in y 1340–1500). It keeps the look of soft white text while measuring ≥ 4.5:1.

**CS-3 "High band"** (same skin as CS-1): block centre **y 1180**. **Use rule:** every shot whose face band (anchor pass) reaches into y 1330–1520. A bright high band uses CS-2's skin via a CS-2 override on that span plus a `CS-3` position: in that case write the line on CS-3 and log it; never stack two profiles on one span.

Profiles switch per span with `captions.overrides: [{t: [a, b], profile: "CS-2"}]`; never write caption cards by hand.

### 5.4 Other text systems
| Element | Class | Recipe | Hold |
|---|---|---|---|
| **Screen label** (P-SCREEN-LABEL) | TC-label | Barlow Condensed 700, caps, `primary` on the `accent` sky, size = 12% of the screen rect height clamped to 48–64 px (audit, v02 sheet @0:12: "EFFORTLESSLY DRINKABLE" 504 px wide on a 660 × 446 px screen → 54 px Barlow Condensed 700), centred on the screen, centre y = screen top + 0.21 × screen height; ≤ 2 words (a 2-word label may run up to 22 characters: "EFFORTLESSLY DRINKABLE"), max width = screen width − 80 px; **blinks** on 6–7 f / off 6 f (≈ 2.4 Hz) while its pack builds (v02 @8.34–14.31) | 1.4–2.0 s per word (≈ 4–5 blinks) |
| **Wordmark image** (P-WORDMARK-CARD) | image | The brand's file, white, centred (540, 960), width 648 px (600–700), fades in over 5 f with no scale (F-A: under the iris snap, v03 @30.20–30.37) | 1.8–2.4 s |
| **Type-set wordmark** (FB-5) | TC-display | Fraunces 800, `paper`; the brand name's first word on a 48° arc (radius 520 px), any second word straight below at 70% size, the whole rotated −6°, total width 600–700 px, centre y 960 | as the image |
| **Screen wordmark arc** (P-SCREEN-LINEUP) | image (or TC-display type-set) | The wordmark at 85% of the screen width, centre y = screen top + 0.45 × height, grows 0.65 → 1.0 in held steps of 2 f over ≈ 18 f with a tilt that settles −6° → 0° (stop-motion steps, not a smooth tween; v02 @15.30–15.87), over the pack lineup | 1.0–1.6 s after it lands |
| **Link line** (P-LINK-LINE) | TC-label | Plus Jakarta Sans 500, 40 px, `paper`, sentence case, centre y 1180 on the end card, text = "{{BV-08.keyword|link in bio}}", in 8 f after the wordmark settles | to the end |
| **Disclosure** (P-DISCLOSURE) | TC-legal | Plus Jakarta Sans 500, 24 px, `paper`, shadow `0 1 4 rgba(0,0,0,.6)`, x 64, y 150, "Paid partnership" (BV-14) | 0.0 → ≥ 2.0 s (default 2.5 s), fade out 6 f |
| **Stockist line** (P-STOCKIST-LINE) | TC-label | Plus Jakarta Sans 500, 40 px, `paper`, "Now at <retailer>" set in type (never a fetched logo), end card y 1180 (replaces the link line) | to the end |

### 5.5 Language and number rules
- Captions are the brand's script, verbatim, aligned to the plate audio. Brand, product and character names exactly as in the glossary.
- Script casing is kept (`as_spoken`); the engine never adds caps, bold or colour.
- Profanity: `inner` mask on screen ("F**k", "S**t", "B***h"); the audio is the brand's call.
- Hinglish captions (`hinglish/hinglish/Latn`): romanised as the script writes it; English product terms verbatim. Hindi (`hi/hi/Deva`): Noto Sans Devanagari 500, 64 px, same position; the mask uses `mask_words` for Hindi profanities listed by the brand.
- Numbers appear only from the claims list and are written as the brand writes them; international grouping by default (BV-06).
- Label words are always in the on-screen language (`on_screen: en` by default); a Hindi-language reel keeps English label words only if the claims list is English.

---

## §6 Hook system `[REQ]`

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| Test | This style's number |
|---|---|
| **ST-1 Thumbnail** | f0 at 25% scale shows a recognisable character or object in a miniature set: the subject fills ≥ 20% of the frame height |
| **ST-3 Motion at f0** | the plate is moving on f0 (a gesture, an entrance, a camera move, a screen playing). A plate that starts on a held still is trimmed to its first moving frame |
| **ST-6 Payoff-by** | subject established by 5.0 s (HA-16) |
| ST-2 Mute | not used as a pass/fail: HA-16 hooks read as pantomime; captions carry any speech |
| ST-4 Read time | n/a (no headline) |
| ST-5 Change count | ≥ 1 weighted change in 0–3 s (the first cut at 1.2–3.0 s); a low number is DNA (evidence 1–1.5) |

### 6.2 Default archetype: HA-16 Diegetic `[DNA]`
The hook is a **character already doing something** in its miniature world. Nothing is written over it. The first change is a cut on the action into a closer or wider size. By 5.0 s the viewer knows who this is, where they are and what they want.

**F-A Dialogue sketch (evidence v03 @0:00–0:05):**

| t (s) | Beat | Tone | Plate / visual | Caption | Cut / move | SFX cue |
|---|---|---|---|---|---|---|
| **f0** | Opener | setup | **P-COLD-ACTION**: wide or medium of character 1 in the set, already moving (holding a snack on a rock; a second character flying in from the frame edge). Subject ≥ 20% of frame height | none | — | none (plate audio only) |
| 0.0–1.1 | Action arc | setup | Character 2 crosses to character 1 (the entrance is the motion that stops the thumb) | none until the first word | — | — |
| 1.1–1.4 | First line | setup | Same shot | **CS-1** cuts on 2 f before the first word ("Dude, you've GOT / to try this", in at 1.17 s) | — | — |
| 1.4 | First cut | setup | **P-MATCH-CUT** to a medium close-up of both characters on the end of the approach | line held across the cut (same speaker) | hard cut ±2 f of the action end (1.42 s) | — |
| 1.4–5.0 | The want | setup | **P-CHAR-LINE-CU**: character 2 offers the thing; character 1 reacts ("Oh… WOW") | next line on its first word | 0–1 cut | — |
| **≤ 5.0** | Payoff (ST-6) | | Two characters, the place and the offer are established | | | |

**F-B Product broadcast (evidence v02 @0:00–0:05):**

| t (s) | Beat | Tone | Plate / visual | Caption | Cut | SFX cue |
|---|---|---|---|---|---|---|
| **f0** | Opener | setup | **P-OTS-WATCH**: over-the-shoulder of a character watching the in-world screen; the screen is already playing (P-SCREEN-SHOW) | none | — | none |
| 0.0–2.8 | Watching | setup | Locked-off; the only motion is the screen and a small character gesture | none | — | — |
| 2.8 | First cut | setup | **P-ESTABLISH-WIDE**: the characters on the couch (who is watching) | none | hard cut | — |
| 2.8–5.2 | Who | setup | Characters settle, reach for drinks | none | — | — |
| 5.2 | Turn on | awe | Cut to the screen close shot; **P-SCREEN-STATIC** (1.2 s), then the spot opens | none | hard cut | `transitions` cue allowed on the static (soft) |
| **≤ 5.0** | Payoff | | Watchers + place established | | | |

**F-C Vignette (evidence v01 @0:00–0:03):**

| t (s) | Beat | Tone | Plate / visual | Caption | Cut | SFX cue |
|---|---|---|---|---|---|---|
| **f0** | Opener | setup | **P-PRODUCT-IN-HAND** inside **P-COLD-ACTION**: a medium shot of the character mid-sip (the cup already at the lips at 0.33 s) | none | — | none |
| 0.0–1.2 | Sip | setup | Sip, lower the cup | none | — | — |
| 1.2–2.9 | Pose | setup | A head tilt, a pose, the product in hand | none | — | — |
| 2.9 | First cut | setup | **P-ESTABLISH-WIDE** / **P-PATIENT-HOLD**: the character walks toward camera down a recognisable street | none | hard cut (2.92 s) | — |
| **≤ 5.0** | Payoff | | Character + product + place established | | | |

**Never** open on: an empty set, a title card, the wordmark, a product pack shot, a still frame, or a slow fade from black.

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`

**HA-15 Atmosphere (the product as the moving object).** Open on the product itself doing something in the world (steam rising from the cup, a pack sliding across a miniature counter, a phone lighting up on a bedside table). The first caption or screen label by 5.0 s.

| t (s) | Visual | Caption | Cut |
|---|---|---|---|
| f0 | Insert of the product in motion, set dressing around it | none | — |
| 0–2.5 | The motion completes (steam curls, the phone buzzes across the table) | none | — |
| 2.5–3.0 | Cut on the motion to the character who reacts to it | none | hard cut |
| ≤ 5.0 | First line or label word | CS-1 on the first word | — |

Examples: `[NICHE: example A, tea brand]` a felt teabag lowers itself into a cup by its string; the mouse who owns the cup peers over the rim. `[NICHE: example B, budgeting app]` a clay phone on a desk buzzes and slides toward the edge; a clay hand catches it.

**HA-14 Cold authority (mid-line open; F-A only).** The first word is spoken at 0.00–0.10 s, so the caption is on f0, and the plate is mid-action.

| t (s) | Visual | Caption | Cut |
|---|---|---|---|
| f0 | Medium close-up of the speaking character, mid-gesture | the first line on f0 (fade-in finishes by f4) | — |
| 0–1.5 | The line plays | held | — |
| 1.5–2.5 | Cut to the listener's reaction (P-REACTION-RUN, one shot) | next line | hard cut |
| ≤ 3.0 | Who and what established | | |

Examples: `[NICHE: example A]` a clay barista bear mid-sentence: "You're telling me you've never had it cold?" `[NICHE: example B]` a clay cat at a laptop mid-sentence: "Okay, where did all my money go?"

**HA-13 Cold action (the chaotic open; F-A, energy step `balanced` only).** A character crashes, falls or bursts in, with its line on f0 and the first cut by 2.1 s.

| t (s) | Visual | Caption | Cut |
|---|---|---|---|
| f0 | Fast action already in progress (a tumble, a door flung open) | the shout as CS-1 on f0 | — |
| 0–2.1 | The action lands | held | first cut ≤ 2.1 s on the landing |
| ≤ 2.3 | The subject in frame, the problem obvious | next line | — |

Examples: `[NICHE: example A]` a felt squirrel skids into frame on an acorn, "I'm LATE!". `[NICHE: example B]` a clay commuter's paper wallet bursts and coins roll everywhere, "Not again…".

### 6.4 Hook pairs by topic `[NICHE]`
Pair type for HA-16 / HA-15 / HA-13 is **subject → reveal**: who or what is on f0, what is revealed by 5.0 s, and where the product turn lands later.

| Topic | First subject (f0) | Revealed by 5.0 s | Product turn (later) |
|---|---|---|---|
| `[NICHE: example A]` Cold brew launch | A clay fox on a hot pavement fanning itself | It is stranded in a desert town; a friend arrives with something "cold" | At 60–70%: a glacier-blue cold-brew waterfall (P-REVEAL-WIDE), then the can in paw |
| `[NICHE: example A]` Herbal sleep tea | A felt owl yawning on a branch at noon | The owl cannot sleep; the moon character offers a cup | At 65%: the pack glows on a bedside stump (P-PRODUCT-IN-HAND) |
| `[NICHE: example A]` Snack multipack | A clay kid opening a lunchbox | The lunchbox is empty; the dog under the table looks guilty | At 55%: the dog's TV shows the multipack (F-B screen spot) |
| `[NICHE: example A]` Morning coffee | A clay character mid-sip in sunglasses (v01) | A sunny street, the character walking with the cup | The cup is the product from f0 (F-C) |
| `[NICHE: example B]` Budgeting app | A felt hamster counting coins in a jar | The jar is empty by Thursday; a friend shows a phone | At 60%: the phone screen shows the app's spending ring (P-SCREEN-* on the phone) |
| `[NICHE: example B]` Savings goal | A paper-cut bird building a nest out of coins | The nest is for a trip; it keeps falling apart | At 65%: a "goal reached" screen on a tiny phone (claims-list wording) |
| `[NICHE: example B]` Bill reminders | A clay character asleep while letters pile up on the mat | The letters are bills; the alarm clock is a phone | At 55%: the phone buzzes with a reminder card (screen spot) |
| `[NICHE: example B]` Splitting costs | Four clay friends at a pizza table, one hand reaching for the bill | Nobody wants to pay; awkward silence | At 60%: one phone shows the split screen (claims list) and everyone relaxes |

### 6.5 Post title writing (no on-screen headline) `[DNA formula; NICHE examples]`
The reel has no on-screen headline. The **post title** (the first line of the Instagram caption) carries the hook in words:
- Formula: `[character] + [their small problem or want]`, lowercase except names, ≤ 8 words, one emoji max at the end, no hashtags in the first line.
- Templates: "{character} just wanted {thing}" · "{character} found out where {product noun} comes from" · "pov: {character} discovers {benefit in plain words}" · "{character} vs {small daily problem}". (Curly braces here are writing slots, not packaging placeholders.)
- Write 3, pick the one whose words match f0 best (the character named in the title is on f0).
- Banned: "You won't believe…", "BEST {product} EVER", claims not in the claims list, prices, all caps.

### 6.6 Hook sound
The hook is the plate's own mix. No SFX-pack cue in 0–3 s except the in-screen static (F-B, soft). When the plates are silent (FB-3), the music bed enters from f0 at bed level (§11).

### 6.7 CTA `[DNA device set; VAR values]`
| Device | Spoken pattern | On-screen element | Hold | Where |
|---|---|---|---|---|
| **end_card** (default) | none (or the brand's own end line in the plate mix) | The wordmark alone on black (P-WORDMARK-CARD) | 1.8–2.4 s | the last 1.6–2.4 s |
| **link_bio** | none | Wordmark + link line at y 1180, in 8 f after the wordmark settles | link line readable ≥ 1.5 s | the end card |
| **post_only** | none | Wordmark card only; the offer goes in the post text | 1.8–2.4 s | end |
| **none** | none | The wordmark card still closes the reel (the brand's signature is DNA, not a CTA) | 1.6–2.0 s | end |

Silence before the card: the button line's last word ends ≥ 6 f before the iris snaps closed or the cut to black. This copy's device: **{{BV-08.device|end_card}}**; link line text: "{{BV-08.keyword|link in bio}}".

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type: `sketch` (every format)
| Beat | F-A Dialogue sketch (24–30 s) | F-B Product broadcast (20–30 s) | F-C Vignette (10–16 s) |
|---|---|---|---|
| **setup** | 0 → 15–20% (0–5 s): who, where, the want (an offer, a problem, a craving) | 0 → 18% (0–5.2 s): who is watching what | 0 → 25% (0–3 s): the character with the product |
| **gag / journey / broadcast** | 20 → 60% (5–17 s): the journey or the misunderstanding, 3–5 shots, 1–2 long travelling shots (4–7 s) | 18 → 60% (5.2–17 s): the screen spot ritual (§7.3) | 25 → 70% (3–9 s): one patient wide (walk, ride, look around) |
| **product turn** | 60 → 78% (17–22 s): the product revealed in the world (P-REVEAL-WIDE, P-PRODUCT-IN-HAND), the longest held shot of the second half | 60 → 85% (17–24 s): reactions to the spot (P-REACTION-RUN) | (the product was in hand from f0) |
| **button** | 78 → 92% (22–27.5 s): the payoff line or non-sequitur; the masked punch line allowed here | 85 → 93%: the wide hold (P-WIDE-HOLD-OUT) | 70 → 86% (9–12 s): a non-sequitur (a cat in the bushes, v01) |
| **logo** | last 1.8–2.4 s: T-IRIS → P-WORDMARK-CARD | last 1.8–2.4 s: T-CUT-BLACK → card | last 1.6–2.0 s: T-CUT-BLACK → card |

Evidence anchors: v03 setup 0–5, journey 7–20, reveal 20–23, button 23–29.6, logo 29.8–32.2; v02 setup 0–5.2, broadcast 5.2–18.3, reactions 19.5–23.9, wide hold 23.9–28.3; v01 sip 0–2.9, walk 2.9–9.1, button 9.1–12.0.

### 7.2 Markers
`markers: none`. A sketch has no numbering, chapter chips or progress bar. The screen spot's label words are claims, not markers.

### 7.3 Unit rituals (frames at 30 fps)

**Line ritual (F-A, every spoken line):**
1. The speaking character's shot is on screen ≥ 8 f before the line (cut in on the previous line's end or on an action).
2. CS-1 cuts on (0 f) 2 f before the first word.
3. The line plays; no cut inside it (R-6).
4. The caption holds through ≤ 0.6 s of pause, then cuts off (0 f).
5. Cut on the reply's first word −2…+3 f to the replying character, or hold the two-shot when both are in it.

**Screen spot ritual (F-B; times from the cut to the screen shot; measured frame by frame on v02 @0:05.17–0:19.49, 29.97 fps):**

| Step | Pattern | Duration | Frames (30 fps) | Change | Evidence |
|---|---|---|---|---|---|
| 0 Show tail | P-SCREEN-SHOW | 0.27 s | 8 | the cut lands on the show still playing | 5.17–5.43 |
| 1 Static on | P-SCREEN-STATIC | 1.1 s (0.6–1.8) | 33 | hard on (no glow ramp) | 5.43–6.55 |
| 2 Pack 1 placed | P-PACK-IN (hand) | 0.8 s | 24 | the pack steps in on 2–3 f poses | 6.81–7.61 |
| 3 Empty sky | (sky only) | 0.7 s | 22 | hard | 7.61–8.34 |
| 4 Label 1 + pack 2 builds | P-LABEL-PLUS-PACK | 1.4–1.6 s | 42–48 | label blinks 6–7 f on / 6 f off; the pack builds in 4–5 held steps of 3 f | 8.34–9.74 |
| 5 Label 2 + pack 3 (hand) | P-LABEL-PLUS-PACK | 1.9 s | 56 | same blink; pack set in by a hand | 9.94–11.81 |
| 6 Label 3 + pack 4 builds | P-LABEL-PLUS-PACK | 1.7–2.3 s | 50–70 | same blink | 12.01–14.31 |
| 7 Clear sky | (sky only) | 0.5 s | 16 | hard | 14.31–14.85 |
| 8 Lineup + wordmark | P-SCREEN-LINEUP | 2.1 s | 63 | packs hard; wordmark grows in 2 f steps over ≈ 18 f, then holds | 14.85–16.95 |
| 9 Static off | P-SCREEN-STATIC | 1.1 s | 32 | hard | 16.97–18.05 |
| 10 Show returns | P-SCREEN-SHOW | 1.4 s | 43 | hard; then cut to the reaction run | 18.05–19.49 |

Total ≈ 14.3 s (one 14.3 s locked-off shot). With 2 claims drop step 5; with 1 claim drop steps 4–5. With 1 SKU every pack step shows the same pack from alternating sides (x 42% / 58% of the screen). Never more than 3 labels. Everything inside the screen moves on **held steps of 2–3 f (≈ 10–15 images/s) or the 6 f blink**, never on smooth tweens (§10.2).

**Journey step ritual (F-A gag beat, 2–4 steps):** each step is one plate in a new place (a log, river stones, giant leaves), 2.5–4.5 s; the travelling character enters from the side the previous shot exited (R-11); one line per step at most ("Follow me!", "Hold on, I can't fly!").

### 7.4 Open loops and re-hooks
- **The want loop:** the setup states or shows a want (an offer "you've GOT to try this", an empty jar, a show everyone is watching). The product turn pays it, on screen.
- **The screen loop (F-B):** the static promises something; the spot pays it.
- **Re-hooks:** none (micro class). **Intro cap:** the hook (0–3 s) is ≤ 15% of runtime by construction.

### 7.5 Rhythm and energy curve
Calm and even. The setup is unhurried; the journey quickens slightly (steps of 2.5–3.5 s); the product turn is the one big held moment (a 2–3 s wide); the button is a beat of stillness and a small laugh; the logo is quiet plus the wordmark. Never escalate with speed tricks; escalate with scale (a bigger set, a brighter reveal).

### 7.6 Cadence (state changes)
| Token | F-A | F-B | F-C | Evidence |
|---|---|---|---|---|
| `sc_per_10s` | 2.5–6.0 | 2.0–6.0 | 1.5–4.0 | v03 6 cuts + 1 glow-out wipe + the iris + ≈ 14 caption swaps in 32 s (shots 1.42, 4.13, 1.75, 4.95, 3.65, 6.65, 7.75 s; median 4.1 s); v02 6 cuts + ≈ 10 screen swaps in 28 s; v01 2 cuts in 12 s |
| `hook_sc_3s` | 1 | 1 | 1 | first cuts at 1.42 / 2.77 / 2.92 s |
| `max_gap_s` (weight ≥ 1) | 8.0 | 6.5 (screen swaps count) | 6.5 | v03 last shot 7.75 s (button + iris, camera pulling out); v01 walk shot 6.16 s |
| `max_static_s` | 3.0 | 4.5 | 3.0 | v02 reaction close-ups are held poses with one blink (20.0–22.0 frozen); v02 wide hold 23.9–28.3 near-still; v01 end pose frozen 1.58 s (7.50–9.08) |
| `caption_weight` | 0.5 | 0.5 | 0.5 | support captions |
| `cuts_per_min` | not DNA (the cut detector misses soft plate changes) | | | |

---

## §8 Visual system `[REQ]`

### 8.1 Graphics role and budget
- `graphics: minimal` (F-A, F-C): the recurring engine devices are (1) captions, (2) the closing iris + wordmark card, (3) the disclosure line. Overlay graphics beyond captions ≤ 15% of runtime (iris 1.5 s + card 2.0 s of 28 s = 12.5%).
- `graphics: support` (F-B): adds (4) the in-world screen spot, ≤ 50% of runtime (v02: 12.3 s of 28.3 s = 43%).
- **Numbers do not become pictures** in this style: there are no data visuals. A number appears only as a claims-list label word.
- Pattern count: **34**: 14 cut and footage-treatment patterns (no graphics added) and 20 caption, screen, end, legal and fallback patterns.

### 8.2 Families
| ID | Family | Source class | The buyer supplies |
|---|---|---|---|
| **B-1** | Plates (the story) | buyer-owned | Every shot (SH-1), native 9:16 (SH-2), with its mix (SH-3) |
| **B-2** | Dialogue captions | engine | The dialogue script (SH-4) |
| **B-3** | In-world screen spot | engine + buyer-owned | A locked-off screen plate (SH-8), pack shots (SH-6) |
| **B-4** | Label words | engine | The approved claims list (SH-7) |
| **B-5** | Wordmark and end card | buyer-owned (engine fallback FB-5) | The wordmark file (SH-5) |
| **B-6** | Closing transitions (iris, cut to black, static) | engine | — |
| **B-7** | Legal and link lines | engine | Disclosure wording (BV-14), link line (BV-08) |
| **B-8** | Third-party stand-ins on screens and lines | creator-supplied third-party, else created (§12.5) | A licensed clip or logo, only if they hold it |

### 8.3 Pattern specs
Frames at 30 fps. "Engine" names the building block.

**Cut and footage-treatment patterns (B-1; no graphics added)**

| ID | Name | Type | What's on screen | Recipe | When | Engine |
|---|---|---|---|---|---|---|
| **P-COLD-ACTION** | Cold action open | cut | A plate already in motion on f0; subject ≥ 20% of frame height | In point = the first frame of a motion or 2–4 f into it; never a held still | Every f0 | cut list (`stage: L-plate`) |
| **P-MATCH-CUT** | Cut on the action | cut | The same action continued in a new size (wide → CU) | Out on the frame the motion completes or reaches its matched pose; in on the same pose ±2 f | The first cut; any size change inside a beat | cut list |
| **P-ESTABLISH-WIDE** | Establish the place | cut | A wide of the set (street, living room, forest) | 2.4–3.5 s; cut in on a character's movement inside the wide | After the opener (1.2–3.0 s) and at each new location | cut list |
| **P-CHAR-LINE-CU** | Character line close-up | cut | One character's face for its line | Line length + 8–15 f; cut in ≥ 8 f before the first word | Every F-A line where a CU exists | cut list |
| **P-REACTION-RUN** | Reaction run | cut | 2–3 single close-ups of different characters | 1.2–2.0 s each (v02: 1.26, 1.27, 1.90 s); never the same character twice in a row | After the product turn (F-B) or a punch line | cut list |
| **P-PATIENT-HOLD** | Patient hold | cut | One continuous action (a walk toward camera, a ride, a long look), usually with the plate's own camera move | 4.0–7.8 s, uncut; ≤ 2 per reel (v01 walk 6.16 s with a 1.45× push; v03 journey 6.65 s) | Gag/journey beat; F-C middle | cut list |
| **P-OTS-WATCH** | Over-the-shoulder watch | cut | Characters from behind, facing the thing they watch | 2.0–3.0 s, locked-off | F-B opener | cut list |
| **P-PRODUCT-IN-HAND** | Product as prop | cut | The product held, sipped, opened, used by a character | Hold ≥ 1.0 s with the product's front visible; never cut while its label is turning | F-C from f0; F-A at the turn | cut list |
| **P-SENSE-FLASH** | Sensory flash | cut | A short imagined or sensory trip (the honey-glow trip, v03 @5.55–7.30) | 1.5–2.0 s (v03 1.75 s); in on T-GLOW-IN, out on T-BLOOM-OUT; a line over it allowed (CS-2 if bright) | The first taste / the moment of delight | cut list |
| **P-JOURNEY-STEPS** | Journey steps | cut | 2–4 travel plates, each a new place | 2.5–4.5 s each; screen direction kept (exit right → enter left) | F-A gag beat | cut list |
| **P-REVEAL-WIDE** | The reveal wide | cut | The product's world revealed (the honey waterfall, a factory of clouds) | 2.0–3.0 s, the longest held shot of the second half; a one-word line ("WOAH") allowed | F-A product turn | cut list |
| **P-BUTTON** | Button | cut | The last character beat: a reaction, a non-sequitur, a satisfied sip, the masked punch line | 2.0–4.0 s (iris included). F-A: the iris may start closing once the button's action peaks, and the last line may play inside the porthole hold; the snap to 0 starts ≥ 6 f after the last word. F-B, F-C: the cut to black comes ≥ 6 f after the last word or action | Every reel, before the logo | cut list |
| **P-WIDE-HOLD-OUT** | Wide hold out | cut | The full cast in the wide, settling | 3.0–4.5 s, locked-off | F-B button | cut list |
| **P-FRAME-HOLD** | End-frame hold | footage-treatment | The plate's last frame held | ≤ 12 f, only to land a caption tail or the iris; at most twice per reel. A held pose that is already in the plate (v01 @7.50–9.08, 38 f frozen) is the plate's beat, not this pattern: keep it | When a plate runs 2–12 f short | cut list (hold on the span) |

**Caption patterns (B-2)**

| ID | Name | Type | What's on screen | Recipe | When | Engine |
|---|---|---|---|---|---|---|
| **P-DIALOGUE-SUB** | Dialogue caption | overlay | CS-1: pale yellow 64 px, ≤ 2 lines, y 1420 | §5.3 | Every spoken line | caption engine (CS-1) |
| **P-BRIGHT-SUB** | Bright-plate caption | overlay | CS-2: same + 2 px warm stroke | `captions.overrides [{t: [a, b], profile: "CS-2"}]` | Shots logged `bright` | caption engine (CS-2) |
| **P-HIGH-SUB** | High-band caption | overlay | CS-3 at y 1180 | override to `CS-3` on the span | A face low in the frame (y 1330–1520) | caption engine (CS-3) |
| **P-MASKED-LINE** | Masked punch line | overlay | The button line with its profanity masked ("F**k that's good") | CS-1 + `profanity_mask: inner`; on the button plate or inside the iris | F-A button | caption engine |

**Screen spot patterns (B-3, B-4; F-B; one scene clipped to the screen rect, `exception: "E6"`, the rect marked `data-slot`)**

| ID | Name | Type | What's on screen | Recipe | When | Engine |
|---|---|---|---|---|---|---|
| **P-SCREEN-ON** | Screen spot | overlay (anchored) | The engine's screen content inside the plate's screen rect: `accent` sky with 3 soft white clouds (45% opacity radial blobs, drift −6 px/s), CRT treatment (2 px scanlines at 6% black every 4 px, inner vignette 18%, one diagonal glass highlight 8% white top-left), corner radius 6% of the rect height | Rect from the anchor pass (§17), constant for the shot; the spot starts and ends hard on the static; clouds drift in 3 f held steps | F-B broadcast beat | bespoke scene z3, `clip-path` to the rect |
| **P-SCREEN-LABEL** | Label word | overlay | 1–2 claims-list words, Barlow Condensed 700 caps, `primary`, centred, centre y = top + 0.21·h | Hard on, then blinks 6–7 f on / 6 f off for 1.4–2.0 s while its pack builds (v02 @8.34–14.31); 2 f before its spoken word when the word is spoken | Spot steps 4–6 | inside the screen scene, `text_class: "TC-label"` |
| **P-PACK-IN** | Pack in | overlay | One pack shot, 0.62·h tall, centred (or x 42% / 58%), bottom at 0.92·h | Enters in held stop-motion steps, never a smooth slide: either set in from the bottom edge by the brand's hand plate, or (engine) 4–5 held poses of 3 f each, scale 0.55 → 0.8 → 0.95 → 1.0 with ±2° tilt and ±6 px jitter per pose, then holds (v02 @6.81, @8.55–9.00 the pack builds from a clay ring) | Spot steps 2, 4–6 | inside the screen scene (`ctx.asset`; the scene's `step_frames: 3` holds each pose 3 f) |
| **P-LABEL-PLUS-PACK** | Claim + pack | overlay | A label word at the top, its pack building under it | Label on at 0 and blinking; pack steps in from +6 f; 42–70 f | Spot step 6 | inside the screen scene |
| **P-SCREEN-LINEUP** | Lineup + wordmark arc | overlay | 1–4 packs at 0.5·h spread across 80% of the width, bottoms at 0.90·h; the wordmark at 85% width over them, centre 0.45·h | Packs hard; wordmark grows 0.65 → 1.0 in held 2 f steps over ≈ 18 f, tilt settling −6° → 0°; hold 1.0–1.6 s (step total 2.1 s) | Spot step 8 | the wordmark is its own scene over the screen (`step_frames: 2`, `overlaps: [<screen scene>]`); the packs stay in the screen scene |
| **P-SCREEN-STATIC** | Channel static | transition (in-screen) | Seeded grey noise (`static` ±40 luminance, 3 px blocks) with 2 slow horizontal roll bars, inside the rect only | 0.6–1.8 s; average luminance constant (no flashing) | Spot steps 1, 9; any channel change | inside the screen scene (canvas, `ctx.rng`) |
| **P-SCREEN-SHOW** | The show on screen | overlay (anchored) | What the screen plays before and after the spot: the brand's own footage, a creator-supplied licensed clip, or a **created** generic show (a green pitch with moving dots, a cartoon sky, a weather map with no real brand) | Created shows carry no real names, logos or broadcaster graphics. A show that stands in for a named real programme is an insert (§12.5) | F-B opener and after the spot | screen scene; `fx.appUI({kind: "video"})` for a recorded insert |
| **P-SCREEN-PACK3D** (optional) | Pack turntable on the screen | overlay (anchored) | The brand's pack as a lit 3D box turning inside the screen rect: the front face is the brand's front pack shot exactly as delivered, the back face its back shot (or the front again), the sides a flat `primary`; no text drawn by the engine | One `VEOS.fx.three` scene clipped to the screen rect, half a turn (180°) over 1.5–2.0 s on 3 f held steps (`extra: {step_frames: 3}`), then holds front-on; replaces one P-PACK-IN step at most once per spot. Never outside the screen (N2), never on a full frame, only when the brand approves a 3D pack | A single-SKU spot that needs one more beat | `fx.three` `custom` (recipe below); one 3D scene at a time (45–150 ms per frame) |

```js
// P-SCREEN-PACK3D (optional): the brand's front / back pack shots on a lit box, half a turn on 3 f held steps, inside the screen rect R
function screenPack3D(id, t_in, t_out, R /* {x, y, w, h} from the anchor pass */, front, back, ratio /* pack w / h */) {
  const h = 2.2, w = h * ratio, d = w * 0.35;
  VEOS.fx.three({ id, t_in, t_out, z: 4, box: R, overlaps: ["screen"], extra: { step_frames: 3 },
    camera: { fov: 28, pos: [0, 0.2, 7] }, ground: { y: -h / 2, size: 3, shadow: 0.3 },
    objects: [{ kind: "custom", pos: [0, 0, 0], build(THREE, ctx) {
      const tex = a => { const t = new THREE.Texture(ctx.assetImage(a)); t.colorSpace = THREE.SRGBColorSpace; t.needsUpdate = true; return t; };
      const side = new THREE.MeshStandardMaterial({ color: ctx.col("primary"), roughness: 0.6 });
      const face = a => new THREE.MeshStandardMaterial({ map: tex(a), roughness: 0.55 });
      return new THREE.Mesh(new THREE.BoxGeometry(w, h, d), [side, side, side, side, face(front), face(back || front)]); },
      keys: [{ at: 0, rot: [0, -180, 0] }, { at: 1.8, rot: [0, 0, 0], ease: "inOut" }] }] }); }
```

**End, legal and fallback patterns (B-5, B-6, B-7, B-8)**

| ID | Name | Type | What's on screen | Recipe | When | Engine |
|---|---|---|---|---|---|---|
| **P-IRIS-OUT** | Iris out | transition | A soft-edged circle closing on the characters, black outside | Centre = the characters' face midpoint (anchor pass; default 540, 920). r 1110 → 510 over 42 f ease-in-out (v03 @28.0–29.4); hold r 510 for 18–24 f while the button line ends (the plate keeps animating and its camera keeps pulling out); snap 510 → 0 over 6 f ease-in (v03 @30.15–30.33); 24 px feather; no black gap: the wordmark fades in under the snap | F-A end | scene z11 (radial-gradient mask); stage → L-endcard on r 0 |
| **P-CUT-BLACK** | Cut to black | transition | Black | Hard cut on the frame after the button's out point; black 4 f before the wordmark fades in | F-B, F-C end | stage `L-endcard`, `via: cut` |
| **P-WORDMARK-CARD** | Wordmark card | stage | The brand's wordmark alone, white on black, centre (540, 960), 648 px wide | Fade over 5 f, no scale (F-A: starting with the iris snap, v03 @30.20–30.37); hold 1.8–2.4 s (v03 1.87 s); hard end (no fade-out) | Every reel | `L-endcard` + scene z5 (`ctx.asset("wordmark")`), `kind: "end-card"` |
| **P-LINK-LINE** | Link line | overlay | The BV-08 link line, 40 px white at y 1180 | In 8 f, 0.3 s after the wordmark settles | `link_bio` only | scene z5 on the card |
| **P-STOCKIST-LINE** | Stockist line | overlay | "Now at <retailer>" set in type, 40 px white at y 1180; never a retailer logo unless the brand supplies it | In 8 f, 0.3 s after the wordmark | When the script names a retailer | scene z5; insert record `logo_plate` |
| **P-DISCLOSURE** | Paid partnership | legal | "Paid partnership" 24 px white at x 64, y 150 | In 6 f at 0.0 s, hold ≥ 2.0 s (default 2.5 s), out 6 f | Paid posts | scene z6, `text_class: "TC-legal"` |
| **P-BAND-PLATE** | 16:9 band | stage | The 16:9 plate in a 608 px band, black above and below | `L-plate-band`; captions at y 1290 | FB-2 (16:9 plates) | stage layout |
| **P-BLUR-PLATE** | 4:5 band | stage | The 4:5 plate band over its own blurred copy | `L-plate-blur`; blur 48 px, luma −0.35 | FB-2 (4:5, 1:1 plates) | stage layout |
| **P-CROP-WINDOW** | Static crop window | footage-treatment | A fixed 9:16 window cut from a wider plate | Only when the action stays inside the window for the whole shot; ≤ 1.35× on 1080p, ≤ 2.0× on 2160p; never animated | FB-2 alternative to a band | cut list crop |

### 8.4 Line → pattern lookup `[NICHE]`
Classify every plate and every line at P5.

| Line / plate type | Primary | Alternates |
|---|---|---|
| Opening action (any character doing something) | P-COLD-ACTION | P-OTS-WATCH (watching a screen), P-PRODUCT-IN-HAND |
| A character speaks | P-CHAR-LINE-CU + P-DIALOGUE-SUB | two-shot hold + P-DIALOGUE-SUB |
| A line over a bright plate | P-BRIGHT-SUB | — |
| A character's face sits low in the frame | P-HIGH-SUB | move the line to the next shot |
| The invitation / the offer ("you've got to try this") | P-MATCH-CUT into a two-shot | P-CHAR-LINE-CU |
| First taste / delight ("Oh… WOW") | P-SENSE-FLASH | P-CHAR-LINE-CU |
| Travel / "follow me" | P-JOURNEY-STEPS | P-PATIENT-HOLD |
| Where the product comes from | P-REVEAL-WIDE | P-SCREEN-ON (a documentary on the TV) |
| The product's benefit as a claim | P-SCREEN-LABEL (F-B) | the character's own line (F-A) |
| Showing the range / flavours | P-SCREEN-LINEUP | P-PACK-IN ×2 |
| `[NICHE: example A]` "It's cold-brewed / organic / low sugar" | P-SCREEN-LABEL (claims list) | a character line saying it |
| `[NICHE: example A]` Pouring, steeping, opening | P-PRODUCT-IN-HAND | P-REVEAL-WIDE |
| `[NICHE: example B]` "It tracks every rupee / dollar" | P-SCREEN-ON on the phone prop + P-SCREEN-LABEL (claims list) | a character line |
| `[NICHE: example B]` A notification / reminder | P-SCREEN-ON (the phone lights; a label word only if the claims list has it) | P-CHAR-LINE-CU reacting |
| `[NICHE: example B]` Splitting, sending, saving | P-SCREEN-LABEL + P-PACK-IN (an app-icon tile the brand supplies, as the "pack") | P-SCREEN-LINEUP of 3 feature tiles |
| Reaction to the product | P-REACTION-RUN | P-WIDE-HOLD-OUT |
| The last laugh | P-BUTTON (+ P-MASKED-LINE) | P-WIDE-HOLD-OUT |
| A real retailer / show / sports league is named | P-STOCKIST-LINE / P-SCREEN-SHOW (created) | the creator's licensed file |
| The end | P-IRIS-OUT (F-A) / P-CUT-BLACK → P-WORDMARK-CARD | + P-LINK-LINE |

### 8.5 Data and truth rules
- No figures module: no charts, counters or hero numbers.
- Every label word, number and product name on screen comes from the claims list (SH-7) or the script, character for character (H9).
- Pack shots are the brand's files, never redrawn, re-coloured or re-labelled; when the claims list ties claims to SKUs, a label word only appears next to its own SKU.
- A created screen show is generic and carries no real names; if it stands in for a real programme, it is recorded as an insert (NC-6, NC-7).
- Character dialogue is fiction; it is never presented as a customer testimonial.

### 8.6 Comedy layer `[COND: tone.comedy = light]`
Comedy is the characters' acting and the edit's timing. The engine adds **no comedy graphics** (no stickers, stamps, marker notes, freeze-frame roasts) and **no meme sounds**. Its comedy tools are timing only:
- **The beat before the button:** hold the shot 8–15 f after a reaction before cutting to the button.
- **The cut-away laugh:** P-BUTTON as a non-sequitur (v01's cat in the bushes after the walk).
- **The masked line:** the button's profanity masked inner-style ("F**k that's good"), always the last line, never in the hook.
- **The reaction run:** three faces, the last one held longest (1.9 s).
- Budget: ≤ 1 masked line per reel; ≤ 1 reaction run per reel.

### 8.7 Asset rules
- Plates, wordmark and pack shots are the brand's own files, used as delivered (crop only per FB-2).
- Created screen content is generic and unbranded (no real channels, leagues, apps or logos).
- No stock footage, no AI-generated characters, no clip art.
- Third-party moments: ask once, then create (§12.5).

### 8.8 Density and variety
- F-A: 6–10 plate shots per 30 s (v03: 7); ≤ 2 long travelling shots; ≤ 1 sensory flash; ≤ 1 reaction run.
- F-B: 6–10 plate shots per 30 s plus one screen spot (5–9 internal swaps).
- F-C: 3–5 plate shots.
- Never two consecutive shots of the same size and angle (R-9). The same journey framing at most twice in a row.

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Transition library
| ID | Transition | Frames | Recipe | SFX role |
|---|---|---|---|---|
| **T-CUT** | Hard cut on action | 0 | Out on a completed or matched motion ±2 f; in on the continuing pose | none (the plate mix carries it) |
| **T-SCREEN-SWAP** | In-screen hard swap | 0 | Content changes inside the fixed screen rect (E6); the plate around it never cuts | none |
| **T-STATIC** | Channel static | 18–54 | P-SCREEN-STATIC inside the screen rect, 0.6–1.8 s | `transitions`: one soft static/noise cue at its start, peak ≤ −24 dB |
| **T-IRIS** | Iris out | 42 + 18–24 + 6 (no black gap) | P-IRIS-OUT | none by default; the plate mix plays through |
| **T-CUT-BLACK** | Cut to black | 0 (+ 4 black) | P-CUT-BLACK | none |
| **T-GLOW-IN** | Glow into the sensory trip | 3 + 12 | Hard cut on a 3 f luminance swell (+80%, warm) with a 6 f radial zoom-blur, then decay over 12 f (v03 @5.55–5.67). Built-in: the swell is a warm `flash` on the cut `{"t": <cut>, "type": "flash", "colour": "#FFE2A8", "peak": 0.45, "pre": 3, "frames": 15}`; the zoom blur is a footage blur envelope `timeline.blur: [{"t": <cut>, "kind": "radial", "amount": 0.12, "at": "centre", "frames": 6, "shape": "decay"}]` (two built-in transitions may not overlap, a blur envelope may) | none |
| **T-BLOOM-OUT** | Bloom out of the trip | 5 + 6 | The trip blooms toward white over 5 f, then the trip image shrinks into a soft circle over 6 f, revealing the next plate (v03 @7.08–7.40). Built-in: a `flash` ending on the cut `{"t": <cut>, "type": "flash", "colour": "#FFF6E0", "peak": 0.9, "pre": 5, "frames": 5}` (peak 0.9: the measured near-white orb, luma ≈ 228), then the orb collapse `{"t": <cut>, "type": "iris", "reveal": "next", "frames": 6, "feather": 40, "at": [<trip centre x>, <y>]}` (the old shot shrinks in a soft circle over the next plate) | none |
| **T-CARD-IN** | Wordmark in | 5 | Fade, no scale; F-A starts on the first frame of the iris snap |  `cta`: one soft chime or shine on the settle frame, peak ≤ −24 dB |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | A plate in motion (P-COLD-ACTION) | A fade from black, a title, the wordmark |
| Opener → second shot | T-CUT on action (1.2–3.0 s) | A dissolve |
| Location change | T-CUT to P-ESTABLISH-WIDE or a journey step | A whip, a slide, a zoom |
| Speaker change | T-CUT on the reply's first word −2…+3 f (or hold the two-shot) | A cut inside a line |
| Into the screen spot | T-CUT to the screen shot, then T-STATIC | A full-frame overlay |
| Inside the spot | T-SCREEN-SWAP | Slides or fades between labels |
| Product turn | T-CUT into P-REVEAL-WIDE | Speed ramps, flashes |
| Into / out of the sensory trip | T-GLOW-IN / T-BLOOM-OUT (once per reel) | A plain hard cut (the trip must read as imagined) |
| Button → logo (F-A) | T-IRIS | A cut straight to the wordmark mid-line |
| Button → logo (F-B, F-C) | T-CUT-BLACK | A fade-out of the plate |
| Last frame | Wordmark hold, hard end | A black tail > 0.2 s |

### 9.3 Shot grammar `[COND: spine = footage] → ON`
| ID | Rule |
|---|---|
| **R-1** | **Cut on action:** every cut lands on a completed motion (a cup lowered, a landing, a turn) or a matched motion ±2 f |
| **R-2** | **Size change early:** the opener runs 1.2–3.0 s, then the size changes (CU ↔ wide) |
| **R-3** | **The speaker is seen:** a character's line plays on its own CU or on a shot where its face is visible; cut on the reply's first word −2…+3 f only when the replier has a CU |
| **R-4** | **Reaction run:** 2–3 CUs, 1.2–2.0 s each, never the same character twice in a row, the last one longest |
| **R-5** | **Long shots travel:** at most two shots of 4.0–7.8 s per reel, and only when the camera moves or a character travels inside them (v03 4.95 s arc, 6.65 s journey, 7.75 s pull-out) |
| **R-6** | **No cut inside a line**, except a match cut that keeps the same speaker on screen (v03 @1.42) |
| **R-7** | **The turn is held:** the product turn gets the longest shot of the second half (2.0–3.0 s) |
| **R-8** | **The button follows the turn** with at most one shot between them |
| **R-9** | **No jump cuts:** never two consecutive shots of the same size and angle |
| **R-10** | **Continuity wins:** keep the brand's animatic order when one is supplied; re-order plates only when the sketch beats (§7.1) demand it and props and positions still match |
| **R-11** | **Screen direction:** a travelling character exits one side and enters the next shot from the opposite side |
| **R-12** | **Handles:** never use the first or last 3 frames of a plate (the animators' settle frames) unless it is the end-frame hold |

### 9.4 Budget (per reel)
- T-STATIC ≤ 3 (F-B spot: 2, plus 1 channel change). T-IRIS = 1 (F-A). T-CUT-BLACK = 1 (F-B, F-C). T-CARD-IN = 1.
- Every other boundary is T-CUT. T-CUT many times in a row is the grammar; any other transition never repeats back to back.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset (captions, spoken label words) |
| Caption swap | hard in, hard out (0 f) |
| Label word swap | hard (E6), inside the screen only |
| Pack in | 4–5 held poses × 3 f, scale 0.55 → 1.0, ±2° / ±6 px jitter per pose (stepped, no easing) |
| Screen on/off | hard (the static cuts on and off; v02 @5.43, @16.97) |
| Static | 0.6–1.8 s; noise refreshed every frame from `ctx.rng(n)`; 2 roll bars moving 3 px/f |
| Screen wordmark arc | ≈ 18 f in 2 f held steps, scale 0.65 → 1.0, rotate −6° → 0° |
| Label blink | 6–7 f on / 6 f off, 1.4–2.0 s per word |
| Cloud drift (screen sky) | −6 px/s, seeded positions |
| Iris | close r 1110 → 510 over 42 f ease-in-out; hold 18–24 f; snap 510 → 0 over 6 f ease-in; feather 24 px |
| Black before the card | F-A 0 f (the wordmark fades in under the iris snap); F-B, F-C 4 f after the cut |
| Wordmark in | 5 f fade, no scale; no exit (hard end) |
| Link line in | 8 f fade + rise 12 px, 0.3 s after the wordmark settles |
| Disclosure | in 6 f at 0.0 s, out 6 f |
| End-frame hold | ≤ 12 f |
| Holds | text ≥ 0.3 s per word; label words 1.4–2.0 s in blinks |
| In-world step | every scene the engine animates inside the world steps on held poses with the scene field `step_frames`: `step_frames: 2` (screen wordmark), `step_frames: 3` (pack builds, clouds); label blink 6–7 f on / 6 f off (drawn from `lt`, not stepped). Captions, the iris and the end card have no `step_frames` |

### 10.2a Plate cadence (measured frame by frame; keep it, copy it)
| Source | Characters / objects | Camera | Evidence |
|---|---|---|---|
| v01 clay (24 fps) | pose-to-pose bursts **on ones** (8 f move), then the key pose held 12–14 f; the bird/cat shot on twos; the walk ends on a pose frozen 38 f | one linear push 1.00 → 1.45× over 3.2 s (≈ +12%/s) on ones, locked off elsewhere | @0.04–0.33 move, @0.38–0.96 hold; @4.30–7.50 push; @7.50–9.08 frozen; @9.1–10.5 twos |
| v02 clay (29.97 fps) | mostly **held poses**: reaction close-ups are stills with one blink/pose pop; screen objects on 2–3 f steps; the TV football is live footage | locked off in every shot (scale 1.000) | @20.0–22.0, @23.2 pop; @8.55–9.00 pack build |
| v03 felt (24 fps) | characters **on twos** (12 images/s) | smooth moves **on ones**: push +6% over 3.9 s, an arc with 4.9° roll + 3% over 4 s, a pull-out −8.5% over 4.3 s under the iris | @1.45–5.3, @8.3–12.25, @26–30.3 |

Rules: the engine never interpolates, blends, retimes or smooths a plate; 24 → 30 fps by frame duplication only. Engine-made motion that lives **inside the world** (P-PACK-IN, the screen wordmark, cloud drift, the optional 3D pack) steps on held poses of 2–3 f with the scene field `step_frames` (the label blink is already a 6 f on / off); engine motion **outside** the world (captions, iris, card fade) is not stepped.

### 10.2 Footage camera: `zoom_policy: source_only`
All camera movement is physical, inside the plates (dolly pushes, rack focus, pans the animators shot). The engine has **no Z presets** for this style: no punch-in, crash zoom, push-drift, shake or rotation. The only geometric change allowed is the static crop window of FB-2 (P-CROP-WINDOW), set once per shot and never animated.

### 10.3 Canvas camera
OFF (§21).

### 10.4 Layer order (back to front)
1. W-plate (the plate) or W-black
2. Screen spot scene (z3, clipped to the screen rect inside the plate)
3. Wordmark card scene (z5, on L-endcard) and link / stockist line (z5)
4. Disclosure line (z6)
5. Captions (z7, auto)
6. Iris mask (z11, momentary)

### 10.5 Finishing
None added. No grain, vignette, bloom, glow, LUT or sharpening on plates (N11). Inside the screen spot only: the CRT treatment of P-SCREEN-ON (scanlines, inner vignette, glass highlight), so the engine's screen content sits in the plate's light. Export 1080×1920, 30 fps CFR, BT.709.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`

Sound comes from the plates' own mix and the bundled SFX pack with its global rules (S1–S6). This template adds no palette.

| Line | Decision |
|---|---|
| **Cue moments** | `reveals` (a pack landing in the screen spot, the screen wordmark arc), `transitions` (the in-screen static), `cta` (the wordmark settle). The hook, story beats, lines and the button carry **no** pack cue; the plate mix carries them |
| **Meme cues** | off (`comedy: light`) |
| **Music bed** | off by default (the plates arrive mixed). **On only for silent plates (FB-3):** a calm bed from the pack from f0, at −22 dB under any foley, fading out over the last 10 f of the button so the wordmark sits in near-silence or with its cue |
| **Ducking** | the plate mix is kept as delivered; a pack bed (FB-3 only) sits ≥ 18 dB under any character voice |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; the last sound ends ≤ 6 f after the wordmark hold ends (NC-8) |

Mirrored in `tokens.json → sound`.

---

## §12 Plates, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's actual plates]`
| Setup | Spec |
|---|---|
| **A: finished plates** | The brand's stop-motion, claymation, felt, puppet, paper-cut or 3D-animated shots; 9:16; 1080×1920 or larger (2160×3840 ideal); 24, 25 or 30 fps (12 fps "on twos" inside 24 is fine); final grade baked in; one mixed audio track per plate (voices, foley, music) or a picture-locked animatic with its mix |
| Framing | Character eyes between y 480 and 1300; nothing that matters below y 1500 (caption band + Instagram UI); the right 110 px between y 900 and 1540 free of key action |
| Handles | 12–24 frames before and after each action |
| Lighting / look | Whatever the brand's world is; the template's evidence look is warm tungsten key, cool fills, macro shallow depth of field |

### 12.2 Shot list `[COND: footage_dependency ≥ medium → ON] [DNA]`
| ID | Shot / asset | Spec | Count per reel | Must / optional | Formats |
|---|---|---|---|---|---|
| **SH-1** | The plates | Every shot of the sketch, each with 12–24 f handles | 4–14 | must | all |
| **SH-2** | Native 9:16 framing | As 12.1 framing | all plates | must | all |
| **SH-3** | Plate audio | Mixed voices, foley, music per plate | 1 mix | optional | all |
| **SH-4** | Dialogue script | Every line with its exact casing and spelling, the speaking character named | 1 | optional (F-A strongly recommended) | F-A |
| **SH-5** | Wordmark | Transparent PNG or SVG, one colour (white), ≥ 1200 px wide | 1 | must | all |
| **SH-6** | Pack shots | Transparent PNG cut-outs, front-on, ≥ 900 px tall, 1–4 products (an app: icon tiles or phone-screen PNGs) | 1–4 | must | F-B |
| **SH-7** | Approved claims list | The exact 1–2 word label words legal has cleared, per SKU when they differ | 1 | optional | F-B (and any label) |
| **SH-8** | Screen plate | A locked-off plate of an in-world screen (TV, phone, billboard, window) with a flat blank face ≥ 600 px wide in frame, ≥ 6 s, plus the same set wide | 1–2 | must | F-B |
| **SH-9** | Button plate | A last 2–4 s character beat | 1 | must | F-A, F-C |

### 12.3 Fallbacks
| ID | For | What the engine does | Fidelity cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | Nothing: the engine cannot make stop-motion | the template cannot run | `no_fallback` |
| **FB-2** | SH-2 | 16:9 plates → L-plate-band (band y 556–1164, captions y 1290); 4:5 or 1:1 → L-plate-blur; a static 9:16 crop instead when the action fits (≤ 1.35× on 1080p, ≤ 2.0× on 2160p) | the miniature no longer fills the phone; reads as a TV spot repost | `degraded` |
| **FB-3** | SH-3 | Silent plates: the pack bed (calm) from f0; no captions (no speech); F-A runs as pantomime | no voices | `holds` |
| **FB-4** | SH-4 | Transcribe the plate audio; captions verbatim, sentence case | the script's emphasis caps and invented spellings are lost | `holds` |
| **FB-5** | SH-5 | Type-set wordmark from BV-01 in the wordmark slot (48° arc, white, 600–700 px) | not the brand's real mark | `degraded` |
| **FB-6** | SH-6 | The screen spot runs label words and the wordmark only | no product on screen; weaker turn | `degraded` |
| **FB-7** | SH-7 | No label words; packs and the wordmark carry the spot | no claims on screen | `holds` |
| **FB-8** | SH-8 | F-B unavailable; use F-A or F-C with the brand's product-in-world plate | no broadcast ritual | `no_fallback` (for F-B) |
| **FB-9** | SH-9 | Hold the last plate's final frame ≤ 12 f and run the end on it | no button laugh; the ending lands softer | `degraded` |

### 12.4 Props, reaction bank, matte, resolution
- **Props:** none from the buyer beyond what is in the plates. The product itself should appear as a prop in at least one plate (F-A, F-C).
- **Reaction bank:** 2–3 character reaction CUs of 1.2–2.0 s each (feeds P-REACTION-RUN and the button).
- **Matte:** none.
- **Minimum source resolution:** 1080×1920 for full-frame plates; a static crop window needs ≥ 1.35× the crop (≥ 1458 px wide for a 1080 output) and is capped at 2.0× on 2160p sources. 720×1280 plates (like the evidence) upscale 1.5× and are flagged at the checkpoint.

### 12.5 Third-party inserts: ask, then create `[REQ always]`
Claude never fetches anyone else's media. In this style, third-party moments are rare and live on **in-world screens, signs and the end line**:
1. **Analyse** the script, the plate log and the brief for third-party moments: a named TV show, sports league or match on the screen; another company's logo or product; a retailer ("now at …"); a celebrity's face on a poster; a song.
2. **Ask the creator once:** "For these N moments, do you hold a licensed clip, logo or image? Drop the files or say no."
3. **Supplied:** use as given inside the screen rect or on the end card, never altered to say something it doesn't.
4. **Not supplied: Claude creates its own visual:**
   - a named programme or match on a screen → `recreated_ui` (a generic show: a green pitch with moving dots, no league marks);
   - a retailer → P-STOCKIST-LINE, the name set in type (`logo_plate`), no logo;
   - a person's photo on a poster in the set → `silhouette`;
   - a song → not created; music only from the bundled pack or the brand's own mix.
5. **Record** every moment in `plan/inserts.json`: `{id, moment, origin: "creator" | "created", file?, substitute_of?}`.

Generic set dressing that stands in for no real thing (an unbranded cartoon on the TV, a made-up shop sign drawn by the animators) is not an insert.

### 12.6 Frame rate and audio
- Output 30 fps CFR by frame duplication (`fps=30`), never optical flow or frame blending: the stop-motion stutter is part of the look.
- Audio: the plate mix as delivered, joined at cuts with 2 f audio crossfades only where a click would occur (picture cuts stay hard); −14 LUFS integrated.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
```yaml
- id: 4
  section: gag                    # setup | gag | product | button | logo
  t0: 7.40
  t1: 10.95
  spoken: "Follow me!"
  trigger: {word: "Follow", at: 9.62}     # or {action: "bee exits right", at: 10.90}
  tone: gag                       # setup | gag | awe | button | cta
  line_type: travel
  layout: L-plate
  visual: "Wide of the log bridge: the lizard climbs on from the left, the bee flies ahead and exits right"
  layers: []                      # scene ids (none: plate + auto captions only)
  pattern: P-JOURNEY-STEPS
  plate: {id: "PL-07", in_f: 14, out_f: 120, cut_reason: action_end}
  caption: {profile: CS-1, overrides: []}
  sfx: []
  shot_id: SH-1
  fallback_used: null
```

### 13.2 Conditional fields
| Switch / module | Beat fields |
|---|---|
| captions (any spoken line) | `caption {profile: CS-1 \| CS-2 \| CS-3, overrides[]}` |
| anchors (F-B screen beats, the iris beat) | `anchor {target: "screen:PL-03" \| "faces:PL-12", rect {x,y,w,h} \| point {x,y}, follow: none}` |
| brand | `sponsor {disclosure: "Paid partnership"}` on beat 1 when paid; `end_card {wordmark: "wordmark", link_line?}` on the logo beat |
| footage (total) | `shot_id`, `fallback_used` (FB-2 on band/blur shots, FB-5 on a type-set wordmark…) |
| any third-party moment | `insert {id, origin: creator \| created}` |
| E6 | `exception: E6` on the screen-spot beat and its scene |

### 13.3 Reel header
```yaml
format: F-A                # F-A | F-B | F-C
theme: null
hook_archetype: HA-16
structure: sketch
count: null
keyword: null
cta: end_card              # from BV-08
paid: false                # true -> P-DISCLOSURE
plates: 11                 # SH-1 count
claims: []                 # SH-7 words used on screen
fallbacks: []              # FB ids used
```

### 13.4 Hook proposals (3)
```yaml
- name: "Bee flies in with the offer"
  archetype: HA-16
  opener: {plate: PL-01, in_f: 4, action: "bee enters frame right, crosses to the frog"}
  first_cut: {at: 1.42, to: PL-02, reason: match}
  hook_pair: {subject: "frog on a mushroom with a snack", reveal_by_5s: "the bee offers something it's GOT to try"}
  captions: {profile: CS-1, first_line: "Dude, you've GOT / to try this", at: 1.17}
  storyboard: "f0 wide frog + bee entering | 1.17 caption cuts on | 1.42 match cut to MCU | 3.9 'Oh… WOW' | 5.0 want established"
  sound: "plate mix only"
  stopper_test: {thumbnail: pass, motion_f0: pass, payoff_by_s: 3.9}
```

### 13.5 Checkpoint (send before building, then wait)
1. The format and why (§0.4 rule).
2. 3 hook proposals with stopper tests.
3. The plate log (P1b) and the cut list with every cut's reason.
4. The beat sheet with tones and the sketch beat timings vs §7.1.
5. The caption plan: which spans use CS-2 / CS-3 and why.
6. F-B: the screen rect (anchor pass) and the spot ritual with the exact label words and their claims-list source.
7. The SFX ledger (allowed moments only) and the transition map.
8. The inserts record (creator-supplied vs created) and every fallback used.
9. Words dropped by the claims pass (H9), if any.
10. Style stills: f0, the first cut, one line with its caption, the product turn, one screen-spot step (F-B), the iris hold (F-A), the wordmark card.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE]`
Times are planning estimates; replace them with the plates' real action frames and `words.json` onsets.

### 14.1 F-A Dialogue sketch: `[NICHE: example A]` an herbal sleep-tea brand (28.0 s)
**Plates:** 11 felt stop-motion shots (an owl who can't sleep, a moon character, a forest at night, a tea "spring"), mixed with voices. **Script excerpt:** OWL "It's NOON and I'm still up." MOON "You need to try this." OWL "Where are we going?" MOON "Just follow the steam." OWL "Is that… a river of tea?" OWL (button) "Okay. Night night." **Claims list:** not needed (no labels in F-A).

**Hook (HA-16):**
| t (s) | Plate / visual | Caption | Cut |
|---|---|---|---|
| f0 | PL-01 wide: the owl on a branch in daylight, mid-yawn (motion from f0) | — | — |
| 0.9 | Same | CS-1 "It's NOON and / I'm still up." (lead 2 f) | — |
| 2.3 | PL-02 MCU: the moon character drifts in from the top, holding a steaming cup | — | match cut on the owl turning its head |
| 3.1 | Same | CS-1 "You need to try this." | — |
| ≤ 5.0 | Subject + want established | | |

**Pattern plan:**
| Section | t (s) | Plates / patterns | Captions | End |
|---|---|---|---|---|
| setup | 0–5.0 | P-COLD-ACTION → P-MATCH-CUT → P-CHAR-LINE-CU | CS-1 ×2 | — |
| gag (journey) | 5.0–16.5 | P-JOURNEY-STEPS ×3 (steam trail through roots 3.6 s; mossy stones 3.4 s; a hollow log 4.3 s, the patient hold) | "Where are we going?" · "Just follow the steam." | — |
| product turn | 16.5–21.0 | P-REVEAL-WIDE: the tea spring glowing amber (2.8 s, CS-2 because bright) → P-PRODUCT-IN-HAND: the owl holds the cup, the pack on a stump beside it (1.7 s) | "Is that… / a river of tea?" (CS-2) | — |
| button | 21.0–25.4 | P-BUTTON: the owl drinks, its eyes droop, it tips over onto a moss pillow (21.0–23.6); P-IRIS-OUT closes on it 23.6–24.7 (r 1110 → 510, centre 540, 1010), holds 24.7–25.2 while the last line finishes inside the porthole, snaps to 0 over 25.2–25.4 | "Okay. Night night." (24.2–25.0, CS-1, over the iris) | snap starts 6 f after the last word |
| logo | 25.2–27.5 | P-WORDMARK-CARD fades in over 5 f under the snap, hold 2.0 s | hidden on the card | hard end 27.5 |

Runtime 27.5 s (target 20–30). CTA: `end_card`. SFX ledger: one soft shine on the wordmark settle (`cta`). Inserts: none. Fallbacks: none.

### 14.2 F-B Product broadcast: `[NICHE: example B]` a budgeting app (24.3 s)
**Plates:** 7 claymation shots of a hamster family in a living room; a locked-off shot of a retro TV with a blank green face (8 s); the couch wide; three character CUs; silent plates (FB-3: calm bed from f0). **Pack shots:** three phone-screen PNGs from the brand (spending ring, savings goal, bill reminder). **Claims list:** "TRACKS EVERYTHING", "ZERO FEES", "AUTO-SAVE".

**Hook (HA-16):**
| t (s) | Plate / visual | Caption | Cut |
|---|---|---|---|
| f0 | PL-01 P-OTS-WATCH: the hamster kid from behind, watching the TV, which already plays a created generic show (a cartoon cheese-rolling race, no real names) | — | — |
| 2.6 | PL-02 P-ESTABLISH-WIDE: mum and dad hamster on the couch counting coins into a jar | — | hard cut on dad dropping a coin |
| 5.0 | Watchers, place and want (the coin jar) established | | |

**Pattern plan:**
| Section | t (s) | Patterns | Screen content (E6 swaps) |
|---|---|---|---|
| setup | 0–5.0 | P-OTS-WATCH (P-SCREEN-SHOW created) → P-ESTABLISH-WIDE | the generic race show |
| broadcast | 5.0–15.4 | Cut to PL-03, the locked-off TV (rect from the anchor pass: x 190, y 700, w 680, h 440). P-SCREEN-ON with the ritual §7.3 | static 1.2 s → "TRACKS EVERYTHING" 1.0 s (Barlow 700 caps 66 px = 0.15 × 440, red on sky; 2 words, 17 chars) → phone PNG 1 slides in 1.0 s → "ZERO FEES" 1.0 s → phone PNG 2 1.0 s → "AUTO-SAVE" + PNG 3 1.5 s → clear sky 0.4 s → three phones + wordmark arc 2.0 s → static 1.0 s |
| reactions | 15.4–19.4 | P-REACTION-RUN: kid CU 1.3 s → mum CU 1.3 s → dad CU 1.4 s (dad drops the coin jar into a drawer) | — |
| button | 19.4–22.0 | P-WIDE-HOLD-OUT: the family settles back, the TV returns to the race (2.6 s) | the generic race show again |
| logo | 22.0–24.3 | P-CUT-BLACK (black 4 f) → P-WORDMARK-CARD (in 5 f, hold 1.9 s) + P-LINK-LINE "Download free · link in bio" (BV-08 `link_bio`) | — |

Screen spot runtime 10.4 s of 24.3 s = 43% (≤ 50%). Inserts: the race show is generic set dressing (not an insert). SFX ledger: static cue ×2 (two different files), a soft pop on each pack slide-in (`reveals`, 3 different files), a shine on the wordmark settle. Fallbacks: FB-3 (bed on).

### 14.3 F-C Vignette: `[NICHE: example A]` a snack brand's new flavour (14.3 s)
**Plates:** 4 claymation shots: a clay skateboarder eating from the bag, a boardwalk wide, a seagull eyeing the bag, the gull stealing a chip. No dialogue (plate mix: foley + music).

| Section | t (s) | Plates / patterns | Text | Cut reason |
|---|---|---|---|---|
| setup (hook) | 0–2.8 | P-COLD-ACTION + P-PRODUCT-IN-HAND: MCU of the skater crunching a chip, bag in hand, front of the bag to camera | none | — |
| wide | 2.8–8.6 | P-PATIENT-HOLD: the skater rolls toward camera down the boardwalk (5.8 s) | none | cut on the bag lifting to the mouth (match) |
| button | 8.6–12.2 | P-BUTTON: a seagull in the railings tilts its head, then snatches a chip (3.6 s); hold 10 f after the snatch | none | cut as the skater passes frame left |
| logo | 12.2–14.3 | P-CUT-BLACK (black 4 f) → P-WORDMARK-CARD (in 5 f, hold 1.7 s) | none | — |

CTA: `end_card`. Captions: none (no speech). Disclosure: the brand posts on its own account → none. SFX ledger: one shine on the wordmark settle. Fallbacks: none.

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] The format matches the §0.4 rule; the runtime is inside the format's target. (V-PROFILE, review)
- [ ] Every shot uses L-plate, or a fallback layout logged as FB-2. (V-LAYOUT)
- [ ] The end card share is 5–20% and ≤ 2.5 s. (V-LAYOUT, V-PROMISE)

**2. Hook**
- [ ] f0 is a plate in motion; no headline, label or logo before the first spoken word. (V-F0)
- [ ] The first cut lands at 1.2–3.0 s on an action. (V-CADENCE, review)
- [ ] Subject (and F-B screen, F-C product) established by 5.0 s; ST-1 thumbnail passes at 25%. (V-F0, review)

**3. Body and cadence**
- [ ] SC/10 s inside the format's band; no weight-1 gap > 8.0 s (F-A) or 6.5 s (F-B, F-C); nothing static > 3.0 s (F-B 4.5 s). (V-CADENCE)
- [ ] Shots 1.4–7.8 s; ≤ 2 long travelling shots; plate cadence untouched (no interpolation, no blending); no cut inside a line; cuts on action ±2 f; no jump cuts; screen direction kept. (review, R-1…R-12)
- [ ] The product turn is the longest held shot of the second half; the button follows within one shot. (review)
- [ ] No engine zoom, speed change, blend, regrade or stabilisation on any plate. (V-CAMERA, review)

**4. Captions**
- [ ] CS-1 skin: Plus Jakarta Sans 500 64 px pale yellow `#F6FA8C`, line height 1.25, y 1420, ≤ 2 lines × ≤ 24 chars, one line per chunk, hard on/off, lead 2 f. (V-CAPTION, V-TYPE)
- [ ] Everything the engine animates inside the world (packs, screen wordmark, label blink) steps on held frames; no smooth tweens inside the world. (review)
- [ ] CS-2 on every bright span; every caption ≥ 4.5:1. (V-TYPE)
- [ ] CS-3 wherever a face sits in y 1330–1520; no caption on eyes or mouth. (review)
- [ ] Script casing kept; profanity masked `inner`; names exact. (V-CAPTION)
- [ ] Captions hidden on the wordmark card. (review)

**5. Modules**
- [ ] §17 anchors (F-B): the screen rect constant ±4 px; screen content clipped to it; label words ≥ 52 px and ≥ 4.5:1; ≤ 3 labels, ≤ 2 words each. (V-EXC, V-TYPE)
- [ ] §17 anchors (all): the iris centre on the characters' faces. (review)
- [ ] §25: wordmark centred y 960, 600–700 px wide, on black, in 5 f (F-A under the iris snap), held 1.8–2.4 s, hard end; link line only with `link_bio`; disclosure ≥ 2.0 s when paid. (V-PROMISE, review)

**6. Truth and inserts**
- [ ] Every label word and product claim is in the claims list or the script. (review, NC-6)
- [ ] Pack shots and wordmark are the brand's files, unaltered. (review)
- [ ] Every third-party moment is creator-supplied or created and recorded. (V-INSERTS)

**7. Sound contract**
- [ ] Plate mix kept; pack cues only on reveals, the static and the wordmark (S1–S6); no meme sounds; no cue on a line. (S1–S6)
- [ ] −14 LUFS, true peak ≤ −1.5 dBTP. (review)

**8. End and export**
- [ ] The reel ends on the wordmark; no black tail > 0.2 s; the last sound ends ≤ 6 f after the hold. (review)
- [ ] 1080×1920, 30 fps CFR by frame duplication, BT.709. (review)

---

## Conditional modules (§16–§25)

§16 Frame template / chrome: OFF (`modules.chrome = false`): no persistent slots; the frame belongs to the plates.

### §17 Running state & anchored graphics `[COND: modules.anchors (F-B)] [DNA mechanics]`
`running_state`: OFF (no counters, clocks or ledgers).

**Anchors** (`anchors.mode: static`, fallback `static_near_target`, `face_clear_px: 40`). The plates are locked-off where it matters, so every anchor is a static rect or point written in the **anchor pass** (P8b) from sampled frames (first, middle, last frame of the plate at full resolution):

| Target | Used by | How it is written | Rule |
|---|---|---|---|
| `screen:<plate id>` | P-SCREEN-ON and everything inside it (F-B) | The screen face's inner rect `{x, y, w, h}` in output px (the glass, inside the bezel), plus `radius` = 6% of h | The plate must be locked-off: the rect measured on the first and last frame differs by ≤ 4 px, else the shot is not usable for the spot (pick another take, or FB-8). The rect must be ≥ 600 px wide; label size = clamp(0.15·h, 52, 72) |
| `faces:<plate id>` | P-IRIS-OUT centre (every format with an iris) | The midpoint of the visible characters' eyes on the iris hold frame | The porthole (r 510) contains every character's face |
| `faceband:<plate id>` | CS-3 switch (H7) | The y range covered by any character's eyes and mouth across the shot (sampled every 0.5 s) | Overlaps y 1330–1520 → CS-3; also overlaps y 1100–1260 → move the line |

**Tracked anchors (when a plate moves).** A screen plate with a camera move (a push-in on the TV), or a label that must stay on a product prop that moves inside a plate (a pack carried across the counter, F-A / F-C), uses a track instead of a static anchor. Request it at the plan stage (P8b), only for that shot's span: `veos track --project P --at <s> --look`, read the box off the grid, then `veos track --project P --id <screen|pack> --at <s> --box x,y,w,h --from <shot in> --to <shot out>` and check the preview. The screen scene gets `anchor: {track: "screen", scale_with: true, lost: "hold"}` and its `box` = the rect at `t_in`; a product label gets `anchor: {track: "pack", point: "top", offset: [0, -60], lost: "fade"}`, claims-list words only (H9). **Fallback:** more than 20 % of the span lost (V-ANCHOR), or the screen rect not readable as one rect, means that take cannot host the spot: pick a locked-off take (static anchor above) or FB-8; a product label without a usable track is dropped (the product stays a prop, the caption carries the word).

**V-STATE:** n/a. The screen rect check is E6's ±4 px slot tolerance (V-EXC).

§18 Data contract: OFF (`modules.data_figures = false`): no figures; numbers only as claims-list words.

§19 Evidence & citations: OFF (`modules.citations = false`): no sources or credit lines; third-party moments follow §12.5.

§20 Dialogue: OFF (`modules.dialogue = false`): character dialogue is part of the plate mix; one caption style for every character; no diarisation or angle map.

§21 Canvas camera: OFF (`modules.canvas_camera = false`, PV-5): the camera is physical and inside the plates.

§22 Ink & annotation layer: OFF (`modules.ink = false`): no marks over the handmade world (N7).

§23 Continuity: OFF (`modules.continuity = false`): continuity is the animators' (R-10); no engine morph chains or bookends.

§24 Series furniture: OFF (`modules.series = false`, VAR). A brand running a character series may switch it on later; its look is then one TC-legal line "Episode N" at x 64, y 150 for 2.0 s from 0.0 s, never a series card.

### §25 Sponsor, brand & end cards `[COND: modules.brand] [DNA look; VAR assets]`
**Wordmark end card (P-WORDMARK-CARD), every reel:**
| Property | Spec |
|---|---|
| Ground | `ink` `#000000`, full frame (L-endcard, W-black) |
| Wordmark | The brand's file (SH-5), white, centre (540, 960), width 648 px (TUNE 600–700), height by its aspect (≈ 250 px for an arched two-line mark) |
| Entry | F-A: fades in over 5 f under the iris snap, no black gap, no scale (v03 @30.20–30.37). F-B, F-C: 4 f of black after the cut, then the same 5 f fade |
| Hold | 1.8–2.4 s (F-C 1.6–2.0 s); total card time ≤ 2.5 s |
| Exit | Hard end on the last frame (no fade-out, no black tail > 0.2 s) |
| Extra lines | Only one: the link line (`link_bio`) or the stockist line, 40 px white at y 1180, in 8 f, 0.3 s after the wordmark settles. Never a tagline, URL card, QR, social icons or "follow us" |
| Type-set fallback (FB-5) | Fraunces 800 white: first word on a 48° arc (radius 520 px), second word straight below at 70%, rotated −6°, total 600–700 px wide, centre y 960 |

**Paid partnership (P-DISCLOSURE):** when an agency or creator posts the ad for the brand: "Paid partnership" (BV-14 wording), TC-legal 24 px white with a soft shadow, x 64, y 150, from 0.0 s for ≥ 2.0 s (default 2.5 s), fade in and out 6 f; plus the platform's own paid-partnership label (NC-12). It is the only text allowed in the hook besides an f0 caption under HA-14/HA-13.

**Screen wordmark (F-B):** the wordmark also appears once inside the screen spot (P-SCREEN-LINEUP), in its own colours over the sky.

**Rules:** the brand's colours appear only on label words, the screen sky and in the wordmark file; no sponsor card, no product card, no logo bug during the story.

---

## Part C. Exceptions and the non-overridable core

### C.1 Declared exceptions
| ID | Limits in this style | Scenes that set it |
|---|---|---|
| **E6** Hard swap | The screen rect constant ±4 px (`slot_tolerance_px: 4`); only content inside it swaps (hard swaps, label blink, stepped pack poses) | The F-B screen spot scene (`exception: "E6"`, the rect element marked `data-slot`) |

E1–E5 are not declared. A buyer may switch E6 off (VAR), which makes every in-screen swap a 4 f cross-fade and weakens the broadcast feel.

### C.2 Non-overridable core (applies in full)
NC-1 face never covered (here: character eyes and mouth, H7) · NC-2 no meaning text overlapping · NC-3 smooth motion · NC-4 legibility floors and 4.5:1 contrast · NC-5 IG UI bands · NC-6 truth (claims list only, H9) · NC-7 creator-owned media only (§12.5) · NC-8 audio · NC-9 determinism · NC-10 ≤ 4 bright hues (this style: 2 engine hues) · NC-12 disclosure (§25) · NC-13 quote integrity (captions verbatim from the script) · NC-14 redaction (any personal data visible on an in-world phone or letter is blurred).

---

## Part D. Personalisation

### D.1 What the buyer is asked at setup (≤ 4 questions, each with "keep the default")
| BV | Question | Feeds | Default |
|---|---|---|---|
| BV-01 | Brand name and handle | the type-set wordmark fallback, the glossary, the post title | {{BV-01.name|the brand}} · {{BV-01.handle|@yourbrand}} |
| BV-02 | One or two brand colours | `primary` (label words) then `accent` (screen sky), contrast-nudged | `#9C0012` / `#C9D9EE` |
| BV-05 | Speech language and caption language/script | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) | en}} → {{BV-05.captions | en / Latn}} |
| BV-08 | End: wordmark only, link in bio (with its line), in the post text, or none | `profile.cta.chosen`, P-LINK-LINE | {{BV-08.device|end_card}} |

**Defaulted, changeable later:** BV-03 fonts within the classes (§5.1); BV-07 captions full ↔ off; BV-09 formats enabled (all three); BV-14 disclosure wording ("Paid partnership"); BV-15 never-on-screen words; BV-16 wordmark and pack files (asked per reel, not at setup); BV-17 duration within the class.

### D.2 Lock summary
- **DNA:** source type, spine, presence, graphics, footage dependency, caption role, the no-text hook, the sketch structure, hard cuts, the iris/cut-to-black ending, the wordmark-on-black card, `zoom_policy: source_only`, no regrade, E6, CS-1 mechanics, label words ≤ 2.
- **TUNE:** caption size 58–72, weight 400–600, y 1360–1440, case as_spoken ↔ sentence, max 20–26 chars per line; label size 52–72; wordmark width 600–700 and y 900–1020; card hold 1.6–2.5 s; cadence ±15%; motion ±15%; duration micro ↔ short; energy calm ↔ balanced; comedy off ↔ light; fonts within each class.
- **VAR:** colours, language, CTA device and line, disclosure wording, formats enabled, sound cue moments and bed.
- **NICHE:** §6.4, §8.4 niche rows, §14, App. A.

### D.3 Per-reel adaptation (NICHE)
At P7 the editor writes this reel's subject → reveal pair into §6.4; at P5/P8 new plate or line types are mapped to existing patterns in §8.4; after the first approved reel of each format it replaces that format's §14 example; approved post titles are added to App. A; confirmed product and character names join the glossary.

---

## Part E. Template change log
| Version | Date | Change |
|---|---|---|
| v1 | 2026-10-06 | First draft from the three Chamberlain Coffee stop-motion ads (claymation and needle-felt). Kept as a brand stop-motion ad template (not Emma Chamberlain's vlog style) by Naman's decision |
| v1.1 | 2026-10-07 | Completeness pass (full-frame-rate motion): captions hard on/off; plate cadence table (§10.2a) and stepped in-world motion; screen spot ritual re-timed (label blink, hand-set / building packs, stepped wordmark); sensory trip 1.75 s with T-GLOW-IN / T-BLOOM-OUT; iris close 42 f, wordmark under the snap with no black gap; shot range 1.4–7.8 s, ≤ 2 long shots |
| v1.2 | 2026-10-07 | Engine built-ins: in-world motion uses `step_frames` (2 / 3) instead of hand quantising; T-BLOOM-OUT = warm `flash` + built-in `iris` (`reveal: "next"`, the orb collapse); T-GLOW-IN = warm `flash` + a radial `timeline.blur`; tracked anchors for a moving screen plate or a product label (§17); optional P-SCREEN-PACK3D (`fx.three`) inside the screen |

---

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D | D1–D8 |
| H, N | H1–H18; N1–N12 |
| E | E6 |
| W, L, G | W-plate, W-black; L-plate, L-endcard, L-plate-band, L-plate-blur; G-CUT, G-IRIS-END, G-BLACK-END, G-BAND |
| CS | CS-1 Soft dialogue, CS-2 Bright plate, CS-3 High band |
| HA, ST | HA-16 (default), HA-15, HA-14, HA-13; ST-1, ST-3, ST-6 (ST-5 informational) |
| P | 34 patterns (§8.3) |
| B | B-1–B-8 |
| T, R | T-CUT, T-SCREEN-SWAP, T-STATIC, T-IRIS, T-CUT-BLACK, T-CARD-IN; R-1–R-12 |
| SH, FB | SH-1–SH-9; FB-1–FB-9 |
| F | F-A Dialogue sketch, F-B Product broadcast, F-C Vignette |
| V | V-F0, V-CADENCE, V-CAPTION, V-TYPE, V-EXC, V-SAFE, V-LAYOUT, V-PROMISE, V-CAMERA, V-INSERTS, V-HUES, V-ONWORD |

---

## App. A Post-title and opener bank `[NICHE]`
On-screen headlines do not exist in this style; the bank is the post title (≤ 8 words) plus the f0 action and the first line it promises. Ten per format, for the two example niches. Archetype in brackets.

**F-A Dialogue sketch**
| # | Post title | f0 action | First line | Archetype |
|---|---|---|---|---|
| 1 | `[A]` the owl who couldn't sleep | an owl yawning on a branch at noon | "It's NOON and I'm still up." | HA-16 |
| 2 | `[A]` fox found the coldest drink in town | a fox fanning itself on hot pavement | "Is it just me or is the road melting?" | HA-16 |
| 3 | `[A]` where does your tea come from? | a felt teabag lowering itself into a cup | "Hold on, let me show you." | HA-15 |
| 4 | `[A]` the bear who'd never had it cold | a bear barista mid-pour | "You've NEVER had it cold?" | HA-14 |
| 5 | `[A]` squirrel vs monday | a squirrel skidding in on an acorn | "I'm LATE!" | HA-13 |
| 6 | `[B]` hamster, meet budget | a hamster counting coins in a jar | "Where did it all go?" | HA-16 |
| 7 | `[B]` the bird saving for a trip | a paper bird stacking coins into a nest | "Just one more coin…" | HA-16 |
| 8 | `[B]` cat finds out where her money goes | a cat at a laptop mid-sentence | "Okay, where did all my money go?" | HA-14 |
| 9 | `[B]` the phone that wouldn't stop buzzing | a clay phone sliding off a desk | "Not now, not NOW." | HA-15 |
| 10 | `[B]` four friends, one bill | four friends staring at a pizza bill | "So… who's got this?" | HA-16 |

**F-B Product broadcast**
| # | Post title | f0 action | Screen spot claim words (from the claims list) | Archetype |
|---|---|---|---|---|
| 1 | `[A]` game night needs snacks | over-the-shoulder of pups watching the match on TV | ORGANIC · SMOOTH | HA-16 |
| 2 | `[A]` the commercial everyone stopped for | a mouse remote-surfing channels | COLD-BREWED · LOW SUGAR | HA-16 |
| 3 | `[A]` breakfast tv just got better | a clay kid eating cereal in front of a TV | NEW FLAVOUR | HA-16 |
| 4 | `[A]` the billboard in snail town | snails sliding past a blank billboard | SLOW ROASTED | HA-16 |
| 5 | `[A]` shop window at midnight | a cat pressing its nose to a shop window | 3 FLAVOURS | HA-15 |
| 6 | `[B]` the ad the hamsters needed | hamster kid watching TV, parents counting coins | TRACKS EVERYTHING · ZERO FEES | HA-16 |
| 7 | `[B]` grandma's new favourite channel | a clay grandma knitting by the TV | EASY SETUP | HA-16 |
| 8 | `[B]` phone check at the bus stop | a commuter frog looking at a giant phone billboard | AUTO-SAVE | HA-16 |
| 9 | `[B]` rent day, but calm | a nervous clay character watching a wall calendar flip | BILL REMINDERS | HA-15 |
| 10 | `[B]` the family meeting | a family of mice gathered around a tiny laptop | SHARED GOALS | HA-16 |

**F-C Vignette**
| # | Post title | f0 action | Button | Archetype |
|---|---|---|---|---|
| 1 | `[A]` sunglasses, coffee, venice | a character mid-sip in sunglasses | a cat peeking from the bushes | HA-16 |
| 2 | `[A]` boardwalk snack run | a skater crunching a chip | a seagull steals one | HA-16 |
| 3 | `[A]` rainy day tea | steam curling from a cup by a rainy window | a snail shelters under the cup's saucer | HA-15 |
| 4 | `[A]` picnic for one | an ant unpacking a tiny basket | a ladybug sits down uninvited | HA-16 |
| 5 | `[A]` first sip of autumn | a bear lifting a cup among falling leaves | a leaf lands in the cup | HA-16 |
| 6 | `[B]` payday walk | a clay character strolling with a phone, smiling | a pigeon checks its own tiny phone | HA-16 |
| 7 | `[B]` coffee you can afford now | a character tapping a phone at a café counter | the barista winks | HA-16 |
| 8 | `[B]` the jar stays full | a jar of coins on a windowsill, a coin drops in | a sparrow adds one more | HA-15 |
| 9 | `[B]` holiday mode | a paper bird packing a suitcase | the suitcase won't close | HA-16 |
| 10 | `[B]` bills? sorted | a character swinging in a hammock, phone on chest | the phone buzzes; they don't move | HA-16 |

---

## App. B Evidence map (summary; full map and the unverified list in `evidence.md`)
| DNA element | Evidence |
|---|---|
| No text in the hook; the plate moves on f0 | v01 @0:00–0:03, v02 @0:00–0:02.8, v03 @0:00–0:01.1 |
| First cut 1.4–2.9 s on action | v01 2.92, v02 2.77, v03 1.42 |
| Captions pale yellow (`#F5FF7C`-`#F7FF7C`, audit) ~63 px, two lines, line 1 glyphs y 1420–1464, line 2 y 1499–1539 (v03 @0:01.5, @0:08), fade-in on the first word | v03 @0:01.17, @0:01–0:05, @0:08–0:11, @0:13–0:17 |
| Script casing kept ("GOT", "WOAH") | v03 @0:01, @0:21 |
| Profanity masked inner ("F**k") | v03 @0:29 |
| In-world TV spot: static, red condensed label words, pack shots, wordmark arc over a lineup | v02 @0:05–0:18 |
| Character close-up run | v02 @0:19.5–0:23.9 |
| Wide hold out | v02 @0:23.9–0:28.3 |
| Iris out on the characters, then the wordmark alone on black | v03 @0:28–0:32 |
| Non-sequitur button | v01 @0:09–0:12 (cat in the bushes) |
| Product as a prop from f0 | v01 @0:00 (cup in hand) |
