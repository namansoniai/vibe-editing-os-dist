# Conversation Clip Style Playbook (template v1)

**Purpose:** you (Claude) receive a recorded conversation and turn it into a vertical clip in which **the conversation itself is the content**. A red quote pill states the question on frame 0, centre captions carry every spoken word in the speaker's colour, and hard cuts follow who talks and who reacts. Nothing else is added.

**Input** (SW-01): **F-A** `multi_speaker`: two people on camera (an audience question at a talk, a client call, a podcast or interview moment), 2+ cameras or one wide shot, plus the room audio or one mic per person. **F-B** `talking_head`: {{BV-01.name|the creator}} alone, answering one question (a comment, a DM, a client question), plus optionally their own screenshot of the question or their own screen.

**Output:** F-A 90–150 s, F-B 45–90 s, 1080×1920, 30 fps, captions on every word.

### Style DNA `[DNA]`
A Conversation Clip reads in one glance as **two real people talking, cut tight**: the opener is a 50/50 vertical stack (host on top, the asker below, seam at y 960) with a **red rounded caps pill** carrying the question; the pill vanishes in 0 f the moment the question sentence ends (3.8–11.6 s), on a cut or mid-shot. From then on the picture is only footage and **one line of centre captions**: 1–4 words at a time, Montserrat 500 at 68 px, **white upright for the host, yellow italic for the other voice**, one bold word for the number or the key noun. Cuts land on the first word of each new speaker, the listener's face appears for 1–3 s while the other talks, a long turn switches to a second camera on the same speaker (front ↔ side or full-body wide; a ×1.25 re-crop when there is only one camera), and the stack comes back for 10–20 s whenever both faces matter. There are no B-roll inserts, no stickers, no lower-thirds, no logos, no zoom animations, no transitions and no sound effects (measured at 30 fps: every cut, caption swap and pill change is 0 f). **Restraint is the signature.**

**Copy these 5 things and it reads as this style:**
1. **The stack opener under the red quote pill**: host top, asker bottom, seam y 960, pill y 672–880, the pill held until the question sentence ends (§3.2 SHOT-STACK, §5.2, §6.2 HA-03).
2. **Centre word-group captions**: 1–4 words, one line, hard swaps, Montserrat 500 68 px at y 960 (full) / on the seam (stack), one bold word (§5.3 CS-1).
3. **Two voices, two colours**: host white upright, the other voice yellow `#F2DF1A` italic; the colour follows the voice, never the face on screen (§5.3 speakers, §20).
4. **The cut grammar**: cut on handover (±3 f), listener cutaways 1–3 s, same-speaker angle switch (×1.25 re-crop fallback), stack returns ≈ 30–35% of runtime, 12–18 cuts per minute (§9.3 R-…, §20).
5. **Style by absence**: the pill and the captions are the only graphics in F-A; F-B adds only the bottom-cell question card / board / the creator's screen (§2.4, §8.1).

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The question is the hook.** The viewer knows what is being asked within 1.0 s, from the pill alone, with the sound off. | §5.2, §6.2, H1–H2 |
| D2 | **Captions are the second picture.** Every spoken word is captioned, centre-screen, one line, in the speaker's colour. They are the strongest element after the faces. | §5.3, H3–H4 |
| D3 | **Two voices, two colours.** The viewer never has to work out who is talking. | §5.3, §20, H4 |
| D4 | **Follow the conversation.** Cut on the speaker change, show the listener, return to the stack when both faces matter. | §9.3, §20, H5–H8 |
| D5 | **Nothing that isn't in the room.** No B-roll, stickers, emoji graphics, logos, lower-thirds, zoom animations, transitions or SFX hits. | §2.4, §8.1, H9 |
| D6 | **Never sit still.** A caption change at least every 2.5 s, a cut at least every 10 s (stack 20 s), 12–18 cuts per minute. | §7.6, H6 |
| D7 | **Mine the moment, never rewrite it.** One self-contained question → answer arc; sentences never reordered; quotes verbatim. | §1 P0, H13, NC-13 |
| D8 | **Let the answer land.** The verdict gets a stack return or a punch caption, then the clip ends on the "thank you" within 6 f. | §7.5, §6.7 |

Buyer directives **BD1…** `[VAR]` are added below this table by the buyer and may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches) | ON |
| §1 | Procedure (P0 clip mining → P13 build) | ON |
| §2 | Hard rules H1–H19, NEVER N1–N14, exception E6 | ON |
| §3 | Worlds, layouts and shot types, stage moves, safe zones, presenter rules | ON |
| §4 | Colour (red pill, white host, yellow guest) | ON (themes OFF, grades OFF) |
| §5 | Type: pill, caption profiles CS-1/CS-2/CS-3, speaker styles, quotes, language | ON |
| §6 | Hook: HA-03 quote pill over the stack (F-A), HA-05 pill + question card (F-B), alternates, pill writing, CTA | ON |
| §7 | Structure (`conversation`), turn ritual, re-hooks, cadence | ON |
| §8 | Visual system: 31 patterns (cut, caption, pill, insert) | ON (comedy layer OFF by default) |
| §9 | Transitions (hard cut only) and shot grammar R-SPK…R-END | ON |
| §10 | Motion, crop-on-cut camera, layers, finishing | ON |
| §11 | Sound contract | ON |
| §12 | Footage, shot list SH-1…SH-5, fallbacks FB-1…FB-5, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (2 × F-A, 1 × F-B) | ON |
| §15 | QA | ON |
| §16 Chrome · §17 State · §18 Data · §19 Citations | — | OFF |
| §20 Dialogue | — | **ON** |
| §21 Canvas camera · §22 Ink · §23 Continuity · §24 Series · §25 Brand/end cards | — | OFF |
| Parts C–F, App. A (headline bank), App. B (evidence) | — | ON |

**Formats:** **F-A "Two-person Q&A"** (default) and **F-B "Solo answer"**. One format per reel, declared in the reel header (§13.3).

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile (F-A values; F-B overrides below)
  source_type: multi_speaker
  presenter: {presence: anchor, share: [80, 100], max_absence_s: 4}
  spine: talking_head
  captions: {mode: full, role: primary, mute_policy: mute_safe}
  graphics: minimal
  duration: {class: long, target_s: [90, 150]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0, style: short}
  tone: {energy: balanced, comedy: off, comedy_max: light}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A, F-B], default: F-A}
  footage_dependency: high
  cta: {devices: [none, post_only, comment_keyword, link_bio], placement: end, chosen: none}
  modules: {chrome: false, running_state: false, anchors: false, data_figures: false, citations: false,
            dialogue: true, canvas_camera: false, ink: false, continuity: false, series: false, brand: false}
formats:
  F-A: {}                        # the profile above
  F-B:                           # "Solo answer"
    source_type: talking_head
    presenter: {presence: anchor, share: [90, 100], max_absence_s: 2.5}
    footage_dependency: low           # the screenshot / screen is optional (FB-5 creates the card)
    duration: {class: standard, target_s: [45, 90]}
    modules: {dialogue: false}
```

Why each switch has this value:
- **source_type: multi_speaker** (F-A), because all three reference clips are live two-person Q&A cut from 3+ camera angles (v01, v02, v03). F-B is `talking_head` because the solo variant has one person (STYLE-COVERAGE row 2).
- **presenter: anchor, 80–100%**, because a face is on screen ~95% of the runtime; the rest is wide room shots where faces are under 6% of frame height (v01 @ 0:37–0:38, v03 @ 0:21–0:26). Longest wide 4 s → `max_absence_s: 4`.
- **spine: talking_head**: the conversation audio is the timeline; pictures are chosen per word (who talks).
- **captions: full / primary / mute_safe**: captions are on screen ~97% of the runtime and are the only text after the pill (v01–v03 every sheet).
- **graphics: minimal**: two recurring devices (the pill, the captions); 0% B-roll in 410 s of evidence.
- **duration: long (90–150 s)** for F-A, because the clips run 112.9 / 150.8 / 146.9 s. F-B is `standard` (45–90 s): one question answered alone has no clarifying exchange.
- **language: en verbatim**, because the burned-in captions match English speech word for word, including "gonna", "cus'", "uhm..". Hinglish and Hindi are buyer options (§5.5).
- **numbers: international, $, short** ("$44M", "$70K a year", "20% to 25%": v01 @ 0:07, v03 @ 0:55, 2:11). Indian buyers switch to `indian / ₹ / lakh_crore` through BV-06.
- **tone: balanced, comedy off (max light)**: no comedy layer; one caption joke ("*alex approves*", v01 @ 0:15) in 410 s is the most this style allows (§8.6).
- **themes: single**: one look; nothing changes colour per reel.
- **formats: F-A + F-B**: the two variants share the pill, the captions and the cut rhythm (STYLE-COVERAGE row 2).
- **footage_dependency: high** (F-A: 2+ camera angles define the look); F-B `low` (just the creator talking; their screenshot or screen is optional because FB-5 creates the question card or the board).
- **cta: none by default**: none of the reference clips has a CTA; they end on "thank you!" (v01 @ 1:52, v02 @ 2:30). The buyer may choose `post_only`, `comment_keyword` or `link_bio` (§6.7).
- **modules: dialogue** only (the cast, cut grammar and speaker colours, §20).

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

This style's craft step is **the turn map** (P3c + P9b): who speaks when, who is worth watching while they do, and which camera shows it.

### F-A "Two-person Q&A"
1. **P0 Mine the clip.** If the recording is longer than 3 min, run `veos shots mine --min 90 --max 150` and pick **one** arc: question → (clarifying exchange) → reframe → advice → verdict → thanks.
   - It starts on the asker's first word (their name, business or situation) or on the host restating the question.
   - It ends on the last "thank you" / verdict word, plus ≤ 6 f.
   - You may drop whole sentences that are off-topic or repeated (≥ 3 s each), false starts, and dead air. You never reorder sentences, never splice two half-sentences into one, and never drop a sentence whose absence changes what someone said (NC-13).
2. **P1 Inventory.** `veos ingest` every camera and mic file; `veos conform`; `veos sync` (2+ files; check every source's `confidence` ≥ 0.5). Register any F-A prop shots (a flip chart) as normal angles.
3. **P2 Prepare.** No matte: multi-speaker reels have no cut-out layer and no `behind` scenes.
4. **P3 Transcribe.** `veos transcribe --id MIX`. Then:
   - **P3b Diarise:** `veos speakers --num 2 --names "S1=<host name>:host,S2=<asker name>:guest"` (`--mode mics` when each person has their own mic). SPK-1 needs ≥ 95% of words labelled; fix the rest by hand in `veos speakers name` before going on.
   - **P3c Angle map:** `veos angles`. Check that `preferred.speakers` gives a host single, a guest single and (if filmed) a wide. With one camera, the angles are faux crops `<src>:S1`, `<src>:S2`, `<src>:W` (FB-1).
5. **P4 Rough cut.** Write the EDL on `MIX` (P0's spans), then `veos cut <edl.json>`. Pauses: tighten to ≤ 0.4 s, except one deliberate thinking pause per minute (≤ 1.2 s) that sits on a listener reaction (P-23).
6. **P5 Segment** into conversation units (§7.1): **Q** question setup, **C** clarifying exchange, **R** reframe, **A** advice, **V** verdict, **T** thanks.
7. **P6 Classify** every sentence with a line type (§8.4) and mark its **bold word** (the number, the niche noun or the key verb). Mark voiced quotes ("and then you're like '…'") and back-channels ("yeah", "mmh", "okay").
8. **P7 Tone-tag** every sentence: `explain` · `warn` · `win` · `cta` (§10, §11).
9. **P8 Hook plan.** Write **3 pills** (§6.5): the asker's question, the host's verdict, and a tighter question. Run the stopper tests (§6.1) and pick one. Decide the opener length (2.7–4.4 s) and which cut drops the pill.
10. **P9 Cut plan.** `veos shots plan --apply`, then edit `plan/shots.json` by the shot grammar (§9.3): the stack opener, handover cuts, listener cutaways, jump re-crops, stack returns, wides, set-pieces. Mark the re-hooks (§7.4).
11. **P9b Cut grammar pass.** `veos shots check` until V-SPEAKER passes (SPK-1…SPK-6). Then write the caption overrides (§5.3): punch lines (CS-2), the defined word (CS-3), voiced quotes, profanity, spelling.
12. **P10 Sound.** The minimal contract (§11): normally zero SFX cues; the bed under everything at −26 dB.
13. **P11 Assets.** `veos shots render` (blurfill fallback for wides that can't crop). Third-party moments: the ask-then-create flow (§12.5); in F-A they are rare (a product name is just a caption).
14. **P12 Checkpoint** (§13.5), then **wait for approval.**
15. **P13 Build.** `prep-frames` → `bundle` → `veos validate` → preview → QA (§15, at most 3 passes) → render.

### F-B "Solo answer" (replaces P0, P3b–c, P9–P9b)
1. **P1 Inventory.** `veos ingest` the take, plus the creator's screenshot of the question (`veos asset add <file> --origin creator`) and any screen recording they reference.
2. **P3 Transcribe** (no diarisation). Find the words where {{BV-01.name|the creator}} **reads the question aloud**; those words are captioned as the asker (`captions.overrides {i: [...], speaker: "guest"}`, yellow italic).
3. **P4 Rough cut with re-crop splits.** Cut dead air (≤ 0.35 s pauses). Then **split the take at a word boundary every 2–4 s** (an EDL boundary with no time removed is allowed) so the cut rhythm reaches 10–18 cuts per minute; each boundary gets a jump re-crop (§10.2).
4. **P8 Layout plan.** Opener `L-solo-stack` (face top, question card bottom) for 2.7–4.4 s; then `L-full-solo` with re-crops; `L-solo-stack` again whenever {{BV-01.name|the creator}} points at something (the board, their screen, the question again): 25–50% of the runtime.
5. Everything else as F-A (P5–P8, P10–P13).

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| E-id | Limits in this style | DNA reason | Evidence |
|---|---|---|---|
| **E6 Hard swap** | Caption chunks swap content in 0 f inside a fixed band (cy 960 full / the seam in stack, ±4 px). The band's first entry and final exit stay eased (4 f fade at reel start only if no word is on f0; 6 f out at the end). Never used for a new element appearing. | Hormozi captions change on the word with no tween; a fade would smear 1-word groups at ~1 group/s. | v01 @ 0:00–0:03 (6 fps hook sheet: "I sell" → "the most effective" with no in-between frame), v02, v03 hook sheets |

No other exception. Behind-subject text (E1), chaos bursts (E2), quiet type (E3), ambient fields (E4) and edge bleed (E5) are **not** used: captions stay at 68 px, nothing goes behind a head.

### 2.3 Style MUST rules
- **H1 Frame 0.** F-A: the pill is fully drawn on frame 0 over a stack showing two faces (host top, asker bottom). F-B: the pill over `L-solo-stack` (the creator's face top, the question card bottom). No entrance animation on the pill; live footage is moving. `check: V-F0`
- **H2 Pill limits.** ≤ 6 words, ≤ 2 lines, ALL CAPS, red `primary` boxes with white text, readable in ≤ 1.2 s; curly quotes only around verbatim spoken words; on screen from 0.0 s, held ≥ 2.7 s (across the first cut when that cut comes before the question ends), removed in 0 f on the word boundary where the question sentence ends (on a cut frame if one falls within 3 f, else mid-shot), and never past 12 s. Measured: v01 out at 3.83 s mid-shot (16 f before the first cut), v02 4.73 s mid-shot (0.73 s after the first cut), v03 11.53 s (2 f before a cut). `check: V-TITLE`
- **H3 Every word captioned.** Captions show every spoken word (fillers included, §5.5), 1–4 words per chunk, one line, ≤ 24 characters, chunk on screen ≥ 0.25 s per word, shown ≤ 1 f before the first word and never cut before the last word ends. `check: V-CAPTION`
- **H4 Speaker colours.** Host: `paper` white, upright. Asker / any other voice: `accent` yellow, italic. A chunk never mixes speakers; the colour follows who is speaking, not who is on screen (v02 @ 2:30 "thank you!" in yellow on the host's shot). `check: V-SPEAKER` (SPK-2) + `V-CAPTION`
- **H5 Cut on handover.** Every new speaker's first word has a cut within ±3 f when either side of it is a full shot. `check: V-SPEAKER` (SPK-3)
- **H6 Cadence.** 12–18 cuts per minute (F-B 10–18), median shot 1.8–3.2 s (F-B 2.0–4.0), weighted state changes 7–18 per 10 s, ≥ 3 in 0–3 s, no gap without a caption change or cut longer than 2.5 s; full shots normally ≤ 6 s, at most one full shot of 6–10 s per 30 s (a monologue on a gesturing host, v01 @ 1:15–1:26), never > 10 s; stack shots 8–20 s mid-reel (measured 12.1–23.7 s). `check: V-CADENCE` + `V-SPEAKER` (SPK-6)
- **H7 Stack share.** F-A: the stack opener lasts 2.7–4.4 s; stacks fill 25–45% of the runtime; a stack always shows the host on top (engine fallback in §20.6). `check: review` (`stats` of `veos shots plan`)
- **H8 Listener cutaways.** 1.0–3 s (measured 1.17–3.0 s; a 1.2 s cutaway is the reaction to a number, v01 @ 0:15.4), never in the first 1 s of a turn or the last 1 s before a handover, never spanning a handover. `check: V-SPEAKER` (SPK-4)
- **H9 Graphics budget.** F-A: only the pill (and the CTA pill when chosen). F-B: the pill, plus one bottom-cell insert at a time (question card, board or the creator's screen). Nothing else, ever. `check: review` (G2 counts)
- **H10 Face rule.** No pill, caption or insert covers a face box. The pill's top edge sits ≥ 40 px below the chin of the face in its cell; captions avoid faces (`avoid_face`). `check: V-FACE`
- **H11 Dead air.** At most 1 pause ≥ 400 ms per 15 s, except one deliberate thinking pause per minute (≤ 1.2 s) shown on a listener reaction. `check: review` (`veos cut` gap report)
- **H12 Presence.** A face ≥ 6% of frame height on screen ≥ 80% of the runtime (F-B 90%); a wide or any faceless span ≤ 4 s (F-B 2.5 s). `check: V-PRESENCE`
- **H13 Verbatim.** Captions are the words as spoken (glossary spellings fixed, profanity masked); sentences are never reordered; every quoted pill or voiced quote is verbatim. `check: V-CAPTION` (spelling) + `review`
- **H14 Re-hooks.** F-A (long): a re-hook at least every 30 s after the hook (§7.4). F-B (standard): one re-hook in the middle 25–75%. Intro (hook) ≤ 15% of the runtime. `check: V-REHOOK`
- **H15 Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 18 dB under the voice (this style: 26 dB), hard end ≤ 6 f after the last word. `check: NC-8` (`veos mix`, `veos qa`)
- **H16 Crop on cut only.** Framing changes only on a cut: another camera on the same person, or a ×1.25 re-crop when there is one camera; never an animated push, punch or shake. Measured: no keyframed zoom in 410 s (the first and last frames of 10–24 s shots match in scale within 1%, v01 @ 0:17.9/0:28.2 ORB 1.000; the only in-shot movement is the live camera operator's slow pan). `check: V-CAMERA`
- **H17 CTA.** If the buyer chose `comment_keyword`, the keyword is spoken in the clip and shown in the CTA pill ≥ 1.5 s. If it was never spoken, the CTA goes in the post text (`post_only`). `check: V-PROMISE`
- **H18 Numbers.** Spoken numbers are captioned as digits in the style's format ("$44M", "20% to 25%", "5 locations"; Indian: "₹1.2 Cr"). `check: V-NUMFMT`
- **H19 Inserts.** F-B question cards and screens are the creator's own files or created substitutes recorded in `plan/inserts.json`. `check: V-INSERTS`
- **Determinism (NC-9):** every scene is a pure function of the frame. `check: review` (scene code)

### 2.4 NEVER
- **N1** No B-roll, stock footage, GIFs, memes, emoji graphics, stickers, logo bugs, lower-thirds, name plates or progress bars. (A single emoji inside a caption, as spoken text, is allowed ≤ 1 per reel: v03 @ 0:02.7 "perfect ✨".)
- **N2** No transitions of any kind (no whip, flash, zoom-blur, slide, fade between shots). Hard cuts only.
- **N3** No animated zooms, punch-ins, shakes, rotation snaps or Ken Burns on footage. The only "zoom" is a crop change on a cut.
- **N4** No caption animation: no pop, bounce, karaoke, typewriter, word-by-word colour fill, scale or blur. Chunks hard-swap.
- **N5** No coloured caption words besides the speaker colour. Emphasis is weight (800), never a third colour, never a box behind the word.
- **N6** No pill after 12 s except the CTA pill; never two pills at once; never a pill with an emoji, a logo or a brand colour other than `primary`.
- **N7** No reordering of sentences, no splicing of two half-sentences, no caption text that wasn't said.
- **N8** No sound effects on cuts, captions or the pill; no meme sounds; no music louder than −26 dB under the voice.
- **N9** No grade, LUT, vignette, grain, glow or blur added to footage (source vignettes are kept as they are).
- **N10** No hairline, gap, border or drop shadow on the stack seam.
- **N11** Never a stack with two shots of the same person, and never the same framing cut to itself (use a ×1.25 re-crop or another angle).
- **N12** No F-B insert that decorates: the bottom cell shows only what the creator is talking about at that moment (the question, the board, their screen).
- **N13** No fake comments, fake DMs or invented usernames. A created question card shows the question exactly as spoken.
- **N14** Captions never in the top 110 px, below y 1500, or in the right 110 px between y 900 and 1540.

Buyer additions **BN1…** `[VAR]` go below this list.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-room** | footage | The room as filmed: stage LED wall, floor mic, audience, studio. Not regraded | Everything in F-A; the full and top cells in F-B | Always under the footage |
| **W-void** | void | `#0E0E10`, noise 0.03 | F-B bottom cell behind the question card or a screen recording | Hard cut with the stage change |
| **W-board** | paper | `#F4F4F1` flip-chart white, noise 0.02, drawn as a **card** (radius 28) filling the insert rect x 80–960, y 1030–1500; the cell ground stays `W-void` so the seam caption always sits on dark | The board (P-28) | Rises 10 f with the board |

### 3.2 Layouts and shot types
F-A reels keep the **stage at `L-full-dialogue`** (engine `full`) for the whole reel: the engine composes the shots (`timeline.shots`) into the footage itself. The shot types below are written as `timeline.shots` entries.

| ID | Engine / shot fields | What | Rects | Share of runtime |
|---|---|---|---|---|
| **SHOT-STACK** | `{"layout": "stack", "seam_y": 960, "top": "source:<host angle>", "bottom": "source:<guest angle>", "top_subject": host, "bottom_subject": guest, "hairline": 0}` | Host top, asker bottom, no gap, no line | top 0–960, bottom 960–1920; face 0.30 of the cell, eye line at 0.42 of the cell (y 403 / y 1363) | F-A 25–45% (target 35%) |
| **SHOT-HOST** | `{"layout": "full", "angle": "<host single>", "subject": host, "step": 1.0}` | Host single, medium to medium close-up | full frame; head top y 140–320; face 17% of frame height | F-A 25–35% |
| **SHOT-GUEST** | `{"layout": "full", "angle": "<guest single>", "subject": guest, "step": 1.0}` | Asker single at the mic or across the table | as above | F-A 18–30% |
| **SHOT-ALT** | `{"layout": "full", "angle": "<second angle of the same person>", "cut_reason": "recrop"}` | The same speaker from another camera: front medium ↔ side (podium) medium-wide ↔ full-body wide from the crowd (v01 @ 0:51.3, v02 @ 0:16.2, 1:09.3) | full frame | 2–4 per reel, inside the host rows |
| **SHOT-RECROP** | same angle, `"step": 1.25`, `"cut_reason": "recrop"` | Fallback for SHOT-ALT when the person has one camera: ×1.25 tighter (or back to 1.0) | as above, ×1.25 | inside the two rows above |
| **SHOT-WIDE** | `{"layout": "full", "angle": "<src>:W" or the room camera, "cut_reason": "establish"}` | Room / crowd wide from behind the audience: the host small on stage, **or the asker standing in the crowd while she speaks** (v01 @ 0:36.8–0:46.4, yellow captions) | full frame (blurfill when a 16:9 wide can't fill 9:16) | F-A 5–12%, each ≤ 4 s (two wides back-to-back ≤ 6 s) |
| **L-full-dialogue** | stage, engine `full` | The stage layout of every F-A reel | full frame; captions cy 960 | F-A 100% (stage) |
| **L-full-solo** | stage, engine `full` | F-B: the creator full-frame, jump re-crops on cuts | full frame; captions cy 960 | F-B 50–75% |
| **L-solo-stack** | stage, engine `stack`, `top: {src: footage, face: 0.30, eye: 0.42}`, `bottom: graphic` | F-B: face top, insert bottom | top 0–960; graphic band x 80–960, y 1030–1500; caption on the seam | F-B 25–50% |

**Layout schedule rule (F-A).** The shot changes on: a new speaker's first word (always), a sentence end inside a long turn, or the bold word of an emphatic run. Full shots hold 0.8–6 s (one 6–10 s shot per 30 s allowed); the opener stack 2.7–4.4 s; mid-reel stacks 8–20 s held as **one** shot with no internal re-crop (measured 12.1 / 23.7 s v01, 14.4 / 13.2 / 16.5 s v02, 12.5 / 9.7 s v03). The picture cut lands on a caption-chunk boundary: the new chunk appears on the cut frame (v01 @ 4.367, 54.067).

**Layout schedule rule (F-B).** `L-solo-stack` ≥ 2.7 s and ≤ 14 s per run; `L-full-solo` 1.5–6 s per shot; switch on a sentence end or on the word that names the thing in the bottom cell ("this", "look", the item's name).

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Hard cut | 0 f. Shot or stage changes on the frame of the word onset − 1 f (`lead_f` 1) | Every boundary in this style |
| **G-2** | Angle switch / jump re-crop | F-A: a hard cut to another camera on the same speaker (SHOT-ALT); with one camera, same angle step 1.0 ↔ 1.25 (shot `step`). F-B: camera preset `recrop-in` / `recrop-out` written 1 f before the cut | Long turns, F-B rhythm |
| **G-3** | Pill carry | The pill scene runs unchanged (same rect, same text) across any cuts inside the question sentence and is removed in 0 f where the sentence ends, cut or no cut | The hook (P-03) |
| **G-4** | Stack return | Hard cut from a full shot into SHOT-STACK (F-A) or `L-solo-stack` (`via: "cut"`, F-B) | Long turns, the verdict, a set-piece |

No slide-down, morph, pip, panel drop, shrink-to-card or fade: write `"via": "cut"` on every F-B stage entry (the engine default into `stack` is `slide-down`).

### 3.4 Layout diagrams
**SHOT-STACK with the pill (the F-A opener):**
```
┌──────────────────────────┐ 0
│  (IG top UI, keep clear) │ ← y 0–110
│        HOST (top)        │ ← host face, eye line y ≈ 403
│      listening or        │
│        answering         │
│ ╭──────────────────────╮ │ ← pill line 1, top y 672
│ │ “SHOULD I SELL MY     │ │   x 120–960 (centred, per-line boxes)
│ ╰─╮ COMPANY?”        ╭─╯ │ ← pill line 2, bottom ≤ y 880
│   ╰──────────────────╯   │
│    I sell  (yellow ital) │ ← caption centred ON the seam, y 960
├──────────────────────────┤ 960 seam: no line, no gap
│       ASKER (bottom)     │ ← asker face, eye line y ≈ 1363
│        at the mic        │
│                          │ ← y 1540–1920 IG UI (faces may sit here, text may not)
└──────────────────────────┘ 1920
```

**SHOT-HOST / SHOT-GUEST (full):**
```
┌──────────────────────────┐ 0
│                          │ ← head top y 140–320
│          FACE            │
│                          │
│     (pill y 672–880      │ ← only while the pill is carried (≤ 12 s)
│      if carried)         │
│    you're playing too    │ ← caption cy 960, one line, max_w 860 (x 110–970)
│        **small**         │   (shown here on two lines only to fit the diagram)
│          chest           │
│                          │
└──────────────────────────┘
```

**L-solo-stack (F-B):**
```
┌──────────────────────────┐ 0
│      THE CREATOR (top)   │ ← face 0.30 of the cell, eye y ≈ 403
│ ╭──────────────────────╮ │ ← pill y 672–880 (opener only)
│ ╰──────────────────────╯ │
│     how do I ask for     │ ← caption on the seam y 960
├──────────────────────────┤ 960
│ ╭──────────────────────╮ │ ← insert rect x 80–960, y 1030–1500
│ │ QUESTION CARD / BOARD │ │
│ │ / THE CREATOR'S SCREEN│ │
│ ╰──────────────────────╯ │
│          W-void          │ ← y 1500–1920 world only (IG UI)
└──────────────────────────┘
```

### 3.5 Safe zones and bands
- **Meaning-text box:** x 64–1016, y 110–1500 (NC-5). The right 110 px between y 900 and 1540 stays empty of text, so captions use `max_w` 860 (x 110–970).
- **Pill band:** top y 672, bottom ≤ 880, x 120–960 (max width 840). The pill's top moves down to chin + 40 px when a face in its cell reaches lower than y 632; if that pushes the bottom below 880, drop the pill on this cut instead of carrying it.
- **Caption band:** full shots centre y 960 (glyph box ≈ y 920–1000; measured centres 955–989 in v01 @0:20, @0:50, v02 @0:10, @1:20, v03 @0:20); stack shots centre on the seam y 960 (≈ 920–1000). `avoid_face` moves a caption to the chest when a close-up face would sit under it.
- **F-B insert band:** x 80–960, y 1030–1500 (≥ 70 px below the seam caption, inside NC-5).
- **CTA pill band:** the same as the hook pill (y 672–880).

### 3.6 Presenter rules
- **Share:** a face is visible ≥ 80% (F-A) / 90% (F-B) of the runtime; any faceless span (a wide where faces are under 6% of the frame height) lasts ≤ 4 s (F-B 2.5 s).
- **Who is "the presenter":** the host (the buyer). The asker counts for presence too (any face).
- **Return:** always by hard cut, on a word onset.
- **Crops:** full shots head top y 140–320 (face 17% of the frame height); stack cells face 0.30, eye 0.42 of the cell; F-B top cell the same. Crops follow the subject with a dead zone (engine `reframe`), never a visible drift faster than 60 px/s.
- **Behind the head:** nothing (no matte, no E1).

---

## §4 Colour `[REQ] [meanings DNA; brandable hex VAR/TUNE]`

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` | `{{BV-02.primary|#E80001}}` | The pill fill (hook pill, CTA pill). Nothing else | `paper` | 4.87:1 (pill text is 68 px display: needs 3:1) | yes (VAR) |
| `accent` | `{{BV-02.accent|#F2DF1A}}` | The second voice: the asker's captions; the asker's question text on the F-B card | `ink` (15.5:1) | on footage via the caption shadow halo | yes (TUNE: a light saturated hue, never white) |
| `paper` | `#FFFFFF` | Host captions, pill text | `ink` | — | no (DNA) |
| `ink` | `#0B0B0B` | Caption shadows, board marker | `paper` | — | no |
| `board` | `#F4F4F1` | F-B board paper | `ink` (17.9:1) | — | no (TUNE) |
| `void` | `#0E0E10` | F-B bottom-cell ground | `paper` (19.6:1) | — | no (TUNE) |

### 4.2 Meanings
- **Red = "this is the question (or the verdict)".** It exists only in the pill. A red caption, red underline or red card is never used.
- **White = the host. Yellow italic = the other voice.** This axis replaces every bad/good axis: the style has no bad/good colours.
- The footage carries all other colour (LED walls, shirts, rooms). Brand colours appear only if they are in the room.

### 4.3 Theme packs
OFF (`themes.policy = single`): one look for every reel.

### 4.4 Grades
OFF: footage is used as filmed. Match exposure and white balance between cameras in `conform` only; never add a grade, LUT, vignette or bloom (source vignettes are kept, as at v01 @ 0:54).

### 4.5 Rules
- **≤ 2 bright hues per frame** (`max_bright_per_frame: 2`): red (pill) + yellow (guest caption), and only during the hook.
- Captions carry exactly one colour per chunk: the speaker's.
- If the buyer's `accent` is dark or near-white, `veos templates copy` nudges it; a guest colour within ΔE 15 of white is refused (SPK-2 needs two distinct styles).

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map
| Slot | Family | Weight | Font class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `display` | **Montserrat** | 800 | geometric sans 800–900 caps | The pill, the CTA pill |
| `body` | **Montserrat** (+ Montserrat Italic file) | 600 / 800 bold / 600 italic | geometric sans 600–800 with a true italic | Every caption |
| `marker` | **Permanent Marker** | 400 | felt-tip marker hand | F-B board words only |
| `ui` | **Montserrat** | 500–700 | geometric sans 500–700 | F-B question card |

Devanagari captions (the `hi` option) use **Noto Sans Devanagari** 600/800 (no italic exists: see §5.5).

### 5.2 Headline element: the quote pill `[DNA recipe; NICHE text]`
| Property | Spec |
|---|---|
| Kind / lifetime | `pill`, lifetime `hook` (scene `kind: "pill"`) |
| Shape | **One red box per line** (`box_per_line`), centred, lines touching so the two boxes read as one stepped shape; radius 16; padding 8 px top/bottom, 22 px left/right; fill `primary`; no stroke; shadow `0 4 10 rgba(0,0,0,.25)`; rotation 0 |
| Text | Montserrat 800, **68 px** (TUNE 64–80), ALL CAPS, tracking 0, line height 1.0 (line box 84 px), `paper` white, centred |
| Size | 2 lines (1 line only when ≤ 3 words); ≤ 6 words; ≤ 18 characters per line; width ≤ 840 px; total height ≈ 168 px |
| Position | Centred at x 540; top y 672 (v01: y 659–825, v03: y 666–882 measured); bottom ≤ 880; ≥ 40 px clear of the caption below and of any chin above |
| Quotes | Curly quotes `“ ”` when the pill is the asker's question in their own words (v02, v03). No quotes when it is the host's verdict (v01) |
| f0 | **Fully drawn on frame 0.** `in: "none"`; no scale, no fade, no shadow grow |
| Life | None. No pulse, flip, colour change or wobble. It just sits there while the footage moves |
| Exit | **Hard, 0 f** (verified frame by frame): `t_out` = the end of the question sentence's last word (snap to a shot boundary if one is within 3 f), `out: "none"`, `cuts: [t_out - t_in]` declared. ≥ 2.7 s, never past 12 s. Measured: v01 out at f115 = 3.83 s mid-shot, v02 f142 = 4.73 s mid-shot (after the 4.0 s cut), v03 f346 = 11.53 s, 2 f before a cut |
| Text class | `TC-display`; `text_content` = the pill text exactly |
| Scene | `z: 10`, `roles: ["primary"]`, `box` = the measured pill rect, `may_overlap_face: false`, F-A openers on a shots stack add `satisfies: ["two_faces"]` (§20.6) |

### 5.3 Caption system profiles `[DNA mechanics; fonts TUNE; language VAR]`
**CS-1 "Conversation" (default; `extends: lib:hormozi`):**
| Group | Value |
|---|---|
| Mode | `full`, role `primary`, `mute_safe` |
| Chunking | `group`, 1–4 words (mean ≈ 2.4), ≤ 24 characters, 1 line; never split a name, a number or a unit ("$44M", "4-year retention"); break on punctuation, on a pause ≥ 0.9 s and on a speaker change; end punctuation stripped except `?` and `!` (v01 "$44M?", v02 "is that appealing", "to you?") |
| Timing | Lead 1 f; ≥ 0.25 s per word; tail 0.12 s; a chunk is held through a pause of ≤ 0.6 s (`pause_hold_s`), then hidden; swap **hard, 0 f** (E6) |
| Skin | Montserrat **500, 68 px** (measured: "okay so you're doing" 66 px tall asc→desc, 681 px wide = Montserrat ≈ 67 px at −1 % tracking, v01 @0:50; "medium-skilled labor" 57 px ascender height, v03 @0:20), tracking −1 %, `TC-subtitle`, case as spoken (lowercase except "I", names, acronyms: "I sell", "salon in LA"), tracking 0, no stroke, no container; shadow `0 2 3 rgba(0,0,0,.85), 0 0 12 rgba(0,0,0,.35)` |
| Position | `fixed_y` cy **960**, cx 540, `max_w` 860, centred, `avoid_face: true`; on the seam (cy 960) in every stack shot and in `L-solo-stack` |
| Speakers | **host** `paper` upright · **guest** `accent` italic · **quote** `paper` italic (§5.3.2) |
| Emphasis | `bold` (800), 1 word per chunk at most, ≤ 0.6 per second; selected from numbers, names, glossary terms, the topic noun and the key verb, never a stop-word; ≈ 40% of chunks carry one (v01 @ 0:21 "to the **greatest**", 0:57 "you're playing too **small**", v03 @ 2:14 "all the **best talent**": a 2-word span counts as one emphasis when it is one idea) |
| Variants | none (no karaoke, tiers, duet or stack) |
| Hide | never hidden while someone speaks (the pill sits above the caption, not on it) |
| Language | Latin script; English terms kept as spoken; spelling not normalised ("gonna", "wanna", "cus'"); profanity masked `inner` (`f**k`; the evidence used a vowel mask, v02 @ 1:41); glossary = the buyer's names and terms |

**CS-2 "Punch line"** (`captions.overrides {t: [a, b], profile: "CS-2"}`): the same skin at **84 px, weight 800**, 1–3 words, ≥ 0.3 s per word. For the one line per 30 s that *is* the answer ("you're gonna / **work again**", v02 @ 0:26–0:27). Budget: ≤ 1 per 30 s, never two in a row, never in the hook.

**CS-3 "The word"** (`{t: [a, b], profile: "CS-3"}`): one word, **120 px, weight 800**, `TC-display`, ≥ 0.5 s. Only when the host names the single concept the whole answer turns on, usually while writing it ("**role**", v03 @ 1:06). Budget: ≤ 1 per reel.

#### 5.3.1 Speaker styles
| Speaker key | Colour | Style | Who |
|---|---|---|---|
| `host` | `paper` #FFFFFF | upright | {{BV-01.name|the creator}} (the one answering) |
| `guest` | `accent` {{BV-02.accent|#F2DF1A}} | italic (500; bold words 800 italic) — sampled `#F0DE18` (v01 @0:01–0:20, v02 @0:10) | The asker in F-A; the question when read aloud in F-B |
| `quote` | `paper` #FFFFFF | italic | The host voicing himself or a third person ("“learn all this shit”", v01 @ 1:31; "“great!”", v01 @ 1:23) |

#### 5.3.2 Quotes and voiced lines (decided recipe)
- **The host voices the asker** ("and then you're like 'I can't do this forever'"): the quoted words take the **guest** style, in curly quotes: `{i: [first..last], speaker: "guest"}` + `{i: first, text: "“I"}` + `{i: last, text: "forever”"}` (v02 @ 0:33–0:35 "“I can't do this” / “forever” / “be an alcoholic”" in yellow italic).
- **The host voices himself, a client or "people"**: the **quote** style (white italic) in curly quotes (v01 @ 1:23–1:25 "“great!” / “total capacity?” / “can you get me?”").
- **The asker voices someone**: stays guest (yellow italic) with curly quotes (v01 @ 0:44 "“oh that's **terrible**”").
- A quoted span is its own chunk (cards never mix speakers), and its words are verbatim.

#### 5.3.3 Other caption conventions
- **Cut-off words** end with a hyphen and the chunk holds through the restart: "where you're-" (v01 @ 1:44–1:45), "I think that if we-" (v02 @ 2:19).
- **Back-channels** ("yeah", "mmh", "okay", "nope", "uhm..") are captioned in the listener's style, as their own chunk, while their reaction shot is up (v02 @ 0:23 "yeah yeah", 2:28 "mmh", 2:29 "okay").
- **Trailing thought** "like.." / "so.." uses two dots (v02 @ 1:24 "like..", v03 @ 0:14 "so..").
- **Emoji:** ≤ 1 per reel, only as the speaker's tone on a one-word reaction ("perfect ✨", v03 @ 0:02.7). Never in the pill.
- **Action captions** ("*alex approves*", "*boop*"): only with `comedy: light` (§8.6).

### 5.4 Other text systems
| Element | Class | Recipe | Hold |
|---|---|---|---|
| **CTA pill** (P-04) | TC-display | The pill recipe, 1–2 lines, e.g. `COMMENT “{{BV-08.keyword|KEYWORD}}”`; enters with a 6 f fade (not on a cut), exits on the last frame | 1.5–3.0 s |
| **F-B question card** (P-25) | TC-label + TC-legal | Created: `fx.quoteCard` restyled: rounded card radius 28, fill `#1A1A1D`, x 80–960 inside y 1030–1500; name line Montserrat 700 40 px `paper` ("A follower asked" or the name the creator gives); the question Montserrat 600 italic 52 px in `accent`, ≤ 3 lines Creator's screenshot: `fx.shot` with `chrome: false`, fitted to the insert rect | the stack run |
| **F-B board** (P-28) | TC-label (TC-display for the title) | A `board`-coloured card (radius 28) in the insert rect on the `W-void` cell; Permanent Marker `ink`, title 96–120 px, items 64–96 px, left-aligned at x 120; each word writes on L → R over 10 f on its spoken word; a 6 px marker tick/underline draws in 6 f on the item being discussed | the stack run |
| **Credit / label** | TC-legal | Montserrat 500 24 px, `#9A9AA0`, inside the insert rect bottom-left | with its insert |

### 5.5 Language and number rules
- **Speech → captions** (BV-05; one combination per reel):
  - `en → en` (default): verbatim.
  - `hinglish → hinglish (Latn)`: verbatim romanised Hinglish; English words in standard spelling; Hindi words phonetic and consistent within a reel ("kya", "nahi", "matlab").
  - `hinglish → en`: translated per chunk, still 1–4 words, still split by speaker; quotes translated faithfully and still in curly quotes.
  - `hi → hi (Deva)`: Noto Sans Devanagari 600, 68 px. **Devanagari has no italic**, so the guest style becomes **yellow, weight 700, upright**; SPK-2 still passes on colour. ALL CAPS does not exist in Devanagari: the pill stays in English or Latin Hinglish caps unless the buyer asks for a Devanagari pill (then 64 px, weight 800, no quotes rule change).
- **Numbers:** digits, never words ("5 locations", "30 days", "$70K a year", "20% to 25%", "6 to 12"); currency glyph pre-painted; international grouping, k/M/B compact (`$4M to $44M`); with BV-06 Indian: `₹` + lakh/crore ("₹40 lakh", "₹1.2 Cr").
- **Spelling:** names and brands exact (glossary); everything else as spoken.
- **Fillers:** "uhm..", "like", "you know" stay when they are spoken on a kept span; whole filler-only stretches longer than 0.4 s are cut in P4.

---

## §6 Hook system `[REQ]`

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| ID | Test | This style's number |
|---|---|---|
| ST-1 | Thumbnail: frame 0 at 25% scale shows "two people, one question" | The pill text is 17 px at 25% and stays legible; both faces visible (F-A) / face + card (F-B) |
| ST-2 | Mute: the first 3 s tell what is being asked without sound | The pill + the first 3 caption chunks carry the question |
| ST-3 | Motion at f0 | Live footage is moving on f0 (people never freeze) |
| ST-4 | Read time | The pill reads in ≤ 1.2 s (≤ 6 words) |
| ST-5 | Change count | ≥ 3 weighted state changes in 0–3 s (caption chunks count 1.0; frame 0 excluded) |
| ST-6 | Payoff-by | The question is understood by 1.0 s (the pill); the answer starts by 60 s |

### 6.2 Default archetype: HA-03 "Quote pill over the conversation" (F-A) `[DNA]`
The hook is **"who is asking what"**. There is no spoken hook line: the asker starts setting up their question, the pill already says what it is, and the viewer stays to hear the answer.

| t (s) | Layout / shot | Pill | Captions | Cut | Cue (SFX pack) |
|---|---|---|---|---|---|
| **f0** | SHOT-STACK: host top (listening, ¾ toward the asker), asker bottom at the mic | **Fully drawn**, y 672–840, e.g. `“SHOULD I SELL MY / COMPANY?”` | The asker's first chunk on the seam in yellow italic, if a word starts by 0.03 s ("I sell") | — | none (dry) |
| 0.0–1.0 | same | same | Asker chunk 1–2, ≈ 1 chunk per 0.7–1.2 s ("I sell" → "performance upgrades") | none | none |
| 1.0–2.7 | same | same | Context chunks; **bold** on the niche noun and the first number ("**$5M** in revenue") | none | none |
| **2.7–4.4** | **First cut** (`open_s`): to SHOT-GUEST if the asker keeps talking, or to SHOT-HOST on the host's first interjection | **Carried** unchanged (P-03) if the question is still being asked | continues (host words white) | 1 cut | none |
| 3.8–12 | Handover cuts and listener cutaways while the question finishes | **Gone in 0 f at the end of the question sentence**, on a cut or mid-shot; never past 12 s | continues | 0–5 cuts | none |
| 10–40 | The host's first clarifying question ("what do you actually want?") on SHOT-HOST, handover cut | — | white | — | none |
| ≤ 60 | The answer starts (reframe or verdict) | — | — | — | — |

Evidence (30 fps bursts): v01 stack 0.00–4.37 s, pill out at 3.83 s while the stack is still up, first caption on f4 (0.13 s), swaps at 0.97 / ≈ 2.1 / ≈ 3.2 s; v02 stack 0.00–4.0 s, pill carried across the cut to 4.73 s; v03 stack 0.00–2.67 s, pill carried across five cuts to 11.53 s. Pill on f0–f3 is identical (no pop, no fade).

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`
**HA-03b Verdict pill (F-A).** Same table; the pill is the host's verdict in his words, **no quotes** ("YOU NEED TO MAKE / BIGGER BETS", v01). Use it when the answer is the hook (a surprising verdict) and the question is ordinary.

| t (s) | What |
|---|---|
| f0 | Stack + verdict pill + the asker's first chunk |
| 0–4.4 | The asker sets up; the viewer reads the verdict and waits for the "why" |
| verdict line | When the host says the pill's words, that chunk is CS-2 (punch) on SHOT-HOST |

Examples `[NICHE: example]`: business coaching "RAISE YOUR PRICES FIRST"; fitness "STOP TRAINING TO FAILURE".

**HA-14 Cold answer (F-A).** Use it when the kept clip opens with the host already talking (the question was asked off-mic, or the host restates it).

| t (s) | What |
|---|---|
| f0 | SHOT-STACK with the host on top **speaking** (white chunk on the seam) + the question pill (quoted only if verbatim) |
| 0–2.7 | The host restates the question in his words; the asker's face is the reaction |
| 2.7–4.4 | First cut to SHOT-HOST; pill carried |
| ≤ 12 | Pill removed; the answer continues |

Examples `[NICHE: example]`: "So your question is, do you hire a manager now?" (business); "You're asking if cardio kills gains." (fitness).

**HA-05 Pill + question card (F-B default).**

| t (s) | Layout | Pill | Captions | Cut |
|---|---|---|---|---|
| f0 | `L-solo-stack`: the creator top (eye y 403), the question card bottom (y 1030–1500) already up | **Fully drawn**, the question in quotes | If the creator reads the question: yellow italic on the seam | — |
| 0.0–2.7 | same; P-30 underlines the phrase of the card being read (6 f) | same | yellow italic while reading, white when answering | none |
| 2.7–4.4 | Hard cut to `L-full-solo` (re-crop 1.0) on the creator's first answer word | Carried | white | 1 |
| 4.4–8 | Jump re-crops every 2–4 s | Removed on the first cut after the question is read, never past 12 s | white | 1–2 |

Examples `[NICHE: example]`: career coaching `“HOW DO I ASK / FOR A RAISE?”`; skincare `“IS RETINOL SAFE / EVERY NIGHT?”`.

### 6.4 Hook pairs by topic: question → answer `[NICHE]`
Write the pair at P7 of every reel and append it here in the buyer's copy.

| Niche | Topic | Question (pill, as asked) | Where the answer lands | How it's shown |
|---|---|---|---|---|
| Business coaching `[NICHE: example]` | Pricing | “SHOULD I RAISE MY PRICES?” | The host's verdict at 25–45 s ("charge double, lose half") | CS-2 punch on SHOT-HOST, then a stack return for the asker's reaction |
| Business coaching `[NICHE: example]` | Hiring | “MANAGER OR ONE MORE CLEANER?” | 40–70 s, after the host asks "what's your margin?" | Handover cuts; bold on the margin number |
| Business coaching `[NICHE: example]` | Selling the company | “SHOULD I SELL MY COMPANY?” | 60–120 s (reframe: "what would you gain?") | Long stack return on the reframe |
| Business coaching `[NICHE: example]` | Retention | “WHY DO MY EMPLOYEES LEAVE?” | 50–90 s, set-piece on a board | P-21 set-piece, CS-3 on the key word |
| Business coaching `[NICHE: example]` | Burnout | “I WORK 80 HOURS. NOW WHAT?” | 30–60 s | Listener cutaways on the asker's nods |
| Fitness / health `[NICHE: example]` | Fat loss | “WHY AM I NOT LOSING WEIGHT?” | The host's clarifying question ("what do you eat at night?") at 15–25 s; verdict 40–60 s | Clarifying exchange in handover cuts |
| Fitness / health `[NICHE: example]` | Training split | “HOW MANY DAYS SHOULD I TRAIN?” | 30–50 s | CS-2 punch on the number ("**3 days**") |
| Fitness / health `[NICHE: example]` | Supplements | “DO I NEED CREATINE?” | 20–40 s | Verdict pill variant when the answer is a flat yes/no |
| Fitness / health `[NICHE: example]` | Motivation | “HOW DO I STAY CONSISTENT?” | 45–80 s | Stack return so the asker's reaction carries the payoff |
| Fitness / health `[NICHE: example]` | Injury | “SHOULD I TRAIN THROUGH PAIN?” | 15–30 s (warn) | SHOT-HOST + jump re-crop on the warning word |

### 6.5 Pill writing `[DNA formula; NICHE text]`
**Question pill formula:** the asker's question as a **verbatim contiguous span** of the transcript, ≤ 6 words, ALL CAPS, curly quotes, ending in "?". You may drop only leading or trailing fillers and articles ("so", "like", "a", "the", "um"). If the asker never says the question in ≤ 6 contiguous words, write it in your own words **without quotes**: it is then the reel's title, not a quote (NC-13).

**Verdict pill formula:** the host's verdict as spoken, ≤ 6 words, ALL CAPS, no quotes, imperative or declarative ("YOU NEED TO MAKE BIGGER BETS").

| Template | Example |
|---|---|
| Should I … ? | “SHOULD I SELL MY COMPANY?” |
| Why do/does … ? | “WHY DO MY EMPLOYEES LEAVE?” |
| How do I … ? | “HOW DO I ASK FOR A RAISE?” |
| X or Y? | “MANAGER OR ONE MORE CLEANER?” |
| Is it … ? | “IS RETINOL SAFE EVERY NIGHT?” |
| Verdict | YOU NEED TO MAKE BIGGER BETS |

- **Line break:** after the 2nd–4th word, so line 1 holds the verb phrase and is the longer or equal line (v01 "YOU NEED TO MAKE / BIGGER BETS", v02 "“SHOULD I SELL MY / COMPANY?”", v03 "“WHY DO MY / EMPLOYEES LEAVE?”").
- **Write 3, pick by the stopper tests** (§13.4).
- **Banned:** words that weren't said in a quoted pill; hype ("INSANE", "MUST WATCH"); emoji; numbers that weren't spoken; the asker's full name or company name unless the creator confirms they may be named.

### 6.6 Hook sound
Dry: no SFX cue in the hook. The music bed (when on) runs from f0 at −26 dB under the voice (§11).

### 6.7 CTA `[DNA device set; VAR values]`
| Device | Spoken pattern | On screen | Hold | Where | Silence before |
|---|---|---|---|---|---|
| `none` (default) | — | Nothing: the clip ends on the last "thank you" / verdict word + ≤ 6 f (v01 @ 1:52, v02 @ 2:30) | — | end | — |
| `post_only` | — | Nothing on screen; the CTA lives in the post text | — | — | — |
| `comment_keyword` | {{BV-01.name|the creator}} says "comment {{BV-08.keyword|KEYWORD}}" **in the recording** | The CTA pill (P-04) `COMMENT “{{BV-08.keyword|KEYWORD}}”` at y 672 on SHOT-HOST / `L-full-solo`, 6 f fade in on the word "comment" | 1.5–3.0 s | end (after the verdict, before "thank you") | No SFX in the 1.0 s before |
| `link_bio` | "link in my bio" spoken | CTA pill `LINK IN BIO` | 1.5–3.0 s | end | No SFX in the 1.0 s before |

If the chosen device was never spoken, fall back to `post_only` and say so at the checkpoint. Never add a CTA voice-over, an end card or a follow button.

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type: `conversation`
| Unit | What | F-A typical span | F-B typical span |
|---|---|---|---|
| **Q** Question setup | The asker: who they are, their numbers, the question (the pill already says it) | 0–15 s | 0–6 s (the creator reads the question) |
| **C** Clarifying exchange | The host asks 1–3 short questions; the asker answers in a few words | 10–45 s | — (or one rhetorical question) |
| **R** Reframe | The host names what the question is really about | 30–70 s | 6–20 s |
| **A** Advice | The concrete what-to-do (steps, a number, a board) | 50–130 s | 15–60 s |
| **V** Verdict | The one line that answers the pill | last 10–20 s | last 5–10 s |
| **T** Thanks | "thank you!" from either side; the clip ends | ≤ 2 s | — (ends on the verdict) |

### 7.2 Markers
`markers: none (spoken only)`. Steps the host counts out loud ("first… second…") stay spoken; no numerals, chips or progress bars appear. The only on-screen structure devices are the CS-2 punch line and, in F-B, the board items.

### 7.3 Unit ritual: the turn ritual (identical for every turn)
1. **Handover cut** to the new speaker's single (SHOT-HOST / SHOT-GUEST) on their first word − 1 f.
2. **Hold the speaker** 1.5–6 s while their first sentence lands.
3. If the turn runs past 4 s: a **listener cutaway** (1–3 s) at a sentence boundary **or** an **angle switch** to the speaker's other camera (×1.25 re-crop with one camera). Alternate the two; never two re-crops in a row on one angle.
4. If the turn runs past 10 s: a **stack return** (host top, asker bottom) held 8–20 s, then back to a single. A 6–10 s single on a gesturing host is the alternative (≤ 1 per 30 s).
5. **Back-channels** ("yeah", "mmh") inside the turn: a ≤ 1.6 s cut to the listener only when the reaction is visible (a laugh, a nod); otherwise caption it on the current shot.
6. The next handover starts the ritual again.

### 7.4 Open loops and re-hooks
- **The loop** is the pill's question. The verdict (V) must answer that exact question.
- **Re-hooks (F-A, long):** at least one every **30 s** after the hook (`rehook_every_s: 30`), marked `rehook: true` on the beat. A re-hook is one of:
  - **RH-1** the host's clarifying question on a handover cut ("do you have kids? are you married?", v02 @ 0:36–0:38);
  - **RH-2** a stack return on the reframe line, so the asker's reaction is visible;
  - **RH-3** a CS-2 punch line;
  - **RH-4** the set-piece start (the host goes to the board, P-21);
  - **RH-5** the "here's what I'd do" turn ("so this is me…", v01 @ 0:51).
- **Re-hook (F-B, standard):** one in the middle 25–75%: the stack return to the board or the question card ("so back to your question…").
- **Intro cap:** the HOOK section (stack opener + pill) ≤ 15% of the runtime (4.4 s of a 90 s reel is 5%).

### 7.5 Rhythm and energy curve
- **Q:** fast caption swaps, slow cuts (the opener holds 2.7–4.4 s).
- **C:** the fastest cutting of the reel (a handover every 1–3 s; v02 @ 0:36–0:44 cuts about every 1 s).
- **R / A:** long host turns broken by cutaways, re-crops and stack returns; one CS-2 punch per 30 s at most.
- **V:** slow down. The verdict line on SHOT-HOST or a stack return, then **one** reaction of the asker (≤ 2 s), then "thank you" and the hard end.
- No comedy beats are planned (comedy off). Laughter in the room is kept and shown on a reaction (P-23).

### 7.6 Cadence (state changes)
| Token | F-A | F-B | Evidence |
|---|---|---|---|
| `sc_per_10s` | 7–18 (caption chunks weigh 1.0) | 7–18 | ≈ 1 chunk/s + 2–3 cuts per 10 s (all sheets) |
| `hook_sc_3s` | ≥ 3 | ≥ 3 | v01 3 swaps, v02 3, v03 3 + 1 cut in 0–3 s |
| `max_gap_s` | 2.5 | 2.5 | longest single-chunk hold ≈ 2 s (v02 @ 1:00–1:01) |
| `max_static_s` | 2.5 (live footage always counts as motion) | 2.5 | — |
| `cuts_per_min` | **12–18 (DNA)** | 10–18 | 13.8 / 17.5 / 15.9 |
| `median_shot_s` | 1.8–3.2 | 2.0–4.0 | 2.2 / 2.0 / 2.9 |
| max full shot | 10 s (≤ 1 shot of 6–10 s per 30 s) | 6 s | full shots > 6 s: v01 @ 0:17.8 (10.5 s), 0:29.5 (7.3 s), 1:15 (10.8 s); v02 @ 0:43.9 (8.6 s); v03 @ 2:10 (8.2 s) |
| max stack shot | 20 s (mid-reel stacks 8–20 s) | 14 s | v01 12.1 / 23.7 s; v02 14.4 / 13.2 / 16.5 s; v03 12.5 / 9.7 s |
| shot length (all, 30 fps scene detection) | median 2.3 s, p75 4.2 s, p90 6.7 s | — | 113 cuts in 410 s; shots > 6 s fill 37% of the runtime (mostly stacks) |

---

## §8 Visual system: graphics, cuts and patterns `[REQ]`

### 8.1 Graphics role and budget
- `graphics: minimal`. **F-A:** one recurring graphic (the pill, ≤ 12 s) plus the captions; graphics beyond captions fill ≤ 10% of the runtime (the pill ≈ 3–8%, the CTA pill ≤ 3 s). **F-B:** the pill plus one bottom-cell insert during `L-solo-stack` runs (≤ 50% of the runtime).
- **Numbers do not become pictures.** In this style a number becomes a **bold caption word** ("**$44M**"), and that is all: no counters, charts, bars or hero numbers.
- **The pattern library is mostly cut grammar:** 31 patterns: 4 pill, 9 caption, 11 cut and 7 F-B layout/insert patterns.

### 8.2 Families
| ID | Family | Source class | The buyer supplies |
|---|---|---|---|
| **B-1** | Camera shots (singles, stack, wide, re-crops) | buyer-owned | F-A: 2+ cameras or one 4K wide; F-B: one camera |
| **B-2** | Caption devices (CS-1/2/3, speaker styles, quotes) | engine | — |
| **B-3** | The pill (hook, CTA) | engine | — |
| **B-4** | F-B bottom-cell inserts (question card, board, screen) | creator-supplied (their own screenshot or screen recording), else an engine-created substitute (`fx.quoteCard`, the board scene) | optional: the screenshot of the question, their screen recording |

### 8.3 Pattern specs (30 fps)
**Pill patterns (B-3)**

| ID | Pattern | Type | What's on screen | Motion (frames) | When | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-01** | Question pill | overlay | The asker's question, verbatim, curly quotes, 2 lines, red per-line boxes | Present from f0; no entrance; removed in 0 f at the end of the question sentence (cut or mid-shot) | HA-03 / HA-05 default | TC-display | `kind: "pill"`, `cuts` at t_out |
| **P-02** | Verdict pill | overlay | The host's verdict as spoken, no quotes | as P-01 | HA-03b | TC-display | as P-01 |
| **P-03** | Pill carry | overlay | The same pill, unchanged, across 1–5 picture cuts | Rect constant (0 px drift) across cuts | Every hook: it rides any cuts inside the question sentence and goes where the sentence ends (3.8–11.6 s measured, ≤ 12 s) | TC-display | — |
| **P-04** | CTA pill | overlay | `COMMENT “KEYWORD”` / `LINK IN BIO` in the pill recipe | Fade in 6 f on the spoken word; out on the last frame | Only with a spoken CTA (§6.7) | TC-display | `kind: "cta-keyword"` |

**Caption patterns (B-2)**

| ID | Pattern | Type | What | Motion | When | Text class |
|---|---|---|---|---|---|---|
| **P-05** | Host caption | overlay | White upright 600, 1–4 words, cy 960 / the seam | Hard swap 0 f, lead 1 f | Every host word | TC-subtitle |
| **P-06** | Asker caption | overlay | Yellow italic 600 | as P-05 | Every asker word (F-B: the question read aloud) | TC-subtitle |
| **P-07** | Bold word | overlay | One word (or one 2-word idea) at 800 inside the chunk | none (weight only) | Numbers, the niche noun, the key verb; ≈ 40% of chunks | TC-subtitle |
| **P-08** | Punch line (CS-2) | overlay | 1–3 words at 84 px, 800 | Hard swap | The answer in one line; ≤ 1 per 30 s | TC-subtitle |
| **P-09** | The word (CS-3) | overlay | One word at 120 px, 800 | Hard swap, ≥ 15 f hold | The single concept the answer turns on; ≤ 1 per reel | TC-display |
| **P-10** | Voiced quote | overlay | A curly-quoted span, italic, in the voiced person's style (§5.3.2) | Hard swap | "and you're like '…'" | TC-subtitle |
| **P-11** | Action caption | overlay | A `*stage direction*` in white upright | Hard swap, 0.8–1.5 s | **Only with `comedy: light`**, ≤ 2 per reel, never in the hook, the verdict or the CTA | TC-subtitle |
| **P-12** | Cut-off hold | overlay | "where you're-" held through the restart pause | Hold ≤ 0.6 s past the word | A self-interruption | TC-subtitle |
| **P-13** | Back-channel caption | overlay | "yeah", "mmh", "okay", "nope" in the listener's style | Own chunk | On the listener's reaction shot, or on the current shot when the reaction isn't visible | TC-subtitle |

**Cut patterns (B-1, F-A)**

| ID | Pattern | Type | What | Recipe (shots) | When |
|---|---|---|---|---|---|
| **P-14** | Stack open | cut | SHOT-STACK host top / asker bottom | 2.7–4.4 s from f0, ends on a word onset | Every F-A reel |
| **P-15** | Stack return | cut | SHOT-STACK mid-reel | 8–20 s per shot, held as one shot (no in-stack re-crop) | Turns > 10 s, the reframe, the verdict |
| **P-16** | Handover cut | cut | The new speaker's single | On the first word − 1 f (±3 f) | Every speaker change on a full shot |
| **P-17** | Listener cutaway | cut | The listener's single while the other talks (`cut_reason: "reaction"`) | 1.0–3.0 s; starts ≥ 1 s into the turn, ends ≥ 1 s before the handover | Turns > 4 s; reactions worth seeing (nod, smile, frown) |
| **P-18** | Angle switch | cut | The same speaker on another camera (SHOT-ALT); fallback same angle step 1.0 → 1.25 (or back) | On a word onset at a sentence end; 2–4 per reel | Long host turns instead of a repeat (v01 @ 0:51.3 front → podium; v02 @ 0:16.2, 1:09.3 → full-body wide) |
| **P-19** | Wide establish | cut | The room / crowd from behind the audience: the host small on stage, or the asker in the crowd while she speaks | 1–4 s; two in a row ≤ 6 s; blurfill if the wide can't crop | Before the answer starts; when the host walks; as the asker's second angle mid-question (v01 @ 0:36.8–0:46.4) |
| **P-20** | Back-channel cut | cut | ≤ 1.6 s on the listener's "yeah" / laugh | Only when the reaction is visible | Inside long turns |
| **P-21** | Set-piece | cut | The host at a board or flip chart: full on the board while he writes, then a stack (board top, asker bottom) while he explains | Full 2–6 s per writing burst; stack 4–14 s | When the host draws or writes (v03 @ 1:03–1:42) |
| **P-22** | Walk follow | cut | The host walking: the medium-wide crop follows with a dead zone | Follow ≤ 60 px/s; cut when he stops | The host moves on stage (v02 @ 1:27–1:29) |
| **P-23** | Laugh hold | cut | The asker or the room laughing | Hold 1–2 s; never cut inside the laugh | A laugh after a host line (v02 @ 0:42–0:43) |
| **P-24** | Thank-you end | cut | The last "thank you!" on whoever says it | Hard end ≤ 6 f after the word | Every F-A reel (v01, v02) |

**F-B layout and insert patterns (B-1, B-4)**

| ID | Pattern | Type | What | Motion | When | Text class | Needs |
|---|---|---|---|---|---|---|---|
| **P-25** | Question card | overlay (insert) | The question in the bottom cell: the creator's screenshot (`fx.shot`) or a created card (`fx.quoteCard`, verbatim) | Present at f0 (opener), or rise 10 f + de-blur on a stack return; it leaves with the stage cut | The opener; "so back to your question" | TC-label + TC-legal | inserts record |
| **P-26** | Solo stack open | stage | `L-solo-stack` + P-25 + the pill | 2.7–4.4 s from f0, out by `via: "cut"` | Every F-B reel | — | — |
| **P-27** | Solo re-crop | camera | `recrop-in` / `recrop-out` on an EDL cut | 1 f, written 1 f before the cut | Every F-B cut that isn't a stage change | — | split EDL |
| **P-28** | Board | overlay (insert) | A `board` card in the insert rect (the cell stays `W-void`); ≤ 4 marker words written L → R on their spoken word; title 96–120 px, items 64–96 px | Write-on 10 f each; tick/underline 6 f on the item being discussed | The creator lists 2–4 things, a formula or a ladder | TC-display / TC-label | — |
| **P-29** | Screen cell | overlay (insert) | The creator's own screen recording or slide in the insert rect (`fx.shot`, `chrome: false`) | Rise 10 f; plays at 1× | "Look at this": a dashboard or document the creator owns | — | creator asset |
| **P-30** | Card highlight | annotation | A 6 px `accent` underline under the phrase of the question card being read | Draws L → R in 6 f on the phrase's first word | The opener; the stack return to the question | — | — |
| **P-31** | Full return | stage | Hard cut from `L-solo-stack` to `L-full-solo` at re-crop 1.0 | 0 f | The first answer word after the opener; the verdict | — | — |

### 8.4 Line → pattern lookup `[NICHE]`
| Line type | Example `[NICHE: example]` (business / fitness) | Primary | Alternates |
|---|---|---|---|
| Question setup (who I am) | "I run a cleaning company, 6 people" / "I'm 34, I train 4 days a week" | P-14 + P-06 + P-07 (bold the niche noun) | P-25 (F-B) |
| Context number | "we did $40K last month" / "I lost 2 kilos in 3 months" | P-06 / P-05 + P-07 on the number | P-17 (the host's reaction to the number) |
| The question itself | "should I hire a manager?" / "why am I not losing weight?" | P-01 already says it; keep the shot | P-30 (F-B) |
| Clarifying question (host) | "what's your margin?" / "what do you eat after 9?" | P-16 handover + re-hook RH-1 | P-15 |
| Short answer (asker) | "about 30%" / "nope" | P-16 to SHOT-GUEST, P-07 on the number | P-13 on the host's shot if < 1 s |
| Back-channel | "yeah", "mmh", "okay" | P-13 | P-20 |
| Reframe | "you don't have a hiring problem, you have a pricing problem" / "it's not the cardio, it's the snacking" | P-15 stack return + re-hook RH-2 | P-08 |
| Advice step | "first, raise prices 20%" / "eat protein first at every meal" | P-05 + P-07, P-18 re-crops | P-28 (F-B board item) |
| Hard truth (warn) | "you're playing too small" / "you're under-eating protein" | SHOT-HOST + P-18 on the bold word | P-08 |
| Voiced quote | "and they go 'great!'" / "you tell yourself 'just this once'" | P-10 | — |
| Demonstration | the host writes on a board / pulls up a screen | P-21 (F-A) | P-28, P-29 (F-B) |
| Laugh in the room | the asker laughs at a host line | P-23 | P-11 (only with comedy light) |
| Verdict | "that's what I would do" / "train 3 days, walk every day" | P-08 on SHOT-HOST, then one asker reaction | P-31 (F-B) |
| Thanks | "thank you!" | P-24 | — |
| Third-party mention (a book, an app, a person) | "read *Atomic Habits*" / "use a food-tracking app" | caption only (glossary spelling) | F-B: ask-then-create logo plate in the insert rect (§12.5) |

### 8.5 Data and truth rules
- No data figures (`data_figures` off). A spoken number appears once, as a caption word, in the style's number format (H18).
- Numbers shown are exactly the spoken numbers: never re-rounded, never added.
- Created cards (F-B) show only words that were spoken or that the creator supplies, with the (NC-6, NC-13).

### 8.6 Comedy layer
OFF by default (`tone.comedy: off`). The buyer may raise it to `light` (BV-11): then **P-11 action captions** are allowed (≤ 2 per reel, white upright, in asterisks, 0.8–1.5 s, on a reaction shot; never in the hook, the verdict or the CTA). Evidence: "*alex approves*" (v01 @ 0:15) and "*boop*" (v03 @ 1:31) in 410 s. No stickers, stamps, meme sounds or freeze-frames at any level: `roast` is not available in this style.

### 8.7 Asset rules
- Real footage only: the conversation as filmed. No stock, no AI scenes.
- F-B question cards: the creator's own screenshot first (blur the commenter's avatar and handle unless the creator confirms permission, NC-14); else a created generic card (no platform logo, no invented username: the name line reads "A follower asked").
- Third-party products, books, apps, people: caption only in F-A; in F-B, the ask-then-create flow (§12.5).

### 8.8 Density and variety
- An SC every 0.5–2.5 s (captions alone give ≈ 1 per second).
- Per 60 s (F-A): 12–18 cuts; ≥ 4 different cut patterns (P-14…P-24); ≥ 2 listener cutaways; ≥ 1 stack run; ≤ 2 CS-2 punch lines.
- The same cut pattern at most 3 times in a row (handover cuts in a fast exchange are the exception).

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Library
| ID | Transition | Frames | SFX role |
|---|---|---|---|
| **T-00** | Hard cut | 0 | none |

That is the whole library (evidence: 26 / 44 / 39 cuts, every one straight). F-B stage changes are written `"via": "cut"`.

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | The stack, the pill and the first caption already there | A fade-in, a black frame, a title card |
| Hook → body | The first cut at 2.7–4.4 s; the pill rides across it only if the question is still being asked, and leaves in 0 f where the question ends | Holding the pill after the question ends just to reach a cut |
| Any cut | Lands on a caption-chunk boundary: the new chunk appears on the cut frame (v01 @ 4.367, 54.067) | A chunk that swaps 1–5 f off the cut |
| Speaker change | T-00 on the new speaker's first word − 1 f | A cut inside a word; a cut more than 3 f late |
| Inside a long turn | T-00 to a listener cutaway, a re-crop or a stack return | Two re-crops in a row on one angle; a cut mid-word |
| Back to the speaker | T-00 | — |
| Into / out of the stack | T-00 | slide-down, morph, fade |
| Last word | Hard end ≤ 6 f after "thank you" / the verdict | A black tail > 0.2 s, an end card |

### 9.3 Shot grammar `[DNA]`
| ID | Rule | Numbers | Evidence |
|---|---|---|---|
| **R-SPK** | Cut on the first word of a new speaker when either side is a full shot | ±3 f (`handover_tol_f`), 1 f lead | v02 @ 0:36–0:37 ("be an alcoholic" → host full) |
| **R-OPEN** | Open on SHOT-STACK (host top, asker bottom) | 2.7–4.4 s (`open_s`) | 4.37 / 4.0 / 2.67 s |
| **R-HOLD** | Full shots ≤ 6 s (one 6–10 s per 30 s), stacks ≤ 20 s | `max_hold_s` 10, `stack_max_s` 20 | full 10.5 / 10.8 s (v01), stacks 12.1–23.7 s |
| **R-REACT** | Listener cutaway inside a turn | 1.0–3.0 s; ≥ 1 s after the turn starts, ≥ 1 s before the next handover | v01 @ 0:54–1:05, v02 @ 1:13–1:14, 1:20–1:21 |
| **R-JZ** | Same-speaker angle switch instead of a repeat; ×1.25 re-crop only when the person has one camera | 2–4 per reel, on a sentence end | v01 @ 0:51.3; v02 @ 0:16.2, 1:09.3 (v01 @ 0:14–0:18 is fast host/asker/wide alternation, not re-crops) |
| **R-WIDE** | Wide establish | 1–4 s (two in a row ≤ 6 s), ≤ 12% of runtime; before the answer, when the host walks, or as the asker's crowd angle | v01 @ 0:37–0:38, 1:08–1:09; v03 @ 0:21–0:26 |
| **R-STACK** | Stack return in turns > 10 s; host always on top; held as one shot 8–20 s | 25–45% of runtime (`stack_share` 0.35; measured 36 / 32 / ≈ 25%) | v01 1:27–1:51, v02 0:22–0:36, v03 1:10–1:30 |
| **R-BC** | A back-channel shows the listener only when the reaction is visible | ≤ 1.6 s (`backchannel_max_s`) | v02 @ 0:28–0:29 "yeah" on the stack |
| **R-SET** | Set-piece: full on the board while writing, stack (board top / asker bottom) while explaining | full 2–6 s, stack 4–14 s | v03 @ 1:03–1:42 |
| **R-LAUGH** | Never cut inside a laugh; hold the laugher 1–2 s | — | v02 @ 0:42–0:43 |
| **R-END** | The clip ends on "thank you" (or the verdict) + ≤ 6 f; no outro | — | v01 @ 1:52, v02 @ 2:30 |
| **R-MIN** | No shot shorter than 0.8 s (`min_shot_s`) | — | — |
| **R-SAME** | Never cut a framing to itself; never a stack of the same person twice | — | — |

### 9.4 Budget (per 60 s)
- Cuts: 12–18 (F-B 10–18). Stack runs: 1–3. Listener cutaways: 2–6. Re-crops: 2–8. Wides: 0–2.
- **The same cut pattern never 3 times in a row**, except handover cuts in a fast exchange.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Lead | Shot cuts and captions 1 f before the word onset |
| Caption swap | Hard, 0 f (E6). Verified at 30 fps: v01 f3 → f4 "I sell" appears full size, f28 → f29 next chunk; CS-2 "you're gonna" static f785–f795 (no pop, no scale, no fade) |
| Pill | No entrance (f0–f3 identical); hard 0 f exit where the question sentence ends (3.83 / 4.73 / 11.53 s) |
| CTA pill | Fade in 6 f, ease `cubic-bezier(0.22, 1, 0.36, 1)`; out on the last frame |
| F-B card rise | 10 f, 24 px rise + 8 → 0 px blur, ease out; exit with the stage cut |
| F-B board write-on | 10 f per word, L → R clip reveal; title 12 f |
| F-B tick / underline | 6 f, 6 px `ink` (board) or `accent` (card) |
| Cut / angle switch / re-crop | 0 f; no flash, blur, dip or whoosh at any of 113 measured cuts |
| End | Hard end on the last frame, no fade (v02 last 24 f on the host, "thank you!" held to f4524) |
| Hold | Captions ≥ 0.25 s per word; CS-3 ≥ 0.5 s; inserts ≥ 2.7 s |

### 10.2 Footage camera: `zoom_policy: crop_on_cut`
- **F-A:** no `camera` events at all. Re-crops are shots with `"step": 1.25` (`veos shots render` composes them; ≤ 2.0× upsampling, 1080p sources ≤ 1.35×).
- **F-B:** two presets only, each on a cut (V-CAMERA checks ±2 f):
  - `recrop-in`: scale 1.00 → 1.25 in 1 f. Write it **1 f before** the EDL cut so the new scale shows on the cut frame.
  - `recrop-out`: scale 1.25 → 1.00 in 1 f, same placement.
  - Alternate in → out → in. **After every stage change the camera resets to 1.0**, so the first re-crop after a stage change is always `recrop-in`.
- **Never:** snap-punch, crash-zoom, push-drift, shake, rotation (N3).

### 10.3 Canvas camera
OFF (§21).

### 10.4 Layer order (back to front)
1. Footage (composed shots in F-A; the stage in F-B)
2. F-B world in the graphic cell (`W-void`)
3. F-B insert (question card, board card, screen) at z 4
4. Captions (auto, z 7)
5. The pill / CTA pill (z 10)

### 10.5 Finishing
No grain, vignette, bloom, glow, LUT or blur is added. Cameras are matched for exposure and white balance only. Insert cards have a soft shadow `0 8 24 rgba(0,0,0,.35)` and radius 28; nothing else has a shadow except the captions' text shadow and the pill's faint shadow.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | `cta` only (one soft pop or click when the CTA pill appears, if a CTA is shown). Hook, cuts, captions, pill and inserts are silent |
| **Meme cues** | Off (comedy is never `roast`) |
| **Music bed** | On, from f0, a soft non-melodic bed at −26 dB under the voice `(unverified: not observable in the evidence)`; off when the room audio already carries ambience the creator wants heard |
| **Ducking** | The bed ≥ 18 dB (here 24–26 dB) under the voice while anyone speaks; the room tone and audience laughter are kept and ducked under the voice |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

Mirrored in `tokens.json → sound`.

---

## §12 Footage requirements, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA assumptions; VAR the buyer's actual setups]`
| ID | Setup | Framing | Notes |
|---|---|---|---|
| **A** | F-A live room: the host on a stage or a chair, the asker at a floor mic or across a table; 2–3 cameras (host single, asker single, room wide) | head top y 140–320 after the 9:16 crop | 1080p+; 4K on the host camera if you want ×1.25 re-crops on a 16:9 source; one mic per person, or one room mic |
| **B** | F-A single wide: one 4K camera sees both people | each faux crop head top y 160–340 | FB-1; both faces must be ≥ 120 px tall in the 4K source |
| **C** | F-B solo: one camera, chest-up, eye-line just off the lens as if answering someone | head top y 150–260 | plain or lived-in background; 4K preferred for re-crops |

### 12.2 Shot list `[DNA]`
| ID | Shot | Spec | Count per 60 s | Must / optional | Formats |
|---|---|---|---|---|---|
| **SH-1** | Host single | medium (waist-up) to medium close-up; optional second host camera (side, or full-body from the crowd) for SHOT-ALT | 6–10 shots | must (second angle optional) | F-A |
| **SH-2** | Asker single | medium close-up at the mic or across the table; catches the listening reactions | 4–8 shots | must | F-A |
| **SH-3** | Room wide / audience | from behind the crowd; the host visible on stage | 0–2 shots | optional | F-A |
| **SH-4** | Solo talking head | chest-up, 1080p minimum, 4K preferred | the whole take | must | F-B |
| **SH-5** | The question as received, or the creator's own screen / slide / whiteboard | screenshot or screen recording, any aspect | 0–3 | optional | F-B |

### 12.3 Fallbacks
| ID | For | What the engine does | Fidelity cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | Two faux crops of one wide (setup B): host crop + asker crop, 9:16 each, face 0.30 of a stack cell / 17% of the full frame (`dialogue.single_cam_fallback: two_crops`) | Softer image (needs 4K), no true eye-line, re-crops limited to ×1.25 | degraded |
| **FB-2** | SH-2 | The asker crop from the wide; if the asker is never visible, switch the reel to F-B (the question becomes a question card) | No dedicated listener reactions | degraded |
| **FB-3** | SH-3 | Skip WIDE; a jump re-crop ×1.25 → ×1.0 on the host replaces it | No sense of the room | holds |
| **FB-4** | SH-4 | none: F-B needs the creator on camera | — | no_fallback |
| **FB-5** | SH-5 | Claude builds the question card (`fx.quoteCard`, verbatim question, "A follower asked") or the board (P-28) from the spoken words | Not the real comment | holds |

### 12.4 Props, reaction bank, matte, resolution
- **Props:** F-A optional: a flip chart or whiteboard on stage for set-pieces (P-21). F-B: none.
- **Reaction bank:** the asker listening, nodding and laughing (free from SH-2); the host listening (arms crossed, hand on chin).
- **Matte:** none.
- **Minimum source resolution:** ×1.25 re-crops need ≥ 1080p in the 9:16 crop; FB-1 faux crops from a 16:9 wide need a 4K source (a 1080p wide gives ≤ 1.35× total).

### 12.5 Third-party inserts: ask, then create `[REQ always]`
1. Run `veos inserts scan`. In this style most moments are dismissed with "caption only" (F-A shows nothing but the room).
2. **F-B only:** for the question itself and for a product, app or document the creator names and points at, ask once: "For these N moments, do you have a screenshot or a screen recording? (drop the files, or say no)".
3. **Supplied:** `veos asset add <file> --origin creator`; show it with `fx.shot` in the insert rect; blur personal identifiers (NC-14).
4. **Not supplied:** the question → `fx.quoteCard` (quote = the question as spoken, name line "A follower asked"); a product or app → `fx.logoPlate` (name set in type); a document or app screen → `fx.appUI` (generic, labelled).
5. Record every insert in `plan/inserts.json` (`origin: creator | created`, `substitute_of`). V-INSERTS checks it.

### 12.6 Frame rate and audio
- 30 fps CFR (conform VFR phone footage); 1080×1920 output.
- F-A: `veos sync` the cameras and mics; the `MIX` source (gain-sharing automix of the mic tracks) is the voice. F-B: one voice track.
- Voice chain: high-pass 80 Hz, de-ess, light compression; −14 LUFS; true peak ≤ −1.5 dBTP.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section` (HOOK | Q | C | R | A | V | T | CTA), `t0`, `t1`, `spoken`, `trigger {word, at}` (the bold word), `tone` (explain | warn | win | cta), `line_type` (§8.4), `layout`, `visual` (one sentence), `layers` (scene ids), `pattern`, `sfx`.

### 13.2 Conditional fields used by this style
| Field | When | Content |
|---|---|---|
| `speaker`, `angle`, `crop`, `cut_reason` | F-A, every beat | `host` / `guest`; the angle id; `step 1.0 / 1.25`; `open` / `handover` / `reaction` / `recrop` / `stack` / `establish` |
| `caption {profile, overrides[], emphasis[]}` | every beat | CS-1 / CS-2 / CS-3; speaker and text overrides (§5.3.2); the forced bold word |
| `rehook: true` | the re-hook beats | §7.4 |
| `shot_id`, `fallback_used` | when a fallback is used | SH-…, FB-… |
| `insert {id, origin}` | F-B question card / screen / logo plate | §12.5 |
| `exception: "E6"` | not on beats (captions inherit E6 from the profile) | — |

### 13.3 Reel header (top of the edit brief)
```yaml
reel:
  format: F-A                     # F-A | F-B
  theme: null                     # single
  hook_archetype: HA-03           # HA-03 | HA-03b (verdict pill) | HA-14 | HA-05 (F-B)
  structure: conversation
  cast: {S1: {name: "<host>", role: host}, S2: {name: "<asker>", role: guest}}
  pill: "“SHOULD I SELL MY / COMPANY?”"
  pill_out_s: 5.2                 # the cut that removes it
  keyword: null                   # BV-08 keyword when the CTA is comment_keyword and it was spoken
  duration_s: 128
  rehooks: [18.4, 41.0, 66.2, 93.5]
```

### 13.4 Hook proposals (3 required)
```yaml
- name: "Question pill: sell or keep"
  archetype: HA-03
  pill: "“SHOULD I SELL MY / COMPANY?”"     # verbatim span: "should I sell my company" at 3.1 s
  hook_pair: {question: "should I sell my company?", answer_lands_s: 74, answer: "what would you gain from the sale?"}
  opener: {stack_s: [0, 4.0], first_cut: "4.0 host 'okay' -> SHOT-HOST", pill_out_s: 5.2}
  captions: ["I sell", "performance upgrades", "to", "german car owners"]   # guest, yellow italic
  stopper_test: {thumbnail: pass, mute: pass, read_s: 1.0, changes_3s: 3, payoff_s: 1.0}
- name: "Verdict pill"
  archetype: HA-03b
  pill: "WHAT WOULD YOU / GAIN?"            # the host's words at 74.2 s, no quotes
  hook_pair: {question: "should I sell my company?", answer_lands_s: 74}
  opener: {stack_s: [0, 4.0], pill_out_s: 5.2}
  stopper_test: {thumbnail: pass, mute: pass, read_s: 0.9, changes_3s: 3, payoff_s: 1.0}
- name: "Tight question"
  archetype: HA-03
  pill: "SELL OR KEEP / THE COMPANY?"       # not a verbatim span, so no quotes (§6.5)
  hook_pair: {question: "should I sell my company?", answer_lands_s: 74}
  opener: {stack_s: [0, 4.0], pill_out_s: 5.2}
  stopper_test: {thumbnail: pass, mute: pass, read_s: 1.0, changes_3s: 3, payoff_s: 1.0}
```

### 13.5 Checkpoint (send, then wait)
1. The 3 hook proposals with stopper-test results; the recommended one.
2. The clip-mining decision (F-A): the kept span, what was dropped and why (whole sentences only).
3. The cast and the angle map (which camera or faux crop shows whom); the fallbacks used (FB-…).
4. The shot plan summary: cuts per minute, median shot, stack share, the longest full and stack shots, `veos shots check` result.
5. The beat sheet with tones, the re-hooks and the caption overrides (CS-2 / CS-3 lines, quotes, masked words).
6. F-B: the inserts record (creator-supplied vs created) and the board words.
7. The sound line (bed on/off, CTA cue).
8. Style stills: f0, the first cut with the pill carried, one stack return, one listener cutaway, the verdict, the last frame.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE]`
Times are planning estimates; replace them with `words.edit.json` onsets. Speaker names are placeholders.

### 14.1 F-A, business coaching: a live workshop Q&A (two cameras + a room wide), 118 s
**Clip:** the asker runs a cleaning company and asks whether to hire a manager. **Archetype:** HA-03. **Pill:** `“SHOULD I HIRE / A MANAGER?”` (verbatim span at 6.9–8.1 s). **CTA:** none.

**Hook table**
| t (s) | Speaker: words | Shot | Pill | Captions | Notes |
|---|---|---|---|---|---|
| f0 | — | SHOT-STACK: host top (arms crossed, listening), asker bottom at the floor mic | drawn | — (first word at 0.12) | Thumbnail: two faces + the question |
| 0.12–1.30 | asker: "I run a cleaning company" | stack | on | "I run a" → "**cleaning** company" (yellow italic, on the seam y 960) | bold = niche noun |
| 1.40–3.20 | asker: "6 people, about $40K a month" | stack | on | "**6** people" → "about **$40K** a month" | numbers as digits |
| 3.30–3.80 | asker: "and I'm stuck" | stack | on | "and I'm stuck" | — |
| **3.80** | asker: "I'm doing every quote myself…" | **cut → SHOT-GUEST** (the end of the opener, R-OPEN; same speaker, so not a handover) | carried | yellow italic, cy 960 | first cut |
| 5.60 | host: "okay" (back-channel, not visible) | stays SHOT-GUEST | carried | "okay" in white, own chunk (P-13) | — |
| 6.90–8.10 | asker: "so should I hire a manager?" | SHOT-GUEST | carried | "so should I" → "hire a **manager**?" | the pill's words are spoken |
| **8.20** | host: "what's your margin?" | **handover cut → SHOT-HOST** | **removed on this cut** (8.2 s) | "what's your **margin**?" white | RH-1 clarifying question |

**Section plan**
| t (s) | Unit | Speaker / line | Shots (patterns) | Caption devices | Re-hook |
|---|---|---|---|---|---|
| 8.2–14.0 | C | host "what's your margin?" / asker "about 30%" / host "and who does the quotes?" / asker "me" | handover cuts every 1–2 s (P-16 ×4) | P-07 on "**30%**"; "me" yellow | 8.2 RH-1 |
| 14.0–26.0 | R | host: "you don't have a hiring problem, you have a you problem…" | SHOT-HOST 3.1 s → P-18 re-crop ×1.25 on "**you** problem" → P-17 asker cutaway 2.2 s (she laughs: P-23 hold 1.4 s) → SHOT-HOST | CS-2 punch "a **you** problem" (≤ 1 per 30 s) | 14.0 RH-2 |
| 26.0–40.0 | R | host keeps going (14 s turn) | P-15 stack return 9.5 s (host top speaking, asker bottom nodding) → SHOT-HOST | P-10 voiced quote: "and the client goes “where's my quote?”" in white italic (quote style) | 26.0 RH-2 |
| 40.0–52.0 | A | host: "so this is me: I'd hire someone to do the quotes first" | SHOT-HOST → P-18 → P-19 wide 1.6 s as he walks to the front → SHOT-HOST | bold on "**quotes**" | 40.0 RH-5 |
| 52.0–66.0 | A | host: "pay them per closed quote, not per hour" | SHOT-HOST 4 s → P-17 asker 2.0 s → SHOT-HOST ×1.25 | CS-2 "per **closed quote**" at 58.4 (29 s after the last CS-2) | — |
| 66.0–78.0 | A | asker: "but what if they're worse at it than me?" / host: "they will be. For 30 days." | handover cuts (P-16 ×2); asker in SHOT-GUEST, host in SHOT-HOST | "they will be" white; "for **30 days**" | 66.0 RH-1 |
| 78.0–96.0 | A | host explains the 30-day handover, counts 3 steps out loud | P-15 stack return 18 s, held as one shot → SHOT-HOST | steps stay spoken (no numerals on screen) | 78.0 RH-2 |
| 96.0–112.0 | V | host: "then you hire the manager. Not before." | SHOT-HOST ×1.0 → P-18 ×1.25 on "**not before**" → P-17 asker 1.8 s (nodding) | CS-2 "**not before**." | 96.0 RH-3 |
| 112.0–118.0 | T | asker: "thank you!" / host: "you got it" | SHOT-GUEST → handover cut SHOT-HOST → hard end 4 f after "it" (P-24) | "thank you!" yellow italic | — |

**Numbers check:** 118 s, 31 cuts → 15.8 cuts per minute; stack share (0–3.8, 26–35.5, 78–96) = 31.3 s = 26.5%; longest full 5.8 s; re-hooks at 8.2, 14, 26, 40, 66, 78, 96 (max gap 26 s); SFX: none.

### 14.2 F-A, fitness podcast: one 4K wide camera (FB-1 faux crops), 96 s
**Clip:** a podcast guest asks the host coach why they are not losing weight. **Archetype:** HA-03b (the verdict is the hook). **Pill:** `EAT THE PROTEIN / FIRST` (the host's words at 71.4 s, no quotes). **Angles:** `CAM:S1` (host faux crop), `CAM:S2` (guest faux crop), `CAM:2S` unused, no wide (FB-3: re-crops instead).

**Hook table**
| t (s) | Speaker: words | Shot | Pill | Captions |
|---|---|---|---|---|
| f0 | — | SHOT-STACK from faux crops: host top (`CAM:S1`, face 0.30 of the cell), guest bottom (`CAM:S2`) | drawn | — |
| 0.05–1.10 | guest: "I train 4 days a week" | stack | on | "I train" → "**4 days** a week" (yellow italic) |
| 1.10–2.60 | guest: "I walk 10,000 steps" | stack | on | "I walk" → "**10,000** steps" |
| 2.60–4.20 | guest: "and the scale doesn't move" | stack | on | "and the scale" → "doesn't **move**" |
| **4.20** | host: "what do you eat after 9?" | handover cut → SHOT-HOST (`CAM:S1`, step 1.0) | carried | "what do you eat" → "after **9**?" white |
| 5.90 | guest: "…honestly? snacks" | handover cut → SHOT-GUEST | **removed on this cut** (5.9 s) | "honestly?" → "**snacks**" |

**Section plan**
| t (s) | Unit | Line | Shots | Caption devices | Re-hook |
|---|---|---|---|---|---|
| 5.9–18.0 | C | 3 short exchanges (protein at breakfast? how much water?) | handover cuts every 1–2.5 s | bold numbers | 5.9 RH-1 |
| 18.0–34.0 | R | host: "it's not the training, it's the 9 pm kitchen" | SHOT-HOST → re-crop ×1.25 → P-17 guest 2.4 s (laughs: P-23) → stack return 6 s | CS-2 "the **9 pm kitchen**" | 18.0 RH-2 |
| 34.0–60.0 | A | host: the plate order, protein first, then fibre, then carbs | re-crops 1.0 ↔ 1.25 every 1.5–2 s (P-18), 2 cutaways, stack return 8 s | voiced quote "you tell yourself “just this once”" (quote style, white italic) | 34.0, 48.0 |
| 60.0–84.0 | A → V | host: "eat the protein first. Every meal." | SHOT-HOST ×1.0 → re-crop ×1.25 on "**first**" → guest reaction 2.0 s | CS-2 "eat the **protein first**" at 71.4 (the pill's words) | 60.0 RH-3 |
| 84.0–96.0 | V / T | host: "do that for 30 days and come back" / guest: "deal" | stack return 8 s → guest "deal" → hard end | "for **30 days**"; "deal" yellow | 84.0 |

**Fallback note at the checkpoint:** "FB-1 used (one 4K wide): faux crops at ≤ 1.9× upsampling; re-crops stay at ×1.25; no wide shot (FB-3)."

### 14.3 F-B, career coaching: a solo answer to a comment, 62 s
**Input:** the creator's take + their screenshot of the comment (supplied). **Archetype:** HA-05. **Pill:** `“HOW DO I ASK / FOR A RAISE?”` (verbatim from the comment, which the creator reads aloud at 0.2–2.0 s).

**Hook table**
| t (s) | Words | Layout | Pill | Bottom cell | Captions |
|---|---|---|---|---|---|
| f0 | — | `L-solo-stack` (face top) | drawn | P-25: the creator's comment screenshot (`fx.shot`, avatar and handle blurred) | — |
| 0.20–2.00 | creator reads: "how do I ask for a raise without sounding greedy?" | stack | on | P-30 underline under "ask for a raise" at 0.6 s (6 f) | yellow italic (speaker override `guest`): "how do I ask" → "for a **raise**" → "without sounding **greedy**?" |
| 2.10–3.40 | "okay, three things" | stack | on | — | white "okay" → "**three** things" |
| **3.40** | "first, bring proof" | `via: cut` → `L-full-solo`, scale 1.0 (P-31) | **removed on this cut** | — | "first," → "bring **proof**" |

**Section plan**
| t (s) | Line | Layout / camera | Inserts | Caption devices | Re-hook |
|---|---|---|---|---|---|
| 3.4–14.0 | "first, bring proof: what you shipped, in numbers" | full; EDL splits at 5.8, 8.1, 10.9, 12.6 with `recrop-in` / `recrop-out` (P-27) | — | bold "**proof**", "**numbers**" | — |
| 14.0–26.0 | "second, ask for a number, not 'more'" | `L-solo-stack` (cut) | P-28 board card: "PROOF" (written at 14.4), "NUMBER" (at 16.2) | voiced quote "not “more”" (quote style) | — |
| 26.0–34.0 | "third, give them a date" | full ×1.0 → `recrop-in` at 30.2 → `recrop-out` at 33.6 | — | CS-2 "a **date**" at 27.1 | — |
| 34.0–44.0 | "so back to your question: it's not greedy if it's priced" | `L-solo-stack` (cut) | P-28 board adds "DATE" (34.3), tick on all three (40.0, 6 f each) | — | **34.0** mid re-hook (window 15.5–46.5 s) |
| 44.0–62.0 | verdict: "proof, number, date. Ask on Monday." | `L-full-solo` (cut, scale 1.0) → `recrop-in` on "**Monday**" | — | CS-2 "ask on **Monday**" | — |

**Numbers check:** 62 s, 15 cuts (EDL splits + stage cuts) → 14.5 per minute; stack share 3.4 + 12 + 10 = 25.4 s = 41%; pill 3.4 s; inserts recorded: I1 question screenshot (creator), board (created, no third party).

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] One format declared (F-A / F-B); duration in range (F-A 90–150 s, F-B 45–90 s). `review`
- [ ] Presence ≥ 80% (F-B 90%); no faceless span > 4 s (F-B 2.5 s). `V-PRESENCE`
- [ ] F-A stage is `L-full-dialogue` throughout; F-B stage only `L-full-solo` / `L-solo-stack`, every entry `via: cut`. `V-LAYOUT`

**2. Hook**
- [ ] f0: pill fully drawn; F-A two faces (stack); F-B face + question card. `V-F0`
- [ ] The pill ≤ 6 words, 2 lines, quotes only if verbatim; out in 0 f where the question sentence ends, between 2.7 and 12 s. `V-TITLE` + `review`
- [ ] Stopper tests: thumbnail, mute, read ≤ 1.2 s, ≥ 3 SCs in 0–3 s, question understood by 1.0 s. `V-F0`, `V-CADENCE`

**3. Body and cadence**
- [ ] 12–18 cuts per minute (F-B 10–18); median shot 1.8–3.2 s (F-B 2.0–4.0); SCs 7–18 per 10 s; max gap 2.5 s. `V-CADENCE`
- [ ] Full shots ≤ 6 s (≤ 1 of 6–10 s per 30 s), stack shots ≤ 20 s; every handover cut ±3 f; cutaways 1–3 s and never across a handover; no cut inside a word. `V-SPEAKER` (SPK-3…6)
- [ ] Stack share 25–45% (F-A); opener 2.7–4.4 s; host on top (or the §20.6 fallback, noted at the checkpoint). `review`
- [ ] Re-hooks every ≤ 30 s (F-A) / one mid re-hook (F-B); intro ≤ 15%. `V-REHOOK`
- [ ] Re-crops only on cuts; no camera events in F-A; F-B alternates `recrop-in` / `recrop-out` and starts with `recrop-in` after each stage change. `V-CAMERA`

**4. Captions**
- [ ] Every word captioned; 1–4 words, 1 line, ≤ 24 characters; sync ≤ 1 f lead; hard swaps. `V-CAPTION`
- [ ] Host white upright, guest yellow italic; ≥ 95% of words labelled; colour follows the voice; voiced quotes styled per §5.3.2. `V-SPEAKER` (SPK-1, SPK-2)
- [ ] Captions 68 px (CS-2 84, CS-3 120) at cy 960 / the seam; never in the NC-5 bands; contrast ≥ 4.5:1 against the real footage. `V-TYPE`, `V-SAFE`
- [ ] Bold ≤ 1 per chunk; CS-2 ≤ 1 per 30 s; CS-3 ≤ 1 per reel; numbers as digits in the style format; glossary spellings; profanity masked. `V-CAPTION`, `V-NUMFMT`

**5. Modules: §20 Dialogue**
- [ ] `veos shots check` passes; the cast names and roles are right; fallbacks (FB-1…) declared. `V-SPEAKER`

**6. Truth and inserts**
- [ ] No sentence reordered or spliced; quoted pill and voiced quotes verbatim. `review` (NC-13)
- [ ] F-B inserts recorded (creator vs created); created cards verbatim; personal identifiers blurred. `V-INSERTS`

**7. Sound contract**
- [ ] No SFX except the optional CTA cue; bed ≥ 18 dB under the voice (target 26); no cue in the 1 s before the CTA. `S1–S6`, `review`
- [ ] −14 LUFS, true peak ≤ −1.5 dBTP. `NC-8`

**8. End and export**
- [ ] The CTA pill (if chosen and spoken) ≥ 1.5 s with the keyword. `V-PROMISE`
- [ ] Hard end ≤ 6 f after the last word; no black tail > 0.2 s; 1080×1920, 30 fps CFR. `review`, `veos qa`
- [ ] Nothing on screen besides footage, captions, the pill(s) and (F-B) the one insert. `review`

---

## Conditional modules (§16–§25)

- **§16 Frame template / chrome:** OFF (`profile.modules.chrome = false`): no persistent slots; the frame is the footage.
- **§17 Running state & anchored graphics:** OFF (`running_state = false`, `anchors = false`): no counters or tracked labels.
- **§18 Data contract:** OFF (`data_figures = false`): numbers are caption words only (§8.5).
- **§19 Evidence & citations:** OFF (`citations = false`): no source cards; the §12.5 inserts flow still applies.

### §20 Dialogue (multi-speaker) `[COND: modules.dialogue] [DNA]` (F-A)
**20.1 Cast**
| ID | Role | Caption style | Preferred angles |
|---|---|---|---|
| `host` | host: {{BV-01.name|the creator}}, the one answering | `host`: white upright | host single (SH-1) → faux crop `<src>:S1` |
| `guest` | asker / interviewee | `guest`: yellow italic | asker single (SH-2) → faux crop `<src>:S2` |
| a third voice (a co-host, an audience shout) | — | `guest` style when it asks, `quote` style when the host voices it | wide (SH-3) |

A third on-camera speaker is not supported in this style: mine a span where only two people talk.

**20.2 Angle map.** From `veos angles`: every real camera is an angle id (its source id); a camera showing 2+ people yields faux angles `<src>:<speaker>`, `<src>:2S`, `<src>:W`. Reframing: single = face 17% of the full frame / 30% of a stack cell, face centre at 36% of the crop, dead-zone subject follow, ≤ 2.0× upsampling; shots that can't crop to 9:16 use `blurfill` (`dialogue.fallback`).

**20.3 Layouts.** SHOT-STACK (host top, asker bottom, seam y 960, no hairline, caption on the seam), SHOT-HOST, SHOT-GUEST, SHOT-RECROP (step 1.25), SHOT-WIDE (§3.2). The stage stays `L-full-dialogue`.

**20.4 Cut grammar.** §9.3 R-SPK…R-SAME; numbers in `dialogue.cut_rules`: `handover_tol_f` 3, `lead_f` 1, `open_s` [2.7, 4.4], `max_hold_s` 10, `stack_max_s` 20, `reaction_s` [1.0, 3.0], `recrop_step` 1.25, `stack_share` 0.35, `min_shot_s` 0.8, `backchannel_max_s` 1.6.

**20.5 Captions.** One speaker per chunk; colour by the speaking voice (§5.3.1); overlapping speech shows only the dominant speaker (the engine labels each word with the dominant talker); the listener's back-channels become their own chunks (P-13).

**20.6 Engine fallbacks in use today (see Engine requests in the report)**
- **Host on top:** the evidence puts the host on top in every stack (v01 @ 0:00 and 0:54, v02 @ 0:00 and 0:54, v03 @ 0:00 and 1:10), even while the asker speaks. Today's generator puts the **speaker** on top and SPK-4 fails otherwise. **Best version today:** keep `veos shots plan`'s speaker-on-top stacks and pass SPK-4 (the asker is on top in the opener); note "host-top pending ER-1" at the checkpoint. When `dialogue.stack.top: "host"` is honoured by the engine, the host goes on top everywhere.
- **Two faces at f0:** V-F0 reads the stage (always `full` in multi-speaker reels), not `timeline.shots`. **Today:** give the pill scene `satisfies: ["two_faces"]` when the first shot is a stack.

**20.7 Single-camera fallback.** One wide → FB-1 (two crops); one person only → F-B.

**20.8 Validator V-SPEAKER.** SPK-1 labels ≥ 95%; SPK-2 one distinct caption style per speaker; SPK-3 a cut within ±3 f of every handover on full shots; SPK-4 the speaker on screen (reactions ≤ 3.5 s, never across a handover; stack top = speaker today); SPK-5 no cut inside a word; SPK-6 holds ≤ max + 1 s.

- **§21 Canvas camera:** OFF (`canvas_camera = false`): footage only.
- **§22 Ink & annotation:** OFF (`ink = false`): the F-B board tick and card underline are part of their insert patterns (P-28, P-30), not an ink layer.
- **§23 Continuity:** OFF (`continuity = false`): no morph chains or motifs.
- **§24 Series furniture:** OFF (`series = false`); the buyer may turn it on (BV-13), but the look is not defined in v1, so it stays off until a template update adds it.
- **§25 Sponsor, brand & end cards:** OFF (`brand = false`; the CTA devices contain no end card). A paid integration still needs the NC-12 disclosure: a TC-legal "Paid partnership" line, Montserrat 500 24 px, x 64, y 1460, for the whole sponsored span.

---

## Part C. Exceptions and the non-overridable core

### C.1 Non-overridable core (how this style meets it)
| NC | In this style |
|---|---|
| NC-1 Face never covered | Pill top ≥ chin + 40 px; captions `avoid_face`; no behind-subject text |
| NC-2 No text on text | Pill (672–880) and caption (905–995) bands never overlap; F-B insert starts at y 1030 |
| NC-3 Smooth motion | Only hard cuts and declared E6 swaps; the pill's 0 f removal is a declared `cuts` time (on a cut or mid-shot) |
| NC-4 Legibility | Captions 68 px (≥ 54), pill 68 px, card text ≥ 40 px, labels 24 px TC-legal; contrast through the caption shadow halo |
| NC-5 IG bands | Captions `max_w` 860 (x 110–970); nothing below y 1500 or above y 110 |
| NC-6 Truth | No figures; created cards labelled; numbers only as spoken |
| NC-7 Creator-owned media | The footage is the creator's; F-B inserts are their files or created substitutes |
| NC-8 Audio | §11 |
| NC-9 Determinism | Scenes are pure functions of the frame |
| NC-10 Hue cap | 2 bright hues max (red + yellow) |
| NC-12 Disclosure | §25 line |
| NC-13 Quote integrity | §1 P0, §5.3.2, §6.5: verbatim quotes, no reordering |
| NC-14 Redaction | Blur names/handles/avatars on comment screenshots; never caption an email or phone number |

### C.2 Declared exceptions
| E-id | Token | Limits | Scenes that use it |
|---|---|---|---|
| E6 Hard swap | `exceptions.E6 {slot_tolerance_px: 4}` | Captions only (inherited from the caption profiles); the band constant ±4 px; first entry / final exit eased | The auto-subtitles |

The buyer may switch E6 off (VAR): captions then swap with a 2 f fade, which softens the style.

---

## Part D. Personalisation

### D.1 What the buyer is asked (one round, ≤ 4 questions, each with "keep the template default")
| ID | Question | Feeds | Default |
|---|---|---|---|
| BV-01 | Your name and handle (you are the host: the white captions) | `creator.name/handle`, the speaker name in `veos speakers --names`, §6.7 | — |
| BV-02 | One or two brand colours | `roles.primary` (the pill), `roles.accent` (the other voice's captions; must stay a light saturated hue) | `#E80001` red, `#F2DF1A` yellow |
| BV-05 | The language you speak, and the captions you want | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) |
| BV-08 | Your call to action: none / in the post text / comment a keyword / link in bio | `profile.cta.chosen`, `creator.cta` | none |

Defaulted, changeable later: BV-03 fonts (Montserrat class), BV-06 number format (₹ + lakh/crore follows an Indian language choice), BV-07 captions are always full in this style (not offered), BV-09 formats (both), BV-11 humour (`off`, max `light`), BV-15 never-on-screen words, BV-17 duration within the class.

### D.2 Lock summary (tokens `locks` holds the full map)
| Area | DNA | TUNE (range) | VAR |
|---|---|---|---|
| Profile | source type, spine, captions mode/role, graphics, footage dependency, modules | duration (adjacent class), presence share ±10, energy one step | language, numbers, formats enabled, CTA choice, comedy (off/light) |
| Colour | the meanings (red pill, white host, yellow guest), `paper`, `ink` | `accent` (light saturated hue, never white), `board`, `void` | `primary` |
| Type | pill recipe (fill, per-line boxes, caps), caption mechanics (1–4 words, 1 line, hard swap, speakers) | pill 64–80 px, captions 56–68 px / 600–700, caption cy 880–1000, CS-2 76–96, CS-3 100–140, emphasis bold ↔ colour | profanity mask |
| Layout & cuts | shot types, hard cuts only, crop-on-cut, host-on-top | seam 900–1020, stack share 25–45%, cut rules ±15%, cadence ±15%, re-crop 1.15–1.35 | the fallback fill (blurfill / letterbox), footage setups |
| Hook & structure | HA-03 default, alternates list, markers none | re-hook interval 20–40 s | per-reel archetype choice |
| Sound | meme cues off | — | bed on/off, CTA cue |

### D.2b How tweaks are classified (examples)
- "Make the pill blue" → `roles.primary` VAR → applied.
- "Bigger captions" → `CS-1.skin.size` 64 → TUNE in range → applied; 72 → out of range → DNA deviation, asked once.
- "Add a zoom on the punch lines" → `zoom_policy` DNA → asked once: "This changes the Conversation Clip DNA (no animated zooms). Keep the style, or change it for you?"
- "Add sound effects on cuts" → `sound` VAR but S1 ties cues to visual moments; cuts are allowed cue moments only if the buyer adds `transitions` to `cue_moments` (VAR).
- "Put my logo in the corner" → a persistent element is not in the style (N1) → DNA deviation.

### D.3 NICHE slots filled per reel
§6.4 hook pairs, §8.4 lookup rows, §14 (after the first approved reel per format), App. A headlines and the glossary are appended per reel from the transcript (structure D.6).

---

## Part E. Changes and decisions

**v1 (2026-10-06), first release as `draft`.** Deviations from the architects' tables (STYLE-COVERAGE row 2) and the analysis, each with its evidence:
| Item | Coverage / analysis said | This template | Why |
|---|---|---|---|
| Stack top | "top = whoever is speaking" (analysis §3) | **Host always on top** (DNA), engine fallback speaker-top until ER-1 | Every stack in v01–v03 has the host on top, including the openers where the asker speaks (v01/v02/v03 @ 0:00) and v02 @ 0:54–1:05 |
| `hook_sc_3s` | 4 | **3** | v01 has 3 caption swaps in 0–3 s and no cut; v02 3; v03 3 + 1 cut |
| Caption anchor | lib:hormozi `chest` (offset 36) | **fixed_y 960** + `avoid_face`, seam in stacks | Measured caption centres sit at y 872–968 in full shots regardless of shot size (v01 @ 0:07, 0:12, 0:51; v02 @ 0:16; v03 @ 0:21) |
| Max chars per line | lib 22 | **24** | "you're playing too small" (24, v01 @ 0:57), "and they'll come to you" (23, v03 @ 2:15) |
| `max_hold_s` / `stack_max_s` | engine 4 / 8 | **10 / 20** | 30 fps scene detection (full and per-cell): full shots up to 10.8 s; stacks 12.1–23.7 s with no in-stack cut (v01 1:27–1:51 is one 23.7 s shot) |
| Pill lifetime | "3–5 s" | **2.7–12 s**, ends in 0 f where the question ends, cut or mid-shot | out at 3.83 / 4.73 / 11.53 s (frame bursts) |
| F-B | "face top, screen/graphic bottom" | the bottom cell holds the **question card**, a **board** or the creator's **screen**: never B-roll | keeps "style by absence"; the card replaces the asker's face |
| Motion (completeness pass, 30 fps) | 1 fps estimates | pill exit tied to the question's end, not to a cut; same-speaker **angle switch** replaces "jump re-crops" (the v01 0:14–0:18 run is host/asker/wide alternation); holds 10 / 20 s; cutaways from 1.0 s; cuts land on chunk boundaries | 113 cuts, 13 frame bursts, `docs/audit/conversation-clip/completeness.md` |
| CTA | none | `none` default; `post_only` / spoken `comment_keyword` / `link_bio` as buyer options with a pill reprise | buyers need a CTA option; the pill is the only device the style owns |

---

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D / BD | D1–D8; BD… (buyer) |
| H / N / BN | H1–H19; N1–N14; BN… (buyer) |
| E / NC | E6; NC-1…NC-14 |
| W / L / G | W-room, W-void, W-board; L-full-dialogue, L-full-solo, L-solo-stack (+ shot types SHOT-STACK, SHOT-HOST, SHOT-GUEST, SHOT-ALT, SHOT-RECROP, SHOT-WIDE); G-1…G-4 |
| CS | CS-1 Conversation, CS-2 Punch line, CS-3 The word |
| HA / ST | HA-03 (+ HA-03b verdict variant), HA-14, HA-05; ST-1…ST-6 |
| SM | none |
| RH | RH-1…RH-5 (re-hook types) |
| P / B | P-01…P-31; B-1…B-4 |
| T / R | T-00; R-SPK, R-OPEN, R-HOLD, R-REACT, R-JZ, R-WIDE, R-STACK, R-BC, R-SET, R-LAUGH, R-END, R-MIN, R-SAME |
| Z | crop_on_cut presets `recrop-in`, `recrop-out` |
| SH / FB | SH-1…SH-5; FB-1…FB-5 |
| F | F-A, F-B |

---

## App. A Headline & hook bank `[NICHE]`
Slots in `[brackets]` are filled per reel from the transcript; quoted pills must be verbatim spans.

**F-A (two-person Q&A)**
| # | Pill | Archetype | Slot notes |
|---|---|---|---|
| 1 | “SHOULD I [VERB] MY / [THING]?” | HA-03 | "SHOULD I SELL MY COMPANY?", "SHOULD I QUIT MY JOB?" |
| 2 | “WHY DO MY / [PEOPLE] [VERB]?” | HA-03 | "WHY DO MY CLIENTS GHOST ME?" |
| 3 | “HOW DO I GET / TO [NUMBER]?” | HA-03 | "HOW DO I GET TO $10K A MONTH?" |
| 4 | “[OPTION A] OR / [OPTION B]?” | HA-03 | "MANAGER OR ONE MORE CLEANER?" |
| 5 | “AM I TOO [ADJ] / TO [VERB]?” | HA-03 | "AM I TOO OLD TO START?" |
| 6 | YOU NEED TO / [VERB] [NOUN] | HA-03b | "YOU NEED TO MAKE BIGGER BETS" |
| 7 | STOP [VERB]-ING / [NOUN] | HA-03b | "STOP TRAINING TO FAILURE" |
| 8 | [NOUN] IS NOT / YOUR PROBLEM | HA-03b | "HIRING IS NOT YOUR PROBLEM" |
| 9 | “IS IT TOO LATE / TO [VERB]?” | HA-14 | the host restates the asker's question |
| 10 | “WHAT WOULD YOU / DO IN MY SHOES?” | HA-03 | for a general "what would you do" ask |

**F-B (solo answer)**
| # | Pill | Archetype | Bottom cell |
|---|---|---|---|
| 1 | “HOW DO I ASK / FOR A RAISE?” | HA-05 | the comment screenshot |
| 2 | “IS [THING] SAFE / EVERY DAY?” | HA-05 | created question card |
| 3 | “WHAT SHOULD I / [VERB] FIRST?” | HA-05 | board with 3 items |
| 4 | “HOW DO I PRICE / MY [SERVICE]?” | HA-05 | board: the formula |
| 5 | “WHY ISN'T MY / [THING] WORKING?” | HA-05 | the creator's own screen |
| 6 | “DO I NEED / [THING]?” | HA-05 | created question card |
| 7 | “HOW LONG UNTIL / I SEE RESULTS?” | HA-05 | board: the timeline (3 dates) |
| 8 | “[A] OR [B] / FOR A BEGINNER?” | HA-05 | board: two columns |
| 9 | “IS IT WORTH / [VERB]-ING?” | HA-14 | the creator restates it on camera |
| 10 | “WHAT WOULD YOU / DO AT [AGE]?” | HA-05 | created question card |

---

## App. B Evidence map
The full source map (every DNA rule → `vNN @ m:ss`) and the `(unverified)` list are in `evidence.md` next to this playbook. Unverified values: the music bed (sound is not observable), the pill's and captions' sub-frame motion (no tween visible at 6 fps: treated as hard), F-B (no solo evidence: built from the analysis's single-speaker fallback), and the CTA devices beyond `none`.
