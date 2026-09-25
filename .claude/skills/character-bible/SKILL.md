---
name: character-bible
description: The source of truth for every recurring character, so each one looks and sounds the same everywhere. Use before drawing, animating, prompting, or writing dialogue for any recurring character, and when creating a new one.
---

# Character bible

## Roles

| Role | Character | Style | Made with |
|---|---|---|---|
| YouTube long-form host | `robot-host` (style test; owner names it) | 2D cartoon killer robot in a hoodie, SVG puppet, lip-synced to the owner's voice | Free tools (`video-assembly`) |
| PoolParty + The Sovereign promos | Not created yet (same cast for both brands) | Realistic AI actor(s) | `higgsfield-api`; **always AI-labeled** |
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

## Characters
- `robot-host`: hooded cartoon killer robot, long-form YouTube host. Working
  name; the owner picks the real name.
- Realistic promo cast (shared by PoolParty and The Sovereign): not created yet.
