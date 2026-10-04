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
| **A** | Connect the real CosmediSites Chirply workspace and run verification tests V1–V10 ([results](chirply-audit.md#verification-results-cosmedisites-workspace)) | Claude + Admin | ✅ run 2026-10-03: Option A confirmed. Re-checked 2026-10-04 after the Chirply platform update ([update](chirply-audit.md#platform-update-2026-10-04)). V5 firing is confirmed on the pilot deal; V7 (API key) is no longer needed for the pilot |
| **B** | Resolve Q3/Q4/Q5/Q7 and bake them into **v1.1 candidates** (see [decisions](#decisions-log)) | Claude | Prepared on the branch as a separate commit, not in v1.0 |
| **C** | Review the GitHub branch once for structure and content correctness | MD | ☐ |
| **D** | Create `main` from the v1.0 commit and tag `v1.0` | MD | ☐ |
| **E** | Attach the Template Pack DOCX, Operational Tracker XLSX and complete Source Pack ZIP to the `v1.0` release | MD | ☐ |
| **F** | Run one real CosmediSites redesign through the system end-to-end (pilot) | Team | ☐ |
| **G** | Log friction as GitHub Issues during the pilot. **Don't edit the SOP mid-pilot** | Team | ☐ |
| **H** | After the pilot, release **v1.1**: the v1.1 candidates plus accepted pilot fixes | MD | ☐ |

### Supporting work inside F (pilot)

Chirply shipped project templates, reviewers, comments, custom columns, tags, team-member fields
and project-task workflows on 2026-10-04 ([audit update](chirply-audit.md#platform-update-2026-10-04)).
The pilot set-up uses them. These are **configuration quick wins, not SOP changes**, so they are
allowed under the pilot rule (#1).

**Before the pilot's Stage 00** (about half a day, once):

| # | Quick win | Replaces | Owner |
|---|---|---|---|
| 1 | Pipeline "Website Redesign" (15 stages), deal fields with **team-member** role fields, Approval Record custom object ([spec §1](operational-stage-spec.md#1-data-model)) | Select-list role fields | Project Lead |
| 2 | Build **one** project "Website Redesign": columns Not Started / In Progress / Blocked / Ready for Review / Complete; tags N/A, Client-gated, Locks decision, Exception authorised; 15 lists; stage tasks with **task links** to the stage card, SOP, template and prompts; DoD subtasks; **native reviewers**; 3 QA gate tasks. Save it as a **project template** | Building every project by hand; fixed columns; reviewer subtask; bare URLs | Project Lead |
| 3 | Deal template "Website Redesign" with `project_template_id` set, so **every new deal auto-creates its linked project** | Provisioning script (most of A1) | Project Lead (admin) |
| 4 | Create the pilot deal from the deal template; confirm the project appeared and check what the template kept (columns, tags, subtasks, links, reviewers) | Manual check | Project Lead |
| 5 | Workflows **A2** (stage approved → open next), **A6** (launch → 30/60/90 tasks) and the V5 check (deal 00 → 01 creates a task) | Apps Script / API key | Project Lead |
| 6 | Drive folder: Project Tracker Sheet + Master Project Context Doc | Unchanged | Project Lead |
| 7 | One Claude Project for the pilot client ([AI execution workflow](ai-execution-workflow.md)) | Unchanged | Strategist |
| 8 | Delete the two `ZZ-TEST` leftovers (UI only) | Housekeeping | Admin |

**Ways of working that change for the team:** post validator results as **comments** on the stage
task; finish a stage with **Request review**, and the reviewer **approves** or **returns** it;
mark Blocked by moving the task to the **Blocked** column (and setting deal Health).

**Add during the pilot, once the above works:** A3 (approval → lock task), A5 (build approved → QA
gates). A8 (weekly digest) and A4 (overdue inputs) stay Apps Script, because Chirply reports still
have no task dataset.

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
