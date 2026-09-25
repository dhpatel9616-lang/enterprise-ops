"""SVG puppet rig for Host-01. Drawn in a 1000x1000 box; the renderer places it.

draw() is the only interface the renderer uses:
  mouth  one of Rhubarb's shapes A B C D E F G H X
  t      seconds since clip start (drives idle motion)
  blink  0 = eyes open, 1 = eyes shut
  wave   0..1 how hard the right arm waves
"""
import math

SKIN, SHADE, CHEEK = "#7FC8A9", "#5FAE8C", "#F4A6A0"
INK, LEAF, HOODIE, NAVY = "#23313F", "#3E8E5E", "#F2B134", "#2E3A4B"
MOUTH_IN, TONGUE = "#3B1F2B", "#E86A7A"

# Rhubarb mouth shapes, centred on (500, 640).
MOUTHS = {
    "X": f'<path d="M462 636 Q500 662 538 636" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>',
    "A": f'<path d="M458 642 L542 642" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>',
    "B": f'<rect x="456" y="628" width="88" height="28" rx="14" fill="{MOUTH_IN}"/>'
         f'<rect x="466" y="630" width="68" height="11" rx="4" fill="#fff"/><rect x="466" y="644" width="68" height="10" rx="4" fill="#fff"/>',
    "C": f'<ellipse cx="500" cy="644" rx="44" ry="26" fill="{MOUTH_IN}"/>'
         f'<rect x="470" y="620" width="60" height="10" rx="4" fill="#fff"/><ellipse cx="500" cy="660" rx="24" ry="9" fill="{TONGUE}"/>',
    "D": f'<ellipse cx="500" cy="650" rx="50" ry="42" fill="{MOUTH_IN}"/>'
         f'<rect x="468" y="610" width="64" height="11" rx="4" fill="#fff"/><ellipse cx="500" cy="676" rx="30" ry="13" fill="{TONGUE}"/>',
    "E": f'<ellipse cx="500" cy="646" rx="34" ry="30" fill="{MOUTH_IN}"/><ellipse cx="500" cy="664" rx="18" ry="8" fill="{TONGUE}"/>',
    "F": f'<ellipse cx="500" cy="644" rx="18" ry="20" fill="{MOUTH_IN}" stroke="{INK}" stroke-width="5"/>',
    "G": f'<path d="M460 634 Q500 628 540 634 Q540 656 500 658 Q460 656 460 634 Z" fill="{MOUTH_IN}"/>'
         f'<rect x="472" y="630" width="56" height="12" rx="4" fill="#fff"/><path d="M462 652 Q500 664 538 652" fill="none" stroke="{TONGUE}" stroke-width="8" stroke-linecap="round"/>',
    "H": f'<ellipse cx="500" cy="646" rx="40" ry="30" fill="{MOUTH_IN}"/><ellipse cx="500" cy="630" rx="20" ry="10" fill="{TONGUE}"/>',
}


def eye(cx, look_x, look_y, blink):
    if blink > 0.6:  # shut: a soft closed-lid curve
        return f'<path d="M{cx-44} 474 Q{cx} 490 {cx+44} 474" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>'
    ry = 62 * (1 - blink)
    return (f'<ellipse cx="{cx}" cy="470" rx="48" ry="{ry:.1f}" fill="#fff" stroke="{INK}" stroke-width="6"/>'
            f'<circle cx="{cx+look_x:.1f}" cy="{474+look_y:.1f}" r="26" fill="{INK}"/>'
            f'<circle cx="{cx+look_x+9:.1f}" cy="{464+look_y:.1f}" r="8" fill="#fff"/>')


def draw(mouth="X", t=0.0, blink=0.0, wave=0.0):
    talking = mouth not in ("X", "A")
    bob = 10 * math.sin(t * 2 * math.pi / 2.2) + (4 if talking else 0)
    tilt = 2.5 * math.sin(t * 2 * math.pi / 3.7)
    look_x, look_y = 6 * math.sin(t * 0.9), 3 * math.sin(t * 1.3)
    brow = -6 if talking else 0
    sway = 6 * math.sin(t * 2 * math.pi / 1.6)
    arm = sway * (1 - wave) + (-95 + 25 * math.sin(t * 2 * math.pi / 0.6)) * wave
    freckles = "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="{SHADE}"/>'
                       for x, y in ((340, 560), (360, 575), (335, 585), (660, 560), (640, 575), (665, 585)))
    return f'''<g transform="translate(0 {bob:.1f})">
  <g transform="rotate({sway:.1f} 330 760)"><rect x="248" y="740" width="86" height="190" rx="43" fill="{HOODIE}" stroke="{INK}" stroke-width="6"/><circle cx="291" cy="930" r="34" fill="{SKIN}" stroke="{INK}" stroke-width="6"/></g>
  <g transform="rotate({arm:.1f} 670 760)"><rect x="666" y="740" width="86" height="190" rx="43" fill="{HOODIE}" stroke="{INK}" stroke-width="6"/><circle cx="709" cy="930" r="34" fill="{SKIN}" stroke="{INK}" stroke-width="6"/></g>
  <path d="M320 710 C290 800 280 900 292 1000 L708 1000 C720 900 710 800 680 710 Z" fill="{HOODIE}" stroke="{INK}" stroke-width="6"/>
  <path d="M400 860 L600 860 L585 940 L415 940 Z" fill="{NAVY}" opacity="0.85"/>
  <path d="M360 720 Q500 800 640 720" fill="none" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"/>
  <g transform="rotate({tilt:.2f} 500 700)">
    <path d="M500 250 Q490 200 512 150" fill="none" stroke="{LEAF}" stroke-width="10" stroke-linecap="round"/>
    <path d="M512 160 C470 120 430 140 420 170 C460 185 495 180 512 160 Z" fill="{LEAF}" stroke="{INK}" stroke-width="5"/>
    <path d="M512 150 C545 105 590 115 600 140 C570 165 530 165 512 150 Z" fill="{LEAF}" stroke="{INK}" stroke-width="5"/>
    <path d="M225 470 C230 300 370 225 500 225 C630 225 770 300 775 470" fill="none" stroke="{NAVY}" stroke-width="18" stroke-linecap="round"/>
    <path d="M500 240 C700 240 800 355 800 500 C800 665 680 745 500 745 C320 745 200 665 200 500 C200 355 300 240 500 240 Z" fill="{SKIN}" stroke="{INK}" stroke-width="7"/>
    <path d="M250 600 C300 700 420 730 500 730 C580 730 700 700 750 600 C700 680 600 715 500 715 C400 715 300 680 250 600 Z" fill="{SHADE}" opacity="0.6"/>
    <ellipse cx="350" cy="590" rx="42" ry="24" fill="{CHEEK}" opacity="0.8"/><ellipse cx="650" cy="590" rx="42" ry="24" fill="{CHEEK}" opacity="0.8"/>
    {freckles}
    <path d="M370 {392+brow} Q410 {372+brow} 450 {392+brow}" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
    <path d="M550 {392+brow} Q590 {372+brow} 630 {392+brow}" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
    {eye(410, look_x, look_y, blink)}{eye(590, look_x, look_y, blink)}
    {MOUTHS.get(mouth, MOUTHS["X"])}
    <circle cx="205" cy="505" r="48" fill="{HOODIE}" stroke="{INK}" stroke-width="6"/><circle cx="205" cy="505" r="20" fill="{NAVY}"/>
    <path d="M225 545 Q260 660 395 668" fill="none" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"/>
    <circle cx="405" cy="668" r="16" fill="{INK}"/>
  </g>
</g>'''
