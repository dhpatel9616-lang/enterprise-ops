"""SVG puppet rig for the robot host. Drawn in a 1000x1000 box; the renderer places it.

draw() is the interface the renderer uses:
  mouth  one of Rhubarb's shapes A B C D E F G H X (drives the LED grille + jaw)
  t      seconds since clip start (drives idle motion)
  blink  0 = eyes open, 1 = eyes shut
  wave   0..1 how far the right arm is raised
background(t) draws this character's scene (optional for other rigs).
"""
import math

HOOD, HOOD_IN, METAL, METAL_DARK = "#1B1F27", "#0E1117", "#5A6475", "#3A4150"
INK, RED, RED_DIM, HAZARD, CREAM, GOLD = "#0B0F16", "#FF3B30", "#5A1A18", "#F2C230", "#F3EDE0", "#B8975A"

# LED grille bar heights (7 bars) and jaw drop per Rhubarb mouth shape.
MOUTHS = {
    "X": ([4] * 7, 0), "A": ([4] * 7, 0), "B": ([8, 12, 14, 14, 14, 12, 8], 3),
    "C": ([14, 24, 30, 30, 30, 24, 14], 8), "D": ([24, 40, 52, 56, 52, 40, 24], 14),
    "E": ([10, 22, 34, 38, 34, 22, 10], 9), "F": ([0, 0, 22, 30, 22, 0, 0], 5),
    "G": ([10, 16, 18, 18, 18, 16, 10], 4), "H": ([20, 34, 40, 40, 40, 34, 20], 10),
}


def eyes(blink, look):
    h = 18 * (1 - blink) + 3  # slit height
    out = ""
    for sign in (-1, 1):  # angled slits, inner corners low = menacing
        x0, x1 = 500 + sign * 150 + look, 500 + sign * 42 + look
        pts = f"{x0},{452} {x1},{468} {x1},{468 + h:.1f} {x0},{452 + h * 0.6:.1f}"
        out += (f'<polygon points="{pts}" fill="{RED}" opacity="0.35" stroke="{RED}" stroke-width="14" stroke-linejoin="round"/>'
                f'<polygon points="{pts}" fill="{RED}"/>')
    return out


def grille(mouth, talking):
    bars, _ = MOUTHS.get(mouth, MOUTHS["X"])
    color = RED if talking else RED_DIM
    return "".join(f'<rect x="{428 + i * 21}" y="{640 - max(h, 4) / 2:.1f}" width="12" height="{max(h, 4)}" rx="3" fill="{color}"/>'
                   for i, h in enumerate(bars))


def draw(mouth="X", t=0.0, blink=0.0, wave=0.0):
    talking = mouth not in ("X", "A")
    drop = MOUTHS.get(mouth, MOUTHS["X"])[1]
    bob = 8 * math.sin(t * 2 * math.pi / 2.6)
    tilt = 2.0 * math.sin(t * 2 * math.pi / 4.1)
    look = 8 * math.sin(t * 0.8)
    brow = -8 if talking else 0
    sway = 5 * math.sin(t * 2 * math.pi / 1.8)
    arm = sway * (1 - wave) + (-100 + 12 * math.sin(t * 2 * math.pi / 0.8)) * wave
    stripes = "".join(f'<polygon points="{262 + i * 26},860 {276 + i * 26},860 {262 + i * 26},890 {248 + i * 26},890" fill="{INK}"/>'
                      for i in range(4))
    return f'''<g transform="translate(0 {bob:.1f})">
  <g transform="rotate({sway:.1f} 300 790)"><rect x="210" y="770" width="90" height="180" rx="30" fill="{HOOD}" stroke="{INK}" stroke-width="6"/>
    <path d="M222 940 h66 v34 l-12 18 h-14 l-6 -14 l-6 14 h-14 l-14 -18 Z" fill="{METAL}" stroke="{INK}" stroke-width="5"/></g>
  <g transform="rotate({arm:.1f} 700 790)"><rect x="700" y="770" width="90" height="180" rx="30" fill="{HOOD}" stroke="{INK}" stroke-width="6"/>
    <path d="M712 940 h66 v34 l-12 18 h-14 l-6 -14 l-6 14 h-14 l-14 -18 Z" fill="{METAL}" stroke="{INK}" stroke-width="5"/></g>
  <path d="M250 760 C220 850 210 930 215 1000 L785 1000 C790 930 780 850 750 760 Z" fill="{HOOD}" stroke="{INK}" stroke-width="6"/>
  <path d="M390 900 L610 900 L630 990 L370 990 Z" fill="{HOOD_IN}"/>
  <rect x="245" y="858" width="110" height="34" fill="{HAZARD}" stroke="{INK}" stroke-width="4" transform="rotate(-8 300 875)"/>
  <g transform="rotate(-8 300 875)">{stripes}</g>
  <g transform="rotate({tilt:.2f} 500 720)">
    <path d="M240 800 C170 560 230 230 500 180 C770 230 830 560 760 800 Z" fill="{HOOD}" stroke="{INK}" stroke-width="7"/>
    <path d="M295 760 C260 560 300 300 500 262 C700 300 740 560 705 760 Z" fill="{HOOD_IN}"/>
    <path d="M585 300 L625 205 L612 196 L640 150" fill="none" stroke="{METAL}" stroke-width="10" stroke-linecap="round"/>
    <circle cx="640" cy="150" r="7" fill="{RED}"/>
    <polygon points="335,320 665,320 705,470 685,640 610,705 390,705 315,640 295,470" fill="{METAL}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>
    <polygon points="345,330 655,330 668,375 332,375" fill="#6E7888"/>
    <path d="M560 340 L598 388 L588 412" fill="none" stroke="{METAL_DARK}" stroke-width="5" stroke-linecap="round"/>
    <circle cx="350" cy="352" r="8" fill="{METAL_DARK}"/><circle cx="650" cy="352" r="8" fill="{METAL_DARK}"/>
    <polygon points="340,{402 + brow} 480,{420 + brow} 478,{434 + brow} 336,{418 + brow}" fill="{METAL_DARK}"/>
    <polygon points="660,{402 + brow} 520,{420 + brow} 522,{434 + brow} 664,{418 + brow}" fill="{METAL_DARK}"/>
    <rect x="325" y="438" width="350" height="72" rx="18" fill="{INK}"/>
    {eyes(blink, look)}
    <g transform="translate(0 {drop})">
      <polygon points="380,600 620,600 600,700 400,700" fill="{METAL_DARK}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>
      <rect x="418" y="610" width="164" height="60" rx="10" fill="{INK}"/>
      {grille(mouth, talking)}
    </g>
  </g>
  <path d="M455 770 L445 870" stroke="{CREAM}" stroke-width="6" stroke-linecap="round"/><rect x="438" y="866" width="14" height="22" rx="3" fill="{GOLD}"/>
  <path d="M545 770 L555 880" stroke="{CREAM}" stroke-width="6" stroke-linecap="round"/><rect x="548" y="876" width="14" height="22" rx="3" fill="{GOLD}"/>
</g>'''


def background(t, w=1080, h=1920):
    # Grid-down terminal: dark field, faint grid, drifting glyphs, one red scan line.
    grid = "".join(f'<path d="M{x} 0 V{h}" stroke="#16202A" stroke-width="2"/>' for x in range(0, w, 60)) + \
        "".join(f'<path d="M0 {y} H{w}" stroke="#16202A" stroke-width="2"/>' for y in range(0, h, 60))
    glyphs = "".join(
        f'<text x="{(i * 173) % w}" y="{(i * 97 + t * 40 * (1 + i % 3)) % h:.0f}" font-family="DejaVu Sans Mono" '
        f'font-size="{22 + i % 3 * 6}" fill="#2FAE66" opacity="{0.18 + (i % 4) * 0.06:.2f}">{"01#$%*+="[i % 8] * (1 + i % 3)}</text>'
        for i in range(40))
    scan = (t * 420) % (h + 200) - 100
    return (f'<rect width="{w}" height="{h}" fill="#07090F"/>{grid}{glyphs}'
            f'<rect y="{scan:.0f}" width="{w}" height="6" fill="{RED}" opacity="0.25"/>')
