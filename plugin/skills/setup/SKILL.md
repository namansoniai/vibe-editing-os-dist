---
name: setup
description: One-time install of the Vibe Editing OS engine on this computer (licence key, Python, ffmpeg, browser, AI models), or update it with "update". Also activates or checks the licence ("activate my licence", "licence status") and moves it to another computer ("move my licence", "new laptop", "deactivate this computer"). Run this first after installing the plugin.
argument-hint: "[update | licence | move]"
user-invocable: true
---
# setup

Installs everything the plugin needs into one folder (`VEOS_HOME`; Windows `%USERPROFILE%\VibeEditingOS`, or
`%LOCALAPPDATA%\VibeEditingOS` for an install from version 0.6.0 or earlier, which keeps working; macOS
`~/Library/Application Support/VibeEditingOS`). No admin rights, nothing else on the computer is changed.

Vibe Editing OS needs a **licence key** from the purchase email (it looks like `VEOS-XXXX-XXXX-XXXX-XXXX`). One key works
on **2 computers**. The engine checks it online about once a day and keeps working **offline for 7 days**. Only the key,
an anonymous computer id and the computer's name are sent.

**Shells.** On Windows you may have PowerShell only (Claude Desktop), Bash only, or both: every command here works in
either, written once when it's the same and twice (PowerShell / Bash) when it isn't. The **plugin root** is two folders
above this skill's base directory. **Running `veos`:** always the plugin's wrapper by its full path (a PATH change never
reaches this session): PowerShell `& "<plugin root>\bin\veos.cmd" <args>`, Bash `bash "<plugin root>/bin/veos" <args>`
(macOS, or Git Bash on Windows); `veos <args>` below always means this. Before the first install it prints
`ENGINE_MISSING`, which means: install.

**Beta first:** check whether the file `<plugin root>/setup/channel.json` exists (Glob or Read it; no shell needed). If it
does, this is the **beta** for Naman's editors: no licence key is needed and every style is unlocked. Follow **Beta**
below instead of everything about licence keys, and never ask for a key.

**Which part to run:**
- argument empty → **Install**
- argument `update` → **Update**
- argument `licence`, "activate my licence", or any engine command answered `LICENCE_REQUIRED` → **Activate the licence**
- argument `move`, "move my licence", "new laptop", "deactivate this computer", "free up a device" → **Move my licence**
- "licence status", "which plan am I on" → run `veos licence status` and say its `line` in plain words.

## Running the installer
The OS is in your environment details (win32 = Windows, darwin = macOS). Run it **in the background** (the shell tool's
background option; it can take 15–60 minutes, depending on the connection) with the key in the environment when there is one:
- Windows, PowerShell: `$env:VEOS_LICENCE_KEY='<key>'; powershell -NoProfile -ExecutionPolicy Bypass -File "<plugin root>\setup\install.ps1"`
- Windows, Bash: `VEOS_LICENCE_KEY='<key>' powershell -NoProfile -ExecutionPolicy Bypass -File "<plugin root>/setup/install.ps1"`
- macOS: `VEOS_LICENCE_KEY='<key>' bash "<plugin root>/setup/install.sh"`

No key (beta, update): leave out the `VEOS_LICENCE_KEY` part. Update: add `-Update` (Windows) or `--update` (macOS) after
the script path. The installer needs no git, Xcode or developer tools, and gets the app version that matches this plugin:
never suggest installing any of them. On a Mac, if macOS offers to install developer tools, the user clicks **Not Now**.

While it runs, read its background output every minute or two (or `install.log` in `VEOS_HOME`, with the Read tool). The
lines look like `[5/10] Installing the veos engine...`: give the user one short progress line each time the step number
changes, never the raw log. When "activating your licence" passes, say "Licence activated" once. The last line is JSON:
- `"ok":true`: run `veos doctor` and report plainly: ready or not, its `licence` line, and any failing check with its
  hint. If `doctor_ready` is false, name the missing piece and offer to run setup again. Its `notes` are advice, never a
  problem; skip the "veos on PATH" note (the skills always call the wrapper by its full path). With
  `"licence_pending":true` the licence server couldn't be reached (the install carried on without it): say its
  `licence_message` plainly and offer **Activate the licence** once they're online (other `licence_error` codes: **Licence
  answers**).
- `"ok":false` with `"step":"licence"`: handle `licence_error` with **Licence answers**, ask for the key again if that
  helps, and run it again with the new key (it resumes; everything done is skipped).
- `"ok":false` with `"step":"busy"`: another install is already running (an earlier background job or session): don't
  start one; follow that one's progress in `install.log` and report as above.
- `"ok":false` with `"step":"platform"` or `"disk"`: say the `error` as it is (it's already plain) and the `hint`. Nothing
  was downloaded. Disk: offer to run it again once space is freed. Platform: stop.
- `"ok":false` otherwise: the failing `step`, the `error` in one sentence, and the `hint`. Common causes: no internet, or
  antivirus HTTPS scanning / an office proxy (the hint names it when that's the cause). Offer to run it again: it resumes.

## Beta (only when `setup/channel.json` exists)
- **Install** (argument empty): run `veos doctor --quick` and `veos licence status`.
  - `ready: true` and the status says `"beta": true`: "The beta is installed and ready" and stop (offer
    `/vibe-editing-os:setup update`).
  - `veos` works but the status has no `"beta": true` (or says a licence is missing): "You have the regular version
    installed; I'll switch it to the beta (your playbooks are kept)", then **Update**.
  - otherwise: Install steps 2 and 4 below, asking **only** "Ready to install now?" (no key), and run the installer
    without a key. Skip "Licence activated".
- **Update**: as below. Afterwards `veos licence status` should say `"beta": true`.
- `licence`, `move`, "activate my licence", "licence status": "This is the beta: it needs no licence key, and every style
  is unlocked. Nothing to activate or move." Never run `veos licence activate` or `deactivate` in the beta.
- `LICENCE_REQUIRED` from any engine command means the regular engine is still installed: run **Update**.

## Install (argument empty)
1. Already installed? `veos doctor --quick`.
   - `ready: true`: say it's ready and stop (offer `/vibe-editing-os:setup update`).
   - `machine_ready: true` but `licence_ok: false`: only the licence is missing: **Activate the licence**.
2. Tell the user in plain words: it downloads about 3 GB (the editing engine with its own Python, the video tool ffmpeg, a
   rendering browser, and three AI models: speech-to-text, background removal, face detection); it takes 15–20 minutes
   on a fast connection and up to an hour on a slow one or a hotspot. Keep Claude open and the computer plugged in (it
   stays awake while installing); if it stops, run setup again: it resumes, half-done downloads included. It needs about 6 GB free to install (about 4 GB stay) plus about 1 GB of free
   space per minute of video while editing. Macs need Apple Silicon (M1 or later) and macOS 14 or newer.
3. One AskUserQuestion call, two questions:
   - **"Ready to install now?"** Options: "Yes, install now", "Not now".
   - **"Your licence key (from your purchase email)"**: "Pick *Other* and paste the key. It looks like
     VEOS-XXXX-XXXX-XXXX-XXXX." Options: "I can't find my key", "I haven't bought it yet".
   Then: "Not now" → stop politely. "I can't find my key" → "Search your inbox for 'Vibe Editing OS'. Or open
   https://veos-licence.shipwithoutcode.workers.dev/find-key and enter your payment ID (it starts with `pay_`, it's in the
   Razorpay receipt email) and the email you paid with", then ask for the key again (that question alone). "I haven't
   bought it yet" → a licence is needed to use Vibe Editing OS; stop. A pasted key: keep only its letters, digits and
   dashes. **Never repeat the full key back**; say "the key ending …XXXX".
4. **Running the installer** above, with the key. It activates the licence right after it installs the engine, before
   the big downloads, so a wrong key is caught in the first few minutes. If the licence server can't be reached, the
   install carries on and tries again at the end.

## Update (argument `update`)
**Running the installer** with the update flag and no key. It pulls the newest app version and reinstalls the engine
packages only if the engine changed; models, browser and ffmpeg that exist are kept, and the user's own playbooks in
`VEOS_HOME/playbooks` are never touched. Then `veos doctor` and report as above (if `licence_ok` is false, continue with
**Activate the licence**).

## Activate the licence (argument `licence`, or after `LICENCE_REQUIRED`)
1. `veos licence status`. If `active: true`: "Your licence is active: <plan> plan, <n> of 2 computers", and stop unless
   they want a different key.
2. Ask for the key with the licence-key question from Install step 3 (alone).
3. `veos licence activate --key '<key>'`.
   - ok: say its `message` in plain words. If it says `replaced_key`, mention the old key on this computer was replaced.
   - not ok: **Licence answers**.

## Move my licence (argument `move`)
This frees **this** computer's slot so the key can be activated on another computer.
1. `veos licence status`. Nothing active here: "This computer doesn't use a licence slot, so there is nothing to free. If
   your key says it's already on 2 computers, run this on one of those, or contact support." Stop.
2. Ask: "Free this computer's licence slot? Vibe Editing OS stops working here until you activate it again." Options:
   "Yes, free it", "No, keep it".
3. Yes: `veos licence deactivate`, say its `message`. On the new computer: install the plugin, run
   `/vibe-editing-os:setup`, paste the same key.
4. `LICENCE_OFFLINE`: "I couldn't reach the licence server, so this computer still counts. Check your internet and try
   again."
5. The old computer is lost or broken: "Contact support at enquiry@deccansoft.com, and we'll free the old computer's slot."

## Licence answers (error code → what to say, then the next step)
Never show the code or raw JSON; use the engine's `message` and `hint` in plain words:
- `KEY_INVALID`: "That key doesn't look right. Copy it from the purchase email (copy and paste works best); it looks like
  VEOS-XXXX-XXXX-XXXX-XXXX." Offer the find-key page. Ask again.
- `KEY_DISABLED`: "This key has been switched off. Please contact support at enquiry@deccansoft.com." Stop.
- `DEVICE_LIMIT`: "Your licence is already active on 2 computers. To use it here, free one of them: on the old computer,
  ask me to **move my licence**. If you can't use that computer any more, contact support at enquiry@deccansoft.com and
  we'll free the slot." Stop.
- `LICENCE_OFFLINE`: "I couldn't reach the licence server. Check your internet connection and try again. Once activated,
  you can keep working offline for 7 days." Offer to retry.
- `DEVICE_NOT_REGISTERED` or `LICENCE_REQUIRED`: "This computer isn't activated (or was moved to another computer)." Go
  to **Activate the licence**.
- anything else: the `message` and `hint`, one sentence each.

## Notes
- Faceless (voice-over) reels need the speech model, the browser and ffmpeg, not the background-removal or face models:
  if only those failed, say faceless reels already work and offer to run setup again for talking-head reels. No-voice
  reels (clips or photos cut to music) need only the browser and ffmpeg.
- Every engine command except `veos doctor`, `veos licence …` and `veos paths` needs an active licence (except in the
  beta); without one it answers `LICENCE_REQUIRED`.
- Never delete `VEOS_HOME`. To uninstall, first **Move my licence**, then delete that folder (`veos doctor` shows it
  as `home`; on Windows also `%LOCALAPPDATA%\VibeEditingOS` if an older version left one).
- Never edit, copy or create `VEOS_HOME/licence.json` by hand: it is signed and tied to this computer.
- Never patch, downgrade or edit the engine, and never ask the user to pick an engine fix. Report the failing step
  plainly and suggest `/vibe-editing-os:setup update`.
