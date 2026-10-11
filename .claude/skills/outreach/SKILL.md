---
name: outreach
description: Personalized cold emails and AI phone calls for sourced leads (Enterprise Leads pipeline), tailored by lead type - small businesses get the automation menu (websites, file management, AI voice agents, social media), law firms get legal AI. Every draft names its offer and CTA and meets CAN-SPAM basics. Use when writing or reviewing outreach copy, personalizing leads, or reporting pipeline numbers.
---

# Outreach

## How the pipeline works (existing Enterprise Leads pattern)
1. GitHub Actions in the `enterprise-leads` repo source leads (Google Places)
   into Supabase `skakrtljfaeopfqigyww` → `leads` table and Notion
   **Raw Leads Inbox**.
2. `outreach-sequencer.js` sends touch 1 and follow-ups automatically within
   the daily caps (CLAUDE.md rule 1) and copies each one to Notion
   (*Drafted Message*, *Offer*). Copy lives in the Supabase `settings` row
   `outreach`.
3. `bland-calls.js` places AI phone calls to screened business landlines
   (never cell phones) for leads with no working email or no reply after two
   emails. It says it's an AI in its first sentence.
4. Sending stops when the lead replies or opts out (`check-replies.js`, hourly).
   A new human reply emails the owner an alert with a suggested answer.

Never touch Supabase `tzebfwmrmzhkeoptwkzy` (PoolParty production).

## Pick the offer by lead type

| Lead | Signal | Offer | CTA |
|---|---|---|---|
| Small business (email and phone) | no site, broken site, not mobile-friendly, or no social presence | **Automation tailored to the business**, always naming the menu: websites, file management, AI voice agents, social media. Lead with the one the evidence supports (free sample site, sample week of posts). | "Worth a 10-minute call this week?" |
| Small business | site works but no SSL, outdated software, exposed login/admin pages, public data leaks | Wade Capital security/risk audit | "Can I send you a free 1-page security check-up for your site?" |
| Restaurant / café (category `restaurant`, `cafe`) | any | **Starter menu** (`touch_sets.restaurant`): Google listing cleanup, simple site with online ordering, AI phone assistant, review texts, text club; plus the sample site and the phone-agent demo recording when they exist | "Worth a 10-minute call this week?" |
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
  - The mailing address. It lives **only** in the Supabase `settings` row
    `business_mailing_address` (hidden from the anon key by RLS; the
    sequencer reads it with the service key). It is used **only** in
    outgoing Wade Capital service emails to businesses (website, social,
    legal AI, security). Never hard-code it or write it into this repo,
    Notion pages, social posts, videos, or emails to individuals or
    researchers.
  - An opt-out line: *Not interested? Reply "unsubscribe" and I won't email
    you again.* Honor it within 10 business days (our system stops at once).
- No AI characters, testimonials, or claims we can't back up (`content-rules`).

## Pipeline numbers (for the Strategy Memo)
See `strategy-memo-pipeline.md` in this folder for the section and where each
number comes from.
