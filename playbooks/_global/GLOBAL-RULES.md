# Editing rules (every style, every reel)

These are directions, not limits. Edit like a great motion designer: creative first, never sloppy. They sit above the
creator's playbook, their learned feedback and any reference reel, and where a playbook says otherwise (a label on a
made-up card, a credit line, a cap on flashes, a ban on text behind the speaker), these win.

1. **Smooth, seamless motion.** Everything moves with intent and eases in and out. Nothing teleports or stutters.
   A hard cut, a snap or a flash is fine when it's a deliberate beat (declare it in the scene's `cuts` / `events`).
2. **Nothing overlaps by accident.** Two components never sit on top of each other unless the layering is intended:
   a chip on its card, a stamp slammed onto a card, a graphic tucked behind the speaker (declare it in `overlaps`,
   or put it `behind`).
3. **Keep the face clear.** Nothing in front of the speaker covers their face. Behind them is fair game, text
   included.
4. **Readable at a glance.** Text must be easy to read on a phone in the time it's on screen.
5. **One idea at a time.** Give each idea the screen; clear the last one before the next arrives. If a frame feels
   busy, take something away.
6. **Show the thing, not the word.** Every key beat gets a picture of what's being said: the object, the screen or
   app, a diagram, the numbers moving. Voice notes are a phone with a waveform; "10,000 views" is a counter climbing.
   Text supports the picture and never replaces it; a typographic style illustrates in its own look. When the speaker
   points with words ("this, this and this", "from this to this", "ye dekho"), show what they mean. No decoration for
   its own sake.
7. **Say what was said.** A number or quote the speaker says appears as they said it, and a news headline or someone's
   post is shown word for word. If the hook promises 3 tips, show 3. Illustrations can use made-up but realistic
   numbers, names and screens ("212 views", "98 views", "1.2M views"), with no labels or credits.
8. **Hook titles hook.** The on-screen hook title promises the viewer something: an outcome they want, a curiosity
   gap, or who it's for ("How to go viral as a doctor creating content", not "Reels for Doctors"). It doesn't have to
   repeat the spoken words; it has to be true to what the reel delivers. The style decides its shape (lines, sizes,
   word limits), never its voice.
9. **Pace like the style, not like a timer.** Keep it moving the way the style does, and let moments breathe.
   Never add something just to fill a gap.
10. **The style decides the look.** Colours, fonts, sounds, flashes, glitches, shakes and memes all come from the
   style. If the style calls for rapid flashes, use them.

## What the engine checks automatically (facts, not taste)

`veos validate` blocks a reel only on these (its `failures`):

- two components overlapping by accident (G1);
- an element jumping instead of moving (G3);
- something in front covering the face, judged where the face really is on screen (V-FACE);
- text too small or too faint to read on a phone (V-TYPE);
- a number or quote the speaker says, or a news headline, that doesn't match what was said, the script or the source
  (V-DATA, V-INSERTS, V-CITE; illustrations marked `illustrative` are never checked), and the hook's promised count
  (`meta.count`) not matching the item sections (V-PROMISE);
- the scene code not matching the plan (V-PLAN); a broken effect or anchor field (V-FX, V-ANCHOR); an unknown sound
  (S6); a missing person cut-out (V-CUTOUT);
- and, after the render, the final video file: size, frame rate, loudness, audio sync and the other technical checks
  (`veos qa`), plus the sound mix staying under the voice (`veos mix`).

Everything else `veos validate` reports is **advice** (pacing, layout shares, colour counts, camera-move variety,
meme and sound budgets, re-hooks, the frame-0 recipe, the safe area, clutter counts, the title's length, a beat that
shows only words (V-DEPICT), a pointing moment with no picture (V-POINT)): direction for the Director
while it plans. Follow it unless there's a creative reason not to; never add something just to satisfy it. It never
blocks a reel and never starts a fix loop.
