# Implementation plan

Don't automate everything on day one. Each phase has an exit criterion. Don't start the next phase
until it is met. This is the OS's own "move on Definition of Done" rule, applied to itself.

## Phase 1 — Source of truth (GitHub) · week 1

| Step | Owner | Status |
|---|---|---|
| Repository structure, governance files, stage registry, stage cards, templates, QA gates, CI | Claude (this PR) | ✅ done on branch `claude/optimistic-sagan-jccqln` |
| Create `main` from the reviewed branch (PR → squash merge). The remote had no `main` when this work started | Admin | ☐ |
| Configure branch protection/ruleset, labels and merge settings ([governance](governance.md)) | Admin | ☐ |
| Decide on GitHub Team plan (needed to *enforce* protection on a private repo) | Admin | ☐ |
| Add at least one second reviewer; create teams; update CODEOWNERS | Admin | ☐ |
| **Import Playbook, SOP v1.0, Template Pack v1.0 and Operational Tracker v1.0** (not in the supplied material). Reconcile the SOP's DoD and owners into `ops/stages.yaml` | Methodology owner | ☐ |
| Tag `v1.0`; attach the original AI Workflow Pack zip, Quickstart DOCX and Template Pack files to the release | Admin | ☐ |

**Exit:** `main` protected, SOP imported and reconciled, `v1.0` released.

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

| # | Question | Needed for | Who |
|---|---|---|---|
| Q1 | **Which Chirply workspace does CosmediSites use?** The connector available here is "FM Recruitment & Provision". Please connect the CosmediSites workspace, or confirm it is a client account under an agency | Phase 2 | MD / Admin |
| Q2 | Who is the agency managing that Chirply account? Can it enable `appDev`/App Marketplace and confirm the plan features? | V1, V8 | Admin |
| Q3 | Please supply **Website Strategy Playbook**, **Website Redesign SOP v1.0**, **Redesign Template Pack v1.0** and **Operational Tracker v1.0**. They weren't in the upload and weren't found in Drive | Phase 1 import | Methodology owner |
| Q4 | Do the SOP's Definitions of Done and stage owners differ from the interim ones in `ops/stages.yaml`? | Reconciliation | Methodology owner |
| Q5 | Is Template 05 "Current → Proposed Summary"? This is inferred: the pack's mapping skips 05 | Templates | Methodology owner |
| Q6 | GitHub plan: Free or Team? Who will be the second reviewer? | Branch protection | Admin |
| Q7 | Add an explicit **AVOID** bucket to the strategist → designer handoff? It is currently covered by DO NOT CHANGE + DO NOT DO ([handoffs](handoffs.md)) | Methodology | Head of Strategy |
| Q8 | Team names for Strategist / Designer / Developer / SEO Lead select fields, and the default reviewer per stage | Chirply config | Project Lead |
| Q9 | Are Notion and/or MonoDesk actively used and paid for? Their connectors are attached to this account. This only matters if the fallback is triggered | Option B | MD |
| Q10 | Slack in use? Chirply has no native Slack, so notifications are email by default | A2/A7 | MD |
| Q11 | Google Workspace edition and who owns Apps Script projects (use a shared/service account, not a personal one) | Phase 5 | Admin |
| Q12 | Jurisdiction-specific compliance sources (e.g. ASA/CAP, GMC/NMC/GDC guidance) to reference in the Compliance QA gate | 12A | Compliance Reviewer |
