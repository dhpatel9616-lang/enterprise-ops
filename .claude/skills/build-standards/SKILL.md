---
name: build-standards
description: Engineering rules for any build that touches Supabase, database security (RLS), storage buckets, scheduled jobs (cron, GitHub Actions, routines), or migrations. Use before writing SQL, a migration, a storage bucket, a cron schedule, or a script that uses a Supabase key.
---

# Build standards

## 1. Never touch PoolParty production
Supabase project `tzebfwmrmzhkeoptwkzy` is off-limits: no reads, writes,
migrations, branches, edge functions, or keys. Scripts that take a Supabase
URL must refuse that project (see `studio/upload_video.py`). If a task seems to
need it, stop and ask the owner.

Enterprise work uses `skakrtljfaeopfqigyww`.

## 2. Migrations are files only
- Every schema, policy, or storage change is a SQL file in
  `supabase/migrations/<YYYYMMDDHHMMSS>_<short_name>.sql`, delivered in a PR.
- Claude never applies changes directly: no `apply_migration`, no DDL
  through `execute_sql`, no dashboard edits.
- Make migrations re-runnable (`if not exists`, `on conflict do nothing`,
  `drop policy if exists` before `create policy`).
- The PR says in plain words how the owner applies it. After merging:
  Supabase → project `skakrtljfaeopfqigyww` → **SQL Editor** → **New query**
  → paste the file → **Run**.

## 3. Supabase RLS (row level security)
- **Turn RLS on for every table** in `public`
  (`alter table … enable row level security;`). A table without RLS is
  readable and writable by anyone holding the anon key.
- **The anon key is public.** Anything in a web page or app ships it.
  Policies are the only protection.
- **The service-role (secret) key bypasses RLS.** Use it only in
  server-side jobs (GitHub Actions secrets, routine environment variables).
  Never put it in a web page, the repo, Notion, or logs.
- **RLS on with no policy means "deny all"** for anon/authenticated. That's
  the right default for tables only jobs touch; add policies only for what a
  client really needs.
- **Read-only dashboards:** `for select to anon using (true)` exposes every
  row. Only do it for data that's fine to be public; for per-user data use
  `using (auth.uid() = user_id)`.
- **Write policies need `with check`** as well as `using`, or users can write
  rows they can't read back.
- **Views run with their creator's rights and skip RLS** unless created
  `with (security_invoker = true)`.
- **`security definer` functions** must `set search_path = ''` (or a fixed
  schema) and check the caller themselves.
- **Storage is RLS on `storage.objects`.** A *public* bucket makes files
  readable by URL without policies, but uploads still need a policy or the
  service key. Our public bucket has **no** anon upload policy; only the
  service key uploads. Never put private files in a public bucket.
- After any migration, run Supabase's security advisor (Dashboard →
  Advisors) and fix "RLS disabled" or "policy exists but RLS off" warnings.

## 4. Off-round cron times
- Never schedule at `:00` or `:30`. Everyone does, so runs get delayed or
  dropped. Pick an odd minute, e.g. `34 13 * * 1-5` (the existing outreach
  job) or `7 2 * * *`.
- Stagger dependent jobs by 10+ minutes (ingest → enrich → digest →
  outreach) and write the order in a comment.
- GitHub Actions cron is **UTC**; say the local time in a comment
  (`# ~9:34am ET`). Routines can use `CRON_TZ=America/New_York`.
- Every scheduled job can be skipped safely: it checks its Automation
  Control switch (Notion) or its settings, and no-ops if a secret is missing.

## 5. Every script
- Reads secrets from environment variables and exits with a clear message
  if one is missing. It never prints them.
- Validates input at the edges (file exists, type is right, size is sane).
- Leaves one runnable check for non-trivial logic (Ponytail rule).
