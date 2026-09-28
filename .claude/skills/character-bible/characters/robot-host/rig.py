"""SVG puppet rig for Robot ("Robot teaches Cybersecurity"). 3D-styled with
gradients and highlights, drawn in a 1000x1000 box; the renderer places it.

draw() is the interface the renderer uses:
  mouth  one of Rhubarb's shapes A B C D E F G H X (drives the jaw)
  t      seconds since clip start (drives idle motion)
  blink  0 = eyes open, 1 = eyes shut
  wave   0..1 how far the right arm is raised
background(t) draws this character's scene.
"""
import math

INK, LENS_HOT, HAZARD, CREAM, GOLD = "#141820", "#FF7A45", "#F2C230", "#F3EDE0", "#B8975A"

# Rhubarb shape -> (jaw drop px, mouth width px)
MOUTHS = {"X": (0, 200), "A": (0, 200), "B": (6, 200), "C": (18, 210), "D": (38, 232),
          "E": (22, 160), "F": (14, 104), "G": (8, 200), "H": (26, 200)}

DEFS = """<defs>
  <linearGradient id="metal" x1="0" y1="0" x2="0.35" y2="1"><stop offset="0" stop-color="#B4BFCE"/><stop offset="0.45" stop-color="#6B7789"/><stop offset="1" stop-color="#2F3644"/></linearGradient>
  <linearGradient id="metalDark" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#555F70"/><stop offset="1" stop-color="#1D222B"/></linearGradient>
  <linearGradient id="hood" x1="0" y1="0" x2="0.3" y2="1"><stop offset="0" stop-color="#343B48"/><stop offset="1" stop-color="#11141A"/></linearGradient>
  <radialGradient id="lens" cx="0.42" cy="0.4" r="0.6"><stop offset="0" stop-color="#FFE0B8"/><stop offset="0.3" stop-color="#FF8A4C"/><stop offset="0.7" stop-color="#E0352B"/><stop offset="1" stop-color="#4A0C0A"/></radialGradient>
  <radialGradient id="cavity" cx="0.5" cy="0.3" r="0.8"><stop offset="0" stop-color="#FF5A36"/><stop offset="0.5" stop-color="#6A1410"/><stop offset="1" stop-color="#140404"/></radialGradient>
  <radialGradient id="shine" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.75"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>
  <radialGradient id="shade" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#000000" stop-opacity="0.5"/><stop offset="1" stop-color="#000000" stop-opacity="0"/></radialGradient>
  <radialGradient id="bulb" cx="0.4" cy="0.35" r="0.6"><stop offset="0" stop-color="#FFE3C8"/><stop offset="0.5" stop-color="#FF5A36"/><stop offset="1" stop-color="#7A140E"/></radialGradient>
  <clipPath id="eyeL"><circle cx="400" cy="430" r="62"/></clipPath>
  <clipPath id="eyeR"><circle cx="600" cy="430" r="62"/></clipPath>
</defs>"""


def eye(cx, clip, lid, look_x, look_y, lid_tilt):
    return f'''<circle cx="{cx}" cy="430" r="80" fill="url(#metalDark)" stroke="{INK}" stroke-width="4"/>
    <circle cx="{cx}" cy="430" r="62" fill="#0B0D12"/>
    <g clip-path="url(#{clip})">
      <circle cx="{cx + look_x:.1f}" cy="{430 + look_y:.1f}" r="50" fill="url(#lens)"/>
      <circle cx="{cx + look_x:.1f}" cy="{430 + look_y:.1f}" r="30" fill="none" stroke="#FFB08A" stroke-opacity="0.55" stroke-width="3"/>
      <circle cx="{cx + look_x:.1f}" cy="{430 + look_y:.1f}" r="13" fill="#2B0605"/>
      <circle cx="{cx + look_x - 18:.1f}" cy="{430 + look_y - 20:.1f}" r="11" fill="#FFFFFF" opacity="0.9"/>
      <circle cx="{cx + look_x + 16:.1f}" cy="{430 + look_y + 15:.1f}" r="5" fill="#FFFFFF" opacity="0.6"/>
      <g transform="rotate({lid_tilt:.1f} {cx} 368)">
        <rect x="{cx - 70}" y="{368 - 130 + 130 * lid:.1f}" width="140" height="130" fill="url(#metal)"/>
        <rect x="{cx - 70}" y="{368 + 130 * lid - 8:.1f}" width="140" height="8" fill="{INK}" opacity="0.7"/>
      </g>
    </g>'''


def arm(pivot_x, angle, mirror):
    s = -1 if mirror else 1
    return f'''<g transform="rotate({angle:.1f} {pivot_x} 730)">
    <rect x="{pivot_x - 48}" y="720" width="96" height="190" rx="44" fill="url(#hood)" stroke="{INK}" stroke-width="5"/>
    <ellipse cx="{pivot_x}" cy="930" rx="46" ry="40" fill="url(#metal)" stroke="{INK}" stroke-width="5"/>
    <rect x="{pivot_x - 38}" y="950" width="22" height="42" rx="11" fill="url(#metal)" stroke="{INK}" stroke-width="4"/>
    <rect x="{pivot_x - 11}" y="956" width="22" height="46" rx="11" fill="url(#metal)" stroke="{INK}" stroke-width="4"/>
    <rect x="{pivot_x + 16}" y="950" width="22" height="42" rx="11" fill="url(#metal)" stroke="{INK}" stroke-width="4"/>
    <ellipse cx="{pivot_x - 14 * s}" cy="916" rx="20" ry="10" fill="url(#shine)"/>
  </g>'''


def draw(mouth="X", t=0.0, blink=0.0, wave=0.0):
    talking = mouth not in ("X", "A")
    drop, width = MOUTHS.get(mouth, MOUTHS["X"])
    bob = 8 * math.sin(t * 2 * math.pi / 2.6)
    tilt = 2.5 * math.sin(t * 2 * math.pi / 4.1)
    look_x, look_y = 10 * math.sin(t * 0.8), 5 * math.sin(t * 1.1)
    lid = max(blink, 0.08 if talking else 0.2)  # droopy lids = smug, not scary
    lid_tilt = -6 if talking else 4
    sway = 4 * math.sin(t * 2 * math.pi / 1.8)
    right = sway * (1 - wave) + (-150 + 14 * math.sin(t * 2 * math.pi / 0.7)) * wave
    pulse = 0.55 + 0.45 * abs(math.sin(t * 2.2))
    teeth = "".join(f'<rect x="{500 - width / 2 + 10 + i * (width - 20) / 7:.1f}" y="552" width="{(width - 20) / 7 - 6:.1f}" height="10" rx="2" fill="#D9DEE6"/>'
                    for i in range(7))
    return f'''{DEFS}<g transform="translate(0 {bob:.1f})">
  {arm(232, 8 - sway, True)}
  {arm(768, right - 8 * (1 - wave), False) if wave < 0.3 else ''}
  <path d="M240 740 C215 840 205 930 210 1000 L790 1000 C795 930 785 840 760 740 C700 700 300 700 240 740 Z" fill="url(#hood)" stroke="{INK}" stroke-width="5"/>
  <path d="M330 720 C360 770 640 770 670 720 C640 690 360 690 330 720 Z" fill="#232833" stroke="{INK}" stroke-width="5"/>
  <path d="M390 900 L610 900 L628 990 L372 990 Z" fill="#0F1217" opacity="0.8"/>
  <g transform="rotate(-8 300 870)"><rect x="245" y="852" width="110" height="34" rx="4" fill="{HAZARD}" stroke="{INK}" stroke-width="4"/>
    {"".join(f'<polygon points="{262 + i * 26},852 {276 + i * 26},852 {262 + i * 26},886 {248 + i * 26},886" fill="{INK}"/>' for i in range(4))}</g>
  <path d="M455 760 L445 870" stroke="{CREAM}" stroke-width="6" stroke-linecap="round"/><rect x="438" y="866" width="14" height="22" rx="3" fill="{GOLD}"/>
  <path d="M545 760 L555 880" stroke="{CREAM}" stroke-width="6" stroke-linecap="round"/><rect x="548" y="876" width="14" height="22" rx="3" fill="{GOLD}"/>
  {arm(768, right, False) if wave >= 0.3 else ''}
  <g transform="rotate({tilt:.2f} 500 690)">
    <ellipse cx="500" cy="700" rx="200" ry="40" fill="url(#shade)"/>
    <rect x="450" y="620" width="100" height="80" rx="12" fill="url(#metalDark)" stroke="{INK}" stroke-width="4"/>
    <path d="M452 648 H548 M452 672 H548" stroke="{INK}" stroke-width="3" opacity="0.6"/>
    <path d="M600 262 C610 220 650 205 640 170" fill="none" stroke="#7D889A" stroke-width="10" stroke-linecap="round"/>
    <circle cx="640" cy="162" r="18" fill="url(#bulb)" opacity="{pulse:.2f}"/><circle cx="634" cy="156" r="5" fill="#FFFFFF" opacity="0.8"/>
    <ellipse cx="262" cy="445" rx="30" ry="64" fill="url(#metalDark)" stroke="{INK}" stroke-width="4"/>
    <ellipse cx="738" cy="445" rx="30" ry="64" fill="url(#metalDark)" stroke="{INK}" stroke-width="4"/>
    <rect x="270" y="250" width="460" height="390" rx="115" fill="url(#metal)" stroke="{INK}" stroke-width="5"/>
    <rect x="288" y="268" width="424" height="354" rx="100" fill="none" stroke="#FFFFFF" stroke-opacity="0.18" stroke-width="4"/>
    <ellipse cx="430" cy="300" rx="130" ry="36" fill="url(#shine)"/>
    <ellipse cx="500" cy="615" rx="200" ry="30" fill="url(#shade)"/>
    <g transform="rotate(28 668 300)"><rect x="630" y="288" width="76" height="24" rx="10" fill="#E6C9A2" stroke="#B8966F" stroke-width="2"/>
      <rect x="656" y="262" width="24" height="76" rx="10" fill="#E6C9A2" stroke="#B8966F" stroke-width="2"/></g>
    <g transform="rotate(-6 340 300)"><rect x="310" y="286" width="66" height="34" rx="4" fill="{HAZARD}"/>
      <text x="343" y="310" font-family="DejaVu Sans" font-weight="bold" font-size="20" fill="{INK}" text-anchor="middle">2FA</text></g>
    {"".join(f'<circle cx="{x}" cy="{y}" r="7" fill="url(#metalDark)" stroke="{INK}" stroke-width="2"/>' for x, y in ((310, 360), (690, 360), (320, 560), (680, 560)))}
    {"".join(f'<path d="M{x} {y} l18 -12" stroke="{INK}" stroke-width="5" stroke-linecap="round" opacity="0.6"/>' for x in (292, 690) for y in (520, 538, 556))}
    {eye(400, "eyeL", lid, look_x, look_y, lid_tilt)}
    {eye(600, "eyeR", lid, look_x, look_y, -lid_tilt)}
    <rect x="{500 - width / 2 - 14:.1f}" y="530" width="{width + 28}" height="30" rx="12" fill="url(#metalDark)" stroke="{INK}" stroke-width="4"/>
    <rect x="{500 - width / 2:.1f}" y="560" width="{width}" height="{drop + 6}" rx="8" fill="url(#cavity)"/>
    {teeth if drop else ""}
    <g transform="translate(0 {drop})">
      <rect x="{500 - width / 2 - 14:.1f}" y="560" width="{width + 28}" height="44" rx="16" fill="url(#metal)" stroke="{INK}" stroke-width="4"/>
      <ellipse cx="480" cy="572" rx="{width / 3:.0f}" ry="6" fill="url(#shine)"/>
    </g>
  </g>
</g>'''


def background(t, w=1080, h=1920):
    # Night desk-lab: dark field, faint grid, drifting terminal glyphs, soft glow behind Robot.
    grid = "".join(f'<path d="M{x} 0 V{h}" stroke="#141D27" stroke-width="2"/>' for x in range(0, w, 60)) + \
        "".join(f'<path d="M0 {y} H{w}" stroke="#141D27" stroke-width="2"/>' for y in range(0, h, 60))
    glyphs = "".join(
        f'<text x="{(i * 173) % w}" y="{(i * 97 + t * 40 * (1 + i % 3)) % h:.0f}" font-family="DejaVu Sans Mono" '
        f'font-size="{22 + i % 3 * 6}" fill="#2FAE66" opacity="{0.14 + (i % 4) * 0.05:.2f}">{"01#$%*+="[i % 8] * (1 + i % 3)}</text>'
        for i in range(40))
    return (f'<defs><radialGradient id="glow" cx="0.5" cy="0.42" r="0.55"><stop offset="0" stop-color="#27425E"/>'
            f'<stop offset="1" stop-color="#07090F"/></radialGradient></defs>'
            f'<rect width="{w}" height="{h}" fill="url(#glow)"/>{grid}{glyphs}')
