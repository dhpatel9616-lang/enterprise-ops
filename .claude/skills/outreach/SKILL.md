---
name: outreach
description: Personalized first-touch cold emails for sourced leads (Enterprise Leads pipeline), tailored by lead type - small business gets the website studio or security audit offer, law firms get legal AI. Every draft names its offer and CTA and meets CAN-SPAM basics. Use when writing or reviewing outreach copy, personalizing leads, or reporting pipeline numbers.
---

# Outreach

## How the pipeline works (existing Enterprise Leads pattern)
1. GitHub Actions in the `enterprise-leads` repo source leads (Google Places)
   into Supabase `skakrtljfaeopfqigyww` → `leads` table and Notion
   **Raw Leads Inbox**.
2. `outreach-sequencer.js` drafts **touch 1** as a Gmail draft (Gmail OAuth)
   and copies it to Notion (*Drafted Message*, *Offer*).
3. The owner reviews it in Notion's **Outreach Approvals** view (phone
   friendly) and ticks **Approve**. Only then does the next run send it.
4. Follow-ups (touches 2-6) send automatically until the lead replies or opts
   out (`check-replies.js` marks replies; an opt-out is a reply).

Never touch Supabase `tzebfwmrmzhkeoptwkzy` (PoolParty production).

## Pick the offer by lead type

| Lead | Signal | Offer | CTA |
|---|---|---|---|
| Small business | no site, broken site, not mobile-friendly | Wade Capital website studio | "Want me to send a free mock-up of a refreshed homepage?" |
| Small business | site works but no SSL, outdated software, exposed login/admin pages, public data leaks | Wade Capital security/risk audit | "Can I send you a free 1-page security check-up for your site?" |
| Small business | site fine, no social presence | Social media management | "Want a sample week of posts for {business}?" |
| Law firm (category `legal`) | any | Legal AI: AI Governance Readiness Audit | "Open to a 15-minute call to see where AI could save your team hours, safely?" |

One offer per email. When two fit, pick the one with the clearest evidence.

## Personalize (one real detail)
- Add one short, specific, checkable sentence from the lead's own site or
  listing (a service they offer, a recent post, a real issue you saw).
  Never invent facts, flattery, or fake familiarity ("loved meeting you").
- The sequencer inserts it from `leads.outreach_context` in Supabase
  `skakrtljfaeopfqigyww`. If you can't write there, put the sentence in the
  lead's Notion *Research Summary* and note "needs outreach_context" in the
  Build Queue.

## Every draft must have
```
Offer: <website studio | security audit | social | legal AI>
CTA: <one question the lead can answer yes to>
```
- Plain, short (under ~120 words), from a real person, honest subject line
  (no "Re:" on a first email, no fake urgency).
- **CAN-SPAM basics** (the sequencer adds these automatically; keep them in
  any hand-written email too):
  - Sender's real name and a working reply address.
  - The business's physical mailing address (a PO box is OK).
  - An opt-out line: *Not interested? Reply "unsubscribe" and I won't email
    you again.* Honor it within 10 business days (our system stops at once).
- No AI characters, testimonials, or claims we can't back up (`content-rules`).

## Pipeline numbers (for the Strategy Memo)
See `strategy-memo-pipeline.md` in this folder for the section and where each
number comes from.
