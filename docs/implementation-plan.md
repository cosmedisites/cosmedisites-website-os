# Implementation plan

Don't automate everything on day one. Each phase has an exit criterion. Don't start the next phase
until it is met. This is the OS's own "move on Definition of Done" rule, applied to itself.

## Phase 1 — Source of truth (GitHub) · week 1

| Step | Owner | Status |
|---|---|---|
| Repository structure, governance files, CI, stage registry, stage cards | Claude | ✅ done |
| Import Playbook, SOP v1.0, Template Pack v1.0 (17 templates) and Tracker v1.0 structure from Source Pack v1.0 | Claude | ✅ done |
| Reconcile SOP owners and Definitions of Done into `ops/stages.yaml`; regenerate stage cards, QA gates and README | Claude | ✅ done |
| Review the branch, then create `main` from it (PR → squash merge). The remote had no `main` when this work started | Admin | ☐ |
| Configure branch protection/ruleset, labels and merge settings ([governance](governance.md)) | Admin | ☐ |
| Decide on GitHub Team plan (needed to *enforce* protection on a private repo) | Admin | ☐ |
| Add at least one second reviewer; create teams; update CODEOWNERS | Admin | ☐ |
| Tag `v1.0`. Attach the Template Pack DOCX, Operational Tracker XLSX, AI Workflow Quickstart DOCX and the Source Pack zip to the release | Admin | ☐ |
| Upload the Operational Tracker to Drive as the master **Google Sheet** template ("make a copy" per project) | Project Lead | ☐ |

**Exit:** `main` protected and `v1.0` released.

## Phase 2 — Chirply audit · week 1–2

| Step | Owner |
|---|---|
| Desk audit of Chirply's capabilities ([chirply-audit.md](chirply-audit.md)) | ✅ done (catalogue-level; wrong workspace, see caveat) |
| Connect the **CosmediSites** Chirply workspace and confirm its plan (V1, V8) | Admin |
| Run verification tests **V2–V9** in the CosmediSites workspace (≈ 60 min) | Project Lead + Claude |
| Confirm Option A, or switch to the Option B fallback | Owner/MD |

**Exit:** a documented decision based on tests in the real workspace.

## Phase 3 — Manual operating system · weeks 2–3

| Step | Owner |
|---|---|
| Configure the pipeline, deal fields, Approval Record custom object and deal template ([spec](operational-stage-spec.md)) | Project Lead |
| Build **one reference project by hand**: 15 task lists, stage tasks with descriptions copied from the stage cards, DoD subtasks, reviewer subtasks | Project Lead |
| Create the Drive folder template + Input Tracker / Proof Inventory / QA Log sheets + MPC Doc | Project Lead |
| Dry-run Stages 00–03 on an internal or past project | Team |

**Exit:** a team member can answer the five Monday-morning questions from Chirply alone.

## Phase 4 — AI integration · week 3–4

| Step | Owner |
|---|---|
| One Claude Project per active client, set up per the [AI execution workflow](ai-execution-workflow.md) | Strategist |
| Stage task descriptions link each prompt, validator and template (from `stage-config.json`) | Project Lead |
| Validator results pasted to stage tasks as standard | Everyone |

**Exit:** two stages completed with the four-input pattern, and validator results recorded.

## Phase 5 — Automation · weeks 5–8

Build in this order, each only after the manual version has worked on a live project:
A6 (native, trivial) → A2 → A3 → A5 → A8 → A4 → A7 → A1 (provisioning) → A9.
See the [automation map](automation-map.md).

**Exit:** a new project is provisioned in under 10 minutes, and the weekly digest arrives.

## Phase 6 — Pilot · one full project

Run a real CosmediSites redesign through Stages 00–14. Track friction in GitHub Issues as it happens.
Capture the first anonymised examples after Stage 9.

**Exit:** pilot past Stage 13, with every friction point logged.

## Phase 7 — v1.1

Fortnightly triage → accepted improvements → `v1.1` release with changelog. Typically: DoD
wording, missing template fields, automation fixes.

---

## Open questions / things requiring access

### Resolved by Source Pack v1.0

- ~~Supply Playbook, SOP, Template Pack and Tracker~~ → imported.
- ~~Do the SOP's DoD and owners differ from the interim ones?~~ → yes, in places. The SOP now
  governs. Notable corrections: the Strategy / UX QA gate is owned by an **Independent QA Reviewer**,
  not the Strategist; Stage 0 is owned by Project Lead / Strategist; Stage 13 by Project Lead (the
  Developer is technical owner).
- ~~Is Template 05 "Current → Proposed Summary"?~~ → confirmed.

### Still open

| # | Question | Needed for | Who |
|---|---|---|---|
| Q1 | **Which Chirply workspace does CosmediSites use?** The connector available here is "FM Recruitment & Provision". Please connect the CosmediSites workspace, or confirm it is a client account under an agency | Phase 2 | MD / Admin |
| Q2 | Who is the agency managing that Chirply account? Can it enable `appDev`/App Marketplace and confirm the plan features? | V1, V8 | Admin |
| Q3 | The SOP has **no Definition of Done checklist for Stages 9, 13 and 14**. The stage cards use the matching template's DoD (Templates 12, 16, 17) plus the SOP's stated rules. Confirm this, or add SOP checklists in v1.1 | Methodology | Methodology owner |
| Q4 | Minor owner wording differences between SOP and Tracker (e.g. Stage 4 "Strategist + SEO Lead" vs "SEO Lead / Strategist"; Stage 10 "Project Lead / Content Lead" vs "Content / Project Lead"). The SOP wording is used. Align the Tracker in v1.1? | Consistency | Methodology owner |
| Q5 | The SOP and Tracker name Stage 3 and 5 reviewers as **Creative / Creative Lead**, but the SOP role table has no Creative Lead role. Is it the Designer, a separate role, or the Project Lead? | Chirply role fields | Head of Strategy |
| Q6 | GitHub plan: Free or Team? Who will be the second reviewer? | Branch protection | Admin |
| Q7 | Add an explicit **AVOID** bucket to the strategist → designer handoff? It is currently covered by DO NOT CHANGE + DO NOT DO ([handoffs](handoffs.md)) | Methodology | Head of Strategy |
| Q8 | Team names for the role select fields, and who holds the Independent QA Reviewer role | Chirply config | Project Lead |
| Q9 | Agree the Tracker tab split (Chirply owns stage status, approvals and dashboard; the Sheet owns inputs, proof, QA checks and measurement), so nothing is maintained twice | Phase 3 | Project Lead |
| Q10 | Are Notion and/or MonoDesk actively used and paid for? Their connectors are attached to this account. This only matters if the fallback is triggered | Option B | MD |
| Q11 | Slack in use? Chirply has no native Slack, so notifications are email by default | A2/A7 | MD |
| Q12 | Google Workspace edition and who owns Apps Script projects (use a shared/service account, not a personal one) | Phase 5 | Admin |
| Q13 | Jurisdiction-specific compliance sources (e.g. ASA/CAP, GMC/NMC/GDC guidance) to reference in the Compliance gate | 12A | Compliance Reviewer |
