# Robot: five realistic directions (owner picks one)

Brief from the owner (2026-09-30): more realistic, more human, less "killer",
some charred flesh. Every option keeps a warm, teacher-like presence so it
reads as protective, not threatening.

**Guardrail:** burnt skin peeling back to reveal a *chrome skull with red eyes*
is the Terminator's signature look. We avoid chrome skulls, red eyes, leather
jackets, and sunglasses, and show the substructure as a different material
(ceramic, copper, carbon, glass) so the design stays original. Damage stays
non-graphic: scorched synthetic skin, no blood or open wounds, which keeps it
fine for a 14-30 audience.

All prompts share: `photorealistic head-and-shoulders portrait, 3/4 view,
soft cinematic key light, dark blue-grey studio background, shallow depth of
field, 85mm, highly detailed skin and material texture, original character
design, no text, no logo`.

## 1. "The Medic" (warmest)
A calm, mid-40s-looking android with kind, tired eyes (warm hazel irises with
a faint amber ring). Synthetic skin is mostly intact; the left cheek and jaw
are scorched and peeled back to show **white ceramic plating with hairline
cracks**. Rolled-sleeve field jacket, stethoscope-like cable around the neck.
*Feels like:* the veteran nurse who has seen everything.
Prompt: `android man mid-40s appearance, gentle hazel eyes with subtle amber
ring, left cheek and jawline synthetic skin scorched and peeled revealing white
ceramic plating with hairline cracks, olive field jacket with rolled sleeves,
thin cable draped around neck like a stethoscope, calm warm expression`

## 2. "The Lineman" (grid-down survival)
A broad-shouldered utility-worker android: hard hat pushed back, reflective
vest singed at the edges. Burns across the right temple and ear expose
**copper wiring and brass fittings**, like the inside of a fuse box. One
brow slightly raised, half-smile.
*Feels like:* the guy who gets your power back on at 3 a.m.
Prompt: `android utility lineman, weathered friendly face, scuffed white hard
hat tilted back, singed high-visibility vest, right temple and ear synthetic
skin burned away revealing neat copper wiring and small brass fittings, soot
smudges, wry half smile, one eyebrow raised`

## 3. "The Professor" (cybersecurity teacher)
Slim, bookish android in a worn cardigan and round wire glasses (one lens
cracked). A scorch mark along the neck and collarbone reveals **transparent
glass-like skin over softly glowing blue circuitry**. Pen behind the ear.
*Feels like:* your favorite professor who also survived a server-room fire.
Prompt: `android professor, slim build, thoughtful expression, round wire
glasses with one cracked lens, worn grey cardigan over collared shirt, pen
behind ear, scorch mark on neck and collarbone revealing translucent glass-like
skin over faint glowing blue circuitry, curious gentle eyes`

## 4. "The Survivor" (most dramatic, still friendly)
Young-adult-looking android with a buzzed haircut and a scarf, recently
through a fire: patchy soot, **a third of the face charred to matte black
carbon-fiber**, the rest human and smiling. One eye human, one a soft
white-blue lens (not red). Bandage wrapped across the forehead.
*Feels like:* the hero at the end of the disaster movie, still cracking jokes.
Prompt: `young adult android, buzzed hair, soot-smudged face, right third of
face synthetic skin charred away showing matte black carbon fiber structure,
right eye a soft white-blue camera lens, left eye human and warm, cloth
bandage around forehead, tattered scarf, relieved grin`

## 5. "The Mechanic" (most humorous)
Stocky, older, grizzled android with a grey beard of fine wires, oil-stained
coveralls, and a welding visor flipped up. Heat damage on both hands and
forearms (visible in frame) shows **brushed-steel joints**; face mostly
intact with small burn freckles. Laugh lines.
*Feels like:* the uncle who fixes your car and your router while telling
dad jokes.
Prompt: `stocky older android mechanic, grey beard made of fine silver wires,
laugh lines, small burn freckles on cheeks, welding visor flipped up on head,
oil-stained navy coveralls, forearms and hands heat-damaged showing brushed
steel joints, hands raised mid-gesture, laughing`

## After the owner picks
1. Generate 4 variations of the chosen prompt (`higgsfield-api`, cheapest
   image model, log cost) and let the owner choose one face.
2. Lock it: `ref-front.png`, `ref-three-quarter.png`, and the exact prompt,
   model, and seed in this folder.
3. Animation for long-form: a 2.5D puppet built from the locked image (separate
   eye and jaw layers moved by the existing lip-sync pipeline), so it stays
   cheap to render every week.
