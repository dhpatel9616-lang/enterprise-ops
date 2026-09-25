# Robot host (working name; owner picks the real name)

**Role:** long-form YouTube host (The Sovereign's topics: cybersecurity,
hacking, grid-down survival, readiness). 2D, cartoonish, cheap to animate.
**Status:** style test, waiting for owner approval.

## Concept (draft for the owner to edit)
A decommissioned killer robot that switched sides. It knows exactly how
things break, so it teaches humans how to protect themselves and the people
they love. Sharp and witty, but caring underneath the menace. Original design;
it must never drift toward any existing film robot (no chrome skull
endoskeleton, no copied logos, no catchphrases from films).

## Look
- Dark charcoal hoodie, hood always up, framing the face. Cream drawstrings
  with small gold tips. Yellow/black hazard patch on the left shoulder.
- Angular gunmetal face plate with a lighter top plate, two corner bolts, and
  a scratch on the right. A snapped antenna pokes out of the hood, with a red
  tip.
- Black visor band with two angled red LED slit eyes, inner corners lower
  (menacing). Metal brow plates lift when it talks.
- Separate jaw plate that drops as it talks, holding a black speaker grille
  with 7 red LED bars that move with the voice (mouth shapes A–H, X; see
  `reference-sheet.png`).
- Three-fingered metal claws at the ends of the sleeves.
- Scene: near-black background, faint grid, drifting green terminal glyphs,
  a red scan line.

## Palette
| Part | Hex |
|---|---|
| Hoodie / inside hood | `#1B1F27` / `#0E1117` |
| Face metal / shadow / top plate | `#5A6475` / `#3A4150` / `#6E7888` |
| Visor, outlines | `#0B0F16` |
| LED eyes and mouth (on / idle) | `#FF3B30` / `#5A1A18` |
| Hazard patch | `#F2C230` |
| Drawstrings / tips | `#F3EDE0` / `#B8975A` (Wade Capital gold) |
| Background / grid / glyphs | `#07090F` / `#16202A` / `#2FAE66` |

## Motion
Slow bob (2.6 s), slight head tilt, visor eyes drift and blink roughly every
3 s, brows lift and jaw drops while talking.

## Voice
Performed by the owner (see `voiceover-workflow`). A light robotic filter
can be added in ffmpeg if the owner wants it.

## Don't
- Don't show it hurting people or giving real-world weapon instructions; the
  menace is a joke, the advice is protective.
- Don't use it as a customer or testimonial (`content-rules`).
