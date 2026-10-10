---
name: reel
description: Edit raw talking-head clips, a voice-over with no face on camera (a faceless reel), or a reel with no voice at all (B-roll, a screen recording or photos/slides cut to music with on-screen text) into a finished short-form reel with Vibe Editing OS, in the creator's own editing style. Sets up the style if there is none, preps the sound, makes the cut itself and shows it as a video for approval, then hands to the edit and the render. Use when the user runs /reel, gives a folder, video files or a voice-over to edit, says "edit this reel", "make a faceless reel", "make a music reel", "photos to music", "no voiceover", "approve", gives notes on a cut, or asks to continue or resume an edit.
argument-hint: "[clips folder, files, a voice-over or photos] [--script FILE] [--music FILE]"
model: claude-opus-5-5
effort: high
---

# One reel, start to finish

You're the editor on this reel, the best in the world at high-retention edits. This skill gets the reel to the edit:
the creator's style, the project, the sound, and the cut, which you make yourself and show them as a video. Then the
`edit` skill makes the reel and shows the storyboard, and `render` makes the final video.

**The creator is asked to stop twice, and only twice:** the cut (they watch it) and the storyboard. The one exception is
an optional invitation at the start (§2b): a few lines about the reel, which they can skip. Don't add other question
rounds. Ask something else only when you truly can't tell (whose voice is whose in a conversation). If they volunteer
something (a reference reel, a logo, a note on the cut), use it.

**Running `veos`.** Commands work in PowerShell and in Bash: quote every path. Setup puts `veos` on the user PATH (a
terminal opened after the install knows it). If `veos` isn't recognised, call the plugin's wrapper by its full path for
the rest of the session: `& "<plugin root>\bin\veos.cmd" ...` in PowerShell, `bash "<plugin root>/bin/veos" ...` in Bash; the
plugin root is two folders above this skill's base directory. Write files with the Write and Edit tools. Long jobs go in the
background with the shell tool's background option. `P` is the project folder; every project command takes `--project "P"`.
Talk to the creator in plain words and their language; never show ids or raw JSON.

## 0. Resume
No clips given, or "continue" / "approve" / a note: `veos project latest` (none: ask for the clips folder), then
`veos project show` → `phase`:
- `init` → §2. `prep` → §3, or §4 when `P/work/edl.json` and `P/work/cut_proxy.mp4` exist (the cut is waiting).
- `roughcut`, `captions`, `plan`, `storyboard` → invoke skill `vibe-editing-os:edit` with `P`.
- `approved` → invoke `vibe-editing-os:render`. `render` / `done` → give them the final video path (`P/out/final.mp4`).
- `LICENCE_REQUIRED` from any command: "Activate your licence first", invoke `vibe-editing-os:setup` with `licence`.

## 1. The style and the project
1. `veos workspace get --dir "<clips folder>"`.
   - A playbook is linked: use it, one line ("Using your **<name>** style").
   - Not linked, playbooks exist: one question with them as options (name + handle) plus "Create a new style"; then
     `veos workspace set --playbook <id> --dir "<clips folder>"`.
   - None, or "create": "First let's set up your editing style (a few minutes, once)", then invoke
     `vibe-editing-os:playbook` (pass any style or creator they named). It links the folder; carry on here.
   The playbook folder `PB` is `<playbooks>/<id>` (`veos paths` → `playbooks`); its `tokens.json` and `playbook.md`
   answer the style questions below.
2. What kind of reel, decided quietly: **talking head** (video of them speaking; the default), **faceless** (only audio,
   or "voice-over only", or `PB/tokens.json` → `profile.source_type` is `voiceover_only`), a **conversation** (two or
   more people), or **no voice** (nobody speaks): they say it's music-only, B-roll, a screen recording with text, or a
   photo or slide reel; or they gave only photos (and maybe a song); or `profile.source_type` is `no_voice`; or a
   talking-head prep finds no speech (transcribe returns almost no words and the clips' sound is music or ambience). If
   you only find out at transcribe, say so in one line and start again with `--no-voice`.
3. `veos project init "<clips folder or files>" [--script "<script>"] [--voiceover "<file>"]` → `P` is
   `<clips folder>/vibe-edit`. Pass a `script.md` / `script.txt` that sits next to the clips. Faceless: `--voiceover`
   names the voice-over (other clips become B-roll). Conversation: ask once who is who and who asks, and save it as
   `P/plan/cast.json` = `{"people": [{"name", "role": "host|guest"}], "files": {"<file>": "<name>"}}`.
   No voice: `veos project init "<folder or files>" --no-voice [--music "<song>"] [--script "<text file>"]`; always pass
   `--no-voice` (and `--music` when there's a song) yourself. Photos and slides in the folder are taken as sources.
   `--script` is the story the on-screen text tells (theirs, if they wrote one). No song given and none in the folder:
   ask once whether they have one; if not, the cut uses the clips' own sound.

## 2. Prep: the sound only
`veos ingest`, `veos conform --audio-only`, then `veos transcribe` (add `--script "<script>"` when there is one; it hears
the playbook's language, `profile.language.speech`, by itself). Transcribe takes a few minutes: run it in the background
and say so in one line.
**First regional reel** (Telugu, Tamil, Kannada, Malayalam, Bengali, Gujarati, Punjabi or Marathi speech): transcribe
downloads a bigger speech model once (~3 GB) and uses it from then on. Tell the creator in one line that this first one
takes longer. If the download fails, it still transcribes with the usual model and gives a warning.
**Conversation:** `veos conform`; with several files `veos sync` (the master is `MIX`, else the single file's id `M`);
`veos transcribe --id M`; `veos speakers --num <N>`, then `veos speakers name "S1=<name>:<role>" "S2=<name>:<role>"`;
`veos angles`.
**No voice:** `veos ingest`, `veos conform --audio-only`, then `veos beats` (the song's beat map: tempo, beats, bar
starts, where it gets bigger or drops). No transcribe.
Then `veos project set phase=prep`.

## 2b. Their words about the reel (optional, while the sound is being prepared)
While the sound is being prepared (transcribe or beats in the background), invite them once, in plain words, with no options to pick:
"While I prepare your clips: want to tell me about this reel in a few lines? What it's about, who it's for, the feeling
you want, and anything that must stand out (a moment, a number, a product, the ending). If you want a particular edit at
a particular point, say it like you'd tell an editor, e.g. *when I say "this website", show the website*, or *zoom in on
the price*. Or just say **skip** and I'll read it from the video."
- They write something: save it word for word as `P/plan/brief.md` (their words first, then nothing else), and say in one
  line what you took from it. It shapes the cut (what must stay, what leads) and the edit.
- They skip or don't answer by the time the cut is ready: carry on; never ask again for this reel.
- If they already described the reel when they started (in the /reel message), save that as the brief and don't ask.
- No voice: the same invitation; what they describe is the story the on-screen text should tell.

## 3. Make the cut yourself
The cut is where the rhythm starts. You decide it like an editor; the engine only cuts.
1. Read `veos roughcut-candidates` → `P/work/roughcut.candidates.json` (sentences per clip with times, take groups with a
   default pick, false starts, pauses, fillers, and a mechanical `suggested_edl` to start from) and `veos context --part
   words` (every word with its time; `?` = the speech model wasn't sure). Read how this style cuts: the playbook's footage
   section and any line about pauses, breaths, tightening or jump cuts (Grep `PB/playbook.md`), and `PB/learned.md` →
   `cut` entries.
2. Decide:
   - **Takes:** the best take of every line, usually the last complete, fluent one. When takes compete, look:
     `veos look --src <clip id> --at <t1>,<t2>,<t3>` (eyes closed, looking away or a flub loses).
   - **Stumbles:** false starts and stutters out; deliberate repeats stay ("alag alag").
   - **Dead air:** no silence of 0.6 s or more survives unless it's a beat you mean (the hold before a reveal). Shorter
     pauses follow the style: a fast style tightens them to about 0.12 s, a style that breathes keeps them.
   - **The cut follows the audio, not the words:** `roughcut-candidates` pauses with `kind: audio` are real silences even
     when words lie on them (`under_words`, `inside_word`); words the transcript marked suspect are already left out.
     Never cut a word for its language or `?`.
   - **Order:** the script's, else the story's (hook, promise, items, payoff, call to action). Their notes win ("put the
     last clip after I say let me show you"). What their brief (`P/plan/brief.md`) says must stand out stays in the cut.
   - **Cut points** on word boundaries: about 0.04 s before the first word, 0.08 s after the last. A clean single take is
     one segment; never cut for the sake of cutting.
3. Write `P/work/edl.json` in source seconds: `{"version": 1, "fps": 30, "segments": [{"src": "A", "in": 0.41, "out": 3.21,
   "note": "hook, take 2"}]}`, then `veos cut "P/work/edl.json"`. After `veos cut`, read `dead_air` (edit seconds, every
   silence ≥ 0.6 s by the audio) and tighten anything you didn't mean; read `dropped_speech`: an entry with
   `clipped: true` means a cut point at `cut_at` falls inside speech — widen that segment.
   - **Faceless:** a clean read is `veos cut --identity --tighten` (`--max-pause <s>` for the style's longest pause, plain
     `--identity` when it breathes); a read with retakes gets an EDL with `"src": "V"`.
   - **Conversation longer than 150 s:** `veos shots mine --min 60 --max 150` and keep the strongest self-contained moment;
     never cut anyone off mid-sentence.

**No voice: cut by eye, on the beat.** There are no words to read: you choose the shots by looking.
1. Look at every source: `veos look --src <id> --at <t1>,<t2>,…` (a clip: a frame every second or two; a long screen
   recording: the moments where something happens). `veos context --part beats` → the tempo, bar starts (`bars`),
   `sections` (`up` = the song gets bigger, `down` = it drops away) and `hits`.
2. Decide the story the pictures tell, in the playbook's order of hook → build → payoff → CTA. The hook is the most
   striking shot, on the first bar. Each shot lasts what it needs to be read (B-roll 0.5–2 s, a photo 1.5–3 s, a screen
   action as long as the action) and the big change in the song (the first `up` section) gets the best shot. Screen
   recordings play in recorded order; cut out the waiting, keep each action whole.
3. Write `P/work/edl.json`: clips `{"src": "S1", "in": 2.0, "out": 3.4, "note": "…"}`, photos `{"src": "S3", "still": true,
   "dur": 2.0}` (add `"fit": "blur"` for a slide or a landscape photo you must see whole; `auto` picks it already when the
   crop would lose too much), and on top `"audio": "music", "music": {"in": <the bar where the song should start>}`
   (usually the first bar, `bars[0]`; a later bar to start on the chorus). Then `veos cut "P/work/edl.json" --snap-beats`
   (every cut lands on a beat; `--snap-beats bars` for slower, bar-length shots; `"snap": false` on a segment you want off
   the grid). Check `cuts_on_beat` and `snapped.off_grid` (segments that had no room to reach a beat: lengthen their
   `out` or accept them). No speed-up here: the music keeps its tempo.
4. Their clips' own sound instead of music: `--audio clips`; silence: `--audio none`.

## 4. Show the cut (stop one)
Open `P/work/cut_proxy.mp4`, the cut as a small video with sound: PowerShell `Start-Process "<path>"`, macOS
`open "<path>"`, Bash on Windows `powershell -NoProfile -Command "Start-Process '<path>'"` (or give the path). In two or
three lines: how long it is and from how much footage, what went (retakes, false starts, dead air, misheard bits), and any close call worth a look.
No voice: the cut plays with the music. Say the tempo, how many shots, and that every cut is on the beat (or which ones
aren't and why).
Ask: "Happy with the cut? Approve it, or tell me what to change." Wait.
- **Changes:** restate each in one line, change `edl.json`, `veos cut` again, show it again.
- **Faster:** speed comes from the playbook (`cut.speed`) automatically; when they ask, `veos cut "P/work/edl.json"
  --speed 1.2`; `--speed 1` turns it off. Never re-encode the video yourself.
- **Approve:** `veos project set phase=roughcut`.

## 5. Ready the footage, then the edit
- **Talking head:** `veos faces`, then `veos prep-frames` (about a minute; only the seconds the cut keeps). If
  `PB/tokens.json` says `"matte": "required"`, start `veos matte` in the background now: the person cut-out takes
  minutes and is ready by the time the edit needs it. Nothing else heavy runs alongside it.
- **Conversation:** `veos prep-frames` comes after the edit's `veos shots render`; nothing here.
- **No voice:** `veos prep-frames` only (no faces, no cut-out).
- Then invoke skill `vibe-editing-os:edit` with `P`. It makes the reel, shows the storyboard (stop two), applies their
  changes, and hands to `vibe-editing-os:render` on approval.

**Never modify the creator's clips;** everything is written inside `P`. If an engine command crashes, run `veos doctor`
once, tell them plainly what failed, suggest `/vibe-editing-os:setup update`, and stop. Never patch the engine.
