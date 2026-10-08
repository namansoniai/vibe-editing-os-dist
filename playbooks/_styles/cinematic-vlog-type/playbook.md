# Cinematic Vlog Type Style Playbook (template v1)

**Purpose.** You (Claude) edit a short-form 9:16 reel for {{BV-01.name|the creator}} ({{BV-01.handle|@yourhandle}}) in the Cinematic Vlog Type style. The input is **narrated footage**: the creator's voice carries the reel (talking pieces filmed in several places, or a voice-over), and the picture is the creator's own cinematic footage (locations, details, staged scenes, drone or overhead shots, screen recordings), chosen sentence by sentence. Your job: pick and cut that footage at 27–51 cuts a minute, lay one hot yellow type layer over it (condensed yellow keyword blocks with thin white script connectors), run a pale-lemon serif subtitle along the bottom, drop examples onto a cream paper world, and close the reel on the exact frame it opened with.

**What makes it hard to copy by hand:** every keyword beat lands on its word within ±5 frames, the blocks slide in with a motion blur and are replaced a beat later, words sit behind the creator's head with a clean matte, and the cut rhythm never drops below one picture change every ~1.6 s. All of it is generated from `words.edit.json` + the beat sheet, so it is exact every time.

### Style DNA `[DNA]`
A cinematic location vlog with a magazine-poster type layer. The footage is always the star: golden-hour exteriors, a signature prop or car, store interiors, staged "characters", drone shots. Over it sits **one** hot yellow (`primary` {{BV-02.primary|#F7DE0B}}), in two voices: a condensed heavy block for the keyword and a thin white script for the words that connect them ("Is your **GIRLFRIEND** still **LOVING THE PICTURES** you got of her?"). A pale pale-lemon serif subtitle sits at y 1468 almost the whole time. Examples, recaps and app screens drop onto a cream paper world as rounded 9:16 cards or white-bordered polaroids, marked with hand-drawn yellow arrows and ovals. Staged personas get their own colour grade. The last frame is the first frame, so the reel loops.

**Copy these 5 things and it reads as this style:**
1. **Duo titles.** Keywords in a yellow condensed block (Anton 180–340 px, each line fitted to ≈ 880 px), connectors in white pen script (84–112 px), 1–2 block words per beat, each block rising ≈ 0.8 cap heights into place with a vertical smear in 4 f on its word and leaving upward a beat later (§5.2, P-DUO-TITLE).
2. **Pale-lemon serif subtitle** on ≥ 85% of the speech: EB Garamond 600, 54 px, pale lemon `#EEF272` with a hard dark drop shadow, sentence case, 3–6 words, centred at y 1468, hard swaps (§5.3, CS-1).
3. **Cinematic footage cut at 27–51 cuts/min**, warm-graded, with location changes, details and staged scenes; persona scenes carry GR-mono / GR-amber / GR-teal (§4.4, §7.6, §9.3, §12).
4. **The cream paper world**: 9:16 cards and polaroids on `#FCFBE6` / grid paper, spin-in cards, yellow ink annotations (§3.1, P-PAPER-CARD, P-POLAROID, §22).
5. **Depth and loop**: one keyword behind the head per 20–60 s (E1), and the bookend: the reel ends on its opening shot so the last frame equals frame 0 (§23; optional, on by default, `continuity.bookend` is a VAR, not DNA).

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Footage first, type serves it.** Never cover a great shot with a card; type goes in the sky, the wall, the empty top third | §3.5, §5.2, §12 |
| D2 | **One yellow.** `primary` is the only bright text colour. Keywords, counters, card titles, ink marks and the CTA keyword are yellow; nothing else is | §4 |
| D3 | **Script connects, block shouts.** Function words are white script; the keyword is always the yellow block. The script never carries the keyword | §5.2 |
| D4 | **The subtitle is always there.** Pale-lemon serif at y 1468 on every spoken line except while a duo title, an E2 burst or a morph is on screen | §5.3 |
| D5 | **A thesis, not a result.** The hook states a thesis or asks a question in 3–4 type beats over a moving cinematic shot; the full thesis is on screen by 3.0 s | §6.2 |
| D6 | **Cut like a vlog.** 27–51 cuts a minute, a picture change every 0.85–1.6 s, cuts on motion, one detail per listed noun | §7.6, §9.3 |
| D7 | **Paper for proof.** Examples, recaps, rules and app screens leave the footage world and sit on cream paper as cards or polaroids | §3.1, §8 |
| D8 | **Close the loop.** The last 1.0–1.5 s returns to the opening shot and ends on frame 0's picture | §23 |

Buyer directives `BD1…` `[VAR]` go here; they may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches) | ON |
| §1 | Procedure | ON |
| §2 | Hard rules, exceptions E1 + E2 | ON |
| §3 | Worlds, layouts, stage moves, safe zones | ON |
| §4 | Colour, grades | ON (themes OFF: single) |
| §5 | Type, duo titles, caption profile CS-1 | ON |
| §6 | Hook system (HA-12 default; HA-05 for F-B) | ON |
| §7 | Structure (story / tutorial) and cadence | ON |
| §8 | Visual system: 41 patterns | ON |
| §9 | Transitions and shot grammar | ON |
| §10 | Motion, camera (slow push only), layers, finishing | ON |
| §11 | Sound contract | ON (minimal) |
| §12 | Footage, shot list SH-1…SH-13, fallbacks, inserts | ON |
| §13 | Output contract | ON |
| §14 | Worked examples (3) | ON |
| §15 | QA | ON |
| §16 Chrome · §17 Running state · §18 Data · §19 Citations · §20 Dialogue · §21 Canvas camera | | OFF |
| §22 Ink · §23 Continuity · §24 Series · §25 Brand & end cards | | ON |
| Formats | F-A "Vlog / story" (default) · F-B "Tutorial with paper cards" | |

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile
  source_type: narrated_footage
  presenter: {presence: host, share: [45, 60], max_absence_s: 6}      # F-B: share [35, 55], max_absence_s 8
  spine: hybrid
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: support
  duration: {class: standard, target_s: [55, 85]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0}
  tone: {energy: balanced, comedy: light, comedy_max: light}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A, F-B], default: F-A}
  footage_dependency: high
  cta: {devices: [comment_keyword, link_bio, end_card, post_only], placement: end}
  modules: {chrome: false, running_state: false, anchors: false, data_figures: false, citations: false,
            dialogue: false, canvas_camera: false, ink: true, continuity: true, series: true, brand: true}
```

Why each switch has its value:
- **source_type: narrated_footage**, because the voice runs continuously while the picture changes to locations, details and staged scenes every ~1.2 s (v01, v02 @ 0:03–0:35). Talking pieces are part of the footage, not the spine.
- **presenter: host 45–60%**: the face is visible in roughly half the runtime, often small (mirror, overhead, persona scenes); B-roll runs of 3–6 s without a face are normal (v01 @ 0:22–0:25). F-B runs 35–55% with absences up to 8 s, because paper-card and device runs hold examples (v03 @ 0:20–0:27, v05 @ 0:30–0:54).
- **spine: hybrid**: talking pieces and footage alternate as equals; the audio decides the order (analysis gap G-A2).
- **captions: full / support / mute_safe**: the serif subtitle is on 85–92% of the runtime (65% in v02, which has more big titles), but the type layer and the picture are the strongest elements.
- **graphics: support**: type, paper cards and ink illustrate the speech; they never carry the argument alone. 10–18% of runtime is keyword titles, 0–29% paper cards.
- **duration: standard 55–85 s** (evidence 58–85 s, mean 77 s). One mid-reel re-hook (§7.4).
- **language** `(unverified)`: all five evidence reels are English. The template supports Hinglish and Hindi as buyer choices ({{BV-05.speech|en}} speech, {{BV-05.captions|en}} captions). On-screen type stays English Latin caps (Anton has no Devanagari; §5.5).
- **numbers: international** (counters "365", "52"); BV-06 switches to Indian grouping and ₹ when the buyer's language is Indian.
- **tone: balanced / light**: dry wit lives in staged personas and script asides; no meme SFX, no stickers.
- **themes: single**: one yellow across every reel. Persona colour comes from grades (§4.4), not theme packs.
- **formats**: F-A vlog/story (v01, v02, v04); F-B tutorial with paper cards (v03, v05). Shared DNA: the same type layer, subtitle, yellow, paper world and loop.
- **footage_dependency: high**: the look depends on footage the creator must shoot (§12). Readiness R4: without it, the §12.3 fallbacks apply and the card says so.
- **cta**: comment keyword (v02 @ 0:54), link in bio / end block (v03 @ 1:22), spoken only (v05 @ 1:09, v01 loops).
- **modules**: ink (yellow arrows, ovals and guide lines, v03), continuity (bookend loop, v01 @ 1:23 = @ 0:00; walk-in/walk-out, v04), series (lockup "ep. 06", v05 @ 0:09), brand (logo chip + disclosure, v05 @ 0:08, @ 0:57).

### 0.4 Formats `[DNA set; VAR enable]`
| Field | F-A "Vlog / story" (default) | F-B "Tutorial with paper cards" |
|---|---|---|
| `when` | A thesis told through places, staged personas or a personal journey: opinions, "N types of X", a visit, a year recap, a challenge | A how-to in 3–8 rules or steps: a technique, an app or tool walkthrough, a before/after fix |
| `profile` overrides | — | `presenter: {share: [35, 55], max_absence_s: 8}` |
| `layouts` | L-full, L-card916, L-hidden | L-full, L-card916, L-card43, L-hidden |
| `hooks.default` | HA-12 thesis typography | HA-05 title lockup (payoff ≤ 0.7 s) |
| `structure` | story · markers SM-1 "#N." | tutorial · markers SM-2 card-title chapters |
| `cadence` | cuts 27–51 /min, median shot 0.85–1.6 s | cuts 27–42 /min, median shot 0.9–1.6 s |
| Paper share | 0–30% | 20–45% |
| Shared DNA | one yellow · duo titles · pale-lemon serif subtitle at y 1468 · graded cinematic footage · cream paper world · bookend loop (optional, on by default) | same |

**Picking the format per reel:** the script names steps, rules, settings or "how to" → F-B. Anything else → F-A. Declare it in the reel header (§13.3). Never mix: an F-A reel may show one paper card run (≤ 30%), but never the F-B rule ritual.

### 0.5 Theme packs
OFF (`themes.policy: single`). One yellow for every reel; a buyer who brands it ({{BV-02.primary|#F7DE0B}}) changes it everywhere.

---

## §1 Procedure (follow in order) `[DNA]`

1. **P1 Inventory.** `ffprobe` every input. Sources are often 23.98/24/25 fps: conform everything to **30 fps CFR**. Register each file with its origin (`creator`, or `created` for what you build, §12.5).
2. **P1b B-roll bank tagging (narrated_footage).** Give every clip an id (`B01…`), tags (subject, place, action, mood: `walk`, `detail`, `hands`, `product`, `wide`, `overhead`, `persona:<name>`), its usable span and its motion direction (for cut-on-motion). Mark which shot is SH-1 (the opener) and check it has **≥ 1.5 s of pre-roll before its in-point** (needed by the bookend, §23). Mark talking pieces by setup (A/B/C/D, §12.1). Talking pieces (or the creator's voice-over file) carry the voice and become the cut map; every other clip is picture-only and plays as a scene over the voice (§12.6).
3. **P2 Matte.** Matte every talking piece and SH-11 headroom shot where a behind-head word (E1) or a poster backdrop (P-POSTER-BACKDROP) may land. Check hair edges at 200%. A take with a messy matte gets no E1 word (FB-11).
4. **P3 Transcribe** with word timestamps. Apply `language.captions.transform` ({{BV-05.captions|en}}); keep the speaker's ellipsis pauses: a pause of 0.35–0.9 s inside a sentence becomes ".." on the subtitle (v04 "I made a post.."). Apply the glossary and mask profanity (`inner` mask).
5. **P4 Rough cut and segment.** Write the EDL from the talking pieces (pauses tightened to ≤ 0.35 s except the ".." pauses) and run `veos cut`. Segment into the structure's units (§7.1): F-A `HOOK · SETUP · SCENE-n · TURN · PAYOFF · CTA · BOOKEND`; F-B `HOOK · CONTEXT · RULE-n · RESULT · CTA · BOOKEND`.
6. **P5 Classify** every sentence with a line type (§8.4) and its trigger word.
7. **P6 Tone-tag** every sentence: `hype` (thesis, claims), `awe` (cinematic reveals, places), `explain` (rules, steps), `warn` (problem state, a negative persona), `win` (result, payoff), `cta`.
8. **P7 Hook plan: the duo split (this style's craft).** Write the thesis in ≤ 12 words. Split it into **connectors** (function words: script) and **keywords** (content words: block), group the keywords into 3–4 beats of 1–2 words, and time each beat to its spoken word (§5.2, §6.2). Write **3 hook variants** with their archetype, run the stopper tests (§6.1).
9. **P8 Visual plan.**
   - **P8b Shot matching:** pick a creator clip for every sentence (the B-roll bank), one picture change every 0.85–1.6 s; listed nouns get one detail each (R-3). Where no clip fits, build a paper card, a polaroid or a created visual (§12.5).
   - A pattern per line (§8.4); decide which lines leave the footage world for the paper world.
   - Behind-head words: at most one per 20 s, only on matted takes with ≥ 300 px headroom (E1).
   - The grade plan (persona → GR id, §4.4) and the one chaos burst if a line is about overload (E2).
10. **P9 Beat sheet** (§13): one beat per trigger; meet §7.6.
11. **P10 Cue moments** (§11) and the transition map (§9).
12. **P11 Assets.** `veos asset add` every B-roll clip and every clip or photo that appears inside a card, polaroid, device or spin (they play through `fx.clip` / `ctx.videoFrame`, §12.6). Ask once for third-party moments (§12.5). Resolve fallbacks (§12.3) and list them.
13. **Module steps:** **anchor pass** for ink (§22: read sampled frames, write the x/y of every arrow tip and oval), **chain design** for the bookend (§23: SH-1's in-point, the pre-roll span, the final sentence that rides it), **series metadata** (§24: episode number), **sponsor check** (§25: logo file, disclosure line).
14. **P12 Checkpoint** (§13.5), then **wait for approval.**
15. **P13 Build:** act by act; `veos validate`; preview and QA (§15, at most 3 passes); render.

---

## §2 Hard rules `[DNA]`

### 2.1 Editing rules (every style)
The ten editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show the thing, not the word; say what was said; hook titles hook; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Picture first, in this style's own look:** every key beat shows the thing being said (an object, a screen or app, a diagram, numbers in motion), not just its word; text supports the picture and never replaces it. When the speaker points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. Illustrations may use made-up but realistic numbers and names ("212 views", "1.2M views"), with no label; a number or quote the speaker says is shown as said. This overrides any rule below that bans made-up numbers or asks for an example tag: those rules now cover claims (the creator's results, prices, benchmarks, testimonials), not illustrations.
- **Hook titles hook:** the on-screen title promises the viewer something (an outcome, a curiosity gap, who it's for) and is true to what the reel delivers; it need not repeat the spoken words. This playbook sets its shape (§5.2, §6.5: lines, sizes, word limits, case), never its voice (§6).
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| ID | Limits in this style (never looser than the registry) | DNA reason | Evidence |
|---|---|---|---|
| **E1** behind-subject type | `TC-display` only (an Anton block word 200–340 px, or a P-COUNT-UP number 280–400 px, `primary`); `behind: true` on a clean matte; visible glyph area ≥ 65% for the whole hold; first and last letters visible; ≤ 1 at a time; hold ≥ 0.6 s; ≤ 3 per 60 s; parallax drift 8–12 px against the head; never inside a GR-L grade span (§4.4) | The depth sandwich is how the style makes a word part of the shot | v02 @ 0:33 BEINGS, 0:38 BACK, 0:39 HOW, 0:40 SUPERPOWER, 0:53 GROW; v05 @ 0:07 EDITING |
| **E2** chaos burst | ≤ 1.5 s; **≤ 1 per reel** (stricter than the registry's 2); ≤ 6 text snippets; nothing in front of the face box; subtitles hidden; GR-mono footage under it; followed by ≥ 1.0 s with ≤ 2 elements; never in the hook's first 2 s, never in the CTA | Overload, self-doubt, "too many options" is shown, not said | v02 @ 0:04–0:08, 0:34–0:36 |

No other exception. Subtitles are 54 px (no E3), display text ≥ 40 px, no edge bleed (E5), no hard-swap slots (E6). A buyer may switch E1 or E2 off (stricter, VAR).

### 2.3 Style MUST rules
- **H1 Frame 0 moves.** f0 is a moving cinematic shot (live footage in motion, a walk-in, a drone move, or Z-1 push-drift starting at f0); in HA-12 the first type beat (a script connector or a block word) starts by **0.7 s**; in HA-05 the title lockup is readable by **0.7 s**. A static frame or a fade-in at f0 fails. `check: V-F0`
- **H2 Cadence.** Weighted state changes 5–12 per 10 s in the body; max gap between weight-1 changes **3.0 s**; nothing static > 2.5 s (footage counts as motion). Hook: ≥ 6 weighted changes in 0–3 s, no gap > 0.8 s. `check: V-CADENCE`
- **H3 Cut rhythm is DNA.** 27–51 cuts/min (F-B 27–42), median shot 0.85–1.6 s (F-B 0.9–1.6 s). Card swaps, carousel slides and spins count as cuts: declare them in `transitions` or scene `cuts`. `check: V-CADENCE`
- **H4 Thesis by 3.0 s.** HA-12: the whole thesis phrase has been on screen (all its beats) by 3.0 s; HA-05: the title by 0.7 s; HA-19: the premise word by 3.0 s; HA-08: the hero number by 1.7 s. `check: V-F0`
- **H5 Subtitle.** CS-1 runs on every spoken word outside duo-title, E2 and morph spans; 3–6 words, one line, ≤ 28 characters, y 1468, hard swaps; sync lead ≤ 0.15 s. `check: V-CAPTION`
- **H6 Behind-head words** follow E1 exactly (2.2). `check: V-EXC`
- **H7 The chaos burst** follows E2 exactly (2.2), and only on a line whose meaning is overload. `check: V-EXC` + review
- **H8 On the word.** Each block keyword starts 2 f before its spoken word and is fully landed within ±5 f; counters land on the number word; ink marks start on the word naming the thing. `check: V-ONWORD`
- **H9 Face.** Front-layer type keeps ≥ 40 px from the face box; a word that must overlap the head goes behind it (E1) or moves. `check: V-FACE`
- **H10 Presence.** Presenter visible 45–60% of runtime (F-B 35–55%; TUNE ±10); longest absence 6 s (F-B 8 s). `check: V-PRESENCE`
- **H11 Promise.** "N types / N rules / N steps" = N items shown with N markers; the thesis is paid off before the CTA; the CTA keyword is on screen ≥ 1.5 s. `check: V-PROMISE`
- **H12 Headline limits.** A duo title is ≤ 7 words total (script + block), ≤ 2 block lines, ≤ 3 block words per line; each beat reads in ≤ 1.2 s. A title lockup is ≤ 6 words, ≤ 2 lines. `check: V-TITLE`
- **H13 One yellow.** `primary` is the only bright text hue; ≤ 2 bright roles per frame (`primary` + `accent` on a poster). `check: V-HUES`
- **H14 Camera.** Only Z-1 push-drift, Z-2 slow-push and Z-3 reset (zoom policy `slow_push`); never a punch, crash, shake or rotation as a camera event (the one measured punch lives inside the T-12 zoom-through transition, §9.1). Never the same preset twice in a row. `check: V-CAMERA`
- **H15 Bookend.** The last 1.0–1.5 s plays SH-1 (or its fallback) so that the **final frame's picture equals frame 0's picture**; no type is fully visible on either frame. `check: V-CONTINUITY` (pending: review)
- **H16 Inserts.** Third-party material (other people's posts, artworks, app UIs, logos) appears only from the creator's files; otherwise a created card. `check: V-INSERTS`
- **H17 Dead air (hybrid).** In talking pieces ≤ 1 gap ≥ 200 ms per 15 s; a deliberate pause ≤ 0.9 s is allowed only where the subtitle shows ".." and the picture keeps moving (a B-roll cut or a camera drift). `check: review`
- **H18 Truth.** Every number on screen (counters, "#3", "52 weeks") is spoken or in the script; app screens are the creator's recordings or generic recreations. `check: V-NUMFMT` + review
- **H19 Spelling.** Brand and place names exactly as in the glossary; ellipses ".." kept only where the speaker pauses. `check: V-CAPTION`
- **H20 Grades.** A persona keeps one grade id for all its shots; two consecutive personas never share a grade; ≤ 8 grade events per reel. `check: V-GRADE` (pending: review)
- **H21 Light worlds flip the type.** On W-paper and W-grid the keyword block is `ink`, never yellow; yellow stays on footage, W-void and W-poster, or burned onto a card's photo. `check: V-TYPE` + review
- **H22 Audio and determinism.** −14 LUFS, true peak ≤ −1.5 dBTP, hard end ≤ 6 f after the last word (NC-8); every frame a pure function of its index (NC-9). `check: review`

### 2.4 NEVER
- **N1** Banner slabs, pills, boxed or highlighted captions, coloured words inside the subtitle, emoji in type.
- **N2** A second text accent (no red/green axis, no pink, no gradients on keywords except the sign-off word P-SIGNOFF-SUN).
- **N3** Yellow text directly on cream or white paper (contrast 1.2:1): use `ink` (H21).
- **N4** Punch-ins (outside the one T-12 zoom-through), crash zooms, shakes, rotation snaps, RGB splits, resting light-leak PNGs, film burns, glitch packs.
- **N5** Stock footage or generated scenes presented as the creator's world; drone-look fakes made from stills.
- **N6** Meme SFX, stickers, stamps, emoji pops (comedy is light: staging and script asides only).
- **N7** Two duo titles at once; a duo title over the CTA keyword; a script connector carrying the keyword.
- **N8** A chaos burst on a line that isn't about overload, or a second one in the reel.
- **N9** Raw full-bleed screen recordings: always inside P-APP-DEVICE or P-PHONE-REEL (a full-bleed UI close-up ≤ 1.5 s is allowed only as a zoom inside the device).
- **N10** Fake UIs, invented metrics or follower counts presented as real.
- **N11** A fade to black or a black tail: the reel ends on the bookend picture.
- **N12** Sans-serif or ALL-CAPS subtitles; subtitles above y 1470 or below y 1510.
- **N13** Meaning text in the top 110 px, below y 1540, or in the right 110 px between y 900 and 1540.
- **N14** Decoration: a card, mark or word that doesn't show what is being said.

Buyer additions `BN1…` `[VAR]`.

---

## §3 Worlds, layouts, stage moves, safe zones `[DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-footage** | footage | The creator's graded cinematic footage, full-bleed (GR-warm, §4.4). Behind a smaller stage: a 28 px-blurred copy at 45% brightness | 55–80% of every reel: places, talking pieces, details, personas | Hard cut (T-1), cut on motion (T-2), blur-through (T-3) |
| **W-paper** | paper | Flat cream `#FCFBE6` (`cream`), noise 0.03, no grid, no vignette | 9:16 cards, 4:3 cards, phone reels, recap riffles, ink guides (v03 @ 0:11–0:27, v04 @ 0:19–0:55) | Hard cut with the card already placed (G-3) or G-1 shrink-to-card; exit by a hard cut (measured v04 @0:27.9), T-6 fade only as an alternate |
| **W-grid** | paper | Greige `#E5E1D3` (`greige`) with a 64 px 1 px grid (`grid` `#CFCBB6`), vignette 0.42, noise 0.04 | Polaroids, device frames, carousels, the series lockup (v02 @ 0:29–0:31, 0:45–0:50; v05 @ 0:09, 0:23–0:25, 0:30–0:54) | Hard cut; polaroid drop (10 f) |
| **W-void** | void | Near-black `#050505` (`night`); plain under the spin card (v03 @0:06.5 shows no dots), white dots 10% at 120 px pitch only behind devices, vignette 0.3 | The spin-in card's launch pad (v03 @ 0:06–0:09), dark device close-ups (v05 @ 0:32–0:51), the end block fallback | Hard cut; T-4 spin out to full |
| **W-poster** | card-world | `accent` sun: a near-solid disc centred (540, 975), r 487, `#D42A05` at the centre to `#B50E05` at the edge, on a near-black `#0A0603`-`#270402` field (audit: v02 @0:54.5) | The CTA and sign-off silhouette (v02 @ 0:52–0:58) | Hard cut. Usually drawn *behind the matted creator* (P-POSTER-BACKDROP) rather than as a stage world |

World colours come from `roles`; the buyer's `accent` recolours W-poster.

### 3.2 Layout library
| ID | Engine | Presenter / footage rect | Graphic rect | Caption | Treatment | Share F-A | Share F-B |
|---|---|---|---|---|---|---|---|
| **L-full** | `full` | 0, 0, 1080 × 1920 | — (type in the sky or top third) | fixed_y 1468 | GR-warm | 55–100% | 35–75% |
| **L-card916** | `card` | x 192, y 160, w 696, h 1238, radius 40, crop 9:16, shadow 0.35, on W-paper | card-top title band x 232–848, y 200–460 | fixed_y 1468 (40 px under the card) | — | 0–30% | 0–40% |
| **L-card43** | `card` | x 72, y 494, w 936, h 702, radius 28, crop 4:3, shadow 0.25, on W-paper | title band y 200–460 | fixed_y 1468 | guide lines (P-GUIDE-LINES) allowed inside | — | 0–25% |
| **L-hidden** | `hidden` | none: every pixel is a scene (paper cards from assets, polaroids, devices, spin, end block) | x 64–1016, y 110–1440 | fixed_y 1468 | — | 0–30% | 10–50% |

Scene-built frames (not stage layouts; they play `veos asset add` clips with `ctx.videoFrame`):
| Frame | Rect (resting) | Used by |
|---|---|---|
| Paper card 9:16 | x 192, y 160, w 696, h 1238, radius 40 (measured v03 @0:11.5 x 189-891, y 183-1431; v04 @0:22 x 162-918, y 168-1479; set so the subtitle clears y 1500 under the card), shadow `0 18px 40px rgba(0,0,0,.18)` | P-PAPER-CARD, P-RECAP-RIFFLE, P-CARD-CAROUSEL |
| Polaroid | image 700 × 875 + 24 px `frame` border all round (outer 748 × 923), centre (540, 860), tilt −2.5…+2.5°, shadow `0 14px 30px rgba(0,0,0,.35)` | P-POLAROID, P-BEFORE-AFTER-POLAROID |
| Device | x 150, y 170, w 780, h 1270, radius 64, 22 px `#0E0E0E` bezel, shadow `0 30px 60px rgba(0,0,0,.45)` | P-APP-DEVICE |
| Phone reel | x 252, y 180, w 576, h 1250, radius 48 | P-PHONE-REEL |
| Spin card | 16:9, w 900, h 506, radius 28, launched from centre (540, 960) | P-SPIN-CARD |

**Layout schedule:** none fixed. Rule: leave L-full for paper only on a line that *shows* something (an example, a recap, a rule, a screen, a photo); come back to L-full on the next opinion or turn word ("but", "so", "and that's why").

### 3.3 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | Shrink-to-card | `stage: {layout: "L-card916", via: "shrink-to-card", dur: 12}`; world switches to W-paper at the same t; the card title (P-PAPER-CARD title) blur-slides in at f+8 | Footage becomes the example ("this is what I mean") |
| **G-2** | Grow-from-card | `via: "grow-from-card", dur: 10` back to L-full | Back to the story from an example |
| **G-3** | Paper cut | Hard cut (0 f) from L-full to L-hidden/L-card916 on W-paper with the card already at rest; the card's content keeps playing | The default way into paper (v03 @ 0:11) |
| **G-4** | Spin-to-vertical | P-SPIN-CARD (T-4): on plain black a playing 16:9 card turns 90° and grows until it covers the frame (2.5–4.5 s), then cuts | Opening a flashback, "the old way", a chapter (v03 @ 0:06–0:10) |
| **G-5** | Fade-through | `via: "fade-through", dur: 8` | Into and out of a device close-up |
| **G-6** | Depth sandwich | Not a move: an E1 word drawn `behind: true` between the footage and the cut-out, drifting 8–12 px | Behind-head words (P-BEHIND-WORD) |

### 3.4 Layout diagrams
```
L-full (hook / thesis beat)                 L-card916 on W-paper
┌─────────────────────────┐ 0               ┌─────────────────────────┐ 0
│ (IG top UI, keep clear) │ ← 0–110          │                         │ ← 0–110 clear
│ script connector  y 250 │                  │ ╭─────────────────────╮ │ ← card y 160 (x 192–888)
│ BLOCK KEYWORD           │ ← duo band       │ │ CARD TITLE (yellow, │ │ ← burned title y 160–420
│ BLOCK KEYWORD           │   y 120–880      │ │ no stroke)          │ │
│        script  bottom-rt│                  │ │                     │ │
│                         │                  │ │   creator clip      │ │
│ (head top ≥ lockup      │                  │ │   (9:16, radius 40) │ │
│  bottom + 40 px)        │                  │ │                     │ │
│     presenter / place   │                  │ ╰─────────────────────╯ │ ← card bottom 1398
│                         │                  │   Lemon serif subtitle  │ ← cy 1468
│  Lemon serif subtitle   │ ← cy 1468         │                         │
│ (IG bottom UI)          │ ← 1540–1920       │ (IG bottom UI)          │
└─────────────────────────┘ 1920             └─────────────────────────┘

L-card43 on W-paper (F-B rule)              Polaroid on W-grid
┌─────────────────────────┐ 0               ┌─────────────────────────┐
│ RULE TITLE (ink, wide)  │ ← y 200–460      │  ┊  ┊  ┊ grid 64 ┊  ┊  │
│╭───────────────────────╮│ ← y 494          │    ╭───────────────╮    │ ← outer y 398
││ 4:3 example + guides  ││   x 72–1008      │    │ ┌───────────┐ │    │   tilt −2.5…+2.5°
││ + yellow ink          ││                  │    │ │ photo 4:5 │ │    │
│╰───────────────────────╯│ ← y 1196         │    │ └───────────┘ │    │
│                         │                  │    ╰───────────────╯    │ ← outer y 1322
│  Lemon serif subtitle   │ ← cy 1468         │  Lemon serif subtitle   │ ← cy 1468
└─────────────────────────┘                  └─────────────────────────┘
```

### 3.5 Safe zones and bands
- **Meaning-text box:** x 64–1016, y 110–1500 (`layout.safe`, TUNE inside NC-5). The right column x > 970 between y 900 and 1540 stays empty.
- **Duo band:** y 120–880, x 64–1016 (measured: v01 @0:02 blocks y 279–711, v05 @0:02.2 y 100–693, v02 @0:01.7 y 300–865). First block line top at y 300 (hook) or y 230 (mid-reel); script connectors at y 230–300 above, or under the last block line + 16 px.
- **Title band (HA-05 lockup, card titles):** y 230–410 on L-full (v03 @0:02.6 y 230–363, v04 @0:02.5 y 250–401); card titles inside the card's top 300 px.
- **Caption band:** centre y 1468 on every layout (one line, ~62 px tall: y 1437–1499). The source sits at cy ≈ 1488 (glyphs y 1467–1510, v01 @0:12, v03 @0:02.6, v05 @0:30); it is lifted 20 px to stay above y 1500.
- **Counter band:** digits top y 200–260; unit stack directly under, ≤ y 900.
- **Legal line:** x 64, y 128, `TC-legal` 24 px.

### 3.6 Presenter rules
- **Share** 45–60% F-A, 35–55% F-B (TUNE ±10). **Longest absence** 6 s F-A, 8 s F-B. A persona scene with the creator counts as presence.
- **Return:** by a hard cut or cut on motion to a talking piece; never by a morph from paper unless G-2.
- **Head-top positions:** setup A 250–520, setup B 420–700, setup C 600–1100, setup D 560–800. **Front-layer type keeps its bottom edge ≥ 40 px above the head top:** a one-line beat (top y 330, 200 px) ends near y 520, so it needs a head top ≥ 560; a two-line beat ends near y 720 and needs ≥ 760. A higher head takes the word behind it (E1), or the beat shifts sideways so its rect clears the face box by 40 px, or the beat moves to a wider shot.
- **Behind the head (E1):** only Anton block words 200–340 px (or count-up digits), centred on the head's x ±120 px, top of word 60–160 px above the head top so that ≥ 65% of the glyph area stays visible; first and last letters always clear of the hair.

---

## §4 Colour, grades `[roles' meanings DNA; brandable hex VAR; grade strength TUNE]`

### 4.1 Role palette
| Role | Hex | One job | Text on it / contrast | Brandable |
|---|---|---|---|---|
| `primary` | {{BV-02.primary|#F7DE0B}} | **The** yellow: keyword blocks, behind-head words, counters, title lockups, card titles, ink arrows and ovals, the CTA keyword | `ink` 15.3:1 | **VAR** (any one saturated hue; contrast-nudged to ≥ 4.5:1 with ink) |
| `accent` | {{BV-02.accent|#D42A05}} | Poster backdrop only: the sun disc / colour wall behind the silhouette (P-POSTER-BACKDROP, P-SIGNOFF-SUN) | `ink` 4.9:1; `primary` on it 3.2:1 (display ≥ 96 px only) | **VAR** |
| `subtitle` | `#EEF272` | Pale-lemon serif subtitle text | with its 1 px `shade` stroke and hard drop shadow it reads on any background | TUNE (pale lemon to cream) |
| `paper` | `#FFFFFF` | White script connectors, guide lines, lasso outlines | — | DNA |
| `ink` | `#0B0B0B` | Keyword blocks and script on light worlds (H21) | on `cream` 18.8:1 | DNA |
| `shade` | `#1A1208` | Warm black for text strokes (subtitle 1 px; connectors and titles carry none) and shadows | — | DNA |
| `cream` | `#FCFBE6` | W-paper background | `ink` 18.8:1 | TUNE |
| `greige` | `#E5E1D3` | W-grid background | `ink` 15:1 | TUNE |
| `grid` | `#CFCBB6` | 1 px grid on W-grid | — | TUNE |
| `frame` | `#F6F4EC` | Polaroid border | — | TUNE |
| `gold` | `#9A6E0A` | Series lockup only (≥ 96 px) | on `greige` 3.5:1 | TUNE |
| `night` | `#050505` | W-void | — | DNA |

`fixed_meaning: []`: this style has no red/green axis. `max_bright_per_frame: 2` (`primary` + `accent`, and `accent` only on a poster).

### 4.2 Meanings
- **Yellow = the word to remember.** Only content words (nouns, numbers, the key verb, the CTA keyword) are yellow. A yellow arrow or oval means "look here".
- **White script = the connective tissue** of the sentence. Never a keyword, never a number.
- **Cream serif = the voice.** Every spoken word, quiet and constant.
- **Accent = the stage for the sign-off.** The poster backdrop appears in at most two beats per reel (a thesis poster, the CTA / sign-off).
- **Grades = characters.** GR-mono, GR-amber and GR-teal tell personas or moods apart (4.4).
- Brand colours appear only inside a logo chip (P-LOGO-CHIP); a logo's own colours never count as a style hue.

### 4.3 Theme packs
OFF (`themes.policy: single`).

### 4.4 Grades `[TUNE strength; ids and meanings DNA]`
| ID | CSS filter stack (renderer) | Look | Use | Evidence |
|---|---|---|---|---|
| **GR-warm** (footage default) | `sepia(0.12) saturate(1.08) contrast(1.04)`; tokens: warmth +0.08, saturation 1.06, bloom 0.08, vignette 0.12 | Warm teal-orange, golden skin, blue skies kept | Every creator clip unless a scene grade applies | v04 @ 0:00 (sky `#3E86C4`, warm skin) |
| **GR-mono** | `grayscale(1) contrast(1.18) brightness(0.92)` | Hard black and white | The negative / stuck persona, self-doubt, the "before" state, under the chaos burst | v02 @ 0:04–0:08, 0:32–0:36 |
| **GR-amber** | `sepia(0.45) saturate(1.35) hue-rotate(-10deg) contrast(1.06) brightness(0.96)` | Tungsten amber, deep shadows | The obsessive / collector persona, nostalgia, late night | v02 @ 0:09–0:17 |
| **GR-teal** | `sepia(0.35) hue-rotate(140deg) saturate(1.25) contrast(1.05)` | Cold teal-green | The shortcut / hacker persona, cold logic, "the algorithm" | v02 @ 0:18–0:23 |

**Grade events:** a grade starts on a cut (never mid-shot), lasts the whole persona or mood segment, ≤ 8 events per reel, and two consecutive personas never share an id (H20). The creator's own "answer" segment returns to GR-warm.

**How grades render today (GR-L, until engine item E-16 ships).** For each grade span write a `timeline.grades` entry `{"t": 4.05, "until": 8.02, "grade": "GR-mono"}` (it counts as a state change and V-GRADE will read it) **and** a z4 scene that grades everything beneath it:
```js
// GR-L: today's grade layer (E-16 pending). z4 sits above the footage group and below every text layer.
VEOS.scene({ id: "grade-mono-1", t_in: 4.05, t_out: 8.02, z: 4, in: "none", out: "none", roles: [],
  box: { x: 0, y: 0, w: 1080, h: 1920 },
  render(ctx) { return ctx.html(`<div style="position:absolute;inset:0;backdrop-filter:grayscale(1) contrast(1.18) brightness(.92)"></div>`); } });
```
Costs of GR-L: it is one of the four G2 scenes, and it would grey a behind-head word (behind words live inside the footage group). So **no E1 word inside a GR-L span**: use a front-layer block above the head there (FB-11). GR-warm is not drawn by GR-L (too subtle to be worth a layer); it applies when E-16 ships.

### 4.5 Rules
- ≤ 2 bright roles per frame (NC-10 allows 4; this style uses 2).
- Yellow never sits on cream, white or greige unless it is burned onto a photo inside a card (H21, N3). On light worlds the block is `ink`.
- Script connectors are thin white monoline handwriting with **no stroke** (audit: v05 @0:02.2 over water, v02 @0:54.5 over black) and only a faint `0 1px 4px rgba(0,0,0,.35)` shadow; on a bright sky move them to the darker side rather than outline them.
- Yellow blocks on footage carry **no shadow and no stroke** (v01 @0:02, v05 @0:02.2, v04 @0:02.5); when V-TYPE reports < 3:1 (bright sky, white wall), add a 3 px `shade` stroke to that block only, or move it to the darker half of the frame.
- Footage is graded only by §4.4. No LUT packs. The only light effects are the flash transitions T-10 / T-11 (§9.1), never a resting overlay.

**Must match `tokens.json`.**

---

## §5 Type & caption system

### 5.1 Font map `[slots DNA; families TUNE within the class]`
| Slot | Family (bundled) | Weight | Font class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `display` | **Anton** | 400 | condensed heavy caps | Duo keyword block, behind-head words, CTA keyword |
| `wide` | **Montserrat** | 900 | wide ultra-heavy caps (audit: the source face is narrower than Archivo Black; Montserrat 900 matches its cap-height-to-width ratio within 5%) | Title lockup, card titles, end block, echo outline, series block |
| `numeric` | **Montserrat** | 900 | wide ultra-heavy caps | Count-up digits |
| `script` | **Nanum Pen Script** | 400 | thin pen handwriting (Pinyon Script is the calligraphic TUNE option) | Duo connectors, script asides, series script |
| `serif` | **EB Garamond** | 600 | old-style serif 500–600 | Subtitles (CS-1), "#N." markers, chaos phrase fragments (italic) |
| `ui` / `body` | **Jost** | 500–700 | geometric sans | UI chips, chaos bracket tags, the logo-plate wordmark, legal line, created UI text |
| `mono` | JetBrains Mono | 400 | mono | `TC-decorative` texture only |

The white pen connectors use **Nanum Pen Script** (slot `script`) and the wide titles **Montserrat 900** (slot `wide`), both bundled. Pinyon Script remains a TUNE option for calligraphic connectors (v02 @ 0:14–0:16 "doesn't care about", 0:57 "See you in there"). Brand wordmarks and series logos are image assets, not fonts.

### 5.2 Headline element: the duo title (`kind: "lockup"`) `[DNA recipe; NICHE text]`
| Property | Spec |
|---|---|
| Block (keyword) | Anton 400, caps, `primary` `#F7DE0B`, **180–340 px**, line height 0.88, tracking −1%, **no shadow**; each line is **size-fitted to span ≈ 860–900 px** (x ≈ 96–984), so a short word gets huge and a long line gets smaller (audit: v01 @0:02 SHOPPING 247 px / cap 211; v05 @0:02.2 LOVING ≈ 335 px / cap 308, THE PICTURES ≈ 180 px). ≤ 3 words per line, ≤ 2 lines; never below 170 px |
| Script (connectors) | Nanum Pen Script 400, as spoken, `paper`, **84–112 px** (default 100; v02 @0:54.5 "Just comment" 542 px wide, glyphs 73 px tall), no stroke, faint shadow `0 1px 4px rgba(0,0,0,.35)` |
| Placement | **Above-left** of the block (script baseline 12–20 px above the block's top, x = block left + 8) for leading connectors; **below-right** (top = block bottom + 16, right-aligned to the block) for trailing ones. **Corners variant** (P-DUO-CORNERS): leading words at (96, 250) and (984, 250, right-aligned), trailing words at the block's bottom corners |
| Block entry | **Rise-smear** (measured v01 @0:00.59–0:00.72, `strip-hook-duo-blurslide.jpg`): the word rises from **y + 0.8 × cap height (≈ 150–220 px)** to rest with a **vertical** motion smear (24 → 0 px, along y only) and opacity 0 → 1 over **4 f** (3 f at the source's 24 fps: +150 → +72 → 0 px, expo-out); starts 2 f before the word's onset |
| Script entry | **Write-on**: a left-to-right clip mask over **8 f** (linear), starts on the word's onset (v01 "when it comes to what" ≈ 0.30–0.47 s) |
| Hold | 0.4–0.6 s per single-word beat; a full two-line lockup holds ≥ 10 f after its last word lands |
| Exit | **Rise-out**: up ≈ 110–150 px (−35 then −110 px measured), vertical smear 0 → 24, opacity 1 → 0 over **3–4 f**, ease-in; words leave **last-in first, 1 f apart** (v01 WEAR leaves 1 f before YOU). The script **un-writes right to left** in 4 f (v01 @0:00.93–1.05), it does not slide. The next beat may start 3–5 f after the exit ends (a short empty beat is allowed, v01 @ 0:01.17) |
| Exit at a cut | The hook's last lockup is **not** animated out: it holds and leaves with the shot on the hard cut (v01 @0:03.99 "IS WAY BETTER" → walk-in, subtitle starts on the cut) |
| Exit inside a burst | Inside the E2 burst a duo blurs out **in place** (blur 0 → 16 px, no travel, 3 f; v02 @0:06.67 "to be PERFECT") |
| Join | A second block word on the same line slides in on its own word while the first holds (v01 "YOU" → "YOU WEAR") |
| Replace | A new beat replaces the whole block (blur out, then in) when the next keyword starts a new idea |
| f0 | In HA-12 nothing is fully visible on f0: the first connector starts writing at f0 (0% revealed) or the first block lands at 0.4–0.7 s |
| Lifetime | `section`: the hook (2.5–4.0 s), a thesis re-hook, a persona label, the CTA |
| Budget | 4–9 duo titles per 60 s (≈ 10–18% of runtime), never two at once, subtitles hidden while one is up (z8) |
| Light worlds | On W-paper / W-grid the block and the script are `ink`, no stroke (v02 @ 0:28 "IT'S ALL", 0:38 "Hold you BACK") |

**Duo split rule (P7):** keywords = nouns, numbers, names, the main verb or adjective of the claim; connectors = articles, pronouns, prepositions, auxiliaries, conjunctions. "When it comes to what **YOU WEAR** / **SHOPPING IN PERSON** / **IS WAY BETTER** than online." Never put two keywords in the script; never set a connector in the block, except a pronoun the block needs to make sense ("**YOU** WEAR").

**Scene recipe (one scene per beat; helpers shared by all duo scenes):**
```js
// Rise-smear state at local time lt for an element that lands at `at` and leaves at `outAt` (seconds, local).
// travel = 0.8 x cap height (cap ≈ 0.73 x font size for Anton), so a 240 px word rises ≈ 140 px.
function blurSlide(lt, at, outAt, size = 240) {
  const k = (lt - at) * 30, T = Math.round(0.8 * 0.73 * size);
  if (k < -2) return null;                                          // lead: starts 2 f before the word
  if (outAt != null && lt >= outAt) { const q = Math.min(1, (lt - outAt) * 30 / 4), qi = q * q; return { o: 1 - q, y: -T * qi, b: 24 * q }; }
  const e = Math.min(1, (k + 2) / 4), ei = 1 - Math.pow(1 - e, 3); // 4 f expo-out
  return { o: ei, y: T * (1 - ei), b: 24 * (1 - ei) };
}
// Vertical smear: the shared directional blur (angle 90 = along y only), whole px so the filter set stays small.
function smear(ctx, b) { return b < 0.5 ? "" : `filter:${ctx.blur(Math.round(b), 90)};`; }
function duoWord(ctx, w, lt, outAt) {   // w = {text, at, x, y, size, kind: "block" | "script", align}
  const block = w.kind === "block";
  const s = block ? blurSlide(lt, w.at, outAt, w.size)              // script: write-on in, un-write out (no slide)
    : (lt < w.at ? null : { o: 1, y: 0, b: 0 });
  if (!s) return "";
  const light = ctx.world === "W-paper" || ctx.world === "W-grid";
  const col = light ? ctx.col("ink") : (block ? ctx.col("primary") : ctx.col("paper"));
  const font = block ? `400 ${w.size}px/0.88 ${ctx.fam("display")}` : `400 ${w.size}px/1.1 ${ctx.fam("script")}`;
  const deco = block ? "text-transform:uppercase;letter-spacing:-0.01em;"            // no stroke, no shadow (audit)
    : (light ? "" : "text-shadow:0 1px 4px rgba(0,0,0,.35);");
  const wr = Math.min(1, Math.max(0, (lt - w.at) * 30 / 8)), un = outAt != null && lt >= outAt ? Math.min(1, (lt - outAt) * 30 / 4) : 0;
  const wipe = block ? "" : `clip-path:inset(0 ${Math.round(100 - 100 * wr * (1 - un))}% 0 0);`;
  const shift = w.align === "right" ? "transform:translateX(-100%);" : "";
  return `<div style="position:absolute;left:${w.x}px;top:${Math.round(w.y + s.y)}px;${shift}font:${font};color:${col};${deco}${wipe}${block ? smear(ctx, s.b) : ""}opacity:${s.o.toFixed(3)};white-space:nowrap">${ctx.esc(w.text)}</div>`;
}
VEOS.scene({ id: "duo-1", t_in: 0.0, t_out: 1.20, z: 8, in: "none", out: "none", kind: "lockup", text: true,
  text_class: "TC-display", roles: ["primary"], text_content: "When it comes to what YOU WEAR",
  box: { x: 64, y: 230, w: 952, h: 300 }, events: [0.47, 0.80, 1.07],
  render(ctx, lt) {
    const out = 1.07, kw = `400 200px ${ctx.fam("display")}`;
    const W = [
      { text: "When it comes to what", at: 0.00, x: 72, y: 220, size: 100, kind: "script" },
      { text: "You", at: 0.47, x: 64, y: 330, size: 200, kind: "block" },
      { text: "Wear", at: 0.80, x: 64 + ctx.measure("YOU ", kw), y: 330, size: 200, kind: "block" }];
    return ctx.html(W.map(w => duoWord(ctx, w, lt, out)).join(""));
  } });
```
Declare every landing and the exit in `events` (they are state changes and V-ONWORD anchors). Take `at` values from `words.edit.json` (word onset − `t_in`).

### 5.3 Caption system profile CS-1 `[DNA mechanics; size and y TUNE; language VAR]`
| Group | CS-1 (extends `lib:omgadrian`) |
|---|---|
| Mode | `full` / `support` / `mute_safe` |
| Chunking | unit `phrase`; **3–6 words** (mean 4); max 28 characters per line; **1 line**; never split a name, number or unit; new chunk on `. , ? !` and on any pause ≥ 0.9 s (`hard_pause_s`) |
| Timing | lead 2 f; hold ≥ 0.25 s per word; tail 0.12 s; swap **hard** (a free chunk swap, not a slot, so no E6); no pause hold |
| Skin | slot `serif` (EB Garamond) **600**, **54 px** (`TC-subtitle`), sentence case as spoken, tracking 0, colour `subtitle` **pale lemon `#EEF272`** (glyph cores `#EDF36A`-`#EFF079`, v01 @0:12, v03 @0:02.6), 1 px `shade` stroke, **hard drop shadow `2px 3px 2px rgba(0,0,0,.85)`** (down-right, v03 @0:11.5 on cream), no container |
| Position | `fixed_y`, **cy 1468**, centred, max width 952, on every layout (L-card916 leaves a 40 px gap under the card); no colour flip (the hard shadow keeps it readable on cream) |
| Speakers | — (a second person on camera keeps the same skin) |
| Emphasis | `none`: the subtitle never highlights (the duo title does) |
| Variants | karaoke, two-tier, duet, kinetic stack: none in CS-1 (the duo title is built as scenes, 5.2) |
| Hide rules | `under_z8` (duo titles, the CTA keyword, the end block, the chaos burst), `E2`, `morph` |
| Language | Latin script; keep English terms verbatim; don't normalise spelling; profanity `inner` mask (`S**T`); glossary = the creator's brand, place and tool names; keep ".." on in-sentence pauses |

Measured at full resolution: EB Garamond-fit width gives **47–48 px** at 1080 (v01 @0:12 "because nothing is worse" 470 px wide; v03 @0:02.6 582 px). The template sets **54 px** so the subtitle meets the G4 floor without the E3 exception (the coverage decision is E1 + E2 only); TUNE range 54–62.

### 5.4 Other text systems
| System | Class | Recipe | Hold |
|---|---|---|---|
| **Title lockup** (HA-05, P-TITLE-LOCKUP) | TC-display | Montserrat 900 caps **80–108 px**, `primary` (v03/v04 use the lemon `#FBF434`, a TUNE alternative), **no stroke, no shadow**, line height 0.92, centred, each line size-fitted to 860–980 px wide (line 2 often smaller: v04 @0:02.5 cap 79 then 62 px), y 230–410, ≤ 6 words in ≤ 2 lines. **Squash-in** (measured v03 @0:00.39–0:00.52, `strip-title-squash-in.jpg`): each line opens from a thin bar (scaleY 0.05 → 1 about the line's centre, slight vertical smear: `filter:${ctx.blur(px, 90)}`) in **3 f**, line 2 starts **2 f** after line 1; no rule (the "dashed rule" on the 6 fps sheet was line 1 at scaleY ≈ 0.05) | 2.0–4.0 s, then leaves with the shot on a cut, or blur-out 4 f |
| **Card title** (burned on a paper card's photo) | TC-display | Montserrat 900 caps 64–84 px, `primary`, no stroke, x card + 40, y card + 40, ≤ 3 lines, ≤ 5 words (v03 @0:11.5, v04 @0:22) | the card's life |
| **Counter** (P-COUNT-UP) | TC-display | Montserrat 900 280–400 px `primary`, centred x 540, top y 220; digits **append** left to right (3 → 36 → 365), one per spoken beat or every 6 f; unit word(s) 90–120 px stacked under, line height 0.9 | ≥ 1.0 s after the last digit |
| **Echo outline** (P-ECHO-OUTLINE) | TC-display | The phrase twice in Montserrat 900 120–170 px: filled `primary`, then outline-only (3 px `primary` stroke, transparent fill), stacked as 4 lines over the presenter | 0.8–1.2 s |
| **Hash marker** (SM-1) | TC-label | "#1." EB Garamond 600 54 px `subtitle` + the subtitle shadow, centred at y 1468 **in place of** the subtitle | 0.5–0.8 s |
| **Script aside** (P-SCRIPT-ASIDE) | TC-display | Nanum Pen Script 84–112 px `paper`, no stroke, alone, top band y 230–420, written on in 8 f | 1.0–2.0 s |
| **UI chip** (P-UI-CHIP) | TC-label | Jost 600 44 px `ink` on a white pill (radius 999, padding 18/34, shadow `0 8px 24px rgba(0,0,0,.25)`) with a 36 px search glyph; or a `primary` pill with `ink` caps text ("BUY NOW") | 1.0–2.0 s |
| **Chaos tag / phrase** (E2) | TC-label | Tags "[Close Up]" Jost 500 44–52 px `paper` at 85%; phrases EB Garamond italic 56–72 px `paper`; all with `0 2px 8px rgba(0,0,0,.6)` | inside the ≤ 1.5 s burst |
| **End block** (P-END-BLOCK) | TC-display | Montserrat 900 caps, 4–7 lines, each line sized to fill x 64–1016 (70–200 px), line height 0.9, `primary`, y 220–1360 | 2.5–4.0 s |
| **Series lockup** (P-SERIES-LOCKUP) | TC-display | Script name Pinyon 120–160 px `gold` over a Montserrat 900 block 130–170 px `gold`, "ep. NN" Jost 600 40 px `gold` under it, centred at y 900 on W-grid with the grid off | 1.2 s |
| **Logo word** (P-LOGO-CHIP) | TC-label | "With" script 60 px + logo (creator file, 88 px tall) + wordmark Jost 500 72 px `paper` | 1.0–1.5 s |
| **Legal line** (P-DISCLOSURE) | TC-legal | Jost 500 24 px, `paper` 85% on footage / `ink` 70% on paper, x 64, y 128 | ≥ 2.0 s, or the whole sponsor segment |

### 5.5 Language and number rules
- Spelling: brand, place and tool names exactly as the glossary; English words exact inside Hinglish captions.
- Numbers on screen are digits, as spoken ("365", "52", "#3"); international grouping by default; Indian grouping and ₹ when the buyer's language is Indian (BV-06).
- Caps: the block, titles and end block are ALL CAPS (Latin only). The subtitle is sentence case.
- **Devanagari** (`hi/hi/Deva`): the subtitle falls back to Noto Sans Devanagari 500 (no serif exists); duo titles, titles and counters stay Latin (English keywords), because Anton and Montserrat have no Devanagari. Script connectors in a Devanagari reel become Noto Sans Devanagari 400 at 60 px (no italic exists).
- Hinglish captions: romanised as spoken; keyword blocks use the English keyword when one is spoken, else the romanised word.

---

## §6 Hook system

**Hook title (every style, 8 Oct 2026; above anything below):** the on-screen title promises the viewer something: an outcome they want, a curiosity gap, or who it's for ("How to go viral as a doctor creating content", not the label "Reels for Doctors"). It doesn't have to repeat the spoken words; it has to be true to what the reel delivers. A title shown as someone's words (in quotes) is still word for word. This section sets the title's shape (lines, sizes, word limits, case, the keyword device), never its voice. Write 8–10 candidates from the formulas below plus the proven patterns ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", "Your X vs mine", a number or a contrast), score them on outcome, curiosity, who it's for and brevity, check the best against the stopper tests, and pick; any "write 3" below means this, and the next two go to the storyboard as alternates. A style with no on-screen title applies this to its post title.

### 6.1 Stopper tests
| Test | This style's number |
|---|---|
| ST-1 Thumbnail | **Not used for HA-12** (f0 is image-only by design); for HA-05, HA-19 and HA-08 the title / word / number reads at 25% scale (≥ 16 px cap height) |
| ST-2 Mute | The first 3 s tell the thesis without sound (the duo beats carry the whole sentence) |
| ST-3 Motion at f0 | Live footage in motion, a walk-in, a drone move, or Z-1 starting at f0 |
| ST-4 Read time | Each beat reads in ≤ 1.2 s (≤ 3 block words + ≤ 5 script words) |
| ST-5 Change count | ≥ 6 weighted state changes in 0–3 s (`hook_sc_3s`) |
| ST-6 Payoff-by | Thesis complete by 3.0 s (HA-12); title by 0.7 s (HA-05); premise by 3.0 s (HA-19); hero number by 1.7 s (HA-08) |

### 6.2 Default archetype: HA-12 Thesis typography `[DNA]`
The thesis or question is split into 3–4 typographic beats over one moving cinematic first shot (SH-1). No banner, no result.

| t (s) | Frames | Beat | Picture (SH-1) | Type layer | Subtitle | Camera | Cue moment |
|---|---|---|---|---|---|---|---|
| **f0** | 0 | Stopper | A composed moving shot: frame-in-frame (mirror, door, window), overhead/drone, or the creator walking in; presenter visible or entering | Nothing fully visible; connector 1 starts writing (0%) | hidden | Z-1 push-drift from f0 if the shot itself is static | hook (soft) |
| 0.00–0.33 | 0–10 | Connector 1 | same shot | Script connector(s) write on L→R in 8 f at (72, 220), 100 px | — | — | — |
| 0.40–0.70 | 12–21 | Keyword 1 | same | Block word 1 blur-slides in (4 f) at x 64, top y 330, 200 px | — | — | — |
| 0.70–1.00 | 21–30 | Join | same | Block word 2 joins on its word (same line), or connector 2 writes | — | — | — |
| 1.00–1.30 | 30–39 | Swap | same (the shot keeps moving) | Block blurs out upward (4 f); ≤ 5 f empty | — | — | — |
| 1.30–2.00 | 39–60 | Keyword 2 | same | Next keyword(s) build line 1 then line 2 (≤ 2 lines) | — | — | — |
| 2.00–2.30 | 60–69 | Hold → out | same | The full lockup holds ≥ 10 f, then blurs out | — | — | — |
| 2.30–2.90 | 69–87 | Keyword 3 + close | same | Last block + closing connector below-right ("than online") | — | — | — |
| 2.70–4.00 | 81–120 | First cut | **T-2 cut on motion** to the first talking piece or B-roll | Lockup holds and leaves with the shot on the cut (no exit animation; v01 @0:03.99) | **CS-1 starts** on the first post-hook word | — | transition |

Payoff: the full thesis has been on screen by **3.0 s** (H4). Typical count in 0–3 s: 7 weighted changes (connector, kw1, join, out, kw2a, kw2b, kw3) ≥ 6.
Evidence: v01 @ 0:00–0:04 (mirror, "When it comes to what YOU WEAR / SHOPPING IN PERSON / IS WAY BETTER than online"), v05 @ 0:00–0:02.7 (overhead couple, P-DUO-CORNERS), v02 @ 0:00–0:02.7 (seated, "3 types of CONTENT creators", block partly behind the cap).

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`
**HA-05 Title lockup** (F-B default; v03, v04)
| t (s) | Picture | Type | Subtitle |
|---|---|---|---|
| f0 | SH-2 overhead or SH-3 walk-in: the creator enters the frame | — | hidden |
| 0.38 | same | Line 1 squash-in starts (a thin yellow bar, 3 f) | — |
| 0.43–0.55 | same | Line 1 then line 2 squash-in (3 f each, 2 f stagger): readable by 0.55 s | — |
| 0.8–4.0 | the creator settles (leans on the car, sits, looks up) | Title holds | CS-1 from the first word (≈ 0.8 s) |
| 2.9–4.0 | cut on motion | Title blurs out on the cut | continues |
Examples: [NICHE: example] fitness "FIX YOUR SQUAT / IN THREE CUES"; travel "SHOOT BETTER / TRAVEL PHOTOS".

**HA-19 Mood montage** (F-A, atmospheric openers)
| t (s) | Picture | Type |
|---|---|---|
| f0 | SH-4 cinematic detail in motion | One block word (Anton 230 px) blur-slides in from f0 (its scene starts at 0; landed by 4 f) |
| 0.9 | cut on motion to clip 2 | Word 2 replaces word 1 |
| 1.8 | clip 3 | Word 3 |
| 2.5–3.0 | talking piece | Closing script line; the premise is complete by 3.0 s |
Examples: [NICHE: example] "SALT. / SWEAT. / SILENCE." over three gym details; "RAIN. / RAMEN. / RESET." over three Tokyo details.

**HA-08 Count hook** (milestones and challenges; v04 @ 0:03, v02 @ 0:00.67)
| t (s) | Picture | Type |
|---|---|---|
| f0 | SH-11 matted headroom shot, the creator mid-gesture | — |
| 0.3–1.7 | same | P-COUNT-UP behind the head (E1): digits append on each spoken beat ("3 … 36 … 365"), landed by 1.7 s |
| 1.7–2.6 | same | The unit stacks under in 100 px ("DAYS STRAIGHT") |
| 2.7 | cut on motion | — |
Examples: [NICHE: example] "100 DAYS / NO SUGAR"; "52 CITIES / ONE BACKPACK".

### 6.4 Hook pairs by topic `[NICHE]` (pair type: thesis → scene promise)
| Topic | Thesis (duo split: **BLOCK** / script) | The scene that carries it | Paid off by |
|---|---|---|---|
| [NICHE: example] Fitness: training alone | "Training **ALONE** is why you **STOPPED** at week three" | Overhead of an empty gym floor, the creator walks in (SH-2/SH-3) | The coach's correction in a 4:3 card with ink arrows |
| [NICHE: example] Fitness: mornings | "Your **MORNING** decides your **WORKOUT**" | Mirror shot, laces being tied (SH-1) | The bookend: the same mirror at the end |
| [NICHE: example] Fitness: personas | "**3** types of **GYM** people" | Seated set, three fingers raised, cut on the hand (SH-5) | Three persona scenes graded GR-mono / GR-amber / GR-teal |
| [NICHE: example] Travel: homestays | "I **STOPPED** booking **HOTELS**. **THIS** happened" | Walk-in through a homestay door (SH-1 frame-in-frame) | A polaroid of the host family's kitchen (P-POLAROID) |
| [NICHE: example] Travel: street food | "The best **FOOD** in this city has **NO MENU**" | Overhead of a hawker stall (SH-2) | A detail run of five dishes (P-DETAIL-RUN) |
| [NICHE: example] Travel: phone photos | "Is your **PHONE** still taking **BORING** travel photos?" | Overhead of the creator at a railing (SH-2), corners layout | A before/after polaroid (P-BEFORE-AFTER-POLAROID) |

### 6.5 Headline writing `[DNA formula; NICHE text]`
- **Duo thesis formula:** `[script lead-in] + BLOCK KEYWORD + [script bridge] + BLOCK KEYWORD(S) + [script close]`, ≤ 12 words spoken, ≤ 7 words per on-screen lockup, 3–4 beats. A question is allowed ("Is your … ?").
- **Title lockup formula (HA-05):** `VERB + OBJECT` or `TOPIC + PROMISE`, ≤ 6 words, 2 lines ("CINEMATIC VERTICAL / VIDEO COMPOSITION", "THIS DECISION / CHANGED MY LIFE").
- Case: blocks and titles ALL CAPS; script as spoken.
- **Write 3, pick by the stopper tests** (§6.1); the other two go to trial reels.
- **Banned:** emoji, hashtags inside titles, "game changer", "you won't believe", a count that doesn't match the reel, a keyword the reel never pays off.

### 6.6 Hook sound
See §11: the hook may carry one soft cue on the first keyword landing and a transition cue on the first cut; the music bed runs from f0.

### 6.7 CTA `[DNA device set; VAR values]`
| Device | Spoken pattern | On screen | Hold | Where |
|---|---|---|---|---|
| `comment_keyword` | "Just comment {{BV-08.keyword|KEYWORD}} to get …" | **P-CTA-KEYWORD**: script "Just comment" at (72, 236) + **{{BV-08.keyword|KEYWORD}}** Anton 230 px `primary` at y 300 + script "to get it" below-right; over P-POSTER-BACKDROP (the `accent` sun behind the matted creator) or plain footage; scene `kind: "cta-keyword"` | ≥ 2.0 s (keyword readable ≥ 1.5 s) | The last 6–10 s, before the bookend |
| `link_bio` | "Link in my bio for …" | **P-END-BLOCK**, 4–6 lines ending "LINK IN BIO", over SH-13 texture | 2.5–4.0 s | End, before the bookend |
| `end_card` | "This was part 1 …" | P-END-BLOCK with the series line ("THIS WAS PART 1 / FOLLOW FOR PART 2") | 2.5–4.0 s | End, before the bookend |
| `post_only` | A spoken sign-off ("Peace.", "Take notes.") | Subtitle only, over the bookend shot | — | The last 1.0–1.5 s |

The buyer's device is {{BV-08.device|comment_keyword}}. Leave 0.3–0.5 s without new type before the CTA keyword lands. CTA tone is `cta`: no meme cues, no chaos. After the CTA, the bookend (§23) carries the last spoken words.

---

## §7 Structure & cadence `[DNA]`

### 7.1 Structure type (one per format)
| Format | Type | Arc and section lengths |
|---|---|---|
| F-A | `story` | **HOOK** 2.5–4.0 s (HA-12) → **SETUP** 4–8 s (where we are, why it matters) → **SCENE-n** 2–5 scenes or personas, 6–15 s each → **TURN** 3–6 s ("but…", "then it changed", the realisation; carries the re-hook) → **PAYOFF** 5–10 s (the thesis proven, the answer) → **CTA** 3–6 s → **BOOKEND** 1.0–1.5 s |
| F-B | `tutorial` | **HOOK** 3.0–4.0 s (HA-05) → **CONTEXT** 4–8 s (why it matters; one spin-in card allowed) → **RULE-n** 3–8 rules, 6–12 s each → **RESULT** 3–6 s (before/after) → **CTA** 3–6 s → **BOOKEND** 1.0–1.5 s |

### 7.2 Markers
| ID | Marker | Recipe | Used in |
|---|---|---|---|
| **SM-1** | Hash marker | "#1." EB Garamond 54 px in the caption band, replacing the subtitle for 0.5–0.8 s, on the ordinal word or the cut into the item (v02 @ 0:03, 0:08) | F-A lists of types or reasons |
| **SM-2** | Rule chapter | The rule's name as a title on W-paper: `ink` Montserrat 900 64 px at y 230, above the example card; or burned on the first example card's photo in `primary` | F-B, every rule |
| **SM-3** | Series lockup | P-SERIES-LOCKUP once, after the hook (§24) | Series reels |
| — | `none (spoken only)` | No marker | F-A pure stories (v01, v04) |
One marker style per reel; numbering ascending.

### 7.3 Unit ritual
**F-A scene / persona ritual (identical for every item):**
1. **0 f** cut (T-1 or T-2) to the item's establishing shot (wide, 1.0–1.5 s); a persona's grade starts on this cut; SM-1 "#N." for 15–24 f.
2. **On the name word:** a persona label duo title (script "The" + BLOCK NAME, z8), held 0.6–1.0 s; or for places the place name as a card title.
3. **2–4 action shots** of 0.8–1.5 s each, one per noun or verb in the description, CS-1 running.
4. **One support visual** on the item's defining habit: a UI chip, a floating panel, a phone reel, or an E1 behind-head word.
5. **The punch line** as a duo (script + block on the punch word, "They care **STORY**") or a script aside.

**F-B rule ritual (identical for every rule):**
1. **On the rule's ordinal or name word:** G-3 paper cut to W-paper; the SM-2 rule title blur-slides in (4 f) at y 230.
2. **f+8:** the example card (L-card43 or a 9:16 paper card) is already at rest; its clip plays.
3. **On the word naming the feature:** P-GUIDE-LINES draw (10 f), then P-INK-ARROWS or P-INK-OVAL (10 f); ≤ 3 marks.
4. **After 1.5–3.0 s on paper:** hard cut to a demonstration clip (the creator applying the rule on location, 2–4 s) or the talking piece.
5. **Second case (optional):** a second example slides in (P-CARD-CAROUSEL, T-5) when the rule names two cases.

### 7.4 Open loops and re-hooks
- **Loops used:** thesis loop (asked in the hook, answered in PAYOFF); count loop ("3 types" → exactly 3 items); result loop (F-B: "by the end…" → the after polaroid); the bookend loop (visual).
- **Payoff rule:** every loop is closed on screen before the CTA (H11).
- **Re-hook (standard class):** one, at **43–53% of runtime**: the thesis keyword repeated as a duo title (v04 @ 0:13 "CHANGED / MY LIFE"), a count-up, or the "BUT…" turn duo. Tag that beat `rehook: true`. With `rehook_every_s: 40`, the gaps hook-end → re-hook and re-hook → CTA must each be ≤ 40 s; reels over 85 s get a second re-hook at ~75%.
- **Intro cap:** hook + series lockup ≤ 15% of runtime (≤ 9 s on a 60 s reel).

### 7.5 Rhythm and energy curve
- The curve is **cinematic-flat with peaks**: hook (peak) → setup (calm, awe shots, no type 1–2 s) → scenes (alternating places/personas) → turn (a dip: slow push, one script aside) → payoff (peak: count-up, polaroid, behind-head word) → CTA (confident, poster) → bookend (calm loop).
- **Light comedy** (tone `comedy: light`): one deadpan beat per 20–30 s: a persona's exaggerated habit, a staged reaction, a dry script aside ("…riveting"). Never two in a row; never on the CTA; no meme cues, no stickers.
- The last item escalates: the biggest scene, a behind-head word or the poster.

### 7.6 Cadence (state changes)
| Token | F-A | F-B | Evidence |
|---|---|---|---|
| `sc_per_10s` | 5–12 | 5–12 | Scene detection at full rate (thr 0.2): 4.8–8.4 picture changes per 10 s (v02 4.8, v03 5.3, v05 6.0, v04 7.1, v01 8.4) + subtitle swaps (0.5) + type beats |
| `hook_sc_3s` | 6 | 6 | v01 hook: 8 type beats in 3 s |
| `max_gap_s` (weight ≥ 1) | 3.0 | 3.0 | v04 @ 0:42–0:47 holds one shot ~6 s: allowed only with a duo title or a Z-2 slow push starting inside it |
| `hook_max_gap_s` | 0.8 | 0.8 | type beats every 0.17–0.5 s |
| `max_static_s` | 2.5 | 2.5 | footage is continuous motion |
| `caption_weight` | 0.5 | 0.5 | support captions |
| `cuts_per_min` **(DNA)** | 27–51 | 27–42 | v01 51.3, v02 37.9, v04 26.7 · v03 28.2, v05 39.1 |
| `median_shot_s` | 0.85–1.6 | 0.9–1.6 | 0.87–1.59 (full-rate re-measure: 0.67–1.79, pooled 1.04 s, p90 3.2 s) |
| Long holds | 1–2 per reel | 1–2 per reel | Single shots of 4.0–6.8 s exist only as the hook mirror (v01 0–4.0), a slow-push hold (v04 @0:42–0:47), the CTA poster (v02 @0:52.5–0:58.5) or the end (v03 @0:59.9, v04 @1:19.8); each carries Z-2 or continuous subject motion + a typed / duo line |

Cuts count from the cut map, scene `cuts` and `transitions` (card swaps, carousel slides, spins, paper cuts): declare them.

---

## §8 Visual system: type, footage, paper and patterns

### 8.1 Graphics role and budget
- `graphics: support`: type, paper cards and ink illustrate the speech; footage carries the story.
- **Pattern count: 41** (support range 20–45).
- Runtime share beyond the subtitle: duo titles 10–18%; paper world F-A 0–30%, F-B 20–45%; ink ≤ 8 marks per 60 s.
- ≥ 4 families per 60 s. **Numbers become pictures:** every spoken count is a P-COUNT-UP or a counted visual (one detail shot per item); never a number only in the subtitle.

### 8.2 Families
| ID | Family | Source class | The buyer supplies |
|---|---|---|---|
| B-1 | Duo type (script + block) | engine | — |
| B-2 | Behind-head type | engine + matte | matted takes with headroom (SH-11) |
| B-3 | Kinetic lockups (title, counter, echo, end block, marker) | engine | — |
| B-4 | Paper cards (9:16, 4:3, riffles, carousels, spin) | engine frame + buyer-owned clips | the clips inside (SH-4, SH-10) |
| B-5 | Polaroids on grid paper | engine frame + buyer-owned photos | photos / stills (SH-9, SH-4) |
| B-6 | Devices and UI (app device, phone reel, chips, panels) | buyer-owned screen recordings; else created generic UI | screen recordings (SH-8) |
| B-7 | Ink and guides | engine | — |
| B-8 | Graded persona scenes | buyer-owned footage + engine grade | staged scenes (SH-6) |
| B-9 | Poster / silhouette | engine backdrop + matte | profile take with back light (SH-12) |
| B-10 | Chaos burst | engine over buyer footage | — |
| B-11 | Brand and series | buyer-owned logo files; else a type-set logo plate | logo PNG/SVG, series logo (optional) |
| B-12 | Location B-roll and shot devices | buyer-owned | SH-1…SH-7 |
| B-13 | Third-party references | **creator-supplied third-party** (another creator's reel, an artwork, a product page); else created (quote card, recreated UI, silhouette) | only what they own or hold |

### 8.3 Pattern specs
Frames are at 30 fps. "Lands" = fully in. Every text pattern sets `text_class`.

**Type and titles (B-1, B-2, B-3)**
| ID | Name | Type | On screen | Motion recipe | When | Family · class | Needs |
|---|---|---|---|---|---|---|---|
| **P-DUO-TITLE** | Duo title | overlay | Script connectors + yellow Anton block, 1–2 block words per beat, ≤ 2 lines | Block blur-slide in 4 f (lead 2 f), hold 0.4–0.6 s, blur-slide out 4 f; script write-on 8 f | Hook, thesis lines, persona labels, the turn | B-1 · TC-display | z8, `kind: lockup` |
| **P-DUO-CORNERS** | Corner duo | overlay | Block centred in the top band; leading script words in the two top corners, trailing words at the block's bottom corners | Corner words write on in sequence (8 f each, 4 f apart); block as P-DUO-TITLE | Question hooks over a symmetric wide (v05 hook) | B-1 · TC-display | z8 |
| **P-WORD-RELAY** | Word relay | overlay | One block line whose words arrive one per spoken word and leave together | Each word blur-slides in on its onset; the line leaves as one (4 f) | A thesis spoken fast (v01 "SHOPPING / IN / PERSON") | B-1 · TC-display | z8 |
| **P-DUO-STACK** | Duo stack | overlay | Two block lines (line 1 230 px, line 2 150–170 px) + one script line under them | Line 1 in, line 2 word by word, script line writes along the bottom (v05 "LOVING / THE PICTURES / You got of her?") | The hook's final beat | B-1 · TC-display | z8 |
| **P-SCRIPT-ASIDE** | Script aside | overlay | A script phrase alone in the top band ("And something…", "trends") | Write-on 8 f, hold 1.0–2.0 s, fade 6 f | A soft transition line, a thought, a dry aside | B-1 · TC-display | z6 |
| **P-BEHIND-WORD** | Behind-head word | overlay (depth) | One Anton block word 200–340 px behind the head, ≥ 65% visible | Blur-slide in 4 f behind the matte; drifts 8–12 px against the head over its hold; out 4 f | One keyword per 20–60 s on a matted headroom take | B-2 · TC-display | `behind: true`, `exception: "E1"`, matte |
| **P-BEHIND-LOCKUP** | Behind lockup | overlay (depth) | Script line in front (above the head, clear of it) + block word behind ("We're emotional / BEINGS") | Script writes 8 f, block blur-slides in behind 6 f later | A thesis line on a talking piece | B-2 · TC-display | two scenes: script z6 front, block `behind` E1 |
| **P-TITLE-LOCKUP** | Title lockup | overlay | Montserrat 900 two-line yellow title in the title band | Lines squash-in (scaleY 0.05 → 1) 3 f, 2 f stagger; hold 2–4 s; leave on the cut or blur-out 4 f | HA-05 hooks, chapter titles over footage | B-3 · TC-display | z6, `kind: lockup` |
| **P-COUNT-UP** | Count-up | overlay | Montserrat 900 digits appending left to right (3 → 36 → 365) + unit stack | A new digit every spoken beat or 6 f, each digit blur-slides in 4 f; unit lines blur-slide in 4 f, 4 f stagger | Any milestone or count (HA-08, payoff) | B-3 · TC-display | z6 (or `behind` E1), `kind: counter` |
| **P-ECHO-OUTLINE** | Echo outline | overlay | The phrase 4 lines: filled, outline, filled, outline | Lines rise 6 f with 3 f stagger; hold 0.8–1.2 s | A repeated key phrase ("cinematic images") | B-3 · TC-display | z6 |
| **P-HASH-MARKER** | Hash marker | overlay | "#N." in the caption band (SM-1) | Hard in on the cut, 15–24 f | Every list item in F-A | B-3 · TC-label | caption band; hide the subtitle with `captions.overrides` |
| **P-CTA-KEYWORD** | Keyword CTA | overlay | "Just comment" script + KEYWORD block 230 px + "to get it" script | Enter the poster by T-11; the lead-in sentence types on in EB Garamond italic 600 64 px `primary` at y ≈ 450, **2 chars/f** (v02 @0:52.53 "So if you'…"), then the P-DUO-TITLE recipe; the keyword holds ≥ 1.5 s | `comment_keyword` CTA | B-1 · TC-display | z8, `kind: cta-keyword` |
| **P-END-BLOCK** | End block | overlay | 4–7 lines of Montserrat 900 filling x 64–1016 over a texture close-up | Lines blur-slide in 3 f apart (line 1 at 0); hold 2.5–4.0 s | `link_bio` / `end_card` CTA (v03 @ 1:22) | B-3 · TC-display | z8, `kind: end-card` |
| **P-SIGNOFF-SUN** | Sign-off sun | overlay (depth) | A giant `soon` gradient block word (yellow → orange) behind the silhouette on the sun backdrop + a script line above | Script writes 8 f; the word rises 10 f behind the matte | The last spoken sign-off of an F-A reel ("See you SOON", v02 @ 0:57) | B-9 · TC-display | `behind` E1 + P-POSTER-BACKDROP |

**Paper world (B-4)**
| ID | Name | Type | On screen | Motion recipe | When | Family · class | Needs |
|---|---|---|---|---|---|---|---|
| **P-PAPER-CARD** | Paper card | stage | A 9:16 creator clip in a rounded card on W-paper with a burned yellow title | Paper cut (G-3, 0 f) with the card at rest, or G-1 shrink (12 f); title blur-slides 4 f at f+8; card leaves by a hard cut (v04 @0:27.9; T-6 fade is an alternate) | An example, a past post, a reference (v03 @ 0:11–0:14) | B-4 · TC-display title | `veos asset add` clip or L-card916 |
| **P-SPIN-CARD** | Spin-to-vertical | stage | A 16:9 (horizontal) clip as a rounded card (radius 28) on plain black, still playing, that turns a quarter and grows until the now-portrait picture covers the frame | Measured v03 @0:06.45–0:11.0 (`strip-spin-card-90.jpg`): card w 900 at rest 0–8 f, then rotates **0 → 90°** clockwise while scaling **0.55 → ≈ 2.0** (cover) over **75–135 f** (2.5–4.5 s), ease-in-out; the subtitle keeps running; hard cut out | The line about horizontal → vertical, "the old way", a perspective change (≤ 1 per reel) | B-4 | video asset; declare the rotation span in `events` |
| **P-RECAP-RIFFLE** | Recap riffle | stage | 9:16 cards with their own burned titles, one per **0.5–0.6 s**, on W-paper | Hard cut into the first card at rest; hard swap of the card content and title every **14–18 f** (measured 0.50–0.58 s, v04 @0:19.3–0:28.4, `strip-recap-riffle.jpg`), the frame never moves; out by a hard cut | Year recaps, "everything I made", past episodes (v04 @ 0:19–0:27) | B-4 · TC-display | one asset per card; `cuts` per swap |
| **P-CARD-CAROUSEL** | Carousel | stage | 9:16 cards sliding horizontally on W-grid; the active card centred (x 176), the next peeking at x 1000 | Slide 8 f ease in-out per step (T-5), 1.0–1.5 s per card | Two to four examples of one idea (v02 @ 0:29–0:31, 0:49–0:51) | B-4 | assets; `cuts` per step |
| **P-LANDSCAPE-CARD** | Landscape card | stage | A 4:3 example card on W-paper with guide lines and ink | Paper cut; card at rest; guides draw 10 f; ink 10 f | F-B rules about framing, before/after on one card (v03 @ 0:24–0:27) | B-4 | L-card43 or asset |
| **P-FLOAT-CARDS** | Floating cards | overlay | 3–6 small 9:16 cards (180–260 px wide, radius 16) floating around the presenter on a light set, each a different example | Cards pop in 6 f with 4 f stagger, drift 10–20 px/s, exit by blur 6 f | "All of these", a community, a body of work (v02 @ 0:27, 0:41–0:42) | B-4 | assets; ≤ 4 at once (G2) |

**Polaroids (B-5)**
| ID | Name | Type | On screen | Motion recipe | When | Family | Needs |
|---|---|---|---|---|---|---|---|
| **P-POLAROID** | Polaroid | stage | A white-bordered photo or clip (24 px `frame` border) on W-grid, tilted −2.5…+2.5° | Enters and leaves through the **T-10 flash** (v01 @0:28.93, 0:31.01; v05 @0:26.38): already at rest with a 1% scale / 0.2° settle over 3 f; photos inside riffle by hard swap every 0.5–1.0 s; no push | A moment, a memory, a "look at this", an after-state (v02 @ 0:45–0:48, v05 @ 0:23–0:25) | B-5 | asset |
| **P-BEFORE-AFTER-POLAROID** | Before/after | stage | Before polaroid, then the after polaroid in the same rect | Before holds 1.0–1.5 s; hard swap of the photo (a cut) on the "after" word; after holds ≥ 1.5 s | F-B RESULT, transformation payoffs (v05 @ 0:57–1:00) | B-5 | two assets (SH-9) |

**Devices and UI (B-6)**
| ID | Name | Type | On screen | Motion recipe | When | Family · class | Needs |
|---|---|---|---|---|---|---|---|
| **P-APP-DEVICE** | App device | stage | A dark rounded device frame with the screen recording, on W-grid | Device rises 10 f; on the button word the camera of the scene scales the device 1.0 → 1.8 toward the control over 12 f, the rest blurs 8 px; back over 10 f | Every app or tool step (v05 @ 0:30–0:54) | B-6 | SH-8 asset; else FB-8; `insert` record |
| **P-PHONE-REEL** | Phone reel | stage | A portrait phone frame showing a reel, a yellow P-INK-OVAL around the caption or UI region | Phone at rest on W-paper; oval draws 10 f on the word | Talking about posts, captions, a platform (v03 @ 1:10–1:15, v04 @ 0:48–0:53) | B-6 | creator screen capture; else created `fx.appUI({kind: "video"})`; `insert` record |
| **P-UI-CHIP** | UI chip | overlay | A search bar pill or a button pill ("BUY NOW") over footage | Pop 6 f (scale 0.9 → 1.0 + blur 8 → 0), hold 1–2 s, out 4 f | A search, a purchase, a click habit (v02 @ 0:12, 0:17) | B-6 · TC-label | z6 |
| **P-FLOAT-PANEL** | Floating panel | overlay | A tall list card (product list, checklist) floating beside the subject, tilted 6° | Slides in from the edge 10 f, drifts 10 px | A persona's habit shown as a list (v02 @ 0:10–0:11) | B-6 · TC-decorative inside + TC-label heading | z5, never on the face |

**Ink and guides (B-7, §22)**
| ID | Name | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|---|
| **P-GUIDE-LINES** | Guide lines | annotation | A 3 px white (75%) centre line, or a 3 × 3 grid, over footage or a card | Lines draw from the top 10 f; hold for the rule | Composition, alignment, "the centre", "thirds" (v03 @ 0:20–0:36) | anchor pass |
| **P-INK-ARROWS** | Ink arrows | annotation | 1–4 hand-drawn `primary` arrows converging on the subject | Shaft 8 f, head 3 f, 4 f stagger, slight wobble | "Look at", "here", "the subject" (v03 @ 0:22, 0:48) | anchor pass |
| **P-INK-OVAL** | Ink oval | annotation | A hand-drawn `primary` oval (5–7 px) around a region | Draw 10 f with a 15° overshoot | A caption area, an object, a detail (v03 @ 0:58, 1:10) | anchor pass |
| **P-LASSO** | Lasso | annotation | A thick white (8 px) outline tracing an object being removed or selected | Draw 12 f along the object's outline | Erase / select / cut-out steps (v05 @ 0:36–0:37) | anchor keyframes |

**Footage devices and grades (B-8, B-12)**
| ID | Name | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|---|
| **P-FRAME-IN-FRAME** | Frame in frame | cut | The opener seen through a mirror, door, window or screen | — (shot selection); Z-1 if static | SH-1 hook shot; any reveal (v01 @ 0:00, 0:08) | SH-1 |
| **P-DETAIL-RUN** | Detail run | cut | One 0.6–1.0 s detail shot per listed noun | Cut on each noun's onset (R-3) | "every colour, every shape, every…" (v01 @ 0:18–0:25) | SH-4 |
| **P-PERSONA-GRADE** | Graded persona | footage-treatment | A staged persona scene with its grade (GR-mono / amber / teal) and a label duo | Grade starts on the cut; label duo on the name word | "N types of X", before/after selves (v02 @ 0:03–0:23) | SH-6 + GR-L |
| **P-WALK-BOOKEND** | Walk bookend | cut | The creator walks in on f0 and walks out of the same frame at the end | — | F-A openers and closers (v04 @ 0:00, 1:23) | SH-3 |
| **P-SNAP-RUN** | Snap run | cut | 2–4 poses of the subject being photographed, each a new shot | One T-10 flash per pose, 10–17 f apart (≤ 3 flashes per s); a shutter / click cue may sit on each flash | "snap the best photos of her", any photo-taking line (v05 @0:16.86–0:18.0, `strip-shutter-flash.jpg`) | SH-4 / SH-6 poses |

**Poster, chaos, brand, references (B-9 … B-13)**
| ID | Name | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|---|
| **P-POSTER-BACKDROP** | Poster backdrop | overlay (depth) | The matted creator (profile) in front of a drawn `accent` sun disc or colour wall, with a duo keyword behind or beside | Backdrop is a `behind: true` z2 scene drawing W-poster's gradient full-frame (the cut-out stays in front); hard cut in | CTA, thesis poster (v02 @ 0:39–0:40, 0:52–0:58) | SH-12, clean matte (FB-12) |
| **P-CHAOS-BURST** | Chaos burst | overlay (E2) | GR-mono footage with a 3–5 hard-cut flurry, 4–6 snippets ("[Close Up]", "[Wide]", phrase fragments) around (never on) the face | ≤ 45 f total (the source runs ≈ 4 s, v02 @0:04.3–0:08.2; the E2 cap keeps 1.5 s); snippets **type on 1 char/f** at three depths (big foreground ones blurred 6–10 px, mid sharp, small back ones), 4–6 f stagger, drift 20 px/s; shots change every 8–12 f, each joined by **one pure-white frame** (T-10 burst variant, v02 @0:06.79, 0:07.17, `strip-chaos-flash-typewriter.jpg`); a duo inside it blurs out in place; ends with a T-13 whip, a cut or T-7 vortex | One line about overload, doubt, too many options (v02 @ 0:04–0:08) | `exception: "E2"`, `snippets` declared |
| **P-LOGO-CHIP** | Logo chip | overlay | "With" script + the brand's logo file + wordmark (white) in the top band | Logo pops 6 f, wordmark blur-slides 4 f, script writes 8 f | Sponsor or tool named (v05 @ 0:08) | creator logo file; else `fx.logoPlate`; `insert` record |
| **P-SERIES-LOCKUP** | Series lockup | stage | Gold script + gold block + "ep. NN" on W-grid without grid | Script writes 10 f; block blur-slides 4 f; hold 1.2 s; cut | Once per series reel, right after the hook (v05 @ 0:09) | §24 |
| **P-DISCLOSURE** | Disclosure | overlay | "Paid partnership" TC-legal line | Fade 6 f; hold ≥ 2 s | Every sponsored segment (NC-12) | §25 |
| **P-REF-CARD** | Reference card | stage | Someone else's work (a reel, an artwork, a product page) in a paper card | Paper cut; card at rest; optional guide line / oval | "Iconic paintings…", "this creator did…" (v03 @ 0:51–0:54) | creator file; else created (§12.5); `insert` record |

### 8.4 Line → pattern lookup `[NICHE]`
| Line type | Primary | Alternates | [NICHE: example] fitness | [NICHE: example] travel |
|---|---|---|---|---|
| Thesis / opinion | P-DUO-TITLE | P-DUO-STACK, P-BEHIND-LOCKUP | "Training **ALONE** is why you **STOPPED**" | "The best **FOOD** has **NO MENU**" |
| Question to the viewer | P-DUO-CORNERS | P-DUO-TITLE | "Is your **SQUAT** still **HURTING** your knees?" | "Is your **PHONE** still taking **BORING** photos?" |
| "N types / N rules / N reasons" | P-DUO-TITLE with the number as a block + SM-1 | P-COUNT-UP | "**3** types of **GYM** people" | "**4** rules for **STREET** photos" |
| A milestone or count | P-COUNT-UP | P-BEHIND-WORD (number) | "100 → 100 DAYS" | "52 → 52 CITIES" |
| Arriving somewhere / a place | P-FRAME-IN-FRAME + card title on a P-PAPER-CARD | P-WALK-BOOKEND | the gym door | the homestay door |
| Taking photos, posing | P-SNAP-RUN | P-POLAROID via T-10 | the post-workout mirror shots | portraits at a doorway |
| Listing nouns | P-DETAIL-RUN | P-RECAP-RIFFLE | chalk, straps, the bar, the clock | spices, steam, bowls, the cook's hands |
| A persona or "type" | P-PERSONA-GRADE + label duo | P-FLOAT-PANEL | "The **EGO LIFTER**" (GR-amber) | "The **CHECKLIST TOURIST**" (GR-teal) |
| A habit shown as a list or a search | P-UI-CHIP | P-FLOAT-PANEL | "best pre-workout" search pill | "top 10 cafés" search pill |
| Doubt, overload, too many options | P-CHAOS-BURST (once) | P-SCRIPT-ASIDE | "am I doing it wrong?", "[Form check]" | "[Itinerary]", "too many tabs" |
| A rule with a frame or alignment | P-LANDSCAPE-CARD + P-GUIDE-LINES | P-PAPER-CARD + P-INK-ARROWS | knee over the toe line | horizon on the third |
| "Look at this / here" | P-INK-OVAL | P-INK-ARROWS | the hip crease | the person in the frame |
| An app or tool step | P-APP-DEVICE | P-LOGO-CHIP | a workout tracker setting | a photo editor slider |
| Remove / select / cut out | P-LASSO | P-INK-OVAL | — | the tourist behind her |
| Before → after | P-BEFORE-AFTER-POLAROID | P-POLAROID ×2 | form before / after | photo before / after |
| A past post or episode | P-PAPER-CARD | P-RECAP-RIFFLE | last month's transformation | last trip's reel |
| Someone else's work | P-REF-CARD (creator file, else created) | P-PHONE-REEL | a coach's viral post (quote card) | a famous photograph (silhouette card) |
| A key phrase repeated | P-ECHO-OUTLINE | P-DUO-TITLE | "PROGRESSIVE OVERLOAD" | "SLOW TRAVEL" |
| The turn ("but…", "then it changed") | P-DUO-TITLE (re-hook) | P-BEHIND-WORD | "**BUT** I was **WRONG**" | "**THEN** it **RAINED**" |
| A feeling, quiet moment | no type: Z-1 push-drift, CS-1 only | P-SCRIPT-ASIDE | sunrise run | a train window |
| Sponsor or tool named | P-LOGO-CHIP + P-DISCLOSURE | — | the shoe brand | the booking app |
| CTA (comment) | P-CTA-KEYWORD on P-POSTER-BACKDROP | P-CTA-KEYWORD on footage | "Just comment **PLAN**" | "Just comment **MAP**" |
| CTA (link / part 2) | P-END-BLOCK | — | "FREE PLAN / LINK IN BIO" | "PART 2 / FOLLOW" |
| Sign-off | P-SIGNOFF-SUN or the bookend | P-WALK-BOOKEND | "See you **TOMORROW**" | "See you **THERE**" |

### 8.5 Data and truth
- Data figures are OFF (§18); counters show only numbers that are spoken or in the script (H18), written as digits.
- Counts are countable: "3 types" shows 3 items; a "52 films" count-up lands on 52.
- App screens are the creator's recordings; a created UI is generic, unbranded (NC-6).
- Before/after photos are the creator's real results; never simulate an "after".

### 8.6 Comedy layer `[COND: comedy = light]`
- **Allowed:** staged persona exaggeration (the shot itself), a deadpan script aside, an ironic UI chip ("best camera to buy" typed by the gear persona), a reaction shot.
- **Not allowed:** stickers, stamps, meme cues, emoji, crash zooms, freeze-frame roasts.
- **Budget:** ≤ 1 comedy beat per 20 s, never two in a row, never in the CTA or the hook's first 2 s.

### 8.7 Asset rules
- **Real captures first:** the creator's own footage, photos, screen recordings and past posts.
- **Allowed mocks:** generic, unbranded UI built with `fx.device` / `fx.appUI`, the search pill and button pill (UI chips are generic shapes, not a brand's UI).
- **No stock clichés:** no stock B-roll, no generated "cinematic" scenes, no drone stock.
- **Logos:** only the creator's files (their own brand, a sponsor's supplied logo); otherwise a type-set logo plate (`fx.logoPlate`).
- **Third-party moments:** ask, then create (§12.5).

### 8.8 Density and variety
- An event (cut, type beat, card swap, ink mark) every 0.6–1.6 s.
- ≥ 8 distinct patterns and ≥ 4 families per 60 s.
- The same pattern ≤ 2 beats in a row, except the F-B rule ritual and P-RECAP-RIFFLE.
- ≤ 1 behind-head word per 20 s; ≤ 1 chaos burst per reel; ≤ 2 poster beats per reel.

---

## §9 Transitions & shot grammar `[DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-1** | Hard cut | 0 | The default (≈ 75% of all cuts) | none |
| **T-2** | Cut on motion | 0 | Cut inside a gesture, a turn, a whip or a walk, so the motion continues into the next shot (v02 @ 0:02.5 the hand "3", 0:25) | whoosh (optional) |
| **T-3** | Blur-through | 4–6 | An out-of-focus foreground object (a wheel, a shelf, a hand) wipes the frame in-camera; if the source has none, a 6 f vertical motion blur ramp 0 → 30 px on the outgoing shot and 30 → 0 on the incoming one (built-in footage blur, §9.5) | whoosh |
| **T-4** | Spin-to-vertical | 75–135 | P-SPIN-CARD (§8.3): 0 → 90°, 0.55 → 2.0, ease-in-out | whoosh |
| **T-5** | Card slide | 8 | Carousel step on W-grid, ease in-out | soft swish |
| **T-6** | Card fade-out | 4 | Alternate only: a paper card fades out on cream, then the next shot cuts in (the measured exit at v04 @0:27.9 is a hard cut into a wheel detail) | none |
| **T-10** | Flash | 5–6 | Exposure bloom: outgoing brightens over 2 f (brightness 1 → 2.5), cut at the white peak, incoming starts blown out and decays to normal over 3 f (v01 @0:28.93 into polaroids, 0:31.01 out; v05 @0:16.86, 0:17.32 one per "photo", 0:26.38; `strip-shutter-flash.jpg`, `strip-flash-polaroid-exit.jpg`). Inside the E2 burst it is a single pure-white frame between shots (v02 @0:06.79, 0:07.17) | shutter / camera click on photo beats, else none |
| **T-11** | Warm flash | 5 | As T-10 but tinted cream-yellow (`#FFF6C8`), 4 f build, cut at the peak into the poster (v02 @0:52.24–0:52.45, `strip-warm-flash-cta.jpg`) | soft whoosh / shine |
| **T-12** | Zoom-through on a gesture | ≈ 4 + 24 | Outgoing: punch-in ≈ 1.0 → 1.6 on the gesture (a raised hand) over 4 f with zoom blur, type layer included; hard cut on the gesture to a shot whose gesture sits in the same place; incoming pulls out ≈ 2.3 → 1.0 over ≈ 24 f, expo-out (ORB per-frame scale 0.91 → 0.997; v02 @0:02.40–0:03.55, `strip-zoom-through-gesture.jpg`) | whoosh |
| **T-13** | Whip pan | 6 + 14 | In-camera: outgoing whips sideways with heavy horizontal smear for 5–6 f; incoming lands still panning, ≈ 130 px/f decelerating to 0 over ≈ 14 f (≈ 750 px total, ORB v02 @0:08.48–0:08.94, `strip-whip-pan.jpg`); the "#N." marker lands mid-whip | whoosh |
| **T-7** | Vortex | 8 | Radial zoom blur tunnel on the last 8 f of a shot (scale 1 → 1.4, radial blur 0 → 24 px), cut to a calm shot (built-in `zoom-blur`, §9.5) | whoosh |
| **T-8** | Paper cut | 0 | G-3: footage → W-paper with the card already at rest | none |
| **T-9** | Hard end | 0 | The bookend's last frame, ≤ 6 f after the last word | none |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| f0 | A moving shot (no transition) | A fade-in, a black frame |
| Hook → body | T-2 cut on motion (2.7–4.0 s) | A morph, a fade |
| New scene / persona / place | T-1 or T-2 | A dissolve |
| Footage → paper | T-8 paper cut (or G-1 shrink for "this is the example") | A cross-fade |
| Paper → footage | T-1 cut (default), T-10 flash out of a polaroid run, or T-6 fade-out then cut | A wipe |
| Footage ↔ polaroid / photo world | T-10 flash in and out | A slide |
| "Snap" / photo-taking line | T-10 on every cut to a new pose (one flash per photo, 0.4–0.7 s apart) | More than 4 in a row |
| Hook → first item ("3 types…" with a hand count) | T-12 zoom-through on the gesture (≤ 1 per reel) | Without a gesture to cut on |
| Persona → persona, place → place | T-13 whip pan when at least one of the two shots was filmed with a whip (the built-in whip completes the other side), else T-1 | A digital whip between two locked-off shots |
| Into the CTA poster | T-11 warm flash | A plain fade |
| Card → card | T-5 slide (carousel) or a content cut (riffle) | A spin |
| Flashback, "the old way", a chapter | T-4 spin-in (≤ 1 per reel) | — |
| Out of the chaos burst | T-7 vortex or T-1 | Another chaos device |
| Last word | T-9 on the bookend picture | A black tail, a fade to black |

### 9.3 Shot grammar `[COND: spine hybrid]`
| ID | Rule |
|---|---|
| **R-1** | Cut on the visual idea, not on every word: one picture change every 0.85–1.6 s in B-roll runs; a talking piece holds ≤ 4 s before a cutaway |
| **R-2** | Cut on motion: a gesture, a turn, a step or a whip continues across the cut within ±2 f (T-2) |
| **R-3** | A list of nouns gets one 0.6–1.0 s detail per noun, cut on each noun's onset (P-DETAIL-RUN) |
| **R-4** | Return to the presenter on the opinion, the turn word or the CTA; never mid-clause |
| **R-5** | A persona opens with a 1.0–1.5 s establishing wide, then medium action, then the label duo |
| **R-6** | Change location at least every 10–15 s in F-A (a new place, set or persona) |
| **R-7** | Type beats follow words; cuts follow pictures. Never cut inside a block's 4 f blur-slide; move the cut ≤ 3 f |
| **R-8** | The bookend: the final 1.0–1.5 s plays SH-1's pre-roll so the last frame is frame 0's picture (§23) |
| **R-9** | Walk-in / walk-out: the creator enters the opening frame within 0.5 s and leaves the closing frame in its last 1.5 s when SH-3 exists |

### 9.4 Budget (per 60 s, scaled by runtime)
- T-1 / T-2: as needed (27–51 cuts/min). T-3 ≤ 3. T-4 ≤ 1 per reel. T-5 ≤ 6. T-6 ≤ 2. T-7 ≤ 1 per reel. T-8 every paper entry. T-10 ≤ 6 (≤ 4 in a row on a photo run). T-11 ≤ 1 per reel. T-12 ≤ 1 per reel. T-13 ≤ 3.
- The same non-cut transition never 3× in a row (except a P-SNAP-RUN's T-10 flashes).

### 9.5 How the transitions render (built-in `timeline.transitions[]` with a `type`; `renderer/transitions.js`)
Core draws these over the picture (world, footage, behind-words, scenes z1–6) and under the captions and duo titles unless `layers` says otherwise. Never write them as z4 / z11 scenes. V-FX checks the fields.

| ID | Timeline entry (measured values) |
|---|---|
| T-10 | `{"t": <cut>, "type": "flash", "frames": 6, "pre": 2, "peak": 0.9, "decay": 1.6}`: 2 f build, white peak on the cut, 3 f decay (v01 @0:28.93, v05 @0:16.86). **Burst variant** (inside P-CHAOS-BURST): one pure-white frame, `{"t": <cut>, "type": "flash", "frames": 1, "pre": 0, "peak": 1}` |
| T-11 | `{"t": <cut>, "type": "flash", "colour": "#FFF6C8", "frames": 7, "pre": 4, "peak": 0.9}`: 4 f cream build, cut at the peak into the poster, short decay (v02 @0:52.24) |
| T-12 | Two built-ins on the same cut. **Outgoing:** `{"t": <cut>, "type": "zoom-blur", "frames": 6, "pre": 4, "amount": 0.3, "punch": 0.4, "at": [<gesture x>, <gesture y>], "layers": "all"}` (4 f punch with zoom blur, type layer included; the engine caps `punch` at 0.4, so the punch reaches 1.4× where the source reaches ≈ 1.6×). **Incoming:** the camera landing Z-4 on the cut, `{"t": <cut>, "preset": "zoom-land", "p": {"origin": {"x": <gesture x>, "y": <gesture y>}}}` (1.5 → 1.0 over 24 f, `expoOut`, radial blur decaying with it). The source pulls out from ≈ 2.3×; V-CAMERA's `slow_push` landing exemption allows at most 1.5×, so the landing starts at 1.5. Cut on the gesture (T-2) so it sits in the same place in both shots; needs ≥ 1.5× headroom (4K, or 1080p with the base reframe at 1.0), else plain T-2 |
| T-13 | `{"t": <cut>, "type": "whip", "dir": "left", "frames": 20, "pre": 6, "px": 90, "travel": 750, "blend": 0}`: 6 f smear out, the incoming shot arrives ≈ 750 px off and decelerates over 14 f; no cross-blend (the source cuts at the blur peak). Match `dir` to the in-camera whip direction. Use it on in-camera whip pairs (it evens out the smear) or when one of the two shots was whipped; never between two locked-off shots (§9.2) |
| T-3 (no in-camera blocker) | `timeline.blur`: `{"t": <cut − 3 f>, "kind": "directional", "angle": 90, "px": 30, "frames": 6, "shape": "pulse"}`: vertical smear 0 → 30 px into the cut and 30 → 0 out of it, footage only |
| T-7 | `{"t": <cut>, "type": "zoom-blur", "frames": 9, "pre": 8, "amount": 0.3, "punch": 0.4}`: the tunnel on the last 8 f (scale 1 → 1.4), then the calm shot cuts in sharp |

---

## §10 Motion, camera, layers, finishing `[DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset |
| Blur-slide in (rise-smear) | 4 f: y + 0.8 × cap height (≈ 150–220 px) → 0, vertical smear 24 → 0 px, opacity 0 → 1, expo-out `cubic-bezier(0.22, 1, 0.36, 1)` (v01 @0:00.59) |
| Blur-slide out | 3–4 f: y 0 → −(110–150) px, smear 0 → 24, opacity 1 → 0, `cubic-bezier(0.64, 0, 0.78, 0)`; last word in leaves first, 1 f apart; script un-writes R→L 4 f |
| Script write-on | 8 f left-to-right clip mask, linear |
| Keyword hold | 0.4–0.6 s per beat; titles 2–4 s |
| Card enter | 6–10 f; card fade-out 4 f |
| Spin card | 75–135 f, 0 → 90°, scale 0.55 → 2.0, ease-in-out |
| Carousel step | 8 f in-out |
| Polaroid entry | via T-10 flash; 3 f settle (1% scale, 0.2°) |
| Flash (T-10) | 2 f up + cut + 3 f decay; burst variant 1 white frame |
| Title squash-in | 3 f per line (scaleY 0.05 → 1), 2 f stagger |
| Typewriter | CTA serif line 2 chars/f; E2 snippets 1 char/f |
| Riffle swap | 14–18 f per card |
| Count digit | 6 f per appended digit when spoken as one number |
| Ink draw | 10 f (arrow shaft 8 + head 3; oval 10 with 15° overshoot) |
| Vortex | 8 f |
| Behind-word parallax | 8–12 px over the hold |
| Hold | Text ≥ 0.25 s per word; titles ≥ 10 f after complete |

### 10.2 Footage camera: zoom policy `slow_push`
| ID | Preset | Recipe | Use |
|---|---|---|---|
| **Z-1** | `push-drift` | 1.00 → 1.06 over the beat (`ease: "linear"`, ≥ 15 f) | A static shot that must feel alive: awe beats, paper-free talking pieces, the hook if SH-1 is static |
| **Z-2** | `slow-push` | 1.00 → 1.06 over 150 f, `ease: "linear"` (measured 1.06 over 5.3 s, ≈ 1.1%/s, v04 @0:42.4–0:47.6, `strip-slow-push.jpg`) | A hold > 3 s: the turn, a confession, the closing talking piece |
| **Z-3** | `reset` | back to 1.00 (4 f) on a cut | Only on a cut |
| **Z-4** | `zoom-land` | landing on a cut: 1.50 → 1.00 over 24 f, `ease: "expoOut"`, `blur: {kind: "radial", amount: 0.18, shape: "decay"}`, `origin` the gesture point (exempt under `slow_push`: starts on a cut, ends on 1.0, ≤ 1.5×) | Only as the incoming half of T-12 (≤ 1 per reel) |
Rules: **the footage is locked off** (ORB scale 1.000 ± 0.003 per frame on v01 @0:00–0:01 and 0:04, v03 @0:00, v05 @1:03–1:07): movement comes from the subject (walk-ins, gestures, cars) or in-camera moves (whips, drone), not from engine zooms; leave a static shot static when its subject moves. Z-1 only when nothing in the frame moves. ≤ 4 Z events per 60 s; never the same preset twice in a row; never two within 0.4 s; never a punch, crash, shake or rotation as a camera event (N4; T-12 is a built-in transition plus the Z-4 landing, §9.5). A 1080p source allows ≤ 1.35× re-crops; 4K allows 2×.

### 10.3 Canvas camera
OFF (§21).

### 10.4 Layer order (back to front)
1. World (W-paper, W-grid, W-void, W-poster) or the blurred footage copy
2. Paper cards, polaroids, devices on L-hidden (z3)
3. Footage group: footage → **behind scenes** (P-BEHIND-WORD, P-POSTER-BACKDROP, P-SIGNOFF-SUN word) → the cut-out
4. GR-L grade layer (z4, until E-16)
5. Card titles, UI chips, floating panels, ink marks (z5–6)
6. Title lockup, counter, script asides (z6)
7. CS-1 subtitle (z7)
8. Duo titles, CTA keyword, end block, chaos snippets (z8; the subtitle hides under them)
9. Legal line (z9, TC-legal)

### 10.5 Finishing
- No grain, no film burns, no resting light-leak overlays (the T-10 / T-11 flashes are transitions). W-paper noise 0.03, W-grid noise 0.04 + vignette 0.42, W-void vignette 0.3.
- Soft shadows only: cards `0 18px 40px rgba(0,0,0,.18)`, polaroids `0 14px 30px rgba(0,0,0,.35)`, device `0 30px 60px rgba(0,0,0,.45)`.
- Glow: none. The only gradient fill on type is the sign-off word (`soon` gradient).
- Card radius: 9:16 cards 40, 4:3 cards 28, device 64, phone 48, floating cards 16, polaroids 2.

---

## §11 Sound contract (minimal) `[VAR]`
Sound comes from the bundled SFX pack and its global rules (S1–S6: every cue marks a visible event, ≤ 2 uses per file, one list-cue exception, no consecutive repeats, catalogue ids only). No per-style palette.

| Line | Decision |
|---|---|
| **Cue moments** | `hook` (one soft cue on the first keyword landing), `transitions` (cut-on-motion, T-13 whip and T-12 zoom-through: whoosh; spin-in, vortex, carousel; T-11 into the poster: soft shine; a camera-shutter click on each P-SNAP-RUN flash), `reveals` (count-up landing, polaroid drop, before → after swap, end block), `cta` (the keyword landing). Duo-title beats after the hook, subtitles and ink marks are silent |
| **Meme cues** | OFF (comedy is `light`) |
| **Music bed** | ON from f0 `(unverified: audio not observable)`; a cinematic or lo-fi bed that rides the whole reel |
| **Ducking** | Bed ≥ 18 dB under the voice while the voice speaks; location sound in B-roll kept at −28 to −22 dB under the voice and ducked with it |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word, on the bookend frame (NC-8) |

Mirrored in `tokens.json → sound`.

---

## §12 Footage, shot list, fallbacks, inserts

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's setups]`
| Setup | Camera and framing | Head top y (output) | Light / set | Notes |
|---|---|---|---|---|
| **A** Location talking piece | Handheld selfie or gimbal at arm's length, 4K preferred, 24/25/30 fps | 250–520 | Natural light, golden hour preferred | 2–5 locations per reel |
| **B** Seated set | Tripod, 50–85 mm look, shallow depth | 420–700 | Warm practicals (lamp, textured wall), dark top | v02 interview set |
| **C** Wide / overhead | Drone, balcony, stairs or tripod high; presenter small | 600–1100 | Composed frame (lines, railings, car, door) | Hook shots, walk-ins |
| **D** Clean-matte headroom | Tripod, plain or distant background, ≥ 300 px above the head | 560–800 | Separation light | Behind-head words (E1), poster |
Wardrobe: solid tops; a signature cap or prop is welcome (it recurs). No mic visible in setups B/D.

### 12.2 Shot list `[DNA]`
| ID | Shot | Spec | Count per 60 s | Must / optional | Formats |
|---|---|---|---|---|---|
| **SH-1** | Opening shot | Moving and composed: mirror, doorway, window, overhead, or a walk-in; 3–5 s **plus 1.5 s pre-roll** before the in-point (the bookend uses it) | 1 | must | F-A, F-B |
| **SH-2** | Overhead / drone | Top-down or high-angle of the presenter at a location, 3–6 s | 0–2 | optional | F-A, F-B |
| **SH-3** | Walk-in / walk-out | Same spot, same framing: the creator enters at the start and leaves at the end | 1 pair | optional | F-A |
| **SH-4** | Location B-roll | Details, hands, products, POV, macro inserts, 1–2 s each, 4K or 1080p | 20–40 | must | F-A, F-B |
| **SH-5** | Talking pieces | 2–5 different setups or locations (A/B) | 2–5 | must | F-A, F-B |
| **SH-6** | Persona scenes | Same person, outfit / prop / place swap, 3–6 s each | 0–4 | optional (must for "types of" reels) | F-A |
| **SH-7** | Signature prop / vehicle | 1–3 s each | 0–6 | optional | F-A, F-B |
| **SH-8** | Screen recordings | The app or tool being taught, portrait, ≥ 1080 px wide | 0–8 | optional (must for app tutorials) | F-B |
| **SH-9** | Before / after | Stills or clips of the real result | 0–2 | optional (must when the topic has a visual result) | F-B |
| **SH-10** | Past posts | Screen captures of the creator's own posts | 0–9 | optional | F-A, F-B |
| **SH-11** | Headroom shot | Setup D, for behind-head words | 1–3 | must | F-A, F-B |
| **SH-12** | Poster shot | Profile or 3/4 against a plain wall with back light | 0–1 | optional | F-A, F-B |
| **SH-13** | Texture close-up | Grass, fabric, water, wall, 3–4 s, for the end block | 0–1 | optional | F-B |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| FB-1 | SH-1 | Open on the most moving wide of the presenter with Z-1 push-drift; the bookend reuses its first 1.0 s (ending on its first frame) | No frame-within-frame surprise | degraded |
| FB-2 | SH-2 | A high-angle phone shot (stairs, balcony); else the title lockup over the widest shot | No aerial scale | degraded |
| FB-3 | SH-3 | Hold an empty plate of the location 0.5 s before the first and after the last talking shot | The entrance/exit is implied | holds |
| FB-4 | SH-4 | Alternate two re-crops of the talking take (≤ 1.35× from 1080p, ≤ 2× from 4K) with paper cards / polaroids of the creator's photos, one change every 1.0–1.5 s | Less location variety; the rhythm comes from crops and cards | degraded |
| FB-5 | SH-5 | One location, two framings (wide / tight) cut on sentence boundaries | No travel feeling | degraded |
| FB-6 | SH-6 | One location with an outfit or prop swap per persona, told apart by GR-mono / GR-amber / GR-teal and a label duo per persona | Less staging | holds |
| FB-7 | SH-7 | Drop the prop beats; use SH-4 details | none structural | holds |
| FB-8 | SH-8 | Created generic UI (`fx.appUI`) inside the P-APP-DEVICE frame | Not the real app | degraded |
| FB-9 | SH-9 | No before/after; the result becomes a P-PAPER-CARD checklist | No visual proof | degraded |
| FB-10 | SH-10 | Recap cards built from SH-4 stills with burned titles | Not the real past posts | holds |
| FB-11 | SH-11 | The word sits above the head on the front layer (40 px clearance), no E1 | No depth sandwich | degraded |
| FB-12 | SH-12 | Matte the best profile take and draw the W-poster backdrop behind it; if the matte fails at 200%, the CTA duo sits over plain footage | Less graphic sign-off | degraded |
| FB-13 | SH-13 | The end block sits on W-void | Flatter end card | holds |
At the checkpoint, list the fallbacks used. If SH-4 gives fewer than 12 clips per 60 s **and** FB-4 cannot reach 27 cuts/min, tell the creator the reel will read as a talking-head edit, and ask for more B-roll before building.

### 12.4 Props, reaction bank, matte, resolution
- **Props:** one signature prop or vehicle per series (optional); the phone with the app open (F-B); outfit / cap swaps for personas.
- **Reaction bank (ask at the shoot, 2–3 s each):** a nod to camera, a laugh off-camera, a turn-and-walk-away, a point to camera, a hand counting fingers (a cut-on-motion source).
- **Matte:** required for E1 and the poster. RobustVideoMatting or Resolve Magic Mask; feather 2 px, choke 1 px; check hair at 200%.
- **Resolution:** a 2× re-crop needs a 4K source; a 1080p source allows ≤ 1.35×. Drone and overhead shots must be ≥ 2.7K to survive the 9:16 crop.

### 12.5 Third-party inserts: ask, then create `[REQ]`
Claude never fetches anyone else's media.
1. **Scan** the transcript (`veos inserts scan`) and list the moments that call for third-party material. In this style they are: another creator's reel or post (P-PHONE-REEL / P-REF-CARD), an artwork or famous photograph (P-REF-CARD), an app's UI (P-APP-DEVICE when it isn't the creator's own recording), a brand logo (P-LOGO-CHIP), a product page (P-FLOAT-PANEL).
2. **Ask once:** "For these N moments, do you have a clip or screenshot? (drop the files, or say no)".
3. **Supplied:** use it as given inside the style's frame (paper card, phone, device), cropped and marked with ink, never altered.
4. **Not supplied: create.** Another creator's reel → `fx.appUI({kind: "video", caption})` in the phone frame; a post → `fx.quoteCard` (verbatim words); an artwork or a person → `fx.silhouette` with the title set in type; an app → `fx.appUI` (generic, unbranded); a logo → `fx.logoPlate`. 
5. **Record** each in `plan/inserts.json` `{id, moment, origin: creator | created, file?, recipe?, substitute_of?}` and pass `insert: "<id>"` on the scene.

### 12.6 Frame rate, audio and how the footage plays
- Output 1080 × 1920, **30 fps CFR**; conform 23.98/24/25 fps sources (cinematic sources are usually 24).
- Voice chain: high-pass 80 Hz, de-ess, light compression; one voice track (a lav or the location mic, never both).
- **The cut map carries the voice.** The EDL (`veos cut`) is built from the talking pieces (setups A/B/D, their own audio), or from a separate voice-over file when the creator recorded one. Talking pieces in the cut map get face boxes, the matte and E1 words.
- **B-roll plays over the voice as picture-only scenes.** Every SH-1/SH-2/SH-4/SH-6/SH-7 clip is `veos asset add`-ed and shown with `VEOS.fx.clip` at z4, full-bleed, frame-exact from its in-point, with `extra: {cuts: [0], continuous: true}` so it counts as a cut and as live motion:
```js
VEOS.fx.clip({ id: "b-kettle", asset: "B07", t_in: 3.10, t_out: 4.02, z: 4, offset: 2.40, kind: "broll",
  in: "none", out: "none", extra: { cuts: [0], continuous: true } });
```
- Grade layers (GR-L) at z4 are declared **after** the B-roll scenes they grade (same z: declaration order decides).
- A persona scene with the creator's own line on camera stays in the cut map; a persona scene played under the voice is B-roll.

---

## §13 Output contract `[DNA]`

### 13.1 Core beat fields
```yaml
- id: 7
  section: SCENE-2                 # HOOK | SETUP | SCENE-n | TURN | PAYOFF | CTA | BOOKEND (F-B: CONTEXT | RULE-n | RESULT)
  t0: 18.40
  t1: 21.10
  spoken: "And the ego lifter only cares about one thing"
  trigger: {word: "ego", at: 18.92}
  tone: warn                        # hype | awe | explain | warn | win | cta
  line_type: persona
  layout: L-full
  visual: "Amber-graded gym, the creator in a lifting belt mid-rep; 'The EGO LIFTER' duo lands on 'ego'"
  layers: [grade-amber-1, duo-ego]
  pattern: P-PERSONA-GRADE
  sfx: []
```

### 13.2 Conditional fields (this style)
| Switch / module | Fields |
|---|---|
| captions | `caption {profile: CS-1, overrides[]}` (hide for "#N." markers, text fixes) |
| ink | `ink [{mark: arrow \| oval \| guide \| lasso, target: {x, y, w, h}, frames}]` from the anchor pass |
| continuity | `bookend {shot: SH-1, src_in, src_out}` on the BOOKEND beat; `walk: in \| out` |
| series | `series {name, number}` on the series beat |
| brand | `sponsor {id, disclosure}` on every sponsored beat |
| grades | `grade: GR-mono \| GR-amber \| GR-teal \| GR-warm` (per beat) |
| footage ≥ medium | `shot_id: SH-n`, `fallback_used: FB-n \| null` |
| third-party moment | `insert {id, origin: creator \| created}` |
| declared exception | `exception: E1 \| E2` (also on the scene) |
| re-hook | `rehook: true` |

### 13.3 Reel header
```yaml
format: F-A                      # F-A | F-B
theme: null                      # single
hook_archetype: HA-12            # HA-12 | HA-05 | HA-19 | HA-08
structure: story                 # story | tutorial
count: 3                         # items / rules / personas promised, or null
keyword: "{{BV-08.keyword|KEYWORD}}"
cta_device: comment_keyword
grades: {persona-1: GR-mono, persona-2: GR-amber, persona-3: GR-teal}
bookend: {shot: SH-1, clip: B01, src_in: 12.40, pre_roll: [10.90, 12.40]}
series: null                     # or {name, number}
sponsor: null                    # or {id, disclosure}
exceptions: {E1: [21.4], E2: [6.1]}
```

### 13.4 Hook proposals (3)
```yaml
- name: "Mirror thesis"
  archetype: HA-12
  thesis: "When it comes to what you wear, shopping in person is way better than online"
  duo_beats: ["when it comes to what | YOU WEAR", "SHOPPING / IN PERSON", "IS WAY / BETTER | than online"]
  scene_promise: {shot: SH-1 mirror, payoff: "the try-on scenes at 0:09-0:26"}
  storyboard: "f0 mirror, creator small, script writing | 0.47 YOU | 0.80 WEAR | 1.07 out | 1.40 SHOPPING IN PERSON | 2.33 IS WAY BETTER + 'than online' | 3.9 cut on motion to the doorway"
  sound: [soft hit on 'YOU', whoosh on the first cut]
  stopper_test: {mute: pass, motion_f0: pass, read_s: 1.0, changes_3s: 8, payoff_s: 2.9}
```

### 13.5 Checkpoint (before building)
1. Three hooks with stopper results.
2. The beat sheet with tones, patterns, grades and shot ids.
3. The transition map and the cue moments.
4. The duo-title list (beats, words, times) and every behind-head word with its matte check.
5. The bookend plan (SH-1 clip, pre-roll span, the words that ride it).
6. The inserts record (creator-supplied vs created) and the fallbacks used.
7. Style stills: f0, 1.5 s (mid-hook), one paper beat, one persona or rule beat, the CTA, the last frame next to f0.
**Wait for approval.**

---

## §14 Worked examples `[NICHE]`
Times are planning estimates; replace them with `words.edit.json` onsets.

### 14.1 F-A story · [NICHE: example] travel · "I stopped booking hotels" (66 s, keyword STAY)
**Header:** F-A · HA-12 · story · count null · CTA `comment_keyword` STAY · bookend SH-1 (a homestay doorway seen from inside; the creator walks in from the street) · no grades beyond GR-warm · E1 at 41.2 s.

**Hook (0–3.1 s):**
| t (s) | Spoken | Picture | Type layer | Subtitle | Camera / cue |
|---|---|---|---|---|---|
| f0 | — | SH-1: doorway frame, the creator far away in the street, walking toward it | "I" starts writing at (72, 236) | hidden | hook cue at 0.45 |
| 0.10 | "I" | same | script "I" written (8 f) | — | — |
| 0.45 | "stopped" | same | **STOPPED** blur-slides in, 220 px, top y 330 | — | — |
| 1.05 | (out) | same, closer | STOPPED blurs out | — | — |
| 1.20 | "booking" | same | **BOOKING** line 1 (200 px) | — | — |
| 1.55 | "hotels." | same | **HOTELS** line 2 | — | — |
| 2.10 | (out) | the creator reaches the door | lockup out | — | — |
| 2.30 | "and this" | same | script "and" + **THIS** | — | — |
| 2.75 | "happened" | same | script "happened" below-right; thesis complete | — | — |
| 3.10 | — | **T-2** cut on his step through the door → SH-4 kettle detail | out 2 f before the cut | CS-1 starts | transition cue |

**Plan:**
| Section | t (s) | Spoken (gist) | Patterns and picture |
|---|---|---|---|
| SETUP | 3.1–9.0 | "Six months, eleven cities, zero hotels." | P-DETAIL-RUN (kettle, keys, shoes at the door) → talking piece A on a rooftop; **P-COUNT-UP** "11" + "CITIES" at 5.2 (lands on "eleven") |
| SCENE-1 | 9.0–20.0 | The first morning: breakfast with the host family | P-DETAIL-RUN of four nouns (rice, chilli, steam, hands) at 0.8 s each → **P-POLAROID** of the family's kitchen (the creator's photo) on W-grid on "they made me family" → back to talking piece B |
| SCENE-2 | 20.0–30.5 | "Half the price, and I knew where the locals eat" | **P-UI-CHIP** "hotels near me" over his phone shot (deadpan, light comedy) → street food B-roll → **P-PAPER-CARD** of his own past reel "Hoi An homestay" (SH-10) with card title |
| TURN (re-hook) | 30.5–35.0 | "But it's not for everyone." | **P-DUO-TITLE** "**BUT** it's not for **EVERYONE**" on a talking piece, `rehook: true` (47% of 66 s) |
| SCENE-3 | 35.0–46.0 | Shared bathrooms, no reception, roosters at 5 am | P-DETAIL-RUN of the three → **P-BEHIND-WORD** "NOISE" behind his head on SH-11 at 41.2 (E1) → P-SCRIPT-ASIDE "…riveting" over a rooster (light comedy) |
| PAYOFF | 46.0–58.0 | "What I got instead: every city from the inside." | **P-RECAP-RIFFLE** of six hosts' doorways, city names as card titles, 0.5 s each (cuts) → talking piece with **Z-2** slow push |
| CTA | 58.0–64.5 | "Comment STAY and I'll send you all eleven." | **P-POSTER-BACKDROP** (SH-12 profile, `accent` sun) + **P-CTA-KEYWORD** "Just comment / **STAY** / for the list", held 2.4 s |
| BOOKEND | 64.5–66.0 | "See you inside." | SH-1 pre-roll [src 10.9–12.4]: the doorway, the creator far in the street; the last frame equals f0 |
Cut count ≈ 37 (34 cuts/min); duo titles 4; paper share ≈ 14%; presence ≈ 52%.

### 14.2 F-A types · [NICHE: example] fitness · "3 types of gym people" (61 s, keyword PLAN)
**Header:** F-A · HA-12 · story (list of types) · count 3 · SM-1 markers · CTA `comment_keyword` PLAN · grades persona-1 GR-mono, persona-2 GR-amber, persona-3 GR-teal · E2 at 6.0 s · E1 at 1.3 s · runtime 61 s.

**Hook (0–2.9 s):**
| t (s) | Spoken | Picture | Type layer | Subtitle | Camera / cue |
|---|---|---|---|---|---|
| f0 | — | Setup B seated set, the creator gesturing (live) | — | hidden | — |
| 0.60 | "There are three" | same | **3** blur-slides in at (150, 360), 230 px, left of his cap (front, 40 px clear) | — | hook cue |
| 0.95 | "types of" | same | script "types of" writes to the right of the 3 | — | — |
| 1.30 | "gym" | same | **GYM** blur-slides in **behind** his head (E1, 260 px, ≥ 65% visible) | — | — |
| 1.70 | "people" | same | script "people" under it, right-aligned | — | — |
| 2.30 | — | he raises three fingers | lockup out | — | — |
| 2.50 | — | **T-2** cut on the hand to a close-up of the three fingers | — | — | transition cue |
| 2.85 | "Number one" | cut to persona 1 | — | **SM-1 "#1."** in the caption band | — |

**Plan:**
| Section | t (s) | Spoken (gist) | Patterns and picture |
|---|---|---|---|
| PERSONA-1 | 2.9–12.5 | The overthinker: 40 tutorials, never lifts | GR-mono starts on the cut (GR-L) → label duo "The **OVERTHINKER**" (z8, front, no E1 inside GR-L) → **P-CHAOS-BURST** at 6.0–7.4 ("[Form check]", "[Program]", "am I doing it wrong", "[Day 1]", "too many") with a 4-cut flurry, then ≥ 1.0 s clean → action shots of him scrolling on a bench → punch duo "Still on **DAY ONE**" |
| PERSONA-2 | 12.5–22.0 | The ego lifter: heavier every week, form gone | "#2." → GR-amber → label duo "The **EGO LIFTER**" → **P-UI-CHIP** search "heaviest deadlift ever" (light comedy) → detail run (chalk, plates, belt) → punch duo "Doesn't care about **FORM**" |
| PERSONA-3 | 22.0–31.0 | The trend chaser: a new program every reel | "#3." → GR-teal → label duo "The **TREND** CHASER" → **P-PHONE-REEL** of his own saved-reels screen capture with **P-INK-OVAL** on the caption |
| TURN (re-hook) | 31.0–35.5 | "The one who wins is the boring one." | Back to GR-warm on a white set (the grade ends on the cut) → **P-DUO-TITLE** "the **BORING** one" `rehook: true` (50% of 61 s) |
| PAYOFF | 35.5–51.0 | Shows up, logs it, repeats | **P-FLOAT-CARDS** of four client check-in clips around him (assets, creator-owned) → **P-COUNT-UP** "312" + "SESSIONS" landing on "three hundred twelve" → talking piece Z-2 |
| CTA | 51.0–59.5 | "Comment PLAN for my 4-week starter plan." | **P-POSTER-BACKDROP** + **P-CTA-KEYWORD** "Just comment / **PLAN** / for the plan" 2.2 s → **P-SIGNOFF-SUN** "See you / **TOMORROW**" |
| BOOKEND | 59.5–61.0 | "Show up." | SH-1 pre-roll of the seated set; last frame equals f0 |
Re-hook check: the turn at 31.0 s sits at 50% of 61 s; the gaps 2.9 → 31.0 s and 31.0 → 51.0 s are both ≤ 40 s. Cut count ≈ 40 (39 cuts/min); grade events 3; E2 once.

### 14.3 F-B tutorial · [NICHE: example] travel · "Edit travel photos on your phone in 4 steps" (72 s, keyword PRESET)
**Header:** F-B · HA-05 · tutorial · count 4 · SM-2 rule chapters · series "Travel Lab" ep. 03 (P-SERIES-LOCKUP) · sponsor: the editing app (P-LOGO-CHIP + P-DISCLOSURE) · CTA `link_bio` (P-END-BLOCK) · bookend SH-2 (overhead of the creator at a river railing).

**Hook (0–3.6 s):**
| t (s) | Spoken | Picture | Type layer | Subtitle | Camera / cue |
|---|---|---|---|---|---|
| f0 | — | SH-2 overhead: the creator walks into the frame toward the railing | — | hidden | — |
| 0.38 | — | same | line 1 squash-in starts | — | hook cue |
| 0.45–0.70 | — | same | **EDIT TRAVEL PHOTOS / ON YOUR PHONE** mask-wipes up (Montserrat 900, 72 px): readable by 0.7 s | — | — |
| 0.85 | "Your travel photos look flat," | he leans on the railing | title holds | CS-1 starts | — |
| 2.40 | "here's the fix in four steps." | same | title holds | — | — |
| 3.60 | — | **T-2** cut on his turn | title blurs out | — | transition cue |

**Plan:**
| Section | t (s) | Spoken (gist) | Patterns and picture |
|---|---|---|---|
| SERIES | 3.6–4.8 | — | **P-SERIES-LOCKUP** "Travel / **LAB** / ep. 03" on W-grid (intro = 4.8 s = 7% ✓) |
| CONTEXT | 4.8–11.0 | "We're doing it all in one free app." | **P-LOGO-CHIP** "With <app>" (the sponsor's supplied logo) + **P-DISCLOSURE** "Paid partnership" for the whole sponsored span (4.8–58.0) → **P-SPIN-CARD** of "the photo I took in Lisbon" |
| RULE-1 | 11.0–22.0 | Remove distractions | SM-2 "REMOVE THE NOISE" (ink on W-paper) → **P-APP-DEVICE** (SH-8) → **P-LASSO** on the tourist behind her (12 f) → zoom into "Erase" (12 f) → hard swap of the screen to the cleaned photo on "gone" |
| RULE-2 | 22.0–33.0 | Straighten and crop | SM-2 "STRAIGHTEN" → **P-LANDSCAPE-CARD** of the photo with **P-GUIDE-LINES** (thirds) + **P-INK-ARROWS** to the horizon → device crop step |
| RULE-3 (re-hook) | 33.0–44.0 | Lift the shadows | **P-DUO-TITLE** "This one **CHANGES** everything" `rehook: true` (46% of 72 s) → device zoom to the Shadows slider (1.0 → 1.8, 12 f) |
| RULE-4 | 44.0–55.0 | Warmth and a soft vignette | SM-2 "WARM IT UP" → device slider → **P-CARD-CAROUSEL** of three more photos with the same settings |
| RESULT | 55.0–62.0 | "Before. After." | **P-BEFORE-AFTER-POLAROID** on W-grid: before 1.2 s, cut to after on "after", hold 1.8 s |
| CTA | 62.0–70.5 | "My preset is free, link in bio." | **P-END-BLOCK** "FREE / TRAVEL / PRESET / LINK / IN BIO" over SH-13 (river water close-up), 3.5 s |
| BOOKEND | 70.5–72.0 | "Go shoot." | SH-2 pre-roll: the empty railing from above, the creator about to enter; the last frame equals f0 |
Cut count ≈ 38 (32 cuts/min, cards and slides included as `transitions`); paper share ≈ 36%; presence ≈ 41% (F-B band 35–55%).

---

## §15 QA checklist `[DNA]`

**1. Profile conformance**
- [ ] Format declared (F-A or F-B) and its layouts only (`V-LAYOUT`); duration 55–85 s (`review`); presence 45–60% (F-B 35–55%) and max absence 6 s / 8 s (`V-PRESENCE`).

**2. Hook**
- [ ] f0 moves; the first type beat by 0.7 s (HA-12) or the title by 0.7 s (HA-05) (`V-F0`).
- [ ] ≥ 6 weighted changes in 0–3 s; no gap > 0.8 s in the hook (`V-CADENCE`).
- [ ] The thesis complete by 3.0 s; each beat reads in ≤ 1.2 s; ≤ 7 words per lockup (`V-F0`, `V-TITLE`).
- [ ] The mute test passes: the beats alone tell the thesis (`review`).

**3. Body and cadence**
- [ ] 27–51 cuts/min (F-B 27–42), median shot 0.85–1.6 s; card swaps declared as cuts (`V-CADENCE`).
- [ ] 5–12 weighted changes per 10 s; max gap 3.0 s; nothing static > 2.5 s (`V-CADENCE`).
- [ ] The unit ritual identical for every item / rule; markers match the count (`V-PROMISE`, `review`).
- [ ] One re-hook at 43–53% of runtime; gaps ≤ 40 s (`V-REHOOK`).
- [ ] Duo titles: 4–9 per 60 s, never two at once, blocks land on their words ±5 f (`V-ONWORD`, `review`).
- [ ] Only `primary` as a bright text hue; ink blocks on light worlds; ≤ 2 bright roles per frame (`V-HUES`, `V-TYPE`).
- [ ] Camera: only push-drift / slow-push / reset; never twice in a row (`V-CAMERA`).

**4. Captions**
- [ ] CS-1 on every spoken word outside duo / E2 / morph spans; 3–6 words, 1 line, ≤ 28 characters, y 1468, 54 px EB Garamond with the 2 px stroke; lead ≤ 0.15 s (`V-CAPTION`, `V-TYPE`).
- [ ] Spelling and glossary exact; ".." only on real pauses (`V-CAPTION`).

**5. Modules**
- [ ] **Ink (§22):** ≤ 3 marks on screen, `primary` 5–7 px, every mark on its target from the anchor pass, finished before the scene ends, never on the face (`review`).
- [ ] **Continuity (§23):** the last frame's picture equals f0's; no type fully visible on either; the bookend carries the last words; walk-in/out when SH-3 exists (`V-CONTINUITY` pending → `review`).
- [ ] **Series (§24):** the lockup once, inside the intro cap; the episode number from the brief (`V-REHOOK`, `review`).
- [ ] **Brand (§25):** disclosure visible ≥ 2 s or for the whole sponsored span and spoken; logo only from the creator's file; end card ≤ 4 s (`V-PROMISE`, `review`).

**6. Truth and inserts**
- [ ] Every number on screen spoken or in the script (`V-NUMFMT`, `review`).
- [ ] Every third-party moment recorded: creator-supplied or created and labelled (`V-INSERTS`).
- [ ] E1: ≥ 65% visible, first/last letters clear, hold ≥ 0.6 s, ≤ 1 at a time, none inside a GR-L span (`V-EXC`).
- [ ] E2: once, ≤ 1.5 s, ≤ 6 snippets, face clear, subtitles hidden, a clean second after, not in the CTA (`V-EXC`).
- [ ] Grades: one id per persona, no two consecutive personas alike, ≤ 8 events (`V-GRADE` pending → `review`).

**7. Sound contract**
- [ ] Cues only on hook / transitions / reveals / CTA moments, each tied to a picture event (S1–S6); no meme cues; bed ≥ 18 dB under the voice; −14 LUFS, true peak ≤ −1.5 dBTP.

**8. End and export**
- [ ] CTA keyword ≥ 1.5 s on screen (`V-PROMISE`); hard end ≤ 6 f after the last word on the bookend frame; no black tail; 1080 × 1920, 30 fps CFR.

---

## §16 Frame template / persistent chrome
OFF (`profile.modules.chrome = false`): nothing persists on screen; the frame changes with every shot.

## §17 Running state & anchored graphics
OFF (`profile.modules.running_state = false`, `profile.modules.anchors = false`): counters are one-off count-ups; ink targets come from the §22 anchor pass as static points or 2–4 keyframes.

## §18 Data contract
OFF (`profile.modules.data_figures = false`): no charts or computed figures; every number on screen is spoken or in the script (H18).

## §19 Evidence & citations
OFF (`profile.modules.citations = false`): no source cards or credit lines. Third-party material follows the ask-then-create flow (§12.5).

## §20 Dialogue
OFF (`profile.modules.dialogue = false`): one voice; a partner or a friend on camera is footage, not a speaker track.

## §21 Canvas camera
OFF (`profile.modules.canvas_camera = false`; graphics are `support`, PV-5): the camera moves over footage only (§10.2).

## §22 Ink & annotation layer `[COND: modules.ink] [DNA look; TUNE width]`
- **Stroke tokens:** colour `primary`, width 5–7 px (6 default), round caps, wobble ±1.5 px (seeded, per path), draw-on 10 f, 15° overshoot at the start of ovals.
- **Guides:** `paper` at 75%, 3 px, straight, drawn from the top in 10 f; centre line, rule-of-thirds grid, or one horizon line.
- **Lasso:** `paper` 8 px, traced along the object's outline over 12 f.
- **Marks:** arrow (shaft 8 f, then head 3 f), oval, underline (8 f), guide line, lasso. No circles of text, no scribbles, no notes in marker type.
- **Targets:** the anchor pass reads sampled frames of the clip and writes each target's rect `{x, y, w, h}` in output px; a moving subject gets 2–4 keyframes (linear between them); a target leaving the frame ends the mark.
- **Rules:** ≤ 3 marks on screen; marks finish before their scene ends; never on the face; one mark per spoken "here / this / look"; arrows converge on the subject, never point off-frame.
```js
// P-INK-OVAL: a hand-drawn oval that draws on over 10 f from local time `at`.
function inkOval(ctx, lt, o) {           // o = {cx, cy, rx, ry, rot, at}
  const p = Math.min(1, Math.max(0, (lt - o.at) * 30 / 10)); if (p <= 0) return "";
  const L = Math.round(2 * Math.PI * Math.sqrt((o.rx * o.rx + o.ry * o.ry) / 2) * 1.04);   // +15° overshoot
  return `<svg width="1080" height="1920" style="position:absolute;left:0;top:0"><ellipse cx="${o.cx}" cy="${o.cy}" rx="${o.rx}" ry="${o.ry}"
    transform="rotate(${o.rot == null ? -6 : o.rot} ${o.cx} ${o.cy})" fill="none" stroke="${ctx.col("primary")}" stroke-width="6"
    stroke-linecap="round" stroke-dasharray="${L}" stroke-dashoffset="${Math.round(L * (1 - p))}"/></svg>`;
}
VEOS.scene({ id: "ink-caption", t_in: 70.2, t_out: 72.4, z: 6, in: "none", out: "blur", roles: ["primary"],
  box: { x: 270, y: 1110, w: 540, h: 170 }, events: [0.0],
  render(ctx, lt) { return ctx.html(inkOval(ctx, lt, { cx: 540, cy: 1195, rx: 260, ry: 74, at: 0 })); } });
```

## §23 Continuity: the bookend loop `[COND: modules.continuity] [DNA]`
- **Bookend (DNA):** the last 1.0–1.5 s replays the opening shot SH-1 from its **pre-roll**, so the reel's final frame shows exactly the picture of frame 0 and the reel loops (v01 @ 1:23 = @ 0:00; v05 @ 1:01 returns to the opening railing).
- **Recipe:**
  1. SH-1 plays at f0 as a picture-only scene from source time `s0` (`VEOS.fx.clip({asset: "B01", offset: s0, ...})`).
  2. The BOOKEND scene plays the same asset with `offset: s0 − d` (`d` = 1.0–1.5 s) and lasts `d + 1/30` s to the reel's end, so its last rendered frame is source frame `s0`, the picture of f0.
  3. No type is fully visible on frame 0 or on the last frame; the subtitle of the last words hides 4 f before the end (`captions.overrides` hide `[end − 0.13, end]`).
  4. The last spoken sentence (sign-off or the end of the CTA) rides the bookend; the hard end is ≤ 6 f after the last word (NC-8).
- **Walk-in / walk-out** (SH-3): when it exists, the creator enters the opening frame within 0.5 s and leaves the closing frame in the last 1.5 s; the bookend then plays the empty plate.
- **Motif / morph chain:** none (`motif: null`, `morph_required: false`).
- **Fallback (SH-1 has < 1.0 s of pre-roll):** the bookend holds SH-1 frozen on source frame `s0` for its last 0.5–1.0 s (a still is allowed there: `max_static_s` 2.5 s), preceded by the reel's last talking shot; the final frame still equals f0.
- **Validator:** V-CONTINUITY is pending (E-19); until it ships, the checkpoint shows the last frame next to f0 and QA compares them (§15).

## §24 Series furniture `[COND: modules.series] [DNA look; VAR name/number]`
- **Series lockup (P-SERIES-LOCKUP):** on W-grid with the grid off and vignette 0.42; script name (Pinyon Script 140 px `gold`) overlapping the top of a block word (Montserrat 900 150 px `gold`), "ep. NN" (Jost 600 40 px `gold`) centred under it; centred on y 900. The creator's own series logo file replaces the type when supplied.
- **Placement:** directly after the hook, starting ≤ 12% of runtime (5–9 s); hold 1.2 s; enters by a cut, script writes 10 f, block blur-slides 4 f; leaves by a cut. It counts toward the intro cap (hook + lockup ≤ 15%).
- **Tokens:** `series {name: null, number: null, tag_format: "ep. {n}", card: {at_s: [5, 9], hold_s: 1.2}}`; the name and the number come from the reel brief (VAR, off until the buyer turns it on).
- No persistent series tag, no progress dots.

## §25 Sponsor, brand & end cards `[COND: modules.brand] [DNA look; VAR assets]`
- **Logo chip (P-LOGO-CHIP):** "With" in script (60 px) + the brand's logo file (88 px tall, its own colours) + the wordmark in Jost 500 72 px `paper`, top band y 380–470, on the word naming the brand; 1.0–1.5 s. Without a logo file: `fx.logoPlate` (the name set in type, no logo).
- **Disclosure (P-DISCLOSURE, NC-12):** "Paid partnership" (BV-14 wording) in `TC-legal` 24 px at (64, 128), from the first sponsored beat for ≥ 2.0 s, or for the whole sponsored span when the product is used on screen; plus a spoken mention.
- **Sponsor placement:** never over the face, never over the CTA keyword, never inside the hook's first 3 s.
- **End cards:** P-END-BLOCK (`link_bio`, `end_card`): 4–7 lines of yellow Montserrat 900 filling the width over a texture close-up (SH-13, else W-void), 2.5–4.0 s, the keyword or URL line readable ≥ 1.5 s, followed by the bookend. No subscribe buttons, no follow stacks, no QR codes.
- **Rules:** end card ≤ 4 s; no black tail; the bookend is the last picture.

---

## Part C. Declared exceptions and the non-overridable core

### C.1 Non-overridable core
NC-1 … NC-14 apply unchanged (structure Part C.1): the face is never covered; meaning text never overlaps meaning text (except an E2 burst); smooth motion; legibility floors; IG UI bands; truth; creator-owned media only; audio targets; determinism; ≤ 4 bright hues; disclosure; quote integrity; redaction.

Style-specific consequences:
- **NC-1:** behind-head words are *behind* (E1), never in front; chaos snippets keep ≥ 40 px from the face box.
- **NC-5:** the subtitle band (y 1437–1499) stays above y 1500; the legal line sits at the top (y 128), not the bottom.
- **NC-14:** screen recordings (SH-8) are checked for emails, phone numbers and account names; blur them for their whole time on screen.

### C.2 Exceptions used
| ID | Token | Limits in tokens.json | Scenes set |
|---|---|---|---|
| E1 | `behind_text` | `{"min_visible": 0.65, "max_at_once": 1, "min_hold_s": 0.6}` | `behind: true`, `exception: "E1"`, `text_class: "TC-display"` |
| E2 | `chaos_burst` | `{"max_s": 1.5, "max_per_60s": 1, "max_per_reel": 1, "max_snippets": 6, "clean_after_s": 1.0}` | `exception: "E2"`, `snippets: N`, z8 |

### C.3 How they are declared
Playbook §2.2 (limits, reason, evidence) → `tokens.json → exceptions` → `exception: "E1" | "E2"` on each scene → V-EXC checks them per frame (E1 visible ratio needs the occlusion measure, E-21; until then a warning and the 200% matte check at the checkpoint).

**E2 scene recipe (P-CHAOS-BURST):**
```js
// ≤ 45 f; 4-6 snippets around (never on) the face; GR-mono under it (GR-L scene, declared after it at z4).
const SNIPS = [{ t: "[Close Up]", x: 96, y: 380, f: "ui", s: 48, at: 0.00 }, { t: "am I doing it wrong", x: 520, y: 520, f: "serif", s: 64, at: 0.13 },
               { t: "[Wide]", x: 760, y: 300, f: "ui", s: 48, at: 0.27 }, { t: "[Day 1]", x: 120, y: 1180, f: "ui", s: 52, at: 0.40 },
               { t: "too many", x: 560, y: 1260, f: "serif", s: 70, at: 0.53 }];
VEOS.scene({ id: "chaos-1", t_in: 6.00, t_out: 7.40, z: 8, in: "none", out: "none", exception: "E2", snippets: SNIPS.length,
  text: true, text_class: "TC-label", text_content: SNIPS.map(s => s.t).join(" "), roles: [],
  box: { x: 64, y: 260, w: 952, h: 1080 }, events: SNIPS.map(s => s.at),
  render(ctx, lt) {
    return ctx.html(SNIPS.map(s => { const k = (lt - s.at) * 30; if (k < 0) return "";
      const e = Math.min(1, k / 3), dx = Math.round(20 * lt);
      return `<div style="position:absolute;left:${s.x + dx}px;top:${s.y}px;font:${s.f === "serif" ? "italic 500" : "500"} ${s.s}px ${ctx.fam(s.f)};
        color:${ctx.col("paper")};opacity:${(0.85 * e).toFixed(2)};filter:blur(${(6 * (1 - e)).toFixed(1)}px);text-shadow:0 2px 8px rgba(0,0,0,.6);white-space:nowrap">${ctx.esc(s.t)}</div>`; }).join(""));
  } });
```
The picture flurry under it (3–5 cuts of 6–9 f) comes from B-roll scenes, each with `cuts: [0]`. Check the face box with `ctx.face()` at planning time and move any snippet that would come within 40 px of it.

---

## Part D. Personalisation

### D.1 Lock levels in this template
| Area | Lock |
|---|---|
| Style DNA, "Copy these 5", D1–D8, §1, §2, §9, §13, §15 | DNA |
| Source type, spine, captions role, graphics, footage dependency, the format set, the CTA device set, the modules ink / continuity | DNA |
| Presenter share (±10 pts), max absence (4–9 s), duration (short ↔ standard), energy (one step), cadence (±15%), motion tokens (±15%), type sizes (ranges in `locks`), caption size 54–62 and y 1470–1510, world tints, grade strength | TUNE |
| `primary` and `accent` hex, language, numbers, CTA device and keyword, series and brand on/off, comedy off ↔ light, formats enabled, footage setups | VAR |
| §6.4 hook pairs, §8.4 lookup, §14, App. A, glossary | NICHE |
| Exceptions E1 / E2 | DNA (switching one off = VAR, stricter) |

### D.2 Branding questions (one round, each with "keep the template default")
| ID | Question | Feeds |
|---|---|---|
| BV-01 | "Your name and handle?" | `creator.name/handle`, the end block, the series lockup, P-LOGO-CHIP for the creator's own brand |
| BV-02 | "One or two brand colours? (the first replaces the yellow, the second the poster sun; or keep yellow + sun)" | `roles.primary` ({{BV-02.primary|#F7DE0B}}), `roles.accent` ({{BV-02.accent|#D42A05}}); nudged to ≥ 4.5:1 with ink |
| BV-05 | "Which language do you speak in your reels, and which captions do you want?" (English / Hinglish in Latin / Hinglish → English captions / Hindi in Devanagari) | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06) | English ({{BV-05.speech|en}} → {{BV-05.captions|en}}) | en}}) |
| BV-08 | "Your call to action: a comment keyword, link in bio, a part-2 end card, or none?" | `profile.cta.chosen` ({{BV-08.device|comment_keyword}}: {{BV-08.keyword|KEYWORD}}) |

Defaulted, changeable later: BV-03 fonts within each class; BV-06 numbers (from BV-05); BV-09 formats; BV-11 comedy off/light; BV-13 series name and number; BV-14 disclosure wording; BV-15 never-on-screen list; BV-16 logo and series logo files; BV-17 duration 55–85 s.

### D.3 Footage is not asked at setup
Per reel the editor uses what the buyer drops in and applies §12.3, listing the fallbacks at the checkpoint. The first reel's checkpoint also shows the shot list (§12.2) as "what to shoot next time".

### D.4 How NICHE slots grow
- §6.4: each reel's thesis → scene-promise pair is appended at P7.
- §8.4: new line types map to existing patterns (≤ 10 niche patterns over time, from existing families).
- §14: after the first approved reel of each format, it becomes that format's worked example.
- App. A: approved hooks and titles are appended.
- Glossary: confirmed brand, place and tool spellings.

---

## Part E. Changes against the structure and the coverage decision
| Item | Decision | Why |
|---|---|---|
| `sc_per_10s` | **5–12** (coverage said 5–8) | At 51 cuts/min the cuts alone are 8.5 per 10 s, before subtitles and type beats; 5–8 would fail v01 itself |
| `max_gap_s` | 3.0 s | v04 @ 0:42–0:47 holds one shot ~6 s under subtitles; the style allows a hold only with a duo title or a Z-2 push inside it |
| Subtitle size | 54 px (measured 47–48 at full resolution) | Coverage chose E1 + E2 only; 54 px meets G4 without E3 |
| E2 per reel | 1 (registry allows 2; v02 shows two) | Naman's brief: once per reel |
| `source_type` | `narrated_footage` with talking pieces as the cut map and B-roll as picture-only clip scenes | The engine's cut map carries a source's picture and its audio together; B-roll over the voice plays as `fx.clip` scenes (§12.6) |
| Duo titles | Built as scenes (§5.2), not as a caption variant | The corners layout, the behind-head words and the per-beat replace/join logic need per-word placement |
| Fonts | (resolved, audit) Nanum Pen Script connectors, Montserrat 900 wide block (closer than Archivo Black) | both bundled |

**Engine requests (for the orchestrator):**
1. ~~Bundle a pen-handwriting OFL font and Archivo Black~~ (done: Nanum Pen Script + Archivo Black are bundled and used).
2. **E-16 grades on the footage layer** (below behind-scenes and the cut-out): today's GR-L z4 backdrop-filter greys E1 words and costs a G2 slot.
3. **E-19 V-CONTINUITY with a bookend check** (last frame vs frame 0 picture difference).
4. **E-21 E1 occlusion measure** (visible-glyph ratio from the matte).
5. ~~Built-in flash / whip / zoom-blur transitions, a directional blur for type, per-preset camera `ease`~~ (done: T-10/T-11/T-12/T-13/T-3/T-7 are `timeline.transitions[]` / `timeline.blur` entries, §9.5; the duo smear uses `ctx.blur(px, 90)`; Z-1/Z-2 run `ease: "linear"`; T-12's incoming half is the Z-4 landing, capped at 1.5× by V-CAMERA where the source reaches 2.3×).
6. A **B-roll-over-voice EDL** (picture from source X, audio from the talking take) would let B-roll count as cut-map cuts and use the cut-out; today B-roll scenes declare `cuts: [0]`.

---

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D / BD | D1–D8 · BD… (buyer) |
| H / N / BN | H1–H22 · N1–N14 · BN… |
| E / NC | E1, E2 · NC-1…NC-14 |
| W / L / G | W-footage, W-paper, W-grid, W-void, W-poster · L-full, L-card916, L-card43, L-hidden · G-1…G-6 |
| GR | GR-warm, GR-mono, GR-amber, GR-teal (GR-L = today's render path) |
| CS | CS-1 |
| HA / ST | HA-12 (default), HA-05 (F-B default), HA-19, HA-08 · ST-1…ST-6 |
| SM | SM-1 hash marker, SM-2 rule chapter, SM-3 series lockup |
| B / P | B-1…B-13 · 41 patterns (§8.3) |
| T / R / Z | T-1…T-13 · R-1…R-9 · Z-1 push-drift, Z-2 slow-push, Z-3 reset, Z-4 zoom-land (T-12 only) |
| SH / FB | SH-1…SH-13 · FB-1…FB-13 |
| F | F-A Vlog / story, F-B Tutorial with paper cards |
| BV | BV-01, BV-02, BV-05, BV-08 asked; BV-03, 06, 09, 11, 13–17 defaulted |
| V | V-F0, V-CADENCE, V-ONWORD, V-SAFE, V-FACE, V-PRESENCE, V-CAPTION, V-TYPE, V-EXC, V-HUES, V-CAMERA, V-LAYOUT, V-TITLE, V-PROMISE, V-INSERTS, V-REHOOK, V-NUMFMT, V-COMEDY, V-GRADE (pending), V-CONTINUITY (pending) |

---

## App. A Headline & hook bank `[NICHE]`
Duo split shown as **BLOCK** / script. Write 3 per reel and pick by §6.1.

**F-A (vlog / story)**
| # | Hook | Archetype | Niche |
|---|---|---|---|
| 1 | "Training **ALONE** is why you **STOPPED** at week three" | HA-12 | fitness |
| 2 | "**3** types of **GYM** people" | HA-12 | fitness |
| 3 | "Your **MORNING** decides your **WORKOUT**" | HA-12 | fitness |
| 4 | "**100 DAYS** / no sugar" (count-up 1 → 100) | HA-08 | fitness |
| 5 | "**SALT.** / **SWEAT.** / **SILENCE.**" | HA-19 | fitness |
| 6 | "I **STOPPED** booking **HOTELS**. **THIS** happened" | HA-12 | travel |
| 7 | "The best **FOOD** in this city has **NO MENU**" | HA-12 | travel |
| 8 | "**52 CITIES** / one backpack" | HA-08 | travel |
| 9 | "When it comes to **TRAVEL**, **SLOW** is way **BETTER**" | HA-12 | travel |
| 10 | "**RAIN.** / **RAMEN.** / **RESET.**" | HA-19 | travel |

**F-B (tutorial)**
| # | Title lockup or duo | Archetype | Niche |
|---|---|---|---|
| 1 | "FIX YOUR SQUAT / IN THREE CUES" | HA-05 | fitness |
| 2 | "BUILD A HOME / WORKOUT PLAN" | HA-05 | fitness |
| 3 | "Is your **SQUAT** still **HURTING** your knees?" | HA-12 | fitness |
| 4 | "STRETCH LIKE / A PRO IN 5 MIN" | HA-05 | fitness |
| 5 | "TRACK YOUR / LIFTS ON YOUR PHONE" | HA-05 | fitness |
| 6 | "EDIT TRAVEL PHOTOS / ON YOUR PHONE" | HA-05 | travel |
| 7 | "SHOOT BETTER / TRAVEL PHOTOS" | HA-05 | travel |
| 8 | "Is your **PHONE** still taking **BORING** travel photos?" | HA-12 | travel |
| 9 | "PACK ONE BAG / FOR TWO WEEKS" | HA-05 | travel |
| 10 | "PLAN A TRIP / IN ONE EVENING" | HA-05 | travel |

## App. B Evidence map
The full map, with every DNA rule traced to frames and the `(unverified)` list, is in `evidence.md` (shipped with the template, not with buyer copies). Summary:
| Element | Evidence |
|---|---|
| Duo titles: yellow condensed block + white script, blur-slide beats | v01 @ 0:00–0:03, v02 @ 0:00.67–0:02.2, v05 @ 0:00–0:02.5 |
| Corners layout of the script words | v05 @ 0:00–0:02.5 |
| Pale-lemon serif subtitle at y ≈ 1468 | v01 from 0:04, v03 from 0:00.83, v04 from 0:02, v05 from 0:02.8 |
| Behind-head words (E1) | v02 @ 0:33, 0:38–0:40, 0:53, 0:57; v05 @ 0:07 |
| Chaos burst (E2) | v02 @ 0:04–0:08 (and 0:34–0:36) |
| Cream paper world and 9:16 cards | v03 @ 0:11–0:14, 0:20–0:23, 0:41–0:43, 0:57–0:59; v04 @ 0:19–0:27, 0:34–0:41 |
| Polaroids and grid paper | v01 @ 0:29–0:30; v02 @ 0:45–0:48; v05 @ 0:23–0:25, 0:57–1:00 |
| Spin-in card | v03 @ 0:06–0:10 |
| Ink arrows, ovals, guide lines | v03 @ 0:20–0:36, 0:48–0:50, 0:57–0:59, 1:10–1:15 |
| Grades per persona | v02 @ 0:04–0:08 (mono), 0:09–0:17 (amber), 0:18–0:23 (teal) |
| Title lockup hook | v03 @ 0:00–0:04, v04 @ 0:00–0:02.9 |
| Count-up | v04 @ 0:03–0:05, 1:14–1:18 |
| Bookend loop, walk-in / walk-out | v01 @ 1:23 vs 0:00; v04 @ 0:00, 1:23; v05 @ 1:01 |
| Cut rhythm 26.7–51.3 cuts/min | `cuts.json` v01–v05 |
| CTA devices | v02 @ 0:54–0:58 (keyword + SOON), v03 @ 1:22 (end block), v05 @ 1:09 (spoken) |
| Series lockup, logo chip, disclosure | v05 @ 0:08, 0:09, 0:57 |
