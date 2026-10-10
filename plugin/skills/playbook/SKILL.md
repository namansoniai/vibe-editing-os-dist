---
name: playbook
description: Set up (or change) a creator's editing style for Vibe Editing OS, written down as their playbook (one person can have several, e.g. one per account). Path A, pick a ready-made style by eye in the gallery and answer two quick questions (the language and whether reels are sped up). Path B, their own style - a quick interview, the reels whose editing they love studied like the best creative director in the world, a first playbook, then an elevate pass that adds high-quality motion graphics for retention - or, with no reels, an original style invented for their niche. Also handles "change my playbook". Use when the user runs /playbook, is new to Vibe Editing OS, says "set up my editing style", "pick a style", "make me a style", or wants to change how their reels are edited.
argument-hint: "[creator name, or a style they named]"
model: claude-opus-5-5
effort: high
---

# The creator's editing style

The playbook is the brain of every edit: before every reel the editor reads it end to end and takes it as the creator's
taste. A great playbook makes every reel great; a form filled in makes every reel look like a template. So decide the
style once, with conviction.

Most creators want this quick, and then they want a result so good they go crazy. Ask only what you can't decide for
them, keep it human, and decide everything else yourself. They never write the playbook, and nothing is required that
most people don't have (no logo, no brand kit, no keyword); when they volunteer something, use it.

**Running `veos`.** Always the plugin's wrapper by its full path (a PATH change never reaches this session): PowerShell
`& "<plugin root>\bin\veos.cmd" <args>`, Bash `bash "<plugin root>/bin/veos" <args>` (macOS, or Git Bash on Windows). The
plugin root is two folders above this skill's base directory; `veos <args>` below always means this. Quote every path.
Write files only with the Write and Edit tools.
Open a page or folder for them with PowerShell `Start-Process "<path>"`, macOS `open "<path>"`, or Bash on Windows
`powershell -NoProfile -Command "Start-Process '<path>'"`; if it won't open, give the path.

Start with `veos paths` (`playbooks` = where their playbooks live, `playbook_template`, `reference_playbook`,
`repo_root`, `renderer_core`) and `veos workspace get` (this folder's playbook and all existing ones;
`"kind": "style_copy"` = made from a ready-made style). `LICENCE_REQUIRED`: "Activate your licence first", invoke `vibe-editing-os:setup` with `licence`.

## New, or a change?
If playbooks exist, ask in one question: **Create a new style** (e.g. for another account) or **Change <name>**. A change
goes to **Changing a playbook** below. A new one never overwrites an existing folder.

Then the path. They named a style or a creator ("Kallaway", "like Ali Abdaal") → path A, A1 step 1. They asked for their
own ("make me a style") → path B. Otherwise run `veos templates list` and ask with AskUserQuestion, path A first:
- **"Pick a ready-made editing style (recommended, about 2 minutes)"**
- **"Make my own style (a few quick questions, plus reels you love if you have them)"**

No templates listed but `locked` isn't empty: "Your <plan> plan includes building your own style; the ready-made styles
come with an upgrade", path B. Nothing at all: path B. Faceless creators (voice-over only): gallery with
`--faceless-first`; path B makes a voice-over style. Creators whose reels have no voice at all (music, B-roll, screen
recordings, photos): path B, with **A no-voice creator** below.

## Path A: a ready-made style

### A1. Pick by eye
A style is never picked without being seen: never offer style names as text-only options, and always name a style with
the creator it's inspired by ("Whiteboard Split, inspired by Kallaway"). Every gallery card plays the style on a real reel.
1. **They named a style or creator:** `veos templates gallery --focus "<their words>"` → open `out`, then ask:
   "**<name>, inspired by <creator>**: it's playing in your browser. Use this one?" ("Yes, use <name>" / "Show me other
   styles" → step 3). `NO_STYLE_MATCH`: open the 2–3 closest (`--only "<id>,<id>"`): "There's no <creator> style yet;
   these are the closest:".
2. **A vague wish** ("something clean", "for finance"): shortlist 2–3 from `veos templates list` (`tagline`, `needs`) →
   `veos templates gallery --only "<id>,<id>,<id>"`, open it, ask which they like.
3. **No preference:** `veos templates gallery`, open it, and say in two lines that each card plays the style, that
   "needs:" says what they'd have to shoot, and to tell you the name they want. No filter questions.
4. Faceless templates: "no face on camera: you record your voice, the edit is all graphics". Locked ones: "That style
   comes with the <unlock_with> plan". Torn between two: open just those two and compare them in two lines; never pick for
   them.

### A2. The language and the speed
One AskUserQuestion call, two questions (free text always allowed):
- **"What language do you speak in your reels?"** "English (default)", "Hinglish", "Hindi", and "Another language":
  type it (Telugu, Tamil, Kannada, Malayalam, Marathi, Bengali, Gujarati, Punjabi, or its mix with English: Tanglish,
  Telugu-English…). → `--language english|hinglish|hindi|<their language>` (a mix as they say it: `telugu-english`).
- **"Should your reels be sped up?"** "Normal", "1.1×", "1.2×". → nothing, `--speed 1.1`, `--speed 1.2`.

Not English: one more question, the captions: "In <language>'s own script, as spoken" (`--captions original`),
"Romanised, in English letters" (`--captions romanised`), "Translated to English" (`--captions english`). Hindi or
Hinglish: own script is Devanagari, romanised is the usual Hinglish.

Numbers follow the speech: English → `$`, 1.2M; Hinglish, Hindi and every Indian language → ₹ with lakh / crore
(`--currency INR` for an English speaker who wants rupees). Ask nothing else.

### A3. Save it and tell them
1. `veos templates copy <template-id> --language <their language> [--captions original|romanised|english] [--speed 1.1|1.2] [--currency INR] [--name "<name>"] [--handle @x] [--colors "#hex[,#hex]"] [--cta device[:value]]`
   (the other bracketed flags only carry what they volunteered). `BAD_CTA` / `LANGUAGE_NOT_SUPPORTED`: say what's
   supported, ask that one thing again.
2. `veos workspace set --playbook <id>` (the id it printed).
3. In 3–4 lines: "Saved **<title>** for this folder", its `nudge_line` and each line of `notes` word for word; put clips in
   a folder here and run `/vibe-editing-os:reel <folder>` (repeat the template's `needs`); they can change anything any
   time. No preview loop: the gallery was the preview.

## Path B: their own style

### B1. The interview (quick and human)
You're the best creative director in the world, meeting a creator who just hired you to give their reels a signature.
One AskUserQuestion round, four questions, free text always allowed (skip what they've already told you):
1. **What are your reels about, and who watches them?** (your best guesses as options)
2. **How should people feel watching?** e.g. "Hyped and entertained (fast, funny)", "Calm and premium", "Smart and clear,
   like a great teacher", "Bold and edgy".
3. **Are you on camera?** "Yes, I talk to camera" / "Sometimes" / "No, voice-over only" / "No voice at all (music,
   B-roll, screen recordings or photos)".
4. **Language:** A2's language question.

Then A2's speed question, with its caption question when the language isn't English, in one short call (no voice: no
speed, no captions; the language is the on-screen text's).

Then one plain message (no options), with a folder already open for them: create `<this folder>/references` (PowerShell
`New-Item -ItemType Directory -Force "<path>"`, Bash `mkdir -p "<path>"`) and open it. "Two optional extras: your brand
colours, fonts or logo if you have them, and anything you hate seeing in reels. And if there are reels whose editing you
love (yours or anyone's), drop 3–5 of them into the **references** folder I just opened, then say **done**. No reels? Just
say **skip** and I'll invent your style." A pasted path or folder works too. When they're done, list the videos in the
folder with the Glob tool (`.mp4 .mov .m4v .webm .mkv .avi`, any case); if it isn't clear which are their own, ask in one
line.

Get an id: `veos playbook new-id --name "<their name, or their niche>" [--handle <handle>]`. Write
`<playbooks>/<id>/profile.md`: their answers, what they volunteered, and every decision you make for them from here on.

**A no-voice creator** (their reels have no voice: they say so, or their reference reels have only music): the style
lives in the cut, the music and the text. Before the references message, ask in one plain message (numbered, with
examples; they answer in their own words):
1. **What they make:** B-roll of themselves / products / places, screen recordings of an app or site, photos or carousel
   slides — or a mix?
2. **Music:** what kind (trending audio, lo-fi, cinematic, upbeat pop, phonk), do they bring their own track every time,
   and does the cut sit on every beat, every bar, or loosely?
3. **Pace:** how long a shot usually stays (quick 0.5 s cuts, 1–2 s, slow 3 s holds); how long a reel runs.
4. **Text:** who writes it (they give a script, or you write it), how much (one word punches, a line at a time, a full
   sentence), where it sits, case and language, and its look (font feel, colour, a box behind it or not).
5. **Moves:** zooms and pans on photos, transitions between shots (cuts only, whips, flashes, zoom-throughs), effects
   they like or hate.
6. **Screen recordings (if any):** zoom into what matters, highlight boxes, step callouts, cursor effects, blur for
   private bits.
7. **The hook and the end:** how a reel opens (the best shot, a text question, a before/after) and ends (a CTA slide, a
   loop back to the start).
8. **Sounds:** any sound effects on top of the music, or the music alone.

Their profile is `source_type: no_voice`, `presenter.presence: none`, `spine: footage` (or `audio` when the music drives
everything), `captions.mode: off` (on-screen text lives in the scenes), `graphics: support`, `footage_dependency: high`
(photos/slides: `total`). The playbook's body describes the cut to the beat, the text style and the kinds they make, in
the same format as every other playbook.

### B2a. With reels: study them like the best creative director in the world
For each reel, an overview sheet at 2 frames a second:
`veos sheet "<playbooks>/<id>/inspiration/<n>" --video "<file>" --frames 0,15,30,45,…` (to about 90 s; frames past the
end are skipped). Where you spot a move worth stealing, a frame-by-frame strip across it (`--frames 210,211,212,…`).
Don't describe the clips. Find why they work:
- **Hierarchy:** on each frame, what does the eye land on first, second, last? What stays quiet so one thing can be loud?
- **Rhythm:** where does it rush, where does it hold, how does it build, where does it peak?
- **The moves:** how one graphic becomes the next; when the screen splits (down the middle or across) and comes back to
  the person; what carries the eye across a cut.
- **The hook:** what's on frame 0, why it stops a thumb, what the first three seconds promise.
- **The world:** colours and what each means, type and its attitude, the B-roll and how it relates to the words, the
  captions, the sound.
- **The feel,** in one sentence.

Measure what will need rebuilding exactly (positions, sizes, frames, hex values). Then be honest about where they're
ordinary. Write it in `profile.md` under **"Inspiration analysis"**, as reusable rules for this creator. From another
niche, translate its language into this one; never copy its content.

### B2b. Without reels: invent the style for the niche
Think like a director handed a new show. Who's watching, what do they trust, what are they tired of seeing, what makes
them stay? What does a reel from this creator always deliver, and how does the viewer *see* it happen? Two or three worlds
the reels live in, each with a job. A palette where every colour has one meaning and one colour leads. Motion with a
character. B-roll this niche can actually show. Two or three signature moves nobody in this niche is doing. Think with
examples, never copy them: a money audience may trust calm precision and numbers that move like a ledger; a cooking
audience wants to almost taste it; a coding audience wakes up for a before and after. These are prompts for thinking;
this creator and this audience decide. Write your reasoning in `profile.md` under **"Style decisions"**.

### B3. The first playbook
1. Read `<playbook_template>/PLAYBOOK-TEMPLATE.md` (the format) and `reference_playbook` end to end (the bar for depth,
   specificity and voice, never the content).
2. Write `<playbooks>/<id>/playbook.md` in that format, in 3–4 parts (a Write, then Edits that append) with a line to them after each.
   It opens with **The feel**: about 400 tokens of conviction about how their reel feels, specific to them, ending with
   a one-line test of the style. Then every section, decided and specific, with the reason behind each choice; rhythm
   described by feel, craft in exact numbers.
3. Write `<playbooks>/<id>/tokens.json`: **the schema of the `tokens.json` next to `reference_playbook`, exactly**, with
   this creator's colours (roles keep their meanings, contrast-safe), bundled fonts, type, layouts, motion, camera
   presets, `creator` (name, handle, language, caption_language, banner_language, cta, glossary; empty when not given)
   and `tone`. A2's answers: `profile.language.speech` (their language as they said it: `telugu`, `tanglish`…) and
   `captions` `{lang, script, transform}` per `<repo_root>/playbooks/_styles/tokens.schema.md` §3.3a (own script
   `verbatim`, romanised `Latn` + `transliterate`, English `translate`); ₹ and Indian grouping in `profile.numbers` for
   an Indian language; `"cut": {"speed": 1.1}` for a speed-up (left out for Normal). **Voice-over only:** add `profile` = `{"source_type": "voiceover_only", "presenter": {"presence": "none"},
   "spine": "audio", ...}` and build the patterns from the faceless families (`SCENES-API.md` §10, in the folder of
   `renderer_core`).
4. **Sound:** pick the palette from `<plugin root>/skills/edit/SOUNDS.md` (every usable sound with what it sounds like
   and what it's best for): vibes, roles, preferred ids per use, whether meme sounds belong. Mirror it in `tokens.json` →
   `sound`. Only ids from that list.

### B4. Elevate it
Now read your playbook back cold, and do exactly this:

> Act like the best editor in the world and the best creative director in the world, and make this playbook better by
> adding high-quality motion graphics which increase the visual appeal of the reel, in turn increasing the retention.

Rewrite it, part by part, a line to them after each: sharper hierarchy, braver moves, a picture wherever it said a word, motion graphics nobody in this niche has,
each specified well enough to build (what's on screen, the motion in frames, when it's used, the words that trigger it).
Keep The feel true, and make `tokens.json` agree with every number you changed. Note in `profile.md` what the elevate pass
added. This is the version they get.

### B5. Preview, confirm, save
1. Write `<playbooks>/<id>/preview/index.html`: one self-contained page (inline CSS/JS; fonts from
   `<repo_root>/assets/fonts` by relative `file:` URL) with 8–14 animated 9:16 frames in their tokens: the hook (a
   silhouette of the speaker, or kinetic type when faceless), their captions, 5–8 signature motion graphics labelled with
   their P-ids and the line each serves, 2–3 moves between scenes, the palette and fonts, and The feel's first lines on
   top. Open it.
2. Ask: **"This is your editing style. Save it?"** — "Yes, save it (recommended)" plus 2–3 quick changes that fit what
   they saw ("Calmer", "More motion graphics", "Different colours"). A change: update playbook, tokens and preview
   together, re-open, ask again.
3. Add `"confirmed_at"` to `profile.md`, run `veos workspace set --playbook <id>`, and tell them in two lines: put clips in
   a folder here and run `/vibe-editing-os:reel <folder>`; for another account, run `/vibe-editing-os:playbook` in another
   folder.

## Changing a playbook
- **A ready-made copy** (`style_copy`): map their words to the token path(s) in `<playbook dir>/tokens.json` ("bigger
  captions" → `captions.profiles.<CS>.skin.size`, "calmer" → `profile.tone.energy`, "my own font" →
  `font_slots.<slot>.family`, "add my handle" → `creator.handle`) and run
  `veos learn add --playbook <id> --source buyer --area <area> --text "<the rule>" --change <path>=<value>`. `applied`:
  confirm in one line. `refused`: say its `message` and offer its `alternative_value`. A rule with no token value is saved
  without `--change`. Never edit the engine-managed blocks (`<!-- veos:lineage -->`, `<!-- veos:appc -->`).
- **Their own style:** change what they asked in `playbook.md`, `tokens.json` and the preview together, then B5 again.

If a `veos` command crashes, say plainly what failed and suggest `/vibe-editing-os:setup update`. Never patch the engine.
