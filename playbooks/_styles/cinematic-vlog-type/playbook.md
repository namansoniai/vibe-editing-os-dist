# Cinematic Vlog Type Style Playbook (template v2)

## The feel

This reel is a short film about the creator's life, with a magazine cover printed over it while they speak. Frame 0 is
already moving: a mirror with the creator small inside it, a doorway they're walking toward, a drone looking straight
down at them on a railing. No title yet. Then a thin white handwritten line starts writing itself across the sky, and a
huge yellow word shoots up into place under it with a streak of motion, on the exact syllable. By the time the first cut
comes, the whole thesis has been said and seen, and you'd get it on mute.

That's the engine. The sentence becomes a poster as it's spoken: the yellow block shouts the word to remember, the white
script whispers the words that join them, and the eye reads only yellow. Underneath, the picture never stops travelling.
The voice runs on while the world keeps changing, each cut hidden inside a step, a turn, a whip: a kettle, keys, a street,
a hand, a rooftop. Every noun they list gets its own shot. It feels like being taken somewhere, not told something.

The creator lives inside the footage, not in a box. Often small, often walking, sometimes framed by a mirror. When a word
deserves depth it slides in behind their head and becomes part of the shot. When they show proof, the reel steps out onto
cream paper like a page from their journal: a card, a polaroid, a yellow hand-drawn circle. When they play a character,
the footage changes colour: black and white for the stuck one, amber for the obsessive, cold teal for the hacker. A quiet
pale-lemon serif runs along the bottom the whole time, like the subtitle of a film.

One yellow, and only for the words that matter. Never a card over a great shot. Dense in the hook, calm in the setup, a
dip at the turn, a peak at the payoff. And the last frame is the first frame, so the reel plays again before anyone
decides to scroll.

**The test:** pause on any frame and it looks like a still from the creator's own film, beautiful without the type, with
at most one yellow idea on it.

## What this playbook is

You're editing a narrated vlog: the creator's voice carries the reel (talking pieces filmed in a few places, or a
voice-over), and the picture is their own cinematic footage, chosen sentence by sentence. You have the authority to make
it the most watchable reel in their niche. This playbook is the style, pulled from five of OMGAdrian's reels (v01 a store
visit, v02 "3 types of content creators", v03 a vertical-composition tutorial, v04 a year of posting, v05 a phone
photo-editing tutorial), measured at full resolution and at full frame rate. Read it all, every time; take what fits this
reel, invent where a moment needs more, and never break the feel above.

**Who it's for and what it needs.** Travel, lifestyle, fashion, fitness, photography and food creators who shoot their
own B-roll. Input: talking pieces in two to five places plus plenty of their own B-roll (places, details, hands, a
signature prop, ideally a drone or overhead shot); the footage *is* the style, and every missing shot has a fallback
(§12.3). A real product, post or logo the reel names is fetched from the web when they don't have it (§12.5). The
person cut-out is needed for behind-the-head words and the poster sign-off. Captions follow the creator's language
(English verbatim by default; Hinglish or Hindi, §5.5); the yellow type stays English Latin caps. Reels run about a
minute to a minute and a half. Machine values live in `tokens.json`; where this text gives a number tokens also
holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Footage first, type serves it.** Never cover a great shot with a card; type goes in the sky, on the wall, in the empty top third, or behind the head | §3.6, §5.2, §12 |
| D2 | **One yellow.** `primary` is the only bright text colour. Keywords, counters, card titles, ink marks and the CTA keyword are yellow; nothing else is | §4 |
| D3 | **Script connects, block shouts.** Function words are white pen script; the keyword is always the yellow block. The script never carries the keyword | §5.2 |
| D4 | **The subtitle is always there.** Pale-lemon serif at y 1468 on every spoken line, except while a duo title, the chaos burst or a morph is on screen | §5.3 |
| D5 | **A thesis, not a result.** The hook states a thesis or asks a question in 3–4 type beats over a moving cinematic shot; the whole thesis is on screen by 3.0 s | §6.2 |
| D6 | **Cut like a vlog.** The picture moves on whenever the words give it a reason, cut on motion, one detail per listed noun | §7.5, §9.3 |
| D7 | **Paper for proof.** Examples, recaps, rules and app screens leave the footage world and sit on cream paper as cards or polaroids | §3.2, §8 |
| D8 | **Close the loop.** The last 1.0–1.5 s returns to the opening shot and ends on frame 0's picture | §7.6 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Formats, worlds, layouts, stage moves, safe zones, the person |
| §4 | Colour and the grades |
| §5 | Type and captions: the duo title, CS-1 pale-lemon serif, other text |
| §6 | Hook system: stopper test, HA-12 thesis typography, alternates, hook pairs, CTA, sponsor and end cards |
| §7 | Structure and rhythm: SM-1…SM-3, the unit rituals, open loops, rhythm by feel, the bookend loop, series furniture |
| §8 | Visual system (B-roll and patterns): families B-1…B-13, 41 patterns, line → pattern lookup, truth, comedy and ink, assets |
| §9 | Transition system T-1…T-13, grammar, shot grammar R-1…R-9, how the transitions render |
| §10 | Motion tokens, camera Z-1…Z-4, layers, finishing |
| §11 | Sound |
| §12 | Footage handling: setups, shots and fallbacks, cut-out, inserts, how B-roll plays |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style
lives or dies on two crafts: choosing which moment of which clip carries each word, and splitting the thesis into the
words that shout and the words that whisper.

1. **Pick the format** (§3.1). The script names steps, rules, settings or "how to" → F-B. Anything else → F-A. Never mix:
   an F-A reel may step onto paper for an example, but never runs the F-B rule ritual.
2. **Log the B-roll bank.** Give every clip an id (`B01…`), tags (subject, place, action, mood: `walk`, `detail`, `hands`,
   `product`, `wide`, `overhead`, `persona:<name>`), its usable span and its motion direction (for cut-on-motion). Mark
   SH-1, the opener, and check it has **at least 1.5 s of pre-roll before its in-point**: the bookend needs it (§7.6).
   Mark talking pieces by setup (A/B/C/D, §12.1). Talking pieces (or the voice-over file) carry the voice and become the
   cut map; every other clip is picture only and plays over the voice (§12.6).
3. **Count on the cut-out** for the talking pieces and the SH-11 headroom and SH-12 poster shots: behind-the-head words
   and the poster both need it (`matte: required`, so it starts right after the cut; make sure it's there before the
   storyboard). Check the hair at 200 %; a take with a messy matte gets its word above the head instead
   (FB-11).
4. **Feel the tone of every line:** `hype` (the thesis, a claim) · `awe` (a place, a cinematic reveal) · `explain` (a
   rule, a step) · `warn` (the problem state, a negative persona) · `win` (the result, the payoff) · `cta`. The tone picks
   the treatment: hype gets duo beats and cuts on motion; awe gets a second or two with no type, a Z-1 drift and the
   subtitle only; explain goes to paper with guide lines and yellow ink; warn gets the GR-mono persona (and the chaos
   burst if the line is about overload); win gets the polaroid after-state, the count-up and the warm grade; cta gets the
   keyword on the poster, then the bookend.
5. **Split the thesis (this style's signature craft).** Write it in 12 spoken words or fewer. Split it into
   **connectors** (articles, pronouns, prepositions, auxiliaries, conjunctions: script) and **keywords** (nouns, numbers,
   names, the main verb or adjective: block), group the keywords into 3–4 beats of 1–2 words, and time each beat to its
   spoken word (§5.2). Write 8–10 candidate hooks, pick by the stopper test (§6.1), keep the next two as alternates.
6. **Match a shot to every sentence.** A creator clip carries each idea; a listed noun gets its own detail shot; a place
   gets its establishing wide. Where no clip fits, the moment goes to paper (a card, a polaroid) or to a created visual
   (§12.5).
7. **Decide what leaves for paper, who gets a grade, and where the depth goes.** Lines that *show* something (an example,
   a recap, a rule, a screen, a photo) step onto paper; personas get their grade (§4.3); a keyword that deserves depth
   goes behind the head on a matted take with headroom; the one chaos burst goes on the one line about overload, if
   there is one.
8. **Keep the speaker's pauses honest.** Tighten talking-piece pauses to 0.35 s, except the deliberate ones (0.35–0.9 s
   inside a sentence): those stay, the subtitle shows ".." there, and the picture keeps moving through them.
9. **Plan the furniture:** the bookend (SH-1's in-point, the pre-roll span, the last sentence that rides it), the ink
   anchors (read sampled frames and write the x/y of every arrow tip and oval), the series number, the sponsor's logo and
   disclosure.
10. **Plan the sound** (§11): sparse; the cuts and the type carry the energy, a cue only marks a landing.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the person clear.** This is their life on film, so keep the face and hair clear of front layers when the moment
  is about them. The framing that does it: front-layer type in the duo band ends ≈ 40 px above the head top (read from
  the cut-out when it exists), or the word goes **behind** the head, or the beat moves sideways or to a wider shot; ink
  marks, chaos snippets, UI chips and floating panels sit beside the face; a card title stays clear of the face inside
  the card's own clip. When the moment wants otherwise (a subtitle crossing the chin of a low wide for a beat), that's
  editing; what's never fine is a head chopped or a face buried by accident. Behind the person is fair game, text
  included (`behind: true`). The geometry is in §3.7.
- **No text over text.** Never two duo titles at once; the subtitle hides under every z8 element (duo titles, the CTA
  keyword, the end block, the chaos burst); a duo never sits over the CTA keyword; at most three ink marks on screen;
  chaos snippets each keep their own spot.
- **On the word.** Each block keyword starts 2 f before its spoken word and is fully landed within ±5 f; counters land on
  the number word; ink marks start on the word naming the thing; a script connector writes on from its word's onset.
  Type follows words, cuts follow pictures: never cut inside a block's 4 f rise (move the cut up to 3 f). Audio is never
  offset.
- **Say what was said.** Every number shown as a fact (a counter, "#3", "52 weeks") is spoken or scripted, as digits.
  Illustrations (a recreated app screen, a search pill, a mock post) may use made-up but realistic numbers and names, no
  label. Before/after photos are the creator's real results: never simulate an "after". Never a fake UI, metric or
  follower count presented as real.
- **Promise integrity.** "N types / N rules / N steps" = N items shown with N markers; the thesis is paid off on screen
  before the CTA; the CTA keyword is readable ≥ 1.5 s.
- **Spelling.** Brand, place and tool names exactly as in the glossary; ".." only where the speaker actually pauses.
- **Readable.** Subtitles 54 px; display text ≥ 40 px; each duo beat reads in 1.2 s or less; text holds ≥ 0.25 s per
  word and every title ≥ 10 f after it completes. Yellow never sits on cream, white or greige (1.2:1): on light worlds
  the block is `ink`. A yellow block over a bright sky or a white wall that falls below 3:1 gets a 3 px `shade` stroke on
  that block only, or moves to the darker half of the frame.
- **Private data.** Screen recordings (SH-8) are checked for emails, phone numbers and account names, blurred for their
  whole time on screen.
- **Disclosure.** A sponsored reel shows "Paid partnership" for ≥ 2.0 s (or the whole sponsored span when the product is
  used on screen) and says it aloud.
- **No dead air.** Talking-piece pauses are tightened to 0.35 s except the speaker's deliberate ".." pauses (up to
  0.9 s), during which the picture keeps moving (a B-roll cut or a drift).
- **Audio and output.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 18 dB under the voice, a hard end ≤ 6 f
  after the last word on the bookend frame, no black tail. 1080 × 1920, 30 fps CFR.

**Never in this style:**
- Banner slabs; pills, boxes or highlights behind captions or titles (a UI chip is a UI object, not a caption); coloured
  words inside the subtitle; emoji in type.
- A second text accent: no red/green axis, no pink, no gradient on a keyword (the one gradient is the sign-off word,
  P-SIGNOFF-SUN).
- Yellow text directly on cream or white paper.
- Punch-ins outside the T-12 zoom-through, crash zooms, shakes, rotation snaps, RGB splits, resting light-leak PNGs,
  film burns, glitch packs. A new move is welcome when it's built in this style's language.
- Stock footage or generated scenes passed off as the creator's world; drone-look fakes made from stills.
- Meme sounds, stickers, stamps, emoji pops. Comedy here is staging and dry script asides, nothing else.
- A script connector carrying the keyword; a duo title over the CTA keyword.
- A chaos burst on a line that isn't about overload, or a second one in the reel.
- Raw full-bleed screen recordings: always inside P-APP-DEVICE or P-PHONE-REEL (a full-bleed UI close-up up to 1.5 s is
  fine only as a zoom inside the device).
- A fade to black or a black tail: the reel ends on the bookend picture.
- Sans-serif or ALL-CAPS subtitles; a subtitle anywhere but its band (§3.6).
- Meaning text in Instagram's bars: the top 110 px, below y 1540, or the right 110 px between y 900 and 1540.
- Decoration: a card, mark or word that doesn't show what is being said.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Formats
| | F-A "Vlog / story" (default) | F-B "Tutorial with paper cards" |
|---|---|---|
| When | A thesis told through places, staged personas or a personal journey: opinions, "N types of X", a visit, a year recap, a challenge | A how-to in 3–8 rules or steps: a technique, an app or tool walkthrough, a before/after fix |
| Layouts | L-full, L-card916, L-hidden | L-full, L-card916, L-card43, L-hidden |
| Default hook | HA-12 thesis typography (§6.2) | HA-05 title lockup, readable by 0.7 s (§6.3) |
| Structure | `story`, markers SM-1 "#N." | `tutorial`, markers SM-2 rule chapters |
| How it feels | Mostly footage, paper only when a line shows something | Paper carries the examples and the yellow ink marks them; the footage carries the creator applying each rule |

What makes them one style: the same yellow type layer (block plus script), the same pale-lemon serif subtitle at y 1468,
the same graded cinematic footage, the same cream paper world and the same bookend loop.

### 3.2 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-footage** | footage | The creator's graded cinematic footage, full-bleed (§4.3). Behind a smaller stage: a 28 px-blurred copy at 45 % brightness (pad 60) on `night` | Most of every reel: places, talking pieces, details, personas | Hard cut (T-1), cut on motion (T-2), blur-through (T-3) |
| **W-paper** | paper | Flat cream `#FCFBE6` (`cream`; measured paper `#FAF8E3`/`#FEFFE8`), noise 0.03, no grid, no vignette | 9:16 cards, 4:3 cards, phone reels, recap riffles, ink guides (v03 @ 0:11–0:27, v04 @ 0:19–0:55) | Hard cut with the card already placed (G-3) or G-1 shrink-to-card; out by a hard cut (measured v04 @0:27.9), T-6 fade only as an alternate |
| **W-grid** | paper | Greige `#E5E1D3` (`greige`) with a 64 px, 1 px grid (`grid` `#CFCBB6`, alpha 0.9), vignette 0.42, noise 0.04 | Polaroids, device frames, carousels, the series lockup (v02 @ 0:29–0:31, 0:45–0:50; v05 @ 0:09, 0:23–0:25, 0:30–0:54) | Hard cut; the polaroid flash (T-10) |
| **W-void** | void | Near-black `#050505` (`night`), noise 0.03, vignette 0.3; plain under the spin card (v03 @0:06.5 shows no dots); white dots at 10 %, 120 px pitch, r 2, only behind devices | The spin card's launch pad (v03 @ 0:06–0:09), dark device close-ups (v05 @ 0:32–0:51), the end block's fallback | Hard cut; T-4 spin out to full |
| **W-poster** | card-world | `accent` sun: a near-solid disc centred (540, 975), r 487, `#D42A05` at the centre to `#B50E05` at the edge, on a near-black `#0A0603`–`#270402` field, noise 0.03, vignette 0.35 (measured v02 @0:54.5) | The CTA and the sign-off silhouette (v02 @ 0:52–0:58) | Hard cut, or the T-11 warm flash. Usually drawn *behind the matted creator* (P-POSTER-BACKDROP) rather than as a stage world |

World colours come from `roles`; a creator's brand `accent` recolours W-poster. Light worlds (W-paper, W-grid) flip the
type to `ink` (§4.4).

### 3.3 Layouts
| ID | Engine | Footage / clip rect | Graphic rect | Caption |
|---|---|---|---|---|
| **L-full** | `full` | 0, 0, 1080 × 1920 | none: type goes in the sky, the wall or the top third | CS-1, cy 1468 |
| **L-card916** | `card` | x 192, y 160, w 696, h 1238, radius 40, crop 9:16, shadow 0.35, on W-paper | the card's top band x 192–888, y 160–460 (the burned title) | CS-1, cy 1468 (≈ 40 px under the card) |
| **L-card43** | `card` | x 72, y 494, w 936, h 702, radius 28, crop 4:3, shadow 0.25, on W-paper; guide lines (P-GUIDE-LINES) allowed inside | title band x 72–1008, y 200–460 | CS-1, cy 1468 |
| **L-hidden** | `hidden` | none: every pixel is a scene (paper cards from assets, polaroids, devices, the spin, the end block) | x 64–1016, y 110–1440 | CS-1, cy 1468 |

Scene-built frames (not stage layouts; they play `veos asset add` clips with `ctx.videoFrame`):
| Frame | Rect (at rest) | Used by |
|---|---|---|
| Paper card 9:16 | x 192, y 160, w 696, h 1238, radius 40 (measured v03 @0:11.5 x 189–891, y 183–1431; v04 @0:22 x 162–918, y 168–1479; set so the subtitle clears the card), shadow `0 18px 40px rgba(0,0,0,.18)` | P-PAPER-CARD, P-RECAP-RIFFLE, P-CARD-CAROUSEL |
| Polaroid | image 700 × 875 + 24 px `frame` border all round (outer 748 × 923), centre (540, 860), tilt −2.5…+2.5°, shadow `0 14px 30px rgba(0,0,0,.35)` | P-POLAROID, P-BEFORE-AFTER-POLAROID |
| Device | x 150, y 170, w 780, h 1270, radius 64, 22 px `#0E0E0E` bezel, shadow `0 30px 60px rgba(0,0,0,.45)` | P-APP-DEVICE |
| Phone reel | x 252, y 180, w 576, h 1250, radius 48 | P-PHONE-REEL |
| Spin card | 16:9, w 900, h 506, radius 28, launched from centre (540, 960) | P-SPIN-CARD |

**When to leave L-full.** Only on a line that *shows* something (an example, a recap, a rule, a screen, a photo); come
back to the footage on the next opinion or turn word ("but", "so", "and that's why"). Paper is proof, and proof is over
the moment the creator starts arguing again.

### 3.4 Stage moves
| ID | Move | Recipe (30 fps) | Use |
|---|---|---|---|
| **G-1** | Shrink-to-card | `stage: {layout: "L-card916", via: "shrink-to-card", dur: 12}`; the world switches to W-paper at the same t; the card title (P-PAPER-CARD) blur-slides in at f+8 | The footage becomes the example ("this is what I mean") |
| **G-2** | Grow-from-card | `via: "grow-from-card", dur: 10` back to L-full | Back to the story from an example |
| **G-3** | Paper cut | Hard cut (0 f) from L-full to L-hidden / L-card916 on W-paper with the card already at rest; the card's content keeps playing | The default way into paper (v03 @ 0:11) |
| **G-4** | Spin-to-vertical | P-SPIN-CARD (T-4): on plain black a playing 16:9 card turns 90° and grows until it covers the frame (2.5–4.5 s), then cuts | Opening a flashback, "the old way", a chapter (v03 @ 0:06–0:10) |
| **G-5** | Fade-through | `via: "fade-through", dur: 8` | Into and out of a device close-up |
| **G-6** | Depth sandwich | Not a move: a keyword drawn `behind: true` between the footage and the cut-out, drifting 8–12 px against the head | Behind-head words (P-BEHIND-WORD, P-BEHIND-LOCKUP) |

### 3.5 Layout diagrams
```
L-full (hook / thesis beat)                 L-card916 on W-paper
┌─────────────────────────┐ 0               ┌─────────────────────────┐ 0
│ (IG top UI, keep clear) │ ← 0–110          │                         │ ← 0–110 clear
│ script connector  y 250 │                  │ ╭─────────────────────╮ │ ← card y 160 (x 192–888)
│ BLOCK KEYWORD           │ ← duo band       │ │ CARD TITLE (yellow, │ │ ← burned title y 160–460
│ BLOCK KEYWORD           │   y 120–880      │ │ no stroke)          │ │
│        script  bottom-rt│                  │ │                     │ │
│                         │                  │ │   creator clip      │ │
│ (head top ≥ lockup      │                  │ │   (9:16, radius 40) │ │
│  bottom + 40 px, or the │                  │ │                     │ │
│  word goes behind it)   │                  │ ╰─────────────────────╯ │ ← card bottom 1398
│     presenter / place   │                  │   Lemon serif subtitle  │ ← cy 1468
│                         │                  │                         │
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

### 3.6 Safe zones and bands
- **Meaning-text box:** x 64–1016, y 110–1500 (`layout.safe`). The right column x > 970 between y 900 and 1540 stays
  empty (Instagram's buttons).
- **Duo band:** y 120–880, x 64–1016 (measured: v01 @0:02 blocks y 279–711, v05 @0:02.2 y 100–693, v02 @0:01.7
  y 300–865). The first block line's top sits at y 300 in the hook, y 230 mid-reel; script connectors at y 230–300 above
  it, or under the last block line + 16 px. The source's LOVING reached y 100, inside Instagram's top bar; keep ≥ 120.
- **Title band (HA-05 lockup):** y 230–410 on L-full (v03 @0:02.6 y 230–363, v04 @0:02.5 y 250–401); card titles inside
  the card's top 300 px.
- **Caption band:** centred at y 1468 on every layout, one line about 62 px tall (54 px × 1.15): y 1437–1499. The source
  sits at cy ≈ 1488 (glyphs y 1467–1510, v01 @0:12, v03 @0:02.6, v05 @0:30); it is lifted 20 px to stay above y 1500.
- **Counter band:** digits' top y 200–260; the unit stack directly under, ending by y 900.
- **Disclosure line:** x 64, y 128, 24 px (the sponsor's "Paid partnership" only).

### 3.7 The person
- **Where they are.** On L-full the creator is wherever the footage puts them: the head top sits at y 250–520 in a
  location talking piece (setup A), 420–700 on the seated set (B), 600–1100 in a wide or overhead (C), 560–800 in a
  headroom shot (D). In a card (L-card916, L-card43) they're inside the card's clip.
- **The head region** is the face, the hair and the room above the head, read from the cut-out when it exists (hair
  included), plus 40 px (`layout.face_clearance`). Keep front layers off it, captions included, unless the moment wants
  otherwise; judge it on the frame.
- **The duo band against the head.** Front-layer type keeps its bottom edge ≥ 40 px above the head top: a one-line beat
  (top y 330, 200 px) ends near y 520, so it needs a head top at y ≥ 560; a two-line beat ends near y 720 and needs
  ≥ 760. A higher head takes the word **behind** it (G-6), or the beat shifts sideways so its rect clears the head region,
  or the beat moves to a wider shot. Setup A and B heads are usually too high for a front two-line beat: that's what the
  depth sandwich is for.
- **The caption against the head.** The caption band (y 1437–1499) sits under the head in every setup: on a talking
  piece it's at chest height or below. In a wide where the person stands low (head top near y 1100), the chin still sits
  well above y 1437; if a shot ever puts the head inside y 1380–1500, pick another moment of the clip or another clip.
- **Behind the head.** Anton block words 200–340 px (or count-up digits), centred on the head's x ± 120 px, the top of
  the word 60–160 px above the head top, so that ≥ 65 % of the glyph area stays visible for the whole hold; the first and
  last letters always clear of the hair; one at a time; held ≥ 0.6 s; drifting 8–12 px against the head (parallax). It
  needs a clean matte (hair checked at 200 %); without one, the word goes above the head on the front layer (FB-11).
- **Cards.** The L-card916 card ends at y 1398 and the caption starts at 1437: 39 px of cream between them. A card's
  burned title (top band y 160–460) stays off the face in the card's clip: pick the clip moment or its `focus` so the
  head sits below y 500, else drop the title and let the subtitle carry the line.
- **How often they're there.** People came for this person's life: they're on screen often, sometimes small, sometimes
  just a pair of hands, and a B-roll run of a few seconds without the face is normal. Bring them back by a hard cut or a
  cut on motion to a talking piece on the opinion, the turn or the CTA, never mid-clause, and never by a morph out of
  paper except G-2. A persona scene with the creator in it counts as them being there.

---

## §4 Colour and the grades

### 4.1 Role palette
| Role | Hex | One job | Text on it / contrast |
|---|---|---|---|
| `primary` | `#F7DE0B` | **The** yellow: keyword blocks, behind-head words, counters, title lockups, card titles, ink arrows and ovals, the CTA keyword | `ink` 15.3:1 |
| `accent` | `#D42A05` | Poster backdrop only: the sun disc or colour wall behind the silhouette (P-POSTER-BACKDROP, P-SIGNOFF-SUN) | `ink` 4.9:1; `primary` on it 3.2:1 (display ≥ 96 px only) |
| `subtitle` | `#EEF272` | The pale-lemon serif subtitle | with its 1 px `shade` stroke and hard drop shadow it reads on any background |
| `paper` | `#FFFFFF` | White script connectors, guide lines, lasso outlines | — |
| `ink` | `#0B0B0B` | Keyword blocks and script on light worlds | on `cream` 18.8:1 |
| `shade` | `#1A1208` | Warm black for the subtitle's 1 px stroke and shadows (connectors and titles carry no stroke) | — |
| `cream` | `#FCFBE6` | W-paper | `ink` 18.8:1 |
| `greige` | `#E5E1D3` | W-grid | `ink` 15:1 |
| `grid` | `#CFCBB6` | The 1 px grid on W-grid | — |
| `frame` | `#F6F4EC` | The polaroid border | — |
| `gold` | `#9A6E0A` | The series lockup only (≥ 96 px) | on `greige` 3.5:1 |
| `night` | `#050505` | W-void | — |

Gradients (tokens `gradients`): `sun` `#FF8A2A` → `#E8401C` → `#7A0F06`; `soon` `#FFE400` → `#FFB21C` → `#F26A12` (the
sign-off word only); `teal_wall` `#1FA3C6` → `#0C7FA0` → `#06465A` (the cool colour wall behind a thesis poster, v02 @
0:39–0:40). A creator's brand colour can replace `primary` (any one saturated hue, nudged to ≥ 4.5:1 with ink) and
`accent`; it then changes everywhere.

### 4.2 Meanings
- **Yellow = the word to remember.** Only content words (nouns, numbers, the key verb, the CTA keyword) are yellow. A
  yellow arrow or oval means "look here".
- **White script = the connective tissue** of the sentence. Never a keyword, never a number.
- **Pale-lemon serif = the voice.** Every spoken word, quiet and constant.
- **Accent = the stage for the sign-off.** The poster is a closing gesture (and at most a thesis poster before it), so it
  feels like the end of a film, not wallpaper.
- **Grades = characters.** GR-mono, GR-amber and GR-teal tell personas or moods apart (§4.3).
- Brand colours appear only inside a logo chip (P-LOGO-CHIP); a logo's own colours never count as a style hue.
- Two bright roles in a frame at most: `primary`, plus `accent` only on a poster.

### 4.3 The grades
| ID | CSS filter stack | Look | Use | Evidence |
|---|---|---|---|---|
| **GR-warm** (footage default) | `sepia(0.12) saturate(1.08) contrast(1.04)`; tokens `grades.footage`: lift 0.02, warmth +0.08, saturation 1.06, bloom 0.08, vignette 0.12 | Warm teal-orange, golden skin, blue skies kept | Every creator clip unless a persona grade applies | v04 @ 0:00 (sky `#3E86C4`, warm skin) |
| **GR-mono** | `grayscale(1) contrast(1.18) brightness(0.92)` | Hard black and white | The negative or stuck persona, self-doubt, the "before" state, under the chaos burst | v02 @ 0:04–0:08, 0:32–0:36 |
| **GR-amber** | `sepia(0.45) saturate(1.35) hue-rotate(-10deg) contrast(1.06) brightness(0.96)` | Tungsten amber, deep shadows | The obsessive or collector persona, nostalgia, late night | v02 @ 0:09–0:17 |
| **GR-teal** | `sepia(0.35) hue-rotate(140deg) saturate(1.25) contrast(1.05)` | Cold teal-green | The shortcut or hacker persona, cold logic, "the algorithm" | v02 @ 0:18–0:23 |

**How grades behave.** A grade starts on a cut, never mid-shot, and lasts the whole persona or mood segment. A persona
keeps one grade for all its shots, and two consecutive personas never share one, so the viewer can tell them apart
without a label. The creator's own "answer" segment comes back to GR-warm (v02 shows a high-key white studio there).

**How they render.** Grades draw on the footage layer, under every graphic: the footage, the cut-out and the breakout all
take the same grade, so a behind-head word stays pure yellow inside a GR-mono span and the person matches the background.
- **Camera footage (talking pieces):** GR-warm is automatic (`tokens.grades.footage`). A persona span is a
  `timeline.grades[]` event from cut to cut, hard in and out: `{"t": 4.05, "t1": 8.02, "grade": "GR-mono", "fade": 0}`.
  When one scene already spans the whole segment, `grade: "GR-mono"` on that scene does the same (the footage takes the
  grade while the scene is on screen). A frozen B&W beat is an event with `"freeze": true`.
- **B-roll clips** are video assets and the engine leaves them natural, so each B-roll scene grades its own frame with
  `ctx.grade(...)`: the persona's id inside a persona span, the warm footage grade everywhere else (§12.6).
- No LUT packs. The only light effects are the flash transitions T-10 / T-11 (§9.1), never a resting overlay.

### 4.4 Rules
- Yellow never sits on cream, white or greige unless it's burned onto a photo inside a card. On W-paper and W-grid the
  keyword block and the script are `ink`, no stroke (v02 @ 0:28 "IT'S ALL", 0:38 "Hold you BACK").
- Script connectors are thin white monoline handwriting with **no stroke** (v05 @0:02.2 over water, v02 @0:54.5 over
  black) and only a faint `0 1px 4px rgba(0,0,0,.35)` shadow; on a bright sky move them to the darker side rather than
  outline them.
- Yellow blocks on footage carry **no shadow and no stroke** (v01 @0:02, v05 @0:02.2, v04 @0:02.5), except the 3 px
  `shade` stroke a block gets when it falls below 3:1 on a bright sky or a white wall (§2).
- Footage is graded only by §4.3.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family (bundled) | Weight | Class | Used for |
|---|---|---|---|---|
| `display` | **Anton** | 400 | condensed heavy caps | The duo keyword block, behind-head words, the CTA keyword |
| `wide` | **Montserrat** | 900 | wide ultra-heavy caps (measured: Montserrat 900 matches the source face's cap-height-to-width ratio within 5 %; Archivo Black is wider) | Title lockup, card titles, the end block, the echo outline, the series block, the counter's unit |
| `numeric` | **Montserrat** | 900 | wide ultra-heavy caps | Count-up digits |
| `script` | **Nanum Pen Script** | 400 | thin pen handwriting | Duo connectors, script asides, the series script |
| `serif` | **EB Garamond** | 600 (subtitle), 500 (markers, chaos phrases) | old-style serif | Subtitles (CS-1), "#N." markers, chaos phrase fragments (italic) |
| `ui` / `body` | **Jost** | 500–700 | geometric sans | UI chips, chaos bracket tags, the logo-plate wordmark, the disclosure line, created UI text |
| `marker` | **Pinyon Script** | 400 | thin calligraphic script | The calligraphic option for a connector or a series name (v02 @ 0:14–0:16 "doesn't care about", 0:57 "See you in there"); rare ink note labels |
| `mono` | JetBrains Mono | 400 | mono | Code-shaped texture only |

Brand wordmarks and series logos are image assets, not fonts.

### 5.2 The headline element: the duo title (`kind: "lockup"`)
The duo title is how this style speaks. It isn't a caption and it isn't a banner: it's the spoken sentence turned into a
poster word by word, the keywords huge and yellow, the joining words small and handwritten. It's for the moments that
deserve a title: the hook, a thesis line, a persona's name, the turn, the CTA. Between those, the subtitle carries the
voice alone.

| Property | Spec |
|---|---|
| Block (keyword) | Anton 400, caps, `primary` `#F7DE0B`, **180–340 px**, line height 0.88, tracking −1 %, **no shadow**; each line is **size-fitted to span ≈ 860–900 px** (x ≈ 96–984), so a short word gets huge and a long line gets smaller (measured: v01 @0:02 SHOPPING 247 px / cap 211; v05 @0:02.2 LOVING ≈ 335 px / cap 308, THE PICTURES ≈ 180 px). Up to 3 words per line, 2 block lines; a lockup is ≤ 7 words in all (3 lines with the script) |
| Script (connectors) | Nanum Pen Script 400, as spoken, `paper`, **84–112 px** (default 100; v02 @0:54.5 "Just comment" 542 px wide, glyphs 73 px tall), no stroke, faint shadow `0 1px 4px rgba(0,0,0,.35)` |
| Placement | **Above-left** of the block (script baseline 12–20 px above the block's top, x = block left + 8) for leading connectors; **below-right** (top = block bottom + 16, right-aligned to the block) for trailing ones. **Corners variant** (P-DUO-CORNERS): leading words at (96, 250) and (984, 250, right-aligned), trailing words at the block's bottom corners |
| Block entry | **Rise-smear** (measured v01 @0:00.59–0:00.72, `strip-hook-duo-blurslide.jpg`): the word rises from **y + 0.8 × cap height (≈ 150–220 px; tokens 180)** to rest with a **vertical** motion smear (24 → 0 px, along y only) and opacity 0 → 1 over **4 f** (3 f at the source's 24 fps: +150 → +72 → 0 px), expo-out; starts 2 f before the word |
| Script entry | **Write-on:** a left-to-right clip mask over **8 f**, linear, from the word's onset (v01 "when it comes to what" ≈ 0.30–0.47 s) |
| Hold | 0.4–0.6 s per single-word beat; a full two-line lockup holds ≥ 10 f after its last word lands; each beat reads in 1.2 s or less |
| Exit | **Rise-out:** up ≈ 130 px (measured −35 then −110 px), vertical smear 0 → 24, opacity 1 → 0 over **4 f** (3 f measured at 24 fps), ease-in; words leave **last-in first, 1 f apart** (v01 WEAR leaves 1 f before YOU). The script **un-writes right to left** in 4 f (v01 @0:00.93–1.05); it never slides. The next beat may start 3–5 f after the exit ends (a short empty beat is part of the rhythm, v01 @ 0:01.17) |
| Exit at a cut | The hook's last lockup is **not** animated out: it holds and leaves with the shot on the hard cut (v01 @0:03.99 "IS WAY BETTER" → the walk-in; the subtitle starts on the cut) |
| Exit inside the chaos burst | The duo blurs out **in place** (blur 0 → 16 px, no travel, 3 f; v02 @0:06.67 "to be PERFECT") |
| Join | A second block word on the same line rises in on its own word while the first holds (v01 "YOU" → "YOU WEAR") |
| Replace | A new beat replaces the whole block (out, then in) when the next keyword starts a new idea |
| Frame 0 | In HA-12 nothing is fully visible on f0: the first connector starts writing at f0 (0 % revealed), or the first block lands at 0.4–0.7 s. The first type beat starts by 0.7 s |
| Lifetime | `section`: the hook (2.5–4.0 s), a thesis re-hook, a persona label, the CTA |
| Light worlds | On W-paper and W-grid the block and the script are `ink`, no stroke |
| Layer | z8; the subtitle hides while a duo is up; never two duo titles at once |

**The duo split.** Keywords are nouns, numbers, names, the main verb or adjective of the claim; connectors are articles,
pronouns, prepositions, auxiliaries, conjunctions. "When it comes to what **YOU WEAR** / **SHOPPING IN PERSON** / **IS WAY
BETTER** than online." Never two keywords in the script; never a connector in the block, except a pronoun the block needs
to make sense ("**YOU** WEAR").

**Scene recipe (one scene per beat; the helpers are shared by every duo scene):**
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
  const deco = block ? "text-transform:uppercase;letter-spacing:-0.01em;"            // no stroke, no shadow
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
Declare every landing and the exit in `events` (they're the on-the-word anchors). Take `at` values from
`words.edit.json` (word onset − `t_in`). A behind-head word is the same scene with `behind: true`.

### 5.3 Caption profile CS-1: the pale-lemon serif
| Group | CS-1 (extends `lib:omgadrian`) |
|---|---|
| Mode | `full` / `support` / `mute_safe`: on every spoken word, but the type layer and the picture are the strongest things on screen |
| Chunking | unit `phrase`; **3–6 words** (mean 4); max 28 characters; **1 line**; never split a name, number or unit; a new chunk on `. , ? !` and on any pause ≥ 0.9 s |
| Timing | lead 2 f; hold ≥ 0.25 s per word; tail 0.12 s; swap **hard** (0 f); no pause hold |
| Skin | slot `serif` (EB Garamond) **600**, **54 px**, sentence case as spoken, tracking 0, line height 1.15, colour `subtitle` **pale lemon `#EEF272`** (measured glyph cores `#EDF36A`–`#EFF079`, v01 @0:12, v03 @0:02.6), a 1 px `shade` stroke, a **hard drop shadow `2px 3px 2px rgba(0,0,0,.85)`** (down-right, v03 @0:11.5 on cream), no container |
| Position | `fixed_y`, **cy 1468**, centred, max width 952, on every layout (L-card916 leaves ≈ 40 px under the card); no colour flip: the hard shadow keeps it readable on cream |
| Speakers | one skin (a second person on camera keeps it) |
| Emphasis | `none`: the subtitle never highlights; the duo title does that job |
| Hide | under every z8 element (duo titles, the CTA keyword, the end block, the chaos burst), and during a morph |
| Language | Latin script; keep English terms verbatim; don't normalise spelling; profanity masked inside (`S**T`); the glossary = the creator's brand, place and tool names; keep ".." on the speaker's in-sentence pauses (v04 "I made a post..") |

Measured at full resolution, the source's serif fits **47–48 px** at 1080 (v01 @0:12 "because nothing is worse" 470 px
wide; v03 @0:02.6 582 px). The style sets **54 px** so it meets the readability floor; 54–62 is the comfortable range.

### 5.4 Other text
| System | Class | Recipe | Hold |
|---|---|---|---|
| **Title lockup** (HA-05, P-TITLE-LOCKUP) | `TC-display` | Montserrat 900 caps **80–108 px**, `primary` (v03/v04 use a lemon `#FBF434`, an option), **no stroke, no shadow**, tracking −2 %, line height 0.92, centred, each line size-fitted to 860–980 px wide (line 2 often smaller: v04 @0:02.5 cap 79 then 62 px), y 230–410, up to 6 words on 2 lines. **Squash-in** (measured v03 @0:00.39–0:00.52, `strip-title-squash-in.jpg`): each line opens from a thin bar (scaleY 0.05 → 1 about the line's centre, a slight vertical smear `filter:${ctx.blur(px, 90)}`) in **3 f**, line 2 starts **2 f** after line 1; no rule (the "dashed rule" on the 6 fps sheet was line 1 at scaleY ≈ 0.05) | 2.0–4.0 s, then leaves with the shot on a cut, or blur-out 4 f |
| **Card title** (burned on a paper card's photo) | `TC-display` | Montserrat 900 caps 64–84 px, `primary`, line height 0.95, no stroke, x card + 40, y card + 40, up to 3 lines and 5 words (v03 @0:11.5, v04 @0:22) | the card's life |
| **Counter** (P-COUNT-UP) | `TC-display` | Montserrat 900 280–400 px `primary`, centred x 540, top y 220; digits **append** left to right (3 → 36 → 365), one per spoken beat or every 6 f; unit word(s) Montserrat 900 90–120 px stacked under, line height 0.9 | ≥ 1.0 s after the last digit |
| **Echo outline** (P-ECHO-OUTLINE) | `TC-display` | The phrase twice in Montserrat 900 120–170 px: filled `primary`, then outline-only (3 px `primary` stroke, transparent fill), stacked as 4 lines over the presenter, clear of the head region | 0.8–1.2 s |
| **Hash marker** (SM-1) | `TC-label` | "#1." EB Garamond 500, 54 px, `subtitle` with the subtitle's shadow, centred at y 1468 **in place of** the subtitle | 0.5–0.8 s |
| **Script aside** (P-SCRIPT-ASIDE) | `TC-display` | Nanum Pen Script 84–112 px `paper`, no stroke, alone, top band y 230–420, written on in 8 f | 1.0–2.0 s |
| **UI chip** (P-UI-CHIP) | `TC-label` | Jost 600 44 px `ink` on a white pill (radius 999, padding 18/34, shadow `0 8px 24px rgba(0,0,0,.25)`) with a 36 px search glyph; or a `primary` pill with `ink` caps text ("BUY NOW") | 1.0–2.0 s |
| **Chaos tag / phrase** (P-CHAOS-BURST) | `TC-label` | Tags "[Close Up]" Jost 500 44–64 px `paper` at 85 %; phrases EB Garamond italic 500, 48–72 px `paper`; all with `0 2px 8px rgba(0,0,0,.6)` | inside the burst |
| **End block** (P-END-BLOCK) | `TC-display` | Montserrat 900 caps, 4–7 lines, each line sized to fill x 64–1016 (70–200 px), line height 0.9, `primary`, y 220–1360 | 2.5–4.0 s |
| **Series lockup** (P-SERIES-LOCKUP) | `TC-display` | The script name 120–160 px `gold` (slot `script`; Pinyon Script from `marker` when a calligraphic name suits it, as the source's "Boyfriend") over a Montserrat 900 block 130–170 px `gold`, "ep. NN" Jost 600 40 px `gold` under it, centred at y 900 on W-grid with the grid off | 1.2 s |
| **Logo word** (P-LOGO-CHIP) | `TC-label` | "With" script 60 px + the logo (the creator's file, 88 px tall) + the wordmark Jost 500 72 px `paper` | 1.0–1.5 s |
| **Disclosure line** (P-DISCLOSURE) | legal | Jost 500 24 px, `paper` at 85 % on footage / `ink` at 70 % on paper, x 64, y 128 | ≥ 2.0 s, or the whole sponsored segment |

### 5.5 Language and numbers
- Spelling: brand, place and tool names exactly as in the glossary; English words exact inside Hinglish captions.
- Numbers on screen are digits, as spoken ("365", "52", "#3"); international grouping by default; Indian grouping and ₹
  when the creator speaks an Indian language.
- Caps: the block, titles and the end block are ALL CAPS (Latin only). The subtitle is sentence case.
- **Devanagari** (Hindi captions): the subtitle falls back to Noto Sans Devanagari 500 (no serif exists); duo titles,
  titles and counters stay Latin (English keywords), because Anton and Montserrat have no Devanagari. Script connectors
  in a Devanagari reel become Noto Sans Devanagari 400 at 60 px.
- Hinglish captions: romanised as spoken; keyword blocks use the English keyword when one is spoken, else the romanised
  word.

---

## §6 Hook system

**The hook title.** In this style the hook title *is* the thesis, built on screen word by word as it's spoken, so the
first sentence the creator says has to be a promise: a thesis the viewer wants to argue with, a question about them
("Is your **GIRLFRIEND** still **LOVING THE PICTURES** you got of her?"), a count that promises a list. Find the
strongest such line in the take and open on it; if the take has none, open with an HA-05 title lockup that promises the
outcome ("How to X as a Y", "Why your X isn't working", "The X nobody tells you", "Stop doing X", a number or a
contrast), which need not repeat the spoken words but must be true to what the reel delivers. Write 8–10 candidates
(thesis splits or lockups), score them on outcome, curiosity, who it's for and brevity, pick the best by the stopper
test, and keep the next two as alternates. The post title follows the same rules.

### 6.1 The stopper test
| Test | In this style |
|---|---|
| Mute | The first 3 s tell the thesis without sound: the duo beats carry the whole sentence |
| Motion at f0 | Live footage in motion, a walk-in, a drone move, or Z-1 push-drift starting at f0; never a static frame or a fade-in |
| Read time | Each beat reads in 1.2 s or less (up to 3 block words + up to 5 script words) |
| Payoff by | HA-12: the whole thesis on screen by 3.0 s; HA-05: the title readable by 0.7 s; HA-19: the premise by 3.0 s; HA-08: the hero number by 1.7 s |
| Thumbnail | Not for HA-12 (f0 is image-only by design); for HA-05, HA-19 and HA-08 the title, word or number reads at 25 % scale (≥ 16 px cap height) |

### 6.2 HA-12 Thesis typography (default)
The thesis or question is split into 3–4 typographic beats over one moving cinematic first shot (SH-1). No banner, no
result. The hook is the densest stretch of the reel: a connector writing, a block rising, a word joining, the line
leaving, the next one building, each landing while the last one settles, all over one shot that keeps moving.

| t (s) | Frames | Beat | Picture (SH-1) | Type layer | Subtitle | Camera | Cue moment |
|---|---|---|---|---|---|---|---|
| **f0** | 0 | Stopper | A composed moving shot: frame-in-frame (mirror, door, window), overhead or drone, or the creator walking in; presenter visible or entering | Nothing fully visible; connector 1 starts writing (0 %) | hidden | Z-1 push-drift from f0 if the shot itself is static | hook (soft) |
| 0.00–0.33 | 0–10 | Connector 1 | same shot | Script connector(s) write on L→R in 8 f at (72, 220), 100 px | — | — | — |
| 0.40–0.70 | 12–21 | Keyword 1 | same | Block word 1 rises in (4 f) at x 64, top y 330, 200 px | — | — | — |
| 0.70–1.00 | 21–30 | Join | same | Block word 2 joins on its word (same line), or connector 2 writes | — | — | — |
| 1.00–1.30 | 30–39 | Swap | same (the shot keeps moving) | The block rises out (4 f); up to 5 f empty | — | — | — |
| 1.30–2.00 | 39–60 | Keyword 2 | same | The next keyword(s) build line 1, then line 2 | — | — | — |
| 2.00–2.30 | 60–69 | Hold → out | same | The full lockup holds ≥ 10 f, then rises out | — | — | — |
| 2.30–2.90 | 69–87 | Keyword 3 + close | same | The last block + the closing connector below-right ("than online") | — | — | — |
| 2.70–4.00 | 81–120 | First cut | **T-2 cut on motion** to the first talking piece or B-roll | The lockup holds and leaves with the shot on the cut (v01 @0:03.99) | **CS-1 starts** on the first post-hook word | — | transition |

The whole thesis has been on screen by **3.0 s**. Evidence: v01 @ 0:00–0:04 (mirror, "When it comes to what YOU WEAR /
SHOPPING IN PERSON / IS WAY BETTER than online"), v05 @ 0:00–0:02.7 (overhead couple, P-DUO-CORNERS), v02 @ 0:00–0:02.7
(seated, "3 types of CONTENT creators", the block partly behind the cap).

### 6.3 Alternate hooks
**HA-05 Title lockup** (F-B default; v03, v04)
| t (s) | Picture | Type | Subtitle |
|---|---|---|---|
| f0 | SH-2 overhead or SH-3 walk-in: the creator enters the frame | — | hidden |
| 0.38 | same | Line 1 squash-in starts (a thin yellow bar, 3 f) | — |
| 0.43–0.55 | same | Line 1 then line 2 squash in (3 f each, 2 f stagger): readable by 0.55 s | — |
| 0.8–4.0 | the creator settles (leans on the car, sits, looks up) | The title holds | CS-1 from the first word (≈ 0.8 s) |
| 2.9–4.0 | cut on motion | The title blurs out on the cut | continues |

For example: "FIX YOUR SQUAT / IN THREE CUES".

**HA-19 Mood montage** (F-A, atmospheric openers)
| t (s) | Picture | Type |
|---|---|---|
| f0 | SH-4 cinematic detail in motion | One block word (Anton 230 px) rises in from f0 (its scene starts at 0; landed by 4 f) |
| 0.9 | cut on motion to clip 2 | Word 2 replaces word 1 |
| 1.8 | clip 3 | Word 3 |
| 2.5–3.0 | talking piece | A closing script line; the premise is complete by 3.0 s |

For example: "RAIN. / RAMEN. / RESET." over three Tokyo details.

**HA-08 Count hook** (milestones and challenges; v04 @ 0:03, v02 @ 0:00.67)
| t (s) | Picture | Type |
|---|---|---|
| f0 | SH-11 matted headroom shot, the creator mid-gesture | — |
| 0.3–1.7 | same | P-COUNT-UP behind the head (`behind: true`): digits append on each spoken beat ("3 … 36 … 365"), landed by 1.7 s |
| 1.7–2.6 | same | The unit stacks under in 100 px ("DAYS STRAIGHT") |
| 2.7 | cut on motion | — |

For example: "52 CITIES / ONE BACKPACK".

### 6.4 Hook pairs by topic (thesis → the scene that carries it)
| Topic | Thesis (duo split: **BLOCK** / script) | The scene that carries it | Paid off by |
|---|---|---|---|
| Fitness: training alone | "Training **ALONE** is why you **STOPPED** at week three" | Overhead of an empty gym floor, the creator walks in (SH-2 / SH-3) | The coach's correction in a 4:3 card with ink arrows |
| Fitness: mornings | "Your **MORNING** decides your **WORKOUT**" | Mirror shot, laces being tied (SH-1) | The bookend: the same mirror at the end |
| Fitness: personas | "**3** types of **GYM** people" | Seated set, three fingers raised, cut on the hand (SH-5) | Three persona scenes graded GR-mono / GR-amber / GR-teal |
| Travel: homestays | "I **STOPPED** booking **HOTELS**. **THIS** happened" | A walk-in through a homestay door (SH-1 frame-in-frame) | A polaroid of the host family's kitchen (P-POLAROID) |
| Travel: street food | "The best **FOOD** in this city has **NO MENU**" | Overhead of a hawker stall (SH-2) | A detail run of five dishes (P-DETAIL-RUN) |
| Travel: phone photos | "Is your **PHONE** still taking **BORING** travel photos?" | Overhead of the creator at a railing (SH-2), corners layout | A before/after polaroid (P-BEFORE-AFTER-POLAROID) |

### 6.5 Headline writing
- **Duo thesis formula:** `[script lead-in] + BLOCK KEYWORD + [script bridge] + BLOCK KEYWORD(S) + [script close]`, up to
  12 words spoken, up to 7 per on-screen lockup, 3–4 beats. A question is welcome ("Is your … ?").
- **Title lockup formula (HA-05):** `VERB + OBJECT` or `TOPIC + PROMISE`, up to 6 words on 2 lines ("CINEMATIC
  VERTICAL / VIDEO COMPOSITION", "THIS DECISION / CHANGED MY LIFE").
- Case: blocks and titles ALL CAPS; script as spoken.
- Write 8–10, pick by the stopper test (§6.1), keep two alternates.
- **Banned:** emoji, hashtags inside titles, "game changer", "you won't believe", a count that doesn't match the reel, a
  keyword the reel never pays off.

### 6.6 Hook sound
The music bed runs from f0. One soft cue may mark the first keyword landing and a transition cue the first cut (§11).

### 6.7 CTA, sponsor and end cards
| Device | Spoken pattern | On screen | Hold | Where |
|---|---|---|---|---|
| `comment_keyword` | "Just comment KEYWORD to get …" | **P-CTA-KEYWORD**: script "Just comment" at (72, 236) + **KEYWORD** Anton 230 px `primary` at y 300 + script "to get it" below-right; over P-POSTER-BACKDROP (the `accent` sun behind the matted creator) or plain footage; scene `kind: "cta-keyword"` | ≥ 2.0 s (the keyword readable ≥ 1.5 s) | The last 6–10 s, before the bookend |
| `link_bio` | "Link in my bio for …" | **P-END-BLOCK**, 4–6 lines ending "LINK IN BIO", over SH-13 texture | 2.5–4.0 s | The end, before the bookend |
| `end_card` | "This was part 1 …" | P-END-BLOCK with the series line ("THIS WAS PART 1 / FOLLOW FOR PART 2") | 2.5–4.0 s | The end, before the bookend |
| `post_only` | A spoken sign-off ("Peace.", "Take notes.") | The subtitle only, over the bookend shot | — | The last 1.0–1.5 s |

Leave 0.3–0.5 s without new type before the CTA keyword lands, so it arrives into air. The CTA is confident and clean: no
chaos, no comedy. After it, the bookend (§7.6) carries the last spoken words.

- **Sponsor (logo chip, P-LOGO-CHIP):** "With" in script (60 px) + the brand's logo file (88 px tall, its own colours) +
  the wordmark in Jost 500 72 px `paper`, top band y 380–470, on the word naming the brand; 1.0–1.5 s. Without a logo
  file, the real logo fetched from the brand's site; `fx.logoPlate` sets the name in type only when none can be found.
  Clear of the face, never over the CTA keyword, never inside the hook's first 3 s.
- **Disclosure (P-DISCLOSURE):** "Paid partnership" (Jost 500 24 px) at (64, 128) from the first sponsored beat for
  ≥ 2.0 s, or for the whole sponsored span when the product is used on screen, plus a spoken mention.
- **End cards:** P-END-BLOCK (`link_bio`, `end_card`): 4–7 lines of yellow Montserrat 900 filling the width over a texture
  close-up (SH-13, else W-void), 2.5–4.0 s, the keyword or URL line readable ≥ 1.5 s, then the bookend. Never longer than
  4 s; no subscribe buttons, no follow stacks, no QR codes; the bookend is always the last picture.

---

## §7 Structure and rhythm

### 7.1 Structure
| Format | Type | Arc |
|---|---|---|
| F-A | `story` | **HOOK** 2.5–4.0 s (HA-12) → **SETUP** (where we are, why it matters) → **SCENE-n**, 2–5 scenes or personas → **TURN** ("but…", "then it changed", the realisation; carries the re-hook) → **PAYOFF** (the thesis proven, the answer) → **CTA** → **BOOKEND** 1.0–1.5 s |
| F-B | `tutorial` | **HOOK** 3.0–4.0 s (HA-05) → **CONTEXT** (why it matters; one spin card allowed) → **RULE-n**, 3–8 rules → **RESULT** (before/after) → **CTA** → **BOOKEND** 1.0–1.5 s |

Section lengths follow the speech. A scene lasts as long as its place or persona has something new to show; a rule lasts
its example and its demonstration.

### 7.2 Markers
| ID | Marker | Recipe | Used in |
|---|---|---|---|
| **SM-1** | Hash marker | "#1." EB Garamond 500, 54 px in the caption band, replacing the subtitle for 0.5–0.8 s, on the ordinal word or the cut into the item (v02 @ 0:03, 0:08) | F-A lists of types or reasons |
| **SM-2** | Rule chapter | The rule's name as a title on W-paper: `ink` Montserrat 900 64 px at y 230, above the example card; or burned on the first example card's photo in `primary` | F-B, every rule |
| **SM-3** | Series lockup | P-SERIES-LOCKUP once, right after the hook (§7.7) | Series reels |
| — | Spoken only | No marker | F-A pure stories (v01, v04) |

One marker style in a reel; numbering ascending.

### 7.3 The unit rituals
**F-A scene or persona ritual (the same for every item):**
1. **0 f** cut (T-1 or T-2) to the item's establishing shot (a wide, 1.0–1.5 s); a persona's grade starts on this cut;
   SM-1 "#N." for 15–24 f.
2. **On the name word:** a persona label duo (script "The" + BLOCK NAME, z8), held 0.6–1.0 s; for a place, the place
   name as a card title.
3. **2–4 action shots** of 0.8–1.5 s each, one per noun or verb in the description, CS-1 running.
4. **One support visual** on the item's defining habit: a UI chip, a floating panel, a phone reel, or a behind-head word.
5. **The punch line** as a duo (script + block on the punch word, "They care **STORY**") or a script aside.

**F-B rule ritual (the same for every rule):**
1. **On the rule's ordinal or name word:** G-3 paper cut to W-paper; the SM-2 rule title rises in (4 f) at y 230.
2. **f+8:** the example card (L-card43 or a 9:16 paper card) is already at rest; its clip plays.
3. **On the word naming the feature:** P-GUIDE-LINES draw (10 f), then P-INK-ARROWS or P-INK-OVAL (10 f); three marks
   at most.
4. **After 1.5–3.0 s on paper:** hard cut to a demonstration clip (the creator applying the rule on location, 2–4 s) or
   the talking piece.
5. **A second case (when the rule names two):** a second example slides in (P-CARD-CAROUSEL, T-5).

### 7.4 Open loops and the re-hook
- **Loops:** the thesis loop (asked in the hook, answered in PAYOFF); the count loop ("3 types" → exactly 3 items); the
  result loop (F-B: "by the end…" → the after polaroid); the bookend loop (visual, §7.6).
- **Every loop closes on screen before the CTA.**
- **The re-hook is the turn.** Near the middle of the reel, the thesis keyword comes back as a duo title (v04 @ 0:13
  "CHANGED / MY LIFE"), a count-up, or the "BUT…" duo. Tag that beat `rehook: true`. A long reel (well past a minute and
  a half) earns a second one late, so no stretch goes long without a reason to stay.
- The hook (and the series lockup, when there is one) is over fast, so the first scene arrives while the promise is
  fresh.

### 7.5 Rhythm by feel
- **The curve is cinematic and flat, with peaks.** The hook peaks: type beats every few frames over one moving shot.
  The setup breathes: an awe shot, a second or two with no type, just the place and the voice. The scenes alternate
  places and personas. The turn dips: a slow push, one script aside, the quietest moment. The payoff peaks again: a
  count-up, a polaroid flash, a word behind the head. The CTA is confident (the poster), and the bookend is calm.
- **The picture never sits still, but it is never random.** In B-roll runs a new shot arrives with each new idea, each
  listed noun, each turn of the head; cuts hide inside motion (a step, a turn, a whip). A talking piece runs as long as
  the thought, then a cutaway shows what it's about. A single shot may hold for a few seconds only when it earns it: the
  hook's moving opener, a slow-push confession, the CTA poster, the end. And it never holds still: Z-2 or the subject
  moves, and a duo or a typed line is on it.
- **Travel.** In F-A the location changes often enough that the reel feels like a journey: a new place, set or persona
  whenever the story moves on.
- **Type is punctuation, not wallpaper.** The duo title is for the lines that deserve a title; most of the reel is
  footage and the quiet serif. A behind-head word is a moment of depth for the keyword that most deserves it, so it
  stays rare enough to feel special. Paper is proof: an F-A reel visits it when a line shows something; an F-B reel
  lives there for its examples.
- **Light comedy.** A deadpan beat comes back often enough that the reel never feels like a lecture: a persona's
  exaggerated habit, a staged reaction, a dry script aside ("…riveting"). Never two comedy beats back to back; never in
  the CTA or the hook's first 2 s.
- **The last item escalates:** the biggest scene, a word behind the head, or the poster.
- For reference, measured on the five reels (a description, not a target): 26.7–51.3 cuts a minute (v01 51.3, v02 37.9,
  v05 39.1, v03 28.2, v04 26.7; F-B runs about 27–42), median shot 0.87–1.59 s (full-rate re-measure 0.67–1.79 s, pooled
  1.04 s, p90 3.2 s), 4.8–8.4 picture changes per ten seconds, longest single holds 4.0–6.8 s (the v01 hook mirror, a
  v04 slow push, the v02 CTA poster, the v03 and v04 ends).

### 7.6 The bookend loop
The reel ends on the exact picture it opened with, so the last frame flows into the first and the reel plays again
(v01 @ 1:23 = @ 0:00; v05 @ 1:01 returns to the opening railing). It's on by default; a reel that doesn't loop says so in
its plan.
1. SH-1 plays at f0 as a picture-only scene from source time `s0` (asset `B01`, `offset: s0`).
2. The BOOKEND scene plays the same asset with `offset: s0 − d` (`d` = 1.0–1.5 s) and lasts `d + 1/30` s to the reel's
   end, so its last rendered frame is source frame `s0`: the picture of f0.
3. No type is fully visible on frame 0 or on the last frame; the subtitle of the last words hides 4 f before the end
   (`captions.overrides` hide `[end − 0.13, end]`).
4. The last spoken sentence (the sign-off, or the end of the CTA) rides the bookend; the hard end is ≤ 6 f after the last
   word.
- **Walk-in / walk-out** (SH-3): when it exists, the creator enters the opening frame within 0.5 s and leaves the closing
  frame in its last 1.5 s; the bookend then plays the empty plate (v04 @ 0:00, 1:23).
- **Short pre-roll** (SH-1 has less than 1.0 s before its in-point): the bookend holds SH-1 frozen on source frame `s0`
  for its last 0.5–1.0 s, after the reel's last talking shot; the final frame still equals f0.
- **Check it by eye:** put the last frame next to f0 in the stills; the pictures must match.

### 7.7 Series furniture
- **Series lockup (P-SERIES-LOCKUP):** on W-grid with the grid off and vignette 0.42; the script name (120–160 px, 140
  default, `gold`) overlapping the top of a block word (Montserrat 900 130–170 px, 150 default, `gold`), "ep. NN" (Jost
  600 40 px `gold`) centred under it; centred on y 900. The creator's own series logo file replaces the type when
  they have one.
- **Placement:** directly after the hook, starting at 5–9 s; holds 1.2 s; enters by a cut, the script writes 10 f, the
  block rises in 4 f; leaves by a cut. Tag format "ep. {n}"; the name and number come from the reel's brief.
- No persistent series tag, no progress dots.

---

## §8 Visual system: B-roll and patterns

### 8.1 The role of graphics
- **Footage carries the story; type, paper and ink illustrate it.** They never carry the argument alone. Most of the
  craft here is choosing and cutting the creator's footage; the patterns below are the vocabulary around it.
- **Numbers become pictures.** Every spoken count is a P-COUNT-UP or a counted visual (one detail shot per item), never a
  number only in the subtitle.
- **Variety comes from the moment.** Places, details, personas, paper and type take turns because the words ask for
  them; the F-B rule ritual and the recap riffle are the deliberate repeats.

### 8.2 Families
| ID | Family | Source | The creator supplies |
|---|---|---|---|
| **B-1** | Duo type (script + block) | engine | — |
| **B-2** | Behind-head type | engine + cut-out | matted takes with headroom (SH-11) |
| **B-3** | Kinetic lockups (title, counter, echo, end block, marker) | engine | — |
| **B-4** | Paper cards (9:16, 4:3, riffles, carousels, spin) | engine frame + the creator's clips | the clips inside (SH-4, SH-10) |
| **B-5** | Polaroids on grid paper | engine frame + the creator's photos | photos and stills (SH-9, SH-4) |
| **B-6** | Devices and UI (app device, phone reel, chips, panels) | the creator's screen recordings; else the real app or page captured from the web; else a created generic UI | screen recordings (SH-8) |
| **B-7** | Ink and guides | engine | — |
| **B-8** | Graded persona scenes | the creator's footage + the grade | staged scenes (SH-6) |
| **B-9** | Poster / silhouette | engine backdrop + cut-out | a profile take with back light (SH-12) |
| **B-10** | Chaos burst | engine over the creator's footage | — |
| **B-11** | Brand and series | the creator's logo files; else the real logo fetched from the web; a type-set logo plate only when none can be found | logo PNG/SVG, series logo (optional) |
| **B-12** | Location B-roll and shot devices | the creator's | SH-1…SH-7 |
| **B-13** | Third-party references | the creator's files (another creator's reel, an artwork, a product page); else the real one fetched from the web, source noted; else rebuilt from its exact text (quote card, recreated UI, silhouette) | what they have; the rest is fetched |

### 8.3 Pattern specs
Frames at 30 fps. "Lands" = fully in. Every text scene sets `text_class`.

**Type and titles (B-1, B-2, B-3)**
| ID | Name | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|---|
| **P-DUO-TITLE** | Duo title | overlay | Script connectors + the yellow Anton block, 1–2 block words per beat, up to 2 block lines | Block rises in 4 f (lead 2 f), holds 0.4–0.6 s, rises out 4 f; the script writes on in 8 f | The hook, thesis lines, persona labels, the turn | `TC-display`, z8, `kind: "lockup"` |
| **P-DUO-CORNERS** | Corner duo | overlay | The block centred in the top band; leading script words in the two top corners, trailing words at the block's bottom corners | Corner words write on in sequence (8 f each, 4 f apart); the block as P-DUO-TITLE | A question hook over a symmetric wide (the v05 hook) | `TC-display`, z8 |
| **P-WORD-RELAY** | Word relay | overlay | One block line whose words arrive one per spoken word and leave together | Each word rises in on its onset; the line leaves as one (4 f) | A thesis spoken fast (v01 "SHOPPING / IN / PERSON") | `TC-display`, z8 |
| **P-DUO-STACK** | Duo stack | overlay | Two block lines (line 1 230 px, line 2 150–170 px) + one script line under them | Line 1 in, line 2 word by word, the script line writes along the bottom (v05 "LOVING / THE PICTURES / You got of her?") | The hook's final beat | `TC-display`, z8 |
| **P-SCRIPT-ASIDE** | Script aside | overlay | A script phrase alone in the top band ("And something…", "trends") | Write-on 8 f, hold 1.0–2.0 s, fade 6 f | A soft transition line, a thought, a dry aside | `TC-display`, z6 |
| **P-BEHIND-WORD** | Behind-head word | overlay (depth) | One Anton block word 200–340 px behind the head, ≥ 65 % visible | Rises in 4 f behind the cut-out; drifts 8–12 px against the head over its hold; out 4 f | The keyword that deserves depth, on a matted headroom take | `TC-display`, `behind: true`, cut-out (§3.7) |
| **P-BEHIND-LOCKUP** | Behind lockup | overlay (depth) | A script line in front (above the head, clear of it) + a block word behind ("We're emotional / BEINGS") | The script writes 8 f, the block rises in behind 6 f later | A thesis line on a talking piece | two scenes: the script z6 in front, the block `behind: true` |
| **P-TITLE-LOCKUP** | Title lockup | overlay | Montserrat 900 two-line yellow title in the title band | Lines squash in (scaleY 0.05 → 1) 3 f, 2 f stagger; hold 2–4 s; leave on the cut or blur out 4 f | HA-05 hooks, chapter titles over footage | `TC-display`, z6, `kind: "lockup"` |
| **P-COUNT-UP** | Count-up | overlay | Montserrat 900 digits appending left to right (3 → 36 → 365) + the unit stack | A new digit on every spoken beat or every 6 f, each digit rising in 4 f; unit lines rise in 4 f, 4 f stagger | Any milestone or count (HA-08, the payoff) | `TC-display`, z6 (or `behind: true`), `kind: "counter"`, `events` per digit |
| **P-ECHO-OUTLINE** | Echo outline | overlay | The phrase in 4 lines: filled, outline, filled, outline | Lines rise 6 f with 3 f stagger; hold 0.8–1.2 s | A repeated key phrase ("cinematic images") | `TC-display`, z6 |
| **P-HASH-MARKER** | Hash marker | overlay | "#N." in the caption band (SM-1) | Hard in on the cut, 15–24 f | Every list item in F-A | `TC-label`; the caption band; hide the subtitle with `captions.overrides` |
| **P-CTA-KEYWORD** | Keyword CTA | overlay | "Just comment" script + the KEYWORD block 230 px + "to get it" script | Enter the poster by T-11; the lead-in sentence types on in EB Garamond italic 600 64 px `primary` at y ≈ 450, **2 chars/f** (v02 @0:52.53 "So if you'…"), then the P-DUO-TITLE recipe; the keyword holds ≥ 1.5 s | The `comment_keyword` CTA | `TC-display`, z8, `kind: "cta-keyword"` |
| **P-END-BLOCK** | End block | overlay | 4–7 lines of Montserrat 900 filling x 64–1016 over a texture close-up | Lines rise in 3 f apart (line 1 at 0); hold 2.5–4.0 s | The `link_bio` / `end_card` CTA (v03 @ 1:22) | `TC-display`, z8, `kind: "end-card"` |
| **P-SIGNOFF-SUN** | Sign-off sun | overlay (depth) | A giant `soon` gradient block word (yellow → orange) behind the silhouette on the sun backdrop + a script line above | The script writes 8 f; the word rises 10 f behind the cut-out | The last spoken sign-off of an F-A reel ("See you SOON", v02 @ 0:57) | `TC-display`, `behind: true` + P-POSTER-BACKDROP |

**Paper world (B-4)**
| ID | Name | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|---|
| **P-PAPER-CARD** | Paper card | stage | A 9:16 creator clip in a rounded card on W-paper with a burned yellow title | Paper cut (G-3, 0 f) with the card at rest, or G-1 shrink (12 f); the title rises in 4 f at f+8; the card leaves by a hard cut (v04 @0:27.9; a T-6 fade is the alternate) | An example, a past post, a reference (v03 @ 0:11–0:14) | `veos asset add` clip or L-card916; title `TC-display` |
| **P-SPIN-CARD** | Spin-to-vertical | stage | A 16:9 (horizontal) clip as a rounded card (radius 28) on plain black, still playing, that turns a quarter and grows until the now-portrait picture covers the frame | Measured v03 @0:06.45–0:11.0 (`strip-spin-card-90.jpg`): card w 900 at rest 0–8 f, then rotates **0 → 90°** clockwise while scaling **0.55 → ≈ 2.0** (cover) over **75–135 f** (2.5–4.5 s), ease-in-out; the subtitle keeps running; hard cut out | The line about horizontal → vertical, "the old way", a perspective change. It's a chapter-opening move: a second spin in the same reel cheapens the first | video asset; declare the rotation span in `events` |
| **P-RECAP-RIFFLE** | Recap riffle | stage | 9:16 cards with their own burned titles, one per **0.5–0.6 s**, on W-paper | Hard cut into the first card at rest; hard swap of the card content and title every **14–18 f** (measured 0.50–0.58 s, v04 @0:19.3–0:28.4, `strip-recap-riffle.jpg`); the frame never moves; out by a hard cut | Year recaps, "everything I made", past episodes (v04 @ 0:19–0:27) | one asset per card; `cuts` per swap; titles `TC-display` |
| **P-CARD-CAROUSEL** | Carousel | stage | 9:16 cards sliding horizontally on W-grid; the active card centred (x 176), the next peeking at x 1000 | Slide 8 f ease in-out per step (T-5), 1.0–1.5 s per card | Two to four examples of one idea (v02 @ 0:29–0:31, 0:49–0:51) | assets; `cuts` per step |
| **P-LANDSCAPE-CARD** | Landscape card | stage | A 4:3 example card on W-paper with guide lines and ink | Paper cut; the card at rest; guides draw 10 f; ink 10 f | F-B rules about framing, a before/after on one card (v03 @ 0:24–0:27) | L-card43 or an asset |
| **P-FLOAT-CARDS** | Floating cards | overlay | 3–6 small 9:16 cards (180–260 px wide, radius 16) floating around the presenter on a light set, each a different example, around the head rather than on it | Cards pop in 6 f with 4 f stagger, drift 10–20 px/s, exit by blur 6 f; up to 4 on screen at once | "All of these", a community, a body of work (v02 @ 0:27, 0:41–0:42) | assets |

**Polaroids (B-5)**
| ID | Name | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|---|
| **P-POLAROID** | Polaroid | stage | A white-bordered photo or clip (24 px `frame` border) on W-grid, tilted −2.5…+2.5° | Enters and leaves through the **T-10 flash** (v01 @0:28.93, 0:31.01; v05 @0:26.38): already at rest, with a 1 % scale / 0.2° settle over 3 f; photos inside riffle by hard swap every 0.5–1.0 s; no push | A moment, a memory, a "look at this", an after-state (v02 @ 0:45–0:48, v05 @ 0:23–0:25) | asset |
| **P-BEFORE-AFTER-POLAROID** | Before/after | stage | The before polaroid, then the after polaroid in the same rect | The before holds 1.0–1.5 s; a hard swap of the photo (a cut) on the "after" word; the after holds ≥ 1.5 s | F-B RESULT, transformation payoffs (v05 @ 0:57–1:00) | two of the creator's real assets (SH-9) |

**Devices and UI (B-6)**
| ID | Name | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|---|
| **P-APP-DEVICE** | App device | stage | A dark rounded device frame with the screen recording, on W-grid | The device rises 10 f; on the button word the scene's own camera scales the device 1.0 → 1.8 toward the control over 12 f, the rest blurs 8 px; back over 10 f. Keep UI text inside the screen above y 1400 (the device's bottom edge meets the subtitle band) | Every app or tool step (v05 @ 0:30–0:54) | SH-8 asset, else FB-8; private data blurred |
| **P-PHONE-REEL** | Phone reel | stage | A portrait phone frame showing a reel, a yellow P-INK-OVAL around the caption or UI region | The phone at rest on W-paper; the oval draws 10 f on the word | Talking about posts, captions, a platform (v03 @ 1:10–1:15, v04 @ 0:48–0:53) | the creator's screen capture, else the real post captured from the web, else a created `fx.appUI({kind: "video"})` |
| **P-UI-CHIP** | UI chip | overlay | A search-bar pill or a button pill ("BUY NOW") over footage | Pop 6 f (scale 0.9 → 1.0 + blur 8 → 0), hold 1–2 s, out 4 f | A search, a purchase, a click habit (v02 @ 0:12, 0:17) | `TC-label`, z6 |
| **P-FLOAT-PANEL** | Floating panel | overlay | A tall list card (product list, checklist) floating beside the subject, tilted 6° | Slides in from the edge 10 f, drifts 10 px | A persona's habit shown as a list (v02 @ 0:10–0:11) | a `TC-label` heading, texture rows inside; z5, beside the face |

**Ink and guides (B-7, §8.6)**
| ID | Name | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|---|
| **P-GUIDE-LINES** | Guide lines | annotation | A 3 px white (75 %) centre line, or a 3 × 3 grid, over footage or a card | Lines draw from the top in 10 f; hold for the rule | Composition, alignment, "the centre", "thirds" (v03 @ 0:20–0:36) | the anchor pass |
| **P-INK-ARROWS** | Ink arrows | annotation | 1–4 hand-drawn `primary` arrows converging on the subject | Shaft 8 f, head 3 f, 4 f stagger, a slight wobble | "Look at", "here", "the subject" (v03 @ 0:22, 0:48) | the anchor pass |
| **P-INK-OVAL** | Ink oval | annotation | A hand-drawn `primary` oval (5–7 px) around a region | Draws 10 f with a 15° overshoot | A caption area, an object, a detail (v03 @ 0:58, 1:10) | the anchor pass |
| **P-LASSO** | Lasso | annotation | A thick white (8 px) outline tracing an object being removed or selected | Draws 12 f along the object's outline | Erase / select / cut-out steps (v05 @ 0:36–0:37) | anchor keyframes |

**Footage devices and grades (B-8, B-12)**
| ID | Name | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|---|
| **P-FRAME-IN-FRAME** | Frame in frame | cut | The opener seen through a mirror, door, window or screen | Shot selection; Z-1 if the shot is static | The SH-1 hook shot; any reveal (v01 @ 0:00, 0:08) | SH-1 |
| **P-DETAIL-RUN** | Detail run | cut | One 0.6–1.0 s detail shot per listed noun | Cut on each noun's onset (R-3) | "every colour, every shape, every…" (v01 @ 0:18–0:25) | SH-4 |
| **P-PERSONA-GRADE** | Graded persona | footage treatment | A staged persona scene in its grade (GR-mono / amber / teal) with a label duo | The grade starts on the cut; the label duo on the name word | "N types of X", before/after selves (v02 @ 0:03–0:23) | SH-6 + the grade (§4.3) |
| **P-WALK-BOOKEND** | Walk bookend | cut | The creator walks in on f0 and walks out of the same frame at the end | — | F-A openers and closers (v04 @ 0:00, 1:23) | SH-3 |
| **P-SNAP-RUN** | Snap run | cut | 2–4 poses of the subject being photographed, each a new shot | One T-10 flash per pose, 10–17 f apart; a shutter cue may sit on each flash | "snap the best photos of her", any photo-taking line (v05 @0:16.86–0:18.0, `strip-shutter-flash.jpg`) | SH-4 / SH-6 poses |

**Poster, chaos, brand, references (B-9 … B-13)**
| ID | Name | Type | On screen | Motion recipe | When | Needs |
|---|---|---|---|---|---|---|
| **P-POSTER-BACKDROP** | Poster backdrop | overlay (depth) | The matted creator (profile) in front of a drawn `accent` sun disc (or the `teal_wall` colour wall for a thesis poster), with a duo keyword behind or beside | The backdrop is a `behind: true` z2 scene drawing W-poster's gradient full-frame (the cut-out stays in front); hard cut in, or T-11 | The CTA, a thesis poster (v02 @ 0:39–0:40, 0:52–0:58) | SH-12, a clean matte (FB-12) |
| **P-CHAOS-BURST** | Chaos burst | overlay | GR-mono footage with a 3–5 hard-cut flurry and 4–6 snippets ("[Close Up]", "[Wide]", phrase fragments) around the face, not on it | Up to 1.5 s, 45 f (the source runs ≈ 4 s, v02 @0:04.3–0:08.2; this style keeps it short); snippets **type on 1 char/f** at three depths (big foreground ones blurred 6–10 px, mid sharp, small back ones), 4–6 f stagger, drift 20 px/s; shots change every 8–12 f, each joined by **one pure-white frame** (the T-10 burst variant, v02 @0:06.79, 0:07.17, `strip-chaos-flash-typewriter.jpg`); a duo inside it blurs out in place; the subtitle hides; it ends with a T-13 whip, a cut or the T-7 vortex, then at least 1.0 s with two elements or fewer | The one line about overload, doubt, too many options (v02 @ 0:04–0:08). Once in a reel, never in the hook's first 2 s or the CTA: a second burst turns chaos into noise | `exception: "E2"`, `snippets` declared, `TC-label`, z8 (recipe §16) |
| **P-LOGO-CHIP** | Logo chip | overlay | "With" script + the brand's logo file + the wordmark (white) in the top band | The logo pops 6 f, the wordmark rises 4 f, the script writes 8 f | A sponsor or tool named (v05 @ 0:08) | the creator's logo file, else the real logo fetched from the web, else `fx.logoPlate` |
| **P-SERIES-LOCKUP** | Series lockup | stage | Gold script + gold block + "ep. NN" on W-grid without the grid | The script writes 10 f; the block rises 4 f; hold 1.2 s; cut | Right after the hook of a series reel (v05 @ 0:09) | §7.7 |
| **P-DISCLOSURE** | Disclosure | overlay | The "Paid partnership" line, 24 px at (64, 128) | Fade 6 f; hold ≥ 2 s | Every sponsored segment | §6.7 |
| **P-REF-CARD** | Reference card | stage | Someone else's work (a reel, an artwork, a product page) in a paper card | Paper cut; the card at rest; an optional guide line or oval | "Iconic paintings…", "this creator did…" (v03 @ 0:51–0:54) | the creator's file, else the real one fetched from the web, else rebuilt from its exact text (§12.5) |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the moment needs, then use it.
| Line type | Primary | Alternates | For example |
|---|---|---|---|
| Thesis / opinion | P-DUO-TITLE | P-DUO-STACK, P-BEHIND-LOCKUP | "Training **ALONE** is why you **STOPPED**" |
| Question to the viewer | P-DUO-CORNERS | P-DUO-TITLE | "Is your **PHONE** still taking **BORING** photos?" |
| "N types / N rules / N reasons" | P-DUO-TITLE with the number as a block + SM-1 | P-COUNT-UP | "**3** types of **GYM** people" |
| A milestone or count | P-COUNT-UP | P-BEHIND-WORD (the number) | "52 → 52 CITIES" |
| Arriving somewhere / a place | P-FRAME-IN-FRAME + a card title on a P-PAPER-CARD | P-WALK-BOOKEND | the homestay door |
| Taking photos, posing | P-SNAP-RUN | P-POLAROID via T-10 | portraits at a doorway |
| Listing nouns | P-DETAIL-RUN | P-RECAP-RIFFLE | spices, steam, bowls, the cook's hands |
| A persona or "type" | P-PERSONA-GRADE + a label duo | P-FLOAT-PANEL | "The **EGO LIFTER**" (GR-amber) |
| A habit shown as a list or a search | P-UI-CHIP | P-FLOAT-PANEL | a "best pre-workout" search pill |
| Doubt, overload, too many options | P-CHAOS-BURST (once) | P-SCRIPT-ASIDE | "am I doing it wrong?", "[Form check]" |
| A rule with a frame or alignment | P-LANDSCAPE-CARD + P-GUIDE-LINES | P-PAPER-CARD + P-INK-ARROWS | the horizon on the third |
| "Look at this / here" | P-INK-OVAL | P-INK-ARROWS | the person in the frame |
| An app or tool step | P-APP-DEVICE | P-LOGO-CHIP | a photo editor's slider |
| Remove / select / cut out | P-LASSO | P-INK-OVAL | the tourist behind her |
| Before → after | P-BEFORE-AFTER-POLAROID | P-POLAROID ×2 | the photo before / after |
| A past post or episode | P-PAPER-CARD | P-RECAP-RIFFLE | last month's transformation |
| Someone else's work | P-REF-CARD (the creator's file, else the real one fetched) | P-PHONE-REEL | a coach's viral post, captured from the web |
| A key phrase repeated | P-ECHO-OUTLINE | P-DUO-TITLE | "SLOW TRAVEL" |
| The turn ("but…", "then it changed") | P-DUO-TITLE (the re-hook) | P-BEHIND-WORD | "**BUT** I was **WRONG**" |
| A feeling, a quiet moment | no type: Z-1 push-drift, CS-1 only | P-SCRIPT-ASIDE | a train window |
| Sponsor or tool named | P-LOGO-CHIP + P-DISCLOSURE | — | the booking app |
| CTA (comment) | P-CTA-KEYWORD on P-POSTER-BACKDROP | P-CTA-KEYWORD on footage | "Just comment **PLAN**" |
| CTA (link / part 2) | P-END-BLOCK | — | "FREE PLAN / LINK IN BIO" |
| Sign-off | P-SIGNOFF-SUN or the bookend | P-WALK-BOOKEND | "See you **TOMORROW**" |

### 8.5 Numbers and truth
- No charts or computed figures in this style; counters show numbers that are spoken or in the script, as digits.
- Counts are countable: "3 types" shows 3 items; a "52 films" count-up lands on 52.
- App screens are the creator's recordings, else the real app captured from the web; a created UI is generic and
  unbranded; illustrations inside it may use
  made-up but realistic values, no label.
- Before/after photos are the creator's real results; never simulate an "after".

### 8.6 Comedy and the ink layer
**Comedy is light.** Staged persona exaggeration (the shot itself), a deadpan script aside, an ironic UI chip ("best
camera to buy" typed by the gear persona), a reaction shot. Never stickers, stamps, meme cues, emoji, crash zooms or
freeze-frame roasts.

**The ink layer** (yellow hand-drawn marks; F-B lives on it, F-A borrows it for "look at this"):
- **Stroke:** colour `primary`, width 5–7 px (6 default), round caps, wobble ±1.5 px (seeded, per path), draw-on 10 f,
  a 15° overshoot at the start of ovals.
- **Guides:** `paper` at 75 %, 3 px, straight, drawn from the top in 10 f; a centre line, a rule-of-thirds grid, or one
  horizon line.
- **Lasso:** `paper` 8 px, traced along the object's outline over 12 f.
- **Marks:** arrow (shaft 8 f, then head 3 f), oval, underline (8 f), guide line, lasso. No circles of text, no scribbles,
  no notes in marker type.
- **Targets:** the anchor pass reads sampled frames of the clip and writes each target's rect `{x, y, w, h}` in output
  px; a moving subject gets 2–4 keyframes (linear between them); a target leaving the frame ends the mark.
- **Rules:** at most three marks on screen; marks finish before their scene ends; around a face, not across it; one mark
  per spoken "here / this / look"; arrows converge on the subject, never point off-frame.
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

### 8.7 Assets
- **Real captures first:** the creator's own footage, photos, screen recordings and past posts.
- **Allowed mocks:** a generic, unbranded UI built with `fx.device` / `fx.appUI`; the search pill and button pill (generic
  shapes, not a brand's UI).
- **No stock clichés:** no stock B-roll, no generated "cinematic" scenes, no drone stock.
- **Logos:** the creator's files first (their own brand, a sponsor's logo), else the real logo fetched from the web; a
  type-set logo plate (`fx.logoPlate`) only when none can be found.
- **Third-party moments:** fetch the real thing, source noted (§12.5).

---

## §9 Transition system

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue |
|---|---|---|---|---|
| **T-1** | Hard cut | 0 | The default, by far the most common | none |
| **T-2** | Cut on motion | 0 | Cut inside a gesture, a turn, a whip or a walk, so the motion continues into the next shot (v02 @ 0:02.5 the hand "3", 0:25) | an optional whoosh |
| **T-3** | Blur-through | 4–6 | An out-of-focus foreground object (a wheel, a shelf, a hand) wipes the frame in-camera; if the source has none, a 6 f vertical motion-blur ramp 0 → 30 px on the outgoing shot and 30 → 0 on the incoming one (§9.5) | whoosh |
| **T-4** | Spin-to-vertical | 75–135 | P-SPIN-CARD (§8.3): 0 → 90°, 0.55 → 2.0, ease-in-out | whoosh |
| **T-5** | Card slide | 8 | A carousel step on W-grid, ease in-out | soft swish |
| **T-6** | Card fade-out | 4 | Alternate only: a paper card fades out on cream, then the next shot cuts in (the measured exit at v04 @0:27.9 is a hard cut into a wheel detail) | none |
| **T-7** | Vortex | 8 | A radial zoom-blur tunnel on the last 8 f of a shot (scale 1 → 1.4, radial blur 0 → 24 px), then a calm shot cuts in sharp (§9.5) | whoosh |
| **T-8** | Paper cut | 0 | G-3: footage → W-paper with the card already at rest | none |
| **T-9** | Hard end | 0 | The bookend's last frame, ≤ 6 f after the last word | none |
| **T-10** | Flash | 6 | An exposure bloom: the outgoing shot brightens over 2 f (brightness 1 → 2.5), cut at the white peak, the incoming one starts blown out and decays to normal over 3 f (v01 @0:28.93 into the polaroids, 0:31.01 out; v05 @0:16.86, 0:17.32 one per "photo", 0:26.38; `strip-shutter-flash.jpg`, `strip-flash-polaroid-exit.jpg`). Inside the chaos burst it's a single pure-white frame between shots (v02 @0:06.79, 0:07.17) | a shutter click on photo beats, else none |
| **T-11** | Warm flash | 7 | As T-10 but tinted cream-yellow (`#FFF6C8`), a 4 f build, cut at the peak into the poster (v02 @0:52.24–0:52.45, `strip-warm-flash-cta.jpg`) | soft whoosh or shine |
| **T-12** | Zoom-through on a gesture | ≈ 4 + 24 | Outgoing: a punch-in ≈ 1.0 → 1.6 on the gesture (a raised hand) over 4 f with zoom blur, the type layer included; a hard cut on the gesture to a shot whose gesture sits in the same place; the incoming shot pulls out ≈ 2.3 → 1.0 over ≈ 24 f, expo-out (ORB per-frame scale 0.91 → 0.997; v02 @0:02.40–0:03.55, `strip-zoom-through-gesture.jpg`) | whoosh |
| **T-13** | Whip pan | 6 + 14 | In-camera: the outgoing shot whips sideways with heavy horizontal smear for 5–6 f; the incoming one lands still panning, ≈ 130 px/f decelerating to 0 over ≈ 14 f (≈ 750 px in all, ORB v02 @0:08.48–0:08.94, `strip-whip-pan.jpg`); the "#N." marker lands mid-whip | whoosh |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| f0 | A moving shot (no transition) | A fade-in, a black frame |
| Hook → body | T-2 cut on motion (2.7–4.0 s) | A morph, a fade |
| New scene / persona / place | T-1 or T-2 | A dissolve |
| Footage → paper | T-8 paper cut (or G-1 shrink for "this is the example") | A cross-fade |
| Paper → footage | T-1 cut (default), T-10 flash out of a polaroid run, or T-6 fade-out then cut | A wipe |
| Footage ↔ polaroid / photo world | T-10 flash in and out | A slide |
| A "snap" / photo-taking line | T-10 on every cut to a new pose (one flash per photo, 0.4–0.7 s apart) | — |
| Hook → first item ("3 types…" with a hand count) | T-12 zoom-through on the gesture | Without a gesture to cut on |
| Persona → persona, place → place | T-13 whip pan when at least one of the two shots was filmed with a whip (the built-in whip completes the other side), else T-1 | A digital whip between two locked-off shots |
| Into the CTA poster | T-11 warm flash | A plain fade |
| Card → card | T-5 slide (carousel) or a content cut (riffle) | A spin |
| Flashback, "the old way", a chapter | T-4 spin | — |
| Out of the chaos burst | T-7 vortex or T-1 | Another chaos device |
| Last word | T-9 on the bookend picture | A black tail, a fade to black |

### 9.3 Shot grammar
| ID | Rule |
|---|---|
| **R-1** | **Cut on the visual idea, not on every word.** In B-roll runs the picture moves on with each new idea; a talking piece runs as long as its thought, then cuts away to what it's about |
| **R-2** | **Cut on motion:** a gesture, a turn, a step or a whip continues across the cut within ±2 f (T-2) |
| **R-3** | **A list of nouns** gets one 0.6–1.0 s detail per noun, cut on each noun's onset (P-DETAIL-RUN) |
| **R-4** | **Return to the presenter** on the opinion, the turn word or the CTA; never mid-clause |
| **R-5** | **A persona** opens with a 1.0–1.5 s establishing wide, then medium action, then the label duo |
| **R-6** | **Travel:** in F-A the place changes whenever the story moves on (a new location, set or persona), so it feels like a journey |
| **R-7** | **Type beats follow words; cuts follow pictures.** Never cut inside a block's 4 f rise; move the cut up to 3 f |
| **R-8** | **The bookend:** the final 1.0–1.5 s plays SH-1's pre-roll so the last frame is frame 0's picture (§7.6) |
| **R-9** | **Walk-in / walk-out:** the creator enters the opening frame within 0.5 s and leaves the closing frame in its last 1.5 s when SH-3 exists |

### 9.4 How the moves breathe
Hard cuts and cuts on motion run constantly and nobody notices them: that's the vlog rhythm. Everything a viewer *can*
name is a moment. The flash belongs to photos and polaroids, and it can fire on every pose of a photo run because that's
what a camera does. The whip joins two places when the camera actually whipped. The warm flash happens once, into the
poster. The spin, the vortex and the zoom-through are one-offs: each is the best move in the reel exactly once, and a
repeat turns it into a trick. Never the same visible move three times running, except the flashes of a snap run.

### 9.5 How the transitions render
Built-in `timeline.transitions[]` entries with a `type` (`renderer/transitions.js`). The engine draws them over the
picture (world, footage, behind-scenes, scenes z1–6) and under the captions and duo titles unless `layers` says
otherwise. Never build them as scenes.

| ID | Timeline entry (measured values) |
|---|---|
| T-10 | `{"t": <cut>, "type": "flash", "frames": 6, "pre": 2, "peak": 0.9, "decay": 1.6}`: 2 f build, the white peak on the cut, 3 f decay (v01 @0:28.93, v05 @0:16.86). **Burst variant** (inside P-CHAOS-BURST): one pure-white frame, `{"t": <cut>, "type": "flash", "frames": 1, "pre": 0, "peak": 1}` |
| T-11 | `{"t": <cut>, "type": "flash", "colour": "#FFF6C8", "frames": 7, "pre": 4, "peak": 0.9}`: a 4 f cream build, cut at the peak into the poster, a short decay (v02 @0:52.24) |
| T-12 | Two built-ins on the same cut. **Outgoing:** `{"t": <cut>, "type": "zoom-blur", "frames": 6, "pre": 4, "amount": 0.3, "punch": 0.4, "at": [<gesture x>, <gesture y>], "layers": "all"}` (a 4 f punch with zoom blur, the type layer included; the engine caps `punch` at 0.4, so it reaches 1.4× where the source reaches ≈ 1.6×). **Incoming:** the camera landing Z-4 on the cut, `{"t": <cut>, "preset": "zoom-land", "p": {"origin": {"x": <gesture x>, "y": <gesture y>}}}` (1.5 → 1.0 over 24 f, `expoOut`, a radial blur decaying with it; the source pulls out from ≈ 2.3×, the `slow_push` policy lands from 1.5× at most). Cut on the gesture (T-2) so it sits in the same place in both shots; it needs ≥ 1.5× headroom (4K, or 1080p with the base reframe at 1.0), else a plain T-2 |
| T-13 | `{"t": <cut>, "type": "whip", "dir": "left", "frames": 20, "pre": 6, "px": 90, "travel": 750, "blend": 0}`: 6 f of smear out, the incoming shot arrives ≈ 750 px off and decelerates over 14 f; no cross-blend (the source cuts at the blur peak). Match `dir` to the in-camera whip; use it on in-camera whip pairs or when one of the two shots was whipped, never between two locked-off shots |
| T-3 (no in-camera blocker) | `timeline.blur`: `{"t": <cut − 3 f>, "kind": "directional", "angle": 90, "px": 30, "frames": 6, "shape": "pulse"}`: a vertical smear 0 → 30 px into the cut and 30 → 0 out of it, footage only |
| T-7 | `{"t": <cut>, "type": "zoom-blur", "frames": 9, "pre": 8, "amount": 0.3, "punch": 0.4}`: the tunnel on the last 8 f (scale 1 → 1.4), then the calm shot cuts in sharp |

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset |
| Block rise-smear in | 4 f: y + 0.8 × cap height (≈ 150–220 px; tokens 180) → 0, vertical smear 24 → 0 px, opacity 0 → 1, expo-out `cubic-bezier(0.22, 1, 0.36, 1)` (v01 @0:00.59) |
| Block rise-out | 4 f: y 0 → −130 px (110–150 measured), smear 0 → 24, opacity 1 → 0, `cubic-bezier(0.64, 0, 0.78, 0)`; last word in leaves first, 1 f apart; the script un-writes R→L in 4 f |
| Script write-on | 8 f left-to-right clip mask, linear |
| Keyword hold | 0.4–0.6 s per beat; titles 2–4 s |
| Card enter | 6–10 f; card fade-out 4 f |
| Spin card | 75–135 f, 0 → 90°, scale 0.55 → 2.0, ease-in-out `cubic-bezier(0.65, 0, 0.35, 1)` |
| Carousel step | 8 f in-out |
| Polaroid entry | via the T-10 flash; a 3 f settle (1 % scale, 0.2°) |
| Flash (T-10) | 2 f up + the cut + 3 f decay; the burst variant is 1 white frame |
| Title squash-in | 3 f per line (scaleY 0.05 → 1), 2 f stagger |
| Typewriter | the CTA serif line 2 chars/f; chaos snippets 1 char/f |
| Riffle swap | 14–18 f per card |
| Count digit | 6 f per appended digit when spoken as one number |
| Ink draw | 10 f (arrow shaft 8 + head 3; oval 10 with a 15° overshoot) |
| Vortex | 8 f |
| Behind-word parallax | 8–12 px over the hold |
| Hold | text ≥ 0.25 s per word; titles ≥ 10 f after complete |

### 10.2 Footage camera (`zoom_policy: slow_push`)
| ID | Preset | Recipe | Use |
|---|---|---|---|
| **Z-1** | `push-drift` | 1.00 → 1.06 over the beat (`ease: "linear"`, at least 15 f) | A static shot that must feel alive: awe beats, plain talking pieces, the hook if SH-1 is static |
| **Z-2** | `slow-push` | 1.00 → 1.06 over 150 f, `ease: "linear"` (measured 1.06 over 5.3 s, ≈ 1.1 %/s, v04 @0:42.4–0:47.6, `strip-slow-push.jpg`) | A hold longer than about 3 s: the turn, a confession, the closing talking piece |
| **Z-3** | `reset` | Back to 1.00 on a cut | Only on a cut |
| **Z-4** | `zoom-land` | Landing on a cut: 1.50 → 1.00 over 24 f, `ease: "expoOut"`, `blur: {kind: "radial", amount: 0.18, shape: "decay"}`, `origin` the gesture point (it starts on a cut and ends on 1.0, so `slow_push` allows it) | Only as the incoming half of T-12 |

**The footage is locked off** (ORB scale 1.000 ± 0.003 per frame on v01 @0:00–0:01 and 0:04, v03 @0:00, v05
@1:03–1:07): movement comes from the subject (walk-ins, gestures, cars) or from in-camera moves (whips, drone), not from
engine zooms. Leave a static shot static when its subject moves; Z-1 only when nothing in the frame moves. The camera is a
breath you feel, never a move you see: never a punch, crash, shake or rotation as a camera event (T-12 is a built-in
transition plus the Z-4 landing), never two moves within 0.4 s, and a different move from one to the next so it never
feels mechanical. A 1080p source allows re-crops up to 1.35×; 4K allows 2×.

### 10.3 Layer order (back to front)
1. The world (W-paper, W-grid, W-void, W-poster) or the blurred footage copy
2. Paper cards, polaroids, devices on L-hidden (z3)
3. The footage group: the graded footage → **behind scenes** (P-BEHIND-WORD, P-POSTER-BACKDROP, the P-SIGNOFF-SUN word)
   → the cut-out. Grades live here, on the footage, never on the graphics.
4. B-roll clip scenes over the voice (z4, each grading its own frame, §12.6)
5. Card titles, UI chips, floating panels, ink marks (z5–6)
6. The title lockup, the counter, script asides (z6)
7. The CS-1 subtitle (z7)
8. Duo titles, the CTA keyword, the end block, chaos snippets (z8; the subtitle hides under them)
9. The disclosure line (z9)

### 10.4 Finishing
- No grain, no film burns, no resting light-leak overlays (the T-10 / T-11 flashes are transitions). W-paper noise 0.03,
  W-grid noise 0.04 + vignette 0.42, W-void vignette 0.3.
- Soft shadows only: cards `0 18px 40px rgba(0,0,0,.18)`, polaroids `0 14px 30px rgba(0,0,0,.35)`, the device `0 30px 60px
  rgba(0,0,0,.45)`.
- No glow. The only gradient fill on type is the sign-off word (`soon`).
- Radii: 9:16 cards 40, 4:3 cards 28, the device 64, the phone 48, floating cards 16, polaroids 2.

---

## §11 Sound

Sound is minimal: the voice, a bed, and a few cues that each mark something you see. Catalogue ids only; every cue sits on
a visible event, no file more than twice, never the same file twice in a row.

| Line | Decision |
|---|---|
| **Cue moments** | `hook` (one soft cue on the first keyword landing), `transitions` (cut on motion, the T-13 whip and the T-12 zoom-through: a whoosh; the spin, the vortex, the carousel; T-11 into the poster: a soft shine; a camera-shutter click on each P-SNAP-RUN flash), `reveals` (the count-up landing, the polaroid drop, the before → after swap, the end block), `cta` (the keyword landing). Duo beats after the hook, subtitles and ink marks are silent |
| **Good starting points** (all in the catalogue) | `appear-enter` (a soft hook or reveal cue), `air-low-woosh` (a calm whoosh on a cut on motion), `fast-swish-movement-fast-swish-movement` (the carousel slide), `camera-shutter-2025-02-19-17-59-23-utc-dslr-camera-shutter-v1` (a snap-run flash), `05405-shine-ding` (the warm flash into the poster, the CTA keyword) |
| **Meme cues** | none: comedy is light |
| **Music bed** | From f0 (not observable in the source; a cinematic-vlog default): a cinematic or lo-fi bed that rides the whole reel |
| **Ducking** | The bed ≥ 18 dB under the voice while it speaks; location sound in B-roll kept at −28 to −22 dB under the voice and ducked with it |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the last word, on the bookend frame |

When in doubt, leave a cue out: the cuts and the type carry the energy.

---

## §12 Footage handling

### 12.1 Setups
| Setup | Camera and framing | Head top y (output) | Light / set | Notes |
|---|---|---|---|---|
| **A** Location talking piece | Handheld selfie or gimbal at arm's length, 4K preferred, 24/25/30 fps | 250–520 | Natural light, golden hour preferred | 2–5 locations in a reel |
| **B** Seated set | Tripod, a 50–85 mm look, shallow depth | 420–700 | Warm practicals (a lamp, a textured wall), a dark top | the v02 interview set |
| **C** Wide / overhead | Drone, balcony, stairs or a high tripod; the presenter small | 600–1100 | A composed frame (lines, railings, a car, a door) | Hook shots, walk-ins |
| **D** Clean-matte headroom | Tripod, a plain or distant background, ≥ 300 px above the head | 560–800 | Separation light | Behind-head words, the poster |

Wardrobe: solid tops; a signature cap or prop is welcome (it recurs). No mic visible in setups B and D.

### 12.2 Shots
| ID | Shot | Spec | How many | Must / optional | Formats |
|---|---|---|---|---|---|
| **SH-1** | Opening shot | Moving and composed: a mirror, doorway, window, overhead, or a walk-in; 3–5 s **plus 1.5 s of pre-roll** before the in-point (the bookend uses it) | 1 | must | F-A, F-B |
| **SH-2** | Overhead / drone | Top-down or high-angle of the presenter at a location, 3–6 s | 0–2 a minute | optional | F-A, F-B |
| **SH-3** | Walk-in / walk-out | The same spot, the same framing: the creator enters at the start and leaves at the end | 1 pair | optional | F-A |
| **SH-4** | Location B-roll | Details, hands, products, POV, macro inserts, 1–2 s each, 4K or 1080p | 20–40 a minute | must | F-A, F-B |
| **SH-5** | Talking pieces | 2–5 different setups or locations (A/B) | 2–5 | must | F-A, F-B |
| **SH-6** | Persona scenes | The same person with an outfit, prop or place swap, 3–6 s each | 0–4 | optional (must for "types of" reels) | F-A |
| **SH-7** | Signature prop / vehicle | 1–3 s each | 0–6 | optional | F-A, F-B |
| **SH-8** | Screen recordings | The app or tool being taught, portrait, ≥ 1080 px wide | 0–8 | optional (must for app tutorials) | F-B |
| **SH-9** | Before / after | Stills or clips of the real result | 0–2 | optional (must when the topic has a visual result) | F-B |
| **SH-10** | Past posts | Screen captures of the creator's own posts | 0–9 | optional | F-A, F-B |
| **SH-11** | Headroom shot | Setup D, for behind-head words | 1–3 | must | F-A, F-B |
| **SH-12** | Poster shot | Profile or 3/4 against a plain wall with back light | 0–1 | optional | F-A, F-B |
| **SH-13** | Texture close-up | Grass, fabric, water, a wall, 3–4 s, for the end block | 0–1 | optional | F-B |

### 12.3 Fallbacks
| ID | For | What happens instead | What it costs | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | Open on the most moving wide of the presenter (walking, gesturing) with Z-1 push-drift; the bookend reuses its first 1.0 s (ending on its first frame) | No frame-within-frame surprise | degraded |
| **FB-2** | SH-2 | A high-angle phone shot (stairs, balcony, pole); else the title lockup over the widest shot | No aerial scale | degraded |
| **FB-3** | SH-3 | Hold an empty plate of the location 0.5 s before the first and after the last talking shot | The entrance and exit are implied | holds |
| **FB-4** | SH-4 | Alternate two re-crops of the talking take (up to 1.35× from 1080p, 2× from 4K) with paper cards and polaroids of the creator's photos, a change every 1.0–1.5 s | Less location variety; the rhythm comes from crops and cards | degraded |
| **FB-5** | SH-5 | One location, two framings (wide / tight) cut on sentence boundaries | No travel feeling | degraded |
| **FB-6** | SH-6 | One location with an outfit or prop swap per persona, told apart by GR-mono / GR-amber / GR-teal and a label duo per persona | Less staging | holds |
| **FB-7** | SH-7 | Drop the prop beats; use SH-4 details | Nothing structural | holds |
| **FB-8** | SH-8 | The real app or page captured from the web inside the P-APP-DEVICE frame; else a created generic UI (`fx.appUI`) | Not the creator's own recording (or, created, not the real app) | degraded |
| **FB-9** | SH-9 | No before/after; the result becomes a P-PAPER-CARD checklist | No visual proof | degraded |
| **FB-10** | SH-10 | Recap cards built from SH-4 stills with burned titles | Not the real past posts | holds |
| **FB-11** | SH-11 | The word sits above the head on the front layer (40 px clear of the head region), not behind it | No depth sandwich | degraded |
| **FB-12** | SH-12 | Matte the best profile take and draw the W-poster backdrop behind it; if the matte fails at 200 %, the CTA duo sits over plain footage | A less graphic sign-off | degraded |
| **FB-13** | SH-13 | The end block sits on W-void | A flatter end card | holds |

Note the fallbacks used in your plan. If the B-roll is too thin to keep the picture moving even with FB-4, build the
strongest edit this style allows from what there is and say so in one line with the storyboard: this style is its
footage, and more B-roll next time is the fix.

### 12.4 Props, the reaction bank, the cut-out, resolution
- **Props:** one signature prop or vehicle per series (optional); the phone with the app open (F-B); outfit or cap swaps
  for personas.
- **Reaction bank (worth asking for at the shoot, 2–3 s each):** a nod to camera, a laugh off camera, a turn and walk
  away, a point to camera, a hand counting fingers (a cut-on-motion source).
- **Cut-out:** needed for behind-head words and the poster; feather 2 px, choke 1 px; check the hair at 200 %.
- **Resolution:** a 2× re-crop needs a 4K source; a 1080p source allows 1.35×. Drone and overhead shots must be ≥ 2.7K
  to survive the 9:16 crop.

### 12.5 Third-party inserts: fetch the real thing
When the creator names a real reel, post, artwork, app, brand or product page, the viewer should see the real one.
1. **Find the moments** that call for it. In this style: another creator's reel or post (P-PHONE-REEL / P-REF-CARD), an
   artwork or famous photograph (P-REF-CARD), an app's UI that isn't the creator's own recording (P-APP-DEVICE), a brand
   logo (P-LOGO-CHIP), a product page (P-FLOAT-PANEL).
2. **The creator's own files** in their folder come first.
3. **Otherwise search the web and fetch it:** the real logo, the real post, the real page or artwork (captured and framed
   on the part that matters). Note where it came from.
4. **Use it as it is** inside the style's frame (paper card, phone, device), cropped and marked with ink, never altered
   to say something it doesn't; a post or headline word for word.
5. **Nothing usable to be found: rebuild it from its exact words.** Another creator's reel →
   `fx.appUI({kind: "video", caption})` in the phone frame; a post → `fx.quoteCard` (verbatim words); an artwork or a
   person → `fx.silhouette` with the title set in type; an app → `fx.appUI` (generic, unbranded); a logo →
   `fx.logoPlate`. No labels, no credit lines.

### 12.6 Frame rate, audio and how the footage plays
- Output 1080 × 1920, **30 fps CFR**; conform 23.98/24/25 fps sources (cinematic sources are usually 24).
- Voice chain: high-pass 80 Hz, de-ess, light compression; one voice track (a lav or the location mic, never both).
- **The cut map carries the voice.** The EDL is built from the talking pieces (setups A/B/D, their own audio), or from
  the separate voice-over file when the creator recorded one. Talking pieces in the cut map get the face boxes, the
  cut-out and the behind-head words, and the engine grades them (GR-warm, or a persona grade, §4.3).
- **B-roll plays over the voice as picture-only scenes.** Every SH-1/SH-2/SH-4/SH-6/SH-7 clip is `veos asset add`-ed and
  shown full-bleed at z4, frame-exact from its in-point, declared as a cut and as live motion. Video assets aren't graded
  by the engine, so the scene grades its own frame: the warm footage grade by default, the persona's grade inside a
  persona span.
```js
// B-roll over the voice, graded like the camera footage. grade: a GR id inside a persona span, else the warm footage grade.
function roll(o) {   // o = {id, asset, t_in, t_out, offset, grade}
  return VEOS.scene({ id: o.id, t_in: o.t_in, t_out: o.t_out, z: 4, in: "none", out: "none", kind: "broll", roles: [],
    cuts: [0], continuous: true, box: { x: 0, y: 0, w: 1080, h: 1920 },
    render(ctx, lt) {
      const g = ctx.grade(o.grade || ctx.tokens.grades.footage);
      return ctx.html(`<div style="position:absolute;inset:0;background:url('${ctx.videoFrame(o.asset, (o.offset || 0) + lt)}') center/cover;${g}"></div>`);
    } });
}
roll({ id: "b-kettle", asset: "B07", t_in: 3.10, t_out: 4.02, offset: 2.40 });
roll({ id: "b-hoarder-1", asset: "B12", t_in: 9.05, t_out: 10.20, offset: 0.80, grade: "GR-amber" });
```
- A persona scene with the creator's own line on camera stays in the cut map (graded by a `timeline.grades[]` span,
  §4.3); a persona scene played under the voice is B-roll (graded by `roll`).

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The format** (F-A or F-B) and the hook archetype (HA-12 / HA-05 / HA-19 / HA-08).
2. **The hook:** SH-1 (clip, in-point, its motion), the duo split of the thesis with every beat's words, frame and rect
   (or the lockup's lines and sizes), the first cut on motion and its frame pair; the 8–10 candidates, the pick, two
   alternates.
3. **The shot map:** for every sentence, the clip that carries it (asset, offset, length), every cut with its T-id and
   the motion it hides in; the detail runs one noun at a time.
4. **The type layer:** every duo title (beats, words, times, rects), every behind-head word (the take, the head top, the
   word's rect, the matte check), the counters, the card titles, the asides.
5. **Paper and personas:** which lines step onto paper and on which card; each persona's grade; the chaos burst, if any,
   with its snippets.
6. **The furniture:** the bookend (SH-1's clip, the pre-roll span, the words that ride it), the ink anchors, the series
   number, the sponsor's logo and disclosure.
7. **The inserts** (creator's / fetched, with its source / created) and the fallbacks used.
8. **The sound:** each cue on its event, the bed from f0.
9. **The moments you'll look at hardest on the storyboard:** f0 (moving, no type fully visible), 1.5 s (mid-hook: a
   block landed, the head clear), a behind-head word (≥ 65 % visible, letters clear of the hair), one paper beat (yellow
   never on cream), one persona or rule beat (its grade), the CTA, and the last frame next to f0.

**Beat fields this style adds:** `caption {profile: CS-1, overrides[]}` (hide for "#N." markers, text fixes); `ink [{mark:
arrow | oval | guide | lasso, target: {x, y, w, h}, frames}]` from the anchor pass; `bookend {shot: SH-1, src_in,
src_out}` on the BOOKEND beat and `walk: in | out`; `series {name, number}`; `sponsor {id, disclosure}` on every
sponsored beat; `grade: GR-warm | GR-mono | GR-amber | GR-teal`; `shot_id: SH-n`, `fallback_used: FB-n | null`;
`exception: E2` (the chaos burst only); `rehook: true`. The reel header carries `format`,
`hook_archetype`, `structure`, `count`, `keyword`, `cta_device`, `grades`, `bookend`, `series`, `sponsor`.

A beat and a header, for the shape:
```yaml
- id: 7
  section: SCENE-2                 # HOOK | SETUP | SCENE-n | TURN | PAYOFF | CTA | BOOKEND (F-B: CONTEXT | RULE-n | RESULT)
  t0: 18.40
  t1: 21.10
  spoken: "And the ego lifter only cares about one thing"
  trigger: {word: "ego", at: 18.92}
  tone: warn                        # hype | awe | explain | warn | win | cta
  layout: L-full
  visual: "Amber-graded gym, the creator in a lifting belt mid-rep; 'The EGO LIFTER' duo lands on 'ego'"
  layers: [grade-amber-1, duo-ego]
  pattern: P-PERSONA-GRADE
  grade: GR-amber
  shot_id: SH-6
  sfx: []
```
```yaml
format: F-A                        # the reel header
hook_archetype: HA-12
structure: story
count: 3
keyword: "PLAN"
cta_device: comment_keyword
grades: {persona-1: GR-mono, persona-2: GR-amber, persona-3: GR-teal}
bookend: {shot: SH-1, clip: B01, src_in: 12.40, pre_roll: [10.90, 12.40]}
series: null                       # or {name, number}
sponsor: null                      # or {id, disclosure}
```

A hook proposal, for the shape (write 8–10; this is the pick):
```yaml
- name: "Mirror thesis"
  archetype: HA-12
  thesis: "When it comes to what you wear, shopping in person is way better than online"
  duo_beats: ["when it comes to what | YOU WEAR", "SHOPPING / IN PERSON", "IS WAY / BETTER | than online"]
  scene_promise: {shot: SH-1 mirror, payoff: "the try-on scenes at 0:09-0:26"}
  storyboard: "f0 mirror, creator small, script writing | 0.47 YOU | 0.80 WEAR | 1.07 out | 1.40 SHOPPING IN PERSON | 2.33 IS WAY BETTER + 'than online' | 3.9 cut on motion to the doorway"
  sound: [soft cue on 'YOU', whoosh on the first cut]
  stopper: {mute: pass, motion_f0: pass, read_s: 1.0, payoff_s: 2.9}
```

---

## §14 Worked examples

Times are planning estimates: take the real ones from the words. They show the standard; match it, then beat it.

### 14.1 F-A story, travel: "I stopped booking hotels" (66 s, keyword STAY)
**Header:** F-A · HA-12 · story · no count · CTA `comment_keyword` STAY · bookend SH-1 (a homestay doorway seen from
inside; the creator walks in from the street) · GR-warm throughout · a behind-head word at 41.2 s.

**Hook (0–3.1 s):**
| t (s) | Spoken | Picture | Type layer | Subtitle | Camera / cue |
|---|---|---|---|---|---|
| f0 | — | SH-1: the doorway frame, the creator far away in the street, walking toward it | "I" starts writing at (72, 236) | hidden | hook cue at 0.45 |
| 0.10 | "I" | same | script "I" written (8 f) | — | — |
| 0.45 | "stopped" | same | **STOPPED** rises in, 220 px, top y 330 | — | — |
| 1.05 | (out) | same, closer | STOPPED rises out | — | — |
| 1.20 | "booking" | same | **BOOKING** line 1 (200 px) | — | — |
| 1.55 | "hotels." | same | **HOTELS** line 2 | — | — |
| 2.10 | (out) | the creator reaches the door | the lockup rises out | — | — |
| 2.30 | "and this" | same | script "and" + **THIS** | — | — |
| 2.75 | "happened" | same | script "happened" below-right; the thesis complete | — | — |
| 3.10 | — | **T-2** cut on his step through the door → SH-4 kettle detail | out 2 f before the cut | CS-1 starts | transition cue |

**Plan:**
| Section | t (s) | Spoken (gist) | Patterns and picture |
|---|---|---|---|
| SETUP | 3.1–9.0 | "Six months, eleven cities, zero hotels." | P-DETAIL-RUN (kettle, keys, shoes at the door) → talking piece A on a rooftop; **P-COUNT-UP** "11" + "CITIES" at 5.2 (lands on "eleven") |
| SCENE-1 | 9.0–20.0 | The first morning: breakfast with the host family | P-DETAIL-RUN of four nouns (rice, chilli, steam, hands) at 0.8 s each → **P-POLAROID** of the family's kitchen (the creator's photo) on W-grid on "they made me family", in and out through T-10 → back to talking piece B |
| SCENE-2 | 20.0–30.5 | "Half the price, and I knew where the locals eat" | **P-UI-CHIP** "hotels near me" over his phone shot (deadpan, light comedy) → street-food B-roll → **P-PAPER-CARD** of his own past reel "Hoi An homestay" (SH-10) with its card title |
| TURN (re-hook) | 30.5–35.0 | "But it's not for everyone." | **P-DUO-TITLE** "**BUT** it's not for **EVERYONE**" on a talking piece, `rehook: true`; Z-2 slow push |
| SCENE-3 | 35.0–46.0 | Shared bathrooms, no reception, roosters at 5 am | P-DETAIL-RUN of the three → **P-BEHIND-WORD** "NOISE" behind his head on SH-11 at 41.2 (`behind: true`) → P-SCRIPT-ASIDE "…riveting" over a rooster (light comedy) |
| PAYOFF | 46.0–58.0 | "What I got instead: every city from the inside." | **P-RECAP-RIFFLE** of six hosts' doorways, city names as card titles, 0.5 s each (cuts) → talking piece with **Z-2** slow push |
| CTA | 58.0–64.5 | "Comment STAY and I'll send you all eleven." | T-11 warm flash → **P-POSTER-BACKDROP** (SH-12 profile, the `accent` sun) + **P-CTA-KEYWORD** "Just comment / **STAY** / for the list", held 2.4 s |
| BOOKEND | 64.5–66.0 | "See you inside." | SH-1 pre-roll [src 10.9–12.4]: the doorway, the creator far away in the street; the last frame equals f0 |

How it breathes: about 37 cuts, mostly hidden in steps and turns; duo titles on the hook, the turn and the CTA, plus the
count-up; paper for about 9 s (the polaroid, the card, the riffle); the creator on screen about half the time.

### 14.2 F-A types, fitness: "3 types of gym people" (61 s, keyword PLAN)
**Header:** F-A · HA-12 · story (a list of types) · count 3 · SM-1 markers · CTA `comment_keyword` PLAN · grades
persona-1 GR-mono, persona-2 GR-amber, persona-3 GR-teal · the chaos burst at 6.0 s · a behind-head word at 1.3 s.

**Hook (0–2.9 s):**
| t (s) | Spoken | Picture | Type layer | Subtitle | Camera / cue |
|---|---|---|---|---|---|
| f0 | — | Setup B seated set, the creator gesturing (live) | — | hidden | — |
| 0.60 | "There are three" | same | **3** rises in at (150, 360), 230 px, left of his cap (front, 40 px clear of the head region) | — | hook cue |
| 0.95 | "types of" | same | script "types of" writes to the right of the 3 | — | — |
| 1.30 | "gym" | same | **GYM** rises in **behind** his head (`behind: true`, 260 px, ≥ 65 % visible) | — | — |
| 1.70 | "people" | same | script "people" under it, right-aligned | — | — |
| 2.30 | — | he raises three fingers | the lockup rises out | — | — |
| 2.50 | — | **T-2** cut on the hand to a close-up of the three fingers | — | — | transition cue |
| 2.85 | "Number one" | cut to persona 1 | — | **SM-1 "#1."** in the caption band | — |

**Plan:**
| Section | t (s) | Spoken (gist) | Patterns and picture |
|---|---|---|---|
| PERSONA-1 | 2.9–12.5 | The overthinker: 40 tutorials, never lifts | GR-mono starts on the cut → the label duo "The **OVERTHINKER**" (z8) → **P-CHAOS-BURST** at 6.0–7.4 ("[Form check]", "[Program]", "am I doing it wrong", "[Day 1]", "too many") with a 4-cut flurry joined by single white frames, then at least 1.0 s clean → action shots of him scrolling on a bench → the punch duo "Still on **DAY ONE**" |
| PERSONA-2 | 12.5–22.0 | The ego lifter: heavier every week, form gone | "#2." → GR-amber → the label duo "The **EGO LIFTER**" → **P-UI-CHIP** search "heaviest deadlift ever" (light comedy) → detail run (chalk, plates, belt) → the punch duo "Doesn't care about **FORM**" |
| PERSONA-3 | 22.0–31.0 | The trend chaser: a new program every reel | "#3." → GR-teal → the label duo "The **TREND** CHASER" → **P-PHONE-REEL** of his own saved-reels screen capture with **P-INK-OVAL** on the caption |
| TURN (re-hook) | 31.0–35.5 | "The one who wins is the boring one." | Back to GR-warm on a white set (the grade ends on the cut) → **P-DUO-TITLE** "the **BORING** one" `rehook: true` |
| PAYOFF | 35.5–51.0 | Shows up, logs it, repeats | **P-FLOAT-CARDS** of four client check-in clips around him (the creator's assets, clear of his head) → **P-COUNT-UP** "312" + "SESSIONS" landing on "three hundred twelve" → talking piece with Z-2 |
| CTA | 51.0–59.5 | "Comment PLAN for my 4-week starter plan." | T-11 → **P-POSTER-BACKDROP** + **P-CTA-KEYWORD** "Just comment / **PLAN** / for the plan" 2.2 s → **P-SIGNOFF-SUN** "See you / **TOMORROW**" |
| BOOKEND | 59.5–61.0 | "Show up." | SH-1 pre-roll of the seated set; the last frame equals f0 |

How it breathes: about 40 cuts; three personas in three different grades, each opened by its marker and closed by its
punch duo; the chaos burst once, early, on the one line about overload; the turn sits near the middle and is the
quietest beat.

### 14.3 F-B tutorial, travel: "Edit travel photos on your phone in 4 steps" (72 s)
**Header:** F-B · HA-05 · tutorial · count 4 · SM-2 rule chapters · series "Travel Lab" ep. 03 (P-SERIES-LOCKUP) ·
sponsor: the editing app (P-LOGO-CHIP + P-DISCLOSURE) · CTA `link_bio` (P-END-BLOCK) · bookend SH-2 (overhead of the
creator at a river railing).

**Hook (0–3.6 s):**
| t (s) | Spoken | Picture | Type layer | Subtitle | Camera / cue |
|---|---|---|---|---|---|
| f0 | — | SH-2 overhead: the creator walks into the frame toward the railing | — | hidden | — |
| 0.38 | — | same | line 1 squash-in starts | — | hook cue |
| 0.45–0.70 | — | same | **EDIT TRAVEL PHOTOS / ON YOUR PHONE** squash in (Montserrat 900, line 1 ≈ 96 px, line 2 fitted smaller): readable by 0.7 s | — | — |
| 0.85 | "Your travel photos look flat," | he leans on the railing | the title holds | CS-1 starts | — |
| 2.40 | "here's the fix in four steps." | same | the title holds | — | — |
| 3.60 | — | **T-2** cut on his turn | the title blurs out | — | transition cue |

**Plan:**
| Section | t (s) | Spoken (gist) | Patterns and picture |
|---|---|---|---|
| SERIES | 3.6–4.8 | — | **P-SERIES-LOCKUP** "Travel / **LAB** / ep. 03" on W-grid |
| CONTEXT | 4.8–11.0 | "We're doing it all in one free app." | **P-LOGO-CHIP** "With <app>" (the sponsor's logo, theirs or fetched from the app's site) + **P-DISCLOSURE** "Paid partnership" for the whole sponsored span (4.8–58.0) → **P-SPIN-CARD** of "the photo I took in Lisbon" |
| RULE-1 | 11.0–22.0 | Remove distractions | SM-2 "REMOVE THE NOISE" (ink on W-paper) → **P-APP-DEVICE** (SH-8) → **P-LASSO** on the tourist behind her (12 f) → zoom into "Erase" (12 f) → a hard swap of the screen to the cleaned photo on "gone" |
| RULE-2 | 22.0–33.0 | Straighten and crop | SM-2 "STRAIGHTEN" → **P-LANDSCAPE-CARD** of the photo with **P-GUIDE-LINES** (thirds) + **P-INK-ARROWS** to the horizon → the device's crop step |
| RULE-3 (re-hook) | 33.0–44.0 | Lift the shadows | **P-DUO-TITLE** "This one **CHANGES** everything" `rehook: true` → the device zooms to the Shadows slider (1.0 → 1.8, 12 f) |
| RULE-4 | 44.0–55.0 | Warmth and a soft vignette | SM-2 "WARM IT UP" → the device slider → **P-CARD-CAROUSEL** of three more photos with the same settings |
| RESULT | 55.0–62.0 | "Before. After." | **P-BEFORE-AFTER-POLAROID** on W-grid: the before 1.2 s, a cut to the after on "after", held 1.8 s |
| CTA | 62.0–70.5 | "My preset is free, link in bio." | **P-END-BLOCK** "FREE / TRAVEL / PRESET / LINK / IN BIO" over SH-13 (a river-water close-up), 3.5 s |
| BOOKEND | 70.5–72.0 | "Go shoot." | SH-2 pre-roll: the empty railing from above, the creator about to enter; the last frame equals f0 |

How it breathes: about 38 cuts, with card swaps and slides declared as cuts; paper and the device carry the middle, and
the creator comes back on location between rules to show each one being used; the before/after is the peak, held longer
than anything before it.

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0 is a moving, composed shot from the creator's life; by the first cut the whole thesis has been seen, and it
  works on mute.
- Without the type, every frame is still a good shot; no card or word covers a great one.
- One yellow, only on words worth remembering; the script never carries a keyword.
- The picture keeps travelling with the voice: cuts hidden in motion, a detail for every listed noun, a new place
  whenever the story moves on.
- Paper appears only when a line shows something, and the reel steps back into the footage on the next opinion.
- Personas are told apart by their grades at a glance; the creator's answer is warm again.
- The curve is there: a dense hook, a calm setup, a quiet turn, a peak at the payoff, a confident CTA, a calm loop.
- The visible moves are moments, not habits: the flash on photos, the whip on real whips, the spin, the vortex and the
  zoom-through once each at most.
- Start to end, it feels like the creator's short film, and the loop makes you watch the start again.

**Craft (by eye, in context; the facts are in §2)**
- The person: the face reads whenever the moment is about them; front duo beats sit above the head or behind it; card
  titles off the faces in their clips; nothing chops a head or buries a face by accident.
- Behind-head words: most of the word visible for the whole hold, the first and last letters clear of the hair, one at a
  time, long enough to read, on a clean matte.
- No text over text by accident: one duo at a time, the subtitle out of the way under every z8 element, at most three ink
  marks.
- On the word: every block lands on its word; counters on the number word; ink on its word; no cut inside a block's rise.
- Every number on screen spoken or scripted, as digits; counts match the items and markers; the thesis paid off before
  the CTA; the CTA keyword readable; names spelt exactly; fetched posts and headlines word for word; ".." only on real
  pauses.
- CS-1: 54 px EB Garamond 600, pale lemon with the 1 px stroke and the hard shadow, one line, cy 1468, on every spoken
  word outside duo, chaos and morph spans.
- Yellow never on cream, white or greige; ink blocks on light worlds; a yellow block that's hard to read has its stroke
  or moved.
- No credit lines on inserts; private data blurred in screen recordings; a sponsored reel carries "Paid partnership"
  ≥ 2 s and says it.
- The chaos burst (if any): short, a handful of snippets around the face, subtitles hidden, a clean second after, not in
  the hook's first 2 s or the CTA.
- The last frame's picture equals f0's; no type fully visible on either.
- The file itself (1080 × 1920, 30 fps, −14 LUFS, a hard end ≤ 6 f after the last word, no black tail) is the render's
  job; it checks it.

---

## §16 Build notes
- **Fonts:** Anton, Montserrat (900), Nanum Pen Script, EB Garamond, Jost, Pinyon Script, JetBrains Mono, Noto Sans
  Devanagari, all bundled.
- **Determinism:** every frame is a function of its index; video frames come from `ctx.videoFrame(name, seconds)` only;
  no CSS animation in scenes.
- **Built in, no scene:** the flashes, the whip, the zoom-blur, the vortex and the blur-through (§9.5); the footage grade
  on camera footage (§4.3); the camera presets (§10.2).
- **Scenes you build:** each duo beat (§5.2 helpers), the B-roll `roll` scenes (§12.6), the paper cards, polaroids and
  devices, the ink (§8.6), the chaos burst (below). Persona grades on camera footage are `timeline.grades[]` spans
  (§4.3), not scenes.
- **Declare the cuts:** card swaps, carousel steps, riffle swaps and spins go in `cuts` or `transitions`, so the engine
  sees the picture changes inside one scene.
- **The chaos burst** (P-CHAOS-BURST): up to 45 f; 4–6 snippets around the face, not on it; the footage under it in
  GR-mono (carry `grade: "GR-mono"` on the burst scene for camera footage; the flurry's B-roll clips are `roll` scenes
  with `grade: "GR-mono"`, each 6–9 f, `cuts: [0]`, joined by the one-white-frame flash).
```js
// Snippets placed clear of the head region (check ctx.face() at planning time and move any that would come within 40 px).
const SNIPS = [{ t: "[Close Up]", x: 96, y: 380, f: "ui", s: 48, at: 0.00 }, { t: "am I doing it wrong", x: 520, y: 520, f: "serif", s: 64, at: 0.13 },
               { t: "[Wide]", x: 760, y: 300, f: "ui", s: 48, at: 0.27 }, { t: "[Day 1]", x: 120, y: 1180, f: "ui", s: 52, at: 0.40 },
               { t: "too many", x: 560, y: 1260, f: "serif", s: 70, at: 0.53 }];
VEOS.scene({ id: "chaos-1", t_in: 6.00, t_out: 7.40, z: 8, in: "none", out: "none", exception: "E2", snippets: SNIPS.length,
  grade: "GR-mono", text: true, text_class: "TC-label", text_content: SNIPS.map(s => s.t).join(" "), roles: [],
  box: { x: 64, y: 260, w: 952, h: 1080 }, events: SNIPS.map(s => s.at),
  render(ctx, lt) {
    return ctx.html(SNIPS.map(s => { const k = (lt - s.at) * 30; if (k < 0) return "";
      const e = Math.min(1, k / 3), dx = Math.round(20 * lt);
      return `<div style="position:absolute;left:${s.x + dx}px;top:${s.y}px;font:${s.f === "serif" ? "italic 500" : "500"} ${s.s}px ${ctx.fam(s.f)};
        color:${ctx.col("paper")};opacity:${(0.85 * e).toFixed(2)};filter:blur(${(6 * (1 - e)).toFixed(1)}px);text-shadow:0 2px 8px rgba(0,0,0,.6);white-space:nowrap">${ctx.esc(s.t)}</div>`; }).join(""));
  } });
```

---

## Appendix A. Evidence map
The full map (every element → `vNN @ m:ss`, the fidelity audit and the full-frame-rate motion pass) is in `evidence.md`.
Sources: five of OMGAdrian's reels (720 × 1280 at 23.98 fps, measured on a 1080 × 1920 upscale), 58–85 s each.

| What | Evidence |
|---|---|
| Duo titles: a yellow condensed block + white pen script, rise-smear beats | v01 @ 0:00–0:03, v02 @ 0:00.67–0:02.2, v05 @ 0:00–0:02.5 (`strip-hook-duo-blurslide.jpg`) |
| The pale-lemon serif subtitle at y ≈ 1468 | v01 from 0:04, v03 from 0:00.83, v04 from 0:02, v05 from 0:02.8 |
| Behind-head words; the poster and the sign-off sun | v02 @ 0:33, 0:38–0:40, 0:52–0:58; v05 @ 0:07 |
| The cream paper world, polaroids on grid paper, ink | v03 @ 0:11–0:36, 1:10–1:15; v04 @ 0:19–0:27; v01 @ 0:29–0:30; v02 @ 0:45–0:48; v05 @ 0:23–0:25 |
| Persona grades and the chaos burst | v02 @ 0:04–0:08 (mono), 0:09–0:17 (amber), 0:18–0:23 (teal) |
| The bookend loop, walk-in / walk-out | v01 @ 1:23 vs 0:00; v04 @ 0:00, 1:23; v05 @ 1:01 |
| Locked-off footage, the flashes, the whip, the zoom-through, the slow push | ORB motion pass, `strip-*.jpg` (v01, v02, v04, v05) |

Not verifiable from the reels: the speech language beyond English (read from burnt-in subtitles), the music bed, the
exact grade numbers (visual approximations), the presenter's on-screen time (estimated from 1 fps sheets).

## Appendix B. Hook-title bank
Duo split shown as **BLOCK** / script. Fill a template for each reel; write 8–10 and pick by §6.1.

| # | Template | Hook | For example |
|---|---|---|---|
| 1 | "[Doing X] **[ALONE / WRONG]** is why you **[STOPPED / FAILED]** at [point]" | HA-12 | "Training **ALONE** is why you **STOPPED** at week three" |
| 2 | "**[N]** types of **[GROUP]** people" | HA-12 | "**3** types of **GYM** people" |
| 3 | "Your **[MOMENT]** decides your **[RESULT]**" | HA-12 | "Your **MORNING** decides your **WORKOUT**" |
| 4 | "**[N] [UNITS]** / [no X / one Y]" (count-up) | HA-08 | "**52 CITIES** / one backpack" |
| 5 | "**[WORD.]** / **[WORD.]** / **[WORD.]**" over three details | HA-19 | "**RAIN.** / **RAMEN.** / **RESET.**" |
| 6 | "I **[STOPPED]** [doing] **[THING]**. **THIS** happened" | HA-12 | "I **STOPPED** booking **HOTELS**. **THIS** happened" |
| 7 | "The best **[THING]** in this [place] has **[NO X]**" | HA-12 | "The best **FOOD** in this city has **NO MENU**" |
| 8 | "When it comes to **[TOPIC]**, **[A]** is way **[BETTER]**" | HA-12 | "When it comes to **TRAVEL**, **SLOW** is way **BETTER**" |
| 9 | "Is your **[THING]** still **[BAD ADJECTIVE]** [your X]?" | HA-12 | "Is your **PHONE** still taking **BORING** travel photos?" |
| 10 | "[VERB] [OBJECT] / [PROMISE]" (title lockup) | HA-05 | "EDIT TRAVEL PHOTOS / ON YOUR PHONE" |
| 11 | "[FIX / BUILD] YOUR [THING] / IN [N] [UNITS]" | HA-05 | "FIX YOUR SQUAT / IN THREE CUES" |
| 12 | "[DO X] LIKE / A PRO IN [N] MIN" | HA-05 | "STRETCH LIKE / A PRO IN 5 MIN" |
| 13 | "[PLAN / PACK] [X] / [IN / FOR] [CONSTRAINT]" | HA-05 | "PACK ONE BAG / FOR TWO WEEKS" |
| 14 | "THIS DECISION / CHANGED MY [X]" | HA-05 | "THIS DECISION / CHANGED MY LIFE" |
