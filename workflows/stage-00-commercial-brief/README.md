# STAGE 00 — COMMERCIAL BRIEF

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Project Lead / Strategist | Project Lead | Yes | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

## Objective

Convert discovery information into a commercial brief that governs every downstream decision.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Known client/domain information
- Scope
- Existing sales notes
- Discovery notes
- Sales notes
- MASTER PROJECT CONTEXT if present

## Run

Route: **0A → 0B → 0C; use 0D if blocked**

- **[0A — Discovery Prep](prompts.md#0a--discovery-prep)** — Before the client kick-off or discovery call. → *Focused discovery agenda.*
- **[0B — Generate Project Strategy Brief](prompts.md#0b--generate-project-strategy-brief)** — Immediately after discovery when the call notes, scope and existing data are available. → *Project Strategy Brief matching Template 01.*
- **[0D — Client Clarification Request](prompts.md#0d--client-clarification-request)** *(only if OPEN items block strategy)* — When Stage 0 has OPEN items that materially block strategy. → *Concise client email/message requesting missing facts.* `CLIENT-FACING`

## Validate

- **[0C — Commercial Brief Validator](prompts.md#0c--commercial-brief-validator)** — Before Stage 0 is marked complete. → *PASS/FAIL/BLOCKED validation report.*

## Output

**Project Strategy Brief**

- Template 01 — [Project Strategy Brief](../../templates/project-strategy-brief.md)

## Definition of Done

*Source: SOP, Stage 0 — Project Strategy Brief*

- [ ] Business objective is explicit.
- [ ] Growth model and priority services are understood.
- [ ] Audience and buying anxieties are documented.
- [ ] Website role in acquisition is clear.
- [ ] Known SEO/compliance constraints are captured.
- [ ] Client confirms the factual brief.

**Also required before moving stage:**

- [ ] The team can answer: What does this business need the new website to achieve? What would make the redesign commercially unsuccessful even if it looked excellent? *(SOP Stage 0)*
- [ ] 0C validator returns PASS *(Workflow Index step 7)*
- [ ] Master Project Context created in the project Drive folder *(AI Workflow Pack README (Recommended workspace))*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **Client factual confirmation**
- Gate: Client factual confirmation

## Method

- SOP: [Stage 0 — Project Strategy Brief](../../sop/website-redesign-sop.md#stage-0--project-strategy-brief)
- Playbook: [1. The CosmediSites Redesign Framework](../../playbook/website-strategy-playbook.md#1-the-cosmedisites-redesign-framework)
- Playbook: [2. Rule Zero: Diagnose Before Designing](../../playbook/website-strategy-playbook.md#2-rule-zero-diagnose-before-designing)
- Playbook: [15. Business Outcomes](../../playbook/website-strategy-playbook.md#15-business-outcomes)

## Handoffs and client communication

- [H01 — Project Lead → Strategist](../../prompts/team-handoffs/role-handoff-prompts.md#h01--project-lead--strategist)
- [C01 — Kick-Off Email](../../prompts/client-communications/client-communication-prompts.md#c01--kick-off-email)
- [C02 — Discovery Input Request](../../prompts/client-communications/client-communication-prompts.md#c02--discovery-input-request)

## Next

[Stage 01 — Evidence](../stage-01-evidence/README.md)
