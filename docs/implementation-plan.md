# Implementation plan

Don't automate everything on day one. The OS's own rule applies to its roll-out: **move on when the
Definition of Done is met**, not when a step feels approximately finished.

## v1.0 success definition

v1.0 succeeds if **a new team member can**:

1. start a redesign;
2. know which stage it is in;
3. see the stage's owner, Definition of Done, prompts and templates;
4. produce the correct artefact;
5. obtain the required approval;
6. move to the next stage

…**without asking where anything lives.** If that works, the operating system is doing its job.
The pilot project tells us what actually needs changing next.

## Agreed sequence (decided 2026-10-03)

| Step | What | Owner | Status |
|---|---|---|---|
| **A** | Connect the real CosmediSites Chirply workspace and run verification tests V1–V10 ([results](chirply-audit.md#verification-results-cosmedisites-workspace)) | Claude + Admin | ✅ run 2026-10-03: Option A confirmed. V5 firing and V7 are confirmed during pilot set-up; delete 2 leftover test objects in the UI |
| **B** | Resolve Q3/Q4/Q5/Q7 and bake them into **v1.1 candidates** (see [decisions](#decisions-log)) | Claude | Prepared on the branch as a separate commit, not in v1.0 |
| **C** | Review the GitHub branch once for structure and content correctness | MD | ☐ |
| **D** | Create `main` from the v1.0 commit and tag `v1.0` | MD | ☐ |
| **E** | Attach the Template Pack DOCX, Operational Tracker XLSX and complete Source Pack ZIP to the `v1.0` release | MD | ☐ |
| **F** | Run one real CosmediSites redesign through the system end-to-end (pilot) | Team | ☐ |
| **G** | Log friction as GitHub Issues during the pilot. **Don't edit the SOP mid-pilot** | Team | ☐ |
| **H** | After the pilot, release **v1.1**: the v1.1 candidates plus accepted pilot fixes | MD | ☐ |

### Supporting work inside F (pilot)

**Manual operating system first.** Before the pilot's Stage 00:

| Step | Owner |
|---|---|
| Configure the Website Redesign pipeline, deal fields, Approval Record custom object and deal template ([spec](operational-stage-spec.md)) | Project Lead |
| Build the pilot's Chirply project **by hand**: 15 task lists, stage tasks with descriptions from the stage cards, DoD subtasks, reviewer subtasks | Project Lead |
| Create the Drive folder: Project Tracker Sheet (copy of the Tracker master) and Master Project Context Doc | Project Lead |
| One Claude Project for the pilot client, per the [AI execution workflow](ai-execution-workflow.md) | Strategist |

**Automation only after the manual version works** on the pilot. Build in this order:
A6 (native, trivial) → A2 → A3 → A5 → A8 → A4 → A7 → A1 (provisioning) → A9.
See the [automation map](automation-map.md). Exit: a new project is provisioned in under 10 minutes
and the weekly digest arrives.

## Decisions log

| # | Decision (2026-10-03) | Where it lands |
|---|---|---|
| D1 | Stages 9, 13 and 14: the template-derived Definitions of Done (Templates 12, 16, 17) become **official** and are added to the SOP | v1.1 candidate: SOP + registry. The registry then has no fallback path; every stage's DoD must match the SOP (CI-enforced) |
| D2 | **Creative Lead** is a defined role, not necessarily a separate hire: "accountable for visual/brand quality; may be fulfilled by the senior designer or Project Lead on smaller projects" | v1.1 candidate: SOP role table + registry roles |
| D3 | **The SOP is canonical** for owner wording (Stages 4 and 10). The Tracker mirrors the SOP and doesn't compete with it | v1.1 candidate: Tracker workbook + Tracker spec |
| D4 | Add an **AVOID** bucket: designer handoffs use `LOCKED / FLEXIBLE / REQUIRED / AVOID / OPEN` | v1.1 candidate: AI Operating Rules §10, prompts H03 and 5C, Quickstart, handoffs doc |
| D5 | **Don't add Notion.** Option A (Chirply) is provisional, conditional on V1–V10 in the real workspace | Chirply audit |
| D6 | **Tracker split agreed:** Chirply owns workflow, status and approvals; the project Google Sheet owns Inputs, Proof, QA checks and Measurement | Operational stage spec; Tracker spec |
| D7 | **Lightweight governance for v1.0:** `main` = production; PRs for material changes; the maintainer's own approval is the release gate until a second reviewer exists | [governance](governance.md#review-model-two-phases) |

## Open questions / things requiring access

| # | Question | Needed for | Who |
|---|---|---|---|
| Q1 | Chirply follow-ups: delete the 2 leftover test objects; UI checks (bare-URL links, board columns, project chats); V5 firing on the pilot deal; V7 API key when automating ([audit](chirply-audit.md#still-to-confirm-no-extra-risk-do-during-pilot-set-up)) | Pilot set-up | Admin |
| Q6 | GitHub plan: Free or Team? Who will be the second reviewer, and when? | Phase 2 governance | MD |
| Q8 | Team names for the role select fields, and who holds the Independent QA Reviewer and Creative Lead roles on the pilot | Chirply config | Project Lead |
| Q11 | Slack in use? Chirply has no native Slack, so notifications are email by default | Automations A2/A7 | MD |
| Q12 | Google Workspace edition, and who owns Apps Script projects (use a shared/service account, not a personal one) | Automation | Admin |
| Q13 | Jurisdiction-specific compliance sources (e.g. ASA/CAP, GMC/NMC/GDC guidance) for the Compliance gate | 12A | Compliance Reviewer |

Resolved: Q3 → D1 · Q4 → D3 · Q5 → D2 · Q7 → D4 · Q9 → D6 · Q10 → D5 · Source Pack imported.
