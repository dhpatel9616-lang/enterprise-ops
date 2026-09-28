#!/usr/bin/env python3
"""Render a lip-synced SVG puppet clip. Free tools only: Rhubarb + ffmpeg (librsvg).

  python3 studio/render_puppet.py --character robot-host --audio vo.wav \
      --dialog script.txt --captions captions.json --out clip.mp4

captions.json (optional): [{"start": 0.0, "end": 1.8, "text": "Hi!"}, ...]
--sheet out.png renders a mouth-shape reference sheet instead of a clip.
"""
import argparse, importlib.util, json, shutil, subprocess, tempfile
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
CHARACTERS = ROOT / ".claude/skills/character-bible/characters"
FPS = 30
# Frame size, where the character sits, caption box (x, y, w, h), footer label y.
LAYOUTS = {
    "tall": dict(W=1080, H=1920, char="translate(40 380)", box=(50, 1480, 980, 150), label_y=1840),  # Shorts/TikTok/Reels
    "wide": dict(W=1920, H=1080, char="translate(900 80)", box=(60, 850, 860, 130), label_y=1060),  # YouTube long-form
}
L = LAYOUTS["tall"]


def load_rig(name):
    spec = importlib.util.spec_from_file_location("rig", CHARACTERS / name / "rig.py")
    rig = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rig)
    return rig


def mouth_cues(audio, dialog):
    cmd = ["rhubarb", "-f", "json", "--machineReadable", str(audio)]
    if dialog:
        cmd[1:1] = ["--dialogFile", str(dialog)]
    return json.loads(subprocess.run(cmd, check=True, capture_output=True, text=True).stdout)["mouthCues"]


def blink_at(t):
    # Blink roughly every 3.1s, 0.15s long; deterministic so re-renders match.
    phase = (t + 0.7) % 3.1
    return 1.0 if phase < 0.15 else 0.0


def caption(t, captions):
    for c in captions:
        if c["start"] <= t < c["end"]:
            text = escape(c["text"])
            x, y, w, h = L["box"]
            return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="36" fill="#23313F" opacity="0.92"/>'
                    f'<text x="{x + w / 2}" y="{y + h / 2 + 16}" font-family="DejaVu Sans" font-weight="bold" font-size="42" '
                    f'fill="#fff" text-anchor="middle">{text}</text>')
    return ""


def frame_svg(rig, t, mouth, captions, label, wave):
    W, H = L["W"], L["H"]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'{rig.background(t, W, H)}<g transform="{L["char"]}">{rig.draw(mouth, t, blink_at(t), wave)}</g>'
            f'{caption(t, captions)}'
            f'<text x="{W / 2}" y="{L["label_y"]}" font-family="DejaVu Sans" font-size="30" fill="#9AA3B2" '
            f'text-anchor="middle">{escape(label)}</text></svg>')


def render_clip(a):
    rig = load_rig(a.character)
    cues = mouth_cues(a.audio, a.dialog)
    captions = json.loads(Path(a.captions).read_text()) if a.captions else []
    seconds = a.seconds or cues[-1]["end"]
    tmp = Path(tempfile.mkdtemp())
    try:
        for i in range(int(seconds * FPS)):
            t = i / FPS
            mouth = next((c["value"] for c in cues if c["start"] <= t < c["end"]), "X")
            wave = max(0.0, 1 - abs(t - a.wave_at) / 1.2) if a.wave_at is not None else 0.0
            (tmp / f"{i:05d}.svg").write_text(frame_svg(rig, t, mouth, captions, a.label, wave))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(tmp / "%05d.svg"),
                        "-i", str(a.audio), "-af", "apad", "-t", f"{seconds:.2f}",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "23", "-c:a", "aac", "-b:a", "128k",
                        "-movflags", "+faststart", str(a.out)], check=True)
    finally:
        shutil.rmtree(tmp)


def render_sheet(a):
    rig = load_rig(a.character)
    shapes = "XABCDEFGH"
    cells = "".join(
        f'<g transform="translate({(i % 3) * 360} {(i // 3) * 400}) scale(0.36)">{rig.draw(m, 0.0, 0.0, 0.0)}</g>'
        f'<text x="{(i % 3) * 360 + 180}" y="{(i // 3) * 400 + 390}" font-family="DejaVu Sans" font-size="30" '
        f'text-anchor="middle" fill="#23313F">mouth {m}</text>'
        for i, m in enumerate(shapes))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1200" viewBox="0 0 1080 1200">'
           f'<rect width="1080" height="1200" fill="#FFF4E0"/>{cells}</svg>')
    src = Path(a.sheet).with_suffix(".svg")
    src.write_text(svg)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-frames:v", "1", str(a.sheet)], check=True)
    src.unlink()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--character", required=True)
    p.add_argument("--audio")
    p.add_argument("--dialog", help="plain-text script; improves Rhubarb accuracy")
    p.add_argument("--captions")
    p.add_argument("--out")
    p.add_argument("--seconds", type=float, help="clip length (defaults to audio length)")
    p.add_argument("--wave-at", type=float, help="second at which the host waves")
    p.add_argument("--label", default="", help="small footer text, e.g. an AI/synthetic disclosure")
    p.add_argument("--sheet", help="write a mouth-shape reference PNG and exit")
    p.add_argument("--layout", choices=LAYOUTS, default="tall", help="tall = 9:16 shorts, wide = 16:9 YouTube")
    a = p.parse_args()
    L = LAYOUTS[a.layout]
    render_sheet(a) if a.sheet else render_clip(a)
