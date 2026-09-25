#!/usr/bin/env bash
# Rebuilds the 10-second the robot host style test with a robot placeholder voice.
# Real videos use the owner's recorded voiceover instead (see voiceover-workflow).
set -euo pipefail
cd "$(dirname "$0")"
work=$(mktemp -d); trap 'rm -rf "$work"' EXIT
lines=("Relax. I'm not here to terminate you." "I'm here to keep you protected." "Hackers. Blackouts. All of it." "Subscribe before the grid goes down.")
printf '%s\n' "${lines[@]}" > dialog.txt
echo '[' > captions.json; t=0.2; parts=()
ffmpeg -loglevel error -f lavfi -i anullsrc=r=22050:cl=mono -t 0.2 "$work/lead.wav"; parts+=("$work/lead.wav")
for i in "${!lines[@]}"; do
  espeak-ng -v en-us -p 25 -s 185 -w "$work/$i.wav" "${lines[$i]}"
  ffmpeg -loglevel error -f lavfi -i anullsrc=r=22050:cl=mono -t 0.25 "$work/gap$i.wav"
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$work/$i.wav")
  end=$(python3 -c "print(round($t+$d,2))")
  sep=$([ "$i" -lt $((${#lines[@]}-1)) ] && echo , || true)
  echo "  {\"start\": $t, \"end\": $end, \"text\": \"${lines[$i]}\"}$sep" >> captions.json
  t=$(python3 -c "print(round($end+0.25,2))"); parts+=("$work/$i.wav" "$work/gap$i.wav")
done
echo ']' >> captions.json
printf "file '%s'\n" "${parts[@]}" > "$work/list.txt"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$work/list.txt" -ar 22050 -ac 1 placeholder-voice.wav
python3 ../../render_puppet.py --character robot-host --audio placeholder-voice.wav --dialog dialog.txt \
  --captions captions.json --seconds 10 \
  --label "Style test - placeholder voice" --out robot-host-style-test.mp4
echo "Wrote $(pwd)/robot-host-style-test.mp4"
