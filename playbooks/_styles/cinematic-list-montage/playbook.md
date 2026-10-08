# Cinematic List / Montage Style Playbook (template v1)

**Purpose.** You (Claude, the AI editor) receive {{BV-01.name|the creator}}'s talking-head take, optionally a bank of their own cinematic B-roll, plus the script. This playbook makes every reel look expensive and minimal: one cobalt title chip, one word on screen at a time in a heavy grotesk ↔ italic didone duet, list titles with a photo card floating above the head, or a moody cut-on-the-word montage of the creator's own footage. Input: SW-01 `talking_head` (both formats); F-B also needs the B-roll bank (§12).

**Style DNA** `[DNA]`. A calm, premium, almost silent-film look: a dark low-key room, a single saturated cobalt blue (`#2B35E8`, brandable) used only as a chip, a highlight box or a full-frame colour beat, and type that does all the talking. Captions are **one word at a time**, swapping with a 4-frame blur-in, and their size tells you how much the word matters: function words small, content words bigger in a heavy grotesk, the one word that carries the feeling huge in an italic didone. Titles are set in a condensed didone; numbers and list titles live **above the head**, never over the face. There are two formats of one style: **F-A list overlay** (one continuous take, zero cuts, "n. Title" + a hovering photo per item) and **F-B cinematic montage** (26–29 cuts per minute of the creator's own B-roll, cut on the word, with type frames and section numerals).

**Copy these 5 things** (the 5 load-bearing traits):
1. **One-word duet captions with an emphasis scale 1× / 1.6× / 2.5×** (heavy grotesk ↔ italic didone), 4-frame blur-in per word. → §5.3 (CS-1, CS-2), P-11, P-12.
2. **One blue.** A cobalt chip title at frame 0 (with a serif sub-line), cobalt highlight chips behind words, cobalt full-frame type beats. Nothing else is saturated except one proof accent. → §4, §5.2, P-01, P-13, P-15.
3. **Titles in a condensed didone, above the head.** F-A: "n. Title" in italic serif at y 250 with a photo card hovering at y 320–760 on top of the head. F-B: "No.n" section numerals and "step n" numerals. → §5.2, §7.2, P-05, P-08, P-09, P-10.
4. **Cinematic own-footage montage cut on the word** (F-B): back-of-head at the desk, hands, side profiles, silhouettes, macro eye, cut every 0.4–1.6 s in bursts, breathing on A-roll. → §3.2, §7.6, §9.3, P-20…P-27.
5. **Premium finish and a quoted CTA.** Shallow depth, dark grade, soft shadows, glass UI tiles and counter rings, and the CTA keyword set huge as `'{{BV-08.keyword|KEYWORD}}'` in a didone with curly quotes and a soft glow, after a community card. → §4.4, §10.5, §25, P-30, P-45, P-46.

### Directives (D1–D8) `[DNA]`
| # | Directive | Where |
|---|---|---|
| D1 | **One word on screen at a time.** Captions never show two words except a name, a number + unit, or the CS-3 chip pair. Size = importance. | §5.3, H11 |
| D2 | **One blue, and it means "read this".** Cobalt is the only saturated colour that carries type; the second bright hue per frame is either the proof accent, the red mistake word or the green level panel, never two of them. | §4, H13 |
| D3 | **Titles live above the head, the face is never covered.** Chip y 330–540, list title y 205–300, thumbnails y 320–760 and clamped 24 px above the face box. | §3.5, H7 |
| D4 | **F-A is a hook take + one continuous item take.** The only cut is the hidden one into item 1 (under the chip exit); after it the change comes from words, titles and thumbnails. | §7.6, H3 |
| D5 | **F-B cuts on the word, 26–29 cuts per minute, in bursts.** Every cut lands on a content-word onset (−2 f); bursts of 3–6 plates breathe on 2–6 s holds. | §7.6, §9.3, H5 |
| D6 | **Only the creator's own footage.** No stock, no fetched clips, no art the creator doesn't hold. Missing material becomes type frames, created cards or the list format. | §12, N3, H16 |
| D7 | **Calm, not hype.** No shakes, no meme sounds, no stickers, no bounces; eases are expo-out, overshoot 0. Energy comes from cut rhythm, size jumps, the 2× pull-out open and short full-frame blur pulses (T-11). | §10, N6 |
| D8 | **The CTA is a quote.** The comment keyword is shown in curly quotes in the didone with a glow, after the community card; it holds ≥ 1.5 s. | §6.7, §25 |

Buyer directives `BD1…` `[VAR]` are added here by the buyer; they may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches, formats) | ON |
| §1 | Procedure P1–P13 (+ F-B bank tagging and shot matching) | ON |
| §2 | Hard rules H1–H18, NEVER N1–N14, exceptions E1, E3 | ON |
| §3 | Worlds, layouts L-full / L-low / L-broll / L-type / L-split, stage moves, safe zones | ON |
| §4 | Colour roles, grades (B-roll only) | ON (§4.3 OFF: single theme) |
| §5 | Fonts, the chip headline, caption profiles CS-1…CS-4, other text | ON |
| §6 | Hooks: F-A HA-05, F-B HA-19, alternates, hook pairs, chip writing, CTA | ON |
| §7 | Structure (list / essay), markers SM-1…SM-3, rituals, cadence | ON |
| §8 | Families B-1…B-9, patterns P-01…P-48 (44 patterns), lookup | ON |
| §9 | Transitions T-01…T-10, grammar, montage shot grammar R-1…R-8 | ON |
| §10 | Motion tokens, zoom Z-1…Z-3, layers, finishing | ON |
| §11 | Sound contract | ON (minimal) |
| §12 | Setups, shot list SH-1…SH-9, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (F-A fitness, F-B finance, F-B fitness on a thin bank) | ON |
| §15 | QA checklist | ON |
| §16–§25 | Modules: §17 running state ON, §25 brand & end cards ON; §16, §18–§24 OFF | — |
| App. A | Headline & hook bank (10 per format) | ON |
| App. B | Evidence map (summary; full map in `evidence.md`) | ON |
| Parts C–F | Exceptions & core, personalisation, changes, IDs | ON |

Formats: **F-A List overlay** (default) · **F-B Cinematic montage**.

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile (base = F-A)
  source_type: talking_head
  presenter: {presence: anchor, share: [95, 100], max_absence_s: 0.5}
  spine: talking_head
  captions: {mode: full, role: primary, mute_policy: mute_safe}
  graphics: support
  duration: {class: short, target_s: [28, 48]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0}
  tone: {energy: calm, comedy: off, comedy_max: off}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A, F-B], default: F-A}
  footage_dependency: low
  cta: {devices: [comment_keyword, dm, link_bio, follow_save_stack, end_card], placement: end, chosen: comment_keyword}
  modules: {chrome: false, running_state: true, anchors: false, data_figures: false, citations: false,
            dialogue: false, canvas_camera: false, ink: false, continuity: false, series: false, brand: true}
# F-B overrides: presenter {presence: guest, share: [20, 50], max_absence_s: 10}, spine: audio,
#                duration {class: standard, target_s: [45, 76]}, footage_dependency: high
```

Why each switch has its value:
- **source_type: talking_head**, because the voice in all five reels is the presenter's own desk take (v03, v04 continuous; v01 @0:14, v02, v05 cut back to it). F-B is the same take with the creator's B-roll laid over it. (Coverage listed F-B as `narrated_footage`; the evidence shows a talking-head voice, and `talking_head` + `high` gives the honest "you + your own B-roll" card line. Deviation noted in Part E.)
- **presenter: anchor 95–100 % (F-A)**, because v03 and v04 never leave the face (0 cuts). **F-B guest 20–50 %**, because the face is on screen ≈ 20 % (v01), ≈ 35 % (v05), ≈ 50 % (v02); the longest absence is ≈ 9–10 s (v01 @0:04–0:13).
- **spine: talking_head (F-A) / audio (F-B)**: F-A edits around one take; F-B picks a picture per spoken word.
- **captions: full / primary / mute_safe**, because one-word captions are the strongest element in every frame (v01–v05) and the reels read without sound.
- **graphics: support**: chips, titles, thumbnails and type frames illustrate; the footage and the words carry the argument (B-roll 45–70 % in F-B; thumbnails overlay 55–85 % of F-A).
- **duration: short (F-A 28–48 s; v03 34 s, v04 29 s) / standard (F-B 45–76 s; v01 67 s, v02 55 s, v05 76 s)**.
- **language: en → en verbatim**, read from the captions (transcripts were unavailable: `unverified`). Hinglish combinations are supported in Latin script only, because the italic didone has no Devanagari italic (§5.5).
- **numbers: international**: the reels show "$150,000+" and view counts. BV-06 switches to Indian grouping and ₹ when the buyer speaks Hinglish.
- **tone: calm, comedy off**: no stickers, no meme cues, no shakes in any reel.
- **themes: single (cobalt)**: one blue in every reel.
- **footage_dependency: low (F-A) / high (F-B)**: F-A needs only the take (+ optional item stills); F-B needs 25–40 own clips.
- **cta: comment_keyword + community card**: "JOIN" / "ELITE" quoted keyword after a community card (v01 @1:04, v02 @0:51, v04 @0:25–0:28, v05). Follow (v03 "10. Follow for more"), DM and link-in-bio are the buyer's alternatives.
- **modules: running_state** (the counter ring, v03 @0:24–0:26, v05 @0:27, v01 @0:42) and **brand** (the community card + keyword quote). Everything else is absent from the evidence.

### 0.4 Formats `[DNA set; VAR enable]`
| Field | F-A "List overlay" (default) | F-B "Cinematic montage" |
|---|---|---|
| `when` | Numbered tips, ways, habits, tools or mistakes delivered in **one continuous take** (5–10 items, 28–48 s) | An idea, a process or a story told over **the creator's own cinematic B-roll** (3–7 sections, 45–76 s) |
| Profile overrides | — | presence guest [20, 50], max absence 10 s; spine audio; duration standard [45, 76]; footage high |
| Layouts | L-full (100 %), L-low (fallback) | L-full 20–50 %, L-broll 35–70 %, L-type 5–20 %, L-split 0–25 % |
| Cadence | weighted SC/10 s [18, 45], hook 8, cuts/min **[0, 2]** | weighted SC/10 s [20, 45], hook 9, cuts/min **[26, 29]**, median shot 1.0–1.6 s |
| Default hook | HA-05 promise chip | HA-19 mood montage |
| Structure | `list`, markers SM-1 "n. Title" | `essay`, markers SM-2 "No.n" (SM-3 "step n" for processes) |
| Captions | CS-1 micro duet (46 px, E3) | CS-2 duet (64 / 102 / 160 px) |
| Needs | "just you talking" (+ optional item photos) | "you + your own B-roll" (25–40 clips; < 12 clips → edit as F-A) |

**Shared DNA (what makes it one style):** the same cobalt chip title, the same italic-didone vs heavy-grotesk duet, the same one-word captions with blur-in, the same premium dark grade, the same `'KEYWORD'` quote CTA after a community card. The two formats share all 5 "Copy these" traits except trait 4 (montage), so they are one style (structure §0.4).

**Choosing the format per reel (decided):** the script enumerates 5–10 parallel items and the creator recorded one take → F-A. The script is an argument, a parable, a process with ≤ 7 steps, or a story, **and** the B-roll bank has ≥ 25 usable clips → F-B. A bank of 12–24 clips → F-B with FB-1 (degraded, say so at the checkpoint). Fewer than 12 clips → F-A, whatever the script (FB-1b).

### 0.5 Theme packs
OFF (`themes.policy = single`): one cobalt reel look; the buyer's BV-02 colours replace `primary` / `accent` directly.

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

This style's craft steps are **P6b the word-tier pass** (which word of each line is tier 2, the italic didone) and, in F-B, **P8b the burst map** (which words get a cut, which spans breathe).

1. **P1 Inventory.** `veos ingest` + `conform`: ffprobe every input, conform VFR to 30 fps CFR. Identify setups (§12.1): A-roll take(s), second angle, screen recordings, item stills, B-roll clips. Register every non-take file with `veos asset add <file> --origin creator` (videos become frame folders for `ctx.videoFrame`).
   - **P1b (F-B) B-roll bank tagging.** For every clip write a row in `plan/broll.json` (E-17 is not built yet: do it by hand from `veos sheet` contact strips): `{id: "BR-07", asset, shot: "SH-1…SH-6", subject, mood: calm|tense|warm|cold|bright, light: practical|daylight|night, motion: static|slow|fast, faces: true|false, usable: [[in, out], …], best_in}`. Count usable clips; pick the format branch (§0.4) and the fallback (FB-1 / FB-1b) **now**.
2. **P2 Prepare.** Matte (`veos matte`) only if the reel uses P-04 behind-head numeral (E1). Otherwise skip.
3. **P3 Transcribe** with word timestamps (`veos transcribe --script`). Captions are verbatim English (or the BV-05 combination). Apply the glossary (tool, brand and place names exact).
4. **P4 Segment.** F-A: `HOOK` (until the first ordinal word) → `ITEM-1…N` (each starts on its ordinal: "one", "first", "number two", "next") → `CTA`. F-B: `HOOK` (≤ 15 % of runtime) → `SEC-1…n` (each starts on its section word: "first", "the second thing", "step three", or a topic turn) → `CTA`. F-A: mark the take's in/out only; **no mid-take cuts** except ≤ 1 hidden fix per 30 s on an item boundary (H3).
5. **P5 Classify** every sentence with a line type from §8.4 and mark its **trigger word** (the noun, number or verb the visual lands on).
6. **P6 Tone-tag** every sentence: `explain` · `awe` · `hype` · `warn` · `win` · `cta` (§10, tone_treatment). There is no `mock`.
   - **P6b Word-tier pass.** For each sentence choose at most one **tier-2 word** (the word that carries the feeling or the claim: "hard", "alive", "elite", "never", "6 months"). Write it as `captions.overrides: {i, emph: true}`; switch off engine picks that land on weak words with `{i, emph: false}`. Budgets: F-A ≤ 1 tier-2 word per 6 s; F-B ≤ 3 per 10 s, never two adjacent words.
7. **P7 Hook plan.** Pick the archetype (§6: F-A HA-05, F-B HA-19 by default), write **3 hook variants** with chip text + sub-line (§6.5), and run the stopper tests (§6.1).
8. **P8 Visual plan.** One pattern per line (§8.4). F-A: the item visual for every item (thumbnail still, logo plate, screen thumb, counter ring). F-B: the picture for every word span.
   - **P8b (F-B) Burst map and shot matching.** Mark every content word as `cut` (a new plate starts on it), `hold` (the current picture continues) or `frame` (a type frame). Match a bank clip to every `cut` by subject and mood (§9.3 R-1…R-8); where no clip fits, use a type frame (P-14/P-15/P-16) or an A-roll punch (P-27), never a stranger's clip. Check the totals against 26–29 cuts per minute and a 1.0–1.6 s median shot before writing the beat sheet.
   - **State plan (§17):** every counter (P-30) gets its figure in `plan/figures.json` with the number's provenance (script or creator).
9. **P9 Beat sheet** (§13): one beat per trigger word, meeting §7.6.
10. **P10 SFX ledger** (§11, the bundled pack's S1–S6) and the transition map (§9).
11. **P11 Assets.** Collect the creator's files; build created substitutes for every third-party moment after asking once (§12.5); resolve fallbacks (§12.3) and list which were used.
12. **P12 Checkpoint** (§13.5), then **wait for approval.**
13. **P13 Build.** Write `plan/timeline.json` + `plan/scenes.js` act by act → `veos scenes-meta` → `veos measure --every 10` → `veos validate` (fix every failure) → test frames + `veos sheet` → QA (§15, at most 3 passes) → render.

**Module steps:** `running_state`: write each counter's figure (inputs, `from: script|creator`, the spoken word span) before P9. `brand`: confirm the community name, its one-line promise and 3–5 creator images for P-45; if a sponsor is present, the logo asset (creator-supplied) and the disclosure line (§25).

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The nine editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show what's being said; never fake facts; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| E-id | This style's limits (≤ registry) | DNA reason | Evidence |
|---|---|---|---|
| **E3 Quiet type** | Subtitles **44–53 px** only in CS-1 (F-A micro captions, 46 px) and CS-3 (hook chip duet, 48 px on a cobalt chip); weight ≥ 600; 1 line; ≤ 16 characters; contrast ≥ 7:1 on footage (CS-1) or ≥ 4.5:1 on the chip (CS-3). Labels 30–39 px only with `redundant: true` (never used by the default patterns). TC-display stays ≥ 40 px. If a CS-1 word measures < 7:1 (a light shirt), switch that span to CS-4 (54 px, no E3). | The micro one-word caption at the chest is how F-A stays quiet while the titles and thumbnails do the work; the hook chip duet is small words on cobalt chips | v03 @0:00–0:33, v04 @0:00–0:28 (≈ 30 px at 720 p = 44–48 px at 1080); v01 @0:00.5–0:03 (chip words) |
| **E1 Behind-subject type** | Only P-04 (the reel's number behind the head) and nothing else; `TC-display` ≥ 340 px; visible glyph area ≥ 65 %, first and last glyphs ≥ 50 % visible; ≤ 1 at a time and **≤ 1 per reel**; hold 0.6–4.5 s; hook only; requires the P2 matte. | A huge numeral half-hidden by the head is the premium depth cue of the hook | v05 @0:00–0:04 ("101" behind the head), v02 @0:04–0:05 ("BY STEP" behind the head) |

No other exception is declared: E2 (chaos), E4 (ambient field), E5 (edge bleed) and E6 (hard swap) are never used. Captions swap with a blur, never hard.

### 2.3 Style MUST rules (H1…)
- **H1 Frame 0.** F-A: the presenter mid-word under the Z-3 pull-out, the P-01 chip already moving in at f0 (first chip word readable by f6, complete by ≤ f24; or the static chip, fully typed at f0), first micro caption by f3. F-B: a moving creator plate (P-22 rack focus) or the A-roll + a one-word type element (P-19) at f0; the premise lands by 3.0 s. `check: V-F0`
- **H2 Cadence.** Captions are primary (weight 1.0). F-A: weighted SC 18–45 per 10 s, ≥ 3 non-caption SC per 10 s (title/thumbnail swaps, counters, keyword slams), max gap 1.2 s, nothing static > 2.5 s. F-B: weighted SC 20–45 per 10 s, max gap 1.0 s, max static 2.0 s. `check: V-CADENCE` (+ `review` for the non-caption count)
- **H3 F-A has one hidden cut.** The hook may be its own take: the cut into item 1 sits on the ordinal word, under the chip's exit (hard, or inside a T-11 blur pulse); measured v03 @0:02.83, v04 @0:03.70 (posture and prop change, same framing). Items 1…N are one continuous take with at most 1 more hidden fix per 30 s on an item boundary; cuts/min ≤ 2. No B-roll, no type frames, no stage changes except L-full ↔ L-low (fallback, once). `check: V-CADENCE`
- **H4 Headline chip limits.** ≤ 5 words, 1 line, ≤ 26 characters at 104 px (F-A serif) or ≤ 24 at 88 px (F-B grotesk), reads in ≤ 1.2 s, sub-line ≤ 6 words; the chip states the same promise the voice says in the first sentence; lifetime the hook only (2.5–5.0 s). `check: V-TITLE`
- **H5 F-B cut rhythm.** 26–29 cuts per minute (cutmap joins + every plate/type-frame entry marked in `timeline.transitions`), median shot 1.0–1.6 s, every cut on a content-word onset −2 f (±2 f), bursts of 3–6 plates at 0.4–1.0 s, a breath of 2–6 s after every burst, no single picture > 6 s in the body unless a graphic event lands on it every ≤ 2 s. `check: V-CADENCE` (+ `review` for bursts)
- **H6 On the word.** Titles, thumbnails, counters and type frames start 2 f before their trigger word and are fully on within ±5 f; a caption word appears ≤ 1 f before its onset. `check: V-ONWORD`
- **H7 Face rule.** Nothing is drawn over the face box (eyebrows to chin) at any z. Thumbnails, rings and tiles sit above it with their bottom edge ≤ face top − 24 px; captions sit at the chest (CS-1 cy 1130) and move below the chin if they would touch it. `check: V-FACE`
- **H8 Presence.** F-A: presenter share 95–100 %, never absent > 0.5 s. F-B: share 20–50 %, longest absence ≤ 10 s, and the face returns at least once per section. `check: V-PRESENCE`
- **H9 Promise integrity.** The chip's count equals the items shown (F-A) or the section numerals (F-B); every numeral counts up without gaps; the CTA keyword appears on screen exactly as spoken, ≥ 1.5 s. `check: V-PROMISE`
- **H10 Truth.** Every number on screen (counters, stats, "$150,000+"-type claims) comes from the script or the creator (`plan/figures.json`, `from: script|creator`); profile tiles show the creator's real profile only; no invented views, followers or results. `check: V-DATA`
- **H11 Captions.** One word per chunk (CS-1/CS-2/CS-4), ≤ 2 in CS-3; blur-in 4 f; tier sizes 1× / 1.6× / 2.5× exactly as the profile; glossary spellings exact; never a hand-written card. `check: V-CAPTION`
- **H12 Type floors.** Display ≥ 40 px, captions ≥ 54 px except the E3 spans (CS-1 46 px, CS-3 48 px), labels ≥ 40 px, handle and disclosure ≥ 22 px TC-legal; contrast ≥ 4.5:1 (3:1 for display ≥ 96 px). `check: V-TYPE`
- **H13 Hues.** ≤ 2 bright hues per frame: cobalt + at most one of {accent ring, bad red word, good green panel}. `check: V-HUES`
- **H14 Layouts by format.** F-A uses only L-full (L-low as the framing fallback); F-B uses L-full, L-broll, L-type, L-split within their shares. `check: V-LAYOUT`
- **H15 Camera.** Only Z-1 snap-punch (F-B), Z-2 push-in (F-B breaths, the CTA), Z-3 pull-out (hook f0, once); the F-A item take is otherwise locked off (measured scale 1.000 ± 0.001 per frame, v03, v04); never the same preset twice in a row; never two moves within 0.4 s; no shake, no crash zoom, no rotation. `check: V-CAMERA`
- **H16 Inserts.** Every third-party moment (a brand, a tool screen, someone's post, a famous image) is creator-supplied or a created substitute (§12.5), recorded in `plan/inserts.json`. `check: V-INSERTS`
- **H17 Dead air (by spine).** F-A (talking_head): ≤ 1 gap ≥ 150 ms per 15 s inside the take is allowed only as a natural breath; never trim it with a visible cut. F-B (audio): pauses ≤ 0.6 s; a pause may hold one plate or one type frame. `check: review`
- **H18 Audio and determinism.** −14 LUFS, true peak ≤ −1.5 dBTP, hard end ≤ 6 f after the last word (NC-8); every frame a pure function of its index, seeded randomness (NC-9). `check: review` (QA) + engine

### 2.4 NEVER list (N1…)
- **N1** Stock clichés: no stock B-roll, no "hustle" city time-lapses that aren't the creator's, no AI-generated scenes, no famous paintings or photos unless the creator holds them (then credited).
- **N2** A second saturated text colour: no yellow, orange, teal or pink type; cobalt is the only colour that carries words on footage (red only on a P-24 mono plate or paper, green only inside P-39).
- **N3** Anyone else's footage, logo file or screenshot fetched by Claude. Logos are creator-supplied files or names set in type (P-06).
- **N4** Text over the face, a thumbnail covering the eyes or brows, or a caption on the chin (v02 @0:02.5 and v05 @0:34 did this; the template does not).
- **N5** Shakes, crash zooms, rotation snaps, whip pans, glitch packs, RGB split, film burns, light-leak PNGs, bouncy overshoot pops.
- **N6** Stickers, emoji, memes, comedy SFX, marker scribbles.
- **N7** Two caption words of the same tier side by side as a sentence line (no 2–3-word subtitle cards).
- **N8** All-caps captions or titles. Case is as spoken; "STEP BY STEP"-style caps appear only as a P-17 stacked pair if spoken as the reel's thesis (≤ 1 per reel).
- **N9** A cut inside a word, or a cut on a function word ("the", "and", "of") in F-B.
- **N10** More than 3 grade events per reel, or the same treatment (B&W, red wash, blue wash, amber) twice in a row.
- **N12** Fake UI presented as real: invented dashboards, invented follower counts, a verification tick the creator doesn't have.
- **N13** A black tail > 0.2 s; an outro louder than the voice.
- **N14** Decoration for its own sake: every chip, card, frame and numeral shows the word being said.

Buyer additions `BN1…` `[VAR]` go here.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds (W-…)
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-room** | `footage` | The creator's own low-key room: dark top, practical lights (monitor glow, lamp), teal-green or warm grade as shot; shallow depth | All A-roll (F-A 100 %, F-B 20–50 %) | Hard cut (T-01) from a plate or frame; the world behind a hidden stage is `W-void` |
| **W-plate** (archive) | `archive` via L-broll | The creator's own cinematic B-roll clip, full bleed 1080×1920, as graded by the creator; optional B-roll grade events (§4.4) | F-B montage pictures (35–70 %) | Hard cut on a content word (T-01), rack-focus open (T-03) at f0, blur-through (T-02) between moods |
| **W-paper** | `paper` | Off-white `#F2F2F2` (`offwhite`), noise 0.03, vignette 0.12; words in cobalt (grotesk) or ink | Type frames for a thesis, a time span, a list of things (P-14, P-36, P-37) | T-04 colour-frame cut, on the word |
| **W-cobalt** | `card-world` | Cobalt `primary` full frame, noise 0.03 | A single decisive word, small, with an underline (P-15); the tilted phone card (P-38) | T-04 |
| **W-void** | `void` | Navy-black `night` `#0B1220`, noise 0.04, vignette 0.3 | A quiet one-word beat (P-16); the backdrop under every hidden-stage layout | T-04 |

### 3.2 Layout library (L-…)
| ID | Engine | Presenter rect | Graphic rect | Caption | Treatment | Share F-A / F-B |
|---|---|---|---|---|---|---|
| **L-full** | `full` | 0,0 → 1080×1920 (as shot) | above-head zone x 64–1016, y 300–780 (chip, title, thumbnail, ring, tiles) | CS-1 fixed y 1130 (F-A) / CS-2 fixed y 1000 (F-B; measured v02 @0:00.3–0:01.2: "Creating" / "videos" centred y ≈ 960–980 just under the chin, ≈ 160 px) | none | 95–100 % / 20–50 % |
| **L-low** | `low`, offset 120 | footage lowered 120 px (top revealed as the blurred copy) | above-head zone y 300–900 | CS-1 fixed y 1250 | none | fallback only (face top < 680) / — |
| **L-broll** | `hidden` (world W-void) + a full-bleed clip scene `kind: "broll"` | none | the plate fills 0,0 → 1080×1920 | CS-2 fixed y 960 | grade events per clip | — / 35–70 % |
| **L-type** | `hidden` + world W-paper / W-cobalt / W-void | none | the whole safe box | CS-2 fixed y 960, colour by background (light → `primary`, dark → `paper`) | none | — / 5–20 % |
| **L-split** | `stack`, seam_y 956 (measured: the hard seam sits at y ≈ 955, v01 @0:00.6–0:02.5), top `graphic`, bottom `footage`, hairline 0, a near-hard 8 px edge (the source seam is a hard cut line) | bottom band y 956–1920 (face cropped to the band) | top band 0,0 → 1080×956 (a second grade of the same shot, screen recording, UI card) | CS-2 centred on the seam, dy +8 (cy ≈ 964; v01 "Picture" 924–996, "period" chip 904–1036) | none | — / 0–25 % |

**Layout schedule (F-B) `[DNA]`:** L-broll runs come in bursts (3–6 plates, 0.4–1.0 s each) or single plates (1.0–2.5 s); every burst is followed by a breath of 2–6 s on L-full or on one plate; L-type beats last 0.5–1.5 s; L-split runs 2–6 s. Switch only on a content word (noun, number, verb, "but", "instead"). F-A never switches layout except once into L-low as a framing fix.

### 3.3 Stage moves (G-…)
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | **Cut to plate** | `stage: {t, layout: "L-broll", via: "cut"}` + the clip scene's `t_in` = the same t + a `transitions` marker `T-01`; 0 f | Every montage picture |
| **G-2** | **Cut back to face** | `stage: {t, layout: "L-full", via: "cut"}` + `T-01` marker; the clip scene ends at t; optional Z-1 on the landing word | The breath after a burst; "here's why", opinions, the CTA |
| **G-3** | **Cut to split** | `via: "cut"` into L-split and back (measured hard cut, v02 @0:16.08; the engine's slide-down is not used) + a `T-01` marker | A screen recording or UI while the creator keeps talking |
| **G-4** | **Colour-frame flip** | `stage → L-type` (cut) + `world: {t, world: "W-paper|W-cobalt|W-void"}` + `T-04` marker | A one-word or one-phrase type beat |
| **G-5** | **Lower for room (F-A fallback)** | `stage: {t: 0, layout: "L-low"}` for the whole reel (no mid-reel move) | The take is framed too high (face top < 680) for the 440 px thumbnail zone |

### 3.4 Layout diagrams
**F-A list frame (L-full)**
```
┌─────────────────────────┐ 0
│   (IG top UI, clear)    │ ← y 0–110
│  1. Edit with purpose   │ ← list title row, italic didone 92 px, cy 250 (glyphs y 205–300)
│     ┌─────────────┐     │ ← thumbnail card x 270–810, y 290–730, radius 10
│     │  item photo │     │   bottom edge clamped to face top − 24
│     │   (cover)   │     │
│     └─(head top)──┘     │ ← head top y 560–660 (the card overlaps hair/cap, never brows)
│        (  face  )       │ ← face box ≈ y 700–960
│          word           │ ← CS-1 micro caption, 46 px bold, cy 1130 (chest)
│        (torso)          │
│   (right UI column x>970 between y 900–1540)
└─────────────────────────┘ 1920   (no meaning text below y 1500)
```
**F-A / F-B hook (L-full)**
```
│  ┌───────────────────┐  │ ← P-01 cobalt chip, cy 400 (y ≈ 330–470), width = text + 56 ≤ 952
│  │ 10 ways to earn…  │  │
│  └───────────────────┘  │
│   as a video editor     │ ← sub-line, serif 56 px, cy 515
│       ( 10 behind )     │ ← optional P-04 numeral behind the head (E1), cy 560
```
**F-B plate frame (L-broll)**
```
┌─────────────────────────┐
│                         │
│   creator's own plate   │ ← full bleed, as graded
│                         │
│        alive.           │ ← CS-2 word at cy 960 (64 / 102 / 160 px by tier)
│                         │
│                         │
└─────────────────────────┘
```
**F-B split (L-split)**
```
┌─────────────────────────┐ 0
│  screen recording / UI  │ ← graphic band 0–900 (content inside y 140–860)
├─────────────────────────┤ 900 seam (60 px fade into the footage)
│          word           │ ← CS-2 on the seam, cy 972
│        ( face )         │ ← presenter band 900–1920, face ≈ y 1080–1330
└─────────────────────────┘ 1920
```

### 3.5 Safe zones and bands
- **Meaning-text box:** x 64–1016, y 110–1500 (NC-5); nothing meaningful in x > 970 between y 900 and 1540.
- **Headline band:** chip cy 400 (top ≥ 330), sub-line cy 515. **Title row band:** y 205–300 (cy 250). **Above-head zone:** y 300–780 for thumbnails, rings, tiles, the community card and the CTA keyword.
- **Caption bands:** F-A chest cy 1130 (L-low 1250); F-B A-roll cy 1000 (avoid_face pushes it down when the chin is lower), plates and type frames cy 960, split seam cy ≈ 964.
- **Side bands for step numerals (P-09):** left x 120–420, right x 640–960, at cy 1120, ≥ 40 px clear of the face box.

### 3.6 Presenter rules `[COND: presence ≠ none]`
- **Share and absence:** F-A 95–100 %, absence ≤ 0.5 s (never). F-B 20–50 %, absence ≤ 10 s; the face returns at least once per section and for the CTA.
- **Return:** always a hard cut (G-2) on a content word, optionally landing with Z-1 (F-B).
- **Framing:** F-A head top y 560–660 (the thumbnail zone needs ≥ 300 px above the brows); F-B head top y 360–580; face centre x 440–640 in both.
- **Behind the head:** only P-04 (E1), hook only. Thumbnails overlap hair or a cap, never the face box.

---

## §4 Colour, grades `[REQ] [roles' meanings DNA; brandable hex VAR; grades TUNE]`

### 4.1 Role palette
Brand colours: `primary` = {{BV-02.primary|#2B35E8}} (BV-02 colour 1), `accent` = {{BV-02.accent|#8B3CF0}} (BV-02 colour 2). The table lists the template defaults.

| Role | Hex | Its one job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` **Cobalt** | `#2B35E8` | The one blue: headline chip, highlight chips behind words, cobalt type frames, underlines, keyword words on paper | `paper` | 7.56:1 | **yes** (colour 1) |
| `accent` **Proof violet** | `#8B3CF0` | Proof and progress: the counter-ring gradient (`G-ring` `#E03BD8 → #8B3CF0 → #5B2BE8`), stat chips, the notification pill | `paper` | 5.25:1 | **yes** (colour 2) |
| `bad` **Mistake red** | `#D91F2A` | The one mistake word on a darkened B&W plate (P-24) or on paper; the "wrong way" red wash | `paper` | 5.02:1; red on `offwhite` 4.49 and on black 4.18 → display ≥ 96 px only | no (fixed) |
| `good` **Level green** | `#2CFF4E` | Level / done: the green meter panel (P-39), ticks | `ink` | 14.2:1 | no (fixed) |
| `ink` | `#0C0F0E` | Text on paper and on white cards | — | on offwhite 17.2:1 | TUNE |
| `paper` | `#FFFFFF` | Captions, titles, chip text on footage and cobalt | — | on `night` 18.7:1 | TUNE |
| `offwhite` | `#F2F2F2` | The paper type-frame world | — | cobalt on it 6.75:1 | TUNE |
| `cream` | `#ECE8D0` | Section numerals (P-08) and the CTA keyword (`G-keyword` `#FFFFFF → #ECE8D0 → #CFC79C`) | — | on dark footage ≥ 14:1 | TUNE |
| `night` | `#0B1220` | The void type-frame world and the backdrop under hidden stages | — | — | TUNE |

When the buyer brands `primary`, the engine nudges it in OKLCH lightness until `paper` text on it keeps ≥ 4.5:1; a light brand colour (yellow, mint) therefore darkens slightly. Cobalt frames (W-cobalt) follow `primary` automatically.

### 4.2 Meanings
- **Cobalt = read this.** It marks the promise (chip), the word being stressed (chip highlight) and the decisive single word (cobalt frame). It never fills a card that is not about a word.
- **Violet = proof.** Only numbers that prove progress (views, clients, kilos, savings) sit in the violet ring.
- **Red = the mistake; green = the level reached.** Fixed meanings; they never appear as decoration.
- **Cream = the ceremony.** Section numerals and the CTA keyword are cream-to-white, warmer than the caption white, so they read as "chapter" and "the word to type".
- **Brand colours** (a sponsor's) appear only inside P-48.
- **Footage keeps its own colour.** The creator's grade (teal-green room, warm window light) is the palette's background; never regrade the A-roll.

### 4.3 Theme packs
OFF (`themes.policy = single`).

### 4.4 Grades `[COND: grade events used]` (B-roll plates only, never the A-roll layer)
| ID | Filter (CSS on the clip scene) | Use | Evidence |
|---|---|---|---|
| **GR-bw** | `grayscale(1) contrast(1.15) brightness(0.92)` (P-24 adds brightness 0.6 and a 420 px radial black 55 % scrim behind the red word) | `warn`: the mistake, the cold truth | v01 @0:10–0:11 ("closer", "goal" in red on B&W) |
| **GR-red-wash** | `grayscale(1) sepia(1) hue-rotate(-50deg) saturate(3.2) brightness(0.8)` | the "before / wrong" half of a split twin; a tense beat | v01 @0:00–0:03 (bottom half), @0:48–0:54 |
| **GR-blue-wash** | `grayscale(1) sepia(1) hue-rotate(175deg) saturate(3.0) brightness(0.85)` | the "after / calm" half of a split twin; night work | v01 @0:00–0:08 (top half) |
| **GR-amber** | `sepia(0.45) saturate(1.25) brightness(0.95)` | warm memory, golden-hour story beats | v01 @0:18–0:20 (hazy skyline) |

- **Events:** ≤ 3 grade events per reel (a split twin counts as 1); never the same treatment twice in a row; never on the A-roll (no engine grade layer for footage yet, and the room grade is DNA).
- **Clip treatments:** `bw`, `red_wash`, `blue_wash`, `amber`, `twin`; `no_repeat: true`.
- **Footage grade:** low-key (audit 2026-10): gain 0.82, gamma 1.08, saturation 0.85, vignette 0.3 (`grades.footage`). The source A-roll is dark (walls #1C2214, v04 @0:08), and the white serif titles, chip sub-line and cream keyword depend on it. Apply it when the buyer's room is brighter than mid-grey behind the title zone (y 150–780); a footage already graded low-key is used as is.

### 4.5 Rules
- **≤ 2 bright hues per frame** (`max_bright_per_frame: 2`): cobalt + one of {violet ring, red word, green panel}. On a paper frame, cobalt alone.
- Coloured text on the paper world is cobalt (6.75:1) or red at ≥ 96 px; never violet or green text on paper.
- Cobalt text on footage is never used (it disappears on dark plates); on footage, cobalt is a **fill** behind white text.
- No glow except the CTA keyword (24 px cream glow) and the section numeral (30 px cream glow at 35 %).
- **Must match `tokens.json`.**

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within the class]`
| Slot | Family | Weights | Font class (the TUNE boundary) | Used for |
|---|---|---|---|---|
| `display` | **Inter Tight** | 600–800 | tight grotesk, tracking −2 to −4 % | tier-1 caption words, F-A tier-2 words, the F-B chip, type-frame words, stacked pair |
| `body` | **Inter Tight** | 600 | tight grotesk 500–700 | tier-0 caption words, micro captions |
| `serif` | **Instrument Serif** (regular + italic) | 400 | condensed high-contrast serif with a true italic (didone feel) | F-B tier-2 caption words (italic), the F-A chip (upright), sub-line, list titles (italic), "No.n" (upright), "step n" (italic) |
| `didone` | **Instrument Serif** | 400 | condensed high-contrast serif (Bodoni Moda allowed as a TUNE swap) | the CTA keyword quote P-46 at tracking −0.03 (the source's 'JOIN' is a condensed didone with touching letters, which Instrument Serif matches and Bodoni Moda does not) |
| `numeric` | **Inter Tight** | 600 | tight grotesk, tabular figures | counter values |
| `ui` | **Inter Tight** | 500–600 | tight grotesk | profile pill, UI cards, labels, handle, disclosure |

Bundled fonts only. A brand wordmark is an image asset from the creator, never a font. There is no Devanagari italic, so Devanagari captions are not offered (§5.5).

### 5.2 Headline element: the cobalt chip `[DNA recipe; NICHE text]`
| Property | Spec |
|---|---|
| Kind | `chip` (`type.headline.kind`); scene `kind: "chip"`, z10, `text_class: "TC-display"` |
| Fill | `primary` cobalt, opacity 1, radius 4 px, padding 18 × 28 px, no stroke, shadow `0 10 30 rgba(0,0,0,.35)` |
| Text | F-A: **Instrument Serif 400, 104 px**, tracking −1 %, `paper`, sentence case. F-B (and any chip containing a word ≥ 11 letters): **Inter Tight 700, 88 px**, tracking −3.5 % |
| Position | centred x 540, **cy 400** (top edge ≈ 330), width = text + 56 px, max 952 px; never 2 lines (shorten the text instead) |
| Words / read | ≤ 5 words, ≤ 26 characters (serif) / ≤ 24 (grotesk); reads in ≤ 1.2 s |
| Sub-line | Instrument Serif 400, **56 px**, `paper`, cy 515, shadow `0 2 10 rgba(0,0,0,.45)`; the rest of the spoken promise (≤ 6 words), **typed letter by letter at ≈ 0.8 char/f, paced to the voice** (v03 @0:00.08–0:00.50: "y" → "you" → "you n" → "you need"), no blur. Drawn **inside the chip scene** (one element for G2) |
| f0 behaviour (default: swing-in typed) | Measured v04 @0:00.08–0:00.76, v05 @0:00.12–0:00.68: at f0 the chip is entering from the **top-left**, rotated ≈ −12° and ≈ 300 px up-left of rest; it slides and straightens to rest over **12–14 f** (expo-out; v05 rests at −3°), while the text **types L → R at ≈ 1 char/f** (the chip's width tracks the text); first word readable by f6, complete by f20–24. No scale change, no overshoot. Runs under the Z-3 pull-out |
| Alternate entry | **Static** (v03 @0:00.00–0:02.83): fully typed and still from f0 (pick it when the f0 thumbnail must read, ST-1). P-02 (grotesk) uses the same swing-in |
| Life | No pulse; the chip holds still (calm). The sub-line types under it |
| Lifetime | the hook: 2.5–5.0 s (v03 2.8 s, v04 3.7 s, v05 4.5 s) |
| Exit | **Hard out on the cut** into item 1 (v03 @0:02.83), or inside a **T-11 blur pulse** (v04 @0:03.58–0:03.74: the whole frame blurs over 4 f, cut, the new take + "1. Title" de-blur over 5 f). Never a separate fly-off |

Examples (niche-neutral): "10 ways to earn money" + "as a freelance designer"; "7 habits that fixed my training" + "you can start today"; "Saving money 101" + "for your first salary".

### 5.3 Caption system profiles (CS-…) `[DNA mechanics; fonts TUNE; language VAR]`
All four profiles extend `lib:antlon` (the engine caption library) and use the **duet** variant: tier 0 = function words, tier 1 = content words (score ≥ `mid_score`, or a number), tier 2 = the emphasised word.

| Group | **CS-1 Micro duet** (F-A default) | **CS-2 Montage duet** (F-B default; all L-broll / L-type / L-split) | **CS-3 Chip duet** (time-range override) | **CS-4 Micro safe** (F-A fallback) |
|---|---|---|---|---|
| Mode | full / primary / mute_safe | same | same | same |
| Chunking | `unit: word`, 1 word; ≤ 16 chars; 1 line; never split names, numbers + units | 1 word; ≤ 14 chars; 1 line | 1–2 words (a noun pair may share a chip); ≤ 16 chars | as CS-1 |
| Timing | lead 1 f; min hold 0.2 s/word; tail 0.12 s; max hold 1.2 s; pause hold 0 | same | lead 1 f; tail 0.1 s; max hold 1.0 s | as CS-1 |
| Swap (outgoing word: hard out) | `blur`, 2 f, 6 px (measured: the micro word reads as a hard swap at 25 fps, v04 @0:00.16, v05 @0:00.20) | **`flicker`**, 5 f, `pattern: [0.4, 0.8, 0.4, 0.8, 1]` (measured **flicker-in**: opacity ≈ 0.4 / 0.8 / 0.4 / 0.8 / 1 over 5 f, v02 @0:00.64–0:00.84) | `blur`, 3 f, 8 px; on the hook plate each new chip shows as a **1-frame empty cobalt chip** before its word (v01 @0:00.00, 0:00.16, 0:00.56) | as CS-1 |
| Skin (tier 0) | Inter Tight 700, **46 px** (measured v04 @0:08 "businesses" ascender band 34 px; centre y 1136; bold), TC-subtitle (E3), as spoken, tracking −2 %, `paper`, shadow `0 2 10 rgba(0,0,0,.55)`, no container | Inter Tight 600, **64 px**, tracking −3 %, `paper`, shadow `0 2 12 rgba(0,0,0,.45)` | Inter Tight 600, **48 px**, `paper`, on a **cobalt chip** (fill `primary`, radius 3, padding 2 × 10) (E3 on a container) | Inter Tight 600, **54 px**, shadow `0 2 14 rgba(0,0,0,.75)` |
| Tier 1 (1.6×) | numbers only (`mid_score` 3.0): Inter Tight 700, 70 px | content words (`mid_score` 1.45): **Inter Tight 700, 102 px** | Inter Tight 700, 77 px, no chip | numbers only: 86 px |
| Tier 2 (2.5×) | the planned keyword: **Inter Tight 800, 110 px** | the feeling word: **Instrument Serif italic 400, 160 px** | Instrument Serif italic, 120 px, no chip | Inter Tight 800, 135 px |
| Position | fixed y **1130** (L-full), 1250 (L-low); centred; `avoid_face` | fixed y **1000** (L-full), **960** (L-broll, L-type), seam **+8** (L-split) | fixed y 1150 (L-full) / 960 (L-broll) | as CS-1 |
| Colour by background | — | light → `primary` (cobalt on paper), dark → `paper` | — | — |
| Emphasis | `size_tier`; select number, glossary, topic noun; min score 1.8; **max 0.15 / s**; never stop-words | `size_tier`; select number, glossary, name, topic noun, key verb; min score 1.6; **max 0.3 / s**; never stop-words | max 0.5 / s | as CS-1 |
| Hide | under z8 scenes; during declared transitions | same | same | same |
| Language | Latn; keep English terms verbatim; no spelling normalisation; profanity masked `inner` (S**T), on by default; glossary from the creator | same | same | same |

**Duet variant (the style's signature)** `[DNA]`
| Tier | Which words | F-A (CS-1) | F-B (CS-2) | Size jump |
|---|---|---|---|---|
| 0 | function words, and content words below `mid_score` | micro grotesk 700 46 px | grotesk 600, 64 px | 1× |
| 1 | content words (F-B) / numbers (F-A) | grotesk 700, 70 px | grotesk 700, 102 px | 1.6× |
| 2 | the one word per line that carries the feeling or the claim (planner `emph: true`, else the engine's best score) | grotesk 800, 110 px | **Instrument Serif italic, 160 px** | 2.5× |

**Assignment rule (P6b):** tier 2 goes to the word you would underline if you could underline only one: the adjective of the judgement ("hard", "alive", "elite"), the contrarian verb ("stop", "never"), the time or quantity that is the point ("6 months", "2 years"), or the noun the reel is about. Never a stop-word, never two tier-2 words within 0.5 s, never the first word of a sentence unless it is the point.

**When to use CS-3:** `captions.overrides: [{t: [a, b], profile: "CS-3"}]` for the F-B hook span (≤ 3.0 s) and at most 2 more 1-second spans per reel (P-13). Never in the F-A body.

**When to use CS-4:** V-TYPE reports a CS-1 caption below 7:1 (a light top, a bright wall at chest height). Switch the reel (or the failing spans) to CS-4 with `captions.profile: "CS-4"` or a range override.

### 5.4 Other text systems
| Element | Class | Recipe | Hold |
|---|---|---|---|
| List title row "n. Title" (SM-1, P-10) | TC-display | Instrument Serif **italic** 400, **92 px**, tracking −2 %, `paper`, shadow `0 2 12 rgba(0,0,0,.4)`, centred x 540, **cy 250**, ≤ 26 characters including "n. " | the whole item |
| Section numeral "No.n" (SM-2, P-08) | TC-display | Instrument Serif 400 upright, **300 px**, `cream`, glow `0 0 30 rgba(236,232,208,.35)`, cy 480; sub-line Inter Tight 600 **56 px** `paper` at cy 720 | 1.2–2.0 s |
| Step numeral "step n" (SM-3, P-09) | TC-display | "step" Instrument Serif italic **72 px** + numeral Instrument Serif italic **260–320 px**, `paper`, flanking the body at cy 1120 (word centred x 330, numeral centred x 720) | 1.0–1.5 s |
| Type-frame word (P-14/P-15/P-16) | caption or TC-display | the CS-2 caption itself (cobalt on paper, white on cobalt and void); a planned big word as a z8 scene: Inter Tight 700 110–170 px or Instrument Serif italic 120–180 px | 0.5–1.5 s |
| Behind-head numeral (P-04) | TC-display, E1 | Instrument Serif italic 340–420 px, `paper` at 85 % opacity, cy 560, `behind: true` | 0.6–4.5 s |
| Stacked pair (P-17) | TC-display | Inter Tight 800, 110–130 px, line height 0.86, tracking −4 %, two lines centred at cy 500 | ≤ 1.5 s |
| Counter value / unit (P-30) | TC-display / TC-label | Inter Tight 600 **80 px** / 500 **44 px** | the beat |
| Card title / line (P-45) | TC-label | Instrument Serif 400 **64 px** `ink` / Inter Tight 500 **40 px** `#3A3A3A` (11.4:1 on white) | ≥ 2.0 s |
| Profile name / handle (P-31, P-47) | TC-label / TC-legal | Inter Tight 600 40 px / 500 30 px | ≥ 1.5 s |
| CTA keyword (P-46) | TC-display | Instrument Serif 400 upright, **260–360 px** (fit to 860 px; measured 'JOIN' cap height ≈ 237 px, width ≈ 700 px incl. quotes, v04 @0:28.4), tracking −0.03 (letters nearly touch; never letter-spaced), `G-keyword` fill, 24 px glow, curly quotes ‘ ’, cy 450 (v01 @1:05 sits at ≈ 510) | ≥ 1.5 s, to the end |
| Disclosure / credit | TC-legal | Inter Tight 500, 24 px, `paper` at 80 % | ≥ 2.0 s |

### 5.5 Language and number rules
- **Spelling:** English words and brand / tool names exact (glossary). Captions verbatim, as spoken, punctuation kept ("you." "attention." carry their full stop, as in the evidence).
- **Supported combinations:** {{BV-05.speech|en}} speech → {{BV-05.captions|en}} captions. The template supports en → en; Hinglish → Hinglish (Latin script); Hinglish → English (translated). Devanagari captions are not supported: no italic didone exists for Devanagari and the duet would lose its tier-2 voice.
- **Numbers (SW-08):** default international ("242,409", "$150,000+"), compact K/M for counts ≥ 10,000 in rings ("212K views"). With Hinglish (BV-05), BV-06 switches to Indian grouping and ₹ ("₹1,20,000", "1.2L"). Every number on screen goes through `ctx.fmtNum` (V-NUMFMT).
- **Case:** as spoken; no all-caps (N8). Titles in sentence case. Numerals as digits in titles and chips ("10 ways", "No.2", "step 3").

---

## §6 Hook system `[REQ]`

### 6.1 Stopper tests
| Test | F-A value | F-B value |
|---|---|---|
| ST-1 Thumbnail (f0 at 25 %) | the chip reads at 26 px (104 px × 0.25) and the face is visible | n/a (mood open) |
| ST-2 Mute (first 3 s) | chip + sub-line + micro captions tell the promise | the premise sentence is on screen word by word by 3.0 s |
| ST-3 Motion at f0 | the chip settling + live presenter | the rack-focus plate + the opening word's blur-in |
| ST-4 Read time | chip ≤ 1.2 s (≤ 5 words) | — |
| ST-5 Change count 0–3 s | ≥ 8 weighted SC | ≥ 9 weighted SC |
| ST-6 Payoff-by | chip readable by 0.7 s; item 1 starts by 4.0 s | premise by 3.0 s; the face or the first section by 6.0 s |

### 6.2 Default archetypes `[DNA]`
**F-A: HA-05 Promise chip** (from v03, v04)

| t (s) | Beat | Visual | Caption | Camera | Cue moment (pack) |
|---|---|---|---|---|---|
| **f0** | Stopper | Presenter mid-sentence (L-full), motion-blurred and ≈ 2× tight. **P-01 chip** swinging in from the top-left and typing (rest by f13, text complete by ≈ f22). Optional **P-04** numeral (the chip's number) behind the head, present from f0 | first word in CS-1 (micro) by f3 | **Z-3 pull-out** 2.0 → 1.0 over 50 f, expo-out (v04 ≈ 2.3×, v05 1.6×) | hook: one whoosh/riser end on f0 |
| 0.1–1.4 | The promise | **Sub-line** types letter by letter under the chip at cy 515 (the rest of the promise: "you need to lock in today") | micro, one per word | pull-out settling | — |
| 1.4–2.6 | Stakes | Chip + sub-line hold; the presenter adds the stake ("each one better than the last") | micro; one tier-2 word allowed | — | — |
| 2.6–4.0 | Item 1 | On the ordinal word: **T-11 blur pulse** (4 f) → hidden cut to the item take (H3) → chip gone; **P-10** "1. Title" + **P-05** thumbnail on with the cut, de-blurring 5 f | micro | — | list cue (first use) |

Payoff: the chip is readable at f0 (≤ 0.7 s); item 1 starts ≤ 4.0 s (v03 2.83 s, v04 4.0 s).

**F-B: HA-19 Mood montage** (from v01, v05)

| t (s) | Beat | Visual | Caption | Camera / move | Cue moment |
|---|---|---|---|---|---|
| **f0** | Stopper | **P-22 rack-focus open** on the strongest plate (SH-1 back-of-head at the glowing desk, or SH-4 silhouette): held defocused (≈ 14 px) under the opening words, snapping sharp through a 1-frame T-11 pulse on the subject word, then a slow pull-out ≈ 1.4 %/f (v01 @0:00.00–0:00.68); or de-blurred over 12 f under the Z-3 pull-out when the hook opens on the face (v05, v02). **P-19 opening word** ("Picture this", "Here's") at cy 960, Inter Tight 700 96 px, already 60 % into its blur-in at f0 | captions hidden until P-19 ends | — | hook: one low hit or a riser end on f0 |
| 0.5–1.0 | The subject | **P-13 chip duet** (CS-3): the subject noun pair on a cobalt chip ("2 lifters"), or **P-23 split twin** of the same plate (blue top / red bottom, caption on the seam) | CS-3 | — | — |
| 1.0–3.0 | The premise | 1–3 cuts on content words (**P-21** mini-burst: same location, different angles); the premise sentence completes ("…over a period of 6 months") with one tier-2 word ("6 months" in italic) | CS-3 → CS-2 at 3.0 s | — | transitions: one whoosh on the burst start only |
| 3.0–6.0 | The turn | **G-2 cut back to the face** for the turn line ("Here's why.") in tier 2, or a **P-14 paper frame** for the thesis word | CS-2 | optional Z-1 on the landing word | — |

Payoff: the premise is complete on screen by 3.0 s; the creator's face or the first section numeral by 6.0 s.

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`
| ID | Name | Short table | Format | Example (fitness) | Example (finance) |
|---|---|---|---|---|---|
| **HA-12** | Thesis typography | f0 **W-paper** frame; the thesis builds in 3–4 type beats ≤ 3 s (cobalt grotesk on paper, the last beat on a cobalt chip: "comes down" → "to 3 things"); cut to the face ≤ 3.5 s | F-B | "Getting strong / comes down / **to 3 things**" | "Being broke / comes down / **to 2 habits**" |
| **HA-05** | Promise chip | as F-A, with **P-02 typed grotesk chip** + **P-04** numeral behind the head (v05 "Editing better videos" + "101") | F-B | chip "Training better 101" + "101" behind | chip "Saving money 101" + "101" behind |
| **HA-02** | Headline + proof | f0 the face + a CS-2 tier-1 first word ("Building"); by 0.7 s **P-35 card wall** of the creator's own results scrolls over the head as proof; a hard cut with Z-1 at ≈ 2.4 s to a tight face for the turn word ("isn't") | F-B | "Building muscle after 30 / isn't hard" + wall of own progress photos | "Saving $10K in a year / isn't hard" + wall of own budget screenshots |
| **HA-14** | Cold authority | f0 the face mid-sentence with a tier-1/2 caption at f0 (no chip); the strongest picture (a plate or a punch) by 1.0 s | F-B | "Most people **quit** in week 3" | "Your salary isn't the **problem**" |
| **HA-19** | Mood montage | the F-B default (§6.2) | F-B | "Picture this: two lifters, same program…" | "Picture this: two friends, same salary…" |
F-A uses only HA-05 (the chip is its stopper); a 1.5–2.0 s HA-12 paper cold open is the one exception and needs an approved checkpoint because it adds a cut.

### 6.4 Hook pairs by topic `[NICHE: example]`
Pair types follow the archetype (structure §6.4). Two example niches: **fitness coaching** and **personal finance**. The editor appends one row per reel (Part D.6).

| Topic | Archetype | Pair type | Promise / premise | Proof / the scene that carries it |
|---|---|---|---|---|
| Gym habits (fitness) | HA-05 | promise → proof | "7 gym habits / that actually build muscle" | item 1 photo (own training log) lands by 3.5 s |
| Fat-loss mistakes (fitness) | HA-05 | promise → proof | "5 fat loss mistakes / you're making today" | item 1 thumbnail by 4.0 s |
| Two lifters (fitness) | HA-19 | thesis → scene promise | "Two lifters train for 6 months; only one improves" | SH-1 back-of-head at the rack, split twin blue / red |
| Consistency (fitness) | HA-12 | thesis → scene promise | "Getting strong comes down to 3 things" | paper frames, then "No.1" over a gym plate |
| Side income (finance) | HA-05 | promise → proof | "10 ways to earn money / as a freelancer" | item 1 logo plate (the platform's name set in type) |
| Budgeting (finance) | HA-05 | promise → proof | "Saving money 101 / for your first salary" | P-04 "101" behind the head; item 1 photo |
| Two friends (finance) | HA-19 | thesis → scene promise | "Two friends earn the same; one is broke in a year" | SH-2 hands counting cash / SH-1 at the laptop, split twin |
| Debt (finance) | HA-14 | claim → evidence | "Your salary isn't the problem" | tight face, then a P-30 ring with the creator's own savings figure |

### 6.5 Chip writing `[DNA formula; NICHE examples]`
**Formula:** `[number or "Topic 101"] + [the thing]`, with `[for whom / the result]` on the sub-line. ≤ 5 words in the chip, ≤ 6 in the sub-line, sentence case, no emoji, no CAPS.

| Template | Chip | Sub-line |
|---|---|---|
| Count + thing | "10 ways to earn money" | "as a [role]" |
| Rated count | "10/10 [niche] habits" | "you need to lock in today" |
| 101 | "[Skill] better 101" | — (P-04 "101" behind the head) |
| Thesis claim (F-B HA-02 / HA-14) | "[Result] in [year] isn't hard" | — |
| Mistakes | "5 [niche] mistakes" | "I wish I knew at [age]" |

- **Write 3 chips and pick by ST-1 and ST-4.** The chip must be spoken: the first sentence contains the chip's words or their exact meaning.
- **Banned:** hype words ("insane", "game-changing"), questions in the chip, numbers that don't match the items (H9), more than 5 words, two lines.

### 6.6 Hook sound
Pointer to §11: the hook may carry **one** cue (an f0 soft hit or a riser end); the music bed runs from f0 under the voice; no cue on caption swaps.

### 6.7 CTA `[DNA device set; VAR values]`
The reel's device is {{BV-08.device|comment keyword}} and its keyword is `'{{BV-08.keyword|KEYWORD}}'`. The CTA lives in the last 4–9 s.

| Device | Spoken pattern | On-screen element | Hold | Where |
|---|---|---|---|---|
| `comment_keyword` (default) | "I built a [community / guide]… comment [KEYWORD] and I'll send it to you" | **P-17** stacked pair on the deliverable ("private community", ≤ 1.5 s) → **P-45 community card** above the head (F-A: as the last item's thumbnail under "n. Join [name]") → **P-46** the keyword as a cream didone quote at cy 450 | card ≥ 2.0 s; keyword ≥ 1.5 s, to the end | end; nothing new for 0.4 s before the keyword word |
| `dm` | "DM me [KEYWORD]" | P-46 with a small "DM" label (Inter Tight 600 40 px) under the quote | ≥ 1.5 s | end |
| `link_bio` | "It's in my bio" | P-45 card + P-31 profile pill with "link in bio" (40 px) | ≥ 1.5 s | end |
| `follow_save_stack` | "Follow for more" | F-A last item "n. Follow for more" + **P-47** follow pill (avatar + name + handle) | ≥ 1.5 s | end (v03) |
| `end_card` | the community / lead magnet named | P-45 alone | ≤ 4 s | end |

Silence before the CTA: no new pattern for 0.4 s before the keyword word, and no SFX cue in the 1.0 s before the CTA section's first word (the pack's S4). End cards are specified in §25.

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type (one per format)
| Format | Type | Arc | Evidence |
|---|---|---|---|
| F-A | `list` | chip promise (hook) → items 1…N in the identical ritual, ascending → the last item is the CTA ("n. Follow for more" / "n. Join [community]") → keyword quote | v03 (10 habits, item 10 = follow), v04 (10 ways, item 10 = join) |
| F-B | `essay` | mood premise (hook) → the turn ("Here's why.") → 2–7 sections, each opened by a marker, each ending on the creator's face → payoff line → deliverable → keyword quote | v01 (parable, "No.2"), v02 (7 steps), v05 (3 things, "No.1–No.3") |

### 7.2 Markers (SM-…) `[DNA]`
| ID | Marker | Format | Recipe |
|---|---|---|---|
| **SM-1** | **"n. Title" row** (P-10) | F-A | Italic didone 92 px at cy 250, one per item, ascending 1…N; the title is the item's name in ≤ 4 words |
| **SM-2** | **"No.n" section numeral card** (P-08) | F-B, argument / "N things" scripts | Cream upright didone 300 px over a fresh plate (or the A-roll top band), sub-line = the section's name as spoken |
| **SM-3** | **"step n" numeral** (P-09; for one step it may sit on paper, P-14, or on the green panel, P-39) | F-B, process scripts ("step 1… step 7") | "step" italic 72 px + numeral italic 260–320 px flanking the body |

One marker style per reel (SM-2 **or** SM-3 in F-B). Numbering is always ascending. No recap, no "next" teaser chips.

### 7.3 Unit rituals (identical every time)
**F-A item ritual** (frames at 30 fps; 0 = the ordinal word's onset):
| Frame | Event |
|---|---|
| −1 → 0 | The previous title and thumbnail vanish on one frame (hard out, no fade) |
| 0 | **P-10** "n. Title" and **P-05** item visual appear on the same frame, in place, no scale or slide (bottom clamped to face top − 24) |
| 0 → +3 | The title **flickers** once (opacity 1 → 0.35 → 1, one frame each); the thumbnail stays solid (measured v04 @0:09.12, @0:13.92; v03 @0:09.09, @0:15.16) |
| +3 → end | Hold; captions continue (CS-1 micro); at most one tier-2 keyword in the item; at most one internal event (a counter landing, or a second still hard-swapping in on the next noun) |
| 0 | the bundled pack's list cue on the ordinal (the one allowed repeat) |

Item length 2.0–4.5 s (measured swap times: v04 2.0–2.6 s apart, v03 3.0–3.7 s). No cut and no footage blur on items 2…N; the item 1 entry is the hook ritual (§6.2). Items never share a frame: the next title starts only after the previous one is gone.

**F-B section ritual:**
| Step | Event |
|---|---|
| 1 | Hard cut (T-01) to a fresh plate on the section word, or the marker over the A-roll's top band (v01 "No.2") |
| 2 | **P-08** "No.n" lands on the cut frame and flickers in over 5 f (v01 @0:37.12) or de-blurs over 4 f (v05 @0:09.82); the sub-line builds on its spoken words (captions hidden for 1.2–2.0 s), or **P-09** "step n" (1.0–1.5 s) |
| 3 | A **burst** (P-21, 3–6 plates on content words) illustrating the section's claim |
| 4 | A **breath**: G-2 cut back to the face for the opinion line (2–6 s), with one proof element above the head if the line has one (P-30 / P-31 / P-32 / P-34), or a split (P-28) for a screen |
| 5 | Optional type beat (P-14 / P-15 / P-16) on the section's punch word, then the next section |

### 7.4 Open loops and re-hooks
- **Loops used:** the count loop (the chip's number, paid by the last item or numeral), the parable loop ("Picture this…" → "Here's why."), the deliverable loop (the community card at the end). All are paid on screen (H9).
- **Re-hooks:** F-A is `short`: no re-hook obligation (the item ritual re-hooks every 3 s). F-B is `standard`: **one mid-reel re-hook between 40 % and 60 % of the runtime, and no gap intro → re-hook → CTA longer than 35 s** (`structure.rehook_every_s: 35`). The re-hook is the next **section numeral card** (scene `kind: "rehook"` or beat `rehook: true`) or a question type frame (P-14 / P-16 with the question as spoken).
- **Intro cap:** hook ≤ 15 % of runtime (F-A ≤ 4.0 s at 30 s; F-B ≤ 10 s at 70 s).

### 7.5 Rhythm and energy curve
- **F-A:** flat and calm by design. Energy comes from the title / thumbnail swap every 2.4–4.5 s and one keyword slam per 6–10 s. The last item (the CTA item) is the warmest: the community card is the largest, brightest visual of the reel.
- **F-B:** hook (mood, slow de-blur) → turn (face, tier-2 word) → sections alternating **burst → breath** → the last section escalates (the longest burst, a colour frame, a macro) → the CTA on the face, still and clean, ending on the cream keyword.
- **Burst / breath rule:** never two bursts back to back; never more than 2 breaths without a burst; a breath longer than 4 s carries a graphic event every ≤ 2 s (a proof element, a split, a stacked pair).

### 7.6 Cadence (state changes) `[TUNE ±15%; cuts DNA]`
| Token | F-A | F-B | Note |
|---|---|---|---|
| `caption_weight` | 1.0 | 1.0 | captions are primary; one word = one SC |
| `sc_per_10s` | [18, 45] | [20, 45] | mostly caption words (≈ 25–33 per 10 s at speaking pace) |
| non-caption SC per 10 s (review) | ≥ 3 (title + thumbnail swaps, counters, keyword slams) | ≥ 6 (cuts, frames, markers, punches) | the visual floor V-CADENCE cannot separate |
| `hook_sc_3s` | 8 | 9 | |
| `max_gap_s` / hook | 1.2 / 0.7 | 1.0 / 0.6 | weight ≥ 1 SC |
| `max_static_s` | 2.5 | 2.0 | live footage counts as motion |
| `cuts_per_min` | **[0, 2]** (DNA) | **[26, 29]** (DNA rhythm; TUNE 22–34) | F-B: cutmap joins + every `transitions` marker (T-01, T-04, T-05) |
| `median_shot_s` | — | **[1.0, 1.6]** | v01 1.32, v02 1.04, v05 1.56 |
| shot p90 / longest picture (measured, scene > 0.2) | items 2.0–3.7 s | p90 3.6–3.8 s; longest 9.0–11.6 s, always the face carrying graphic events | v01 9.2 s, v02 11.6 s, v05 9.0 s |

**How F-B reaches 26–29 cuts/min (decided arithmetic for a 60 s reel):** ≈ 27 cuts = hook 3 + 4 sections × (marker cut 1 + burst 4 + back to the face 1) = 24 + 3 type-frame cuts. Count them in the beat sheet before building; a section without a burst needs two type frames instead.

**Transition markers count as cuts.** In F-B, every plate entry, every return to the face and every type frame writes `timeline.transitions: [{t, id: "T-01" | "T-04" | "T-05"}]` at the same t as its stage change, so V-CADENCE counts it. In F-A, write **no** transitions.

---

## §8 Visual system: graphics, B-roll and patterns `[REQ]`

### 8.1 Graphics role and budget
`graphics: support`. 44 patterns (support band 20–45). Runtime share of graphics beyond captions: F-A 55–90 % (a title and a thumbnail are on screen for every item), F-B 15–35 % (chips, markers, frames, proof tiles; the plates are footage, not graphics). Families per 60 s: F-A ≥ 3, F-B ≥ 5. **Numbers become pictures** only through the counter ring (P-30) and real proof tiles; a number is never decorated with made-up charts.

### 8.2 Families (B-…)
| ID | Family | Source class | The buyer supplies |
|---|---|---|---|
| **B-1** | Headline chip & markers (chip, sub-line, list titles, numerals) | `engine` | — |
| **B-2** | Duet captions (auto) | `engine` | — |
| **B-3** | Type frames (paper, cobalt, void; stacked pair; keyword over plate) | `engine` | — |
| **B-4** | Cinematic plates (montage) | `buyer-owned` | 25–40 own clips (SH-1…SH-6) |
| **B-5** | Item stills (F-A thumbnails, polaroids, card wall) | `buyer-owned` (else a created card, FB-8) | photos the creator owns (SH-8) |
| **B-6** | Proof UI (counter ring, profile pill / tile, notification pill, toggle, level panel) | `engine`, filled with the creator's real numbers | the numbers and the profile facts |
| **B-7** | Screens (screen recordings, screenshots) | `buyer-owned` | SH-7 files |
| **B-8** | Third-party moments (a tool, a brand, a famous image, a post) | `creator-supplied third-party`; else a created substitute: logo plate (P-06), recreated UI (P-40), quote card (`fx.quoteCard`), silhouette (`fx.silhouette`) | the file, if they hold it |
| **B-9** | CTA & brand cards (community card, keyword quote, follow pill, sponsor chip) | `engine` + the creator's community images | community name, promise, 3–5 images; a sponsor's logo file |

### 8.3 Pattern specs (P-…)
Motion at 30 fps; "lead" = frames before the trigger word. Engine blocks: `VEOS.scene` (bespoke), `VEOS.fx.*`, `VEOS.data.counter`, the stage / world / camera / transitions entries of `timeline.json`, and `captions.overrides`.

**Headline & markers (B-1)**
| ID | Name | Type | On screen | Motion recipe | When | Engine / class / needs |
|---|---|---|---|---|---|---|
| **P-01** | **Promise chip** | overlay | Cobalt chip (serif 104 px) + sub-line (serif 56 px) above the head | f0 swinging in from the top-left (−12°, ≈ 300 px) → rest by f13 (expo-out) while typing ≈ 1 char/f; or static at f0 (v03); sub-line typed ≈ 0.8 char/f; exit hard on the item-1 cut or inside T-11 | F-A hook (default); F-B HA-05 | `VEOS.scene` z10 `kind: "chip"`, one element, TC-display + TC-label nodes |
| **P-02** | **Typed chip** | overlay | Cobalt chip (grotesk 88 px) growing from its left edge as the text types | the P-01 swing-in with the grotesk text; width tracks the typed text (≈ 1 char/f; first word by f6; done ≤ f24) (v05 @0:00.12–0:00.68) | F-B hook (HA-05); chips with long words | `VEOS.scene` z10 `kind: "chip"`; `events` at the typing end |
| **P-03** | **Sub-line build** | overlay | The rest of the spoken promise under the chip | typed letter by letter ≈ 0.8 char/f, paced to the voice (v03 @0:00.08–0:00.50) | with P-01 / P-02 | drawn inside the chip scene |
| **P-04** | **Behind-head numeral** | overlay | The reel's number ("10", "101", "7") huge, behind the head | on from f0 at 0.85 opacity, riding the Z-3 pull-out (v05 @0:00.00); exits with the chip | hook only, ≤ 1 per reel, when the chip has a number | `VEOS.scene` z3, `behind: true`, `exception: "E1"`, TC-display; needs the matte |
| **P-08** | **Section numeral card** (SM-2) | overlay | "No.n" cream didone 300 px at cy 480 + the section sub-line at cy 720, over a fresh plate | on the cut frame; flicker-in 5 f (opacity 1 / 0.4 / 0.8 / 0.4 / 1, v01 @0:37.12) or de-blur 4 f (v05 @0:09.82); sub-line words on their onsets; exit hard on the next cut | every F-B section start; the middle one is the re-hook | `VEOS.scene` z8 (`kind: "rehook"` for the mid section); captions hidden under z8 |
| **P-09** | **Step numeral** (SM-3) | overlay | "step" italic 72 px left of the body + numeral italic 260–320 px right of it, cy 1120 | "step" and the numeral each flicker in over 5–6 f on their words (v02 @0:16.08–0:16.44), no rise; exit hard on the next cut | F-B process scripts | `VEOS.scene` z8, TC-display; ≥ 40 px clear of the face box |
| **P-10** | **List title row** (SM-1) | overlay | "n. Title" italic didone 92 px at cy 250 | hard swap on the ordinal (lead 0–2 f) + one-frame flicker (1 → 0.35 → 1) (T-06) | every F-A item | `VEOS.scene` z6, TC-display |

**Captions & type (B-2, B-3)**
| ID | Name | Type | On screen | Motion recipe | When | Engine / class / needs |
|---|---|---|---|---|---|---|
| **P-11** | **One-word duet** | overlay | One word, tiered 1× / 1.6× / 2.5× | blur-in 2 f per word (CS-1), `flicker` 5 f (CS-2) | always (automatic) | caption engine; never hand-written |
| **P-12** | **Keyword slam** | overlay | The tier-2 word (F-A grotesk 110 px; F-B italic didone 160 px) | as P-11 (the size is the event) | 1 per 6 s (F-A); ≤ 3 per 10 s (F-B) | `captions.overrides: {i, emph: true}` |
| **P-13** | **Chip highlight** | overlay | Small words riding cobalt chips; content words plain | blur-in 3 f | F-B hook (≤ 3 s) + ≤ 2 one-second uses | `captions.overrides: {t: [a, b], profile: "CS-3"}` (E3 on the chip) |
| **P-14** | **Paper frame** | stage | Off-white frame; the caption word in cobalt grotesk (or a planned italic-didone word); optional creator still (polaroid 300×300) at cy 1330 | G-4 cut; still pops 8 f | a thesis, a time span ("2 years."), a question re-hook | `stage L-type` + `world W-paper` + `transitions T-04`; still as `VEOS.scene` z3 |
| **P-15** | **Cobalt frame** | stage | Cobalt frame; one small white word (CS-2 tier 0, 64 px) with a 4 px `paper` underline 40 px wider than the word, 30 px below it | G-4 cut; the underline is on from the cut and **resizes to each new word's width** over ≈ 3 f (v01 @0:27.16–0:27.40) | one decisive word ("managed", "timeline") | `stage L-type` + `world W-cobalt` + `T-04`; underline `VEOS.scene` z5 (no text) |
| **P-16** | **Void frame** | stage | Navy-black frame; one word | G-4 cut | a quiet beat before a reveal; a question | `L-type` + `W-void` + `T-04` |
| **P-17** | **Stacked pair** | overlay | Two heavy grotesk words stacked above the head ("private / community") | each word rise 30 px + blur-in 6 f on its onset; hold ≤ 1.5 s; exit blur 6 f | the deliverable noun before the CTA; a 2-word thesis (≤ 1 per reel) | `VEOS.scene` z8, TC-display |
| **P-18** | **Keyword over plate** | overlay | A big upright or italic didone word (170 px) centred on a plate; the next 1–2 spoken words in micro grotesk 44 px under it (cy 1050) as they are spoken | big word blur-in 8 f; micro words blur-in 4 f on their onsets | a named thing or person in the montage ("Editor 1", "key difference") | `VEOS.scene` z8, one element; micro nodes `data-tc="TC-subtitle"`, `exception: "E3"`; captions hidden under z8 |
| **P-19** | **Opening word** | overlay | The first 1–2 spoken words, Inter Tight 700 96 px at cy 960 | at f0 already 60 % into a 10 f blur-in; exit blur 4 f when the captions take over | F-B HA-19 f0 (satisfies V-F0 "one word") | `VEOS.scene` z8, TC-display |

**Footage & montage (B-4)**
| ID | Name | Type | On screen | Motion recipe | When | Engine / class / needs |
|---|---|---|---|---|---|---|
| **P-20** | **Plate cut** | cut | One creator clip, full bleed | hard cut on a content-word onset −2 f; optional push 1.0 → 1.04 over the shot | every montage picture | `stage L-broll` (cut) + `VEOS.fx.clip({asset, kind: "broll", kenburns: [1, 1.04]})` z3 + `transitions T-01`; beat carries `shot_id`, `fallback_used` |
| **P-21** | **Burst** | cut | 3–6 plates, 0.4–1.0 s each, one subject family | cuts on consecutive content words; no motion added in frame | the body of every F-B section; ≤ 1 burst per 10 s | P-20 × n |
| **P-22** | **Rack-focus open** | footage-treatment | The first plate de-blurring | held defocused (≈ 14 px) under the opening words, then a 1 f snap to sharp on the subject word + a ≈ 1.4 %/f pull (v01 @0:00.00–0:00.68); or blur 14 → 0 over 12 f under Z-3 (v05) | F-B f0; a new mood after a type frame | the clip scene with a CSS `filter: blur()` driven by `lt` |
| **P-23** | **Split twin** | footage-treatment | One plate twice: top half GR-blue-wash, bottom half GR-red-wash, seam at 960, caption on the seam | static split for 2–4 s (no flicker) | hook only, once; "two people / two paths" premises | one `VEOS.scene` z3 drawing two crops of `ctx.videoFrame`; counts as 1 grade event |
| **P-24** | **Mono accent** | footage-treatment | A plate in GR-bw, darkened under a 420 px radial scrim; the mistake word in `bad` red Inter Tight 700 ≥ 120 px at cy 960 | grade on with the cut; red word blur-in 6 f | `warn` lines: the mistake, the cold truth | clip scene filter + word `VEOS.scene` z8 (captions hidden for that word) |
| **P-25** | **Colour wash** | footage-treatment | A plate in GR-red-wash / GR-blue-wash / GR-amber | grade on with the cut | a tense / calm / warm beat; ≤ 3 grade events per reel, no repeats in a row | clip scene filter |
| **P-26** | **Macro punch** | cut | A macro plate (eye, nib, dial) for 0.6–1.0 s with a tier-2 word | push 1.0 → 1.08 over the shot | "look closer / focus / notice" lines | P-20 with SH-5 |
| **P-27** | **Crop punch** | cut | The A-roll jumps tighter (1.0 → 1.35 on 1080 p; 1.6 on 4K) | hard cut to the tighter frame (`snap-punch`, 1 f) + its built-in 5 f de-blur; then hold or a slight drift (v02 @0:02.44) | F-B emphasis on the face (≤ 1 per 10 s; never two in a row) | camera preset Z-1; mark `T-05` |
| **P-28** | **Split screen** | stage | A screen recording in the top band (0–900), the presenter below, the caption on the seam | hard cut in and out (`via: "cut"`, v02 @0:16.08); the step numeral flickers in on the seam | "here's my timeline / settings / app" while talking | `stage L-split` + `VEOS.fx.shot` or `ctx.videoFrame` inside `ctx.layout().rects.graphic` |
| **P-29** | **Framed take on paper** | stage | The live A-roll in a 520×560 card (radius 10, soft shadow) centred on W-paper, a small grotesk lead-in above it ("If you want to") and a 2–3-word `accent` tag under it ("stay relevant") | cut in (T-04); the card hard-exits with a 2 f 3D flick (rotateY ≈ 30°, blur) into the next frame (v01 @0:16.08–0:16.28) | a quoted condition or a rule spoken to camera inside a burst; ≤ 1 per reel | `stage {layout: "card", rect, radius: 10}` + `world W-paper` + a z5 text scene |

**Item visuals (B-5, B-7, B-8)**
| ID | Name | Type | On screen | Motion recipe | When | Engine / class / needs |
|---|---|---|---|---|---|---|
| **P-05** | **Hover thumbnail** | overlay | The item's picture in a 540 × (300–440) card by the picture's aspect (x 270–810, top y 290, radius 10; measured v04 @0:08 x 272–812, top 288, shadow `0 18 40 rgba(0,0,0,.45)`), cover crop, bottom ≤ face top − 24 | hard in and out with the title (T-06); no scale, no blur | every F-A item | `VEOS.scene` z3 with `ctx.asset` / `ctx.videoFrame` |
| **P-06** | **Logo plate card** | overlay | A white card 460×190 radius 28 at cy 450 with the brand / tool name set in Inter Tight 800 96 px `ink` (or the creator's own logo file) | as P-05 | a named platform, tool or company | `VEOS.fx.logoPlate({name, theme: "light"})` + an `insert` record |
| **P-07** | **Screen thumbnail** | overlay | A screenshot / screen recording in the thumbnail rect (no window chrome), private data blurred | as P-05; a recording plays from its in-point | "my folder / my template / my timeline" | `VEOS.fx.shot({asset, chrome: false})` in the rect |

**Proof & UI (B-6)** (numbers only from the script or the creator, §8.5)
| ID | Name | Type | On screen | Motion recipe | When | Engine / class / needs |
|---|---|---|---|---|---|---|
| **P-30** | **Counter ring** | state | A Ø 430 ring, 14 px stroke in `G-ring`, open 20° at the bottom; value 80 px + unit 44 px inside. On L-full: centre (540, 520) above the head. On W-paper: centre (540, 760), text `ink` | the arc sweeps in from its start while the gradient rotates ≈ 30°/f; the value **odometer-rolls per digit**, fast (8 → 152,565 in 13 f) then easing, and keeps climbing across the beat to land on the spoken number ±5 f (v03 @0:23.90–0:26) | a spoken count (views, clients, kilos, savings) | `VEOS.data.counter({figure, …})` inside a ring scene, `figure` bound; beat `state_ops` |
| **P-31** | **Profile pill** | overlay | Dark glass pill 360×120 (`rgba(20,20,22,.78)`, 1 px `rgba(255,255,255,.12)` border, radius 60) at (540, 500): avatar Ø 84 (the creator's photo or initials) + name 40 px + handle 30 px TC-legal | rise 20 px + blur-in 8 f | "me", "my name is", "follow" | `VEOS.scene` z5; the creator's real name and handle only |
| **P-32** | **Glass profile tile** | overlay | A 900×300 glass card at y 280–580 with the creator's profile (avatar, name, handle, 3 counts, 1 bio line) | rotateY 8° → 0 and blur 6 → 0 over 14 f | "my account / this page grew" | `VEOS.scene` z5; counts from `plan/figures.json` (`from: creator`) |
| **P-33** | **Notification pill** | overlay | An `accent` pill with 3 glyph + count pairs (comments, likes, follows) and a pointer tail | pop scale 0.9 → 1 over 6 f (no overshoot); counts roll 18 f | "the comments, likes and follows started coming" | `VEOS.scene` z5; the counts are figures |
| **P-34** | **Toggle compare** | annotation | A glass bar 760×110 at cy 340: label A — toggle — label B (words from the script); a cursor clicks; the plate below switches grade | cursor travels 10 f, click 2 f, knob slides 8 f, the plate filter switches on the click | before / after on a creator plate ("original / enhanced") | `VEOS.scene` z5 + the clip scene's filter event |
| **P-35** | **Card wall** | overlay | 6–9 of the creator's own thumbnails / clips on a curved perspective wall above the head (y 0–760); cards 220×390, radius 16; columns rotateY −35° / 0 / 35° | scroll up 120 px/s; each card lingers 5–10 f in the centre column | HA-02 proof: "all of this" / "my work"; 1.5–2.0 s | one `VEOS.scene` z3 (one element) |
| **P-36** | **File float** | overlay | On W-paper: 6–12 white file labels drifting (icon + "01_name.ext"), TC-decorative at 70 %; the caption word at the centre | drift ±20 px over the hold; fade in 8 f, staggered 2 f | "a pile of assets / files / options" | `VEOS.scene` z3, labels `data-tc="TC-decorative"`; names from the creator's files or the script |
| **P-37** | **Polaroid grid** | overlay | On W-paper: a 3×2 grid of creator stills 230×300 (10 px white border, seeded ±2° tilt); rows at y 600–900 and 1020–1320; the caption word in cobalt at cy 960 | polaroids pop 6 f, staggered 3 f | "my portfolio / these moments / all these clients" | `VEOS.scene` z3 |
| **P-38** | **Tilt phone card** | overlay | On W-cobalt: a phone-shaped card 520×1000 (radius 48) playing a creator clip, rotateY −18° → −8°; a didone word (Instrument Serif 120 px, `paper`) across its lower third | card swings in from edge-on (rotateY ≈ 85° → −18°) over 3 f with motion blur, then drifts (v01 @0:16.32–0:16.44) | "fast", "on my phone", reels about reels | `VEOS.scene` z4 with `ctx.videoFrame` |
| **P-39** | **Level panel** | state | On black: a `good` green vertical meter 560×1400 with tick marks; "step" + numeral in `ink` inside | the level rises 0 → target over 14 f on the number word | one process step about levels / volume / progress; ≤ 1 per reel | `VEOS.scene` z4, TC-display (ink on green 14:1) |
| **P-40** | **UI card** | overlay | A recreated generic UI (export dialog, menu, settings list) in a dark card, radius 24, in the above-head zone or the split's top band; a cursor clicks the named control | rise + de-blur 10 f; cursor 10 f; click 2 f | "click export", "turn this on", with no creator recording | `VEOS.fx.appUI({kind: "settings"})` (or `list`, `browser`); or `fx.shot` with the creator's own capture |

**CTA & brand (B-9)**
| ID | Name | Type | On screen | Motion recipe | When | Engine / class / needs |
|---|---|---|---|---|---|---|
| **P-45** | **Community card** | overlay | White card 886×490 (radius 28) at x 97–983, y 290–780: community name (Instrument Serif 64 px `ink`), one-line promise (Inter Tight 500 40 px `#3A3A3A`), a fanned collage of 3–5 creator images in the lower half | rise 24 px + blur-in 10 f; collage cards fan out, 3 f stagger | the CTA (F-A: the last item's thumbnail; F-B: above the head on the deliverable line) | `VEOS.scene` z4 `kind: "end-card"`, 2.0–4.0 s |
| **P-46** | **Keyword quote** | overlay | The keyword in curly quotes, Instrument Serif 260–360 px (fit 860 px, tracking −0.03), `G-keyword` fill, 24 px cream glow, cy 450 | after a 1-frame T-11 pulse with nothing on screen, the word lands at full size; colour cycles `primary` → teal → white over 3 f (v04 @0:27.68–0:27.80) or fades in cream over 4–6 f (v01 @1:04.34); the footage pushes 1.0 → 1.06 over 12 f (Z-2) | on the spoken keyword; holds ≥ 1.5 s, to the end | `VEOS.scene` z10 `kind: "cta-keyword"`; `text_content` contains the keyword |
| **P-47** | **Follow pill** | overlay | P-31 under the F-A title "n. Follow for more" | as P-31 | the follow device | P-31 + P-10 |
| **P-48** | **Sponsor chip** | overlay | A cobalt chip "with [Brand]" (grotesk 56 px) at cy 400 + "Paid partnership" TC-legal 24 px at cy 470 (+ the creator-supplied logo file, 120 px tall, if given) | as the P-01 settle (8 f) | a sponsored segment; ≥ 2 s | `VEOS.scene` z10; `sponsor` on the beat (NC-12) |

### 8.4 Line → pattern lookup `[NICHE: example]`
The editor classifies every sentence with this table (P5). Example rows for the two template niches; append the buyer's own rows per reel.

| Line type | Primary | Alternates | Fitness example | Finance example |
|---|---|---|---|---|
| The promise / title ("Here are 7…") | P-01 (+ P-04 when the chip has a number) | P-02; HA-12 opener (F-B) | "7 gym habits that build muscle" | "10 ways to earn money as a freelancer" |
| An item's name (F-A) | P-10 + P-05 | P-06, P-07, P-30 | "1. Train to failure" + own training photo | "1. One-off gigs" + logo plate of the platform |
| A named platform / tool / brand | P-06 logo plate | P-40, the creator's own logo file | a tracking app (name in type) | a freelance marketplace (name in type) |
| "Look at my screen / app / sheet" | P-07 (F-A) / P-28 split (F-B) | P-40 | own workout-tracker screen | own budget spreadsheet |
| A spoken count of proof (views, clients, kg, savings) | P-30 counter ring | P-32, P-33 | "lost 12 kg" ring (the creator's figure) | "saved $8,400" ring (the creator's figure) |
| "Me / my name / my page" | P-31 profile pill | P-32 glass tile | "I'm [name], I coach…" | "I'm [name], I teach money…" |
| A process step ("step 3") | P-09 step numeral | P-39 level panel (one step), P-14 + numeral | "step 3: progressive overload" | "step 3: automate the transfer" |
| A section opener ("the second thing") | P-08 No.n | P-14 paper question | "No.2 / your sleep" | "No.2 / your spending" |
| A feeling / mood line | P-20 plate + P-12 italic keyword | P-22, P-25 | "and it felt **impossible**" over an SH-3 profile | "every month felt **tight**" over SH-1 at the laptop |
| A list of many things | P-37 polaroids / P-36 file float | P-35 card wall | "all these programs" | "all these subscriptions" |
| The mistake / the cold truth | P-24 mono accent | P-14 with the word in red (≥ 96 px) | "**skipping** legs" | "**minimum** payments" |
| A time span or the decisive word | P-14 paper (italic didone) / P-15 cobalt | P-16 | "**6 months.**" | "**2 years.**" |
| Before vs after | P-34 toggle | P-23 split twin (hook only) | "form before / after" | "budget before / after" |
| A tight emphasis on the face (F-B) | P-27 crop punch | P-12 | "**stop** doing this" | "**stop** doing this" |
| A quote someone said / a post | `fx.quoteCard` (verbatim, created) | the creator's screenshot via `fx.shot` | a client's message (creator-supplied) | a viral post (created quote card) |
| The deliverable ("my community / guide") | P-17 stacked pair → P-45 | P-31 | "free training plan" | "budget template" |
| The comment ask | P-46 keyword quote | — | 'PLAN' | 'BUDGET' |
| A sponsor mention | P-48 | — | — | — |

### 8.5 Data and truth rules
- There is no §18 module, but **every counter or stat number is a figure** in `plan/figures.json` (`kind: counter`, `formula: none`, `from: script` with the spoken words, or `from: creator`), so V-DATA checks it (NC-6).
- Profile tiles and pills show the creator's real name, handle and counts only; never a verification tick they don't have (N12).
- No charts, no invented results. "Illustrative" graphics are not used in this style.

### 8.6 Comedy layer
OFF (`tone.comedy = off`, `comedy_max = off`).

### 8.7 Asset rules
- **Real captures first:** the creator's own plates, stills, screen recordings and profile.
- **Allowed mocks:** generic, unbranded UI; logo plates set in type (P-06).
- **No stock, no AI scenes, no famous artworks or press photos** unless the creator holds them (then `origin: creator`).
- **Blur** personal data on screens (NC-14).
- **Ask, then create** for every third-party moment (§12.5).

### 8.8 Density and variety
- **F-A:** one item visual per item (P-05 / P-06 / P-07 / P-30), ≥ 3 different item patterns per reel; at most one internal event per item; the same thumbnail never twice.
- **F-B:** ≥ 10 distinct patterns per 60 s; ≥ 5 families; the same plate never in two adjacent bursts; a clip used at most twice per reel, with different in-points; the same pattern at most 2 beats in a row (bursts and the F-A ritual are the exceptions).

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Library (T-…)
| ID | Transition | Frames | Recipe | Timeline / engine | Cue role |
|---|---|---|---|---|---|
| **T-01** | **Hard cut** | 0 | The picture changes on a content-word onset −2 f (±2 f) | stage `via: "cut"` + `transitions {t, id: "T-01"}` (F-B) | burst start only (whoosh), otherwise silent |
| **T-02** | **Blur-through** | 4 + 5 | The whole frame blurs 0 → 16 px (4 f), cut at the peak, the incoming shot (and its new graphics) de-blurs 16 → 0 (5 f) (measured v04 @0:03.58–0:03.90) | built in: `transitions {t, type: "blur-through", px: 16, frames: 9, pre: 4}` (layers `picture`: footage, plates and the incoming title / thumbnail de-blur together; captions stay sharp) | silent (calm) |
| **T-03** | **Rack-focus open** | 12 | Blur 14 → 0 px, scale 1.06 → 1.0 (P-22) | clip scene filter | hook cue |
| **T-04** | **Colour-frame cut** | 0 | Cut into / out of W-paper, W-cobalt or W-void (G-4); min hold 0.4 s; ≥ 0.34 s between two colour frames | stage L-type + world entry + `transitions {id: "T-04"}` | optional soft tick (pack `click`/`tap`), ≤ 1 per 5 s |
| **T-05** | **Crop punch** | 1 + 5 | A hard cut to a much tighter face (Z-1, 1 f) that de-blurs over 5 f; the tier-2 word flickers in on it (v02 @0:02.44) | camera preset + `transitions {id: "T-05"}` | silent |
| **T-06** | **Title swap** (F-A) | 0 + 3 | Old title + thumbnail out and new ones in on the same frame; the new title flickers once (1 → 0.35 → 1); no fade, no scale (v04 @0:09.12, @0:13.92; v03 @0:09.09) | scene exits / entries; no marker | list cue |
| **T-07** | **Chip cut-out** | 0 | Chip + sub-line end on the item-1 cut (hard) or inside T-11 (v03 @0:02.83, v04 @0:03.70) | chip scene ends at the cut | silent |
| **T-08** | **Wash cross-grade** | 6 | The plate's filter cross-fades from neutral into a wash (or back) without a cut | clip scene filter ramp + an `events` entry | silent |
| **T-09** | **Split cut** | 0 | Hard cut into L-split and back (measured v02 @0:16.08; no slide) | stage `via: "cut"` + `transitions {id: "T-01"}` | silent |
| **T-11** | **Blur pulse** | 1–4 | The whole picture blurs ≈ 14 px for 1–4 f and snaps (or eases) back; nothing new reads during it. On: hook word beats on the f0 plate (v01 @0:00.16, @0:00.56), the item-1 cut (v04 @0:03.62), a face push (v01 @0:41.7), the CTA keyword entry (v04 @0:27.68, v01 @1:04.34), a big caption word (v02 @0:00.60) | built in: `timeline.grades: [{t, blur: 14, dur: 0.04–0.16, frame: true}]` (no grade id): the whole picture blurs, graphics z1–6 included, captions stay sharp; graphics may already be on screen during it (v04 @0:27.68, v01 @0:00.16) | optional whoosh (pack) on the CTA / item-1 pulse only |
| **T-10** | **Hard end** | 0 | Last word + ≤ 6 f, then end on the keyword quote (no fade to black, black tail ≤ 0.2 s) | — | none |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | F-A: Z-3 pull-out + the chip swing-in on live footage (no transition). F-B: T-03 rack-focus open | a fade-in from black; a flash |
| Hook → item 1 (F-A) | T-02 / T-11 + the hidden cut, chip out (T-07), title + thumbnail in | a visible jump without the pulse; a chip fly-off |
| Item → item (F-A) | T-06 | a cut, a fade, a slide, a push |
| Hook → body (F-B) | T-01 cut back to the face (G-2) on the turn line | a crossfade |
| Section start (F-B) | T-01 to a fresh plate + P-08 / P-09 | a type frame without the numeral |
| Plate → plate (burst) | T-01 on content words | a cut on a function word; a dissolve |
| Mood change between plates | T-02 blur-through (≤ 3 per reel) or T-08 wash | a dissolve, a whip |
| Face ↔ screen | T-09 split cut | a slide, a full-screen raw recording |
| Emphasis on the face (F-B) | T-05 crop punch | a shake, a crash zoom |
| One-word beat | T-04 colour frame | two colour frames < 0.34 s apart |
| The CTA | T-01 back to the face, the card, then T-11 (1 f, empty frame) into the keyword with a Z-2 push | any other transition into the keyword |
| Last word | T-10 | a black tail > 0.2 s |

### 9.3 Shot grammar R-… `[ON for F-B by declaration: the montage cut grammar is DNA; OFF for F-A]`
- **R-1 Cut on the word.** Every plate starts on the onset of a content word (noun, verb, number, adjective) −2 f; the content word is the one the plate shows ("headphones" → SH-3 with headphones).
- **R-2 Literal first, mood second.** If the bank has a literal match for the word, use it; otherwise use the mood match (tags `mood`, `light`); otherwise a type frame. Never a mismatched literal (a phone when the word is "notebook").
- **R-3 Burst families.** A burst stays in one family: the same location from 3–6 angles (desk: back of head → hands → screen glow → profile) or one action across places (writing → typing → editing). Never mix bright daylight and night practicals inside one burst.
- **R-4 Burst speed.** 0.4–1.0 s per plate inside a burst; the last plate of a burst holds 1.0–2.5 s (the landing).
- **R-5 Breathe on the face.** After every burst, return to the face (G-2) or hold one plate for 2–6 s; the opinion line, "Here's why", numbers and the CTA are always on the face.
- **R-6 Macro on attention words.** "look", "notice", "focus", "detail" → SH-5 macro (P-26).
- **R-7 Silhouettes for the abstract.** "goal", "future", "years", "dream" → SH-4 environment / silhouette plates (with GR-amber at most once).
- **R-8 No repeats in reach.** A plate never appears twice within 15 s, and never as the first and last plate of the same section.

### 9.4 Budget (per 60 s)
- F-A: 1 hidden cut into item 1 (under T-02 / T-11), ≤ 1 more hidden fix per 30 s, T-06 once per item, T-07 once.
- F-B: T-01 22–26, T-04 2–5, T-05 ≤ 4, T-02 ≤ 3 per reel, T-09 ≤ 2, T-08 ≤ 2.
- **The same transition never 3× in a row**, except T-01 inside a burst and T-06 in the F-A ritual.
- Cuts within ±1 f of word boundaries; the voice is never cut or offset.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the trigger word (captions 1 f) |
| Entry (titles, numerals, tier-2 words) | **flicker-in** 3–5 f (opacity 1 / 0.35–0.4 / 0.8 / … / 1, lands on its first frame) or de-blur 4–5 f (blur 12 → 0); no slide, no scale; ease `cubic-bezier(0.22, 1, 0.36, 1)` |
| Caption swap | outgoing hard; incoming blur 2 f (CS-1, CS-4), 5 f `flicker` 0.4 / 0.8 / 0.4 / 0.8 / 1 (CS-2), 3 f (CS-3) |
| Exit | hard on the next cut / swap (measured everywhere); a 4 f blur only inside T-02 / T-11 |
| Chip swing-in | 12–14 f from −12° / ≈ 300 px up-left, typing ≈ 1 char/f |
| Blur pulse (T-11) | 1–4 f, ≈ 14 px, ≤ 1 per 3 s, structural beats only |
| Overshoot | **0** (no back-out, no elastic; calm) |
| Counter roll | fast odometer (≈ 13 f for the bulk), easing out across the beat; lands on the spoken number ±5 f |
| Rack focus | held defocus → 1 f snap (v01) or 12 f de-blur (v05) |
| Colour-frame minimum hold | 0.4 s |
| Text hold | ≥ 0.25 s per word; titles ≥ 10 f after built |
| Drift (plates, numerals) | ≤ 8 px or ≤ 4 % scale over the hold |

### 10.2 Footage camera (Z-…) `zoom_policy: presets`
| ID | Preset | Recipe | Use | Limits |
|---|---|---|---|---|
| **Z-1** | `snap-punch` | a cut-in: 1.0 → 1.35 in 1 f (1.6 only with a 4K take) + a 5 f de-blur (the preset's own `blur`: defocus 14 px, `shape: decay`, 5 f), hold until the next cut (v02 @0:02.44) | F-B emphasis on the face (P-27) | ≤ 1 per 10 s; F-B only; never twice in a row |
| **Z-2** | `push-drift` (push-in) | 1.0 → 1.12 over 28 f, `ease: "expoOut"` (preset), opened by a 1–2 f blur dip (v01 @0:41.6 1.14×, @0:45.4 1.12×); CTA variant 1.0 → 1.06 over 12 f (v04 @0:27.68) | F-B face breaths (≤ 1 per breath), the CTA keyword | F-A items stay locked off; a breath may also stay static (v05 @0:11.6–0:15.6) |
| **Z-3** | `pull-out` | **2.0 → 1.0 over 50 f**, `ease: "expoOut"` (half the travel by f6), motion-blurred for the first 8–12 f (preset `blur`: radial 0.15 at the face, 12 f, `decay`) (v04 ≈ 2.3×, v02 2.1×, v05 1.6×) | hook f0 on the face, both formats (3 of 5 reels) | hook only, once; needs ≥ 1080p (the blur hides the softness) |

Rules: never the same Z twice in a row; never two moves within 0.4 s (NC-3); never move the face under the chip or the thumbnail (re-check the face box after a punch); no shake, crash zoom or rotation (N5).

### 10.3 Canvas camera
OFF (`modules.canvas_camera = false`).

### 10.4 Layer order (back to front)
1. World (W-void under hidden stages, W-paper, W-cobalt)
2. Footage (A-roll) **or** the full-bleed plate scene (z3, `kind: "broll"`) with its grade filter
3. P-04 behind-head numeral (`behind: true`, between the footage and the matte cut-out)
4. Presenter cut-out (only when P-04 is visible)
5. Item visuals and proof (z3–z5): thumbnail, logo plate, ring, pills, tiles, card wall, community card
6. Title row (z6)
7. Captions (z7, automatic)
8. Big type (z8): section numerals, step numerals, stacked pair, keyword over plate, opening word, red word
9. Chip and CTA keyword (z10)
10. TC-legal lines (disclosure), inside their scenes

### 10.5 Finishing
- **No added grain or vignette on footage** (engine rule); the worlds carry their own noise (0.03–0.04) and vignette (W-paper 0.12, W-void 0.3).
- **Shadows:** soft only (chip `0 10 30 rgba(0,0,0,.35)`, cards `0 18 40 rgba(0,0,0,.45)`, captions `0 2 10–12`); never hard offset shadows or strokes.
- **Glow:** only the CTA keyword (24 px) and section numerals (30 px at 35 %).
- **Radius:** chip 4, thumbnails 10, UI / glass 24–28, pills 60, phone card 48.
- **Glass:** `rgba(20,20,22,.78)` fill + 1 px `rgba(255,255,255,.12)` border; no `backdrop-filter` stacks (30 ms budget).

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | `hook` (one cue on f0), `transitions` (F-B: one whoosh on a burst's first cut, ≤ 1 per 10 s; type frames may take one soft tick), `reveals` (counter landing, community card), `list_cue` (F-A: one file on every ordinal, the single allowed repeat), `cta` (one soft shine on the keyword quote). Caption swaps never carry a cue |
| **Meme cues** | off (`comedy: off`) |
| **Music bed** | on, from f0 (calm / premium vibe from the pack), under the voice the whole reel; a 0.5 s drop-out allowed before the keyword quote |
| **Ducking** | the bed ≥ 18 dB under the voice while the voice speaks; the creator's B-roll audio is muted (plates are picture only) |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

Mirrored in `tokens.json → sound`. Pack budget: ≤ 5 cues per 10 s (`budgets.sfx_per_10s`), ≤ 2 uses per file (S5).

---

## §12 Footage requirements, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's actual setups]`
| Setup | Use | Spec |
|---|---|---|
| **A** (F-A take) | the whole F-A reel | Seated front-on at the desk; phone or camera at chest height, slightly wide (24–28 mm equivalent); **head top y 560–660** in the 1080×1920 frame, face centre x 440–640; dark plain top (the chest is the caption band: no logos or text on the shirt); low-key room with 1–2 practical lights (monitor glow, a lamp), a teal-green or warm look; 30 fps or higher; mic not at chest height (a held prop sits below y 1200); one continuous take |
| **B** (F-B A-roll) | the face beats of F-B | The same room, framed a little tighter: head top y 360–580; optional second angle (SH-9); a 4K take when 1.6× punches are wanted |
| **C** (F-B bank) | the plates | The creator's own cinematic B-roll (§12.2), shot or graded in the same family as the room: shallow depth, practical light, slow camera, 25–60 fps |

### 12.2 Shot list (SH-…) `[COND: footage_dependency ≥ medium → F-B] [DNA]`
| ID | Shot | Spec | Count per 60 s | Must / optional | Formats |
|---|---|---|---|---|---|
| **SH-1** | Back-of-head / over-the-shoulder at the workspace | practical light only, the screen or the work glowing; 3–8 s clips; static or a slow slide | 3–6 | must | F-B |
| **SH-2** | Hands doing the niche's work | top-down or 45°: keyboard, notebook, barbell, ingredients, product; 3–6 s | 3–6 | must | F-B |
| **SH-3** | Side-profile portrait | thinking, listening with headphones, looking off frame; shallow depth; 3–6 s | 2–5 | must | F-B |
| **SH-4** | Environment / silhouette | window, balcony, street, gym floor, city; the creator small in frame; 4–8 s | 2–4 | must | F-B |
| **SH-5** | Macro detail | an eye close-up, a pen nib, a lens, a dial; 1–2 s usable | 1–3 | optional | F-B |
| **SH-6** | Behind the scenes | the camera / light / tripod set up in shot | 1–3 | optional | F-B |
| **SH-7** | Screens | screen recordings or screenshots of the tools / results the reel names | 0–6 | optional | F-A, F-B |
| **SH-8** | Item stills | photos the creator owns for F-A thumbnails (objects, places, own results) | 0–10 | optional | F-A |
| **SH-9** | Second angle | a tighter angle of the A-roll take, or a 4K take | 0–4 | optional | F-B |

**Bank size:** 25–40 usable clips per reel (full fidelity); 12–24 clips → FB-1 (degraded); < 12 → FB-1b (edit as F-A). Each clip may be used at most twice per reel with different in-points.

### 12.3 Fallbacks (FB-…)
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-1…SH-4, SH-6 (bank of 12–24) | reuse clips with different in-points (max 2 uses, never adjacent); lengthen breaths to 3–6 s; fill bursts with type frames (P-14 / P-15 / P-16) and A-roll punches (P-27); keep 26–29 cuts/min by counting type frames | fewer locations, more typography; the cinematic feel thins | degraded |
| **FB-1b** | the bank (< 12 clips) | the reel is edited as **F-A** (list overlay); if the script is not a list, F-A titles become its 3–7 key points ("1. The premise", "2. …") | no montage | **no_fallback** (F-B unavailable) |
| **FB-5** | SH-5 | a 1.35× crop of an SH-2 / SH-3 clip with a 12 f rack-focus in, or a type frame | no macro texture | holds |
| **FB-7** | SH-7 | `fx.appUI` recreated generic UI card (unbranded) or a logo plate set in type (P-06) | not the real tool screen | holds |
| **FB-8** | SH-8 | a created thumbnail: `fx.card` icon / illustration on a dark glass card, or a type card with the item's noun in italic didone on cobalt | less editorial; still on-brand | holds |
| **FB-9** | SH-9 | crop the main take (≤ 1.35× on a 1080 p source) for punches | a softer punch | holds |

The checkpoint lists every fallback used (`fallback_used` on the beats).

### 12.4 Props, matte, resolution
- **Props:** optional; one hand prop the creator holds while talking (a mic, a pen, a notebook) sits below y 1200 so it never fights the chest caption (the evidence shows a teal object colliding with captions at y ≈ 1130; the template moves the caption, not the prop: CS-1 `avoid_face` + 40 px clearance).
- **Reaction bank:** none.
- **Matte:** optional; required only for P-04 (E1).
- **Minimum source resolution:** a 1.35× punch needs 1080 p; a 1.6× punch or a 2× macro crop needs 4K (2160 px).

### 12.5 Third-party inserts: ask, then create `[REQ always]`
Claude never fetches anyone else's media. Per reel:
1. **Analyse** the transcript (`veos inserts scan`) and list the moments that call for third-party material (a platform's logo, a tool's screen, a famous artwork, another creator's post, a person's photo).
2. **Ask once**, as a short list: "For these N moments, do you have a clip, logo file or screenshot? (drop the files, or say no)".
3. **Supplied:** use it as given (P-06 logo file, P-07 screenshot, P-05 still), never altered to say something it doesn't.
4. **Not supplied:** create it, in this style:
   - a platform, tool or company → **P-06 logo plate** (the name set in Inter Tight 800 on a white card; `fx.logoPlate`);
   - an app screen → **P-40** `fx.appUI` recreated, unbranded UI;
   - a post or quote → `fx.quoteCard` in the dark glass skin, verbatim;
   - a person → `fx.silhouette` (name + role from the script);
   - a famous artwork or press photo → an F-A thumbnail type card (FB-8), never the artwork.
5. **Record** each moment in `plan/inserts.json`: `{id, moment, origin: "creator" | "created", file?, recipe?, substitute_of?}`.



### 12.6 Frame rate and audio
30 fps CFR output, 1080×1920, BT.709. One voice track (the take): high-pass 80 Hz, de-ess, light compression, −14 LUFS. Plates are silent.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1–13.2 Beat fields
Core fields: `id`, `section` (HOOK | ITEM-n | SEC-n | CTA), `t0`/`t1`, `spoken`, `trigger {word, at}`, `tone`, `line_type`, `layout`, `visual` (one sentence), `layers` (scene ids), `pattern`, `sfx`.
Conditional fields used by this style:

| Switch / module | Beat fields |
|---|---|
| captions (always) | `caption {profile: CS-1 \| CS-2 \| CS-3 \| CS-4, overrides[], emphasis[] (the tier-2 word), tier[]}` |
| running_state | `state_ops [{var: "count", op: "set" \| "tick_to", value, at}]` + `figure_id` |
| footage ≥ medium (F-B) | `shot_id` (SH-…), `clip` (BR-…), `fallback_used` (FB-… or null), `cut: true` |
| grades | `grade` (GR-…), `clip_treatment` |
| third-party moment | `insert {id, origin: creator \| created}` |
| exception | `exception: "E1"` (P-04) or `"E3"` (P-18 micro words) |
| re-hook (F-B) | `rehook: true` on the mid-section marker beat |
| brand | `sponsor {id, disclosure}` (when present) |

```yaml
- id: 14
  section: SEC-2
  t0: 23.40
  t1: 24.10
  spoken: "every month felt tight"
  trigger: {word: "tight", at: 23.86}
  tone: awe
  line_type: feeling
  layout: L-broll
  pattern: P-20
  shot_id: SH-1
  clip: BR-07
  fallback_used: null
  visual: "Back-of-head at the laptop in practical light; 'tight' lands in italic didone at cy 960"
  layers: ["plate-br07-23"]
  caption: {profile: CS-2, emphasis: ["tight"]}
  grade: null
  cut: true
  sfx: []
```

### 13.3 Reel header (top of the edit brief)
`format` (F-A | F-B), `theme` (null), `hook_archetype`, `structure` (list | essay), `count` (items / sections), `markers` (SM-1 | SM-2 | SM-3), `keyword`, `cta_device`, `state` (`count` figures), `bank` (usable clips, fallback FB-…), `cuts_planned` (F-B: the number and the per-minute rate), `sponsor`.

### 13.4 Hook proposals (3)
```yaml
- name: "Promise chip: 10 ways"
  archetype: HA-05
  chip: "10 ways to earn money"
  sub_line: "as a freelance designer"
  hook_pair: {promise: "10 ways to earn money as a freelance designer", proof: "item 1 logo plate by 3.4 s"}
  stoppers: [P-01, P-04]
  captions: {profile: CS-1, tier2: ["each"]}
  storyboard: "f0 chip settling + face | 0.2 sub-line builds | 1.6 '10' behind the head | 3.0 chip blurs up, '1. One-off gigs' + logo plate"
  sound: [f0 soft hit, list cue on 'one']
  stopper_test: {thumbnail: pass, mute: pass, read_s: 1.0, changes_3s: 11, payoff_s: 0.0}
```

### 13.5 Checkpoint (before building)
1. 3 hooks with the stopper-test results.
2. The beat sheet with tones and tier-2 words; F-B: the burst map (cut / hold / frame per content word) and the planned cuts per minute + median shot.
3. The transition map and the SFX ledger (the pack's S1–S6).
4. The state plan (counters → figures) and the inserts record (creator-supplied vs created).
5. The fallbacks used (FB-…), with the bank count.
6. Style stills: f0; the first item (F-A) or the first burst + face return (F-B); one type frame; one proof element; the CTA card + keyword.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE: example]`
Times are estimates; replace them with `words.edit.json` onsets. The personaliser rewrites these for the buyer's niche after their first approved reel of each format (Part D.6).

### 14.1 F-A List overlay · fitness · "7 gym habits that actually build muscle" (34 s, keyword PLAN)
**Reel header:** format F-A · hook HA-05 · structure list · count 7 · markers SM-1 · keyword PLAN · device comment_keyword · state: one counter (`kg`, from: creator) · bank n/a.
**Chip:** "7 gym habits" · sub-line "that actually build muscle" · P-04 "7" behind the head.

| t (s) | Spoken | Tone | Visual | Caption | Camera | Cue |
|---|---|---|---|---|---|---|
| f0 | "Here are seven gym habits…" | hype | Face (L-full) + **P-01** chip "7 gym habits" swinging in and typing (rest f13) + **P-04** "7" behind the head (E1, 0.0–3.2 s) | CS-1 "Here" by f3 | Z-3 pull-out 2.0 → 1.0 (50 f) | f0 soft hit |
| 0.4–1.6 | "…that actually build muscle" | explain | Sub-line types letter by letter at cy 515 | micro; "muscle" tier 2 (110 px) | — | — |
| 1.6–3.0 | "most people skip number four" | explain | Chip + sub-line hold (open loop on item 4) | micro | — | — |
| 3.0 | "One, train close to failure" | explain | T-11 pulse (2.88–3.00) + hidden cut to the item take, chip out, **P-10** "1. Train to failure", **P-05** own training-log photo | micro; "failure" tier 2 | — | list cue |
| 6.2 | "Two, sleep eight hours" | explain | "2. Sleep 8 hours" + P-05 own bedroom-at-night still | "8" tier 1 (70 px) | — | list cue |
| 9.4 | "Three, track every lift" | explain | "3. Track every lift" + **P-07** own tracker screen (blurred account id) | micro | — | list cue |
| 12.6 | "Four, eat protein first" | explain | "4. Protein first" + P-05 own meal photo | "first" tier 2 | — | list cue |
| 15.8 | "Five, progressive overload — I added 12 kilos to my squat" | win | "5. Progressive overload" + **P-30** ring counting 0 → 12 "kg added" (figure `squat_gain`, from: creator), landing on "12" | "12" tier 1 | — | list cue + reveal on landing |
| 19.6 | "Six, deload every sixth week" | explain | "6. Deload week" + FB-8 created type card "deload" (italic didone on cobalt) | micro | — | list cue |
| 23.0 | "Seven, join the people doing it with you" | cta | "7. Join the 6AM club" + **P-45** community card (name, "train, track & grow", 4 own gym photos) | micro | — | list cue |
| 28.8 | "comment PLAN and I'll send you my program" | cta | (0.4 s nothing new) → **P-46** 'PLAN' cream didone at cy 450 (title row exits) | micro; "PLAN" tier 2 | — | cta shine |
| 33.4 | — | — | T-10 hard end on the keyword | — | — | — |

Cadence check: ≈ 100 words → 100 caption SC in 34 s (≈ 29 per 10 s); non-caption SC: 7 item swaps + chip + numeral + counter + card + keyword ≈ 3.7 per 10 s; cuts 0. Inserts: none (all creator photos). Fallbacks: FB-8 for item 6.

### 14.2 F-B Cinematic montage · personal finance · "Two friends, same salary" (62 s, keyword BUDGET)
**Reel header:** format F-B · hook HA-19 · structure essay · 3 sections · markers SM-2 · keyword BUDGET · device comment_keyword · bank 31 clips (full) · cuts planned 28 (27.1/min), median shot ≈ 1.3 s.

**Hook table**
| t (s) | Spoken | Tone | Visual | Caption | Move / transition | Cue |
|---|---|---|---|---|---|---|
| f0 | "Picture this:" | awe | **P-22** rack-focus open on BR-03 (SH-1: back of head at the laptop, night practicals) + **P-19** "Picture this" (96 px) | hidden (P-19) | T-03 | f0 riser end |
| 0.7 | "two friends" | awe | **P-23** split twin of BR-03: top GR-blue-wash, bottom GR-red-wash; "2 friends" on a cobalt chip at the seam | CS-3 | — | — |
| 1.3 | "earn the exact same salary" | explain | cut to BR-11 (SH-2 hands on a payslip) | CS-3; "same" tier 2 | T-01 | burst whoosh |
| 2.0 | "One is broke in a year." | warn | cut to BR-17 (SH-4 silhouette at a window), **P-24** GR-bw + "broke" in red 130 px | red word scene | T-01 | — |
| 3.2 | "Here's why." | explain | **G-2** cut back to the face (L-full), "why." tier 2 italic 160 px | CS-2 | T-01 + Z-1 | — |

**Section plan**
| Section | Spoken (gist) | Patterns (in order) | Cuts |
|---|---|---|---|
| SEC-1 (4.5–19) "No.1 / pay yourself first" | "The first friend saves whatever is left… the second moves 20 % out on payday" | T-01 → BR-05 plate + **P-08** "No.1 / pay yourself first" (1.6 s) → **P-21** burst BR-11, BR-12, BR-14, BR-05b (hands, phone banking app blurred, notebook) → G-2 face (opinion, 4 s, Z-2 push-drift) + **P-30** ring "20 %" (figure from: script) → **P-15** cobalt frame "payday" | 8 |
| SEC-2 (19–36) "No.2 / every month felt tight" (re-hook, `kind: rehook`) | "The first friend says every month felt tight… subscriptions, food apps, upgrades" | T-01 → BR-21 + **P-08** "No.2" → P-20 BR-07 "tight" italic → **P-37** polaroid grid on W-paper "subscriptions" (6 own receipts photos) → burst BR-08, BR-09, BR-22 → G-2 face → **P-28** split with own spreadsheet (blurred numbers not spoken) | 9 |
| SEC-3 (36–52) "No.3 / two years later" | "Two years later, one has a cushion, the other has a card bill" | T-01 → BR-17 + **P-08** "No.3" → **P-14** paper frame "2 years." (italic didone, cobalt) → burst BR-25, BR-26, BR-29 (amber window, GR-amber) → G-2 face → **P-34** toggle "spent / saved" on BR-11 | 8 |
| CTA (52–62) | "I made the budget sheet I use… comment BUDGET and I'll send it" | G-2 face → **P-17** "budget / template" (1.4 s) → **P-45** community card → **P-46** 'BUDGET' | 3 |

Totals: 28 cuts in 62 s = 27.1 / min ✓; grade events: split twin, GR-bw, GR-amber = 3 ✓; presence ≈ 38 % ✓; longest absence 8.6 s (SEC-2) ✓. Inserts: the banking app → the creator's own screen recording (creator); no created inserts.

### 14.3 F-B on a thin bank · fitness · "Getting strong comes down to 3 things" (55 s, keyword PLAN)
**Reel header:** format F-B · hook HA-12 · structure essay · 3 sections · markers SM-2 · bank **16 clips → FB-1 (degraded)**, declared at the checkpoint · cuts planned 25 (27.3/min): 14 plate cuts + 7 type frames + 4 face returns.

| Section | Patterns |
|---|---|
| Hook (0–4) | **HA-12**: W-paper "Getting strong" (P-14) → "comes down" → cobalt chip "to 3 things" (CS-3) → T-01 to the face "Let me show you." |
| SEC-1 "No.1 / show up" | BR-02 + P-08 → burst BR-02b, BR-05, BR-06 (same gym, 3 angles) → face (Z-2) → **P-16** void frame "consistency" |
| SEC-2 "No.2 / eat enough" (re-hook) | BR-09 + P-08 → **P-24** mono "skipping" (red) on BR-05b (reused, different in-point) → face + **P-30** ring "140 g" (figure from: script) |
| SEC-3 "No.3 / sleep" | BR-14 + P-08 → **P-15** cobalt "8 hours" → BR-14b → face |
| CTA | face → P-17 "free / program" → P-45 → P-46 'PLAN' |

Fallback note at the checkpoint: "FB-1: 16 clips; 4 clips reused once with new in-points; 7 type frames carry the rhythm. With 25+ clips this reel gains 2 bursts and loses 3 type frames."

---

## §15 QA checklist `[REQ] [DNA]`
**1. Profile conformance**
- [ ] Format declared (F-A / F-B) and chosen by the §0.4 rule; bank count and fallback stated (V-PROFILE, review).
- [ ] Presence: F-A 95–100 %, never absent; F-B 20–50 %, absence ≤ 10 s (V-PRESENCE).
- [ ] Duration in class: F-A 28–48 s; F-B 45–76 s (review).
- [ ] Layouts only from the format's list, shares in range (V-LAYOUT).

**2. Hook**
- [ ] F-A: chip moving at f0 and first word readable by f6 (or static), ≤ 5 words, 1 line, rest by f14; sub-line ≤ 6 words; item 1 by 4.0 s (V-F0, V-TITLE).
- [ ] F-B: moving plate + one-word element at f0; premise by 3.0 s; face or first section by 6.0 s (V-F0).
- [ ] ≥ 8 (F-A) / ≥ 9 (F-B) weighted SC in 0–3 s (V-CADENCE).
- [ ] Mute test: the promise / premise reads without sound (review).

**3. Body and cadence**
- [ ] SC per 10 s in range; max gap 1.2 / 1.0 s; nothing static > 2.5 / 2.0 s (V-CADENCE).
- [ ] F-A: only the hidden item-1 cut (+ ≤ 1 fix per 30 s, ≤ 2/min), no transitions markers; ≥ 3 non-caption SC per 10 s (V-CADENCE, review).
- [ ] F-B: 26–29 cuts/min, median shot 1.0–1.6 s, cuts on content-word onsets −2 f, bursts 3–6 then a breath (V-CADENCE, V-ONWORD, review).
- [ ] Every item uses the identical ritual; every section opens with its marker; numerals ascend without gaps (V-PROMISE, review).
- [ ] F-B re-hook between 40 % and 60 %, no gap > 35 s (V-REHOOK).

**4. Captions and type**
- [ ] One word per chunk (≤ 2 in CS-3), blur-in swaps, tiers 1× / 1.6× / 2.5× (V-CAPTION).
- [ ] Tier-2 budget: F-A ≤ 1 per 6 s; F-B ≤ 3 per 10 s; never two adjacent; never a stop-word (V-CAPTION, review).
- [ ] Floors: E3 only in CS-1 (46 px) and CS-3 (48 px on a chip), contrast ≥ 7:1 / 4.5:1; everything else ≥ its class floor; nothing clipped (V-TYPE, V-EXC).
- [ ] Spelling of names, tools and brands exact (V-CAPTION glossary).

**5. Modules**
- [ ] §17: every counter bound to a figure, lands ±5 f on the spoken number; shows only script or creator numbers (V-DATA, V-STATE).
- [ ] §25: community card 2.0–4.0 s; keyword quote ≥ 1.5 s and equal to the spoken keyword; sponsor disclosed ≥ 2 s (V-PROMISE, NC-12).

**6. Truth and inserts**
- [ ] Every plate, still and screen is the creator's (origin creator); every third-party moment recorded and either supplied or created (V-INSERTS).
- [ ] Profile pills / tiles show real facts; no invented counts or ticks (V-DATA, review).
- [ ] Personal data on screens blurred (NC-14, review).

**7. Look**
- [ ] ≤ 2 bright hues per frame; cobalt is the only colour carrying words on footage (V-HUES, review).
- [ ] Nothing over the face box; thumbnails ≤ face top − 24 (V-FACE).
- [ ] Grade events ≤ 3, never the same twice in a row, never on the A-roll (review).
- [ ] Colour frames ≥ 0.4 s, ≥ 0.34 s apart, ≤ 1 per second (review).
- [ ] Camera: only Z-1 / Z-2 / Z-3, never repeated in a row, ≥ 0.4 s apart (V-CAMERA).

**8. Sound contract and end**
- [ ] Cues only on allowed moments; list cue the single repeat; no cue on caption swaps; nothing in the 1.0 s before the CTA (S1–S6).
- [ ] Bed ≥ 18 dB under the voice; −14 LUFS; true peak ≤ −1.5 dBTP (NC-8).
- [ ] Ends ≤ 6 f after the last word on the keyword quote; black tail ≤ 0.2 s; 1080×1920, 30 fps CFR (review).

---

## Conditional modules (§16–§25)

### §16 Frame template / persistent chrome
OFF (`modules.chrome = false`): the F-A title row and thumbnail rect are layout bands (§3.5), not persistent slots; content enters and exits with the item ritual.

### §17 Running state & anchored graphics `[COND: modules.running_state] [DNA mechanics]`
- **17.1 State variable:** `count` `{type: counter, start: 0, format: numbers (SW-08), display: P-30, persist: within_beat}`. One per proof moment (views, followers, clients, kilos, savings, days). Ops per beat: `state_ops [{var: "count", op: "tick_to", value, at}]`, where `value` is a `plan/figures.json` value (`from: script` with the spoken words, or `from: creator`).
- **Display rules:** one position per format (L-full centre (540, 520); W-paper centre (540, 760)); the value changes only by rolling 24–36 f; it lands within ±5 f of the spoken number word; it never contradicts the caption.
- **Counts shown by P-32 / P-33** are figures too (`kind: counter`, `formula: none`).
- **17.2 Anchors:** OFF (`modules.anchors = false`); thumbnails and rings use the face box only for their bottom clamp (§3.6).
- **17.3 Validator:** V-STATE (displayed = state; totals = ops) and V-DATA (provenance, landing).

### §18 Data contract
OFF as a module (`modules.data_figures = false`). Counters still write `plan/figures.json` (§17) so V-DATA runs; no charts, bars or computed figures are part of this style.

### §19 Evidence & citations
OFF (`modules.citations = false`). Third-party moments use §12.5.

### §20 Dialogue
OFF (one presenter).

### §21 Canvas camera
OFF (`graphics: support`; PV-5).

### §22 Ink & annotation layer
OFF: no hand-drawn marks in this style (only the P-15 underline, which is a type element).

### §23 Continuity
OFF: no morph chains or motifs; consistency comes from the type duet and the cobalt.

### §24 Series furniture
OFF by default (`modules.series = false`, VAR). If the buyer turns it on: the series tag is the SM-2 numeral language — "No.{n}" in cream didone 120 px at cy 250 for 1.2 s inside the hook (counts toward the intro cap); name and number from the reel brief (BV-13).

### §25 Sponsor, brand & end cards `[COND: modules.brand] [DNA look; VAR assets]`
- **Community card (P-45)** = this style's end card (`brand.endcard.type: lead_magnet`): white card 886×490 at y 290–780, community name (Instrument Serif 64 px), one-line promise (Inter Tight 500 40 px), 3–5 creator images fanned; 2.0–4.0 s; in F-A it is the last item's thumbnail.
- **Keyword quote (P-46):** the comment keyword, ≥ 1.5 s, to the end; never another element on top of it except the chest caption.
- **Follow pill (P-47):** the follow device's end element.
- **Sponsor chip (P-48):** a cobalt chip "with [Brand]" at cy 400 + "Paid partnership" (BV-14 wording) TC-legal 24 px at cy 470, held ≥ 2 s or for the whole segment; the sponsor's logo only as the creator-supplied file, 120 px tall, never over the face; the disclosure is also spoken (NC-12).
- **Rules:** end elements ≤ 4 s in total before the hard end; the keyword readable ≥ 1.5 s; black tail ≤ 0.2 s.

---

## Part C. Declared exceptions and the non-overridable core
- **NC-1…NC-14 apply unchanged** (structure Part C.1): the face is never covered; meaning text never overlaps meaning text; smooth motion; legibility floors; IG UI bands; truth; creator-owned media; audio; determinism; ≤ 4 bright hues (this style: 2); disclosure; quote integrity; redaction.
- **Declared exceptions:** E3 and E1 exactly as §2.2 (`tokens.exceptions`: E3 `{subtitle_min_px: 44, label_min_px: 30, contrast_min: 7.0, pill_contrast_min: 4.5, weight_min: 600, max_lines: 1, max_chars_line: 16}`; E1 `{min_visible: 0.65, max_at_once: 1, min_hold_s: 0.6}`).
- **Scene usage:** P-04 sets `exception: "E1"` and `behind: true`; P-18 sets `exception: "E3"` (its micro words); captions inherit E3 from CS-1 / CS-3.
- **Buyer switches:** turning E1 off (no behind-head numeral) or E3 off (CS-4 as the F-A default) is VAR. No new exception may be added without a DNA deviation.

## Part D. Personalisation
- **Asked at setup (one round):** BV-01 name and handle (the profile pill, the follow pill, the handle line); BV-02 one or two colours → `primary` (the cobalt role) and `accent` (the proof violet), contrast-nudged; BV-05 language (en → en, Hinglish → Hinglish Latin, Hinglish → English); BV-08 the CTA device and keyword (default comment keyword).
- **Defaulted:** fonts within their classes (BV-03); niche (BV-04, per reel); number format from the language (BV-06); formats enabled (BV-09, both); sponsor wording (BV-14); never-on-screen list (BV-15); the community card's images (BV-16).
- **Lock map highlights:** DNA — the duet mechanics and tier rule, the chip recipe, one blue, the F-A zero-cut rule, the F-B cut rhythm, the marker styles, the layouts. TUNE — caption sizes (CS-1 44–54, CS-2 58–72), chip size 92–116, title 80–104, cadence ±15 %, F-B cuts/min 22–34, median shot 0.8–2.0 s, motion ±15 %, grades, presence share ±10. VAR — colours of `primary` / `accent`, language, numbers, CTA device and keyword, sound, setups, series and brand modules on/off.
- **NICHE slots** filled per reel (D.6): §6.4 hook pairs, §8.4 lookup rows, §14 (replaced by the first approved reel of each format), App. A, the glossary.
- **Learned feedback** (`veos learn add`): "bigger captions" → CS-1 size within 44–54 (TUNE), above 54 → CS-4 (allowed alternative, no deviation); "more cuts" → F-B cuts/min within 22–34; "no cuts in the montage" → a DNA change (warn and record DV-n, or suggest F-A).

## Part E. What this template changes vs the coverage tables and the structure
| Item | Coverage / structure said | This template | Why (evidence) |
|---|---|---|---|
| F-B `source_type` | `narrated_footage` | `talking_head` + spine `audio` + footage `high` | The voice is the desk take in every montage (v01 @0:14, v02 throughout, v05); the card line becomes "you + your own B-roll" |
| F-B presence | host (20–50) | guest, share 20–50 | 20–50 % sits mostly in the guest band (v01 ≈ 20 %, v05 ≈ 35 %, v02 ≈ 50 %) |
| F-A micro caption size | 36 px | 44 px | measured 29–32 px at 720 p (≈ 44–48 px at 1080, v03 @0:00–0:03, v04 @0:00–0:03); 44 keeps the quiet look with better legibility |
| Exceptions | E3 | E3 + **E1** (≤ 1 per reel, hook only) | v05 @0:00–0:04 "101" and v02 @0:04 "BY STEP" sit behind the head |
| Cadence SC/10 s | F-A 4–6 | F-A 18–45 (+ ≥ 3 non-caption SC per 10 s by review) | captions are primary (weight 1.0) and one word per chunk, so word swaps dominate the count; the coverage figure is the non-caption floor |
| Notification pill colour | red (v01 @0:07) | `accent` violet | `bad` red is fixed to "the mistake" in this palette |
| Level panel text | white on green (v02 @0:12) | `ink` on green | white on `#2CFF4E` fails contrast (1.3:1) |
| Captions over the chin | v02 @0:02.5, v05 @0:34 | never (H7) | NC-1 |
| Stock / famous art stills | v02, v03, v04, v05 | creator-owned only; created type cards otherwise | NC-7 |
| §9.3 shot grammar | COND on spine footage / hybrid | ON for F-B by declaration | the montage cut grammar is the format's DNA |

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D / BD | D1–D8 / BD… (buyer) |
| H, N, BN | H1–H18, N1–N14, BN… |
| E | E1, E3 |
| W | W-room, W-plate (archive via L-broll), W-paper, W-cobalt, W-void |
| L | L-full, L-low, L-broll, L-type, L-split |
| G | G-1 cut to plate, G-2 cut back to face, G-3 cut to split, G-4 colour-frame flip, G-5 lower for room |
| GR | GR-bw, GR-red-wash, GR-blue-wash, GR-amber |
| CS | CS-1 micro duet, CS-2 montage duet, CS-3 chip duet, CS-4 micro safe |
| HA | HA-05 (F-A default), HA-19 (F-B default), HA-12, HA-02, HA-14 |
| SM | SM-1 "n. Title", SM-2 "No.n", SM-3 "step n" |
| B | B-1…B-9 |
| P | P-01–P-05, P-06–P-10, P-11–P-19, P-20–P-29, P-30–P-40, P-45–P-48 (44 patterns) |
| T, R | T-01–T-11 (T-11 blur pulse), R-1–R-8 |
| Z | Z-1 snap-punch, Z-2 push-drift, Z-3 pull-out |
| SH, FB | SH-1–SH-9; FB-1, FB-1b, FB-5, FB-7, FB-8, FB-9 |
| F | F-A, F-B |
| V-… | V-PROFILE, V-F0, V-CADENCE, V-REHOOK, V-ONWORD, V-SAFE, V-FACE, V-PRESENCE, V-CAPTION, V-TYPE, V-EXC, V-HUES, V-LAYOUT, V-TITLE, V-CAMERA, V-PROMISE, V-NUMFMT, V-DATA, V-STATE, V-INSERTS |

---

## App. A Headline & hook bank `[NICHE]`
Slots: `[N]` a count, `[niche]` the buyer's field, `[role]` the audience, `[result]`, `[year]`, `[thing]`. Tagged with the archetype. Fitness / finance fillings in brackets.

**F-A List overlay (chip + sub-line)**
| # | Chip | Sub-line | Archetype |
|---|---|---|---|
| 1 | "[N] ways to earn money" | "as a [role]" (freelancer) | HA-05 |
| 2 | "10/10 [niche] habits" (gym) | "you need to lock in today" | HA-05 |
| 3 | "[Skill] better 101" (Saving money 101) | "for your first [thing]" (salary) + "101" behind | HA-05 |
| 4 | "[N] [niche] mistakes" (5 fat loss mistakes) | "I made for [N] years" | HA-05 |
| 5 | "[N] tools I use daily" (7 money apps) | "and what they replaced" | HA-05 |
| 6 | "[N] rules for [result]" (5 rules for lean bulking) | "nobody tells you" | HA-05 |
| 7 | "[N] signs you're [state]" (6 signs you're overspending) | "and the fix for each" | HA-05 |
| 8 | "My [N]-step [routine]" (My 6-step morning routine) | "after [N] years of trying" | HA-05 |
| 9 | "[N] things to stop doing" (5 things to stop buying) | "if you want [result]" | HA-05 |
| 10 | "[N] questions before you [act]" (7 questions before you invest) | "save this one" | HA-05 |

**F-B Cinematic montage (opening line + first type beat)**
| # | Opening (P-19 / chip / first frame) | Premise by 3 s | Archetype |
|---|---|---|---|
| 1 | "Picture this:" | "two [people] doing the same [thing] for [N] months" (two lifters / two friends) | HA-19 |
| 2 | "Picture this:" | "you start [thing] today; here's [year]" | HA-19 |
| 3 | paper "[Result]" → "comes down" → chip "to [N] things" | (Getting strong / Being broke) | HA-12 |
| 4 | paper "[N] years." (italic) | "that's how long [thing] took me" | HA-12 |
| 5 | typed chip "[Skill] better" + "101" behind | "you want to [goal] but don't know where to start" | HA-05 |
| 6 | "[Result] in [year]" + card wall of own work | "isn't hard." | HA-02 |
| 7 | face: "Most people **quit** at week [N]" | the strongest plate by 1.0 s | HA-14 |
| 8 | face: "Your [thing] isn't the **problem**" | (salary / program) | HA-14 |
| 9 | "Picture this:" over a silhouette plate | "[N] people want [goal]; one gets it" | HA-19 |
| 10 | paper "[step] by step" stacked | "here's my exact process" | HA-12 |

## App. B Evidence map (summary; the full map with timestamps is `evidence.md`)
| DNA element | Evidence |
|---|---|
| Two formats: list overlay (0 cuts) / montage (26–29 cuts/min) | v03, v04 (0 cuts); v01 28.8, v02 26.2, v05 26.1 cuts/min (`meta.json`) |
| Cobalt chip title + serif sub-line at cy ≈ 400 / 515 | v03 @0:00–0:03, v04 @0:00–0:04, v05 @0:00–0:04 |
| One-word duet captions, size by importance, blur-in | v01–v05 throughout; v02 @0:00–0:03 ("Creating", "isn't") |
| Micro chest captions ≈ 44–48 px at cy ≈ 1130 | v03, v04 |
| "n. Title" italic serif at cy ≈ 250 + photo card at y ≈ 300–760 over the head | v03 @0:03–0:33, v04 @0:04–0:28 |
| "No.n" section cards; "step n" numerals | v01 @0:37, v05 @0:10, @0:21, @0:34; v02 @0:08–0:37 |
| Type frames (paper, cobalt, void) | v01 @0:12–0:13, @0:25–0:28, @0:55–0:57; v05 @0:08–0:09, @0:19–0:20, @0:30–0:31 |
| Split twin grade, B&W + red word | v01 @0:00–0:08, @0:10–0:11 |
| Counter ring, profile pill / tile, notification pill, toggle, card wall | v03 @0:24, @0:30; v01 @0:07, @0:42–0:47; v02 @0:00.6–0:02.3, @0:09–0:11; v05 @0:27 |
| Community card + quoted keyword CTA | v04 @0:25–0:28; v01 @1:02–1:06; v02 @0:51–0:54 |
| `(unverified)` | speech language (no transcripts), sound (not observable), the F-B voice source |
