---
name: character-bible
description: The source of truth for every recurring character, so each one looks and sounds the same everywhere. Use before drawing, animating, prompting, or writing dialogue for any recurring character, and when creating a new one.
---

# Character bible

## Roles

| Role | Character | Style | Made with |
|---|---|---|---|
| Long-form YouTube tutorials (grid-down survival, cybersecurity, history, politics) | `robot-host`, named **Robot** | cartoon robot with a screen face; SVG puppet lip-synced to the owner's voice | Free tools (`video-assembly`), `--layout wide` |
| Short-form promos (PoolParty, The Sovereign, The Global Aggregate) | `promo-cast` (approved by the owner) | Realistic AI adults | `higgsfield-api`; **always AI-labeled** |
| All other promos | None required | Motion graphics, text, screen recordings, product shots | Free tools first |

Don't put a character into a video just because one exists. Character-free
promos are normal.

## Folders
Each character has a folder in `characters/<id>/`.

**Cartoon characters:**

| File | What it is |
|---|---|
| `README.md` | Description, personality, palette (hex), do/don't list, which brands use it |
| `rig.py` | The SVG puppet (the drawing itself), used by `studio/render_puppet.py` |
| `reference-sheet.png` | All 9 mouth shapes, for checking consistency |
| `reference-pose.png` | Hero pose in a real scene |

**Realistic AI characters:**

| File | What it is |
|---|---|
| `README.md` | Description, personality, wardrobe, voice, which brands use it, do/don't list |
| `prompt.md` | The exact generation prompt, negative prompt, model, seed, and settings |
| `ref-front.png`, `ref-three-quarter.png`, `ref-full-body.png` | Approved reference images, attached to every new generation |

A realistic character is locked only after the owner approves its reference
images in a PR. Until then, don't use it in any post.

## Rules
- **Never redraw a character from memory.** Render from its `rig.py`. For AI
  image/video tools, attach `reference-pose.png` and paste the README's
  description and hex colors into the prompt.
- Changing a character's look = edit `rig.py`, re-render both reference PNGs
  (`python3 studio/render_puppet.py --character <id> --sheet
  .claude/skills/character-bible/characters/<id>/reference-sheet.png`), and
  open a PR so the owner sees the before/after.
- New characters must be original: not resembling any existing character,
  mascot, or real person (see `content-rules`). Names and brand fit come from
  the owner (see `brand-voice`).
- Characters are actors: never a fake customer or testimonial.
- **Rig performance:** use `fill-opacity` / `stroke-opacity`, never the
  `opacity` attribute on individual shapes, and avoid SVG filters and
  per-frame clip-paths. Each makes the renderer draw on a separate layer
  (Robot went from 0.5 s to 0.07 s per frame after this change). Target
  under 0.2 s per frame so a 10-minute video renders in about 20 minutes.

## Characters
- `robot-host` (**Robot**): long-form YouTube host only.
- `promo-cast`: four fictional adult friends (approved) for short-form promos
  of all three brands. Promotion only, never long-form content.
