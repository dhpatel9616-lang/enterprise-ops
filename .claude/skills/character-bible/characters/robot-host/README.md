# Robot

**Shows:** Robot's long-form YouTube tutorials (16:9, `--layout wide`) on
grid-down survival, cybersecurity, history, and politics. Long-form content
only. Not for promos, ads, or PoolParty (those use realistic `promo-cast`).

## Concept
A friendly cartoon robot with a screen for a face that came back from a
war. It has seen how things break (power grids, passwords, governments), so
it shows beginners how to stay ready and think for themselves. Battered and
patched up, but warm: the damage says "survivor", never "threat".
Approachable and a bit goofy on the outside; sharp, witty, and caring
underneath.
**Status:** v4.1. The owner approved the cartoon direction and asked for
more battered, war-torn wear (2026-10-01). Original design: no red eyes, no
chrome skull, nothing lifted from film robots.

## Look
- Rounded-square steel-blue head with thick dark outlines, a glossy
  highlight, side "ear" bolts, and an antenna with a blinking red bulb.
- Face is a dark screen. Eyes are glowing mint pills with small brows that
  lift when it talks and glance slowly left and right. It blinks by
  squashing the pills.
- Mouth is drawn on the same screen (shapes A–H, X; see
  `reference-sheet.png`): a line when closed, ovals when open, a tongue
  for "L", teeth for "F/V".
- Battle damage (fixed positions, flat shapes): a cracked face screen
  over its left eye (that eye stutters now and then), bullet strikes with
  bare-metal rings, scorch marks, paint chipped to bare metal, scratches, a
  riveted patch plate, a cross of cream tape, a bent antenna, and a missing
  ear panel with red and yellow wires hanging out.
- Tattered brown scarf at the neck with a frayed tail; faded stencil "07"
  on its chest; tape wrapped around one forearm; one dead chest light.
- Boxy body with a chest panel: four blinking status lights and a gold bar
  (Wade gold `#B8975A`). Tube arms with round hands; its right arm waves
  (`--wave-at`).
- Scene: cozy navy workshop with soft shelves and boxes, a few drifting
  code symbols. In widescreen, Robot sits on the right third
  (`reference-pose.png`).
- Flat colors only: no filters, textures, or per-frame clip paths
  (rig performance rule).

## Palette
| Part | Hex |
|---|---|
| Body / shade / highlight | `#5B8DB8` / `#3E6A91` / `#8DB6D9` |
| Outline | `#14202E` |
| Face screen | `#0B1628` |
| Eyes, brows, mouth glow | `#8DF7E8` |
| Antenna bulb, tongue | `#FF5A3C` |
| Chest bar, accent | `#B8975A` |
| Tape, stencil | `#E9E2CF` |
| Bare metal (chips, scratches, strike rings) | `#C9D1D9` |
| Soot (scorch marks, bullet pits) | `#0E1620` |
| Scarf | `#7A5A3C` |
| Background glow / edge | `#1D3350` / `#0A121D` |

## Motion
Gentle bob (3 s), slight head tilt that leans in while talking, blink
roughly every 3 s, slow eye glance, antenna bulb blinks, chest lights
cycle, jaw-free mouth follows the voice on the screen.

## Voice
Performed by the owner (see `voiceover-workflow`). An ffmpeg robot filter can
be added if the owner wants it.

## Don't
- Don't show it hurting people or give real-world weapon or attack
  instructions; the menace is a joke, the advice is protective.
- Don't use it as a customer or testimonial (`content-rules`).
