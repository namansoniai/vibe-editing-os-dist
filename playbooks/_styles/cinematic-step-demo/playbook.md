# Cinematic Step Demo Style Playbook (template v1)

**Purpose:** you (Claude) receive {{BV-01.name|the creator}}'s footage for one reel: a seated desk take plus overhead clips of their hands doing the thing (format F-A, step demo), or a recorded two-person conversation (format F-B, podcast clip). Use this playbook to cut that footage into a quiet, cinematic short that teaches by **showing the hands do it**, step by numbered step, under one warm grade. You add almost no graphics: captions with one gold italic word, a label-tape STEP chip, a recap strip. Everything else is the footage and where you cut it.

**Input it expects** (SW-01): F-A `talking_head` A-roll + overhead hand clips the creator shot (`footage_dependency: high`, §12); F-B `multi_speaker` (one camera per person, or one 4K wide).

### Style DNA `[DNA]`
A dark, warm, low-key picture: tungsten practicals, crushed blacks, shallow depth of field, a lined background behind the presenter and a deep-coloured patterned surface under the hands. The camera looks **straight down at the hands** for most of the reel and cuts are hidden inside their movement. Type is small and quiet: a white grotesk subtitle line where **one word turns into a gold italic serif**, and a black **label-maker tape** reading `STEP 1` at the top of each step, which comes back as a fast recap at the end. Nothing shouts. No banner, no emoji, no stickers, no colour except the gold word.

**Copy these 5 things** (if any one is missing, it is not this style):
1. **One gold italic serif word inside a white grotesk subtitle**, about once every 4 s, always the topic noun or the key verb (§5.3 CS-1, P-KEYWORD-SWAP).
2. **Top-down hand demo on a dark patterned surface** as the main picture of F-A, 45-80% of runtime (§3 L-overhead, §8 P-OVERHEAD-PLATE, §12 SH-1).
3. **The `STEP N` label tape**: white tracked mono caps on black tape, top centre, printed on at the first frame of each step, replayed in the recap strip (§7.2 SM-TAPE, P-STEP-TAPE, P-RECAP-STRIP).
4. **The tungsten grade** on every frame of footage: warm, slightly desaturated, contrasty, vignetted (§4.4 GR-tungsten, P-GRADE-PASS: the built-in footage grade).
5. **Cuts hidden in motion**: on a hand swipe, a page flip, an object turning; in F-B, on the new speaker's first word (§9, T-02, T-03, T-05). The one exception is a rare **white flash** (T-08) at a step boundary or time skip, at most twice a reel.

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Show the hands do it.** Every step that is spoken is seen being done, in overhead footage, on the word | §7.3, §8.4, §12.2 SH-1 |
| D2 | **Result first, in the hands.** F-A opens on the finished result, moving, at frame 0 | §6.2 |
| D3 | **Quiet type.** Captions + one gold word + one tape. No headline, no banner, no emoji, no comedy | §2.4 N1, §5 |
| D4 | **One grade.** Every footage frame is GR-tungsten; created cards sit on the warm-black desk world | §4.4 |
| D5 | **Invisible editing.** Cut in motion, match the action; the only drawn transition is the T-08 white flash, ≤ 2 per reel | §9 |
| D6 | **Numbered and recapped.** Every step gets its tape; the reel ends with a recap of every step | §7.2, §7.3 |
| D7 | **The conversation drives the cut** (F-B): cut on handover, cut away to the listener's reaction, nothing else | §20 |
| D8 | **Calm pacing, dense in time, never in space**: about 20-24 cuts a minute (desk jump cuts included), never more than 2 text elements on screen | §7.6, §2.3 |

Buyer directives `BD1…` `[VAR]` are added here by the buyer and may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches, formats) | ON |
| §1 | Procedure | ON |
| §2 | Hard rules, exceptions (E6), NEVER list | ON |
| §3 | Worlds, layouts, stage moves, safe zones | ON |
| §4 | Colour, grade | ON (§4.3 themes OFF) |
| §5 | Type, caption profiles CS-1/CS-2/CS-3, tapes | ON |
| §6 | Hook system | ON |
| §7 | Structure, ritual, cadence | ON |
| §8 | Visual system: 35 patterns | ON (§8.6 comedy OFF) |
| §9 | Transitions and shot grammar | ON |
| §10 | Motion, camera, layers, finishing | ON |
| §11 | Sound contract | ON (minimal) |
| §12 | Footage, shot list, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (F-A food, F-A craft, F-B podcast) | ON |
| §15 | QA | ON |
| §16 Chrome · §17 State/anchors · §18 Data · §19 Citations | | OFF |
| §20 Dialogue | | ON for F-B |
| §21 Canvas camera · §22 Ink · §23 Continuity · §24 Series · §25 Brand/end cards | | OFF |
| Parts C-F, App. A, App. B | Exceptions, personalisation, changes, IDs, hook bank, evidence | ON |

Formats: **F-A Step demo** (default) · **F-B Podcast clip**.

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile (F-B overrides in formats.F-B.profile)
  source_type: talking_head      # F-B: multi_speaker
  presenter: {presence: guest, share: [20, 50], max_absence_s: 30}     # F-B: anchor [95, 100], 1.0 s
  spine: hybrid                  # F-B: talking_head
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: minimal
  duration: {class: standard, target_s: [55, 90]}                       # F-B: short [35, 60]
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: dual, decimals: 0}
  tone: {energy: calm, comedy: off, comedy_max: off}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A, F-B], default: F-A}
  footage_dependency: high
  cta: {devices: [none, comment_keyword, link_bio, post_only], placement: end, chosen: none}
  modules: {chrome: false, running_state: false, anchors: false, data_figures: false, citations: false,
            dialogue: false, canvas_camera: false, ink: false, continuity: false, series: false, brand: false}
            # F-B: dialogue: true
```

Why each switch has its value:
- **source_type `talking_head` (F-A) / `multi_speaker` (F-B):** v01 is a seated presenter plus a second, overhead camera pass; v02 is a two-camera podcast (15 speaker cuts in 47 s).
- **presenter `guest` 20-50% (F-A):** the face is on screen about 30% of v01; the hands carry the rest. `max_absence_s 30` because v01 runs 0:08-0:39 overhead without the face (31 s), rounded down. F-B is `anchor` 95-100%: a face fills every frame of v02.
- **spine `hybrid` (F-A):** the voice carries the timeline, but the overhead picture decides where the cuts go (cuts on hand motion). F-B is `talking_head`: the conversation take is the timeline.
- **captions `full / support / mute_safe`:** text is on screen 90-95% of both videos, but it never outranks the picture.
- **graphics `minimal`:** three recurring devices only (caption keyword, STEP tape, recap strip). Patterns in §8 are mostly cut and footage patterns.
- **duration `standard` (F-A) / `short` (F-B):** v01 is 110 s, v02 47 s. F-A is trimmed to 55-90 s for short-form reach; `long` stays reachable as a TUNE step.
- **language `en` verbatim:** both videos are English with verbatim burned-in subtitles. Hinglish and Hindi are supported combinations (§5.5).
- **numbers international, dual units:** hands-on niches quote weights, temperatures and lengths; dual units ("18 g (0.6 oz)") keep a global audience.
- **tone `calm`, comedy `off`:** nothing in either video is a gag; the tone is a mentor at a desk.
- **themes `single`:** the grade is the identity (D4); there are no colour packs.
- **footage_dependency `high`:** the overhead second camera is the style (F-A); two synced cameras (F-B). Every shot has a fallback (§12.3).
- **cta `none` default:** neither video has an on-screen CTA. The buyer may pick a quiet device (§6.7).
- **modules:** only `dialogue` (F-B). No data module: numbers appear only as spoken quantities on a tape, never as charts.

### 0.4 Formats `[DNA set; VAR enable]`
| Field | F-A Step demo | F-B Podcast clip |
|---|---|---|
| `when` | A hands-on process taught in 3-7 steps: a recipe, a brew, a craft build, a camera setting, a repair, a routine | A 35-60 s opinion or story moment cut from a two-person conversation the creator recorded |
| profile overrides | none | `source_type: multi_speaker`, `presenter: anchor [95,100] / 1.0 s`, `spine: talking_head`, `duration: short [35,60]`, `modules.dialogue: true` |
| layouts | L-desk, L-overhead, L-insert | L-speaker, L-insert |
| default hook | HA-14 "Result in hand" (§6.2) | HA-14 "Mid-sentence cold open" (§6.2b) |
| structure | `tutorial`: hook → promise → STEP 1…N → recap → close | `conversation`: claim → push-back or question → reframe → button |
| caption profile | CS-1 (56 px, cy 1440) | CS-2 (76 px, cy 1385, speaker colours) |
| cadence | 3-8 SC/10 s, hook ≥ 4, max gap 5.0 s | 2.5-7 SC/10 s, hook ≥ 2, max gap 6.0 s |
| needs | you at a desk + an overhead camera on your hands | a recorded conversation (two cameras, or one 4K wide) |

**Shared DNA** (what makes it one style): the same tungsten grade, the same white grotesk captions with one gold italic serif word, cuts hidden in motion or on speech, and quiet type only. The two formats share 4 of the 5 "copy these" traits (1, 4, 5 fully; 3 is F-A only, 2 is F-A only), so they are one style.

### 0.5 Theme packs
OFF (`themes.policy = single`): the grade is DNA, so the look never changes per topic.

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

The craft step of this style is **P8b "hand-cut selection"**: choosing, in every overhead clip, the frame where a hand or object crosses the frame, so each cut disappears.

### F-A Step demo
1. **P1 Inventory.**
   - `veos ingest` the desk take (source `A`, kind talking-head). `veos conform`.
   - Every overhead clip, result clip and desk insert goes in with `veos asset add <file> --name <id> --origin creator`, named `oh-<step>-<n>` (overhead), `res-<n>` (result), `ins-<n>` (desk insert). Assets are conformed to 30 fps and scaled to 1080 px wide, so **overhead clips must be vertical 9:16** (§12.2). A horizontal clip triggers FB-1 band mode (P-PLATE-BAND).
   - Log each clip: duration, step it shows, the start state, the end state, and the frames where a hand crosses (§1 P8b).
   - Check the grade need: look at frames 25/50/75% of the desk take. Footage that is already warm with crushed blacks gets `GR-tungsten-soft`; neutral or cool footage gets `GR-tungsten` (default).
2. **P2 Prepare.** No matte (the style never puts text behind the head).
3. **P3 Transcribe** source A with word timestamps (`veos transcribe`). Apply `language.captions.transform` (`verbatim` for `en`; §5.5 for the other combinations). Add every tool, ingredient and brand name the creator says to the glossary.
4. **P4 Segment** into `HOOK` (result in hand), `PROMISE` (the desk line naming the outcome and the step count), `STEP-1…STEP-N`, `RECAP`, `CLOSE` (+ `CTA` if a device is chosen). Mark jump-cut points on word boundaries in the desk take.
5. **P5 Classify** every sentence with a line type (§8.4) and its trigger word (the ordinal, the tool, the quantity, the action verb).
6. **P6 Tone-tag** every sentence: `explain` (how), `awe` (the result, the satisfying moment), `win` (it worked, the payoff), `warn` (a mistake to avoid), `cta`.
7. **P7 Hook plan.** Pick the hook pair (§6.4): which result clip opens the reel, which noun gets the first gold word. Write **3 hook variants** (§13.4) and run the stopper tests (§6.1).
8. **P8 Visual plan.**
   - For each step: the overhead clips that show it, in order (§7.3 ritual), and the one optional tape (P-TOOL-TAPE, P-MEASURE-TAPE or P-WAIT-TAPE).
   - **P8b Hand-cut selection:** for every cut between two overhead clips, or overhead → desk, pick the out-frame and in-frame (motion inside ±2 f, §9 T-02/T-03). Read `veos sheet` contact sheets of each asset at 10 fps to find the frames.
   - The recap: one continuous overhead flip-through of the finished object (≤ 1 hidden cut), with the frame where each step's page is open and its ordinal is spoken (§7.3).
   - Inserts: run `veos inserts scan`, then §12.5.
9. **P9 Beat sheet** (§13): one beat per trigger, meeting §7.6. Each beat carries `shot_id` and `fallback_used`.
10. **P10 SFX ledger** (§11) and transition map (§9).
11. **P11 Assets:** every plate scene points at a creator asset; resolve every missing shot with its fallback (§12.3) and say which ones you used.
12. **P12 Checkpoint** (§13.5), then **wait for approval.**
13. **P13 Build:** write `plan/timeline.json` + `plan/scenes.js` (plates graded with `ctx.grade`, §8 P-GRADE-PASS), `veos scenes-meta`, `veos measure`, `veos validate`; preview; QA (§15, at most 3 passes); render.

### F-B Podcast clip (the `multi_speaker` branch)
1. **P1** `veos ingest` every camera and mic file; `veos conform`; **P1b** `veos sync` (two or more files). The session master is `MIX`.
2. **P2** No matte.
3. **P3** `veos transcribe --id MIX`. **P3b** `veos speakers --names "S1=<host name>:host,S2=<guest name>:guest"`. **P3c** `veos angles` (which camera shows whom).
4. **P4 Select the clip:** `veos shots mine --min 35 --max 60`, then pick the candidate that **opens mid-thought on a claim** and **ends on a reaction or a short button line** (§6.2b). Write the EDL on `MIX`; `veos cut`.
5. **P5-P6** Classify and tone-tag (line types §8.4: claim, push-back, story beat, reframe, agreement, laugh).
6. **P7** Three cold-open variants (three different first sentences), stopper tests.
7. **P9b Cut grammar pass:** `veos shots plan --no-stack` (this style never splits the screen), then review every handover and reaction against §20. `veos shots render`. `veos shots check` (V-SPEAKER).
8. **P10-P13** as F-A (`prep-frames` uses the composed footage).

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The nine editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show what's being said; never fake facts; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| ID | Limits in this style | DNA reason | Evidence |
|---|---|---|---|
| **E6** Hard swap | Only the STEP tape inside P-RECAP-STRIP: the tape's text changes `STEP 1` → `STEP 2` on the frame the spoken ordinal ("…one.") lands, during a page flip; the tape container (`data-slot`) keeps one rect (width of the widest label) ±4 px; its first entry and final exit land on picture cuts | The recap is one continuous flip-through; the tape label flips on each spoken count, it doesn't animate | v01 @1:31.1-1:44.2 (STEP 1 → 5 at 91.1, 93.1, 95.0, 98.6, 101.3; one hidden cut at 93.3) |

No other exception. Captions stay ≥ 54 px (no E3): the full-resolution audit measured the v01 subtitle at 52-57 px (cap height 37-42 px on 1080 × 1920), so 56 px is faithful, not a lift.

### 2.3 Style MUST rules
- **H1 Frame 0** (F-A): f0 is the finished result in the creator's hands, already moving (a turn, an open, a lift), full-bleed overhead or angled; the first caption word is on screen by 0.10 s. F-B: f0 is the speaker mid-sentence in a tight single; the first word by 0.10 s. No headline element exists. `check: V-F0`
- **H2 Cadence** (F-A / F-B): weighted state changes 3-8 / 2.5-7 per 10 s; ≥ 4 / ≥ 2 in 0-3 s; longest gap between weight-1 changes 5.0 / 6.0 s; nothing static > 2.5 s; 14-26 cuts per minute; median shot 1.8-3.6 / 2.0-4.2 s. `check: V-CADENCE`
- **H3 Payoff by 1.0 s** (F-A): the finished result is fully inside the frame (y 200-1250) and sharp by 30 f; the first gold word names it by 1.5 s. F-B: the claim's gold word by 1.5 s. `check: V-F0` + `review`
- **H4 Headline limits:** there is no headline element. The only on-screen words are captions, one tape at a time (`STEP N`, or ≤ 3 words + an optional number), and created insert cards (§12.5). `check: review`
- **H5 On the word:** the STEP tape pops on complete on the cut frame into the step and goes off on the next cut; other tapes pop on within 1 f of their trigger word (the tool or quantity); a cut into a new step's overhead lands within ±2 f of the ordinal word. `check: V-ONWORD`
- **H6 Face:** nothing is drawn over a face. The STEP tape (y 165-265) never appears over L-desk unless the head top is ≥ 300; captions sit at cy 1440 (F-A) / 1385 (F-B), below the chin; `avoid_face` stays on. `check: V-FACE`
- **H7 Presence** (F-A): face share 20-50%, longest face absence ≤ 30 s; every reel shows the desk take at least once between the hook and STEP 1 and once at the close. F-B: 95-100%, absence ≤ 1.0 s (an insert ≤ 1.0 s). `check: V-PRESENCE`
- **H8 Promise integrity:** the spoken step count = the number of STEP tapes = the number of recap entries; every step shown in the recap was shown in the body; a promised result in the hook is the result shown at the close. `check: V-PROMISE` + `review`
- **H9 Truth:** every quantity, temperature, time and setting on a tape is exactly what the creator said (with SW-08 formatting); nothing is added. Products shown are the creator's; brand names only as spoken. `check: V-NUMFMT` + `review`
- **H10 Dead air** (spine hybrid): in desk spans, at most 1 gap ≥ 150 ms per 15 s; in overhead spans a breath of ≤ 0.6 s is allowed while the hands keep working (the action carries it); never a pause on a static frame. `check: review`
- **H11 Captions:** profile CS-1 (F-A), CS-2 (F-B), CS-3 (Devanagari); 3-7 words per chunk, ≤ 2 lines, ≤ 17 characters per line (a narrow block); at most one gold word or 2-word phrase per chunk (F-B: two) and ≤ 1 per 4 s; exact spelling of tools, ingredients and brands. `check: V-CAPTION`
- **H12 Layout share** (F-A): L-overhead 45-80%, L-desk 20-50%, L-insert ≤ 15%. F-B: L-speaker ≥ 92%. `check: V-LAYOUT`
- **H13 Handover** (F-B): a cut within ±3 f of every new speaker's first word on full shots; reaction cutaways 1.0-2.6 s, never across a handover; no shot longer than 5 s + 1 s. `check: V-SPEAKER`
- **H14 One grade:** every footage frame (desk, overhead, inserts, podcast) takes the reel's single preset (P-GRADE-PASS: `tokens.grades.footage` on the stage, `ctx.grade` on plates and creator images in cards). `check: review`
- **H15 Overhead framing:** the worked object stays inside y 200-1250; the caption band (y 1380-1500) falls over the dark surface or the hands, never over white paper or a bright plate; caption contrast ≥ 4.5:1 on the measured background. `check: V-TYPE`
- **H16 Audio:** −14 LUFS integrated, true peak ≤ −1.5 dBTP, bed ≥ 18 dB under the voice (NC-8). `check: review`
- **H17 Determinism:** every frame is a function of its index; video frames come from `ctx.videoFrame(name, seconds)` only. `check: review`

### 2.4 NEVER
- **N1** A banner, slab, title card, lockup, emoji, sticker, chunky caption, kinetic type stack or glow. More than one coloured word per chunk. Any coloured caption word other than the `primary` gold.
- **N2** A synthetic transition: whip pan, light leak, glitch, zoom transition, crossfade, slide, push. Cuts only, plus the T-08 white flash (≤ 2 per reel, never in the hook, never in F-B) (§9).
- **N3** A visible fast zoom, shake, crash zoom or rotation snap. Both cameras are locked off (measured: no synthetic zoom in v01 or v02); the only moves are the Z-1 slow drift and a rare Z-2 re-crop on a jump cut.
- **N4** A second bright hue. The only colours added to the footage are the gold word, the tape (dark), cream and warm black.
- **N5** Stock footage, AI-generated hands, food or products, or anyone else's media fetched from the web (NC-7).
- **N6** An ungraded, cool or clinical frame; a white seamless or white desk under the overhead camera (it kills caption contrast and the look).
- **N7** Two tapes at once; a tape over a face; a tape over the caption band.
- **N8** A spoken step with no picture of it being done (D1). If no overhead clip exists, use its fallback (§12.3) or cut the step.
- **N9** Meme sounds, comedy visuals, roast lines treated as jokes.
- **N10** Numbers drawn as charts, counters or bars; a number appears only as spoken, on a tape or in a caption.

Buyer additions `BN1…` `[VAR]` go here.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-footage** | `footage` | The creator's own room and surface, under GR-tungsten | Everything in F-A and F-B: desk take, overhead plates, desk inserts, podcast singles | Hard cuts |
| **W-desk** | `void` | Warm black `#0D0A08` with a radial lift `#2A1E15` → `#140F0B` → `#0A0806` centred at (540, 806), noise 0.035, vignette 0.45 | Created insert cards (P-SCREEN-INSERT, P-PHOTO-PRINT, P-QUOTE-CARD, P-PRODUCT-TAPE) and fallback bands (P-PLATE-BAND, P-STEP-STILL) | Hard cut in and out, on a word boundary |

The surface under the overhead camera is part of W-footage and is the style's second "world": a **deep-coloured patterned surface** (rug, slate, walnut, dark linen; v01 red `#8C1C22` and navy `#233A5E` rug). It is filmed, never drawn.

### 3.2 Layout library
| ID | Engine | Presenter rect | Graphic rect | Caption | Share (F-A / F-B) |
|---|---|---|---|---|---|
| **L-desk** | `full` | full frame; head top y 220-360, face centre x 420-660 | none (the tape is not used here) | CS-1 cy 1440 | 20-50% / — |
| **L-overhead** | `hidden` (stage off; the plate scene fills the frame at z1) | none (the hands are on screen, the face is not) | 0, 0, 1080 × 1920 (the plate) | CS-1 cy 1440 | 45-80% / — |
| **L-insert** | `hidden` + W-desk | none | 64, 200, 952 × 1080 (card) | CS-1 cy 1440 | ≤ 15% / ≤ 8% |
| **L-speaker** | `full` (the composed multi-camera footage from `shots render`) | full frame, tight single: face (brow to chin) ≈ 28% of the frame height, face centre ≈ 40% from the top (audit: v02 @0:01.5, @0:04.4, @0:29 face box y ≈ 450-1170), mic in the lower right | none | CS-2 cy 1385 | — / ≥ 92% |

**Layout schedule (F-A):** a step is one L-overhead run of 4-15 s (several plate cuts inside it), followed by an L-desk return of 2-5 s. An L-overhead run may last up to 30 s (H7) only when the step is one continuous action (writing a full page, kneading); then it carries ≥ 1 cut every 3.6 s inside it.

### 3.3 Stage moves (all cuts)
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Desk → overhead | `stage {t, layout: "L-overhead", via: "cut"}` on the ordinal word; the plate scene starts on the same frame | Into every step |
| **G-2** | Overhead → desk | `stage {t, layout: "L-desk", via: "cut"}` on the first word of the "why" sentence, or on a hand exit (T-02) | After each step, the close |
| **G-3** | Any → insert | `stage {t, layout: "L-insert", via: "cut"}` + world W-desk; the card rises 10 f | A third-party moment (§12.5), a photo print |
| **G-4** | Speaker → speaker (F-B) | a `timeline.shots[]` boundary (`cut_reason: handover / reaction / recrop`) | Every handover and cutaway |

There are no panel drops, splits, PiPs, bubbles or morphs in this style.

### 3.4 Layout diagrams
```
L-overhead (F-A, 45-80%)            L-desk (F-A, 20-50%)              L-speaker (F-B)
┌─────────────────────────┐ 0       ┌─────────────────────────┐ 0      ┌─────────────────────────┐ 0
│ (IG top UI)             │ 110     │ (IG top UI)             │ 110    │ (IG top UI)  books, warm│ 110
│      ▐ S T E P  1 ▌     │ 165-265 │  shelves / lamps, soft  │        │      ╭──────╮ head top  │ ~300
│  dark patterned surface │         │   ╭──────╮ head top     │ 220-360│      │ face │ eyes      │ ~600
│ ┌─────────────────────┐ │ 200     │   │ face │            │        │      │      │ chin      │ ~880
│ │  the object, hands  │ │         │   │      │ chin       │ ~760   │   mic ╲╰──────╯           │
│ │  working on it      │ │         │   ╰──────╯             │        │      shoulders          │
│ │  (object zone)      │ │         │  chest, the object     │        │                         │
│ └─────────────────────┘ │ 1250    │  in hand at the desk   │        │  white caption + gold   │ cy 1385
│   hands enter from the  │         │                         │        │  word (2 lines max)     │ 1310-1460
│ white caption + *gold*  │ cy 1440 │ white caption + *gold* │cy 1440 │                         │
│ (over dark surface)     │1380-1500│                         │        │                         │
│ (IG bottom UI)          │ 1540    │ (IG bottom UI)          │ 1540   │ (IG bottom UI)          │ 1540
└─────────────────────────┘ 1920    └─────────────────────────┘ 1920   └─────────────────────────┘ 1920
```

### 3.5 Safe zones and bands
- Meaning text box: x 64-1016, y 110-1500 (NC-5 bands: nothing in y < 110, y > 1540, or x > 970 between y 900 and 1540).
- **Tape band:** y 165-265 (top 165, h 100), centred at x 540 (TUNE top 150-200). Measured v01 @0:08.5 STEP 1 tape x 386-687, y 165-264 on 1080 × 1920.
- **Caption band:** CS-1 y 1380-1500 (cy 1440); CS-2 y 1310-1460 (cy 1385). Measured at full resolution: v01 blocks span y ≈ 1490-1645 (cy ≈ 1565) and v02 y ≈ 1300-1470 (cy ≈ 1385); v01's position is lifted ≈ 125 px, to the lowest spot that keeps the block above y 1500 (App. B).
- **Overhead object zone:** y 200-1250; nothing important of the demo below y 1300 (the caption band and the IG UI).
- **Tool/measure tape zone:** a free rect beside the object, inside y 280-1200, ≥ 40 px from the object's edge and from the caption band.

### 3.6 Presenter rules
- **F-A:** share 20-50% (v01 ≈ 30%); longest absence ≤ 30 s; the presenter returns by a hard cut (G-2) on a sentence start. Desk crop: head top y 220-360 (v01 @0:06 ≈ 238, @0:57 ≈ 270), face centre x 420-660. The hands on the overhead plates are the presenter's own (keep them; never use someone else's hands without saying so in the post).
- **F-B:** each speaker in a tight single, eyes ≈ y 600, chin ≈ y 880 (v02 @0:00-0:05); the mic may enter the frame from the side.
- Nothing ever sits behind the head (E1 not declared).

---

## §4 Colour and grade `[REQ] [role meanings DNA; brandable hex VAR; grade TUNE]`

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `primary` **Keyword gold** | {{BV-02.primary|#D9A441}} | The emphasised caption word or 2-word phrase (gold italic serif). Nothing else | `ink` | 10.4:1 (ink on gold); gold text on the graded footage ≥ 4.5:1 with the caption shadow | yes (VAR) |
| `accent` **Label tape** | {{BV-02.accent|#0B0B0B}} | Tape fill: STEP chip, tool/measure/wait tapes, name tape, CTA tape | `paper` | 19.6:1 | yes (TUNE: a dark tape colour, OKLCH L ≤ 0.35: black, oxblood, navy, forest) |
| `paper` | `#FFFFFF` | Caption text, tape lettering | — | — | no |
| `ink` | `#0B0B0B` | Card text, shadows | — | — | no |
| `cream` | `#EFE4CC` | The second speaker's captions (F-B guest); paper-print and quote card fill | `ink` | 15.9:1 | TUNE |
| `night` | `#0D0A08` | W-desk base | `paper` | 19.8:1 | TUNE |

Measured at full resolution (fidelity audit): v01 gold is a muted amber (glyph cores `#D9A441`-`#DDAE5A`, median with antialiasing `#CE9C44`, @0:01.2, @0:04, @0:06.6, @1:32), so F-A `primary` is `#D9A441`; v02 (podcast) is a bright saffron-yellow `#F5C518`-`#FAD109` with a faint glow (@0:01.5, @0:04.4), so CS-2 sets that hex directly. Chip black is pure `#000000`-`#0B0B0B`; cream paper `#EDE3C8`.

### 4.2 Meanings
- **Gold = the word that matters** in this sentence: the thing, the action, the name. It never marks good/bad; it marks importance.
- **Black tape = where we are** (step, tool, quantity). A physical label, not a UI element.
- **Cream = paper** (the guest's voice in F-B; prints and quotes).
- There is **no good/bad axis** in this style: a mistake is shown by the hands (a do-over), named in the caption, and its warning word goes gold.
- Brand colours appear only on the creator's own products as filmed.

### 4.3 Theme packs
OFF (`themes.policy = single`).

### 4.4 Grade
| Field | Value (GR-tungsten, default) | GR-tungsten-soft (already-graded footage) |
|---|---|---|
| Footage CSS filter (`tokens.grades.footage`, applied by the engine; plates via `ctx.grade`) | `contrast(1.14) saturate(0.9) sepia(0.16) brightness(0.82)` | `contrast(1.04) saturate(0.95) sepia(0.08) brightness(0.98)` |
| Warmth | +0.16 (sepia 0.14 ≈ tungsten shift towards 3200 K) | +0.08 |
| Saturation | 0.90 | 0.95 |
| Contrast / lift / gain | 1.14 / +0.02 / 0.86 | 1.04 / +0.01 / 0.98 |
| Vignette | radial, transparent to 55% radius, `rgba(0,0,0,0.50)` at the corners | 0.22 |
| Bloom | 0.12 (drawn by the engine grade, E-16) | 0.08 |

Audit (full resolution): McKinnon's A-roll averages `#28201B` over the frame and `#0F100F` above the head (v01 @0:06.6, @1:47.5): the background falls almost to black. Our first stills on Naman's room averaged `#4F4237`, about twice as bright, so the default pass is now darker (brightness 0.82, contrast 1.14, vignette 0.50). Footage that is already dark takes GR-tungsten-soft.

- **One grade per reel**, chosen at P1; no grade events (`grades.events.max_per_reel = 0`), no clip treatments (no B&W, no duotone, no halftone).
- The grade sits **above the footage and created cards, below every piece of type** (z4): tapes and captions keep their exact colours.
- TUNE ranges: warmth 0.08-0.26, saturation 0.80-1.00, contrast 1.00-1.15, vignette 0.20-0.50.

### 4.5 Rules
- `max_bright_per_frame = 2` (gold + at most one bright colour that is in the filmed object itself). Practically: one added hue, the gold.
- Coloured text: only the gold word, on footage, always with the caption shadow `0 2 10 rgba(0,0,0,.62)`.
- Footage **is** regraded in this style, and only by §4.4.

---

## §5 Type and caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within the class]`
| Slot | Family | Weight | Class (TUNE boundary) | Use |
|---|---|---|---|---|
| `body` | **Inter Tight** | 600 | neutral grotesk 400-600 (Inter Tight, Plus Jakarta Sans, Space Grotesk, Poppins) | Captions |
| `serif` | **Instrument Serif** | 400 italic | italic high-contrast serif (Instrument Serif, EB Garamond, Source Serif 4) | The gold keyword; print and quote card lines |
| `mono` | **Courier Prime** | 700 | typewriter slab mono caps | STEP tape and every other tape |
| `display` | Inter Tight | 600 | neutral grotesk 500-700 | Created-card titles (P-SCREEN-INSERT, P-PRODUCT-TAPE subline) |
| `numeric` | JetBrains Mono | 600 | monospace | Numbers on measure tapes |
| Devanagari | **Noto Sans Devanagari** | 500 / 700 | (fixed) | CS-3 captions |

Measured (full-resolution audit): a Helvetica-Now-like grotesk **semibold** with **very tight tracking (≈ −5%, word spaces almost closed)**; italic serif keyword, condensed and high-contrast (closest bundled: Instrument Serif Italic, a near match); the STEP chip is a rough hand-inked typewriter/label-maker face (closest Google: Special Elite, not bundled; the bundled Courier Prime 700 at 60 px, +0.18 em, is the typewriter stand-in and replaces JetBrains Mono).

### 5.2 Headline element
OFF (`type.headline.kind = none`). This style never puts a headline on screen (v01 and v02 have none). The hook is carried by the result picture and the first caption.

### 5.3 Caption profiles `[DNA mechanics; fonts TUNE; language VAR]`

**CS-1 "Gold word" (F-A, every layout)** — `extends: lib:mckinnon`
| Group | Value |
|---|---|
| Mode | `full`, role `support`, `mute_safe` |
| Chunking | unit `phrase`, 3-7 words, ≤ 17 characters per line (block ≈ 300-440 px wide), ≤ 2 lines; never split a name, number or unit; a sentence end breaks; a pause ≥ 0.9 s always breaks |
| Timing | lead 1 f; **reveal `word`**: each word appears on its onset in its final place (the line builds "This" → "This is" → "This is my"), v01 @0:00.17-0:00.83; hold ≥ 0.25 s per word; tail 0.12 s after the last word; **each word fades in over 3 f with a 4 px blur clearing** (v01 f91-93, f32-34); the old chunk clears hard (0 f) on the frame before the next chunk's first word |
| Skin | Inter Tight 600, **56 px** (TC-subtitle), case as spoken (sentence case), tracking **−5%**, line height 1.0 (the two lines nearly touch), `paper` white, no stroke, soft shadow `0 1 6 rgba(0,0,0,.45)`, no container |
| Position | `fixed_y` cy **1440** in L-desk, L-overhead and L-insert; centred, max width 560; `avoid_face` on |
| Emphasis | **`font_swap`**: the chosen word switches to **Instrument Serif italic 400, `primary` gold, 1.3× size** (73 px), same baseline; `span: phrase`, so the gold may run over 2 adjacent content words (v01 @0:04 "Track habits,", @0:06.6 "track everything"). Selection: topic noun, a name, a glossary term or a number; ≤ 1 per chunk, ≤ 1 per 4 s (0.25/s), min score 1.2; never a stop-word |
| Hide | during declared transitions only (there are none in normal use); captions stay on through the recap |
| Language | Latin script; keep English terms verbatim; no spelling normalisation; glossary from the creator |

Second-line behaviour: in the evidence the second line is often smaller (≈ 0.6×, v01 @0:02 "and how I am productive."). Full-resolution frames show what this is: the two lines are often **size-fitted to one common width** (block justify): "This is my *system*" and "and how I am productive." both span x 363-717 (≈ 354 px). **Built in:** CS-1 and CS-3 set `skin.line_fit: "block"`: every line grows to the widest line's width (lines only grow, max 1.6×, never below 56 px), so a short line is set larger and the block reads justified, as measured. Never fake it with a forced line break or a second caption.

**CS-2 "Gold word, two voices" (F-B)** — as CS-1 with: 2-6 words, ≤ 16 characters per line, **76 px** (v02 cap height ≈ 55 px), cy **1385**, max width 640, gold `#F5C518` (v02's brighter yellow), up to 2 gold words per chunk (v02 @0:04.4 "*photographer* … *content*"), `span: word`, emphasis also selects key verbs, profanity mask `inner`. **Speakers:** host `paper` white upright; guest `cream` `#EFE4CC` upright. (v02 shows both speakers in white; the engine requires two distinct speaker styles, so the guest is a warm off-white that reads as white. App. B.)

**CS-3 "Devanagari" (`hi` / Deva)** — as CS-1 with Noto Sans Devanagari 600 at 56 px, line height 1.2, tracking 0; emphasis switches to **`colour`**: the word turns `primary` gold at weight 700 and 1.1× (Devanagari has no true italic serif). Set `captions.profile: "CS-3"` in the timeline for these reels.

**Recap and chunk shape:** a chunk may be a single word when it is a count ("one.", "two.") or a short reply ("Mm-hmm.", F-B back-channels are captioned).

**Gold-word selection rules (P-KEYWORD-SWAP, the single most visible device):**
1. Pick the word a viewer would search for: the object (`tracker`, `dough`, `aperture`), the action (`peel`, `fold`, `bloom`), or the payoff (`fresh`, `sharp`, `crispy`).
2. In a step, the first gold word is the step's subject; in the hook, it is the result's name.
3. Never gold on: pronouns, articles, "really", "just", "so", numbers inside a unit phrase that a tape already shows.
4. If two candidates are in one chunk, gold goes to the noun; the verb stays white.
5. Spacing: ≥ 4.0 s between gold words (≈ 15/min; v01 ≈ 16/min, v02 ≈ 15/min). Force with `captions.overrides {i, emph: true|false}`.

### 5.4 Other text systems
| ID | Element | Recipe | Class | Hold |
|---|---|---|---|---|
| **TX-1** | STEP tape | §8 P-STEP-TAPE: `accent` tape (pure black), h 100, padding 0 16, **square corners**, Courier Prime 700 **60 px** caps (measured cap height 44 px), tracking 0.18 em, `paper` lettering with a 1 px dark emboss (`text-shadow: 0 1px 0 rgba(0,0,0,.55)`) and a 1 px top highlight on the tape (`inset 0 1px 0 rgba(255,255,255,.08)`); top y 165, centred x 540; width ≈ 300 px for `STEP 1` (audit: x 386-687, y 165-264) | TC-label | the first plate shot: on with its cut, off with the next (2.1-3.4 s) |
| **TX-2** | Tool / measure / wait tape | Same tape, h 64, 40 px, tracking 0.25 em, rotated −2…+2° (seeded per reel), pinned beside the object | TC-label | 1.5-3.0 s |
| **TX-3** | Name tape (F-B) | Same tape, h 64, 40 px, `NAME · ROLE`, x 64, top 1200 | TC-label | 2.0 s on the guest's first full shot |
| **TX-4** | CTA tape | Tape h 100, square, Courier Prime 700 56 px, tracking 0.18 em, top 165 | TC-label | ≥ 1.5 s (2.5 s default) |
| **TX-5** | Card title | Inter Tight 600 52 px, sentence case, on cream or night cards | TC-label | the card's life |
| **TX-6** | Print caption | Instrument Serif italic 48 px under a P-PHOTO-PRINT | TC-label | the card's life |
| **TX-7** | Legal line | Inter Tight 500 24 px, `paper` at 70%: "example" | TC-legal | the card's life |

Tape text is ≤ 3 words + an optional number ("STEP 3", "0.5 MM NIB", "18 G · 0.6 OZ", "WAIT 4 MIN"). All caps, never sentence case.

### 5.5 Language and number rules
- `en` → captions verbatim; brand, tool and ingredient names exact (glossary).
- `hinglish` → `hinglish` Latin: romanised as spoken, English terms verbatim; gold rules unchanged (italic serif works on Latin).
- `hinglish` → `en`: translate; the gold word is chosen in the English line.
- `hi` → `hi` Devanagari: CS-3 (colour emphasis, no italic); tapes stay Latin caps (`STEP 1`) because mono caps are Latin-only.
- Numbers: international grouping and dual units by default ("200 ml (6.8 fl oz)", "180°C (356°F)"); with Hindi or Hinglish (BV-06) Indian grouping and metric only. The currency glyph is pre-painted. A quantity on a tape uses the creator's unit first.

---

## §6 Hook system `[REQ]`

### 6.1 Stopper tests
| Test | This style's number |
|---|---|
| ST-1 Thumbnail | At 25% scale, frame 0 shows the finished result (F-A), filling ≥ 35% of the frame area, or a face filling ≥ 20% (F-B). No headline is needed |
| ST-2 Mute | With sound off, 0-3 s shows *what was made* (F-A: the result + its gold name) or *what is claimed* (F-B: the gold word of the claim) |
| ST-3 Motion at f0 | Hands moving the result (F-A) or the speaker talking (F-B) on frame 0 |
| ST-5 Change count | ≥ 4 weighted SCs in 0-3 s (F-A: two hidden cuts + caption swaps); ≥ 2 (F-B) |
| ST-6 Payoff by | Result in frame and sharp by 1.0 s (F-A); the claim's gold word by 1.5 s (F-B) |

ST-4 (headline read time) is n/a: no headline.

### 6.2 Default archetype F-A: HA-14 "Result in hand" `[DNA]`
The finished result, in the creator's hands, is the first picture; the first sentence names it; the reel then promises how to make it.

| t | Beat | Tone | Picture (layout) | Caption (CS-1) | Camera / cut | Cue moment |
|---|---|---|---|---|---|---|
| **f0** | Result in motion | awe | L-overhead: SH-2 result clip mid-motion (hands turning, opening or lifting it); motion blur on f0-f4 is fine | — (the first word lands by f3) | — | — |
| 0.10-1.0 | "This is my…" | awe | Result settles, sharp by f30, inside y 200-1250 | "This is my" → word by word | — | — |
| ~1.0 | The name | awe | Same plate | "…**system**" (gold italic: the result's name) | — | — |
| 1.6-2.7 | Hand passes | awe | Same shot: the free hand swipes across the result 3-4 times (each pass ≈ 5 f of blur), which keeps the frame alive without a cut | second line builds under the first ("and how I stay on track.") | — | — |
| ~2.8 | Hidden cut | awe | **T-02** on the frame the last pass exits → angled hero insert (P-ANGLED-HERO): result held at 30-45°, background black, soft and pushing in | "**Track** habits," | T-02 | — |
| 3.5-5.5 | Benefit run | awe | 1-2 more result angles, 1.0-1.5 s each, each with its own gold word | "track work, track **everything**" | T-02 / T-01 | — |
| 5.5-8.0 | Promise | explain | **G-2 hard cut to L-desk**: the creator, seated, says the promise and the count ("…here's how I set one up in five steps") | "in **five** steps" (gold on the count) | Z-1 push-drift 1.00 → 1.05 | — |
| 8.0 | Into step 1 | explain | **G-1 cut on "First"** to L-overhead, STEP 1 tape pops on | "First, I…" | T-01 | list cue (first) |

Evidence: v01 0:00-0:08 (f0-f2 a blurred flip, cut f3, the notebook swings open f4-f9 and settles sharp at f10; hand passes 1.6-2.7 inside one shot (strip-hook, strip-swipe); "This is my *system*" at 1.0, cut 2.77 to the angled notebook, "*Track habits, track work,* track everything" 0:03-0:05, desk at 0:06, STEP 1 at 0:08).

Archetype mapping note: STYLE-COVERAGE lists F-A as HA-01; the engine's HA-01 requires a headline and the presenter's face at f0, neither of which this style shows (v01 @0:00). HA-14 (caption + live footage at f0, payoff by 1 s) is the archetype the evidence satisfies; the result-first content of HA-01 is kept through the hook pair (§6.4).

### 6.2b Default archetype F-B: HA-14 "Mid-sentence cold open" `[DNA]`
| t | Beat | Picture (L-speaker) | Caption (CS-2) | Cut |
|---|---|---|---|---|
| **f0** | Mid-thought | The speaker who makes the claim, tight single, mouth already moving | first word by 0.10 s | — |
| 0.1-1.5 | Claim builds | same | words build one by one; the claim's key noun goes gold by 1.5 s ("like, *printing*") | — |
| 1.5-3.0 | Claim lands | same | "*photos* is what makes the…" | — |
| 3.0-5.2 | First turn | **cut on handover** to the other speaker, or a 1.0-2.6 s reaction cutaway if the speaker continues | the listener's words in `cream` (guest) or white (host) | T-05 / T-06 |

Evidence: v02 0:00-0:05 (face at f0, "I'm wondering" at 0.17, "*printing*" at 1.33, "*photos*" at 1.83, first cut 5.03).

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`
| ID | Name here | Format | f0 | Payoff | Use when | Example (food) | Example (craft / photo) |
|---|---|---|---|---|---|---|---|
| **HA-10** | Desk flash → result | F-A | L-desk: the creator holding up or pointing at the result, first caption word | Cut to the result full-frame overhead by 0.7 s | The creator's face is the draw (an established channel) or the result is small | "This is the only knife I sharpen like this" → cut to the blade on the stone | "I bind every notebook I use" → cut to the stack of notebooks |
| **HA-16** | Process cold open | F-A, F-B | F-A: the most satisfying moment of the process (a pour, a fold, a stitch pulled tight), no caption needed for 1 s; F-B: a laugh or reaction already in progress | The result or the claim by 5 s | The process itself is the hook (ASMR-like), or the clip starts on a reaction | the bloom of a pour-over, 1.5 s, then "this is how I…" | wax thread pulled tight through leather |

### 6.4 Hook pairs by topic `[NICHE]` (pair type: subject → reveal; F-B: question → answer)
| Topic | First subject (f0) | Reveal by 1.0-5.5 s | How each is shown |
|---|---|---|---|
| [NICHE: example] Morning pour-over (food) | The finished cup, crema swirling as the hand sets it down | "This is my morning **ritual**" → kettle, grounds, the pour (2 angles) → desk promise "four steps" | SH-2 overhead cup; SH-4 angled cup; desk |
| [NICHE: example] Sourdough loaf (food) | Hands turning the baked loaf to show the ear | "This is my everyday **loaf**" → crumb shot when it is torn | SH-2 overhead; SH-4 crumb close |
| [NICHE: example] Weekly meal prep (food) | Hands sliding five filled containers into a row | "Five lunches, one **hour**" → lids closing one by one | SH-2 overhead row |
| [NICHE: example] Leather card holder (craft) | Hands sliding cards into the finished holder | "This is the last **wallet** I'll ever buy" → stitching close-up | SH-2 overhead; SH-4 edge burnish insert |
| [NICHE: example] Hand-bound notebook (craft) | Fanning the pages of the bound notebook | "This is my **notebook** system" → spine stitch close | SH-2 overhead; SH-4 angled |
| [NICHE: example] Film camera loading (photography) | Hands closing the back of the loaded camera, advancing the lever | "Load **film** without wasting a frame" → first frame counter | SH-2 overhead; SH-4 top plate insert |
| [NICHE: example] Print your photos (photography) | Hands laying three prints onto the desk | "Your photos deserve **paper**" → the printer feed | SH-2 overhead prints |
| [NICHE: example] Plant propagation (other hands-on) | Hands lifting a rooted cutting out of a jar | "One **leaf**, one new plant" → the cut node | SH-2 overhead; SH-4 roots |
| [NICHE: example] F-B: printing photos | "I'm wondering if, like, **printing** photos is what makes…" | the listener's push-back by 5 s | L-speaker singles |
| [NICHE: example] F-B: home bread | "The thing that ruins most home **bread** isn't the flour" | "…it's the oven" by 4 s, the listener laughs | L-speaker singles |

The editor writes the row for each new reel at P7 and appends it here in the buyer's copy.

### 6.5 Opening line and post title formula `[DNA formula; NICHE examples]`
There is no on-screen headline. The hook is the **first spoken sentence** (it becomes the first captions) and the post title.
- **Opening line (F-A):** `This is my [gold RESULT NOUN]` / `[Result] in [N] steps` / `The [gold ADJECTIVE] way to [verb] [thing]`. ≤ 8 words before the first gold word lands; the gold word lands by 1.5 s. If the creator's take opens with filler ("So, um, today…"), cut it: the first kept word is the first word of this formula.
- **Opening line (F-B):** the clip starts on the claim, never on the question that led to it; the first gold word is the claim's subject.
- **Post title:** `[Result noun]: [N] steps` or the claim quoted (F-B). Sentence case, no emoji (the post caption may carry one).
- **Write 3 opening variants** from the take (three different cut-in points) and pick by ST-1/ST-2/ST-6.
- **Banned:** "Game changer", "You won't believe", "Life hack", counts that don't match the steps, any line the reel does not show.

### 6.6 Hook sound
See §11: the hook carries no SFX cue (dry, the process sound and voice only); the bed enters after the promise line.

### 6.7 CTA `[DNA device set; VAR values]`
Default `{{BV-08.device|none}}`.
| Device | Spoken pattern | On screen | Hold | Where |
|---|---|---|---|---|
| `none` (default) | The last line is the close ("…and now it's ready to go.") | Nothing; the reel ends on the result (P-END-ON-RESULT) | — | end |
| `comment_keyword` | "Comment {{BV-08.keyword|KEYWORD}} and I'll send you the [deliverable]." | P-CTA-TAPE `COMMENT · {{BV-08.keyword|KEYWORD}}` at the tape band over the final overhead or desk shot; the keyword is also the gold word in the caption | ≥ 1.5 s (2.5 s default) | last 4 s |
| `link_bio` | "The [tool/recipe] is linked in my bio." | P-CTA-TAPE `LINK IN BIO` | ≥ 1.5 s | last 4 s |
| `post_only` | none in the video | Nothing; the CTA lives in the post caption | — | — |

No SFX in the 1.0 s before the CTA's first word. The reel ends ≤ 6 f after the last word (T-07).

---

## §7 Structure and cadence `[REQ] [DNA]`

### 7.1 Structure type
- **F-A `tutorial`:** hook (result in hand, 5-6 s) → promise (desk, 2-3 s) → STEP 1…N (8-25 s each) → recap (one flip-through, 1.9-3.6 s per step) → close (desk, 2-5 s) → optional CTA. Evidence v01: hook 0-6, promise 6-8, STEP 1 0:08-0:37, STEP 2 0:38-0:46, STEP 3 0:47-1:06, STEP 4 1:07-1:24, STEP 5 1:25-1:30, recap 1:31-1:43, close 1:44-1:50.
- **F-B `conversation`:** claim (cold open) → push-back or question → reframe or story → agreement / laugh (button). No markers.

Step counts: 3-7 (VAR per reel). With > 5 steps at 60 s, steps 4+ shrink to 6-8 s each.

### 7.2 Markers (SM-TAPE)
- **Style:** P-STEP-TAPE, one at **every** step, numbering ascending from 1 (`STEP 1`…). Never "Step one", never "01", never "STEP 1/5" (v01 shows the bare number).
- **Recap:** on (P-RECAP-STRIP): after the last step, every tape replays in order over its step's finished-state shot.
- **Teaser chips:** none.
- F-B: `markers: none` (spoken only).

### 7.3 Unit ritual (every step, identical)
| # | Frames (from the ordinal word onset = 0) | What |
|---|---|---|
| 1 | −1 f | **G-1 cut** from L-desk (or from the previous step's last plate) to L-overhead on the ordinal word ("First", "Step two", "Next", "Then"). If the take has no ordinal, cut on the step's action verb |
| 2 | 0 | **STEP N tape pops on, complete, on the cut frame**: no feed, no typing, no fade (measured on all 5 steps, v01 7.73, 37.77, 46.80, 66.90, 84.93) |
| 3 | 0 → the next cut (2.1-3.4 s, mean 2.8 s) | The tape holds for exactly the first plate shot and **disappears hard on the next picture cut** (0-4 f before it). So the step's first plate is a 2.1-3.4 s shot; declare that cut in `cuts` |
| 4 | the step's body, 4-15 s | 2-5 overhead plates, cuts every 1.8-3.6 s, each hidden in motion (T-02/T-03, P8b). The step's subject noun gets the first gold word. On the tool or quantity word: P-TOOL-TAPE / P-MEASURE-TAPE / P-WAIT-TAPE (≤ 1 per step, never while the STEP tape is up; if the trigger word falls inside the STEP tape's hold, skip the tape and make that word the gold word instead) |
| 5 | last 1.0-1.5 s of the run | **P-STATE-JUMP** to the step's finished state (same framing, later moment) |
| 6 | the "why" sentence, 2-5 s | **G-2 cut** to L-desk (with Z-1 push-drift) for the reason or the tip, or P-DESK-SHOW (the creator shows the object to camera). Skip the desk return for a step < 6 s; the next step's G-1 follows directly |

Recap ritual: the desk line that starts the recap ("So now you've got…") → a cut to **one continuous overhead shot of the finished object in both hands**, the STEP 1 tape popping on with it. The hands flip to each step's page (≤ 1 hidden cut on a flip). For each step k the caption builds "You've got your **[item]**," then the ordinal alone as its own chunk ("one."), and the tape swaps to `STEP k+1` on the flip that follows that ordinal (E6). 1.9-3.6 s per step; the tape exits hard on the cut back to the desk. Then the close.

### 7.4 Open loops and re-hooks
- **Loops used:** the result shown at f0 is the loop (paid off when the last step finishes and the close shows it again); the step count spoken in the promise (paid off by the recap).
- **Re-hook (F-A standard: one, `rehook_every_s 35`):** before the first step that starts after 35 s (or at 40-60% of runtime), insert **P-RESULT-FLASH**: 0.8-1.2 s of the finished result from a new angle, with the gold word on the result noun ("…and this is where the **tracker** starts to pay off"). If a step's own payoff shot already shows the full result in that window, it is the re-hook.
- **F-B:** `short`, no re-hook.
- **Intro cap:** hook + promise ≤ 15% of runtime (≤ 9 s at 60 s; v01 8 s at 110 s).

### 7.5 Rhythm and energy curve
- Information only; no entertainment beats (comedy off). The satisfaction is the process: every step ends on a visibly changed object.
- **Energy:** hook (most cuts: ≥ 3 in 5 s) → promise (one calm desk shot) → steps (even, 1 cut per 2-3 s) → **last step gets the most satisfying visual** (the final assembly, the reveal pour, the stitch pulled tight) → recap (calm: one flip-through, the tape counting) → close (one calm desk or result shot, hard end).
- F-B: steady handovers every 3-5 s; the last 2 s is a reaction or a short button line; end on it.

### 7.6 Cadence (state changes)
| Token | F-A | F-B | Evidence |
|---|---|---|---|
| `sc_per_10s` | [3, 8] | [2.5, 7] | ≈ 3 cuts + 4 caption swaps (×0.5) per 10 s |
| `hook_sc_3s` | 4 | 2 | v01: cuts 0.1, 2.77 + 4 swaps; v02: 0 cuts + 4 swaps |
| `max_gap_s` | 5.0 | 6.0 | v01 longest overhead hold 6.7 s (24.67-31.33); v02 5.9 s (15.77-21.7) |
| `hook_max_gap_s` | 3.0 | 5.5 | v02 first cut 5.03 |
| `max_static_s` | 2.5 | 2.5 | live footage counts as continuous motion |
| `caption_weight` | 0.5 | 0.5 | support captions |
| `cuts_per_min` | [14, 26] | [14, 26] | 23.5 (v01, full-rate recount incl. desk jump cuts), 19.0 (v02) |
| `median_shot_s` | [1.8, 3.6] | [2.0, 4.2] | 1.98 (v01; p90 4.7), 2.67 (v02; p90 5.3) |

How the validator sees cuts: cut-map joins (desk jump cuts), stage changes (G-1/G-2/G-3), `timeline.shots` starts (F-B) and **each plate scene's declared `cuts`** (overhead cuts inside one plate scene, §8 P-OVERHEAD-PLATE). Declare every plate cut, or the cadence undercounts.

---

## §8 Visual system: footage, patterns, quiet graphics `[REQ]`

### 8.1 Graphics role and budget (SW-05 `minimal`)
- **Three recurring graphic devices only:** the gold caption word, the tape family (STEP / tool / measure / wait / name / CTA tapes), the recap strip. Everything else is footage you select, cut and grade.
- Graphics beyond captions ≤ 15% of runtime outside the recap; the recap itself ≤ 14 s (v01 13.0 s for 5 steps).
- **Numbers do not become pictures** in this style (minimal graphics): a quantity is shown by the hands doing it (the scale reading, the thermometer in shot) and, at most, named on a P-MEASURE-TAPE.
- Pattern count: 35 named patterns below. 12 are graphic overlays or created cards; the rest are cut, stage and footage-treatment patterns (how the footage is chosen and joined), which is where this style's craft lives.
- Per 60 s (F-A): ≥ 4 families, ≥ 8 distinct patterns.

### 8.2 Families
| ID | Family | Source class | The buyer supplies |
|---|---|---|---|
| **B-1** | Overhead demo footage | buyer-owned | SH-1, SH-2 vertical overhead clips |
| **B-2** | Desk footage (A-roll, inserts) | buyer-owned | SH-3 desk take, SH-4 inserts |
| **B-3** | Conversation footage | buyer-owned | SH-5 cameras, SH-6 reactions |
| **B-4** | Label tapes | engine | — |
| **B-5** | Caption keyword | engine (caption profile) | — |
| **B-6** | Grade and finishing | engine | — |
| **B-7** | Created insert cards | engine (created substitute), or a creator-supplied third-party file | screenshots, screen recordings, photos the creator owns (optional; else created, §12.5) |
| **B-8** | Cut grammar | editor (the cut itself) | — |

### 8.3 Pattern specs
Frames at 30 fps. Engine building blocks are named so the scene code is unambiguous.

**A. Type and tapes (B-4, B-5)**
| ID | Type | What's on screen | Motion recipe | When | Text class / engine |
|---|---|---|---|---|---|
| **P-KEYWORD-SWAP** | annotation (caption) | One word of the white caption set in Instrument Serif italic, gold, 1.3× | Fades in on its onset like every word (3 f, blur 4 → 0); stays until the chunk clears (hard) | ≤ 1 per chunk, ≤ 1 per 4 s, on the topic noun / key verb / name (§5.3) | TC-subtitle; caption engine CS-1/2 `emphasis.mechanism: font_swap`; force with `captions.overrides {i, emph}` |
| **P-STEP-TAPE** | overlay (marker) | Black label tape `STEP N`, top centre y 165-265, ≈ 300 × 100, square corners | Pops on complete on the cut frame (0 f); holds for the first plate shot (2.1-3.4 s); off hard on the next picture cut (0 f). No feed, no typing, no fade | First frame of every step's overhead run | TC-label 60 px; bespoke scene, z6, `in: "none"`, `out: "none"`, t1 = the next cut |
| **P-RECAP-STRIP** | stage + overlay | One continuous overhead shot: both hands flip the finished object to each step's page; the tape counts `STEP 1` → `STEP N`, one per spoken ordinal; caption "You've got your **[item]**," then "one." | One tape scene for the strip: container fixed at the widest label's width (`data-slot`), pops on at the cut in, text swaps hard on the frames listed in `events` (E6), off hard on the cut out; one plate scene (1-2 segments, the join on a page flip) | After the last step, before the close | TC-label; `exception: "E6"` |
| **P-TOOL-TAPE** | overlay (label) | A tape naming the tool, ingredient or material ("0.5 MM NIB", "BREAD FLOUR") beside the object, rotated −2…+2° (seeded) | Pops on (0 f) on the trigger word or a cut; hold 1.5-3.0 s; off hard on a cut, else a 2 f fade | On the tool's name, when the object is in shot; ≤ 1 per step; never while the STEP tape is up | TC-label 40 px, z5 (inferred extension of the STEP tape, App. B) |
| **P-MEASURE-TAPE** | overlay (label) | A tape with the spoken quantity, creator unit first: "18 G · 0.6 OZ", "92°C · 198°F", "3 MM · 1/8 IN" | as P-TOOL-TAPE | On the spoken number; the number must be spoken (H9) | TC-label 40 px, z5; numbers via `ctx.fmtNum(v, {unit, units: "dual"})` |
| **P-WAIT-TAPE** | overlay (label) | A tape with a duration: "WAIT 4 MIN", "REST 1 HR" | as P-TOOL-TAPE, starting on the cut that skips the wait (P-STATE-JUMP) | Wherever the process skips time | TC-label 40 px, z5 |
| **P-NAME-TAPE** | overlay (label, F-B) | `NAME · ROLE` tape at x 64, top 1200 | Pops on (0 f); hold 2.0 s; off hard on a cut, else a 2 f fade | The guest's first full single, when the guest is not the creator | TC-label 40 px, z5; bottom 1264 stays clear of the CS-2 band (1280) |
| **P-CTA-TAPE** | overlay (CTA) | `COMMENT · KEYWORD` or `LINK IN BIO`, top centre, 48 px | Pops on (0 f); hold ≥ 1.5 s; no exit (the reel ends) | Last 4 s, only with a CTA device (§6.7) | TC-label; `kind: "cta-keyword"`, `text_content` contains the keyword |

**B. Overhead and desk footage (B-1, B-2, B-8)**
| ID | Type | What's on screen | Motion recipe | When | Engine / evidence |
|---|---|---|---|---|---|
| **P-OVERHEAD-PLATE** | stage (footage) | A vertical overhead clip full-bleed (1080 × 1920, cover crop) while the stage is `L-overhead` (hidden) | One z1 scene per overhead run with `segments: [{asset, from (local s), offset (clip s), crop?}]`; render picks the active segment and draws `ctx.videoFrame(seg.asset, lt - seg.from + seg.offset)`; every segment boundary is listed in `cuts`; `kind: "broll"` | Every step body | SH-1; `veos asset add`; z1, graded with `ctx.grade` (P-GRADE-PASS) |
| **P-RESULT-OPEN** | stage (footage) | The finished result moving in the hands at f0 | A P-OVERHEAD-PLATE from t 0 on SH-2, offset chosen so f0 is mid-motion and f30 is sharp | Hook f0 (§6.2) | SH-2 (FB-2); `satisfies: ["footage"]`; v01 @0:00 |
| **P-HAND-SWIPE-CUT** | cut | Cut on the frame where a hand or arm covers ≥ 50% of the frame width while moving ≥ 25 px/frame; the next clip starts on a hand leaving or entering in the same direction | 0 f; out-frame and in-frame picked at P8b, ±2 f around peak blur | Overhead → overhead; overhead → desk | v01 @0:01.5, @0:34, @1:12 |
| **P-FLIP-CUT** | cut | Cut at the peak of an object rotation: a page turning, the object flipped, a lid lifting | 0 f; the frame of maximum blur or edge-on angle | When the object turns | v01 @0:00.1, @1:12 |
| **P-HELD-TO-CAMERA** | stage (insert) | The object held up close to the desk camera, background falling to black | Plate on SH-4 (or the desk take, crop 1.0); P-RACK-IN on entry when the footage has no real rack | Naming a detail, a component; the recap entries | SH-4 (FB-4); v01 @0:03-0:05, @0:38, @1:31-1:43 |
| **P-ANGLED-HERO** | stage (insert) | The result held at 30-45°, shallow focus, dark surround | Plate on SH-4 that **pushes in 1.00 → 1.15-1.22 over the shot, ease-out** (most of it in the first 0.6 s) **and racks from soft to sharp over 30-40 f** (measured 2.77-4.57: ×1.22, sharp at 4.3). Keep the footage's own push; else draw the scale in the plate | The hook's second angle; the close | SH-4; v01 @0:02.8-0:05 |
| **P-DESK-TALK** | stage (A-roll) | The creator seated, chest-up, lined background | L-desk; Z-1 slow drift on shots ≥ 5 s; plain jump cuts on sentence ends (Z-2 re-crop only 1 in 3 or fewer) | Promise, every "why", the close | SH-3; v01 @0:06, @0:57-1:06 |
| **P-DESK-SHOW** | stage (A-roll) | The creator shows the object or material to the camera in the desk take | L-desk; no zoom; the caption names it in gold | Introducing a material, a tool, the result | SH-3; v01 @0:41, @1:05, @1:48 |
| **P-MACRO-PUNCH** | footage-treatment | A crop-in on the overhead detail (1.20-1.35×): the nib, the seam, the dial | A hard re-crop on a cut (never animated); the scale stays for the shot; the detail lands inside y 300-1200 | The detail word ("this edge", "right on the line") | Segment `crop: {scale, cx, cy}`; 4K vertical for 1.35× |
| **P-STATE-JUMP** | cut | Same framing, later state (time skipped): the empty grid → the filled grid | Hard cut, 0 f; the object's position matches within ±30 px | The end of a step; any wait | SH-1 filmed in two passes; v01 @0:34-0:35 |
| **P-RESULT-FLASH** | stage (re-hook) | 0.8-1.2 s of the finished result from a new angle | A plate segment cut in and out hard; the gold word on the result noun | The mid-reel re-hook (§7.4) | SH-2 / SH-4 |
| **P-RACK-IN** | footage-treatment | The insert starts soft and racks into focus | Plate filter `blur(6px)` → `blur(0)` over 30-40 f, ease-in-out, from the cut frame (a slow rack, not a snap) | Entering P-HELD-TO-CAMERA / P-ANGLED-HERO without a real rack | v01 @0:03 (real rack) |
| **P-SLOW-PUSH** | footage-treatment (camera) | The desk shot drifts in 1.00 → 1.03 (barely seen) | `camera {t, preset: "push-drift"}` over the shot | L-desk shots ≥ 5 s; ≤ 1 per 2 desk shots | Z-1; v01 57.0-66.9 measured 1.00 → 1.024 over 9.9 s |
| **P-JUMP-RECROP** | footage-treatment (camera) | A desk jump cut. Default: a **plain jump cut, same framing** (4 of 5 measured: v01 60.9, 80.8, 89.7, 107.8); occasionally a small re-crop 1.00 ↔ 1.07 (v01 90.2) | Plain cut on a sentence end; for the re-crop `camera {t: cut, preset: "snap-punch"}` + `reset` on the next cut | Every jump cut inside one desk take (≈ 1 per 5-6 s of desk talk); re-crop ≤ 1 in 3 | Z-2 |

**C. Grade and fallbacks (B-6, B-1)**
| ID | Type | What | Recipe | When | Engine |
|---|---|---|---|---|---|
| **P-GRADE-PASS** | footage-treatment | GR-tungsten over the whole reel | **Built-in (E-16), no scene.** The stage footage takes `tokens.grades.footage` (GR-tungsten numbers, vignette 0.50 on the window, bloom 0.12) automatically; GR-tungsten-soft is `timeline.grade: "GR-tungsten-soft"`. Video assets are not graded by core, so every z1 plate / still scene that draws `ctx.videoFrame` or an image asset sets `style="${ctx.grade(ctx.gradeId \|\| "GR-tungsten", {spatial: true})}"` on its `<img>` / plate div (same preset, vignette included). Creator photos/recordings inside z3 cards take `ctx.grade(...)` colour-only (no `spatial`); drawn card chrome, tapes and captions stay ungraded (the engine never grades graphics) | Every reel, both formats (H14) | App. B |
| **P-PLATE-BAND** | stage (fallback) | A horizontal 16:9 overhead clip as a band (1080 × 608, cy 760) over a blurred, darkened copy of itself (blur 40 px, brightness 0.45) | A plate variant: two draws of the same frame (blurred cover + sharp band) | FB-1: the creator's overhead is horizontal | W-desk; `fx.clip` building blocks |
| **P-STEP-STILL** | stage (fallback) | A still photo of the step's state, full-bleed, pushing 1.00 → 1.06 over the shot | Plate segment on an image asset; push eased; hard cuts between stills | FB-1: only photos of the steps exist | image assets |

**D. Conversation (B-3, F-B)**
| ID | Type | What | Recipe | When | Evidence |
|---|---|---|---|---|---|
| **P-COLD-OPEN** | cut | The clip starts mid-sentence on the claim | EDL in-point 1-3 f before the first kept word; no lead-in silence | F-B f0 | v02 @0:00 |
| **P-SPEAKER-CUT** | cut | Cut to the new speaker on their first word | `timeline.shots` boundary, 1 f lead, ±3 f | Every handover | v02, 15 cuts in 47 s |
| **P-REACTION-CUTAWAY** | cut | 1.0-2.6 s of the listener (nod, smile, look away) while the speaker continues | Shot `cut_reason: "reaction"`; never across a handover; captions stay with the speaker | Every 6-10 s of one speaker's run, on a punchline or a strong claim | v02 @0:08, @0:37 |
| **P-TALK-RECROP** | cut | A re-crop 1.00 ↔ 1.15 on a sentence boundary inside one speaker's run (> 5 s) | Shot `cut_reason: "recrop"`, `step: 1.15` | Long single runs | 4K source |
| **P-BUTTON-END** | cut | The last 1.0-2.0 s is a reaction or a two-word reply ("Yeah, yeah."), then a hard end | The last shot is the reaction or reply; T-07 | F-B end | v02 @0:43-0:46 |

**E. Inserts (B-7; §12.5)**
| ID | Type | What | Recipe | When | Created substitute |
|---|---|---|---|---|---|
| **P-SCREEN-INSERT** | overlay (card) | The creator's screen recording or screenshot in a dark card (radius 18, 1 px `rgba(255,255,255,.12)` border) on W-desk | `fx.shot` (creator file) or `fx.appUI` (generic UI) at x 64-1016, y 260-1240; rise 10 f; a 1.00 → 1.04 push inside the card | An app or software in the step (an editing app, a timer, a camera menu) | `recreated_ui` |
| **P-PHOTO-PRINT** | overlay (card) | A photo as a matte print: cream border 28 px, rotated −1.5°, soft shadow, on W-desk; an italic serif line under it | Card rise 10 f; hold; hard out | A photo the creator owns (a past result, a reference) | none: creator-supplied only; otherwise use P-RESULT-FLASH or cut the moment |
| **P-PRODUCT-TAPE** | overlay (label) | A product or brand name set on a tape (type, never a logo), optional serif subline ("my everyday kettle") | P-TOOL-TAPE recipe at 48 px, centred at y 700 on W-desk, or beside the object on a plate | A product named with no clean shot of it | `logo_plate` |
| **P-QUOTE-CARD** | overlay (card) | A cream card (radius 6): the quote in Instrument Serif italic 54 px, the name in mono 28 px caps; verbatim | `fx.quoteCard` with the paper theme; word-by-word reveal | Someone else's words read aloud | `quote_card` |

**F. Close**
| ID | Type | What | Recipe | When | Evidence |
|---|---|---|---|---|---|
| **P-FLASH-CUT** | transition | The picture blooms to white and the next shot is revealed from the top down | T-08 (§9.1). **Built-in transition, no scene:** `timeline.transitions[]` entry `{"t": <cut>, "type": "flash", "frames": 7, "pre": 2, "peak": 1.0, "decay": 0.4, "colour": "#FFFFFF", "clear": "wipe", "clear_frames": 2, "dir": "down"}` (default `layers: "picture"`: covers the world, the footage and the z1 plates, under the captions). Rises over the 2 `pre` frames (the bloom), peaks on the cut, holds near-white ≈ 3 f, then clears in the measured 2 f top → bottom wipe (`clear: "wipe"`, `dir: "down"`) | A step boundary or a P-STATE-JUMP time skip; ≤ 2 per reel | v01 34.57 ("It starts to fill"), 37.57 (into STEP 2) |
| **P-END-ON-RESULT** | stage | The final shot shows the finished result: in hand, at the desk or overhead | Hard end ≤ 6 f after the last word | Every F-A reel | v01 @1:48 |

### 8.4 Line → pattern lookup `[NICHE]`
| Line type | Primary | Alternates |
|---|---|---|
| "This is my [result]" (hook) | P-RESULT-OPEN + P-KEYWORD-SWAP | P-ANGLED-HERO |
| A benefit of the result ("track habits, track work") | P-ANGLED-HERO / P-HELD-TO-CAMERA, one angle per benefit | P-RESULT-FLASH |
| The promise + count ("here's how, in five steps") | P-DESK-TALK + gold on the count | P-DESK-SHOW |
| Ordinal + action ("First, I flip to the back") | G-1 + P-STEP-TAPE + P-OVERHEAD-PLATE | — |
| Naming a tool or material | P-OVERHEAD-PLATE with the tool in hand + P-TOOL-TAPE | P-DESK-SHOW, P-PRODUCT-TAPE |
| A quantity, temperature, size or setting | P-MACRO-PUNCH on the reading + P-MEASURE-TAPE | the number as the gold word |
| A precise detail ("right on the line") | P-MACRO-PUNCH | P-HELD-TO-CAMERA |
| A wait or time skip ("let it rest an hour") | P-STATE-JUMP + P-WAIT-TAPE | — |
| The step's outcome ("and it starts to fill") | P-STATE-JUMP | P-HELD-TO-CAMERA |
| Why it works / a tip | P-DESK-TALK + P-SLOW-PUSH | P-DESK-SHOW |
| A mistake to avoid (`warn`) | P-OVERHEAD-PLATE of the wrong way (if filmed), then the right way; gold on the warning word | P-DESK-TALK + P-JUMP-RECROP |
| An app, a site or software in the process | P-SCREEN-INSERT | P-DESK-TALK |
| A past result / a reference photo | P-PHOTO-PRINT (creator file) | P-RESULT-FLASH |
| A product or brand with no shot of it | P-PRODUCT-TAPE | caption only |
| Someone else's words read aloud | P-QUOTE-CARD | caption only |
| Recap ("you've got your…") | P-RECAP-STRIP | — |
| Closing line | P-END-ON-RESULT | P-DESK-SHOW |
| F-B claim / opinion | P-COLD-OPEN, the speaker single | P-TALK-RECROP |
| F-B new speaker | P-SPEAKER-CUT | — |
| F-B listener reacts | P-REACTION-CUTAWAY | — |
| F-B laugh or agreement at the end | P-BUTTON-END | — |
| [NICHE: example] Food: "add the salt", "pour in circles", "fold the dough" | P-OVERHEAD-PLATE (+ P-MEASURE-TAPE for the amount) | P-MACRO-PUNCH |
| [NICHE: example] Food: "it's ready when…" | P-STATE-JUMP → P-HELD-TO-CAMERA (texture to camera) | P-ANGLED-HERO |
| [NICHE: example] Craft: "punch the holes", "stitch", "burnish the edge" | P-OVERHEAD-PLATE + P-MACRO-PUNCH | P-TOOL-TAPE |
| [NICHE: example] Craft: "the glue needs to dry" | P-STATE-JUMP + P-WAIT-TAPE | — |
| [NICHE: example] Photography: "set your aperture to f/2" | P-MACRO-PUNCH on the dial + P-MEASURE-TAPE `F/2` | P-SCREEN-INSERT (the creator's camera-menu recording) |
| [NICHE: example] Photography: "in my editing app I…" | P-SCREEN-INSERT | P-DESK-TALK |

### 8.5 Data and truth rules
- No data figures (module off). Quantities are spoken by the creator and shown by the hands; a tape repeats them exactly (H9, NC-6).

### 8.6 Comedy layer
OFF (`tone.comedy = off`).

### 8.7 Asset rules
- **Real footage first:** every step is the creator's own overhead footage. No stock, no AI-generated hands, food or objects (N5).
- Created cards (§8.3 E) are generic and unbranded; product names are set in type on a tape, never a fetched logo.
- Third-party moments follow ask-then-create (§12.5).
- Blur personal data on screen recordings and labels (NC-14).

### 8.8 Density and variety
- F-A: a weight-1 change (cut, tape, stage) at least every 5.0 s, caption swaps every 1.0-1.6 s between them.
- ≥ 8 distinct patterns and ≥ 4 families per 60 s.
- The same plate framing never twice in a row across a cut, except P-STATE-JUMP (that is its point).
- The step ritual repeats identically (§7.3); that repetition is intended.

---

## §9 Transitions and shot grammar `[REQ] [DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-01** | Hard cut | 0 | On a word boundary ±1 f (desk), or anywhere inside an action (overhead) | none |
| **T-02** | Hand-swipe cut | 0 | P-HAND-SWIPE-CUT: out on ≥ 50% hand coverage in motion, in on a matching hand motion, ±2 f | none |
| **T-03** | Flip cut | 0 | P-FLIP-CUT: cut at the object's peak rotation / blur | none |
| **T-04** | Rack-in | 8 (on the incoming insert) | P-RACK-IN: blur 6 → 0 px, ease-out, from the cut frame | none |
| **T-05** | Speaker cut (F-B) | 0 | On the new speaker's first word, 1 f lead, ±3 f | none |
| **T-06** | Reaction cut (F-B) | 0 | Into and out of a listener reaction, on a word boundary of the speaker | none |
| **T-07** | Hard end | 0 | ≤ 6 f after the last word; no black tail, no fade | none |
| **T-08** | White flash | 6-7 | P-FLASH-CUT: f0-1 the outgoing shot washes out (bluish-white bloom), f2-4 solid white `#FFFFFF`, f5-6 the white recedes downward (a soft-edged top → bottom wipe) revealing the incoming shot; captions stay on top. Measured v01 34.57-34.77 and 37.57-37.77. Built: `transitions[]` `type: "flash"` (7 f, pre 2, peak 1.0, decay 0.4, `clear: "wipe"`, `clear_frames: 2`, `dir: "down"`: the measured top → bottom reveal) | none (silent; sound not observable) |

That is the whole library. T-08 is the only thing drawn between shots, ≤ 2 per reel, never in the hook or F-B.

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | A mid-motion result (F-A), a mid-sentence speaker (F-B) | A fade-in, a still frame, a title |
| Inside the hook | T-02 / T-03: two hidden cuts by 3 s | A visible jump on a static frame |
| Hook → promise | T-01 to L-desk on the promise's first word | — |
| New step | T-01 or T-02 + the STEP tape; T-08 at most once (v01: into STEP 2) | Any other effect, a pause |
| Overhead → overhead | T-02 / T-03; P-STATE-JUMP for time skips (T-08 allowed on one) | Two identical framings back to back (except P-STATE-JUMP) |
| Overhead → desk | T-02 (the hand leaves the frame) or T-01 on the "why" sentence | A cut inside a word |
| Desk jump cut | T-01 + P-JUMP-RECROP, alternating | Two re-crops in a row |
| Into an insert | T-01; T-04 for desk inserts | — |
| Recap entries | No cut: the hands flip pages, the tape counts; ≤ 1 hidden cut (T-03 on a flip) | Hard cuts between stills |
| F-B handover | T-05 | A cut inside a word; a split screen |
| Last word | T-07 | A black tail; an outro card (unless a §6.7 device) |

### 9.3 Shot grammar R-…
| ID | Rule |
|---|---|
| **R-1** | **Cut on hand motion:** in overhead runs ≥ 60% of the cuts are T-02 or T-03 (hidden). A hard cut on a static frame only at a step's first frame |
| **R-2** | **Ordinal → overhead:** the cut into a step's overhead lands within ±2 f of the ordinal word |
| **R-3** | **Why → desk:** the desk returns on the first word of the reason/tip sentence and lasts 2-5 s |
| **R-4** | **Match action:** a motion that crosses a cut keeps its direction (a hand moving right exits right; the next clip's hand moves right) |
| **R-5** | **State-jump framing:** P-STATE-JUMP keeps the object's position within ±30 px; otherwise it reads as a mistake, so re-frame with a segment crop |
| **R-6** | **Handover (F-B):** a cut within ±3 f of every new speaker's first word; a back-channel ≤ 1.6 s ("yeah", "right") does not take the floor |
| **R-7** | **Reaction (F-B):** a 1.0-2.6 s listener cutaway at least every 10 s of one speaker's run, on a punchline or a strong claim; never across a handover |
| **R-8** | **Re-crop (F-B):** in a single run > 5 s, re-crop 1.00 ↔ 1.15 on a sentence boundary |
| **R-9** | **Never cut inside a word**, in any format |

### 9.4 Budget (per 60 s)
- Cuts: 14-26 (F-A ≈ 19; F-B ≈ 19).
- T-04 ≤ 3. T-08 ≤ 2 per reel. Z-2 re-crops ≤ 2. P-REACTION-CUTAWAY 3-6 (F-B).
- T-01/T-02 may repeat 3× in a row inside overhead runs and the recap (they are invisible by design); every other transition never 3× in a row.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Lead | 1 f before the onset (captions, tapes) |
| Tape in / out | 0 f: pops on with a cut, off with the next cut (measured, all 6 tape appearances) |
| Caption word in | 3 f: opacity 0 → 1 with blur 4 → 0 px (v01 f91-93, f32-34; v02 f38-40); the chunk clears hard (0 f) |
| White flash | 7 f (T-08) |
| Card rise (inserts) | 10 f, translateY 40 → 0 + blur 8 → 0, expo-out; exit 6 f fade |
| Rack-in | 30-40 f, blur 6 → 0 px, ease-in-out |
| Push-drift | 1.00 → 1.03 over the whole shot, in-out (desk); 1.00 → 1.15-1.22 ease-out (P-ANGLED-HERO) |
| Re-crop | on a cut: 1.07 (desk, rare), 1.15 (F-B), 1.20 (overhead take change, v01 84.9), 1.20-1.35 (P-MACRO-PUNCH) |
| Hold | tapes ≥ 2.0 s (STEP) / ≥ 1.5 s (others); text ≥ 0.25 s per word |

### 10.2 Footage camera (`zoom_policy: presets`)
| ID | Preset | Recipe | Use |
|---|---|---|---|
| **Z-0** | `reset` | Back to 1.00 on the next cut | After a Z-2 |
| **Z-1** | `push-drift` | 1.00 → 1.03 over the shot (≥ 5 s), eased in-out | Desk shots (`explain`, `awe`, `win`) |
| **Z-2** | `snap-punch` | 1.00 → 1.07 in **1 f, on a jump cut only** (a re-crop, never a visible zoom) | ≤ 1 in 3 desk jump cuts (`explain`, `warn`) |

Rules (measured with ORB on every frame of v01/v02: no synthetic zoom, rotation or shake anywhere; all apparent scale change is the hands or the subject moving): ≤ 1-2 camera events per minute; never the same Z twice in a row; never two moves within 0.4 s; plates are never zoomed by the camera (P-MACRO-PUNCH is a segment crop on a cut); the face never leaves y 220-760 in L-desk.

### 10.3 Canvas camera
OFF (§21).

### 10.4 Layer order (back to front)
1. World (W-footage / W-desk), then **z1 overhead plates** (P-OVERHEAD-PLATE, P-STEP-STILL, P-PLATE-BAND)
2. The stage footage (the desk take; the composed podcast footage)
3. z3 created insert cards (P-SCREEN-INSERT, P-PHOTO-PRINT, P-QUOTE-CARD; P-PRODUCT-TAPE on W-desk)
4. (z4 free: the grade is built in, P-GRADE-PASS; footage graded by the engine, plates by `ctx.grade`)
5. z5 tool / measure / wait / name tapes
6. z6 STEP tape, CTA tape
7. z7 captions (auto)

z8-z11 are never used.

### 10.5 Finishing
- Vignette: in the grade only (0.50 on the footage window and on plates via `ctx.grade(..., {spatial: true})`; TUNE 0.30-0.60).
- Grain: only on W-desk (noise 0.035); none added over footage.
- Glow and bloom: the grade's bloom only (0.12, built in); no glow.
- Shadows: captions `0 2 10 rgba(0,0,0,.62)`; tapes `0 3 8 rgba(0,0,0,.35)`; cards `0 18 40 rgba(0,0,0,.45)`.
- Radii: tapes 3 px; cards 18 px (screen) / 6 px (paper).

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | `reveals` (a tape popping on, an insert card landing), `list_cue` (the STEP tape: one soft cue file for every step's tape, the one allowed repeat), `cta` (the CTA tape). The hook and every cut are silent: hidden cuts must stay hidden |
| **Meme cues** | Off (comedy off) |
| **Music bed** | On; enters on the first word of the promise line (after the hook); the pack's calm palette; ducked |
| **Ducking** | The bed sits 20 dB under the voice while the voice speaks. The overhead clips' own process sound (pen scratch, pour, sizzle) is kept when clean, ≥ 18 dB under the voice. F-B room tone is kept and ducked under the speaker |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

SFX cap: 3 per 10 s (`budgets.sfx_per_10s`); palette by `tone.energy: calm`.

---

## §12 Footage, shot list, fallbacks, inserts `[REQ]`

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's actual setups]`
| ID | Setup | Spec |
|---|---|---|
| **A** | Desk A-roll | Seated, chest-up, a 50-85 mm look at f/1.8-2.8 (background soft), warm practical lamps 2700-3200 K, a lined background (shelves of books, tools, jars, plants), a dark top. Vertical 9:16, 4K preferred. Head top y 220-360 |
| **B** | Overhead | Camera straight down (90°) over a **dark, deep-coloured or patterned surface**; vertical 9:16, 1080 × 1920 minimum (4K vertical for P-MACRO-PUNCH 1.35×); soft side light; hands enter from the bottom edge; the object inside y 200-1250 |
| **C** | Desk insert | The desk camera lowered close: the object held up or set at 30-45°, background to black, a manual focus pull if possible |
| **D** | Podcast | One camera per speaker (tight single, eyes ≈ y 600 in the 9:16 crop), a mic entering from the side, warm practicals behind; or one 4K wide of both |

### 12.2 Shot list
| ID | Shot | Spec | Count per 60 s | Must | Formats |
|---|---|---|---|---|---|
| **SH-1** | Overhead hand demo | Setup B; each step filmed start to finish in 3-12 s clips, **twice** (a wide pass and a close pass), plus 3 s of each step's finished state; hands moving in and out of frame at both ends of each clip (the cut points) | 6-12 clips | must | F-A |
| **SH-2** | Finished result | 3-6 s: hands turning, opening, lifting or presenting the finished result; overhead or angled | 1-2 | must | F-A |
| **SH-3** | Desk take | Setup A, the whole script, one or a few takes | 1 | must | F-A |
| **SH-4** | Desk inserts | Setup C, 2-4 s each: the result at an angle, a detail held up, each step's piece held up (for the recap) | 1-3 (+ 1 per step) | optional | F-A |
| **SH-5** | Podcast cameras | Setup D, synced (a clap or shared audio), one per speaker, or one 4K wide | 1 set | must | F-B |
| **SH-6** | Listener reactions | 2-3 s nods, laughs, look-aways from the listener camera (part of SH-5) | 2-4 | optional | F-B |

### 12.3 Fallbacks
| ID | For | What the engine does | Fidelity cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | (a) No overhead rig: film with the desk camera tilted down 45-60° and run it as the plate. (b) Horizontal 16:9 overhead: P-PLATE-BAND. (c) Only phone photos of each step: P-STEP-STILL | (a) the top-down look is lost; (b) not full-bleed; (c) no motion and no hidden cuts | degraded |
| **FB-2** | SH-2 | The last overhead clip's final 3 s (the finished state) opens the reel, from the frame where the hand leaves | No presenting motion at f0 | holds |
| **FB-3** | SH-3 | None: without a desk take the creator never appears and the reel becomes a voice-over hand demo | Presence below 20%; no returns between steps | **no_fallback** (F-A needs a desk take) |
| **FB-4** | SH-4 | P-MACRO-PUNCH into the overhead clip instead of a desk insert; the recap uses each step's overhead finished state | No depth, no rack focus | holds |
| **FB-5** | SH-5 | One camera: two virtual crops of a 4K wide (one per speaker); a 1080p wide: a blurfill band per speaker | Softer image (up to 2× upsampling), or no full-bleed face | degraded |
| **FB-6** | SH-6 | No reactions: P-TALK-RECROP at each would-be reaction point | The conversation feels one-sided | holds |

Say at the checkpoint which fallbacks this reel uses (`fallback_used` per beat).

### 12.4 Props, reaction bank, matte, resolution
- **Props:** a dark patterned or deep-coloured work surface; the finished result ready to show; warm lamps in the desk background; each step's tools laid out before filming.
- **Reaction bank (F-B):** listener nod, laugh, look-away. F-A close: the creator's small smile to camera.
- **Matte:** none.
- **Resolution:** Z-2 (1.07) and P-MACRO-PUNCH (1.2-1.35) need ≥ 1296-1458 px wide; a 1080p vertical source allows ≤ 1.35× with visible softening (4K vertical preferred). F-B virtual crops need a 4K wide. Overhead clips must be **vertical** (`veos asset add` scales videos to 1080 px wide).

### 12.5 Third-party inserts: ask, then create `[REQ]`
1. `veos inserts scan` lists the moments (an app, a product, a site, a post, a person, a quote).
2. **Ask the creator once:** "For these N moments, do you have a clip or screenshot? (drop the files, or say no)".
3. Supplied: `veos asset add <file> --origin creator`; show it in P-SCREEN-INSERT (`fx.shot`) or P-PHOTO-PRINT, never altered.
4. Not supplied, Claude creates:

| Moment | Created substitute |
|---|---|
| An app or software screen | P-SCREEN-INSERT with `fx.appUI` (`recreated_ui`, generic) |
| A product or brand | P-PRODUCT-TAPE (`logo_plate`: the name in type on tape) |
| A post or quote read aloud | P-QUOTE-CARD (`quote_card`, verbatim) |
| A news headline | `fx.headlineCard` on W-desk, paper theme (`headline_card`) |
| A person | `fx.silhouette` on W-desk (`silhouette`) |
| Another creator's video | Said, not shown: caption only |

5. Record each moment in `plan/inserts.json`: `{id, moment, origin: "creator" | "created", file?, substitute_of?}`.

### 12.6 Frame rate and audio
30 fps CFR, 1080 × 1920, BT.709. One voice track (F-A: source A; F-B: `MIX`), high-pass 80 Hz, de-ess, light compression, −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core and conditional beat fields
Core (every beat): `id`, `section`, `t0`/`t1`, `spoken`, `trigger {word, at}`, `tone`, `line_type`, `layout`, `visual`, `layers`, `pattern`, `sfx`. Conditional fields used by this style:

| Switch / module | Fields |
|---|---|
| captions on | `caption {profile, emphasis[], overrides[]}` |
| footage ≥ medium | `shot_id`, `fallback_used` |
| overhead runs (F-A) | `segments [{asset, from, offset, crop?}]`, `cuts [{at, kind: T-01/T-02/T-03, out_frame, in_frame}]` |
| dialogue (F-B) | `speaker`, `angle`, `crop`, `cut_reason` (open / handover / reaction / recrop) |
| third-party moment | `insert {id, origin: creator \| created}` |
| declared exception | `exception: E6` (recap tape only) |

### 13.2 Beat sheet example (the first `yaml` block of the edit brief)
```yaml
- id: 7
  section: STEP-2                # HOOK | PROMISE | STEP-n | RECAP | CLOSE | CTA  (F-B: CLAIM | TURN | REFRAME | BUTTON)
  t0: 21.40
  t1: 24.10
  spoken: "Then I add my two habit trackers"
  trigger: {word: "Then", at: 21.43}
  tone: explain
  line_type: ordinal_action
  layout: L-overhead
  pattern: P-OVERHEAD-PLATE      # + P-STEP-TAPE on the first beat of each step
  layers: [grade, plate-s2, tape-s2]
  visual: "Overhead: hands rule the tracker grid on the blank page; STEP 2 tape pops on top centre"
  caption: {profile: CS-1, emphasis: ["trackers"], overrides: []}
  shot_id: SH-1
  fallback_used: null
  segments: [{asset: oh-2-1, from: 0.0, offset: 0.40}, {asset: oh-2-2, from: 1.57, offset: 0.53}]
  cuts: [{at: 22.97, kind: T-02, out_frame: "oh-2-1 @ 1.97", in_frame: "oh-2-2 @ 0.53"}]
  sfx: [{id: "<catalogue id>", t: 21.43, on: "tape-s2@0", why: "list cue: STEP 2"}]
  insert: null
  exception: null
```

### 13.3 Reel header (top of the edit brief)
```yaml
reel:
  format: F-A                    # F-A | F-B
  theme: null
  hook_archetype: HA-14          # HA-14 | HA-10 | HA-16
  structure: tutorial            # tutorial | conversation
  count: 5                       # steps (F-A); null (F-B)
  keyword: null                  # {{BV-08.keyword|KEYWORD}} when a CTA device uses one
  grade: GR-tungsten             # GR-tungsten | GR-tungsten-soft
  cast: null                     # F-B: {S1: {name, role: host}, S2: {name, role: guest}}
  fallbacks_used: []             # e.g. [FB-4]
```
`timeline.meta.hook_archetype` and `timeline.meta.format` carry the same values for the validator.

Scene naming: `plate-<section>` (one per overhead run, `kind: "broll"`, `segments`, `cuts`), `tape-<section>` (z6, `in: "none"`, `events: [0.27]`, `text_class: "TC-label"`), `recap-plate`, `recap-tape` (`exception: "E6"`, `data-slot` on the container), `tt-<n>` (tool/measure/wait tapes, z5), `ins-<n>` (inserts, z3).

### 13.4 Hook proposals (3 required)
```yaml
- name: "Result in hand: the finished cup"
  archetype: HA-14
  opening_line: "This is my morning ritual."          # first captions; gold on "ritual"
  hook_pair: {first_subject: "finished pour-over set down, still swirling", reveal: "the pour (2 angles) + desk promise 'four steps'"}
  shots: [res-1 @ 0.40, oh-4-2 @ 2.10, ins-1 @ 1.20, desk @ 31.2]
  hidden_cuts_0_3s: [1.43 T-02, 2.70 T-03]
  captions: {profile: CS-1, gold: ["ritual", "water", "day"]}
  storyboard: "f0 cup set down (motion) | 0.07 'This is my' | 0.9 gold 'ritual' | 1.43 hand pass → pour | 2.70 flip → angled cup | 5.6 desk 'four steps'"
  sound: "dry hook; bed from the promise"
  stopper_test: {thumbnail: pass, mute: pass, payoff_s: 0.9, changes_3s: 4.5}
```

### 13.5 Checkpoint (before building)
1. The 3 hook proposals with stopper tests.
2. The beat sheet with tones, the plate segment list per step (asset, in, out) and every hidden-cut frame pair.
3. The transition map (a T-id per cut) and the SFX ledger.
4. The count check: spoken steps = tapes = recap entries.
5. The grade choice (GR-tungsten / soft) with one before/after still.
6. The inserts record (creator vs created) and the fallbacks used.
7. Style stills: f0, 1.0 s (gold word), one STEP tape frame, one desk return, one recap frame, the last frame. F-B: f0, the first handover, one reaction, the last frame.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE]`
Times are estimates; replace them with `words.edit.json` onsets. The editor rewrites these for the buyer's niche after their first approved reel of each format (Part D.6).

### 14.1 F-A, food: "My 4-step morning pour-over" (≈ 62 s)
[NICHE: example] Shots: the desk take (SH-3); overhead clips of grinding, rinsing the filter, the bloom and the spiral pour (SH-1, 9 clips); the finished cup set down and lifted (SH-2); the cup at an angle and the spent filter held up (SH-4).

**Hook table**
| t (s) | Spoken | Tone | Picture | Caption (gold) | Cut / camera |
|---|---|---|---|---|---|
| f0 | — | awe | P-RESULT-OPEN: overhead, the cup being set down on dark walnut, the coffee still swirling | — | — |
| 0.07 | "This is my morning ritual." | awe | same plate, sharp by 0.9 s | "This is my morning **ritual**." | — |
| 1.43 | "Same beans, same water…" | awe | T-02 on the hand lifting away → overhead pour close (spout, spiral) | "Same beans, same **water**," | T-02 |
| 2.70 | "…same cup every day." | awe | T-03 on the cup turning → P-ANGLED-HERO: the cup at 35°, steam, background black | "same cup every **day**." | T-03; in-plate push 1.00 → 1.04 |
| 4.20 | "And it takes four minutes." | win | P-HELD-TO-CAMERA: the spent filter held up, P-RACK-IN | "it takes four **minutes**." | T-04 |
| 5.60 | "Here's exactly how I make it, in four steps." | explain | G-2 L-desk: the creator seated, kettle in shot | "in four **steps**." | T-01; Z-1 |
| 8.10 | "First, grind your beans…" | explain | G-1 L-overhead + STEP 1 tape | "First, **grind** your beans" | T-01 |

**Section plan**
| Section | t (s) | Patterns |
|---|---|---|
| STEP 1 Grind | 8.1-17.5 | P-OVERHEAD-PLATE (beans into the grinder → grounds tapped out, 3 segments, T-02 ×2); gold "**grind**" on "First, grind your beans"; P-MEASURE-TAPE `18 G · 0.6 OZ` on "eighteen grams" at 10.9-13.4 (after the STEP tape exits at 10.6); P-STATE-JUMP to the grounds in the dripper; G-2 desk "medium-fine, like sea salt" (Z-1) |
| STEP 2 Rinse | 17.5-24.0 | STEP 2 tape; overhead: the filter in, hot-water rinse, water dumped (T-03 on the tilt); gold "**paper**" on "rinse the paper taste out"; no desk return (step < 7 s) |
| STEP 3 Bloom | 24.0-36.0 | STEP 3 tape; overhead pour of 40 g, the bed swelling; P-MACRO-PUNCH 1.25× on the bubbles ("see the gas escaping"); P-WAIT-TAPE `WAIT 30 SEC` on the P-STATE-JUMP; desk "fresh beans bloom more" (Z-2 on a jump cut); **re-hook** at ≈ 35 s: P-RESULT-FLASH of the finished cup 1.0 s, gold "**cup**" |
| STEP 4 Spiral pour | 36.0-49.0 | STEP 4 tape; the most satisfying visual: the slow spiral pour, 3 angles joined with T-02; P-MEASURE-TAPE `250 G · 8.8 OZ`; P-STATE-JUMP to the drained flat bed; desk "a flat bed means an even extraction" |
| RECAP | 49.0-56.4 | Desk "So: grind, rinse, bloom, pour." → one overhead shot moving across the set-out pieces: grounds (STEP 1), wet filter (STEP 2), bloom (STEP 3), the cup (STEP 4), ≈ 1.6 s each; the tape counts on each spoken ordinal (E6); "your **grind**," "your **rinse**," "your **bloom**," "your **pour**." |
| CLOSE | 56.4-61.8 | P-ANGLED-HERO → P-END-ON-RESULT: the hand lifts the cup out of frame; "…and that's my morning." T-07 |

### 14.2 F-A, craft: "A leather card holder in 5 steps" (≈ 74 s)
[NICHE: example] Shots: the desk take; overhead of cutting, marking, punching, stitching and burnishing (SH-1, 12 clips, 4K vertical); the finished holder with cards slid in (SH-2); each step's piece held up (SH-4, for the recap).

**Hook table**
| t (s) | Spoken | Tone | Picture | Caption (gold) | Cut |
|---|---|---|---|---|---|
| f0 | — | awe | P-RESULT-OPEN: hands sliding two cards into the finished holder on dark slate | — | — |
| 0.05 | "This is the last wallet I'll ever buy…" | awe | same | "This is the last **wallet**" | — |
| 1.38 | "…because I made it." | win | T-02 → overhead close of the saddle stitch along the edge | "because I **made** it." | T-02 |
| 2.75 | "One piece of leather." | explain | T-03 (the holder flipped) → P-HELD-TO-CAMERA: the flat cut piece, P-RACK-IN | "One piece of **leather**." | T-03 + T-04 |
| 4.30 | "No sewing machine." | explain | overhead: two needles crossing through one hole | "No sewing **machine**." | T-02 |
| 5.80 | "Five steps, one evening. Let's go." | explain | G-2 desk, the holder in hand (P-DESK-SHOW) | "Five **steps**," | T-01 |

**Section plan**
| Section | t (s) | Patterns |
|---|---|---|
| STEP 1 Cut | 8.0-20.0 | STEP 1; overhead: template on the leather, the knife along the ruler (2 segments, T-02); P-TOOL-TAPE `ROTARY CUTTER`; P-STATE-JUMP to the cut piece; desk "always cut away from your fingers" (`warn`, gold "**away**", Z-2) |
| STEP 2 Mark | 20.0-28.0 | STEP 2; overhead: the wing divider tracing the stitch line; P-MEASURE-TAPE `3 MM · 1/8 IN`; P-MACRO-PUNCH 1.3× on the line |
| STEP 3 Punch | 28.0-38.5 | STEP 3; overhead: pricking iron and mallet (T-02 on the mallet swing); gold "**holes**"; **re-hook** at ≈ 35 s: P-RESULT-FLASH of the finished holder 1.0 s |
| STEP 4 Stitch | 38.5-54.0 | STEP 4; the most satisfying visual: the saddle stitch pulled tight, 4 segments (two angles, a P-STATE-JUMP from 2 holes to the whole edge); P-TOOL-TAPE `WAXED THREAD`; desk "two needles, one thread" (Z-1) |
| STEP 5 Burnish | 54.0-61.5 | STEP 5; overhead: the edge sanded and burnished; P-HELD-TO-CAMERA of the glossy edge (T-04) |
| RECAP | 61.5-70.0 | One overhead shot, the hands turning the holder to each detail, ≈ 1.6 s each; the tape counts STEP 1-5 (E6); "your **cut**," "your **line**," "your **holes**," "your **stitch**," "your **edge**." |
| CLOSE | 70.0-74.0 | Desk: cards slid in, the holder into a pocket; "…and it'll outlive me." T-07 |

### 14.3 F-B, podcast clip: "Most home bread fails in the oven" (≈ 46 s)
[NICHE: example] Two cameras (host and a baker guest); `veos sync`; `veos speakers --names "S1=Host:host,S2=Maya:guest"`; `veos shots plan --no-stack`.

**Hook table**
| t (s) | Speaker | Spoken | Picture | Caption (gold; colour) | Cut |
|---|---|---|---|---|---|
| f0 | guest | (mid-sentence) "…the thing that ruins most home bread isn't the flour," | P-COLD-OPEN: guest single, mouth moving | "the thing that ruins" → "most home **bread**" (cream) | — |
| 2.10 | guest | "it's the oven." | same | "it's the **oven**." (cream) | — |
| 3.20 | host | "Really? Not the starter?" | P-SPEAKER-CUT → host single | "Really? Not the **starter**?" (white) | T-05 |
| 4.60 | guest | "Your oven lies to you…" | P-SPEAKER-CUT → guest | "Your oven **lies** to you" (cream) | T-05 |

**Section plan**
| Section | t (s) | Patterns |
|---|---|---|
| CLAIM | 0-4.6 | P-COLD-OPEN, P-SPEAKER-CUT; P-NAME-TAPE `MAYA · BAKER` 2.0 s from 0.4 s (the guest's first shot) |
| TURN | 4.6-18.0 | The guest's thermometer story: P-TALK-RECROP at 9.8 (sentence boundary); P-REACTION-CUTAWAY host nod 12.4-14.0; gold "**thermometer**", then "**fifty**" (degrees off) |
| REFRAME | 18.0-38.0 | Handover cuts every 3-5 s; host: "so what do you do?"; guest: "preheat an hour, steam for the first twenty minutes"; gold "**steam**"; reaction 31.0-32.6 |
| BUTTON | 38.0-46.0 | Host: "I've been blaming my starter for two years." The guest laughs (P-BUTTON-END, guest single 1.6 s); T-07 |

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] The format is declared; F-A presence 20-50% and absence ≤ 30 s; F-B ≥ 95% (V-PRESENCE).
- [ ] Duration in class: F-A 55-90 s, F-B 35-60 s (review).
- [ ] Layout shares within §3.2 (V-LAYOUT).

**2. Hook**
- [ ] f0 = a moving result in the hands (F-A) / a mid-sentence speaker (F-B); the first caption by 0.10 s (V-F0).
- [ ] The result sharp and inside y 200-1250 by 1.0 s; the first gold word by 1.5 s (review).
- [ ] ≥ 4 (F-A) / ≥ 2 (F-B) weighted SCs in 0-3 s; F-A has two hidden cuts by 3 s (V-CADENCE).
- [ ] No headline, emoji or title anywhere (review).

**3. Body and cadence**
- [ ] 3-8 / 2.5-7 SC per 10 s; max gap 5.0 / 6.0 s; 14-26 cuts per minute; median shot in range (V-CADENCE).
- [ ] Every step: G-1 on the ordinal ±2 f, the STEP tape at its first frame, hold 2.0-3.5 s, the overhead demo of every spoken action (V-ONWORD, review).
- [ ] Step count = tapes = recap entries (V-PROMISE, review).
- [ ] ≥ 60% of overhead cuts hidden in motion; no two identical framings back to back except state jumps (review).
- [ ] One re-hook (P-RESULT-FLASH) in F-A at 40-60% of runtime (review).
- [ ] Every tape pops on with a cut and off with the next cut; T-08 ≤ 2 and never in the hook (review).

**4. Captions**
- [ ] CS-1 / CS-2 / CS-3 as declared; 56 / 76 / 56 px; cy 1440 / 1385; word reveal; ≤ 2 lines (V-CAPTION, V-TYPE).
- [ ] ≤ 1 gold word per chunk and per 4 s; gold on nouns, key verbs, names; never on stop-words (V-CAPTION).
- [ ] The caption band over a dark surface; contrast ≥ 4.5:1 as measured (V-TYPE).
- [ ] F-B: host white, guest cream; one speaker per chunk (V-SPEAKER SPK-2).
- [ ] Every tool, ingredient and brand spelled exactly (V-CAPTION glossary).

**5. Modules**
- [ ] F-B (§20): a cut within ±3 f of every handover; reactions 1.0-2.6 s, never across a handover; no stack; holds ≤ 6 s (V-SPEAKER).

**6. Truth and inserts**
- [ ] Every number on a tape was spoken and follows SW-08 (V-NUMFMT).
- [ ] Every third-party moment is creator-supplied or created (V-INSERTS).
- [ ] Personal data blurred (NC-14, review).

**7. Look**
- [ ] One grade on every footage frame and plate (`grades.footage` + `ctx.grade` on every plate scene); tapes and captions ungraded (review).
- [ ] ≤ 2 text elements and ≤ 1 tape at any frame; never a tape over a face (G2, V-FACE).
- [ ] No synthetic transition except ≤ 2 T-08 flashes; no shakes or visible zooms (V-CAMERA, review).

**8. Sound contract**
- [ ] Cues only on tapes, insert landings and the CTA; the hook silent; ≤ 3 per 10 s; ledger clean (S1-S6).
- [ ] The bed from the promise line, 20 dB under the voice; −14 LUFS, TP ≤ −1.5 dBTP (review).

**9. End and export**
- [ ] The last frame shows the result (F-A) or a reaction or reply (F-B); hard end ≤ 6 f after the last word; no black tail (review).
- [ ] The CTA tape (when a device is chosen) holds ≥ 1.5 s with the keyword (V-PROMISE).
- [ ] 1080 × 1920, 30 fps CFR.

---

## §16 Frame template / chrome
OFF (`profile.modules.chrome = false`): nothing persists; the STEP tape lives per step.

## §17 Running state and anchored graphics
OFF (`profile.modules.running_state = false`, `profile.modules.anchors = false`): no counters or totals; tapes are placed statically beside the object (§3.5 tape zone), not tracked.

## §18 Data contract
OFF (`profile.modules.data_figures = false`): numbers appear only as spoken quantities on tapes (H9, N10).

## §19 Evidence and citations
OFF (`profile.modules.citations = false`). The always-on inserts flow is §12.5.

## §20 Dialogue (multi-speaker) `[COND: modules.dialogue, F-B] [DNA]`
- **Cast:**
  | ID | Role | Caption style | Preferred angle |
  |---|---|---|---|
  | `host` | host (usually {{BV-01.name|the creator}}) | CS-2, `paper` white, upright | the host's single camera |
  | `guest` | guest | CS-2, `cream` `#EFE4CC`, upright | the guest's single camera |
- **Angle map:** `veos angles` assigns each camera to a speaker; faux angles `<src>:<speaker>` from a 4K wide when there is one camera (FB-5). Framing: face height 17% of the frame, face centre at 36% from the top, ≤ 2.0× upsampling.
- **Layouts:** `full` singles only (L-speaker). **No stack, no two-shot split** (`dialogue.stack = false`, `shots plan --no-stack`); a two-shot wide appears only as a 1.0-2.0 s establishing cut when both laugh (blurfill if it can't be cropped).
- **Cut grammar** (`dialogue.cut_rules`): cut on the new speaker's first word (1 f lead, ±3 f); opener 3.0-5.2 s on the first speaker; max hold 5.0 s (+1 s tolerance); reactions 1.0-2.6 s; re-crop step 1.15; minimum shot 0.8 s; a back-channel ≤ 1.6 s does not take the floor; never cut inside a word.
- **Captions:** speaker colours as the cast table; one speaker per chunk; overlapping speech shows only the dominant speaker.
- **Single-camera fallback:** FB-5.
- **Validator:** V-SPEAKER (SPK-1 labels ≥ 95%, SPK-2 distinct styles, SPK-3 handover cuts, SPK-4 speaker on screen, SPK-5 no cut inside a word, SPK-6 holds).

## §21 Canvas camera
OFF (`profile.modules.canvas_camera = false`): there is no graphics world to travel.

## §22 Ink and annotation layer
OFF (`profile.modules.ink = false`): the style never draws on the footage; the hands point.

## §23 Continuity
OFF (`profile.modules.continuity = false`): continuity comes from match-action cuts (R-4), not morphs.

## §24 Series furniture
OFF (`profile.modules.series = false`, VAR): a buyer may switch it on; the series tag then uses the tape recipe (TX-2) at x 64, top 165, only in the hook, never with a STEP tape.

## §25 Sponsor, brand and end cards
OFF (`profile.modules.brand = false`; `cta.devices` has no `end_card` / `product_card`). A sponsored reel needs the brand module switched on (VAR) and the NC-12 disclosure: a TC-legal "Paid partnership" line for ≥ 2 s.

---

## Part C. Exceptions and the non-overridable core

### C.1 Non-overridable core
NC-1…NC-14 apply unchanged (STYLE-PLAYBOOK-STRUCTURE Part C.1). The ones this style touches most:
- **NC-1** the face is never covered: tapes stay off L-desk (H6).
- **NC-4** legibility: captions 56/76 px, tapes ≥ 40 px, contrast ≥ 4.5:1 over the surface (H15).
- **NC-5** IG bands: the measured v01 caption block (cy ≈ 1565, bottom ≈ 1645) is lifted to cy 1440 so it ends at y 1500.
- **NC-6** truth: tapes repeat only spoken numbers.
- **NC-7** creator-owned media: every step's footage is the creator's; no fetched product shots.
- **NC-8** audio; **NC-9** determinism (plates read frames with `ctx.videoFrame`); **NC-14** redaction on screen recordings.

### C.2 Declared exceptions (this style)
| ID | Limits | Where |
|---|---|---|
| **E6** Hard swap | Recap tape only: one `data-slot` container, rect constant ±4 px, text swaps on the picture-cut frames, eased first entry and final exit | §2.2, `tokens.exceptions.E6`, scene `recap-tape` |

E1-E5 are not used. A buyer may switch E6 off (VAR): the recap then uses one tape scene per entry with a 4 f fade between them.

---

## Part D. Personalisation

### D.1 What the buyer is asked (one round, each with "keep the template default")
| ID | Question | Lands on | Default |
|---|---|---|---|
| BV-01 | Your name and handle | `creator.name`, `creator.handle`, the F-B host | {{BV-01.name|the creator}} / {{BV-01.handle|@yourhandle}} |
| BV-02 | One or two brand colours | `roles.primary` (the gold word) and `roles.accent` (the tape, nudged to a dark tape colour) | {{BV-02.primary|#D9A441}} / {{BV-02.accent|#0B0B0B}} |
| BV-05 | The language you speak and the caption language | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) | en}} → {{BV-05.captions | en}} |
| BV-08 | Your call to action | `profile.cta.chosen` + keyword | {{BV-08.device|none}} / {{BV-08.keyword|KEYWORD}} |

Defaulted, changeable later: fonts within their class (BV-03), niche (BV-04, inferred per reel), numbers (BV-06, from the language), formats enabled (BV-09: both), series (BV-13: off), sponsor wording (BV-14), never-on-screen list (BV-15), logo files (BV-16), duration target (BV-17: F-A 55-90 s).

### D.2 Lock map for this template
| Area | Lock | Range (TUNE) |
|---|---|---|
| Gold word colour (`roles.primary`) | VAR | any; contrast-nudged against the footage shadow |
| Tape colour (`roles.accent`) | TUNE | dark tape colour, OKLCH L ≤ 0.35 |
| Caption size CS-1 / CS-2 | TUNE | 56-66 / 62-74 px |
| Caption y CS-1 / CS-2 | TUNE | 1400-1460 / 1340-1420 |
| Gold ratio / frequency | TUNE | 1.15-1.4× / 0.20-0.33 per s |
| Emphasis mechanism (font swap) | DNA | — |
| Fonts | TUNE | class lists in §5.1 |
| Grade warmth / saturation / contrast / vignette | TUNE | 0.08-0.26 / 0.80-1.00 / 1.00-1.15 / 0.20-0.50 |
| Cadence numbers, motion tokens | TUNE | ±15% |
| STEP tape size / top | TUNE | 40-52 px / 150-240 |
| Presence share | TUNE | ±10 points |
| Duration class | TUNE | short / standard / long |
| Energy | TUNE | calm / balanced |
| Comedy | TUNE | off only |
| Source type, spine, graphics role, captions mode and role, footage dependency, themes policy, the format set, CTA device set | DNA | — |
| CTA device chosen, keyword, language, numbers, series, brand, sound contract | VAR | — |
| §6.4 hook pairs, §8.4 NICHE rows, §14, App. A | NICHE | appended per reel |

### D.3 Typical tweaks and how they classify
| Buyer says | Classification |
|---|---|
| "Make the gold word my brand teal" | VAR (BV-02 primary) |
| "Bigger captions" (to 64 px) | TUNE in range |
| "Captions at 80 px" | out of range → DNA deviation, confirm |
| "Add a yellow banner on top" | DNA deviation (H4, N1): warn that it leaves the style; record DV-n if confirmed |
| "Use crossfades between steps" | DNA deviation (N2) |
| "Warmer grade" | TUNE (warmth ≤ 0.26) |
| "No recap" | DNA deviation (D6) |
| "Turn the series tag on" | VAR (§24) |

### D.4 Lineage, upgrades, niche slots
As STYLE-PLAYBOOK-STRUCTURE Part D.4-D.6: lineage in `tokens.json → lineage`; DNA deviations are `DV-n` (3 or more makes the copy `derived`); NICHE rows (§6.4, §8.4, §14, App. A, the glossary) are appended per reel from the transcript.

---

## Part E. Changes from the architects' decision (STYLE-COVERAGE row 18) and from the analysis

| Item | Coverage / analysis | This template | Why (evidence) |
|---|---|---|---|
| F-A default hook | HA-01 (physical result) | **HA-14** "Result in hand"; HA-10 and HA-16 alternates | The engine's HA-01 needs a headline and the presenter's face at f0; v01 @0:00 has neither (hands + result + caption). The result-first content is kept as the hook pair |
| Exceptions | none | **E6** for the recap tape only | v01 @1:31-1:43: the tape label swaps on each hard cut |
| Hook SC (F-B) | 4 | **2** | v02 0-3 s has no cut (first at 5.03) and four caption swaps (4 × 0.5) |
| Caption y | 71-81% | **cy 1440 (F-A), 1385 (F-B)** | audit: v01 block cy ≈ 1565 sits in the NC-5 band (lifted to the lowest compliant spot); v02 cy ≈ 1385 kept |
| Caption size | ~62 px | **56 px (F-A), 76 px (F-B)** | audit at 1080 × 1920: v01 52-57 px (the earlier 46 px read came from 300 px sheets), v02 ≈ 76-80 px |
| F-B speakers | (white both) | host white, guest **cream** | V-SPEAKER SPK-2 needs two distinct styles; cream reads as white |
| Duration F-A | std-long 47-110 | **standard 55-90 s** | 110 s exceeds the short-form sweet spot; `long` stays a TUNE step |
| Grade | DNA | DNA, **built in**: `grades.footage` on the stage, `ctx.grade` on plates (P-GRADE-PASS) | E-16 now applies `grades.footage` (vignette, bloom); core leaves video assets natural, so plates grade themselves |
| Patterns | graphics `minimal` (5-12) | 35 patterns, 12 of them graphic | The brief requires 20-60; the extra patterns are cut, stage and footage patterns, which carry this style |
| Tool / measure / wait / name tapes | not observed | inferred extensions of the STEP tape | Hands-on niches name tools and quantities; the tape is the style's only label device |
| Tape motion | feed 6 f + typed letters, fade out | **pops on with a cut, off with the next cut** | completeness audit, all 6 tape appearances in v01 |
| Recap | hard cuts between held-up pieces, 1.2-2.0 s | **one continuous flip-through, tape counts on the spoken ordinal** | v01 91.1-104.2 |
| Transitions | cuts only, flash banned | cuts + **T-08 white flash ≤ 2 per reel** | v01 34.57, 37.57 |
| Desk camera | Z-2 snap-punch 1.18 alternating | plain jump cuts; re-crop 1.07 rarely; drift 1.03 | v01 60.9, 80.8, 89.7, 90.2, 107.8; 57.0-66.9 |

---

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D / BD | D1-D8 / BD… (buyer) |
| H / N / BN | H1-H17 / N1-N10 / BN… |
| NC / E | NC-1…NC-14 / E6 |
| W / L / G | W-footage, W-desk / L-desk, L-overhead, L-insert, L-speaker / G-1…G-4 |
| GR | GR-tungsten, GR-tungsten-soft |
| CS | CS-1, CS-2, CS-3 |
| TX | TX-1…TX-7 |
| HA / ST | HA-14 (default both), HA-10, HA-16 / ST-1, ST-2, ST-3, ST-5, ST-6 |
| SM | SM-TAPE |
| P | P-KEYWORD-SWAP, P-STEP-TAPE, P-RECAP-STRIP, P-TOOL-TAPE, P-MEASURE-TAPE, P-WAIT-TAPE, P-NAME-TAPE, P-CTA-TAPE, P-OVERHEAD-PLATE, P-RESULT-OPEN, P-HAND-SWIPE-CUT, P-FLIP-CUT, P-HELD-TO-CAMERA, P-ANGLED-HERO, P-DESK-TALK, P-DESK-SHOW, P-MACRO-PUNCH, P-STATE-JUMP, P-RESULT-FLASH, P-RACK-IN, P-SLOW-PUSH, P-JUMP-RECROP, P-GRADE-PASS, P-PLATE-BAND, P-STEP-STILL, P-COLD-OPEN, P-SPEAKER-CUT, P-REACTION-CUTAWAY, P-TALK-RECROP, P-BUTTON-END, P-SCREEN-INSERT, P-PHOTO-PRINT, P-PRODUCT-TAPE, P-QUOTE-CARD, P-FLASH-CUT, P-END-ON-RESULT (36) |
| B | B-1…B-8 |
| T / R | T-01…T-08 / R-1…R-9 |
| Z | Z-0, Z-1, Z-2 |
| SH / FB | SH-1…SH-6 / FB-1…FB-6 |
| F | F-A, F-B |
| BV | BV-01, BV-02, BV-05, BV-08 (asked); BV-03, 04, 06, 09, 13-17 (defaulted) |
| V | V-PROFILE, V-F0, V-CADENCE, V-ONWORD, V-SAFE, V-FACE, V-PRESENCE, V-CAPTION, V-TYPE, V-EXC, V-HUES, V-LAYOUT, V-CAMERA, V-PROMISE, V-INSERTS, V-CITE, V-NUMFMT, V-SPEAKER |

---

## App. A Hook and title bank `[NICHE]`
Opening lines (they become the first captions; **bold** = the gold word) and post titles. Fill the `[slots]` per reel.

**F-A Step demo**
| # | Opening line | Post title | Archetype |
|---|---|---|---|
| 1 | "This is my [result] **[noun]**." | "My [result] in [N] steps" | HA-14 |
| 2 | "This is the last **[object]** I'll ever buy, because I made it." | "Make your own [object]" | HA-14 |
| 3 | "[N] steps. One **[evening / morning / hour]**." | "[Result], start to finish" | HA-14 |
| 4 | "Everyone gets the **[part]** wrong. Here's the fix." | "The [part] trick" | HA-10 |
| 5 | "I've made this **[thing]** every [day / week] for [N] years." | "My everyday [thing]" | HA-14 |
| 6 | (no words for 1 s: the pour / the stitch / the fold) "That's the **[moment]** you want." | "Chasing the perfect [moment]" | HA-16 |
| 7 | "You don't need a **[expensive tool]** for this." | "[Result] without a [tool]" | HA-10 |
| 8 | "This is how I **[verb]** every single [object]." | "How I [verb] my [object]" | HA-14 |
| 9 | "[Result] in [N] minutes, no **[shortcut]**." | "[N]-minute [result]" | HA-14 |
| 10 | "If your [thing] looks like this, you skipped the **[step]**." | "The step everyone skips" | HA-10 |

[NICHE: example] food: "This is my morning **ritual**." / "Four steps. One **kettle**." — craft: "This is the last **wallet** I'll ever buy." — photography: "Load **film** without wasting a frame."

**F-B Podcast clip**
| # | Opening line (cut in mid-sentence) | Post title | Archetype |
|---|---|---|---|
| 1 | "…the thing that ruins most **[craft]** isn't the [obvious thing]," | "It's not the [obvious thing]" | HA-14 |
| 2 | "…if, like, **[action]** is what separates a [pro] from a [hobbyist]." | "[Pro] vs [hobbyist]" | HA-14 |
| 3 | "…nobody talks about the **[hidden cost]**." | "The hidden cost of [topic]" | HA-14 |
| 4 | "…I stopped **[habit]** and everything got better." | "Why I stopped [habit]" | HA-14 |
| 5 | "…if [platform] disappeared tomorrow, where's your **[work]**?" | "Where's your [work]?" | HA-14 |
| 6 | (a laugh in progress) "…no, seriously, **[claim]**." | "[Claim], seriously" | HA-16 |
| 7 | "…the best **[tool]** is the one you [use daily]." | "The best [tool]" | HA-14 |
| 8 | "…you don't need more **[gear]**, you need [practice]." | "Not more [gear]" | HA-14 |
| 9 | "…I wasted [N] years on **[mistake]**." | "[N] years of [mistake]" | HA-14 |
| 10 | "…that's the moment it became a **[craft]**, not a [hobby]." | "When it became a [craft]" | HA-14 |

[NICHE: example] photography: "…if, like, **printing** photos is what makes you a photographer." — food: "…most home **bread** isn't ruined by the flour."

---

## App. B Evidence map `[DNA]`
The full source map, with timestamps and the list of unverified values, is in `evidence.md` (this template's folder). Key anchors:
| DNA element | Source |
|---|---|
| Gold italic serif keyword in a white grotesk subtitle, ≈ 1 per 4 s | v01 @0:01 "system", @0:03 "Track habits", @1:03 "sticky"; v02 @0:01.3 "printing", @0:04 "photographer" / "content" |
| Word-by-word caption reveal | v01 @0:00.17-0:00.83; v02 @0:00.17-0:01.0 |
| Overhead hand demo on a patterned rug ≈ 70% of v01 | v01 @0:08-0:37, @0:47-0:49, @1:07-1:29 |
| STEP N tape at y ≈ 212, ≈ 324 px wide, every step + recap | v01 @0:08, @0:38, @0:47, @1:07, @1:25, @1:31-1:43 |
| Tungsten grade, shallow depth of field, lined background | all frames, v01 and v02 |
| Cuts hidden in hand motion; speaker cuts on handover | v01 @0:00.1, @0:01.5, @0:34, @1:12; v02 cuts 5.03-46.13 |
| Hook: the result in hand, payoff by 1 s | v01 @0:00-0:08 |
| Cold open mid-sentence, first cut 5.03 s | v02 @0:00-0:05 |
| Cadence 23.5 / 19.0 cuts per minute, median shot 1.98 / 2.67 s (full-rate recount, desk jump cuts included) | completeness audit |
| Tapes pop on/off with cuts; recap flip-through; T-08 white flash; captions word fade 3 f | completeness audit (`docs/audit/cinematic-step-demo/completeness.md`) |

Unverified: the speech language beyond English (no transcript), the bed and process sound (not observable), the exact per-word fade length, the exact grade numbers (estimated from frames).
