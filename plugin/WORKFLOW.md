# Workflow: the `vibe-editing-os` plugin

The plugin is the raw workflow that produced the best reels, run as five skills on Opus at high effort, with no
subagents and no check gates:

1. A playbook holds the creator's style (picked by eye, or written: interview → reels they love → first playbook →
   an elevate pass for motion graphics and retention).
2. The editor cuts the raw clips itself and shows the cut as a video.
3. The editor reads the playbook like a creative director, looks at the reel itself, plans on its own, codes what it
   ideated, looks at its own storyboard once, and shows it.
4. The creator asks for a few changes, approves, and gets the final video.

## 1. User experience
```
/vibe-editing-os:setup                 install / update / licence (once)
/vibe-editing-os:playbook              the creator's style (once per account; reel runs it when there is none)
/vibe-editing-os:reel <clips folder>   style → prep → the cut → ⛔ approve the cut (video)
                                       → edit → ⛔ approve the storyboard → render → final.mp4
/vibe-editing-os:reel                  (no args) resume the latest project where it stopped
"approve" / "hook thoda fast karo"     continue / change
```
**Two stops per reel, and only two:** the cut (a video with sound) and the storyboard. No inputs round, no concept gate,
no title gate. Third-party logos, screenshots and posts the reel needs are fetched from the web, with the source noted.

**Project folder:** `<clips folder>/vibe-edit/`.

## 2. Plugin layout
```
plugin/
  .claude-plugin/plugin.json   name "vibe-editing-os"
  bin/veos  bin/veos.cmd       wrapper → VEOS_HOME python -m veos (skills always call it by its full path)
  setup/install.ps1|sh         the installer (setup skill)
  skills/setup/SKILL.md        install, update, doctor, licence; PowerShell or Bash (user's own model)
  skills/playbook/SKILL.md     path A: a ready-made style by eye + the language; path B: interview → inspiration reels
                               → v1 (template format, The feel first) + tokens.json → elevate → v2 → preview → save
  skills/reel/SKILL.md         one reel: playbook, project init, prep (sound only), Opus makes the cut (edl.json →
                               veos cut), stop 1 = the cut video, faces + frames (+ the cut-out early when the style
                               requires it), → edit
  skills/edit/SKILL.md         the creative director's brief: read the playbook in full, look at the reel, captions,
                               fetch from the web, plan/ideas.md, timeline.json + scenes.js written section by section,
                               sounds, storyboard, one look and one fix pass, stop 2 = the storyboard, changes, → render
  skills/edit/REFERENCE.md     the mechanics: commands, timeline and scene fields, sound cues, cut-out, storyboard sheets
  skills/edit/SOUNDS.md        every usable sound with its description (generated: tools/sounds_list.py)
  skills/render/SKILL.md       render → voice → sfx → mix → assemble → qa → hand over final.mp4
```
Every skill except `setup` runs on `claude-opus-5-5` at `effort: high`. There are no agents. Skills reference app files
through `veos paths`, never hard-coded paths.

## 3. Phases (`project.json`, set only with `veos project set`)
| Phase | Done when | Skill |
|---|---|---|
| `init` | project.json exists | reel |
| `prep` | sources.json, audio/, words/ for every source (sound only: `conform --audio-only`, `transcribe`) | reel |
| `roughcut` | edl.json, cutmap.json, words.edit.json, **and the creator approved the cut** (cut_proxy.mp4) | reel |
| `captions` | caption fixes applied (`veos captions apply`) | edit |
| `plan` | plan/timeline.json + plan/scenes.js written and `veos scenes-meta` clean | edit |
| `storyboard` | review/mockup.html built, looked at once by the editor, and shown | edit |
| `approved` | the creator approved the storyboard (`approved_at`) | edit |
| `render` / `done` | out/final.mp4 assembled and `veos qa` run | render |

Every phase is resumable: re-running a command reuses what's cached. The engine never requires a phase value, a passing
validate, a scene plan or a brief: `storyboard` needs `plan/timeline.json` + `plan/scenes.js` (+ footage frames for a
talking head); `render` needs the bundle.

## 4. The command path of one talking-head reel
```
project init → ingest → conform --audio-only → transcribe (background)
roughcut-candidates + context --part words → work/edl.json → cut → cut_proxy.mp4  ⛔
faces → prep-frames (→ matte in the background when tokens footage.matte = required)
look + context --part all → captions status / apply
plan/ideas.md → plan/timeline.json → plan/scenes.js (section by section) → scenes-meta
(matte --if-needed → prep-frames, when the edit puts something behind the person)
storyboard → sheet (review/mockup/anim → review/watch/reel_N.jpg) → look, one fix pass → mockup.html  ⛔
prep-frames → bundle → render (background) ‖ voice → sfx → mix → assemble → qa → out/final.mp4
```
Faceless: no faces / matte / frames; `cut --identity --tighten`; the stage is hidden and every second is scenes.
Conversation: sync → transcribe the master → speakers → angles; `shots plan` / `shots render` before `prep-frames`.

## 5. What the engine checks, and what it doesn't
Only the build blocks: the scene code must load (`scenes-meta`), the storyboard and render must complete, the final file
must pass `veos qa` (size, frame rate, loudness, sync) and the mix must keep sounds under the voice. `veos validate`,
`measure`, `stills` and `figures` are tools the editor may use when something looks broken, never a gate or a loop. Taste
and craft are judged by eye on the storyboard (`playbooks/_global/GLOBAL-RULES.md`).

## 6. Engine commands the skills use
`project init|show|set|latest`, `workspace get|set`, `playbook new-id`, `templates list|gallery|copy`, `learn add`,
`ingest`, `conform`, `transcribe`, `sync`, `speakers`, `angles`, `roughcut-candidates`, `context`, `look`, `cut`,
`faces`, `matte`, `prep-frames`, `captions status|apply`, `asset add`, `scenes-meta`, `storyboard`, `sheet`, `stills`,
`bundle`, `render`, `voice`, `sfx`, `mix`, `assemble`, `qa`, `paths`, `doctor`, `licence`. Details: `engine/SPEC.md`,
renderer: `renderer/CONTRACT.md` and `renderer/SCENES-API.md`.
