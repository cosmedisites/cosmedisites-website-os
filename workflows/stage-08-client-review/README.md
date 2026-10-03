# STAGE 08 — CLIENT STRATEGY REVIEW

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Project Lead *(default role)* | Strategist *(default role)* | *set per project* |

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

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] All ten 8D red-team questions answered CLEAR
- [ ] The decisions the client must approve are explicit
- [ ] No new strategy introduced in the deck
- [ ] Presenter notes ready
- [ ] Review meeting held

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Review meeting**
- Required: client review meeting held

## Handoffs and client communication

- [C03 — Strategy Review Invitation](../../prompts/client-communications/client-communication-prompts.md#c03--strategy-review-invitation)

## Next

[Stage 09 — Approval Gate](../stage-09-approval/README.md)
