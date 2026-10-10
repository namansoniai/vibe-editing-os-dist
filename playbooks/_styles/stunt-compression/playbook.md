# Stunt Compression Style Playbook (template v2)

## The feel

This reel is a stunt you walk into halfway through. Frame 0 is someone already moving, already mid-sentence, a fat white
caption already on their chest: "I'M ABOUT TO". Before you've decided to stay, it has cut, and there it is: real cash in a
real hand, the amount typing itself onto the notes in neon green. You stay because something is at stake and it's
happening right now.

Then it compresses. A whole afternoon of chaos becomes less than a minute of only the moments that matter: the ask, the
answer, the verdict, the face. Every shot means one thing and ends the instant its peak has passed, because breathing is
where people scroll. Yet it never feels like a montage. The stunt has a spine, one question ("can they win it?") that opens
on the first word and stays open until the money changes hands. Each attempt is bigger than the last; past the middle the
stakes jump, and the cuts get faster all the way into the reveal.

The heroes are the faces. Every reveal is followed, almost instantly, by the face of the person who just won or lost:
hands on head, the scream, the hug. The host sets it up; the people taking part pay it off.

The graphics are almost nothing, and that's why they hit. Green means money and nothing else, pinned to the money itself.
Red means it's gone. Yellow means somebody is shouting. Captions get loud when the energy is up, drop to one small
lowercase word when it's intimate, and vanish when a number, a clock or the action says it better. No titles, no splits,
no cards, no outro: the frame is always the real event, and the reel stops on a face at its peak.

**The test:** pause on any frame and you can point at the stake or at the face it's happening to; if you can't, that
frame should have been cut.

## What this playbook is

You're editing a real stunt: a giveaway, a challenge, a street question, a timed task, a prank or a reveal, shot on two
or more cameras, with real money or a real prize on the line. You have the authority to make it the reel people can't
stop watching. This playbook is the style, pulled from four of MrBeast's shorts (v01 "Answer the call", v02 "Unlimited
money", v03 "Classroom quiz", v04 "College tuition") and measured at full resolution and full frame rate. Read it all,
every time; take what fits this stunt, invent where a moment needs more, and never break the feel above.

**Who it's for and what it needs.** Creators who stage things with real people and a real stake: giveaways, street
games, gym and sports challenges, classroom and workplace surprises. Input: 5–20 minutes of raw vertical footage per
minute of reel from cameras A (host), B (the people taking part), C (wide) and D (phone screens), with lav audio, plus the
creator's stake log (who got what, every amount, every clock value) and, when there's a sponsor, its logo (theirs, else
fetched from the sponsor's site). Nothing in this style can be generated: **the footage is the product** (§12). The cut-out is optional and only feeds the ghost
replay (P-34). Reels run about 40–75 s. Captions follow the creator's language (English verbatim by default; Hinglish
romanised; Hindi in Devanagari; §5.5). Machine values live in `tokens.json`; where this text gives a number tokens also
holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Compress, don't present.** Keep only the moments that tell the stunt, about a tenth of the shoot; every shot carries one meaning and ends when its action peaks; a long shot earns its length with something changing inside it | §1, §7.5, §12.4 |
| D2 | **Cold open mid-action.** No intro, no logo, no title card, no "hey guys": frame 0 is action plus a caption | §6.2, §2 |
| D3 | **The stake is a real object, and the number sits on it.** A tag shows the exact amount handed over, pinned to the cash or prize, never to an empty frame | §8.3 P-20, §8.5, §8.6 |
| D4 | **Cut to the face that wins or loses** within 6 frames of the reveal; reactions belong to the people taking part, not only the host | §9.3 R-03, §7.3 |
| D5 | **Hard cuts, and a tighter real angle first.** The camera has three measured moves only: a jump re-crop on the same take, an eased push into a reaction, a crash zoom on a crowd; no Ken Burns, no shakes | §9.1, §10.2 |
| D6 | **Caption mode is chosen per beat:** comic caps for hype and rules, yellow for shouts and the subjects' lines, neutral lowercase for intimate beats, none when a tag, the clock or the action carries the beat | §5.3 |
| D7 | **Colour has one job each:** green = money and gain, red = loss and no, yellow = a shout. The black-and-white hold and the green flash are the only colour events | §4 |
| D8 | **End on the reaction or the number.** No outro, no end card, no black tail; the CTA, if any, rides the final reaction | §6.7, §7.5 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style (moment selection is the craft) |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Worlds W-set / W-band, layouts L-full / L-wide-band, safe zones, the person |
| §4 | Colour system: green, red, yellow; the two colour events GR-bw / GR-green |
| §5 | Type and captions: CS-1 neutral, CS-2 comic caps, CS-3 yellow shout, CS-4 pink punch, mode none; tags, clock, other text |
| §6 | Hook system: stopper test, HA-13 Cold action, HA-14, HA-16, hook pairs, the stake line, CTA |
| §7 | Structure and rhythm: the stunt arc, the stake beat, open loops and the re-hook, rhythm by feel |
| §8 | Visual system (B-roll and patterns): families B-1…B-7, P-01…P-53, line → pattern lookup, money and truth, running state, anchors, comedy, sponsor, assets |
| §9 | Transition system T-00…T-05, grammar, shot grammar R-01…R-12, how the moves breathe |
| §10 | Motion tokens, camera Z-R1 / Z-R2 / Z-P1 / Z-C1, layers, finishing |
| §11 | Sound |
| §12 | Footage handling: the shoot brief, setups, shots and fallbacks, choosing the moments, inserts |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes: the money tag, the clock, determinism |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, cut, plan, build and look at the storyboard yourself; the reel and edit skills have the mechanics.
This style's craft is **moment selection**: out of a whole shoot, finding the few moments that tell the stunt, and putting them in an
order that keeps one question open until the money changes hands. Everything else serves it. The selection rules live in
§12.4, for the cut; when you come to the edit with the cut already made, read it with the same eyes.

1. **Log the moments and the stake.** Every continuous action with one meaning is a moment (§12.4: who, what, energy,
   face size, words). Mark the stake as it really happened: every amount, prize and clock value, exactly as said, shown or
   written in the creator's stake log. A money figure you can't trace to the speech or the log never goes on screen.
2. **Sync the angles.** Wherever two cameras caught the same moment (A on the host, B on the subject), sync them so an
   angle switch inside that moment keeps one continuous sound (§12.4).
3. **Map the stunt onto the arc** (§7.1): COLD OPEN → SETUP → ESCALATION → RE-HOOK → REVEAL → END. Name the one to three
   moments that carry each slot before you look at anything else.
4. **Build the reaction bank.** For everyone who wins or loses, find their best two to four reactions (shock, hands on
   head, a jump, a hug). The reaction cut (P-03) draws from this bank; it is the reel's emotional currency.
5. **Choose the register** (§5.3.6): comic, neutral or action, from how people actually talk in the footage. Then decide
   each beat's caption mode.
6. **Feel the tone of each beat:** `hype` (the stake line, the escalation) · `explain` (the rules) · `win` · `warn` (a
   loss, a no) · `awe` (the stake revealed).
7. **Write the hook** (§6): pick HA-13, HA-14 or HA-16 from the footage; write 8–10 stake lines and post titles, pick by
   the stopper test, keep two alternates.
8. **Plan the stake on screen:** every tag, gain, loss, total and clock value, with its figure and its provenance (§8.5);
   the state ops per beat (§8.6); which tags ride a moving object and need a track (§8.7).
9. **Place the punctuation:** the B&W hold before the verdict that deserves suspense, the green flash on the yes that
   deserves it, the camera moves on the reactions and the crowd, the rare whip (§4.3, §9, §10.2).
10. **Get the third-party files** (§12.6): the sponsor's logo (the creator's, else fetched from the sponsor's site), the
    phone recordings; note which fallbacks (§12.3) the reel runs on.
11. **Plan the sound** (§11): cues on the hook, the reveals and the whips; the real cheers stay loud.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the faces clear.** The faces are the heroes, so every face on screen (the host's, a subject's, a bystander's)
  keeps its head region (face, hair and the room above the head) clear of front layers: captions, tags, the chip, the X,
  name calls, logo pops, the clock, the sticker. The framing that does it: tags and chips 40 px off the head region,
  captions under the chin, no head under the clock (§3.6). A caption crossing a chin for a beat is editing; a reaction
  face buried by accident is not.
- **No text over text.** Captions hide while a money tag, loss tag, logo pop, brand type, name call or the clock is on
  screen; never two caption systems at once; never a caption over a tag.
- **On the word, on the action.** Tags, X flashes and logo pops land 1 f before the trigger word or on the visible action
  frame (the case opens, the cash touches the hand) and are fully on within ±5 f. Cuts sit on word boundaries ±1 f or on
  the action frame; inside a synced moment the sound runs continuously across the angle switch.
- **Money truth.** Every amount shown equals what was actually given, won, lost or stated, from the speech or the
  creator's stake log; totals equal the sum of their parts; prop or fake money is never tagged with an amount. A number
  the creator says is shown exactly as said.
- **State integrity.** A total never contradicts the last spoken or shown value and never decreases; the clock only goes
  down, may jump between cuts, and never jumps between two frames of one shot.
- **Number format.** `$10,000` / `₹1,20,000`, compact only from 1,000,000 (10,00,000) up; a `+` only on gains, never on a
  total (§5.5).
- **Promise integrity.** The stake named in the cold open is paid off on screen (handed over, won or lost) before the
  end; the CTA keyword, if chosen, is on screen ≥ 1.5 s.
- **Spelling.** The creator's name and handle, the sponsor, people's and place names exact in captions and type.
- **Readable.** Comic captions ≥ 84 px, neutral ≥ 54 px, tags ≥ 72 px, the clock ≥ 140 px, labels ≥ 40 px, the legal
  line ≥ 22 px; contrast ≥ 4.5:1 (3:1 for display text ≥ 96 px), carried by the 5–10 px ink stroke on busy footage.
- **Privacy.** Phone numbers, emails, bank details and addresses on any phone screen are blurred for their whole time on
  screen.
- **Audio.** −14 LUFS integrated, true peak ≤ −1.5 dBTP, the bed ≥ 20 dB under speech; the reel ends ≤ 6 f after the last
  reaction or word, no black tail.

**Never in this style:**
- An intro: a title card, a logo sting, "welcome back", a channel animation or a black frame before the action.
- A headline banner, pill, lower-third or chapter marker anywhere in the reel.
- Split screens, cards, panels, picture-in-picture or a canvas world: the frame is always footage.
- A tag on an empty frame, a tag that floats away from its object, or a number that isn't on the money, prize or person it
  describes.
- Ken Burns, slow drifts on wides, shakes, rotations; zooms on the host's talking lines; glitch, RGB-split and film-burn
  packs, light leaks, wipes and crossfades. The camera's language is the real tighter angle and the three measured moves
  (§10.2); invent inside it.
- Coloured caption words except the money word in green; yellow on host lines that aren't shouts; pink outside a
  neutral-register reel.
- Stock footage, AI-generated people or money, "money rain" overlays: every frame of money is the creator's real stake.
- A made-up balance, payout or follower count presented as a real moment. A recreated screen only stands in for something
  that really happened, with the words from the transcript (§12.3 FB-8).
- Holding a shot past its action "to breathe"; a reaction that plays on after its peak.
- Colour events back to back, or a green flash longer than 10 f.
- Meme sounds, laugh tracks, record scratches (the comedy is light and lives in the footage).
- An outro, end card, subscribe animation or slate after the last reaction.
- Dead air: a gap over 0.6 s with no speech **and** no visible action is cut. A picture-led gap while the action continues
  is fine.

---

## §3 Worlds, layouts, stage moves, safe zones

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-set** | `footage` | The stunt's real location exactly as shot: daylight or bright practicals, ungraded, natural saturation | The whole reel's picture | Hard cut only |
| **W-band** | `footage` | A blurred, darkened copy of the same clip behind a horizontal shot (blur 40 px, brightness 0.55) | Only horizontal wides from camera C (L-wide-band) | Hard cut in and out |

There is no canvas, data stage, paper or void world. A frame without footage never exists in this style.

### 3.2 Layout library
| ID | Engine | The picture | Graphics | Caption | Treatment |
|---|---|---|---|---|---|
| **L-full** | `full` | Full frame 0, 0, 1080, 1920: any person, any camera | The whole frame; tags sit on their objects | `chest` anchor: the caption's top sits 30 px under the chin of the face on screen; with no face found it sits at its profile's cy (CS-2 / CS-3 1000, CS-1 940, CS-4 900) | none |
| **L-wide-band** | `blurfill` | A 16:9 band 1080 × 608 at cy 960 (y 656–1264) over its own blurred copy | Inside the band | `fixed_y` cy 1380 (below the band) | blur 40, luma −0.45 |

L-full is the reel. L-wide-band exists only for a horizontal camera-C clip that can't be cropped to 9:16 without losing
the subject (FB-5). It's a compromise frame, so it's a visit: in on a cut, out on the next as soon as the scale has read
(about two seconds at most).

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-0** | Cut | `via: cut`, 0 f | every layout change; the only stage move of the style |

No panel drops, pop-backs, shrinks, slides or morphs exist in this style. What moves is the footage itself.

### 3.4 Layout diagrams (1080 × 1920)
**L-full** (the reel):
```
┌──────────────────────────────┐ 0
│   IG top UI: no text         │ y 0-110
│        ┌─────────┐           │
│        │  0:58   │  P-24     │ clock box y 205-375 (cy 290), x 290-790; no head under it
│        └─────────┘           │
│      ( faces: y 250-800 )    │ host/subject heads usually here; keep their head region clear
│  HOLY GOD!   (P-36 / CS-3)   │ a name call beside a low or small head, not over it
│        $10,000   (P-20)      │ tag band y 560-1460, ON the object, 40 px off every head
│      I'M ABOUT TO  (CS-2)    │ chest: caption top = chin + 30 (cy 1000 / 940 with no face)
│      [ LOGO POP  cy 1000 ]   │ P-30 / P-31 brand, w 760-900
│ Paid partnership (legal)     │ x 64, y 1450-1480
│   IG bottom UI: no meaning   │ y 1540-1920
└──────────────────────────────┘ 1920
```
**L-wide-band** (horizontal C clip):
```
┌──────────────────────────────┐ 0
│  blurred copy (luma -0.45)   │
│        0:46  (if clock run)  │ cy 290
├──────────────────────────────┤ y 656
│   16:9 wide: the set/crowd   │ band 1080 x 608, cy 960
│      $50,000 tag on pile     │ tags stay inside the band
├──────────────────────────────┤ y 1264
│      CAPTION cy 1380         │
│  blurred copy                │
└──────────────────────────────┘ 1920
```

### 3.5 Safe zones and bands
- **Meaning-text box:** x 64–1016, y 110–1500; between y 900 and 1540 nothing with meaning goes right of x 970 (Instagram's
  button column).
- **Caption band:** the chest (above). Measured on the reference reels: comic captions cy 800–1140, neutral cy 885–935,
  always on the chest of a person whose face fills 8–25 % of the frame.
- **Clock band:** y 205–375 (cy 290). **Tag band:** y 560–1460. **Chip band:** y 700–1300. **Legal line:** y 1450–1480 at
  x 64.
- **Brand band:** logo pop or brand type centred cy 1000; when a face sits in y 800–1200 it moves to cy 330 (the top band)
  and the clock is off for that beat, provided no head reaches into the logo's box; if one does, the logo waits for the
  next cut.

### 3.6 The person
In this style "the person" is every face in the frame: the host, the people taking part, the friend screaming in the back.
Keep the head region (face, hair and the room above the head) clear on all of them, judged by eye on the storyboard.
- **Captions sit under the chin.** The `chest` anchor puts the caption's top 30 px below the face box's bottom, and the
  engine moves any caption that would touch a head region off it (`avoid_face`). In a two-shot the caption goes under the
  lower chin; in a crowd frame, captions are off anyway (§5.3.6). There are no forehead captions in this style:
  captions live under the chin, not above or across a head.
- **A low face.** When a chin sits so low that the chest band falls out of the safe zone (below about y 1370 for a one-line
  comic chunk, y 1280 for a two-line one), that beat goes caption-less, or a shout becomes a P-36 name call beside the head.
- **A close selfie** (face box over 30 % of frame height): the chest band is under the chin, so captions sit at fixed_y
  cy 1180–1300, not above the head.
- **The clock** owns x 290–790, y 205–375, and camera A puts the host's head top anywhere in y 120–420. During a clock run,
  choose shots whose heads sit below y 415 or outside x 250–830; a shot that would put a head under the clock either stays
  out of the run or the clock leaves on the cut before it (it jumps on cuts anyway).
- **Tags, chips, the X, name calls:** 40 px off every head region (§8.7). The gain tag sits on the chest (face bottom +
  140 px); the chip and the name call sit beside the head, off the hair and the room above it.
- **Crops:** in close-ups the face is 18–35 % of the frame height with the eyes at y 520–760; in two-shots both heads sit
  between y 220 and 820; re-crops (FB-2) keep the eyes inside y 480–800.
- **Return to a face** is always a hard cut, never a move.
- **No cut-out layer** except the ghost replay (P-34). Behind the person is fair game in principle; this style simply has
  nothing there.

A face is never more than a beat away: an insert of the money or a phone screen is a glance, then back to someone's
face. For reference, a face was on screen about 85 % of the time in the four reels, and the longest stretch without one
was a two-second cash-pile insert or a phone screen.

---

## §4 Colour system

### 4.1 Role palette
| Role | Hex | Its one job | Text on it |
|---|---|---|---|
| `good` | `#39FF14` | Money and gain: P-20 / P-21 / P-23 tags, the money word in a comic chunk, P-25 object glow, P-51 green flash | `ink` (15.5:1) |
| `bad` | `#E5191B` | Loss, zero, wrong: P-22 `$0`, P-27 X flash, the clock at 0:00 | `paper` (4.7:1; as text it always carries a 6 px white stroke) |
| `accent` | `#FFE600` | Shout yellow: CS-3 lines (the subjects' lines and exclamations), P-36 name calls | `ink` (16.6:1) |
| `primary` | `#1179CB` | The creator's own colour: P-26 chip ring and avatar, P-29 avatar badge, P-35 keyword sticker fill | `paper` (4.6:1) |
| `punch` | `#F34FF7` | The one CS-4 pink punch word in a neutral-register reel (sampled v01 @0:30.5, the glyph core) | `ink` (as text fill: a black stroke) |
| `paper` | `#FFFFFF` | Caption fill, clock fill, chip fill, brand in type | — |
| `ink` | `#000000` | Every stroke (5–10 px) and hard shadow | — |
| `money_edge` | `#0A3A06` | The 5 px inner stroke of money tags | — |

Measured fills on the reference tags (recipe colour, not roles): the money glow core `#94FF6C`, `+$3k` `#19FF56`,
`$14,000` lime `#73FF12`, the `$0` red `#E90005` with a white outline. Gradient `glow_good` (`#B6FF9E` → `#39FF14` →
`#1FB80A`) lives in tokens. A creator's brand colour replaces `primary` (and a light warm hue may replace `accent`);
`good` and `bad` never change.

### 4.2 Meanings
- **Green = money changes hands or is won. Red = it doesn't, or it's gone.** The axis of every reel is green ↔ red; green
  never marks anything that isn't money or gain.
- **Yellow = someone shouts** (a subject's line, an exclamation, a name call). It never marks money.
- **The creator's colour (`primary`) appears only on the creator's own furniture** (handle chip, avatar badge, keyword
  sticker).
- **Brand colours appear only inside the sponsor's own logo file** (P-30) and the real product.

### 4.3 Grades: the two colour events
**Footage grade: none.** Footage is never regraded; only exposure and white balance are matched between cameras A, B and C
of one moment, so an angle switch doesn't jump in colour.

| ID | Name | Recipe | Frames | When | Evidence |
|---|---|---|---|---|---|
| **GR-bw** | B&W hold | z11 light-pass scene: a full-frame `#808080` fill with `mix-blend-mode: saturation` (everything below turns greyscale; tokens: `grayscale(1) contrast(1.12)`); hard in with a Z-R1 jump re-crop 1.13× on the same take (or on a cut) and a slow push (+0.3 % a frame) through the hold; hard out on the next cut; captions off or CS-1 white only; no tags under it | 24–45 (0.8–1.5 s) | **suspense:** the subject reads the phone, waits for the answer, the case is about to open | v04 @ 0:06–0:07 |
| **GR-green** | Green flash | **built-in flash transition** (no scene): `{"t": <moment>, "type": "flash", "colour": "good", "peak": 0.6, "pre": 0, "frames": 10, "decay": 0.5}` in `timeline.transitions`; peak on the moment, near 0.6 for the first ~5 f, gone by f9 | 6–10 | **yes / confirmed / won:** the follow tap lands, the answer is right, the money is handed over | v04 @ 0:12 |

GR-bw is live, not a freeze (measured v04 @ 6.40: the footage keeps moving). Declare each GR-bw in `timeline.grades`
(`{"t": 6.10, "id": "GR-bw", "dur": 1.2}`) so the timeline knows it; GR-green is its `flash` transition entry.

These two are punctuation. The B&W hold is the held breath before a verdict, the green flash is the yes. Spend them on the
moments that turn the reel, with air around each one, never back to back, so each still lands as an event.

### 4.4 Rules
- A frame holds at most three bright hues: a green tag, a yellow shout and a sponsor logo is the limit.
- Coloured text always carries an ink or paper stroke (5–10 px): footage is busy and bright.
- No tint, vignette, grain, bloom or LUT on footage outside GR-bw and GR-green.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family (bundled) | Weight | Used for |
|---|---|---|---|
| `chunky` | **Bangers** | 400 | CS-2 comic captions, CS-3 shouts, P-36 name calls, P-35 keyword sticker |
| `body` | **Inter Tight** | 700 / 800 | the handle chip (700), the URL line (800) |
| (direct) | **Poppins** | 600 / 700 | CS-1 neutral captions (600) and the CS-4 punch word (700): both profiles set Poppins directly |
| `numeric` | **Lilita One** | 400 | money and loss tags, running totals, the clock |
| `display` | **Montserrat** | 900 | P-31 brand in type |
| `ui` | **Inter Tight** | 600 | the disclosure line |

The comic and numeric faces in the evidence are closest to Bangers and Lilita One (unverified: the originals may be
licensed faces). The source comic face is a wide italic (Komika Axis-like); Bangers is narrower. Logos are image files,
never fonts.

### 5.2 Headline element
None (`type.headline.kind = none`; frame 0 forbids a headline). The cold-open caption is the only text at f0.

### 5.3 Caption system profiles

#### 5.3.1 CS-1 Neutral (`extends: lib:mrbeast_neutral`)
| Group | Value |
|---|---|
| Mode | full / support / mute-safe |
| Chunking | `unit: word`, 1 word per chunk, ≤ 16 characters; never split a name, number or unit (a number with its currency is one chunk: "$10,000"); end punctuation stripped |
| Timing | lead 1 f; min hold 0.13 s (4 f) per word, as spoken (measured v01 0.07–0.37 s: "are" 5 f, "you" 4 f, "subscribed" 16 f); tail 0.10 s; **hard swap** (`exception: E6`: the word is fully on in its first frame); no pause hold (a long pause clears the word); the f0 caption may start 2 f in |
| Skin | **Poppins 600, 64 px**, lowercase, tracking 0, `paper`, **5 px black stroke** (audit v01 @0:00.4 "subscribed": a wide geometric bold with a solid black outline, ascender band 52 px, 356 px wide, cy ≈ 934), shadow `0 2 6 rgba(0,0,0,.5)`, no container |
| Position | `chest` (top = chin + 30 px), **cy 940** with no face; centred x 540, max width 900; `avoid_face` |
| Emphasis | none (the punch word uses CS-4) |
| Hide | under z8 (logo pop, brand type, keyword sticker); by override during tags, the clock, name calls and GR-bw |
| Language | Latin; keep English terms; no spelling normalisation; profanity mask `inner` (`f**k`) |

#### 5.3.2 CS-2 Comic caps (`extends: lib:mrbeast_comic`): the default register
| Group | Value |
|---|---|
| Chunking | `unit: group`, **1–5 words**, ≤ 20 characters a line, 1 line (2 when the money word stacks under its noun: "UNLIMITED / MONEY"); single-word chunks are common on fast speech ("WE'RE" → "GONNA" → "KIDNAP", "COST?"); punctuation kept ("QUESTION...", "TO :)"); audit v04 @0:02.9 "CAN I SEE IF YOU'RE" (5 words, 19 characters) |
| Timing | lead 1 f; min hold 0.15 s per word; tail 0.10 s; **`reveal: word`, swap `pop` 2 f** (each new word scales 0.5 → 1.05 → 1.0 in 3 f; measured v02 @0.93 "MONEY", v02 @4.08 "WE'RE"); chunk-to-chunk changes read as hard (v04 @1.60). A chunk keeps running across a hard cut inside its sentence (v04 @1.30) |
| Skin | Bangers 400, **96 px**, UPPER, tracking 0.02, `paper` fill, **10 px `ink` stroke** (audit: v04 @0:00.6 "ASK PEOPLE", cap 65 px; @0:02.9 cap ≈ 72 px, 5 words on one line), soft shadow `0 3 6 rgba(0,0,0,.5)`, **no rotation** (white comic chunks sit level; only the yellow shout tilts), line height 1.0 |
| Position | `chest` (top = chin + 30 px), **cy 1000** with no face; centred, max width 920; `avoid_face`. Measured: v04 @0:00.6 cy ≈ 920, @0:02.9 ≈ 800, v02 @0:00.6 ≈ 1140. Close selfie: §3.6 |
| Emphasis | `colour`: the money word or number in the chunk turns **`good`** ("UNLIMITED / **MONEY**"); a subject's spoken amount alone in the chunk is the same green word, on their close-up (v04 @15.10 "$14,000", on with the cut); `select: number`, plus the planner's `{i, emph: true}` on money nouns (money, cash, prize, the amount word); one money word a chunk at most (`max_per_chunk: 1`, `max_per_s: 0.5`) |
| Hide | as CS-1 |
| Language | as CS-1 |

#### 5.3.3 CS-3 Yellow shout (`extends: lib:mrbeast_comic`)
| Group | Value |
|---|---|
| Use | **(a) every line spoken by a subject (not the host)** and **(b) every exclamation by anyone** ("HOLY GOD!", "SERIOUS!", "YEAH! :D"). Selected by planner overrides `{t: [a, b], profile: "CS-3"}`. Inferred from the colour use in v02 and v04 (unverified) |
| Chunking | 1–3 words, ≤ 14 characters |
| Timing | lead 1 f; min hold 0.30 s per word; tail 0.12 s; pop 2 f, or fully on with the cut to the shouter (v04 @2.00 "HOLY"); pause hold 0.4 s (a shout lingers) |
| Skin | Bangers 400, **112 px**, UPPER, tracking 0.02, **`accent` fill**, 10 px `ink` stroke, soft shadow `0 3 6`, **rotate −8°** (measured −10° on "HOLY" v04 @2.00; a calm subject line like "I'M LIKE..." may sit level, 0°) |
| Position | `chest`, cy 1000 with no face. A shout over a wide shot whose speaker is small or off-centre is not a caption: it's a P-36 name call beside the speaker's head, with the captions hidden for it |

#### 5.3.4 CS-4 Pink punch (`extends: lib:mrbeast_neutral`)
| Group | Value |
|---|---|
| Use | Only in a **neutral-register reel**: the single funniest or most surprising word of a beat ("god", "beast!"). It's a surprise, so it stays rare: when it's everywhere it's nothing |
| Skin | **Poppins 700, 96 px**, lowercase, `punch` `#F34FF7` fill, **7 px black stroke**, shadow `0 3 6 rgba(0,0,0,.45)` (audit v01 @0:30.5 "god": the same geometric face as CS-1 in magenta, with a black outline) |
| Timing | 1 word (≤ 12 characters), pop 2 f, min hold 0.3 s |
| Position | `chest`, cy 900 with no face |

#### 5.3.5 Mode `none`
Captions hidden by `captions.overrides {t: [a, b], hide: true}` (or a `captions.hide` range), on the beats in 5.3.6. A
hidden span still passes the mute test when it matters: a tag, the clock, a sign in the footage or the next caption carries
the meaning.

#### 5.3.6 Per-beat caption mode
**Reel register** (one for the reel, `timeline.captions.profile`):
| Register | Default profile | When | Evidence |
|---|---|---|---|
| **Comic** (default) | CS-2 | The host pitches the stunt to camera: giveaways, challenges, sponsored stunts, any reel whose cold open is a stake line | v02, v04 |
| **Neutral** | CS-1 | The reel is built from normal-volume conversations with strangers: street questions, phone calls, surprises told quietly | v01 |
| **Action** | CS-2, hidden on most beats | Speech is crowd noise, children or chants, or the stunt explains itself through tags, a clock or a sign; the host's rule lines and the shouts keep captions | v03 |

**Per beat** (overrides on top of the register):
| Beat | Mode | Profile |
|---|---|---|
| Host stake line, rules, escalation line | comic (neutral in a neutral reel) | CS-2 / CS-1 |
| A subject's line; any exclamation; a cheer word | shout | CS-3 (in a neutral reel: CS-1, or CS-4 for the one punch word) |
| A money tag, loss tag, logo pop, brand type or name call is on screen | **none** | hide |
| The clock is on screen | none; if a rule is spoken, CS-2 at cy 1000 (heads clear) | hide / CS-2 |
| GR-bw hold | none (or CS-1 white) | hide / CS-1 |
| Crowd chaos, unintelligible speech, a phone screen with readable text | none | hide |
| The last reaction (end) | none, unless it's a short clear line ("THANK YOU") | hide / CS-3 |

#### 5.3.7 Overrides in the timeline (never hand-written cards)
```json
"captions": {"subtitles": "auto", "profile": "CS-2",
  "overrides": [
    {"t": [2.70, 3.40], "profile": "CS-3"},
    {"t": [15.00, 16.20], "hide": true},
    {"i": 7, "emph": true},
    {"t": [30.40, 30.90], "profile": "CS-4"}],
  "hide": [[36.0, 47.5]]}
```

### 5.4 Other text
| Element | Recipe | Hold |
|---|---|---|
| **Money tag** (P-20 / P-21 / P-23) | Lilita One 400, **112 px** by default (by object size: 112 for an object ≥ 300 px wide on screen, 96 for a smaller one, never under 72, max 150; audit v01 @0:15.2 `$10,000` ≈ 370 px wide with its glow, cap ≈ 80 px; v04 @0:15.2 `$14,000` 286 × 75), `good` fill, 5 px `money_edge` stroke, glow `0 0 22px` + `0 0 6px` in `good`, hard shadow `0 6 0` 55 % black; `$10,000` style; gains carry `+`; **enters by type-on** (P-20) | 0.6–2.2 s; ends on the cut (v01 @15.0–17.13 held 2.1 s) |
| **Loss tag** (P-22) | Lilita One 122 px, `bad` fill, 6 px `paper` stroke, shadow `0 6 0` 70 % black | 0.6–1.4 s |
| **Clock** (P-24) | Lilita One **170 px**, `paper` fill, **9 px `ink` stroke + a soft dark outer glow** (`0 0 18px` 70 % black; measured v02 @36.3), `M:SS`, centred x 540, cy 290; the first value carries a `good` glow (`0 0 22px`) that drops at the next cut (v02 @36.0); digits hard-swap (`exception: E6`), ticking once a second inside a shot (v02 @36.47 0:59 → 0:58) | the clock run |
| **Brand in type** (P-31) | Montserrat 900 caps 96–128 px, `paper`, 6 px `ink` stroke, shadow `0 6 0` | 0.8–1.4 s |
| **URL line** (P-32) | Inter Tight 800 caps **64 px**, `paper`, 4 px `ink` stroke | ≥ 1.5 s |
| **Handle chip** (P-26) | white pill h 96, radius 48; avatar Ø 112 overlapping its left end with a 5 px `primary` ring; the creator's handle in Inter Tight 700 **44 px** `ink` | 0.5–0.9 s |
| **Name call** (P-36) | Bangers 72 px caps, `accent`, 6 px `ink` stroke, rotate −6° | 0.5–0.8 s |
| **Keyword sticker** (P-35) | Bangers 120 px caps, `paper` text on a `primary` rounded slab (radius 22, padding 12 / 30), 7 px `ink` stroke on the text, rotate −4° | 1.5–2.5 s |
| **Disclosure** | Inter Tight 600, 26 px, `paper`, shadow `0 2 4` 80 % black, at x 64, y 1450 | ≥ 2 s from the first sponsor beat |
| **X flash** (P-27) | two 34 px-thick `bad` strokes forming an X, 200 px, red glow 26 px (the reaction carries the meaning) | 15–24 f, to the cut |

### 5.5 Language and numbers
- **Spelling:** captions are verbatim speech; brand names, the creator's name and handle are exact (glossary). Shouted
  fillers keep their spelling ("NOOO", "BRO").
- **Hinglish** (Hinglish speech, Hinglish captions, Latin): romanised Hinglish in caps for CS-2 / CS-3 ("YE ₹10,000
  TUMHARE"), lowercase for CS-1. **Hinglish speech, English captions:** translate each line to short spoken English, 1–4
  words a chunk.
- **Hindi** (Devanagari): Bangers and Lilita One have no Devanagari, so CS-2 / CS-3 render in **Noto Sans Devanagari 800**
  with the same stroke, shadow and rotation and no case change; CS-1 renders in Noto Sans Devanagari 600. Money tags keep
  Latin digits in Lilita One.
- **Numbers:** international `$10,000` by default; Indian creators get `₹1,20,000` grouping. Compact (`$1.2M`, `₹12 L`)
  only from 1,000,000 / 10,00,000 up. Gains are `+$3,000`, never `+$3k`. The `₹` glyph draws from a font-stack fallback
  (`Lilita One, Inter Tight`); check it on the storyboard (no empty boxes).
- **Spoken number words** ("ten thousand", "das hazaar") become digits on tags and captions.

---

## §6 Hook system

There is no on-screen title in this style. The hook is the stunt itself: a person already in motion saying the stake out
loud, with the stake on screen a second later. The words that hook are the **stake line**, spoken by the host and shown
by the captions, and the **post title**. Both promise something real: a sum, a prize, a test someone might pass or fail,
true to what the reel pays off ("Hold 60 Seconds, Win $500", not "Gym Challenge"). Write 8–10 stake lines and titles, pick
by the stopper test, keep the next two as alternates.

### 6.1 The stopper test
| Test | In this style | How it's met |
|---|---|---|
| Mute | the first 3 s tell who, what's at stake, and that it's happening now | the stake line in comic caps + the stake object or the first reaction by 2.3 s |
| Motion at f0 | a person or the stake is visibly moving on frame 0 | SH-1 walk-and-talk (or the moving pile, the hands) |
| Payoff | the stake (money, prize, the pile, the clock) or the first big reaction is on screen by 2.3 s | the scene tagged `payoff: true`: a money tag, the object glow, the stake insert or the first big reaction |
| Read | the first caption chunk reads in ≤ 1.0 s | 1–4 words |

The first three seconds feel dense: the walk, the caption swapping, the cut, the tag typing on, the face. Dense in time,
never in space: each thing lands while the last one settles.

### 6.2 HA-13 Cold action (default)
Frame 0 = a moving subject + a caption; first cut by 2.1 s; the money or the object by 2.3 s. Evidence: v04 (cut 1.30,
"HOLY GOD!" 2.0), v01 (cut 1.47, chip 0.83, X 1.5), v02 (cut 1.53, MONEY 1.0, logo 2.33).

| t (s) | Visual | Caption | Layout / camera | Graphics / state | Cue moment |
|---|---|---|---|---|---|
| **f0** | SH-1: the host mid-stride, already talking to camera (or to the subject beside him); the location readable behind | CS-2 first chunk **already on screen** ("I'M ABOUT TO"); the first word starts ≤ 3 f in | L-full; no camera move | none | one hit on the first chunk pop |
| 0.0–1.3 | same shot; the stake line continues; chunks swap every 0.3–0.5 s | CS-2 1–5 words a chunk; the money word in `good` ("WIN **$10,000**") | — | P-26 handle chip if the creator's channel is named (0.5–0.9 s, beside the subject's shoulder) | silent (caption pops never carry cues) |
| **1.0–2.1** | **first hard cut** (P-02) to a second angle of the same moment, or to the subject the line is about | CS-2 continues across the cut (same sentence) | cut (R-08 if synced) | — | — |
| **1.5–2.3** | **payoff:** the stake as an object (P-06) with its P-20 tag, or the subject's first big reaction (P-03) with a CS-3 shout | CS-3 for the shout, else hidden under the tag | cut; Z-P1 push when it's a reaction (v01 @1.48) | P-20 tag `payoff: true` (or P-25 glow, or P-27 X blur-in) | one reveal cue on the tag |
| 2.3–3.0 | third shot: a reaction (R-03) or the establishing wide (P-05) | CS-2 / hidden | cut | — | — |
| 3.0–6.0 | SETUP: the rule of the stunt in a few quick cuts | CS-2 | cuts on the words | — | — |

### 6.3 Alternate hooks

**HA-14 Cold authority:** a caption at f0 over the strongest image of the reel, which is on screen by 1 s. Evidence: v02
(the host in front of the cash waterfall, "THIS IS UNLIMITED MONEY" from f0).
| t | Visual | Caption | Graphics |
|---|---|---|---|
| f0 | the biggest image of the shoot: the pile, the prize wall, the crowd, with the host in it | CS-2 "THIS" → "IS" (1-word chunks, 0.15–0.35 s) | — |
| 0.6–1.4 | same shot | CS-2 two-word stack with the money word in `good` ("UNLIMITED / MONEY") | — |
| 1.5 | first cut, closer on the stake | hidden | P-20 tag or P-30 logo pop (sponsored) by 2.3 s, `payoff: true` |
| 2.3–3.0 | a reaction or the host's next line | CS-2 | — |

For example: "THIS IS ₹1,00,000 IN COINS" over the pile.

**HA-16 Diegetic / object open:** no caption needed at f0: a moving subject, and the stake shown fast (by 2.3 s in
practice). Evidence: v03 (the host holding a bucket of cash, glow on the stack at 1.67, walk-away cut at 2.13).
| t | Visual | Caption | Graphics |
|---|---|---|---|
| f0 | the host holding the stake close to camera, talking or gesturing | hidden (the first words aren't the stake line) or CS-2 if they are | — |
| 1.0–1.7 | the host lifts the stake toward camera | — | **P-25 object glow** on the stake, `payoff: true` |
| 2.1 | **P-11 walk-away reveal**: cut to the host walking into the location from behind | — | — |
| 3.0–4.0 | the room reacts (P-04) | CS-3 on the loudest shout | — |

For example: the host holds the trophy and the stopwatch at the edge of the field, the trophy glows, he walks on.

Use HA-13 unless (a) the shoot has one image so big it beats any walk-in (HA-14), or (b) the host's first words aren't
usable as a stake line (HA-16).

### 6.4 Hook pairs by topic (subject → reveal)
Write the pair for each new reel in this form: what's moving on frame 0, and what the stake reveal is.
| Topic | First subject at f0 | The reveal |
|---|---|---|
| "Name my shop, win ₹5,000" | the host walking up the market lane toward a stranger, envelope in hand | the envelope opens: notes + P-20 "₹5,000" on them by 2.2 s |
| "I'll pay your bill if you can guess it" | the host at the billing counter beside a customer | the receipt in close-up + P-20 tag on the total by 2.0 s |
| "Guess the price, keep the product" | the host holding the product up to a passer-by | the product + its price tag (P-20) by 2.3 s |
| "Every right answer = +₹500" | the host with a cash stack facing a group | the first answer + P-21 "+₹500" on the subject by 2.3 s |
| "Hold the bar 60 seconds, win $500" | a subject gripping the pull-up bar, the host beside with cash | P-24 clock "1:00" + P-20 "$500" on the cash on the bench by 2.3 s |
| "Every rep = $10" | an athlete mid-rep, the host counting | P-21 "+$10" on the athlete by 1.8 s |
| "Beat my 100 m time, win my shoes" | the host lacing the shoes on the track | the shoes in close-up + P-20 price tag by 2.2 s |
| "Last one standing keeps the prize" | a line of people in a plank, the prize on the floor | the prize insert + P-20 tag by 2.3 s |

### 6.5 The stake line and the post title
- **Stake line formula:** `[I'm about to / If you … / Whoever …] + [the stake with its number] + [the condition]`, ≤ 14
  words, spoken in ≤ 3.5 s. "If you can name my shop, this ₹5,000 is yours"; "Whoever holds this bar for 60 seconds wins
  $500".
- **Templates:** *Offer* ("If you can X, you win Y") · *Countdown* ("You have N seconds to X") · *Escalation* ("Every X =
  +Y") · *Surprise* ("I'm about to pay for X") · *Choice* ("X or Y, you pick").
- **Post title:** `[Action], [Win/Keep] [stake]` in Title Case, ≤ 8 words: "Name My Shop, Win ₹5,000"; "Hold 60 Seconds, Win
  $500".
- The number in the line is the number on the tag. No promise the reel doesn't pay; never "you won't believe".

### 6.6 Hook sound
One cue on the first caption pop at f0 and one on the payoff tag (§11). The bed runs from f0 under the speech.

### 6.7 CTA
By default the reel ends on the reaction with nothing after it (none of the four reference reels has a CTA).
| Device | Spoken | On screen | Hold | Where |
|---|---|---|---|---|
| `none` (default) | — | — | — | — |
| `post_only` | — | nothing; the CTA lives in the post caption | — | — |
| `comment_keyword` | "Comment KEYWORD and …" over or right after the final reaction | **P-35 keyword sticker** over the last reaction shot, never a separate card | 1.5–2.5 s | the last 2.5 s, after the stake is paid |
| `link_bio` | "Link in bio" | **P-32 URL line** "LINK IN BIO" at cy 300 (top band) over the final reaction, heads clear | ≥ 1.5 s | the last 2 s |

No silence is added before the CTA (the sound rules keep 1.0 s cue-free before it). The CTA never delays the hard end by
more than 2.5 s.

---

## §7 Structure and rhythm

### 7.1 Structure: the stunt arc
| Section | What happens | How it plays | Evidence |
|---|---|---|---|
| **COLD OPEN** | §6.2: action + the stake line + the first cut + the payoff by 2.3 s | over in about three seconds | all four |
| **SETUP** | the rule of the stunt and who's playing | the one calmer stretch: a wide, the host's rule, a face or two | v03 @ 0:03–0:12; v02 @ 0:02–0:06 |
| **ESCALATION** | the stake beats (§7.3) one after another, each bigger or closer to the end | the body of the reel; reactions dominate | v03 @ 0:12–0:48; v01 @ 0:05–0:27 |
| **RE-HOOK** | one escalation beat: a second stake, a doubled prize, the clock starting, the room or pile reveal (§7.4) | a wide or the stake insert, then fast again | v02 @ 0:27–0:36 (vault + clock), v03 @ 0:48–0:57 (prize reveal) |
| **REVEAL** | the payoff: the money handed over, the prize revealed, the clock hitting 0:00 | the fastest cuts of the reel | v01 @ 0:34–0:37; v04 @ 0:24–0:29 |
| **REACTION / END** | the winner's biggest reaction, a hug, the host's laugh; hard end | one held reaction, the longest shot of the reel | v04 @ 0:36; v03 @ 1:13; v02 @ 0:50 |

The cold open and the setup together stay short: the first stake beat arrives while the promise is still ringing.

### 7.2 Markers
None: spoken only. No step numbers, chapter cards or progress bars. The running total (P-23) and the clock (P-24) are the
only progress devices, and no motif chain holds the reel together: the stake and the cut rhythm do.

### 7.3 The ritual: the stake beat (the same for every attempt, answer or handover)
| Step | Frames | Shot | Text | Graphics |
|---|---|---|---|---|
| 1 Ask / attempt | 24–48 f (0.8–1.6 s) | SH-3 two-shot or the host | CS-2 (CS-1 in a neutral reel) | — |
| 2 Answer / action | 18–36 f | cut to the subject on their first word (SH-2) | CS-3 on the subject's line | — |
| 3 Verdict | 15–36 f | the stake object or the subject's hands | **hidden** | right/won: P-21 "+$X" or P-20, a green flash when it deserves one; wrong/lost: P-27 X or P-22 "$0" |
| 4 Reaction | 18–36 f, within 6 f of the verdict frame | the face that won or lost (SH-2) | CS-3 only for a clear shout | the P-23 total stays if the person stays on screen |
| 5 Others react (optional) | 18–30 f | the host or the crowd (SH-7) | hidden | — |

A stake beat runs about three to six seconds. Each one is bigger than the last: more money, less time, a harder question.

### 7.4 Open loops and the re-hook
- **Loops:** the stake loop ("can they win it?") opens at f0 and pays at the REVEAL; the clock loop (timed reels) opens
  when P-24 appears and pays at 0:00; the total loop (P-23) pays at its last op.
- **The re-hook:** around the middle of the reel the stakes jump, once: a doubled stake ("double it"), a second prize
  behind a cover, the clock starting, or the wide reveal of the pile or the room. It opens with a P-05 wide or a P-06
  stake insert + tag within 0.5 s of the line. (The reference reels put it at 53–71 % and 65–77 % of the runtime.)
- **Payoff rule:** every amount or prize named is handed over, won or lost on screen before the end.

### 7.5 Rhythm by feel
- **The action is the rhythm.** A shot lasts as long as its meaning: the ask as long as the question, a reaction up to its
  peak and not a frame after, the money long enough for the tag to type on and read. Cut the moment the peak has passed;
  never hold a shot to breathe. It never sits still, because live footage never does, and something new arrives every
  time the stunt gives it a reason.
- **The energy only rises.** The cold open is hot. The setup is the one calmer stretch, where the rule gets a wide and a
  steady face. Escalation runs quicker, with a reaction every couple of cuts. The re-hook takes a breath on a wide, then
  it's faster than before. The reveal is the fastest stretch of the reel. Then the end holds: one reaction held longest
  of anything, or a moving celebration wide, and stop.
- **Variety comes from the people**, not from a quota: alternate host, subject and crowd, and skip a reaction that says
  what the last one said.
- **A long shot earns its length** with something changing inside it: a group shot where three tags type on, the clock
  ticking, the caption moving through a line.
- **Light comedy is a garnish:** a ghost replay or a silly shout lands when the footage hands you one, with room between
  them, and never during the reveal.
- **The end feels like a payoff, not a goodbye:** no wave, no "see you", no outro.
- For reference, measured on the four reels at full frame rate (a description, not a target): 35.9 / 47.1 / 48.1 / 45.6
  cuts a minute; median shot 1.28 / 1.10 / 1.03 / 1.23 s (all shots: p10 0.73 s, p90 2.13 s; 19 % under 0.8 s, 6 % over
  2.5 s); the first cut at 1.30–2.13 s; the longest shots a 4.5 s group shot with tags typing on (v01 @12.6–17.13) and a
  6.0 s moving end wide (v03 @67.6–73.5).

---

## §8 Visual system: B-roll and patterns

### 8.1 The role of graphics
- The footage is the show; graphics only mark the stake. Tags, totals, the clock, the chip, the X and logo pops come and
  go with their moment (about 13–27 % of the runtime in the reference reels, captions aside); nothing persists across the
  reel, and every graphic belongs to a moment.
- **Numbers become pictures** in the literal sense: a number is never alone on screen. It's pinned to the real money,
  prize or person (P-20…P-23), or it's the clock (P-24). Every stake beat gets its number.
- **The style looks raw:** a frame carries the tag that matters and maybe one more element besides the caption, never a
  dashboard. The one exception is the multi-object reveal, where three tags type onto three cases at once (v01 @0:15) with
  the captions hidden.

### 8.2 Families
| ID | Family | Source | What the creator supplies |
|---|---|---|---|
| **B-1** | Stunt footage (host, subjects, wides) | the creator's own | cameras A / B / C (§12) |
| **B-2** | Inserts: the stake object, phone screens | the creator's own | SH-4 object shots, SH-8 screen recordings |
| **B-3** | Money and state graphics (tags, totals, clock) | engine | the stake log (amounts, clock times) |
| **B-4** | Captions (CS-1…CS-4) | engine | clean lav audio |
| **B-5** | Brand (sponsor logo pop, brand in type, URL) | the sponsor's logo file (the creator's, else fetched from the sponsor's site); brand in type (P-31) only when none can be found | the logo file, the URL text |
| **B-6** | Colour events (GR-bw, GR-green) and blur transitions (T-01 whip, T-05 zoom blur) | engine (GR-green, T-01, T-05 are `timeline.transitions` built-ins) | — |
| **B-7** | Light comedy (ghost replay, shouts, name calls, hidden-cam HUD) | engine (+ matte for P-34) | — |

### 8.3 Pattern specs
Motion is in frames at 30 fps (f0 = the scene's first frame). "Block" names the engine building block.

**Cut patterns** (family B-1 / B-2; no text unless captions run)
| ID | Pattern | On screen | Recipe | Use | Block |
|---|---|---|---|---|---|
| **P-01** | Cold walk-in | SH-1: the host mid-stride, talking | first frame mid-step with the mouth open; the first word starts ≤ 3 f in; held 1.0–2.1 s | f0 of HA-13 | EDL segment |
| **P-02** | Second-angle cut | the same moment from camera B or C | cut on a word boundary inside the stake sentence at the same session time (R-08) | the first cut, 1.0–2.1 s | EDL / `timeline.shots` |
| **P-03** | Reaction cut | the subject's face, 18–35 % of frame height | starts 2 f before the reaction begins, ends at its peak; 18–36 f; within 6 f of the verdict frame; the biggest reaction of a beat gets **Z-P1** (push 1.0 → 1.15 over 15 f, from the cut or the gesture: v01 @1.48, @20.40) | after every verdict, reveal, handover | EDL from the reaction bank |
| **P-04** | Crowd reaction | bystanders, friends, the class | medium or wide, 18–30 f; a crowd erupting gets **Z-C1** crash zoom from its first frame (1.0 → 1.6 over 24 f, ease-out, v03 @7.27) | after a big win, at the re-hook | EDL |
| **P-05** | Wide establish | the whole set: pile, room, prize wall, crowd | 24–45 f, before the reveal it explains; in L-wide-band if horizontal | SETUP, RE-HOOK | EDL (+ `stage` L-wide-band) |
| **P-06** | Stake insert | macro of the money or prize: the case opening, the stack in a hand, the pile | 15–36 f; the opening frame lands on the stake word (±2 f) | every stake beat, the payoff | EDL + P-20 |
| **P-07** | Phone-screen cut | a full-frame screen recording from camera D | 30–60 f; personal data blurred | the call, the follow tap, the balance | EDL source S1 |
| **P-08** | Tighter-angle punch | a real close-up of the same person | the incoming shot is ≥ 1.4× tighter; cut on the emphasis word | emphasis inside a speech run | EDL |
| **P-09** | Handoff match cut | the money or prize changing hands | the outgoing shot ends mid-motion; the incoming continues it within ±2 f | every handover | EDL |
| **P-10** | Jump re-crop | the same take jumps 1.13–1.20× tighter in 1 f (Z-R1), with no frames removed | `camera` `recrop-in` on the jump, `recrop-out` on the next cut; a marker, so it stays rare | a sponsor logo leaves (v02 @4.05, 1.20×), GR-bw starts (v04 @6.40, 1.13×); FB-2 / FB-3 | `camera` presets |
| **P-13** | Detail re-crop insert | a 2–2.5× crop of the same take on the hands, phone or object, 12–18 f, between two normal shots | EDL segment of the same source + `recrop-in` at `p.scale` 2.0 (4K) / 1.35 (1080p) and `recrop-out` on the next cut | a phone or object beat with no SH-4 / SH-8 close-up (v04 @10.73–11.23, phone in hands) | EDL + `camera` presets |
| **P-11** | Walk-away reveal | the host walking away from camera into the location | 24–45 f; cut to the location's reaction next | HA-16, RE-HOOK | EDL |
| **P-12** | Reaction ending | the winner's biggest reaction, a hug, the host's laugh | 45–90 f; ends on the peak; hard end ≤ 6 f after the last word; a moving handheld celebration wide (the room cheering, the host walking to camera with the stake) may run to 180 f (v03 @67.6–73.5) | END | EDL + T-04 |

**Overlay and state patterns** (engine scenes; family B-3 / B-5 / B-7)
| ID | Pattern | On screen | Motion recipe | Use | z · needs | Block |
|---|---|---|---|---|---|---|
| **P-20** | **Money tag** | the amount ("$10,000") pinned on the real money or prize | **type-on, left to right:** one glyph every 1.5 f (`$10,000` = 7 glyphs in 10–11 f); each new glyph drops in stretched (scaleY 1.4 → 1.0 over 2 f, from y −20 px) with the glow already on; the caption hides on the first glyph frame; hold 18–66 f; **ends on the cut** (no exit animation). Measured v01 @14.67–15.00 | the stake is shown, opened, handed over | z6 · anchor + figure; `payoff: true` in the hook | `VEOS.scene` + built-in `VEOS.fx.typeOn(text, lt, {cps: 20, frames: 2, drop: 0.18, stretch: 0.4})`, `ctx.fmtNum`, `figure`, `anchor` (§16) |
| **P-21** | **Gain tag** | "+$3,000" on the person who gains | as P-20; 104 px; x = face centre, y = face bottom + 140 (clamped to the tag band) | a right answer, a won round | z6 · anchor (face) + figure | bespoke scene, `ctx.face()` |
| **P-22** | **Loss tag** | "$0" (or "−$500") in `bad` | stamp: f0–f4 scale 1.4 → 1.0, rotate −6° → 0; shake ±10 px x, seeded, decaying over 8 f; hold 18–42 f; may persist across one cut at the same screen spot when the loser stays on screen (declare the cut in `cuts`) | a wrong answer, a lost stake | z6 · figure | bespoke scene, `ctx.rng` |
| **P-23** | **Running total** | one number per person or object that ticks up | `exception: E6` container (`data-slot`, rect constant ±4 px) at the person's tag spot; on each op the digits roll 8 f to the new value and the number pulses 1.0 → 1.15 → 1.0 over 6 f; re-enters with the P-20 pop when the person returns after a cut away | quizzes, rounds, per-rep money | z6 · state + figure + `exception: E6` | `VEOS.data.counter` (static spot) or a bespoke scene with `anchor` on the person's track (moving spot) |
| **P-24** | **Countdown clock** | `M:SS` set time, top centre | pop in 5 f on the first value; on every cut hard-swap to that shot's set value (`exception: E6`, events declared); inside a shot ≥ 1.0 s with a visibly running timer, tick every 30 f; the last three values land on consecutive cuts; at `0:00` the fill turns `bad` for 12 f with a 1.0 → 1.12 → 1.0 pulse, then exit 4 f | timed stunts (SH-9) | z6 · state (clock) + `exception: E6` | bespoke scene (§16) |
| **P-25** | **Object glow** | the money or prize lit neon green | radial glow ellipse 1.25× the object box in `good` (opacity 0.75 → 0 at the edge, `mix-blend-mode: screen`) + a 35 % `good` tint ellipse (`mix-blend-mode: color`); f0–f3 rise, peak 6–8 f, then a slow decay to ~60 % that **ends on the cut** (measured v03 @1.63–2.13, 15 f in all); rides the object's track (`anchor`, §8.7). The engine has no object mask yet, so the glow is an ellipse on the object box, not the object itself | the stake's first appearance, the HA-16 payoff | z5 · anchor (no text) | bespoke scene |
| **P-26** | **Handle chip** | white pill: avatar + the creator's handle | grows out of the subject's side in 4 f (0.4 → 1.0, the avatar flips in); the caption word under it fades in 2 f; rides the subject (`anchor` on its track) over a 0.5–0.7 s hold; **ends on the cut** (measured v01 @0.80–1.47) | the creator's channel or name is said ("are you subscribed?") | z5 · anchor (beside the shoulder: face box side ± 40 px, y face bottom + 20…120, inside y 700–1300) | bespoke scene, the creator's logo or initials |
| **P-27** | **X flash** | a glowing red X on the wrong answer | **blur-in 6 f** from the first frame after the cut (opacity 0.4 → 1, blur 10 → 0 px, engine preset `blur`); rides the subject's chest (`anchor` on its track); hold 15–24 f; **ends on the cut** (measured v01 @1.52–2.20) | "no", a wrong answer, a refused offer | z5 · anchor (chest or hand, ≥ 40 px off the head region) | bespoke SVG scene |
| **P-28** | **Icon glow** | ✓ (`good`) / ✕ (`bad`) / + (`primary`) 120–160 px on a hand or phone | pop 5 f; glow 20 px; hold 12–24 f; fade 4 f | a tap, a check, an add | z5 · anchor | `fx.icon` in a scene |
| **P-29** | **Follow confirm** | the creator's avatar badge Ø 140 (white 8 px ring) above the phone, a ✓ beneath | badge 0 → 1.15 → 1.0 in 6 f; ✓ pops at f4; **P-51 green flash on the same frame**; hold 18 f; exit 5 f | the subject follows or subscribes on camera | z5 · anchor (phone track) + GR-green | bespoke scene + built-in `flash` transition |
| **P-30** | **Sponsor logo pop** | the sponsor's own logo file, centred, w 760–900, cy 1000 | a **light** radial haze (`scrim_brand`, white 0.3 at the centre) fades in 3 f; logo scale 0.25 → 0.55 → 0.8 → 1.0 → 1.02 (f0–f4) and keeps growing to 1.04 over the hold; hold 24–52 f; **exits on a cut or a Z-R1 jump of the same take** (v02 @2.33–4.05); disclosure line from the first pop for ≥ 2 s | the product is named or shown in a sponsored reel | z8 (captions hide) · the logo (the creator's or fetched) + brand | bespoke scene, `ctx.asset` |
| **P-31** | **Brand in type** | the brand or place name set in Montserrat 900 caps | as P-30 without the haze; 96–128 px | no logo to be found; a store or place name | z8 · created insert (`logo_plate`) | bespoke scene |
| **P-32** | **URL / link line** | an "OLDNAVY.COM"-style line or "LINK IN BIO" | rise 8 f (y +24 → 0, opacity 0 → 1); hold ≥ 45 f; exit 5 f | a sponsor URL; the `link_bio` CTA | z8 | bespoke scene |
| **P-33** | **Hidden-cam HUD** | 4 corner brackets (60 × 60, 4 px `paper` 85 %) at x 64 / 1016, y 150 / 1480; "● REC" top-left (40 px, the dot in `bad` blinking 15 f on / 15 f off); a running timecode top-right | hard on with the first hidden-cam shot, hard off with the last | candid and hidden-camera segments only | z5 | bespoke scene |
| **P-34** | **Ghost replay** | the subject's cut-out at 45 % opacity, 160–220 px to the side, replaying their gesture 6 f late | fade in 4 f, 30–45 f, fade out 6 f; a one-off gag | a funny gesture or dance | z9 · matte required | bespoke scene on the cut-out (skip without a matte) |
| **P-35** | **Keyword sticker** | the CTA keyword on a `primary` slab | pop 6 f with rotate −10° → −4°; wobble ±2° for 12 f; hold 1.5–2.5 s; exit 5 f; cy 1180, heads clear | the `comment_keyword` CTA only | z8 · `kind: cta-keyword` | bespoke scene |
| **P-36** | **Name call** | a short shout in yellow beside the shouter's head ("NOLAN!!") | pop 2 f or on with the cut (v04 @2.00); hold 15–24 f; exit on the cut; captions hidden for its span | a shouted name or a one-word call from a small or off-centre speaker | z6 · anchor (face side ± 40 px, at the height of the face top − 20…+80; off the hair, not above the head) | bespoke scene |

**Caption patterns** (the auto-caption engine; family B-4)
| ID | Pattern | Recipe | Use | Evidence |
|---|---|---|---|---|
| **P-40** | Neutral word stream | CS-1, 1 word, hard swap, chest (cy 940) | neutral-register reels | v01 0:00–0:35 |
| **P-41** | Comic caps stream | CS-2, 1–5 words revealed word by word, pop 2 f, chest (cy 1000), level | the default register | v02, v04 |
| **P-42** | Money word | CS-2 with the money noun or number in `good` | the stake line | v02 @ 0:01 "UNLIMITED / MONEY" |
| **P-43** | Yellow shout | CS-3, `accent`, −8° | subjects' lines, exclamations | v04 @ 0:02, 0:19, 0:33–0:35; v02 @ 0:18 |
| **P-44** | Pink punch | CS-4, one word | neutral reels: the one word that deserves it | v01 @ 0:30–0:31 |
| **P-45** | Captions off | `hide` override | tags, clock, logo, crowd chaos | v03 throughout; v02 @ 0:36–0:47 |

**Footage treatments** (family B-6)
| ID | Pattern | Recipe | Use | Evidence |
|---|---|---|---|---|
| **P-50** | B&W hold | GR-bw (§4.3), 24–45 f, between two cuts | suspense before a verdict | v04 @ 0:06–0:07 |
| **P-51** | Green flash | GR-green (§4.3): built-in `flash` transition, colour `good`, 6–10 f | a yes / confirm / win moment | v04 @ 0:12 |
| **P-52** | Whip-blur cut | T-01 (§9.1) | a jump in place or time inside the story | v02 @ 21.3–21.6 |
| **P-53** | Zoom-blur punch | T-05 (§9.1) | a beat inside the host's line, into a tighter angle | v02 @ 4.42 |

40 patterns in all (13 cut, 17 overlay and state, 6 caption, 4 treatment).

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the moment needs, then use it.
| Line type (what is said or happens) | Primary | Alternates | For example |
|---|---|---|---|
| The stake line ("If you X, you win Y") | P-01 + P-41 + P-42 | P-11 (HA-16) | "Name my shop, this ₹5,000 is yours" |
| The rules | P-05 + P-41 | P-24 starts | "Hands off the bar = you're out" |
| The ask to a stranger | P-03 + P-41 (P-40 neutral) | P-26 when the channel is named | "Do you know this shop?" |
| A subject's answer | P-03 + P-43 | P-40 | "IT'S SHARMA STORES!" |
| Wrong / no / lost | P-27 or P-22 + P-03 | P-50 before it | lets go of the bar → "$0" |
| Right / yes / won | P-21 or P-20 + P-03 | P-51 | "+₹500" on the subject |
| Money or prize handed over | P-09 + P-20 | P-06 | the envelope into the hand |
| The stake revealed (case opens, pile, prize wall) | P-06 + P-20 (or P-25) | P-05 first | the jar of notes glows |
| The timer starts / the time is called | P-24 | P-41 | "60 seconds, go!" |
| A shouted name or one-word call | P-36 | P-43 | "BHAIYA!!" |
| A phone moment (call, follow, payment) | P-07 + P-28 / P-29 | FB-8 created screen | the subject follows the shop's page |
| The creator's channel or name is said | P-26 | — | "Do you follow me?" |
| A sponsor is named or shown | P-30 (+ P-32) | P-31 | the sponsor's protein tub |
| Escalation ("double it", "but that's not all") | P-05 + P-41 (re-hook) | P-11, P-06 | the stake doubles to $1,000 |
| A suspense pause | P-50 | P-08 | the subject reads the bill |
| A silly gesture or dance | P-34 | P-43 | the uncle's victory dance |
| The crowd reacts | P-04 + P-45 | P-43 on one shout | the gym cheers |
| Hidden-camera segment | P-33 | — | the secret-shopper aisle |
| The ending | P-12 | P-35 (keyword CTA) | the hug at the counter |

Third-party patterns and what replaces them (§12.6): P-30 sponsor logo (the creator's file, else fetched) → P-31 brand in
type only when none can be found; P-07 a screen that isn't the creator's → the real one fetched, else a recreated screen.

### 8.5 Money and truth
- Every amount on screen (tag, total, prize price, clock value) is in `plan/figures.json` with its provenance: the words
  that said it (`from: "script"` + `said`, or `from: "spoken@<t>"`) or the creator's stake log (`from: "creator"`).
  Allowed formulas: `sum`, `diff`, `per_period`; anything else is a stated value (`formula: none`). Recompute with
  `veos figures`.
- A tag shows **what this object or person is worth right now**: the stack in the hand, the case, the prize's real
  price. Totals are `sum` figures of their parts, one per running total, with steps on each op.
- `format`: the number style above (§5.5); tags `style: full`; `sign: "+"` only on P-21 gains. `scale_id` isn't used (no
  charts).
- Stunt money is real, so `illustrative` is never set on a money figure: in this style every amount is a claim. No tag on
  prop or fake money.
- The clock shows the set time the creator logged or the timer visible in the shot, never an invented value.

The teacher's total from §14.3, as a figures file:
```json
{"inputs": {
   "a1": {"value": 500, "from": "spoken@11.2", "said": "five hundred"},
   "a2": {"value": 500, "from": "creator"}, "a3": {"value": 500, "from": "creator"},
   "a4": {"value": 500, "from": "creator"}, "a5": {"value": 500, "from": "creator"},
   "prize": {"value": 250, "from": "creator", "label": "gift card"}},
 "figures": [
   {"id": "teacher_total", "kind": "counter", "formula": "sum", "args": {"values": ["a1", "a2", "a3", "a4", "a5"]},
    "steps": [{"args": {"values": ["a1"]}, "value": 500, "at": 12.4},
              {"args": {"values": ["a1", "a2"]}, "value": 1000, "at": 17.9},
              {"args": {"values": ["a1", "a2", "a3"]}, "value": 1500, "at": 23.6},
              {"args": {"values": ["a1", "a2", "a3", "a4"]}, "value": 2000, "at": 31.0},
              {"args": {"values": ["a1", "a2", "a3", "a4", "a5"]}, "value": 2500, "at": 60.2}]},
   {"id": "prize_tag", "kind": "hero_number", "formula": "none", "args": {}, "value": 250}]}
```
`veos figures` recomputes every step. Keep each tag scene's `text_content` to its figure's values, land counters within
±5 f of the spoken number, and hold to the `$2,500` / `₹1,20,000` grouping and the `+` rule.

### 8.6 Running state: the stake, the total, the clock
| Var | Type | Start | Format | Display | Persist | Ops |
|---|---|---|---|---|---|---|
| `stake` | money | 0 | full (`$10,000`) | P-20 on the stake object | across cuts, while the object is on screen | `set` when the stake is named or raised |
| `total` (one per person or group when several win) | money | 0 | full, `+` on gains only (P-21), none on totals (P-23) | P-23 at the person's tag spot | across cuts, while that person is on screen | `add` per won round or right answer; never `set` mid-reel |
| `clock` | clock, **set time base** | the logged start (e.g. `1:00`) | `M:SS` | P-24 top centre | across cuts for the clock run | `tick_to` per clock shot; jumps allowed, down only |

Ops are written per beat: `state_ops: [{var: "total", op: "add", value: 500, at: 14.20}]`. One fixed position per variable
per person; the number changes only on an op; it never contradicts the spoken or shown amount; a total re-entering after a
cut away appears with the P-20 pop at its last value (no roll).

**How the state is built on today's engine** (the renderer has no `ctx.state`, so you resolve the state in the plan):
- Money variables become figures (§8.5): a `total` is a `sum` figure whose steps land on each op's `at`. P-23 binds
  `figure` and shows `ctx.figAt(id, ctx.t, {roll: 8})` (or uses `VEOS.data.counter` with `roll: 8` when the spot is
  static).
- The clock becomes a list of `{t, v}` pairs in the scene (from the `tick_to` ops), and a `formula: none` figure `clock`
  whose steps are the logged values, so every displayed time has a provenance. The clock's `M:SS` is written by the scene.

### 8.7 Anchors: tags that sit on things
| Target | Placement (tag centre) | Clearance |
|---|---|---|
| `object:<label>` (case, stack, envelope, prize box) | x = the object's centre x; y = the object's top + 0.35 × its height (the number sits on the upper part of the object, as in v01 @ 0:35) | clamp to the tag band y 560–1460 and x 64–1016; ≥ 40 px from every head region |
| `person:<id>` (gains, totals) | x = the face centre x; y = face bottom + 140 px (the chest) | ≥ 40 px below the chin |
| `object:phone` (icons, avatar badge) | 40–80 px above the phone's top edge | ≥ 40 px from every head region |
| `face` side (chip, name call) | beside the head: face box side ± 40 px; y = face bottom + 20…120 (chip) or face top − 20…+80 (name call) | outside the head region (face, hair, the room above) |

**Modes:** `static` (the default: the position read off the look frame at `t_in`, held for the tag's life) or `track`
(when the target moves more than 90 px during the hold: the scene's `anchor: {track, offset, point, scale_with: true,
lost}` rides a tracked path; `veos track` makes it, SCENES-API §13). Track only the tag's own span (0.5–2.5 s
here; ≤ 10 s a run) and **look at the preview**. Use `--clip A` when the span crosses an angle switch of another camera.
**When it goes wrong:** the object leaves the frame or the track is lost for more than a few frames → `lost: "fade"` (4 f)
for a short dropout, otherwise end the tag on the cut before it's lost; nothing trackable (motion blur, a crowd, a tiny
envelope) → `static` at the `t_in` position, with the hold kept ≤ 1.0 s; a face target (P-21, P-26, P-36) uses
`ctx.face()` and needs no track. A tag rides its track and never sits on a lost object, and it stays off the heads.

### 8.8 Comedy layer (light)
- The comedy is in the footage: P-34 ghost replay, P-43 shouts, P-36 name calls, P-44 pink punch, and a caption emoticon
  (":D", ":)") appended to a CS-2 / CS-3 chunk when the speaker laughs, via `{t, text}` overrides. Each is a garnish the
  footage hands you, not a running gag.
- Not in this style: meme sounds, stickers or stamps, freeze-frame roasts, marker scribbles, comedic crash zooms on one
  face (Z-C1 is for an erupting crowd only).
- Never during the REVEAL or on the final reaction.

### 8.9 Sponsor and brand
| Element | Recipe |
|---|---|
| Sponsor logo pop (P-30) | the sponsor's logo file (PNG / SVG; the creator's, else fetched from the sponsor's site), w 760–900 px, centred cy 1000 (cy 330 when a face is in y 800–1200 and no head reaches the logo's box), a light radial haze behind it, pop 4 f, hold 0.8–1.7 s, out on a cut or a Z-R1 jump; on the product's name or first appearance, and back only when the product returns; clear of faces, tags and the clock |
| Brand in type (P-31) | Montserrat 900 caps 96–128 px in `paper` with a 6 px ink stroke, when no logo can be found or the brand is a place |
| URL line (P-32) | Inter Tight 800 caps 64 px under the brand (24 px gap) or at cy 300; ≥ 1.5 s |
| Disclosure | the "Paid partnership" line (or the creator's own wording), Inter Tight 600 26 px at x 64, y 1450, from the first sponsor beat for ≥ 2.0 s; the disclosure is also spoken in the script |
| Product in footage | the host holds or uses the product in SH-3 / SH-4 shots; the brand colours appear only in the logo file and the real product |
| End cards | none (`brand.endcard = null`); the CTA, if chosen, rides the last reaction (§6.7) |

Sponsor beats never interrupt a stake beat between the verdict and the reaction; the sponsor's colours never recolour the
tags, captions or clock.

### 8.10 Assets
- **Real captures only:** every frame of people, money and prizes is the creator's footage.
- **Created graphics** are only the engine's money, state, colour and comedy graphics, the brand-in-type plate (P-31) and,
  as a fallback, a recreated phone screen (FB-8).
- **Logos:** a sponsor's logo is the creator's file (they hold the rights through the deal), else the real logo fetched
  from the sponsor's own site; the brand set in type (P-31) only when none can be found.
- **Third-party material:** the creator's files first, else the real thing fetched, source noted (§12.6).

---

## §9 Transition system

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-00** | **Hard cut** | 0 | nearly every boundary (measured: 2 blur transitions in 150 changes); on a word boundary ±1 f, or on the action frame | silent |
| **T-01** | **Whip blur** | 4 + 2 + 3 | measured v02 @21.3: the outgoing shot smears horizontally over 4 f (blur 0 → ~60 px at 1080 w, content sliding right), 2 f where both shots blend ~50/50, then the incoming smear clears over 3 f. **Built-in:** `{"t": <cut>, "type": "whip", "dir": "right", "px": 60, "frames": 9, "pre": 4, "blend": 2}` in `timeline.transitions` (core draws the directional smear, the travel and the 2 f cross-blend on the picture, under the captions) | a whoosh |
| **T-05** | **Zoom-blur punch** | 0 + 4 | measured v02 @4.42: on the cut a radial blur peaks on the incoming shot (a ~1.3× tighter angle of the host) and clears over 4 f; captions stay sharp on top. **Built-in:** cut to the tighter real angle (or `recrop-in` 1.25) and declare `{"t": <cut>, "type": "zoom-blur", "pre": 0, "frames": 4, "amount": 0.15, "punch": 0, "at": "face"}` (`punch: 0` because the tighter angle is the real cut, not a scale) | a whoosh |
| **T-02** | **Match cut on action** | 0 | P-09: the motion continues across the cut within ±2 f | silent |
| **T-03** | **Band cut** | 0 | `stage` switch to or from L-wide-band on a cut (`via: cut`) | silent |
| **T-04** | **Hard end** | 0 | the last frame is the peak of the last reaction; ≤ 6 f after the last word; no fade, no black tail | silent |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | nothing: the reel starts mid-shot | a fade-in, a black frame, a logo |
| Cold open → setup | T-00 | T-01 |
| Inside a sentence (synced angles) | T-00 (R-08) | T-01 |
| Verdict → reaction | T-00 within 6 f (R-03) | T-01, T-02 |
| Handover | T-02 | — |
| A jump in place or time (store → car, day → night) | T-01 | a crossfade, a wipe |
| A beat inside the host's pitch, cutting tighter on the same set | T-05 | T-01 |
| A sponsor logo leaving, or GR-bw starting, on the same take | Z-R1 jump (no frames removed) | a cut to another source |
| Into or out of a horizontal wide | T-03 | a morph |
| Last frame | T-04 | an outro, an end card, a fade |

### 9.3 Shot grammar
| ID | Rule |
|---|---|
| **R-01** | The first cut comes by 2.1 s, on a word boundary inside the stake sentence. |
| **R-02** | One meaning per shot: cut as soon as the action's peak has passed; never hold to "breathe". |
| **R-03** | Every verdict, reveal and handover is followed within 6 f by the face that won or lost, held 0.6–1.2 s. |
| **R-04** | Never two shots of the same person in a row unless the second is ≥ 1.4× tighter (P-08); alternate host ↔ subject ↔ crowd. |
| **R-05** | A reveal of scale (the pile, the room, the prize wall) gets a 0.8–1.5 s wide first. |
| **R-06** | The stake word is the cut point to the stake insert (±2 f). |
| **R-07** | Emphasis = a cut to a tighter **real** angle (P-08); a jump re-crop (P-10) marks a logo exit or GR-bw; pushes belong to reactions (Z-P1) and crash zooms to crowds (Z-C1), never to the host's talking lines. |
| **R-08** | Inside a sync group, angle switches keep the session time; a sentence may run across up to 4 cuts. |
| **R-09** | Money or prizes changing hands are match-cut on the motion (P-09). |
| **R-10** | When a subject starts to speak, cut to them on their first word (±3 f). |
| **R-11** | A shot lasts as long as its action, most under two seconds (measured median 1.10 s, p90 2.13 s); a shot runs long only when things change inside it: a group shot carrying two or more events (tags typing on, caption changes: v01 @12.6–17.13, 4.5 s), or the moving end wide (P-12, up to 6 s). |
| **R-12** | End on the peak of the last reaction, then T-04. |

### 9.4 How the moves breathe
The cut is the transition: nearly every boundary is a hard cut you don't notice, because the meaning changes, not the
picture. That's what makes the two blur transitions special. The whip (T-01) says "we jumped": a new place or a later
time, and only that. The zoom-blur punch (T-05) is a single accent inside the host's pitch, cutting into a tighter angle.
In the reference reels both appear in one reel only (v02, twice in 51 s); in most reels neither is needed, and two never
sit close together. The match cut on a handover (T-02) is the most satisfying cut in the style: look for it every time
money changes hands. The colour events (§4.3) and the camera moves (§10.2) follow the same law: they mark the moments that
turn the reel, and they're worth more the rarer they are.

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Lead | 1 f before the trigger word, or on the action frame |
| Entries (measured) | money tags **type on** 1.5 f a glyph (P-20); chip 4 f grow (0.4 → 1.0); logo 4 f (0.25 → 1.02 → 1.0, ease `cubic-bezier(0.34, 1.56, 0.64, 1)`); X flash blur-in 6 f; object glow rise 3 f; sticker 6 f |
| Exit | **the default exit is the next hard cut** (tags, chip, X, logo, glow all measured ending on a cut); an exit animation, when the shot continues, is ease `cubic-bezier(0.64, 0, 0.78, 0)` 4 f |
| Caption swap | CS-1 hard; CS-2 / 3 / 4 word pop 2 f (0.5 → 1.05 → 1.0) |
| Hard swaps (`exception: E6`) | only the clock digits, the running-total digits and CS-1 words; the container's rect stays constant ±4 px, and its first entry and final exit stay eased (pop in 5 f, out 4 f) |
| Number roll (P-23) | 8 f, then a 6 f pulse 1.0 → 1.15 → 1.0 |
| Loss shake | ±10 px x, 8 f, seeded, decaying |
| Glow pulse | intensity 1.0 → 1.25 → 1.0 over 6 f after a tag lands |
| Flash | GR-green 6–10 f (the built-in runs 10 f with decay 0.5) |
| Hold | text ≥ 0.13 s a word (CS-1) and 0.15 s (CS-2); tags ≥ 18 f; logos ≥ 24 f; any element ≥ 12 f |
| Anchor follow | the object's tracked path (`anchor`, smooth 2 f); an anchored scene's motion is the object's own |

### 10.2 Footage camera (`zoom_policy: presets`)
Measured frame by frame (ORB + `estimateAffinePartial2D`; strips in `docs/audit/stunt-compression/`).

| ID | Preset | Recipe | Use | Evidence |
|---|---|---|---|---|
| **Z-R1** | `recrop-in` | scale 1.0 → 1.13–1.20 in 1 f (no rotation), held to the next cut (≤ 1.35× on 1080p, ≤ 2.0× on 4K; the P-13 detail insert up to 2.0×) | a jump on the same take: the sponsor logo leaves, GR-bw starts; FB-2 / FB-3 | v02 @4.05 (1.20×), v04 @6.40 (1.135×), v04 @10.73 (≈ 2.5× detail) |
| **Z-R2** | `recrop-out` | back to 1.0 in 1 f on the next cut | always follows Z-R1 / Z-P1 / Z-C1 | — |
| **Z-P1** | `reaction-push` | 1.0 → 1.15 over 15 f, ease-out (peak rate ~1.8 % a frame on f5–f8), no rotation; holds to the cut | the biggest reaction of a stake beat (shock, a hand over the mouth), from the cut or the gesture | v01 @20.40–20.87 (1.17× in 14 f), v01 @1.48–2.05 (1.14× in 17 f) |
| **Z-C1** | `crash-zoom` | 1.0 → 1.6 over 24 f, ease-out (≈ 5–6 % a frame on f1–f4, then decaying), **radial** motion blur on the fast frames (built in: the preset's `blur {kind: "radial", amount: 0.18, at: "face", frames: 6, shape: "decay"}` in `tokens.json`, drawn by core on the stage only; captions and tags stay sharp); holds to the cut | a crowd or class erupting, from its first frame | v03 @7.27–8.17 (1.72× in 27 f) |

No Ken Burns, no slow drifts on wides, no shakes and no rotation; the host's talking lines are never zoomed (the handheld
walk-and-talk is the camera there). The push belongs to the reaction that's bigger than the others and the crash zoom to a
crowd that genuinely erupts; spend them there and they hit. Change the kind of move from one to the next, and never put
two camera moves within 0.4 s of each other. Camera moves never move captions (they're screen space), as in the evidence.
There's no canvas camera: there's no graphics world to move over.

### 10.3 Layer order (back to front)
| z | Layer |
|---|---|
| 1 | W-band blurred copy (L-wide-band only) |
| 4 | footage (the stage) |
| 5 | object glow (P-25), handle chip (P-26), X flash (P-27), icons (P-28 / P-29), hidden-cam HUD (P-33) |
| 6 | money and loss tags and totals (P-20…P-23), clock (P-24), name calls (P-36), the disclosure line |
| 7 | auto-captions CS-1…CS-4 |
| 8 | sponsor logo pop (P-30), brand in type (P-31), URL line (P-32), keyword sticker (P-35): captions hide under them |
| 9 | ghost replay (P-34) |
| 11 | light passes: GR-bw (the z11 saturation scene). GR-green / P-51, the T-01 whip and the T-05 zoom blur are **built-in transitions** drawn by core over the picture (world, footage, z1–6), under the captions: no scene |

### 10.4 Finishing
No grain, no vignette, no bloom, no LUT. Glow exists only on tags (P-20…P-23), the X flash and the object glow. Strokes are
hard (5–10 px) and shadows are hard offsets (`0 6 0`, `0 7 0`); only the captions and the legal line use a soft shadow.

---

## §11 Sound

The reference's sound couldn't be measured (no audio in the evidence); this is a decision. The real sound of the stunt is
the soundtrack: the screams, the cheers, the "NO WAY". Cues only mark the money and the jumps.

| Line | Direction |
|---|---|
| **Where sound goes** | `hook`: one hit on the f0 caption pop (a short sub thump such as `abstract-hit-sub-bass-07`) and one on the payoff tag. `reveals`: a money tag landing (a ka-ching such as `cash-machine-2025-02-19-03-33-58-utc-cash-machine`), a loss tag or the X flash (a dry smack such as `hitsmack-cte01-79-4`), the green flash and logo pops (a bright ding such as `05405-shine-ding`), the clock's first value (`digital-click`) and its 0:00 (the cue follows the outcome: the ding for a win, the smack for a fail). `transitions`: T-01 and T-05 take a whoosh (`swinging-sword-sfx-swinging-sword` for the whip, `cinematic-transition-flash-05` for the zoom-blur punch); a Z-C1 crash zoom may take one deep hit (`boom-2025-01-08-02-40-38-utc-boom`) on its first frame. Caption pops, cuts, re-crops and total ticks are silent |
| **Meme sounds** | None (the comedy is light and lives in the footage) |
| **The bed** | On, from f0, under the dialogue |
| **Ducking** | The bed sits ≥ 20 dB under speech while anyone speaks; the source audio (the crowd, the room, the subjects' reactions) is kept and is the loudest thing after speech: never mute a cheer |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; a hard end ≤ 6 f after the last word |

Pick each cue for its moment so no sound turns into wallpaper. No file plays more than twice in a reel (keep the count
as you place the cues), so the money cue rotates through its family: the ka-ching, a coin (`coin-flip-sfx-coin-flip`), a sparkle
(`christmas-magic-positive-coin-treasure-touch-1-sparkle-glitter`), always bright, always meaning money. If in doubt, leave
it out and let the room be loud.

---

## §12 Footage handling

**The footage is everything.** This style can't be made from a talking head, a voice-over or stock: it's the compression
of a real event the creator stages and films, on two or more cameras (the creator, the people taking part, the prize).
When footage is missing, the fallbacks below say what degrades; if the stake itself was never filmed and no one reacts on
camera, the reel can't be made in this style, and the creator hears that plainly.

### 12.1 The shoot brief (send this to the creator before the shoot)
1. **Stage a real stake.** Real money or real prizes, physically present, visible to camera; know the exact amounts. Prop
   or fake money is never tagged with an amount.
2. **Two vertical cameras minimum** (phones are fine): A follows you, B stays on the people taking part. A third (C) on a
   tripod for the wide is better. Shoot 9:16 vertical, **4K at 30 or 60 fps**, daylight or bright light.
3. **Mic everyone who matters:** a lav on you and one on the main participant; start every camera and recorder, then clap
   once on camera (the sync point).
4. **Open walking and talking.** Start each take already moving toward the participant and saying the stake line ("If you
   can … this ₹5,000 is yours"). Do it three times.
5. **Film every reveal from two angles at once:** A on you, B on their face, never stopping between the reveal and the
   reaction.
6. **Film the stake up close** for 3–5 s each: the envelope opening, the stack in a hand, the pile, the prize boxes.
7. **Get a wide of everything** at least once per location: the whole crowd, the whole pile, the whole room.
8. **Timed challenge?** Put a visible timer on set or call the time out loud, and write down the clock value of every take
   ("take 7: 0:49 left").
9. **Phone moments** (a call, a follow, a payment): screen-record your phone; with the participant's consent, theirs.
10. **Let it run.** Don't cut the camera after the reaction; the hug, the jump and the friend screaming are the reel.
11. **Shoot ten times what you'll use.** About 10 minutes of usable footage per minute of final reel, at least 40 distinct
    moments.
12. **Write the stake log** after the shoot: who got what, every amount, every clock value, the sponsor and its URL. The
    edit tags only what's in it.

### 12.2 Setups
| ID | Camera | Spec | Framing |
|---|---|---|---|
| **A** | Host camera | vertical handheld or gimbal, 4K 30 / 60, follows the host; the host's lav may show | the host's face 18–30 % of frame height, head top y 120–420 |
| **B** | Subject camera | a second vertical 4K camera on the participants' faces and hands | face 20–35 % of frame height for reactions, head top y 140–520 |
| **C** | Wide / set | tripod or high handheld, vertical preferred; horizontal accepted (it goes to L-wide-band) | the whole set; heads y 300–900 |
| **D** | Phone screen | the creator's phone screen recording (or a participant's, with consent) | full screen |

Wardrobe: the host in one plain, saturated tee across the whole shoot (continuity between cuts); no logos the creator
doesn't own on the host.

### 12.3 Shots and fallbacks
| ID | Shot | Spec | Must |
|---|---|---|---|
| **SH-1** | Cold-open walk-and-talk | A: the host already moving and speaking the stake line, 3 takes | **must** |
| **SH-2** | Subject close-up reactions | B: face + hands; at least 3 per subject who wins or loses, clips of 0.6–1.2 s | **must** |
| **SH-3** | Host two-shot with the subject | A or B, medium: the ask, the offer, the handover | **must** |
| **SH-4** | The stake as an object | A / B macro: the envelope or case opening, the stack, the pile, the prizes, 0.5–1.5 s each | **must** |
| **SH-5** | Wide establish | C: the set, the crowd, the reveal of the room or pile | **must** |
| **SH-6** | The reveal from two angles at once | A on the host + B on the subject, synced by sound | **must** |
| **SH-7** | Bystander and crowd reactions | B or C: friends, passers-by, the room | optional |
| **SH-8** | Phone screen recording | D: the call, the follow tap, the payment | optional |
| **SH-9** | The time limit on set | a visible timer or the host calling the time; clock values logged | optional (timed stunts: must) |
| **SH-10** | The ending reaction | the winner's biggest reaction, a hug or the host's laugh, held 1.5–3 s | **must** |

| ID | For | What the edit does instead | Cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | open on the strongest SH-6 reveal (HA-16 or HA-14) and move the stake line to 2–4 s | no walk-in energy; the hook reads as a highlight | degraded |
| **FB-2** | SH-2 | re-crop the subject's face from SH-3 or SH-5 (P-10: ≤ 1.35× on 1080p, ≤ 2.0× on 4K) on each reaction cut | softer reactions with the two-shot's eye-line | degraded |
| **FB-3** | SH-3 | two crops of the wide (SH-5) for the host and the subject | flat angles; a slower read of who speaks | degraded |
| **FB-4** | SH-4 | pin the tag on the recipient's chest at the handover (P-21) and hold the two-shot 0.3 s longer; never a created picture of money | the money is named, not shown: the money-on-the-money rule weakens | degraded |
| **FB-5** | SH-5 | the widest A / B frame as the establish; a horizontal C clip in L-wide-band | less sense of scale | holds |
| **FB-6** | SH-6 | single-angle reveal: hold A on the reveal, then cut to the subject's next reaction from B, even 1–3 s late | no simultaneous host + subject reveal | degraded |
| **FB-7** | SH-7 | a second subject reaction (SH-2) instead | less social proof | holds |
| **FB-8** | SH-8 | film the phone over the shoulder (SH-3 angle) with P-28; if the creator says the call happened and has no recording, a recreated generic phone screen (`fx.appUI`, the words from the transcript) | less intimacy | holds |
| **FB-9** | SH-9 | no clock: the time pressure is carried by the captions only | P-24 is off for the reel | holds |
| **FB-10** | SH-10 | end on the last SH-2 reaction or the stake insert (P-06) | a weaker button | holds |

Note in `ideas.md` which fallbacks the reel runs on and what each costs.

### 12.4 Choosing the moments
This is the craft of the style. A moment is one continuous action with one meaning, 0.5–4 s long. Log them all, then keep
only the ones that tell the stunt.

**The take log** (in your notes; logging 10–20 minutes of footage at 2× speed is the slow part, so start early). The
shape that works:
```json
{"version": 1, "moments": [
  {"id": "m014", "src": "B", "in": 312.40, "out": 313.55, "kind": "reaction", "who": "subject-1",
   "what": "hands on head after the case opens", "energy": 5, "face_h": 0.31, "words": "",
   "stake": null, "sync_group": "reveal-1"},
  {"id": "m015", "src": "A", "in": 311.80, "out": 313.10, "kind": "reveal", "who": "host",
   "what": "host flips the case open toward the subject", "energy": 4, "face_h": 0.12,
   "words": "it's yours", "stake": {"amount": 10000, "currency": "$", "object": "case-1"}, "sync_group": "reveal-1"}],
 "bank": {"subject-1": ["m014", "m022", "m031"]}}
```
`kind` ∈ `walk` (host walk-and-talk) · `stake` (the stake named or shown) · `rule` (how the stunt works) · `ask` ·
`answer` · `reveal` · `reaction` · `crowd` · `object` · `phone` · `wide` · `clock` · `brand` · `end`. `energy` 1–5 (5 =
a shout, a jump, tears). `face_h` = the largest face height ÷ frame height.

**What a kept moment looks like:**
| Kind | Length each | Notes |
|---|---|---|
| walk / stake / rule (host talking) | 1.2–2.2 s | the sentence may run across cuts (R-08) |
| ask / answer (two-shot or subject) | 0.8–1.6 s | cut to the subject on their first word |
| reaction (subjects, from the bank) | 0.6–1.2 s | the biggest group of the cuts: the reel lives on faces |
| object (cash, case, pile, prize) | 0.5–1.2 s | carries the P-20 tag |
| wide / crowd | 0.8–1.5 s | establishes before a reveal (R-05) |
| phone | 1.0–2.0 s | full-frame screen recording, used sparingly |
| clock (timed stunts only) | 0.6–1.2 s | each shot shows one clock value |
| end | 1.5–3.0 s | the last reaction (P-12) |

**How to choose:**
1. **Arc first.** Write the arc with target seconds (§7.1). Every slot names the one to three moments that carry it before
   any other moment is considered.
2. **Prefer** the higher energy, the bigger face (a face of 18 % of the frame or more reads as a reaction), the clear line,
   and the shot that shows the stake. Skip a reaction that repeats the kind of reaction you used a moment ago. When two
   are equal, the shorter one wins.
3. **Trim every moment to its action:** start 2–4 f before the action or the first word, end on the action's peak (a
   reaction ends at the peak of the shock, not after it). Speech moments end on a word boundary ±1 f.
4. **Same moment, two angles:** wherever two cameras recorded the same moment, sync them first (`veos sync --ids A,B[,C]`
   writes `work/sync.json`), then cut between angles on the session time (R-08): hand-write `timeline.shots` on the synced
   mix (`veos shots render`), or put two EDL segments whose `in` points are the same session second. Never cut back in
   time inside a sync group. (Speech isn't the spine here and caption colour follows the beat's mode, so this isn't the
   dialogue module: the subjects' lines get CS-3 by overrides.)
5. **Cut long first,** to about one and a half times the target, then take out the weakest moments until the reel sits in
   its 40–75 s and every shot feels like it's on the edge of too short.
6. **A thin shoot makes a shorter reel, never a slower one.** If there aren't enough strong moments for the length, say
   so and shorten; never stretch a moment past its action to fill time.

**The reaction bank:** per winning or losing subject: shock (a hand over the mouth), hands on head, a jump, a hug; the host:
a laugh to camera, a point, a shrug; the crowd: a cheering wide, one friend's face.

### 12.5 Props, matte, resolution
- **Props:** the stake in clear view (cash in visible stacks or an open case, gift cards, prize boxes); a timer for timed
  stunts; the sponsor's product only in sponsored reels.
- **Matte:** optional, only for the P-34 ghost replay. Nothing else in this style needs the cut-out.
- **Minimum source resolution for crops:** a 2× re-crop needs a 2160 px-wide (4K) source; a 1080p source allows ≤ 1.35×.
  Horizontal 1080p wides go to L-wide-band, never cropped to 9:16.

### 12.6 Third-party inserts: fetch the real thing
In stunt reels the third-party moments are usually:
| Moment | The creator's own | Else fetched (source noted) | Nothing usable: create |
|---|---|---|---|
| A sponsor or a store is named | the logo file (they hold it through the deal) → P-30 logo pop | the real logo from the brand's own site → P-30 | P-31 brand in type (`logo_plate`) |
| A call, chat or app on someone's phone | the screen recording → P-07 phone-screen cut | — (it's their moment) | over-the-shoulder SH-3 + P-28; else a recreated generic screen (`fx.appUI`, the words from the transcript) |
| Another creator's video or post is referenced | the clip or screenshot → full-frame ≤ 2 s | the real post captured from the web, full-frame ≤ 2 s | `fx.quoteCard` (verbatim words) or `fx.appUI({kind: "video"})` |
| A famous person is named | a photo they own → a framed still ≤ 1.5 s | a real photo of them, framed still ≤ 1.5 s | `fx.silhouette` with the name |

The creator's files come first, then the web; use what you get as it is, never altered to say something it doesn't, and
rebuild only when nothing usable turns up. Created screens and cards carry no label and no credit line.

### 12.7 Frame rate and audio
- Output 1080 × 1920, 30 fps CFR; 60 fps sources are conformed to 30 (no slow motion in this style).
- A dialogue chain per lav (high-pass 80 Hz, de-ess, light compression); camera audio carries the crowd and the reactions.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The hook:** HA-13, HA-14 or HA-16; the stake line (8–10 candidates, the pick, two alternates) and its caption chunks;
   the post title; the first cut and the payoff frame.
2. **The arc and the moments:** COLD OPEN → SETUP → ESCALATION → RE-HOOK → REVEAL → END with times, every kept moment
   (its take-log id, camera, in and out, why it's there), and how much of the shoot made it in.
3. **The register and every beat's caption mode** (§5.3.6), as `captions.overrides`.
4. **The stake on screen:** every amount, its figure and provenance, every total recomputed, every clock value and its
   source; the state ops per beat.
5. **The anchors:** every tag, chip, X, icon and glow, static or tracked, with its box and its clearance from the heads.
6. **The punctuation:** the GR-bw and GR-green moments, the camera moves, the rare whip or zoom-blur punch, every match cut.
7. **The inserts and the sponsor:** the creator's files, what was fetched (with the source) and what was created, the
   disclosure, the fallbacks used and their cost.
8. **The sound:** the cue moments and the bed.
9. **The moments you'll look at hardest on the storyboard:** f0 (the moving person + the first chunk), the payoff frame, one stake beat
   (the verdict + the reaction), the re-hook, a clock frame (timed reels: no head under the clock), a two-shot with a
   caption (under the lower chin), the last frame.

**Fields this style leans on:** beats carry `section` (COLD OPEN | SETUP | ESCALATION | REHOOK | REVEAL | END), `trigger
{word | action, at}` and `state_ops [{var, op: set | add | tick_to, value, at}]`; scenes carry `payoff: true` (the hook's
payoff), `figure`, the `anchor` field (SCENES-API §13; `{track, offset, scale_with, lost: hold | fade}`) and `exception:
E6` (clock, total); each beat's caption mode is a `captions.overrides` entry; GR-bw goes in `timeline.grades`.

A hook, for the shape: stake line "If you can name my shop, this ₹5,000 is yours" (alternates "Name my shop and this
envelope is yours", "One guess. Get my shop's name right, win ₹5,000"); post title "Name My Shop, Win ₹5,000"; chunks "IF
YOU CAN" / "NAME MY SHOP" / "THIS ₹5,000" / "IS YOURS"; f0 walk + CS-2 → 1.4 cut to B on the stranger → 2.1 envelope
insert + tag (payoff) → 2.7 the stranger's reaction in CS-3; a hit on the f0 caption pop, a ka-ching on the tag.

---

## §14 Worked examples

Times are planning estimates: take the real ones from the word onsets and the action frames. They show the standard; match
it, then beat it.

### 14.1 Street giveaway, comic register, ₹ (a local-business / street creator, Hinglish)
**Reel:** "Meri shop ka naam batao, ₹5,000 jeeto" · 45 s · HA-13 · register comic (CS-2, Hinglish Latin caps) · numbers
Indian ₹ · CTA none.
**Stake log:** stake 1 = ₹5,000 (envelope 1); re-hook stake = ₹10,000 (envelope 2); given: ₹10,000 to subject 3.

**Hook (0–3.2 s)**
| t (s) | Visual | Caption | Graphics / state | Cue moment |
|---|---|---|---|---|
| f0 | P-01: the host walking down the market lane toward camera, envelope in hand, mid-word | CS-2 "AGAR TUM" on screen from f0 | — | hit on the f0 pop |
| 0.45 | same shot | "MERI SHOP KA" | — | — |
| 0.95 | same shot | "NAAM BATA DO" | — | — |
| **1.40** | P-02: cut to camera B, a student turning toward the host (same sentence) | "TOH YE" | — | — |
| **1.85** | P-06: the envelope opened by the host's thumb, the notes fanned | hidden | **P-20 "₹5,000"** on the notes, `figure: stake_1`, **`payoff: true`** | ka-ching on the tag |
| 2.55 | P-03: the student's face, eyebrows up | CS-3 "SACH MEIN?!" | `state_ops: stake set 5000` | — |

**Section plan**
| Section (s) | Beats | Patterns | Caption mode |
|---|---|---|---|
| SETUP 3.2–7.4 | the host hides the shop board behind him; "ek guess, bas" | P-05 wide of the lane (1.2 s) → P-03 → P-26 handle chip on "mera page follow karte ho?" (0.7 s) | CS-2; hidden under the chip |
| ESCALATION 7.4–21.5 | stake beat 1: the student guesses wrong | P-03 (answer) → **P-27 X** on his chest → P-04 his friends laughing | CS-3 for his guess; hidden for the X |
| | stake beat 2: an aunty guesses wrong | P-03 → **P-50 B&W hold** 1.0 s while she thinks → P-22 **"₹0"** with shake → P-03 her laugh | CS-3 / hidden / none |
| RE-HOOK 21.5–25.0 (48–56 %) | "Theek hai… ab ₹10,000!" a second envelope | P-08 tighter on the host → **P-06 + P-20 "₹10,000"** (`state_ops: stake set 10000`) → P-04 the lane reacts | CS-2 with "₹10,000" in `good` (P-42) |
| ESCALATION 25.0–31.0 | a delivery rider stops; the host asks | P-03 (his face) → P-08 (tighter on the host's question) → P-03 his grin; no B&W hold here: the suspense already played at stake beat 2, and this beat is quick | CS-2 / CS-3 |
| REVEAL 31.0–41.5 | he names the shop correctly | P-03 (his answer, CS-3 "SHARMA GENERAL STORE!") → **P-51 green flash** → **P-09 match cut** on the envelope into his hand → **P-20 "₹10,000"** on it (`state_ops: total add 10000`) → P-03 his shock → P-04 the shopkeepers cheer → P-34 ghost replay of his little dance (only with a matte) | CS-3 / hidden / hidden |
| END 41.5–45.0 | the rider hugs the host | **P-12** (2.6 s), hard end on the peak | none |

**State and figures:** `stake` set 5000 at 1.85, set 10000 at 22.6; `total` add 10000 at 34.9. `plan/figures.json`: inputs
`stake_1` (5000, `said: "₹5,000"`), `stake_2` (10000, `said: "₹10,000"`); figure `given` = `sum([stake_2])` shown at 34.9.
Format `₹10,000` (Indian grouping).
**Rhythm:** the first assembly ran 38 cuts in 45 s and felt crowded in ESCALATION: two reactions said the same thing as
their neighbours. Taking them out gave each laugh room: 36 cuts, median shot 1.2 s.

### 14.2 Timed fitness challenge, comic register, $ (a fitness coach / gym creator)
**Reel:** "Hang on this bar for 60 seconds, win $500" · 56 s · HA-13 · register comic · clock on (SH-9 logged) · CTA
`comment_keyword` "HANG".
**Stake log:** rule: $50 for every 10 s held; 60 s = $500. Subject 1 drops at 0:31 left → held 29 s → $100; subject 2
drops at 0:12 left → held 48 s → $200; subject 3 holds to 0:00 → $500, and the host doubles it at the re-hook → $1,000.

**Hook (0–3 s)**
| t | Visual | Caption | Graphics / state | Cue |
|---|---|---|---|---|
| f0 | P-01: the host walking across the gym floor with a cash stack, talking to camera | CS-2 "HANG ON THIS BAR" | — | hit on the pop |
| 0.80 | same | "FOR 60 SECONDS" | — | — |
| **1.30** | P-02: cut to C, the pull-up bar with three people waiting | "AND WIN" | — | — |
| **1.75** | P-06: the cash stack fanned on the bench | hidden | **P-20 "$500"**, `payoff: true` | ka-ching on the tag |
| 2.35 | P-03: subject 1 grinning, chalking his hands | CS-3 "EASY!" | — | — |

**Section plan**
| Section (s) | Beats | Patterns | Caption mode |
|---|---|---|---|
| SETUP 3.0–7.5 | the rule: $50 every 10 s | P-05 wide → P-08 host close → P-24 **clock "1:00" pops** (`state_ops: clock set 60`) | CS-2 "$50 EVERY 10 SECONDS" with the number in `good`; the clock then hides captions |
| ESCALATION 7.5–26.0 | subject 1 hangs: the clock cuts 0:52 → 0:44 → 0:37 → 0:31 (one value per shot, E6) | P-03 face strain / hands close-up / P-04 friends; at the drop he has still earned money, so **P-21 "+$100"** on his chest (a gain, not a loss) | hidden while the clock runs; CS-3 "MY ARMS!!" |
| | subject 2 hangs: the clock 0:58 → 0:40 → 0:21 → 0:12 | P-03 / P-08 / P-03; drop → P-21 "+$200" | hidden / CS-3 |
| RE-HOOK 26.0–31.5 (46–56 %) | host: "Last one. Make it to zero and I double it." | P-08 host → **P-06 a second stack + P-20 "$1,000"** (`stake set 1000`) → P-04 the gym "OHHH" | CS-2 with "$1,000" in `good` |
| REVEAL 31.5–50.5 | subject 3 hangs; the clock runs 0:60 → 0:45 → 0:30 → 0:15 → **0:03 → 0:02 → 0:01** on consecutive ~0.8 s cuts → **0:00 turns red** | P-24 + P-03 / P-08 / P-04 alternating, every clock shot framed with her head below the clock; **P-50 B&W hold** at 0:05 for 1.0 s, the one held breath of the reel; 0:00 → **P-51 green flash** → P-09 the stack into her hands → **P-20 "$1,000"** → P-03 her scream | hidden during the clock; CS-3 "LET'S GOOO!" after |
| END 50.5–56.0 | she drops to the floor laughing; the host high-fives | P-12 (2.0 s) + **P-35 keyword sticker "HANG"** for 2.0 s over the last shot, spoken "comment HANG and I'll come to your gym" | none + sticker |

**State and figures:** `clock` values come from the stake log, one per shot, down only (`state_ops: clock tick_to <value>`
on each clock cut). Inputs: `rate` (50, `said: "$50 every 10 seconds"`), `paid_s1` (100, `from: creator`, the log says
29 s held), `paid_s2` (200, `from: creator`, 48 s held), `stake_base` (500, `said: "$500"`), `stake_bonus` (500, `said:
"I double it"`). Figures: `s1` and `s2` with `formula: none` (stated values), `final` = `sum([stake_base, stake_bonus])` =
1,000, shown at 47.6 s. The plan never computes "held seconds × rate" on screen: the creator's log is the provenance of
each payout.
**Rhythm:** the clock run is the fastest stretch of the reel, one value a cut into 0:00 (44 cuts in 56 s, median shot
1.1 s).

### 14.3 Sponsored group quiz, action register, $ (an education / workplace creator; with a sponsor)
**Reel:** "Every right answer = +$500 for your teacher" · 66 s · HA-16 (the host holds the stake; no stake line at f0) ·
register action · sponsor: a stationery brand (the creator's logo file) · CTA none.

**Hook (0–3 s)**
| t | Visual | Caption | Graphics / state | Cue |
|---|---|---|---|---|
| f0 | the host in the corridor holding a bucket of cash stacks toward camera, talking | hidden (his first words aren't the stake) | — | — |
| **1.65** | same shot, he lifts one stack | — | **P-25 object glow** on the stack, `payoff: true` | reveal cue |
| **2.10** | P-11: cut to him walking away into the classroom | — | — | — |
| 2.90 | P-04: the class sees him, screams | CS-3 "NO WAY!" | — | — |

**Section plan**
| Section (s) | Beats | Patterns | Caption mode |
|---|---|---|---|
| SETUP 3.0–9.5 | the rule on the classroom TV ("every question you get right = +$500 for your teacher") | P-05 wide with the TV readable → **P-30 sponsor logo pop** on "this quiz is brought to you by …" (1.0 s) + disclosure "Paid partnership" (2.0 s) → P-03 the teacher's face | CS-2 for the host's rule; hidden under the logo |
| ESCALATION 9.5–36.0 | 5 questions, each a stake beat: the question on the TV (P-05) → a kid answers (P-03, CS-3) → right: **P-23 total on the teacher** ticks +$500 (rolls 8 f) → the teacher reacts (P-03) | P-23 ticks: $500 → $1,000 → $1,500 (one wrong answer: **P-27 X**, no tick) → $2,000 | action register: hidden except the kids' shouts (CS-3) |
| RE-HOOK 36.0–42.0 (55–64 %) | "And everyone in this class gets a prize": a red cloth over a table | P-08 host → P-06 the cloth pulled → P-05 the prize table → **P-31 brand in type** (the store's name) + **P-32 URL line** (1.5 s) | CS-2 for the host line; hidden under the brand |
| REVEAL 42.0–62.5 | handing out prizes; the teacher's final total | P-09 handovers ×4, P-20 price tags on two prizes ("$250"), P-03 / P-04 alternating, the teacher's **P-23 "$2,500"** final tick on the last answer, **P-51 green flash** on her total | hidden; CS-3 on two shouts |
| END 62.5–66.0 | the host laughing to camera with the last cash stack | P-12 (2.2 s) | none |

**State and figures:** `total` (teacher) add 500 per right answer at each tick (a `sum` figure with steps `[500, 1000,
1500, 2000, 2500]`, each step's `args.values` listing the answers so far; the figures file is in §8.5). Prize tags `$250`
from the stake log (`from: creator`). Sponsor: the logo is the creator's file, the disclosure on from the first brand beat; the
store had no logo to be found, so its name is set in type (P-31, `logo_plate`).
**Rhythm:** with no captions on most beats, the tags and the faces carry it: 52 cuts in 66 s, median shot 1.04 s (as v03).

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0: a person (or the stake) already moving, the first caption chunk already on screen (HA-13 / HA-14); no
  headline, logo or black frame. The first cut by 2.1 s; the stake or the first big reaction by 2.3 s.
- At full speed it feels like the stunt with the boring parts removed: every shot means one thing and ends at its peak;
  nothing is held to breathe; it gets faster into the reveal.
- Every verdict, reveal and handover is followed within 6 f by the face that won or lost; the reel ends on a reaction
  peak, no outro.
- Almost every boundary a hard cut; the camera only re-crops, pushes into a big reaction or crashes into an erupting
  crowd; overlays end on cuts.
- Green only on money, red only on loss, yellow only on shouts; the B&W hold and the green flash on the moments that turn
  the reel.
- One caption register; each beat's mode right for it (loud, intimate or off); no hand-written caption cards.
- The stakes jump once, around the middle, and each stake beat is bigger than the one before.
- Start to end: you needed to know if they'd win, and you felt it on their face.

**Craft (by eye, in context)**
- The faces read (host, subject, bystander): captions under the chin (the lower chin in a two-shot), tags and chips off
  the heads, no head under the clock; nothing buries a reaction face by accident.
- Captions out of the way under every tag, logo, brand type, name call and GR-bw; never two caption systems; no text over
  text by accident.
- Tags, X flashes and logo pops land on their word or the action frame; cuts on word boundaries or the action frame;
  synced angle switches keep one continuous sound.
- Every amount is in `plan/figures.json` with its provenance and matches what was really given, won, lost or stated; no
  tag on prop money; totals equal their parts and never decrease; the clock only goes down, changes only on cuts or
  visible ticks, turns red at 0:00.
- Every tag sits on its object or person and rides its track when the object moves.
- The stake named in the cold open is paid off on screen; the CTA keyword, if any, readable.
- Captions, tags and the clock big enough to read on a phone, ink strokes present; names, brands and the handle spelt
  exactly; `$10,000` / `₹1,20,000` formats, `+` only on gains.
- Phone screens: personal data blurred for the whole time on screen.
- Logos are the creator's files or the real ones fetched; the sponsor disclosure on screen ≥ 2 s from the first sponsor
  beat.
- The real cheers stay loud. The file itself (1080 × 1920, 30 fps, −14 LUFS, the bed under speech, the end ≤ 6 f after
  the last reaction or word) is the render's job; it checks it.

---

## §16 Build notes
- **Fonts:** Bangers (400), Lilita One (400), Poppins (600, 700), Inter Tight (600, 700, 800), Montserrat (900), and Noto
  Sans Devanagari (600, 800) for Hindi.
- **Determinism:** every frame is a function of its index; shakes, blinks and flickers use `ctx.rng(seed)`.

**P-20 money tag** (one scene per tagged object; the type-on is the built-in `fx.typeOn`, the follow is the built-in
`anchor`):
```js
// anchor pass: `veos track --id case1 --at 1.85 --box 400,1010,280,360 --from 1.85 --to 2.55` -> plan/tracks/case1.json
// the tag sits on the upper part of the object: offset = -0.15 x the object's height at t_in (scaled with the object)
const T1 = { id: "tag-case1", figure: "stake_1", t_in: 1.85, t_out: 2.55, track: "case1", dy: -54 };
const TAG = { cps: 20, frames: 2, drop: 0.18, stretch: 0.4 };   // 1.5 f per glyph; drop-in from -20 px, scaleY 1.4 -> 1.0 over 2 f
VEOS.scene({ id: T1.id, t_in: T1.t_in, t_out: T1.t_out, z: 6, in: "none", out: "none", kind: "number", payoff: true,
  text: true, text_class: "TC-display", roles: ["good"], figure: T1.figure,
  events: [+(VEOS.fmtNum(VEOS.fig(T1.figure).shown, T1.figure).length / TAG.cps).toFixed(3)],   // the last glyph lands
  text_content: VEOS.fmtNum(VEOS.fig(T1.figure).shown, T1.figure), box: { x: 240, y: 1060, w: 600, h: 200 },
  anchor: { track: T1.track, offset: [0, T1.dy], scale_with: true, lost: "hold" },
  render(ctx, lt) {
    const v = ctx.fmtNum(ctx.fig(T1.figure).shown, T1.figure), b = ctx.scene.box;
    return ctx.html(`<div style="position:absolute;left:${b.x}px;top:${b.y}px;width:${b.w}px;text-align:center;white-space:nowrap;
      font:400 112px/1.5 ${ctx.fam("numeric")};color:${ctx.col("good")};
      -webkit-text-stroke:5px ${ctx.col("money_edge")};paint-order:stroke fill;
      text-shadow:0 0 22px ${ctx.hexA("good", 0.85)},0 0 6px ${ctx.hexA("good", 0.9)},0 6px 0 rgba(0,0,0,.55)">${VEOS.fx.typeOn(v, lt, TAG)}</div>`);
  } });
```
The box is drawn where the anchor puts it (its centre on the track point + offset). A static object needs no track: drop
`anchor` and set `box` from the look frame. Untyped glyphs keep their place, so the box never moves while it types.

**P-24 clock** (bespoke scene, `exception: E6`):
```js
const CLK = [{ t: 36.00, v: 58 }, { t: 37.27, v: 49 }, { t: 38.77, v: 48 }, { t: 41.47, v: 47 }, { t: 42.43, v: 46 },
             { t: 44.57, v: 3 }, { t: 45.70, v: 2 }, { t: 46.60, v: 1 }, { t: 47.40, v: 0 }];   // tick_to ops (set time, s)
const mss = v => `${Math.floor(v / 60)}:${String(v % 60).padStart(2, "0")}`;
VEOS.scene({ id: "clock", t_in: 36.0, t_out: 48.0, z: 6, in: "pop", out: "none", exception: "E6", figure: "clock",
  text: true, text_class: "TC-display", roles: ["bad"], box: { x: 290, y: 205, w: 500, h: 170 },
  events: CLK.slice(1).map(c => +(c.t - 36.0).toFixed(3)), text_content: CLK.map(c => mss(c.v)).join(" "),
  render(ctx) {
    const c = CLK.filter(c => ctx.t >= c.t).pop(), zero = c.v === 0;
    const red = zero && ctx.t - c.t < 0.4, s = zero ? 1 + 0.12 * Math.sin(Math.PI * Math.min(1, (ctx.t - c.t) / 0.2)) : 1;
    return ctx.html(`<div data-slot style="position:absolute;left:290px;top:205px;width:500px;height:170px;text-align:center;
      transform:scale(${s});font:400 170px/170px ${ctx.fam("numeric")};color:${red ? ctx.col("bad") : ctx.col("paper")};
      -webkit-text-stroke:9px ${ctx.col("ink")};paint-order:stroke fill;filter:drop-shadow(0 0 0 #fff) drop-shadow(0 0 3px #fff)">${mss(c.v)}</div>`);
  } });
```
The clock's exit after 0:00 is the next cut (`t_out` on that cut).

---

## Appendix A. Evidence map
| What | Evidence |
|---|---|
| Cold open mid-action, caption at f0 | v01 hook @ 0:00 ("are"), v02 @ 0:00 ("THIS"), v04 @ 0:00 ("I'M ABOUT TO"); v03 @ 0:00 face + cash, no caption (HA-16) |
| First cut 1.30–2.13 s; 35.9–48.1 changes a minute, median shot 1.03–1.28 s (full-rate detection) | `cuts.json` / `meta.json` v01–v04 |
| Money tags on objects, neon green with glow, typing on glyph by glyph | v01 @ 0:15 (three cases), 0:19, 0:25, 0:35–0:37; v03 @ 0:12–0:13, 0:23, 0:43–0:44, 0:52–0:53, 1:07; v04 @ 0:15; type-on v01 @14.67–15.00 |
| Countdown clock, set time, jumps | v02 @ 0:36–0:47 (0:58 → 0:49 → 0:48 → 0:47 → 0:46 → 0:26 → 0:03 → 0:02 → 0:01) |
| Caption registers: neutral lowercase / comic caps, yellow shouts, green money word / pink punch | v01 throughout / v02 @ 0:00–0:01, 0:07–0:30, v04 throughout / v01 @ 0:30–0:31 |
| Camera: jump re-crop, reaction push, crash zoom; whip and zoom blur | v02 @ 4.05, v04 @ 6.40; v01 @ 1.48, 20.40; v03 @ 7.27; v02 @ 21.3 (whip), 4.42 (zoom blur) |
| Ends on a reaction, no CTA | v01 @ 0:37, v02 @ 0:50, v03 @ 1:13, v04 @ 0:36 |

The full map, with every timestamp, the fidelity and completeness audits and what's unverified (the speech language, the
exact comic and number typefaces, the yellow-caption rule, the bed, the CTA set), is in `evidence.md`.

## Appendix B. Hook-title bank
Slots: `[STAKE]` the amount or prize as written on the tag · `[ACT]` what the person must do · `[N]` seconds or a count ·
`[WHO]` the person or group · `[PLACE]`.
| # | Spoken stake line (cold open) | Post title | Archetype | Example |
|---|---|---|---|---|
| 1 | "If you can [ACT], this [STAKE] is yours" | "[ACT], Win [STAKE]" | HA-13 | "If you can name my shop, this ₹5,000 is yours" |
| 2 | "You have [N] seconds to [ACT]" | "[N] Seconds To Win [STAKE]" | HA-13 | "You have 60 seconds to hold this bar" |
| 3 | "Every [ACT] = +[STAKE]" | "Every [ACT] Pays [STAKE]" | HA-13 | "Every rep is +$10" |
| 4 | "I'm about to pay for [WHO]'s [THING]" | "I Paid For [WHO]'s [THING]" | HA-13 | "I'm about to pay for this whole queue's chai" |
| 5 | "This is [STAKE] in [FORM]" | "[STAKE] In [FORM]" | HA-14 | "This is ₹1,00,000 in ₹10 coins" |
| 6 | "Last one standing keeps [STAKE]" | "Last One Standing Wins [STAKE]" | HA-13 | "Last one in the plank keeps $1,000" |
| 7 | "[STAKE] or [OTHER STAKE], you pick" | "[STAKE] Or [OTHER STAKE]?" | HA-13 | "₹10,000 or the mystery box, you pick" |
| 8 | (no line: the host lifts the stake, walks into [PLACE]) | "Surprising [WHO] With [STAKE]" | HA-16 | "Surprising the night-shift guards with ₹20,000" |
| 9 | "Whoever [ACT] first wins [STAKE]" | "First To [ACT] Wins [STAKE]" | HA-13 | "Whoever finishes the sprint first wins my shoes" |
| 10 | "Answer right and [WHO] gets +[STAKE]" | "Every Right Answer = +[STAKE]" | HA-16 | "Answer right and your teacher gets +$500" |
