# STAGE 04 — IA + SEO

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply). This card and the files it links to are the source.

| Status | Owner | Reviewer | Client involved | Deadline |
|---|---|---|---|---|
| *set per project* | Strategist + SEO Lead | Project Lead | Yes if structure changes | *set per project* |

Status values: Not Started · In Progress · Blocked · Ready for Review · Complete · N/A.

## Objective

Protect valuable search equity while structuring the site around patient intent, commercial priorities and future growth.

## Inputs

- Master Project Context for this project (in the project's Drive folder)
- [AI Operating Rules](../00-ai-operating-rules.md)
- Existing URL export
- GSC/analytics if available
- Current sitemap
- Links/rankings if supplied
- Positioning Thesis
- Commercial priorities
- User journeys
- URL inventory
- Approved sitemap
- Brand Architecture
- Existing URL inventory

## Run

Route: **4A → 4B + 4C → 4D → 4E**

- **[4A — Existing URL Preservation Audit](prompts.md#4a--existing-url-preservation-audit)** — Before approving a new sitemap. → *Retain / improve / merge / remove / redirect inventory.*
- **[4B — Build Sitemap / IA](prompts.md#4b--build-sitemap--ia)** — After positioning and URL preservation review. → *Proposed sitemap and navigation model.*
- **[4C — Internal Linking + Ownership Rules](prompts.md#4c--internal-linking--ownership-rules)** — Once sitemap exists. → *Internal-linking rules.*
- **[4D — Migration / Redirect Map](prompts.md#4d--migration--redirect-map)** — When URLs will change. → *Redirect and migration map.*

## Validate

- **[4E — IA + SEO Validator](prompts.md#4e--ia--seo-validator)** — Before design locks navigation/page system. → *PASS/FAIL/BLOCKED IA report.*

## Output

**Approved Sitemap + SEO Architecture Map**

- Template 06 — [Sitemap + SEO Architecture](../../templates/sitemap-seo-architecture.md)

## Definition of Done

*Source: SOP v1.0, Stage 4 — Information Architecture + SEO*

- [ ] Every primary page has a purpose.
- [ ] Every primary page has a user/search intent.
- [ ] Existing high-value URLs have a retain/merge/redirect decision.
- [ ] Navigation model is defined.
- [ ] Internal linking is defined.
- [ ] Location/practitioner architecture is explicit.
- [ ] Redirect requirements are known before build.

**Also required before moving stage:**

- [ ] 4E validator returns PASS *(Workflow Index step 7)*

> Never move to the next stage because the previous one feels approximately finished.
> Move when its Definition of Done has been met, or an authorised exception is recorded.

## Approval

- Approval required: **Conditional (required where service presentation materially changes)**
- Gate: Conditional client approval

## Method

- SOP: [Stage 4 — Information Architecture + SEO](../../sop/website-redesign-sop.md#stage-4--information-architecture--seo)
- Playbook: [21. SEO Architecture Before Final Design](../../playbook/website-strategy-playbook.md#21-seo-architecture-before-final-design)
- Playbook: [8. User Journey](../../playbook/website-strategy-playbook.md#8-user-journey)

## Handoffs and client communication

- [H04 — SEO Lead → Designer](../../prompts/team-handoffs/role-handoff-prompts.md#h04--seo-lead--designer)

## Next

[Stage 05 — Visual Direction](../stage-05-visual-direction/README.md)
