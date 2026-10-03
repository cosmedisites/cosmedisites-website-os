# STAGE 09 — APPROVAL GATE

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Project Lead *(default role)* | Strategist *(default role)* | *set per project* |

## Objective

Convert client feedback into explicit decisions, controlled revisions and locked strategic choices.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Meeting notes/transcript
- Deck
- Current Approval Record
- Raw client feedback
- Locked decisions
- Classified feedback
- Approved decisions
- Scope

## Run

Route: **9A + 9B → 9C + 9D; use 9E for reopened decisions**

- **[9A — Meeting Notes → Approval Record](prompts.md#9a--meeting-notes--approval-record)** — Immediately after the client review meeting. → *Updated Approval Record.*
- **[9B — Feedback Classifier](prompts.md#9b--feedback-classifier)** — When client comments arrive by email, comments or meeting notes. → *Classified feedback table.*
- **[9C — Revision Plan](prompts.md#9c--revision-plan)** — After feedback is classified. → *Controlled revision plan.*
- **[9D — Approval Follow-Up](prompts.md#9d--approval-follow-up)** — After review meeting / revision round. → *Client email confirming decisions.* `CLIENT-FACING`

## Validate

- **[9E — Change-Control Evaluator](prompts.md#9e--change-control-evaluator)** *(only when an approved decision is challenged)* — When someone tries to reopen an approved decision. → *Decision on whether to reopen.*

## Output

**Approval Record + revision plan**

- Template 12 — [Approval Record](../../templates/approval-record.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Every decision classified (Approved / Changes Requested / Pending / Locked / Not discussed)
- [ ] No approval inferred from silence
- [ ] Every change request has an owner and a deadline
- [ ] Revision plan protects LOCKED decisions
- [ ] Follow-up sent to the client asking for specific outstanding decisions
- [ ] Client sign-off recorded
- [ ] Approved decisions added to LOCKED DECISIONS in the Master Project Context

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Client sign-off**
- Required: client approval
- On approval, lock: **Approved strategic decisions** (add to LOCKED DECISIONS in the Master Project Context)

## Handoffs and client communication

- [H08 — Project Lead → Client](../../prompts/team-handoffs/role-handoff-prompts.md#h08--project-lead--client)
- [C04 — Strategy Review Follow-Up](../../prompts/client-communications/client-communication-prompts.md#c04--strategy-review-follow-up)
- [C06 — Revision Summary](../../prompts/client-communications/client-communication-prompts.md#c06--revision-summary)

## Next

[Stage 10 — Production Inputs](../stage-10-production-inputs/README.md)
