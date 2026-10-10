---
name: render
description: Render an approved Vibe Editing OS reel to its final video - frames, voice, sound effects, mix, assembly and a light technical check - and hand the creator the finished MP4. Called by the edit skill when the storyboard is approved; also use when the user says "render it" for an approved reel.
argument-hint: "[project folder]"
model: claude-opus-5-5
effort: high
---

# Render the reel

The creator approved the storyboard. Make the final video, check it's technically sound, and hand it over. No creative
changes here, no review rounds, nothing they didn't ask for.

**Running `veos`.** Commands work in PowerShell and in Bash: quote every path. Setup puts `veos` on the user PATH; if
`veos` isn't recognised, call the plugin's wrapper by its full path: `& "<plugin root>\bin\veos.cmd" ...` in PowerShell, `bash "<plugin root>/bin/veos" ...` in
Bash; the plugin root is two folders above this skill's base directory. `P` is the project folder; every project command
takes `--project "P"`. Use absolute paths for every file argument.

## Steps
1. `veos project show`: `approved_at` must be set. If it isn't, say the storyboard isn't approved yet and hand back to
   `vibe-editing-os:edit`.
2. `veos prep-frames` (cached; it adds anything the last change needs), then `veos bundle` → note its `url` and `frames`
   (N). `veos paths` → `renderer_player`. D = `meta.duration` in `P/plan/timeline.json`.
3. Tell the creator it's rendering and roughly how long (a minute of reel takes several minutes), then in the background:
   `veos render --html "<renderer_player>" --query "bundle=<url>" --frames N`
   It writes `P/work/render/chunk_*.mp4`. Re-running resumes; a `CHUNK_MISMATCH` names the `--range` to re-render.
4. While it renders (these are light):
   - `veos voice` → `P/work/voice.wav`.
   - When `timeline.sfx` has cues: `veos sfx` → `P/work/sfx.wav`. A sound that won't download is left out and named in
     its `warnings` (the rest plays): swap that cue's `id` for another of the same role (the edit skill's `SOUNDS.md`)
     and run it again.
5. `veos mix "P/work/voice.wav" "P/out/mix.wav" --dur D` (add `--sfx "P/work/sfx.wav"` when it exists). `SFX_TOO_LOUD`
   names the cues crowding the voice: lower their `db` in the timeline by 4–6, `veos sfx` and mix again.
6. When the render is done: `veos assemble --out "P/out/final.mp4" --chunks "P/work/render" --audio "P/out/mix.wav" --frames N`.
7. `veos qa "P/out/final.mp4" --expect-frames N --ref-audio "P/work/voice.wav"`. That's the whole check: size, frame
   rate, loudness, sync. If something fails, fix the cause once if it's obvious (a re-render range, a re-mix); otherwise
   tell them plainly what's off and still give them the file. A no-voice reel has no voice to sync; the check says
   `sync: skipped`.
8. `veos project set phase=render`, then `veos project set phase=done`. Open the video for them (PowerShell
   `Start-Process "<path>"`, macOS `open "<path>"`, Bash on Windows `powershell -NoProfile -Command "Start-Process '<path>'"`).

## Hand it over
In three lines: the path of `P/out/final.mp4`, its length, and the check result in plain words. Then offer: change
something in this reel, or edit the next one.

If an engine command crashes, run `veos doctor` once, tell them plainly what failed, suggest
`/vibe-editing-os:setup update`, and stop. Never patch the engine or encode video yourself.
