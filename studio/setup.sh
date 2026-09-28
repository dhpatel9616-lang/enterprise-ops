#!/usr/bin/env bash
# Studio environment setup: everything the video-assembly skill needs.
#   ffmpeg (with SVG support) + ffprobe, Rhubarb Lip Sync, espeak-ng
#   (placeholder voices), DejaVu fonts (captions), curl/unzip.
# Self-contained and safe to re-run. Paste the whole file into the cloud
# environment's "Setup script" box, or run: bash studio/setup.sh
set -euo pipefail

RHUBARB_VERSION=1.13.0
SUDO=$([ "$(id -u)" = 0 ] && echo "" || echo sudo)

need=()
for c in ffmpeg ffprobe espeak-ng curl unzip; do command -v "$c" >/dev/null || need+=("$c"); done
fc-list 2>/dev/null | grep -ci dejavu >/dev/null || need+=(fonts)
if [ ${#need[@]} -gt 0 ]; then
  export DEBIAN_FRONTEND=noninteractive
  $SUDO apt-get update -qq
  $SUDO apt-get install -y -qq ffmpeg espeak-ng fonts-dejavu-core curl unzip >/dev/null
fi

if ! command -v rhubarb >/dev/null; then
  tmp=$(mktemp -d)
  curl -fsSL -o "$tmp/rhubarb.zip" \
    "https://github.com/DanielSWolf/rhubarb-lip-sync/releases/download/v${RHUBARB_VERSION}/Rhubarb-Lip-Sync-${RHUBARB_VERSION}-Linux.zip"
  $SUDO rm -rf /opt/rhubarb && $SUDO mkdir -p /opt/rhubarb
  $SUDO unzip -q "$tmp/rhubarb.zip" -d /opt/rhubarb
  # Rhubarb needs its res/ folder next to the real binary, so link, don't copy.
  $SUDO ln -sf "/opt/rhubarb/Rhubarb-Lip-Sync-${RHUBARB_VERSION}-Linux/rhubarb" /usr/local/bin/rhubarb
  rm -rf "$tmp"
fi

# Fail loudly if anything the renderer relies on is still missing.
ffmpeg -hide_banner -decoders 2>/dev/null | grep -c librsvg >/dev/null || { echo "setup: ffmpeg has no SVG (librsvg) support" >&2; exit 1; }
rhubarb --version >/dev/null
python3 -c "import json, subprocess, urllib.request"
echo "studio setup OK: $(ffmpeg -version | head -1 | cut -d' ' -f1-3), rhubarb $(rhubarb --version 2>&1 | grep -o "[0-9.]*[0-9]"), espeak-ng $(espeak-ng --version | cut -d' ' -f4)"
