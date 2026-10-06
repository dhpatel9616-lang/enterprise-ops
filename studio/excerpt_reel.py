#!/usr/bin/env python3
"""The Sovereign excerpt reel (9:16): one verbatim excerpt over the newsletter's
own navy backdrop and logo, revealed word by word, then an invitation to read
the issue. Matches the Substack share-card look (owner, 2026-10-06).

  python3 studio/excerpt_reel.py spec.json out.mp4

spec.json:
  {"hook": "WAS YOUR FIRST ADDICTION A VIDEO GAME?",   # 2-3 s, big caps, the search phrase
   "quote": "For many of us, our first real addiction was ...",  # word for word from the issue
   "issue": "5. Video Games",
   "subtitle": "An examination of the American boy's first love, and first addiction."}
"""
import base64, json, shutil, subprocess, sys, tempfile, textwrap
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).parent))
from text_reel import FPS, W, H, lines  # noqa: E402

HERE = Path(__file__).parent
NAVY, DEEP, WHITE, MIST, RULE = "#1B2A4B", "#0B1224", "#FFFFFF", "#AEB9D3", "#5D6E93"
URL = "SOVEREIGNNEWSLETTER.SUBSTACK.COM"


def fonts():
    # Brand fonts ship in studio/fonts; fontconfig only sees them in ~/.fonts.
    dest = Path.home() / ".fonts"
    if not (dest / "Oswald-Bold.ttf").exists():
        dest.mkdir(exist_ok=True)
        for f in (HERE / "fonts").glob("*.ttf"):
            shutil.copy(f, dest)
        subprocess.run(["fc-cache", "-f"], check=False)


def frame(spec, t, total, logo):
    ease = lambda x: 1 - (1 - min(max(x, 0), 1)) ** 3
    words = spec["quote"].split()
    hook_end, per_word = 2.6, 0.22
    quote_end = hook_end + len(words) * per_word + 2.2
    drift = 40 * (t / total)
    body = ""
    if t < hook_end:  # the hook: big condensed caps, like the Substack "headline" card
        k = ease(t / 0.4)
        body = lines(spec["hook"].upper(), 14, 118, 960, WHITE, "Oswald", "bold", k, 30 * (1 - k))
    elif t < quote_end:  # the excerpt, one word at a time
        long = len(spec["quote"]) > 110  # long quotes go smaller and wider so they clear the logo
        rows, size = textwrap.wrap(spec["quote"], 27 if long else 22), 62 if long else 72
        top = 980 - (len(rows) - 1) * size * 0.65
        i, out = 0, []
        for r, row in enumerate(rows):
            spans = []
            for w in row.split():
                k = ease((t - hook_end - i * per_word) / 0.35)
                spans.append(f'<tspan fill-opacity="{k:.2f}">{escape(w)} </tspan>')
                i += 1
            out.append(f'<text x="{W / 2}" y="{top + r * size * 1.3:.0f}" font-family="EB Garamond" font-size="{size}" '
                       f'fill="{WHITE}" text-anchor="middle" xml:space="preserve">{"".join(spans).rstrip()}</text>')
        k = ease((t - hook_end) / 0.4)
        body = (f'<text x="{W / 2}" y="{top - 110:.0f}" font-family="EB Garamond" font-size="180" fill="{MIST}" '
                f'fill-opacity="{0.5 * k:.2f}" text-anchor="middle">“</text>' + "".join(out))
    else:  # read-more card
        k = ease((t - quote_end) / 0.5)
        body = (lines(spec["issue"], 20, 84, 880, WHITE, "EB Garamond", "normal", k, 30 * (1 - k))
                + lines(spec.get("subtitle", ""), 38, 44, 1060, MIST, "EB Garamond", "normal", k)
                + f'<rect x="300" y="1200" width="480" height="96" rx="48" fill="none" stroke="{WHITE}" stroke-opacity="{k:.2f}" stroke-width="3"/>'
                + lines("READ THE FULL ISSUE", 40, 38, 1260, WHITE, "Oswald", "bold", k))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<defs><radialGradient id="g" cx="0.5" cy="{0.38 + drift / 2000:.3f}" r="0.85"><stop offset="0" stop-color="{NAVY}"/>'
            f'<stop offset="1" stop-color="{DEEP}"/></radialGradient></defs><rect width="{W}" height="{H}" fill="url(#g)"/>'
            f'<image href="{logo}" x="{W / 2 - 170}" y="150" width="340" height="222"/>'
            + body
            + f'<rect x="390" y="{H - 250}" width="300" height="1" fill="{RULE}"/>'
            + lines(URL, 60, 28, H - 190, MIST, "DejaVu Sans", "normal")
            + f'<rect x="0" y="{H - 10}" width="{W * t / total:.0f}" height="10" fill="{MIST}"/></svg>')


def main(spec_path, out):
    fonts()
    spec = json.loads(Path(spec_path).read_text())
    total = 2.6 + len(spec["quote"].split()) * 0.22 + 2.2 + 4.0
    logo = "data:image/png;base64," + base64.b64encode((HERE / "brand" / "sovereign-logo.png").read_bytes()).decode()
    tmp = Path(tempfile.mkdtemp())
    try:
        for i in range(int(total * FPS)):
            (tmp / f"{i:05d}.svg").write_text(frame(spec, i / FPS, total, logo))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(tmp / "%05d.svg"),
                        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest", "-c:v", "libx264",
                        "-pix_fmt", "yuv420p", "-crf", "20", "-c:a", "aac", "-movflags", "+faststart", out], check=True)
    finally:
        shutil.rmtree(tmp)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
