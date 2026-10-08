# Tech Countdown Style Playbook (template v1)

**Purpose.** This playbook makes the editor (Claude) turn {{BV-01.name|the creator}}'s talking-head take into a premium tech-news reel of 90–170 s: a numbered countdown of tools, features or launches (F-A), or a one-story "Day N" brief (F-B). Every sentence is subtitled in a small pill with one italic-serif emphasis phrase, every item opens on a giant lime-and-white `#NN` numeral, every tool appears as a branded card over the dimmed presenter, and the reel ends on a Save → Follow → Community stack.
**Input (SW-01 `talking_head`):** one A-roll take of the presenter (seated or standing), plus a screen recording per item (SH-1) and optional logos, product B-roll and the creator's own post/clip for the borrowed-post hook. Missing material follows §12.3 and §12.5.

**Style DNA** `[DNA]`. A calm, expensive tech-news desk. The presenter talks from a warm, tidy room; the words sit under the chin in a small rounded pill, and one phrase per thought is promoted to a large white *italic serif*. Items are announced by a giant `#NN` numeral at chest height (white `#`, lime digits) with a small white italic chip above it; then the presenter blurs and darkens and the tool slides in as a card: logo + name row, a rounded window with the real screen recording, the caption pill under it. B-roll lives in the top half of a 50/50 split with the caption sitting exactly on the seam. A "Welcome to Day 60" series card closes the intro, warm orange washes separate sections, and a dark-green community card with a lime "Link in Bio" pill ends it. No memes, no shakes, no stickers: authority comes from evidence on screen.

**Copy these 5 things** (they make it read as this style at a glance):
1. **Small captions + one huge italic-serif phrase** (CS-1, §5.3): an emphasis chunk is bare white sans (60 px, soft shadow) with one 2–4-word phrase blown up to ≈ 116 px Instrument Serif Italic, the plain words split around it. Plain-only chunks are a small 44 px black pill in TH-studio (v01 @1:13.95 "It's called shortcuts") and bare 60 px white that types on character by character in TH-lime (v03 @0:17.6, @2:33.7). The seam (CS-1S) and the tool card (CS-2 lime) keep their small pills. *(Motion audit 2026-10, full frame rate.)*
2. **The `#NN` numeral with a chip** (SM-NUM, §7.2): 300 px numeral at chest (cy ≈ 1070), white `#` + lime digits (or a lime hash + white condensed digits in TH-lime), an italic label/teaser chip above it (cy ≈ 866).
3. **The tool card over the dimmed presenter** (P-TOOL-CARD, §8.3): footage blur 12 px, luma −50 %; brand row at y 660–720; a 972 × 540 window at y 740; the lime caption pill under it at cy 1343; the tool's logo behind the head for the first 1–2 s.
4. **The 50/50 split with the caption on the seam** (L-split, §3): graphic or B-roll y 0–960, presenter y 952–1920, a 140 px black fade above the seam (v02) or a hard 2 px dark seam line (v01), the small seam caption (CS-1S, 42 px, 65 % black pill) centred on y 952.
5. **Series card + Save/Follow/Community end stack** (§24, §25): "Welcome to / *Day 60* / of …" at 8–15 s; the end runs Save badge → Follow line → deliverable line → community card with a lime Link in Bio pill.

**Directives** `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Evidence on screen.** Every tool, feature, number or claim gets its visual: the real recording, a card, a note card or a stat line. Never just a talking head saying a product name | §8, H6 |
| D2 | **Premium calm, fast doors.** No meme layer, no shakes, no stickers, no rotation. Inside a beat everything holds still; the energy lives in the doors between beats: the warm light-leak flash, the rush-in zoom that starts on its cut, the smear wipes (§9) | §9, §10, N1–N2 |
| D3 | **Countdown identity.** Every item opens with the same `#NN` ritual; the numbering direction and the count are promised in the intro and paid off | §7.2–7.3, H9 |
| D4 | **Every sentence is subtitled** in the pill; exactly one phrase per thought becomes italic serif | §5.3, H11 |
| D5 | **Series identity.** A "Day / Week N" card closes the intro; the end stack asks for Save, Follow and the community | §24, §25 |
| D6 | **One skin per reel.** TH-studio (black pill, white # + lime digits) or TH-lime (lime pill, lime hash + white digits); never mixed | §4.3 |
| D7 | **The presenter is the anchor.** Dimmed, split or full, the face is on screen ≥ 75 % of the runtime; only the borrowed-post hook may leave it, for ≤ 8 s | §3.6, H8 |
| D8 | **Re-hook every ≤ 25 s.** A numeral, a teaser chip or an italic-serif question lands at least every 25 s | §7.4, H10 |

Buyer directives (`BD1…`) are added below this table `[VAR]` and may only make the style stricter or more specific.

**Quick index**
| § | What | Status |
|---|---|---|
| §0 | Style profile | ON |
| §1 | Procedure | ON |
| §2 | Hard rules, exceptions E1 + E3 | ON |
| §3 | Worlds, layouts (L-full, L-split, L-card, L-board), stage moves | ON |
| §4 | Colour, themes TH-studio / TH-lime | ON |
| §5 | Type, plate headline, caption profiles CS-1 / CS-2 | ON |
| §6 | Hooks: HA-02 default, HA-18, HA-12, HA-05 | ON |
| §7 | Structure (news countdown / explainer), markers, ritual, re-hooks, cadence | ON |
| §8 | Visual system: 36 patterns | ON |
| §9 | Transitions T-1…T-10 | ON |
| §10 | Motion, rush-in camera, layers | ON |
| §11 | Sound contract | ON |
| §12 | Footage, shot list, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA | ON |
| §16 | Frame template / chrome | OFF |
| §17 | Running state & anchors | OFF |
| §18 | Data contract | OFF |
| §19 | Evidence & citations | OFF |
| §20 | Dialogue | OFF |
| §21 | Canvas camera | OFF |
| §22 | Ink | OFF |
| §23 | Continuity | OFF |
| §24 | Series furniture | ON |
| §25 | Sponsor, brand & end cards | ON |
| Parts C–F | Exceptions, personalisation, changes, IDs | ON |
| App. A | Headline & hook bank | ON |
| App. B | Evidence map (see `evidence.md`) | ON |

Formats: **F-A Countdown** (default) · **F-B Daily brief**.

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile
  source_type: talking_head
  presenter: {presence: anchor, share: [75, 95], max_absence_s: 8}
  spine: talking_head
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: support
  duration: {class: long, target_s: [90, 170]}          # F-B overrides: standard [70, 100]
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0, style: short}
  tone: {energy: calm, comedy: off, comedy_max: off}
  themes: {policy: per_reel, packs: [TH-studio, TH-lime], default: TH-studio}
  formats: {list: [F-A, F-B], default: F-A}
  footage_dependency: medium
  cta: {devices: [follow_save_stack, link_bio, comment_keyword, end_card], placement: end}
  modules: {chrome: false, running_state: false, anchors: false, data_figures: false, citations: false,
            dialogue: false, canvas_camera: false, ink: false, continuity: false, series: true, brand: true}
```

Why each value:
- **source_type `talking_head`**: all three reference reels are one presenter on a tripod (v01 standing with a handheld mic, v02/v03 seated at a desk); the extra inputs (recordings, logos, one borrowed clip) are inserts.
- **presenter `anchor` 75–95 %, max absence 8 s**: the face is visible (full, split or dimmed) ≈ 80–85 % of runtime; the only long absence is v03's borrowed-clip hook (0:00–0:08). In the body no absence exceeds 4 s (H8).
- **spine `talking_head`**: the A-roll is the timeline; every visual is inserted on its sentence.
- **captions `full` / `support` / `mute_safe`**: every spoken word is subtitled (v01–v03), but the captions are small and the cards carry the meaning.
- **graphics `support`**: tool cards, splits and numerals cover ≈ 45–60 % of runtime (v01 ≈ 45 %, v03 ≈ 60 %), illustrating rather than carrying the argument.
- **duration `long` 90–170 s**: evidence 89–179 s (mean ≈ 144 s). F-B (v02, 89 s) is `standard` 70–100 s.
- **language**: on-screen text is English in all three; the speech language is **(unverified)** (no transcript), so the template ships three language options (English, Hinglish, Hindi) and the buyer picks one (BV-05: {{BV-05.speech|en}} speech, {{BV-05.captions|en}} captions).
- **numbers international, `$`, k_m_b**: the default for English speech (BV-06); a buyer who picks Hinglish or Hindi gets Indian grouping, `₹` and lakh/crore (v03 shows `₹0`, v01 shows `₹2,54,900` inside a recording).
- **tone calm, comedy off (max off)**: no meme layer, stickers or shakes in any reel.
- **themes `per_reel`**: the caption skin is chosen per series: black pill (v01, v02) or lime pill (v03). Both packs exist; one per reel.
- **formats F-A + F-B**: v01 and v03 are numbered countdowns; v02 is a single-story "Day 60" brief with no numerals. They share the caption profile, split, series card and end card (4 of the 5 traits), so they are one style with two formats. *(The coverage table lists one format; this split is a deliberate, evidence-based deviation: v02 has no numbered items.)*
- **footage_dependency `medium`**: the style needs the creator's screen recordings and logos; B-roll is optional.
- **cta**: Save → Follow → Community (link in bio) end stack (v03 @2:30–2:41, v01 @2:45, v02 @1:26); v01 also ends on a "Comment below" question card, so `comment_keyword` is allowed.
- **modules**: `series` (Day/Week card) and `brand` (end stack, sponsor row) on; everything else off (§16–§23 below).

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

The craft of this style is **item → card pairing** (P8b): every item gets a numeral, a chip, a logo moment and a card whose screens change on the spoken features; and **emphasis-phrase picking** (P5b): one phrase per thought, 2–4 words, the one a viewer would quote.

1. **P1 Inventory.** `ffprobe` every input. Identify the setup (§12.1: A seated / B standing). Conform VFR to 30 fps CFR. Register every asset with its origin: `creator` (their recordings, logos they hold, their own post) or `created` (§12.5). Note each recording's resolution (≥ 1080 px wide for a full card window).
2. **P1b Tool inventory** `[F-A]`. List the items in spoken order: number, tool/feature name exactly as the product spells it, its recording file (SH-1), its logo file (SH-3) or `none`, its 2–3-word label (from the script), and the 2–4 features said about it (each becomes a screen swap).
3. **P2 Prepare.** Matte only when the reel uses P-LOGO-BEHIND, P-SAVE-BADGE or P-DELIVERABLE-TILE (behind-the-head elements). Otherwise no matte.
4. **P3 Transcribe** with word timestamps. Apply `language.captions.transform` (verbatim for English; translate for Hinglish speech with English captions; product names stay verbatim). Add every tool and brand name to the glossary **with its exact product casing** ("MiniMax", "n8n", "Midjourney").
5. **P4 Segment** into `HOOK`, `INTRO` (promise + teaser), `SERIES`, `ITEM-n` (F-A) or `BEAT-n` (F-B), `PAYOFF`, `CTA`. Mark jump-cut points on word boundaries (±1 f).
6. **P5 Classify** every sentence with a line type (§8.4) and its trigger word (the tool name, the number, the feature verb).
7. **P5b Emphasis pick.** For each thought (≈ every 4–8 s), choose the one phrase of 2–4 words (≤ 22 characters) that becomes italic serif. Prefer the tool's benefit ("completely free"), the twist ("nobody is talking"), the number with its noun ("in just 60 seconds"). Never a stop-word phrase, never two in one chunk. Write them as `captions.overrides` `{i, emph: true}` / `{i, emph: false}`.
8. **P6 Tone-tag** every sentence: `explain` · `awe` · `warn` · `win` · `cta` (no `mock`: comedy is off).
9. **P7 Hook plan.** Pick the archetype (§6.2–6.3) by what the creator supplied: a proof image or prop → HA-02; their own viral post + a clip they hold → HA-18; cinematic B-roll of one story → HA-12 (F-B); a tools roundup → HA-05. Write **3 hook variants** with plates/lockups (§6.5) and run the stopper tests (§6.1).
10. **P8 Visual plan.** One pattern per line from §8.4; per item the ritual of §7.3; the re-hook map (§7.4: a numeral, teaser or italic question every ≤ 25 s); the inserts list (§12.5).
11. **P8b Item → card pairing** `[F-A]`. For each item: numeral variant (SM-NUM-A for TH-studio, SM-NUM-B for TH-lime), chip text (label / teaser / recap), logo moment (creator logo or monogram), card screens (one per spoken feature, swapped on the feature word), the cursor box on the one UI element that is clicked or named, and the pop-back line with its emphasis phrase.
12. **P9 Beat sheet** (§13): one beat per trigger, meeting the cadence of §7.6.
13. **P10 SFX ledger** (§11) and the transition map (§9).
14. **P11 Assets.** Build or collect them; resolve fallbacks (§12.3) and list which were used.
15. **P11b Series metadata** (§24): series unit and number from the reel brief (`Day 60`, `Week 09`), or the count-card fallback.
16. **P11c Sponsor check** (§25): only for a paid integration: the logo asset, the disclosure line, its positions.
17. **P12 Checkpoint** (§13.5), then **wait for approval.**
18. **P13 Build** act by act; `veos validate` (global checks + `validator.rules`); preview and QA (§15, at most 3 passes); render.

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The nine editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show what's being said; never fake facts; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| E-id | This style's limits (never looser than the registry) | DNA reason | Evidence |
|---|---|---|---|
| **E1 Behind-subject type** | Only the **monogram** of a created logo plate (P-LOGO-BEHIND, P-DELIVERABLE-TILE) may sit behind the head; `TC-display` ≥ 120 px; ≥ 65 % of the glyph area visible for the whole hold; first and last letters ≥ 50 % visible; ≤ 1 at a time; hold ≥ 0.6 s; the letters' centre ≥ 40 px above the head top at the scene's first frame. A creator-supplied logo image behind the head is **not text** and needs no exception, only `behind: true` | The logo-behind-the-head entry is the signature of every item in v03 | v03 @0:24, 0:45, 0:56, 1:06, 1:17, 1:29, 1:44, 1:55, 2:09; @2:30 save badge, @2:38 tile |
| **E3 Quiet type** | Seam and card captions (CS-1S, CS-2) 40–53 px (default 42); full-frame CS-1 is 60 px and does not use E3, weight ≥ 500, ≤ 3 lines per chunk (1 italic line + up to 2 plain lines), ≤ 30 characters per line, contrast ≥ 7:1 on bare footage or ≥ 4.5:1 inside the pill. Labels 32–39 px only when `redundant: true`. Display stays ≥ 40 px | The small pill caption under a big italic phrase is the look; 54 px plain text reads as a different style | Measured 38–42 px plain captions at 1080 (v01 @0:02 "Apple just launched one", v02 @0:00 "One image gen AI company just", v03 @0:57 lime pill) |

Each scene that relies on one sets `exception: "E1"`; captions inherit E3 from CS-1/CS-2.

### 2.3 Style MUST rules
- **H1 Frame 0.** The archetype's f0 is fully built on frame 0: HA-02 = plate (both lines readable) + proof card + presenter; HA-18 = post header + the clip playing; HA-12 = moving B-roll in the split + the first caption by 0.33 s; HA-05 = presenter + the italic lockup readable by 0.7 s. `check: V-F0`
- **H2 Cadence.** Body: 4–8 weighted state changes per 10 s (captions weigh 0.5); no gap > 2.5 s between weight-1 changes; nothing static > 2.5 s; hook ≥ 4 weighted SCs in 0–3 s. `check: V-CADENCE`
- **H3 Payoff.** The proof (card, product, clip, B-roll subject) is on screen by 2.5 s (HA-02, HA-18), the thesis readable by 3.0 s (HA-12), the lockup by 0.7 s (HA-05). `check: V-F0`
- **H4 Headline limits.** The plate is ≤ 9 words on exactly 2 lines (line 1 ≤ 5 words, line 2 ≤ 4 words), reads in ≤ 1.5 s and lives only in the hook (2.5–8 s). An italic lockup (HA-05) is ≤ 8 words on ≤ 2 lines. `check: V-TITLE`
- **H5 Dead air.** At most 1 gap ≥ 150 ms per 15 s in the A-roll; jump cuts on word boundaries ±1 f. A pause ≤ 0.6 s may hold the last caption chunk (`pause_hold_s`). `check: review`
- **H6 On the word.** Every numeral lands 2 f before its ordinal/number word and is settled within ±5 f; every tool card's brand row lands within ±2 f of the tool's name; every screen swap lands on its feature word ±5 f. `check: V-ONWORD`
- **H7 Face rule.** Nothing is drawn in front of the face box. The chip's top edge sits ≥ 40 px below the chin (chip cy = max(866, chin + 76)); the numeral sits under the chip; behind-the-head elements stay behind the matte. `check: V-FACE`
- **H8 Presence.** Presenter visible ≥ 75 % of runtime (dimmed under a card counts); the longest absence ≤ 8 s and only in the HA-18 hook; anywhere else ≤ 4 s. `check: V-PRESENCE` (8 s) + `review` (the 4 s body rule)
- **H9 Promise integrity.** The count said or shown in the intro equals the numerals shown; the numbering runs without gaps in one direction (desc 10 → 01 or asc 01 → 10); a teaser chip's "next NN" equals the items left; every "I'll share the links" is paid by the deliverable line and the community card; a comment keyword is on screen ≥ 1.5 s. `check: V-PROMISE`
- **H10 Re-hooks.** Intro (hook + promise + series card) ≤ 15 % of runtime; after it, a re-hook (numeral, teaser chip, italic question) at least every 25 s until the CTA. `check: V-REHOOK`
- **H11 Captions.** Every spoken word is captioned with CS-1 (TH-studio) or CS-2 (TH-lime); ≤ 1 emphasis phrase per chunk and ≤ 1 per 4 s; brand names spelled exactly as the product spells them (the reference reel shipped "elevanlabs": that is a QA fail here). `check: V-CAPTION`
- **H12 Layouts.** Only L-full, L-split, L-card and L-board; shares inside §3.2; no L-card run longer than 14 s without a screen swap; L-board ≤ 4 s per run except the HA-18 hook. `check: V-LAYOUT` (+ `review` for the run limits)
- **H13 Exceptions.** Monograms behind the head follow E1; captions follow E3; nothing else bends a G-rule. `check: V-EXC`
- **H14 Inserts.** Every third-party moment (another company's UI, logo, post, clip, product photo) is creator-supplied or a created substitute, with its record in `plan/inserts.json`. `check: V-INSERTS`
- **H15 Numbers.** Every number on screen is spoken or part of the creator's own recording, written in the buyer's number format (BV-06). `check: V-NUMFMT`
- **H16 Truth.** Prices, dates, model sizes and claims come from the script or the creator; a created UI; no invented benchmarks. `check: review`
- **H17 Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice, hard end ≤ 6 f after the last word (NC-8). `check: review` (mix QA)
- **H18 Determinism.** Every frame a pure function of its index; seeded randomness only (NC-9). `check: review`

### 2.4 NEVER list
- **N1** Meme sounds, stickers, stamps, freeze-frame roasts, emoji in captions or chips.
- **N2** Shakes, rotation snaps, whip pans, punch-ins mid-sentence; any zoom that does not start on a cut. The only camera moves are the Z-1 / Z-2 rush-ins under a wash and Z-3's slow drift (§10.2).
- **N3** Raw full-bleed screen recordings over the presenter for more than 4 s. Recordings live in the card window, the split top or the L-board phone mock.
- **N4** Two emphasis phrases in one chunk; emphasis on a stop-word phrase ("and then", "of the").
- **N5** Coloured words inside the caption pill (the pill is one colour; emphasis is size + serif, never colour).
- **N6** Lime on lime: no lime chip on a CS-2 pill line, no lime text on the lime Link in Bio pill.
- **N7** Glowing robot brains, Matrix rain, random stock "AI" footage, hooded hackers. Show the product, the UI or a created diagram.
- **N8** A fetched logo, screenshot, tweet or clip (NC-7); a fake product UI presented as the real one (NC-6).
- **N9** A brand's colours on anything that is not that brand's logo (created logo plates stay on the neutral `tile`).
- **N10** More than 3 bright hues in one frame (lime + red + one brand logo at most).
- **N11** A black tail > 0.2 s; an outro louder than the voice.
- **N12** The plate outside the hook; the series card after 15 s; two numerals on screen at once.
- **N13** Text on text: a caption under the numeral or the series card (captions hide under z8), a chip over the brand row.
- **N14** A numeral or tool card the speech hasn't reached yet (no early reveals, except the HA-05 teaser tiles).

Buyer additions `BN1…` go here `[VAR]`.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-studio** | footage | The presenter's own room: warm key + practicals (lamp, shelves, plaques), mid-chest framing, never regraded | Claims, opinions, numerals, series card, end-stack lines | Hard cut; dim on/off (8 f) |
| **W-void** | void | `#000000` | The HA-18 borrowed-post hook; P-FRAMED-CLIP (a rounded clip on black with italic lines) | Hard cut in; warm wash (T-2) out |
| **W-board** | canvas | Vertical two-stop gradient: TH-studio warm `#E9773C → #F6C9A5`, TH-lime cool `#2F7FD8 → #7FD8E6`, noise 0.03, one soft darker glow blob drifting ±40 px over the hold (v01 @1:14.2–1:14.6) | A full-screen phone or browser mock showing a flow (P-PHONE-BOARD) | **Hard cut in** (v01 @1:14.20); out by **T-12 zoom-through** into the phone's screen (v01 @1:17.68–1:17.93) |
| **W-wheel** | behind-matte stage | The presenter cut out over a radial "tool wheel": a 4–6-segment colour wheel (category names from the script) behind the head, ringed by rows of small app tiles radiating to the edges, on deep purple | The promise beat after the series card (v03 @0:17.4–0:22.6, ≈ 5 s, once per reel, F-A TH-lime) | **T-5** in (zoom-through into the wheel); out with radial white speed lines + T-2 |
| **W-endcard** | stage | `#050B06` with a lime dot grid (pitch 26, r 1.6, 10 %), one 620 px lime glow at (540, 520) drifting ±14 px, vignette 0.35 | The community card (P-COMMUNITY-CARD) only | Warm wash (T-2) in; hard end |

### 3.2 Layout library
| ID | Engine | Presenter | Graphic | Caption | Treatment | Share F-A | Share F-B |
|---|---|---|---|---|---|---|---|
| **L-full** | `full` | Full frame; head top y 300–460 (setup A) / 220–380 (B); chin ≈ 760–880 (A) / 700–820 (B) | Chest band x 64–1016, y 760–1500 for numerals, chips, note cards, logo pops | `fixed_y` cy **1080** (chest; measured block centres 1047–1121) | none | 30–50 % | 35–60 % |
| **L-split** | `stack`, seam_y **952** | Bottom band y 952–1920, face centred (eye line ≈ y 1220–1300) | Top band y 0–952: B-roll, recording, created UI, stat line | `seam`: CS-1S centred on y 952 | black fade 140 px above the seam (side top), no hairline | 15–35 % | 25–50 % |
| **L-card** | `full` + dim | Full frame dimmed: blur 12 px, luma −0.50 (face still recognisable) | Brand row y 660–720; window x 54–1026, y 740–1280 (972 × 540, 16:9); behind-head logo y 150–560 | `fixed_y` cy **1343** (CS-2 lime pill under the card; measured v03 @0:27, @0:50) | `dim {blur_px 12, luma −0.5}` | 20–50 % | 0–15 % |
| **L-board** | `hidden` | none | x 64–1016, y 120–1340: phone mock (centred, 600 × 1210) or clip | `fixed_y` cy **960** (the pill sits over the phone's screen, v01 @1:14.3, @1:17.6) | world W-board / W-void | 0–8 % (+ the HA-18 hook) | 0–12 % |

The token shares are wide (`[0.25, 0.65]`, `[0.15, 0.55]`, `[0, 0.55]`, `[0, 0.15]`) so one token set serves both formats; the per-format columns above are the editor's targets, checked at review.

**Layout schedule rule.** L-full runs 1.5–6 s; L-split runs ≤ 8 s (swap the top content every 1–3 s inside it); L-card runs 6–14 s per item with a screen swap every 2–3.5 s; L-board ≤ 4 s. Switch layouts on a trigger: an ordinal ("number seven", "next"), a tool name, "look", "here's", a number, or a sentence start.

### 3.3 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | Cut to split | `via: cut` into L-split on the word; band, seam and the seam caption are complete on the cut frame; the bottom band re-frames the presenter (v01 @0:01.85, @0:25.30) | Default (≈ 85 % of split entries) |
| **G-2** | Slide-down split | `via: slide-down`, 9 f | Rare (≤ 1 per reel): a split entered mid-sentence |
| **G-3** | Dim under card | **T-11 smear wipe** (3 f) carries the numeral out and leaves the brand row + window complete; then `via: dim` ramps blur 0 → 12, luma 0 → −0.5 over **12 f** (v03 @0:24.55–0:24.95) | Into every tool card |
| **G-4** | Undim | Hard cut (default) or `via: dim` 8 f back; the card leaves with the cut | Back to the presenter for the opinion line |
| **G-5** | Cut to board | `via: cut` (v01 @1:14.20); out by T-12 zoom-through | Into a full-screen phone flow |
| **G-6** | Slide-up split | `via: slide-up`, 9 f; hard cut is the default | Leaving a split when the next beat is L-full |

### 3.4 Layout diagrams
```
L-full (numeral beat)              L-split                            L-card (tool card)
┌──────────────────────┐ 0         ┌──────────────────────┐ 0         ┌──────────────────────┐ 0
│ IG top UI  y 0-110   │           │ B-ROLL / RECORDING   │           │  [LOGO behind head]  │ y 150-560
│                      │           │ top band y 0-960     │           │      (head)          │
│      (head)          │ y 300-460 │                      │           │ ◼ Tool name          │ y 660-720
│      (face)          │           │ ░░ fade 820-960 ░░░░ │           │╭────────────────────╮│ y 740
│   ╭─chip─╮           │ cy 866    │ ▬ caption on seam ▬  │ y 952     ││  WINDOW 972 × 540  ││
│    #07               │ cy 1056   ├──────────────────────┤           ││  recording         ││
│  (chest)             │           │  (presenter face)    │ y 1220    │╰────────────────────╯│ y 1280
│ ▬ bare caption ▬     │ cy 1080*  │                      │           │   ▬ lime pill ▬      │ cy 1343
│                      │           │                      │           │  (dimmed presenter)  │
│ IG bottom UI >1540   │           │ IG bottom UI >1540   │           │ IG bottom UI >1540   │
└──────────────────────┘ 1920      └──────────────────────┘ 1920      └──────────────────────┘ 1920
* captions are hidden while the numeral (z8) is up.
```

### 3.5 Safe zones and bands
- Meaning text stays inside x 64–1016, y 110–1500 (NC-5: nothing meaningful above 110, below 1540, or at x > 970 between y 900 and 1540).
- **Caption bands:** L-full cy 1080 (TH-lime) / 1000 (TH-studio: its plain-only pill sits at cy ≈ 960, its emphasis blocks at 1047–1121) (TUNE 960–1130); L-split on the seam (952); L-card cy 1343; L-board cy 960. Avoid-face is on: a chunk that would touch the face box moves down to chin + 40 px.
- **Headline band (plate):** line 1 cy 960, line 2 cy 1036 (both centred on x 540); the proof card y 1084–1484.
- **Numeral band:** chip cy = max(866, chin + 76) (h ≈ 72); numeral cy = chip cy + 204 (SM-NUM-A) or + 234 (SM-NUM-B). Nothing else in that band while they show.
- **Series card band:** kicker cy 1000, number cy 1130, sub cy 1250 (all + the same chin shift when the chin is below 790).
- **Brand row band:** y 660–720; window y 740–1280.

### 3.6 Presenter rules
- Share ≥ 75 %; longest absence 8 s (HA-18 hook only), ≤ 4 s anywhere else (L-board runs, P-FRAMED-CLIP).
- Return to the presenter by hard cut, undim (G-4) or slide-up (G-6). Never by a wash in the body (washes are section breaks, §9).
- Crops: L-full as shot; jump cuts keep the same crop (measured: 5 of 5 sampled full → full jump cuts change scale < 2 %, v01 @0:39.8, 0:44.5, 0:57.1, 1:01.2; v02 @1:08.3); the only crop changes are the Z-1 / Z-2 rush-ins under a wash, which land back on the base framing (§10.2). L-split bottom band with the eye line at y 1220–1300; L-card full frame, dimmed.
- Behind the head (with the matte): only P-LOGO-BEHIND (a creator logo, or a monogram under E1), P-SAVE-BADGE and P-DELIVERABLE-TILE; their top edge ≥ y 140, never wider than 560 px.

---

## §4 Colour, themes, grades `[REQ] [roles' meanings DNA; brandable hex VAR; theme hues TUNE]`

### 4.1 Role palette
| Role | Hex | Its one job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` **Signal Lime** | {{BV-02.primary|#C6FF0C}} | Navigation: numeral digits (SM-NUM-A) or hash (SM-NUM-B), the CS-2 pill, the Link in Bio pill, the community headline, the cursor box, teaser arrows | `ink` | 15.1:1 | yes (BV-02 colour 1) |
| `accent` **Plate Red** | {{BV-02.accent|#E60005}} | The plate's second line, the Save badge, the "Comment below" title | `paper` | 4.75:1 | yes (BV-02 colour 2) |
| `bad` **Paid Red** | `#FF453A` | Paid / risky / the old way: price chips, strike lines | `ink` | 5.8:1 | no (fixed) |
| `good` **Free Green** | `#30D158` | Free / works / the new way: FREE chip, ticks | `ink` | 9.8:1 | no (fixed) |
| `ink` | `#0A0A0A` | Text on light cards and chips; plate line 1 fill; the CS-1S seam pill (65 %) | — | — | no |
| `paper` | `#FFFFFF` | White text, chips, note cards, the SM-NUM-A hash, italic emphasis | — | — | no |
| `tile` | `#1C1C1E` | The neutral glass tile of created logo plates and monograms | `paper` | 17.0:1 | no |
| `night` | `#050B06` | End-card ground | — | — | no |
| `canvas` | `#E9773C` | W-board top stop (TH-studio) | — | — | no |
| `grid` | `#C6FF0C` | End-card dot grid (10 %) | — | — | no |

### 4.2 Meanings
- **Lime = where you are in the reel**: the item number, the call to action, the thing to click. It never decorates.
- **White = the voice**: captions, italic emphasis, chips. Emphasis is never coloured (N5).
- **Red (accent) = the stake**: the plate's second line ("of WWDC-26"), Save, "Comment below".
- **The money axis is `bad` → `good`**: "$22 a month" in a `bad` chip with a strike, "free forever" in a `good` chip. Use it only when the script contrasts paid and free.
- **Brand colours appear only inside brand logos** the creator supplied. Created logo plates use `tile` + `paper` (N9).

### 4.3 Theme packs (`per_reel`, one per reel: the caption skin of a series)
| Pack | Caption profile | Numeral | Tool window | W-board | When |
|---|---|---|---|---|---|
| **TH-studio** (default) | **CS-1** on full frames: plain-only chunks in a 44 px `ink` pill (hard swap), emphasis chunks bare; **CS-1S** `ink` pill at 65 %, white 42 px on the seam | **SM-NUM-A**: white `#` + lime digits, Montserrat 900, inline | dark window `#111214` with a 2 px `rgba(255,255,255,.14)` border, radius 28 | warm `#E9773C → #F6C9A5` | Keynote and launch recaps, feature lists, F-B daily briefs (v01, v02) |
| **TH-lime** | **CS-1** bare white 60 px on full frames, typed on character by character (`reveal: "char"`, 50 cps); **CS-2** lime pill (`primary`, 100 %), black 42 px, weight 600, under tool cards | **SM-NUM-B**: giant lime `#` behind white condensed digits (Barlow Condensed 700) | white 8 px frame around the window, radius 28 | cool `#2F7FD8 → #7FD8E6` | "Tools of the week" roundups (v03) |

Rules:
- The reel header declares `theme`. Captions pick their profile by layout (`captions.by_layout`): CS-1 on L-full/L-board, CS-1S on L-split, CS-2 on L-card. A TH-studio reel overrides its L-card captions to CS-1S. Never mix profiles, numeral variants or window frames inside one reel (D6, V-THEME).
- A buyer's BV-02 colour 1 replaces lime in both packs (the CS-2 pill follows `primary`); `veos templates copy` nudges it to ≥ 4.5:1 against `ink`.
- A series keeps its pack: "Week NN of the AI tools" is always TH-lime; "Day NN of future tech" always TH-studio. The first reel of a series picks; later reels inherit it (series memory, §24).

### 4.4 Grades
Footage is **not regraded** (the reference rooms are already warm). Only exposure and white balance are matched between setups. No grade events, no clip treatments. The only treatments are the L-card **dim** (blur 12 px, luma −0.5) and the warm-wash transition (§9).

### 4.5 Rules
- `max_bright_per_frame` = 3: lime + red + one supplied brand logo at most (N10). The `bad`/`good` pair counts as two: never show it in a frame that also has the red plate.
- Coloured text on light worlds (W-board, white note cards) needs a chip: lime text never sits on white; red text on white is ≥ 48 px bold (the "Comment below" title).
- On footage, white text carries the soft shadow `0 2 8 rgba(0,0,0,.55)` or sits in the pill.
- **Must match `tokens.json`** (`roles`, `themes`, `captions.profiles`).

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map
| Slot | Family | Weights | Font class (the TUNE boundary) | Used for |
|---|---|---|---|---|
| `body` | **Inter Tight** | 400 / 500 / 600 / 700 | neo-grotesk sans 400–700 | Caption connector text, brand rows, plate lines, card text, series kicker/sub |
| `serif` | **Instrument Serif** | 400 italic | high-contrast italic display serif | Emphasis phrases, series number, chips, end-card kicker, stat values |
| `display` | **Montserrat** | 900 | heavy geometric grotesk 800–900 (the real `#01` has Montserrat-like round `0` and flagged `1`) | SM-NUM-A numerals, the SM-NUM-B hash, the community headline |
| `numeric` | **Barlow Condensed** | 700 | condensed sans 600–700 | SM-NUM-B white digits |
| `mono` | **JetBrains Mono** | 400 | monospace | Created terminal / code texture inside a card (`TC-decorative` unless it carries the point) |

All bundled (OFL). Brand logos are image assets the creator supplies, never fonts. Devanagari: `Noto Sans Devanagari` replaces `body`; Devanagari has no true italic, so the emphasis becomes `Noto Sans Devanagari 700` at the same size tier (§5.5).

### 5.2 Headline element: the two-line plate (`kind: plate`) `[DNA recipe; NICHE text]`
| Property | Spec |
|---|---|
| Line 1 plate | `ink` fill, radius 6, padding 6/18; text `paper`, Inter Tight 600, **62 px**, line height 1.0, tracking −1 %; centred on x 540, **cy 960** |
| Line 2 plate | `accent` fill (red), radius 6, padding 6/18; text `paper`, Inter Tight 700, **62 px**; centred on x 540, **cy 1036**; usually narrower than line 1 |
| Words | ≤ 9 in total; line 1 ≤ 5 (the setup), line 2 ≤ 4 (the stake: the event, the number, the twist) |
| Proof card | Directly under the plate: white card x 120–960, y 1084–1484, radius 18, soft shadow `0 18 40 rgba(0,0,0,.35)`; the subject image on the left 45 %, a 2-line counter-claim on the right (Inter Tight 600, 52 px; line 1 `ink`, line 2 `accent`) |
| f0 | Plate + proof card arrive as **one group zooming in from the viewer**: scale 1.25 → 1.00 over f0–f6 (expo-out) with 8 → 0 px motion blur, cross-dissolving over the presenter; settled and sharp by **0.2 s** (real: a 2-frame pre-roll, then ≈ 2× → 1.0 over f2–f7, settled f8, v01 @0:00.07–0:00.27) |
| Life | The held prop strobes: the product in the presenter's hand flips colour (red ↔ black) every 2–3 f from 0.33 s for ≈ 1 s (v01 @0:00.33–0:01.3; an edit of two takes/photos alternated). Without a prop: the card's image flips the same way. The plate itself does not move |
| Lifetime | The hook: 2.5–8 s; gone before the first L-split or at the first warm wash |
| Exit | Blur 0 → 12 px + fade over 6 f, or it leaves with the hook beat on a hard cut |
| Text class | `TC-display` (62 px ≥ 40) |

### 5.3 Caption profiles CS-1 / CS-1S / CS-2 (all extend `lib:vaibhav`) `[DNA mechanics; fonts TUNE; language VAR]`
| Group | CS-1 (full frame, both packs) — CS-1S (seam) differs only where noted | CS-2 (tool-card pill) |
|---|---|---|
| Mode | `full` / `support` / `mute_safe` | same |
| Chunking | `unit: phrase`, 2–5 words, ≤ 30 characters per line, ≤ 3 lines (the italic line + plain lines); never split names, numbers or units; a new chunk on punctuation and on pauses ≥ 0.9 s | same |
| Timing | lead 2 f; min hold 0.25 s/word; pause hold ≤ 0.6 s; tail 0.12 s. **Swap (measured at 30 fps):** TH-studio plain chunks **hard** (complete on their word or cut, v01 @0:01.85, @1:17.95); the italic phrase **smears in** horizontally over 2–3 f (v02 @0:01.57–0:01.70; word groups smear out 2 f / in 3 f, v02 @0:34.77–0:34.93) → the base CS-1 swap is `smear` (`frames: 3`, `out_frames: 2`, `smear_px` 24 at `angle` 0, `stretch` 1.6, `dir: right`); TH-lime plain lines **type on** ≈ 1.5–2 characters per frame (v03 @0:17.67–0:17.95 "I went through", @2:33.67 "And follow") → `reveal: "char"`, `cps: 50`, the italic phrase blur-pops in 1–2 f (v03 @0:17.92: `blur` 2 f) | `blur` 3 f |
| Skin (plain words) | Inter Tight **500**; emphasis chunks **60 px** (measured 62–66 px, v01 @0:05), sentence case, `paper`, shadow `0 2 8 rgba(0,0,0,.55)`, line height 1.12. Plain-only chunks: TH-studio **44 px** (cap 32 px, v01 @1:13.95), TH-lime 60 px. CS-1S: **42 px** (`TC-subtitle`, E3; measured 40–44 px) | Inter Tight **600**, 42 px, `ink`, no shadow |
| Container | CS-1 TH-lime: **none** (bare). CS-1 TH-studio: plain-only chunks in an `ink` pill, opacity 0.75, radius 8, padding 4/14 (v01 @1:13.95 pill y 928–992); emphasis chunks bare, their plain lines too (`tiers.connector_container_when: "plain_only"`: only chunks with no keyword get the pill). CS-1S: `ink` pill, opacity 0.65 (sampled #5A5A5A over white B-roll), radius 8, padding 4/14, one pill per plain line | `primary` (lime) pill, opacity 1.0, radius 10, padding 6/16 |
| Emphasis | `size_tier`: the chosen phrase in Instrument Serif **Italic 400, 116 px** on full frames (measured ≈ 125 px, v01 @0:05; ≈ 84 px v03 @2:31), **80 px** in CS-1S (measured ≈ 76 px, v02 @0:02), `paper`, no pill, soft shadow; `split` stacking: the plain words before it above, after it below. ≤ 1 per chunk, ≤ 0.25 per s (one per 4 s); selection: the P5b pick (§1), else a topic noun / name / number / glossary term with score ≥ 1.5 | same; the italic line stays white on footage (never lime) |
| Position | `fixed_y` cy 1080 (L-full; TH-studio 1000), cy 960 (L-board); CS-1S `seam` (L-split, y 952); `avoid_face` on | cy 1343 (L-card) |
| Colour flips | none: CS-1 relies on the soft shadow (keep the chest band mid-to-dark; the reels shoot dark tops), CS-1S on its pill | none |
| Hide rules | under z8 scenes (numeral, chips, series card, end-card lines), during the T-2/T-5/T-6 transitions, during stage morphs | same |
| Language | Latin script; English product terms verbatim; the speaker's grammar not normalised; profanity mask `inner`; glossary = every tool and brand name of the reel with exact casing | same |

**Emphasis-phrase rules** (the craft step P5b):
1. 2–4 words, ≤ 22 characters, so the 116 px italic line fits inside 952 px. Shorten longer spans with `captions.overrides {i, emph: false}` on the extra words.
2. One phrase per thought: about every 4–8 s in L-full, every 6–10 s in splits. Inside L-card chunks emphasis stays off unless the phrase is the tool's key benefit.
3. Pick the quotable part: the benefit ("completely free"), the twist ("nobody is talking"), the stake ("sell your data"), the number + noun ("in just 60 seconds").
4. A question carries its emphasis on its last ≤ 22 characters ("So why does an AI / *company want it?*") and is a re-hook (§7.4).
5. Never on stop-words, on the tool name inside its own tool card (the brand row shows it), or on the CTA keyword (it has its own card).

### 5.4 Other text systems
| Element | Class | Recipe | Hold |
|---|---|---|---|
| **Numeral SM-NUM-A** | TC-display | `#` `paper` + digits `primary`, Montserrat 900, 350 px (digit cap measured 252 px, whole numeral ≈ 618 px wide, v01 @0:11), tracking −4 %, soft shadow `0 10 30 rgba(0,0,0,.35)`; centred on x 540, cy 1056 | 1.2–2.0 s |
| **Numeral SM-NUM-B** | TC-display | Lime `#` Montserrat 900, 540 px (hash measured 394 px tall, x 342–738, v03 @0:24), with a darker bevel edge (`#8FB51F`, offset +6/+6) behind; white digits Barlow Condensed 700, 330 px (digit height 234 px), centred on the hash; cy 1200 | 1.2–2.0 s |
| **Chip (label / teaser / recap)** | TC-label | `paper` box, radius 4, padding 2/16; Instrument Serif Italic 54 px `ink`; centred on x 540, cy = max(866, chin + 76) | with the numeral |
| **Series card** | TC-display | "Welcome to" Inter Tight 400 52 px `paper` (cy 1000) / "Day 60" Instrument Serif Italic 170 px `paper` (cy 1130) / "of future tech updates" Inter Tight 400 50 px `paper` (cy 1250); soft shadow. Built while the T-2 tint is still fading: the kicker **types on** ≈ 1 character per frame from 6 f after the flash (v02 @0:07.45–0:07.58), the number blur-pops in, the sub types on; it leaves under the next wash (v03 @0:17.12) | 1.8–2.2 s |
| **Brand row** | TC-label | Logo or monogram square 80 px (radius 18) + 18 px gap + the tool name in Inter Tight 500 50 px `paper`; left-aligned at x 64, y 660–720 | the whole card |
| **Note card** | TC-label | `paper` card w 700, radius 26, padding 36/40; optional title Inter Tight 700 48 px `accent`; body Inter Tight 500 44 px `ink`, ≤ 3 lines; a 120 px generic gradient orb (`orb` gradient, never a product's assistant logo) overlapping the top edge by 50 % | 2–4 s |
| **Stat line** | TC-display | Value Instrument Serif Italic 104 px `paper` + label Inter Tight 500 44 px `paper` under it; on the split top's lower third (y 640–860) or at chest | 1.5–3 s |
| **Price chips** | TC-label | `bad` chip, Inter Tight 800 48 px `ink`, with a 6 px `ink` strike line drawn L → R over 6 f; `good` chip "FREE", Inter Tight 800 48 px `ink` | 1.5–3 s |
| **Plate** | TC-display | §5.2 | hook |
| **Legal / disclosure** | TC-legal | Inter Tight 500 26 px `paper` 80 %, top-left of the card it labels (x + 16, y + 14), or x 64, y 140 for "Paid partnership" | the whole element |

### 5.5 Language and number rules
- **Spelling:** English captions verbatim; brand and tool names exactly as the product writes them (case included): the glossary is the source of truth (V-CAPTION).
- **Hinglish speech → English captions** (BV-05 `hinglish/en`): transform `translate`; product terms verbatim; the emphasis phrase is picked in the translated text.
- **Hinglish captions** (`hinglish/hinglish`): romanised; phonetic spelling allowed for Hindi words, English words exact.
- **Hindi (Devanagari):** `Noto Sans Devanagari`; the emphasis tier becomes weight 700 at 116 px (no italic); chips and the series card stay in English (Latin) unless the buyer asks otherwise.
- **Numbers (BV-06):** international `$1.2M`, `200`, `22,000` for English; Indian `₹1,20,000`, `₹2.5 L` for Hinglish/Hindi. Currency glyphs are written, never "Rs"/"INR" (V-NUMFMT). Marker numerals are always two digits: `#01`…`#10`.
- **Units:** metric; a spoken imperial unit is shown as spoken.

---

## §6 Hook system `[REQ]`

### 6.1 Stopper tests
| Test | This style's number |
|---|---|
| **ST-1 Thumbnail** | f0 at 25 % shows the plate (62 px → 15.5 px, readable) and the proof card; for HA-18, the post line and the clip's subject |
| **ST-2 Mute** | The first 3 s say what the reel is about with sound off: the plate or the post line + the proof + the first caption |
| **ST-3 Motion at f0** | The presenter's live footage, the clip playing, or the B-roll moving on frame 0 |
| **ST-4 Read time** | The plate or lockup reads in ≤ 1.5 s (≤ 9 words) |
| **ST-6 Payoff-by** | Proof ≤ 2.5 s (HA-02, HA-18), thesis ≤ 3.0 s (HA-12), lockup ≤ 0.7 s (HA-05) |

ST-5 (change count) is enforced through `hook_sc_3s` = 4 in V-CADENCE.

### 6.2 Default archetype: HA-02 Headline + proof ("Plate + proof") `[DNA]`
Spoken pattern: "*The most exciting part of [EVENT] isn't [THE OBVIOUS THING]… it's [THE THING NOBODY IS TALKING ABOUT].*"

| t | Beat | Tone | Visual | Caption | Layout / camera | SFX moment |
|---|---|---|---|---|---|---|
| **f0** | Stopper frame | awe | **Plate** "The most exciting part / **of [EVENT]**" settled (cy 960/1036) + **proof card** (subject image + "This is not the / **exciting part**") under it + the presenter holding the product or gesturing | hidden (the plate is up) | L-full, as shot | hook hit on f0 |
| 0.0–0.2 | Group lands | awe | Plate + card zoom in from 1.25 → 1.00 with motion blur (f0–f6), one group | — | — | whoosh into the hit |
| 0.33–1.3 | Prop strobe | awe | The held product flips colour every 2–3 f (or the card image does) | — | — | soft ticks (one file) |
| 1.8–1.9 | First proof cut | explain | **Hard cut to L-split** (v01 @0:01.85): the product/feature B-roll or recording, moving, in the top band | seam pill: the first phrase ("[Company] just launched one"), complete on the cut | G-1 cut | light whoosh on the cut |
| 1.9–3.0 | Proof runs | explain | The top band animates; the plate is gone | the seam pill swaps per phrase | L-split | — |
| 3.0–6.0 | The twist | awe | L-full; the **italic emphasis** on the twist ("*exciting part*") | split tiers: "This is / *exciting part* / not the most" | L-full | — |
| 6.0–8.0 | Proof montage | explain | L-split: 3 B-roll/recording swaps, one per phrase (feature grid, a screen, the product) | seam pill | L-split | — |
| 8.0–8.5 | Section break | — | **T-2 warm wash** (≈ 16 f, white peak) | hidden | cut under the wash; **Z-1 rush-in** starts on the cut | wash + impact on the white frame |
| 8.5–10.4 | **Series card** | awe | "Welcome to / *Day 60* / of [SERIES]" over the presenter (L-full), kicker typing on | hidden (the card is z8) | L-full | reveal on the number; the bed enters |
| 10.4–12 | Promise | win | italic "*nobody is talking about*" + the count ("here are the 10 that matter") | split tiers | L-full | — |
| ≈ 12 | Item 1 | explain | `#10` (or `#01`) numeral on the ordinal word (§7.3) | hidden | L-full | **list cue** |

Never skip the proof: with no product image, the proof card shows a created P-THUMB-CARD from the script's words (§12.5) and the 1.5 s cut goes to a created UI in the split (P-SPLIT-UI).

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`

**HA-18 Borrowed post ("Post + clip")**: when the creator supplies **their own** post screenshot and a clip they hold (v03).
| t | Visual | Caption | Layout |
|---|---|---|---|
| f0 | W-void: the post header (avatar initials circle 72 px + name Inter Tight 600 34 px + handle 28 px TC-legal + the post line Inter Tight 500 40 px) at y 300–440; the clip in a band x 0–1080, y 470–1400 (cover crop); a 6 px white progress bar on the band's bottom edge with a 64 px avatar dot riding it | the clip's own words as a CS pill at cy 1240 | L-board |
| 0.0–3.0 | The clip plays its payoff line (the viral moment) | pill per phrase | L-board |
| 3.0–7.5 | The clip continues (or a second clip); the avatar dot travels the bar (0 → 100 % over the hook) | pill | L-board |
| 7.5–8.0 | **T-2 warm wash** out | — | — |
| 8.0–10 | Presenter; italic reaction lockup ("*[Name]* / is literally…") | split tiers | L-full |
| 10–13 | Teaser: "*#02, #03 and #08* / do the whole job for free" + 3 tool tiles (P-TEASER-TILES) | split tiers | L-full |
| 13–17 | Series card "Welcome to / *Week 09* / of the AI tools" | hidden | L-full |
| 17–22.6 | **T-5** into **W-wheel**: the presenter over the tool wheel; "I went through / *100 launches this week*" … "*Let's dive into it*" | typed plain + italic | W-wheel |
| 22.6–23.1 | Radial speed lines + **T-2** → Z-1 rush-in → lime swipe → `#10` | hidden | L-full |
Presenter absent ≤ 8 s. Payoff (the clip's line) ≤ 3 s. Without the creator's clip: FB-4 (HA-02, or a created quote card + a created video UI).

**HA-12 Thesis typography ("Split thesis")**: the F-B default (v02).
| t | Visual | Caption | Layout |
|---|---|---|---|
| f0 | L-split: moving B-roll of the story's subject in the top band (or P-DOT-REVEAL), black fade above the seam; the presenter below | — | L-split |
| 0.17–0.33 | **T-9 dot dissolve** (6 f): the B-roll subject dissolves into the dot-matrix figure (v02 @0:00.17–0:00.33) | — | L-split |
| 0.37 | The first plain phrase on the seam ("One [kind of company] just"), 1 f blur-in | seam | L-split |
| 1.67 | The thesis phrase in italic below it ("*announced a full-body scanner*" → shortened to ≤ 22 characters: "*a full-body scanner*"), blur-in 6 f | split tiers | L-split |
| 2.2–2.8 | HUD corner brackets (P-HUD-MARKS) draw on the B-roll | — | L-split |
| 3.0–6.0 | A second B-roll + "*in just 60 seconds*" | seam | L-split |
| 6.0–7.0 | L-full, italic reaction ("Even experts / *are shocked*") | tiers | L-full |
| 7.0–7.4 | T-2 warm wash | — | — |
| 7.4–9.5 | Series card "Welcome to / *Day 60* / of future tech updates" | hidden | L-full |
Thesis readable ≤ 3.0 s.

**HA-05 Claim lockup ("Teaser lockup")**: roundups whose payoff is "N tools that replace a paid one".
| t | Visual | Caption | Layout |
|---|---|---|---|
| f0 | L-full; the italic lockup built by 0.7 s at cy 1060–1180: "*#02, #03 and #08*" (92 px) / "do the whole job for free" (42 px pill) | the lockup is the caption (tiers) | L-full |
| 0.4–1.2 | P-TEASER-TILES: 3 tool tiles (240 px, gap 24) pop below it (cy 1340), 4 f stagger | — | — |
| 1.5–3.0 | Presenter line "Let me show you"; the tiles exit | pill | L-full |
| 3.0–5.0 | Series card | hidden | L-full |

### 6.4 Hook pairs by topic `[NICHE: example]`
| Topic | Archetype | Pair type | Column 1 | Column 2 | How each is shown |
|---|---|---|---|---|---|
| A keynote / launch event (N1 tech) | HA-02 | promise → proof | "The most exciting part of [EVENT]" | the one feature nobody covered | plate + proof card (a product photo the creator holds) → its recording in the split at 1.6 s |
| A weekly AI-tools roundup (N1) | HA-05 | promise → proof | "[#a, #b and #c] do the whole job for free" | the three tool tiles, then item #10 | italic lockup + 3 tiles (logo plates if no logos) |
| A rival's viral moment (N1) | HA-18 | claim → evidence | the creator's own post line about it | the clip they hold | post header + clip band |
| A single AI product launch (N1, F-B) | HA-12 | thesis → scene promise | "[Company] just announced [product]" | the product B-roll / render | split B-roll + italic thesis |
| New UPI / banking-app features (N2 money) | HA-02 | promise → proof | "The best update of [APP] this month" | the one feature that saves money | plate + proof card (their own app screenshot) |
| Free apps that replace paid ones (N2) | HA-05 | promise → proof | "[#a and #b] replace a ₹[X]/month app" | the paid app's price vs FREE chips | lockup + tiles + P-PRICE-STRIKE at item 1 |
| A finance-news story (N2, F-B) | HA-12 | thesis → scene promise | "Your bank just changed [rule]" | a created note card of the rule + their own screenshot | split + italic thesis |

### 6.5 Headline writing `[DNA formula; NICHE examples]`
**Plate formula:** line 1 `[the setup, ≤ 5 words]` (white on black) / line 2 `[the stake: the event, a number or the twist, ≤ 4 words]` (white on red). Sentence case, no emoji, no exclamation marks.

| Template | Example |
|---|---|
| **Most-X part** (default) | "The most exciting part / of [EVENT]" |
| **Nobody is talking** | "The feature nobody / is talking about" |
| **Free replaces paid** | "Free tools that / replace [PAID TOOL]" |
| **Count + window** | "10 AI tools / from this week" |
| **Warning** | "Turn this setting off / before [DATE]" |
| **Switch** | "Why I'm switching / back to [PRODUCT]" |

- The plate says what the proof card and the first split show (ST-2).
- **Write 3 and pick by the stopper tests**; the other two go to the post caption or to trial reels.
- **Banned:** "game changer", "insane", "you won't believe"; counts that don't match the numerals (H9); claims the reel doesn't show.

### 6.6 Hook sound
See §11: the hook may carry cues (the f0 hit, the first cut, the wash); the music bed enters after the hook, at the series card.

### 6.7 CTA `[DNA device set; VAR values]`
The CTA is the end stack (§25.3), in this order, in the last 10–14 s:
| Step | Spoken pattern | On screen | Hold |
|---|---|---|---|
| 1 **Save** | "Save this now, because 90 % of you will forget" | P-SAVE-BADGE (a red bookmark badge behind the head) + italic "*90% of you*" (plain "Save this now because" above, "will forget" below) | 2.0–3.0 s |
| 2 **Follow** | "And follow, because I do this every single week" | italic "*every single week*" (L-full); the handle {{BV-01.handle|@yourhandle}} as a TC-legal chip under the caption | 1.5–2.5 s |
| 3 **Deliverable** | "And if you want all [N] with the links…" | P-DELIVERABLE-TILE (a link tile behind the head) + italic "*all [N] with the links*" | 1.5–2.5 s |
| 4 **Community / device** | "…join the free community, link in bio" | **P-COMMUNITY-CARD** (W-endcard): "Join the free / [COMMUNITY]" + phone mock + the **Link in Bio** pill tapped by the cursor | 3.0–4.0 s |

Device variants (BV-08 = {{BV-08.device|follow_save_stack}}):
- `link_bio` / `follow_save_stack` (default): steps 1–4 as above.
- `comment_keyword`: step 4 becomes P-COMMENT-CARD: a white note card "**Comment below**" (accent) + "Comment **{{BV-08.keyword|KEYWORD}}** and I'll send you the list", the keyword in a lime chip; held ≥ 1.5 s after the keyword is spoken.
- `end_card`: steps 1–2, then the community card without the phone (headline + pill), 3 s.
- No silence is needed before the CTA: the warm wash (T-2) before step 1 is the break. TH-lime also puts a T-2 + Z-1 door between Save and Follow (v03 @2:33.20–2:33.77); the Follow line types on.

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type
| Format | Type | Arc | Typical timing (150 s F-A / 90 s F-B) |
|---|---|---|---|
| **F-A Countdown** | `news` | hook (2.5–8 s) → promise + teaser (2–5 s) → **series card** (8–15 s) → items `#NN` (5–10 items, 10–20 s each, one direction) → final verdict (0–6 s, optional) → end stack (10–14 s) | hook 0–8 · promise 8–12 · series 12–14 · items 14–136 · end 136–150 |
| **F-B Daily brief** | `explainer` | hook (thesis, 3–7 s) → **series card** → what it is (mechanism, B-roll) → the twist question (italic re-hook) → why it matters / the catch → the honest caveat ("To be fair…") → end card | hook 0–7 · series 7–9.5 · what 9.5–35 · twist 35–55 · why 55–75 · caveat 75–82 · end 82–90 |

### 7.2 Markers
| ID | Marker | Recipe | Used |
|---|---|---|---|
| **SM-NUM** | `#NN` numeral + chip | TH-studio → **SM-NUM-A** (white `#`, lime digits, inline); TH-lime → **SM-NUM-B** (lime hash, white condensed digits); chip above, numeral below (§5.4) | Every F-A item, without exception |
| **SM-CHIP-LABEL** | label chip | the item's 2–3-word name or feature ("Personal context", "Dictation", "Notify me") | Default chip |
| **SM-CHIP-TEASER** | teaser chip | "Wait for the next 02 >>>" (the count of items left, two digits) | Once per reel, on the item where 2 or 3 items remain |
| **SM-CHIP-RECAP** | recap chip | "Recap feature" | On an item that returns to an earlier feature or sums up |
| **SM-SERIES** | series card | §24 | Once, closing the intro |
| **SM-QUESTION** | italic question chunk | the question as a full italic emphasis chunk in L-full | F-B re-hooks; F-A mid-item re-hooks |

**Numbering:** `desc` (10 → 01, the countdown) is the default and the stronger loop ("the best is last"); `asc` (01 → 10) when the items are equal features of one launch (v01). Declared in the reel header; never both in one reel. Count: 5–10 items (fewer than 5 is F-B; more than 10 splits into two reels).

### 7.3 Unit ritual (F-A item; identical for every item; t = 0 at the ordinal/number word's onset)
| Frame | Step | Recipe |
|---|---|---|
| −14…0 f | **Entry door** | **TH-lime (every item, v03 ×10):** T-2 warm leak wash over the previous card (≈ 8 f build), cut under it to L-full, **Z-1 / Z-2 rush-in** from the cut (×1.7, 12 f, `expoOut`, alternating) while the red tint fades (v03 @0:22.67–0:23.10, @1:28.03–1:28.47). **TH-studio:** hard cut to L-full (v01 @0:29.37); the first item only enters through the white-peak T-2 (v01 @0:10.13–0:10.37) |
| −2 f | **Numeral** | TH-lime: **T-6 lime swipe** (3 bars, 2 f, motion-blurred) across the numeral band, then SM-NUM-B **snaps in at full size** and its white digits **flicker** (on 1 f, dim 2 f, off 1 f, on; ≈ 8 f) (v03 @0:23.10–0:23.37, @1:28.43–1:28.67). TH-studio: SM-NUM-A lands **on the cut frame** as a 1–2 f horizontal smear-stretch (scaleX 1.3 → 1, scaleY 0.5 → 1, h-blur 16 → 0), no overshoot (v01 @0:29.37–0:29.40). No growth during the hold. Captions hide; **list cue** |
| +4 f | **Chip** | P-LABEL-CHIP (or teaser/recap) drops 24 px + fades in over 6 f above the numeral |
| +14 f | **Logo behind the head** | P-LOGO-BEHIND **cuts on at full size** ≈ 0.45 s after the numeral, no grow (v03 @0:23.55); holds dimmed through the card |
| +36…+45 f | Numeral out | Leaves inside the T-11 smear wipe that brings the card (v03 @0:24.55); the chip leaves with it |
| tool name ±2 f | **Card in** | **T-11 smear wipe** (3 f of horizontal streaks across the chest band) → brand row + window complete on the next frame, no rise; dim ramps over 12 f (G-3); the CS-2 lime pill may land 2–3 f before the card (v03 @0:24.55–0:24.65) |
| card body | **Features** | One screen per spoken feature, swapped on the feature word (crossfade 4 f, `events`); P-CURSOR-BOX on the element that is clicked or named; P-PRICE-STRIKE when a price is said |
| 6–14 s after card in | **Pop-back** (optional) | Hard cut or G-4 undim to L-full for the opinion line, one italic phrase (≥ 1.5 s). TH-lime cards often run straight into the next wash (v03 @1:28.0, @2:33.1) |
| next ordinal | Next item | Repeat the same door every item: TH-lime every item through T-2; TH-studio by hard cut (T-2 ≤ once per 40 s) |

**F-B beat unit** (t = 0 at the beat's first sentence): L-split B-roll + seam captions (3–8 s) → L-full with the italic key phrase (2–4 s) → P-FRAMED-CLIP or P-STAT-LINE for the number (2–4 s) → back to L-full. Every second beat opens with SM-QUESTION.

### 7.4 Open loops and re-hooks
- **Loop types:** the count loop ("10 tools; #02 is free forever"); the teaser loop (P-TEASER-TILES, or "#02, #03 and #08 do the whole job for free"); the "wait for the next 02" chip; the deliverable loop ("I'll share all 10 with the links"); F-B's question loop ("So why does an AI company want it?").
- **Payoff rule:** every loop is paid on screen: the teased items appear with their numerals; the deliverable is the community card; a question's answer is the next italic phrase.
- **Re-hooks (`long`):** at least one every **25 s** after the intro (H10): every numeral is a re-hook (scene `rehook: true`), plus the teaser chip and SM-QUESTION. An item longer than 22 s gets a mid-item re-hook: an italic question or a P-PRICE-STRIKE beat flagged `rehook: true`.
- **F-B (`standard`):** one mid-reel re-hook between 25 % and 75 % of the runtime (the twist question), plus the 25 s maximum gap.
- **Intro cap:** hook + promise + series card ≤ 15 % of runtime (≤ 22 s at 150 s; ≤ 13 s at 90 s).

### 7.5 Rhythm and energy curve
- Information-led and calm: no comedy beats. The entertainment is the reveal rhythm: numeral → logo → card → screen swaps.
- **Every item has one opinion beat** (the pop-back), so the presenter's personality returns every 10–20 s.
- **Escalation:** the last two items get the longest cards and the strongest claims ("this one is my favourite", "free forever"); in `desc` order `#01` is the biggest item and gets a P-PRICE-STRIKE or a P-STAT-LINE.
- **The end** is fast and confident: the wash, then Save → Follow → Deliverable → Community in 10–14 s, with no recap of the items.

### 7.6 Cadence (state changes)
| Token | F-A | F-B | Why |
|---|---|---|---|
| `sc_per_10s` | 4–8 | 4–8 | Captions swap every 1–1.5 s (0.5 each) plus 2–4 picture changes (splits, screen swaps, cuts) per 10 s (v01, v03 sheets) |
| `hook_sc_3s` | 4 | 4 | v01: card event, cut to split, 2 caption swaps, B-roll event; v02: dissolve, caption, italic, HUD marks |
| `max_gap_s` | 2.5 | 2.5 | Card screens swap every 2–3 s (v03 @0:57–1:04) |
| `max_static_s` | 2.5 | 2.5 | Live footage and playing recordings count as motion |
| `caption_weight` | 0.5 | 0.5 | support captions |
| `cuts_per_min` | — | — | Not gated. Measured (scene score > 0.2, full frame rate): v01 35.6/min, v02 27.5/min, v03 17.3/min (long cards; their screen swaps are crossfades) |
| `median_shot_s` | ≤ 3.5 | ≤ 3.5 | Measured median / p90 / max shot: v01 1.33 / 3.07 / 5.2 s; v02 1.67 / 4.0 / 4.3 s; v03 3.03 / 8.5 / 12.6 s (a card with ≥ 4 screen swaps). Longest picture-static stretch outside cards ≈ 5 s (v01 @2:48.9–2:53.9, carried by a Z-3 drift) |

*(The coverage table lists 3–4 SC per 10 s, counted without captions; with captions at weight 0.5 the measured body rate is 4–8, which is what V-CADENCE computes.)*

---

## §8 Visual system: graphics, B-roll and patterns `[REQ]`

### 8.1 Graphics role and budget
`graphics: support`. Graphics and inserts cover **45–60 %** of runtime (L-split + L-card + L-board + chest graphics). **36 patterns** (support range 20–45). Per 60 s: ≥ 4 families, ≥ 6 distinct patterns, 12–25 visual events. Every spoken product, feature, price or number gets a visual (D1); numbers become pictures only as stat lines or price chips with the spoken value (no charts: `data_figures` is off).

### 8.2 Families
| ID | Family | Source class | The buyer supplies | Created substitute (§12.5) |
|---|---|---|---|---|
| **B-1** | Numerals & chips | engine | — | — |
| **B-2** | Tool card (brand row + window) | creator-supplied third-party (a tool's UI, recorded by the creator) | screen recordings (SH-1), logos (SH-3) | `recreated_ui` (fx.appUI) + `logo_plate` (fx.logoPlate / monogram) |
| **B-3** | Split B-roll | buyer-owned / creator-supplied | B-roll, product shots, screenshots (SH-2, SH-5) | `diagram` / a created icon grid / a note card |
| **B-4** | Chest graphics (note card, logo pop, logo cluster, stat line, price chips) | engine (+ creator logos) | logos | monogram tiles |
| **B-5** | Borrowed post & clip | creator-supplied third-party (their own post; a clip they hold) | SH-4 | `quote_card` + `recreated_ui` (video) |
| **B-6** | Boards (phone flow, framed clip on black) | engine + creator media | screenshots / B-roll | fx.device phone with created rows |
| **B-7** | Series & end furniture (series card, save badge, deliverable tile, community card, comment card) | engine | the community name; optionally a screenshot of their own community page | a created community screen (generic rows) |
| **B-8** | Hook furniture (plate, proof card, teaser tiles, dot reveal, HUD marks) | engine (+ a creator image) | a product photo (optional) | a created icon / silhouette |

### 8.3 Pattern specs (30 fps; z per SCENES-API)
| ID | Name | Type | What's on screen | Motion recipe | When | Family · class | Engine block · needs |
|---|---|---|---|---|---|---|---|
| **P-PLATE-HOOK** | Two-line plate | overlay | §5.2 plate | zooms in with the proof card as one group 1.25 → 1.0 + blur 8 → 0, f0–f6; exit blur 6 f or with the cut | HA-02 f0 | B-8 · TC-display | bespoke scene `kind: "plate"`, z10 |
| **P-THUMB-CARD** | Proof card | overlay | A white card under the plate: image left, a 2-line counter-claim right | part of the plate group's zoom-in (f0–f6); the image (or the held prop) strobes 2 colours every 2–3 f from 0.33 s for ≈ 1 s | HA-02 f0 | B-8 · TC-label | `kind: "proof"`; the creator's image via `fx.shot`, else `fx.card({theme: "light", icon})`; insert record |
| **P-POST-CLIP** | Post header + clip band | overlay | Avatar initials + name + handle + the post line (y 300–440) over a clip band (y 470–1400) | already in at f0; the clip plays; the bar progresses linearly | HA-18 | B-5 · TC-label / TC-legal | header `kind: "post"`; clip `fx.clip` (creator) or `fx.appUI({kind: "video"})`; insert record |
| **P-PROGRESS-AVATAR** | Clip progress | overlay | A 6 px white bar on the clip's bottom edge, a 64 px avatar dot riding it | x = clip progress, linear | with P-POST-CLIP | B-5 · none | part of the P-POST-CLIP scene |
| **P-DOT-REVEAL** | Dot-matrix reveal | overlay | A subject outline (fx.icon or silhouette) built from a 12 px cyan-white dot grid on white, with 3–5 scan markers | the B-roll subject dissolves into the dots over 6 f (f5–f10, v02 @0:00.17); markers pop 3 f stagger | HA-12 f0 when there is no B-roll | B-8 · none | canvas scene in the split top; `fx.silhouette` / `fx.icon` as the mask |
| **P-HUD-MARKS** | HUD brackets | annotation | 4 corner brackets (40 px arms, 3 px `paper`) around the subject + an optional readout of a **spoken** number | brackets draw 6 f; the readout types 1 char/f (`fx.typeOn(text, lt, {at, cps: 30, frames: 2})`) | a B-roll subject is introduced | B-8 · TC-label | bespoke scene z5 in the split top |
| **P-CLAIM-SPLIT** | Split thesis | stage | L-split with the italic thesis on the seam | captions only (CS tiers) | HA-12, F-B beats | B-3 · TC-subtitle | stage + `captions.overrides` |
| **P-TEASER-TILES** | Teaser tiles | overlay | 3 rounded tiles (240 px, radius 44, gap 24) of the teased tools at cy 1340 | pop 0.6 → 1.05 → 1 over 7 f, 4 f stagger; exit fade 5 f | HA-05, the promise beat | B-8 · TC-decorative (monograms) | creator logos in tiles, else `fx.logoPlate` monograms |
| **P-SERIES-CARD** | Series card | overlay | §5.4 series card over L-full | built under the fading T-2 tint: kicker types on 1 char/f from +6 f (`fx.typeOn(text, lt, {at, cps: 30, frames: 2, drop: 0, stretch: 0})`); number blur-pops 3 f; sub types on (the same `fx.typeOn`); exits under the next wash or a hard cut | closes the intro (8–15 s) | B-7 · TC-display | bespoke scene z8, `kind: "title_card"` |
| **P-NUMERAL-A** | Inline numeral | marker | White `#` + lime digits, 300 px | lands on the cut frame: 1–2 f horizontal smear-stretch (scaleX 1.3 → 1, scaleY 0.5 → 1, h-blur 16 → 0 as `filter:${ctx.blur(16, 0)}`: a directional smear, not a uniform blur), no overshoot, no growth; exits with the next cut or wipe | every item (TH-studio) | B-1 · TC-display | scene z8, `kind: "numeral"`, `rehook: true` |
| **P-NUMERAL-B** | Hash numeral | marker | A lime 540 px `#` behind white condensed digits | T-6 lime swipe (2 f) reveals it at full size; the white digits flicker on/dim/off/on over ≈ 8 f; holds still ≥ 1.1 s; exits inside T-11 | every item (TH-lime) | B-1 · TC-display | scene z8, `kind: "numeral"`, `rehook: true` |
| **P-LABEL-CHIP** | Label chip | marker | A white chip, italic 54 px `ink`, above the numeral | drop 24 px + fade 6 f | every item | B-1 · TC-label | scene z8 (its own rect, ≥ 40 px from the numeral's) |
| **P-TEASER-CHIP** | Teaser chip | marker | "Wait for the next 02 >>>" in the chip | as the label chip; the ">>>" steps in 2 f per arrow | once, 2–3 items left | B-1 · TC-label | scene z8, `kind: "teaser"` |
| **P-RECAP-CHIP** | Recap chip | marker | "Recap feature" | as the label chip | summary items | B-1 · TC-label | scene z8 |
| **P-LOGO-BEHIND** | Logo behind the head | overlay | The tool's logo (or a `tile` monogram: 420 px square, radius 80, initials 220 px `paper`) centred on x 540, y 150–560, behind the presenter | cuts on at full size ≈ 14 f after the numeral (v03 @0:23.55), no grow; holds (dimmed) through the card; exits with the item's wash | every item start | B-2 · TC-display (monogram) | `behind: true` + matte; a monogram sets `exception: "E1"`; insert record (logo) |
| **P-BRAND-ROW** | Brand row | overlay | Logo/monogram 80 px + the tool name 50 px at x 64, y 660–720 | complete on the frame after the T-11 smear (no slide) | with every tool card | B-2 · TC-label | part of P-TOOL-CARD |
| **P-TOOL-CARD** | Tool card | stage + overlay | L-card: brand row + window (972 × 540, radius 28) with the recording; TH-lime adds the 8 px white frame | T-11 smear wipe 3 f → window + brand row complete, no rise; dim ramps 12 f; exits under the next T-2 wash (TH-lime) or a hard cut | every F-A item; F-B product mentions | B-2 · TC-label | `fx.shot` / `fx.clip` (creator) or `fx.appUI` (created); `kind: "card"`; insert record |
| **P-SCREEN-SWAP** | Screen swap | state | The next screenshot / recording segment in the same window | crossfade 4 f; the window rect never moves | each spoken feature inside a card | B-2 · none | scene `events` (crossfade: no E6) |
| **P-CURSOR-BOX** | Cursor box | annotation | A 4 px `primary` rounded box (radius 10) around the named UI element + a 56 px arrow cursor that taps it | the box draws clockwise in 8 f; the cursor glides 10 f and taps (scale 0.9, 3 f) | "click", "upload", "add", "you get…" on a visible element | B-2 · none | bespoke scene z5, `overlaps: [<card id>]` |
| **P-PRICE-STRIKE** | Paid vs free | overlay | A `bad` chip with the spoken price ("$22/month") and a strike line, then a `good` chip "FREE" beside it, at the card's top-right corner (or chest in L-full) | the chip pops 6 f; the strike draws L → R 6 f on "charges"; FREE pops on "free" | paid → free comparisons | B-4 · TC-label | bespoke scene z6; the price must be spoken (V-NUMFMT); may carry `rehook: true` |
| **P-SPLIT-BROLL** | Split B-roll | stage | L-split with the creator's B-roll / screenshot / recording in the top band, caption on the seam | the top content swaps per phrase (crossfade 4 f or cut) | any sentence about a product or an event | B-3 · none | stage `L-split` + `fx.clip` / `fx.shot` in `rects.graphic`; insert record |
| **P-SPLIT-UI** | Split created UI | stage | L-split with a recreated generic UI flow (list, chat, settings) in the top band | rows type/appear per spoken step (`at` times) | no recording; a flow is described | B-3 · TC-label | `fx.appUI` in `rects.graphic` |
| **P-FEATURE-GRID** | Feature grid | overlay | 2–3 rows of 72 px icons in coloured circles (fx.icon) in the split top | pop 4 f stagger, one row per spoken feature | a list of features ("health, sleep, fitness") | B-3 · none | `fx.icon` scene in the split top |
| **P-NOTE-CARD** | Note card | overlay | §5.4 note card (orb on top) at chest (L-full, cy 1160) or in the split top | rise 30 px + de-blur 8 f; the text types word by word at 9 words/s | a spoken request, notification, prompt or quote | B-4 · TC-label | `fx.quoteCard`-style or bespoke; quotes verbatim (NC-13) |
| **P-LOGO-POP** | Logo pop | overlay | One 320 px logo tile at chest (cy 1250) under the caption | pop 0.6 → 1.05 → 1 (7 f); exit fade 5 f | a single app named in L-full | B-4 · none | creator logo, else `fx.logoPlate` |
| **P-LOGO-CLUSTER** | Logo cluster | overlay | 2–4 round 240 px badges at chest (cy 1200–1380) in a triangle/arc | each pops on its name (7 f) | "tools like A, B and C" | B-4 · none | as P-LOGO-POP |
| **P-STAT-LINE** | Stat line | overlay | §5.4 stat line (the spoken value + a label) on the split top's lower third or at chest | the value blurs in 6 f; the label fades 6 f (+4 f) | a spoken number that matters | B-4 · TC-display | bespoke scene; value exactly as spoken (V-NUMFMT) |
| **P-PHONE-BOARD** | Phone board | stage | L-board on W-board: a 600 × 1210 phone mock centred; rows build inside per spoken step | hard cut in; rows rise 20 px + fade 6 f; out by T-12 (the phone pushes 1.03–1.06×/f for 4 f, then rushes into its white screen with motion blur for 4 f, hard cut) | a step-by-step flow ("you just explain… it sets it up"), ≤ 4 s | B-6 · TC-label | `fx.device("phone")` + created rows, or the creator's screenshot inside |
| **P-FRAMED-CLIP** | Framed clip on black | stage | W-void: a 640 × 640 rounded (radius 44) clip at cy 860 with italic serif lines above (cy 470) and below (cy 1290) | the clip scales 0.94 → 1 (12 f); the lines blur in | F-B "what it is" beats, ≤ 4 s | B-6 · TC-display | `fx.clip` (creator) or `fx.card`; L-board |
| **P-RENDER-WORDS** | Words on B-roll | overlay | Full-bleed creator B-roll (L-board) with one italic serif word group per beat at cy 1370 ("No radiation" → "No magnet" → "No tube") | each group smears out 2 f and the next smears in 3 f (horizontal blur: `filter:${ctx.blur(px, 0)}`, px 24 → 0), the B-roll cutting on the same word (v02 @0:34.77–0:34.93) | a spoken list of 2–4 short properties | B-3 · TC-display | L-board + `fx.clip`; captions hidden for the span |
| **P-SAVE-BADGE** | Save badge | overlay | A 560 px `accent` circle with a white bookmark glyph (soft 3-D: inner shadow + highlight) behind the head, y 140–700 | cuts on at full size behind the head (as P-LOGO-BEHIND); holds through the Save line; leaves under a T-2 (v03 @2:33.2) | end stack step 1 | B-7 · none | `behind: true` + matte |
| **P-DELIVERABLE-TILE** | Deliverable tile | overlay | A 300 px `tile` square with a link or code glyph (fx.icon) behind the head | as P-SAVE-BADGE | end stack step 3 | B-7 · none | `behind: true` |
| **P-COMMUNITY-CARD** | Community end card | stage | W-endcard: "Join the free" italic 76 px `paper` (cy 300) / the community name in Inter Tight 900 120 px `primary` with a 28 px glow (cy 400–520) / a 600 × 900 phone mock at y 600–1500 showing a created group screen (the creator's avatar, the group name, 3 generic rows) / the **Link in Bio** pill (`primary`, 64 px `ink`) at cy 1440 / a 3-D-style cursor arrow tapping it / 3 floating chat-bubble glyphs (generic, `primary` at 60 %) | headline lines fade + rise 6 f each; the phone rises 80 px (12 f); the pill shows its outline first and fills lime on the tap (6 f); bubbles drift ±10 px | end stack step 4 (3–4 s) | B-7 · TC-display | L-board on W-endcard; `kind: "end-card"`; the creator's own community screenshot may replace the created screen |
| **P-COMMENT-CARD** | Comment card | overlay | A note card at chest: "Comment below" (accent, 48 px) + the question, or "Comment {{BV-08.keyword|KEYWORD}}…" with the keyword in a `primary` chip | as P-NOTE-CARD | the `comment_keyword` device; or a closing question | B-7 · TC-label | `kind: "cta-keyword"` when a keyword is used |
| **P-WHEEL-STAGE** | Tool-wheel world | stage | W-wheel behind the cut-out presenter: a colour wheel of 4–6 category names (from the script) behind the head + radiating rows of 40 px monogram/app tiles | in by T-5 (the wheel zooms through 1.19 → 1.0×/f, expo-out, ≈ 10 f); the tiles drift outward slowly; out with 24 white radial speed lines (4 f) + T-2 | the promise beat after the series card, once per reel (F-A TH-lime) | B-8 · TC-decorative | `behind: true` full-frame scene + matte; creator logos in the tiles, else monograms |
| **P-SPONSOR-ROW** | Sponsor row | overlay | The sponsor's brand row over its card + "Paid partnership" TC-legal at x 64, y 140, held ≥ 2 s | as P-BRAND-ROW | paid integrations only (§25) | B-2 · TC-legal | `kind: "sponsor"` |

### 8.4 Line → pattern lookup `[NICHE: example]`
| Line type | Example (N1 AI tools / N2 money apps) | Primary | Alternates |
|---|---|---|---|
| Ordinal / item start | "Number seven…", "Next up…", "And number one…" | P-NUMERAL-A/B + P-LABEL-CHIP + P-LOGO-BEHIND | P-TEASER-CHIP (2–3 left), P-RECAP-CHIP |
| Tool / app named with what it does | "[TOOL] turns any video link into notes" / "[APP] now splits bills automatically" | P-TOOL-CARD (+ P-BRAND-ROW) | P-SPLIT-BROLL, P-LOGO-POP |
| A feature of the tool | "It records, transcribes and summarises" / "It shows your credit score for free" | P-SCREEN-SWAP | P-CURSOR-BOX on the feature |
| A click / an action | "Just paste the link and hit analyse" / "Tap pay later" | P-CURSOR-BOX | P-PHONE-BOARD |
| Price / paid vs free | "[OTHER] charges $22 a month for this" / "Banks charge ₹500 for this" | P-PRICE-STRIKE | P-STAT-LINE |
| A spoken number that matters | "200 open-source models" / "₹1 lakh a year" | P-STAT-LINE | caption emphasis on the number |
| A request / prompt / notification | "Hey, find me the cheapest flight" / "Your EMI is due tomorrow" | P-NOTE-CARD | P-SPLIT-UI |
| A step-by-step flow | "You explain it, it builds the shortcut" / "Set the limit, pick the account" | P-PHONE-BOARD (≤ 4 s) | P-SPLIT-UI |
| Several apps named together | "Tools like Make, Zapier, n8n" / "GPay, PhonePe, Paytm" | P-LOGO-CLUSTER | P-TEASER-TILES |
| A single app mentioned in passing | "…like on [TRAVEL APP]" / "…your bank app" | P-LOGO-POP | P-BRAND-ROW alone |
| A product / launch / event | "[Company] just launched one" / "[Regulator] just announced" | P-SPLIT-BROLL | P-NOTE-CARD (a created headline card) |
| A list of features or properties | "health, sleep, fitness, hearing" / "no fees, no paperwork" | P-FEATURE-GRID | P-RENDER-WORDS (F-B) |
| The twist / an opinion | "But here's what nobody is talking about" | L-full + italic emphasis | SM-QUESTION (F-B) |
| A rhetorical question | "So why does an AI company want it?" | SM-QUESTION (L-full, an italic chunk) | — |
| A post / another creator's moment | "This tweet blew up", "[Name] said…" | P-POST-CLIP (the creator's own material) | P-NOTE-CARD as a created quote |
| A story subject with B-roll (F-B) | "a ring of a million sensors" | P-SPLIT-BROLL + P-HUD-MARKS | P-FRAMED-CLIP, P-DOT-REVEAL |
| The promise of the items | "#02, #03 and #08 do the whole job for free" | P-TEASER-TILES + italic lockup | — |
| Series / welcome | "Welcome to Day 60 of…" | P-SERIES-CARD | the count card (§24) |
| Save / Follow / links / community | "Save this now…", "join the free community" | P-SAVE-BADGE → follow line → P-DELIVERABLE-TILE → P-COMMUNITY-CARD | P-COMMENT-CARD |
| A paid integration | "This video is sponsored by…" | P-SPONSOR-ROW + P-TOOL-CARD | — |

### 8.5 Data and truth rules
`data_figures` is off (§18): every number on screen is the **spoken** value or part of the creator's own recording; stat lines and price chips show the exact spoken figure in the BV-06 format (V-NUMFMT); comparisons are paid-vs-free chips, never charts; no invented benchmarks, star counts or prices (NC-6). Created UIs show only words from the script.

### 8.6 Comedy layer: OFF (`profile.tone.comedy = off`)

### 8.7 Asset rules
- **Real captures first:** the creator's own screen recordings of each tool (SH-1). A recording beats any created UI.
- **Logos:** only files the creator supplies (press kits, the tool's own downloads they hold). Otherwise the monogram / logo plate on `tile`, never a redrawn brand mark.
- **Created UIs** are generic and unbranded (fx.appUI, fx.device), never a look-alike of a real product.
- **No stock clichés** (N7). Cinematic renders appear only when the creator owns or holds them (SH-5).
- **Third-party moments:** ask once, then create (§12.5).

### 8.8 Density and variety
- 12–25 visual events per 60 s; ≥ 6 distinct patterns and ≥ 4 families per 60 s.
- The same pattern at most 3 beats in a row, except the item ritual and P-SCREEN-SWAP inside one card.
- One idea per screen: the numeral leaves before the card enters; a chest graphic leaves before the next one arrives.

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | SFX role |
|---|---|---|---|---|
| **T-1** | Hard cut | 0 | On a word boundary ±1 f; ≈ 85 % of boundaries (v01: 106 cuts in 179 s, almost all hard) | none |
| **T-2** | Warm leak wash | 15 | A light leak (`wash`: magenta `#FF5E7A` → orange `#FF8A3D` → pale yellow `#FFC2A8`) sweeps in from one edge or corner over **6 f**, covering the frame; **peak:** section breaks flash to **full white for 1 f** (v01 @0:10.30, v02 @0:07.25, v03 @0:08.50); TH-lime item doors hold a saturated red-yellow field for 3–6 f instead (v03 @0:22.70–0:22.87); the cut sits under the peak; the white falls off in 1–2 f and a **warm tint residue** pulses over the new shot for 6–10 f (v01 @0:10.40–0:10.57, v02 @0:07.38–0:07.58). **Build (core draws it):** `timeline.transitions` `{"t": <cut>, "type": "leak", "frames": 15, "pre": 6, "colours": ["#FF5E7A", "#FF8A3D", "#FFC2A8", "#FFFFFF"], "angle": 35, "peak": 1.0}` (6 f build, cut, 9 f residue). Section breaks add the 1 f white on the cut: `fx.flash({id, at: <cut>, up: 1, hold: 0, decay: 2, peak: 1.0})`. TH-lime item doors: the same leak with `"colours": ["#FF3B2F", "#FF8A3D", "#FFC83D"], "peak": 0.95` and no white flash. Two luminous starts per door at most, doors ≥ 6 s apart: inside | whoosh + impact on the peak |
| **T-3** | Dim | 12 | `via: dim`: blur 0 → 12, luma 0 → −0.5, ramped over 12 f after T-11 (v03 @0:24.62–0:25.0) | — |
| **T-4** | Slide-down / slide-up split | 9 | engine `slide-down` / `slide-up` | light whoosh |
| **T-5** | Vortex into the wheel | 18 | T-2's leak (built-in `leak`, 8 f: `"frames": 8, "pre": 8`) covers the series card; under it the frame **zooms through** into W-wheel: the wheel world scales in ×1.19, 1.13, 1.08, 1.05 … per frame (expo-out, ≈ 10 f), the presenter ghosted, then matted in front (v03 @0:17.12–0:17.60). The wheel scene does its own scale; its radial blur is a `timeline.grades` `{"t": <cut>, "blur": 14, "dur": 0.33, "frame": true}` frame blur pulse (no bespoke CSS blur). Without W-wheel: 36 seeded radial streaks + scale 1.0 → 1.25 | riser end (transition) |
| **T-6** | Lime swipe | 2 | 3 horizontal `primary` bars (h 60, gap 30, over the numeral band, cy ≈ 1200) sweep L → R with heavy motion blur in 2 f; the numeral is complete on the next frame (v03 @0:23.03–0:23.10, @1:28.43–1:28.47). **Build:** `fx.streak({id, at, frames: 2, y: 1200, angle: 0, color: "primary", width: 60, count: 3, spread: 90, length: 1.0, glow: 12})` | swish |
| **T-7** | Screen crossfade | 4 | inside a card window only | none (or a soft click on a click) |
| **T-8** | Fade-through | 14 | engine `fade-through`; fallback only (boards enter by cut and leave by T-12) | light whoosh |
| **T-9** | Dot dissolve | 6 | the opening image dissolves into P-DOT-REVEAL dots, sweeping, f5–f10 (v02 @0:00.17–0:00.33) | none |
| **T-10** | Hard end | 0 | cut to black ≤ 6 f after the last word | none |
| **T-11** | Smear wipe | 3 | Horizontal streaks (white + the outgoing colours, 6–20 px tall, h-blur 40 px) race across the chest band and carry the numeral out; the card is complete on the next frame (v03 @0:24.55–0:24.65). **Build:** `fx.streak({id, at, frames: 3, y: <chest band cy>, angle: 0, color: "paper", width: 14, count: 6, spread: 200})` (a second one in the outgoing colour if wanted); the numeral leaves with `out: "slide-r", out_frames: 3, smear: true` (a directional smear, not a uniform blur) | swish |
| **T-12** | Zoom-through | 8 | The board's phone pushes ×1.03–1.06 per frame for 4 f, then rushes into its own white screen with motion blur for 4 f; hard cut on the white (v01 @1:17.68–1:17.93). The phone scene scales itself; the motion blur of the last 4 f is a built-in `{"t": <cut>, "type": "zoom-blur", "frames": 4, "pre": 4, "amount": 0.25, "punch": 0, "at": "centre"}` | whoosh |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | the archetype's f0, already built | a fade from black |
| Hook → series card | **T-2 warm wash** | a hard cut |
| Series card → promise / first item | **T-5** into W-wheel (TH-lime, once per reel); **T-2** white peak into `#01` (TH-studio, v01 @0:10.3) | — |
| New item | **TH-lime: T-2 → Z-1 rush-in → T-6 → numeral, every item.** TH-studio: T-1 with the numeral smearing in on the cut frame | mixing the two doors in one reel |
| Numeral → tool card | **T-11 smear** + T-3 dim | a slow fade into a card |
| Card → presenter | T-1 (or T-3 reversed) | — |
| Sentence → its B-roll | T-1 into L-split (default) / T-4 (≤ 1 per reel) | — |
| Into / out of a full-screen flow | T-1 in, **T-12** out | a fade |
| Screen → screen inside a card | T-7 | moving the window |
| Body → end stack | **T-2 warm wash** | — |
| Last word | T-10 | a black tail > 0.2 s |

### 9.3 Shot grammar: OFF (the spine is `talking_head`; jump cuts follow H5 and §10.2)

### 9.4 Budget (per 60 s, scaled for 90–170 s)
- T-2: TH-studio ≤ 4 per reel (hook → series / #01, one mid-reel break, body → end stack); TH-lime one per item door + the 3 section breaks (v03: 13 in 163 s), never two within 6 s.
- T-5: 0 or 1 per reel.
- T-6: TH-lime one per item (the numeral's door); TH-studio none.
- T-3: one pair per tool card.
- T-11: one per tool card. T-12: one per board. Hard cuts are free.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset |
| Entry ease | `cubic-bezier(0.22, 1, 0.36, 1)` (expo-out); doors are 1–3 f (smears, swipes, snaps), soft entries (chips, notes, series number) 3–8 f |
| Exit ease | `cubic-bezier(0.64, 0, 0.78, 0)`, 4–6 f |
| Numeral | A: 1–2 f horizontal smear-stretch on the cut frame, no overshoot. B: 2 f lime swipe, snap, digit flicker ≈ 8 f. No growth during the hold |
| Chip drop | 24 px + fade, 6 f |
| Card in | T-11 smear 3 f, then complete (no rise); dim ramp 12 f |
| Blur-in (series number, stat value) | blur 14 → 0 px + fade, 3–6 f; word groups and italic lines smear in horizontally over 2–3 f |
| Type-on | ≈ 50 characters/s (1.5–2 per frame): TH-lime plain caption lines; the series kicker 1 char/f. Captions: `reveal: "char"`, `cps: 50`; scenes: `fx.typeOn` |
| Warm leak (T-2) | build 6 f, peak 1 f white or 3–6 f red-yellow, fall 1–2 f, residue 6–10 f: built-in `leak` `frames` 15, `pre` 6 (+ `fx.flash` 1 f white at section breaks) |
| Logo behind the head | cut on at full size, +14 f after the numeral |
| Screen swap | crossfade 4 f |
| Cursor glide / tap | 10 f glide, 3 f tap at scale 0.9 |
| Holds | text ≥ 0.25 s per word; titles ≥ 10 f after built; numerals ≥ 36 f |

### 10.2 Footage camera: `zoom_policy: crop_on_cut`
| ID | Preset | Recipe | Use |
|---|---|---|---|
| **Z-1** | `snap-punch` (**rush-in**) | The cut lands **wide** and rushes ×1.7 to the base framing over **12 f**, `ease: "expoOut"` (per-frame ×1.20, 1.15, 1.07, 1.05, 1.035, 1.025 …), starting **on the cut under a T-2 wash**: `from_wide: 0.59` (= 1 / 1.7), `scale` [1.0, 1.0] (measured v03 @0:22.97–0:23.37, @1:28.27–1:28.67, @2:33.47–2:33.77). After the hook wash the softer one: `{"t": <cut>, "preset": "snap-punch", "p": {"from_wide": 0.89, "frames": 8}}` (×1.12 over 8 f, v03 @0:08.73–0:08.93). It ends on the base framing, so nothing resets it | every T-2 door: TH-lime every item; both themes at section breaks |
| **Z-2** | `crash-zoom` (**rush-in B**) | Identical to Z-1 (`from_wide: 0.59`, 12 f, `expoOut`) under a second preset id | consecutive doors alternate Z-1 / Z-2 (V-CAMERA rejects the same preset twice in a row) |
| **Z-3** | `push-drift` | 1.00 → 1.08, linear, over a ≥ 3 s beat, starting on a cut (measured +9.6 % over 5 s, v01 @2:48.9–2:53.9) | L-full holds ≥ 3 s (the only long static stretches); `awe` beats |
Rules: camera moves start only on cuts (V-CAMERA `crop_on_cut`); never the same Z twice in a row; plain jump cuts keep the crop (measured, §3.6); no camera change while a card or the split is up; no shake, no rotation. `from_wide` never goes wider than the raw footage: the rush-in starts at 1 / (base reframe), capped at 1 / 1.7. So the full ×1.7 needs a base reframe ≥ 1.7 (shoot 4K, or frame the take wide: head small in the frame); a take already framed tight rushes in only as far as the raw frame allows (a take at the target framing: no rush at all, so shoot wide).

### 10.3 Canvas camera: OFF (§21)

### 10.4 Layer order (back to front)
1. The world (W-void / W-board / W-endcard), the presenter's footage, or W-wheel (behind the cut-out)
2. Behind-the-head elements (`behind: true`: P-LOGO-BEHIND, P-SAVE-BADGE, P-DELIVERABLE-TILE)
3. The presenter cut-out (only while a behind scene is up), then the L-card **dim** treatment
4. Split-top content (B-roll, created UI) and its black seam fade
5. Cards: tool-card window, note card, proof card, phone mock (z3/z4)
6. Brand row, stat lines, HUD marks, cursor box (z5)
7. Price chips, logo pops (z6)
8. Captions CS-1/CS-2 (z7)
9. Numeral, chips, series card, end-card lines (z8; captions hide)
10. The plate (z10)
11. Light passes: T-2 leaks and blur pulses are drawn by core (`timeline.transitions` / `timeline.grades`, under the captions); the white peak (`fx.flash`) and the T-6 / T-11 streaks (`fx.streak`) are z11

### 10.5 Finishing
- No grain, no vignette on footage, no bloom except the community headline's 28 px lime glow and the end-card world's glow.
- Cards: radius 28 (windows), 26 (note cards), 18 (proof card); soft shadows only (`0 18 40 rgba(0,0,0,.35)`); no hard offset shadows anywhere.
- Footage is not regraded; exposure and white balance are matched between setups.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
Sound comes from the bundled SFX pack and its global rules S1–S6 (every cue marks a visible event, ≤ 2 uses per file, one list-cue exception, no consecutive repeats, catalogue ids only).

| Line | Decision |
|---|---|
| **Cue moments** | `hook` (f0 whoosh-hit as the plate group lands, the first cut), `transitions` (T-2: whoosh into an impact on the white peak; T-5: riser end; T-6 / T-11: swish; T-12: whoosh), `reveals` (series card number, price strike, community card), `list_cue` (every numeral shares one cue, on its swipe/cut frame), `cta` (the Link in Bio tap). The rush-in (Z-1) rides the T-2 cue; no separate sound |
| **Meme cues** | off (comedy is off) |
| **Music bed** | on; enters at the series card (after the hook); calm tech / lo-fi from the pack |
| **Ducking** | bed ≥ 18 dB under the voice while the voice speaks; supplied clips (HA-18) keep their own audio, the bed is muted under them |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

Mirrored in `tokens.json → sound`.

---

## §12 Footage requirements, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's setups]`
| Setup | Camera | Framing | Set & light | Wardrobe |
|---|---|---|---|---|
| **A Seated desk** (default) | Tripod at eye level, 35–50 mm equiv., 4K 30 fps preferred | Mid-chest, centred; head top y 300–460, chin y 760–880; hands on the desk in frame | A tidy, warm room: one lamp or practical, shelves or a plaque in soft focus; warm key from 45° | A plain mid-tone or dark top (no logos), so the dimmed L-card still separates |
| **B Standing** | Tripod at chest height | Mid-thigh, centred; head top y 220–380, chin y 700–820; a handheld or lapel mic is fine | Bright, clean studio, practicals behind | Same |

Frame rate: 30 fps CFR (conform VFR). The presenter looks into the lens; no B-cam needed.

### 12.2 Shot list
| ID | Shot | Spec | Count per 60 s | Must / optional | Formats |
|---|---|---|---|---|---|
| **SH-1** | Screen recording of each tool / feature | 1080 px wide or more, 30 fps, cursor visible, 5–15 s per item covering the 2–4 features said; personal data blurred (NC-14) | 3–6 clips | **must** (F-A) | F-A |
| **SH-2** | Product / feature B-roll or screenshots | the creator's own captures or press material they hold | 2–6 | optional | F-A, F-B |
| **SH-3** | Logo files of each tool | SVG/PNG with transparency | one per item | optional | F-A |
| **SH-4** | Own post screenshot + a clip the creator holds | post PNG; clip ≥ 720 p, 3–8 s | 0–1 per reel | optional | F-A, F-B (HA-18) |
| **SH-5** | Story B-roll (renders, product films) | the creator owns or holds them | 3–8 | optional | F-B |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Format |
|---|---|---|---|---|
| **FB-1** | SH-1 | A recreated generic UI (`fx.appUI` list / browser / terminal / chat) built from the script's words inside the same tool card; the cursor box still taps the named element | No real product footage; reads as an illustration | **degraded** |
| **FB-2** | SH-2 | P-SPLIT-UI, P-FEATURE-GRID, P-NOTE-CARD or P-STAT-LINE in the split top | Less "proof", more explainer | holds |
| **FB-3** | SH-3 | Logo plate: the tool's name in type on the `tile` chip; a monogram tile behind the head (E1) | No brand mark or colour | holds |
| **FB-4** | SH-4 | HA-02 plate + proof hook instead; or a created quote card (verbatim words from the script) + a created video UI | Loses the "someone else's viral moment" pull | holds |
| **FB-5** | SH-5 | P-FRAMED-CLIP and P-SPLIT-BROLL with created diagrams, P-DOT-REVEAL and stat lines | Less cinematic | degraded |

Say at the checkpoint which fallbacks were used.

### 12.4 Props, matte, resolution
- **Props:** optional: the product the reel is about, held at chest height for the hook (v01's foldable phone). Never block the face with it.
- **Reaction bank:** none.
- **Matte:** only when the reel uses a behind-the-head pattern (P-LOGO-BEHIND, P-SAVE-BADGE, P-DELIVERABLE-TILE). Check hair edges at 200 %.
- **Minimum source resolution:** the Z-1 / Z-2 rush-in starts on the raw (wide) take and lands on the base framing, so the base reframe sets its size: ×1.7 needs a take framed wide enough that the base reframe is ≥ 1.7 (4K, or the head small in a 1080p frame). Shot at the target framing, the door has no rush-in; frame wider than §12.1. Recordings < 1080 px wide go into the split top (960 px tall band) rather than the card window.

### 12.5 Third-party inserts: ask, then create `[REQ always]`
This style is built on other companies' products, so it has more third-party moments than most. Per reel:
1. **Analyse the transcript** (`veos inserts scan`) and list the moments: each tool's UI and logo, product photos, posts, clips, news headlines.
2. **Ask the creator once**, as one list: "For these N moments, do you have a recording, screenshot, logo or clip? (drop the files, or say no)". Recordings the creator made of a tool's public UI count as theirs.
3. **Supplied:** use them as given (cropped, framed in the card, highlighted with the cursor box), never altered to say something they don't.
4. **Not supplied:** Claude builds its own visual from the script's words:
   | Moment | Created substitute | Recipe |
   |---|---|---|
   | A tool's UI / recording | `recreated_ui` | `fx.appUI` (list / browser / terminal / chat) in the card window |
   | A logo | `logo_plate` | `fx.logoPlate` on `tile` (brand row), a monogram tile behind the head (E1) |
   | A post / tweet | `quote_card` | `fx.quoteCard` with the verbatim words from the script; generic avatar initials |
   | Another creator's clip | `recreated_ui` (video) | `fx.appUI({kind: "video", caption})` with the spoken line as its caption |
   | A news headline | `headline_card` | `fx.headlineCard` with the outlet name in type and the exact headline from the script |
   | A person's photo | `silhouette` | `fx.silhouette` with the name and role from the script |
   | A product photo | `diagram` | `fx.card` with an `fx.icon` of the product type |
5. **Record** every insert in `plan/inserts.json` (`{id, moment, origin: creator | created, file?, substitute_of?}`), and pass its id as `insert` on the scene.

### 12.6 Frame rate and audio
30 fps CFR, 1080 × 1920, BT.709. One voice track: high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section` (`HOOK | INTRO | SERIES | ITEM-n | BEAT-n | PAYOFF | CTA`), `t0`/`t1`, `spoken`, `trigger {word, at}`, `tone`, `line_type`, `layout` (L-…), `visual` (one sentence), `layers` (scene ids), `pattern` (P-…), `sfx`.

### 13.2 Conditional fields used by this style
| Switch / module | Beat fields |
|---|---|
| captions | `caption {profile: CS-1 \| CS-2, overrides[], emphasis[]}` (emphasis = the P5b phrase) |
| series | `series {unit, number}` on the SERIES beat |
| brand | `sponsor {id, disclosure}` on paid beats |
| themes per_reel | none per beat (the reel header carries `theme`) |
| footage ≥ medium | `shot_id`, `fallback_used` |
| third-party moments | `insert {id, origin: creator \| created}` |
| exceptions | `exception: "E1"` on monogram beats |
| re-hooks | `rehook: true` on numeral, teaser and question beats |
| item ritual | `item {n, of, numeral: SM-NUM-A \| SM-NUM-B, chip: label \| teaser \| recap, chip_text, tool, logo: creator \| monogram}` |

### 13.3 Reel header
```yaml
reel:
  format: F-A                 # F-A Countdown | F-B Daily brief
  theme: TH-lime              # TH-studio (CS-1, SM-NUM-A) | TH-lime (CS-2, SM-NUM-B)
  hook_archetype: HA-05
  structure: news             # F-A news | F-B explainer
  count: 10
  numbering: desc
  series: {unit: Week, number: 9, name: "{{BV-13.name|the AI tools}}"}
  cta: {device: "{{BV-08.device|follow_save_stack}}", community: "the free community", keyword: null}
  sponsor: null
  captions_profile: CS-2
```

### 13.4 Hook proposals (3)
```yaml
- name: "Teaser lockup: three free tools"
  archetype: HA-05
  headline: "#02, #03 and #08 / do the whole job for free"       # lockup, 8 words
  pair: {promise: "three of ten tools replace a paid one", proof: "three tool tiles, then #10"}
  stoppers: [lockup readable at 0.7 s, 3 tiles popping, presenter live]
  captions: {profile: CS-2, emphasis: ["#02, #03 and #08"]}
  storyboard: "f0 presenter + italic lockup | 0.4 tiles pop x3 | 1.5 'let me show you' | 3.0 wash | 3.4 series card Week 09"
  sound: [hook hit f0, soft pops x3 (one file + pack variants), wash whoosh]
  stopper_test: {thumbnail: pass, mute: pass, read_s: 1.1, changes_3s: 5, payoff_s: 0.7}
```

### 13.5 Checkpoint
Send, then **wait for approval**:
1. 3 hooks with their stopper-test results.
2. The beat sheet with tones, the item → card table (number, tool, chip, logo origin, screens, cursor element, pop-back line) and the emphasis phrases.
3. The transition map and the SFX ledger.
4. The inserts record (creator-supplied vs created) and the fallbacks used.
5. Style stills: f0, the payoff (≤ 2.5 s), the series card, one numeral, one tool card, one split, the community card.

---

## §14 Worked examples `[REQ] [NICHE: example]`

Times are planning estimates; replace them with `words.json` onsets. Bracketed names are slots the reel's script fills (no real product claims are implied).

### 14.1 F-A Countdown, N1 AI tools: "Week 09 of the AI tools" (TH-lime, HA-05, desc 10 → 01, 150 s)
**Hook table**
| t (s) | Spoken | Tone | Visual | Caption | Layout / camera | SFX moment |
|---|---|---|---|---|---|---|
| f0 | — | awe | Presenter at the desk; italic lockup building | "*#02, #03 and #08*" (92 px) / "do the whole job for free" | L-full | hook hit |
| 0.4 | "#02, #03 and #08 do the whole job for free" | win | P-TEASER-TILES: three tiles pop (monograms if no logos) at cy 1340 | tiers | L-full | pop ×3 (pack variants) |
| 1.6 | "Let me show you" | explain | Tiles exit; hard jump cut (same crop) | plain pill "Let me show you" (no emphasis: stop-words only) | L-full | — |
| 2.6 | "I went through 100 launches this week" | explain | — | pill "I went through" / "*100 launches*" / "this week" | L-full | — |
| 4.4 | "and picked these 10, completely free" | win | — | "and picked these 10" / "*completely free*" | L-full | — |
| 6.2 | — | — | **T-2 warm wash** | hidden | cut under the wash | wash |
| 6.6 | "Welcome to Week 09 of the AI tools" | awe | **P-SERIES-CARD** "Welcome to / *Week 09* / of the AI tools" | hidden | L-full, Z-3 drift | bed enters; reveal on "09" |
| 8.8 | "Let's dive into it" | hype | **T-5 vortex** into item 10 | italic "*Let's dive into it*" | — | riser end |
| 9.6 | "Number ten…" | explain | Item 10 ritual | hidden under the numeral | L-full | list cue |

Intro = 9.6 s (6.4 % of 150 s, ≤ 15 %). Payoff (lockup) at 0.4 s.

**Section plan**
| Section | Spoken gist | Layout | Patterns |
|---|---|---|---|
| #10 (9.6–22) | "[TOOL-10] turns any video link into notes, a transcript and key takeaways" | L-full → L-card | P-NUMERAL-B "10" + chip "Video to notes" + P-LOGO-BEHIND; P-TOOL-CARD (recording, 3 screens: link pasted / transcript / takeaways) with P-CURSOR-BOX on "Analyse"; pop-back "you never sit through / *a lecture again*" |
| #09 (22–34) | "[TOOL-9] records your screen and turns repetitive tasks into automations" | L-card | ritual; 4 screens; P-PRICE-STRIKE: "[OTHER] charges $[X] a month" → FREE |
| #08 (34–46) | "[TOOL-8] makes original music for your reels" | L-card | ritual; screens: plans page → generator → download; cursor box on "Add to downloads" |
| #07 (46–58) | "[TOOL-7] gives you 200 open models for image, video and audio in one place" | L-card → L-full | ritual; P-STAT-LINE "*200* open models" on the pop-back |
| #06 (58–70) | "[TOOL-6] checks if the person on your call is real or a deepfake" | L-card | ritual; screens with created "DEEPFAKE DETECTED" only if it is in the recording (never added) |
| #05 (70–82) | "[TOOL-5] records, transcribes and summarises meetings on your own laptop" | L-card | ritual; P-LOGO-CLUSTER of two paid alternatives on "unlike [A] and [B]" |
| #04 (82–96) | "[TOOL-4] finally gets text right in images" | L-card | **T-6 lime swipe** into the numeral; screens ×4 |
| #03 (96–108) | "[TOOL-3] makes a full video from one prompt" | L-card | ritual; **teaser chip** "Wait for the next 02 >>>" replaces the label chip |
| #02 (108–122) | "[TOOL-2] clones your voice from 3 seconds of audio, free forever" | L-card | ritual; P-PRICE-STRIKE "$22 a month" → FREE; pop-back "*free forever*" |
| #01 (122–136) | "[TOOL-1] is a free coding agent you run on your own machine" | L-card → L-full | ritual; the longest card (5 screens); pop-back "*my favourite this week*" |
| End (136–150) | Save / Follow / all 10 with the links / community | L-full → L-board | T-2 wash → P-SAVE-BADGE + "*90% of you*" → follow line + handle chip → P-DELIVERABLE-TILE + "*all 10 with the links*" → P-COMMUNITY-CARD 3.5 s → T-10 |

Re-hooks: every numeral (≤ 14 s apart) + the teaser at #03. Third-party: 10 recordings (creator), 10 logos (creator or FB-3 monograms).

### 14.2 F-A Countdown, N2 money apps: "5 app updates that save you money" (TH-studio, HA-02, asc 01 → 05, 100 s, Hinglish speech → English captions)
**Hook table**
| t (s) | Spoken (translated caption) | Tone | Visual | Caption | Layout | SFX |
|---|---|---|---|---|---|---|
| f0 | — | awe | Plate "The best update / **of [APP] this month**" + proof card (the creator's own app screenshot left, "This isn't the / **best part**" right) + presenter holding the phone | hidden | L-full | hook hit |
| 1.0 | — | awe | Card event: the screenshot's toggle flips on | — | — | soft pop |
| 1.7 | "[APP] just shipped five updates" | explain | Cut to L-split: the creator's screen recording of the app (top) | seam pill | L-split | light whoosh |
| 3.2 | "but nobody is talking about the one that saves you money" | awe | L-full (jump cut, same crop) | "but" / "*nobody is talking*" / "about the one…" | L-full | — |
| 5.8 | — | — | T-2 wash | — | — | wash |
| 6.2 | "Welcome to Day 12 of money made simple" | awe | P-SERIES-CARD "Welcome to / *Day 12* / of money made simple" | hidden | L-full | reveal |
| 8.2 | "Number one…" | explain | `#01` SM-NUM-A + chip "Split bills" | hidden | L-full | list cue |

**Section plan**
| Section | Spoken gist | Patterns |
|---|---|---|
| #01 (8–24) | "Split a bill with friends inside the app" | P-TOOL-CARD (creator recording), P-CURSOR-BOX on "Split", P-NOTE-CARD "Your friend owes you ₹450" (the spoken amount) at chest on the pop-back |
| #02 (24–40) | "Auto-pay limit you set yourself" | P-PHONE-BOARD (TH-studio warm board) 3.5 s with created rows "Set limit → Pick account → Done" → back to L-card |
| #03 (40–56) | "Free credit score, no third-party app" | P-PRICE-STRIKE "₹99 per report" → FREE; teaser chip "Wait for the next 02 >>>" |
| #04 (56–72) | "UPI Lite for small payments without a PIN" | P-SPLIT-BROLL (the creator paying at a shop) + P-STAT-LINE "*₹500* without a PIN" (spoken value) |
| #05 (72–86) | "International payments at the real rate" | P-TOOL-CARD; pop-back "*this one is my favourite*" |
| End (86–100) | Save / Follow / Comment MONEY | wash → P-SAVE-BADGE → follow line → P-COMMENT-CARD "Comment **MONEY** and I'll send you all 5 steps" (keyword ≥ 1.5 s) → T-10 |

Numbers in Indian format (BV-06 from Hinglish): ₹450, ₹99, ₹500.

### 14.3 F-B Daily brief, N1 tech: "Day 60: [COMPANY] built a full-body scanner" (TH-studio, HA-12, 90 s)
| Section | t (s) | Spoken gist | Layout | Patterns |
|---|---|---|---|---|
| Hook | 0–3 | "One image-gen AI company just announced a full-body ultrasound scanner" | L-split | creator B-roll (or P-DOT-REVEAL), seam pill at 0.33 s, italic "*a full-body scanner*" at 1.67 s, P-HUD-MARKS at 2.2 s |
| Hook | 3–6.5 | "that scans your body in just 60 seconds. Even radiologists are shocked" | L-split → L-full | second B-roll + "*in just 60 seconds*"; L-full "Even radiologists / *are shocked*" |
| Series | 6.5–9.5 | "Welcome to Day 60 of future tech updates" | L-full | T-2 wash → P-SERIES-CARD |
| What | 9.5–22 | "Why would a company that makes AI art build this?" | L-split → L-full | P-SPLIT-BROLL of the product page they recorded; SM-QUESTION "So why does an AI / *company want it?*" (re-hook) |
| Mechanism | 22–36 | "a shallow pool, a million sensors, sound through you, a computer maps everything" | L-split | P-SPLIT-BROLL ×4 swaps (creator renders) or FB-5 diagrams; P-RENDER-WORDS "No radiation" / "No magnet" / "No tube" (L-board, 3 s) |
| Twist | 36–55 | "But here's where you slow down… 50,000 scanners doing a billion scans a month by 2031" | L-full → L-split | italic "*where you slow down*" (re-hook); P-STAT-LINE "*50,000* scanners" and "*1 billion* scans a month" (spoken values) |
| Stakes | 55–72 | "You can change a password. You cannot change your organs. Who owns that file?" | L-split → L-full | P-SPLIT-UI password field (created) → SM-QUESTION "*Who owns that file?*" (re-hook) |
| Caveat | 72–82 | "To be fair, it's still a prototype; it can't diagnose anything yet" | L-full | italic "*still a prototype*"; P-FRAMED-CLIP 3 s with "That 60-second scan / *takes twenty minutes today*" |
| End | 82–90 | "You ask the questions before you step into the water… join the community" | L-full → L-board | "You ask the questions before you step" / "*into the water*" → P-COMMUNITY-CARD 3.5 s |

Re-hooks at 9.5 (question), 36 (twist), 62 (question), 72 (caveat): max gap 26 s → move the stakes question to ≤ 60 s.

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] Format and theme declared; caption profile matches the theme (CS-1 ↔ TH-studio, CS-2 ↔ TH-lime); one numeral variant and one window frame in the whole reel. `V-THEME` + review
- [ ] Duration inside the class (F-A 90–170 s, F-B 70–100 s). `review`
- [ ] Presenter ≥ 75 %, longest absence ≤ 8 s (hook only), ≤ 4 s elsewhere. `V-PRESENCE` + review
- [ ] Layout shares inside §3.2; only L-full / L-split / L-card / L-board. `V-LAYOUT`

**2. Hook**
- [ ] f0 per archetype (plate + proof + presenter / post + clip / split B-roll + caption / lockup). `V-F0`
- [ ] Payoff by 2.5 s (3.0 s HA-12, 0.7 s HA-05); ≥ 4 weighted SCs in 0–3 s. `V-F0`, `V-CADENCE`
- [ ] Plate ≤ 9 words on 2 lines, reads in ≤ 1.5 s, gone by the first split or wash. `V-TITLE`
- [ ] Mute test passes. `review`

**3. Body and cadence**
- [ ] 4–8 weighted SCs per 10 s; max gap 2.5 s; nothing static > 2.5 s. `V-CADENCE`
- [ ] Every F-A item has the full ritual: door (TH-lime T-2 + Z-1 + T-6; TH-studio hard cut), numeral, chip, logo moment, T-11 into the card, ≥ 2 screens. `review`
- [ ] Motion check at full frame rate (step through 0.7 s around one door, one numeral, one card entry): doors 1–3 f, no eased pops or rises, the rush-in starts on the cut, the white peak is 1 frame, no zoom anywhere else but Z-3 drifts. `V-CAMERA` + review
- [ ] Numbering continuous in one direction; count matches the promise; teaser number right. `V-PROMISE`
- [ ] Intro ≤ 15 %; a re-hook every ≤ 25 s. `V-REHOOK`
- [ ] Numerals on their ordinal ±5 f; brand rows on the tool name ±2 f; screens on their feature word. `V-ONWORD`
- [ ] Cards never move while screens swap; no card run > 14 s without a swap. `review`

**4. Captions**
- [ ] Every word captioned; ≤ 1 emphasis phrase per chunk and per 4 s; phrases 2–4 words, ≤ 22 characters, never stop-words. `V-CAPTION` + review
- [ ] Full frames: emphasis chunks bare 60 px; plain-only chunks a 44 px pill (TH-studio, hard swap) or bare 60 px typed on (TH-lime); 42 px pill text on the seam/card (pill contrast ≥ 4.5:1); emphasis 116 px (80 px on the seam) Instrument Serif Italic; sync lead ≤ 0.15 s. `V-TYPE`, `V-EXC`, `V-CAPTION`
- [ ] Glossary spellings exact for every tool and brand. `V-CAPTION`
- [ ] Captions hidden under the numeral, series card, plate and end-card lines. `review`

**5. Modules**
- [ ] §24 Series card at 8–15 s (or the count card), hold 1.8–2.2 s, inside the intro cap. `V-REHOOK` + review
- [ ] §25 End stack order Save → Follow → Deliverable → Community/Comment; community card ≤ 4 s; Link in Bio or keyword readable ≥ 1.5 s; disclosure ≥ 2 s on paid integrations. `V-PROMISE` + review

**6. Truth and inserts**
- [ ] Every tool UI, logo, post, clip is creator-supplied or a created substitute with a record; created UIs. `V-INSERTS`
- [ ] Prices and numbers on screen are spoken or in the creator's recording; formatted per BV-06. `V-NUMFMT` + review
- [ ] Monograms behind the head: ≥ 65 % visible, letters readable. `V-EXC`
- [ ] Personal data in recordings blurred (NC-14). `review`

**7. Sound contract**
- [ ] Cues only on the §11 moments; one list cue for all numerals; no meme cues; bed from the series card; −14 LUFS, TP ≤ −1.5 dBTP. S1–S6 + review

**8. End and export**
- [ ] Hard end ≤ 6 f after the last word; no black tail. `review`
- [ ] 1080 × 1920, 30 fps CFR. `review`

---

## §16 Frame template / chrome: OFF (`profile.modules.chrome = false`; no persistent slot: every frame re-composes around the presenter)

## §17 Running state & anchored graphics: OFF (`profile.modules.running_state = false`, `anchors = false`; the countdown number is a per-item marker, not a running counter; chest graphics use static positions from §3.5)

## §18 Data contract: OFF (`profile.modules.data_figures = false`; numbers appear only as spoken values in stat lines, price chips and captions, checked by V-NUMFMT; no charts)

## §19 Evidence & citations: OFF (`profile.modules.citations = false`; no credit lines or source cards in the reference reels. Third-party moments still follow the §12.5 inserts flow)

## §20 Dialogue: OFF (`profile.modules.dialogue = false`; one presenter)

## §21 Canvas camera: OFF (`profile.modules.canvas_camera = false`; `graphics: support`)

## §22 Ink & annotation layer: OFF (`profile.modules.ink = false`; the only annotation is the clean P-CURSOR-BOX, no hand-drawn marks)

## §23 Continuity: OFF (`profile.modules.continuity = false`; the ritual repeats, but scenes are not morph-chained)

---

## §24 Series furniture `[COND: modules.series] [DNA look; VAR name/number]`
- **Series card (P-SERIES-CARD):** "Welcome to" / *{unit} {number}* / "of {{BV-13.name|future tech updates}}". Placement 8–15 s (after the hook's wash, before the first item), hold 1.8–2.2 s, captions hidden, Z-3 drift on the presenter. It counts toward the 15 % intro cap.
- **Unit and number:** `Day`, `Week`, `Episode` or `Part` + the number from the reel brief, two digits for 1–9 in `Week` series ("Week 09") and as said for `Day` ("Day 60").
- **Tokens:** `series {name, number, unit, tag_format: "{unit} {n}", pad: 2, card {at_s: [8, 15], hold_s: 2.0}}`.
- **No series yet (count card fallback):** the same three-line recipe with the count: "Here are / *10 tools* / you can't miss this week" (F-A) or "Today's / *one story* / in 90 seconds" (F-B). Never invent a series number.
- **Series memory:** a series keeps its theme pack (§4.3) and its unit; the editor records `{name, unit, last_number, theme}` in the copy's niche notes after each approved reel.
- **No persistent series tag** (the reference reels show none).

## §25 Sponsor, brand & end cards `[COND: modules.brand or cta ∋ end_card] [DNA look; VAR assets]`

### 25.1 Sponsor
- **P-SPONSOR-ROW** on the sponsor's tool card: their logo (supplied) in the brand row; **"Paid partnership"** (BV-14 wording) as TC-legal 26 px at x 64, y 140, held for the whole sponsored item (≥ 2 s) and said in speech (NC-12).
- The sponsor's colours stay inside their logo; the card frame keeps the theme's style.
- Never over the face, never in the end stack.

### 25.2 Logo pops
P-LOGO-POP / P-LOGO-CLUSTER use the brand's own logo files only (supplied), else monogram tiles on `tile`.

### 25.3 End stack (`follow_save_stack`, the default)
| Step | Element | Geometry | Timing |
|---|---|---|---|
| 0 | T-2 warm wash from the last item | full frame | 12 f |
| 1 | **P-SAVE-BADGE** behind the head + "Save this now because" / "*90% of you*" / "will forget" | badge x 260–820, y 140–700 | 2.0–3.0 s |
| 2 | Follow line: "And follow because I do this" / "*every single week*" + handle chip {{BV-01.handle|@yourhandle}} (TC-legal 28 px, `paper` on 60 % `ink`) at cy 1220 | L-full | 1.5–2.5 s |
| 3 | **P-DELIVERABLE-TILE** behind the head + "And if you want" / "*all 10 with the links*" | tile x 390–690, y 180–480 | 1.5–2.5 s |
| 4 | **P-COMMUNITY-CARD** (W-endcard): "Join the free / {{BV-08.community|Community}}", phone mock, **Link in Bio** pill tapped at 1.2 s | §8.3 | 3.0–4.0 s (≤ 4 s) |
| 5 | Hard end (T-10) ≤ 6 f after the last word | — | — |

Rules: the end stack lasts 10–14 s in F-A, 6–9 s in F-B (steps 2–3 may merge); the community card ≤ 4 s; "Link in Bio" readable ≥ 1.5 s; black tail ≤ 0.2 s. Variant `comment_keyword` swaps step 4 for P-COMMENT-CARD; variant `end_card` keeps steps 1, 2 and a 3 s community card without the phone.

---

## Part C. Exceptions and the non-overridable core (this template)
- **Declared:** E1 (monograms behind the head only, ≥ 65 % visible, hold ≥ 0.6 s, ≤ 1 at a time) and E3 (40–53 px captions, weight ≥ 500, pill contrast ≥ 4.5:1, labels 32–39 px only when redundant). Limits: §2.2; tokens: `exceptions.E1`, `exceptions.E3`.
- **Not used:** E2 (no chaos bursts), E4 (no ambient fields; the end-card dot grid is a world, not items), E5 (no edge bleed: numerals keep 64 px margins), E6 (screen swaps crossfade, captions fade).
- **NC-1…NC-14 apply unchanged.** The ones this style touches most: NC-1 (numerals and chips under the chin; behind-head elements behind the matte), NC-5 (the card window ends at y 1280 and its caption at 1343, clear of the bottom 380 px), NC-6/NC-7 (other companies' UIs: creator recordings or labelled recreations), NC-12 (sponsored items), NC-14 (blur emails and keys in recordings).
- A buyer may switch E1 off (VAR): monograms then sit on the `tile` above the head instead of behind it (y 150–420, fully visible).

## Part D. Personalisation (pick → brand → edit)
**Asked at setup (≤ 4 questions, each with "keep the template default"):**
| BV | Question | Lands on |
|---|---|---|
| BV-01 | Your name and handle | `creator.name`, `creator.handle`; the follow-line chip; the community card's group name default |
| BV-02 | One or two brand colours | `roles.primary` (lime: numerals, CS-2 pill, Link in Bio) and `roles.accent` (red: plate line 2, Save badge); contrast-nudged against `ink` / `paper` |
| BV-05 | Your speech language and caption language | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06). |
| BV-08 | Your call to action | `profile.cta.chosen`: Save/Follow + community link in bio (default), comment keyword (+ keyword), or follow end card; plus the community name |

**Defaulted, changeable later:** BV-03 fonts (inside each slot's class, §5.1), BV-07 caption mode (DNA here: always full), BV-09 formats (both on), BV-10 default theme (TH-studio), BV-13 series (unit, name, number; off → count card), BV-14 disclosure wording, BV-15 never-on-screen list, BV-16 logo and community screenshot, BV-17 duration inside the class.

**Lock summary** (full map in `tokens.json → locks`):
| Level | What |
|---|---|
| DNA | The profile switches, the layouts and their engines, the caption mechanics (tiers, italic serif, unit), numeral recipes, the item ritual, hooks set, transitions, zoom policy, E1/E3 |
| TUNE | Caption sizes (CS-1 54–66 / 100–130; CS-1S, CS-2 40–48 / 72–92), caption y (1000–1130), seam y (900–1060), dim (blur 8–16, luma −0.6…−0.35), numeral size (300–380), cadence ±15 %, motion ±15 %, fonts within class, presence share 65–100, energy calm/balanced |
| VAR | Brand colours, language, numbers, CTA device and values, series, default theme and format, numbering direction, sound, disclosure wording |
| NICHE | §6.4 hook pairs, §8.4 lookup, §14 examples, App. A |

Per reel, the editor appends: the hook pair (§6.4), new line types (§8.4), approved headlines (App. A), confirmed tool names (glossary), and the series memory (§24).

## Part E. Changes vs the reference playbook (v2) and this template's history
| Area | Reference (Naman) | This template |
|---|---|---|
| Hook | Result-First Roast, yellow slab | HA-02 plate + proof (two-line black/red plate), with HA-18 / HA-12 / HA-05 alternates |
| Captions | Chunky captions + 54–60 px subtitles | Emphasis chunks bare 60 px + 116 px italic serif; plain-only chunks a 44 px pill (TH-studio) or bare 60 px typed on (TH-lime); 42 px pill on the seam and cards (E3) |
| Comedy | Meme layer on `mock` | Off |
| Camera | Z-1…Z-7 snap/crash/shake | Rush-in ×1.7 from wide (`from_wide`) on the cut under each warm wash (Z-1 / Z-2 alternating) + 8 % drift on long holds (Z-3); jump cuts keep the crop |
| Structure | Items with panel drops | `#NN` countdown ritual with tool cards over the dimmed presenter |
| Sound | Per-style palettes and ledger | Minimal contract; bundled pack |
| History | — | v1 (draft): first release from v01–v03 evidence. 2026-10 fidelity audit (stills). 2026-10 motion audit (full frame rate, `docs/audit/tech-countdown/completeness.md`): T-2 is a leak with a white peak and is TH-lime's door on every item; Z-1 became the post-wash rush-in (no re-crops on jump cuts); numeral, logo and card entries are 1–3 f smears/snaps, not eased pops; new T-11 smear wipe, T-12 zoom-through, W-wheel / P-WHEEL-STAGE; TH-studio plain chunks back in a 44 px pill; TH-lime captions type on. 2026-10 built-ins pass: captions `smear` / `reveal: "char"` / `plain_only` pills, Z-1 / Z-2 rush-in ×1.7 via `from_wide` (the 1.25 cap and the Z-2 reset are gone), T-2 as a built-in `leak` + 1 f `fx.flash`, T-6 / T-11 via `fx.streak`, kicker / readout via `fx.typeOn` |
| Engine gaps | — | Closed by the engine built-ins (2026-10): plain-only pills (`connector_container_when: "plain_only"`), per-character type-on (`reveal: "char"`, `cps` 50), horizontal smear swaps (`swap.type: "smear"`), the ×1.7 rush-in from wide (`from_wide` 0.59, `expoOut`), the T-2 leak (built-in `leak` + `fx.flash`), T-6 / T-11 streaks (`fx.streak`). Still open: the leak cannot hold a pure-white full frame itself (the 1 f white is a z11 `fx.flash` on the cut); the T-5 wheel zoom-through and T-12 phone push are scene-driven (the blur parts are built-in) |

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D / BD | D1–D8; BD… (buyer) |
| H / N / BN | H1–H18; N1–N14; BN… |
| E | E1, E3 |
| W | W-studio, W-void, W-board, W-endcard |
| L / G | L-full, L-split, L-card, L-board; G-1–G-6 |
| TH | TH-studio, TH-lime |
| CS | CS-1, CS-2 |
| HA / ST | HA-02 (default), HA-18, HA-12, HA-05; ST-1, ST-2, ST-3, ST-4, ST-6 (+ ST-5 via cadence) |
| SM | SM-NUM (SM-NUM-A, SM-NUM-B), SM-CHIP-LABEL, SM-CHIP-TEASER, SM-CHIP-RECAP, SM-SERIES, SM-QUESTION |
| P / B | 36 patterns (§8.3); B-1–B-8 |
| T / Z | T-1–T-10; Z-1–Z-3 |
| SH / FB | SH-1–SH-5; FB-1–FB-5 |
| F | F-A Countdown, F-B Daily brief |
| V | V-F0, V-CADENCE, V-TITLE, V-ONWORD, V-FACE, V-PRESENCE, V-PROMISE, V-REHOOK, V-CAPTION, V-LAYOUT, V-EXC, V-TYPE, V-INSERTS, V-NUMFMT, V-THEME, V-HUES, V-SAFE, V-CAMERA, V-PROFILE |

---

## App. A Headline & hook bank `[NICHE: example]`

**F-A Countdown** (plates are 2 lines: line 1 / line 2; lockups are italic phrase / pill line)
| # | Headline | Archetype | Niche |
|---|---|---|---|
| 1 | "The most exciting part / of [EVENT]" | HA-02 | N1 |
| 2 | "*#02, #03 and #08* / do the whole job for free" | HA-05 | N1 |
| 3 | "10 AI tools / from this week" | HA-02 | N1 |
| 4 | "Free tools that / replace [PAID TOOL]" | HA-02 | N1 |
| 5 | "The feature nobody / is talking about" | HA-02 | N1 / N2 |
| 6 | "This free tool / ruined [X]'s plan" (the creator's own post) | HA-18 | N1 |
| 7 | "The best update / of [APP] this month" | HA-02 | N2 |
| 8 | "*#01 and #04* / save you ₹[X] a year" | HA-05 | N2 |
| 9 | "5 app settings / to change today" | HA-02 | N2 |
| 10 | "Turn this off / before [DATE]" | HA-02 | N2 |

**F-B Daily brief** (thesis phrase in italic on the seam)
| # | Headline | Archetype | Niche |
|---|---|---|---|
| 1 | "One [kind of] company just / *announced [PRODUCT]*" | HA-12 | N1 |
| 2 | "[COMPANY] just / *changed [THING] forever*" | HA-12 | N1 |
| 3 | "Why would [COMPANY] / *build [PRODUCT]?*" | HA-12 | N1 |
| 4 | "This is the / *end of [OLD WAY]*" | HA-12 | N1 |
| 5 | "Your bank just / *changed this rule*" | HA-12 | N2 |
| 6 | "[REGULATOR] just / *made [PAYMENT] free*" | HA-12 | N2 |
| 7 | "Nobody read / *the fine print*" | HA-12 | N2 |
| 8 | "This prototype / *could replace [THING]*" | HA-12 | N1 |
| 9 | "The story behind / *[VIRAL MOMENT]*" (own post + clip) | HA-18 | N1 |
| 10 | "*Who owns* / your data?" | HA-12 | N1 / N2 |

## App. B Evidence map
See `evidence.md` (templates only): every DNA rule traced to `vNN @ m:ss`, the `(unverified)` list and the known gaps.
