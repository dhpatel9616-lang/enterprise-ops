#!/usr/bin/env python3
"""Robot's AI voice: script text -> narration WAV.

  python3 studio/ai_voice.py script.txt vo.wav [--engine auto|chatterbox|elevenlabs|kokoro] [--voice ID] [--speed 1.0]

script.txt is the spoken words only (no stage directions). Blank lines split
paragraphs and become short pauses.

Engines:
  chatterbox  Robot's voice: a free clone (MIT licence) of Marley's voice, used with her
              consent (character-bible). Reference clip: private Supabase bucket
              voice-samples/robot-ref.wav (ENTERPRISE_SUPABASE_URL / _SERVICE_KEY).
              Installs itself into /opt/chatterbox on first use; model files come from
              huggingface.co. CPU only: ~7 minutes of work per minute of audio.
  elevenlabs  Robot's cloned voice (character-bible). Needs ELEVENLABS_API_KEY and
              ELEVENLABS_VOICE_ID (or --voice). Network: api.elevenlabs.io.
  kokoro      Free offline fallback (Apache-2.0); model files cached in /opt/kokoro
              (studio/setup.sh pre-downloads them).
  auto        ElevenLabs if its key and voice are set, else Chatterbox if the Supabase
              keys are set, else Kokoro. If Chatterbox fails, falls back to Kokoro. (default)
"""
import argparse, json, os, re, subprocess, sys, tempfile, urllib.error, urllib.parse, urllib.request
from pathlib import Path

MODEL_DIR = Path(os.environ.get("KOKORO_DIR", "/opt/kokoro"))
BASE = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
FILES = ("kokoro-v1.0.onnx", "voices-v1.0.bin")
KOKORO_VOICE = "bf_emma"  # fallback only
EL_MODEL = os.environ.get("ELEVENLABS_MODEL", "eleven_multilingual_v2")
PAUSE = 0.45  # seconds between paragraphs
CB_VENV = Path(os.environ.get("CHATTERBOX_DIR", "/opt/chatterbox"))
CB_RUN = '''
import json, sys, torchaudio
from chatterbox.tts import ChatterboxTTS
job = json.load(open(sys.argv[1]))
m = ChatterboxTTS.from_pretrained(device="cpu")
for i, text in enumerate(job["chunks"]):
    torchaudio.save(f"{job['dir']}/{i:03d}.wav", m.generate(text, audio_prompt_path=job["ref"], exaggeration=0.6, cfg_weight=0.5), m.sr)
    print(f"ai_voice: chatterbox chunk {i + 1}/{len(job['chunks'])}", file=sys.stderr, flush=True)
'''


def chatterbox(paras, voice, speed, tmp):
    parts = urllib.parse.urlparse(os.environ["ENTERPRISE_SUPABASE_URL"].strip())
    key = os.environ["ENTERPRISE_SUPABASE_SERVICE_KEY"].strip()
    req = urllib.request.Request(f"{parts.scheme}://{parts.netloc}/storage/v1/object/voice-samples/robot-ref.wav",
                                 headers={"apikey": key, "Authorization": f"Bearer {key}"})
    (tmp / "ref.wav").write_bytes(urllib.request.urlopen(req, timeout=60).read())
    py = CB_VENV / "bin" / "python"
    if not py.exists():
        print("ai_voice: installing Chatterbox (one time, a few minutes)...", file=sys.stderr)
        subprocess.run([sys.executable, "-m", "venv", str(CB_VENV)], check=True)
        subprocess.run([str(py), "-m", "pip", "install", "-q", "chatterbox-tts"], check=True)
    # Chatterbox drifts on long inputs: feed it a few sentences (~250 chars) at a time.
    chunks, bounds = [], []
    for para in paras:
        cur = ""
        for sent in re.split(r"(?<=[.!?])\s+", para):
            if cur and len(cur) + len(sent) > 250:
                chunks.append(cur)
                cur = ""
            cur = f"{cur} {sent}".strip()
        chunks.append(cur)
        bounds.append(len(chunks))
    (tmp / "job.json").write_text(json.dumps({"chunks": chunks, "ref": str(tmp / "ref.wav"), "dir": str(tmp)}))
    subprocess.run([str(py), "-I", "-c", CB_RUN, str(tmp / "job.json")], check=True,
                   env={**os.environ, "HF_HUB_DISABLE_XET": "1"})
    # One file per paragraph so the paragraph pauses still apply.
    out, start = [], 0
    for n, end in enumerate(bounds):
        files = [tmp / f"{i:03d}.wav" for i in range(start, end)]
        para = tmp / f"para{n:03d}.wav"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *sum((["-i", str(f)] for f in files), []), "-filter_complex",
                        "".join(f"[{i}:a]" for i in range(len(files))) + f"concat=n={len(files)}:v=0:a=1"
                        + (f",atempo={speed}" if speed != 1.0 else "") + "[o]", "-map", "[o]", str(para)], check=True)
        out.append(para)
        start = end
    return out


def kokoro(paras, voice, speed, tmp):
    try:
        import numpy as np, soundfile as sf
        from kokoro_onnx import Kokoro
    except ImportError:
        sys.exit("ai_voice: run `pip install kokoro-onnx soundfile` (studio/setup.sh does this).")
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    for f in FILES:
        if not (MODEL_DIR / f).exists():
            print(f"ai_voice: downloading {f}...", file=sys.stderr)
            urllib.request.urlretrieve(BASE + f, MODEL_DIR / f".{f}.part")
            (MODEL_DIR / f".{f}.part").rename(MODEL_DIR / f)
    k = Kokoro(str(MODEL_DIR / FILES[0]), str(MODEL_DIR / FILES[1]))
    chunks, sr = [], 24000
    for i, para in enumerate(paras, 1):
        audio, sr = k.create(para, voice=voice or KOKORO_VOICE, speed=speed, lang="en-gb")
        chunks += [audio, np.zeros(int(sr * PAUSE), dtype=audio.dtype)]
        print(f"ai_voice: kokoro paragraph {i}/{len(paras)}", file=sys.stderr)
    out = tmp / "raw.wav"
    sf.write(out, np.concatenate(chunks), sr)
    return [out]


def elevenlabs(paras, voice, speed, tmp):
    key = os.environ["ELEVENLABS_API_KEY"]
    parts = []
    for i, para in enumerate(paras):
        body = {"text": para, "model_id": EL_MODEL,
                # Neighbouring paragraphs keep the delivery continuous across requests.
                "previous_text": paras[i - 1] if i else None, "next_text": paras[i + 1] if i + 1 < len(paras) else None,
                "voice_settings": {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "speed": speed}}
        req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128",
                                     data=json.dumps(body).encode(), method="POST",
                                     headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
        try:
            mp3 = urllib.request.urlopen(req, timeout=300).read()
        except urllib.error.HTTPError as e:
            sys.exit(f"ai_voice: ElevenLabs refused paragraph {i + 1} ({e.code}): {e.read().decode(errors='replace')[:300]}")
        (tmp / f"{i:03d}.mp3").write_bytes(mp3)
        parts.append(tmp / f"{i:03d}.mp3")
        print(f"ai_voice: elevenlabs paragraph {i + 1}/{len(paras)}", file=sys.stderr)
    return parts


def main():
    p = argparse.ArgumentParser()
    p.add_argument("script"), p.add_argument("out")
    p.add_argument("--engine", choices=("auto", "chatterbox", "elevenlabs", "kokoro"), default="auto")
    p.add_argument("--voice", help="ElevenLabs voice ID or Kokoro voice name")
    p.add_argument("--speed", type=float, default=1.0)
    a = p.parse_args()
    voice = a.voice or os.environ.get("ELEVENLABS_VOICE_ID")
    engine = a.engine
    auto = engine == "auto"
    if auto:
        engine = ("elevenlabs" if os.environ.get("ELEVENLABS_API_KEY") and voice
                  else "chatterbox" if os.environ.get("ENTERPRISE_SUPABASE_SERVICE_KEY") else "kokoro")
    if engine == "elevenlabs" and not (os.environ.get("ELEVENLABS_API_KEY") and voice):
        sys.exit("ai_voice: set ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID (or --voice).")
    paras = [re.sub(r"\s+", " ", x).strip() for x in Path(a.script).read_text().split("\n\n") if x.strip()]
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        if engine == "chatterbox":
            try:
                parts = chatterbox(paras, voice, a.speed, tmp)
            except Exception as e:  # never lose an episode over the voice: fall back to the free stock voice
                if not auto:
                    raise
                print(f"ai_voice: Chatterbox failed ({e}); using Kokoro instead.", file=sys.stderr)
                engine, parts = "kokoro", kokoro(paras, a.voice, a.speed, tmp)
        else:
            parts = elevenlabs(paras, voice, a.speed, tmp) if engine == "elevenlabs" else kokoro(paras, a.voice, a.speed, tmp)
        # Join with a short pause between paragraphs, then normalise loudness for YouTube (-14 LUFS), 44.1 kHz.
        inputs = sum((["-i", str(x)] for x in parts), [])
        n = len(parts)
        pad = "".join(f"[{i}:a]apad=pad_dur={PAUSE if n > 1 else 0}[a{i}];" for i in range(n))
        graph = pad + "".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1,loudnorm=I=-14:TP=-1.5:LRA=11[out]"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", graph, "-map", "[out]",
                        "-ar", "44100", a.out], check=True)
    print(f"{a.out} ({engine})")


if __name__ == "__main__":
    main()
