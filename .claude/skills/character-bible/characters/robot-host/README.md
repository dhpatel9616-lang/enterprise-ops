# Robot

**Show:** "Robot teaches Cybersecurity". **Used only for The Sovereign's
YouTube long-form videos** (16:9, `--layout wide`). Not for Shorts, ads, or
PoolParty.
**Status:** style test v2, waiting for owner approval.

## Concept
A retired killer robot that switched sides. It knows exactly how systems
break, so it teaches humans to protect themselves and the people they love.
The look is 3D-styled and a bit menacing, but whimsical: droopy "smug" eyelids,
a bandage on its head, a "2FA" sticker, a bent antenna with a blinking bulb.
Sharp and witty, caring underneath. Original design; never drift toward any
existing film robot (no skull endoskeleton, no film catchphrases).

## Look
- Rounded-box chrome head with soft shading, top highlight, and a bevel
  glint. Four corner rivets, side vents, and cylinder "ear" caps.
- Two big round camera-lens eyes in recessed sockets: glowing orange-red
  lenses with an iris ring, dark pupil, and two white highlights. Metal
  eyelids sit slightly droopy at rest, lift when it talks, and close to blink.
- Hinged jaw: a metal upper lip bar with white "teeth"; the lower jaw drops to
  show a glowing red mouth (mouth shapes A–H, X; see `reference-sheet.png`).
- Beige cross bandage (top right), yellow "2FA" sticker (top left), bent
  antenna with a pulsing red bulb.
- Ribbed metal neck. Dark charcoal hoodie with the hood down, cream
  drawstrings with gold tips, yellow/black hazard patch on the left shoulder.
  Three-fingered chrome hands; the right one can wave.
- Scene: dark navy room with a soft blue glow, faint grid, and drifting green
  terminal glyphs. In widescreen, Robot sits on the right third, leaving the
  left side for captions and graphics.

## Palette
| Part | Hex |
|---|---|
| Chrome (light / mid / dark) | `#B4BFCE` / `#6B7789` / `#2F3644` |
| Dark metal (sockets, ears, lip bar) | `#555F70` → `#1D222B` |
| Outlines | `#141820` |
| Lens (core / hot / rim) | `#FFE0B8` / `#FF8A4C` / `#E0352B` |
| Mouth glow | `#FF5A36` → `#140404` |
| Hoodie | `#343B48` → `#11141A` |
| Hazard / sticker | `#F2C230` |
| Bandage | `#E6C9A2` |
| Drawstrings / tips | `#F3EDE0` / `#B8975A` (Wade Capital gold) |
| Background glow / edge | `#27425E` / `#07090F` |

## Motion
Slow bob (2.6 s), slight head tilt, lenses drift, blink roughly every 3 s,
jaw follows the voice, antenna bulb pulses. The right hand waves when the
renderer's `--wave-at` is used.

## Voice
Performed by the owner (see `voiceover-workflow`). An ffmpeg robot filter can
be added if the owner wants it.

## Don't
- Don't show it hurting people or give real-world weapon or attack
  instructions; the menace is a joke, the advice is protective.
- Don't use it as a customer or testimonial (`content-rules`).
