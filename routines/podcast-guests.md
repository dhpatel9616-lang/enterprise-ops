# Podcast Guest Research (step of Builder + Leads, Wednesdays)

The owner lists people they want on The Sovereign podcast in Notion →
Automation (Claude-managed) → **Podcast Guests** (data source
`collection://5c31eab0-40f8-4d8a-988b-b08c46fb8746`). Your job is to make each
new row ready for the invite emails, which send on their own (Enterprise-leads
`ingest/podcast-guests.js` picks up Ready rows before Thursday's 9:34 AM ET
outreach run). Query with view mode or fetch, never SQL mode (CLAUDE.md rule 9).

For up to 10 rows with Status **Wanted** (oldest first), set Researching, then:

1. **Who they are:** a living public figure (author, academic, journalist,
   comedian, creator, official). A private person, a minor, or someone who
   has died: Status "Needs owner", with the reason in Raw Notes.
2. **Contact:** find a publicly listed address meant for this: the booking,
   press or speaking contact on their official site, their agent or
   publicist as named on that site, a university faculty page, or the
   contact email on their own newsletter or podcast. Put it in Contact email
   and the page in Contact source. **Never guess an address** (no
   firstname@domain patterns) and never use data-broker, leaked, or
   "find anyone's email" sites. Only a contact form or a booking agency
   with no email: Status "Needs owner", form link in Contact source. Nothing
   public: "No contact found".
3. **Personal line** (the invite's opening sentence, `brand-voice` → the
   owner's voice): one sentence naming a specific, real piece of their work
   and what it did for the owner or why it fits the show. Use the owner's
   "Why them" if given. Check the work exists. No flattery clichés ("huge
   fan", "your incredible work"), no claims about audience size.
4. **Topic idea:** one line connecting their work to The Sovereign's topics
   (philosophy, policy, history, readiness, the human condition).
5. Contact email and Personal line both filled: Status **Ready**.

Then, for rows with Status Queued whose Raw Notes show a reply: set
**Replied** and add a line to the Strategy Memo's owner to-do ("<name>
replied to the podcast invite: answer in Gmail"). Never reply to a guest
yourself.

Report in the memo: how many rows moved to Ready, Needs owner, No contact
found, and any replies.
