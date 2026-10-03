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
| Strategist · SEO Lead · Creative Lead · Designer · Developer · Content Lead · Compliance Reviewer · Independent QA Reviewer | select (team list), one field each | SOP roles (Creative Lead may be the senior designer or Project Lead on smaller projects). Chirply has no user-type custom field. One person may hold several roles, but every stage still has one named owner (SOP) |
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

- **Task lists:** one per stage (`S00 Brief` … `S14 Measurement`).
- **In each list:** one **stage task**, named per the AI pack convention, e.g.
  `S03 — Positioning — 3A → 3B + 3C → 3D → 3E`.
  - Assignees: the stage **owner** (SOP) and the **reviewer**. They must be **project members**
    (V2), so add the project team as members at set-up.
  - Due date: stage deadline.
  - Status: project boards are fixed at To do / In progress / Done, and project tasks have no tags
    (V10). The Tracker's stage statuses are expressed like this:

    | Tracker status | In Chirply |
    |---|---|
    | Not Started | Stage task open; deal not yet at this stage |
    | In Progress | Deal is at this pipeline stage; task in *In progress* |
    | Blocked | Deal field **Health = Blocked** + Blocker text |
    | Ready for Review | All DoD subtasks done; `✔ Reviewer sign-off` still open |
    | Complete | Stage task completed (reviewer signed off); deal moved on |
    | N/A | Stage task completed with `N/A —` prefixed to its title, plus a deal note giving the reason |

  - Description: **plain text** (V4). A short version of the stage card, with **bare URLs, one per
    line**. The full stage card with formatted links goes in a **project notebook** (HTML), one per stage.
- **Subtasks of the stage task:**
  - one per **SOP Definition of Done** item;
  - one per **"also required"** gate check (validator PASS, approval recorded, lock recorded);
  - a final `✔ Reviewer sign-off — <reviewer>` subtask.
- **Stage 12** has three gate tasks, `QA — Compliance` (Compliance Reviewer), `QA — Strategy / UX`
  (Independent QA Reviewer) and `QA — Technical / SEO` (Developer + SEO Lead). Each has a single
  `Gate sign-off` subtask. The 29 individual checks live in the Tracker **QA** tab and are not
  duplicated as subtasks.

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

The description is generated from `dist/stage-config.json` (per release), so it always matches GitHub.
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
☐ Reviewer sign-off

APPROVAL
Required: Yes (client strategic approval). On approval, lock: Positioning.

METHOD
SOP Stage 3 → [open]   Playbook §4 Positioning Thesis → [open]   Playbook §11 Brand Architecture → [open]

HANDOFFS
• H02 Strategist → SEO Lead → [open]   • H03 Strategist → Designer → [open]

NEXT
Stage 04 — IA + SEO                      Stage card → [open]   OS version: v1.0
```

In the stage task description each `[open]` becomes a **bare URL** on its own line, because
descriptions are plain text (V4). Whether bare URLs are auto-linked is a UI check. The same card with
proper links lives in the stage's **project notebook** (HTML), which keeps `<a href>` links.

## 3. Moving stage: the human gate

1. The owner works through the DoD subtasks and runs the validator. Project tasks can't take comments
   (V3), so **the PASS/FAIL/BLOCKED result is logged as a note on the deal timeline**, e.g.
   `S03 — 3D validator: PASS — <link to the report in Drive>`.
2. For client-gated stages, the Approval Record is set to **Approved**, with an evidence link.
3. When all DoD subtasks are done, the stage is **Ready for Review**. The reviewer ticks
   `✔ Reviewer sign-off` and completes the stage task (**Complete**).
4. **The Project Lead moves the deal to the next pipeline stage.** This is the "stage complete" event.
5. Automation ([automation map](automation-map.md)) flags any DoD item still open and opens the next
   stage task.

Moving a deal while DoD items are open requires an **authorised exception**: a comment on the stage
task saying who authorised it, why, and which items remain (Workflow Index step 7).

## 4. Operational dashboard

| Need | Where |
|---|---|
| Active redesign projects, current stage, owner, target launch | Pipeline board; saved report over deals (stage × owner) |
| Blocked projects | Deals with Health = Blocked |
| Upcoming approvals | Approval Records with Status = Pending; deal field `Next approval due` |
| Missing inputs | Weekly digest: Tracker *Content Inputs* rows not Verified/N/A (the Tracker's own "Open Inputs" KPI) |
| QA status | Stage 12 gate tasks; weekly digest: Tracker *QA* rows with Status = Fix (the Tracker's "QA Fixes Open" KPI) |
| Overdue items | **Weekly digest**, because Chirply's report builder has no task dataset |

The **weekly digest** is a single email every Monday at 07:30. It is built by Apps Script from
Chirply (deals, stage tasks, approvals) and each project's Tracker Sheet. It reproduces the Tracker
*Dashboard* KPIs (stages complete, open inputs, QA fixes open) across all projects, and answers the
Quickstart's five Monday-morning questions.

## 5. Repeatable set-up for a new client

1. Create the deal from the **deal template** "Website Redesign" (prefills pipeline, stage 00 and fields).
2. Run provisioning ([automation map](automation-map.md), A1). It creates the project, 15 task lists,
   stage tasks with descriptions, DoD and reviewer subtasks from the current release's
   `stage-config.json`, and copies the Drive folder template, Tracker Sheet and MPC Doc.
3. Until provisioning is automated, build the pilot project **by hand** and use it as the pattern
   (implementation plan, step F).
