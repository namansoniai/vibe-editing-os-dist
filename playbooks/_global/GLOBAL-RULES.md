# Global quality rules (apply to EVERY playbook, every reel; nothing overrides them)

Every edit made with Vibe Editing OS must look **premium**: clean, smooth, never cluttered. These rules sit above the creator's playbook, their learned feedback, and any reference reel.

**The validator checks G1–G3 automatically on the measured frames** (`veos measure` + `veos validate`). Fix every failure before the storyboard.

## G1 No overlapping
- **Nothing on screen overlaps anything else unless it's deliberately nested.** That covers text on text, a card over a caption, a chip over a title, and subtitles under a graphic.
  - A deliberate nesting (a chip pinned on its own card) must be declared in the scene with `overlaps: ["<card id>"]`. The validator then allows it.
- **Text never covers the face.** Only `behind: true` depth-sandwich graphics may pass behind the head.
- **Give every element its own space:**
  - Plan positions from the free bands (`veos context`).
  - Elements that appear together go on a clear grid, with at least 40 px between rects.
  - Subtitles get their band, and graphics stay out of it while subtitles show.

## G2 No clutter
- **At most 4 graphic elements on screen at once** (z 3–10). **At most 3 text blocks at once, subtitles included.**
- **One idea per screen:** when a new visual idea starts, the previous one exits first. Never stack a third card onto two.
- **Breathing room:** keep at least 64 px of margin to the frame edges and the safe zone. A layout that feels full is too full; remove the least important element.
- **Every element earns its place.** It shows what's being said. **No decoration for its own sake.**

## G3 Smooth motion
- **Every element enters and exits with eased motion** (expo-out / back-out entries 6–14 frames; exits 4–8 frames). Nothing just appears or disappears, except a deliberate hard cut declared with `cuts: [...]`.
- **No jumps:**
  - An element never teleports, jumping more than 90 px or resizing more than 25% between two frames, unless the jump is a declared event or cut.
  - Morph positions and sizes; don't swap them.
- **Hold before moving on:** text holds at least 0.25 s per word; titles at least 10 frames after they finish building.
- **Camera moves are eased** (no linear zooms); never two camera moves within 0.4 s.
- **Keep the frame rate honest:** keep each frame's render ≤ 30 ms so nothing stutters.

## G4 High quality (checked by the frame reviewer and the planner's self-check)
- Crisp text: real fonts from the playbook, measured to fit, never clipped, never smaller than 40 px on the final 1080×1920 frame (subtitles ≥ 54 px).
- Colours from the playbook tokens only; readable contrast; at most yellow (primary) + 2 bright hues per frame unless the playbook says otherwise.
- Visuals are **literal**: they show the exact thing being said (an app → a phone app, a dish → that dish, a number → that number).
- No placeholder text, no empty cards, no broken glyphs, no stock clichés.
