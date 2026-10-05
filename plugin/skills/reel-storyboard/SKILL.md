---
name: reel-storyboard
description: Storyboard phase of a reel project: build tokens, frames and the bundle, render storyboard stills, run an automated layout check, and open the mockup for the user. Called by the reel orchestrator after the plan validates.
user-invocable: false
---
# reel-storyboard

Input: project folder `P`. Precondition: `P/plan/timeline.json` validated (`passed: true`); otherwise stop and return to the orchestrator.

1. Delegate with the Agent tool (`subagent_type: "vibe-editing-os:veos-runner"`) with the project path and, in order:
   - `veos tokens --project "P"`
   - `veos prep-frames --project "P"`
   - `veos bundle --project "P"`
   - `veos storyboard --project "P"`

   Tell it to use Bash timeout 600000 and stop at the first failure.
2. If the verdict is `failed`: `veos project set --project "P" last_error="storyboard: <reason>"` and stop with a plain-language message.
3. Check that `P/review/mockup.html` and `P/review/mockup/still_*.jpg` exist (Bash `ls`).
4. Build ONE contact sheet: `veos sheet "P/review/mockup" "P/review/mockup/sheet" --per 24 --cols 6 --tile 240 --project "P"`. If it makes several sheets, review only the first four.
5. Delegate (`subagent_type: "vibe-editing-os:frame-reviewer"`) with: the sheet paths, a 5-line beats summary from `plan/timeline.json` (beat start times and main component ids), and this checklist: face covered? text overlapping text? element off-screen? text unreadable (too small or low contrast)? empty frame longer than 1 s? broken glyphs or emoji?
6. Parse its JSON list. If empty, continue. If it has issues, do NOT fix creative things here: return them verbatim (frame, issue, layer_hint) to the orchestrator, which revises the plan and calls this skill again. Do not open the mockup for the user in that case.
7. Open the mockup for the user:
   - Windows: PowerShell `Start-Process "<absolute path to P/review/mockup.html>"`
   - macOS: `open "<path>"`

   If opening fails, just print the path.
8. `veos project set --project "P" phase=storyboard last_error=""`.
9. Reply: mockup path, duration, number of beats, "layout check: clean". The orchestrator owns the approval gate; do not ask for approval yourself.
