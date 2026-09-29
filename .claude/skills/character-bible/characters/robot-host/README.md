# Robot

**Show:** "Robot teaches Cybersecurity". **Used only for The Sovereign's
YouTube long-form videos** (16:9, `--layout wide`). Not for Shorts, ads, or
PoolParty.

## Concept
A decommissioned combat android that switched sides. It has seen every way
systems get broken, so it teaches humans how to protect themselves and the
people they love. Humanoid and battle-worn, detailed rather than cartoonish;
sharp and witty, caring underneath. Original design; never drift toward any
existing film robot (no chrome skull endoskeleton, no film catchphrases).
**Status:** v3, still being refined with the owner.

## Look
- Humanoid android head: olive-drab armored cranium with panel seams, heavy
  dark brow ridge, gunmetal face plate with cheekbone plates and a nose
  bridge with two vents, a narrow jaw.
- Two recessed eye sockets with glowing orange lenses. The **right lens is
  cracked and flickers**. Metal shutters close to blink.
- Hinged lower jaw that drops to show a glowing orange mouth (mouth shapes
  A–H, X; see `reference-sheet.png`); horizontal slats when closed.
- Battle damage (fixed positions, same in every frame): bullet dents, bare
  metal where paint chipped, scorch marks, fine scratches, a missing cheek
  panel on its right showing red and yellow wires, grime.
- Neck of hydraulic pistons and a red cable. Olive armor torso with big
  shoulder pauldrons, faded stencil "07" on the left pauldron, rivets.
- Tattered brown scarf wrapped at the collar, one frayed tail hanging down.
- Cool blue rim light on its left edge from the room's screens.
- Scene: dim bunker-lab, dark navy glow, faint grid, drifting green
  terminal glyphs. In widescreen, Robot sits on the right third.

## Palette
| Part | Hex |
|---|---|
| Armor paint (light / mid / dark) | `#7A8266` / `#4E5540` / `#262A20` |
| Face plate gunmetal | `#8C939B` → `#2A2E33` |
| Bare chipped metal | `#C9CDD2` → `#43474D` |
| Dark metal (brow, neck, torso panel) | `#3B3F45` → `#15171A` |
| Eyes / mouth glow | `#FF6A2B` core, `#FFE2B0` hot spot |
| Scarf | `#6E5642` → `#2A1F16` |
| Stencil | `#C9C39A` |
| Rim light | `#7FB6FF` |
| Background glow / edge | `#23384F` / `#06080C` |

## Motion
Slow breathing bob (3.2 s), slight head tilt that leans in while talking,
blink roughly every 3 s, cracked lens flickers, jaw follows the voice.

## Voice
Performed by the owner (see `voiceover-workflow`). An ffmpeg robot filter can
be added if the owner wants it.

## Don't
- Don't show it hurting people or give real-world weapon or attack
  instructions; the menace is a joke, the advice is protective.
- Don't use it as a customer or testimonial (`content-rules`).
