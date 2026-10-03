# STAGE 09 — APPROVAL GATE

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Project Lead | — | Yes | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

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

**Approval Record**

- Template 12 — [Approval Record](../../templates/approval-record.md)
- Project Tracker tab(s): Approvals ([structure](../../templates/operational-tracker.md))

## Definition of Done

*Source: SOP, Stage 9 — Approval Gate*

- [ ] Every strategic decision has a status.
- [ ] Feedback is classified before action.
- [ ] Locked decisions are identified.
- [ ] Client has a clear record of what happens next.

**Also required before moving stage:**

- [ ] Explicit decisions recorded for positioning, visual direction, navigation/user journey, service hierarchy, practitioner hierarchy, homepage structure and photography direction *(SOP Stage 9)*
- [ ] Nothing enters full build until required strategic decisions are approved. *(SOP Stage 9)*
- [ ] Approved decisions added to LOCKED DECISIONS in the Master Project Context *(SOP Revision Control / Deployment Guide)*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **Yes**
- Gate: Client sign-off
- On approval, lock: **Approved strategic decisions**. Add it to LOCKED DECISIONS in the Master Project Context.

## Method

- SOP: [Stage 9 — Approval Gate](../../sop/website-redesign-sop.md#stage-9--approval-gate)
- Playbook: [17. Client Feedback Classification](../../playbook/website-strategy-playbook.md#17-client-feedback-classification)
- Playbook: [18. Revision Control](../../playbook/website-strategy-playbook.md#18-revision-control)
- Playbook: [19. Approval Gate](../../playbook/website-strategy-playbook.md#19-approval-gate)

## Handoffs and client communication

- [H08 — Project Lead → Client](../../prompts/team-handoffs/role-handoff-prompts.md#h08--project-lead--client)
- [C04 — Strategy Review Follow-Up](../../prompts/client-communications/client-communication-prompts.md#c04--strategy-review-follow-up)
- [C06 — Revision Summary](../../prompts/client-communications/client-communication-prompts.md#c06--revision-summary)

## Next

[Stage 10 — Production Inputs](../stage-10-production-inputs/README.md)
