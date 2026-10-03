# STAGE 08 — CLIENT STRATEGY REVIEW

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Project Lead | Strategist / Designer | Yes | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

## Objective

Turn the approved internal strategy into a concise client presentation that earns decisions rather than vague feedback.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Project context
- Positioning
- Current→Proposed
- Mockups
- Proof
- Page system
- Draft deck
- Approved client deck

## Run

Route: **8A → 8B → 8C → 8D**

- **[8A — Client Strategy Deck Generator](prompts.md#8a--client-strategy-deck-generator)** — When strategy, IA and visual direction are sufficiently mature. → *12–16 slide deck outline/copy.*
- **[8B — Deck Compression / Edit](prompts.md#8b--deck-compression--edit)** — When the draft deck is too long or text-heavy. → *Tighter client deck preserving strategic content.*
- **[8C — Presenter Notes](prompts.md#8c--presenter-notes)** — Before the strategy review meeting. → *Speaker notes and decision prompts.*

## Validate

- **[8D — Client Deck Red Team](prompts.md#8d--client-deck-red-team)** — Before sending/presenting. → *Red-team QA.*

## Output

**Client Strategy Deck**

- Template 11 — [Client Strategy Deck](../../templates/client-strategy-deck.md)

## Definition of Done

*Source: SOP, Stage 8 — Client Strategy Review*

- [ ] Deck tells a strategic story.
- [ ] Commercial outcome is explicit.
- [ ] Client approval items are explicit.
- [ ] Inputs/next steps are separated from approvals.

**Also required before moving stage:**

- [ ] Internal quality test passed: someone who did not work on the design can answer the 60-second questions *(Playbook §23)*
- [ ] 8D red team returns PASS *(Workflow Index step 7)*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **Review meeting**
- Gate: Review meeting

## Method

- SOP: [Stage 8 — Client Strategy Review](../../sop/website-redesign-sop.md#stage-8--client-strategy-review)
- Playbook: [16. Client Strategy Presentation](../../playbook/website-strategy-playbook.md#16-client-strategy-presentation)
- Playbook: [23. Internal Quality Test](../../playbook/website-strategy-playbook.md#23-internal-quality-test)

## Handoffs and client communication

- [C03 — Strategy Review Invitation](../../prompts/client-communications/client-communication-prompts.md#c03--strategy-review-invitation)

## Next

[Stage 09 — Approval Gate](../stage-09-approval/README.md)
