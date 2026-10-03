# Operational stage spec (Chirply)

How the Website OS appears to the team inside Chirply. **Chirply behaves like the UI for GitHub:
GitHub stays the source.**

The team member never needs to understand the repository. They open their stage task and see
everything they need, with links.

> Configuration below uses Chirply features observed in the [audit](chirply-audit.md). Items marked
> ⚑ depend on verification tests in the CosmediSites workspace.

---

## 1. Data model

### 1.1 Pipeline: "Website Redesign"

- Value tracking **off** (process board).
- Stages, in order: `00 Commercial Brief`, `01 Evidence`, `02 Strategic Diagnosis`,
  `03 Positioning`, `04 IA + SEO`, `05 Visual Direction`, `06 Page + Component System`,
  `07 Proof + Content + Photography`, `08 Client Strategy Review`, `09 Approval Gate`,
  `10 Production Inputs`, `11 Build`, `12 QA`, `13 Launch`, `14 Measurement`, plus outcome stages
  `Complete` (won) and `Paused / Cancelled` (lost).

### 1.2 Deal = project record

| Field | Type | Notes |
|---|---|---|
| Title | built-in | `CLIENT — Website Redesign` |
| Company / contact | built-in link | Client and main client contact (approver) |
| Owner | built-in user | **Project Lead** |
| Domain | url | |
| Strategist | select (team list) | No user-type field exists in Chirply |
| Designer | select (team list) | |
| Developer | select (team list) | |
| SEO Lead | select (team list) | |
| Target launch | date | |
| Commercial objective | textarea | One sentence, copied from the approved Strategy Brief |
| Priority services | multiselect or textarea | |
| Health | select: On track / At risk / **Blocked** | Drives the "blocked projects" view |
| Blocker | text | Required when Health = Blocked (by convention) |
| Next approval due | date | Drives "upcoming approvals" |
| OS version | select: v1.0, v1.1… | The OS version the project started on |
| Master Project Context | url | Google Doc in the project Drive folder |
| Project Strategy Brief | url | |
| Drive folder | url | |
| Figma | url | |
| Client deck | url | |
| Staging URL | url | |
| Input Tracker | url | Google Sheet |
| Proof Inventory | url | Google Sheet |

### 1.3 Project = delivery workspace (one per deal)

- **Task lists:** one per stage (`S00 Commercial Brief` … `S14 Measurement`).
- **In each list:** one **stage task** named per the pack convention, e.g.
  `S03 — Positioning — 3A → 3B + 3C → 3D → 3E`.
  - Assignees: stage owner (+ reviewer).
  - Due date: stage deadline.
  - Description: the stage card (format below).
- **Subtasks of the stage task:**
  - one per Definition of Done item (from `ops/stages.yaml`);
  - a final `✔ Reviewer sign-off — <role>` subtask assigned to the reviewer.
- **Stage 12** has three parent tasks (`QA — Compliance`, `QA — Strategy / UX`,
  `QA — Technical / SEO`). Each has one subtask per check in `qa/*.md` and a `Gate sign-off` subtask.

### 1.4 Custom object: "Approval Record"

| Field | Type |
|---|---|
| Project | text (deal title) or url (deal link) |
| Stage | select 00–14 |
| Decision | text, e.g. "Positioning thesis" |
| Status | select: **Pending / Approved / Changes Requested / Locked / N/A** |
| Decision level | select: 1 Business strategy · 2 Positioning · 3 UX/IA · 4 Content/proof · 5 Visual |
| Approver | contact_link (client) or text (internal) |
| Decision date | date |
| Feedback | text |
| Locked | checkbox |
| Evidence link | url (meeting notes / email / signed document) |

Rule (from 9A): **never infer approval from silence.** Status changes only with an evidence link.

### 1.5 Google Sheets (in the project Drive folder, linked from the deal)

- **Input Tracker** (Template 13 columns)
- **Proof Inventory** (Template 09 columns)
- **QA Issue Log** (one tab per gate, 12A/12B/12C columns)

---

## 2. What a team member sees: the stage task

The stage task description is generated from `dist/stage-config.json` (per release), so it always
matches GitHub. Example for Stage 03:

```
STAGE 03 — POSITIONING
Status: In Progress        Owner: Sarah (Strategist)        Reviewer: Project Lead        Due: 14 Oct

OBJECTIVE
Define the market perception, brand architecture and strategic ideas the new website must make obvious.

INPUTS
• Master Project Context → [open]           (deal field)
• Project Strategy Brief → [open]  • Evidence Pack → [open]  • Strategic Diagnosis → [open]

RUN
• 3A Generate Positioning Directions → [open]
• 3B Select and Sharpen Positioning → [open]
• 3C Brand Architecture → [open]
• 3E Client-Facing Positioning Explanation → [open]   (client-facing)

VALIDATE
• 3D Positioning Validator → [open]

OUTPUT
Positioning Thesis + Brand Architecture → Template 04 [open]  → save to Drive: 04_Positioning/

DEFINITION OF DONE        (ticked as subtasks below)
☐ Three-second perception
☐ Wrong perception
☐ Positioning thesis (25 words or fewer)
☐ Priority services
☐ Brand architecture
☐ 3D validator returns PASS on every test
☐ Client strategic approval recorded
☐ Positioning added to LOCKED DECISIONS in the Master Project Context
☐ Reviewer sign-off

APPROVAL
Required: client strategic approval → create/update Approval Record "Positioning"
On approval, lock: Positioning

HANDOFFS
• H02 Strategist → SEO Lead → [open]   • H03 Strategist → Designer → [open]

NEXT
Stage 04 — IA + SEO

Stage card → [open]   SOP → [open]   OS version: v1.0
```

Every `[open]` is a deep link (GitHub blob URL with heading anchor, or Drive URL). ⚑ V4 confirms
links are clickable; if not, the same block goes in the project notebook, which accepts HTML.

## 3. Moving stage: the human gate

1. The owner ticks the DoD subtasks and runs the validator. **Paste the PASS/FAIL/BLOCKED result into
   the stage task as a comment** (or as a file link, if comments are unavailable: ⚑ V3).
2. For client-gated stages, the Approval Record is set to **Approved** (with an evidence link).
3. The reviewer ticks `✔ Reviewer sign-off`.
4. **The Project Lead moves the deal to the next pipeline stage.** This is the "stage complete" event.
5. Automation (see [automation map](automation-map.md)) creates a "Confirm DoD — Stage NN" check
   task if any DoD subtask is still open, and opens the next stage task.

Moving a deal while DoD items are open is allowed only with an **authorised exception**: a comment
on the stage task saying who authorised it, why, and which items remain. This matches the pack:
"Do not move stage until PASS or an authorised exception is recorded."

## 4. Operational dashboard

| Need | View in Chirply |
|---|---|
| Active redesign projects, current stage, owner, target launch | Pipeline board "Website Redesign"; saved report over deals (stage × owner) |
| Blocked projects | Deals filtered on Health = Blocked |
| Upcoming approvals | Approval Record list, Status = Pending, sorted by date; deal field `Next approval due` |
| Missing inputs | Weekly digest (reads the Input Tracker sheets) |
| QA status | Stage 12 parent tasks per project; weekly digest |
| Overdue items | **Weekly digest**, because Chirply's report builder has no task dataset |

The **weekly digest** is a single email/Chirply note every Monday at 08:00. It is built by Apps Script
(or by Claude via the Chirply connector) from deals, project tasks and the tracker sheets. It answers
the Quickstart's five Monday-morning questions for every project.

## 5. Repeatable set-up for a new client

1. Create the deal from the **deal template** "Website Redesign" (prefills pipeline, stage 00 and fields).
2. Run provisioning ([automation map](automation-map.md), A1). It creates the project, 15 task lists,
   stage tasks with descriptions, DoD subtasks and reviewer subtasks from the current release's
   `stage-config.json`, and copies the Drive folder template.
3. Until provisioning is automated (Phase 5), build one **reference project by hand** in Phase 3 and
   use it as the pattern.
