#!/usr/bin/env bash
# Installs the free video tools (ffmpeg with SVG support, espeak-ng for
# placeholder voices, Rhubarb Lip Sync). Safe to re-run. Paste
# "bash studio/setup.sh" into a cloud environment's setup script.
set -euo pipefail
command -v ffmpeg >/dev/null && command -v espeak-ng >/dev/null || {
  sudo_cmd=$([ "$(id -u)" = 0 ] && echo "" || echo sudo)
  $sudo_cmd apt-get update -qq && $sudo_cmd apt-get install -y -qq ffmpeg espeak-ng fonts-dejavu-core
}
if ! command -v rhubarb >/dev/null; then
  dir="$HOME/.local/rhubarb" && mkdir -p "$dir" "$HOME/.local/bin"
  curl -sSL -o /tmp/rhubarb.zip https://github.com/DanielSWolf/rhubarb-lip-sync/releases/download/v1.13.0/Rhubarb-Lip-Sync-1.13.0-Linux.zip
  unzip -q -o /tmp/rhubarb.zip -d "$dir"
  ln -sf "$dir"/Rhubarb-Lip-Sync-1.13.0-Linux/rhubarb "$HOME/.local/bin/rhubarb"
  echo 'Rhubarb installed to ~/.local/bin (make sure it is on PATH).'
fi
