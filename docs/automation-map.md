# Automation map

**Automate the administration around strategy, never strategic judgement.**

Nothing here runs on day one. Each automation is built only after the manual version has run
cleanly on the pilot project (implementation plan, step F). Glue code runs in **Google Apps Script**
(part of the existing Google Workspace), so no Zapier/Make/n8n subscription is needed.

Evidence tags refer to the [Chirply audit](chirply-audit.md).

## Building blocks

| Block | System | Evidence |
|---|---|---|
| Deal template → **project from template** (`project_template_id`) | Chirply (native, no workflow) | OBSERVED-catalogue 2026-10-04 |
| `deal_stage_changed` trigger (filter: pipeline, stage) | Chirply workflow | OBSERVED-live |
| `custom_record_updated` trigger (filter: field, value) | Chirply workflow | OBSERVED-live (V6 fired) |
| **`project_task_completed`, `project_subtask_completed`, `project_task_moved`** triggers (filters: project, column, task list; run without a contact) | Chirply workflow | OBSERVED-catalogue 2026-10-04 |
| **`create_project_task`** (list, column, assignees, `due_in_days`, parent) and **`update_project_task`** (target by trigger task or title; status; column; assignees) | Chirply workflow | OBSERVED-catalogue 2026-10-04 |
| `create_task` (CRM task, `due_in_days`, assignee, reviewer) | Chirply workflow | OBSERVED-live |
| `move_pipeline_stage`, `update_custom_record`, `send_email` | Chirply workflow | OBSERVED-live |
| `webhook` action → Apps Script / Chirply REST API | Chirply workflow | Feasible; needs an API key (V7) |
| Time-driven triggers, Drive/Sheets/Gmail APIs | Apps Script | Standard Google Workspace |
| Release payload `stage-config.json` (DoD, links, roles per stage) | GitHub Release | This repo |

**Chirply limits that still shape the design** (re-checked 2026-10-04):
- no "project task created" trigger;
- workflow actions can't set a task's reviewer, tags or comments;
- no "date field reached" or "deal field changed" trigger;
- no tasks/projects dataset in reports;
- no native internal notification (use `send_email`);
- no native Drive or Slack integration;
- `appDev` is off.

Project-task triggers filter by a **specific** project, column or list. A workflow that serves every
redesign project therefore runs unfiltered and branches on the trigger task's title prefix
(`S03 — …`) with a `switch`. This is INFERRED; confirm it on the pilot.

**Loop risk:** `update_project_task` can start other project-task workflows. Every workflow below
targets a *different* task than the one that triggered it, and none re-triggers its own trigger.

Since 2026-10-04, **native workflows cover A2, A3, A5 and A6 without Apps Script or an API key.**
Apps Script is still needed for Drive (part of A1), for the Tracker Sheet (A4) and for anything that
needs reporting (A7, A8).

**The deal stage move is still the business-level "stage complete" event.** A human makes it after
the reviewer approves the stage task.

## Automations

### A1 — New redesign project → provision

| | |
|---|---|
| **Trigger** | Deal created from the deal template "Website Redesign" |
| **Action** | **Native:** Chirply creates the project from the "Website Redesign" project template, linked to the deal, starting today. It brings the status columns, tags, 15 lists, stage tasks with links, DoD subtasks, QA gate tasks and reviewers (verify which of these the template keeps on first use). **Remaining Apps Script (or manual):** copy the Drive folder template (`00_Admin` … `14_Measurement`, Project Tracker Sheet, MPC Doc) and write the Drive URLs to the deal fields |
| **System** | Chirply (native) + Apps Script for Drive |
| **Owner** | Operations / OS maintainer |
| **Failure condition** | Deal created without the deal template, so there's no project. `projects_for_deal` returns nothing; create the project from the template by hand (`projects_create_from_template` with `deal_id`) |
| **Human override** | The Project Lead adjusts assignees and reviewers to the actual team |

### A2 — Stage approved → open next stage

| | |
|---|---|
| **Trigger** | `project_task_completed` where the task title starts `S` + stage number (i.e. the reviewer approved the stage task) |
| **Action** | `switch` on the stage number → `update_project_task` targeting the **next** stage task by title: column **In Progress**. Then `create_task` (CRM, linked to the deal) for the Project Lead: "Stage NN approved: move the deal to NN+1". If `project_subtask_completed` shows DoD subtasks still open, the Project Lead sees them on the task; a formal open-items check is an optional Apps Script extra |
| **System** | Chirply workflow (native) |
| **Owner** | Project Lead |
| **Failure condition** | Title convention broken, so the switch finds no match; the workflow ends and the Project Lead opens the next stage by hand |
| **Human override** | Return the review (`projects_return_review`) or move the task back. Moving the deal stays human |

### A3 — Client approval recorded → lock and open next workstream

| | |
|---|---|
| **Trigger** | `custom_record_updated` on Approval Record where Status → Approved |
| **Action** | `create_project_task` in the current stage list for the Strategist: "Add <Decision> to LOCKED DECISIONS in the MPC" (due 1 day). `update_project_task` ticks the "approval recorded" DoD subtask (target by title). For Stage 9 sign-off: `update_project_task` moves the S10 stage task to **In Progress** (the standard input items live in the Tracker *Content Inputs* tab) |
| **System** | Chirply workflow (native) |
| **Owner** | Project Lead |
| **Failure condition** | Approval recorded without an evidence link (branch on empty `Evidence link` → create a "missing approval evidence" task instead) |
| **Human override** | Set Status back to Pending. The lock wording in the MPC is always written by a human |

> **Not automated:** writing the LOCKED wording into the MPC, and moving the deal to the next stage.
> Both are human acts.

### A4 — Missing input overdue → reminder

| | |
|---|---|
| **Trigger** | Apps Script, daily at 08:00, over every active project's Tracker *Content Inputs* tab |
| **Action** | Rows with Status = Requested and Due Date < today: one **internal** email per owner listing overdue items by project. For P0/blocking items: create a Chirply task "Chase client: <items>" linked to the deal, with prompt **10B** in the description |
| **System** | Apps Script → Gmail / Chirply API |
| **Owner** | Project Lead |
| **Failure condition** | Sheet structure changed (missing columns). The script reports the bad sheet instead of skipping it silently |
| **Human override** | Client-facing chasers are **drafted (10B) and sent by a human** from the Chirply inbox. Automatic client reminders are optional later, per project, using Chirply sequences |

### A5 — Build approved → open QA gates

| | |
|---|---|
| **Trigger** | `project_task_completed` on the S11 Build stage task |
| **Action** | The three QA gate tasks already exist (from the template). `update_project_task` × 3 moves Compliance, Strategy / UX and Technical / SEO to **In Progress**, so their owners and reviewers see them. The 29 checks are in the Tracker *QA* tab |
| **System** | Chirply workflow (native) |
| **Owner** | Project Lead |
| **Failure condition** | Gate owners not set on the tasks → the Project Lead assigns them |
| **Human override** | A gate can be tagged N/A only with a Project Lead comment |

### A6 — Launch → baseline and 30/60/90 reviews

| | |
|---|---|
| **Trigger** | `project_task_completed` on the S13 Launch stage task (or `deal_stage_changed` → `13 Launch` on launch day) |
| **Action** | `create_project_task` × 4 in the S14 list: "13D Capture measurement baseline" (due 0 days), "14A 30-day review" (`due_in_days` 30), "14B 60-day review" (60), "14C 90-day review" (90), each assigned to the Strategist |
| **System** | Chirply workflow (native) |
| **Owner** | Strategist |
| **Failure condition** | Triggered before the actual launch date, so the dates drift |
| **Human override** | Edit the due dates. If launch slips, the Project Lead re-dates the three review tasks |

### A7 — Stage due date approaching

| | |
|---|---|
| **Trigger** | Apps Script, daily, over open stage tasks via API |
| **Action** | Stage task due within 2 days with DoD < 100% → email owner and reviewer. Overdue → included in the weekly digest and the deal Health suggestion |
| **System** | Apps Script → Chirply API / Gmail |
| **Owner** | Project Lead |
| **Failure condition** | API rate limits / auth expiry → the script emails the maintainer |
| **Human override** | None needed (informational) |

### A8 — Weekly operations digest (closes the dashboard gap)

| | |
|---|---|
| **Trigger** | Apps Script, Mondays 07:30 |
| **Action** | One email to the team: per active project, the stage, owner, target launch, Health/blocker, overdue stage tasks, open DoD items, pending approvals, plus the Tracker *Dashboard* KPIs (stages complete, open inputs, QA fixes open) |
| **System** | Apps Script → Chirply API + Sheets → Gmail |
| **Owner** | Project Lead (as reader); OS maintainer (as script owner) |
| **Failure condition** | Script error → the digest isn't sent, and the maintainer gets an alert |
| **Human override** | n/a |

### A9 — OS release → new projects use the new version

| | |
|---|---|
| **Trigger** | GitHub Release published (`v*`) |
| **Action** | `release.yml` attaches `stage-config.json`. A1 always fetches the **latest release** asset. Running projects keep the version they started on (`OS version` field) unless the Project Lead chooses to migrate |
| **System** | GitHub Actions |
| **Owner** | OS maintainer |
| **Failure condition** | Release without the asset → A1 falls back to the previous release and alerts |
| **Human override** | Pin a version in A1's script properties |

## Explicitly not automated

From the AI Workflow Pack Deployment Guide, and kept here:
positioning approval · regulated claims · practitioner credentials · URL removals/migrations ·
ambiguous feedback classification · launch GO/NO-GO · commercial conclusions from post-launch data ·
moving a deal to the next stage · writing LOCKED decisions.
