# To-Do Email (Thursdays ~8 AM ET)

Read only ~/enterprise-ops/CLAUDE.md. READ-ONLY run: change nothing anywhere;
send one email.

Notion: view mode or fetch only, never SQL. Retry temporary Notion errors up
to 3 times, 60 s apart.

Collect only what needs the owner:
1. Open PRs waiting to merge in dhpatel9616-lang/enterprise-ops and
   dhpatel9616-lang/Enterprise-leads (title + link).
2. Leads who replied or asked for a call back in the last 7 days (Supabase,
   ENTERPRISE_SUPABASE_URL / ENTERPRISE_SUPABASE_SERVICE_KEY via REST, or the
   Supabase connector on project skakrtljfaeopfqigyww; read only: status = replied, or call_outcome in (interested, callback)): business,
   phone or email, one-line note. These are warm leads; the owner replies.
3. Notion → Automation Control rows whose Last Run Status is Error (one line
   each), and Build Queue items that are Blocked on the owner (quote the
   action).
4. Buffer: posts scheduled for the next 7 days, and any in error.

Email dhpatel9616@gmail.com only, subject "Enterprise to-do: <YYYY-MM-DD>",
plain text, under 200 words: "Top 3" (link + minutes each), then the rest
grouped as above, skipping empty sections. If nothing needs the owner, say so
in one line. Never mention outreach approvals or recordings; never include an
address or anything from settings.
