# enterprise-ops

Control room for the autonomous content studio and night-shift routines.
Rules for Claude live in [`CLAUDE.md`](CLAUDE.md); skills live in
[`.claude/skills/`](.claude/skills).

| Folder | What's in it |
|---|---|
| `.claude/skills/` | brand-voice, platform-formats, content-rules, character-bible, higgsfield-api, video-assembly, voiceover-workflow, monetization, outreach, and the Ponytail coding skills |
| `.claude/rules/` | Ponytail ruleset (MIT), loaded from `CLAUDE.md` |
| `studio/` | Free video tools: puppet renderer, caption timing, environment setup script, public video upload |
| `supabase/migrations/` | Database/storage changes as files (applied by the owner; see `build-standards`) |
| `studio/samples/robot-host-style-test/` | 10-second style test of Robot (YouTube long-form host) |
| `campaigns/` | Campaign plans (e.g. PoolParty "Friendly Wagers") |

Set up the video tools in a new environment: `bash studio/setup.sh`.
