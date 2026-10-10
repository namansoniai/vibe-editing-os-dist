# Brand Stop-motion Ad Style Playbook (template v2)

## The feel

This reel is a tiny handmade film that happens to be an ad, and nobody minds, because it's charming long before it sells
anything. Frame 0 is a felt bee already flying into shot, a clay character already halfway through a sip, a living-room TV
already playing. No title, no logo, no "NEW". A miniature world, lit warm, shot so close you can see the thumbprints in the
clay, and someone in it is already doing something. You stop because it's alive, and because nothing else in the feed looks
like it.

Then the edit trusts the characters. Shots are patient. Cuts land on the end of a movement, so you never feel them. The
world keeps its own stutter: puppets on twos, poses that hold, a camera gliding on ones. Nothing the edit adds may move
more smoothly than the world it sits in. When someone speaks, small pale-yellow words appear low in the frame, on with the
first syllable and gone with the last; when nobody speaks, the screen is clean. The comedy is acting and timing: the beat
of silence before the reaction, a cat peeking out of the bushes, a punch line that's a little bit rude.

The product never interrupts the story; the story arrives at the product. It's the cup in a paw, the honey waterfall at
the end of the journey, the commercial on the tiny TV between bursts of static, its claim words blinking red like an old
broadcast. That turn gets the biggest, longest-held shot of the second half. Right after it the sketch earns one more
laugh, the button. Then a soft iris closes on the characters, or a hard cut to black, and the brand's wordmark sits alone
on black, quiet, like the artist's signature at the bottom of a drawing.

Calm is the power here. Escalate with scale, never with speed: a bigger set, a brighter reveal, a longer hold. The brand
signs it at the end and nowhere else.

**The test:** pause on any frame before the wordmark and it looks like a still from a handmade short film, not an advert;
if anything the edit added breaks that, it's wrong.

## What this playbook is

You're cutting a brand's own stop-motion or animated plates into a 10–30 s ad, and you have the authority to make it the
most charming thing in the feed. The engine never makes the characters, sets, lighting or depth of field; you make the
edit: which plates, in what order, cut on which frame, the small captions, the product spot inside the world, the iris and
the wordmark. This playbook is the style, pulled from three Chamberlain Coffee stop-motion ads (claymation v01 and v02,
needle-felt v03) and measured frame by frame. Read it all, every time; take what fits these plates, invent where a moment
needs more, and never break the feel above.

**Who it's for and what it needs.** Brands and agencies that already own (or are commissioning) stop-motion, claymation,
felt, puppet, paper-cut or 3D-animated shots. Input: the plates (`animated_plates`; native 9:16 ideal), their mixed audio,
the wordmark file, and for the product broadcast format the pack shots and an approved claims list. Nothing here can be
generated: **the plates are the product**, and without them there is no reel (§12). No presenter, no cut-out: the faces
that matter are the characters'. Captions follow the brand's script in the language chosen at setup (English by default;
Hinglish romanised; Hindi in Devanagari). Machine values live in `tokens.json`; where this text gives a number tokens also
holds, they agree.

### Style directives (non-negotiable)
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Characters act before anything is written.** No headline, banner, title card or label in the hook; the first text on screen is the first spoken line's caption (and, on a paid post, the disclosure) | §6.2, §2 |
| D2 | **The plates are the look.** Never retime, interpolate, regrade, punch in, stabilise or speed-ramp a plate. The only engine changes to a plate are a trim, an end-frame hold of up to 12 f, or the fallback crop or band (FB-2) | §10.2, §10.3, §2 |
| D3 | **Captions are small and quiet:** pale yellow `#F6FA8C`, 64 px, up to 2 lines of up to 24 characters, block centre y 1420, one character line per caption, cut on and off with no fade, no coloured or bold emphasis | §5.3 |
| D4 | **The product lives inside the world.** It's a prop, the place the journey ends, or a broadcast on an in-world screen. Never a full-frame pack shot pasted over the plates | §8.3, §2 |
| D5 | **Calm rhythm, hard cuts on action.** No dissolves, whips, zoom transitions, light leaks or glitches. The in-screen static, the sensory-trip glow and the closing iris are the only designed transitions | §9, §7.5 |
| D6 | **Every sketch has a button:** a last character beat (a reaction, a non-sequitur, a satisfied sip, the masked punch line) between the product turn and the wordmark | §7.1 |
| D7 | **The wordmark closes alone on black** (y 960, 600–700 px wide, held 1.8–2.4 s), then a hard end. Nothing else on the card except an optional link or stockist line | §6.7 |
| D8 | **Every word on screen is approved:** captions verbatim from the brand's script, label words only from the approved claims list, profanity masked inner-style (`F**k`) | §5.5, §8.5 |

### Quick index
| § | What |
|---|---|
| §1 | Procedure: how to approach a reel in this style (the plate cut pass is the craft) |
| §2 | Hard rules: the craft and the style's never-list |
| §3 | Formats F-A / F-B / F-C, worlds W-plate / W-black, layouts, stage moves, safe zones, the characters' faces |
| §4 | Colour system: the plates own colour; label red, screen sky, black |
| §5 | Type and captions: CS-1 soft dialogue, CS-2 bright plate, CS-3 high band; label words, wordmark, link, disclosure |
| §6 | Hook system: stopper test, HA-16 Diegetic, HA-15 / HA-14 / HA-13, hook pairs, post title, CTA, end card and disclosure |
| §7 | Structure and rhythm: the sketch, the line ritual, the screen spot ritual, journey steps, open loops, rhythm by feel |
| §8 | Visual system (B-roll and patterns): families B-1…B-8, 35 patterns, line → pattern lookup, truth, anchors, comedy, assets |
| §9 | Transition system: T-CUT…T-CARD-IN, grammar, shot grammar R-1…R-12, how the moves breathe |
| §10 | Motion tokens, the plate cadence, camera (`source_only`), layers, finishing |
| §11 | Sound |
| §12 | Footage handling: plates, shots and fallbacks, inserts, frame rate |
| §13 | What your plan should settle |
| §14 | Worked examples (3) |
| §15 | Your look at the storyboard: the checklist |
| §16 | Build notes |
| App. A / B | Evidence map / hook-title bank |

---

## §1 Procedure: how to approach a reel in this style

You watch, listen, plan, build and look at the storyboard yourself; the edit skill has the mechanics. This style's
craft is **the plate cut pass**: choosing the in and out frame of every plate on the action inside it, so that every cut
lands on a completed or matched motion and the sketch keeps its calm, patient rhythm. Everything else serves it.

1. **Log the plates.** One row per plate: an id, the setting, the characters, the action in one sentence, the shot size
   (`W` wide · `M` medium · `CU` close-up · `INS` insert), the camera (locked · push · pan · rack), the frames where the
   action starts and ends, the usable in and out, whether an in-world screen is in shot (and whether it's locked off), the
   plate's luminance in the caption band y 1340–1500 (dark · mid · bright), and the y range every character's head
   occupies. Read one frame a second plus the first and last frame of each plate.
2. **Pick the format** by the rule in §3.1: dialogue → F-A; a locked-off in-world screen → F-B; one short silent moment →
   F-C.
3. **Get the words right.** When the plates have speech, the captions are the brand's dialogue script (SH-4) aligned to the
   word timings (`transform: verbatim`, the script's casing kept: "you've **GOT** to try this"), with the profanity mask
   `inner` and the glossary (brand, product and character names). Without a script, FB-4.
4. **Map the plates onto the sketch** (§7.1): `setup`, `gag` (or `journey` / `broadcast`), `product`, `button`, `logo`.
   Every plate gets a beat. Keep the brand's animatic order unless the beats demand otherwise (R-10).
5. **Cut every plate on the action** (the craft step). In on the first frame of a motion (or 2–4 f into it); out on the
   frame the motion completes, or on the matching moment of the next plate's action (R-1). Write each cut's reason
   (`action_end`, `match`, `line_end`, `reaction`). Never use a plate's first or last 3 frames (R-12).
6. **Feel the tone of each beat:** `setup` · `gag` · `awe` (the product turn) · `button` · `cta` (the wordmark).
7. **Choose the hook** (§6): the opener plate and its first cut, from every plate that could open; then 8–10 post titles,
   the best by the stopper test, two alternates.
8. **Plan the overlays** (there are few, and each one matters): CS-1 captions, CS-2 on every shot logged `bright`, CS-3 on
   every shot where a head reaches the caption band (§3.6); in F-B the screen spot and its label words from the claims list;
   the end (T-IRIS in F-A, T-CUT-BLACK in F-B and F-C) and the card; the disclosure when the post is paid.
9. **Run the anchor pass** (§8.6): the screen rect of every F-B screen plate, the iris centre on the button plate, and every
   shot's head band.
10. **Run the claims pass:** every label word, number and product name on screen is matched to the claims list or the
    script, character for character. Unmatched words are dropped and listed in the plan.
11. **Plan the sound and the transition map** (§11, §9): the plate mix carries the story; pack cues only on the reveals, the
    static and the wordmark.
12. **Gather the assets:** the wordmark (SH-5), the pack shots (SH-6), the screen show content (§12.4): the brand's
    files first, else the real ones fetched from the web (the brand's own site for its marks and packs), source noted.
    Resolve the fallbacks (§12.2) and note which ones ran.

---

## §2 Hard rules: the craft and the style's never-list

**Craft, by eye** (judge it on the storyboard, in context, the way an editor does):
- **Keep the characters' heads clear.** The viewer is watching the puppets' faces, so keep captions, labels, link lines
  and the disclosure off every character's head region (face, eyes, mouth, hair, fur, ears, antennae, hat, and the room
  above the head) when the moment is theirs. The framing that does it: captions ≈ 40 px off every head region; when a
  head reaches the caption band, the line moves up to CS-3 or to another shot. A word brushing a hat brim for a beat can
  be fine; what's never fine is a face buried or a head chopped by accident. The geometry is in §3.6. The iris porthole
  holds every character's head.
- **No text over text.** One caption at a time; label words only inside the screen rect; the disclosure in the legal band
  at the top; captions hidden on the wordmark card.
- **On the word, on the action.** Captions cut on 2 f before the first word and off 0.25 s after the last; a label word
  that is spoken lands 2 f before its word, otherwise on its hard swap ±2 f. Cuts land on a completed or matched motion
  ±2 f; no cut inside a line (except a match cut that keeps the same speaker on screen, R-6).
- **Product truth.** Every label word and product claim on screen is in the approved claims list (SH-7) or the script,
  character for character. Pack shots are the brand's own files, shown unaltered. No invented claims, prices, ratings,
  awards, "new", "best" or "#1"; numbers only when the claims list states them. Character dialogue is fiction and is never
  presented as a customer testimonial.
- **Words exact.** Captions verbatim from the script, its casing kept; listed profanity masked inner-style ("F**k",
  "S**t") while the audio stays as the brand mixed it; brand, product and character names spelt exactly as in the glossary.
- **Readable.** Captions 64 px, ≥ 4.5:1 against the plate under them (CS-2 on every bright span); label words 48–64 px,
  `#9C0012` on the `#C9D9EE` sky ≈ 6.0:1; the disclosure 24 px set as legal small print (the legal text class, floor 22 px).
- **Disclosure.** When the post is paid (an agency or creator posting for the brand), "Paid partnership" shows from 0.0 s
  for at least 2.0 s, plus the platform's own paid-partnership label. It's a legal disclosure, not decoration.
- **Safe zones.** Captions, labels, links and the disclosure sit inside x 64–1016, y 110–1500; nothing that carries meaning
  below y 1500 or in the right 110 px between y 900 and 1540.
- **Privacy.** Any personal data visible on an in-world phone, letter or screen is blurred for its whole time on screen.
- **Someone else's media.** A real show, match, company, celebrity or retailer named on an in-world screen, sign or line
  is the real one: the creator's file first, else fetched from the web with its source noted, else a generic stand-in
  (§12.4).
- **Audio.** The plate mix as the brand delivered it; −14 LUFS integrated, true peak ≤ −1.5 dBTP; the last sound ends
  ≤ 6 f after the wordmark hold ends.

**Never in this style:**
- A title, banner, "NEW!", product name card or logo bug in the hook or over the story beats.
- A full-frame pack shot, product turntable or price card pasted over or between plates (the product stays in the world;
  FB-8 is the only way round a missing screen plate).
- Engine zooms, punch-ins, shakes, speed ramps, reverse, freeze-frames longer than 12 f, motion blur, frame blending or
  optical-flow retiming on plates.
- Dissolves, cross-fades between plates, whip pans, zoom transitions, light leaks, film burns, flash frames between plates,
  glitches or RGB splits. (The warm glow into the sensory trip is the trip's own recipe, §9.1.)
- Coloured, bold, stroked (except CS-2), boxed or karaoke caption words; ALL-CAPS captions unless the script writes the word
  in caps.
- Meme sounds, cartoon boings, record scratches, laugh tracks or any pack cue over a character's line.
- Stickers, emoji, arrows, circles, marker notes or reaction-GIF overlays: nothing is drawn over the handmade world.
- Unstroked pale captions on a bright plate (the honey-yellow and sunlit-felt failure, v03 @0:06).
- Label words that aren't in the claims list, or more than 2 words in one label.
- A wordmark on anything but black, a wordmark narrower than 600 px, a tagline or URL card that outlasts the wordmark's own
  hold, or a black tail after the card longer than 0.2 s.
- Grain, vignette, bloom, LUTs or a "film look" added on top of the plates.
- A look-alike of a real broadcaster's graphics: a named show is the real one (§12.4), anything else is a plainly generic
  show.

---

## §3 Worlds, layouts, stage moves, safe zones

No presenter: the brand's plates are the picture, and the engine draws only small things into them.

### 3.1 Formats
| Field | F-A Dialogue sketch (default) | F-B Product broadcast | F-C Vignette |
|---|---|---|---|
| When | Plates with character dialogue: a two-character mini story that turns on the product and ends on a button line | Silent or music-only plates with a locked-off in-world screen (TV, phone, billboard, shop window); the engine runs the product spot on that screen | One short character moment with no dialogue (a sip, a stroll, a look) |
| Evidence | v03 | v02 | v01 |
| Duration | 20–30 s | 18–30 s | 10–16 s |
| Differences | — | graphics `support` (the screen spot); anchors on | — |
| Layouts | L-plate, L-endcard (+ fallbacks L-plate-band, L-plate-blur) | same | same |
| Default hook | HA-16 | HA-16 | HA-16 |
| Structure | setup → gag/journey → product turn → button → logo | setup → product broadcast → reactions → wide hold → logo | action → wide → button → logo |
| End | T-IRIS → wordmark card (held 1.8–2.4 s) | T-CUT-BLACK → wordmark card (1.8–2.4 s) | T-CUT-BLACK → wordmark card (1.6–2.0 s) |
| Captions | CS-1 (CS-2 on bright plates, CS-3 where a head sits low) | only if a plate has speech | none (no speech) |

All three share one spine: plates open mid-action with no added text, small pale-yellow two-line captions only when someone
speaks, hard cuts on action, the product inside the world, a button beat, the wordmark alone on black last.

**Which format.** Dialogue in the plate mix → F-A. No dialogue and a locked-off in-world screen plate of at least 6 s
(SH-8) → F-B. No dialogue, no screen, under 18 s of plates → F-C. No dialogue, no screen, 18 s or more → the F-A structure
without captions: the sketch reads as pantomime (FB-3).

### 3.2 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-plate** | `footage` | The brand's plates, full frame, untouched (in the evidence: warm tungsten key, shallow depth of field, miniature sets; peach `#F7D7B5`, warm skin `#E8A46A`, teal fills `#2FA39A`, honey `#F6D21B`) | Every story beat; the in-world screen spot is drawn into a plate | Hard cuts between plates |
| **W-black** | `void` | `#000000` (`ink`), no texture, no noise | The iris surround, the cut to black, the wordmark card | T-IRIS closes into it; T-CUT-BLACK cuts into it; the reel ends on it |

The in-world screen's content (sky, labels, packs, static) is **not a world**: it's a scene clipped to the screen rect inside
W-plate (P-SCREEN-*).

### 3.3 Layout library
| ID | Name | Engine | Rects | Caption |
|---|---|---|---|---|
| **L-plate** | Full plate | `full` | the plate fills 1080 × 1920 | CS-1 block centre y 1420 (CS-3 y 1180) |
| **L-endcard** | Wordmark on black | `hidden` (stage hidden, W-black shows) | graphic x 64, y 640, w 952, h 640 (x 64–1016, y 640–1280) | none (captions hidden on the card) |
| **L-plate-band** | 16:9 plate band (fallback FB-2) | `letterbox` | band_h 608, centre y 860 → band y 556–1164, fill `#000000` | CS-1 at y 1290 (under the band) |
| **L-plate-blur** | 4:5 or 1:1 plate band (fallback FB-2) | `blurfill` | band_h 1350, centre y 900 → band y 225–1575, blur 48 px, luma −0.35, scale 1.15 | CS-1 at y 1420 (inside the band) |

**One layout per plate,** decided by the plate's aspect. A reel mixes L-plate and a fallback layout only when the brand's
plates are mixed, and every fallback shot is listed in the plan. The plate fills the phone almost the whole reel; the card
is the last two seconds.

### 3.4 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-CUT** | Plate to plate | `via: cut`, 0 f | Every shot change |
| **G-IRIS-END** | Plate to end card | The P-IRIS-OUT scene closes to r 0 on the plate (§9.1 T-IRIS); on the frame it reaches 0 the stage switches to `L-endcard` (`via: cut`) and the world is W-black | F-A ending |
| **G-BLACK-END** | Plate to end card | `via: cut` straight to `L-endcard` on the frame after the button plate's out point | F-B, F-C ending |
| **G-BAND** | Plate to a fallback band | `via: cut` (never a morph: the band arrives with its plate) | FB-2 plates only |

### 3.5 Layout diagrams
```
L-plate (F-A dialogue shot)                 L-endcard
┌─────────────────────────┐ 0               ┌─────────────────────────┐ 0
│ (IG top UI, keep clear) │ ← y 0–110        │                         │
│ Paid partnership        │ ← legal y 150    │                         │
│                         │   (paid only,    │                         │
│   [character heads,     │    from 0.0 s)   │                         │
│    eyes y 480–1300]     │                  │   ╭╮ wordmark (image)   │ ← centre y 960
│                         │                  │  ╰──╯ 600–700 px wide   │   ≈ 250 px tall
│   CS-3 line y 1180 ─ ─  │ ← only when a    │                         │
│                         │   head is low    │  link in bio            │ ← link line y 1180
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

### 3.6 Safe zones and the characters' faces
- **Meaning text box:** x 64–1016, y 110–1500. Nothing that matters below y 1500 or in the right 110 px between y 900 and
  1540 (Instagram's buttons).
- **Caption band (CS-1):** block centre y 1420; a two-line block (64 px × line height 1.25, line pitch 80 px; the source
  pitch measured 79 px) occupies y 1340–1500, a single line y 1380–1460.
- **High band (CS-3):** block centre y 1180; a two-line block occupies y 1100–1260.
- **Band fallback (L-plate-band):** captions at y 1290, under the band's bottom edge (y 1164).
- **Legal band:** y 136–164 (the 24 px line at y 150), left-aligned at x 64.
- **Screen band (F-B):** wherever the plate's screen is; label words stay ≥ 24 px inside the screen rect and inside the
  meaning box.
- **End card band:** the wordmark y 835–1085 (centre 960); the link or stockist line y 1160–1200.

**The characters are the people here.** There's no presenter, but every puppet, felt animal and clay figure has a head the
viewer is watching, and it's treated exactly as a person's: keep the face, eyes, mouth, hair or fur, ears and the room
above the head clear of anything in front, captions included, unless the moment wants otherwise; judge it on the frame.
- **Where heads sit:** plates are framed with the characters' eyes between y 480 and 1300 (SH-2), so in a normal plate the
  CS-1 band (y 1340–1500) runs under the characters, clear of them.
- **The head band** (from the anchor pass, §8.6) is the y range covered by any character's head region across the shot,
  sampled every 0.5 s. Captions keep 40 px off it.
- **Which band, per shot** (heads first, captions second):
  1. The head band stays clear of y 1300–1540 (the CS-1 band with its 40 px) → CS-1.
  2. Otherwise, the head band stays clear of y 1060–1300 (the CS-3 band with its 40 px), as when a small character sits at
     the very bottom of the frame → CS-3 (block y 1100–1260).
  3. Otherwise (a big close-up whose head fills both bands) → the line moves to the previous or next shot, where the
     speaker or listener leaves a band free, rather than onto the face.
- **The iris:** the porthole (r 510, centre on the faces' midpoint) contains every character's head while it holds; a
  caption under the porthole (v03 @0:29) stays 40 px off the heads inside it.
- **Behind the characters** is the plate itself; the engine never draws there (no cut-out in this style).

---

## §4 Colour system

### 4.1 Role palette
| Role | Hex | Its one job | Text on it | Contrast |
|---|---|---|---|---|
| `primary` | `#9C0012` (the audit sampled `#980014`–`#9F000D` on the TV sky) | Label words on the in-world screen; the link line's accent dot | `paper` | white on it 8.7:1; as text on `accent` ≈ 6.0:1 |
| `accent` | `#C9D9EE` (the pale screen sky) | The ground of engine-built screen content: a pale sky with soft clouds | `primary` | ≈ 6.0:1 |
| `paper` | `#FFFFFF` | The wordmark (in the brand's white file) and its type-set fallback, the link and stockist lines, the disclosure | `ink` | 21:1 on black |
| `ink` | `#000000` | The end card, the iris surround, the cut to black | `paper` | 21:1 |
| `shade` | `#2A1E14` | CS-2's caption stroke and shadow tint on bright plates | — | — |
| `static` | `#8E8E8E` | The mid grey of the in-world screen static | — | — |

The captions' pale yellow `#F6FA8C` belongs to the caption skin (§5.3), not to a role: it's measured from v03 (glyph cores
`#F5FF7C`–`#F7FF7C`) and never changes with the brand.

`primary` and `accent` are the brand's two colours when they give them: label red becomes their word colour, the sky their
light colour, nudged at setup so white keeps ≥ 4.5:1 on `primary` and `primary` keeps ≥ 4.5:1 on `accent`.

### 4.2 Meanings
- **The plates own colour.** Every hue in the story is the brand's set design; the engine adds no colour to a plate.
- **Pale yellow = words someone says** (captions). **White = the brand's signature** (the wordmark) and its small lines.
- **Red label words = what the brand claims**, shown only inside a screen in the world.
- **Black = the story is over;** only the wordmark lives there.
- Brand colours appear only on brand elements: label words, the screen sky, the wordmark (in its own file's colours).

### 4.3 Rules
- The edit adds at most the two brand colours to a frame, and only inside the screen; plate colours don't count.
- Label words sit only on the `accent` sky inside the screen, never directly on a plate.
- Captions are always the pale yellow; never brand-coloured.
- One theme: the plates set the look. Plates are never regraded; if plates from two shoots differ in white balance, the
  brand fixes it in their grade and the plan says so.

---

## §5 Type and captions

### 5.1 Font map
| Slot | Family | Weight | Class (the alternatives that keep the look) | Uses |
|---|---|---|---|---|
| `caption` | **Plus Jakarta Sans** | 500 (CS-2 600) | friendly geometric-humanist sans 400–600 (Plus Jakarta Sans, Inter Tight, Poppins, Jost) | Captions, the link and stockist lines, the disclosure |
| `label` | **Barlow Condensed** | 700 | condensed grotesque caps 600–700 (Barlow Condensed, Anton) | Screen label words |
| `wordmark` | **Fraunces Soft** (Fraunces with SOFT 100 / opsz 9 baked in, so canvas text gets the soft shapes too) | 800 | soft chunky serif 700–900 (Fraunces Soft, Fraunces, EB Garamond, Instrument Serif, Lilita One, Source Serif 4) | The type-set wordmark fallback only (FB-5) |

The brand's wordmark and pack shots are **image assets**, never fonts. Devanagari captions use Noto Sans Devanagari 500 (it
has no italic; none is used).

### 5.2 No headline element
This style has no headline, banner, pill or title card (`type.headline.kind: none`). The wordmark card (§6.7) is the only
"title", and it comes last. The hook's promise lives in the post title (§6.5).

### 5.3 Caption system profiles

Captions here are the opposite of a loud reel's: small, quiet, and only for speech. They exist so a muted viewer can follow
the characters, and they get out of the way of the felt and clay. One style for every character, no emphasis, no animation:
the line is simply there while it's said.

**CS-1 "Soft dialogue"** (the default; `extends: lib:chamberlain`):

| Group | Value |
|---|---|
| Mode | `full` / `support` / `mute_safe`; only spoken lines get captions |
| Chunking | `unit: sentence`: one character line per chunk (split at the line's own sentence end); 1–8 words; ≤ 24 characters per line; ≤ 2 lines; break at the natural phrase boundary closest to the middle ("Dude, you've GOT / to try this", "Told ya! I can show you / where it came from"); never split a name, number or unit; a new chunk on every new speaker and every sentence end; a line over 8 words or 48 characters splits into two chunks at its comma |
| Timing | lead 2 f before the first word; **hard on, hard off (0 f)**: the source caption is full on its first frame (v03 @1.167) and gone in one frame (@30.23); a line spoken across a cut stays on through it (@1.42); min hold 0.3 s per word; tail 0.25 s after the last word; held through pauses up to 0.6 s, then off; a pause of 0.9 s or more always ends the chunk |
| Skin | Plus Jakarta Sans 500, **64 px**, `TC-subtitle`, case `as_spoken` (the script's casing: "GOT" stays caps), tracking 0, **pale yellow `#F6FA8C`** (measured v03 @0:01.5 and @0:08: glyph cores `#F5FF7C`–`#F7FF7C`, reading `#F1FFD1` over yellow felt @0:20; not white), no stroke, shadow `0 2 10 rgba(0,0,0,.55)`, line height 1.25 (cap height 44 px measured, so ≈ 63 px Plus Jakarta Sans), no container |
| Position | `fixed_y`, block centre **y 1420**, centred at x 540, max width 860, `avoid_face: true`; the same y in every plate shot (the source's first line sits at ≈ 1444; lifted so a two-line block ends above y 1500) |
| Speakers | none: every character's line is the same pale yellow (the frog and the bee share one style in v03) |
| Emphasis | `none`. Emphasis exists only where the brand's script writes caps |
| Karaoke / two-tier / duet / kinetic stack | none |
| Hide rules | hidden on the wordmark card; shown over the iris (on its black surround, v03 @0:29) |
| Language | script Latn; English terms kept verbatim; spelling not normalised (the script wins); profanity mask `inner`; glossary = brand, product and character names |

**CS-2 "Bright plate"** (as CS-1 except): weight 600, stroke 2 px `shade` `#2A1E14`, shadow `0 2 14 rgba(42,30,20,.75)`.
**Use:** every shot logged `bright` in the plate log (sky, white walls, honey, snow, light fabric in y 1340–1500). It keeps
the look of soft pale text while measuring ≥ 4.5:1.

**CS-3 "High band"** (CS-1's skin): block centre **y 1180**. **Use:** every shot whose head band reaches into the CS-1
band (y 1300–1540 with its clearance) but stays clear of y 1060–1300 (§3.6). A bright high band takes CS-2's skin via a CS-2 override on that span with the line placed at y 1180; write the line
on CS-3 and note it in the plan; never stack two profiles on one span.

Profiles switch per span with `captions.overrides: [{t: [a, b], profile: "CS-2"}]`; never write caption cards by hand.

### 5.4 Other text
| Element | Recipe | Hold |
|---|---|---|
| **Screen label** (P-SCREEN-LABEL) | Barlow Condensed 700, caps, tracking 0.01, `primary` on the `accent` sky, `text_class: "TC-label"`; size = 12 % of the screen rect's height, clamped to 48–64 px (measured v02 @0:12: "EFFORTLESSLY DRINKABLE" 504 px wide on a 660 × 446 px screen → 54 px Barlow Condensed 700); centred on the screen, centre y = screen top + 0.21 × screen height; ≤ 2 words (a two-word label may run to 22 characters: "EFFORTLESSLY DRINKABLE"), max width = screen width − 80 px; **blinks** 6–7 f on / 6 f off (≈ 2.4 Hz) while its pack builds (v02 @8.34–14.31) | 1.4–2.0 s per word (≈ 4–5 blinks) |
| **Wordmark image** (P-WORDMARK-CARD) | The brand's file, white, centred (540, 960), width 648 px (600–700), fades in over 5 f with no scale (F-A: under the iris snap, v03 @30.20–30.37) | 1.8–2.4 s |
| **Type-set wordmark** (FB-5) | Fraunces Soft 800, `paper`, 104 px (92–120); the brand name's first word on a 48° arc (radius 520 px), any second word straight below at 70 % size, the whole rotated −6°, total width 600–700 px, centre y 960 | as the image |
| **Screen wordmark arc** (P-SCREEN-LINEUP) | The wordmark at 85 % of the screen width, centre y = screen top + 0.45 × height, grows 0.65 → 1.0 in held steps of 2 f over ≈ 18 f with a tilt that settles −6° → 0° (stop-motion steps, not a smooth tween; v02 @15.30–15.87), over the pack lineup | 1.0–1.6 s after it lands |
| **Link line** (P-LINK-LINE) | Plus Jakarta Sans 500, 40 px, `paper`, sentence case, centre y 1180 on the end card; the reel's link line ("link in bio" by default), in over 8 f after the wordmark settles | to the end |
| **Disclosure** (P-DISCLOSURE) | Plus Jakarta Sans 500, 24 px, `paper`, shadow `0 1 4 rgba(0,0,0,.6)`, x 64, y 150, "Paid partnership" (or the brand's required wording), legal small print | from 0.0 s for ≥ 2.0 s (2.5 s is a good default), out over 6 f |
| **Stockist line** (P-STOCKIST-LINE) | Plus Jakarta Sans 500, 40 px, `paper`, "Now at <retailer>" set in type (the quiet look: the brand's wordmark is the only mark on the card), end card y 1180 (in place of the link line) | to the end |

### 5.5 Language and numbers
- Captions are the brand's script, verbatim, aligned to the plate audio; brand, product and character names exactly as in
  the glossary. The engine never adds caps, bold or colour (`as_spoken`).
- Profanity: `inner` on screen ("F**k", "S**t", "B***h"); the audio is the brand's call.
- Hinglish captions (`hinglish/hinglish/Latn`): romanised as the script writes it; English product terms verbatim. Hindi
  (`hi/hi/Deva`): Noto Sans Devanagari 500, 64 px, same position; the mask uses `mask_words` for the Hindi profanities the
  brand lists.
- Numbers appear only from the claims list, written as the brand writes them; international grouping by default.
- Label words are in the on-screen language (English by default); a Hindi-language reel keeps English label words only if
  the claims list is English.

---

## §6 Hook system

**The hook title, in this style:** nothing is written over the hook, so the promise lives in two places. On screen, it's
the picture: a character already doing something, wanting something, in a world you've never seen. In words, it's the
**post title** (the first line of the Instagram caption), and it promises the way a children's book title does: a
character, their small problem or want, a curiosity gap ("the owl who couldn't sleep", not "Herbal sleep tea, now in
stores"). It's true to what the sketch delivers. Write 8–10 candidates (§6.5), check the best against the stopper test,
pick one and keep two alternates for the storyboard.

### 6.1 The stopper test
| Test | This style's number |
|---|---|
| **Thumbnail** | f0 at 25 % scale shows a recognisable character or object in a miniature set: the subject fills ≥ 20 % of the frame height |
| **Motion at f0** | the plate is moving on f0 (a gesture, an entrance, a camera move, a screen playing). A plate that starts on a held still is trimmed to its first moving frame |
| **Payoff by** | by 5.0 s the viewer knows who the sketch is about and where they are (the subject full in frame, ≥ 20 % of the frame height, for at least 1 s). F-B: the in-world screen is on screen by 3.0 s and the product is on it by 8.0 s. F-C: the product is in a character's hand or in frame by 5.0 s |
| Mute | not pass/fail: these hooks read as pantomime; captions carry any speech |
| Read time | none (no headline) |

The first change is a cut on the action, when the opening action completes (the source ads cut at 1.42, 2.77 and 2.92 s).
A quiet first three seconds is the style, not a weakness: the motion inside the plate is the stopper.

### 6.2 HA-16 Diegetic (default)
The hook is **a character already doing something** in its miniature world. Nothing is written over it. The first change
is a cut on the action into a closer or wider size. By 5.0 s the viewer knows who this is, where they are and what they
want. Frame 0 never shows an empty set, a title card, the wordmark, a pack shot, a still frame or a slow fade from black.

**F-A Dialogue sketch (v03 @0:00–0:05):**

| t (s) | Beat | Tone | Plate / visual | Caption | Cut / move | Sound |
|---|---|---|---|---|---|---|
| **f0** | Opener | setup | **P-COLD-ACTION**: wide or medium of character 1 in the set, already moving (holding a snack on a rock; a second character flying in from the frame edge). Subject ≥ 20 % of frame height | none | — | the plate mix only |
| 0.0–1.1 | Action arc | setup | Character 2 crosses to character 1 (the entrance is the motion that stops the thumb) | none until the first word | — | — |
| 1.1–1.4 | First line | setup | Same shot | **CS-1** cuts on 2 f before the first word ("Dude, you've GOT / to try this", on at 1.17 s) | — | — |
| 1.4 | First cut | setup | **P-MATCH-CUT** to a medium close-up of both characters at the end of the approach | the line holds across the cut (same speaker) | hard cut ±2 f of the action's end (1.42 s) | — |
| 1.4–5.0 | The want | setup | **P-CHAR-LINE-CU**: character 2 offers the thing; character 1 reacts ("Oh… WOW") | the next line on its first word | at most one more cut | — |
| **≤ 5.0** | Payoff | | Two characters, the place and the offer are established | | | |

**F-B Product broadcast (v02 @0:00–0:05):**

| t (s) | Beat | Tone | Plate / visual | Caption | Cut | Sound |
|---|---|---|---|---|---|---|
| **f0** | Opener | setup | **P-OTS-WATCH**: over the shoulder of a character watching the in-world screen; the screen is already playing (P-SCREEN-SHOW) | none | — | the plate mix only |
| 0.0–2.8 | Watching | setup | Locked off; the only motion is the screen and a small character gesture | none | — | — |
| 2.8 | First cut | setup | **P-ESTABLISH-WIDE**: the characters on the couch (who is watching) | none | hard cut | — |
| 2.8–5.2 | Who | setup | The characters settle, reach for drinks | none | — | — |
| 5.2 | Turn on | awe | Cut to the screen close shot; **P-SCREEN-STATIC** (1.2 s), then the spot opens | none | hard cut | a soft `transitions` cue on the static |
| **≤ 5.0** | Payoff | | Watchers and place established | | | |

**F-C Vignette (v01 @0:00–0:03):**

| t (s) | Beat | Tone | Plate / visual | Caption | Cut | Sound |
|---|---|---|---|---|---|---|
| **f0** | Opener | setup | **P-PRODUCT-IN-HAND** inside **P-COLD-ACTION**: a medium shot of the character mid-sip (the cup already at the lips at 0.33 s) | none | — | the plate mix only |
| 0.0–1.2 | Sip | setup | Sip, lower the cup | none | — | — |
| 1.2–2.9 | Pose | setup | A head tilt, a pose, the product in hand | none | — | — |
| 2.9 | First cut | setup | **P-ESTABLISH-WIDE** / **P-PATIENT-HOLD**: the character walks toward camera down a recognisable street | none | hard cut (2.92 s) | — |
| **≤ 5.0** | Payoff | | Character, product and place established | | | |

### 6.3 Alternate hooks

**HA-15 Atmosphere (the product as the moving object).** Open on the product itself doing something in the world (steam
rising from the cup, a pack sliding across a miniature counter, a phone lighting up on a bedside table). The first caption
or screen label by 5.0 s.

| t (s) | Visual | Caption | Cut |
|---|---|---|---|
| f0 | Insert of the product in motion, set dressing around it | none | — |
| 0–2.5 | The motion completes (steam curls, the phone buzzes across the table) | none | — |
| 2.5–3.0 | Cut on the motion to the character who reacts to it | none | hard cut |
| ≤ 5.0 | First line or label word | CS-1 on the first word | — |

For example: a felt teabag lowers itself into a cup by its string, and the mouse who owns the cup peers over the rim. It
travels beyond drinks: a clay phone buzzes and slides toward the desk's edge, and a clay hand catches it.

**HA-14 Cold authority (mid-line open; F-A only).** The first word is spoken at 0.00–0.10 s, so the caption is on f0, and
the plate is mid-action.

| t (s) | Visual | Caption | Cut |
|---|---|---|---|
| f0 | Medium close-up of the speaking character, mid-gesture | the first line on f0 (hard on, like every caption) | — |
| 0–1.5 | The line plays | held | — |
| 1.5–2.5 | Cut to the listener's reaction (P-REACTION-RUN, one shot) | the next line | hard cut |
| ≤ 3.0 | Who and what established | | |

For example: a clay barista bear mid-sentence, "You're telling me you've never had it cold?"

**HA-13 Cold action (the chaotic open; F-A, only when the brand wants a livelier edge).** A character crashes, falls or
bursts in, with its line on f0 and the first cut by 2.1 s.

| t (s) | Visual | Caption | Cut |
|---|---|---|---|
| f0 | Fast action already in progress (a tumble, a door flung open) | the shout as CS-1 on f0 | — |
| 0–2.1 | The action lands | held | the first cut by 2.1 s, on the landing |
| ≤ 2.3 | The subject in frame, the problem obvious | the next line | — |

For example: a felt squirrel skids into frame on an acorn, "I'm LATE!"

### 6.4 Hook pairs by topic (subject → reveal)
The pair for every hook here is **subject → reveal**: who or what is on f0, what's revealed by 5.0 s, and where the product
turn lands later.

| Topic | First subject (f0) | Revealed by 5.0 s | Product turn (later) |
|---|---|---|---|
| Cold brew launch | A clay fox on a hot pavement fanning itself | It's stranded in a desert town; a friend arrives with something "cold" | At 60–70 %: a glacier-blue cold-brew waterfall (P-REVEAL-WIDE), then the can in paw |
| Herbal sleep tea | A felt owl yawning on a branch at noon | The owl can't sleep; the moon character offers a cup | At 65 %: the pack glows on a bedside stump (P-PRODUCT-IN-HAND) |
| Snack multipack | A clay kid opening a lunchbox | The lunchbox is empty; the dog under the table looks guilty | At 55 %: the dog's TV shows the multipack (F-B screen spot) |
| Morning coffee | A clay character mid-sip in sunglasses (v01) | A sunny street, the character walking with the cup | The cup is the product from f0 (F-C) |
| Budgeting app | A felt hamster counting coins in a jar | The jar is empty by Thursday; a friend shows a phone | At 60 %: the phone screen shows the app's spending ring (P-SCREEN-* on the phone) |
| Splitting costs | Four clay friends at a pizza table, one hand reaching for the bill | Nobody wants to pay; awkward silence | At 60 %: one phone shows the split screen (claims-list words) and everyone relaxes |

### 6.5 Post title writing
The reel has no on-screen headline; the post title carries the hook in words.
- **Shape:** `[character] + [their small problem or want]`, lowercase except names, ≤ 8 words, one emoji at most at the end,
  no hashtags in the first line.
- **Templates:** "{character} just wanted {thing}" · "{character} found out where {product noun} comes from" · "pov:
  {character} discovers {benefit in plain words}" · "{character} vs {small daily problem}" (the braces are writing slots).
- **Pick:** write 8–10, keep the one whose character is on f0 and whose want the sketch pays off; two alternates go to the
  storyboard.
- **Never:** "You won't believe…", "BEST {product} EVER", a claim not in the claims list, a price, all caps.

### 6.6 Hook sound
The hook is the plate's own mix. No pack cue in the first seconds except the in-screen static (F-B, soft). When the plates
are silent (FB-3), the music bed enters from f0 at bed level (§11).

### 6.7 CTA, end card and disclosure
| Device | Spoken pattern | On-screen element | Hold | Where |
|---|---|---|---|---|
| **end_card** (default) | none (or the brand's own end line in the plate mix) | The wordmark alone on black (P-WORDMARK-CARD) | 1.8–2.4 s | the last 1.6–2.4 s |
| **link_bio** | none | Wordmark + link line at y 1180, in over 8 f after the wordmark settles | the link line readable ≥ 1.5 s | the end card |
| **post_only** | none | Wordmark card only; the offer goes in the post text | 1.8–2.4 s | end |
| **none** | none | The wordmark card still closes the reel (the brand's signature is the style, not a CTA) | 1.6–2.0 s | end |

Silence before the card: the button line's last word ends at least 6 f before the iris snaps shut or the cut to black.

**The wordmark end card** (P-WORDMARK-CARD), every reel:

| Property | Spec |
|---|---|
| Ground | `ink` `#000000`, full frame (L-endcard, W-black) |
| Wordmark | The brand's file (SH-5), white, centre (540, 960), width 648 px (600–700), height by its aspect (≈ 250 px for an arched two-line mark; measured v03: 633 px wide, y 842–1077) |
| Entry | F-A: fades in over 5 f under the iris snap, no black gap, no scale (v03 @30.20–30.37). F-B, F-C: 4 f of black after the cut, then the same 5 f fade |
| Hold | 1.8–2.4 s (F-C 1.6–2.0 s; v03 held 1.87 s); the whole card ≤ 2.5 s |
| Exit | A hard end on the last frame (no fade-out, no black tail over 0.2 s) |
| Extra lines | One at most: the link line (`link_bio`) or the stockist line, 40 px white at y 1180, in over 8 f, 0.3 s after the wordmark settles. Never a tagline, URL card, QR, social icons or "follow us" |
| Type-set fallback (FB-5) | Fraunces Soft 800 white: first word on a 48° arc (radius 520 px), second word straight below at 70 %, rotated −6°, total 600–700 px wide, centre y 960 |

**The disclosure** (P-DISCLOSURE): when an agency or creator posts the ad for the brand, "Paid partnership" (or the brand's
required wording), 24 px white with a soft shadow at x 64, y 150, from 0.0 s for at least 2.0 s (2.5 s by default), in and
out over 6 f, plus the platform's own paid-partnership label. It's a legal disclosure, and it's the only text the hook
carries besides an f0 caption under HA-14 or HA-13. When the brand posts on its own account, there's none.

**The screen wordmark (F-B):** the wordmark also appears once inside the screen spot (P-SCREEN-LINEUP), in its own colours
over the sky.

The brand's colours appear only on label words, the screen sky and in the wordmark file; no sponsor card, product card or
logo bug during the story.

---

## §7 Structure and rhythm

### 7.1 Structure: the sketch (every format)
| Beat | F-A Dialogue sketch (24–30 s) | F-B Product broadcast (20–30 s) | F-C Vignette (10–16 s) |
|---|---|---|---|
| **setup** | 0 → 15–20 % (0–5 s): who, where, the want (an offer, a problem, a craving) | 0 → 18 % (0–5.2 s): who is watching what | 0 → 25 % (0–3 s): the character with the product |
| **gag / journey / broadcast** | 20 → 60 % (5–17 s): the journey or the misunderstanding, a few plates, one or two of them long travelling shots | 18 → 60 % (5.2–17 s): the screen spot ritual (§7.3) | 25 → 70 % (3–9 s): one patient wide (a walk, a ride, a look around) |
| **product turn** | 60 → 78 % (17–22 s): the product revealed in the world (P-REVEAL-WIDE, P-PRODUCT-IN-HAND), the longest held shot of the second half | 60 → 85 % (17–24 s): reactions to the spot (P-REACTION-RUN) | (the product was in hand from f0) |
| **button** | 78 → 92 % (22–27.5 s): the payoff line or non-sequitur; the masked punch line belongs here | 85 → 93 %: the wide hold (P-WIDE-HOLD-OUT) | 70 → 86 % (9–12 s): a non-sequitur (a cat in the bushes, v01) |
| **logo** | the last 1.8–2.4 s: T-IRIS → P-WORDMARK-CARD | the last 1.8–2.4 s: T-CUT-BLACK → card | the last 1.6–2.0 s: T-CUT-BLACK → card |

Measured: v03 setup 0–5, journey 7–20, reveal 20–23, button 23–29.6, logo 29.8–32.2; v02 setup 0–5.2, broadcast 5.2–18.3,
reactions 19.5–23.9, wide hold 23.9–28.3; v01 sip 0–2.9, walk 2.9–9.1, button 9.1–12.0.

### 7.2 Markers
None (`markers: none`). A sketch has no numbering, chapter chips or progress bar. The screen spot's label words are claims,
not markers.

### 7.3 The rituals (frames at 30 fps)

**The line ritual (F-A, every spoken line):**
1. The speaking character's shot is on screen ≥ 8 f before the line (cut in on the previous line's end or on an action).
2. CS-1 cuts on (0 f) 2 f before the first word.
3. The line plays; no cut inside it (R-6).
4. The caption holds through up to 0.6 s of pause, then cuts off (0 f).
5. Cut on the reply's first word −2…+3 f to the replying character, or hold the two-shot when both are in it.

**The screen spot ritual (F-B; times from the cut to the screen shot; measured frame by frame on v02 @0:05.17–0:19.49,
29.97 fps):**

| Step | Pattern | Duration | Frames (30 fps) | Change | Evidence |
|---|---|---|---|---|---|
| 0 Show tail | P-SCREEN-SHOW | 0.27 s | 8 | the cut lands on the show still playing | 5.17–5.43 |
| 1 Static on | P-SCREEN-STATIC | 1.1 s (0.6–1.8) | 33 | hard on (no glow ramp) | 5.43–6.55 |
| 2 Pack 1 placed | P-PACK-IN (hand) | 0.8 s | 24 | the pack steps in on 2–3 f poses | 6.81–7.61 |
| 3 Empty sky | (sky only) | 0.7 s | 22 | hard | 7.61–8.34 |
| 4 Label 1 + pack 2 builds | P-LABEL-PLUS-PACK | 1.4–1.6 s | 42–48 | the label blinks 6–7 f on / 6 f off; the pack builds in 4–5 held steps of 3 f | 8.34–9.74 |
| 5 Label 2 + pack 3 (hand) | P-LABEL-PLUS-PACK | 1.9 s | 56 | the same blink | 9.94–11.81 |
| 6 Label 3 + pack 4 builds | P-LABEL-PLUS-PACK | 1.7–2.3 s | 50–70 | the same blink | 12.01–14.31 |
| 7 Clear sky | (sky only) | 0.5 s | 16 | hard | 14.31–14.85 |
| 8 Lineup + wordmark | P-SCREEN-LINEUP | 2.1 s | 63 | packs hard; the wordmark grows in 2 f steps over ≈ 18 f, then holds | 14.85–16.95 |
| 9 Static off | P-SCREEN-STATIC | 1.1 s | 32 | hard | 16.97–18.05 |
| 10 Show returns | P-SCREEN-SHOW | 1.4 s | 43 | hard; then cut to the reaction run | 18.05–19.49 |

About 14.3 s in all, one locked-off shot. The ritual has room for three claims: with two, drop step 5; with one, drop steps
4–5. With one SKU, every pack step shows the same pack from alternating sides (x 42 % / 58 % of the screen). Everything
inside the screen moves on **held steps of 2–3 f (≈ 10–15 images/s) or the 6 f blink**, never on smooth tweens (§10.2).

**The journey step ritual (F-A gag beat, 2–4 steps):** each step is one plate in a new place (a log, river stones, giant
leaves), 2.5–4.5 s; the travelling character enters from the side the previous shot exited (R-11); a line per step at most
("Follow me!", "Hold on, I can't fly!").

### 7.4 Open loops
- **The want loop:** the setup states or shows a want (an offer, "you've GOT to try this"; an empty jar; a show everyone is
  watching). The product turn pays it, on screen.
- **The screen loop (F-B):** the static promises something; the spot pays it.
- A sketch this short needs no re-hook: the hook is over within seconds, and the want carries the viewer to the turn.

### 7.5 Rhythm by feel
- **The action is the rhythm.** A shot lasts as long as its movement: in on the start of a gesture, out the frame it
  completes. A close-up holds its whole line plus 8–15 f, so the line lands before the cut. Nothing is cut short to feel
  fast, and nothing is held past its action to feel arty.
- **Calm and even, with one swell.** The setup is unhurried. The journey quickens a little (steps of 2.5–3.5 s). The product
  turn is the one big held moment, a 2–3 s wide that gets the longest shot of the second half. The button is a beat of
  stillness and a small laugh. The logo is quiet. Escalate with scale (a bigger set, a brighter reveal), never with speed
  tricks.
- **Long shots travel.** A shot of 4 s or more earns its length only when the plate's camera moves or a character travels
  inside it; the long, patient walk is a pleasure because it's rare.
- **Held poses are beats, not dead air.** A plate's own frozen pose (v01 @7.50–9.08, 38 f) is the animators' timing: keep
  it. A silent, motionless stretch with nothing happening is trimmed.
- **Variety comes from the plates,** not from a quota: change the size and angle from one shot to the next (R-9), follow
  the journey's screen direction, give the reaction run three different faces.
- **The graphics stay out of the story.** During the setup, the gag and the button the only things the edit adds are the
  captions (and the disclosure at the start). The screen spot (F-B) and the end are where the engine is allowed to show.
- For reference, measured on the three ads (a description, not a target): v03 shots 1.42, 4.13, 1.75, 4.95, 3.65, 6.65,
  7.75 s (median 4.1 s) with ≈ 14 caption swaps in 32 s; v02 six cuts plus ≈ 10 screen swaps in 28 s; v01 two cuts in
  12 s; the first cuts at 1.42 / 2.77 / 2.92 s; the longest uncut action 7.75 s (v03's pull-out under the iris) and 6.16 s
  (v01's walk); v02's reaction close-ups are held poses with one blink (20.0–22.0).

---

## §8 Visual system: B-roll and patterns

### 8.1 The role of graphics
- The plates are the show. The edit's recurring devices are the captions, the closing iris and wordmark card, and the
  disclosure; F-B adds the in-world screen spot (in v02 about 43 % of the runtime).
- **Numbers don't become pictures** in this style: there are no data visuals. A number appears only as a claims-list label
  word.
- The vocabulary below has 35 patterns: 14 cut and footage-treatment patterns that add no graphics, 4 caption patterns, 8
  screen spot patterns, and 9 end, legal and fallback patterns.

### 8.2 Families
| ID | Family | Source | What the brand supplies |
|---|---|---|---|
| **B-1** | Plates (the story) | the brand's own | Every shot (SH-1), native 9:16 (SH-2), with its mix (SH-3) |
| **B-2** | Dialogue captions | engine | The dialogue script (SH-4) |
| **B-3** | In-world screen spot | engine + the brand's own | A locked-off screen plate (SH-8), pack shots (SH-6) |
| **B-4** | Label words | engine | The approved claims list (SH-7) |
| **B-5** | Wordmark and end card | the brand's own (engine fallback FB-5) | The wordmark file (SH-5) |
| **B-6** | Closing transitions (iris, cut to black, static) | engine | — |
| **B-7** | Disclosure, link and stockist lines | engine | The disclosure wording, the link line |
| **B-8** | Third-party moments on screens and lines | the creator's file, else the real one fetched from the web, else a generic stand-in (§12.4) | A clip or logo they hold (optional; the rest is fetched) |

### 8.3 Pattern specs
Frames at 30 fps. "Engine" names the building block.

**Cut and footage-treatment patterns (B-1; no graphics added)**

| ID | Name | Type | What's on screen | Recipe | When | Engine |
|---|---|---|---|---|---|---|
| **P-COLD-ACTION** | Cold action open | cut | A plate already in motion on f0; subject ≥ 20 % of frame height | In point = the first frame of a motion or 2–4 f into it; never a held still | Every f0 | cut list (`stage: L-plate`) |
| **P-MATCH-CUT** | Cut on the action | cut | The same action continued in a new size (wide → CU) | Out on the frame the motion completes or reaches its matched pose; in on the same pose ±2 f | The first cut; any size change inside a beat | cut list |
| **P-ESTABLISH-WIDE** | Establish the place | cut | A wide of the set (street, living room, forest) | 2.4–3.5 s; cut in on a character's movement inside the wide | After the opener (1.2–3.0 s) and at each new location | cut list |
| **P-CHAR-LINE-CU** | Character line close-up | cut | One character's face for its line | The line's length + 8–15 f; cut in ≥ 8 f before the first word | Every F-A line where a CU exists | cut list |
| **P-REACTION-RUN** | Reaction run | cut | 2–3 single close-ups, each a different character | 1.2–2.0 s each (v02: 1.26, 1.27, 1.90 s), the last one longest | After the product turn (F-B) or a punch line | cut list |
| **P-PATIENT-HOLD** | Patient hold | cut | One continuous action (a walk toward camera, a ride, a long look), usually with the plate's own camera move | 4.0–7.8 s, uncut (v01 walk 6.16 s with a 1.45× push; v03 journey 6.65 s); a pleasure because it's rare | Gag/journey beat; F-C middle | cut list |
| **P-OTS-WATCH** | Over-the-shoulder watch | cut | Characters from behind, facing the thing they watch | 2.0–3.0 s, locked off | F-B opener | cut list |
| **P-PRODUCT-IN-HAND** | Product as prop | cut | The product held, sipped, opened, used by a character | Hold ≥ 1.0 s with the product's front visible; never cut while its label is turning | F-C from f0; F-A at the turn | cut list |
| **P-SENSE-FLASH** | Sensory flash | cut | A short imagined or sensory trip (the honey-glow trip, v03 @5.55–7.30) | 1.5–2.0 s (v03 1.75 s); in on T-GLOW-IN, out on T-BLOOM-OUT; a line over it is fine (CS-2 when bright) | The first taste, the moment of delight: the reel's one imagined moment | cut list |
| **P-JOURNEY-STEPS** | Journey steps | cut | 2–4 travel plates, each a new place | 2.5–4.5 s each; screen direction kept (exit right → enter left) | F-A gag beat | cut list |
| **P-REVEAL-WIDE** | The reveal wide | cut | The product's world revealed (the honey waterfall, a factory of clouds) | 2.0–3.0 s, the longest held shot of the second half; a one-word line ("WOAH") is welcome | F-A product turn | cut list |
| **P-BUTTON** | Button | cut | The last character beat: a reaction, a non-sequitur, a satisfied sip, the masked punch line | 2.0–4.0 s (iris included). F-A: the iris may start closing once the button's action peaks, and the last line may play inside the porthole hold; the snap to 0 starts ≥ 6 f after the last word. F-B, F-C: the cut to black comes ≥ 6 f after the last word or action | Every reel, before the logo | cut list |
| **P-WIDE-HOLD-OUT** | Wide hold out | cut | The full cast in the wide, settling | 3.0–4.5 s, locked off | F-B button | cut list |
| **P-FRAME-HOLD** | End-frame hold | footage-treatment | The plate's last frame held | ≤ 12 f, only to land a caption tail or the iris; a rescue, not a device. A held pose already in the plate (v01 @7.50–9.08, 38 f frozen) is the plate's beat, not this pattern: keep it | When a plate runs 2–12 f short | cut list (a hold on the span) |

**Caption patterns (B-2)**

| ID | Name | Type | What's on screen | Recipe | When | Engine |
|---|---|---|---|---|---|---|
| **P-DIALOGUE-SUB** | Dialogue caption | overlay | CS-1: pale yellow 64 px, ≤ 2 lines, block centre y 1420 | §5.3 | Every spoken line | caption engine (CS-1) |
| **P-BRIGHT-SUB** | Bright-plate caption | overlay | CS-2: the same + a 2 px warm stroke | `captions.overrides [{t: [a, b], profile: "CS-2"}]` | Shots logged `bright` | caption engine (CS-2) |
| **P-HIGH-SUB** | High-band caption | overlay | CS-3, block centre y 1180 | an override to `CS-3` on the span | A head low in the frame (in the CS-1 band, clear of the high band, §3.6) | caption engine (CS-3) |
| **P-MASKED-LINE** | Masked punch line | overlay | The button line with its profanity masked ("F**k that's good") | CS-1 + `profanity_mask: inner`; on the button plate or inside the iris | F-A button; always the last line, never in the hook | caption engine |

**Screen spot patterns (B-3, B-4; F-B; one scene clipped to the screen rect, `exception: "E6"`, the rect element marked
`data-slot`, the rect constant within ±4 px for the whole spot: `slot_tolerance_px: 4`)**

E6 is what makes the spot read as television: content changes inside the screen rect are hard cuts, like a channel change
(label → pack → label → lineup → static), while the plate around the screen never cuts. The static comes on and goes off
hard (v02 @5.43, @16.97). E6 never covers an element appearing outside the screen.

| ID | Name | Type | What's on screen | Recipe | When | Engine |
|---|---|---|---|---|---|---|
| **P-SCREEN-ON** | Screen spot | overlay (anchored) | The engine's screen content inside the plate's screen rect: the `accent` sky with 3 soft white clouds (45 % opacity radial blobs, drift −6 px/s), a CRT treatment (2 px scanlines at 6 % black every 4 px, inner vignette 18 %, one diagonal glass highlight 8 % white top-left), corner radius 6 % of the rect height | The rect from the anchor pass (§8.6), constant for the shot; the spot starts and ends hard on the static; clouds drift in 3 f held steps | F-B broadcast beat | bespoke scene z3, `clip-path` to the rect |
| **P-SCREEN-LABEL** | Label word | overlay | 1–2 claims-list words, Barlow Condensed 700 caps, `primary`, centred, centre y = top + 0.21·h, 12 % of h (48–64 px) | Hard on, then blinks 6–7 f on / 6 f off for 1.4–2.0 s while its pack builds (v02 @8.34–14.31); 2 f before its spoken word when the word is spoken | Spot steps 4–6 | inside the screen scene, `text_class: "TC-label"` |
| **P-PACK-IN** | Pack in | overlay | One pack shot, 0.62·h tall, centred (or x 42 % / 58 %), bottom at 0.92·h | Enters in held stop-motion steps, never a smooth slide: either set in from the bottom edge by the brand's hand plate, or (engine) 4–5 held poses of 3 f each, scale 0.55 → 0.8 → 0.95 → 1.0 with ±2° tilt and ±6 px jitter per pose, then holds (v02 @6.81; @8.55–9.00 the pack builds from a clay ring) | Spot steps 2, 4–6 | inside the screen scene (`ctx.asset`; the scene's `step_frames: 3` holds each pose 3 f) |
| **P-LABEL-PLUS-PACK** | Claim + pack | overlay | A label word at the top, its pack building under it | The label on at 0 and blinking; the pack steps in from +6 f; 42–70 f | Spot steps 4–6 | inside the screen scene |
| **P-SCREEN-LINEUP** | Lineup + wordmark arc | overlay | 1–4 packs at 0.5·h spread across 80 % of the width, bottoms at 0.90·h; the wordmark at 85 % width over them, centre 0.45·h | Packs hard; the wordmark grows 0.65 → 1.0 in held 2 f steps over ≈ 18 f, tilt settling −6° → 0°; holds 1.0–1.6 s (the step 2.1 s in all) | Spot step 8 | the wordmark is its own scene over the screen (`step_frames: 2`, `overlaps: [<screen scene>]`); the packs stay in the screen scene |
| **P-SCREEN-STATIC** | Channel static | transition (in-screen) | Seeded grey noise (`static` ±40 luminance, 3 px blocks) with 2 slow horizontal roll bars, inside the rect only | 0.6–1.8 s; the average luminance stays constant, so it reads as a TV between channels, not a strobe | Spot steps 1, 9; any channel change | inside the screen scene (canvas, `ctx.rng`) |
| **P-SCREEN-SHOW** | The show on screen | overlay (anchored) | What the screen plays before and after the spot: the brand's own footage, the creator's clip, the real programme when the script names one (fetched, §12.4), or a **created** generic show (a green pitch with moving dots, a cartoon sky, a weather map with no real brand) | Created shows carry no real names, logos or broadcaster graphics. A named real programme is the real one (§12.4) | F-B opener and after the spot | screen scene; `fx.appUI({kind: "video"})` for a recorded insert |
| **P-SCREEN-PACK3D** (optional) | Pack turntable on the screen | overlay (anchored) | The brand's pack as a lit 3D box turning inside the screen rect: the front face is the brand's front pack shot exactly as delivered, the back face its back shot (or the front again), the sides a flat `primary`; no text drawn by the engine | One `VEOS.fx.three` scene clipped to the screen rect, half a turn (180°) over 1.5–2.0 s on 3 f held steps (`extra: {step_frames: 3}`), then holds front-on; it takes the place of one P-PACK-IN step in a spot. Never outside the screen, never full frame, only when the brand approves a 3D pack | A single-SKU spot that needs one more beat | `fx.three` `custom` (recipe below); one 3D scene at a time (45–150 ms per frame) |

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
| **P-CUT-BLACK** | Cut to black | transition | Black | A hard cut on the frame after the button's out point; black 4 f before the wordmark fades in | F-B, F-C end | stage `L-endcard`, `via: cut` |
| **P-WORDMARK-CARD** | Wordmark card | stage | The brand's wordmark alone, white on black, centre (540, 960), 648 px wide | Fade over 5 f, no scale (F-A: starting with the iris snap, v03 @30.20–30.37); hold 1.8–2.4 s (v03 1.87 s); a hard end (no fade-out) | Every reel | `L-endcard` + scene z5 (`ctx.asset("wordmark")`), `kind: "end-card"` |
| **P-LINK-LINE** | Link line | overlay | The reel's link line, 40 px white at y 1180 | In over 8 f, 0.3 s after the wordmark settles | `link_bio` only | scene z5 on the card |
| **P-STOCKIST-LINE** | Stockist line | overlay | "Now at <retailer>" set in type, 40 px white at y 1180; the retailer's name, not its logo (the wordmark is the card's only mark) | In over 8 f, 0.3 s after the wordmark | When the script names a retailer | scene z5 |
| **P-DISCLOSURE** | Paid partnership | legal | "Paid partnership" 24 px white at x 64, y 150 | In over 6 f at 0.0 s, hold ≥ 2.0 s (2.5 s by default), out over 6 f | Paid posts | scene z6, set as legal small print (the legal text class) |
| **P-BAND-PLATE** | 16:9 band | stage | The 16:9 plate in a 608 px band, black above and below | `L-plate-band`; captions at y 1290 | FB-2 (16:9 plates) | stage layout |
| **P-BLUR-PLATE** | 4:5 band | stage | The 4:5 plate band over its own blurred copy | `L-plate-blur`; blur 48 px, luma −0.35 | FB-2 (4:5, 1:1 plates) | stage layout |
| **P-CROP-WINDOW** | Static crop window | footage-treatment | A fixed 9:16 window cut from a wider plate | Only when the action stays inside the window for the whole shot; ≤ 1.35× on 1080p, ≤ 2.0× on 2160p; never animated | FB-2 alternative to a band | cut list crop |

### 8.4 Line → pattern lookup
Vocabulary, not a decision table: it tells you what this style reaches for. Ask what the moment needs, then use it.

| Line / plate type | Primary | Alternates |
|---|---|---|
| Opening action (any character doing something) | P-COLD-ACTION | P-OTS-WATCH (watching a screen), P-PRODUCT-IN-HAND |
| A character speaks | P-CHAR-LINE-CU + P-DIALOGUE-SUB | two-shot hold + P-DIALOGUE-SUB |
| A line over a bright plate | P-BRIGHT-SUB | — |
| A character's head sits low in the frame | P-HIGH-SUB | move the line to the next shot |
| The invitation, the offer ("you've got to try this") | P-MATCH-CUT into a two-shot | P-CHAR-LINE-CU |
| First taste, delight ("Oh… WOW") | P-SENSE-FLASH | P-CHAR-LINE-CU |
| Travel, "follow me" | P-JOURNEY-STEPS | P-PATIENT-HOLD |
| Where the product comes from | P-REVEAL-WIDE | P-SCREEN-ON (a documentary on the TV) |
| The product's benefit as a claim | P-SCREEN-LABEL (F-B) | the character's own line (F-A) |
| Showing the range, the flavours | P-SCREEN-LINEUP | P-PACK-IN ×2 |
| A claim word ("it's cold-brewed / organic / low sugar") | P-SCREEN-LABEL (claims list) | a character line saying it |
| Pouring, steeping, opening the product | P-PRODUCT-IN-HAND | P-REVEAL-WIDE |
| An app's feature ("it tracks every rupee") | P-SCREEN-ON on the phone prop + P-SCREEN-LABEL (claims list) | a character line |
| A notification, a reminder | P-SCREEN-ON (the phone lights; a label word only if the claims list has it) | P-CHAR-LINE-CU reacting |
| Splitting, sending, saving (an app) | P-SCREEN-LABEL + P-PACK-IN (an app-icon tile the brand supplies, as the "pack") | P-SCREEN-LINEUP of 3 feature tiles |
| Reaction to the product | P-REACTION-RUN | P-WIDE-HOLD-OUT |
| The last laugh | P-BUTTON (+ P-MASKED-LINE) | P-WIDE-HOLD-OUT |
| A real retailer, show or sports league is named | P-STOCKIST-LINE / P-SCREEN-SHOW (the real show: the creator's file, else fetched) | a generic created show when nothing usable turns up |
| The end | P-IRIS-OUT (F-A) / P-CUT-BLACK → P-WORDMARK-CARD | + P-LINK-LINE |

### 8.5 Product truth
- No figures: no charts, counters or hero numbers.
- Every label word, number and product name on screen comes from the claims list (SH-7) or the script, character for
  character.
- Pack shots are the brand's files, never redrawn, recoloured or relabelled; when the claims list ties claims to SKUs, a
  label word only appears next to its own SKU.
- A created screen show is generic and carries no real names; a named real programme is the real one, fetched (§12.4).
- Character dialogue is fiction; it is never presented as a customer testimonial.

### 8.6 Anchors: the screen rect, the iris centre, the head band
The plates are locked off where it matters, so every anchor is a static rect or point written in the anchor pass from
sampled frames (the first, middle and last frame of the plate at full resolution); `anchors.mode: static`, fallback
`static_near_target`, `face_clear_px: 40`.

| Target | Used by | How it's written | Rule |
|---|---|---|---|
| `screen:<plate id>` | P-SCREEN-ON and everything inside it (F-B) | The screen face's inner rect `{x, y, w, h}` in output px (the glass, inside the bezel), plus `radius` = 6 % of h | The plate must be locked off: the rect measured on the first and last frame differs by ≤ 4 px, else that take can't host the spot (pick another take, or FB-8). The rect must be ≥ 600 px wide; label size = 12 % of h, clamped to 48–64 px |
| `faces:<plate id>` | P-IRIS-OUT centre (every format with an iris) | The midpoint of the visible characters' eyes on the iris hold frame | The porthole (r 510) contains every character's head |
| `headband:<plate id>` | the CS-3 switch (§3.6) | The y range covered by any character's head region (face, hair or fur, ears, the room above the head) across the shot, sampled every 0.5 s | Clear of y 1300–1540 → CS-1; else clear of y 1060–1300 → CS-3; else move the line (§3.6) |

**When a plate moves.** A screen plate with a camera move (a push-in on the TV), or a label that must stay on a product
prop moving inside a plate (a pack carried across the counter, F-A / F-C), uses a track instead of a static anchor, only
for that shot's span (`veos track`, SCENES-API §13). The screen scene gets
`anchor: {track: "screen", scale_with: true, lost: "hold"}` with its `box` = the rect at `t_in`; a product label gets
`anchor: {track: "pack", point: "top", offset: [0, -60], lost: "fade"}`, claims-list words only. If more than 20 % of the
span is lost, or the screen can't be read as one rect, that take can't host the spot: pick a locked-off take or FB-8. A
product label without a usable track is dropped (the product stays a prop; the caption carries the word).

### 8.7 Comedy layer (light)
Comedy is the characters' acting and the edit's timing. The engine adds **no comedy graphics** (no stickers, stamps,
marker notes, freeze-frame roasts) and **no meme sounds**. Its tools are timing only:
- **The beat before the button:** hold the shot 8–15 f after a reaction before cutting to the button.
- **The cut-away laugh:** P-BUTTON as a non-sequitur (v01's cat in the bushes after the walk).
- **The masked line:** the button's profanity masked inner-style ("F**k that's good"), always the last line, never in the
  hook. It's the sketch's one cheeky moment; a second one cancels it.
- **The reaction run:** three faces, the last one held longest (1.9 s). It lands because the sketch has earned it.

### 8.8 Assets
- Plates, wordmark and pack shots are the brand's own files, used as delivered (cropped only under FB-2).
- Created screen content is generic and unbranded (no real channels, leagues, apps or logos).
- No stock footage, no AI-generated characters, no clip art.
- Third-party moments: fetch the real thing, source noted (§12.4).

---

## §9 Transition system

### 9.1 Library
| ID | Transition | Frames | Recipe | Sound |
|---|---|---|---|---|
| **T-CUT** | Hard cut on action | 0 | Out on a completed or matched motion ±2 f; in on the continuing pose | none (the plate mix carries it) |
| **T-SCREEN-SWAP** | In-screen hard swap | 0 | Content changes inside the fixed screen rect (E6); the plate around it never cuts | none |
| **T-STATIC** | Channel static | 18–54 | P-SCREEN-STATIC inside the screen rect, 0.6–1.8 s | `transitions`: one soft static/noise cue at its start, peak ≤ −24 dB |
| **T-IRIS** | Iris out | 42 + 18–24 + 6 (no black gap) | P-IRIS-OUT | none by default; the plate mix plays through |
| **T-CUT-BLACK** | Cut to black | 0 (+ 4 black) | P-CUT-BLACK | none |
| **T-GLOW-IN** | Glow into the sensory trip | 3 + 12 | A hard cut on a 3 f luminance swell (+80 %, warm) with a 6 f radial zoom-blur, then a decay over 12 f (v03 @5.55–5.67). Built in: the swell is a warm `flash` on the cut `{"t": <cut>, "type": "flash", "colour": "#FFE2A8", "peak": 0.45, "pre": 3, "frames": 15}`; the zoom blur is a footage blur envelope `timeline.blur: [{"t": <cut>, "kind": "radial", "amount": 0.12, "at": "centre", "frames": 6, "shape": "decay"}]` (two built-in transitions may not overlap; a blur envelope may) | none |
| **T-BLOOM-OUT** | Bloom out of the trip | 5 + 6 | The trip blooms toward white over 5 f, then the trip image shrinks into a soft circle over 6 f, revealing the next plate (v03 @7.08–7.40). Built in: a `flash` ending on the cut `{"t": <cut>, "type": "flash", "colour": "#FFF6E0", "peak": 0.9, "pre": 5, "frames": 5}` (peak 0.9: the measured near-white orb, luma ≈ 228), then the orb collapse `{"t": <cut>, "type": "iris", "reveal": "next", "frames": 6, "feather": 40, "at": [<trip centre x>, <y>]}` (the old shot shrinks in a soft circle over the next plate) | none |
| **T-CARD-IN** | Wordmark in | 5 | A fade, no scale; in F-A it starts on the first frame of the iris snap | `cta`: one soft chime or shine on the settle frame, peak ≤ −24 dB |

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
| Into / out of the sensory trip | T-GLOW-IN / T-BLOOM-OUT | A plain hard cut (the trip must read as imagined) |
| Button → logo (F-A) | T-IRIS | A cut straight to the wordmark mid-line |
| Button → logo (F-B, F-C) | T-CUT-BLACK | A fade-out of the plate |
| Last frame | The wordmark hold, a hard end | A black tail over 0.2 s |

### 9.3 Shot grammar
| ID | Rule |
|---|---|
| **R-1** | **Cut on action:** every cut lands on a completed motion (a cup lowered, a landing, a turn) or a matched motion ±2 f |
| **R-2** | **Size change early:** the opener runs 1.2–3.0 s, then the size changes (CU ↔ wide) |
| **R-3** | **The speaker is seen:** a character's line plays on its own CU or on a shot where its face is visible; cut on the reply's first word −2…+3 f only when the replier has a CU |
| **R-4** | **Reaction run:** 2–3 CUs, 1.2–2.0 s each, each a different character, the last one longest |
| **R-5** | **Long shots travel:** a shot of 4.0–7.8 s earns its length only when the camera moves or a character travels inside it (v03 4.95 s arc, 6.65 s journey, 7.75 s pull-out) |
| **R-6** | **No cut inside a line**, except a match cut that keeps the same speaker on screen (v03 @1.42) |
| **R-7** | **The turn is held:** the product turn gets the longest shot of the second half (2.0–3.0 s) |
| **R-8** | **The button follows the turn** with at most one shot between them |
| **R-9** | **No jump cuts:** two consecutive shots never share the same size and angle |
| **R-10** | **Continuity wins:** keep the brand's animatic order when one is supplied; reorder plates only when the sketch beats (§7.1) demand it and props and positions still match |
| **R-11** | **Screen direction:** a travelling character exits one side and enters the next shot from the opposite side |
| **R-12** | **Handles:** never use the first or last 3 frames of a plate (the animators' settle frames) unless it's the end-frame hold |

### 9.4 How the moves breathe
The hard cut on action is the whole language: dozens of them in a row and the viewer never notices one, because each lands
on a movement that's already finishing. That's what makes the four designed moves special. The static is the TV changing
channel, and it belongs only to the screen. The glow into the sensory trip says "this is imagined", so it belongs to the
first taste, the moment of delight, and nowhere else. The iris is the storybook ending and the cut to black is the
broadcast one: each reel gets the one its format calls for, and the wordmark's soft fade is the last breath. Any designed
move repeated back to back stops being a moment and becomes a gimmick.

---

## §10 Motion tokens, camera and zoom, layers, finishing

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Beat lead | 2 f before the onset (captions, spoken label words) |
| Caption swap | hard in, hard out (0 f) |
| Label word swap | hard (E6), inside the screen only |
| Pack in | 4–5 held poses × 3 f (≈ 15 f), scale 0.55 → 1.0, ±2° / ±6 px jitter per pose (stepped, no easing) |
| Screen on/off | hard (the static cuts on and off; v02 @5.43, @16.97) |
| Static | 0.6–1.8 s (1.1 s by default); noise refreshed every frame from `ctx.rng(n)`; 2 roll bars moving 3 px/f |
| Screen wordmark arc | ≈ 18 f in 2 f held steps, scale 0.65 → 1.0, rotate −6° → 0° |
| Label blink | 6–7 f on / 6 f off, 1.4–2.0 s per word |
| Cloud drift (screen sky) | −6 px/s, seeded positions |
| Iris | close r 1110 → 510 over 42 f ease-in-out; hold 18–24 f; snap 510 → 0 over 6 f ease-in; feather 24 px |
| Black before the card | F-A 0 f (the wordmark fades in under the iris snap); F-B, F-C 4 f after the cut |
| Wordmark in | 5 f fade, no scale; no exit (a hard end) |
| Link line in | 8 f fade + rise 12 px, 0.3 s after the wordmark settles |
| Disclosure | in 6 f at 0.0 s, out 6 f |
| Sensory trip | 1.5–2.0 s; glow-in 3 f, bloom-out 5 f, orb collapse 6 f |
| End-frame hold | ≤ 12 f |
| Holds | text ≥ 0.3 s per word; label words 1.4–2.0 s in blinks |
| In-world step | every scene the engine animates inside the world steps on held poses with the scene field `step_frames`: `step_frames: 2` (the screen wordmark), `step_frames: 3` (pack builds, clouds, the 3D pack); the label blink is 6–7 f on / 6 f off (drawn from `lt`, not stepped). Captions, the iris and the end card have no `step_frames` |

### 10.2 The plate cadence (measured frame by frame; keep it, copy it)
| Source | Characters / objects | Camera | Evidence |
|---|---|---|---|
| v01 clay (24 fps) | pose-to-pose bursts **on ones** (an 8 f move), then the key pose held 12–14 f; the bird/cat shot on twos; the walk ends on a pose frozen 38 f | one linear push 1.00 → 1.45× over 3.2 s (≈ +12 %/s) on ones, locked off elsewhere | @0.04–0.33 move, @0.38–0.96 hold; @4.30–7.50 push; @7.50–9.08 frozen; @9.1–10.5 twos |
| v02 clay (29.97 fps) | mostly **held poses**: the reaction close-ups are stills with one blink or pose pop; screen objects on 2–3 f steps; the TV football is live footage | locked off in every shot (scale 1.000) | @20.0–22.0, @23.2 pop; @8.55–9.00 pack build |
| v03 felt (24 fps) | characters **on twos** (12 images/s) | smooth moves **on ones**: a push +6 % over 3.9 s, an arc with 4.9° roll + 3 % over 4 s, a pull-out −8.5 % over 4.3 s under the iris | @1.45–5.3, @8.3–12.25, @26–30.3 |

The engine never interpolates, blends, retimes or smooths a plate; 24 → 30 fps by frame duplication only (§12.5). Engine
motion that lives **inside the world** (P-PACK-IN, the screen wordmark, the cloud drift, the optional 3D pack) steps on
held poses of 2–3 f with `step_frames` (the label blink is already a 6 f on / off). Engine motion **outside** the world
(captions, the iris, the card fade) is not stepped. That's the rule that keeps the spot looking animated by the same hands
as the plates.

### 10.3 Footage camera (`zoom_policy: source_only`)
Every camera move is physical, inside the plates (the dolly pushes, rack focus and pans the animators shot). The engine has
**no zoom presets** in this style: no punch-in, crash zoom, push-drift, shake or rotation. The only geometric change allowed
is FB-2's static crop window (P-CROP-WINDOW), set once per shot and never animated. There is no canvas camera either: the
camera is physical and lives inside the plates.

### 10.4 Layer order (back to front)
1. W-plate (the plate) or W-black
2. The screen spot scene (z3, clipped to the screen rect inside the plate); the 3D pack (z4) and the screen wordmark over it
3. The wordmark card scene (z5, on L-endcard) and the link or stockist line (z5)
4. The disclosure line (z6)
5. Captions (z7, auto)
6. The iris mask (z11, momentary)

### 10.5 Finishing
None added. No grain, vignette, bloom, glow, LUT or sharpening on plates. Inside the screen spot only: the CRT treatment of
P-SCREEN-ON (scanlines, inner vignette, glass highlight), so the engine's screen content sits in the plate's light. Export
1080 × 1920, 30 fps CFR, BT.709.

---

## §11 Sound

The plates arrive mixed; the brand's mix is the soundtrack. The bundled SFX pack adds a few soft touches with its global
rules, and nothing else.

| Line | Decision |
|---|---|
| **Cue moments** | `reveals` (a pack landing in the screen spot, the screen wordmark arc), `transitions` (the in-screen static), `cta` (the wordmark settle). The hook, the story beats, the lines and the button carry **no** pack cue: the plate mix carries them |
| **Meme cues** | off (the comedy is light and lives in the acting) |
| **Music bed** | off by default. **On only for silent plates (FB-3):** a calm bed from the pack from f0, at −22 dB under any foley, fading out over the last 10 f of the button so the wordmark sits in near-silence or with its cue |
| **Ducking** | the plate mix stays as delivered; a pack bed (FB-3 only) sits ≥ 18 dB under any character voice |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; the last sound ends ≤ 6 f after the wordmark hold ends |

Each soft cue is a different file (in the F-B example: two static cues, three pack pops, one shine). Sparse: the plate is
the drama; a pack cue only marks a landing. If in doubt, leave it out.

---

## §12 Footage handling

### 12.1 Plates
| Setup | Spec |
|---|---|
| **A: finished plates** | The brand's stop-motion, claymation, felt, puppet, paper-cut or 3D-animated shots; 9:16; 1080 × 1920 or larger (2160 × 3840 ideal); 24, 25 or 30 fps (12 fps "on twos" inside 24 is fine); the final grade baked in; one mixed audio track per plate (voices, foley, music) or a picture-locked animatic with its mix |
| Framing | The characters' eyes between y 480 and 1300; nothing that matters below y 1500 (the caption band and Instagram's UI); the right 110 px between y 900 and 1540 free of key action |
| Handles | 12–24 frames before and after each action |
| Look | Whatever the brand's world is; the source look is a warm tungsten key, cool fills, macro shallow depth of field |

### 12.2 Shots and fallbacks
| ID | Shot / asset | Spec | Must / optional | Formats |
|---|---|---|---|---|
| **SH-1** | The plates | Every shot of the sketch (usually 4–14), each with 12–24 f handles | must | all |
| **SH-2** | Native 9:16 framing | As §12.1 framing | must | all |
| **SH-3** | Plate audio | Mixed voices, foley, music per plate | optional | all |
| **SH-4** | Dialogue script | Every line with its exact casing and spelling, the speaking character named | optional (strongly recommended for F-A) | F-A |
| **SH-5** | Wordmark | Transparent PNG or SVG, one colour (white), ≥ 1200 px wide | must | all |
| **SH-6** | Pack shots | Transparent PNG cut-outs, front-on, ≥ 900 px tall, 1–4 products (an app: icon tiles or phone-screen PNGs) | must | F-B |
| **SH-7** | Approved claims list | The exact 1–2 word label words legal has cleared, per SKU when they differ | optional | F-B (and any label) |
| **SH-8** | Screen plate | A locked-off plate of an in-world screen (TV, phone, billboard, window) with a flat blank face ≥ 600 px wide in frame, ≥ 6 s, plus the same set wide | must | F-B |
| **SH-9** | Button plate | A last 2–4 s character beat (a reaction, a non-sequitur, a satisfied sip) | must | F-A, F-C |

| ID | For | What the engine does | What it costs | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | Nothing: the engine can't make stop-motion; without plates there is no reel | the style can't run | `no_fallback` |
| **FB-2** | SH-2 | 16:9 plates → L-plate-band (band y 556–1164, captions y 1290); 4:5 or 1:1 → L-plate-blur; a static 9:16 crop instead when the action fits (≤ 1.35× on 1080p, ≤ 2.0× on 2160p) | the miniature no longer fills the phone; it reads as a TV spot repost | `degraded` |
| **FB-3** | SH-3 | Silent plates: the calm pack bed from f0; no captions (no speech); F-A runs as pantomime | no voices | `holds` |
| **FB-4** | SH-4 | Transcribe the plate audio; captions verbatim, sentence case | the script's emphasis caps ("you've GOT to") and invented spellings are lost | `holds` |
| **FB-5** | SH-5 | The real wordmark fetched from the brand's own site (source noted); only when none is usable, the type-set wordmark from the brand name in the wordmark slot (48° arc, white, 600–700 px) | type-set, not the brand's real mark | `degraded` |
| **FB-6** | SH-6 | The brand's own product images fetched from its site; else the screen spot runs label words and the wordmark only | no product on screen; a weaker turn | `degraded` |
| **FB-7** | SH-7 | No label words; packs and the wordmark carry the spot | no claims on screen | `holds` |
| **FB-8** | SH-8 | F-B unavailable; use F-A or F-C with the brand's product-in-world plate | no broadcast ritual | `no_fallback` (for F-B) |
| **FB-9** | SH-9 | Hold the last plate's final frame up to 12 f and run the end on it | no button laugh; the ending lands softer | `degraded` |

### 12.3 Props, the reaction bank, resolution
- **Props:** nothing beyond what's in the plates. The product itself should appear as a prop in at least one plate (F-A,
  F-C).
- **Reaction bank:** 2–3 character reaction close-ups of 1.2–2.0 s each (they feed P-REACTION-RUN and the button).
- **Cut-out:** none. The engine never draws behind a puppet.
- **Minimum source resolution:** 1080 × 1920 for full-frame plates; a static crop window needs ≥ 1.35× the crop (≥ 1458 px
  wide for a 1080 output) and is capped at 2.0× on 2160p sources. 720 × 1280 plates (like the source ads) upscale 1.5×,
  and the plan says so.

### 12.4 Third-party inserts: fetch the real thing
In this style, third-party moments are rare and live on **in-world screens, signs and the end line**. When the script
names a real one, the viewer should see the real one.
1. **Find them** in the script, the plate log and the brief: a named TV show, sports league or match on the screen; another
   company's logo or product; a retailer ("now at …"); a celebrity's face on a poster; a song.
2. **The creator's own files** in their folder come first.
3. **Otherwise search the web and fetch it:** the real logo, the real programme still or clip, the real poster image.
   Note where it came from.
4. **Use it as it is,** inside the screen rect or on the set's poster, never altered to say something it doesn't.
5. **Nothing usable to be found: a generic stand-in,** with no label and no credit line:
   - a named programme or match on a screen → `recreated_ui` (a generic show: a green pitch with moving dots, no league
     marks);
   - a person's photo on a poster in the set → `silhouette`;
   - a song → not fetched or created; music only from the bundled pack or the brand's own mix.
   A retailer is always P-STOCKIST-LINE, the name set in type: the end card carries only the brand's mark.

Generic set dressing that stands in for no real thing (an unbranded cartoon on the TV, a made-up shop sign the animators
drew) is not an insert.

### 12.5 Frame rate and audio
- Output 30 fps CFR by frame duplication (`fps=30`, which repeats frames: a 24 fps plate gets a 2-2-2-3 cadence, and a
  12 fps "on twos" plate keeps its stutter), never optical flow or frame blending: the stop-motion stutter is the look.
- Audio: the plate mix as delivered, joined at cuts with 2 f audio crossfades only where a click would occur (the picture
  cuts stay hard); −14 LUFS integrated.

---

## §13 What your plan should settle

Your `ideas.md` is a page or two, for you. In this style it has decided, before any code:
1. **The format and why** (§3.1).
2. **The hook:** the opener plate, its in frame and the first cut; the post title (8–10 candidates, the pick, two
   alternates); the stopper test.
3. **The plate log and the cut list:** every plate's in and out frame and each cut's reason (`action_end`, `match`,
   `line_end`, `reaction`).
4. **The sketch:** every beat's section, tone and timing against §7.1.
5. **The captions:** which spans use CS-2 or CS-3 and why (the head band, the luminance).
6. **F-B:** the screen rect from the anchor pass, the spot ritual step by step, the exact label words and their claims-list
   source.
7. **The end:** T-IRIS (centre, close, hold, snap frames) or T-CUT-BLACK, the card, the link or stockist line, the
   disclosure when paid.
8. **The sound and the transition map:** the allowed cue moments only.
9. **The inserts and the fallbacks:** the creator's, fetched (with the source) or created; every fallback used and its
   cost; words the claims pass dropped.
10. **The moments you'll look at hardest on the storyboard:** f0, the first cut, one line with its caption (heads clear
    of it), a bright plate with CS-2, the product turn, one screen-spot step (F-B), the iris hold (F-A, the button line
    under the porthole), the wordmark card.

A beat, for the shape (`section`: setup | gag | product | button | logo; `tone`: setup | gag | awe | button | cta). Beats
also carry, where they apply: `anchor {target: "screen:PL-03" | "faces:PL-12" | "headband:PL-05", rect {x,y,w,h} | point
{x,y}, follow: none}` (F-B screen beats, the iris beat), `sponsor {disclosure: "Paid partnership"}` on beat 1 when paid,
`end_card {wordmark: "wordmark", link_line?}` on the logo beat, `exception: E6` on
the screen-spot beat and its scene, and `fallback_used` (FB-2 on band and blur shots, FB-5 on a type-set wordmark…).
```yaml
- id: 4
  section: gag
  t0: 7.40
  t1: 10.95
  spoken: "Follow me!"
  trigger: {word: "Follow", at: 9.62}     # or {action: "bee exits right", at: 10.90}
  tone: gag
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

The reel header:
```yaml
format: F-A                # F-A | F-B | F-C
hook_archetype: HA-16
structure: sketch
cta: end_card              # end_card | link_bio | post_only | none
paid: false                # true -> P-DISCLOSURE
plates: 11                 # SH-1 count
claims: []                 # SH-7 words used on screen
fallbacks: []              # FB ids used
```

A hook proposal, for the shape:
```yaml
- name: "Bee flies in with the offer"
  archetype: HA-16
  opener: {plate: PL-01, in_f: 4, action: "bee enters frame right, crosses to the frog"}
  first_cut: {at: 1.42, to: PL-02, reason: match}
  hook_pair: {subject: "frog on a mushroom with a snack", reveal_by_5s: "the bee offers something it's GOT to try"}
  post_title: "frog finds out where honey comes from"
  alternates: ["the bee who wouldn't stop talking about honey", "pov: you've never had honey like this"]
  captions: {profile: CS-1, first_line: "Dude, you've GOT / to try this", at: 1.17}
  storyboard: "f0 wide frog + bee entering | 1.17 caption cuts on | 1.42 match cut to MCU | 3.9 'Oh… WOW' | 5.0 want established"
  sound: "plate mix only"
  stopper: {thumbnail: pass, motion_f0: pass, payoff_by_s: 3.9}
```

---

## §14 Worked examples

Times are planning estimates: take the real ones from the plates' action frames and the word onsets. They show the
standard; match it, then beat it.

### 14.1 F-A Dialogue sketch: an herbal sleep-tea brand (27.5 s)
**Plates:** 11 felt stop-motion shots (an owl who can't sleep, a moon character, a forest at night, a tea "spring"), mixed
with voices. **Script excerpt:** OWL "It's NOON and I'm still up." MOON "You need to try this." OWL "Where are we going?"
MOON "Just follow the steam." OWL "Is that… a river of tea?" OWL (button) "Okay. Night night." **Claims list:** not needed
(no labels in F-A).

**Hook (HA-16):**
| t (s) | Plate / visual | Caption | Cut |
|---|---|---|---|
| f0 | PL-01 wide: the owl on a branch in daylight, mid-yawn (motion from f0) | — | — |
| 0.9 | Same | CS-1 "It's NOON and / I'm still up." (lead 2 f) | — |
| 2.3 | PL-02 MCU: the moon character drifts in from the top, holding a steaming cup | — | match cut on the owl turning its head |
| 3.1 | Same | CS-1 "You need to try this." | — |
| ≤ 5.0 | Subject and want established | | |

**Pattern plan:**
| Section | t (s) | Plates / patterns | Captions | End |
|---|---|---|---|---|
| setup | 0–5.0 | P-COLD-ACTION → P-MATCH-CUT → P-CHAR-LINE-CU | CS-1 ×2 | — |
| gag (journey) | 5.0–16.5 | P-JOURNEY-STEPS ×3 (a steam trail through roots 3.6 s; mossy stones 3.4 s; a hollow log 4.3 s, the patient hold) | "Where are we going?" · "Just follow the steam." | — |
| product turn | 16.5–21.0 | P-REVEAL-WIDE: the tea spring glowing amber (2.8 s, CS-2 because bright) → P-PRODUCT-IN-HAND: the owl holds the cup, the pack on a stump beside it (1.7 s) | "Is that… / a river of tea?" (CS-2) | — |
| button | 21.0–25.4 | P-BUTTON: the owl drinks, its eyes droop, it tips over onto a moss pillow (21.0–23.6); P-IRIS-OUT closes on it 23.6–24.7 (r 1110 → 510, centre 540, 1010), holds 24.7–25.2 while the last line finishes inside the porthole, snaps to 0 over 25.2–25.4 | "Okay. Night night." (24.2–25.0, CS-1, under the porthole and clear of the owl's head) | the snap starts 6 f after the last word |
| logo | 25.2–27.5 | P-WORDMARK-CARD fades in over 5 f under the snap, holds 2.0 s | hidden on the card | a hard end at 27.5 |

Runtime 27.5 s (target 20–30). CTA: `end_card`. Sound: one soft shine on the wordmark settle (`cta`). Inserts: none.
Fallbacks: none. Disclosure: the brand posts on its own account → none.

### 14.2 F-B Product broadcast: a budgeting app (24.3 s)
**Plates:** 7 claymation shots of a hamster family in a living room; a locked-off shot of a retro TV with a blank green face
(8 s); the couch wide; three character close-ups; silent plates (FB-3: the calm bed from f0). **Pack shots:** three
phone-screen PNGs from the brand (spending ring, savings goal, bill reminder). **Claims list:** "TRACKS EVERYTHING", "ZERO
FEES", "AUTO-SAVE". Posted by an agency → the disclosure is on.

**Hook (HA-16):**
| t (s) | Plate / visual | Caption | Cut |
|---|---|---|---|
| f0 | PL-01 P-OTS-WATCH: the hamster kid from behind, watching the TV, which already plays a created generic show (a cartoon cheese-rolling race, no real names); "Paid partnership" at x 64, y 150 from 0.0 s | — | — |
| 2.5–2.7 | The disclosure fades out over 6 f (held 2.5 s) | — | — |
| 2.6 | PL-02 P-ESTABLISH-WIDE: mum and dad hamster on the couch counting coins into a jar | — | a hard cut on dad dropping a coin |
| 5.0 | Watchers, place and want (the coin jar) established | | |

**Pattern plan:**
| Section | t (s) | Patterns | Screen content (E6 swaps) |
|---|---|---|---|
| setup | 0–5.0 | P-OTS-WATCH (P-SCREEN-SHOW, created) → P-ESTABLISH-WIDE | the generic race show |
| broadcast | 5.0–15.4 | Cut to PL-03, the locked-off TV (the rect from the anchor pass: x 190, y 700, w 680, h 440). P-SCREEN-ON with the §7.3 ritual | static 1.2 s → "TRACKS EVERYTHING" 1.0 s (Barlow Condensed 700 caps 53 px = 0.12 × 440, red on the sky; 2 words, 17 characters) → phone PNG 1 steps in 1.0 s (4 held poses of 3 f) → "ZERO FEES" 1.0 s → phone PNG 2 1.0 s → "AUTO-SAVE" + PNG 3 1.5 s → clear sky 0.4 s → three phones + the wordmark arc 2.0 s → static 1.0 s |
| reactions | 15.4–19.4 | P-REACTION-RUN: kid CU 1.3 s → mum CU 1.3 s → dad CU 1.4 s (dad drops the coin jar into a drawer) | — |
| button | 19.4–22.0 | P-WIDE-HOLD-OUT: the family settles back, the TV returns to the race (2.6 s) | the generic race show again |
| logo | 22.0–24.3 | P-CUT-BLACK (black 4 f) → P-WORDMARK-CARD (in over 5 f, hold 1.9 s) + P-LINK-LINE "Download free · link in bio" (`link_bio`) | — |

The screen spot runs 10.4 s of 24.3 s (about 43 %, like v02). Inserts: the race show is generic set dressing (not an
insert). Sound: two static cues (two different files), a soft pop on each phone landing (`reveals`, three different
files), a shine on the wordmark settle. Fallbacks: FB-3 (the bed on).

### 14.3 F-C Vignette: a snack brand's new flavour (14.3 s)
**Plates:** 4 claymation shots: a clay skateboarder eating from the bag, a boardwalk wide, a seagull eyeing the bag, the
gull stealing a chip. No dialogue (the plate mix: foley + music).

| Section | t (s) | Plates / patterns | Text | Cut reason |
|---|---|---|---|---|
| setup (hook) | 0–2.8 | P-COLD-ACTION + P-PRODUCT-IN-HAND: MCU of the skater crunching a chip, bag in hand, the front of the bag to camera | none | — |
| wide | 2.8–8.6 | P-PATIENT-HOLD: the skater rolls toward camera down the boardwalk (5.8 s) | none | a cut on the bag lifting to the mouth (match) |
| button | 8.6–12.2 | P-BUTTON: a seagull on the railings tilts its head, then snatches a chip (3.6 s); hold 10 f after the snatch | none | a cut as the skater passes frame left |
| logo | 12.2–14.3 | P-CUT-BLACK (black 4 f) → P-WORDMARK-CARD (in over 5 f, hold 1.7 s) | none | — |

CTA: `end_card`. Captions: none (no speech). Disclosure: the brand posts on its own account → none. Sound: one shine on the
wordmark settle. Fallbacks: none.

---

## §15 Your look at the storyboard: the checklist

Watch it once as a stranger with a thumb over the next reel, then once as the editor whose name is on it. Fix what
bothers you, in one pass.

**The style (does it feel like §The feel?)**
- Frame 0 is a plate in motion with nothing written on it; the thumbnail reads as a character in a miniature world.
- The first cut lands on an action and you don't feel it; the subject and the want are clear within five seconds.
- The plates are untouched: no zoom, speed change, blend, regrade or stabilisation; the puppets keep their stutter.
- Everything the edit animates inside the world (packs, the screen wordmark, the clouds, the label blink) steps on held
  frames like the plates; nothing glides.
- The cuts follow the action: patient shots, long ones only when something travels, the size changing from shot to shot,
  the journey's screen direction kept.
- The product arrives inside the world, and the turn is the longest-held shot of the second half; the button follows it
  and earns a laugh.
- The comedy is acting and timing: no stickers, no meme sounds, the masked line only at the end.
- The end: the iris (F-A) or the cut to black, then the wordmark alone on black, centred at y 960, 600–700 px wide, in
  over 5 f, held 1.8–2.4 s, a hard end; only a link or stockist line beside it.
- Start to end: it feels like a handmade short film that happens to be signed by a brand.

**Craft (by eye, in context; the facts are in §2)**
- The characters' faces read: captions, labels, lines and the disclosure sit off the heads, CS-3 or a moved line wherever
  a head reaches the CS-1 band (§3.6); the iris porthole holds every head; nothing buries a face by accident.
- One caption at a time; label words only inside the screen rect, the rect steady through the spot; captions hidden on
  the card.
- Captions on with the first word and off after the last, hard on and off, long enough to read; spoken label words on
  their word; cuts on action; no cut inside a line.
- Words exact: captions verbatim with the script's casing and the `inner` mask; label words and claims from the claims
  list; pack shots and wordmark unaltered; fetched screen content shown as it is; names spelt right.
- CS-1 as specified (Plus Jakarta Sans 500, 64 px, `#F6FA8C`, line height 1.25, y 1420, ≤ 2 lines of ≤ 24 characters);
  CS-2 on every bright span; every caption readable on its plate; label words 48–64 px.
- Paid post: the disclosure from 0.0 s for ≥ 2.0 s. Personal data blurred.
- The file itself (1080 × 1920, 30 fps CFR by frame duplication, −14 LUFS, the last sound ≤ 6 f after the wordmark hold,
  no black tail) is the render's job; it checks it.

---

## §16 Build notes
- **Fonts:** Plus Jakarta Sans (500, 600), Barlow Condensed 700, Fraunces Soft 800, Noto Sans Devanagari 500, all bundled.
- **Determinism:** the static noise, the cloud drift and every animated element are functions of the frame index (seeded
  through `ctx.rng`); no CSS animation in scenes.
- **Stepped motion is built in:** set `step_frames` on the scene (2 for the screen wordmark, 3 for packs, clouds and the 3D
  pack) instead of quantising time by hand.
- **The end iris is a scene:** P-IRIS-OUT stays a z11 radial-gradient mask scene, because the built-in `iris` transition
  has no partial close and hold. The orb collapse out of the sensory trip *is* the built-in `iris` (`reveal: "next"`).
- **The clay pack "build"** (a ring that morphs into the pack, v02 @8.55–9.00) is object animation: best as the brand's own
  plate; the engine fallback is P-PACK-IN's stepped poses.
- **One 3D scene at a time:** P-SCREEN-PACK3D costs 45–150 ms a frame.
- **Built in, no scene:** the warm glow and radial blur of T-GLOW-IN, the bloom and orb collapse of T-BLOOM-OUT (§9.1).

---

## Appendix A. Evidence map
The full map (every element → `vNN @ m:ss`, the inferred items and the unverified list) is in `evidence.md`. Sources: three
Chamberlain Coffee stop-motion ads (v01 claymation vignette, 11.96 s; v02 claymation TV spot, 28.29 s; v03 needle-felt
sketch, 32.21 s), their frame sheets, a full-resolution fidelity audit and a full-frame-rate completeness pass (Oct 2026).

| What | Evidence |
|---|---|
| No text in the hook; the plate moving on f0; the first cut on action | v01 @0:00–0:03 (cut 2.92), v02 @0:00–0:02.8 (2.77), v03 @0:00–0:01.1 (1.42) |
| Pale-yellow two-line captions, hard on and off, script caps kept, the inner mask | v03 @0:01.167, @0:01–0:05, @0:21 ("WOAH"), @0:29 ("F**k that's good"), off @30.23 |
| The in-world TV spot: static, blinking red label words, packs built in held steps, the wordmark arc over the lineup | v02 @0:05.17–0:19.49 |
| Reaction run and wide hold out | v02 @0:19.5–0:23.9, @0:23.9–0:28.3 |
| Iris out on the characters, then the wordmark alone on black | v03 @0:28–0:32.2 |
| The plate cadence: ones, twos, held poses; every camera move physical | v01, v02, v03 completeness pass |

Inferred, not shown: the wordmark card in F-C (v01's clip has none), the disclosure line, the link and stockist lines, CS-2
and CS-3 (fixes for contrast and low heads), the sound decisions (the sound wasn't observable).

## Appendix B. Hook-title bank
On-screen headlines don't exist in this style; the bank is the post title (≤ 8 words, lowercase) with the f0 action it
names. Templates: "{character} just wanted {thing}" · "{character} found out where {product noun} comes from" · "pov:
{character} discovers {benefit}" · "{character} vs {small daily problem}".

**F-A Dialogue sketch**
| # | Post title | f0 action | First line | Hook |
|---|---|---|---|---|
| 1 | the owl who couldn't sleep | an owl yawning on a branch at noon | "It's NOON and I'm still up." | HA-16 |
| 2 | fox found the coldest drink in town | a fox fanning itself on hot pavement | "Is it just me or is the road melting?" | HA-16 |
| 3 | where does your tea come from? | a felt teabag lowering itself into a cup | "Hold on, let me show you." | HA-15 |
| 4 | the bear who'd never had it cold | a bear barista mid-pour | "You've NEVER had it cold?" | HA-14 |
| 5 | squirrel vs monday | a squirrel skidding in on an acorn | "I'm LATE!" | HA-13 |
| 6 | four friends, one bill | four friends staring at a pizza bill | "So… who's got this?" | HA-16 |

**F-B Product broadcast**
| # | Post title | f0 action | Screen spot claim words (from the claims list) | Hook |
|---|---|---|---|---|
| 1 | game night needs snacks | over the shoulder of pups watching the match on TV | ORGANIC · SMOOTH | HA-16 |
| 2 | the commercial everyone stopped for | a mouse channel-surfing with the remote | COLD-BREWED · LOW SUGAR | HA-16 |
| 3 | shop window at midnight | a cat pressing its nose to a shop window | 3 FLAVOURS | HA-15 |
| 4 | the ad the hamsters needed | the hamster kid watching TV, parents counting coins | TRACKS EVERYTHING · ZERO FEES | HA-16 |
| 5 | rent day, but calm | a nervous clay character watching a wall calendar flip | BILL REMINDERS | HA-15 |

**F-C Vignette**
| # | Post title | f0 action | Button | Hook |
|---|---|---|---|---|
| 1 | sunglasses, coffee, venice | a character mid-sip in sunglasses | a cat peeking from the bushes | HA-16 |
| 2 | boardwalk snack run | a skater crunching a chip | a seagull steals one | HA-16 |
| 3 | rainy day tea | steam curling from a cup by a rainy window | a snail shelters under the saucer | HA-15 |
| 4 | the jar stays full | a jar of coins on a windowsill, a coin drops in | a sparrow adds one more | HA-15 |
| 5 | bills? sorted | a character swinging in a hammock, phone on chest | the phone buzzes; they don't move | HA-16 |
