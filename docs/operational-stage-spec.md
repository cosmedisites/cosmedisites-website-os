# Operational stage spec (Chirply)

How the Website OS appears to the team inside Chirply. **Chirply behaves like the UI for GitHub:
GitHub stays the source.** The SOP says the same: *"The project-management interface should behave
like the UI for the operating system."*

The team member never needs to understand the repository. They open their stage task and see
everything they need, with links.

> The configuration uses Chirply features observed in the [audit](chirply-audit.md). Items marked
> ⚑ depend on verification tests in the CosmediSites workspace. Statuses, roles, owners and
> Definitions of Done come from the SOP v1.0 and Operational Tracker v1.0, via `ops/stages.yaml`.

---

## 1. Data model

### 1.1 Pipeline: "Website Redesign"

- Value tracking **off** (process board).
- Stages, mirroring the SOP's *Project Board Structure*: `00 Brief`, `01 Evidence`, `02 Diagnosis`,
  `03 Positioning`, `04 IA + SEO`, `05 Visual Direction`, `06 Page System`,
  `07 Content + Proof + Photography`, `08 Client Review`, `09 Approval`, `10 Inputs`, `11 Build`,
  `12 QA`, `13 Launch`, `14 Measurement`, plus outcome stages `Complete` (won) and
  `Paused / Cancelled` (lost).

### 1.2 Deal = project record

| Field | Type | Notes |
|---|---|---|
| Title | built-in | `CLIENT — Website Redesign` |
| Company / contact | built-in link | Client and main client contact (approver) |
| Owner | built-in user | **Project Lead** |
| Domain | url | |
| Strategist · SEO Lead · Creative Lead · Designer · Developer · Content Lead · Compliance Reviewer · Independent QA Reviewer | **user (Team member)**, one field each | SOP roles (Creative Lead may be the senior designer or Project Lead on smaller projects). Team-member fields shipped 2026-10-04 (deals only), so deals can be filtered by `member_field` + `member` ("projects where I'm the designer"). One person may hold several roles, but every stage still has one named owner (SOP) |
| Target launch | date | |
| Commercial objective | textarea | One sentence, from the approved Strategy Brief |
| Priority services | multiselect or textarea | |
| Health | select: On track / At risk / **Blocked** | Drives the "blocked projects" view |
| Blocker | text | Required when Health = Blocked (by convention) |
| Next approval due | date | Drives "upcoming approvals" |
| OS version | select: v1.0, v1.1… | The OS version the project started on |
| Master Project Context | url | Google Doc in the project Drive folder |
| Project Tracker | url | Google Sheet copy of Operational Tracker v1.0 |
| Project Strategy Brief · Drive folder · Figma · Client deck · Staging URL | url | |

### 1.3 Project = delivery workspace (one per deal)

Created **automatically from the project template "Website Redesign"** when a deal is made from the
deal template (`deal_templates_create` → `project_template_id`). The project is named after the deal,
starts on the day the deal is created, and is linked to it.

- **Board columns** (renamed from To do / In progress / Done, saved in the template): the Tracker's
  stage statuses **Not Started · In Progress · Blocked · Ready for Review · Complete**. N/A is a tag
  (below), so there are five columns.
- **Tags:** `N/A`, `Client-gated`, `Locks decision`, `Exception authorised`. Set with
  `projects_set_task_tags`, which replaces the task's whole tag list.
- **Task lists:** one per stage (`S00 Brief` … `S14 Measurement`).
- **In each list:** one **stage task**, named per the AI pack convention, e.g.
  `S03 — Positioning — 3A → 3B + 3C → 3D → 3E`.
  - Assignee: the stage **owner** (SOP). Assignees must be project members.
  - **Reviewer:** the native task reviewer (`projects_set_task_reviewer`), i.e. the SOP reviewer for
    that stage. This replaces the old `✔ Reviewer sign-off` subtask.
  - Due date: stage deadline.
  - Description: **plain text** (still no formatting). A short version of the stage card.
  - **Links:** the stage card, SOP section, template, each prompt and the Drive folder are added as
    **task links** (`projects_add_task_link`), so they're clickable without relying on the description.
  - **Comments:** validator results, review notes and decisions go in the task's comment thread
    (`projects_add_comment`). Comments notify the assignee and reviewer.
- **Subtasks of the stage task:**
  - one per **SOP Definition of Done** item;
  - one per **"also required"** gate check (validator PASS, approval recorded, lock recorded).
- **Stage 12** has three gate tasks, `QA — Compliance` (Compliance Reviewer), `QA — Strategy / UX`
  (Independent QA Reviewer) and `QA — Technical / SEO` (Developer + SEO Lead). Each has a native
  reviewer and links to the Tracker **QA** tab, which holds the 29 individual checks (not duplicated
  as subtasks).

How the Tracker's stage statuses map:

| Tracker status | In Chirply |
|---|---|
| Not Started | Stage task in **Not Started** |
| In Progress | Stage task in **In Progress**; the deal is at this pipeline stage |
| Blocked | Stage task in **Blocked**, plus deal **Health = Blocked** and Blocker text (for the pipeline view) |
| Ready for Review | Owner runs **request review** (`projects_request_review`); task moves to **Ready for Review** |
| Complete | Reviewer **approves** (`projects_approve_review`, which completes the task); task moves to **Complete** |
| N/A | Tag **N/A** plus a comment giving the reason; task completed |

> **Change log for this section.** On 2026-10-03, Chirply had no project comments, fixed columns, no
> tags, no reviewer and no project templates, so this section used deal notes, the deal Health field
> and a reviewer subtask. Chirply shipped all five by 2026-10-04 (see the
> [audit update](chirply-audit.md#platform-update-2026-10-04)). These are configuration changes,
> not SOP changes.

### 1.4 Custom object: "Approval Record" (mirrors the Tracker *Approvals* tab)

| Field | Type | Values |
|---|---|---|
| Project | url (deal) | |
| Decision | text | Positioning · Visual direction · Navigation / user journey · Service hierarchy · Practitioner hierarchy · Homepage structure · Photography direction · *project-specific* |
| Level | select | L1 … L5 (combinations such as L1/L3 allowed, as in the Tracker) |
| Owner | select (team) | |
| Status | select | **Pending / Approved / Changes Requested / Locked / N/A** |
| Date | date | |
| Client / Approver | contact_link | |
| Feedback Classification | select | Strategic / Accuracy / User / UX / Compliance / Preference / New Information |
| Notes | text | |
| Locked | checkbox | |
| Evidence link | url | Meeting notes / email / signed document |

Rule (9A): **never infer approval from silence.** Status changes only with an evidence link.
A Locked decision reopens only through 9E change control (SOP *Revision Control*).

### 1.5 Project Tracker (Google Sheet in the project Drive folder)

A copy of Operational Tracker v1.0. Which tab is live where:
[templates/operational-tracker.md](../templates/operational-tracker.md#how-the-tracker-is-used-with-chirply).
In short: **Content Inputs, Proof Inventory, QA (check level) and Measurement live in the Sheet.
Stage status, approvals and the dashboard live in Chirply.**

---

## 2. What a team member sees: the stage task

The description and task links are generated from `dist/stage-config.json` (per release), so they always match GitHub.
Example for Stage 03:

```
STAGE 03 — POSITIONING
Status: In Progress     Owner: Sarah (Strategist)     Reviewer: Creative Lead / Project Lead     Due: 14 Oct
Client involved: Strategic approval

OBJECTIVE
Define the market perception, brand architecture and strategic ideas the new website must make obvious.

INPUTS
• Master Project Context → [open]   • Project Strategy Brief → [open]
• Evidence Pack → [open]            • Strategic Diagnosis → [open]

RUN
• 3A Generate Positioning Directions → [open]
• 3B Select and Sharpen Positioning → [open]
• 3C Brand Architecture → [open]
• 3E Client-Facing Positioning Explanation → [open]   (client-facing)

VALIDATE
• 3D Positioning Validator → [open]

OUTPUT
Positioning Thesis → Template 04 [open] → save to Drive: 03_Positioning/

DEFINITION OF DONE (SOP v1.0, Stage 3)           ticked as subtasks below
☐ Desired perception written.
☐ Wrong perception written.
☐ Positioning thesis agreed internally.
☐ Priority services/categories identified.
☐ Clinic/practitioner relationship defined.
☐ Future growth test passed.
Also required:
☐ No visual design begins until this is internally approved.  (SOP)
☐ 3D validator returns PASS                                    (Workflow Index)
☐ Client strategic approval recorded in the Approval Record
☐ Approved positioning added to LOCKED DECISIONS in the MPC
→ then: Request review (reviewer: Creative / Project Lead)

APPROVAL
Required: Yes (client strategic approval). On approval, lock: Positioning.

METHOD
SOP Stage 3 → [open]   Playbook §4 Positioning Thesis → [open]   Playbook §11 Brand Architecture → [open]

HANDOFFS
• H02 Strategist → SEO Lead → [open]   • H03 Strategist → Designer → [open]

NEXT
Stage 04 — IA + SEO                      Stage card → [open]   OS version: v1.0
```

Each `[open]` is a **task link** (`projects_add_task_link`), so it's clickable even though the
description itself is plain text. The longer stage card can also live in the stage's **project notebook**
(HTML, with version history), but task links remove the need for that on most stages.

## 3. Moving stage: the human gate

1. The owner works through the DoD subtasks and runs the validator. **The PASS/FAIL/BLOCKED result
   is posted as a comment on the stage task**, e.g. `3D validator: PASS — <link to the report in Drive>`.
2. For client-gated stages, the Approval Record is set to **Approved**, with an evidence link.
3. When every DoD subtask is done, the owner **requests review**. The task moves to
   **Ready for Review** and the reviewer is notified.
4. The reviewer either **approves** (task completed → **Complete**) or **returns** it with a comment
   (`projects_return_review`; back to **In Progress**).
5. **The Project Lead moves the deal to the next pipeline stage.** This remains the business-level
   "stage complete" event.
6. Automation ([automation map](automation-map.md)) flags any DoD item still open and opens the next
   stage task.

Moving a deal while DoD items are open requires an **authorised exception**: a comment on the stage
task saying who authorised it, why, and which items remain, plus the tag `Exception authorised`
(Workflow Index step 7).

## 4. Operational dashboard

| Need | Where |
|---|---|
| Active redesign projects, current stage, owner, target launch | Pipeline board; saved report over deals (stage × owner) |
| Blocked projects | Deals with Health = Blocked; stage tasks in the **Blocked** column |
| Upcoming approvals | Approval Records with Status = Pending; deal field `Next approval due` |
| Missing inputs | Weekly digest: Tracker *Content Inputs* rows not Verified/N/A (the Tracker's own "Open Inputs" KPI) |
| Pending reviews | `projects_my_reviews` per reviewer |
| QA status | Stage 12 gate tasks; weekly digest: Tracker *QA* rows with Status = Fix (the Tracker's "QA Fixes Open" KPI) |
| Overdue items | **Weekly digest**, because Chirply's report builder has no task dataset |

The **weekly digest** is a single email every Monday at 07:30. It is built by Apps Script from
Chirply (deals, stage tasks, approvals) and each project's Tracker Sheet. It reproduces the Tracker
*Dashboard* KPIs (stages complete, open inputs, QA fixes open) across all projects, and answers the
Quickstart's five Monday-morning questions.

## 5. Repeatable set-up for a new client

**One-off (before the pilot):**
1. Build the project **"Website Redesign"** once by hand from the stage cards: five status columns,
   tags, 15 task lists, stage tasks with links, DoD subtasks and reviewers. Then
   `projects_save_as_template` it.
   Re-save the template after each OS release; existing projects keep their version.
2. Create or update the **deal template** "Website Redesign" with `project_template_id` set to that
   template.

**Per client:**
1. Create the deal from the deal template. **The project is created automatically and linked to the deal.**
2. Set the deal's team-member role fields. Add the team as project members, and check each stage
   task's assignee and reviewer.
3. Copy the Drive folder template, Tracker Sheet and MPC Doc (manual, or Apps Script: [A1](automation-map.md)).

> To verify on first use: whether the template keeps the renamed columns, tags, subtasks, task
> links and reviewers. `include_people` covers people. Comments, files and completion state are
> never copied, by design.
