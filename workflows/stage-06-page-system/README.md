# STAGE 06 — PAGE + COMPONENT SYSTEM

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | Designer *(default role)* | Strategist *(default role)* | *set per project* |

## Objective

Create reusable page and component patterns that scale across treatments, concerns, practitioners, locations and future growth.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Positioning Thesis
- Sitemap
- Proof inventory
- Visual principles
- Approved IA
- Brand Architecture
- Proof requirements
- Page templates
- Visual system
- Desktop page architecture / mockups
- Conversion priorities

## Run

Route: **6A + 6B + 6C + 6D → 6E**

- **[6A — Homepage Architecture](prompts.md#6a--homepage-architecture)** — After IA and visual direction are approved. → *Homepage section architecture.*
- **[6B — Page Template Generator](prompts.md#6b--page-template-generator)** — When defining treatment, concern, practitioner, result and other core templates. → *Reusable page-template specifications.*
- **[6C — Component Library Specification](prompts.md#6c--component-library-specification)** — Once page templates are known. → *Component inventory and rules.*
- **[6D — Mobile Adaptation](prompts.md#6d--mobile-adaptation)** — Before approving page systems. → *Mobile UX specification.*

## Validate

- **[6E — Scalability Validator](prompts.md#6e--scalability-validator)** — Before Stage 6 is marked complete. → *Scalability QA.*

## Output

**Page / Component System**

- Template 08 — [Page + Component System](../../templates/page-component-system.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Homepage architecture defined section by section
- [ ] Each page template has a distinct job
- [ ] Component library specified, including empty / missing-data behaviour
- [ ] Mobile behaviour defined deliberately (not just "stack vertically")
- [ ] 6E scalability scenarios pass with no routine growth needing an architecture change

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Internal / included in review**
- Internal sign-off only

## Next

[Stage 07 — Proof + Content + Photography](../stage-07-proof-content-photography/README.md)
