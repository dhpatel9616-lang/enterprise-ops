---
name: character-bible
description: The source of truth for every recurring character, so each one looks and sounds the same everywhere. Use before drawing, animating, prompting, or writing dialogue for any recurring character, and when creating a new one.
---

# Character bible

Each character has a folder in `characters/<id>/`:

| File | What it is |
|---|---|
| `README.md` | Description, personality, palette (hex), do/don't list, which brands use it |
| `rig.py` | The SVG puppet (the drawing itself), used by `studio/render_puppet.py` |
| `reference-sheet.png` | All 9 mouth shapes, for checking consistency |
| `reference-pose.png` | Hero pose in a real scene |

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
- `host-01`: sprout-headed cartoon host (working name; the owner picks the real
  name and which brand it belongs to).
