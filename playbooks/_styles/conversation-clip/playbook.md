# Conversation Clip Style Playbook (template v2)

## The feel

This reel is a real conversation, and the edit's only job is to put you in the room. Frame 0 is two faces stacked one
over the other, the one who answers on top and the one who asked below, and across them a red pill already saying the
question in the asker's own words. You've read it before you've decided to stay. Now you need the answer.

Nothing else is added. No B-roll, no stickers, no zooms, no whooshes. The picture is only people, and all the power is in
where the cut puts your eyes: on the new voice the instant it starts, on the listener's face while the answer lands on
them, on both faces again when what's being said matters to both. The cuts are the editing. They move the way your own
eyes would if you sat at that table, which is why it feels honest, and why you keep watching a stranger's question for two
minutes.

The captions are the second picture. One line in the middle of the screen, a few words at a time, swapping hard on the
words. The one answering speaks in white; the other voice speaks in yellow italic, and the colour follows the voice, never
the face, so you always know who said it, even with the sound off. One word in a line goes bold: the number, the thing,
the verb that matters. When the answer itself arrives, it gets bigger. Once.

It breathes like talk. The setup moves slowly while the pill does the work. The back-and-forth of clarifying questions
cuts fast, almost line by line. A long answer settles onto the stack so you can watch it land on the person who asked.
The verdict slows right down: the line, one reaction, a thank-you, and it stops. Restraint is the signature. Every frame is
the room, and the only colour that isn't the room is the question.

**The test:** pause on any frame and you know who's talking, who's listening and what was asked, and nothing on screen is
anything but the room, their words or the question.

## What this playbook is

You're editing a real conversation, cut to a vertical clip in which the conversation itself is the content, and you have
the authority to make it the clip people send to the friend who has the same question. This playbook is the style, pulled
from three of Alex Hormozi's live audience Q&A clips (v01 "bigger bets", v02 "sell my company", v03 "employees leave")
and measured frame by frame at 30 fps. Read it all, every time; take what fits the clip, invent where a moment needs more,
and never break the feel above.

**Who it's for and what it needs.** Coaches, consultants, podcasters and experts who answer real people's questions on
camera. Two formats share one look: **F-A "Two-person Q&A"** (the default: two people on camera, an audience question at
a talk, a client call, a podcast or interview moment; 2+ cameras or one 4K wide, plus the room audio or a mic each) and
**F-B "Solo answer"** (the creator alone answering one question, a comment, a DM or a client's question, plus optionally
their screenshot of it or their own screen). F-A clips run long, about 90–150 s, because a real question needs its
answer; F-B runs 45–90 s. F-A lives or dies on the footage: the cameras define the look. There's no cut-out layer in
either format. Captions follow the creator's language (English verbatim by default; Hinglish romanised; Hindi in
Devanagari; §5.5). Machine values live in `tokens.json`; where this text gives a number tokens also holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **The question is the hook.** The viewer knows what's being asked within 1.0 s, from the pill alone, with the sound off | §5.2, §6.2 |
| D2 | **Captions are the second picture.** Every spoken word is captioned, centre-screen, one line, in the speaker's colour; after the faces they're the strongest thing on screen | §5.3 |
| D3 | **Two voices, two colours.** The viewer never has to work out who's talking | §5.3.1, §3.8 |
| D4 | **Follow the conversation.** Cut on the speaker change, show the listener, come back to the stack when both faces matter | §9.3, §7.3 |
| D5 | **Nothing that isn't in the room.** No B-roll, stickers, emoji graphics, logos, lower-thirds, zoom animations, transitions or SFX hits | §2, §8.1 |
| D6 | **It never sits still, and it never fidgets.** The captions move with the words, the picture moves with the conversation, and a shot lasts exactly as long as something is happening in it | §7.5, §9.4 |
| D7 | **Mine the moment, never rewrite it.** One self-contained question → answer arc; sentences never reordered; quotes word for word | §1, §5.3.2 |
| D8 | **Let the answer land.** The verdict gets a stack return or a punch caption, then the clip ends on the "thank you" within 6 f | §7.5, §6.7 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style (the turn map is the craft) |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Worlds, layouts and shot types (SHOT-STACK…), stage moves, diagrams, safe zones, the person, the dialogue cast |
| §4 | Colour system: the red pill, the white host, the yellow guest |
| §5 | Type and captions: the quote pill, CS-1 / CS-2 / CS-3, speaker styles, quotes, other text, language |
| §6 | Hook system: stopper test, HA-03 quote pill (F-A default), HA-03b, HA-14, HA-05 (F-B), hook pairs, pill writing, CTA |
| §7 | Structure and rhythm: the conversation units, the turn ritual, open loops and re-hooks RH-1…RH-5, rhythm by feel |
| §8 | Visual system (B-roll and patterns): families B-1…B-4, patterns P-01…P-31, line → pattern lookup, truth, comedy |
| §9 | Transition system: the hard cut, grammar, shot grammar R-SPK…R-SAME, how the moves breathe |
| §10 | Motion tokens, the footage camera (crop on cut), layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setups, shots and fallbacks, props, inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (2 × F-A, 1 × F-B) |
| §15 | Your look at the storyboard: the checklist |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics, and its
conversation notes run the shot tools. This style's craft is **the turn map**: who speaks when, who is worth watching
while they do, and which camera shows it. Decide these, in this order.

**F-A "Two-person Q&A"**
1. **Mine the clip.** From a long recording (`veos shots mine --min 90 --max 150` finds candidate spans), pick **one** arc:
   question → (clarifying exchange) → reframe → advice → verdict → thanks. It starts on the asker's first word (their
   name, their business, their situation) or on the host restating the question, and ends on the last "thank you" or
   verdict word, plus up to 6 f. Drop whole sentences that are off-topic or repeated, false starts and dead air. Never
   reorder sentences, never splice two half-sentences into one, never drop a sentence whose absence changes what someone
   meant.
2. **Name the cast.** The host answers (white); the guest asks (yellow). Label the two voices
   (`veos speakers --num 2 --names "S1=<host name>:host,S2=<asker name>:guest"`, `--mode mics` when each has a mic) and
   fix unlabelled words by hand until nearly every word carries a speaker (about 95 % or more).
3. **Map the angles.** Which camera or faux crop shows whom (`veos angles`): a host single, a guest single and, if
   filmed, a wide. One camera gives faux crops `<src>:S1`, `<src>:S2`, `<src>:W` (FB-1).
4. **Take the air out.** Tighten pauses to about 0.4 s. Keep a longer thinking pause (up to 1.2 s) only when it's a real
   moment and you can show the listener's face during it (P-23).
5. **Find the units and feel each line** (§7.1): **Q** setup, **C** clarifying exchange, **R** reframe, **A** advice,
   **V** verdict, **T** thanks. Each line's tone is `explain` (plain captions, the cut grammar only), `warn` (the hard
   truth: a host single or an angle switch in, bold on the cost word), `win` (the answer lands: a punch caption or a stack
   return so the asker's reaction is seen) or `cta`.
6. **Mark every line's bold word** (the number, the niche noun, the key verb), every voiced quote ("and then you're like
   '…'") and every back-channel ("yeah", "mmh", "okay").
7. **Write the pill** (§6.5): 8–10 candidates (the asker's question, the host's verdict, a tighter question), the best by
   the stopper test (§6.1), two alternates. Decide the opener's length and the word where the pill leaves.
8. **Plan the shots.** `veos shots plan --apply`, then shape `timeline.shots` by the shot grammar (§9.3): the stack
   opener, the handover cuts, the listener cutaways, the angle switches, the stack returns, the wides, the set-pieces.
   Mark the re-hooks (§7.4), then `veos shots render`. If a cut looks wrong on the storyboard and you can't see why,
   `veos shots check` measures the turn map (§3.8); it's a tool, never a gate.
9. **Write the caption overrides** (§5.3): the punch line (CS-2), the word (CS-3), voiced quotes, masked words, spellings.
10. **Sound** (§11): dry. The bed sits far under the voice; nothing marks a cut.
11. **Third-party moments** (§12.4): in F-A a product or a book is just a caption.

**F-B "Solo answer"** (replaces steps 1–3 and 8)
1. Take the creator's take, plus their screenshot of the question and any screen they point at: their files first, a
   real product or page they name fetched from the web (§12.4).
2. Find the words where the creator **reads the question aloud**: those words are captioned as the asker
   (`captions.overrides {i: [...], speaker: "guest"}`, yellow italic).
3. **Give a solo take a living rhythm.** It has no second camera, so the re-crop does that job: split the take at a word
   boundary wherever a new thought starts (an EDL boundary with no time removed is allowed), cut dead air to about 0.35 s,
   and give each boundary a jump re-crop (§10.2).
4. **Plan the stage:** `L-solo-stack` opener (face top, question card bottom) for 2.7–4.4 s, then `L-full-solo` with
   re-crops, and `L-solo-stack` again whenever the creator points at something: the board, their screen, the question
   again.
5. Everything else as F-A (steps 5–7, 9–11).

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Every face is the person.** Both speakers in a stack, the listener in a cutaway, the asker standing in the crowd:
  the faces are the picture in this style, so keep the face, the hair and the room above the head clear of the pill, the
  captions and any insert. The framing that does it: the pill's top ≈ 40 px under the chin of any face in its cell; a
  caption moved off a head rather than across it. A caption grazing a chin for a beat on a low single can be fine; what's
  never fine is a face buried or a head chopped by accident. The exact geometry is in §3.7.
- **No text over text.** The pill band (y 672–880) and the caption band (≈ y 921–999) never meet; one pill at a time; the
  F-B insert starts at y 1030, under the seam caption.
- **On the word.** Cuts and captions land 1 f before the word onset. A new speaker's first word has a cut within ±3 f when
  either side of it is a full shot. Never a cut inside a word. A picture cut lands on a caption-chunk boundary: the new
  chunk appears on the cut frame (v01 @ 4.367, 54.067).
- **Say what was said.** Captions are the words as spoken (fillers kept, glossary spellings fixed, profanity masked).
  Sentences are never reordered or spliced. A quoted pill is a verbatim contiguous span; a voiced quote is word for word.
  Numbers appear exactly as spoken, as digits in the style's format. The created question card shows the question as
  asked.
- **The colour follows the voice.** A chunk never mixes speakers; two speakers never share a caption style.
- **Spelling.** Names and brands exact in captions and on the pill.
- **Readable.** Captions 68 px (never under 54), at least 0.25 s per word, one line of up to 24 characters; the pill reads
  in 1.2 s. Captions never sit in the top 110 px, below y 1500, or right of x 970 between y 900 and 1540 (Instagram's
  buttons).
- **Privacy.** On a real comment screenshot, blur the commenter's avatar and handle unless the creator confirms they may
  be shown; never caption an email address or a phone number.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed at least 18 dB under the voice (this style sits it at
  −26 dB), a hard end ≤ 6 f after the last word, no black tail.
- **Determinism.** Every scene is a pure function of the frame.

**Never in this style:**
- B-roll, stock footage, GIFs, memes, emoji graphics, stickers, logo bugs, lower-thirds, name plates or progress bars. An
  emoji appears only inside a caption, as the speaker's own tone on a one-word reaction ("perfect ✨", v03 @ 0:02.7): it
  happened once in 410 s of reference, and it should feel that rare.
- Transitions of any kind: no whip, flash, zoom-blur, slide or fade between shots. Hard cuts only.
- Animated zooms, punch-ins, shakes, rotation snaps or Ken Burns on footage. The only "zoom" is a crop change on a cut.
- Caption animation: no pop, bounce, karaoke, typewriter, word-by-word colour fill, scale or blur. Chunks hard-swap.
- A caption colour other than the speaker's. Emphasis is weight (800), never a third colour, never a box behind a word.
- A pill after 12 s except the CTA pill; two pills at once; a pill with an emoji, a logo or any colour but the pill red.
- Caption text that wasn't said.
- Sound effects on cuts, captions or the pill; meme sounds; music louder than −26 dB under the voice.
- A grade, LUT, vignette, grain, glow or blur added to the footage (a vignette baked into the source stays).
- A hairline, gap, border or drop shadow on the stack seam.
- A stack with the same person twice, or a framing cut to itself (use another angle or the ×1.25 re-crop).
- An F-B insert that decorates: the bottom cell shows only what the creator is talking about right then.
- A fake comment, a fake DM or an invented username. The question is real, so the created card names no handle: "A
  follower asked", or the name the creator gives.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-room** | footage | The room as filmed: stage LED wall, floor mic, audience, studio. Not regraded | Everything in F-A; the full frame and the top cell in F-B | Always under the footage |
| **W-void** | void | `#0E0E10`, noise 0.03 | F-B bottom cell behind the question card or a screen recording | Hard cut with the stage change |
| **W-board** | paper | `#F4F4F1` flip-chart white, noise 0.02, drawn as a **card** (radius 28) filling the insert rect x 80–960, y 1030–1500; the cell ground stays `W-void`, so the seam caption always sits on dark | The board (P-28) | Rises 10 f with the board |

### 3.2 Layouts and shot types
F-A reels keep the **stage at `L-full-dialogue`** (engine `full`) for the whole reel: the engine composes the shots
(`timeline.shots`) into the footage itself. The shot types below are written as `timeline.shots` entries.

| ID | Engine / shot fields | What | Rects |
|---|---|---|---|
| **SHOT-STACK** | `{"layout": "stack", "seam_y": 960, "top": "source:<host angle>", "bottom": "source:<guest angle>", "top_subject": host, "bottom_subject": guest, "hairline": 0}` | Host top, asker bottom, no gap, no line. The home of the conversation: the opener, and every return when both faces matter | top 0–960, bottom 960–1920; the renderer frames each cell with the face ≈ 27 % of the cell height, face centre at 36 % of the cell (y ≈ 346 top, ≈ 1306 bottom) |
| **SHOT-HOST** | `{"layout": "full", "angle": "<host single>", "subject": host, "step": 1.0}` | Host single, medium to medium close-up | full frame; face ≈ 17 % of the frame height |
| **SHOT-GUEST** | `{"layout": "full", "angle": "<guest single>", "subject": guest, "step": 1.0}` | Asker single at the mic or across the table | as above |
| **SHOT-ALT** | `{"layout": "full", "angle": "<second angle of the same person>", "cut_reason": "recrop"}` | The same speaker from another camera: front medium ↔ side (podium) medium-wide ↔ full-body wide from the crowd (v01 @ 0:51.3, v02 @ 0:16.2, 1:09.3) | full frame |
| **SHOT-RECROP** | same angle, `"step": 1.25`, `"cut_reason": "recrop"` | The fallback for SHOT-ALT when the person has one camera: ×1.25 tighter (or back to 1.0) | as above, ×1.25 |
| **SHOT-WIDE** | `{"layout": "full", "angle": "<src>:W" or the room camera, "cut_reason": "establish"}` | Room or crowd from behind the audience: the host small on stage, **or the asker standing in the crowd while she speaks** (v01 @ 0:36.8–0:46.4, yellow captions) | full frame (blurfill when a 16:9 wide can't fill 9:16); 1–4 s, two wides back to back up to 6 s |
| **L-full-dialogue** | stage, engine `full` | The stage layout of every F-A reel | full frame; captions cy 960 |
| **L-full-solo** | stage, engine `full` | F-B: the creator full frame, jump re-crops on cuts | full frame; captions cy 960 |
| **L-solo-stack** | stage, engine `stack`, `top: {src: footage, face: 0.30, eye: 0.42}`, `bottom: graphic`, hairline 0, fade 0 | F-B: face top, insert bottom | top 0–960; graphic band x 80–960, y 1030–1500; caption on the seam |

### 3.3 How the shots follow the conversation
The picture changes on a new speaker's first word (always), on a sentence end inside a long turn, or on the bold word of
an emphatic run. A single holds while something is happening in it: a short answer for a beat, a gesturing host through a
whole thought (a long one runs 6–10 s, as at v01 @ 1:15–1:26), never long enough to sit. A mid-reel stack is held as
**one** shot with no internal re-crop, because its job is to let you watch the answer land on the asker; for reference,
the measured stacks ran 12.1 / 23.7 s (v01), 14.4 / 13.2 / 16.5 s (v02) and 12.5 / 9.7 s (v03). The stack is the
conversation's home: it opens the reel, and it comes back whenever both faces matter (for reference it filled about a
third of each reference clip: 36 / 32 / ≈ 25 %).

**F-B.** `L-solo-stack` holds while the bottom cell is the subject; `L-full-solo` carries the talking between. Switch on a
sentence end, or on the word that names the thing in the bottom cell ("this", "look", the item's name).

### 3.4 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-1** | Hard cut | 0 f. A shot or stage change lands on the frame of the word onset − 1 f (`lead_f` 1) | Every boundary in this style |
| **G-2** | Angle switch / jump re-crop | F-A: a hard cut to another camera on the same speaker (SHOT-ALT); with one camera, the same angle at step 1.0 ↔ 1.25 (the shot's `step`). F-B: the camera preset `recrop-in` / `recrop-out` written 1 f before the cut | Long turns; the F-B rhythm |
| **G-3** | Pill carry | The pill scene runs unchanged (same rect, same text) across any cuts inside the question sentence and is removed in 0 f where the sentence ends, cut or no cut | The hook (P-03) |
| **G-4** | Stack return | A hard cut from a full shot into SHOT-STACK (F-A) or `L-solo-stack` (`via: "cut"`, F-B) | Long turns, the reframe, the verdict, a set-piece |

No slide-down, morph, pip, panel drop, shrink-to-card or fade: write `"via": "cut"` on every F-B stage entry (the engine's
default into `stack` is `slide-down`).

### 3.5 Layout diagrams
**SHOT-STACK with the pill (the F-A opener):**
```
┌──────────────────────────┐ 0
│  (IG top UI, keep clear) │ ← y 0–110
│        HOST (top)        │ ← host head; face centre y ≈ 346, chin ≈ y 476
│      listening or        │
│        answering         │
│ ╭──────────────────────╮ │ ← pill line 1, top y 672 (≈ 196 px under the host's chin)
│ │ “SHOULD I SELL MY     │ │   x 120–960 (centred, per-line boxes)
│ ╰─╮ COMPANY?”        ╭─╯ │ ← pill line 2, bottom ≤ y 880
│   ╰──────────────────╯   │
│    I sell  (yellow ital) │ ← caption centred ON the seam, glyphs ≈ y 921–999
├──────────────────────────┤ 960 seam: no line, no gap
│                          │ ← the asker's head region starts ≈ y 1085 (clear of the caption)
│       ASKER (bottom)     │ ← asker face centre y ≈ 1306
│        at the mic        │
│                          │ ← y 1540–1920 IG UI (faces may sit here, text may not)
└──────────────────────────┘ 1920
```

**SHOT-HOST / SHOT-GUEST (full):**
```
┌──────────────────────────┐ 0
│                          │
│       HEAD + FACE        │ ← the head region: keep it clear
│                          │
│     (pill y 672–880      │ ← only while the pill is carried, and only under a chin at y ≤ 632
│      if carried)         │
│    you're playing too    │ ← caption cy 960, one line, max_w 860 (x 110–970)
│        **small**         │   (shown here on two lines only to fit the diagram)
│          chest           │
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

### 3.6 Safe zones and bands
- **Meaning-text box:** x 64–1016, y 110–1500. The right 110 px between y 900 and 1540 stays empty of text, so captions
  use `max_w` 860 (x 110–970).
- **Pill band:** top y 672, bottom ≤ 880, x 120–960 (max width 840).
- **Caption band:** cy 960 in full shots and on the seam (y 960) in every stack, glyphs ≈ y 921–999 (measured centres
  955–989 at v01 @ 0:20, @ 0:50, v02 @ 0:10, @ 1:20, v03 @ 0:20). The pill's bottom (≤ 880) sits ≥ 40 px above it.
- **F-B insert band:** x 80–960, y 1030–1500 (≥ 30 px under the seam caption's glyphs, inside the meaning box).
- **CTA pill band:** the same as the hook pill (y 672–880).

### 3.7 The person
In this style "the person" is every face in the frame: the host, the asker, both of them at once in a stack, the asker
standing in the crowd in a wide. Keep the face, hair and the room above the head clear on all of them, of the pill, the
captions and any insert, unless the moment wants otherwise; judge it on the frame. There's no cut-out in this style,
so the head region is read from the face track: brow to chin, plus the hair and the room above it.
- **The stack.** The renderer frames each cell with the face ≈ 27 % of the cell height and the face centre at 36 % of the
  cell. The **top speaker**'s head reaches up to about y 125 and the chin sits near y 476: the pill (from y 672) is about
  196 px under that chin and the seam caption sits on their chest. The **bottom speaker**'s head region starts around
  y 1085 (face box from ≈ y 1176, hair and headroom above it), about 85 px under the seam caption's glyphs (≈ y 999). A
  tall hairdo, a hat or an asker framed high closes that gap: look at the bottom head on every stack, and if the
  hair reaches the caption band, reframe the bottom cell lower rather than move the caption off the seam.
- **A carried pill on a single.** The pill's band is fixed (y 672–880), so it rides into a single only when that face's
  chin is at y 632 or higher (40 px of clearance, `layout.face_clearance`). When the single frames the face lower, the
  pill's top moves to chin + 40; if that pushes its bottom past 880, the pill leaves on that cut instead (its `t_out` is the
  cut). Look at every cut the pill crosses on the storyboard.
- **Captions on a single.** cy 960 sits on the chest of a medium shot. The caption engine moves any caption that would
  touch a head region off it (`avoid_face`): below the chin when it sits at or below the face centre, otherwise above the
  head. Look at the result: it should read as moved off the head, not across it.
- **A wide.** The speakers are small, but they're still the person: keep the caption off the host's and the asker's
  heads. If one of them sits at the caption's height, choose a wide where they sit clear. The crowd's backs of heads are
  the room.
- **F-B.** `L-solo-stack` puts the creator's face at 0.30 of the top cell with the eye line at 0.42 (y ≈ 403); the chin
  sits well above the pill, and the seam caption and the insert are below them. On `L-full-solo` the creator is a single
  (above).
- **Behind the person** is fair game in principle, text included; with no cut-out, this style simply has nothing there.
- **Crops follow the subject** with a dead zone (the renderer's virtual operator), never a visible drift faster than
  60 px/s. A return to a face is always a hard cut on a word onset.

A face is never more than a beat away: a wide is a glance at the room (the longest measured wide ran 4 s), and in F-B the
creator is always on screen, full or in the top cell.

### 3.8 Dialogue: the cast, the angle map and the cut rules (F-A)
| Who | Role | Caption style (§5.3.1) | Preferred angles |
|---|---|---|---|
| host | the creator, the one answering | `host`: white upright | host single (SH-1) → faux crop `<src>:S1` |
| guest | the asker or interviewee | `guest`: yellow italic | asker single (SH-2) → faux crop `<src>:S2` |
| a third voice (a co-host, an audience shout) | — | `guest` style when it asks, `quote` style when the host voices it | the wide (SH-3) |

A third on-camera speaker isn't part of this style: mine a span where two people talk.

- **The angle map.** From `veos angles`: every real camera is an angle id (its source id); a camera showing 2+ people
  yields faux angles `<src>:<speaker>`, `<src>:2S`, `<src>:W`. Reframing: single = face 17 % of the full frame, 27 % of a
  stack cell, face centre at 36 % of the crop, dead-zone subject follow, at most 2.0× upsampling; shots that can't crop to
  9:16 use `blurfill` (`dialogue.fallback`; `letterbox` is the other choice).
- **Host on top, always.** Every stack in the references has the host on top, even while the asker speaks (v01 @ 0:00 and
  0:54, v02 @ 0:00 and 0:54, v03 @ 0:00 and 1:10). Tokens hold `dialogue.stack.top: "host"`; `veos shots plan` and the
  speaker check honour it.
- **Two faces on frame 0.** The hook check reads the stage (always `full` in F-A), not `timeline.shots`, so give the pill
  scene `satisfies: ["two_faces"]` when the first shot is a stack.
- **The cut rules** (`dialogue.cut_rules`, what `veos shots plan` builds and `veos shots check` measures): `handover_tol_f`
  3, `lead_f` 1, `open_s` [2.7, 4.4], `max_hold_s` 10, `stack_max_s` 20, `reaction_s` [1.0, 3.0], `recrop_step` 1.25,
  `stack_share` 0.35, `min_shot_s` 0.8, `backchannel_max_s` 1.6. The grammar they encode is §9.3.
- **The speaker check** (`veos shots check`, a tool for when a cut looks off, never a gate) measures: at least 95 % of
  words labelled; one distinct caption style per speaker; a cut within ±3 f of every handover on full shots; the speaker
  on screen (reaction cutaways up to 3.5 s and never across a handover; in a stack, the host on top); no cut inside a
  word; no full shot past 11 s, no stack past 21 s (the holds + 1 s).
- **Overlapping speech** shows only the dominant speaker (the engine labels each word with the dominant talker), and the
  cut follows the dominant speaker.
- **One camera.** One wide → FB-1 (two crops); one person only → F-B.

---

## §4 Colour system

### 4.1 Role palette
| Role | Hex | One job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` | `#E80001` | The pill fill (hook pill, CTA pill). Nothing else | `paper` | 4.87:1 (the pill's text is 68 px display, which needs 3:1) |
| `accent` | `#F2DF1A` | The second voice: the asker's captions; the asker's question on the F-B card (sampled `#F0DE18`, v01 @ 0:01–0:20, v02 @ 0:10) | `ink` (15.5:1) | on footage through the caption's shadow halo |
| `paper` | `#FFFFFF` | Host captions, pill text | `ink` | — |
| `ink` | `#0B0B0B` | Caption shadows, board marker | `paper` | — |
| `board` | `#F4F4F1` | F-B board paper | `ink` (17.9:1) | — |
| `void` | `#0E0E10` | F-B bottom-cell ground | `paper` (19.6:1) | — |

The pill red can take the creator's brand colour. The guest colour can too, as long as it stays a light, saturated hue
readable on footage with the shadow (never white or near-white: two voices need two looks).

### 4.2 Meanings
- **Red = "this is the question (or the verdict)".** It exists only in the pill. Never a red caption, a red underline or a
  red card.
- **White = the host. Yellow italic = the other voice.** This axis replaces every bad/good axis: the style has no bad or
  good colours.
- The footage carries every other colour (LED walls, shirts, rooms). Brand colours appear only if they're in the room.

### 4.3 Grades
None: the footage is used as filmed. Match exposure and white balance between cameras when the footage is readied; never
add a grade, LUT, vignette or bloom (vignettes baked into a source stay, as at v01 @ 0:54).

### 4.4 Rules
- Never more than two bright hues in a frame (`max_bright_per_frame` 2): the pill red and the guest yellow, and both
  together only during the hook.
- A caption chunk carries exactly one colour: its speaker's.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weight | Used for |
|---|---|---|---|
| `display` | **Montserrat** | 800, caps | The pill, the CTA pill |
| `body` | **Montserrat** (+ the Montserrat Italic file) | 500 / 800 bold / 500 italic | Every caption |
| `marker` | **Permanent Marker** | 400 | F-B board words only |
| `ui` | **Montserrat** | 500–700 | F-B question card |

Devanagari captions use **Noto Sans Devanagari** (no italic exists: §5.5).

### 5.2 Headline element: the quote pill
| Property | Recipe |
|---|---|
| Kind / lifetime | `pill`, lifetime `hook` (scene `kind: "pill"`) |
| Shape | **One red box per line** (`box_per_line`), centred, the lines touching so the two boxes read as one stepped shape; radius 16; padding 8 px top/bottom, 22 px left/right; fill `primary`; no stroke; shadow `0 4 10 rgba(0,0,0,.25)`; rotation 0 |
| Text | Montserrat 800, **68 px**, ALL CAPS, tracking 0, line height 1.0 (line box 84 px), `paper` white, centred (measured cap height 48 px = Montserrat 800 at 68 px) |
| Size | 2 lines (1 line only for 3 words or fewer); up to 6 words; up to 18 characters a line; width ≤ 840 px; total height ≈ 168 px; reads in 1.2 s |
| Position | Centred at x 540; top y 672 (measured y 656–914 across v01–v03); bottom ≤ 880; ≥ 40 px clear of the caption below and of any chin above (§3.7) |
| Quotes | Curly quotes `“ ”` when the pill is the asker's question in their own words (v02, v03). No quotes when it's the host's verdict (v01) or a title in your words (§6.5) |
| f0 | **Fully drawn on frame 0.** `in: "none"`; no scale, no fade, no shadow grow (v01 f0–f3 identical) |
| Life | None. No pulse, flip, colour change or wobble. It just sits there while the footage moves |
| Exit | **Hard, 0 f**: `t_out` = the end of the question sentence's last word (snapped to a shot cut if one falls within 3 f, else mid-shot), `out: "none"`, `cuts: [t_out - t_in]` declared. Held at least 2.7 s, never past 12 s. Measured: v01 out at f115 = 3.83 s mid-shot, v02 f142 = 4.73 s mid-shot (after the 4.0 s cut), v03 f346 = 11.53 s, 2 f before a cut |
| Scene | `z: 10`, `roles: ["primary"]`, `box` = the pill rect, `may_overlap_face: false`, `text_content` = the pill text exactly; an F-A opener on a shots stack adds `satisfies: ["two_faces"]` (§3.8) |

### 5.3 Caption system profiles
Captions hard-swap inside a fixed band (`exceptions.E6`: the band holds within ±4 px); only the band's first entry (a 4 f
fade, and only if no word is on f0) and final exit (6 f out at the end) are eased, and the swap is never used for a new
element appearing. A fade would smear one-word groups at about a chunk a second; on the words, they change with no tween.

**CS-1 "Conversation"** (default; `extends: lib:hormozi`):
| Group | Recipe |
|---|---|
| Mode | `full`, role `primary`, mute-safe: every spoken word, fillers included |
| Chunking | `group`, 1–4 words (mean ≈ 2.4), up to 24 characters, 1 line; never split a name, a number or a unit ("$44M", "4-year retention"); break on punctuation, on a pause of 0.9 s or more and on a speaker change; end punctuation stripped except `?` and `!` (v01 "$44M?", v02 "is that appealing", "to you?") |
| Timing | Lead 1 f; at least 0.25 s per word; tail 0.12 s; a chunk holds through a pause of up to 0.6 s (`pause_hold_s`), then hides; swap **hard, 0 f** |
| Skin | Montserrat **500, 68 px**, tracking −1 % (measured: "okay so you're doing" 66 px tall ascender to descender, 681 px wide, v01 @ 0:50; "medium-skilled labor" 57 px ascender height, v03 @ 0:20), case as spoken (lowercase except "I", names and acronyms: "I sell", "salon in LA"), no stroke, no container; shadow `0 2 3 rgba(0,0,0,.85), 0 0 12 rgba(0,0,0,.35)`; `TC-subtitle` |
| Position | `fixed_y` cy **960**, cx 540, `max_w` 860, centred, `avoid_face: true`; anchored on the seam (y 960) in every stack shot and in `L-solo-stack` (`by_layout`) |
| Speakers | **host** `paper` upright · **guest** `accent` italic · **quote** `paper` italic (§5.3.1) |
| Emphasis | `bold` (800), one word per chunk at most (a 2-word span counts when it's one idea), the profile caps it at 0.6 a second; chosen from numbers, names, glossary terms, the topic noun and the key verb, never a stop-word (v01 @ 0:21 "to the **greatest**", 0:57 "you're playing too **small**", v03 @ 2:14 "all the **best talent**"; for reference, about 40 % of the reference chunks carry one) |
| Variants | none (no karaoke, tiers, duet or kinetic stack) |
| Hide | never hidden while someone speaks (the pill sits above the caption, not on it) |
| Language | Latin script; English terms as spoken; spelling not normalised ("gonna", "wanna", "cus'"); profanity masked inside the word (`f**k`; the reference used a vowel mask, v02 @ 1:41); glossary = the creator's names and terms |

**CS-2 "Punch line"** (`captions.overrides {t: [a, b], profile: "CS-2"}`): the same look at **84 px, weight 800**, 1–3
words, up to 16 characters, at least 0.3 s per word, shadow `0 3 4 rgba(0,0,0,.85), 0 0 16 rgba(0,0,0,.4)`. It's for the
line that *is* the answer ("you're gonna / **work again**", v02 @ 0:26–0:27), so it's rare by nature: an answer has only a
few lines like that. Never two back to back, never in the hook.

**CS-3 "The word"** (`{t: [a, b], profile: "CS-3"}`): one word, **120 px, weight 800**, `TC-display`, up to 10
characters, at least 0.5 s, shadow `0 4 6 rgba(0,0,0,.85), 0 0 20 rgba(0,0,0,.4)`. Only when the host names the single
concept the whole answer turns on, usually while writing it ("**role**", v03 @ 1:06). An answer turns on one thing.

#### 5.3.1 Speaker styles
| Speaker key | Colour | Style | Who |
|---|---|---|---|
| `host` | `paper` #FFFFFF | upright | The creator (the one answering) |
| `guest` | `accent` #F2DF1A | italic (500; bold words 800 italic) | The asker in F-A; the question when read aloud in F-B |
| `quote` | `paper` #FFFFFF | italic | The host voicing himself or a third person ("“learn all this shit”", v01 @ 1:31; "“great!”", v01 @ 1:23) |

The colour follows who is **speaking**, not who is on screen: the asker's "thank you!" stays yellow on the host's shot
(v02 @ 2:30), and the host's words stay white on the asker's wide (v02 @ 2:00–2:05).

#### 5.3.2 Quotes and voiced lines
- **The host voices the asker** ("and then you're like 'I can't do this forever'"): the quoted words take the **guest**
  style, in curly quotes: `{i: [first..last], speaker: "guest"}` + `{i: first, text: "“I"}` + `{i: last, text: "forever”"}`
  (v02 @ 0:33–0:35 "“I can't do this” / “forever” / “be an alcoholic”" in yellow italic).
- **The host voices himself, a client or "people"**: the **quote** style (white italic) in curly quotes (v01 @ 1:23–1:25
  "“great!” / “total capacity?” / “can you get me?”").
- **The asker voices someone**: stays guest (yellow italic) with curly quotes (v01 @ 0:44 "“oh that's **terrible**”").
- A quoted span is its own chunk (chunks never mix speakers), and its words are verbatim.

#### 5.3.3 Other caption conventions
- **Cut-off words** end with a hyphen and the chunk holds through the restart: "where you're-" (v01 @ 1:44–1:45), "I think
  that if we-" (v02 @ 2:19).
- **Back-channels** ("yeah", "mmh", "okay", "nope", "uhm..") are captioned in the listener's style, as their own chunk,
  while their reaction shot is up (v02 @ 0:23 "yeah yeah", 2:28 "mmh", 2:29 "okay").
- **A trailing thought** "like.." / "so.." uses two dots (v02 @ 1:24 "like..", v03 @ 0:14 "so..").
- **Emoji:** only as the speaker's tone on a one-word reaction ("perfect ✨", v03 @ 0:02.7). Never in the pill.
- **Action captions** ("*alex approves*", "*boop*"): only with light comedy on (§8.6).

### 5.4 Other text
| Element | Recipe | Hold |
|---|---|---|
| **CTA pill** (P-04) | The pill recipe (Montserrat 800 68 px caps, `primary` per-line boxes, radius 16, padding 8/22), 1–2 lines: `COMMENT “KEYWORD”` or `LINK IN BIO`; fades in over 6 f on the spoken word (not on a cut), leaves on the last frame | 1.5–3.0 s |
| **F-B question card** (P-25) | **Created:** a quote card (`fx.quoteCard`) restyled: a rounded card, radius 28, fill `#1A1A1D`, in the insert rect x 80–960, y 1030–1500; a name line in Montserrat 700 40 px `paper` ("A follower asked", or the name the creator gives); the question in Montserrat 600 italic, 48–56 px (52 by default), in `accent`, up to 3 lines, word for word. **The creator's screenshot:** `fx.shot` with `chrome: false`, fitted to the insert rect, identifiers blurred | the stack run |
| **F-B board** (P-28) | A `board` card (radius 28) in the insert rect on the `W-void` cell; Permanent Marker in `ink`, title 96–120 px (writes on in 12 f), items 64–96 px (10 f each), left-aligned at x 120; each word writes on left to right on its spoken word; a 6 px marker tick or underline draws in 6 f on the item being discussed | the stack run |

### 5.5 Language and numbers
- **Speech → captions** (one combination per reel, set in the creator's copy):
  - `en → en` (default): verbatim.
  - `hinglish → hinglish (Latn)`: verbatim romanised Hinglish; English words in standard spelling; Hindi words phonetic
    and consistent within a reel ("kya", "nahi", "matlab").
  - `hinglish → en`: translated per chunk, still 1–4 words, still split by speaker; quotes translated faithfully and still
    in curly quotes.
  - `hi → hi (Deva)`: Noto Sans Devanagari 600, 68 px. **Devanagari has no italic**, so the guest style becomes **yellow,
    weight 700, upright**; two voices still look different by colour. ALL CAPS doesn't exist in Devanagari: the pill stays
    in English or Latin Hinglish caps unless the creator asks for a Devanagari pill (then 64 px, weight 800, the quotes rule
    unchanged).
- **Numbers:** digits, never words ("5 locations", "30 days", "$70K a year", "20% to 25%", "6 to 12"); the currency glyph
  pre-painted; international grouping, k/M/B compact ("$4M to $44M"). An Indian creator's copy uses `₹` and lakh/crore
  ("₹40 lakh", "₹1.2 Cr").
- **Spelling:** names and brands exact (the glossary); everything else as spoken.
- **Fillers:** "uhm..", "like", "you know" stay when they're spoken on a kept span; whole filler-only stretches longer than
  0.4 s are cut.

---

## §6 Hook system

**The pill is this reel's hook title, and here the best title is the question itself.** A question a real person asked
out loud is a promise the viewer feels in their stomach: they have the same question, and someone is about to answer it.
So the pill quotes the asker word for word when their own words make that promise in six or fewer. When they don't, write
the pill as a title in your own words, without quotes, that promises the answer the clip really delivers (an outcome, a
curiosity gap, who it's for); it needn't repeat the spoken words, but it must be true to them. A verdict that surprises is
a promise too (HA-03b). Write 8–10 candidates from the formulas in §6.5 and the proven shapes ("Should I X?", "Why do my
X…?", "How do I X as a Y?", "X or Y?", a number or a contrast), score them on outcome, curiosity, who it's for and
brevity, check the best against the stopper test, and keep the next two as alternates.

### 6.1 The stopper test
| Test | In this style |
|---|---|
| Thumbnail | Frame 0 at 25 % scale shows "two people, one question": the pill text is 17 px at that scale and still legible; both faces visible (F-A) / face + card (F-B) |
| Mute | The pill plus the first caption chunks tell what's being asked without sound |
| Motion at f0 | Live footage is moving on f0 (people never freeze) |
| Read time | The pill reads in 1.2 s (6 words or fewer) |
| Payoff | The question is understood by 1.0 s (the pill); the answer starts by 60 s |

### 6.2 HA-03 Quote pill over the conversation (default, F-A)
The hook is **"who is asking what"**. There's no spoken hook line: the asker starts setting up their question, the pill
already says what it is, and the viewer stays to hear the answer.

| t (s) | Layout / shot | Pill | Captions | Cut | Sound |
|---|---|---|---|---|---|
| **f0** | SHOT-STACK: host top (listening, ¾ toward the asker), asker bottom at the mic | **Fully drawn**, y 672–840, e.g. `“SHOULD I SELL MY / COMPANY?”` | The asker's first chunk on the seam in yellow italic, if a word starts by 0.03 s ("I sell") | — | dry |
| 0.0–1.0 | same | same | The asker's chunks 1–2, about one chunk per 0.7–1.2 s ("I sell" → "performance upgrades") | none | dry |
| 1.0–2.7 | same | same | Context chunks; **bold** on the niche noun and the first number ("**$5M** in revenue") | none | dry |
| **2.7–4.4** | **First cut** (`open_s`): to SHOT-GUEST if the asker keeps talking, or to SHOT-HOST on the host's first interjection | **Carried** unchanged (P-03) while the question is still being asked, if it clears the new face (§3.7) | continues (host words white) | the first cut | dry |
| 3.8–12 | Handover cuts and listener cutaways while the question finishes | **Gone in 0 f at the end of the question sentence**, on a cut or mid-shot; never past 12 s | continues | as the talk needs | dry |
| 10–40 | The host's first clarifying question ("what do you actually want?") on SHOT-HOST, by a handover cut | — | white | — | dry |
| by 60 | The answer starts (reframe or verdict) | — | — | — | — |

Measured (30 fps bursts): v01 stack 0.00–4.37 s, pill out at 3.83 s while the stack is still up, first caption on f4
(0.13 s), swaps at 0.97 / ≈ 2.1 / ≈ 3.2 s; v02 stack 0.00–4.0 s, pill carried across the cut to 4.73 s; v03 stack
0.00–2.67 s, pill carried across five cuts to 11.53 s. The pill on f0–f3 is identical (no pop, no fade). The first three
seconds feel full without a single graphic moving: the faces are live, the captions swap on the words, the pill holds still
over them.

### 6.3 Alternate hooks
**HA-03b Verdict pill (F-A).** The HA-03 table, but the pill is the host's verdict in his words, **no quotes** ("YOU NEED
TO MAKE / BIGGER BETS", v01). Use it when the answer is the hook (a surprising verdict) and the question is ordinary; e.g.
"RAISE YOUR PRICES FIRST".

| t (s) | What |
|---|---|
| f0 | Stack + verdict pill + the asker's first chunk |
| 0–4.4 | The asker sets up; the viewer reads the verdict and waits for the "why" |
| the verdict line | When the host says the pill's words, that chunk is CS-2 (the punch) on SHOT-HOST |

**HA-14 Cold answer (F-A, F-B).** Use it when the kept clip opens with the host already talking (the question was asked
off-mic, or the host restates it): "So your question is, do you hire a manager now?"

| t (s) | What |
|---|---|
| f0 | SHOT-STACK with the host on top **speaking** (a white chunk on the seam) + the question pill (quoted only if verbatim) |
| 0–2.7 | The host restates the question in his words; the asker's face is the reaction |
| 2.7–4.4 | The first cut, to SHOT-HOST; the pill carried |
| by 12 | The pill gone; the answer continues |

**HA-05 Pill + question card (F-B default).** Every solo answer: the question card takes the asker's place in the bottom
cell, so the frame still says "someone asked this"; e.g. `“HOW DO I ASK / FOR A RAISE?”`.

| t (s) | Layout | Pill | Captions | Cut |
|---|---|---|---|---|
| f0 | `L-solo-stack`: the creator top (eye y 403), the question card bottom (y 1030–1500) already up | **Fully drawn**, the question in quotes | If the creator reads the question: yellow italic on the seam | — |
| 0.0–2.7 | same; P-30 underlines the phrase of the card being read (6 f) | same | yellow italic while reading, white when answering | none |
| 2.7–4.4 | Hard cut to `L-full-solo` (re-crop 1.0) on the creator's first answer word | Carried | white | the first cut |
| 4.4–8 | Jump re-crops on the new thoughts | Removed on the first cut after the question is read, never past 12 s | white | as the talk needs |

### 6.4 Hook pairs by topic: question → answer
Write the pair for every reel: the question the pill asks, and the moment it's answered.

| Topic | Question (pill, as asked) | Where the answer lands | How it's shown |
|---|---|---|---|
| Pricing | “SHOULD I RAISE MY PRICES?” | The host's verdict at 25–45 s ("charge double, lose half") | CS-2 punch on SHOT-HOST, then a stack return for the asker's reaction |
| Hiring | “MANAGER OR ONE MORE CLEANER?” | 40–70 s, after the host asks "what's your margin?" | Handover cuts through the clarifying exchange; bold on the margin number |
| Selling the company | “SHOULD I SELL MY COMPANY?” | 60–120 s (the reframe: "what would you gain?") | A long stack return on the reframe |
| Retention | “WHY DO MY EMPLOYEES LEAVE?” | 50–90 s, a set-piece at a board | P-21 set-piece, CS-3 on the key word |
| Burnout | “I WORK 80 HOURS. NOW WHAT?” | 30–60 s | Listener cutaways on the asker's nods |
| A flat yes/no (supplements) | “DO I NEED CREATINE?” | 20–40 s | The verdict pill (HA-03b) when the answer is a flat yes or no |
| A warning (injury) | “SHOULD I TRAIN THROUGH PAIN?” | 15–30 s (`warn`) | SHOT-HOST and an angle switch on the warning word |

### 6.5 Pill writing
**Question pill formula:** the asker's question as a **verbatim contiguous span** of the transcript, 6 words or fewer, ALL
CAPS, curly quotes, ending in "?". Drop only leading or trailing fillers and articles ("so", "like", "a", "the", "um"). If
the asker never says the question in 6 contiguous words or fewer, write it in your own words **without quotes**: it's then
the reel's title, not a quote.

**Verdict pill formula:** the host's verdict as spoken, 6 words or fewer, ALL CAPS, no quotes, imperative or declarative
("YOU NEED TO MAKE BIGGER BETS").

| Template | Example |
|---|---|
| Should I … ? | “SHOULD I SELL MY COMPANY?” |
| Why do/does … ? | “WHY DO MY EMPLOYEES LEAVE?” |
| How do I … ? | “HOW DO I ASK FOR A RAISE?” |
| X or Y? | “MANAGER OR ONE MORE CLEANER?” |
| Is it … ? | “IS RETINOL SAFE EVERY NIGHT?” |
| Verdict | YOU NEED TO MAKE BIGGER BETS |
| A title in your words | SELL OR KEEP THE COMPANY? (not a verbatim span, so no quotes) |

- **Line break:** after the 2nd–4th word, so line 1 holds the verb phrase and is the longer or equal line (v01 "YOU NEED
  TO MAKE / BIGGER BETS", v02 "“SHOULD I SELL MY / COMPANY?”", v03 "“WHY DO MY / EMPLOYEES LEAVE?”").
- **Never:** words that weren't said inside a quoted pill; hype ("INSANE", "MUST WATCH"); emoji; numbers that weren't
  spoken; the asker's full name or company name unless the creator confirms they may be named.

### 6.6 Hook sound
Dry: no cue in the hook. The bed (when on) runs from f0 at −26 dB under the voice (§11).

### 6.7 CTA
| Device | Spoken | On screen | Hold | Where | Silence before |
|---|---|---|---|---|---|
| none (default) | — | Nothing: the clip ends on the last "thank you" or verdict word + up to 6 f (v01 @ 1:52, v02 @ 2:30) | — | end | — |
| post only | — | Nothing on screen; the CTA lives in the post text | — | — | — |
| comment keyword | The creator says "comment KEYWORD" **in the recording** | The CTA pill (P-04) `COMMENT “KEYWORD”` at y 672 on SHOT-HOST / `L-full-solo`, 6 f fade in on the word "comment" | 1.5–3.0 s | end (after the verdict, before "thank you") | no cue in the 1.0 s before |
| link in bio | "link in my bio" spoken | The CTA pill `LINK IN BIO` | 1.5–3.0 s | end | no cue in the 1.0 s before |

If the chosen device was never spoken, it goes in the post text and the plan says so. Never a CTA voice-over, an end card
or a follow button. A paid integration carries a "Paid partnership" line (Montserrat 500 24 px, x 64, y 1460) for the
whole sponsored span.

---

## §7 Structure and rhythm

### 7.1 Structure: the conversation
| Unit | What | F-A, where it usually sits | F-B |
|---|---|---|---|
| **Q** Question setup | The asker: who they are, their numbers, the question (the pill already says it) | 0–15 s | 0–6 s (the creator reads the question) |
| **C** Clarifying exchange | The host asks a few short questions; the asker answers in a few words | 10–45 s | — (or one rhetorical question) |
| **R** Reframe | The host names what the question is really about | 30–70 s | 6–20 s |
| **A** Advice | The concrete what-to-do (steps, a number, a board) | 50–130 s | 15–60 s |
| **V** Verdict | The one line that answers the pill | the last 10–20 s | the last 5–10 s |
| **T** Thanks | "thank you!" from either side; the clip ends | a breath | — (ends on the verdict) |

### 7.2 Markers
None on screen. Steps the host counts out loud ("first… second…") stay spoken: no numerals, chips or progress bars. The
only on-screen structure is the CS-2 punch line and, in F-B, the board items.

### 7.3 The turn ritual (the same for every turn)
1. **Handover cut** to the new speaker's single (SHOT-HOST / SHOT-GUEST) on their first word − 1 f.
2. **Hold the speaker** while their first sentence lands.
3. As the turn goes on, give the eye somewhere new at a sentence end: the **listener's face** (P-17) or the speaker's
   **other camera** (P-18; the ×1.25 re-crop with one camera). Alternate the two; never two re-crops in a row on one angle.
4. When the answer keeps developing, **come home to the stack** (P-15), host top, asker bottom, and hold it as one shot
   while the asker takes it in; then back to a single. A long single on a gesturing host is the alternative.
5. **Back-channels** ("yeah", "mmh") inside the turn: a short cut to the listener (P-20) only when the reaction is visible
   (a laugh, a nod); otherwise caption it on the current shot (P-13).
6. The next handover starts the ritual again.

### 7.4 Open loops and re-hooks
**The loop** is the pill's question, and the verdict must answer that exact question. A long conversation sags without
fresh tension, so something new grabs whenever the energy dips; mark it `rehook: true` on the beat.

| ID | Re-hook | Example |
|---|---|---|
| **RH-1** | The host's clarifying question on a handover cut | "do you have kids? are you married?" (v02 @ 0:36–0:38) |
| **RH-2** | A stack return on the reframe line, so the asker's reaction is visible | v01 @ 1:27, v02 @ 0:22 |
| **RH-3** | A CS-2 punch line | "you're gonna / **work again**" (v02 @ 0:26) |
| **RH-4** | The set-piece starts: the host goes to the board (P-21) | v03 @ 1:03 |
| **RH-5** | The "here's what I'd do" turn | "so this is me…" (v01 @ 0:51) |

**F-B:** one re-hook in the middle, the stack return to the board or to the question card ("so back to your question…").
The hook is over fast: the first answer word arrives while the question is still fresh.

### 7.5 Rhythm by feel
The speech is the rhythm. Each unit breathes its own way:
- **Q:** captions swap fast; the picture barely moves. The opener holds while the asker sets up, and the pill does the
  work.
- **C:** the fastest cutting of the reel, almost line by line (v02 @ 0:36–0:44 cuts about every second): two people
  throwing short lines at each other, and the picture right there with every one.
- **R / A:** long host turns, broken by a listener's face, an angle switch, a return to the stack. Long enough to think,
  never long enough to sit. The punch caption waits for the line that *is* the answer.
- **V:** slow down. The verdict line on SHOT-HOST or a stack return, then **one** reaction from the asker, then "thank
  you" and the hard end. Tension, then release.
- There are no planned comedy beats. Laughter in the room is kept and shown on a reaction (P-23).

For reference, measured on the three reels (a description, not a target): 13.8 / 17.5 / 15.9 cuts a minute; median shot
2.2 / 2.0 / 2.9 s; across all 113 cuts, median 2.3 s, p75 4.2 s, p90 6.7 s; the longest single-chunk caption hold ≈ 2 s
(v02 @ 1:00–1:01). F-B has no reference clip: its rhythm is designed to feel the same.

---

## §8 Visual system: B-roll and patterns

### 8.1 The role of graphics
Graphics are almost nothing, and that's the style. In F-A the pill rides the hook and the captions carry the words; the
CTA pill appears only when a CTA was spoken. In F-B, the pill plus one bottom-cell insert while `L-solo-stack` is up. The
references have no B-roll at all in 410 s.

**Numbers don't become pictures here.** A number becomes a **bold caption word** ("**$44M**"), and that's all: no
counters, charts, bars or hero numbers. The pictures in this style are faces, and the "show the thing" rule is served by
the cut: when the host says "you", the cut shows you the asker; when he talks about a board, the cut shows you the board.

The pattern library is mostly cut grammar: 4 pill, 9 caption, 11 cut and 7 F-B layout and insert patterns. Variety comes
from the conversation, never from a quota.

### 8.2 Families
| ID | Family | Source | The creator supplies |
|---|---|---|---|
| **B-1** | Camera shots (singles, stack, wide, re-crops) | the creator's footage | F-A: 2+ cameras or one 4K wide; F-B: one camera |
| **B-2** | Caption devices (CS-1/2/3, speaker styles, quotes) | engine | — |
| **B-3** | The pill (hook, CTA) | engine | — |
| **B-4** | F-B bottom-cell inserts (question card, board, screen) | the creator's own screenshot or screen recording; a real product or page they name, fetched from the web; else a created card (`fx.quoteCard`, the board scene) | optional: the screenshot of the question, their screen recording |

### 8.3 Pattern specs (30 fps)
**Pill patterns (B-3)**

| ID | Pattern | What's on screen | Motion (frames) | Use when | Needs |
|---|---|---|---|---|---|
| **P-01** | Question pill | The asker's question, verbatim, curly quotes, 2 lines, red per-line boxes | Present from f0, no entrance; removed in 0 f at the end of the question sentence (cut or mid-shot) | HA-03 / HA-05 default | `kind: "pill"`, `cuts` at t_out |
| **P-02** | Verdict pill | The host's verdict as spoken, no quotes | as P-01 | HA-03b | as P-01 |
| **P-03** | Pill carry | The same pill, unchanged, across the picture cuts inside the question sentence | Rect constant (0 px drift) across cuts | Every hook: it rides any cuts inside the question sentence and goes where the sentence ends (3.8–11.6 s measured, never past 12 s), as long as it clears every face it crosses | — |
| **P-04** | CTA pill | `COMMENT “KEYWORD”` / `LINK IN BIO` in the pill recipe | Fade in 6 f on the spoken word; out on the last frame | Only with a spoken CTA (§6.7) | `kind: "cta-keyword"` |

**Caption patterns (B-2)**

| ID | Pattern | What | Motion | Use when |
|---|---|---|---|---|
| **P-05** | Host caption | White upright 500, 1–4 words, cy 960 / the seam | Hard swap 0 f, lead 1 f | Every host word |
| **P-06** | Asker caption | Yellow italic 500 | as P-05 | Every asker word (F-B: the question read aloud) |
| **P-07** | Bold word | One word (or one 2-word idea) at 800 inside the chunk | none (weight only) | Numbers, the niche noun, the key verb |
| **P-08** | Punch line (CS-2) | 1–3 words at 84 px, 800 | Hard swap | The line that is the answer |
| **P-09** | The word (CS-3) | One word at 120 px, 800 | Hard swap, held at least 15 f | The single concept the answer turns on |
| **P-10** | Voiced quote | A curly-quoted span, italic, in the voiced person's style (§5.3.2) | Hard swap | "and you're like '…'" |
| **P-11** | Action caption | A `*stage direction*` in white upright | Hard swap, 0.8–1.5 s | **Only with light comedy on**: a wink on a reaction shot, spent on the reactions that earn one; never in the hook, the verdict or the CTA |
| **P-12** | Cut-off hold | "where you're-" held through the restart pause | Held up to 0.6 s past the word | A self-interruption |
| **P-13** | Back-channel caption | "yeah", "mmh", "okay", "nope" in the listener's style | Its own chunk | On the listener's reaction shot, or on the current shot when the reaction isn't visible |

**Cut patterns (B-1, F-A)**

| ID | Pattern | What | Recipe (shots) | Use when |
|---|---|---|---|---|
| **P-14** | Stack open | SHOT-STACK, host top / asker bottom | 2.7–4.4 s from f0, ending on a word onset | Every F-A reel |
| **P-15** | Stack return | SHOT-STACK mid-reel | Held as one shot (no in-stack re-crop), up to 20 s | A long turn, the reframe, the verdict: whenever both faces matter |
| **P-16** | Handover cut | The new speaker's single | On the first word − 1 f (±3 f) | Every speaker change on a full shot |
| **P-17** | Listener cutaway | The listener's single while the other talks (`cut_reason: "reaction"`) | 1.0–3.0 s; starts at least 1 s into the turn, ends at least 1 s before the handover, never spans one | Inside a turn long enough to want a new view; reactions worth seeing (a nod, a smile, a frown); a 1.2 s cutaway is the reaction to a number (v01 @ 0:15.4) |
| **P-18** | Angle switch | The same speaker on another camera (SHOT-ALT); the fallback is the same angle at step 1.0 → 1.25 (or back) | On a word onset at a sentence end | Long host turns, instead of a repeat (v01 @ 0:51.3 front → podium; v02 @ 0:16.2, 1:09.3 → full-body wide) |
| **P-19** | Wide establish | The room or crowd from behind the audience: the host small on stage, or the asker in the crowd while she speaks | 1–4 s; two in a row up to 6 s; blurfill if the wide can't crop | Before the answer starts; when the host walks; as the asker's second angle mid-question (v01 @ 0:36.8–0:46.4) |
| **P-20** | Back-channel cut | Up to 1.6 s on the listener's "yeah" or laugh | Only when the reaction is visible | Inside long turns |
| **P-21** | Set-piece | The host at a board or flip chart: full on the board while he writes, then a stack (board top, asker bottom) while he explains | Full 2–6 s per writing burst; stack 4–14 s | When the host draws or writes (v03 @ 1:03–1:42) |
| **P-22** | Walk follow | The host walking: the medium-wide crop follows with a dead zone | Follow ≤ 60 px/s; cut when he stops | The host moves on stage (v02 @ 1:27–1:29) |
| **P-23** | Laugh hold | The asker or the room laughing | Hold 1–2 s; never cut inside the laugh | A laugh after a host line (v02 @ 0:42–0:43) |
| **P-24** | Thank-you end | The last "thank you!" on whoever says it | Hard end ≤ 6 f after the word | Every F-A reel (v01, v02) |

**F-B layout and insert patterns (B-1, B-4)**

| ID | Pattern | What | Motion | Use when | Needs |
|---|---|---|---|---|---|
| **P-25** | Question card | The question in the bottom cell: the creator's screenshot (`fx.shot`) or a created card (`fx.quoteCard`, verbatim) | Present at f0 (the opener), or rises 10 f + de-blurs on a stack return; leaves with the stage cut | The opener; "so back to your question" | — |
| **P-26** | Solo stack open | `L-solo-stack` + P-25 + the pill | 2.7–4.4 s from f0, out by `via: "cut"` | Every F-B reel | — |
| **P-27** | Solo re-crop | `recrop-in` / `recrop-out` on an EDL cut | 1 f, written 1 f before the cut | Every F-B cut that isn't a stage change | the split EDL |
| **P-28** | Board | A `board` card in the insert rect (the cell stays `W-void`); up to 4 marker words written left to right on their spoken word; title 96–120 px, items 64–96 px | Write-on 10 f each (title 12 f); tick or underline 6 f on the item being discussed | The creator lists 2–4 things, a formula or a ladder | — |
| **P-29** | Screen cell | The creator's own screen recording or slide in the insert rect (`fx.shot`, `chrome: false`) | Rises 10 f; plays at 1× | "Look at this": a dashboard or document the creator owns, or a real page they name | the creator's asset, else the real page captured from the web |
| **P-30** | Card highlight | A 6 px `accent` underline under the phrase of the question card being read | Draws left to right in 6 f on the phrase's first word | The opener; the stack return to the question | — |
| **P-31** | Full return | A hard cut from `L-solo-stack` to `L-full-solo` at re-crop 1.0 | 0 f | The first answer word after the opener; the verdict | — |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Watch the conversation, ask what the viewer
should be looking at right now, then use it.

| Line type | For example | Primary | Alternates |
|---|---|---|---|
| Question setup (who I am) | "I run a cleaning company, 6 people" | P-14 + P-06 + P-07 (bold the niche noun) | P-25 (F-B) |
| Context number | "we did $40K last month" | P-06 / P-05 + P-07 on the number | P-17 (the host's reaction to the number) |
| The question itself | "should I hire a manager?" | P-01 already says it; keep the shot | P-30 (F-B) |
| Clarifying question (host) | "what's your margin?" | P-16 handover + RH-1 | P-15 |
| Short answer (asker) | "about 30%" / "nope" | P-16 to SHOT-GUEST, P-07 on the number | P-13 on the host's shot if it's under a second |
| Back-channel | "yeah", "mmh", "okay" | P-13 | P-20 |
| Reframe | "you don't have a hiring problem, you have a pricing problem" | P-15 stack return + RH-2 | P-08 |
| Advice step | "first, raise prices 20%" | P-05 + P-07, P-18 angle switches | P-28 (F-B board item) |
| Hard truth (`warn`) | "you're playing too small" | SHOT-HOST + P-18 on the bold word | P-08 |
| Voiced quote | "and they go 'great!'" | P-10 | — |
| Demonstration | the host writes on a board or pulls up a screen | P-21 (F-A) | P-28, P-29 (F-B) |
| Laugh in the room | the asker laughs at a host line | P-23 | P-11 (only with light comedy) |
| Verdict | "that's what I would do" | P-08 on SHOT-HOST, then one asker reaction | P-31 (F-B) |
| Thanks | "thank you!" | P-24 | — |
| Third-party mention (a book, an app, a person) | "read *Atomic Habits*" | caption only (glossary spelling) | F-B: the real cover, logo or page in the insert rect, the creator's or fetched (§12.4) |

### 8.5 Numbers and truth
- No data figures. A spoken number appears as a caption word, in the style's number format (§5.5).
- Numbers shown are exactly the spoken numbers: never re-rounded, never added.
- Created F-B cards show only words that were spoken or that the creator gives; they need no label.

### 8.6 Comedy layer
Off by default. The creator may turn it up to **light**: then **P-11 action captions** come in (white upright, in
asterisks, 0.8–1.5 s, on a reaction shot; never in the hook, the verdict or the CTA). The references hold two in 410 s
("*alex approves*", v01 @ 0:15; "*boop*", v03 @ 1:31): they're a wink, not a running gag. No stickers, stamps, meme sounds
or freeze-frames at any level: roasting isn't part of this style.

### 8.7 Assets
- Real footage only: the conversation as filmed. No stock, no AI scenes.
- F-B question cards: the creator's own screenshot first (identifiers blurred, §2); else a created generic card (no
  platform logo, no invented username: the name line reads "A follower asked").
- Third-party products, books, apps, people: caption only in F-A (the room is the picture); in F-B, the real thing,
  fetched when the creator doesn't have it, source noted (§12.4).

---

## §9 Transition system

### 9.1 Library
| ID | Transition | Frames | Sound |
|---|---|---|---|
| **T-00** | Hard cut | 0 | none |

That's the whole library (26 / 44 / 39 cuts in the references, every one straight; 113 measured at 30 fps). F-B stage
changes are written `"via": "cut"`.

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | The stack, the pill and the first caption already there | A fade-in, a black frame, a title card |
| Hook → body | The first cut at 2.7–4.4 s; the pill rides across it only while the question is still being asked, and leaves in 0 f where the question ends | Holding the pill after the question ends just to reach a cut |
| Any cut | Lands on a caption-chunk boundary: the new chunk appears on the cut frame (v01 @ 4.367, 54.067) | A chunk that swaps 1–5 f off the cut |
| Speaker change | T-00 on the new speaker's first word − 1 f | A cut inside a word; a cut more than 3 f late |
| Inside a long turn | T-00 to a listener cutaway, an angle switch or a stack return | Two re-crops in a row on one angle; a cut mid-word |
| Back to the speaker | T-00 | — |
| Into / out of the stack | T-00 | slide-down, morph, fade |
| The last word | Hard end ≤ 6 f after "thank you" or the verdict | A black tail over 0.2 s, an end card |

### 9.3 Shot grammar
These are the rules `veos shots plan` builds from (`dialogue.cut_rules`, §3.8). The holds are ceilings, never targets.

| ID | Rule | Recipe | Evidence |
|---|---|---|---|
| **R-SPK** | Cut on the first word of a new speaker when either side is a full shot | ±3 f (`handover_tol_f`), 1 f lead | v02 @ 0:36–0:37 ("be an alcoholic" → host full) |
| **R-OPEN** | Open on SHOT-STACK (host top, asker bottom) | 2.7–4.4 s (`open_s`) | 4.37 / 4.0 / 2.67 s |
| **R-HOLD** | A single holds as long as something is happening in it; a stack as long as the answer is landing | ceilings: full 10 s (`max_hold_s`), stack 20 s (`stack_max_s`) | full 10.5 / 10.8 s (v01); stacks 12.1–23.7 s |
| **R-REACT** | A listener cutaway inside a turn | 1.0–3.0 s (`reaction_s`); at least 1 s after the turn starts and 1 s before the next handover | v01 @ 0:54–1:05, v02 @ 1:13–1:14, 1:20–1:21 |
| **R-JZ** | A same-speaker angle switch instead of a repeat; the ×1.25 re-crop (`recrop_step`) only when the person has one camera | on a sentence end | v01 @ 0:51.3; v02 @ 0:16.2, 1:09.3 (v01 @ 0:14–0:18 is fast host / asker / wide alternation, not re-crops) |
| **R-WIDE** | A wide establish: a glance at the room | 1–4 s, two in a row up to 6 s; before the answer, when the host walks, or as the asker's crowd angle | v01 @ 0:37–0:38, 1:08–1:09; v03 @ 0:21–0:26 |
| **R-STACK** | A stack return when both faces matter; host always on top; held as one shot | `stack_share` 0.35 is the planner's aim (measured 36 / 32 / ≈ 25 %) | v01 1:27–1:51, v02 0:22–0:36, v03 1:10–1:30 |
| **R-BC** | A back-channel shows the listener only when the reaction is visible | up to 1.6 s (`backchannel_max_s`) | v02 @ 0:28–0:29 "yeah" on the stack |
| **R-SET** | A set-piece: full on the board while writing, the stack (board top / asker bottom) while explaining | full 2–6 s, stack 4–14 s | v03 @ 1:03–1:42 |
| **R-LAUGH** | Never cut inside a laugh; hold the laugher 1–2 s | — | v02 @ 0:42–0:43 |
| **R-END** | The clip ends on "thank you" (or the verdict) + up to 6 f; no outro | — | v01 @ 1:52, v02 @ 2:30 |
| **R-MIN** | No shot shorter than 0.8 s (`min_shot_s`) | — | — |
| **R-SAME** | Never cut a framing to itself; never a stack of the same person twice | — | — |

### 9.4 How the moves breathe
Every cut has a reason you could say out loud: someone new is talking, someone is reacting, the speaker turned a corner in
their thought, both faces matter now. If you can't name the reason, don't cut. The clarifying exchange is where the cuts
come thick and fast; the advice is where the stack settles in and the cuts slow to the speed of thinking. The listener's
face is the most powerful shot in the style, so spend it on reactions worth seeing. Wides are rare glances, angle switches
come when a long turn needs fresh air, and the same kind of cut doesn't come round again and again unless the
conversation itself is a rapid volley.

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Lead | Shot cuts and captions 1 f before the word onset |
| Caption swap | Hard, 0 f. Verified at 30 fps: v01 f3 → f4 "I sell" appears full size, f28 → f29 the next chunk; CS-2 "you're gonna" static f785–f795 (no pop, no scale, no fade) |
| Pill | No entrance (f0–f3 identical); hard 0 f exit where the question sentence ends (3.83 / 4.73 / 11.53 s) |
| CTA pill | Fade in 6 f, ease `cubic-bezier(0.22, 1, 0.36, 1)`; out on the last frame |
| Exit ease (the caption band's final 6 f out) | `cubic-bezier(0.64, 0, 0.78, 0)` |
| F-B card rise | 10 f, a 24 px rise + 8 → 0 px blur, ease out; it leaves with the stage cut |
| F-B board write-on | 10 f per word, a left-to-right clip reveal; the title 12 f |
| F-B tick / underline | 6 f, 6 px, `ink` (board) or `accent` (card) |
| Cut / angle switch / re-crop | 0 f; no flash, blur, dip or whoosh at any of the 113 measured cuts |
| End | A hard end on the last frame, no fade (v02: the last 24 f on the host, "thank you!" held to f4524) |
| Holds | Captions at least 0.25 s per word; CS-3 at least 0.5 s; titles and inserts at least 10 f after they finish building; inserts up for at least 2.7 s |

### 10.2 Footage camera: crop on cut (`zoom_policy: crop_on_cut`)
Framing changes only on a cut: another camera on the same person, or a ×1.25 re-crop when there's one camera; never an
animated push, punch or shake. Measured: no keyframed zoom in 410 s (the first and last frames of 10–24 s shots match in
scale within 1 %: v01 @ 0:17.9 / 0:28.2 ORB scale 1.000; the only movement inside a shot is the live operator's slow pan).
- **F-A:** no `camera` events at all. Re-crops are shots with `"step": 1.25` (`veos shots render` composes them; at most
  2.0× upsampling, and a 1080p source at most 1.35×).
- **F-B:** two presets only, each on a cut (checked within ±2 f):
  - `recrop-in`: scale 1.00 → 1.25 in 1 f, written **1 f before** the EDL cut so the new scale shows on the cut frame;
  - `recrop-out`: scale 1.25 → 1.00 in 1 f, placed the same way.
  - Alternate in → out → in. **After every stage change the camera resets to 1.0**, so the first re-crop after a stage
    change is always `recrop-in`.
- **Never:** snap-punch, crash-zoom, push-drift, shake, rotation. There's no canvas camera: the footage is the frame.

### 10.3 Layer order (back to front)
1. Footage (composed shots in F-A; the stage in F-B)
2. F-B world in the graphic cell (`W-void`)
3. F-B insert (question card, board card, screen) at z 4
4. Captions (auto, z 7)
5. The pill / CTA pill (z 10)

### 10.4 Finishing
No grain, vignette, bloom, glow, LUT or blur is added. Cameras are matched for exposure and white balance only. Insert
cards have a soft shadow `0 8 24 rgba(0,0,0,.35)` and radius 28; nothing else has a shadow except the captions' text shadow
and the pill's faint one.

---

## §11 Sound
| Line | Decision |
|---|---|
| **Where sound goes** | Only on the CTA: one soft pop or click when the CTA pill appears, if a CTA is shown. The hook, the cuts, the captions, the pill and the inserts are silent: the conversation is the soundtrack |
| **Meme sounds** | None, ever |
| **Music bed** | On, from f0, a soft non-melodic bed at −26 dB under the voice (not observable in the references, so it's a decision, not a measurement); off when the room audio already carries an ambience the creator wants heard |
| **Ducking** | The bed ducks 24 dB under the voice while anyone speaks (never less than 18); room tone and audience laughter are kept and ducked under the voice |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the last word |

---

## §12 Footage handling

### 12.1 Setups
| ID | Setup | Framing | Notes |
|---|---|---|---|
| **A** | F-A live room: the host on a stage or a chair, the asker at a floor mic or across a table; 2–3 cameras (host single, asker single, room wide) | head top y 140–320 after the 9:16 crop | 1080p+; 4K on the host camera for ×1.25 re-crops on a 16:9 source; a mic per person, or one room mic |
| **B** | F-A single wide: one 4K camera sees both people | each faux crop's head top y 160–340 | FB-1; both faces at least 120 px tall in the 4K source |
| **C** | F-B solo: one camera, chest-up, the eye-line just off the lens as if answering someone | head top y 150–260 | a plain or lived-in background; 4K preferred for re-crops |

### 12.2 Shots and fallbacks
| ID | Shot | Spec | Must / optional | Formats | Fallback |
|---|---|---|---|---|---|
| **SH-1** | Host single | medium (waist-up) to medium close-up; an optional second host camera (side, or full-body from the crowd) for SHOT-ALT | must (the second angle optional) | F-A | FB-1 |
| **SH-2** | Asker single | medium close-up at the mic or across the table; it catches the listening reactions | must | F-A | FB-2 |
| **SH-3** | Room wide / audience | from behind the crowd; the host visible on stage | optional | F-A | FB-3 |
| **SH-4** | Solo talking head | chest-up, 1080p minimum, 4K preferred | must | F-B | FB-4 |
| **SH-5** | The question as received, or the creator's own screen, slide or whiteboard | a screenshot or a screen recording, any aspect | optional | F-B | FB-5 |

| ID | For | What the engine does | What it costs | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | Two faux crops of one wide (setup B): host crop + asker crop, 9:16 each, the face 27–30 % of a stack cell / 17 % of the full frame (`dialogue.single_cam_fallback: two_crops`) | A softer image (needs 4K), no true eye-line, re-crops limited to ×1.25 | degraded |
| **FB-2** | SH-2 | The asker crop from the wide; if the asker is never visible, the reel becomes F-B (the question becomes a question card) | No dedicated listener reactions | degraded |
| **FB-3** | SH-3 | Skip the wide; a jump re-crop ×1.25 → ×1.0 on the host replaces it | No sense of the room | holds |
| **FB-4** | SH-4 | none: F-B needs the creator on camera | — | no fallback |
| **FB-5** | SH-5 | Claude builds the question card (`fx.quoteCard`, the verbatim question, "A follower asked") or the board (P-28) from the spoken words | Not the real comment | holds |

### 12.3 Props, reaction bank, matte, resolution
- **Props:** F-A optional: a flip chart or whiteboard on stage for set-pieces (P-21). F-B: none.
- **Reaction bank:** the asker listening, nodding and laughing (free from SH-2); the host listening (arms crossed, hand on
  chin).
- **Matte:** none. Multi-speaker reels have no cut-out layer and no `behind` scenes.
- **Source resolution:** ×1.25 re-crops need at least 1080p in the 9:16 crop; FB-1 faux crops from a 16:9 wide need a 4K
  source (2160 px; a 1080p wide gives at most 1.35× in total).

### 12.4 Third-party inserts: fetch the real thing
1. **Find the moments.** In this style most of them stay "caption only": F-A shows nothing but the room.
2. **F-B only:** for the question itself and for a product, app, book or document the creator names and points at, the
   creator's own files in their folder come first (`veos asset add "<file>" --name <name>`).
3. **Otherwise search the web and fetch it:** the real logo, the book cover, the real app or page (captured and framed on
   the part that matters), with `veos asset add "<file>" --name <name> --source "<url>"`. Show it with `fx.shot` in the
   insert rect, as it is; blur personal identifiers.
4. **Nothing usable to be found:** the question → `fx.quoteCard` (the question as spoken, name line "A follower asked");
   a product or app → `fx.logoPlate` (the name set in type); a document or app screen → `fx.appUI` (a generic
   recreation, no label, no credit).

### 12.5 Frame rate and audio
- 30 fps CFR (conform VFR phone footage); 1080×1920 output.
- F-A: sync the cameras and mics (`veos sync`; every source's confidence at least 0.5); the `MIX` source (a gain-sharing
  automix of the mic tracks) is the voice. F-B: one voice track.
- Voice chain: high-pass 80 Hz, de-ess, light compression; −14 LUFS; true peak ≤ −1.5 dBTP.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The format** (F-A or F-B) and **the mined span** (F-A): what was kept, what was dropped and why (whole sentences
   only).
2. **The cast and the angle map:** which camera or faux crop shows whom; the fallbacks used (FB-…).
3. **The hook:** the archetype (HA-03 / HA-03b / HA-14 / HA-05), the pill with its alternates (verbatim span and time, or
   "a title, no quotes"), the opener's length, the word where the pill leaves, and the hook pair (where the answer lands).
4. **The turn map:** `timeline.shots` shaped by the grammar, every beat with its speaker, angle, crop step and
   `cut_reason` (`open` / `handover` / `reaction` / `recrop` / `stack` / `establish`), and the re-hooks marked.
5. **The captions:** the profile per beat, the speaker and text overrides (§5.3.2), the forced bold words, the CS-2 and
   CS-3 lines, the masked words.
6. **F-B:** the inserts (the creator's, fetched with the source, or created) and the board words with their spoken times.
7. **The sound:** bed on or off, the CTA cue.
8. **The moments you'll look at hardest on the storyboard:** f0 (both heads clear of the pill and the caption), the
   first cut with the pill carried, one stack return (the bottom head against the seam caption), one listener cutaway,
   the verdict, the last frame.

The reel header, for the shape:
```yaml
reel:
  format: F-A                     # F-A | F-B
  hook_archetype: HA-03           # HA-03 | HA-03b (verdict pill) | HA-14 | HA-05 (F-B)
  structure: conversation
  cast: {S1: {name: "<host>", role: host}, S2: {name: "<asker>", role: guest}}
  pill: "“SHOULD I SELL MY / COMPANY?”"     # verbatim span: "should I sell my company" at 3.1 s
  pill_out_s: 5.2                 # the cut that removes it
  pill_alternates: ["WHAT WOULD YOU / GAIN?", "SELL OR KEEP / THE COMPANY?"]   # the host's words at 74.2 s; a title, no quotes
  hook_pair: {question: "should I sell my company?", answer_lands_s: 74, answer: "what would you gain from the sale?"}
  keyword: null                   # the CTA keyword, when it was spoken
  duration_s: 128
  rehooks: [18.4, 41.0, 66.2, 93.5]
```

---

## §14 Worked examples
Times are planning estimates; the real ones come from the word onsets. Speaker names are placeholders.

### 14.1 F-A, business coaching: a live workshop Q&A (two cameras + a room wide), 118 s
**Clip:** the asker runs a cleaning company and asks whether to hire a manager. **Archetype:** HA-03. **Pill:**
`“SHOULD I HIRE / A MANAGER?”` (verbatim span at 6.9–8.1 s). **CTA:** none.

**Hook table**
| t (s) | Speaker: words | Shot | Pill | Captions | Notes |
|---|---|---|---|---|---|
| f0 | — | SHOT-STACK: host top (arms crossed, listening), asker bottom at the floor mic | drawn | — (first word at 0.12) | Thumbnail: two faces + the question |
| 0.12–1.30 | asker: "I run a cleaning company" | stack | on | "I run a" → "**cleaning** company" (yellow italic, on the seam y 960) | bold = the niche noun |
| 1.40–3.20 | asker: "6 people, about $40K a month" | stack | on | "**6** people" → "about **$40K** a month" | numbers as digits |
| 3.30–3.80 | asker: "and I'm stuck" | stack | on | "and I'm stuck" | — |
| **3.80** | asker: "I'm doing every quote myself…" | **cut → SHOT-GUEST** (the end of the opener, R-OPEN; same speaker, so not a handover) | carried (her chin clears y 632 on this medium shot) | yellow italic, cy 960 | the first cut |
| 5.60 | host: "okay" (back-channel, not visible) | stays SHOT-GUEST | carried | "okay" in white, its own chunk (P-13) | — |
| 6.90–8.10 | asker: "so should I hire a manager?" | SHOT-GUEST | carried | "so should I" → "hire a **manager**?" | the pill's words are spoken |
| **8.20** | host: "what's your margin?" | **handover cut → SHOT-HOST** | **removed on this cut** (8.2 s) | "what's your **margin**?" white | RH-1 clarifying question |

**Section plan**
| t (s) | Unit | Speaker / line | Shots (patterns) | Caption devices | Re-hook |
|---|---|---|---|---|---|
| 8.2–14.0 | C | host "what's your margin?" / asker "about 30%" / host "and who does the quotes?" / asker "me" | handover cuts every 1–2 s (P-16 ×4) | P-07 on "**30%**"; "me" yellow | 8.2 RH-1 |
| 14.0–26.0 | R | host: "you don't have a hiring problem, you have a you problem…" | SHOT-HOST 3.1 s → P-18 re-crop ×1.25 on "**you** problem" → P-17 asker cutaway 2.2 s (she laughs: P-23 hold 1.4 s) → SHOT-HOST | CS-2 punch "a **you** problem" | 14.0 RH-2 |
| 26.0–40.0 | R | the host keeps going (a 14 s turn) | P-15 stack return 9.5 s (host top speaking, asker bottom nodding) → SHOT-HOST | P-10 voiced quote: "and the client goes “where's my quote?”" in white italic (quote style) | 26.0 RH-2 |
| 40.0–52.0 | A | host: "so this is me: I'd hire someone to do the quotes first" | SHOT-HOST → P-18 → P-19 wide 1.6 s as he walks to the front → SHOT-HOST | bold on "**quotes**" | 40.0 RH-5 |
| 52.0–66.0 | A | host: "pay them per closed quote, not per hour" | SHOT-HOST 4 s → P-17 asker 2.0 s → SHOT-HOST ×1.25 | CS-2 "per **closed quote**" at 58.4 | — |
| 66.0–78.0 | A | asker: "but what if they're worse at it than me?" / host: "they will be. For 30 days." | handover cuts (P-16 ×2); the asker in SHOT-GUEST, the host in SHOT-HOST | "they will be" white; "for **30 days**" | 66.0 RH-1 |
| 78.0–96.0 | A | the host explains the 30-day handover, counting 3 steps out loud | P-15 stack return 18 s, held as one shot → SHOT-HOST | the steps stay spoken (no numerals on screen) | 78.0 RH-2 |
| 96.0–112.0 | V | host: "then you hire the manager. Not before." | SHOT-HOST ×1.0 → P-18 ×1.25 on "**not before**" → P-17 asker 1.8 s (nodding) | CS-2 "**not before**." | 96.0 RH-3 |
| 112.0–118.0 | T | asker: "thank you!" / host: "you got it" | SHOT-GUEST → handover cut SHOT-HOST → hard end 4 f after "it" (P-24) | "thank you!" yellow italic | — |

**How it breathes:** 118 s, 31 cuts. The stack is up for the opener, the long reframe and the 30-day handover (31.3 s in
all), so the asker's face is there whenever the answer is about her; the longest single is 5.8 s; the clarifying exchange
is the fastest stretch; the verdict slows to one line, one nod and a thank-you. No sound effects.

### 14.2 F-A, fitness podcast: one 4K wide camera (FB-1 faux crops), 96 s
**Clip:** a podcast guest asks the host coach why they aren't losing weight. **Archetype:** HA-03b (the verdict is the
hook). **Pill:** `EAT THE PROTEIN / FIRST` (the host's words at 71.4 s, no quotes). **Angles:** `CAM:S1` (host faux crop),
`CAM:S2` (guest faux crop), `CAM:2S` unused, no wide (FB-3: re-crops instead).

**Hook table**
| t (s) | Speaker: words | Shot | Pill | Captions |
|---|---|---|---|---|
| f0 | — | SHOT-STACK from faux crops: host top (`CAM:S1`), guest bottom (`CAM:S2`) | drawn | — |
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
| 34.0–60.0 | A | host: the plate order, protein first, then fibre, then carbs | re-crops 1.0 ↔ 1.25 every 1.5–2 s (P-18), 2 cutaways, a stack return 8 s | voiced quote "you tell yourself “just this once”" (quote style, white italic) | 34.0, 48.0 |
| 60.0–84.0 | A → V | host: "eat the protein first. Every meal." | SHOT-HOST ×1.0 → re-crop ×1.25 on "**first**" → guest reaction 2.0 s | CS-2 "eat the **protein first**" at 71.4 (the pill's words) | 60.0 RH-3 |
| 84.0–96.0 | V / T | host: "do that for 30 days and come back" / guest: "deal" | stack return 8 s → guest "deal" → hard end | "for **30 days**"; "deal" yellow | 84.0 |

**The fallback, in the plan's words:** "FB-1 used (one 4K wide): faux crops at ≤ 1.9× upsampling; re-crops stay at
×1.25; no wide shot (FB-3)." With one camera the re-crops do the work a second angle would: each new thought gets a new
frame.

### 14.3 F-B, career coaching: a solo answer to a comment, 62 s
**Input:** the creator's take + their screenshot of the comment (in their folder). **Archetype:** HA-05. **Pill:**
`“HOW DO I ASK / FOR A RAISE?”` (verbatim from the comment, which the creator reads aloud at 0.2–2.0 s).

**Hook table**
| t (s) | Words | Layout | Pill | Bottom cell | Captions |
|---|---|---|---|---|---|
| f0 | — | `L-solo-stack` (face top) | drawn | P-25: the creator's comment screenshot (`fx.shot`, avatar and handle blurred) | — |
| 0.20–2.00 | the creator reads: "how do I ask for a raise without sounding greedy?" | stack | on | P-30 underline under "ask for a raise" at 0.6 s (6 f) | yellow italic (speaker override `guest`): "how do I ask" → "for a **raise**" → "without sounding **greedy**?" |
| 2.10–3.40 | "okay, three things" | stack | on | — | white "okay" → "**three** things" |
| **3.40** | "first, bring proof" | `via: cut` → `L-full-solo`, scale 1.0 (P-31) | **removed on this cut** | — | "first," → "bring **proof**" |

**Section plan**
| t (s) | Line | Layout / camera | Inserts | Caption devices | Re-hook |
|---|---|---|---|---|---|
| 3.4–14.0 | "first, bring proof: what you shipped, in numbers" | full; EDL splits at 5.8, 8.1, 10.9, 12.6 with `recrop-in` / `recrop-out` (P-27) | — | bold "**proof**", "**numbers**" | — |
| 14.0–26.0 | "second, ask for a number, not 'more'" | `L-solo-stack` (cut) | P-28 board card: "PROOF" (written at 14.4), "NUMBER" (at 16.2) | voiced quote "not “more”" (quote style) | — |
| 26.0–34.0 | "third, give them a date" | full ×1.0 → `recrop-in` at 30.2 → `recrop-out` at 33.6 | — | CS-2 "a **date**" at 27.1 | — |
| 34.0–44.0 | "so back to your question: it's not greedy if it's priced" | `L-solo-stack` (cut) | P-28 board adds "DATE" (34.3), a tick on all three (40.0, 6 f each) | — | **34.0** the mid re-hook |
| 44.0–62.0 | verdict: "proof, number, date. Ask on Monday." | `L-full-solo` (cut, scale 1.0) → `recrop-in` on "**Monday**" | — | CS-2 "ask on **Monday**" | — |

**How it breathes:** 62 s, 15 cuts (EDL splits + stage cuts); the stack is up for the question, the list building and the
return to the question (25.4 s), and full frame for every point said to the viewer's face. Inserts: the question
screenshot (the creator's), the board (created, no third party).

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0: two live faces (F-B: a face and the question card) and the question in red; you'd stop.
- Nothing on screen besides the footage, the captions, the pill(s) and (F-B) the one insert. No zoom moves, no
  transitions, no sound on cuts.
- Every cut has a reason you can name: a new voice, a reaction worth seeing, a turn in the thought, both faces mattering.
- The stack is the home: it opens the reel, the host is on top, and it comes back when the answer is landing on the
  asker.
- The clarifying exchange is the fastest stretch; the advice breathes; the verdict slows to one line, one reaction and a
  thank-you.
- The punch caption is on the line that *is* the answer; bold words are numbers, things and verbs, never filler.
- Start to end with the sound off: you always know who's talking, and the verdict answers the pill's question.

**Craft (by eye, in context; the facts are in §2)**
- The faces read: both heads in every stack (the top chin above the pill, the bottom head's hair clear of the seam
  caption), the speaker in every single, the asker in the crowd in a wide; nothing buries a face or chops a head by
  accident.
- The pill: 6 words or fewer, 2 lines, quotes only if verbatim; drawn on f0; gone where the question sentence ends,
  between 2.7 and 12 s; clear of the faces on a carried cut.
- Every word captioned, 1–4 words, one line, up to 24 characters; hard swaps on the words; a cut on a chunk boundary;
  never a cut inside a word; handover cuts on the new voice.
- Host white upright, guest yellow italic, voiced quotes styled by §5.3.2; the colour follows the voice; the cast names
  and roles are right.
- Captions 68 px (CS-2 84, CS-3 120) at cy 960 / on the seam, out of Instagram's bands; readable against the real
  footage.
- Numbers as digits in the style's format, exactly as spoken; names and brands spelt right; profanity masked; no sentence
  reordered or spliced; quotes verbatim; created cards verbatim; fetched pages shown as they are; identifiers blurred.
- The CTA pill (if chosen and spoken) up long enough to read the keyword.
- The file itself (1080×1920, 30 fps CFR, −14 LUFS, the bed under the voice, a hard end ≤ 6 f after the last word, no
  black tail) is the render's job; it checks it.

---

## Appendix A. Evidence map
| What | Measured | Where |
|---|---|---|
| The stack opener under the red pill, host on top | seam y 960, no line; host top even while the asker speaks | v01 0:00–4.37, v02 0:00–4.0, v03 0:00–2.67 |
| The pill's life | drawn on f0; out where the question ends: 3.83 / 4.73 / 11.53 s | 30 fps bursts (v01 f115, v02 f142, v03 f346) |
| Captions | Montserrat 500 68 px, cy 960, hard swaps; guest `#F2DF1A` italic | fidelity audit, v01 @ 0:50, v02 @ 0:10 |
| Cuts | 113 hard cuts, no transitions, no editor zoom; cut frame = chunk swap frame | completeness pass, v01 @ 4.367, 54.067 |

The full map, the inferred values (F-B as a whole, the CTA devices beyond none, the bed) and the audits are in
`evidence.md` next to this playbook.

## Appendix B. Hook-title bank
Slots in `[brackets]` are filled per reel from the transcript; quoted pills must be verbatim spans.

**F-A (two-person Q&A)**
| # | Pill | Archetype | For example |
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
| 2 | “IS [THING] SAFE / EVERY DAY?” | HA-05 | a created question card |
| 3 | “WHAT SHOULD I / [VERB] FIRST?” | HA-05 | a board with 3 items |
| 4 | “HOW DO I PRICE / MY [SERVICE]?” | HA-05 | a board: the formula |
| 5 | “WHY ISN'T MY / [THING] WORKING?” | HA-05 | the creator's own screen |
| 6 | “DO I NEED / [THING]?” | HA-05 | a created question card |
| 7 | “HOW LONG UNTIL / I SEE RESULTS?” | HA-05 | a board: the timeline (3 dates) |
| 8 | “[A] OR [B] / FOR A BEGINNER?” | HA-05 | a board: two columns |
| 9 | “IS IT WORTH / [VERB]-ING?” | HA-14 | the creator restates it on camera |
| 10 | “WHAT WOULD YOU / DO AT [AGE]?” | HA-05 | a created question card |
