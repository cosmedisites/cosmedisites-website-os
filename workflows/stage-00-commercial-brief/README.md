# STAGE 00 — COMMERCIAL BRIEF

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Strategist *(default role)* | Project Lead *(default role)* | *set per project* |

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

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Primary commercial objective stated
- [ ] Measurable success metric recorded (or marked OPEN)
- [ ] Priority revenue services identified
- [ ] Services / categories to grow identified
- [ ] Target audience and main anxieties defined
- [ ] Current and planned locations recorded
- [ ] Current and planned team recorded
- [ ] Current lead sources and booking method recorded
- [ ] Website's role in acquisition stated
- [ ] Known SEO priorities recorded
- [ ] Compliance / operational constraints recorded
- [ ] Actual business reason for the redesign stated
- [ ] “This redesign succeeds if…” and “fails even if it looks good if…” completed
- [ ] No inference presented as fact (0C)
- [ ] Client has confirmed the facts
- [ ] Master Project Context created

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Client factual confirmation**
- Required: client approval

## Handoffs and client communication

- [H01 — Project Lead → Strategist](../../prompts/team-handoffs/role-handoff-prompts.md#h01--project-lead--strategist)
- [C01 — Kick-Off Email](../../prompts/client-communications/client-communication-prompts.md#c01--kick-off-email)
- [C02 — Discovery Input Request](../../prompts/client-communications/client-communication-prompts.md#c02--discovery-input-request)

## Next

[Stage 01 — Evidence](../stage-01-evidence/README.md)
