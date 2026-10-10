# Cinematic Step Demo Style Playbook (template v2)

## The feel

This reel feels like sitting across a warm desk from someone who is very good at one thing with their hands, and being let
in on how they do it. The first frame is the finished thing, already moving: a cup set down with the coffee still
swirling, a notebook swinging open, two cards sliding into a wallet somebody made. Nothing is explained yet. You stop
because it's beautiful, and because you want one.

Then the camera looks straight down and the hands take over. That's the engine: you watch the thing get made, step by
step, the way you'd watch a friend at the counter. Each step opens with a small black label, printed on the frame as if
punched out of a label maker, and it's gone the moment the shot changes. The cuts vanish inside the movement: a hand
sweeps across, a page turns, and you're somewhere new without feeling moved. Time folds quietly, an empty grid and then a
full one. Between steps the creator looks up from the desk, lamp glowing behind them, and tells you why in a sentence.
Then you're back down at the hands.

Everything is quiet so the making can be loud. One warm, dark grade on every frame, the room falling away to black. A
small white subtitle where one word, the one that matters, turns into gold italic serif, as if the creator underlined it
in their head. No banners, no stickers, no zoom you can see, no whoosh on a cut. The calm is the luxury. A conversation
clip lives by the same rules: you drop in mid-thought, the cut follows whoever speaks, and the listener's face is the only
cutaway.

It builds the way a good process builds: steady through the middle, the most satisfying moment saved for the last step,
the slow spiral pour, the stitch pulled tight. Then the recap, the finished object in both hands, turned page by page
while the label counts along. It ends on the thing itself, and stops.

**The test:** pause on any frame and it should look like a still from a short film about making this one thing, with
nothing on it louder than the hands.

## What this playbook is

You're editing a hands-on how-to: a seated desk take plus overhead clips of the creator's hands doing the thing (F-A, the
step demo), or a recorded two-person conversation (F-B, the podcast clip). You have the authority to make it the most
watchable, most saveable how-to in their niche. This playbook is the style, pulled from two of Peter McKinnon's reels
(v01 a five-step notebook system, v02 a podcast clip), measured frame by frame and at full frame rate. Read it all, every
time; take what fits this reel, invent where a moment needs more, and never break the feel above.

**Who it's for and what it needs.** Food, craft, photography and other hands-on creators who can film their hands from
above. F-A needs the desk take and vertical overhead clips of every step (the footage is the style; every shot has a
fallback, §12.2), and runs about a minute to a minute and a half. F-B needs a recorded conversation (two cameras, or one 4K
wide) and runs 35–60 s. No cut-out: nothing in this style layers behind the person. Captions follow the creator's language
(English verbatim by default; Hinglish or Hindi, §5.5). Machine values live in `tokens.json`; where this text gives a
number tokens also holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Show the hands do it.** Every step that is spoken is seen being done, in overhead footage, on the word | §7.3, §8.4, §12.2 SH-1 |
| D2 | **Result first, in the hands.** F-A opens on the finished result, moving, at frame 0 | §6.2 |
| D3 | **Quiet type.** Captions with one gold word, and one tape at a time. No headline, no banner, no emoji, no comedy | §2, §5 |
| D4 | **One grade.** Every footage frame is GR-tungsten (or its soft twin); created cards sit on the warm-black desk world | §4.3 |
| D5 | **Invisible editing.** Cut in motion, match the action; the only thing ever drawn between shots is the T-08 white flash | §9 |
| D6 | **Numbered and recapped.** Every step gets its tape; the reel ends with a recap of every step | §7.2, §7.3 |
| D7 | **The conversation drives the cut** (F-B): cut on the handover, cut away to the listener's reaction, nothing else | §3.8 |
| D8 | **Calm, dense in time, never in space.** The picture keeps changing as the hands work; the screen never holds more than the caption and one tape | §7.5, §2 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Formats, worlds, layouts, stage moves, safe zones, the person, the conversation |
| §4 | Colour and the tungsten grade |
| §5 | Type and captions: CS-1 / CS-2 / CS-3 gold-word captions, the tapes TX-1…TX-7 |
| §6 | Hook system: stopper test, HA-14 result in hand (F-A) and mid-sentence cold open (F-B), alternates, hook pairs, CTA |
| §7 | Structure and rhythm: SM-TAPE, the step ritual, the recap, open loops, rhythm by feel |
| §8 | Visual system (B-roll and patterns): families B-1…B-8, 36 patterns, line → pattern lookup, truth, assets |
| §9 | Transition system T-01…T-08, grammar, shot grammar R-1…R-9 |
| §10 | Motion tokens, camera Z-0…Z-2, layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setups, shots and fallbacks, third-party inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style's
craft is choosing and joining footage: which moment of which clip carries each word, and the exact frame where a hand or
an object crossing the frame hides the cut. Get those right and the reel feels made by hand.

**F-A, the step demo**
1. **Log every clip.** Each overhead (`oh-<step>-<n>`), result (`res-<n>`) and desk insert (`ins-<n>`): its length, the
   step it shows, its start and end state, the frames where a hand crosses. Overhead clips must be vertical 9:16 (a
   horizontal one becomes P-PLATE-BAND, FB-1).
2. **Pick the grade** from the desk take at 25/50/75 %: already warm with crushed blacks → GR-tungsten-soft; neutral or
   cool → GR-tungsten (§4.3).
3. **Shape the talk:** HOOK → PROMISE (the desk line naming the outcome and the count) → STEP 1…N → RECAP → CLOSE
   (→ CTA). Cut filler from the top (§6.6). Every tool, ingredient and brand the creator names goes in the glossary.
4. **Feel the tone of each line:** `explain` · `awe` (the result, the satisfying moment) · `win` · `warn` (a mistake to
   avoid) · `cta`. Awe and win put the gold on the result; warn puts it on the warning word.
5. **Write the hook** (§6) and **plan each step** (§7.3): its clips in order, the one tape it may carry, the state jump
   that finishes it, the desk return or not; then the recap's turn-through and the frame of each spoken ordinal.
6. **Select the hand cuts.** For every cut between two overhead clips, or overhead → desk, pick the out-frame and the
   in-frame (motion inside ±2 f, T-02 / T-03) from contact sheets of each clip at 10 fps. This is the craft; take the
   time.
7. **Get the third-party moments** (§12.4): the creator's files first, else the real thing fetched from the web (source
   noted). Name the fallback for every missing shot (§12.2), and plan the sound
   (§11): silent cuts, one soft cue for the tape, the bed from the promise.

**F-B, the podcast clip**
1. **Find the clip:** 35–60 s that **opens mid-thought on a claim** and **ends on a reaction or a short button line**
   (§6.3). Name the speakers (host / guest) and map each camera to its speaker.
2. **Feel each line:** claim, push-back, story beat, reframe, agreement, laugh.
3. **Write the cold opens:** different first sentences from the take, judged by the stopper test.
4. **Cut the conversation** (§3.8): every handover, every reaction, singles only, never a split.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person clear.** The face visits, so when it's on screen keep it and the hair clear of front layers. The
  framing that does it: the caption band on the chest, no STEP tape on a desk shot, the name tape beside the face. What's
  never fine is a head chopped or a face buried by accident. The geometry is in §3.7.
- **No text over text.** The screen holds at most the caption and one tape; never two tapes, never a tape on the caption
  band.
- **On the word.** The STEP tape pops on complete on the cut into its step; the cut into a step lands within ±2 f of the
  ordinal word; other tapes pop on within 1 f of their trigger word (the tool or the quantity). Desk cuts sit on word
  boundaries ±1 f; never cut inside a word, in any format. F-B cuts land within ±3 f of the new speaker's first word.
- **Say what was said.** Every quantity, temperature, time and setting on a tape is exactly what the creator said, in
  their unit first; nothing is added. Products shown are the creator's; brand names only as spoken. Illustrations inside
  created cards (a recreated app screen) may use made-up but realistic values, no label.
- **Promise integrity.** The spoken step count = the STEP tapes = the recap entries; every step in the recap was shown in
  the body; the result promised in the hook is the result shown at the close; a CTA keyword is on screen ≥ 1.5 s.
- **Spelling.** Tools, ingredients and brands exact in captions and on tapes (the glossary).
- **Readable.** Captions ≥ 54 px (CS-1 56, CS-2 76); tapes ≥ 40 px; the caption band falls over the dark surface or the
  hands, never over white paper or a bright plate; caption contrast ≥ 4.5:1 on the background it actually sits on. Text
  holds ≥ 0.25 s per word.
- **No dead frame.** Never a pause on a static frame. In overhead spans a breath while the hands keep working is fine:
  the action carries it.
- **One grade.** Every footage frame (desk, overhead, inserts, podcast) takes the reel's one preset; tapes and captions
  keep their exact colours, ungraded.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 18 dB under the voice, a hard end ≤ 6 f after the last
  word, no black tail.

**Never in this style:**
- A banner, slab, title card, lockup, emoji, sticker, chunky caption, kinetic type stack or glow. More than one coloured
  word or phrase per chunk (F-B: two). Any coloured caption word other than the gold.
- A synthetic transition: whip pan, light leak, glitch, zoom transition, crossfade, slide, push. Cuts, plus the T-08 white
  flash, which never appears in the hook or in F-B.
- A visible fast zoom, shake, crash zoom or rotation snap. Both reference cameras are locked off (measured: no synthetic
  zoom, rotation or shake anywhere in v01 or v02); the only moves are the Z-1 slow drift and a rare Z-2 re-crop on a jump
  cut.
- A second bright hue. The only colours added to the footage are the gold word, the dark tape, cream and warm black.
- Stock footage, AI-generated hands, food or products, or anyone else's footage standing in for the creator's own
  steps. (A third-party moment the reel names, an app, a post, a product photo, is the real thing: fetched when the
  creator doesn't have it, §12.4.)
- An ungraded, cool or clinical frame; a white seamless or a white desk under the overhead camera (it kills caption
  contrast and the look).
- A tape dropped over a face by accident, a tape on the caption band, two tapes at once.
- A spoken step with no picture of it being done (D1). With no overhead clip, use its fallback (§12.2) or cut the step.
- Meme sounds, comedy visuals, roast lines played as jokes.
- Numbers drawn as charts, counters or bars; a number appears only as spoken, on a tape or in a caption.
- Drawing on the footage: no circles, arrows or marker. The hands point.
- A split screen, PiP, bubble or morph, in either format.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Formats
| | F-A Step demo (default) | F-B Podcast clip |
|---|---|---|
| When | A hands-on process taught in 3–7 steps: a recipe, a brew, a craft build, a camera setting, a repair, a routine | A 35–60 s opinion or story moment cut from a two-person conversation the creator recorded |
| Input | `talking_head` desk take + overhead hand clips; spine `hybrid` (the voice carries the timeline, the hands decide where the cuts go) | `multi_speaker`; spine `talking_head` (the conversation is the timeline); `dialogue` on |
| Layouts | L-desk, L-overhead, L-insert | L-speaker, L-insert |
| Default hook | HA-14 "Result in hand" (§6.2) | HA-14 "Mid-sentence cold open" (§6.3) |
| Structure | `tutorial`: hook → promise → STEP 1…N → recap → close | `conversation`: claim → push-back or question → reframe → button |
| Captions | CS-1 (56 px, cy 1440) | CS-2 (76 px, cy 1385, speaker colours) |
| Needs | The creator at a desk + an overhead camera on their hands | A recorded conversation: two cameras, or one 4K wide |

What makes them one style: the same tungsten grade, the same white grotesk captions with one gold italic serif word, cuts
hidden in motion or on speech, and quiet type only. The STEP tape and the hands-from-above picture are F-A's own.

### 3.2 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-footage** | `footage` | The creator's own room and work surface, under GR-tungsten; base `#0D0A08` | Everything in F-A and F-B: desk take, overhead plates, desk inserts, podcast singles | Hard cuts |
| **W-desk** | `void` | Warm black `#0D0A08` with a radial lift `#2A1E15` → `#140F0B` (0.55) → `#0A0806` centred at (540, 806) (x 0.5, y 0.42), noise 0.035, vignette 0.45 | Insert cards (P-SCREEN-INSERT, P-PHOTO-PRINT, P-QUOTE-CARD, P-PRODUCT-TAPE) and fallback bands (P-PLATE-BAND, P-STEP-STILL) | Hard cut in and out, on a word boundary |

The surface under the overhead camera is part of W-footage and is the style's second "world": a **deep-coloured,
patterned surface** (a rug, slate, walnut, dark linen; v01's rug measured red `#8C1C22` and navy `#233A5E`). It is
filmed, never drawn, and it's why the white caption reads on top of it.

### 3.3 Layouts
| ID | Engine | Presenter | Graphic rect | Caption |
|---|---|---|---|---|
| **L-desk** | `full` | Full frame, the creator seated chest-up; head top y 220–360, face centre x 420–660 | none (no tape here) | CS-1, cy 1440 |
| **L-overhead** | `hidden` (the stage is off; the plate scene fills the frame at z1) | none: the hands are on screen, the face is not | 0, 0, 1080 × 1920 (the plate) | CS-1, cy 1440 |
| **L-insert** | `hidden` + W-desk | none | 64, 200, 952 × 1080 (the card) | CS-1, cy 1440 |
| **L-speaker** | `full` (the composed multi-camera footage) | Full frame, a tight single: face ≈ 28 % of the frame height, face centre ≈ 40 % from the top (v02 measured face y ≈ 450–1170 @0:01.5, @0:04.4, @0:29), the mic entering from the lower right | none | CS-2, cy 1385 |

The hands carry F-A and the face visits. In the reference the face is on screen for about a third of v01, and the
longest stretch without it is the first step (≈ 31 s of continuous overhead writing). The creator returns between the
hook and STEP 1 and again at the close, always by a hard cut on a sentence start. In F-B a face fills every frame; an
insert lasts a second at most.

### 3.4 Stage moves (all cuts)
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Desk → overhead | `stage {t, layout: "L-overhead", via: "cut"}` on the ordinal word; the plate scene starts on the same frame | Into every step |
| **G-2** | Overhead → desk | `stage {t, layout: "L-desk", via: "cut"}` on the first word of the "why" sentence, or on a hand exit (T-02) | After a step, the close |
| **G-3** | Any → insert | `stage {t, layout: "L-insert", via: "cut"}` + world W-desk; the card rises 10 f | A third-party moment (§12.4), a photo print |
| **G-4** | Speaker → speaker (F-B) | a `timeline.shots[]` boundary (`cut_reason: handover / reaction / recrop`) | Every handover and cutaway |

There are no panel drops, splits, PiPs, bubbles or morphs in this style. Continuity comes from match-action cuts (R-4),
never from a morph.

### 3.5 Layout diagrams
```
L-overhead (F-A)                    L-desk (F-A)                       L-speaker (F-B)
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
│ (over dark surface)     │1360-1500│                         │        │                         │
│ (IG bottom UI)          │ 1540    │ (IG bottom UI)          │ 1540   │ (IG bottom UI)          │ 1540
└─────────────────────────┘ 1920    └─────────────────────────┘ 1920   └─────────────────────────┘ 1920
```

### 3.6 Safe zones and bands
- Meaning text box: x 64–1016, y 110–1500; nothing in y < 110 or y > 1540 (Instagram's bars), nothing at x > 970 between
  y 900 and 1540 (the right-hand buttons).
- **Tape band:** y 165–265 (top 165, h 100), centred at x 540. Measured v01 @0:08.5: the STEP 1 tape at x 386–687,
  y 165–264 on 1080 × 1920.
- **Caption band:** CS-1 y 1360–1500 (cy 1440); CS-2 ≈ y 1310–1460 (cy 1385). Measured at full resolution: v01's blocks
  span y ≈ 1490–1645 (cy ≈ 1565), lifted ≈ 125 px to the lowest spot that keeps the block above y 1500; v02's
  y ≈ 1300–1470 (cy ≈ 1385) is kept as measured.
- **Overhead object zone:** y 200–1250, x 64–1016; nothing important of the demo below y 1300 (the caption band and the
  Instagram UI).
- **Tool / measure tape zone:** a free rect beside the object, inside y 280–1200, ≥ 40 px from the object's edge and from
  the caption band. Tapes are placed statically, never tracked.

### 3.7 The person
- **F-A, at the desk (L-desk):** head top y 220–360 (v01 @0:06 ≈ 238, @0:57 ≈ 270), face centre x 420–660, the face down
  to about y 820 (measured face y ≈ 380–820 @0:06.6). The caption band (y 1360–1500) is ≥ 540 px below the chin. The STEP
  tape band (y 165–265) would sit in the room above the head, so the STEP tape never appears on a desk shot (none does in
  v01: STEP 2 exits before the desk cut @0:40). A CTA tape over a desk shot needs the head top at y ≥ 305 (its bottom at
  265 plus 40 px, judged on the storyboard); otherwise it goes on the final result shot. The camera keeps the face inside y 220–760 on every Z-move.
- **F-A, overhead (L-overhead):** no face; the hands on the plates are the creator's own. Keep them; never use someone
  else's hands without saying so in the post.
- **F-B (L-speaker):** each speaker in a tight single, eyes ≈ y 600, chin ≈ y 880 in a typical take (the measured face
  box reaches y ≈ 1170); the caption band starts ≈ y 1310, under the chin. The name tape (y 1200–1264, x 64) sits on the
  chest beside the face, clear of the chin and hair; if a guest sits so low that it can't be, skip the tape and let the
  caption name them.
- No cut-out, nothing behind the person: this style has no layer there to put.

### 3.8 The conversation (F-B): cast and cut grammar
| Cast | Role | Caption style | Preferred angle |
|---|---|---|---|
| host | host (usually the creator) | CS-2, `paper` white, upright | the host's single camera |
| guest | guest | CS-2, `cream` `#EFE4CC`, upright | the guest's single camera |

- **Angles:** each camera is mapped to its speaker; with one camera, faux angles `<src>:<speaker>` cropped from a 4K wide
  (FB-5), ≤ 2.0× upsampling.
- **Singles only.** No stack, no two-shot split (`dialogue.stack: false`); a two-shot wide appears only as a 1.0–2.0 s
  establishing cut when both laugh (blurfill if it can't be cropped).
- **Cut grammar** (`dialogue.cut_rules`): cut on the new speaker's first word (1 f lead, ±3 f); the opener holds 3.0–5.2 s
  on the first speaker; a single holds at most 5.0 s before a reaction or re-crop; reactions 1.0–2.6 s; re-crop step 1.15;
  minimum shot 0.8 s; a back-channel ≤ 1.6 s ("yeah", "right") doesn't take the floor; never cut inside a word.
- **Captions:** speaker colours as the cast table; one speaker per chunk; overlapping speech shows only the dominant
  speaker. v02 shows both speakers in white; the guest's cream is a warm off-white that still reads as white, so each
  voice has its own style.

---

## §4 Colour and the tungsten grade

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` **Keyword gold** | `#D9A441` | The emphasised caption word or 2-word phrase (gold italic serif). Nothing else | `ink` | 10.4:1 (ink on gold); gold on the graded footage ≥ 4.5:1 with the caption shadow |
| `accent` **Label tape** | `#0B0B0B` | Tape fill: STEP, tool, measure, wait, name and CTA tapes | `paper` | 19.6:1 |
| `paper` | `#FFFFFF` | Caption text, tape lettering | — | — |
| `ink` | `#0B0B0B` | Card text, shadows | — | — |
| `cream` | `#EFE4CC` | The guest's captions (F-B); the paper-print and quote-card fill | `ink` | 15.9:1 |
| `night` | `#0D0A08` | The W-desk base | `paper` | 19.8:1 |

Measured at full resolution: v01's gold is a muted amber (glyph cores `#D9A441`–`#DDAE5A`, the antialiased median
`#CE9C44`; @0:01.2, @0:04, @0:06.6, @1:32), so F-A's `primary` is `#D9A441`. v02 (the podcast) uses a bright
saffron-yellow `#F5C518`–`#FAD109` with a faint glow (@0:01.5, @0:04.4), so CS-2 sets `#F5C518` directly. The tape is pure
black (`#000000`–`#0B0B0B`); the cream paper measured `#EDE3C8`. A creator's brand colour may take the gold's job; the
tape stays a dark tape colour (black, oxblood, navy, forest) so its white lettering keeps ≥ 7:1.

### 4.2 Meanings
- **Gold = the word that matters** in this sentence: the thing, the action, the name. It never marks good or bad; it marks
  importance.
- **Black tape = where we are** (the step, the tool, the quantity). A physical label, not a UI element.
- **Cream = paper** (the guest's voice in F-B; prints and quotes).
- There's **no good/bad axis**: a mistake is shown by the hands (a do-over), named in the caption, and its warning word goes
  gold.
- Brand colours appear only on the creator's own products, as filmed, and inside a real screenshot or photo as it is.

### 4.3 The grade
| Field | GR-tungsten (default) | GR-tungsten-soft (footage already graded) |
|---|---|---|
| CSS filter (`tokens.grades`; the stage footage automatically, plates via `ctx.grade`) | `contrast(1.14) saturate(0.9) sepia(0.16) brightness(0.82)` | `contrast(1.04) saturate(0.95) sepia(0.08) brightness(0.98)` |
| Warmth | 0.16 (a tungsten shift towards 3200 K) | 0.08 |
| Saturation | 0.90 | 0.95 |
| Contrast / lift / gamma / gain | 1.14 / 0.02 / 0.9 / 0.86 | 1.04 / 0.01 / — / 0.98 |
| Vignette | 0.50 (radial, clear to 55 % radius, `rgba(0,0,0,0.50)` at the corners) | 0.22 |
| Bloom | 0.12 (drawn by the engine grade) | 0.08 |

Measured at full resolution: the reference A-roll averages `#28201B` over the frame and `#0F100F` above the head (v01
@0:06.6, @1:47.5): the background falls almost to black. The first test stills on a real creator's room came out about
twice as bright, which is why the default is this dark (brightness 0.82, contrast 1.14, vignette 0.50). Footage that is
already dark takes GR-tungsten-soft.

- **One grade per reel**, chosen up front; no grade events, no clip treatments (no B&W, no duotone, no halftone).
- The grade sits **above the footage and the created cards, below every piece of type**: tapes and captions keep their
  exact colours.

### 4.4 Rules
- One added hue: the gold. The only other bright colour in a frame is one that's in the filmed object itself.
- Coloured text: only the gold word, on footage, always with the caption shadow `0 1 6 rgba(0,0,0,.45)`.
- Footage **is** regraded in this style, and only by §4.3.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weight | Use |
|---|---|---|---|
| `body` | **Inter Tight** | 600 | Captions |
| `serif` | **Instrument Serif** | 400 italic | The gold keyword; print and quote card lines |
| `mono` | **Courier Prime** | 700 | The STEP tape and every other tape |
| `display` | Inter Tight | 600 | Created-card titles (P-SCREEN-INSERT, P-PRODUCT-TAPE subline) |
| `numeric` | JetBrains Mono | 600 | Numbers on measure tapes |
| `ui` | Inter Tight | 400–600 | Recreated UI text inside created inserts |
| Devanagari | **Noto Sans Devanagari** | 600 / 700 | CS-3 captions |

Measured at full resolution: a Helvetica-Now-like grotesk **semibold** with **very tight tracking (≈ −5 %, the word spaces
almost closed)**; the italic serif keyword is condensed and high-contrast (Instrument Serif Italic is a near match); the
STEP tape is a rough, hand-inked typewriter / label-maker face (closest Google font: Special Elite, not bundled), so the
bundled Courier Prime 700 at 60 px, +0.18 em, stands in.

### 5.2 No headline element
`type.headline.kind = none`. This style never puts a headline on screen (neither v01 nor v02 has one). The hook is carried
by the result picture and the first caption; the hook title lives in the post title (§6.6).

### 5.3 Caption profiles

**CS-1 "Gold word" (F-A, every layout)** (`extends: lib:mckinnon`)
| Group | Value |
|---|---|
| Mode | `full`, role `support`, `mute_safe`: text is on screen nearly all the time, but it never outranks the picture |
| Chunking | unit `phrase`, 3–7 words, ≤ 17 characters per line (a narrow block ≈ 300–440 px wide), ≤ 2 lines; never split a name, number or unit; a sentence end breaks; a pause ≥ 0.9 s always breaks |
| Timing | lead 1 f; **reveal `word`**: each word appears on its onset in its final place (the line builds "This" → "This is" → "This is my", v01 @0:00.17–0:00.83); hold ≥ 0.25 s per word; tail 0.12 s after the last word; **each word fades in over 3 f with a 4 px blur clearing** (v01 f91–93, f32–34); the old chunk clears hard (0 f) on the frame before the next chunk's first word |
| Skin | Inter Tight 600, **56 px**, case as spoken (sentence case), tracking **−5 %**, line height 1.0 (the two lines nearly touch), `paper` white, no stroke, soft shadow `0 1 6 rgba(0,0,0,.45)`, no container; `line_fit: "block"` (below) |
| Position | `fixed_y` cy **1440** in L-desk, L-overhead and L-insert; centred, max width 560; `avoid_face` on |
| Emphasis | **`font_swap`**: the chosen word switches to **Instrument Serif italic 400, `primary` gold, 1.3× size** (73 px), same baseline; `span: phrase`, so the gold may run over 2 adjacent content words (v01 @0:04 "Track habits,", @0:06.6 "track everything"). Selects the topic noun, a name, a glossary term or a number; one per chunk; spaced about four seconds apart by the caption engine (`max_per_s: 0.25`, min score 1.2); never a stop-word |
| Hide | only during declared transitions (none in normal use); captions stay on through the recap |
| Language | Latin script; English terms verbatim; no spelling normalisation; glossary from the creator |

**The block fit.** In the reference the second line often looks smaller (≈ 0.6×, v01 @0:02 "and how I am productive.").
Full-resolution frames show why: the two lines are **size-fitted to one common width**: "This is my *system*" and "and how
I am productive." both span x 363–717 (≈ 354 px). CS-1 and CS-3 set `skin.line_fit: "block"`: every line grows to the
widest line's width (lines only grow, up to 1.6×, never below 56 px), so a short line is set larger and the block reads
justified. Never fake it with a forced break or a second caption.

**CS-2 "Gold word, two voices" (F-B)**: as CS-1 with 2–6 words, ≤ 16 characters per line, **76 px** (v02 cap height
≈ 55 px), cy **1385**, max width 640, gold `#F5C518` (v02's brighter yellow), up to 2 gold words per chunk (v02 @0:04.4
"*photographer* … *content*"), `span: word`, emphasis also selects key verbs, profanity masked `inner`. Speakers: host
`paper` white, guest `cream` `#EFE4CC`, both upright (§3.8).

**CS-3 "Devanagari" (`hi`, Deva)**: as CS-1 with Noto Sans Devanagari 600 at 56 px, line height 1.2, tracking 0; emphasis
switches to **`colour`**: the word turns `primary` gold at weight 700 and 1.1× (Devanagari has no true italic serif). Set
`captions.profile: "CS-3"` in the timeline for these reels.

**Single-word chunks** are fine when the word is a count ("one.", "two." in the recap) or a short reply ("Mm-hmm."; F-B
back-channels are captioned).

**Choosing the gold word (P-KEYWORD-SWAP, the single most visible device):**
1. Pick the word a viewer would search for: the object (`tracker`, `dough`, `aperture`), the action (`peel`, `fold`,
   `bloom`) or the payoff (`fresh`, `sharp`, `crispy`).
2. In a step, the first gold word is the step's subject; in the hook, it's the result's name.
3. Never gold on pronouns, articles, "really", "just", "so", or a number inside a unit phrase a tape already shows.
4. Two candidates in one chunk: the noun gets the gold; the verb stays white.
5. It's a rhythm, not wallpaper: about one every four seconds (v01 ≈ 16 a minute, v02 ≈ 15), so each one lands as an
   underline. Force or forbid one with `captions.overrides {i, emph: true|false}`.

### 5.4 Other text: the tapes
| ID | Element | Recipe | Hold |
|---|---|---|---|
| **TX-1** | STEP tape | P-STEP-TAPE: `accent` tape (pure black), h 100, padding 0 16, **square corners**, Courier Prime 700 **60 px** caps (measured cap height 44 px), tracking 0.18 em, `paper` lettering with a 1 px dark emboss (`text-shadow: 0 1px 0 rgba(0,0,0,.55)`) and a 1 px top highlight on the tape (`inset 0 1px 0 rgba(255,255,255,.08)`); top y 165, centred x 540; ≈ 300 px wide for `STEP 1` (measured x 386–687, y 165–264); `TC-label` | The step's first plate shot: on with its cut, off with the next (2.1–3.4 s measured) |
| **TX-2** | Tool / measure / wait tape | The same tape at h 64, Courier Prime 700 40 px, tracking 0.25 em, padding 0 26, rotated −2…+2° (seeded per reel), pinned beside the object | 1.5–3.0 s |
| **TX-3** | Name tape (F-B) | The same tape, h 64, 40 px, `NAME · ROLE`, x 64, top 1200 | 2.0 s on the guest's first full single |
| **TX-4** | CTA tape | Tape h 100, square, Courier Prime 700 56 px, tracking 0.18 em, padding 0 20, top 165, centred x 540 | ≥ 1.5 s (2.5 s default) |
| **TX-5** | Card title | Inter Tight 600 52 px, sentence case, on cream or night cards | the card's life |
| **TX-6** | Print caption | Instrument Serif italic 48 px under a P-PHOTO-PRINT | the card's life |
| **TX-7** | Paid-partnership line | Inter Tight 500 24 px, `paper` at 70 %: "Paid partnership", only on a sponsored reel | ≥ 2 s |

Tape text is ≤ 3 words plus an optional number ("STEP 3", "0.5 MM NIB", "18 G · 0.6 OZ", "WAIT 4 MIN"). All caps, never
sentence case.

### 5.5 Language and numbers
- `en` → captions verbatim; brand, tool and ingredient names exact (the glossary).
- `hinglish` → `hinglish`, Latin: romanised as spoken, English terms verbatim; the gold rules are unchanged (the italic
  serif works on Latin).
- `hinglish` → `en`: translate; choose the gold word in the English line.
- `hi` → `hi`, Devanagari: CS-3 (colour emphasis, no italic); tapes stay Latin caps (`STEP 1`), because the mono caps are
  Latin-only.
- Numbers: international grouping and dual units by default ("200 ml (6.8 fl oz)", "180°C (356°F)"); with Hindi or
  Hinglish, Indian grouping and metric only. Pre-paint the currency glyph. A quantity on a tape uses the creator's unit
  first, formatted with `ctx.fmtNum(v, {unit, units: "dual"})`.

---

## §6 Hook system

There's no on-screen title in this style, so the hook is a picture and a sentence: the finished thing, moving, at frame 0,
and the first words naming it. The post title does the promising, and it follows the hook-title rule: it promises the
viewer something (an outcome they want, a curiosity gap, or who it's for), true to what the reel delivers ("My 4-step
morning pour-over", "The last wallet you'll ever buy", not "Coffee tutorial"). Write 8–10 title candidates (§6.6, App. B),
pick by the stopper test, keep the next two as alternates.

HA-14 is the default for both formats because it's what the reference does: caption and live footage at frame 0, payoff
within a second. (HA-01's result-first idea lives on in the hook pair, §6.5; HA-01 itself needs a headline and a face at
frame 0, which this style never shows.)

### 6.1 The stopper test
- **Thumbnail:** at 25 % scale, frame 0 shows the finished result filling ≥ 35 % of the frame (F-A), or a face filling
  ≥ 20 % (F-B). No headline is needed.
- **Mute:** with the sound off, the first three seconds show *what was made* (the result and its gold name) or *what's
  claimed* (the claim's gold word).
- **Motion at frame 0:** hands moving the result (F-A) or the speaker mid-word (F-B).
- **Payoff:** the result in frame and sharp by 1.0 s, its gold name by 1.5 s (F-A); the claim's gold word by 1.5 s (F-B).
- **Dense, never busy:** the first seconds of F-A carry two hidden cuts and the caption building word by word; nothing
  else.

### 6.2 HA-14 "Result in hand" (default, F-A)
The finished result, in the creator's hands, is the first picture; the first sentence names it; the reel then promises
how to make it.

| t | Beat | Tone | Picture (layout) | Caption (CS-1) | Camera / cut |
|---|---|---|---|---|---|
| **f0** | Result in motion | awe | L-overhead: the SH-2 result clip mid-motion (hands turning, opening or lifting it); motion blur on f0–f4 is fine | — (the first word lands by f3) | — |
| 0.10–1.0 | "This is my…" | awe | The result settles, sharp by f30, inside y 200–1250 | "This is my" → word by word | — |
| ~1.0 | The name | awe | Same plate | "…**system**" (gold italic: the result's name) | — |
| 1.6–2.7 | Hand passes | awe | Same shot: the free hand sweeps across the result 3–4 times (each pass ≈ 5 f of blur), keeping the frame alive without a cut | the second line builds under the first ("and how I stay on track.") | — |
| ~2.8 | Hidden cut | awe | **T-02** on the frame the last pass exits → P-ANGLED-HERO: the result held at 30–45°, background black, soft and pushing in | "**Track** habits," | T-02 |
| 3.5–5.5 | Benefit run | awe | 1–2 more result angles, 1.0–1.5 s each, each with its own gold word | "track work, track **everything**" | T-02 / T-01 |
| 5.5–8.0 | Promise | explain | **G-2 hard cut to L-desk**: the creator, seated, says the promise and the count ("…here's how I set one up in five steps") | "in **five** steps" (gold on the count) | Z-1 push-drift 1.00 → 1.03 |
| 8.0 | Into step 1 | explain | **G-1 cut on "First"** to L-overhead; the STEP 1 tape pops on | "First, I…" | T-01; the list cue |

Evidence: v01 0:00–0:08 (f0–f2 a blurred flip, cut f3, the notebook swings open f4–f9 and is sharp at f10; the hand
passes 1.6–2.7 s inside one shot; "This is my *system*" at 1.0; cut 2.77 to the angled notebook; "*Track habits, track
work,* track everything" 0:03–0:05; the desk at 0:06; STEP 1 at 0:08).

### 6.3 HA-14 "Mid-sentence cold open" (default, F-B)
| t | Beat | Picture (L-speaker) | Caption (CS-2) | Cut |
|---|---|---|---|---|
| **f0** | Mid-thought | The speaker who makes the claim, tight single, mouth already moving | the first word by 0.10 s | — |
| 0.1–1.5 | The claim builds | same | words build one by one; the claim's key noun goes gold by 1.5 s ("like, *printing*") | — |
| 1.5–3.0 | The claim lands | same | "*photos* is what makes the…" | — |
| 3.0–5.2 | The first turn | **cut on the handover** to the other speaker, or a 1.0–2.6 s reaction cutaway if the speaker keeps going | the listener's words in `cream` (guest) or white (host) | T-05 / T-06 |

Evidence: v02 0:00–0:05 (a face at f0, "I'm wondering" at 0.17, "*printing*" at 1.33, "*photos*" at 1.83, the first cut
at 5.03).

### 6.4 Alternate hooks
| ID | Name here | Format | f0 | Payoff | Use when | For example |
|---|---|---|---|---|---|---|
| **HA-10** | Desk flash → result | F-A | L-desk: the creator holding up or pointing at the result, the first caption word | Cut to the result full-frame overhead by 0.7 s | The creator's face is the draw (an established channel) or the result is small | "This is the only knife I sharpen like this" → cut to the blade on the stone |
| **HA-16** | Process cold open | F-A, F-B | F-A: the most satisfying moment of the process (a pour, a fold, a stitch pulled tight), no caption needed for 1 s; F-B: a laugh or reaction already in progress | The result or the claim by 5 s | The process itself is the hook (ASMR-like), or the clip starts on a reaction | The bloom of a pour-over for 1.5 s, then "this is how I…" |

### 6.5 Hook pairs by topic
Subject → reveal (F-B: claim → answer). Write the pair for every new reel.

| Topic | First subject (f0) | Reveal by 1.0–5.5 s | How each is shown |
|---|---|---|---|
| Morning pour-over (food) | The finished cup, coffee swirling as the hand sets it down | "This is my morning **ritual**" → kettle, grounds, the pour (2 angles) → desk promise "four steps" | SH-2 overhead cup; SH-4 angled cup; desk |
| Sourdough loaf (food) | Hands turning the baked loaf to show the ear | "This is my everyday **loaf**" → the crumb when it's torn | SH-2 overhead; SH-4 crumb close |
| Weekly meal prep (food) | Hands sliding five filled containers into a row | "Five lunches, one **hour**" → lids closing one by one | SH-2 overhead row |
| Leather card holder (craft) | Hands sliding cards into the finished holder | "This is the last **wallet** I'll ever buy" → the stitching close | SH-2 overhead; SH-4 edge burnish insert |
| Hand-bound notebook (craft) | Fanning the pages of the bound notebook | "This is my **notebook** system" → the spine stitch close | SH-2 overhead; SH-4 angled |
| Film camera loading (photography) | Hands closing the back of the loaded camera, advancing the lever | "Load **film** without wasting a frame" → the first frame counter | SH-2 overhead; SH-4 top plate insert |
| Print your photos (photography) | Hands laying three prints onto the desk | "Your photos deserve **paper**" → the printer feed | SH-2 overhead prints |
| Plant propagation (other hands-on) | Hands lifting a rooted cutting out of a jar | "One **leaf**, one new plant" → the cut node | SH-2 overhead; SH-4 roots |
| F-B: printing photos | "I'm wondering if, like, **printing** photos is what makes…" | the listener's push-back by 5 s | L-speaker singles |
| F-B: home bread | "The thing that ruins most home **bread** isn't the flour" | "…it's the oven" by 4 s; the listener laughs | L-speaker singles |

### 6.6 The opening line and the post title
- **Opening line (F-A):** `This is my [gold RESULT NOUN]` / `[Result] in [N] steps` / `The [gold ADJECTIVE] way to
  [verb] [thing]`. At most 8 words before the first gold word lands; the gold word lands by 1.5 s. If the take opens with
  filler ("So, um, today…"), cut it: the first kept word is the first word of the line.
- **Opening line (F-B):** the clip starts on the claim, never on the question that led to it; the first gold word is the
  claim's subject. Try every cut-in point the take offers and pick by the stopper test.
- **Post title:** `[Result noun]: [N] steps`, a promise ("Make your own [object]"), or the claim quoted (F-B). Sentence
  case, no emoji in the title (the post caption may carry one). 8–10 candidates; the best by the stopper test; two
  alternates.
- **Banned:** "Game changer", "You won't believe", "Life hack", a count that doesn't match the steps, any line the reel
  doesn't show.

### 6.7 Hook sound
Dry: the voice and the process sound only (the pour, the page, the pen). No cue in the hook; the bed enters with the
promise line (§11).

### 6.8 CTA
| Device | Spoken pattern | On screen | Hold | Where |
|---|---|---|---|---|
| `none` (default) | The last line is the close ("…and now it's ready to go.") | Nothing; the reel ends on the result (P-END-ON-RESULT) | — | the end |
| `comment_keyword` | "Comment KEYWORD and I'll send you the [deliverable]." | P-CTA-TAPE `COMMENT · KEYWORD` in the tape band over the final overhead or result shot (§3.7 for a desk shot); the keyword is also the gold word in the caption | ≥ 1.5 s (2.5 s default) | the last 4 s |
| `link_bio` | "The [tool / recipe] is linked in my bio." | P-CTA-TAPE `LINK IN BIO` | ≥ 1.5 s | the last 4 s |
| `post_only` | none in the video | Nothing; the CTA lives in the post caption | — | — |

No cue in the 1.0 s before the CTA's first word. The reel ends ≤ 6 f after the last word (T-07). A sponsored reel carries
the TX-7 "Paid partnership" line for ≥ 2 s; there is no end card.

---

## §7 Structure and rhythm

### 7.1 Structure
- **F-A `tutorial`:** hook (the result in hand, a few seconds) → promise (the desk, one sentence) → STEP 1…N → recap (one
  turn-through) → close (the desk or the result) → optional CTA. v01 for the shape: hook 0–6, promise 6–8, STEP 1
  0:08–0:37, STEP 2 0:38–0:46, STEP 3 0:47–1:06, STEP 4 1:07–1:24, STEP 5 1:25–1:30, recap 1:31–1:43, close 1:44–1:50.
- **F-B `conversation`:** claim (the cold open) → push-back or question → reframe or story → agreement or laugh (the
  button). No markers.

A step lasts as long as its action needs to be understood. With many steps in a short reel, the later ones tighten to
their single most telling action and the state jump.

### 7.2 Markers
**SM-TAPE** (F-A): the STEP tape (P-STEP-TAPE) at **every** step, numbered from 1 (`STEP 1`…). Never "Step one", never
"01", never "STEP 1/5" (v01 shows the bare number). After the last step the recap (P-RECAP-STRIP) replays every tape in
order. No teaser chips. F-B has no markers (spoken only).

### 7.3 The unit ritual (every step, identical)
| # | Frames (from the ordinal word's onset = 0) | What |
|---|---|---|
| 1 | −1 f | **G-1 cut** from L-desk (or from the previous step's last plate) to L-overhead on the ordinal word ("First", "Step two", "Next", "Then"). With no ordinal in the take, cut on the step's action verb |
| 2 | 0 | **The STEP N tape pops on, complete, on the cut frame**: no feed, no typing, no fade (measured on all 5 steps, v01 7.73, 37.77, 46.80, 66.90, 84.93) |
| 3 | 0 → the next cut (2.1–3.4 s measured, mean 2.8 s) | The tape holds for exactly the first plate shot and **disappears hard on the next picture cut** (0–4 f before it). So the step's first plate is a 2.1–3.4 s shot; declare that cut in `cuts` |
| 4 | the step's body | Overhead plates, each cut hidden in motion (T-02 / T-03, the hand-cut selection, §1). The step's subject noun gets the first gold word. On the tool or quantity word: one P-TOOL-TAPE, P-MEASURE-TAPE or P-WAIT-TAPE, never while the STEP tape is up; if the trigger word falls inside the STEP tape's hold, skip the tape and make that word the gold word instead |
| 5 | the run's last 1.0–1.5 s | **P-STATE-JUMP** to the step's finished state (the same framing, a later moment) |
| 6 | the "why" sentence | **G-2 cut** to L-desk (with the Z-1 drift) for the reason or the tip, or P-DESK-SHOW (the creator shows the object to the camera). A short step skips the desk; the next step's G-1 follows directly |

**The recap ritual:** the desk line that starts it ("So now you've got…") → a cut to **one continuous overhead shot of the
finished object in both hands**, the STEP 1 tape popping on with it. The hands turn to each step's page (at most one hidden
cut, on a flip). For each step k the caption builds "You've got your **[item]**," then the ordinal alone as its own chunk
("one."), and the tape swaps to `STEP k+1` on the flip after that ordinal (E6, P-RECAP-STRIP). Each entry gets a beat of
its own (1.9–3.6 s in v01, 13.0 s for five steps); the tape exits hard on the cut back to the desk. Then the close.

### 7.4 Open loops
- **The result at frame 0 is the loop**: paid off when the last step finishes and the close shows it again.
- **The step count spoken in the promise** is paid off by the recap.
- **The re-hook (F-A, a longer reel):** around the middle, before a step starts, P-RESULT-FLASH: about a second of the
  finished result from a new angle, the gold on the result noun ("…and this is where the **tracker** starts to pay off").
  If a step's own payoff shot already shows the full result there, that shot is the re-hook. F-B is short and needs none.
- The hook and the promise are over fast, so the first step arrives while the promise is fresh (v01: 8 s of a 110 s reel).

### 7.5 Rhythm by feel
- **It breathes with the hands.** The picture never sits still because the hands never do, but the edit never hurries
  them: a cut arrives when the action reaches a new moment, hidden inside the motion that got it there. Something new
  always comes when the words or the hands give it a reason.
- **Dense in time, never in space.** The hook is the busiest moment: two hidden cuts and a caption building word by word
  inside three seconds. The promise is one calm desk shot. The steps run even, a cut every couple of seconds, each one
  invisible. The caption swaps keep a soft pulse underneath.
- **Escalate into the last step.** It gets the most satisfying visual: the final assembly, the reveal pour, the stitch
  pulled tight, held a little longer than anything before it. Then the recap slows down (one shot, the tape counting), and
  the close is one calm shot and a hard end.
- **Holds are earned.** A long continuous action (writing out a full page, kneading) may run unbroken while it's still
  changing on screen; the moment it stops changing, cut or jump.
- **The desk is a breath, not a stop.** A return lasts the length of one "why" sentence and no longer.
- **F-B:** the handovers set the rhythm, a cut every few seconds as the floor changes; the listener's face comes in on the
  punchlines and strong claims; the last two seconds are a reaction or a short reply, and it ends there.
- For reference, measured on the two reels (a description, not a target): v01 23.5 cuts a minute (desk jump cuts
  included), median shot 1.98 s (p90 4.7 s), longest overhead hold 6.7 s (continuous writing); v02 19.0 cuts a minute,
  median shot 2.67 s (p90 5.3 s), longest 5.9 s.
- Information only: no entertainment beats. The satisfaction is the process; every step ends on a visibly changed object.

---

## §8 Visual system: B-roll and patterns

### 8.1 The role of graphics
- **Three recurring graphic devices, and only three:** the gold caption word, the tape family (STEP / tool / measure /
  wait / name / CTA), the recap strip. Everything else is footage you select, cut and grade. Most of the 36 patterns below
  are cut and footage patterns (how the footage is chosen and joined), because that's where this style's craft lives.
- **Numbers don't become pictures.** A quantity is shown by the hands doing it (the scale reading, the thermometer in
  shot) and, at most, named on a P-MEASURE-TAPE.
- **Variety comes from the moment:** a new angle, a closer pass, a state jump, a detail punch. The step ritual is the one
  deliberate repeat. Two identical framings never sit back to back across a cut, except P-STATE-JUMP (that's its point).

### 8.2 Families
| ID | Family | Source | What it comes from |
|---|---|---|---|
| **B-1** | Overhead demo footage | the creator's | SH-1, SH-2 vertical overhead clips |
| **B-2** | Desk footage (A-roll, inserts) | the creator's | SH-3 desk take, SH-4 inserts |
| **B-3** | Conversation footage | the creator's | SH-5 cameras, SH-6 reactions |
| **B-4** | Label tapes | engine | — |
| **B-5** | Caption keyword | engine (the caption profile) | — |
| **B-6** | Grade and finishing | engine | — |
| **B-7** | Insert cards | the creator's third-party file, else the real one fetched from the web, else engine (a created substitute) | screenshots, screen recordings, photos (the creator's, else fetched with the source noted; created only when nothing usable turns up, §12.4) |
| **B-8** | Cut grammar | the editor (the cut itself) | — |

### 8.3 Pattern specs
Frames at 30 fps. Engine building blocks are named so the scene code is unambiguous.

**A. Type and tapes (B-4, B-5)**
| ID | Type | What's on screen | Motion recipe | When | Engine |
|---|---|---|---|---|---|
| **P-KEYWORD-SWAP** | annotation (caption) | One word of the white caption set in Instrument Serif italic, gold, 1.3× | Fades in on its onset like every word (3 f, blur 4 → 0); stays until the chunk clears (hard) | One per chunk, about every four seconds, on the topic noun / key verb / name (§5.3) | `TC-subtitle`; CS-1/2 `emphasis.mechanism: font_swap`; force with `captions.overrides {i, emph}` |
| **P-STEP-TAPE** | overlay (marker) | Black label tape `STEP N`, top centre y 165–265, ≈ 300 × 100, square corners | Pops on complete on the cut frame (0 f); holds for the first plate shot (2.1–3.4 s); off hard on the next picture cut (0 f). No feed, no typing, no fade | The first frame of every step's overhead run | `TC-label` 60 px; bespoke scene, z6, `in: "none"`, `out: "none"`, t1 = the next cut |
| **P-RECAP-STRIP** | stage + overlay | One continuous overhead shot: both hands turn the finished object to each step's page; the tape counts `STEP 1` → `STEP N`, one per spoken ordinal; the caption "You've got your **[item]**," then "one." | One tape scene for the strip: the container fixed at the widest label's width (`data-slot`), pops on at the cut in, its text swaps hard on the frames listed in `events`, off hard on the cut out; one plate scene (1–2 segments, the join on a page flip) | After the last step, before the close | `TC-label`; `exception: "E6"`: one `data-slot` rect constant ±4 px, the text swapping on the frame the ordinal lands, during a flip; first entry and final exit on picture cuts (v01 @1:31.1–1:44.2: STEP 1 → 5 at 91.1, 93.1, 95.0, 98.6, 101.3; one hidden cut at 93.3) |
| **P-TOOL-TAPE** | overlay (label) | A tape naming the tool, ingredient or material ("0.5 MM NIB", "BREAD FLOUR") beside the object, rotated −2…+2° (seeded) | Pops on (0 f) on the trigger word or a cut; holds 1.5–3.0 s; off hard on a cut, else a 2 f fade | On the tool's name, with the object in shot; one per step at most; never while the STEP tape is up | `TC-label` 40 px, z5; placed statically in the tape zone (§3.6), never tracked; an extension of the STEP tape (inferred, not in the reference) |
| **P-MEASURE-TAPE** | overlay (label) | A tape with the spoken quantity, the creator's unit first: "18 G · 0.6 OZ", "92°C · 198°F", "3 MM · 1/8 IN" | as P-TOOL-TAPE | On the spoken number; the number must be spoken | `TC-label` 40 px, z5; numbers via `ctx.fmtNum(v, {unit, units: "dual"})` |
| **P-WAIT-TAPE** | overlay (label) | A tape with a duration: "WAIT 4 MIN", "REST 1 HR" | as P-TOOL-TAPE, starting on the cut that skips the wait (P-STATE-JUMP) | Wherever the process skips time | `TC-label` 40 px, z5 |
| **P-NAME-TAPE** | overlay (label, F-B) | `NAME · ROLE` tape at x 64, top 1200 | Pops on (0 f); holds 2.0 s; off hard on a cut, else a 2 f fade | The guest's first full single, when the guest isn't the creator | `TC-label` 40 px, z5; bottom 1264, clear of the CS-2 band (from ≈ 1310) and of the face (§3.7) |
| **P-CTA-TAPE** | overlay (CTA) | `COMMENT · KEYWORD` or `LINK IN BIO`, top centre, 56 px (TX-4) | Pops on (0 f); holds ≥ 1.5 s; no exit (the reel ends) | The last 4 s, only with a CTA device (§6.8) | `TC-label`; `kind: "cta-keyword"`, `text_content` contains the keyword |

**B. Overhead and desk footage (B-1, B-2, B-8)**
| ID | Type | What's on screen | Motion recipe | When | Engine / evidence |
|---|---|---|---|---|---|
| **P-OVERHEAD-PLATE** | stage (footage) | A vertical overhead clip full-bleed (1080 × 1920, cover crop) while the stage is `L-overhead` (hidden) | One z1 scene per overhead run with `segments: [{asset, from (local s), offset (clip s), crop?}]`; render picks the active segment and draws `ctx.videoFrame(seg.asset, lt - seg.from + seg.offset)`; every segment boundary is listed in `cuts`; `kind: "broll"` | Every step's body | SH-1; z1, graded with `ctx.grade` (P-GRADE-PASS) |
| **P-RESULT-OPEN** | stage (footage) | The finished result moving in the hands at f0 | A P-OVERHEAD-PLATE from t 0 on SH-2, offset chosen so f0 is mid-motion and f30 is sharp | Hook f0 (§6.2) | SH-2 (FB-2); `satisfies: ["footage"]`; v01 @0:00 |
| **P-HAND-SWIPE-CUT** | cut | Cut on the frame where a hand or arm covers ≥ 50 % of the frame width while moving ≥ 25 px a frame; the next clip starts on a hand leaving or entering in the same direction | 0 f; out-frame and in-frame picked at ±2 f around the peak blur | Overhead → overhead; overhead → desk | v01 @0:01.5, @0:34, @1:12 |
| **P-FLIP-CUT** | cut | Cut at the peak of an object's rotation: a page turning, the object flipped, a lid lifting | 0 f; the frame of maximum blur or the edge-on angle | When the object turns | v01 @0:00.1, @1:12 |
| **P-HELD-TO-CAMERA** | stage (insert) | The object held up close to the desk camera, the background falling to black | A plate on SH-4 (or the desk take, crop 1.0); P-RACK-IN on entry when the footage has no real rack | Naming a detail or a component; the recap entries | SH-4 (FB-4); v01 @0:03–0:05, @0:38, @1:31–1:43 |
| **P-ANGLED-HERO** | stage (insert) | The result held at 30–45°, shallow focus, a dark surround | A plate on SH-4 that **pushes in 1.00 → 1.18, ease-out** (most of it in the first 0.6 s; measured up to ×1.22) **and racks soft → sharp over ≈ 35 f** (measured 2.77–4.57 s: ×1.22, sharp at 4.3). Keep the footage's own push if it has one; else draw the scale in the plate | The hook's second angle; the close | SH-4; v01 @0:02.8–0:05 |
| **P-DESK-TALK** | stage (A-roll) | The creator seated, chest-up, the lined background | L-desk; Z-1 slow drift on longer shots; plain jump cuts on sentence ends, an occasional Z-2 re-crop | The promise, every "why", the close | SH-3; v01 @0:06, @0:57–1:06 |
| **P-DESK-SHOW** | stage (A-roll) | The creator shows the object or material to the camera in the desk take | L-desk; no zoom; the caption names it in gold | Introducing a material, a tool, the result | SH-3; v01 @0:41, @1:05, @1:48 |
| **P-MACRO-PUNCH** | footage treatment | A crop-in on the overhead detail (1.20–1.35×): the nib, the seam, the dial | A hard re-crop on a cut (never animated); the scale stays for the shot; the detail lands inside y 300–1200 | The detail word ("this edge", "right on the line") | Segment `crop: {scale, cx, cy}`; 4K vertical for 1.35× |
| **P-STATE-JUMP** | cut | The same framing, a later state (time skipped): the empty grid → the filled grid | Hard cut, 0 f; the object's position matches within ±30 px | The end of a step; any wait | SH-1 filmed in two passes; v01 @0:34–0:35 |
| **P-RESULT-FLASH** | stage (re-hook) | About a second (0.8–1.2 s) of the finished result from a new angle | A plate segment cut in and out hard; the gold word on the result noun | The mid-reel re-hook (§7.4) | SH-2 / SH-4 |
| **P-RACK-IN** | footage treatment | The insert starts soft and racks into focus | Plate filter `blur(6px)` → `blur(0)` over ≈ 35 f (30–40), ease-in-out, from the cut frame (a slow rack, not a snap) | Entering P-HELD-TO-CAMERA / P-ANGLED-HERO without a real rack | v01 @0:03 (a real rack) |
| **P-SLOW-PUSH** | footage treatment (camera) | The desk shot drifts in 1.00 → 1.03 (barely seen) | `camera {t, preset: "push-drift"}` over the shot | Longer L-desk shots, not every one | Z-1; v01 57.0–66.9 measured 1.00 → 1.024 over 9.9 s |
| **P-JUMP-RECROP** | footage treatment (camera) | A desk jump cut. Default: a **plain jump cut, same framing** (4 of 5 measured: v01 60.9, 80.8, 89.7, 107.8); occasionally a small re-crop 1.00 ↔ 1.07 (v01 90.2) | Plain cut on a sentence end; for the re-crop `camera {t: cut, preset: "snap-punch"}` + `reset` on the next cut | Every jump cut inside one desk take; the re-crop stays the exception | Z-2 |

**C. Grade and fallbacks (B-6, B-1)**
| ID | Type | What | Recipe | When | Engine |
|---|---|---|---|---|---|
| **P-GRADE-PASS** | footage treatment | GR-tungsten over the whole reel | **Built in, no scene.** The stage footage takes `tokens.grades.footage` (the GR-tungsten numbers, vignette 0.50 on the window, bloom 0.12) automatically; GR-tungsten-soft is `timeline.grade: "GR-tungsten-soft"`. Video assets aren't graded by the core, so every z1 plate or still scene that draws `ctx.videoFrame` or an image asset sets `style="${ctx.grade(ctx.gradeId \|\| "GR-tungsten", {spatial: true})}"` on its `<img>` / plate div (the same preset, vignette included). Creator photos or recordings inside z3 cards take `ctx.grade(...)` colour-only (no `spatial`); drawn card chrome, tapes and captions stay ungraded | Every reel, both formats | — |
| **P-PLATE-BAND** | stage (fallback) | A horizontal 16:9 overhead clip as a band (1080 × 608, cy 760) over a blurred, darkened copy of itself (blur 40 px, brightness 0.45) | A plate variant: two draws of the same frame (the blurred cover + the sharp band) | FB-1: the creator's overhead is horizontal | W-desk; `fx.clip` building blocks |
| **P-STEP-STILL** | stage (fallback) | A still photo of the step's state, full-bleed, pushing 1.00 → 1.06 over the shot | A plate segment on an image asset; the push eased; hard cuts between stills | FB-1: only photos of the steps exist | image assets |

**D. Conversation (B-3, F-B)**
| ID | Type | What | Recipe | When | Evidence |
|---|---|---|---|---|---|
| **P-COLD-OPEN** | cut | The clip starts mid-sentence on the claim | The in-point 1–3 f before the first kept word; no lead-in silence | F-B f0 | v02 @0:00 |
| **P-SPEAKER-CUT** | cut | Cut to the new speaker on their first word | `timeline.shots` boundary, 1 f lead, ±3 f | Every handover | v02, 15 cuts in 47 s |
| **P-REACTION-CUTAWAY** | cut | 1.0–2.6 s of the listener (a nod, a smile, a look away) while the speaker continues | Shot `cut_reason: "reaction"`; never across a handover; the captions stay with the speaker | On a punchline or a strong claim inside one speaker's long run | v02 @0:08, @0:37 |
| **P-TALK-RECROP** | cut | A re-crop 1.00 ↔ 1.15 on a sentence boundary inside one speaker's run | Shot `cut_reason: "recrop"`, `step: 1.15` | Long single runs (beyond about 5 s) | 4K source |
| **P-BUTTON-END** | cut | The last 1.0–2.0 s is a reaction or a two-word reply ("Yeah, yeah."), then a hard end | The last shot is the reaction or the reply; T-07 | F-B end | v02 @0:43–0:46 |

**E. Inserts (B-7; §12.4)**
| ID | Type | What | Recipe | When | Created substitute |
|---|---|---|---|---|---|
| **P-SCREEN-INSERT** | overlay (card) | A screen recording or screenshot (the creator's, else the real page captured from the web) in a dark card (radius 18, a 1 px `rgba(255,255,255,.12)` border) on W-desk | `fx.shot` (the creator's or a fetched file) or `fx.appUI` (a generic UI, when no real screen turns up) at x 64–1016, y 260–1240; rises 10 f; a 1.00 → 1.04 push inside the card | An app or software in the step (an editing app, a timer, a camera menu) | `recreated_ui` |
| **P-PHOTO-PRINT** | overlay (card) | A photo as a matte print: a 28 px cream border, rotated −1.5°, a soft shadow, on W-desk; an italic serif line under it (TX-6) | The card rises 10 f; holds; hard out | A photo the reel needs (a past result, a reference, the product): the creator's, else a real one fetched from the web | none: when no real photo turns up, use P-RESULT-FLASH or cut the moment |
| **P-PRODUCT-TAPE** | overlay (label) | A product or brand name set on a tape (type, never a logo), with an optional serif subline ("my everyday kettle") | The P-TOOL-TAPE recipe at 48 px, centred at y 700 on W-desk, or beside the object on a plate | A product named with no clean shot of it (a fetched product photo goes in P-PHOTO-PRINT instead) | `logo_plate` |
| **P-QUOTE-CARD** | overlay (card) | A cream card (radius 6): the quote in Instrument Serif italic 54 px, the name in mono 28 px caps; word for word | `fx.quoteCard` with the paper theme; a word-by-word reveal | Someone else's words read aloud | `quote_card` |

**F. Close**
| ID | Type | What | Recipe | When | Evidence |
|---|---|---|---|---|---|
| **P-FLASH-CUT** | transition | The picture blooms to white and the next shot is revealed from the top down | T-08 (§9.1). **A built-in transition, no scene:** a `timeline.transitions[]` entry `{"t": <cut>, "type": "flash", "frames": 7, "pre": 2, "peak": 1.0, "decay": 0.4, "colour": "#FFFFFF", "clear": "wipe", "clear_frames": 2, "dir": "down"}` (default `layers: "picture"`: it covers the world, the footage and the z1 plates, under the captions). It rises over the 2 `pre` frames (the bloom), peaks on the cut, holds near-white ≈ 3 f, then clears in the measured 2 f top → bottom wipe | A step boundary or a P-STATE-JUMP time skip | v01 34.57 ("It starts to fill"), 37.57 (into STEP 2) |
| **P-END-ON-RESULT** | stage | The final shot shows the finished result: in hand, at the desk or overhead | A hard end ≤ 6 f after the last word | Every F-A reel | v01 @1:48 |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the moment needs (what should the
viewer see the hands do right now?), then use it.

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
| Food: "add the salt", "pour in circles", "fold the dough" | P-OVERHEAD-PLATE (+ P-MEASURE-TAPE for the amount) | P-MACRO-PUNCH |
| Food: "it's ready when…" | P-STATE-JUMP → P-HELD-TO-CAMERA (the texture to camera) | P-ANGLED-HERO |
| Craft: "punch the holes", "stitch", "burnish the edge" | P-OVERHEAD-PLATE + P-MACRO-PUNCH | P-TOOL-TAPE |
| Craft: "the glue needs to dry" | P-STATE-JUMP + P-WAIT-TAPE | — |
| Photography: "set your aperture to f/2" | P-MACRO-PUNCH on the dial + P-MEASURE-TAPE `F/2` | P-SCREEN-INSERT (the creator's camera-menu recording) |
| Photography: "in my editing app I…" | P-SCREEN-INSERT | P-DESK-TALK |

### 8.5 Numbers and truth
No charts, counters or figure cards. Quantities are spoken by the creator and shown by the hands; a tape repeats them
exactly. A recreated app screen (P-SCREEN-INSERT with `fx.appUI`) may show made-up but realistic values (`illustrative:
true`), with no label and no credit line; a value the creator says is shown as said.

### 8.6 Assets
- **Real footage first:** every step is the creator's own overhead footage. No stock, no AI-generated hands, food or
  objects.
- Third-party moments: the creator's files first, else the real thing fetched from the web, source noted (§12.4).
- Created cards (§8.3 E), only when nothing usable turns up, are generic and unbranded; product names on a plate are set
  in type on a tape (the style's quiet label).
- Blur personal data on screen recordings and labels for its whole time on screen.

---

## §9 Transition system

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue |
|---|---|---|---|---|
| **T-01** | Hard cut | 0 | On a word boundary ±1 f (desk), or anywhere inside an action (overhead) | none |
| **T-02** | Hand-swipe cut | 0 | P-HAND-SWIPE-CUT: out on ≥ 50 % hand coverage in motion, in on a matching hand motion, ±2 f | none |
| **T-03** | Flip cut | 0 | P-FLIP-CUT: cut at the object's peak rotation / blur | none |
| **T-04** | Rack-in | 8 (on the incoming insert) | P-RACK-IN: blur 6 → 0 px, ease-out, from the cut frame | none |
| **T-05** | Speaker cut (F-B) | 0 | On the new speaker's first word, 1 f lead, ±3 f | none |
| **T-06** | Reaction cut (F-B) | 0 | Into and out of a listener reaction, on a word boundary of the speaker | none |
| **T-07** | Hard end | 0 | ≤ 6 f after the last word; no black tail, no fade | none |
| **T-08** | White flash | 7 | P-FLASH-CUT: f0–1 the outgoing shot washes out (a bluish-white bloom), f2–4 solid white `#FFFFFF`, f5–6 the white recedes downward (a soft-edged top → bottom wipe) revealing the incoming shot; the captions stay on top. Measured v01 34.57–34.77 and 37.57–37.77. Built: `transitions[]` `type: "flash"` (7 f, pre 2, peak 1.0, decay 0.4, `clear: "wipe"`, `clear_frames: 2`, `dir: "down"`) | none (silent) |

That's the whole library. The flash is the only thing ever drawn between shots; it has no cap, but in this style it's a
rare punctuation mark, so each one reads as a turn of the page (v01 used it twice: on the state jump and into STEP 2).

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | A mid-motion result (F-A), a mid-sentence speaker (F-B) | A fade-in, a still frame, a title |
| Inside the hook | T-02 / T-03: two hidden cuts by 3 s | A visible jump on a static frame; a flash |
| Hook → promise | T-01 to L-desk on the promise's first word | — |
| A new step | T-01 or T-02 + the STEP tape; T-08 when the step boundary is a real turn (v01: into STEP 2) | Any other effect, a pause |
| Overhead → overhead | T-02 / T-03; P-STATE-JUMP for time skips (T-08 may mark one) | Two identical framings back to back (except P-STATE-JUMP) |
| Overhead → desk | T-02 (the hand leaves the frame) or T-01 on the "why" sentence | A cut inside a word |
| Desk jump cut | T-01, plain; now and then P-JUMP-RECROP | Two re-crops in a row |
| Into an insert | T-01; T-04 for desk inserts | — |
| Recap entries | No cut: the hands turn the pages, the tape counts; at most one hidden cut (T-03 on a flip) | Hard cuts between stills |
| F-B handover | T-05 | A cut inside a word; a split screen; a flash |
| Last word | T-07 | A black tail; an outro card (unless a §6.8 device) |

### 9.3 Shot grammar
| ID | Rule |
|---|---|
| **R-1** | **Cut on hand motion:** in overhead runs nearly every cut is hidden (T-02 or T-03). A hard cut on a static frame only at a step's first frame |
| **R-2** | **Ordinal → overhead:** the cut into a step's overhead lands within ±2 f of the ordinal word |
| **R-3** | **Why → desk:** the desk returns on the first word of the reason or tip sentence and lasts that sentence |
| **R-4** | **Match action:** a motion that crosses a cut keeps its direction (a hand moving right exits right; the next clip's hand moves right) |
| **R-5** | **State-jump framing:** P-STATE-JUMP keeps the object's position within ±30 px; otherwise it reads as a mistake, so re-frame with a segment crop |
| **R-6** | **Handover (F-B):** a cut within ±3 f of every new speaker's first word; a back-channel ≤ 1.6 s ("yeah", "right") doesn't take the floor |
| **R-7** | **Reaction (F-B):** when one speaker holds the floor, cut away to the listener on a punchline or a strong claim (1.0–2.6 s), so the conversation never feels one-sided; never across a handover |
| **R-8** | **Re-crop (F-B):** in a long single run, re-crop 1.00 ↔ 1.15 on a sentence boundary |
| **R-9** | **Never cut inside a word**, in any format |

### 9.4 How the moves breathe
The cuts are invisible by design, so they can come as often as the hands give them a reason; T-01 and T-02 run back to
back through overhead runs and the recap without anyone noticing. Everything you *can* see is rare: a rack-in is for a
held-up detail, a re-crop for a long desk thought, a flash for a real turn. If a viewer could name the transition, it
should be the flash, and only at a step's edge.

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Lead | 1 f before the onset (captions, tapes) |
| Tape in / out | 0 f: pops on with a cut, off with the next cut (measured, all 6 tape appearances) |
| Caption word in | 3 f: opacity 0 → 1 with blur 4 → 0 px (v01 f91–93, f32–34; v02 f38–40); the chunk clears hard (0 f) |
| White flash | 7 f (T-08: 2 bloom, 3 white, 2 reveal) |
| Card rise (inserts) | 10 f, translateY 40 → 0 + blur 8 → 0, expo-out; exit 6 f fade |
| Rack-in | 35 f (30–40), blur 6 → 0 px, ease-in-out |
| Push-drift | 1.00 → 1.03 over the whole shot, in-out (desk); 1.00 → 1.18 ease-out (P-ANGLED-HERO, measured up to 1.22) |
| Re-crop | on a cut: 1.07 (desk, rare), 1.15 (F-B), 1.20 (an overhead take change, v01 84.9), 1.20–1.35 (P-MACRO-PUNCH) |
| Hold | tapes ≥ 2.0 s (STEP) / ≥ 1.5 s (others); text ≥ 0.25 s per word; any element ≥ 10 f |
| Easing | entry `cubic-bezier(0.22, 1, 0.36, 1)`; exit `(0.64, 0, 0.78, 0)`; in-out `(0.65, 0, 0.35, 1)` |

### 10.2 Footage camera (`zoom_policy: presets`)
| ID | Preset | Recipe | Use |
|---|---|---|---|
| **Z-0** | `reset` | Back to 1.00 on the next cut (1 f) | After a Z-2 |
| **Z-1** | `push-drift` | 1.00 → 1.03 over the shot, eased in-out | Longer desk shots (`explain`, `awe`, `win`) |
| **Z-2** | `snap-punch` | 1.00 → 1.07 in **1 f, on a jump cut only**, held until the next cut (a re-crop, never a visible zoom) | An occasional desk jump cut (`explain`, `warn`) |

Measured with ORB on every frame of v01 and v02: no synthetic zoom, rotation or shake anywhere; every apparent scale
change is the hands or the subject moving. So the camera barely exists: a drift you only feel, a re-crop you only notice
as a fresh angle, never two moves within 0.4 s, and a different move from one to the next so it never feels mechanical.
Plates are never zoomed by the camera (P-MACRO-PUNCH is a segment crop on a cut). The face never leaves y 220–760 on
L-desk.

### 10.3 Layer order (back to front)
1. The world (W-footage / W-desk), then **z1 overhead plates** (P-OVERHEAD-PLATE, P-STEP-STILL, P-PLATE-BAND)
2. The stage footage (the desk take; the composed podcast footage)
3. z3 insert cards (P-SCREEN-INSERT, P-PHOTO-PRINT, P-QUOTE-CARD; P-PRODUCT-TAPE on W-desk)
4. z4 free: the grade is built in (P-GRADE-PASS; footage graded by the engine, plates by `ctx.grade`)
5. z5 tool / measure / wait / name tapes
6. z6 the STEP tape, the CTA tape
7. z7 captions (automatic)

z8–z11 are never used.

### 10.4 Finishing
- Vignette: in the grade only (0.50 on the footage window, and on plates through `ctx.grade(..., {spatial: true})`).
- Grain: only on W-desk (noise 0.035); none added over footage.
- Glow and bloom: the grade's bloom only (0.12, built in); no glow on type.
- Shadows: captions `0 1 6 rgba(0,0,0,.45)`; tapes `0 3 8 rgba(0,0,0,.35)`; cards `0 18 40 rgba(0,0,0,.45)`.
- Radii: tapes square (0); cards 18 px (screen) / 6 px (paper).

---

## §11 Sound

Quiet, like the picture: the voice, the bed, and the sound of the work itself. Hidden cuts must stay hidden, so they're
silent. (The reference's sound couldn't be measured; this is a decision, not a measurement.)
| Line | Direction |
|---|---|
| **Where sound goes** | A tape popping on (the STEP tape takes one soft cue for every step: the list cue, the one sound that repeats; a dry click such as `mouse-click-mouse-click` or a page turn such as `paper-turn-page`), an insert card landing (`paper-turn-page`), the CTA tape (`05405-shine-ding`). **The hook and every cut are silent.** If in doubt, leave it out |
| **Meme sounds** | None |
| **The bed** | On; it enters on the first word of the promise line (after the hook); a calm palette; ducked |
| **Ducking** | The bed sits 20 dB under the voice while the voice speaks. The overhead clips' own process sound (the pen scratch, the pour, the sizzle) stays when it's clean, ≥ 18 dB under the voice. F-B room tone stays, ducked under the speaker |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the last word |

No file more than twice in a reel, except the list cue.

---

## §12 Footage handling

### 12.1 Setups
| Setup | Spec |
|---|---|
| **A** Desk A-roll | Seated, chest-up, a 50–85 mm look at f/1.8–2.8 (the background soft), warm practical lamps 2700–3200 K, a lined background (shelves of books, tools, jars, plants), a dark top. Vertical 9:16, 4K preferred. Head top y 220–360 |
| **B** Overhead | Camera straight down (90°) over a **dark, deep-coloured or patterned surface**; vertical 9:16, 1080 × 1920 minimum (4K vertical for a 1.35× P-MACRO-PUNCH); soft side light; the hands enter from the bottom edge; the object inside y 200–1250 |
| **C** Desk insert | The desk camera lowered and close: the object held up or set at 30–45°, the background to black, a manual focus pull if possible |
| **D** Podcast | One camera per speaker (a tight single, eyes ≈ y 600 in the 9:16 crop, head top y 140–320), a mic entering from the side, warm practicals behind; or one 4K wide of both |

### 12.2 Shots and fallbacks
| ID | Shot | Spec | Must | Format |
|---|---|---|---|---|
| **SH-1** | Overhead hand demo | Setup B; each step filmed start to finish in 3–12 s clips, **twice** (a wide pass and a close pass), plus 3 s of each step's finished state; hands moving in and out of frame at both ends of each clip (the cut points) | must | F-A |
| **SH-2** | Finished result | 3–6 s: hands turning, opening, lifting or presenting the finished result; overhead or angled | must | F-A |
| **SH-3** | Desk take | Setup A, the whole script, one or a few takes | must | F-A |
| **SH-4** | Desk inserts | Setup C, 2–4 s each: the result at an angle, a detail held up, each step's piece held up (for the recap) | optional | F-A |
| **SH-5** | Podcast cameras | Setup D, synced (a clap or shared audio), one per speaker, or one 4K wide | must | F-B |
| **SH-6** | Listener reactions | 2–3 s nods, laughs, look-aways from the listener camera (part of SH-5) | optional | F-B |

| ID | For | What happens without it | Cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | (a) No overhead rig: film with the desk camera tilted down 45–60° and run it as the plate. (b) A horizontal 16:9 overhead: P-PLATE-BAND. (c) Only phone photos of each step: P-STEP-STILL | (a) the top-down look is lost; (b) not full-bleed; (c) no motion and no hidden cuts | degraded |
| **FB-2** | SH-2 | The last overhead clip's final 3 s (the finished state) opens the reel, from the frame where the hand leaves | No presenting motion at f0 | holds |
| **FB-3** | SH-3 | None: without a desk take the creator never appears, there are no returns between steps, and the reel becomes a voice-over hand demo | The face is gone | **no fallback** (F-A needs a desk take) |
| **FB-4** | SH-4 | P-MACRO-PUNCH into the overhead clip instead of a desk insert; the recap uses each step's overhead finished state | No depth, no rack focus | holds |
| **FB-5** | SH-5 | One camera: two virtual crops of a 4K wide (one per speaker); a 1080p wide: a blurfill band per speaker | Softer image (up to 2× upsampling), or no full-bleed face | degraded |
| **FB-6** | SH-6 | No reactions: P-TALK-RECROP at each would-be reaction point | The conversation feels one-sided | holds |

Note which fallbacks this reel uses (`fallback_used` per beat).

### 12.3 Props, the reaction bank, resolution
- **Props:** a dark, patterned or deep-coloured work surface; the finished result ready to show; warm lamps in the desk
  background; each step's tools laid out before filming.
- **Reaction bank:** F-B the listener's nod, laugh, look-away; F-A's close, the creator's small smile to camera.
- **No cut-out.**
- **Resolution:** a Z-2 re-crop (1.07) and P-MACRO-PUNCH (1.2–1.35) want ≥ 1296–1458 px of width; a 1080p vertical
  source allows up to 1.35× with visible softening (4K vertical preferred). F-B virtual crops need a 4K wide. Overhead
  clips must be **vertical** (assets are scaled to 1080 px wide and conformed to 30 fps).

### 12.4 Third-party inserts: fetch the real thing
When the creator names a real app, product, site, post, person or quote, the viewer should see the real one.
1. List the moments (an app, a product, a site, a post, a person, a quote).
2. The creator's own files in their folder come first: add each as their asset.
3. Otherwise search the web and fetch it: the real app or site page (captured and framed on the part that matters), the
   product photo, the post, a public photo of the person. Note where it came from. Show it in P-SCREEN-INSERT (`fx.shot`)
   or P-PHOTO-PRINT, unaltered; a post or quote word for word.
4. Nothing usable to be found: rebuild it from its exact words (no labels, no credit lines):

| Moment | Created substitute |
|---|---|
| An app or software screen | P-SCREEN-INSERT with `fx.appUI` (`recreated_ui`, generic) |
| A product or brand | P-PRODUCT-TAPE (`logo_plate`: the name in type on tape) |
| A post or quote read aloud | P-QUOTE-CARD (`quote_card`, word for word) |
| A news headline | `fx.headlineCard` on W-desk, paper theme (`headline_card`) |
| A person | `fx.silhouette` on W-desk (`silhouette`) |
| Another creator's video | Said, not shown: caption only |

### 12.5 Frame rate and audio
30 fps CFR, 1080 × 1920, BT.709. One voice track (F-A: the desk take; F-B: the synced mix), high-pass 80 Hz, de-ess,
light compression, −14 LUFS.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The format and the grade:** F-A or F-B; GR-tungsten or GR-tungsten-soft, with one before/after still.
2. **The hook:** the opening clip and its offset, the first gold word, the two hidden cuts and their frame pairs; the post
   title (8–10 candidates, the pick, two alternates).
3. **The step map:** for every step, the plate segments (asset, in, out), every hidden-cut frame pair with its T-id, the
   tape it carries, the state jump, the desk return or not. The count check: spoken steps = tapes = recap entries.
4. **The recap:** the turn-through clip, the frame of each ordinal, the E6 swap times.
5. **The gold words:** the one per chunk, chosen by §5.3.
6. **F-B:** the cast, the clip's in and out, every handover, every reaction, every re-crop.
7. **The inserts** (creator / fetched, with its source / created) and the fallbacks used.
8. **The sound:** the silent cuts, the list cue, the bed's entry.
9. **The moments you'll look at hardest on the storyboard:** f0, 1.0 s (the gold word, the result sharp), one STEP tape frame, one desk
   return (the head clear, the caption on the chest), one recap frame, the last frame. F-B: f0, the first handover, one
   reaction, the name tape frame (clear of the chin), the last frame.

**Beat fields this style adds:** `segments [{asset, from, offset, crop?}]` and `cuts [{at, kind: T-01/T-02/T-03,
out_frame, in_frame}]` on overhead runs; `shot_id`, `fallback_used`; F-B `speaker`, `angle`, `crop`, `cut_reason` (open /
handover / reaction / recrop); `exception: E6` (the recap tape only). The reel header carries
`format`, `hook_archetype` (HA-14 / HA-10 / HA-16), `structure`, `count`, `grade`, `cast` (F-B) and `fallbacks_used`;
`timeline.meta.hook_archetype` and `timeline.meta.format` carry the same values.

A beat from a step, for the shape:
```yaml
- id: 7
  section: STEP-2                # HOOK | PROMISE | STEP-n | RECAP | CLOSE | CTA  (F-B: CLAIM | TURN | REFRAME | BUTTON)
  t0: 21.40
  t1: 24.10
  spoken: "Then I add my two habit trackers"
  trigger: {word: "Then", at: 21.43}
  tone: explain
  layout: L-overhead
  pattern: P-OVERHEAD-PLATE      # + P-STEP-TAPE on the first beat of each step
  visual: "Overhead: hands rule the tracker grid on the blank page; STEP 2 tape pops on top centre"
  caption: {profile: CS-1, emphasis: ["trackers"], overrides: []}
  shot_id: SH-1
  fallback_used: null
  segments: [{asset: oh-2-1, from: 0.0, offset: 0.40}, {asset: oh-2-2, from: 1.57, offset: 0.53}]
  cuts: [{at: 22.97, kind: T-02, out_frame: "oh-2-1 @ 1.97", in_frame: "oh-2-2 @ 0.53"}]
  sfx: [{id: "mouse-click-mouse-click", t: 21.43, on: "tape-s2@0", why: "list cue: STEP 2"}]
```

Scene names: `plate-<section>` (one per overhead run, `kind: "broll"`, `segments`, `cuts`), `tape-<section>` (z6,
`in: "none"`, `events: [0.27]`, `text_class: "TC-label"`), `recap-plate`, `recap-tape` (`exception: "E6"`, `data-slot` on
the container), `tt-<n>` (tool / measure / wait tapes, z5), `ins-<n>` (inserts, z3). Declare every plate cut in `cuts`:
it's how the engine sees the cuts inside one plate scene.

---

## §14 Worked examples

Times are planning estimates: take the real ones from the words. They show the standard; match it, then beat it.

### 14.1 F-A, food: "My 4-step morning pour-over" (≈ 62 s)
Shots: the desk take (SH-3); overhead clips of grinding, rinsing the filter, the bloom and the spiral pour (SH-1, 9 clips);
the finished cup set down and lifted (SH-2); the cup at an angle and the spent filter held up (SH-4).

**Hook**
| t (s) | Spoken | Tone | Picture | Caption (gold) | Cut / camera |
|---|---|---|---|---|---|
| f0 | — | awe | P-RESULT-OPEN: overhead, the cup being set down on dark walnut, the coffee still swirling | — | — |
| 0.07 | "This is my morning ritual." | awe | the same plate, sharp by 0.9 s | "This is my morning **ritual**." | — |
| 1.43 | "Same beans, same water…" | awe | T-02 on the hand lifting away → the overhead pour close (the spout, the spiral) | "Same beans, same **water**," | T-02 |
| 2.70 | "…same cup every day." | awe | T-03 on the cup turning → P-ANGLED-HERO: the cup at 35°, steam, the background black | "same cup every **day**." | T-03; in-plate push 1.00 → 1.04 |
| 4.20 | "And it takes four minutes." | win | P-HELD-TO-CAMERA: the spent filter held up, P-RACK-IN | "it takes four **minutes**." | T-04 |
| 5.60 | "Here's exactly how I make it, in four steps." | explain | G-2 L-desk: the creator seated, the kettle in shot | "in four **steps**." | T-01; Z-1 |
| 8.10 | "First, grind your beans…" | explain | G-1 L-overhead + the STEP 1 tape | "First, **grind** your beans" | T-01 |

**Section plan**
| Section | t (s) | Patterns |
|---|---|---|
| STEP 1 Grind | 8.1–17.5 | P-OVERHEAD-PLATE (beans into the grinder → the grounds tapped out, 3 segments, T-02 ×2); gold "**grind**" on "First, grind your beans"; P-MEASURE-TAPE `18 G · 0.6 OZ` on "eighteen grams" at 10.9–13.4 (after the STEP tape exits at 10.6); P-STATE-JUMP to the grounds in the dripper; G-2 desk "medium-fine, like sea salt" (Z-1) |
| STEP 2 Rinse | 17.5–24.0 | STEP 2 tape; overhead: the filter in, the hot-water rinse, the water dumped (T-03 on the tilt); gold "**paper**" on "rinse the paper taste out"; no desk return (a short step) |
| STEP 3 Bloom | 24.0–36.0 | STEP 3 tape; the overhead pour of 40 g, the bed swelling; P-MACRO-PUNCH 1.25× on the bubbles ("see the gas escaping"); P-WAIT-TAPE `WAIT 30 SEC` on the P-STATE-JUMP; desk "fresh beans bloom more" (Z-2 on a jump cut); **the re-hook** at ≈ 35 s: P-RESULT-FLASH of the finished cup, 1.0 s, gold "**cup**" |
| STEP 4 Spiral pour | 36.0–49.0 | STEP 4 tape; the most satisfying visual: the slow spiral pour, 3 angles joined with T-02; P-MEASURE-TAPE `250 G · 8.8 OZ`; P-STATE-JUMP to the drained flat bed; desk "a flat bed means an even extraction" |
| RECAP | 49.0–56.4 | Desk "So: grind, rinse, bloom, pour." → one overhead shot moving across the set-out pieces: the grounds (STEP 1), the wet filter (STEP 2), the bloom (STEP 3), the cup (STEP 4), ≈ 1.6 s each; the tape counts on each spoken ordinal (E6); "your **grind**," "your **rinse**," "your **bloom**," "your **pour**." |
| CLOSE | 56.4–61.8 | P-ANGLED-HERO → P-END-ON-RESULT: the hand lifts the cup out of frame; "…and that's my morning." T-07 |

### 14.2 F-A, craft: "A leather card holder in 5 steps" (≈ 74 s)
Shots: the desk take; overhead of cutting, marking, punching, stitching and burnishing (SH-1, 12 clips, 4K vertical); the
finished holder with cards slid in (SH-2); each step's piece held up (SH-4, for the recap).

**Hook**
| t (s) | Spoken | Tone | Picture | Caption (gold) | Cut |
|---|---|---|---|---|---|
| f0 | — | awe | P-RESULT-OPEN: hands sliding two cards into the finished holder on dark slate | — | — |
| 0.05 | "This is the last wallet I'll ever buy…" | awe | same | "This is the last **wallet**" | — |
| 1.38 | "…because I made it." | win | T-02 → the overhead close of the saddle stitch along the edge | "because I **made** it." | T-02 |
| 2.75 | "One piece of leather." | explain | T-03 (the holder flipped) → P-HELD-TO-CAMERA: the flat cut piece, P-RACK-IN | "One piece of **leather**." | T-03 + T-04 |
| 4.30 | "No sewing machine." | explain | overhead: two needles crossing through one hole | "No sewing **machine**." | T-02 |
| 5.80 | "Five steps, one evening. Let's go." | explain | G-2 desk, the holder in hand (P-DESK-SHOW) | "Five **steps**," | T-01 |

**Section plan**
| Section | t (s) | Patterns |
|---|---|---|
| STEP 1 Cut | 8.0–20.0 | STEP 1; overhead: the template on the leather, the knife along the ruler (2 segments, T-02); P-TOOL-TAPE `ROTARY CUTTER`; P-STATE-JUMP to the cut piece; desk "always cut away from your fingers" (`warn`, gold "**away**", Z-2) |
| STEP 2 Mark | 20.0–28.0 | STEP 2; overhead: the wing divider tracing the stitch line; P-MEASURE-TAPE `3 MM · 1/8 IN`; P-MACRO-PUNCH 1.3× on the line |
| STEP 3 Punch | 28.0–38.5 | STEP 3; overhead: the pricking iron and mallet (T-02 on the mallet swing); gold "**holes**"; **the re-hook** at ≈ 35 s: P-RESULT-FLASH of the finished holder, 1.0 s |
| STEP 4 Stitch | 38.5–54.0 | STEP 4; the most satisfying visual: the saddle stitch pulled tight, 4 segments (two angles, a P-STATE-JUMP from 2 holes to the whole edge); P-TOOL-TAPE `WAXED THREAD`; desk "two needles, one thread" (Z-1) |
| STEP 5 Burnish | 54.0–61.5 | STEP 5; overhead: the edge sanded and burnished; P-HELD-TO-CAMERA of the glossy edge (T-04) |
| RECAP | 61.5–70.0 | One overhead shot, the hands turning the holder to each detail, ≈ 1.6 s each; the tape counts STEP 1–5 (E6); "your **cut**," "your **line**," "your **holes**," "your **stitch**," "your **edge**." |
| CLOSE | 70.0–74.0 | Desk: the cards slid in, the holder into a pocket; "…and it'll outlive me." T-07 |

### 14.3 F-B, podcast clip: "Most home bread fails in the oven" (≈ 46 s)
Two cameras (the host and a baker guest), synced; speakers named host and guest (Maya); singles only, no stack.

**Hook**
| t (s) | Speaker | Spoken | Picture | Caption (gold; colour) | Cut |
|---|---|---|---|---|---|
| f0 | guest | (mid-sentence) "…the thing that ruins most home bread isn't the flour," | P-COLD-OPEN: the guest single, mouth moving | "the thing that ruins" → "most home **bread**" (cream) | — |
| 2.10 | guest | "it's the oven." | same | "it's the **oven**." (cream) | — |
| 3.20 | host | "Really? Not the starter?" | P-SPEAKER-CUT → the host single | "Really? Not the **starter**?" (white) | T-05 |
| 4.60 | guest | "Your oven lies to you…" | P-SPEAKER-CUT → the guest | "Your oven **lies** to you" (cream) | T-05 |

**Section plan**
| Section | t (s) | Patterns |
|---|---|---|
| CLAIM | 0–4.6 | P-COLD-OPEN, P-SPEAKER-CUT; P-NAME-TAPE `MAYA · BAKER` 2.0 s from 0.4 s (the guest's first shot) |
| TURN | 4.6–18.0 | The guest's thermometer story: P-TALK-RECROP at 9.8 (a sentence boundary); P-REACTION-CUTAWAY, the host's nod 12.4–14.0; gold "**thermometer**", then "**fifty**" (degrees off) |
| REFRAME | 18.0–38.0 | Handover cuts every few seconds; host: "so what do you do?"; guest: "preheat an hour, steam for the first twenty minutes"; gold "**steam**"; a reaction 31.0–32.6 |
| BUTTON | 38.0–46.0 | Host: "I've been blaming my starter for two years." The guest laughs (P-BUTTON-END, the guest single 1.6 s); T-07 |

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0: the finished result, moving, in the hands (F-A) or a speaker mid-sentence (F-B); the result sharp by 1.0 s,
  its gold name by 1.5 s.
- The hook's cuts are invisible: two hidden in motion inside three seconds; no title, no emoji, no flash.
- Watched at full speed, the overhead cuts are invisible; motion keeps its direction across each one.
- One gold word per chunk, on the word a viewer would search for, never on a stop-word; it lands like an underline.
- The desk returns are breaths, one sentence long; the face comes back for the "why" and the close.
- The last step is the most satisfying moment; the recap is one calm turn-through with the tape counting.
- Nothing shouts: no visible zoom, no shake, no second bright hue; the flash only at a step's edge.
- F-B: the cut follows the floor; the listener's face on the punchlines; it ends on a reaction or a short reply.
- Start to end: it feels like a short film, and you could make the thing yourself.

**Craft (by eye, in context; the facts are in §2)**
- Desk frames: the face reads, no tape in the top band, the caption on the chest. F-B: the caption under the chin, the
  name tape beside the face. Nothing chops a head or buries a face by accident.
- At most the caption and one tape; never a tape on the caption band.
- Every step: the cut on the ordinal, the STEP tape on its first frame and off on the next cut, every spoken action seen.
  Tapes on their word; F-B cuts on the handover; never a cut inside a word.
- Steps = tapes = recap entries; tape numbers exactly as said; names spelt exactly; fetched posts and quotes word for
  word; a CTA keyword readable.
- Captions as profiled (CS-1 56 px cy 1440 / CS-2 76 px cy 1385 / CS-3 56 px), the block fit, over a dark background.
- One grade on every footage frame and plate; tapes and captions ungraded. Personal data blurred.
- The file itself (1080 × 1920, 30 fps, −14 LUFS, a hard end ≤ 6 f after the last word, no black tail) is the render's
  job; it checks it.

---

## §16 Build notes
- **Fonts:** Inter Tight, Instrument Serif (italic), Courier Prime, JetBrains Mono, Noto Sans Devanagari, all bundled.
  Pre-paint the currency glyph, °, · and × before first use.
- **Determinism:** every frame is a function of its index; video frames come from `ctx.videoFrame(name, seconds)` only; no
  CSS animation in scenes.
- **Plates grade themselves:** the engine grades the stage footage, never video assets, so every plate and still scene
  sets `ctx.grade(ctx.gradeId || "GR-tungsten", {spatial: true})` (P-GRADE-PASS). Forget it once and that step looks cold
  and clinical next to the desk.
- **Hand-cut frames are chosen by eye:** there's no motion detector for the cut point; read contact sheets of each clip at
  10 fps and pick the out- and in-frame around the peak blur.
- **Built in, no scene:** the flash (§8.3 F) and the grade on the stage footage (§4.3).

---

## Appendix A. Evidence map
The full map (every element → `vNN @ m:ss`) is in `evidence.md`. Sources: two of Peter McKinnon's reels (v01 a five-step
notebook system, 109.9 s; v02 a podcast clip, 47.4 s), their frame sheets, a full-resolution fidelity audit and a
full-frame-rate completeness pass (Oct 2026).

| What | Evidence |
|---|---|
| The gold italic serif word in a white grotesk caption, ≈ 1 every 4 s | v01 @0:01 "system", @0:03 "Track habits", @1:03 "sticky"; v02 @0:01.3 "printing", @0:04 "photographer" / "content" |
| The overhead hand demo on a patterned rug, ≈ 70 % of v01 | v01 @0:08–0:37, @0:47–0:49, @1:07–1:29 |
| The STEP tape pops on with the cut, off with the next; the recap turn-through | v01 7.73, 37.77, 46.80, 66.90, 84.93; recap 91.1–104.2 |
| Cuts hidden in hand motion; the white flash; speaker cuts on the handover | v01 @0:00.1, @0:01.5, @0:34, @1:12; flash 34.57, 37.57; v02 cuts 5.03–46.13 |
| Locked-off cameras: no synthetic zoom, rotation or shake | ORB on every frame of v01 and v02 |

Not verifiable from the reels: the speech language beyond English (read from burnt-in subtitles), the bed and the process
sound, the exact per-word fade length, the exact grade numbers (estimated from frames).

## Appendix B. Hook-title bank
Opening lines become the first captions (**bold** = the gold word); post titles promise. `[…]` slots are filled per reel.

**F-A Step demo**
| # | Opening line | Post title | Hook | For example (the title) |
|---|---|---|---|---|
| 1 | "This is my [result] **[noun]**." | "My [result] in [N] steps" | HA-14 | "My 4-step morning pour-over" |
| 2 | "This is the last **[object]** I'll ever buy, because I made it." | "Make your own [object]" | HA-14 | "Make your own card holder" |
| 3 | "[N] steps. One **[evening / morning / hour]**." | "[Result], start to finish" | HA-14 | "Pour-over, start to finish" |
| 4 | "Everyone gets the **[part]** wrong. Here's the fix." | "The [part] trick" | HA-10 | "The bloom trick" |
| 5 | "I've made this **[thing]** every [day / week] for [N] years." | "My everyday [thing]" | HA-14 | "My everyday loaf" |
| 6 | (no words for 1 s: the pour / the stitch / the fold) "That's the **[moment]** you want." | "Chasing the perfect [moment]" | HA-16 | "Chasing the perfect bloom" |
| 7 | "You don't need a **[expensive tool]** for this." | "[Result] without a [tool]" | HA-10 | "A wallet without a sewing machine" |
| 8 | "This is how I **[verb]** every single [object]." | "How I [verb] my [object]" | HA-14 | "How I sharpen my knives" |
| 9 | "[Result] in [N] minutes, no **[shortcut]**." | "[N]-minute [result]" | HA-14 | "10-minute cold brew" |
| 10 | "If your [thing] looks like this, you skipped the **[step]**." | "The step everyone skips" | HA-10 | "Flat bread? The step everyone skips" |

**F-B Podcast clip**
| # | Opening line (cut in mid-sentence) | Post title | Hook | For example (the title) |
|---|---|---|---|---|
| 1 | "…the thing that ruins most **[craft]** isn't the [obvious thing]," | "It's not the [obvious thing]" | HA-14 | "It's not the flour" |
| 2 | "…if, like, **[action]** is what separates a [pro] from a [hobbyist]." | "[Pro] vs [hobbyist]" | HA-14 | "Photographer vs hobbyist" |
| 3 | "…nobody talks about the **[hidden cost]**." | "The hidden cost of [topic]" | HA-14 | "The hidden cost of shooting RAW" |
| 4 | "…I stopped **[habit]** and everything got better." | "Why I stopped [habit]" | HA-14 | "Why I stopped posting daily" |
| 5 | "…if [platform] disappeared tomorrow, where's your **[work]**?" | "Where's your [work]?" | HA-14 | "Where are your photos?" |
| 6 | (a laugh in progress) "…no, seriously, **[claim]**." | "[Claim], seriously" | HA-16 | "Preheat for an hour, seriously" |
| 7 | "…the best **[tool]** is the one you [use daily]." | "The best [tool]" | HA-14 | "The best camera" |
| 8 | "…you don't need more **[gear]**, you need [practice]." | "Not more [gear]" | HA-14 | "Not more lenses" |
| 9 | "…I wasted [N] years on **[mistake]**." | "[N] years of [mistake]" | HA-14 | "Two years of the wrong starter" |
| 10 | "…that's the moment it became a **[craft]**, not a [hobby]." | "When it became a [craft]" | HA-14 | "When it became a craft" |
