# enterprise-ops

Control room for the autonomous content studio and night-shift routines.
Rules for Claude live in [`CLAUDE.md`](CLAUDE.md); skills live in
[`.claude/skills/`](.claude/skills).

| Folder | What's in it |
|---|---|
| `.claude/skills/` | brand-voice, platform-formats, content-rules, character-bible, higgsfield-api, video-assembly, voiceover-workflow, monetization, outreach, and the Ponytail coding skills |
| `.claude/rules/` | Ponytail ruleset (MIT), loaded from `CLAUDE.md` |
| `studio/` | Free video tools: puppet renderer, caption timing, setup script |
| `studio/samples/host-01-style-test/` | 10-second style test of the cartoon host |

Set up the video tools in a new environment: `bash studio/setup.sh`.
