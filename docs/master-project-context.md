# Master Project Context: creation, maintenance and storage

The Master Project Context (MPC) is the single, current block of confirmed commercial and strategic
facts for one client project. Every AI task receives it first. Every human handoff relies on it.

Template: [workflows/00-master-project-context.md](../workflows/00-master-project-context.md)

## Recommendation: a Google Doc in the project's Drive folder

**Location:** `Drive › Clients › <Client> › Website Redesign <YYYY> › 00_Admin › Master Project Context`
(a native Google Doc, not a .docx).

| Option | Verdict | Why |
|---|---|---|
| **Project Google Drive (Google Doc)** | ✅ **Recommended** | Client data stays with the other client files, under the same restricted sharing. Full version history, plus **named versions** at each approval. Comments for review. Every team member can edit it without Git. Claude and ChatGPT can read it directly (Drive connectors) or have it pasted in. It can be linked from Chirply in one URL field. |
| Chirply (deal notes / custom field) | ❌ | Task and CRM descriptions are plain text with no structure. Notes are timeline items, not a living document. No version history suitable for LOCKED/OPEN tracking. Hard to hand to an AI tool cleanly. |
| Project-specific private Git repo | ❌ | Puts client data into GitHub, against the core principle. Non-technical team members would need Git. Version control is more than this needs. |
| Claude/ChatGPT project knowledge only | ❌ | The AI tool becomes the system of record; the pack says it must not be. Use it as a *copy* refreshed from the Doc. |

Chirply holds the **link** (deal field `Master Project Context`). The AI project holds a **copy**,
refreshed when the Doc changes. The Doc is the original.

## How it is created

| When | Who | What |
|---|---|---|
| Project set-up | Project Lead | Copy the template into the Drive folder as a Google Doc. Fill PROJECT basics from the signed scope. Link it on the Chirply deal |
| End of Stage 00 | Strategist | Populate COMMERCIAL, AUDIENCE, GROWTH MODEL from the approved Project Strategy Brief. Every fact tagged `[CONFIRMED]`, `[OBSERVED]`, `[INFERRED]` or `[OPEN]` |
| Each stage exit | Stage owner | Update the relevant section(s) and `Current stage`; add the artefact link under CURRENT ARTEFACTS |
| Each approval (Stages 3, 5, 9 …) | Project Lead | Add the decision to **LOCKED DECISIONS**, with date and Approval Record link. Create a **named version** in Doc history, e.g. `v1.0 APPROVED — Positioning — 2026-10-14` |

## Maintenance rules

1. **One MPC per client project.** A second project for the same client gets a new MPC; carry over
   only facts that are still true.
2. **Confirmed facts only, clearly tagged.** Distinguish CONFIRMED / OBSERVED / INFERRED / OPEN /
   LOCKED (AI Operating Rules §2). An INFERRED item never becomes client-facing fact.
3. **Update when genuine decisions or facts change**, not on every conversation.
4. **Never casually rewrite LOCKED decisions.** A locked item changes only after a
   [9E Change-Control](../workflows/stage-09-approval/prompts.md) decision of REOPEN. When that
   happens, strike through the old line (don't delete it), add the new decision with date and
   reason, and note the downstream stages affected.
5. **Don't delete OPEN items until resolved.** Resolve them by moving them into the right section
   as CONFIRMED.
6. **Keep it short.** If a section needs more than a few lines, link to the artefact instead. The MPC
   is loaded into every AI task, so length costs accuracy.
7. **Never push an MPC, or any filled-in part of it, into the OS GitHub repository.**
8. **Add a change log at the bottom of the Doc:** `date — section — change — by — reason`.

## Access

- Share with the project team only, not "anyone with the link".
- The client doesn't get edit access. Share an exported, client-safe summary if needed
  (H08 / C-prompts translate the content).
