"""SVG puppet rig for Robot (long-form tutorials): a battle-worn cartoon
robot with a screen for a face. Flat colors and thick outlines, so frames render fast.
Drawn in a 1000x1000 box; the renderer places it.

draw() is the interface the renderer uses:
  mouth  one of Rhubarb's shapes A B C D E F G H X (drawn on the face screen)
  t      seconds since clip start (drives idle motion)
  blink  0 = eyes open, 1 = eyes shut
  wave   0..1 raises Robot's right arm in a wave
background(t) draws this character's scene.
"""
import math

INK, BODY, SHADE, LIGHT = "#2A1622", "#E07FA6", "#B9567F", "#F6B8CF"
SCREEN, GLOW, BULB, GOLD = "#0B1628", "#8DF7E8", "#FF5A3C", "#B8975A"
METAL, SOOT, SCARF = "#C9D1D9", "#0E1620", "#7A5A3C"

# War damage, fixed positions so it's identical every frame. Flat shapes only (rig performance rule).
def scorch(x, y, rx, ry):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{SOOT}" fill-opacity="0.45"/><ellipse cx="{x}" cy="{y}" rx="{rx * 0.55:.0f}" ry="{ry * 0.55:.0f}" fill="{SOOT}" fill-opacity="0.55"/>'


def dent(x, y, r):
    # bullet strike: dark pit, bare-metal ring, little radial cracks
    return (f'<circle cx="{x}" cy="{y}" r="{r + 5}" fill="{METAL}"/><circle cx="{x}" cy="{y}" r="{r}" fill="{SOOT}"/>'
            + "".join(f'<path d="M{x} {y} l{dx * r * 2.2:.0f} {dy * r * 2.2:.0f}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
                      for dx, dy in ((1, 0.3), (-0.6, 0.9), (-0.4, -1))))


def chip(points):  # paint chipped down to bare metal
    return f'<polygon points="{points}" fill="{METAL}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'


def scratches(lines):
    return "".join(f'<path d="M{x} {y} l{dx} {dy}" stroke="{METAL}" stroke-width="5" stroke-opacity="0.8" stroke-linecap="round"/>' for x, y, dx, dy in lines)


HEAD_DAMAGE = (scorch(645, 570, 85, 55) + scorch(325, 255, 55, 38) + scorch(672, 250, 30, 50)
               + chip("300,420 330,400 338,440 312,452") + chip("560,196 610,192 600,214 572,220")
               + dent(370, 230, 13) + dent(668, 300, 10) + dent(300, 560, 9)
               + scratches(((596, 612, 46, 20), (606, 628, 40, 16), (300, 480, 22, 40), (306, 500, 18, 36), (640, 200, 36, 10)))
               # riveted patch plate over a hole, upper left
               + '<rect x="350" y="200" width="70" height="56" rx="6" fill="#7E8C99" stroke="#14202E" stroke-width="6" transform="rotate(-8 385 228)"/>'
               + "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="#14202E"/>' for x, y in ((360, 213), (408, 206), (364, 250), (412, 243))))
# Cracked screen (lower right corner) and a missing ear panel with loose wires
SCREEN_CRACK = ('<path d="M668 312 L628 360 L642 378 L598 420 L610 436 L570 470 M628 360 L600 350 M642 378 L668 396 M598 420 L566 408" '
                'stroke="#E8F4FF" stroke-width="5" fill="none" stroke-opacity="0.75" stroke-linejoin="round"/>')
EAR_WIRES = ('<rect x="705" y="345" width="50" height="140" rx="20" fill="#0E1620" stroke="#14202E" stroke-width="10"/>'
             '<path d="M720 370 q30 30 6 60 q-14 20 18 44 M732 362 q-18 40 10 70" stroke="#FF5A3C" stroke-width="6" fill="none" stroke-linecap="round"/>'
             '<path d="M742 380 q-20 26 4 52" stroke="#E0B040" stroke-width="6" fill="none" stroke-linecap="round"/>')
BODY_DAMAGE = (scorch(640, 960, 95, 60) + scorch(350, 760, 60, 38)
               + dent(338, 900, 10) + dent(368, 948, 8) + dent(326, 970, 7) + dent(664, 790, 9)
               + chip("620,920 668,908 676,944 640,956") + chip("300,820 330,808 336,846")
               + scratches(((556, 936, 56, -16), (566, 956, 50, -14), (576, 976, 44, -12), (420, 930, 30, 20)))
               + '<text x="610" y="1000" font-family="DejaVu Sans" font-weight="bold" font-size="40" fill="#E9E2CF" fill-opacity="0.55" transform="rotate(-6 610 1000)">07</text>')
# Tattered scarf at the neck, one frayed tail
SCARF_SVG = ('<path d="M420 690 C460 668 540 668 580 690 L600 730 C550 716 450 716 400 730 Z" fill="#7A5A3C" stroke="#14202E" stroke-width="8" stroke-linejoin="round"/>'
             '<path d="M420 716 L350 820 L370 814 L352 856 L374 842 L370 876 L398 800 Z" fill="#7A5A3C" stroke="#14202E" stroke-width="8" stroke-linejoin="round"/>')

# Rhubarb shape -> mouth drawn on the screen (centre 500,505)
def mouth_svg(m):
    g = f'fill="{GLOW}" stroke="none"'
    return {
        "X": f'<rect x="465" y="500" width="70" height="10" rx="5" {g}/>',
        "A": f'<rect x="470" y="500" width="60" height="10" rx="5" {g}/>',
        "B": f'<rect x="460" y="494" width="80" height="22" rx="11" {g}/>',
        "C": f'<ellipse cx="500" cy="505" rx="42" ry="22" {g}/>',
        "D": f'<ellipse cx="500" cy="510" rx="50" ry="34" {g}/><ellipse cx="500" cy="522" rx="26" ry="10" fill="{SCREEN}"/>',
        "E": f'<ellipse cx="500" cy="506" rx="32" ry="20" {g}/>',
        "F": f'<ellipse cx="500" cy="506" rx="16" ry="14" {g}/>',
        "G": f'<rect x="462" y="498" width="76" height="16" rx="8" {g}/><rect x="476" y="492" width="48" height="8" rx="3" fill="#FFFFFF"/>',
        "H": f'<ellipse cx="500" cy="508" rx="44" ry="26" {g}/><ellipse cx="500" cy="500" rx="18" ry="8" fill="{BULB}"/>',
    }.get(m, None) or mouth_svg("X")


def eyes(blink, t, talking):
    look = 6 * math.sin(t * 2 * math.pi / 7.3)           # slow glance left/right
    h = max(6, 64 * (1 - blink))
    brow = -6 if talking else 0                            # brows lift a little while talking
    out = ""
    glitch = (t * 1.7) % 4.3 < 0.12  # the damaged eye stutters briefly every few seconds
    for cx in (430, 570):
        dim = 0.3 if cx == 570 and glitch else 1
        out += f'<rect x="{cx - 24 + look:.1f}" y="{430 - h / 2:.1f}" width="48" height="{h:.1f}" rx="{min(24, h / 2):.1f}" fill="{GLOW}" fill-opacity="{dim}"/>'
        out += f'<path d="M{cx - 26 + look:.1f} {382 + brow} q26 -12 52 0" stroke="{GLOW}" stroke-width="8" fill="none" stroke-linecap="round"/>'
    return out


def arm(side, raise_amt):
    # side -1 = Robot's right (viewer's left). Pivot at the shoulder.
    sx = 500 + side * 215
    angle = side * -(150 * raise_amt) + side * 8
    return (f'<g transform="rotate({angle:.1f} {sx} 760)">'
            f'<rect x="{sx - 28}" y="750" width="56" height="190" rx="28" fill="{SHADE}" stroke="{INK}" stroke-width="10"/>'
            f'<circle cx="{sx}" cy="955" r="44" fill="{BODY}" stroke="{INK}" stroke-width="10"/>'
            f'<path d="M{sx - 20} 960 h40" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
            + (f'<path d="M{sx - 30} 850 l60 -14 M{sx - 30} 872 l60 -14" stroke="#E9E2CF" stroke-width="12"/>' if side == 1 else "")
            + '</g>')


def draw(mouth="X", t=0.0, blink=0.0, wave=0.0):
    talking = mouth not in ("X", "A")
    bob = 6 * math.sin(t * 2 * math.pi / 3.0)
    tilt = 2.5 * math.sin(t * 2 * math.pi / 5.1) + (1.5 if talking else 0)
    bulb = 0.55 + 0.45 * (math.sin(t * 2 * math.pi / 1.6) > 0)  # antenna blinks
    wave_rot = 12 * math.sin(t * 2 * math.pi * 1.6) * wave       # hand wiggle while waving
    return f'''<g transform="translate(0 {bob:.1f})">
  {arm(1, 0)}
  <g transform="rotate({wave_rot:.1f} 285 760)">{arm(-1, wave)}</g>
  <rect x="285" y="700" width="430" height="330" rx="70" fill="{BODY}" stroke="{INK}" stroke-width="12"/>
  <rect x="300" y="715" width="60" height="300" rx="30" fill="{LIGHT}" fill-opacity="0.5"/>
  <rect x="390" y="770" width="220" height="130" rx="24" fill="{SCREEN}" stroke="{INK}" stroke-width="8"/>
  {"".join(f'<circle cx="{430 + i * 46}" cy="810" r="13" fill="{c}" fill-opacity="{0.35 + 0.65 * ((int(t * 2) + i) % 3 == 0) if i != 2 else 0.12:.2f}"/>' for i, c in enumerate((GLOW, GOLD, BULB, GLOW)))}
  <rect x="425" y="845" width="150" height="16" rx="8" fill="{GOLD}"/>
  {BODY_DAMAGE}
  <rect x="455" y="640" width="90" height="80" rx="16" fill="{SHADE}" stroke="{INK}" stroke-width="10"/>
  {SCARF_SVG}
  <g transform="rotate({tilt:.2f} 500 650)">
    <path d="M500 190 V150 L524 118" stroke="{INK}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <circle cx="530" cy="104" r="26" fill="{BULB}" fill-opacity="{bulb:.2f}" stroke="{INK}" stroke-width="10"/>
    <rect x="245" y="345" width="50" height="140" rx="20" fill="{SHADE}" stroke="{INK}" stroke-width="10"/>
    {EAR_WIRES}
    <rect x="280" y="185" width="440" height="470" rx="90" fill="{BODY}" stroke="{INK}" stroke-width="12"/>
    <path d="M330 230 q170 -40 340 0" stroke="{LIGHT}" stroke-width="18" fill="none" stroke-linecap="round" stroke-opacity="0.8"/>
    <rect x="330" y="300" width="340" height="290" rx="60" fill="{SCREEN}" stroke="{INK}" stroke-width="10"/>
    <path d="M350 330 q20 -16 60 -18" stroke="#FFFFFF" stroke-width="10" fill="none" stroke-linecap="round" stroke-opacity="0.18"/>
    {eyes(blink, t, talking)}
    {mouth_svg(mouth)}
    {SCREEN_CRACK}
    {HEAD_DAMAGE}
    <path d="M610 215 l46 14 M618 238 l34 -26" stroke="#E9E2CF" stroke-width="16" stroke-linecap="round"/>
    <circle cx="315" cy="620" r="9" fill="{INK}"/><circle cx="685" cy="620" r="9" fill="{INK}"/>
  </g>
</g>'''


def background(t, w=1080, h=1920):
    # Cozy workshop: navy wall, soft shelf shapes, a few drifting code glyphs.
    shelves = "".join(f'<rect x="{x}" y="{y}" width="{bw}" height="18" rx="9" fill="#16263C"/>'
                      for x, y, bw in ((60, int(h * 0.22), 300), (w - 380, int(h * 0.30), 320), (90, int(h * 0.62), 260)))
    boxes = "".join(f'<rect x="{x}" y="{y - s}" width="{s}" height="{s}" rx="10" fill="{c}" fill-opacity="0.55"/>'
                    for x, y, s, c in ((90, int(h * 0.22), 70, "#22476B"), (180, int(h * 0.22), 50, GOLD),
                                       (w - 340, int(h * 0.30), 60, "#22476B"), (120, int(h * 0.62), 80, "#1F3B58")))
    glyphs = "".join(
        f'<text x="{(i * 173) % w}" y="{(i * 97 + t * 30 * (1 + i % 3)) % h:.0f}" font-family="DejaVu Sans Mono" '
        f'font-size="{24 + i % 3 * 6}" fill="{GLOW}" fill-opacity="{0.06 + (i % 4) * 0.02:.2f}">{"{}[]/=*+"[i % 8]}</text>'
        for i in range(24))
    return (f'<defs><radialGradient id="bg" cx="0.62" cy="0.45" r="0.7"><stop offset="0" stop-color="#1D3350"/>'
            f'<stop offset="1" stop-color="#0A121D"/></radialGradient></defs>'
            f'<rect width="{w}" height="{h}" fill="url(#bg)"/>{shelves}{boxes}{glyphs}')
