---
name: reel-render
description: Render phase of a reel project: render frames, mix audio, assemble final.mp4 and run QA. Only after the user approved the storyboard. Called by the reel orchestrator.
model: claude-opus-5-5
effort: high
user-invocable: false
---
# reel-render

Input: project folder `P`. Never hand-edit project.json; use `veos project`.

1. Gate: `veos project show --project "P"` must have `approved_at` set. If not, stop and tell the orchestrator the storyboard is not approved.
2. Gather values:
   - `veos paths` gives `renderer_player` (path of player.html) and the VEOS_HOME path.
   - `P/plan/timeline.json` `meta.frames` = N and `meta.duration` = D seconds.
   - Chunks folder `C` = `<VEOS_HOME>/scratch/<project name>/chunks` (project name = name of the folder that contains `vibe-edit`).
   - Bundle URL = `file:///` + absolute path of `P/work/render/bundle.js` with forward slashes and spaces as %20.
3. Delegate with the Agent tool (`subagent_type: "vibe-editing-os:veos-runner"`) these commands in order (Bash timeout 600000; render can take many minutes):
   - `veos render --html "<renderer_player>" --query bundle=<bundle URL> --frames N --out "C" --project "P"`
   - `veos voice --project "P"` (builds work/voice.wav from the rough-cut list; works for any number of clips, and for a faceless reel's voice-over)
   - `veos sfx --project "P"` (only if `plan/timeline.json` has `sfx` cues: builds work/sfx.wav from the catalogue)
   - `veos mix "P/work/voice.wav" "P/out/mix.wav" --dur D --project "P"`, adding `--sfx "P/work/sfx.wav"` when sfx.wav exists. It fails if the sounds are too loud against the voice.
   - `veos assemble --out "P/out/final.mp4" --chunks "C" --audio "P/out/mix.wav" --frames N --project "P"`
   - `veos qa "P/out/final.mp4" --expect-frames N --ref-audio "P/work/voice.wav" --project "P"`
4. If the verdict is `failed`: `veos project set --project "P" last_error="render: <reason>"` and stop with a plain-language message. Re-running resumes from cached chunks.
5. If the qa JSON does not show `all_pass` true: `veos project set --project "P" phase=render last_error="qa: <failed checks>"`, report the failures, and stop.
6. On pass: `veos project set --project "P" phase=render last_error=""`, then `veos project set --project "P" phase=done`.
7. Report to the orchestrator: absolute path of `P/out/final.mp4`, duration, frame count, and a one-line QA summary (resolution, fps, loudness, audio sync).

Optional side-by-side review: `veos sheet --video "P/out/final.mp4" --frames <list> "P/out/review"`.
