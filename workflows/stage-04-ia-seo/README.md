# STAGE 04 — IA + SEO

<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->

> This is the stage card: what you need to work this stage. Day-to-day status lives in the
> operational tool (Chirply); this card and the files it links to are the source.

| Status | Owner | Reviewer | Deadline |
|---|---|---|---|
| *set per project* | SEO Lead *(default role)* | Strategist *(default role)* | *set per project* |

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

**Sitemap / SEO Architecture**

- Template 06 — [Sitemap + SEO Architecture](../../templates/sitemap-seo-architecture.md)

## Definition of Done

> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow
> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile
> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).

- [ ] Every primary page has a distinct purpose
- [ ] Priority commercial services have landing pages
- [ ] Concern pages are useful, not thin duplicates
- [ ] Practitioner pages fit the brand architecture
- [ ] Locations structured consistently
- [ ] Valuable existing URLs protected
- [ ] Removed URLs have sensible decisions
- [ ] Internal links support patient journeys
- [ ] Navigation understandable without industry knowledge
- [ ] Future practitioners / treatments / locations can be added
- [ ] Cannibalisation risks identified
- [ ] Redirects known before build
- [ ] Launch-critical SEO risks listed

Do not move stage until every item passes, or an authorised exception is recorded.

## Approval

- Gate: **Conditional client approval**
- Conditional: client approval where the sitemap/URL changes are material

## Handoffs and client communication

- [H04 — SEO Lead → Designer](../../prompts/team-handoffs/role-handoff-prompts.md#h04--seo-lead--designer)

## Next

[Stage 05 — Visual Direction](../stage-05-visual-direction/README.md)
