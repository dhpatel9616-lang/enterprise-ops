# Routines

Each routine's prompt in claude.ai/code/routines is the same short text, with
its own file name. The real instructions live in this folder, so changing a
routine only takes a merged PR, never another paste.

| Routine | File | Schedule (Eastern) |
|---|---|---|
| Strategist | `strategist.md` | Sunday ~11:30 PM |
| Social Studio | `social-studio.md` | Monday ~12:30 AM |
| Builder + Leads | `builder-leads.md` | Wednesday ~1:30 AM |
| To-Do Email | `todo-email.md` | Thursday ~8 AM |
| YT Video Studio | `yt-video-studio.md` | Friday ~12:30 AM |

The prompt to paste (replace FILE with the file name above):

```
UNATTENDED SCHEDULED RUN. Nobody is watching: don't ask questions; make
reasonable decisions and note them. Run
`git clone --depth 1 https://github.com/dhpatel9616-lang/enterprise-ops ~/enterprise-ops`,
then read ~/enterprise-ops/routines/FILE and follow it exactly. If the clone
fails, send a push notification with the error and stop.
```

All routines use the same environment. Its Setup script box holds the whole of
`studio/setup.sh`; its variables hold the keys (HF_KEY, ENTERPRISE_SUPABASE_URL,
ENTERPRISE_SUPABASE_SERVICE_KEY, YOUTUBE_*, ELEVENLABS_*). Builder + Leads also
needs enterprise-ops and Enterprise-leads under its Repositories, so it can push
PRs. Use Sonnet for every routine; none needs a bigger model.
