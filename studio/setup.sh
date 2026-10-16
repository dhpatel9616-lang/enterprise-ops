#!/usr/bin/env bash
# Studio environment setup: everything the video-assembly skill needs.
#   ffmpeg (with SVG support) + ffprobe, Rhubarb Lip Sync, espeak-ng
#   (placeholder voices), DejaVu fonts (captions), curl/unzip.
# Safe to re-run. The cloud environment's "Setup script" box holds one line:
#   bash /home/user/enterprise-ops/studio/setup.sh || true
# so it always runs this file's latest version. It never fails the session:
# anything it couldn't install is listed at the end ("setup: MISSING ...")
# and the routines check for their tools themselves.
set -uo pipefail

RHUBARB_VERSION=1.13.0
SUDO=$([ "$(id -u)" = 0 ] && echo "" || echo sudo)

need=()
for c in ffmpeg ffprobe espeak-ng curl unzip; do command -v "$c" >/dev/null || need+=("$c"); done
fc-list 2>/dev/null | grep -ci dejavu >/dev/null || need+=(fonts)
if [ ${#need[@]} -gt 0 ]; then
  export DEBIAN_FRONTEND=noninteractive
  $SUDO apt-get update -qq || echo "setup: apt-get update failed" >&2
  $SUDO apt-get install -y -qq ffmpeg espeak-ng fonts-dejavu-core curl unzip >/dev/null || echo "setup: apt-get install failed" >&2
fi

if ! command -v rhubarb >/dev/null; then
  tmp=$(mktemp -d)
  curl -fSL --retry 2 -o "$tmp/rhubarb.zip" \
    "https://github.com/DanielSWolf/rhubarb-lip-sync/releases/download/v${RHUBARB_VERSION}/Rhubarb-Lip-Sync-${RHUBARB_VERSION}-Linux.zip"
  $SUDO rm -rf /opt/rhubarb && $SUDO mkdir -p /opt/rhubarb
  $SUDO unzip -q "$tmp/rhubarb.zip" -d /opt/rhubarb
  # Rhubarb needs its res/ folder next to the real binary, so link, don't copy.
  $SUDO ln -sf "/opt/rhubarb/Rhubarb-Lip-Sync-${RHUBARB_VERSION}-Linux/rhubarb" /usr/local/bin/rhubarb
  rm -rf "$tmp"
fi

# Robot's AI voice (studio/ai_voice.py): Kokoro engine from PyPI, model files from GitHub.
# Speech-to-text for studio/vo_check.py (checks every voiceover against its script).
# `python3 -m pip` so packages land where python3 looks; pip's own error is kept
# in $PIPLOG and its last lines are printed with the MISSING report (a routine
# run on 2026-10-16 got MISSING kokoro faster-whisper with no reason shown).
PIPLOG=/tmp/studio-setup-pip.log; : > "$PIPLOG"
pipi() {  # pipi <import names> -- <packages>
  local mods=$1; shift
  python3 -c "import $mods" 2>/dev/null && return
  for extra in "" "--break-system-packages" "--user --break-system-packages"; do
    python3 -m pip install -q --root-user-action=ignore --retries 5 --timeout 60 $extra "$@" >>"$PIPLOG" 2>&1 \
      && python3 -c "import $mods" 2>>"$PIPLOG" && return
  done
}
pipi "kokoro_onnx, soundfile" kokoro-onnx soundfile
pipi faster_whisper faster-whisper
$SUDO mkdir -p /opt/kokoro && $SUDO chmod 777 /opt/kokoro
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -f "/opt/kokoro/$f" ] || { curl -fSL --retry 2 -o "/opt/kokoro/$f.part" "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f" && mv -f "/opt/kokoro/$f.part" "/opt/kokoro/$f"; }
done

# Report (don't fail on) anything still missing; the routines check before use.
missing=()
ffmpeg -hide_banner -decoders 2>/dev/null | grep -c librsvg >/dev/null || missing+=("ffmpeg-with-svg")
command -v rhubarb >/dev/null || missing+=(rhubarb)
python3 -c "import kokoro_onnx, soundfile" 2>/dev/null || missing+=(kokoro)
python3 -c "import faster_whisper" 2>/dev/null || missing+=(faster-whisper)
if [ ${#missing[@]} -gt 0 ]; then
  echo "setup: MISSING ${missing[*]}" >&2
  [ -s "$PIPLOG" ] && grep -v '^\s*$' "$PIPLOG" | tail -4 | sed 's/^/setup: pip: /' >&2
  df -h /tmp | tail -1 | awk '{print "setup: disk free " $4}' >&2
  exit 0
fi
echo "studio setup OK: $(ffmpeg -version | head -1 | cut -d' ' -f1-3), rhubarb $(rhubarb --version 2>&1 | grep -o "[0-9.]*[0-9]"), espeak-ng $(espeak-ng --version | cut -d' ' -f4)"
