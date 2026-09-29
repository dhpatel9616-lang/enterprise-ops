"""SVG puppet rig for Robot ("Robot teaches Cybersecurity"): a humanoid,
combat-worn android bust. Drawn in a 1000x1000 box; the renderer places it.

draw() is the interface the renderer uses:
  mouth  one of Rhubarb's shapes A B C D E F G H X (drives the jaw)
  t      seconds since clip start (drives idle motion)
  blink  0 = eyes open, 1 = eyes shut
  wave   0..1 (unused: bust framing, kept for the renderer's interface)
background(t) draws this character's scene.
"""
import math, random

INK, EYE, SCARF = "#0E1013", "#FF6A2B", "#5B4432"

# Rhubarb shape -> (jaw drop px, mouth width px)
MOUTHS = {"X": (0, 150), "A": (0, 150), "B": (5, 150), "C": (15, 158), "D": (30, 170),
          "E": (18, 128), "F": (11, 92), "G": (7, 150), "H": (22, 150)}

_rng = random.Random(7)  # fixed seed: damage lands in the same place every frame
SCRATCHES = [(_rng.uniform(330, 670), _rng.uniform(150, 600), _rng.uniform(-40, 40), _rng.uniform(-10, 10)) for _ in range(38)]
# Pre-placed grime blotches (vector, cheap to render; a noise filter took ~1s/frame).
# Sampled inside simple ellipses (head) / a band (torso) so no clip-path is needed.
def _inside(n, cx, cy, rx, ry, size):
    out = []
    while len(out) < n:
        x, y = _rng.uniform(cx - rx, cx + rx), _rng.uniform(cy - ry, cy + ry)
        if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1:
            out.append((x, y, _rng.uniform(4, size), _rng.uniform(3, size * 0.6), _rng.uniform(0.06, 0.2)))
    return out
STAINS_HEAD = _inside(90, 500, 380, 125, 235, 14)
STAINS_BODY = _inside(80, 500, 1000, 300, 240, 18) + _inside(30, 255, 772, 95, 70, 14) + _inside(30, 745, 772, 95, 70, 14)
ARMOR_SCRATCHES = [(_rng.uniform(140, 860), _rng.uniform(700, 990), _rng.uniform(-60, 60), _rng.uniform(-14, 14)) for _ in range(46)]

DEFS = """<defs>
  <linearGradient id="paint" x1="0" y1="0" x2="0.4" y2="1"><stop offset="0" stop-color="#7A8266"/><stop offset="0.5" stop-color="#4E5540"/><stop offset="1" stop-color="#262A20"/></linearGradient>
  <linearGradient id="bare" x1="0" y1="0" x2="0.3" y2="1"><stop offset="0" stop-color="#C9CDD2"/><stop offset="0.5" stop-color="#8A9097"/><stop offset="1" stop-color="#43474D"/></linearGradient>
  <linearGradient id="dark" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3B3F45"/><stop offset="1" stop-color="#15171A"/></linearGradient>
  <linearGradient id="cloth" x1="0" y1="0" x2="0.2" y2="1"><stop offset="0" stop-color="#6E5642"/><stop offset="1" stop-color="#2A1F16"/></linearGradient>
  <linearGradient id="rim" x1="0" y1="0" x2="1" y2="0"><stop offset="0.75" stop-color="#7FB6FF" stop-opacity="0"/><stop offset="1" stop-color="#7FB6FF" stop-opacity="0.45"/></linearGradient>
  <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FFE2B0"/><stop offset="0.35" stop-color="#FF7A30"/><stop offset="1" stop-color="#FF3D00" stop-opacity="0"/></radialGradient>
  <radialGradient id="mouthGlow" cx="0.5" cy="0.2" r="0.9"><stop offset="0" stop-color="#FF6A2B"/><stop offset="0.6" stop-color="#5A1505"/><stop offset="1" stop-color="#0A0302"/></radialGradient>
  <radialGradient id="scorch" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#0B0806" stop-opacity="0.8"/><stop offset="1" stop-color="#0B0806" stop-opacity="0"/></radialGradient>
  <radialGradient id="shade" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#000" stop-opacity="0.55"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
  <linearGradient id="gun" x1="0" y1="0" x2="0.35" y2="1"><stop offset="0" stop-color="#8C939B"/><stop offset="0.5" stop-color="#5A6068"/><stop offset="1" stop-color="#2A2E33"/></linearGradient>
  <clipPath id="sockets"><ellipse cx="445" cy="425" rx="44" ry="21"/><ellipse cx="555" cy="425" rx="44" ry="21"/></clipPath>
</defs>"""


def stains(items):
    return "".join(
        f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="#1A1509" fill-opacity="{o:.2f}" transform="rotate({(x * 7) % 180:.0f} {x:.0f} {y:.0f})"/>'
        for x, y, rx, ry, o in items)


def scratches(items, color="#D8DCE0"):
    return "".join(f'<path d="M{x:.0f} {y:.0f} l{dx:.0f} {dy:.0f}" stroke="{color}" stroke-width="{1 + i % 2}" stroke-opacity="{0.18 + (i % 4) * 0.07:.2f}" stroke-linecap="round"/>'
                   for i, (x, y, dx, dy) in enumerate(items))


def dent(x, y, r):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#1A1C1F" fill-opacity="0.85"/>'
            f'<path d="M{x - r} {y} A{r} {r} 0 0 1 {x + r} {y}" fill="none" stroke="#D5D9DE" stroke-width="2" stroke-opacity="0.5"/>'
            f'<circle cx="{x}" cy="{y}" r="{r * 2.2:.0f}" fill="none" stroke="#2A2C2F" stroke-width="1.5" stroke-opacity="0.35"/>')


def chip(points):
    return f'<polygon points="{points}" fill="url(#bare)" fill-opacity="0.9"/>'


def eyes(blink, t):
    flicker = 0.35 + 0.65 * (0.5 + 0.5 * math.sin(t * 37) * math.sin(t * 5.3)) ** 2  # cracked right eye
    lid = 22 * blink
    out = '<rect x="390" y="395" width="220" height="60" fill="#050607"/>'
    for cx, op in ((445, 1.0), (555, flicker)):
        out += (f'<ellipse cx="{cx}" cy="425" rx="40" ry="22" fill="url(#glow)" fill-opacity="{op:.2f}"/>'
                f'<ellipse cx="{cx}" cy="425" rx="17" ry="9" fill="{EYE}" fill-opacity="{op:.2f}"/>'
                f'<ellipse cx="{cx - 5}" cy="422" rx="7" ry="3" fill="#FFE6C8" fill-opacity="{0.9 * op:.2f}"/>')
    out += ('<path d="M540 406 l10 12 l-5 8 l12 14 M550 418 l14 -5 M545 426 l-10 7" fill="none" stroke="#E8ECEF" '
            'stroke-width="1.6" stroke-opacity="0.8"/>')  # crack across the right lens
    if lid:
        out += f'<rect x="390" y="403" width="220" height="{lid:.1f}" fill="url(#gun)"/><rect x="390" y="{447 - lid:.1f}" width="220" height="{lid:.1f}" fill="url(#gun)"/>'
    return f'<g clip-path="url(#sockets)">{out}</g>'


def draw(mouth="X", t=0.0, blink=0.0, wave=0.0):
    drop, width = MOUTHS.get(mouth, MOUTHS["X"])
    talking = mouth not in ("X", "A")
    bob = 5 * math.sin(t * 2 * math.pi / 3.2)
    tilt = 1.8 * math.sin(t * 2 * math.pi / 4.7) + (1.2 if talking else 0)
    breath = 1 + 0.006 * math.sin(t * 2 * math.pi / 3.2)
    slats = "".join(f'<rect x="{500 - width / 2 + 8:.0f}" y="{566 + i * 7}" width="{width - 16}" height="4" rx="2" fill="#2A2D31"/>' for i in range(4))
    return f'''{DEFS}<g transform="translate(0 {bob:.1f})">
  <g>
    <path d="M430 610 C400 660 380 700 360 740 M570 610 C600 660 620 700 640 740" stroke="#1B1D20" stroke-width="16" fill="none"/>
    <g transform="translate(500 850) scale({breath:.4f}) translate(-500 -850)">
      <path d="M150 1000 C150 860 200 760 330 720 L670 720 C800 760 850 860 850 1000 Z" fill="url(#paint)" stroke="{INK}" stroke-width="5"/>
      <path d="M360 740 L640 740 L610 860 L390 860 Z" fill="url(#dark)" stroke="{INK}" stroke-width="4"/>
      <path d="M380 760 H620 M392 790 H608 M404 820 H596" stroke="#51565D" stroke-width="5"/>
      <path d="M140 770 C150 710 215 676 300 684 C352 690 378 732 370 796 C362 850 300 866 232 858 C172 850 136 818 140 770 Z" fill="url(#paint)" stroke="{INK}" stroke-width="5"/>
      <path d="M860 770 C850 710 785 676 700 684 C648 690 622 732 630 796 C638 850 700 866 768 858 C828 850 864 818 860 770 Z" fill="url(#paint)" stroke="{INK}" stroke-width="5"/>
      <path d="M130 770 C150 720 210 690 290 694" stroke="#A7AE8F" stroke-width="3" fill="none" stroke-opacity="0.5"/>
      {chip("150,800 185,782 205,806 176,826 158,818")}{chip("700,700 760,690 772,712 730,730")}{chip("540,880 600,872 590,905 548,900")}
      {dent(250, 760, 9)}{dent(282, 812, 6)}{dent(760, 780, 10)}{dent(810, 820, 7)}{dent(460, 930, 8)}
      <ellipse cx="770" cy="760" rx="70" ry="45" fill="url(#scorch)"/><ellipse cx="300" cy="930" rx="90" ry="50" fill="url(#scorch)"/>
      <text x="215" y="815" font-family="DejaVu Sans" font-weight="bold" font-size="38" fill="#C9C39A" fill-opacity="0.55" transform="rotate(-12 215 815)">07</text>
      {"".join(f'<circle cx="{x}" cy="{y}" r="5" fill="url(#bare)" stroke="{INK}" stroke-width="1.5"/>' for x, y in ((170, 740), (340, 700), (660, 700), (830, 740), (380, 980), (620, 980)))}
      {stains(STAINS_BODY)}{scratches(ARMOR_SCRATCHES)}
    </g>
    <path d="M300 700 C360 650 640 650 700 700 L720 760 C640 740 560 790 500 770 C440 790 360 740 280 760 Z" fill="url(#cloth)" stroke="{INK}" stroke-width="4"/>
    <path d="M640 720 L690 860 L664 850 L676 900 L650 880 L646 930 L622 870 L610 740 Z" fill="url(#cloth)" stroke="{INK}" stroke-width="4"/>
    <path d="M330 712 C400 690 600 690 670 712" stroke="#8A7058" stroke-width="3" fill="none" stroke-opacity="0.6"/>
  </g>
  <g transform="rotate({tilt:.2f} 500 640)">
    <rect x="452" y="590" width="96" height="110" rx="10" fill="url(#dark)" stroke="{INK}" stroke-width="4"/>
    <path d="M466 596 V700 M534 596 V700" stroke="url(#bare)" stroke-width="10"/>
    <path d="M488 600 C470 640 520 660 500 700" stroke="#A33A1E" stroke-width="5" fill="none"/>
    <ellipse cx="500" cy="630" rx="170" ry="30" fill="url(#shade)"/>
    <path d="M336 330 L352 320 L356 470 L340 462 Z M664 330 L648 320 L644 470 L660 462 Z" fill="url(#dark)" stroke="{INK}" stroke-width="4"/>
    <path d="M350 250 C350 160 425 118 500 118 C575 118 650 160 650 250 L656 372 C656 410 646 440 634 462 L620 556 C606 604 562 646 500 652 C438 646 394 604 380 556 L366 462 C354 440 344 410 344 372 Z" fill="url(#paint)" stroke="{INK}" stroke-width="6"/>
    <path d="M500 122 V352 M428 140 C408 210 402 290 404 352 M572 140 C592 210 598 290 596 352" stroke="#2C3026" stroke-width="3" fill="none" stroke-opacity="0.8"/>
    {chip("548,164 606,182 616,226 570,220 550,198")}{chip("368,300 398,288 404,330 372,340")}
    <path d="M372 392 C420 382 470 386 500 400 C530 386 580 382 628 392 L622 470 C600 500 574 520 556 548 L444 548 C426 520 400 500 378 470 Z" fill="url(#gun)" stroke="{INK}" stroke-width="5"/>
    <path d="M380 470 C400 500 420 520 440 550 L420 560 C400 530 384 506 372 474 Z M620 470 C600 500 580 520 560 550 L580 560 C600 530 616 506 628 474 Z" fill="url(#bare)" stroke="{INK}" stroke-width="3" fill-opacity="0.9"/>
    <path d="M486 440 L514 440 L520 500 L500 512 L480 500 Z" fill="url(#bare)" stroke="{INK}" stroke-width="3"/>
    <path d="M488 506 h8 M504 506 h8" stroke="#1A1C1F" stroke-width="4" stroke-linecap="round"/>
    <path d="M388 478 L424 470 L434 512 L404 528 Z" fill="#101113" stroke="{INK}" stroke-width="3"/>
    <path d="M398 484 C410 496 402 510 414 520 M406 478 C418 490 422 504 428 512" stroke="#C0392B" stroke-width="3" fill="none"/>
    <path d="M396 498 C404 506 410 516 406 524" stroke="#E0B040" stroke-width="3" fill="none"/>
    <path d="M364 372 C410 356 470 360 500 380 C530 360 590 356 636 372 L632 398 C590 386 530 388 500 404 C470 388 410 386 368 398 Z" fill="url(#dark)" stroke="{INK}" stroke-width="4"/>
    {eyes(blink, t)}
    <rect x="{500 - width / 2 - 6:.0f}" y="556" width="{width + 12}" height="{max(drop, 1) + 40}" rx="10" fill="url(#mouthGlow)" fill-opacity="{1 if drop else 0.12}"/>
    <g transform="translate(0 {drop})">
      <path d="M{500 - width / 2 - 8:.0f} 592 L{500 + width / 2 + 8:.0f} 592 L{500 + width / 2 - 14:.0f} 634 L{500 - width / 2 + 14:.0f} 634 Z" fill="url(#bare)" stroke="{INK}" stroke-width="4"/>
      <path d="M{500 - width / 2 + 10:.0f} 610 H{500 + width / 2 - 10:.0f}" stroke="#4B5057" stroke-width="3"/>
    </g>
    <rect x="{500 - width / 2 - 12:.0f}" y="548" width="{width + 24}" height="14" rx="4" fill="url(#bare)" stroke="{INK}" stroke-width="4"/>
    {slats if not drop else ""}
    {dent(610, 290, 8)}{dent(386, 230, 6)}{dent(590, 600, 5)}
    <ellipse cx="620" cy="220" rx="60" ry="42" fill="url(#scorch)"/><ellipse cx="420" cy="600" rx="40" ry="24" fill="url(#scorch)"/>
    {stains(STAINS_HEAD)}{scratches(SCRATCHES)}
    <path d="M350 250 C350 160 425 118 500 118 C575 118 650 160 650 250 L656 372 C656 410 646 440 634 462 L620 556 C606 604 562 646 500 652" fill="none" stroke="url(#rim)" stroke-width="10"/>
    <ellipse cx="450" cy="180" rx="90" ry="26" fill="#FFFFFF" fill-opacity="0.10"/>
  </g>
</g>'''


def background(t, w=1080, h=1920):
    # Dim bunker-lab: dark field, faint grid, drifting terminal glyphs, cool glow behind Robot.
    grid = "".join(f'<path d="M{x} 0 V{h}" stroke="#121A22" stroke-width="2"/>' for x in range(0, w, 60)) + \
        "".join(f'<path d="M0 {y} H{w}" stroke="#121A22" stroke-width="2"/>' for y in range(0, h, 60))
    glyphs = "".join(
        f'<text x="{(i * 173) % w}" y="{(i * 97 + t * 40 * (1 + i % 3)) % h:.0f}" font-family="DejaVu Sans Mono" '
        f'font-size="{22 + i % 3 * 6}" fill="#2FAE66" fill-opacity="{0.12 + (i % 4) * 0.04:.2f}">{"01#$%*+="[i % 8] * (1 + i % 3)}</text>'
        for i in range(40))
    return (f'<defs><radialGradient id="bg" cx="0.62" cy="0.45" r="0.6"><stop offset="0" stop-color="#23384F"/>'
            f'<stop offset="1" stop-color="#06080C"/></radialGradient></defs>'
            f'<rect width="{w}" height="{h}" fill="url(#bg)"/>{grid}{glyphs}')
