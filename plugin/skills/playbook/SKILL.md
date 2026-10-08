---
name: playbook
description: Set up (or change) a creator's editing playbook for Vibe Editing OS (one person can have several, e.g. one per account). Path A, pick a ready-made editing style from the gallery and brand it in 4 questions (name, colours, language, call to action); path B, build their own style (interview, inspiration videos, a full playbook, a preview to confirm). Also handles "change my playbook" tweaks to an existing one. Use when the user runs /playbook, is new to Vibe Editing OS, says "set up my editing style", "pick a style", or wants to change how their reels are edited.
argument-hint: "[creator name or handle]"
model: claude-opus-5-5
effort: high
---

# Set up the creator's editing playbook

The playbook is the brain of every edit. There are two ways to get one, and **path A comes first**:
- **A. Pick a ready-made style** (a template): gallery → 4 branding questions (name, colours, language, call to action) → saved and linked. They edit their
  first reel right away. No interview, no inspiration videos, no preview loop.
- **B. Build my own style:** interview → inspiration → a full playbook as deep as the reference → preview → confirm.

The creator answers questions and confirms. **They never write the playbook.**

Run `veos paths` first. You need:
- `playbooks`: where this user's playbooks live (write here)
- `playbook_template`: the template folder (path B)
- `reference_playbook`: the reference playbook (read-only, path B)
- `repo_root`

**Also read `<repo_root>/playbooks/_global/GLOBAL-RULES.md`.** Every playbook follows its ten directions (smooth motion,
nothing overlapping by accident, a clear face, readable text, one idea at a time, show the thing not the word, say what
was said, hook titles hook, pace like the style, the style decides the look). Directions, not limits: write the
playbook's own rules the same way.

## Step −1: New playbook, or change an existing one
1. Run `veos workspace get`. It shows the playbook linked to this folder, if any, and all existing playbooks. Entries
   with `"kind": "style_copy"` were made from a template (path A): they also show `template` and `style`.
2. Ask in one question (skip it if there are no playbooks yet):
   - **Create a new playbook** (e.g. for another account).
   - **Change** `<existing one>`.
3. **New:** go to Step 0. **Never overwrite an existing playbook folder.** One person can own several playbooks; each is
   fully independent (its own style, brand, learned rules).
4. **Change:**
   - a template copy (`style_copy`): follow **"Tweak a template copy"** below;
   - a path-B playbook: jump to the step they want to change (interview answers, inspiration, a section, colours…), then
     do Steps 4–6 again.

## Step 0: Choose the path (one question)
Run `veos templates list` first.
- **They already named a style or a creator** ("Kallaway style", "like Ali Abdaal", or `style: …` from the reel skill):
  skip this question and go straight to path A, A1 step 1.
- **It lists templates** (`count` > 0): ask with AskUserQuestion, path A first:
  - **"Pick a ready-made editing style (recommended, about 2 minutes)"**
  - **"Build my own style from scratch (interview + inspiration videos)"**
- **It lists none but `locked` is not empty** (the buyer's plan, `plan`, includes only building their own style): say in
  one line "Your <plan> plan includes building your own editing style; the ready-made styles come with an upgrade", and
  use path B.
- **It lists none and nothing is locked:** say in one line that ready-made styles arrive with an app update, and use path B.
- Templates in `locked` are not in the buyer's plan (`unlock_with` names the plan that unlocks them). The gallery shows
  them in an "Unlock with an upgrade" section. If the buyer picks one, say "That style comes with the <unlock_with>
  plan" and offer the styles in their plan; `templates copy` refuses it with `TEMPLATE_LOCKED`.
- `LICENCE_REQUIRED` from any command: say "Activate your licence first" and invoke `vibe-editing-os:setup licence`.
- **Faceless buyers** (they said they won't appear on camera, or they only have voice-overs): in path A, open the
  gallery with `--faceless-first`; in path B, use the faceless branch of Step 1.

## Path A: pick a ready-made style

Templates are ready-to-use graphic editing styles (STYLE-PLAYBOOK-STRUCTURE Part D.0). Each template's playbook is
complete; the buyer only brands it.

### A1. Gallery (pick by eye: a style is never picked without being seen)
**Never offer styles as text-only options** (no AskUserQuestion list of style names before they have seen them), and
always name a style together with the creator it's inspired by ("Whiteboard Split, inspired by Kallaway"). Every page
below plays each style on the creator's own reel. Open a page for them with Windows `Start-Process "<out>"` or macOS
`open "<out>"`. **If opening fails**, say so in one line and give the page's path and
https://www.shipwithoutcode.com/veos#styles (every style plays there too); ask only after they've looked.
1. **They named a style or a creator** ("Kallaway", "like Ali Abdaal", "Whiteboard Split"): run
   `veos templates gallery --focus "<their words>"` (add `--faceless-first` for faceless buyers). It matches ids, style
   names and the creators a style is inspired by, writes a page with that style first and highlighted (the rest follow),
   and prints `out` and `focus` (the matched style: `name`, `inspired_by`). Open it, then ask in one AskUserQuestion:
   "**<name>, inspired by <creator>**: it's playing in your browser. Use this one?" Options: "Yes, use <name>" /
   "Show me other styles" (→ step 3).
   - `NO_STYLE_MATCH` (no style is inspired by that creator yet): pick the 2–3 closest from `veos templates list`
     (`tagline`, `needs`, `inspired_by`) and open them as in step 2, saying "There's no <creator> style yet; these are
     the closest:".
2. **A vague request** ("something clean", "for my finance reels"): shortlist 2–3 from `veos templates list` (`tagline`,
   `needs`, faceless) and run `veos templates gallery --only "<id>,<id>,<id>"`. Open it, then ask which one they like,
   naming each with its creator.
3. **No preference, or "show me all":** run `veos templates gallery` (add `--faceless-first` for faceless buyers) and
   open it. Say in 2 lines: each card plays the style on the creator's own reel; **"needs:"** says what they have to
   shoot; tell me the name of the one you want. **Ask no filter questions.** Templates in the last section ("For brands
   & agencies", `section: brands`) are made for product and brand ads.
4. Faceless templates (`faceless: true`, or listed in `faceless_formats`): describe them as "no face on camera: you record
   your voice, the edit is all graphics". A template may be faceless in one format only: say which.
5. They answer with a name (or "the second one"). Match it to its `veos templates list` entry. If they hesitate between
   two, open just those two (`--only "<id>,<id>"`), compare them in two lines from `tagline` and `needs`, and let them
   choose. Never pick for them.

### A2. Brand it (one AskUserQuestion round, 4 questions)
Ask exactly these four questions, all in **one** AskUserQuestion call (skip only the colour question when `brandable` is
empty). **Every question has a "Keep the template default"
option**, and free text is always allowed. Take the options from the template's `veos templates list` entry.
1. **Name and handle** (BV-01): "What name and handle should appear in your reels?" Options: the name and handle from
   the conversation or an existing playbook if you know them, and "Keep the template default (no name on screen)".
2. **Brand colours** (BV-02): "Your brand colours?" Options: 2–3 concrete choices that suit the style (hex, shown as
   `#4B2FCF purple`), and "Keep the template's colours". Free text: one or two hex values (convert colour names to
   hex). Skip this question when `brandable` is empty.
3. **Language for this folder's playbook** (BV-05): **always asked.** Four options, English first:
   - **"English (default)"**: English speech, English captions in plain Latin script (`--language english`);
   - **"Hinglish"**: Hinglish speech, captions in romanised Hinglish (Latin script) (`--language hinglish`);
   - **"Hinglish speech, English captions"**: they talk in Hinglish, the captions are translated to English
     (`--language hinglish-en`; offered when `hinglish/en/Latn` is in the template's `languages`, which every template
     with English captions has). Each reel then needs the English caption script (`translate` transform);
   - **"Hindi"**: Hindi speech, Devanagari captions (`--language hindi`; offer it when `hi/hi/Deva` is in the
     template's `languages`; every shipped template has it).
   Numbers follow the speech: English → `$`, 1.2M; Hinglish (either caption choice) / Hindi → ₹ with lakh / crore. If an
   English speaker wants rupees, pass `--currency INR`.
4. **Call to action** (BV-08): options from `cta_devices` in plain words ("Comment a keyword and I DM you", "Link in bio",
   "Follow and save"), plus "Keep the template default". For a keyword device, ask for the keyword in the free text
   (e.g. "BUDGET"). Any other device they name is fine too: pass it, it is applied.

Everything else takes the template default (structure D.3): fonts, formats, theme packs, humour, series, sponsor wording,
duration, profanity masking (on: S**T, F**K; they can turn it off later). Footage isn't asked at setup.

### A3. Save it
1. Write the copy:
   `veos templates copy <template-id> [--name "<name>"] [--handle @x] [--colors "#hex[,#hex]"] --language english|hinglish|hinglish-en|hindi [--currency INR] [--cta device[:value]]`
   - Leave out every flag whose question they answered with the template default (no `--name` = no name on screen).
     Always pass `--language` (`english` when they kept the default).
   - `--cta` takes a device, with its value after a colon (`comment_keyword:BUDGET`, `link_bio`).
2. Link this folder: `veos workspace set --playbook <id>` (the `id` printed by step 1).
3. If the copy fails with `BAD_CTA` or `LANGUAGE_NOT_SUPPORTED`, say in one line what the editor supports and ask again
   for that one answer. Any other error: report it plainly.

### A4. Tell them (3–4 lines, then stop)
1. "Saved **<title>** for this folder." Add the `nudge_line` if there is one, and each line of `notes`, word for word
   (e.g. "Your brand colour replaces the per-reel colour rotation.", "Numbers follow your language: …").
2. Put raw clips in a folder here and run `/vibe-editing-os:reel <folder>`. Faceless: drop the voice-over file (and the
   script if they have one). Repeat the template's `needs` line.
3. They can change anything in the style any time: "change my playbook", or feedback while editing.

No preview loop and no "anything to improve?" round: the gallery was the preview.

## Tweak a template copy (any time)
Triggered by "change my playbook" on a `style_copy`, or by feedback while editing (the `reel` skill's "Save this for
future reels too?" flow uses the same command). **Buyers can change anything**: just apply it. No DNA warnings, no
"this moves away from the style", no confirm question.
1. Restate the change in one line, and map it to the token path(s) it changes in `<playbook dir>/tokens.json`.
   Examples: "bigger captions" → `captions.profiles.<CS>.skin.size`, "calmer" → `profile.tone.energy`, "my own font" →
   `font_slots.<slot>.family`, "turn the series tag on" → `profile.modules.series` + `series.name`, "no bookend" →
   `continuity.bookend`, "stop masking swear words" → `captions.profanity.mask`.
2. Run `veos learn add --playbook <id> --source buyer --area <area> --text "<the rule>" --change <path>=<value> [--change …]`
   (`--source buyer` for a direct request; leave it out for feedback while editing). Read `status`:
   - **`applied`**: confirm in one line ("Done: captions 36 → 42 px."). That's all, whatever `class` says (a `DV-n` is
     only the record).
   - **`refused`** (only the global quality guarantees: text over the face, overlapping text, legibility / contrast
     floors, untrue numbers, fetching other people's media, and the other never-bendable rules): say the `message` (one
     friendly line with the nearest allowed option), and offer to apply that option instead (`alternative_value`,
     through the same command).
3. A rule that changes no token value ("always open with the total") is saved without `--change`. A rule that, as
   worded, breaks a never-bendable rule ("put the number over my face") goes in with `--nc NC-<n>` (structure C.1), so
   it is refused the same way.
4. When the change also needs the prose updated, edit that line of `playbook.md` (add `(DV-n)` when the result lists a
   deviation). Never edit the engine-managed blocks (`<!-- veos:lineage -->`, `<!-- veos:appc -->`).

## Path B: build my own style
The full flow below: interview → inspiration → playbook → glimpse → confirm. Get a unique id first with
`veos playbook new-id --name "<creator or account name>" --handle <handle>`.

**Faceless styles:** a playbook whose `tokens.json` → `profile.source_type` is `voiceover_only` (`presenter.presence: none`,
`spine: audio`) is a **voice-over style**: "needs: a voice-over only" ("no face on camera: you record your voice, the edit
is all graphics"). The faceless branch is in Steps 1 and 3.

## Step 1: Interview (plain language, 2–3 rounds of questions, multiple-choice where possible)
Ask with the AskUserQuestion tool (≤ 4 questions per round; always allow free text):
1. **Content:** niche and topics (ask for 3–5 recent or upcoming reel ideas), the audience, what viewers should feel/learn, and recurring formats (listicles, tutorials, stories, rants, reviews, before/after).
2. **Voice and language:** spoken language (e.g. Hinglish / English / Hindi), the caption language and script (romanised or native), humour level (none / light / roast and meme), and energy (calm / balanced / hype).
3. **Shooting:** first ask **"Do you appear on camera?"** with options "Yes, I talk to camera", "Sometimes", "No, voice-over only (faceless)".
   - **On camera:** camera setups (selfie / tripod / desk / walking / kitchen / gym…), background, whether they record screen recordings or B-roll, and typical raw length.
   - **Faceless:** how they make the voice-over (phone mic, studio mic, AI voice they own the rights to), whether they write a script first, typical length, and what of their own they can show (screen recordings, B-roll, photos, past reels as proof). This makes a **faceless playbook** (see Step 3).
4. **Brand:** name and handle, primary + accent colours (hex, or "pick for me"), fonts they like (or "pick for me"), whether they have a logo (the file goes into the references folder in Step 2), CTA habits (comment keyword → DM, follow, link in bio, community name), anything they **never** want on screen.
5. **Assets:** do they have B-roll clips, product shots, screen recordings, or a sound-effects library they're licensed to use? (Just yes or no here: files are dropped into a folder later, never typed as paths.)

Write the answers to `<playbooks>/<id>/profile.md` (id from `veos playbook new-id`).

## Step 2: Editing inspiration
**Nobody types a file path.** Make a folder, open it for them, and let them drop the videos in:
1. Create `<the folder they are working in>/references` (Bash `mkdir -p`) and open it: Windows PowerShell `Start-Process "<absolute path>"`, macOS `open "<path>"`.
2. Say in one plain message, with no multiple-choice options: "I've opened a folder called **references**. Drop 1–5 reels whose **editing** you love into it (downloaded video files: links alone can't be analysed), and 2–3 of your own past reels if you like. Then reply **done**."
3. When they reply, list the video files in that folder with Bash (`.mp4 .mov .m4v .webm .mkv .avi`, any case). If some are their own reels and the file names don't say so, ask in one line which ones. Nothing there: say so in one line and ask them to drop the files into that folder (or paste a path: a pasted path or folder still works).

For each video file, do a style extraction (the reference process P1). Use the `vibe-editing-os:veos-runner` agent for the heavy commands:
- `veos sheet <out> --video "<file>" --frames <2 fps list>` for overview contact sheets.
- Scene cuts with ffmpeg (`select='gt(scene,0.25)',showinfo`), then frame-by-frame strips around 3–5 transitions (`veos sheet --video … --frames …`).
- Look at the sheets yourself and note:
  - layout grid and caption styles (font feel, size, colour, position, animation)
  - the hook construction in the first 3 s
  - B-roll families and how they relate to the words
  - transition recipes (frames, direction, colour)
  - zoom habits, pacing (cuts and changes per second), colour palette, sound feel if obvious
- Write the findings, as reusable rules and not a clip description, into `profile.md` under "Inspiration analysis".

If they have no inspiration files:
- Ask them to **describe** the editing they like: 2–3 creators or reels by name, plus what they like about them.
- Then build the style from that description and their answers.
- If `veos templates list` shows templates, offer path A (a ready-made style) instead.

## Step 3: Write the playbook
1. Read `<playbook_template>/PLAYBOOK-TEMPLATE.md` (the required structure).
2. Read the reference playbook (`reference_playbook`) **selectively** for depth and format: its header + directives, §2, §6, §8.3–8.4 and §13. Don't copy its content.
3. Write `<playbooks>/<id>/playbook.md` with **every** template section, specific to this creator. §2 starts with the editing rules (GLOBAL-RULES.md):
   - **Directives (D1…)** from what they said matters.
   - **Result-pair table and line → pattern lookup built from their actual topics** (use the reel ideas they gave).
   - **20–60 named visual patterns (P-…) invented for their niche,** each with on-screen content + a motion recipe in frames. These are ideas the editor will build as bespoke code, so describe them concretely; don't limit them to what's easy.
   - **Rules from the inspiration analysis**, translated into tokens (sizes, frames, colours).
   - **The assets list:** what they should record or supply for each B-roll family.
4. Write `<playbooks>/<id>/tokens.json`: **copy the schema of the `tokens.json` that sits next to `reference_playbook` exactly**, with this creator's colours (roles keep their meanings; contrast-safe), font slots (bundled Google/OFL fonts only), type sizes, layout, motion, camera presets, budgets, `creator` (name, handle, language, caption_language, banner_language, cta, glossary) and `tone`.
   - **Faceless playbook:** add a `profile` block to `tokens.json` (`source_type: voiceover_only`, `presenter: {presence: none}`, `spine: audio`, `graphics: support|primary`, `footage_dependency: none|medium`, `modules.canvas_camera` when the style travels across a canvas) so the engine and the reel skills pick the voice-over branch by themselves. In `playbook.md`, §1 uses the voice-over branch (no matte; one scene per sentence, stage hidden), §3 has no presenter rules, and §8 builds its patterns from the faceless families (kinetic type, diagrams with the canvas camera, icon/illustration cards, morph hand-offs, ambient worlds, the creator's own clips; SCENES-API §10). Leave `M1` and `M12` out of `rules_v0` (they check a speaker on screen).
5. **Sound palette (§11 + `tokens.json` → `sound`):**
   - Read `<sfx_pack>/catalog.json` (from `veos paths`).
   - Pick the vibes, roles and preferred sound ids that fit this creator's energy and humour answers. A calm creator gets soft, premium sounds and no meme hits; a hype creator gets punchier ones; meme sounds only if they chose roast/meme humour.
   - **Use only sounds that are in the catalogue.**
6. Write it in 3–4 large Write calls (header → §1–5 → §6–8 → §9–15 + appendix). Keep the reference's density.

## Step 4: The glimpse (preview page)
Write `<playbooks>/<id>/preview/index.html`: one self-contained page (inline CSS/JS, fonts from `<repo_root>/assets/fonts` via relative `file:` URLs or Google Fonts, no other network). Show 8–14 **animated 9:16 frames** (CSS/JS loops, ~360×640 each) using **their** tokens:
- **Frame 0 / hook:** their banner style + a result pair from their niche + a speaker silhouette (faceless: the kinetic type hook on their world instead, no silhouette). If they shared a raw clip, extract one frame with ffmpeg and use it instead.
- **Their caption systems:** keyword captions + subtitles in their language.
- **5–8 signature B-roll / motion patterns** from §8, each labelled with its P-id and the kind of line it serves.
- **2–3 transitions** and **the zoom feel** (a short loop each).
- **The palette and fonts** strip, and their CTA moment.
- **Their sound palette:** 4–6 play buttons (HTML `<audio>` with relative `file:` URLs into the SFX pack), each labelled with what it marks ("card arrives", "key word pops").

Under each frame, a one-line caption: "Used when you say … (P-xx)". Open the page for them (Windows `Start-Process`, macOS `open`).

## Step 5: Improve (always ask, right after the preview)
Ask: **"Anything you'd like to improve or add to your editing style before we save it?"**
- Offer 3–4 quick options that fit what they just saw (e.g. "Calmer transitions", "Bigger captions", "More motion graphics", "Different colours"), plus free text and **"No, it's good"**.
- For every change: restate it in one line, then update `playbook.md`, `tokens.json` and the preview together.
  - If a request would break a global rule (e.g. "fill the screen with text"), explain in one line and offer the closest clean alternative.
- Re-open the preview and ask again, until they choose "No, it's good".

## Step 6: Save and link this folder
- Add `"confirmed_at"` to `profile.md`.
- Run `veos workspace set --playbook <id>` so **this folder** uses this playbook. Reels edited in this folder or below it pick it automatically.
- Tell them in 3 lines:
  1. Put raw clips in a folder here and run `/vibe-editing-os:reel <folder>` (faceless: drop the voice-over file, and the script if they have one).
  2. For another account, open a different folder and run `/vibe-editing-os:playbook` there.
  3. Feedback they give while editing can be saved into this playbook, and they can revise it anytime with `/vibe-editing-os:playbook`.

**Token note (path B):** this runs once per creator. The playbook is long by design, because it's what makes every future reel good.

**Never patch or edit the engine, and never ask the user to pick an engine fix.** If a `veos` command fails, report it plainly and suggest `/vibe-editing-os:setup update`.
