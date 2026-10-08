# Stunt Compression Style Playbook (template v1)

**Purpose:** you (Claude) receive **raw multi-person stunt footage**: a giveaway, a challenge, a street question, a timed task, a prank or a reveal, shot on two or more cameras, plus the creator's notes on what was at stake. Use this playbook to **select the ~10% of moments that tell the stunt**, cut them to a new shot every 1.0–1.5 s, pin the stake to the real money or prize on screen, switch the caption mode beat by beat, and end on the face that won.

**Input** (SW-01 `stunt_footage`): 5–20 minutes of raw vertical footage per 60 s reel from cameras A (host), B (subject), C (wide), D (phone screen), with lav audio; optional sponsor logo file; the creator's stake log (amounts given, clock times on set). Nothing in this style can be generated: **the footage is the product** (SW-12 `total`, §12).

**What this playbook makes the editor do:** compress, not present. There is no headline, no talking-head spine, no intro, no outro. Every decision below is about which moment to keep, when to cut, what the stake is worth on screen, and which caption mode a beat gets.

### Style DNA `[DNA]`
A Stunt Compression reel looks like a stunt that is already happening when you arrive: a person mid-stride, mid-sentence, with a chunky caption already on the frame; then a hard cut every second or so between the host, the subject's face and the stake itself. Money and prizes are real objects, and the number sits **on** them as a glowing neon-green tag; losses flash red. Captions are loud comic caps when the energy is up, small lowercase single words when the moment is intimate, and gone when the action speaks. There are no splits, no cards, no titles; colour appears only as money green, loss red, shout yellow, and at most two colour events (a black-and-white hold, a green flash). It ends on a reaction, not a slate.

**Copy these 5 things** (each one is load-bearing):
1. **Cold open mid-action**: f0 is a moving person with a caption already running; first hard cut by 2.1 s; the stake on screen by 2.3 s. → §6.2 (HA-13), H1–H3.
2. **One moment per 1.0–1.3 s**: 30–48 hard cuts per minute, a median shot of 1.0–1.3 s, plus a camera move on the big reactions, keep ~10% of the shoot. → §1 P4b, §7.6, §9.3.
3. **The money is literal and tagged where it sits**: a neon-green `good` number pinned to the real cash or prize, red `$0` for a loss, totals that tick in place. → §8 P-20…P-24, §17, §18.
4. **Per-beat caption modes**: comic caps (CS-2) / yellow shout (CS-3) / neutral lowercase single words (CS-1) / none. → §5.3.
5. **Cut to the face that wins or loses**: every reveal is followed by the reacting subject within 6 frames, and the reel ends on a reaction. → §9.3 R-03, §7.5.

### Directives `[DNA]`
| # | Directive | Where it lives |
|---|---|---|
| D1 | **Compress, don't present.** Keep about 10% of the shoot, one moment per 1.0–1.5 s; a shot longer than 2.5 s needs a state change inside it | §1 P4b, §7.6, H2 |
| D2 | **Cold open mid-action.** No intro, no logo, no title card, no "hey guys": f0 is action + caption | §6.2, H1, N1 |
| D3 | **The stake is a real object, and the number sits on it.** Tags show the exact amount handed over, pinned to the cash or prize, never to an empty frame | §8 P-20, §17, §18, H8 |
| D4 | **Cut to the face that wins or loses** within 6 frames of the reveal; reactions belong to the subjects, not only the host | §9.3 R-03, H4 |
| D5 | **Hard cuts (≈ 95%); a tighter real angle first.** The camera has three measured moves only: a jump re-crop on the same take, an eased push into a reaction, a crash zoom on a crowd; no Ken Burns, no shakes | §9.1, §10.2, H12 |
| D6 | **Caption mode is chosen per beat:** comic caps for hype and rules, yellow for shouts and subjects' lines, neutral lowercase for intimate beats, none when a tag, the clock or the action carries the beat | §5.3, H10 |
| D7 | **Colour has one job each:** green = money/gain, red = loss/no, yellow = shout. At most 2 colour events (GR-bw, GR-green) per reel | §4, H13 |
| D8 | **End on the reaction or the number.** No outro, no end card, no black tail; the CTA, if any, rides the final reaction | §6.7, §7.5, H15 |

Buyer directives `BD1…` `[VAR]` are added below this table by the buyer's copy; they may only make the style stricter or more specific.

### Quick index
| § | What | Status |
|---|---|---|
| §0 | Style profile (switches) | REQ |
| §1 | Procedure (moment selection is the craft) | REQ |
| §2 | Hard rules H1–H18, NEVER N1–N14, exception E6 | REQ |
| §3 | Worlds W-set / W-band, layouts L-full / L-wide-band, bands | REQ |
| §4 | Colour roles, grades GR-bw / GR-green | REQ |
| §5 | Type, caption profiles CS-1…CS-4 + mode none | REQ |
| §6 | Hook system: HA-13 default, HA-14, HA-16 | REQ |
| §7 | Structure `stunt`, the stake-beat ritual, cadence | REQ |
| §8 | Visual system: families B-1…B-7, patterns P-01…P-52 | REQ |
| §9 | Transitions T-00…T-05, shot grammar R-01…R-12 | REQ |
| §10 | Motion, zoom policy `presets` (Z-R1/R2, Z-P1, Z-C1), layers | REQ |
| §11 | Sound contract | REQ |
| §12 | Footage: the shoot brief, shot list SH-1…SH-10, fallbacks FB-1…FB-10, inserts | REQ |
| §13 | Output contract | REQ |
| §14 | Worked examples (3) | REQ |
| §15 | QA | REQ |
| §16 | Frame template / chrome | OFF |
| §17 | Running state & anchored graphics | **ON** |
| §18 | Data contract | **ON** |
| §19 | Evidence & citations | OFF |
| §20 | Dialogue | OFF |
| §21 | Canvas camera | OFF |
| §22 | Ink | OFF |
| §23 | Continuity | OFF |
| §24 | Series furniture | OFF (VAR) |
| §25 | Sponsor, brand & end cards | **ON** (VAR) |
| Parts C–F | Exceptions & core, personalisation, changes, IDs | REQ |
| App. A | Cold-open line and post-title bank | REQ |
| App. B | Evidence map (full map in `evidence.md`) | REQ |

Formats: **F-A "Stunt compression"** (the only format).

---

## §0 Style profile `[REQ]`

```yaml
profile:                         # mirrored in tokens.json -> profile
  source_type: stunt_footage
  presenter: {presence: host, share: [60, 100], max_absence_s: 3.0}
  spine: footage
  captions: {mode: full, role: support, mute_policy: mute_safe}
  graphics: support
  duration: {class: standard, target_s: [40, 75]}
  language: {speech: en, captions: {lang: en, script: Latn, transform: verbatim}, on_screen: en, post_title: en,
             supported: [[en, en, Latn], [hinglish, hinglish, Latn], [hi, hi, Deva]]}
  numbers: {grouping: international, currency: "$", compact: k_m_b, units: metric, decimals: 0, style: full}
  tone: {energy: hype, comedy: light, comedy_max: light}
  themes: {policy: single, packs: [], default: null}
  formats: {list: [F-A], default: F-A}
  footage_dependency: total
  cta: {devices: [none, post_only, comment_keyword, link_bio], placement: end, chosen: none}
  modules: {chrome: false, running_state: true, anchors: true, data_figures: true, citations: false,
            dialogue: false, canvas_camera: false, ink: false, continuity: false, series: false, brand: true}
```

Why each switch has its value:
- **source_type: stunt_footage**, because all four evidence reels are raw handheld multi-person footage of an event, with the edit keeping ~10% (v03: 58 moments in 74 s).
- **presenter: host, share 60–100, max absence 3.0 s**: a face (host or subject) is on screen ~85% of runtime, but group wides and object inserts drop the detected face under 6% of frame height; the longest face-less run in the evidence is a ~2 s cash-pile insert (v02 @ 0:33–0:34) or a phone screen (v01 @ 0:12, 0:28).
- **spine: footage**: the picture moments are the timeline; speech follows the picture and a sentence often runs across 2–4 cuts (v04 @ 0:00–2.7).
- **captions: full / support / mute_safe**: captions run word by word on most beats (v01, v02, v04), but they serve the action; they switch off when a tag or the clock carries the beat (v02 @ 0:36–0:47, v03 throughout).
- **graphics: support**: overlays (tags, clock, logo pops, chip, X) cover 13–27% of runtime (v01 ≈ 15%, v02 ≈ 27%, v03 ≈ 13%); this is above the `minimal` cap of 15% (deviation from STYLE-COVERAGE, Part E).
- **duration: standard 40–75 s**: evidence 37–74 s, mean 50 s; one mid-reel escalation (re-hook) every reel (§7.4).
- **language: en**, `(unverified)` speech; Hinglish and Hindi are supported for buyers (§5.5).
- **numbers: international $, full style**: "$10,000", "$14,000", "+$8,370" are written out; compact only from 1,000,000 up.
- **tone: hype / light**: high energy, visual gags without meme sounds (v03 ghost replay @ 0:29–0:30).
- **themes: single**: the palette never changes; only footage changes.
- **formats: F-A only**: the four reels share one visual system; their differences are caption modes per beat (§5.3).
- **footage_dependency: total**: without the stunt there is no reel; §12 says exactly what to shoot.
- **cta: none by default**: no evidence reel has a CTA; the buyer may pick a comment keyword or link line that rides the last reaction (§6.7).
- **modules**: `running_state` (totals and the set clock), `anchors` (tags pinned to objects), `data_figures` (every money figure recomputes; this is how the running total is built on today's engine, §17), `brand` (sponsor logo pops, v02 and v03).

---

## §1 Procedure (follow in order) `[REQ] [DNA]`

The craft step of this style is **P4b moment selection**. Everything else serves it.

| Step | Do | Output |
|---|---|---|
| **P1 Inventory** | `veos ingest` every file; ffprobe resolution, fps, rotation, audio. Name sources by camera: A host, B subject, C wide, D phone screen (S1…). Conform everything to 30 fps CFR (`veos conform`). Register any sponsor logo with `veos asset add <file> --origin creator`. | `work/sources.json` |
| **P1b Take log** | Watch every source at 2× and log **moments** (a moment = one continuous action with one meaning, 0.5–4 s) into `plan/moments.json` (schema below). Mark the stake: every amount, prize and time on set, exactly as said or shown. | `plan/moments.json` |
| **P1c Sync** | When two or more cameras recorded the same moment (A on the host, B on the subject), run `veos sync --ids A,B[,C]` so angle switches inside that moment keep one continuous audio. | `work/sync.json` |
| **P2 Prepare** | Matte only for P-34 ghost replay (optional). No other step needs a matte. | `work/matte/*` (optional) |
| **P3 Transcribe** | `veos transcribe` every source with speech (host lav, subject lav, camera audio). Apply `language.captions.transform`; glossary = the creator's name, handle, sponsor and place names. | `work/words/*.json` |
| **P4 Segment** | Map the stunt onto the arc (§7.1): COLD OPEN → SETUP → ESCALATION → (RE-HOOK) → REVEAL → REACTION/END. | arc table in the brief |
| **P4b Moment selection** | Fill the arc with moments by the quotas and scores below; write `plan/edl.json` (`veos cut`). | `edl.json`, `cutmap.json` |
| **P5 Classify** | Every kept moment gets a line type (§8.4) and a trigger (the word or the visible action the picture lands on). | beat sheet |
| **P5b Reaction bank** | For every subject who wins or loses, list their 2–4 best reaction moments (shock, hands on head, jump, hug) with times; R-03 draws from this bank. | `plan/moments.json` `bank` |
| **P6 Tone-tag** | `hype` · `explain` · `win` · `warn` · `awe` (tone treatment in tokens). | beat sheet |
| **P7 Hook plan** | Pick the archetype (HA-13 default), write **3 cold-open variants** (§6.5), run the stopper tests (§6.1). | 3 hook proposals |
| **P8 Visual plan** | Per beat: pattern (§8.4), caption mode (§5.3.6), state ops (§17), figures (§18), anchors (anchor pass below), grade event (§4.4), sponsor beats (§25). | beat sheet + `plan/figures.json` |
| **P9 Beat sheet** | One beat per kept moment (§13), meeting §7.6 cadence. | beat sheet |
| **P10 SFX + transitions** | Cue moments only on the hook, reveals and the whip (§11); transition map (§9). | `timeline.sfx`, `transitions` |
| **P11 Assets** | Sponsor logo (ask once), phone recordings, inserts flow (§12.5); say which fallbacks (§12.3) are used. | `plan/assets`, `plan/inserts.json` |
| **P12 Checkpoint** | §13.5. **Wait for approval.** | checkpoint message |
| **P13 Build** | Scenes act by act → `veos scenes-meta` → `veos measure` → `veos validate` → preview → QA §15 (≤ 3 passes) → render. | final MP4 |

### 1.1 `plan/moments.json` (the take log)
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
`kind` ∈ `walk` (host walk-and-talk) · `stake` (the stake named or shown) · `rule` (how the stunt works) · `ask` · `answer` · `reveal` · `reaction` · `crowd` · `object` · `phone` · `wide` · `clock` · `brand` · `end`. `energy` 1–5 (5 = shout, jump, tears). `face_h` = the largest face height / frame height.

### 1.2 Moment selection (P4b): quotas, scores, cutting
1. **Arc first.** Write the arc table with target seconds (§7.1). Every arc slot names the 1–3 moments that carry it before any other moment is considered.
2. **Quotas per 60 s of final reel** (they produce the 30–48 cuts/min DNA):

| Kind | Per 60 s | Length each | Notes |
|---|---|---|---|
| walk / stake / rule (host talking) | 6–10 | 1.2–2.2 s | the sentence may run across cuts (R-08) |
| ask / answer (two-shot or subject) | 6–10 | 0.8–1.6 s | |
| reaction (subjects, from the bank) | 10–16 | 0.6–1.2 s | the biggest share of cuts |
| object (cash, case, pile, prize) | 3–6 | 0.5–1.2 s | carries P-20 tags |
| wide / crowd | 3–7 | 0.8–1.5 s | establish before a reveal (R-05) |
| phone | 0–2 | 1.0–2.0 s | full-frame screen recording |
| clock (timed stunts only) | 4–10 | 0.6–1.2 s | each shot shows one clock value |
| end | 1 | 1.5–3.0 s | the last reaction (P-12) |

3. **Score** each candidate: `score = 2×energy + 2×(face_h ≥ 0.18) + (speech clear) + (shows the stake) − 2×(repeats a reaction type already used in the last 10 s)`. Fill each slot with the highest score; ties go to the moment that is shorter.
4. **Trim** every moment to its action: start 2–4 f before the action or the first word, end on the action's peak (a reaction ends at the peak of the shock, not after it). Speech moments end on a word boundary ±1 f.
5. **Same moment, two angles:** inside one `sync_group`, cut between angles on the session time (R-08): either hand-write `timeline.shots` on the synced MIX (`veos shots render`), or put two EDL segments whose `in` points are the same session second (from `work/sync.json`). Never cut back in time inside a group.
6. **Cut to ≤ 1.5× the target duration first**, then remove the weakest moments until the reel is inside `target_s` and the median shot is 1.0–1.3 s. Check with `veos validate` (V-CADENCE reports cuts/min and median shot).
7. **Ratio check:** if the shoot gives fewer than 35 usable moments per 60 s of reel, say so at the checkpoint and shorten the reel; never stretch moments past 2.5 s to fill time.

### 1.3 Module steps
| Module | Step |
|---|---|
| `running_state` | **State plan:** list every variable (`total`, `stake`, `clock`) with its ops per beat (§17.1); the clock values come from the creator's log or the visible timer, never invented. |
| `anchors` | **Anchor pass:** for every tag, `veos track --project P --at <t_in> --look` and read the object's box off `plan/tracks/look_<t>.jpg`. Static object (moves < 90 px during the hold): place the tag from that box, no track. Moving object: `veos track --project P --id <tag> --at <t_in> --box x,y,w,h --from <t_in> --to <t_out>` (`--point` for a hand or fingertip), check `plan/tracks/<tag>.preview.jpg`, and give the scene `anchor: {track: "<tag>", ...}` (§17.2). |
| `data_figures` | **Data check:** every amount on screen is an input or a figure in `plan/figures.json`, with its words (`said`) or the creator's log as provenance; totals are `sum` figures; recompute with `veos figures` (§18). |
| `brand` | **Sponsor check:** logo file (creator-supplied) or brand-in-type; the disclosure wording (BV-14, default "Paid partnership"); which beats show the product (§25). |

---

## §2 Hard rules `[REQ] [DNA]`

### 2.1 Editing rules (every style)
The nine editing rules in `playbooks/_global/GLOBAL-RULES.md` apply. They are directions, not limits: smooth, seamless motion; nothing overlaps by accident; keep the face clear (behind the speaker is fair game, text included); readable at a glance; one idea at a time; show what's being said; never fake facts; pace like the style, not like a timer; the style decides the look.
- **Facts the engine checks:** accidental overlaps, jumps, the face covered, unreadable text, numbers and quotes that don't match what was said, the promised count. Every count, timing and budget this playbook gives is direction for the edit, not a limit.
- **Retired (8 Oct 2026), whatever this playbook says below:** no REPRESENTATIONAL or example labels on made-up cards, no credit lines, no flash limit (flash as often as this style calls for; any "NC-11" cap below no longer applies), and text may sit behind the speaker without an exception.

### 2.2 Declared exceptions
| ID | Limits in this style | DNA reason | Evidence |
|---|---|---|---|
| **E6 Hard swap** | Only for (a) the countdown clock digits (P-24), (b) running-total digits (P-23), (c) CS-1 neutral caption words. Container rect constant ±4 px; the container's first entry and final exit stay eased (pop in 5 f, out 4 f) | The set clock jumps 0:58 → 0:49 → 0:48 on cuts and the neutral captions swap one word every 0.17–0.3 s; a fade would blur the rhythm | v02 @ 0:36–0:47 (clock); v01 hook 0:00–1.0 ("are" → "you" → "subscribed") |

No other exception is used. Captions and tags on the torso are not an exception (structure C.2: footage bodies are not elements).

### 2.3 MUST rules
| ID | Rule | Check |
|---|---|---|
| **H1** | **Frame 0** shows live footage of a moving person (or the moving stake for HA-14/HA-16) **and** a caption chunk already on screen (HA-13/HA-14; the first chunk starts ≤ 3 f in). No headline, logo, title or black frame at f0. | V-F0 |
| **H2** | **Cadence:** 30–48 picture changes per minute, median shot 1.0–1.3 s, p90 ≤ 2.2 s, ~20% of shots under 0.8 s; weighted SC 5–14 per 10 s; no gap > 2.5 s without a weight-1 change; first cut by 2.1 s. | V-CADENCE |
| **H3** | **Payoff by 2.3 s:** the stake (money, prize, the pile, the clock) or the first big reaction is on screen by 2.3 s; tag that scene `payoff: true`. | V-F0 |
| **H4** | **Reaction rule:** every reveal, verdict and handover is followed by a cut to the face of the person who won or lost within 6 frames of the reveal frame, held 0.6–1.2 s. | review |
| **H5** | **On the word / on the action:** tags, X flashes and logo pops land 1 f before the trigger word or on the visible action frame (case opens, cash touches the hand), fully on within ±5 f. | V-ONWORD |
| **H6** | **Face rule:** no tag, chip, caption or sticker covers a face box (eyebrows to chin, ear to ear); 40 px clearance from the face for tags and chips; captions sit at the chest. | V-FACE |
| **H7** | **Presence:** a face ≥ 6% of frame height is on screen ≥ 60% of runtime; no face-less run longer than 3.0 s (object inserts, phone screens and wides included). | V-PRESENCE |
| **H8** | **Money truth:** every displayed amount equals what was actually given, won, lost or stated, from the creator's log or the speech; totals equal the sum of their parts; prop or fake cash is never tagged with an amount. | V-DATA |
| **H9** | **State integrity:** a total never contradicts the last spoken or shown value; the clock only goes down, may jump between cuts, never between two frames of one shot. | V-STATE (pending; review) |
| **H10** | **Caption mode per beat** is declared in the beat sheet (`caption.mode`: comic / shout / neutral / punch / none) and written with `captions.overrides`; captions are hidden while a money tag, loss tag, logo pop or name call is on screen. Max 4 words per chunk (1 in neutral). | V-CAPTION |
| **H11** | **Type floors:** comic captions ≥ 84 px, neutral ≥ 54 px, tags ≥ 72 px, clock ≥ 140 px, labels ≥ 40 px, legal ≥ 22 px; contrast ≥ 4.5:1 (3:1 for ≥ 96 px display) via the 5–9 px ink stroke. | V-TYPE |
| **H12** | **Camera = the §10.2 presets only:** Z-R1 jump re-crop (on a cut or a same-take jump), Z-P1 reaction push, Z-C1 crowd crash zoom; 3–7 camera events per 60 s, never two within 0.4 s, never the same one twice in a row. No Ken Burns on wides, no shake, no rotation, no zoom on the host's talking lines. Re-crops stay ≤ 1.35× on 1080p, ≤ 2.0× on 4K. | V-CAMERA |
| **H13** | **Colour discipline:** ≤ 3 bright hues per frame; `good` only for money/gain, `bad` only for loss/no, `accent` only for shouts; ≤ 2 grade events per reel, ≥ 6 s apart, never the same one twice in a row. | V-HUES |
| **H14** | **Escalation:** one re-hook between 45% and 65% of runtime (a second stake, a doubled prize, the clock starting, the room or pile reveal). | V-REHOOK |
| **H15** | **Promise integrity:** the stake named in the cold open is paid off on screen (handed over, won or lost) before the end; the CTA keyword, if chosen, is on screen ≥ 1.5 s; the reel ends ≤ 6 f after the last reaction or word. | V-PROMISE |
| **H16** | **Inserts:** every third-party moment (another brand's logo, a screen that isn't the creator's, a referenced video) is creator-supplied or a created substitute recorded in `plan/inserts.json`. | V-INSERTS |
| **H17** | **Number format:** amounts follow SW-08 exactly (`$10,000`, `₹1,20,000`, compact only ≥ 1,000,000); a `+` prefix only on gains, never on a total. | V-NUMFMT |
| **H18** | **Exceptions:** E6 only for the clock, running-total digits and CS-1 words; the container is marked `data-slot`. | V-EXC |
| **H-dead-air** | Dead air (spine `footage`): picture-led gaps are allowed while the action continues; a gap of > 0.6 s with no speech **and** no visible action is cut. | review |
| **H-TB** | n/a (captions are on). | — |
| Audio | −14 LUFS integrated, true peak ≤ −1.5 dBTP (NC-8). | `veos qa` |
| Determinism | Every frame is a function of its index; shakes and flickers use `ctx.rng(seed)` (NC-9). | review |

### 2.4 NEVER list
- **N1** An intro: no title card, logo sting, "welcome back", channel animation or black frame before the action.
- **N2** A headline banner, pill, lower-third or chapter marker anywhere in the reel.
- **N3** Split screens, cards, panels, picture-in-picture or a canvas world; the frame is always footage.
- **N4** A tag on an empty frame, a tag that floats away from its object, or a number that is not on the money/prize/person it describes.
- **N5** Camera moves outside §10.2 (Ken Burns, slow drifts on wides, shakes, rotations), glitch/RGB-split/film-burn packs, light leaks, wipes and crossfades.
- **N6** Coloured caption words except the CS-2 money word in `good`; yellow on host lines that are not shouts; pink outside a neutral-register reel.
- **N7** Stock footage, AI-generated people or money, or "money rain" overlays; every frame of money is the creator's real stake.
- **N8** Fake on-screen UIs presented as real (a fake bank balance, a fake follower count, a fake call screen).
- **N9** A caption covering a money tag, the clock or a logo pop; two caption systems at once.
- **N10** Holding a shot past its action "to breathe"; a reaction that plays after its peak.
- **N11** Colour events back to back, or a green flash longer than 10 f.
- **N12** Meme sounds, laugh tracks or record scratches (comedy is `light`).
- **N13** An outro, end card, subscribe animation or slate after the last reaction.
- **N14** Redaction failures: phone numbers, emails, bank details and addresses on any phone screen are blurred for their whole time on screen (NC-14).

Buyer NEVER items `BN1…` `[VAR]` are added here by the buyer's copy.

---

## §3 Worlds, layouts, stage moves, safe zones `[REQ] [DNA; coordinates TUNE ±5%]`

### 3.1 Worlds
| ID | Kind | Look | Carries | Enter / exit |
|---|---|---|---|---|
| **W-set** | `footage` | The stunt's real location exactly as shot: daylight or bright practicals, un-graded, natural saturation | 100% of the reel's picture | Hard cut only |
| **W-band** | `footage` | A blurred, darkened copy of the same clip behind a horizontal shot (blur 40 px, brightness 0.55) | Only horizontal wides from camera C (L-wide-band) | Hard cut in and out |

There is no canvas, data stage, paper or void world. A frame without footage never exists in this style.

### 3.2 Layout library
| ID | Engine | Presenter rect | Graphic rect | Caption band | Treatment | Share of runtime |
|---|---|---|---|---|---|---|
| **L-full** | `full` | full frame 0,0,1080,1920 (any person, any camera) | the whole frame; tags sit on their objects | comic cy 1000 / neutral cy 940, `chest` anchor (face bottom + 30 px, clamped to y 880–1150) | none | 90–100% |
| **L-wide-band** | `blurfill` | a 16:9 band 1080×608 at cy 960 (y 656–1264) over its own blurred copy | inside the band | `fixed_y` cy 1380 (below the band) | blur 40, luma −0.45 | 0–10% |

**Layout schedule:** none. L-wide-band is used only for a horizontal camera-C clip that cannot be cropped to 9:16 without losing the subject (FB-5), ≤ 2.0 s per use, ≤ 3 uses per reel.

### 3.3 Stage moves
| ID | Move | Recipe | Use |
|---|---|---|---|
| **G-0** | Cut | `via: cut`, 0 f | every layout change; the only stage move of the style |

No panel drops, pop-backs, shrinks, slides or morphs exist in this style.

### 3.4 Layout diagrams (1080 × 1920)
**L-full** (the reel):
```
┌──────────────────────────────┐ 0
│   IG top UI: no text         │ y 0-110
│        ┌─────────┐           │
│        │  0:58   │  P-24     │ clock box y 205-375 (cy 290), x 290-790
│        └─────────┘           │
│      ( faces: y 250-800 )    │ host/subject heads usually here
│  HOLY GOD!   (P-36 / CS-3)   │ shout band y 450-620 when it sits beside a low head
│        $10,000   (P-20)      │ tag band y 560-1460, ON the object
│      I'M ABOUT TO  (CS-2)    │ comic cy 1000 / neutral cy 940 (chest anchor)
│      [ LOGO POP  cy 1000 ]   │ P-30 / P-31 brand, w 760-900
│ Paid partnership (TC-legal)  │ x 64, y 1450-1480
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
- **Meaning-text box:** x 64–1016, y 110–1500; between y 900 and 1540 nothing with meaning goes right of x 970 (NC-5 button column).
- **Caption band:** comic `chest` anchor, default cy 1000, allowed 880–1150; neutral cy 940, allowed 880–1000. When the face box bottom is below y 1000 (a crouching subject, a low angle), the caption moves above the head (engine `avoid_face`).
- **Clock band:** y 205–375. **Tag band:** y 560–1460. **Legal line:** y 1450–1480 at x 64.
- **Brand band:** logo pop / brand type centred cy 1000; when a face sits in y 800–1200, it moves to cy 330 (top band) and the clock is off for that beat.

### 3.6 Presenter rules (`presence: host`)
- **Who counts:** any face, the host's or a subject's. The host is not required on screen; **the stake and the reacting faces are**.
- **Share:** a face ≥ 6% of frame height on ≥ 60% of runtime (evidence ≈ 85% at any size). **Longest absence:** 3.0 s (an object insert followed by a phone screen is the limit).
- **Return:** always a hard cut to a face, never a move.
- **Crops:** in close-ups the face height is 18–35% of the frame, eyes at y 520–760; in two-shots both heads between y 220 and 820. Recrops (FB-2) keep the eyes inside y 480–800.
- **Behind the head:** nothing (no E1, no depth sandwich).

---

## §4 Colour, themes, grades `[REQ] [roles' meanings DNA; brandable hex VAR; grade TUNE]`

### 4.1 Role palette
| Role | Hex | Its one job | Text on it | Contrast | Brandable |
|---|---|---|---|---|---|
| `good` | `#39FF14` | Money and gain: P-20/P-21/P-23 tags, the CS-2 money word, P-25 object glow, P-51 green flash | `ink` | 15.5:1 | **fixed** |
| `bad` | `#E5191B` | Loss, zero, wrong: P-22 `$0`, P-27 X flash, the clock at 0:00 | `paper` | 4.7:1 (as text it always carries a 6 px white stroke) | **fixed** |
| `accent` | `#FFE600` | Shout yellow: CS-3 lines (subjects' lines and exclamations), P-36 name calls | `ink` | 16.6:1 | TUNE (light warm hue) |
| `primary` | `#1179CB` | The creator's own colour: P-26 handle chip ring and avatar, P-29 avatar badge, P-35 keyword sticker fill | `paper` | 4.6:1 | **VAR** (BV-02, first colour) |
| `punch` | `#F34FF7` (audit: v01 @0:30.5 glyph core) | The one CS-4 pink punch word in a neutral-register reel | `ink` (as text fill: 6 px white stroke) | 7.4:1 vs ink | VAR |
| `paper` | `#FFFFFF` | Caption fill, clock fill, chip fill, brand-in-type | — | — | fixed |
| `ink` | `#000000` | Every stroke (5–9 px) and hard shadow | — | — | fixed |
| `money_edge` | `#0A3A06` | The 5 px inner stroke of money tags | — | — | TUNE |

The buyer's colours land here: primary = `{{BV-02.primary|#1179CB}}`, accent = `{{BV-02.accent|#FFE600}}`.

### 4.2 Meanings
- **Green = money changes hands or is won. Red = it doesn't, or it's gone.** The axis of every reel is green ↔ red; never use green for anything that is not money or gain.
- **Yellow = someone shouts** (a subject's line, an exclamation, a name call). It never marks money.
- **The creator's colour (`primary`) appears only on the creator's own furniture** (handle chip, avatar badge, keyword sticker).
- **Brand colours appear only inside the sponsor's own logo file** (P-30).

### 4.3 Theme packs
OFF (`themes.policy = single`): the palette never changes per reel.

### 4.4 Grades `[TUNE]`
- **Footage grade:** none. Footage is not regraded; only exposure and white balance are matched between cameras A/B/C of one moment, so an angle switch doesn't jump in colour.
- **Colour events** (`grades.events.max_per_reel = 2`, ≥ 6 s apart, never the same one twice in a row):

| ID | Name | Recipe (today's engine) | Frames | When | Evidence |
|---|---|---|---|---|---|
| **GR-bw** | B&W hold | z11 light-pass scene: full-frame `#808080` fill with `mix-blend-mode: saturation` (everything below turns greyscale); hard in with a Z-R1 jump on the same take (or on a cut), hard out on the next cut; captions off or CS-1 white only; no tags under it | 24–45 (0.8–1.5 s) | **suspense:** the subject reads the phone, waits for the answer, the case is about to open | v04 @ 0:06–0:07 |
| **GR-green** | Green flash | **built-in flash transition** (no scene): `{"t": <moment>, "type": "flash", "colour": "good", "peak": 0.6, "pre": 0, "frames": 10, "decay": 0.5}` in `timeline.transitions`; peak on the moment, held near 0.6 for the first ~5 f, gone by f9 | 6–10 | **yes / confirmed / won:** the follow tap lands, the answer is right, the money is handed over | v04 @ 0:12 |

**GR-bw is live, not a freeze** (measured v04 @ 6.40: the footage keeps moving). It enters on the same take with a **Z-R1 jump re-crop 1.13×** on its first frame and a slow push (+0.3% per frame) through the hold; it leaves on the next hard cut. Declare each GR-bw event in `timeline.grades` (`{"t": 6.10, "id": "GR-bw", "dur": 1.2}`) so V-CADENCE counts it; GR-green is its `flash` transition entry (the colour-event budget above still counts it).

### 4.5 Rules
- ≤ 3 bright hues per frame (`max_bright_per_frame: 3`); a green tag + a yellow shout + a sponsor logo is the limit.
- Coloured text always carries an ink or paper stroke (5–9 px); footage is busy and bright.
- No tint, vignette, grain, bloom or LUT on footage outside GR-bw / GR-green.

**Must match `tokens.json`.**

---

## §5 Type & caption system `[REQ]`

### 5.1 Font map `[slots DNA; families TUNE within the class]`
| Slot | Family (bundled) | Weight | Font class (TUNE boundary) | Used for |
|---|---|---|---|---|
| `chunky` | **Bangers** | 400 | condensed comic caps, single weight | CS-2 comic captions, CS-3 shouts, P-36 name calls, P-35 keyword sticker |
| `body` | **Inter Tight** | 600 / 700 / 800 | neo-grotesque sans 600–800 | CS-1 neutral captions (600), handle chip (700), URL line (800) |
| `numeric` | **Lilita One** | 400 | rounded heavy display, one weight | money/loss tags, running totals, the clock (CS-4 moved to Poppins 700 by the audit) |
| `display` | **Montserrat** | 900 | geometric sans 800–900 caps | P-31 brand-in-type plates |
| `ui` | **Inter Tight** | 600 | neo-grotesque sans 500–700 | TC-legal lines (disclosure) |

The comic and numeric faces in the evidence are closest to Bangers and Lilita One `(unverified)`: the originals may be licensed faces. Logos are image files, never fonts.

### 5.2 Headline element
OFF (`type.headline.kind = none`): the style has no headline, and `hooks.f0.forbid: [headline]`. The cold-open caption is the only text at f0.

### 5.3 Caption system profiles `[DNA mechanics; sizes TUNE; language VAR]`

#### 5.3.1 CS-1 Neutral (`extends: lib:mrbeast_neutral`)
| Group | Value |
|---|---|
| Mode | full / support / mute_safe |
| Chunking | `unit: word`, 1 word per chunk, ≤ 16 characters; never split a name, number or unit (a number with its currency is one chunk: "$10,000"); end punctuation stripped |
| Timing | lead 1 f; min hold 0.13 s (4 f) per word, as spoken (measured v01 0.07–0.37 s: "are" 5 f, "you" 4 f, "subscribed" 16 f); tail 0.10 s; **swap hard (E6)**, the word is fully on in its first frame; no pause hold (a pause > 0.9 s clears the word); the f0 caption may start 2 f in |
| Skin | **Poppins 600, 64 px** (TC-subtitle), lowercase, tracking 0, `paper`, **5 px black stroke** (audit v01 @0:00.4 "subscribed": a wide geometric bold with a solid black outline, ascender band 52 px, 356 px wide, cy ≈ 934), shadow `0 2 6 rgba(0,0,0,.5)`, no container |
| Position | `chest`: face bottom + 30 px, default **cy 940**, clamped 880–1000; centred x 540, max width 900; `avoid_face` |
| Emphasis | none (the punch word uses CS-4) |
| Hide | under z8 (logo pop, brand type, keyword sticker); by override during tags, the clock, name calls and GR-bw |
| Language | Latin; keep English terms; no spelling normalisation; profanity mask `inner` (`f**k`) |

#### 5.3.2 CS-2 Comic caps (`extends: lib:mrbeast_comic`): the default register
| Group | Value |
|---|---|
| Chunking | `unit: group`, **1–5 words**, ≤ 20 characters per line, 1 line (2 when the money word stacks under its noun: "UNLIMITED / MONEY"); single-word chunks are common on fast speech ("WE'RE" → "GONNA" → "KIDNAP", "COST?"); punctuation kept ("QUESTION...", "TO :)"); audit v04 @0:02.9 "CAN I SEE IF YOU'RE" (5 words, 19 chars) |
| Timing | lead 1 f; min hold 0.15 s per word; tail 0.10 s; **`reveal: word`, swap `pop` 2 f** (each new word scales 0.5 → 1.05 → 1.0 in 3 f; measured v02 @0.93 "MONEY", v02 @4.08 "WE'RE"); chunk-to-chunk changes read as hard (v04 @1.60). A chunk keeps running across a hard cut inside its sentence (v04 @1.30) |
| Skin | Bangers 400, **96 px** (TC-subtitle), UPPER, tracking 0.02, `paper` fill, **10 px `ink` stroke** (audit: the outline is ≈ 10 px, v04 @0:00.6 "ASK PEOPLE", cap 65 px; @0:02.9 cap ≈ 72 px, 5 words on one line), soft shadow `0 3 6 rgba(0,0,0,.5)`, **no rotation** (white comic chunks sit level; only the yellow shout tilts), line height 1.0. The source face is a wide italic comic (Komika Axis-like); Bangers is the closest bundled font, but it is narrower |
| Position | `chest`, default **cy 1000**, allowed 880–1150; centred, max width 920; `avoid_face`. Measured: v04 @0:00.6 cy ≈ 920, @0:02.9 ≈ 800, v02 @0:00.6 ≈ 1140, always on the chest of a person whose face fills 8–25% of the frame. **Close selfie (face box > 30% of the frame height):** the chest band is under the chin, so put captions at fixed_y cy 1180–1300 and never above the head; the style has no forehead captions |
| Emphasis | `colour`: the money word or number in the chunk turns **`good`** ("UNLIMITED / **MONEY**"); a subject's spoken amount alone in the chunk is the same green word, on their close-up (v04 @15.10 "$14,000", on with the cut); `select: number`, plus the planner's `{i, emph: true}` on money nouns (money, cash, prize, the amount word); ≤ 1 per chunk, ≤ 0.5 per s |
| Hide | as CS-1 |
| Language | as CS-1 |

#### 5.3.3 CS-3 Yellow shout (`extends: lib:mrbeast_comic`)
| Group | Value |
|---|---|
| Use | **(a) every line spoken by a subject (not the host)** and **(b) every exclamation by anyone** ("HOLY GOD!", "SERIOUS!", "YEAH! :D"). Selected by planner overrides `{t: [a, b], profile: "CS-3"}`. The rule is inferred from the colour use in v02 and v04 `(unverified)` |
| Chunking | 1–3 words, ≤ 14 characters |
| Timing | lead 1 f; min hold 0.30 s per word; pop 2 f, or fully on with the cut to the shouter (v04 @2.00 "HOLY"); pause hold 0.4 s (a shout lingers) |
| Skin | Bangers 400, **112 px**, UPPER, **`accent` fill**, 10 px `ink` stroke, soft shadow `0 3 6`, **rotate −8°** (measured −10° on "HOLY" v04 @2.00; a calm subject line like "I'M LIKE..." may sit level, 0°) |
| Position | `chest`, cy 1000. A shout over a wide shot whose speaker is small or off-centre is not a caption: use P-36 name call (a scene beside the speaker's head) and hide the captions for it |

#### 5.3.4 CS-4 Pink punch (`extends: lib:mrbeast_neutral`)
| Group | Value |
|---|---|
| Use | Only in a **neutral-register reel**: the single funniest or most surprising word of a beat ("god", "beast!"), ≤ 2 per reel, ≥ 10 s apart |
| Skin | **Poppins 700, 96 px**, lowercase, `punch` `#F34FF7` fill, **7 px black stroke**, shadow `0 3 6 rgba(0,0,0,.45)` (audit v01 @0:30.5 "god": the same geometric face as CS-1 in magenta, with a black outline rather than white) |
| Timing | 1 word, pop 2 f, min hold 0.3 s |
| Position | `chest`, cy 900 |

#### 5.3.5 Mode `none`
Captions are hidden by `captions.overrides {t: [a, b], hide: true}` (or a `captions.hide` range). Use it on the beats listed in 5.3.6. A hidden span still passes the mute test when it matters: a tag, the clock, a sign in the footage or the next caption carries the meaning.

#### 5.3.6 Per-beat caption mode (decide in P8, write in the beat sheet)
**Reel register** (one per reel, `timeline.captions.profile`):
| Register | Default profile | When | Evidence |
|---|---|---|---|
| **Comic** (default) | CS-2 | The host pitches the stunt to camera: giveaways, challenges, sponsored stunts, any reel whose cold open is a stake line | v02, v04 |
| **Neutral** | CS-1 | The reel is built from normal-volume conversations with strangers: street questions, phone calls, surprises told quietly | v01 |
| **Action** | CS-2, hidden on ≥ 60% of beats | Speech is crowd noise, children or chants, or the stunt explains itself through tags, a clock or a sign; host rule lines and shouts keep captions | v03 |

**Per beat** (overrides on top of the register):
| Beat | Mode | Profile |
|---|---|---|
| Host stake line, rules, escalation line | comic (neutral in a neutral reel) | CS-2 / CS-1 |
| A subject's line; any exclamation; a cheer word | shout | CS-3 (in a neutral reel: CS-1, or CS-4 for the one punch word) |
| A money tag, loss tag, logo pop, brand type or name call is on screen | **none** | hide |
| The clock is on screen | none; if a rule is spoken, CS-2 at cy 1000 | hide / CS-2 |
| GR-bw hold | none (or CS-1 white) | hide / CS-1 |
| Crowd chaos, unintelligible speech, a phone screen with readable text | none | hide |
| The last reaction (end) | none, unless it is a short clear line ("THANK YOU") | hide / CS-3 |

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

### 5.4 Other text systems
| Element | Class | Recipe | Hold |
|---|---|---|---|
| **Money tag** (P-20/P-21/P-23) | TC-display | Lilita One 400, **112 px** (audit v01 @0:15.2 `$10,000` ≈ 370 px wide incl. glow, cap ≈ 80 px; v04 @0:15.2 `$14,000` 286 × 75; by object size: 112 for an object ≥ 300 px wide on screen, 96 for a smaller one, never < 72; max 150; fills sampled `#94FF6C` (glow core) to `#19FF56` and `#73FF12`), `good` fill, 5 px `money_edge` stroke, glow `0 0 22px` + `0 0 6px` in `good`, hard shadow `0 6 0` 55% black; `$10,000` style (SW-08); gains carry `+`; **enters by type-on** (P-20) | 0.6–2.2 s; ends on the cut (v01 @15.0–17.13 held 2.1 s) |
| **Loss tag** (P-22) | TC-display | Lilita One 122 px, `bad` fill, 6 px `paper` stroke, shadow `0 6 0` 70% black | 0.6–1.4 s |
| **Clock** (P-24) | TC-display | Lilita One **170 px**, `paper` fill, **9 px `ink` stroke + a soft dark outer glow** (`0 0 18px` 70% black; measured v02 @36.3), `M:SS`, centred x 540, cy 290; the first value carries a `good` glow (`0 0 22px`) that drops at the next cut (v02 @36.0); digits hard-swap (E6), ticking once per second inside a shot (v02 @36.47 0:59 → 0:58) | the clock run |
| **Brand type** (P-31) | TC-display | Montserrat 900 caps 96–128 px, `paper`, 6 px `ink` stroke, shadow `0 6 0` | 0.8–1.4 s |
| **URL line** (P-32) | TC-label | Inter Tight 800 caps **64 px**, `paper`, 4 px `ink` stroke | ≥ 1.5 s |
| **Handle chip** (P-26) | TC-label | white pill h 96, radius 48; avatar Ø 112 overlapping its left end with a 5 px `primary` ring; text `{{BV-01.handle|@yourhandle}}` Inter Tight 700 **44 px** `ink` | 0.5–0.9 s |
| **Name call** (P-36) | TC-display | Bangers 72 px caps, `accent`, 6 px `ink` stroke, rotate −6° | 0.5–0.8 s |
| **Keyword sticker** (P-35) | TC-display | Bangers 120 px caps, `paper` text on a `primary` rounded slab (radius 22, padding 12/30), 7 px `ink` stroke on the text, rotate −4° | 1.5–2.5 s |
| **Disclosure** | TC-legal | Inter Tight 600, 26 px, `paper`, shadow `0 2 4` 80% black, at x 64, y 1450 | disclosure ≥ 2 s from the first sponsor beat |
| **X flash** (P-27) | TC-decorative (the reaction carries the meaning) | two 34 px-thick `bad` strokes forming an X, 200 px, red glow 26 px | 15–24 f, to the cut |

### 5.5 Language and number rules
- **Spelling:** captions are verbatim speech; brand names, the creator's name and handle are exact (glossary). Shouted fillers keep their spelling ("NOOO", "BRO").
- **Hinglish** (`[hinglish, hinglish, Latn]`): romanised Hinglish in caps for CS-2/CS-3 ("YE ₹10,000 TUMHARE"), lowercase for CS-1. **Hinglish speech, English captions** (`[hinglish, en, Latn]`): translate each line to short spoken English, ≤ 4 words per chunk.
- **Hindi** (`[hi, hi, Deva]`): Bangers and Lilita One have no Devanagari, so CS-2/CS-3 render in **Noto Sans Devanagari 800** with the same stroke, shadow and rotation and no case change; CS-1 renders in Noto Sans Devanagari 600. Money tags keep Latin digits in Lilita One.
- **Numbers (SW-08):** international `$10,000` by default; Indian buyers get `₹1,20,000` grouping (BV-06). Compact (`$1.2M`, `₹12 L`) only from 1,000,000 / 10,00,000 up. Gains are `+$3,000`, never `+$3k`. The `₹` glyph is drawn with a font-stack fallback (`Lilita One, Inter Tight`) and checked at P13 (no tofu).
- **Spoken number words** ("ten thousand", "das hazaar") become digits on tags and captions.
- Speech language is `{{BV-05.speech|en}}`; captions are `{{BV-05.captions|en}}`.

---

## §6 Hook system `[REQ]`

### 6.1 Stopper tests
| Test | This style's number | How it is met |
|---|---|---|
| ST-2 Mute | the first 3 s tell who, what's at stake, and that it's happening now | the stake line in comic caps + the stake object or the first reaction by 2.3 s |
| ST-3 Motion at f0 | a person or the stake is visibly moving on f0 | SH-1 walk-and-talk (or the moving pile / hands) |
| ST-5 Change count | **≥ 5 weighted SCs in 0–3 s** (`hook_sc_3s: 5`) | 2–3 hard cuts + 4–6 caption chunks (×0.5) + the payoff tag (1) |
| ST-6 Payoff-by | **2.3 s** (`payoff_by_s: 2.3`) | the scene tagged `payoff: true` (a money tag, the object glow, the stake insert or the first big reaction) starts by 2.3 s |

ST-1 (thumbnail headline) and ST-4 (headline read time) do not apply: the style has no headline. The read test for the first caption chunk is ≤ 1.0 s (`read_s: 1.0`): 1–4 words.

### 6.2 Default archetype: HA-13 Cold action `[DNA]`
f0 = a moving subject + a caption; first cut ≤ 2.1 s; money/object ≤ 2.3 s. Evidence: v04 (cut 1.30, "HOLY GOD!" 2.0), v01 (cut 1.47, chip 0.83, X 1.5), v02 (cut 1.53, MONEY 1.0, logo 2.33).

| t (s) | Visual | Caption | Layout / camera | Graphics / state | Cue moment (SFX pack) |
|---|---|---|---|---|---|
| **f0** | SH-1: the host mid-stride, already talking to camera (or to the subject beside him); the location readable behind | CS-2 first chunk **already on screen** ("I'M ABOUT TO"); the first word starts ≤ 3 f in | L-full; no camera move | none | allowed: one hit on the first chunk pop |
| 0.0–1.3 | same shot; the stake line continues; chunks swap every 0.3–0.5 s | CS-2 1–5 words per chunk; the money word in `good` ("WIN **$10,000**") | — | P-26 handle chip if the creator's channel is named (0.5–0.9 s, beside the subject's shoulder) | silent (caption pops never carry cues) |
| **1.0–2.1** | **first hard cut** (P-02) to a second angle of the same moment, or to the subject the line is about | CS-2 continues across the cut (same sentence) | cut (R-08 if synced) | — | — |
| **1.5–2.3** | **payoff:** the stake as an object (P-06) with its P-20 tag, or the subject's first big reaction (P-03) with a CS-3 shout | CS-3 for the shout, else hidden under the tag | cut; Z-P1 push when it is a reaction (v01 @1.48) | P-20 tag `payoff: true` (or P-25 glow, or P-27 X blur-in) | allowed: one reveal cue on the tag pop |
| 2.3–3.0 | third shot: a reaction (R-03) or the establish wide (P-05) | CS-2 / hidden | cut | — | — |
| 3.0–6.0 | SETUP: the rule of the stunt in 2–3 cuts | CS-2 | cuts every 0.8–1.5 s | — | — |

Change count 0–3 s in this table: 3 cuts + 5 caption chunks × 0.5 + 1 tag = **6.5** (≥ 5).

### 6.3 Allowed alternates `[DNA list; VAR choice per reel]`

**HA-14 Cold authority** (caption at f0 + the strongest image of the reel on f0; strongest image ≤ 1 s). Evidence: v02 (the host in front of the cash waterfall, "THIS IS UNLIMITED MONEY" from f0).
| t | Visual | Caption | Graphics |
|---|---|---|---|
| f0 | the biggest image of the shoot: the pile, the prize wall, the crowd, with the host in it | CS-2 "THIS" → "IS" (chunks of 1 word, 0.15–0.35 s) | — |
| 0.6–1.4 | same shot | CS-2 two-word stack with the money word in `good` ("UNLIMITED / MONEY") | — |
| 1.5 | first cut, closer on the stake | hidden | P-20 tag or P-30 logo pop (sponsored) by 2.3 s, `payoff: true` |
| 2.3–3.0 | reaction or the host's next line | CS-2 | — |
Examples: *giveaway niche:* "THIS IS ₹1,00,000 IN COINS" over the pile; *challenge niche:* "THIS IS 1,000 KG OF ICE" over the ice wall.

**HA-16 Diegetic / object open** (no caption needed at f0: a moving subject; the stake shown ≤ 5 s, in practice ≤ 2.3 s). Evidence: v03 (host holding a bucket of cash, glow on the stack at 1.67, walk-away reveal cut at 2.13).
| t | Visual | Caption | Graphics |
|---|---|---|---|
| f0 | the host holding the stake close to camera, talking or gesturing | hidden (the first words are not the stake line) or CS-2 if they are | — |
| 1.0–1.7 | the host lifts the stake toward camera | — | **P-25 object glow** on the stake, `payoff: true` |
| 2.1 | **P-11 walk-away reveal**: cut to the host walking into the location from behind | — | — |
| 3.0–4.0 | the room reacts (P-04) | CS-3 on the loudest shout | — |
Examples: *giveaway niche:* host holds a jar of notes at the shop door, the jar glows, he walks in; *challenge niche:* host holds the trophy and the stopwatch, the trophy glows, he walks onto the field.

Use HA-13 unless (a) the shoot has one image so big it beats any walk-in (HA-14), or (b) the host's first words are not usable as a stake line (HA-16).

### 6.4 Hook pairs by topic (subject → reveal) `[NICHE: example]`
Columns: topic · first subject (f0) · the reveal by N s. **Niche A (street giveaways / local shop owner)** and **niche B (fitness challenges / coach)**.

| Niche | Topic | First subject at f0 | The reveal by N s |
|---|---|---|---|
| A | "Name my shop, win ₹5,000" | host walking up the market lane toward a stranger, envelope in hand | the envelope opens: notes + P-20 "₹5,000" on them by 2.2 s |
| A | "I'll pay your bill if you can guess it" | host at the billing counter beside a customer | the receipt in close-up + P-20 tag on the total by 2.0 s |
| A | "Guess the price, keep the product" | host holding the product up to a passer-by | the product + its price tag (P-20) by 2.3 s |
| A | "Every right answer = +₹500" | host with a cash stack facing a group | first answer + P-21 "+₹500" on the subject by 2.3 s |
| B | "Hold the bar 60 seconds, win $500" | subject gripping the pull-up bar, host beside with cash | P-24 clock "1:00" + P-20 "$500" on the cash on the bench by 2.3 s |
| B | "Every rep = $10" | athlete mid-rep, host counting | P-21 "+$10" on the athlete by 1.8 s |
| B | "Beat my 100 m time, win my shoes" | host lacing the shoes on the track | the shoes in close-up + P-20 price tag by 2.2 s |
| B | "Last one standing keeps the prize" | a line of people in a plank, the prize on the floor | the prize insert + P-20 tag by 2.3 s |

The editor writes the pair for each new reel at P7, in this form, and appends it to the copy's table (Part D.6).

### 6.5 Cold-open line and post title `[DNA formula; NICHE text]`
There is no on-screen headline. The hook text is the **spoken stake line**, shown by the captions, plus the post title.
- **Stake line formula:** `[I'm about to / If you … / Whoever …] + [the stake with its number] + [the condition]`, ≤ 14 words, spoken in ≤ 3.5 s. Examples: "If you can name my shop, this ₹5,000 is yours"; "Whoever holds this bar for 60 seconds wins $500".
- **Templates:** *Offer* ("If you can X, you win Y") · *Countdown* ("You have N seconds to X") · *Escalation* ("Every X = +Y") · *Surprise* ("I'm about to pay for X") · *Choice* ("X or Y, you pick").
- **Post title:** `[Action], [Win/Keep] [stake]` in Title Case, ≤ 8 words: "Name My Shop, Win ₹5,000"; "Hold 60 Seconds, Win $500".
- **Rules:** the number in the line is the number on the tag; no clickbait the reel doesn't pay; never "you won't believe". Write 3 lines at P7, pick by ST-2/ST-5/ST-6, keep the others for A/B.

### 6.6 Hook sound
The hook may carry cues (§11): one on the first caption pop at f0 and one on the payoff tag. The music bed runs from f0 under the speech.

### 6.7 CTA `[DNA device set; VAR choice]`
Default `{{BV-08.device|none}}`: the reel ends on the reaction, with nothing after it (evidence: no CTA in 4 of 4 reels).
| Device | Spoken | On screen | Hold | Where |
|---|---|---|---|---|
| `none` (default) | — | — | — | — |
| `post_only` | — | nothing; the CTA lives in the post caption | — | — |
| `comment_keyword` | "Comment {{BV-08.keyword|KEYWORD}} and …" over or right after the final reaction | **P-35 keyword sticker** over the last reaction shot, never a separate card | 1.5–2.5 s | the last 2.5 s, after the stake is paid |
| `link_bio` | "Link in bio" | **P-32 URL line** "LINK IN BIO" at cy 300 (top band) over the final reaction | ≥ 1.5 s | the last 2 s |
No silence is added before the CTA (S4 keeps 1.0 s cue-free before it). The CTA never delays the hard end by more than 2.5 s.

---

## §7 Structure & cadence `[REQ] [DNA]`

### 7.1 Structure type: `stunt`
| Section | Share of runtime | Content | Evidence |
|---|---|---|---|
| **COLD OPEN** | 0–3 s (≤ 6%) | §6.2: action + stake line + first cut + payoff by 2.3 s | all four |
| **SETUP** | 8–15% | the rule of the stunt and who is playing; 3–6 cuts | v03 @ 0:03–0:12; v02 @ 0:02–0:06 |
| **ESCALATION** | 35–50% | the stake beats (§7.3) one after another, each bigger or closer to the end; reactions dominate | v03 @ 0:12–0:48; v01 @ 0:05–0:27 |
| **RE-HOOK** | one beat at 45–65% | a second stake, a doubled prize, the clock starting, the room/pile reveal (§7.4) | v02 @ 0:27–0:36 (vault + clock), v03 @ 0:48–0:57 (prize reveal) |
| **REVEAL** | 15–25% | the payoff: the money handed over, the prize revealed, the clock hitting 0:00 | v01 @ 0:34–0:37; v04 @ 0:24–0:29 |
| **REACTION / END** | last 1.5–3 s | the winner's biggest reaction, a hug, the host's laugh; hard end | v04 @ 0:36; v03 @ 1:13; v02 @ 0:50 |

### 7.2 Markers
`markers: none (spoken only)`. No step numbers, chapter cards or progress bars: the running total (P-23) and the clock (P-24) are the only progress devices.

### 7.3 Unit ritual: the stake beat (identical for every attempt, answer or handover)
| Step | Frames | Shot | Text | Graphics |
|---|---|---|---|---|
| 1 Ask / attempt | 24–48 f (0.8–1.6 s) | SH-3 two-shot or the host | CS-2 (CS-1 in a neutral reel) | — |
| 2 Answer / action | 18–36 f | cut to the subject on their first word (SH-2) | CS-3 on the subject's line | — |
| 3 Verdict | 15–36 f | the stake object or the subject's hands | **hidden** | right/won: P-21 "+$X" or P-20, optional GR-green; wrong/lost: P-27 X or P-22 "$0" |
| 4 Reaction | 18–36 f, within 6 f of the verdict frame | the face that won or lost (SH-2) | CS-3 only for a clear shout | P-23 total stays if the person stays on screen |
| 5 Others react (optional) | 18–30 f | host or crowd (SH-7) | hidden | — |
One stake beat = 3.2–6.0 s. A reel has 3–8 of them; each later beat is bigger (more money, less time, harder question).

### 7.4 Open loops and re-hooks
- **Loops:** the stake loop ("can they win it?") opens at f0 and pays at REVEAL; the clock loop (timed reels) opens when P-24 appears and pays at 0:00; the total loop (P-23) pays at the last op.
- **Re-hook (standard class, `rehook_every_s: 30`):** exactly one escalation beat between 45% and 65% of runtime: a doubled stake ("double it"), a second prize behind a cover, the clock starting, or the wide reveal of the pile/room. It opens with a P-05 wide or a P-06 object insert + tag within 0.5 s of the line.
- **Payoff rule:** every amount or prize named is either handed over, won or lost on screen before the end (H15).
- **Intro cap:** COLD OPEN + SETUP ≤ 15% of runtime.

### 7.5 Rhythm and energy curve
- Energy rises monotonically: COLD OPEN (high) → SETUP (the one calmer stretch, 1.3–1.8 s shots) → ESCALATION (0.8–1.2 s shots, reactions every 2–3 cuts) → RE-HOOK (a 1.0–1.5 s wide, then fast again) → REVEAL (the fastest cuts: 0.5–1.0 s) → END (one held reaction 1.5–3.0 s, or a moving celebration wide up to 6 s: the longest shot of the reel).
- Light comedy (P-34 ghost replay, a silly shout) appears at most once per 20 s and never during the REVEAL.
- The end feels like a payoff, not a goodbye: no wave, no "see you", no outro.

### 7.6 Cadence (state changes)
| Token | Value | Note |
|---|---|---|
| `sc_per_10s` | **[5, 14]** weighted | cuts 4.7–7.9 per 10 s alone |
| `hook_sc_3s` | **5** | §6.1 |
| `max_gap_s` | **2.5** | weight-1 changes (cuts, tags, events); only 4 of 135 evidence cuts are > 3 s apart |
| `max_static_s` | 2.5 | live footage is continuous motion, so this never binds |
| `caption_weight` | 0.5 | support captions |
| `cuts_per_min` | **[30, 48] (DNA)** | full-rate scene detection (threshold 0.2): 35.9 / 47.1 / 48.1 / 45.6 |
| `median_shot_s` | **[1.0, 1.3] (DNA)** | 1.28 / 1.10 / 1.03 / 1.23 (all: 1.10; p10 0.73, p90 2.13; 19% under 0.8 s, 6% over 2.5 s) |
| longest shots | 4.5 s group shot with tags, 6.0 s moving end wide | v01 @12.6–17.13; v03 @67.6–73.5 (R-11) |

V-CADENCE reads all of these from the timeline (cutmap cuts, `timeline.shots`, scene entries and events, grades, captions).

---

## §8 Visual system: footage, graphics and patterns `[REQ]`

### 8.1 Graphics role and budget (`graphics: support`)
- Overlay graphics (tags, totals, clock, chip, X, logo pops) cover **15–30% of runtime**; captions are extra.
- **At most 2 overlay elements at once** besides captions (G2 allows 4; the style looks raw), except the 3-tag moment of a multi-object reveal (captions hidden).
- **Numbers become pictures** in the literal sense: the number is never alone on screen. It is pinned to the real money, prize or person (P-20…P-23), or it is the clock (P-24).
- 6–10 distinct patterns per 60 s; 3–10 money/loss tags per 60 s.

### 8.2 Families
| ID | Family | Source class | The buyer must supply |
|---|---|---|---|
| **B-1** | Stunt footage (host, subjects, wides) | buyer-owned | cameras A/B/C (§12) |
| **B-2** | Inserts: the stake object, phone screens | buyer-owned | SH-4 object shots, SH-8 screen recordings |
| **B-3** | Money and state graphics (tags, totals, clock) | engine | the stake log (amounts, clock times) |
| **B-4** | Captions (CS-1…CS-4) | engine | clean lav audio |
| **B-5** | Brand (sponsor logo pop, brand in type, URL) | creator-supplied third-party (the sponsor's logo file) → created substitute: brand in type (P-31) | the logo file, the URL text |
| **B-6** | Colour events (GR-bw, GR-green) and blur transitions (T-01 whip, T-05 zoom blur) | engine (GR-green, T-01, T-05 are `timeline.transitions` built-ins) | — |
| **B-7** | Light comedy (ghost replay, shout stickers, name calls, hidden-cam HUD) | engine (+ matte for P-34) | — |

### 8.3 Pattern specs
Motion is in frames at 30 fps (f0 = the scene's first frame). "Block" names the engine building block.

**Cut patterns** (type `cut`; family B-1/B-2; no text unless captions run)
| ID | Pattern | On screen | Recipe | Use | Block |
|---|---|---|---|---|---|
| **P-01** | Cold walk-in | SH-1: the host mid-stride, talking | first frame mid-step with the mouth open; the first word starts ≤ 3 f in; held 1.0–2.1 s | f0 of HA-13 | EDL segment |
| **P-02** | Second-angle cut | the same moment from camera B or C | cut on a word boundary inside the stake sentence at the same session time (R-08) | the first cut, 1.0–2.1 s | EDL / `timeline.shots` |
| **P-03** | Reaction cut | the subject's face, 18–35% of frame height | starts 2 f before the reaction begins, ends at its peak; 18–36 f; within 6 f of the verdict frame; the biggest reaction of a beat gets **Z-P1** (push 1.0 → 1.15 over 15 f, starting on the cut or on the gesture: v01 @1.48, @20.40) | after every verdict, reveal, handover | EDL from the reaction bank |
| **P-04** | Crowd reaction | bystanders, friends, the class | medium or wide, 18–30 f; a crowd erupting gets **Z-C1** crash zoom from its first frame (1.0 → 1.6 over 24 f, ease-out, v03 @7.27) | after a big win, at the re-hook | EDL |
| **P-05** | Wide establish | the whole set: pile, room, prize wall, crowd | 24–45 f, before the reveal it explains; in L-wide-band if horizontal | SETUP, RE-HOOK | EDL (+ `stage` L-wide-band) |
| **P-06** | Stake insert | macro of the money or prize: the case opening, the stack in a hand, the pile | 15–36 f; the opening frame lands on the stake word (±2 f) | every stake beat, the payoff | EDL + P-20 |
| **P-07** | Phone-screen cut | a full-frame screen recording from camera D | 30–60 f; personal data blurred (NC-14) | the call, the follow tap, the balance | EDL source S1 |
| **P-08** | Tighter-angle punch | a real close-up of the same person | the incoming shot is ≥ 1.4× tighter; cut on the emphasis word | emphasis inside a speech run | EDL |
| **P-09** | Handoff match cut | the money or prize changing hands | the outgoing shot ends mid-motion; the incoming continues it within ±2 f | every handover | EDL |
| **P-10** | Jump re-crop | the same take jumps 1.13–1.20× tighter in 1 f (Z-R1), with no frames removed | `camera` `recrop-in` on the jump, `recrop-out` on the next cut; ≤ 1 per 10 s | a sponsor logo leaves (v02 @4.05, 1.20×), GR-bw starts (v04 @6.40, 1.13×); FB-2/FB-3 | `camera` presets |
| **P-13** | Detail re-crop insert | a 2–2.5× crop of the same take on the hands, phone or object, 12–18 f, between two normal shots | EDL segment of the same source + `recrop-in` at `p.scale` 2.0 (4K) / 1.35 (1080p) and `recrop-out` on the next cut | a phone or object beat with no SH-4 / SH-8 close-up (v04 @10.73–11.23, phone in hands) | EDL + `camera` presets |
| **P-11** | Walk-away reveal | the host walking away from camera into the location | 24–45 f; cut to the location's reaction next | HA-16, RE-HOOK | EDL |
| **P-12** | Reaction ending | the winner's biggest reaction, a hug, the host's laugh | 45–90 f; ends on the peak; hard end ≤ 6 f after the last word; a moving handheld celebration wide (the room cheering, the host walking to camera with the stake) may run to 180 f (v03 @67.6–73.5) | END | EDL + T-04 |

**Overlay and state patterns** (engine scenes; family B-3/B-5/B-7)
| ID | Pattern | On screen | Motion recipe | Use | Class · z · needs | Block |
|---|---|---|---|---|---|---|
| **P-20** | **Money tag** | the amount ("$10,000") pinned on the real money/prize | **type-on, left to right:** one glyph every 1.5 f (`$10,000` = 7 glyphs in 10–11 f); each new glyph drops in stretched (scaleY 1.4 → 1.0 over 2 f, from y −20 px) with the glow already on; the caption hides on the first glyph frame; hold 18–66 f; **ends on the cut** (no exit animation). Measured v01 @14.67–15.00 | the stake is shown, opened, handed over | TC-display · z6 · anchor + figure; `payoff: true` in the hook | `VEOS.scene` + built-in `VEOS.fx.typeOn(text, lt, {cps: 20, frames: 2, drop: 0.18, stretch: 0.4})`, `ctx.fmtNum`, `figure`, `anchor` (§17.1) |
| **P-21** | **Gain tag** | "+$3,000" on the person who gains | as P-20; 104 px; x = face centre, y = face bottom + 140 (tag band clamp) | a right answer, a won round | TC-display · z6 · anchor (face) + figure | bespoke scene, `ctx.face()` |
| **P-22** | **Loss tag** | "$0" (or "−$500") in `bad` | stamp: f0–f4 scale 1.4 → 1.0, rotate −6° → 0; shake ±10 px x, seeded, decaying over 8 f; hold 18–42 f; may persist across one cut at the same screen spot when the loser stays on screen (declare the cut in `cuts`) | a wrong answer, a lost stake | TC-display · z6 · figure | bespoke scene, `ctx.rng` |
| **P-23** | **Running total** | one number per person/object that ticks up | E6 container (`data-slot`) at the person's tag spot; on each op the digits roll 8 f to the new value and the number pulses 1.0 → 1.15 → 1.0 over 6 f; re-enters with the P-20 pop when the person returns after a cut away | quizzes, rounds, per-rep money | TC-display · z6 · state + figure + E6 | `VEOS.data.counter` (static spot) or a bespoke scene with `anchor` on the person's track (moving spot) |
| **P-24** | **Countdown clock** | `M:SS` set time, top centre | pop in 5 f on the first value; on every cut hard-swap to that shot's set value (E6, events declared); inside a shot ≥ 1.0 s with a visibly running timer, tick every 30 f; the last 3 values land on consecutive cuts; at `0:00` the fill turns `bad` for 12 f with a 1.0 → 1.12 → 1.0 pulse, then exit 4 f | timed stunts (SH-9) | TC-display · z6 · state (clock) + E6 | bespoke scene |
| **P-25** | **Object glow** | the money/prize lit neon green | radial glow ellipse 1.25× the object box in `good` (opacity 0.75 → 0 at the edge, `mix-blend-mode: screen`) + a 35% `good` tint ellipse (`mix-blend-mode: color`); f0–f3 rise, peak 6–8 f, then a slow decay to ~60% that **ends on the cut** (measured v03 @1.63–2.13, 15 f in all); rides the object's track (`anchor`, §17.2) | the stake's first appearance, HA-16 payoff | none (no text) · z5 · anchor | bespoke scene (engine request: object mask) |
| **P-26** | **Handle chip** | white pill: avatar + `{{BV-01.handle|@yourhandle}}` | grows out of the subject's side in 4 f (0.4 → 1.0, avatar flips in); the underlying caption word fades under it in 2 f; rides the subject (`anchor` on its track) over a 0.5–0.7 s hold; **ends on the cut** (measured v01 @0.80–1.47) | the creator's channel or name is said ("are you subscribed?") | TC-label · z5 · anchor (beside the shoulder: face box side ± 40 px, y face bottom + 20…120, inside y 700–1300) | bespoke scene, BV-16 logo or initials |
| **P-27** | **X flash** | a glowing red X on the wrong answer | **blur-in 6 f** from the first frame after the cut (opacity 0.4 → 1, blur 10 → 0 px, engine preset `blur`); rides the subject's chest (`anchor` on its track); hold 15–24 f; **ends on the cut** (measured v01 @1.52–2.20) | "no", a wrong answer, a refused offer | TC-decorative · z5 · anchor (chest/hand, ≥ 40 px off the face) | bespoke SVG scene |
| **P-28** | **Icon glow** | ✓ (`good`) / ✕ (`bad`) / + (`primary`) 120–160 px on a hand or phone | pop 5 f; glow 20 px; hold 12–24 f; fade 4 f | a tap, a check, an add | none · z5 · anchor | `fx.icon` in a scene |
| **P-29** | **Follow confirm** | the creator's avatar badge Ø 140 (white 8 px ring) above the phone, a ✓ beneath | badge 0 → 1.15 → 1.0 in 6 f; ✓ pops at f4; **P-51 green flash on the same frame**; hold 18 f; exit 5 f | the subject follows/subscribes on camera | none · z5 · anchor (phone track) + GR-green | bespoke scene + built-in `flash` transition |
| **P-30** | **Sponsor logo pop** | the sponsor's own logo file, centred, w 760–900, cy 1000 | a **light** radial haze (`scrim_brand`, white 0.3 at the centre) fades in 3 f; logo scale 0.25 → 0.55 → 0.8 → 1.0 → 1.02 (f0–f4) and keeps growing to 1.04 over the hold; hold 24–52 f; **exits on a cut or a Z-R1 jump of the same take** (v02 @2.33–4.05); disclosure line from the first pop for ≥ 2 s | the product is named or shown in a sponsored reel | image · z8 (captions hide) · insert (creator) + brand | bespoke scene, `ctx.asset` |
| **P-31** | **Brand in type** | the brand or place name set in Montserrat 900 caps | as P-30 without the scrim; 96–128 px | no logo file; a store or place name | TC-display · z8 · insert (created, `logo_plate`) | bespoke scene |
| **P-32** | **URL / link line** | "OLDNAVY.COM"-style line or "LINK IN BIO" | rise 8 f (y +24 → 0, opacity 0 → 1); hold ≥ 45 f; exit 5 f | sponsor URL; `link_bio` CTA | TC-label · z8 | bespoke scene |
| **P-33** | **Hidden-cam HUD** | 4 corner brackets (60×60, 4 px `paper` 85%) at x 64/1016, y 150/1480; "● REC" top-left (40 px, the dot in `bad` blinking 15 f on / 15 f off); a running timecode top-right | hard on with the first hidden-cam shot, hard off with the last | candid / hidden-camera segments only | REC: TC-label; timecode: TC-decorative · z5 | bespoke scene |
| **P-34** | **Ghost replay** | the subject's cut-out at 45% opacity, 160–220 px to the side, replaying their gesture 6 f late | fade in 4 f, 30–45 f, fade out 6 f; ≤ 1 per reel | a funny gesture or dance (comedy light) | none · z9 · matte required | bespoke scene on the cut-out (skip without a matte) |
| **P-35** | **Keyword sticker** | the CTA keyword on a `primary` slab | pop 6 f with rotate −10° → −4°; wobble ±2° for 12 f; hold 1.5–2.5 s; exit 5 f; cy 1180 | `comment_keyword` CTA only | TC-display · z8 · `kind: cta-keyword` | bespoke scene |
| **P-36** | **Name call** | a short shout in yellow beside the shouter's head ("NOLAN!!") | pop 2 f or on with the cut (v04 @2.00); hold 15–24 f; exit on the cut; captions hidden for its span | a shouted name or a one-word call from a small or off-centre speaker | TC-display · z6 · anchor (face side ± 40 px, face top − 20…+80) | bespoke scene |

**Caption patterns** (the auto-caption engine; family B-4)
| ID | Pattern | Recipe | Use | Evidence |
|---|---|---|---|---|
| **P-40** | Neutral word stream | CS-1, 1 word, hard swap, cy 940 | neutral-register reels | v01 0:00–0:35 |
| **P-41** | Comic caps stream | CS-2, 1–5 words revealed word by word, pop 2 f, cy 1000, level | the default register | v02, v04 |
| **P-42** | Money word | CS-2 with the money noun or number in `good` | the stake line | v02 @ 0:01 "UNLIMITED / MONEY" |
| **P-43** | Yellow shout | CS-3, `accent`, −8° | subjects' lines, exclamations | v04 @ 0:02, 0:19, 0:33–0:35; v02 @ 0:18 |
| **P-44** | Pink punch | CS-4, one word | neutral reels, ≤ 2 per reel | v01 @ 0:30–0:31 |
| **P-45** | Captions off | `hide` override | tags, clock, logo, crowd chaos | v03 throughout; v02 @ 0:36–0:47 |

**Footage treatments** (family B-6)
| ID | Pattern | Recipe | Use | Evidence |
|---|---|---|---|---|
| **P-50** | B&W hold | GR-bw (§4.4), 24–45 f, between two cuts | suspense before a verdict | v04 @ 0:06–0:07 |
| **P-51** | Green flash | GR-green (§4.4): built-in `flash` transition, colour `good`, 6–10 f | a yes / confirm / win moment | v04 @ 0:12 |
| **P-52** | Whip-blur cut | T-01 (§9.1) | a jump in place inside the story | v02 @ 21.3–21.6 |
| **P-53** | Zoom-blur punch | T-05 (§9.1) | a beat inside the host's line, into a tighter angle | v02 @ 4.42 |

40 patterns in total (13 cut, 17 overlay/state, 6 caption, 4 treatment).

### 8.4 Line → pattern lookup `[NICHE: example]`
| Line type (what is said or happens) | Primary | Alternates | Niche A example (street giveaway) | Niche B example (fitness challenge) |
|---|---|---|---|---|
| The stake line ("If you X, you win Y") | P-01 + P-41 + P-42 | P-11 (HA-16) | "Name my shop, this ₹5,000 is yours" | "Hold 60 seconds, win $500" |
| The rules | P-05 + P-41 | P-24 starts | "You get one guess" | "Hands off the bar = you're out" |
| The ask to a stranger | P-03 + P-41 (P-40 neutral) | P-26 when the channel is named | "Do you know this shop?" | "Want to try?" |
| A subject's answer | P-03 + P-43 | P-40 | "IT'S SHARMA STORES!" | "LET'S GO!" |
| Wrong / no / lost | P-27 or P-22 + P-03 | P-50 before it | wrong shop name → X | lets go of the bar → "$0" |
| Right / yes / won | P-21 or P-20 + P-03 | P-51 | "+₹500" on the subject | "+$10" per rep |
| Money or prize handed over | P-09 + P-20 | P-06 | envelope into the hand | cash onto the bench |
| The stake revealed (case opens, pile, prize wall) | P-06 + P-20 (or P-25) | P-05 first | the jar of notes glows | the trophy and the cash on the mat |
| The timer starts / the time is called | P-24 | P-41 | "60 seconds, go!" | "Thirty left!" |
| A shouted name or one-word call | P-36 | P-43 | "BHAIYA!!" | "PUSH!!" |
| A phone moment (call, follow, payment) | P-07 + P-28 / P-29 | FB-8 created screen | the subject follows the shop's page | the subject checks their split time |
| The creator's channel or name is said | P-26 | — | "Do you follow {{BV-01.handle|@yourhandle}}?" | same |
| A sponsor is named or shown | P-30 (+ P-32) | P-31 | the sponsor's sweets box | the sponsor's protein tub |
| Escalation ("double it", "but that's not all") | P-05 + P-41 (re-hook) | P-11, P-06 | a second, bigger envelope | the stake doubles to $1,000 |
| A suspense pause | P-50 | P-08 | the subject reads the bill | the last 5 seconds on the bar |
| A silly gesture or dance | P-34 | P-43 | the uncle's victory dance | the celebration flex |
| The crowd reacts | P-04 + P-45 | P-43 on one shout | the shopkeepers cheer | the gym cheers |
| Hidden-camera segment | P-33 | — | the secret shopper aisle | the "fake trainer" prank |
| The ending | P-12 | P-35 (keyword CTA) | the hug at the counter | the winner on the floor laughing |

Third-party patterns and their created substitutes (§12.5): P-30 sponsor logo → P-31 brand in type; P-07 a screen that isn't the creator's → `recreated_ui`.

### 8.5 Data and truth rules
- Every amount on screen is in `plan/figures.json` (§18) with its provenance: the words that said it (`said`) or the creator's stake log (`from: creator`).
- A tag shows **what this object or person is worth right now**: the stack in the hand, the case, the prize's real price. Totals are `sum` figures of their parts.
- No tag on prop or fake money; no "illustrative" money in this style (`illustrative` is never used).
- The clock shows the set time the creator logged or the timer visible in the shot; never invented values.

### 8.6 Comedy layer (`comedy: light`)
- Allowed: P-34 ghost replay (≤ 1 per reel), P-43 shouts, P-36 name calls, P-44 pink punch, and a caption emoticon (":D", ":)") appended to a CS-2/CS-3 chunk when the speaker laughs, ≤ 2 per reel, via `{t, text}` overrides.
- Not allowed: meme sounds, stickers or stamps, freeze-frame roasts, marker scribbles, comedic crash zooms on one face (Z-C1 is for an erupting crowd only).
- Never during the REVEAL or on the final reaction.

### 8.7 Asset rules
- **Real captures only:** every frame of people, money and prizes is the creator's footage.
- **Created graphics** are only the B-3/B-6/B-7 engine graphics, the brand-in-type plate (P-31) and, in the fallback, a generic phone screen (FB-8).
- **Logos:** a sponsor's logo appears only as the file the creator supplies (they hold the rights through the deal); otherwise the brand is set in type (P-31). Never fetched.
- **Third-party material** follows the ask-then-create flow (§12.5).

### 8.8 Density and variety
- Overlay events (tags, chips, X, clock swaps, logo pops) every 3–8 s on average; ≥ 1 per stake beat.
- ≥ 6 distinct patterns per 60 s; the same overlay pattern ≤ 3 beats in a row, except P-23/P-24 rituals.
- ≤ 2 overlay elements at once besides captions (3 tags only in a multi-object reveal, captions hidden).

---

## §9 Transitions & shot grammar `[REQ] [DNA]`

### 9.1 Library
| ID | Transition | Frames | Recipe | Cue role |
|---|---|---|---|---|
| **T-00** | **Hard cut** | 0 | ≈ 95% of all boundaries (measured: 2 blur transitions in 150 changes); on a word boundary ±1 f, or on the action frame | silent |
| **T-01** | **Whip blur** | 4 + 2 + 3 | measured v02 @21.3: the outgoing shot smears horizontally over 4 f (blur 0 → ~60 px at 1080 w, content sliding right), 2 f where both shots blend ~50/50, then the incoming smear clears over 3 f. **Built-in:** `{"t": <cut>, "type": "whip", "dir": "right", "px": 60, "frames": 9, "pre": 4, "blend": 2}` in `timeline.transitions` (core draws the directional smear, the travel and the 2 f cross-blend on the picture, under the captions) | whoosh allowed |
| **T-05** | **Zoom-blur punch** | 0 + 4 | measured v02 @4.42: on the cut a radial blur peaks on the incoming shot (a ~1.3× tighter angle of the host) and clears over 4 f; captions stay sharp on top. **Built-in:** cut to the tighter real angle (or `recrop-in` 1.25) and declare `{"t": <cut>, "type": "zoom-blur", "pre": 0, "frames": 4, "amount": 0.15, "punch": 0, "at": "face"}` (radial blur peaks on the cut and clears in 4 f; `punch: 0` because the tighter angle is the real cut, not a scale) | whoosh allowed |
| **T-02** | **Match cut on action** | 0 | P-09: the motion continues across the cut within ±2 f | silent |
| **T-03** | **Band cut** | 0 | `stage` switch to/from L-wide-band on a cut (`via: cut`) | silent |
| **T-04** | **Hard end** | 0 | the last frame is the peak of the last reaction; ≤ 6 f after the last word; no fade, no black tail | silent |

### 9.2 Grammar
| Boundary | Use | Never |
|---|---|---|
| Frame 0 | nothing: the reel starts mid-shot | a fade-in, a black frame, a logo |
| Cold open → setup | T-00 | T-01 |
| Inside a sentence (synced angles) | T-00 (R-08) | T-01 |
| Verdict → reaction | T-00 within 6 f (R-03) | T-01, T-02 |
| Handover | T-02 | — |
| A jump in place or time (store → car, day → night) | T-01 (≤ 1 per 15 s) | crossfade, wipe |
| A beat inside the host's pitch, cutting tighter on the same set | T-05 (≤ 1 per reel) | T-01 |
| A sponsor logo leaving, or GR-bw starting, on the same take | Z-R1 jump (no frames removed) | a cut to another source |
| Into/out of a horizontal wide | T-03 | a morph |
| Last frame | T-04 | outro, end card, fade |

### 9.3 Shot grammar
| ID | Rule |
|---|---|
| **R-01** | First cut by 2.1 s, on a word boundary inside the stake sentence. |
| **R-02** | One meaning per shot: cut as soon as the action's peak has passed; never hold to "breathe". |
| **R-03** | Every verdict, reveal and handover is followed within 6 f by the face that won or lost, held 0.6–1.2 s. |
| **R-04** | Never two shots of the same person in a row unless the second is ≥ 1.4× tighter (P-08); alternate host ↔ subject ↔ crowd. |
| **R-05** | A reveal of scale (the pile, the room, the prize wall) gets a 0.8–1.5 s wide first. |
| **R-06** | The stake word is the cut point to the stake insert (±2 f). |
| **R-07** | Emphasis = a cut to a tighter **real** angle (P-08); a jump re-crop (P-10) marks a logo exit or GR-bw; pushes belong to reactions (Z-P1) and crash zooms to crowds (Z-C1), never to the host's talking lines. |
| **R-08** | Inside a sync group, angle switches keep the session time; a sentence may run across up to 4 cuts. |
| **R-09** | Money or prizes changing hands are match-cut on the motion (P-09). |
| **R-10** | When a subject starts to speak, cut to them on their first word (±3 f). |
| **R-11** | Shot length 0.4–2.5 s (measured median 1.10 s, p90 2.13 s); up to 4.5 s only for a group shot carrying ≥ 2 events (tags typing on, caption changes: v01 @12.6–17.13), up to 6 s for a moving end wide (P-12). |
| **R-12** | End on the peak of the last reaction, then T-04. |

### 9.4 Budget (per 60 s)
- T-00: 30–48 (the DNA cut rate). T-01 + T-05: ≤ 3 per reel, never two within 10 s (evidence: 2 in v02, 0 in v01/v03/v04). T-02: 2–4. T-03: ≤ 3 per reel.
- Colour events: ≤ 2 per reel (§4.4). Camera (§10.2): 3–7 events per 60 s; Z-R1 ≤ 1 per 10 s, Z-P1 ≤ 1 per 10 s, Z-C1 ≤ 2 per reel.

---

## §10 Motion, camera, layers, finishing `[REQ] [DNA; motion tokens TUNE ±15%]`

### 10.1 Motion tokens (30 fps)
| Token | Value |
|---|---|
| Lead | 1 f before the trigger word or on the action frame |
| Entries (measured) | money tags **type-on** 1.5 f per glyph (P-20); chip 4 f grow (0.4 → 1.0); logo 4 f (0.25 → 1.02 → 1.0, ease `cubic-bezier(0.34, 1.56, 0.64, 1)`); X flash blur-in 6 f; object glow rise 3 f; sticker 6 f |
| Exit | **the default exit is the next hard cut** (tags, chip, X, logo, glow all measured ending on a cut); an exit animation, when the shot continues, is ease `cubic-bezier(0.64, 0, 0.78, 0)` 4 f |
| Caption swap | CS-1 hard; CS-2/3/4 word pop 2 f (0.5 → 1.05 → 1.0) |
| Number roll (P-23) | 8 f, then a 6 f pulse 1.0 → 1.15 → 1.0 |
| Loss shake | ±10 px x, 8 f, seeded, decaying |
| Glow pulse | intensity 1.0 → 1.25 → 1.0 over 6 f after a tag lands |
| Flash | GR-green 6–10 f; X flash ≤ 15 f |
| Hold | text ≥ 0.13 s per word (CS-1) and 0.15 s (CS-2); tags ≥ 18 f; logos ≥ 24 f |
| Anchor follow | the object's `veos track` track (`anchor`, smooth 2 f); anchored scenes are exempt from G3 (the motion is the object's) |

### 10.2 Footage camera: `zoom_policy: presets`
Measured with ORB + `estimateAffinePartial2D` frame by frame (strips in `docs/audit/stunt-compression/`).

| ID | Preset | Recipe | Use | Evidence |
|---|---|---|---|---|
| **Z-R1** | `recrop-in` | scale 1.0 → 1.13–1.20 in 1 f (no rotation), held to the next cut (≤ 1.35× on 1080p, ≤ 2.0× on 4K; P-13 detail insert up to 2.0×) | a jump on the same take: the sponsor logo leaves, GR-bw starts; FB-2/FB-3 | v02 @4.05 (1.20×), v04 @6.40 (1.135×), v04 @10.73 (≈ 2.5× detail) |
| **Z-R2** | `recrop-out` | back to 1.0 in 1 f on the next cut | always follows Z-R1 / Z-P1 / Z-C1 | — |
| **Z-P1** | `reaction-push` | 1.0 → 1.15 over 15 f, ease-out (peak rate ~1.8% per frame on f5–f8), no rotation; holds to the cut | the biggest reaction of a stake beat (shock, hand over mouth), from the cut or the gesture; ≤ 1 per 10 s | v01 @20.40–20.87 (1.17× in 14 f), v01 @1.48–2.05 (1.14× in 17 f) |
| **Z-C1** | `crash-zoom` | 1.0 → 1.6 over 24 f, ease-out (≈ 5–6% per frame on f1–f4, then decaying), **radial** motion blur on the fast frames (built-in: the preset's `blur {kind: "radial", amount: 0.18, at: "face", frames: 6, shape: "decay"}` in `tokens.json`, drawn by core on the stage only; captions and tags stay sharp); holds to the cut | a crowd or class erupting, from its first frame; ≤ 2 per reel | v03 @7.27–8.17 (1.72× in 27 f) |

No Ken Burns, no slow drifts on wides, no shakes and no rotation; the host's talking lines are never zoomed (handheld walk-and-talk motion is the camera there). Never the same Z twice in a row; never two camera entries within 0.4 s (NC-3). Camera moves never move captions (they are screen space), as in the evidence.

### 10.3 Canvas camera
OFF (see §21).

### 10.4 Layer order (back to front)
| z | Layer |
|---|---|
| 1 | W-band blurred copy (L-wide-band only) |
| 4 | footage (the stage) |
| 5 | object glow (P-25), handle chip (P-26), X flash (P-27), icons (P-28/P-29), hidden-cam HUD (P-33) |
| 6 | money/loss tags and totals (P-20…P-23), clock (P-24), name calls (P-36), disclosure line |
| 7 | auto-captions CS-1…CS-4 |
| 8 | sponsor logo pop (P-30), brand in type (P-31), URL line (P-32), keyword sticker (P-35): captions hide under them |
| 9 | ghost replay (P-34) |
| 11 | light passes: GR-bw (z11 saturation scene). GR-green / P-51, T-01 whip and T-05 zoom blur are **built-in transitions** drawn by core over the picture (world, footage, z1–6), under the captions: no scene |

### 10.5 Finishing
No grain, no vignette, no bloom, no LUT. Glow exists only on tags (P-20…P-23), the X flash and the object glow. Strokes are hard (5–9 px) and shadows are hard offsets (`0 6 0`, `0 7 0`); only the neutral captions and the legal line use a soft shadow.

---

## §11 Sound contract (minimal) `[REQ] [VAR]`
| Line | Decision |
|---|---|
| **Cue moments** | `hook` (the f0 caption pop and the payoff tag), `reveals` (money/loss tags landing, the X flash, logo pops, the clock's first value and 0:00, the green flash), `transitions` (T-01 whip and T-05 zoom blur: whoosh category; a Z-C1 crash zoom may take one riser-hit). Caption pops, cuts, re-crops and total ticks are silent. |
| **Meme cues** | off (`comedy: light`) |
| **Music bed** | on, from f0, under the dialogue |
| **Ducking** | the bed sits ≥ 20 dB under speech while anyone speaks (`duck_db: -20`); the source audio (crowd, room, the subjects' reactions) is kept and is the loudest thing after speech: never mute a cheer |
| **Loudness** | −14 LUFS integrated, true peak ≤ −1.5 dBTP; hard end ≤ 6 f after the last word (NC-8) |

Mirrored in `tokens.json → sound`. The SFX pack and its global rules (S1–S6) choose the sounds.

---

## §12 Footage requirements, shot list, fallbacks, inserts `[REQ]`

**Footage dependency: total.** This style cannot be made from a talking head, a voice-over or stock: it is the compression of a real event the creator stages and films. The template card says: *needs: a real stunt filmed on 2+ cameras (you, the people taking part, the prize)*. When the footage is missing, the fallbacks below say what degrades; if the stake itself was never filmed and no one reacts on camera, the reel cannot be made in this style (tell the creator at P12).

### 12.0 The shoot brief (send this to the creator before the shoot)
1. **Stage a real stake.** Real money or real prizes, physically present, visible to camera; know the exact amounts. Prop or fake money is never tagged with an amount.
2. **Two vertical cameras minimum** (phones are fine): A follows you, B stays on the people taking part. A third (C) on a tripod for the wide is better. Shoot 9:16 vertical, **4K at 30 or 60 fps**, daylight or bright light.
3. **Mic everyone who matters:** a lav on you and one on the main participant; start every camera and recorder, then clap once on camera (sync point).
4. **Open walking and talking.** Start each take already moving toward the participant and saying the stake line ("If you can … this ₹5,000 is yours"). Do it 3 times.
5. **Film every reveal from two angles at once:** A on you, B on their face, never stopping between the reveal and the reaction.
6. **Film the stake up close** for 3–5 s each: the envelope opening, the stack in a hand, the pile, the prize boxes.
7. **Get a wide of everything** at least once per location: the whole crowd, the whole pile, the whole room.
8. **Timed challenge?** Put a visible timer on set or call the time out loud, and write down the clock value of every take ("take 7: 0:49 left").
9. **Phone moments** (a call, a follow, a payment): screen-record your phone; with the participant's consent, theirs.
10. **Let it run.** Do not cut the camera after the reaction; the hug, the jump and the friend screaming are the reel.
11. **Shoot 10×.** About 10 minutes of usable footage per minute of final reel, at least 40 distinct moments.
12. **Write the stake log** after the shoot: who got what, every amount, every clock value, the sponsor and its URL. The editor tags only what is in it.

### 12.1 Setups `[DNA what the style assumes; VAR the buyer's actual setups]`
| ID | Camera | Spec | Framing |
|---|---|---|---|
| **A** | Host camera | vertical handheld or gimbal, 4K 30/60, follows the host; the host's lav may show | host face 18–30% of frame height, head top y 120–420 |
| **B** | Subject camera | second vertical 4K camera on the participants' faces and hands | face 20–35% of frame height for reactions, head top y 140–520 |
| **C** | Wide / set | tripod or high handheld, vertical preferred; horizontal accepted (goes to L-wide-band) | the whole set; heads y 300–900 |
| **D** | Phone screen | the creator's phone screen recording (or a participant's, with consent) | full screen |
Wardrobe: the host in one plain, saturated tee across the whole shoot (continuity between cuts); no logos the creator doesn't own on the host.

### 12.2 Shot list
| ID | Shot | Spec | Count per 60 s | Must / optional | Formats |
|---|---|---|---|---|---|
| **SH-1** | Cold-open walk-and-talk | A: the host already moving and speaking the stake line, 3 takes | 1 | **must** | F-A |
| **SH-2** | Subject close-up reactions | B: face + hands; at least 3 per subject who wins or loses | 8–16 clips of 0.6–1.2 s | **must** | F-A |
| **SH-3** | Host two-shot with the subject | A or B, medium: the ask, the offer, the handover | 6–12 | **must** | F-A |
| **SH-4** | The stake as an object | A/B macro: the envelope/case opening, the stack, the pile, the prizes | 3–6 of 0.5–1.5 s | **must** | F-A |
| **SH-5** | Wide establish | C: the set, the crowd, the reveal of the room or pile | 2–5 | **must** | F-A |
| **SH-6** | The reveal from two angles at once | A on the host + B on the subject, synced by sound | 1–3 | **must** | F-A |
| **SH-7** | Bystander / crowd reactions | B or C: friends, passers-by, the room | 2–6 | optional | F-A |
| **SH-8** | Phone screen recording | D: the call, the follow tap, the payment | 0–2 | optional | F-A |
| **SH-9** | The time limit on set | a visible timer or the host calling the time; clock values logged | 0–1 run | optional (timed stunts: must) | F-A |
| **SH-10** | The ending reaction | the winner's biggest reaction, a hug or the host's laugh, held 1.5–3 s | 1 | **must** | F-A |

### 12.3 Fallbacks
| ID | For | What the engine does instead | Fidelity cost | Result |
|---|---|---|---|---|
| **FB-1** | SH-1 | open on the strongest SH-6 reveal (HA-16 or HA-14) and move the stake line to 2–4 s | no walk-in energy; the hook reads as a highlight | degraded |
| **FB-2** | SH-2 | re-crop the subject's face from SH-3 or SH-5 (P-10: ≤ 1.35× on 1080p, ≤ 2.0× on 4K) on each reaction cut | softer reactions with the two-shot's eye-line | degraded |
| **FB-3** | SH-3 | two crops of the wide (SH-5) for the host and the subject | flat angles; a slower read of who speaks | degraded |
| **FB-4** | SH-4 | pin the tag on the recipient's chest at the handover (P-21) and hold the two-shot 0.3 s longer; never a created picture of money | the money is named, not shown: the money-literal DNA weakens | degraded |
| **FB-5** | SH-5 | the widest A/B frame as the establish; a horizontal C clip in L-wide-band | less sense of scale | holds |
| **FB-6** | SH-6 | single-angle reveal: hold A on the reveal, then cut to the subject's next reaction from B, even 1–3 s late | no simultaneous host + subject reveal | degraded |
| **FB-7** | SH-7 | a second subject reaction (SH-2) instead | less social proof | holds |
| **FB-8** | SH-8 | film the phone over the shoulder (SH-3 angle) with P-28; if the creator says the call happened and has no recording, a generic phone screen built with `fx.appUI` (the words from the transcript) | less intimacy; a created screen is labelled | holds |
| **FB-9** | SH-9 | no clock: time pressure is carried by the captions only | P-24 is off for the reel | holds |
| **FB-10** | SH-10 | end on the last SH-2 reaction or the stake insert (P-06) | a weaker button | holds |
At P12 the checkpoint lists every fallback used and its cost.

### 12.4 Props, reaction bank, matte, resolution
- **Props:** the stake in clear view (cash in visible stacks or an open case, gift cards, prize boxes); a timer for timed stunts; the sponsor's product only in sponsored reels.
- **Reaction bank (P5b):** per winning or losing subject: shock (hand over mouth), hands on head, jump, hug; the host: laugh to camera, point, shrug; the crowd: a cheering wide, one friend's face.
- **Matte:** optional, only for P-34 ghost replay.
- **Minimum source resolution for crops:** a 2× re-crop needs a 2160 px-wide (4K) source; a 1080p source allows ≤ 1.35×. Horizontal 1080p wides go to L-wide-band, never cropped to 9:16.

### 12.5 Third-party inserts: ask, then create `[REQ always]`
Claude never fetches anyone else's media. In stunt reels the third-party moments are usually:
| Moment | Ask the creator for | If supplied | If not supplied: Claude creates |
|---|---|---|---|
| A sponsor or a store is named | the logo file (they hold it through the deal) | P-30 logo pop (origin `creator`) | P-31 brand in type (`logo_plate`, origin `created`) |
| A call, chat or app on someone's phone | the screen recording | P-07 phone-screen cut | over-the-shoulder SH-3 + P-28; else `fx.appUI` generic screen |
| Another creator's video or post is referenced | the clip or screenshot they own or were given | full-frame ≤ 2 s | `fx.quoteCard` (verbatim words) or `fx.appUI({kind: "video"})` |
| A famous person is named | a photo they own | framed still ≤ 1.5 s | `fx.silhouette` with the name |
Flow: (1) `veos inserts scan` after P3; (2) ask once, as one short list ("For these N moments, do you have a file? Drop it or say no"); (3) use what is supplied as given; (4) create the rest; (5) record every one in `plan/inserts.json` `{id, moment, origin, file?, substitute_of?}`. 

### 12.6 Frame rate and audio
- Output 1080×1920, 30 fps CFR; 60 fps sources are conformed to 30 (no slow motion in this style).
- Dialogue chain per lav (high-pass 80 Hz, de-ess, light compression); camera audio is used for crowd and reactions; −14 LUFS.

---

## §13 Output contract `[REQ] [DNA]`

### 13.1 Core beat fields
`id`, `section` (COLD OPEN | SETUP | ESCALATION | REHOOK | REVEAL | END), `t0`/`t1`, `spoken`, `trigger {word | action, at}`, `tone`, `line_type`, `layout`, `visual` (one sentence), `layers` (scene ids), `pattern`, `sfx`.

### 13.2 Conditional fields used by this style
| Switch / module | Fields |
|---|---|
| captions (always) | `caption {mode: comic \| shout \| neutral \| punch \| none, profile: CS-1…CS-4 \| null, overrides[], emphasis[]}` |
| stunt footage (always) | `moment` (`plan/moments.json` id), `src`, `angle` (A/B/C/D), `cut_reason` (open \| angle \| reaction \| reveal \| handover \| establish \| insert \| end) |
| running_state | `state_ops [{var, op: set \| add \| tick_to, value, at}]` |
| anchors | `anchor {target: object:<label> \| person:<id> \| face, follow: none \| track, track?: <plan/tracks id>, offset, lost: hold \| fade}` (the scene's own `anchor` field, SCENES-API §13) |
| data_figures | `figure_id` |
| grades | `grade` (GR-bw \| GR-green \| null) |
| footage ≥ medium | `shot_id` (SH-…), `fallback_used` (FB-… or null) |
| brand | `sponsor {id, disclosure}` |
| third-party moment | `insert {id, origin}` |
| exception | `exception: E6` (clock, total, CS-1) |

### 13.3 Reel header
```yaml
reel:
  format: F-A
  hook_archetype: HA-13            # HA-13 | HA-14 | HA-16
  structure: stunt
  register: comic                  # comic | neutral | action  -> captions.profile CS-2 | CS-1 | CS-2 + hides
  stake: {currency: "$", items: ["case-1 $10,000", "case-2 $10,000"], total_given: 20000}
  state: {total: {start: 0}, clock: {from: "1:00", values_from: "stake log"}}
  figures: plan/figures.json
  cast: {host: "{{BV-01.name|the creator}}", subjects: ["subject-1", "subject-2"]}
  sponsor: null                    # or {name, logo: "plan/assets/<file>", url, disclosure: "Paid partnership"}
  cta: none
  duration_target_s: [40, 75]
```

### 13.4 Hook proposals (3)
```yaml
- name: "Walk-in offer"
  archetype: HA-13
  stake_line: "If you can name my shop, this ₹5,000 is yours"
  hook_pair: {topic: "name my shop", first_subject: "host walking up the lane, envelope in hand", reveal: "envelope opens + P-20 ₹5,000 at 2.1 s"}
  captions: {register: comic, chunks: ["IF YOU CAN", "NAME MY SHOP", "THIS ₹5,000", "IS YOURS"]}
  storyboard: "f0 walk + CS-2 | 1.4 cut to B on the stranger | 2.1 envelope insert + tag (payoff) | 2.7 stranger's reaction CS-3"
  sound: [hit on the f0 caption pop, reveal cue on the tag]
  stopper: {mute: pass, motion_f0: pass, sc_3s: 6.5, payoff_s: 2.1}
```

### 13.5 Checkpoint (send, then wait for approval)
1. The 3 hook proposals with their stopper results.
2. The arc table with target seconds and the moment count per kind (vs the §1.2 quotas); the shoot-to-reel ratio.
3. The beat sheet with caption modes, tones, patterns, state ops and anchors.
4. `plan/figures.json` summary: every amount shown, its provenance, every total recomputed; the clock values and their source.
5. The transition map and the cue moments.
6. The inserts record (creator-supplied vs created) and the sponsor/disclosure plan.
7. The fallbacks used and their cost.
8. Style stills: f0, the payoff frame, one stake beat (verdict + reaction), the re-hook, a clock frame (if timed), the last frame.

**Wait for approval.**

---

## §14 Worked examples `[REQ] [NICHE: example]`
Times are planning estimates: replace them with the real word onsets and action frames. Each example is one complete plan; the buyer's first approved reel replaces the matching example (Part D.6).

### 14.1 Street giveaway, comic register, ₹ (niche A: a local-business / street creator, Hinglish)
**Reel:** "Meri shop ka naam batao, ₹5,000 jeeto" · 45 s · HA-13 · register comic (CS-2, Hinglish Latin caps) · numbers Indian ₹ · CTA none.
**Stake log:** stake 1 = ₹5,000 (envelope 1); re-hook stake = ₹10,000 (envelope 2); given: ₹10,000 to subject 3.

**Hook (0–3.2 s)**
| t (s) | Visual | Caption | Graphics / state | Cue moment |
|---|---|---|---|---|
| f0 | P-01: host walking down the market lane toward camera, envelope in hand, mid-word | CS-2 "AGAR TUM" on screen from f0 | — | hit on the f0 pop |
| 0.45 | same shot | "MERI SHOP KA" | — | — |
| 0.95 | same shot | "NAAM BATA DO" | — | — |
| **1.40** | P-02: cut to camera B, a student turning toward the host (same sentence) | "TOH YE" | — | — |
| **1.85** | P-06: the envelope opened by the host's thumb, the notes fanned | hidden | **P-20 "₹5,000"** on the notes, `figure: stake_1`, **`payoff: true`** | reveal cue |
| 2.55 | P-03: the student's face, eyebrows up | CS-3 "SACH MEIN?!" | `state_ops: stake set 5000` | — |
Change count 0–3 s: 3 cuts + 4 chunks × 0.5 + 1 tag + 1 shout chunk × 0.5 = 6.5.

**Section plan**
| Section (s) | Beats | Patterns | Caption mode |
|---|---|---|---|
| SETUP 3.2–7.4 | the host hides the shop board behind him; "ek guess, bas" | P-05 wide of the lane (1.2 s) → P-03 → P-26 handle chip on "mera page follow karte ho?" (0.7 s) | CS-2; hidden under the chip |
| ESCALATION 7.4–21.5 | stake beat 1: the student guesses wrong | P-03 (answer) → **P-27 X** on his chest → P-04 his friends laughing | CS-3 for his guess; hidden for the X |
| | stake beat 2: an aunty guesses wrong | P-03 → **P-50 B&W hold** 1.0 s while she thinks → P-22 **"₹0"** with shake → P-03 her laugh | CS-3 / hidden / none |
| RE-HOOK 21.5–25.0 (48–56%) | "Theek hai… ab ₹10,000!" a second envelope | P-08 tighter on the host → **P-06 + P-20 "₹10,000"** (`state_ops: stake set 10000`) → P-04 the lane reacts | CS-2 with "₹10,000" in `good` (P-42) |
| ESCALATION 25.0–31.0 | a delivery rider stops; the host asks | P-03 (his face) → P-08 (tighter on the host's question) → P-03 his grin; no second B&W hold (GR-bw was used at stake beat 2) | CS-2 / CS-3 |
| REVEAL 31.0–41.5 | he names the shop correctly | P-03 (his answer, CS-3 "SHARMA GENERAL STORE!") → **P-51 green flash** → **P-09 match cut** on the envelope into his hand → **P-20 "₹10,000"** on it (`state_ops: total add 10000`) → P-03 his shock → P-04 the shopkeepers cheer → P-34 ghost replay of his little dance (only with a matte) | CS-3 / hidden / hidden |
| END 41.5–45.0 | the rider hugs the host | **P-12** (2.6 s), hard end on the peak | none |

**State and figures:** `stake` set 5000 at 1.85, set 10000 at 22.6; `total` add 10000 at 34.9. `plan/figures.json`: inputs `stake_1` (5000, `said: "₹5,000"`), `stake_2` (10000, `said: "₹10,000"`); figure `given` = `sum([stake_2])` shown at 34.9. Format `₹10,000` (Indian grouping).
**Cut count:** 38 cuts in 45 s = 50.7/min → trim two weak reactions in ESCALATION to land at ≤ 47/min (36 cuts); median shot 1.2 s.

### 14.2 Timed fitness challenge, comic register, $ (niche B: a fitness coach / gym creator)
**Reel:** "Hang on this bar for 60 seconds, win $500" · 56 s · HA-13 · register comic · clock on (SH-9 logged) · CTA `comment_keyword` "HANG" (example of a chosen CTA).
**Stake log:** rule: $50 for every 10 s held; 60 s = $500. Subject 1 drops at 0:31 left → held 29 s → $100; subject 2 drops at 0:12 left → held 48 s → $200; subject 3 holds to 0:00 → $500, and the host doubles it at the re-hook → $1,000.

**Hook (0–3 s)**
| t | Visual | Caption | Graphics / state | Cue |
|---|---|---|---|---|
| f0 | P-01: host walking across the gym floor with a cash stack, talking to camera | CS-2 "HANG ON THIS BAR" | — | hit on the pop |
| 0.80 | same | "FOR 60 SECONDS" | — | — |
| **1.30** | P-02: cut to C, the pull-up bar with three people waiting | "AND WIN" | — | — |
| **1.75** | P-06: the cash stack fanned on the bench | hidden | **P-20 "$500"**, `payoff: true` | reveal cue |
| 2.35 | P-03: subject 1 grinning, chalking hands | CS-3 "EASY!" | — | — |

**Section plan**
| Section (s) | Beats | Patterns | Caption mode |
|---|---|---|---|
| SETUP 3.0–7.5 | the rule: $50 every 10 s | P-05 wide → P-08 host close → P-24 **clock "1:00" pops** (`state_ops: clock set 60`) | CS-2 "$50 EVERY 10 SECONDS" with the number in `good`; the clock then hides captions |
| ESCALATION 7.5–26.0 | subject 1 hangs: clock cuts 0:52 → 0:44 → 0:37 → 0:31 (one value per shot, E6) | P-03 face strain / hands close-up / P-04 friends; at the drop he has still earned money, so **P-21 "+$100"** on his chest (gain, not loss) | hidden while the clock runs; CS-3 "MY ARMS!!" |
| | subject 2 hangs: clock 0:58 → 0:40 → 0:21 → 0:12 | P-03 / P-08 / P-03; drop → P-21 "+$200" | hidden / CS-3 |
| RE-HOOK 26.0–31.5 (46–56%) | host: "Last one. Make it to zero and I double it." | P-08 host → **P-06 a second stack + P-20 "$1,000"** (`stake set 1000`) → P-04 the gym "OHHH" | CS-2 with "$1,000" in `good` |
| REVEAL 31.5–50.5 | subject 3 hangs; the clock runs 0:60 → 0:45 → 0:30 → 0:15 → **0:03 → 0:02 → 0:01** on consecutive ~0.8 s cuts → **0:00 turns red** | P-24 + P-03 / P-08 / P-04 alternating; **P-50 B&W hold** at 0:05 for 1.0 s (the only one); 0:00 → **P-51 green flash** → P-09 the stack into her hands → **P-20 "$1,000"** → P-03 her scream | hidden during the clock; CS-3 "LET'S GOOO!" after |
| END 50.5–56.0 | she drops to the floor laughing; host high-fives | P-12 (2.0 s) + **P-35 keyword sticker "HANG"** for 2.0 s over the last shot, spoken "comment HANG and I'll come to your gym" | none + sticker |

**State and figures:** `clock` values come from the stake log, one per shot, down only (`state_ops: clock tick_to <value>` on each clock cut). Inputs: `rate` (50, `said: "$50 every 10 seconds"`), `paid_s1` (100, `from: creator`, the log says 29 s held), `paid_s2` (200, `from: creator`, 48 s held), `stake_base` (500, `said: "$500"`), `stake_bonus` (500, `said: "I double it"`). Figures: `s1` and `s2` with `formula: none` (stated values), `final` = `sum([stake_base, stake_bonus])` = 1,000, shown at 47.6 s. The planner never computes "held seconds × rate" on screen: the creator's log is the provenance of each payout.
**Cadence:** 44 cuts in 56 s = 47/min (the top of the range; the clock run is the fastest stretch); median 1.1 s.

### 14.3 Sponsored group quiz, action register, $ (an education / workplace creator; brand module)
**Reel:** "Every right answer = +$500 for your teacher" · 66 s · HA-16 (the host holds the stake; no stake line at f0) · register action · sponsor: a stationery brand (logo file supplied) · CTA none.

**Hook (0–3 s)**
| t | Visual | Caption | Graphics / state | Cue |
|---|---|---|---|---|
| f0 | host in the corridor holding a bucket of cash stacks toward camera, talking | hidden (his first words are not the stake) | — | — |
| **1.65** | same shot, he lifts one stack | — | **P-25 object glow** on the stack, `payoff: true` | reveal cue |
| **2.10** | P-11: cut to him walking away into the classroom | — | — | — |
| 2.90 | P-04: the class sees him, screams | CS-3 "NO WAY!" | — | — |

**Section plan**
| Section (s) | Beats | Patterns | Caption mode |
|---|---|---|---|
| SETUP 3.0–9.5 | the rule on the classroom TV ("every question you get right = +$500 for your teacher") | P-05 wide with the TV readable → **P-30 sponsor logo pop** on "this quiz is brought to you by …" (1.0 s) + disclosure "Paid partnership" (2.0 s) → P-03 the teacher's face | CS-2 for the host's rule; hidden under the logo |
| ESCALATION 9.5–36.0 | 5 questions, each a stake beat: the question on the TV (P-05) → a kid answers (P-03, CS-3) → right: **P-23 total on the teacher** ticks +$500 (rolls 8 f) → the teacher reacts (P-03) | P-23 ticks: $500 → $1,000 → $1,500 (one wrong answer: **P-27 X**, no tick) → $2,000 | action register: hidden except kids' shouts (CS-3) |
| RE-HOOK 36.0–42.0 (55–64%) | "And everyone in this class gets a prize" — a red cloth over a table | P-08 host → P-06 the cloth pulled → P-05 the prize table → **P-31 brand in type** (the store's name) + **P-32 URL line** (1.5 s) | CS-2 for the host line; hidden under the brand |
| REVEAL 42.0–62.5 | handing out prizes; the teacher's final total | P-09 handovers ×4, P-20 price tags on two prizes ("$250"), P-03 / P-04 alternating, the teacher's **P-23 "$2,500"** final tick on the last answer, **P-51 green flash** on her total | hidden; CS-3 on two shouts |
| END 62.5–66.0 | the host laughing to camera with the last cash stack | P-12 (2.2 s) | none |

**State and figures:** `total` (teacher) add 500 per right answer at each tick (`sum` figure with steps `[500, 1000, 1500, 2000, 2500]`, each step's `args.values` listing the answers so far). Prize tags `$250` from the stake log (`from: creator`). Sponsor: `sponsor {id: "brand-1", disclosure: "Paid partnership"}` on every brand beat; `plan/inserts.json` records the logo (origin `creator`) and the store name in type (origin `created`, `logo_plate`).
**Cadence:** 52 cuts in 66 s = 47.3/min; median 1.04 s (matches v03).

---

## §15 QA checklist `[REQ] [DNA]`

**1. Profile conformance**
- [ ] Format F-A; layouts only L-full (≥ 90%) and L-wide-band (≤ 10%, ≤ 2.0 s per use). (V-LAYOUT)
- [ ] A face ≥ 6% of frame height on ≥ 60% of runtime; no face-less run > 3.0 s. (V-PRESENCE)
- [ ] Duration inside 40–75 s; one re-hook at 45–65%. (V-REHOOK)

**2. Hook**
- [ ] f0: moving footage + a caption chunk on screen (HA-13/HA-14), or a moving subject (HA-16); no headline, logo or black frame. (V-F0)
- [ ] First cut by 2.1 s; the `payoff: true` scene by 2.3 s; ≥ 5 weighted SCs in 0–3 s. (V-F0, V-CADENCE)
- [ ] The stake line's number equals the tag's number. (V-DATA)

**3. Body and cadence**
- [ ] 30–48 cuts/min; median shot 1.0–1.3 s; SC 5–14 per 10 s; no weight-1 gap > 2.5 s. (V-CADENCE)
- [ ] Every verdict/reveal/handover is followed within 6 f by the reacting face (R-03). (review)
- [ ] ≈ 95% hard cuts; T-01 + T-05 ≤ 3 per reel; camera only Z-R1/R2, Z-P1 (reactions), Z-C1 (crowds), 3–7 per 60 s; overlays end on cuts. (V-CAMERA, review)
- [ ] The reel ends on a reaction peak, ≤ 6 f after the last word; no outro. (V-PROMISE)

**4. Captions**
- [ ] One register per reel; every beat's mode declared; overrides only (no hand-written cards). (V-CAPTION)
- [ ] Hidden while a tag, logo pop, brand type, name call or GR-bw is on screen. (review + G1)
- [ ] CS-1 ≥ 54 px, CS-2 ≥ 84 px, CS-3 ≥ 96 px; ink strokes present; ≤ 4 words per chunk (1 in CS-1). (V-TYPE, V-CAPTION)
- [ ] Yellow only on subjects' lines and exclamations; green only on the money word; pink ≤ 2 per neutral reel. (review)
- [ ] Captions ≤ 0.15 s ahead of the word; brand and name spelling exact. (V-CAPTION)

**5. Modules**
- [ ] *running_state:* totals equal the sum of their ops; the clock only goes down, changes only on cuts (or visible ticks), turns red at 0:00. (V-STATE pending → review)
- [ ] *anchors:* every tag sits on its object or person at t_in, ≥ 40 px off any face, rides its `veos track` track when the object moves (preview checked, lost share ≤ 0.2). (V-ANCHOR, V-FACE)
- [ ] *data_figures:* every amount is in `plan/figures.json` with provenance; `veos figures` shows no mismatch. (V-DATA, V-NUMFMT)
- [ ] *brand:* every sponsor beat has the disclosure ≥ 2 s; ≤ 3 logo pops; logos only from creator files. (V-PROMISE, V-INSERTS)

**6. Truth and inserts**
- [ ] No tag on fake or prop money; every amount was really given, won or stated. (V-DATA, review)
- [ ] Every third-party moment recorded (creator vs created); created screens. (V-INSERTS)
- [ ] Phone screens: personal data blurred for its whole time on screen (NC-14). (review)

**7. Sound contract**
- [ ] Cues only on the hook, reveals and whips (S1–S6); no meme cues; the bed ≥ 20 dB under speech; cheers not ducked out; −14 LUFS, TP ≤ −1.5 dBTP. (S1–S6, `veos qa`)

**8. End and export**
- [ ] CTA (if any) on screen ≥ 1.5 s over the last reaction; 1080×1920, 30 fps CFR; frame count = round(duration × 30). (V-PROMISE, `veos qa`)

---

## Conditional modules

### §16 Frame template / persistent chrome
OFF (`profile.modules.chrome = false`): nothing persists on screen across the reel; every graphic belongs to a moment.

### §17 Running state & anchored graphics `[COND: modules.running_state, modules.anchors] [DNA mechanics]`

#### 17.1 State variables
| Var | Type | Start | Format | Display | Persist | Ops |
|---|---|---|---|---|---|---|
| `stake` | money | 0 | SW-08 full (`$10,000`) | P-20 on the stake object | across cuts, while the object is on screen | `set` when the stake is named or raised |
| `total` (one per person or group when several win) | money | 0 | SW-08 full, `+` prefix on gains only (P-21), none on totals (P-23) | P-23 at the person's tag spot | across cuts, while that person is on screen | `add` per won round / right answer; never `set` mid-reel |
| `clock` | clock, **set time base** | the logged start (e.g. `1:00`) | `M:SS` | P-24 top centre | across cuts for the clock run | `tick_to` per clock shot; jumps allowed, down only |

Ops are written per beat: `state_ops: [{var: "total", op: "add", value: 500, at: 14.20}]`. Display rules: one fixed position per variable per person; the number changes only on an op; it never contradicts the spoken or shown amount; a total re-entering after a cut away appears with the P-20 pop at its last value (no roll).

**How the state is built on today's engine.** The renderer has no `ctx.state` yet (engine request, Part E). The planner resolves the state at P8:
- Money variables become figures in `plan/figures.json` (§18): a `total` is a `sum` figure whose steps land on each op's `at`. P-23 binds `figure` and shows `ctx.figAt(id, ctx.t, {roll: 8})` (or uses `VEOS.data.counter` with `roll: 8` when the spot is static).
- The clock becomes a list of `{t, v}` pairs in the scene (from the `tick_to` ops), and a `formula: none` figure `clock` whose steps are the logged values, so every displayed time has a provenance.

**P-20 money tag** (one scene per tagged object; the type-on is the built-in `fx.typeOn`, the follow is the built-in `anchor`):
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
The box is drawn where the anchor puts it (its centre on the track point + offset). A static object needs no track: drop `anchor` and set `box` from the look frame. Untyped glyphs keep their place, so the box never moves while it types.

**P-24 clock** (bespoke scene, E6):
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
The clock's exit after 0:00 is the next cut (t_out on that cut).

#### 17.2 Anchors
| Target | Placement (tag centre) | Clearance |
|---|---|---|
| `object:<label>` (case, stack, envelope, prize box) | x = the object's centre x; y = the object's top + 0.35 × its height (the number sits on the upper part of the object, as in v01 @ 0:35) | clamp to the tag band y 560–1460 and x 64–1016; ≥ 40 px from any face box |
| `person:<id>` (gains, totals) | x = the face centre x; y = face bottom + 140 px (the chest) | ≥ 40 px below the chin |
| `object:phone` (icons, avatar badge) | 40–80 px above the phone's top edge | ≥ 40 px from any face |
| `face` side (chip, name call) | beside the head: face box side ± 40 px; y = face bottom + 20…120 (chip) or face top − 20…+80 (name call) | never inside the face box |

**Modes:** `static` (default: the position read off the `--look` frame at `t_in`, held for the tag's life); `track` (when the target moves > 90 px during the hold: the scene's `anchor: {track, offset, point, scale_with: true, lost}` rides a `veos track` track, SCENES-API §13). Hand-written keyframes are no longer used.

**Anchor pass (P8, plan time, short spans):** request a track as soon as a beat's visual says a tag, chip, X, icon or glow sits on something that moves (a case carried, a hand, a walking subject). For each: `veos track --project P --at <t_in> --look`, read the box, then `veos track --project P --id <tag> --at <t_in> --box x,y,w,h --from <t_in> --to <t_out>` (`--point x,y` for a hand or chest; `--clip A` when the span crosses an angle switch of another camera). Track only the tag's own span (0.5–2.5 s here; ≤ 10 s per run) and **look at the preview**.
**Fallbacks:** the object leaves the frame or the track is lost for more than a few frames → `lost: "fade"` (fade 4 f) for a short dropout, otherwise end the tag on the cut before it is lost; no trackable object (motion blur, a crowd, a tiny envelope) → `static` at the `t_in` position, and keep the tag's hold ≤ 1.0 s; a face target (P-21, P-26, P-36) uses `ctx.face()` and needs no track.

#### 17.3 Validator V-STATE (pending; run as review until it is registered)
- Every displayed money value equals the figure's shown value at that time (V-DATA checks the figures today).
- Totals equal the sum of their ops; a total never decreases.
- The clock is monotonic down; its value changes only at a cut or a visible tick.
- A tag rides its track (V-ANCHOR: the track covers the span, ≤ 20% lost, never still on a lost object > 15 f) and never covers a face (V-ANCHOR / V-FACE, 40 px clearance).

### §18 Data contract `[COND: modules.data_figures] [DNA rules]`
Every amount on screen (tag, total, prize price, clock value) is in `plan/figures.json`. Allowed formulas: `sum`, `diff`, `per_period`; anything else is a stated value (`formula: none`) with provenance.

| Field | Rule in this style |
|---|---|
| `inputs` | each amount from the speech (`from: "script"` + `said`, or `from: "spoken@<t>"`) or from the creator's stake log (`from: "creator"`) |
| `figures` | one per tagged amount; one `sum` figure per running total, with steps on each op |
| `format` | SW-08 base; tags `style: full`; `sign: "+"` only on P-21 gains |
| `illustrative` | never used: stunt money is real |
| `scale_id` | not used (no charts) |

Example (example 14.3, the teacher's total):
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
**V-DATA** recomputes every step, checks that each tag scene's `text_content` holds only its figure's values, and lands counters within ±5 f of the spoken number. **V-NUMFMT** checks `$2,500` / `₹1,20,000` grouping and the `+` sign rule.

### §19 Evidence & citations
OFF (`profile.modules.citations = false`): the style shows events, not claims. The always-on inserts flow is §12.5.

### §20 Dialogue
OFF (`profile.modules.dialogue = false`): speech is not the spine and the caption colour follows the beat's mode, not a diarised speaker map. Subjects' lines get CS-3 through planner overrides (§5.3.3). Synced multi-camera angle switches use `veos sync` (+ `timeline.shots` when convenient), not the dialogue module.

### §21 Canvas camera
OFF (`profile.modules.canvas_camera = false`; PV-5: graphics are `support`): there is no graphics world to move over.

### §22 Ink & annotation layer
OFF (`profile.modules.ink = false`): no hand-drawn marks; the X flash (P-27) is a glyph, not ink.

### §23 Continuity
OFF (`profile.modules.continuity = false`): no morph chains or motifs; the reel is held together by the stake and the cut rhythm.

### §24 Series furniture
OFF (`profile.modules.series = false`; VAR). A buyer who runs a numbered series ("Day 12") turns it on: a P-31-style plate "DAY 12" in brand type, 1.0 s, inside SETUP; it counts toward the 15% intro cap.

### §25 Sponsor, brand & end cards `[COND: modules.brand] [DNA look; VAR assets]`
| Element | Spec |
|---|---|
| **Sponsor logo pop** (P-30) | the creator-supplied logo file (PNG/SVG), w 760–900 px, centred cy 1000 (cy 330 when a face is in y 800–1200), light radial haze behind it, pop 4 f, hold 0.8–1.7 s, out on a cut or a Z-R1 jump, ≤ 3 per reel, on the product's name or first appearance; never over a face, a tag or the clock |
| **Brand in type** (P-31) | Montserrat 900 caps 96–128 px in `paper` with a 6 px ink stroke when no logo file exists or the brand is a place |
| **URL line** (P-32) | Inter Tight 800 caps 64 px under the brand (24 px gap) or at cy 300; ≥ 1.5 s |
| **Disclosure** | TC-legal line in the BV-14 wording (default "Paid partnership"), Inter Tight 600 26 px at x 64, y 1450, from the first sponsor beat for ≥ 2.0 s (NC-12); the disclosure is also spoken in the script |
| **Product in footage** | the host holds or uses the product in SH-3/SH-4 shots; the brand colours appear only in the logo file and the real product |
| **End cards** | none: `brand.endcard = null`. The CTA (if chosen) rides the last reaction (§6.7) |

Rules: sponsor beats never interrupt a stake beat between the verdict and the reaction; the sponsor's own colours never recolour the tags, captions or clock; the logo is recorded in `plan/inserts.json` as `origin: creator`.

---

## Part C. Declared exceptions and the non-overridable core

### C.1 The non-overridable core in this style
| ID | How this style meets it |
|---|---|
| NC-1 Face never covered | tags 40 px off faces (§17.2), captions at the chest with `avoid_face`, chips beside the head |
| NC-2 No text on text | captions hidden under every tag, logo, brand type and name call (§5.3.6) |
| NC-3 Smooth motion | pops 4–7 f, exits 4–5 f, anchor travel ≤ 60 px per frame; re-crops only on cuts |
| NC-4 Legibility | 5–9 px ink strokes on all coloured type; floors in H11 |
| NC-5 IG bands | text inside y 110–1500, not right of x 970 between y 900 and 1540 |
| NC-6 Truth | every amount from the speech or the stake log (§18); no tag on prop money |
| NC-7 Creator-owned media | footage is the creator's; logos only from the creator; everything else created (§12.5) |
| NC-8 Audio | −14 LUFS, TP ≤ −1.5 dBTP; the bed ≥ 20 dB under speech |
| NC-9 Determinism | shakes and blinks from `ctx.rng(seed)` |
| NC-10 Hue cap | ≤ 3 bright hues per frame |
| NC-12 Disclosure | the sponsor disclosure line (§25) |
| NC-13 Quote integrity | captions verbatim; created quote cards only with the transcript's words |
| NC-14 Redaction | phone screens blurred where personal data shows (N14) |

### C.2 Exceptions used
**E6 hard swap** only (§2.2): `tokens.exceptions.E6 = {slot_tolerance_px: 4}`; scenes `clock` and every P-23 total set `exception: "E6"` and mark their container `data-slot`; CS-1 inherits it from its `hard` swap. A buyer may switch E6 off (VAR): the clock and totals then roll over 4 f instead of swapping, and CS-1 uses a 2 f fade.

### C.3 What is not an exception here
Captions and tags over bodies, hands and props are not elements and need no exception (structure C.2). Three money tags at once during a multi-object reveal are within G2 because captions are hidden.

---

## Part D. Personalisation

### D.1 What the buyer is asked at setup (one round, ≤ 4 questions, each with "keep the template's")
| ID | Question | Lands on |
|---|---|---|
| BV-01 | "Your name and handle?" | the handle chip (P-26), the avatar initials, `creator.name/handle` |
| BV-02 | "One or two brand colours?" | `roles.primary` (chip ring, avatar badge, keyword sticker); a second colour goes to `roles.accent` only if it is a light warm hue (TUNE range), else it is ignored with a note |
| BV-05 | "What language do you speak, and captions in?" | `profile.language`, always asked: **English** → English captions (default) · **Hinglish** → romanised Hinglish captions · **Hindi** → Devanagari captions; numbers follow (BV-06). |
| BV-08 | "A call to action at the end? (none / comment keyword / link in bio / post caption only)" | `profile.cta.chosen`, P-35 / P-32 |

**Defaulted, changeable later:** BV-03 fonts (inside each slot's class), BV-06 numbers (Indian ₹ grouping for Indian languages), BV-11 humour (`off` or `light`), BV-14 disclosure wording, BV-16 logo (the avatar), BV-17 duration (40–75 s), BV-15 never-on-screen list.

### D.2 Lock summary (full map in `tokens.json → locks`)
- **DNA:** source type, spine, graphics role, footage dependency, the caption mechanics and modes, `good`/`bad` colours and meanings, the money-tag look, the clock format, the hook archetype set, the cut rhythm's existence, the zoom policy, no headline, no outro.
- **TUNE:** cadence ±15% (cuts/min, median shot), caption sizes and y within ranges, tag sizes, clock size and y, accent hue, grade-event count 0–3, motion ±15%.
- **VAR:** the creator's colour, the punch pink, language, numbers, CTA choice, the sponsor module on/off, disclosure wording, the bed, the setups.
- **NICHE:** §6.4 hook pairs, §8.4 lookup, §14 examples, App. A.

### D.3 NICHE slots filled per reel
At P7 the editor writes the reel's hook pair (§6.4) and appends it; at P5/P8 new line types go into §8.4 (≤ 10 new patterns over time, from existing families); the first approved reel becomes the §14 example; approved stake lines and titles join App. A; confirmed names and brands join the glossary.

---

## Part E. Changes and deviations

### E.1 Deviations from the architects' decision (STYLE-COVERAGE row 15), with evidence
| Item | Coverage said | This template | Evidence |
|---|---|---|---|
| `graphics` | minimal | **support** | overlays cover 13–27% of runtime (above the 15% `minimal` cap); the style needs 38 named patterns (tags, totals, clock, chips, X, logo pops, grade events, cut patterns) |
| `modules.data_figures` | off | **on** | money truth (H8) and the running total are built on `plan/figures.json` until `ctx.state` exists |
| `presenter` | anchor-ish (~85, any face) | **host, 60–100%** | ~85% of frames show a face, but group wides and inserts put faces under the 6% measuring floor |
| Countdown clock source | analysis: v03 @ 0:36–0:47 | **v02 @ 0:36–0:47** | the clock is on the v02 sheet s_03 (vault, cash-grab); v03 has no clock |
| Yellow captions | "yellow exclaim" | **yellow = subjects' lines + exclamations** `(unverified)` | v02 "YEAH! :D", "NOLAN!!", "TIME..."; v04 "SERIOUS!", "I'M LIKE...", "THANK YOU" |

### E.2 Engine requests (the template works today with the fallbacks named)
| # | Request | Why | Today's fallback |
|---|---|---|---|
| ER-1 | `ctx.state(var)` reading `state_ops` from the timeline, and **V-STATE** | totals and the clock are the structure of timed and scored stunts | figures + per-scene value lists (§17.1); V-DATA + review |
| ER-2 | ~~Object tracking for anchors~~ **done** (Package E: `veos track` + scene `anchor`, §17.2) | money tags ride moving cases and hands | — |
| ER-3 | **Object mask** (segment the stake) for P-25 | the evidence glow lights the object itself | a radial glow + tint ellipse on the object box |
| ER-4 | ~~Footage freeze~~ withdrawn: full-rate frames show GR-bw is live (v04 @6.40) | — | — |
| ER-5 | **Grade events rendered by the engine** from `timeline.grades` + **V-GRADE** | colour events should be one line in the timeline, checked for count and spacing | GR-green is now a built-in `flash` transition; GR-bw stays a z11 saturation-blend scene + `timeline.grades` marker |
| ER-6 | A **clock format** in `fmtNum` (`M:SS`) known to V-DATA / V-NUMFMT | clock values are figures but not money | a `formula: none` figure + `M:SS` written by the scene |
| ER-7 | A **position override per time range** in `captions.overrides` (`{t: [a, b], cy}`) | shouts sometimes sit beside a small speaker | P-36 name-call scenes with captions hidden |
| ER-8 | A **moment-selection helper** (E-23): scene detection + face size + audio energy to pre-log `plan/moments.json` | P1b is the most time-consuming step for 10–20 min of footage | manual logging at 2× speed |
| ER-9 | ~~Built-in footage blur transitions~~ **done** (`timeline.transitions` `whip` / `zoom-blur`, §9.1) | T-01 / T-05 | — |
| ER-10 | ~~Radial motion blur on camera moves~~ **done** (camera preset `blur {kind: radial}`, §10.2) | Z-C1 smears radially at 5–6% zoom per frame | — |
| ER-11 | ~~Per-glyph type-on~~ **done** (`VEOS.fx.typeOn`, §17.1) | P-20 money tags type on glyph by glyph | — |

### E.3 Version history
- v1 (draft): first release of the template.

---

## Part F. IDs used in this playbook
| Prefix | IDs |
|---|---|
| D | D1–D8 |
| H, N | H1–H18, H-dead-air; N1–N14 |
| E, NC | E6; NC-1…NC-14 |
| W, L, G | W-set, W-band; L-full, L-wide-band; G-0 |
| GR | GR-bw, GR-green |
| CS | CS-1 neutral, CS-2 comic, CS-3 shout, CS-4 punch (+ mode none) |
| HA, ST | HA-13 (default), HA-14, HA-16; ST-2, ST-3, ST-5, ST-6 |
| SM | none |
| B, P | B-1…B-7; P-01…P-13, P-20…P-36, P-40…P-45, P-50…P-53 |
| T, R | T-00…T-05; R-01…R-12 |
| Z | Z-R1, Z-R2, Z-P1, Z-C1 |
| SH, FB | SH-1…SH-10; FB-1…FB-10 |
| F | F-A |
| BV | BV-01, BV-02, BV-05, BV-08 (asked); BV-03, BV-06, BV-11, BV-14, BV-15, BV-16, BV-17 (defaulted) |
| ER | ER-1…ER-11 (engine requests; ER-4 withdrawn) |
| V | V-F0, V-CADENCE, V-ONWORD, V-SAFE, V-FACE, V-PRESENCE, V-CAPTION, V-LAYOUT, V-CAMERA, V-TYPE, V-EXC, V-HUES, V-NUMFMT, V-DATA, V-STATE (pending), V-GRADE (pending), V-PROMISE, V-REHOOK, V-INSERTS, V-CITE, V-COMEDY |

---

## App. A Cold-open line and post-title bank `[NICHE]`
Slots: `[STAKE]` the amount or prize as written on the tag · `[ACT]` what the person must do · `[N]` seconds or count · `[WHO]` the person or group · `[PLACE]`.
| # | Spoken stake line (cold open) | Post title | Archetype | Niche example |
|---|---|---|---|---|
| 1 | "If you can [ACT], this [STAKE] is yours" | "[ACT], Win [STAKE]" | HA-13 | A: "If you can name my shop, this ₹5,000 is yours" |
| 2 | "You have [N] seconds to [ACT]" | "[N] Seconds To Win [STAKE]" | HA-13 | B: "You have 60 seconds to hold this bar" |
| 3 | "Every [ACT] = +[STAKE]" | "Every [ACT] Pays [STAKE]" | HA-13 | B: "Every rep is +$10" |
| 4 | "I'm about to pay for [WHO]'s [THING]" | "I Paid For [WHO]'s [THING]" | HA-13 | A: "I'm about to pay for this whole queue's chai" |
| 5 | "This is [STAKE] in [FORM]" | "[STAKE] In [FORM]" | HA-14 | A: "This is ₹1,00,000 in ₹10 coins" |
| 6 | "Last one standing keeps [STAKE]" | "Last One Standing Wins [STAKE]" | HA-13 | B: "Last one in the plank keeps $1,000" |
| 7 | "[STAKE] or [OTHER STAKE], you pick" | "[STAKE] Or [OTHER STAKE]?" | HA-13 | A: "₹10,000 or the mystery box, you pick" |
| 8 | (no line: the host lifts the stake, walks into [PLACE]) | "Surprising [WHO] With [STAKE]" | HA-16 | A: "Surprising the night-shift guards with ₹20,000" |
| 9 | "Whoever [ACT] first wins [STAKE]" | "First To [ACT] Wins [STAKE]" | HA-13 | B: "Whoever finishes the sprint first wins my shoes" |
| 10 | "Answer right and [WHO] gets +[STAKE]" | "Every Right Answer = +[STAKE]" | HA-16 | A/B: "Answer right and your teacher gets +$500" |

---

## App. B Evidence map (summary; the full map with timestamps is `evidence.md`)
| DNA element | Evidence |
|---|---|
| Cold open mid-action, caption at f0 | v01 hook @ 0:00 ("are"), v02 @ 0:00 ("THIS"), v04 @ 0:00 ("I'M ABOUT TO"); v03 @ 0:00 face + cash, no caption (HA-16) |
| First cut 1.30–2.13 s; 30–48 changes/min, median 1.03–1.28 s (full-rate detection) | `cuts.json` / `meta.json` v01–v04 |
| Money tags on objects, neon green with glow | v01 @ 0:15 (three cases), 0:19, 0:25, 0:35–0:37; v03 @ 0:12–0:13, 0:23, 0:43–0:44, 0:52–0:53, 1:07; v04 @ 0:15 |
| Loss tag red `$0` across a cut | v01 @ 0:20–0:21 |
| Running total ticking in place | v03 @ 0:43 "+$8,370" → 0:44 "+$9,000" |
| Countdown clock, set time, jumps | v02 @ 0:36–0:47 (0:58 → 0:49 → 0:48 → 0:47 → 0:46 → 0:26 → 0:03 → 0:02 → 0:01) |
| Neutral lowercase captions | v01 throughout |
| Comic caps, yellow shouts, green money word | v02 @ 0:00–0:01, 0:07–0:30; v04 throughout |
| Pink punch word | v01 @ 0:30–0:31 ("god", "beast!") |
| Handle chip, X flash | v01 hook @ 0:00.83–1.33, 1.5–2.0 |
| Logo pops, brand in type, URL | v02 @ 0:02–0:03, 0:17; v03 @ 0:49, 0:59–1:01 |
| B&W hold, green flash + avatar badge | v04 @ 0:06–0:07, 0:12–0:13 |
| Object glow | v03 hook @ 1.67–2.0; v01 @ 0:36 |
| Whip blur / zoom-blur punch | v02 @ 21.3 (whip), 4.42 (zoom blur); v03 @ 7.27 is a hard cut into a crash zoom |
| Camera: jump re-crop, reaction push, crash zoom | v02 @ 4.05, v04 @ 6.40; v01 @ 1.48, 20.40; v03 @ 7.27 (full-rate ORB, completeness audit) |
| Hidden-cam viewfinder look | v02 @ 0:06–0:16 |
| Ghost replay | v03 @ 0:29–0:30 |
| Ends on a reaction, no CTA | v01 @ 0:37, v02 @ 0:50, v03 @ 1:13, v04 @ 0:36 |

`(unverified)` values: the speech language (no transcripts); the comic and numeric typefaces (closest bundled: Bangers, Lilita One); the yellow-caption rule (inferred); the bed (sound not observable); the CTA set (no evidence reel has one). Resolved: GR-bw is live, not a freeze.
