"""SVG puppet rig for Robot (long-form tutorials): a cartoon robot with a
screen for a face. Flat colors and thick outlines, so frames render fast.
Drawn in a 1000x1000 box; the renderer places it.

draw() is the interface the renderer uses:
  mouth  one of Rhubarb's shapes A B C D E F G H X (drawn on the face screen)
  t      seconds since clip start (drives idle motion)
  blink  0 = eyes open, 1 = eyes shut
  wave   0..1 raises Robot's right arm in a wave
background(t) draws this character's scene.
"""
import math

INK, BODY, SHADE, LIGHT = "#14202E", "#5B8DB8", "#3E6A91", "#8DB6D9"
SCREEN, GLOW, BULB, GOLD = "#0B1628", "#8DF7E8", "#FF5A3C", "#B8975A"

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
    for cx in (430, 570):
        out += f'<rect x="{cx - 24 + look:.1f}" y="{430 - h / 2:.1f}" width="48" height="{h:.1f}" rx="{min(24, h / 2):.1f}" fill="{GLOW}"/>'
        out += f'<path d="M{cx - 26 + look:.1f} {382 + brow} q26 -12 52 0" stroke="{GLOW}" stroke-width="8" fill="none" stroke-linecap="round"/>'
    return out


def arm(side, raise_amt):
    # side -1 = Robot's right (viewer's left). Pivot at the shoulder.
    sx = 500 + side * 215
    angle = side * -(150 * raise_amt) + side * 8
    return (f'<g transform="rotate({angle:.1f} {sx} 760)">'
            f'<rect x="{sx - 28}" y="750" width="56" height="190" rx="28" fill="{SHADE}" stroke="{INK}" stroke-width="10"/>'
            f'<circle cx="{sx}" cy="955" r="44" fill="{BODY}" stroke="{INK}" stroke-width="10"/>'
            f'<path d="M{sx - 20} 960 h40" stroke="{INK}" stroke-width="8" stroke-linecap="round"/></g>')


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
  {"".join(f'<circle cx="{430 + i * 46}" cy="810" r="13" fill="{c}" fill-opacity="{0.35 + 0.65 * ((int(t * 2) + i) % 3 == 0):.2f}"/>' for i, c in enumerate((GLOW, GOLD, BULB, GLOW)))}
  <rect x="425" y="845" width="150" height="16" rx="8" fill="{GOLD}"/>
  <rect x="455" y="640" width="90" height="80" rx="16" fill="{SHADE}" stroke="{INK}" stroke-width="10"/>
  <g transform="rotate({tilt:.2f} 500 650)">
    <path d="M500 190 V120" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>
    <circle cx="500" cy="105" r="26" fill="{BULB}" fill-opacity="{bulb:.2f}" stroke="{INK}" stroke-width="10"/>
    <rect x="245" y="345" width="50" height="140" rx="20" fill="{SHADE}" stroke="{INK}" stroke-width="10"/>
    <rect x="705" y="345" width="50" height="140" rx="20" fill="{SHADE}" stroke="{INK}" stroke-width="10"/>
    <rect x="280" y="185" width="440" height="470" rx="90" fill="{BODY}" stroke="{INK}" stroke-width="12"/>
    <path d="M330 230 q170 -40 340 0" stroke="{LIGHT}" stroke-width="18" fill="none" stroke-linecap="round" stroke-opacity="0.8"/>
    <rect x="330" y="300" width="340" height="290" rx="60" fill="{SCREEN}" stroke="{INK}" stroke-width="10"/>
    <path d="M350 330 q20 -16 60 -18" stroke="#FFFFFF" stroke-width="10" fill="none" stroke-linecap="round" stroke-opacity="0.18"/>
    {eyes(blink, t, talking)}
    {mouth_svg(mouth)}
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
