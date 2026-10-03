# Automation map

**Automate the administration around strategy, never strategic judgement.**

Nothing here runs on day one. Each automation is built only after the manual version has run
cleanly on the pilot project (implementation plan, step F). Glue code runs in **Google Apps Script**
(part of the existing Google Workspace), so no Zapier/Make/n8n subscription is needed.

Evidence tags refer to the [Chirply audit](chirply-audit.md).

## Building blocks

| Block | System | Evidence |
|---|---|---|
| `deal_stage_changed` trigger (filter: pipeline, stage) | Chirply workflow | OBSERVED-live |
| `custom_record_updated` trigger (filter: field, value) | Chirply workflow | OBSERVED-live |
| `create_task` (with `due_in_days`, assignee) | Chirply workflow | OBSERVED-live |
| `move_pipeline_stage`, `update_custom_record`, `send_email` | Chirply workflow | OBSERVED-live |
| `webhook` action (any HTTPS call with auth) | Chirply workflow → Apps Script / Chirply REST API | OBSERVED-live; end-to-end INFERRED (V7) |
| Chirply REST API (`projects_create`, `projects_save_task`, …) | Apps Script | OBSERVED-catalogue |
| Time-driven triggers, Drive/Sheets/Gmail APIs | Apps Script | Standard Google Workspace |
| Release payload `stage-config.json` (DoD, links, roles per stage) | GitHub Release | This repo |

**Known Chirply limits that shape the design:** no triggers on project tasks; no "date field
reached" or "deal field changed" trigger; no native internal notification (use email); no native
Drive or Slack integration.

**The deal stage move is the single "stage complete" event.** A human makes it after the DoD gate.
Everything else reacts to it.

## Automations

### A1 — New redesign project → provision

| | |
|---|---|
| **Trigger** | Deal created in the "Website Redesign" pipeline (from the deal template) |
| **Action** | Chirply `webhook` → Apps Script: (1) create the Chirply project with 15 task lists, stage tasks (description = stage card + links), DoD subtasks and reviewer subtasks from the **current release's** `stage-config.json`; (2) assign owners from the deal's role fields, per the SOP owner of each stage; (3) copy the Drive folder template (`00_Admin` … `14_Measurement`, plus the Project Tracker Sheet from Operational Tracker v1.0 and the MPC Doc); (4) write the Drive URLs back to the deal fields; (5) set `OS version` |
| **System** | Chirply → Apps Script → Chirply REST API + Drive API |
| **Owner** | Operations / OS maintainer |
| **Failure condition** | Webhook fails or the script errors part-way. The script is idempotent (it checks for an existing project linked to the deal) and emails the Project Lead the error |
| **Human override** | Project Lead can re-run from the deal ("manual" workflow trigger), or create the project by hand from the reference project |

### A2 — Stage complete → flag gate and open next stage

| | |
|---|---|
| **Trigger** | `deal_stage_changed` (pipeline = Website Redesign) |
| **Action** | Apps Script reads the previous stage's DoD subtasks. **If any are open**, it creates a task "Confirm DoD — Stage NN moved with N open items" for the Project Lead, due today, and emails them. It then sets the new stage task to *In progress*, emails its owner (stage card link, due date), and updates `Current stage` in the MPC (marked "auto"; this is the only automated MPC write, and it's a status, not strategy) |
| **System** | Chirply → Apps Script |
| **Owner** | Project Lead |
| **Failure condition** | Deal moved by mistake / backwards |
| **Human override** | Move the deal back. The check task stays as an audit trail. An authorised exception is a comment on the stage task |

### A3 — Client approval recorded → lock and open next workstream

| | |
|---|---|
| **Trigger** | `custom_record_updated` on Approval Record where Status → Approved (and Locked = true) |
| **Action** | Create a task for the Strategist: "Add <Decision> to LOCKED DECISIONS in the MPC" (due 1 day), linking the Approval Record. Tick the "approval recorded" DoD subtask. For Stage 9 sign-off: create the Stage 10 standard input tasks (one per category from Template 13). The Project Lead prunes them to what the project needs (10A) |
| **System** | Chirply workflow (+ Apps Script for subtask updates) |
| **Owner** | Project Lead |
| **Failure condition** | Approval recorded without an evidence link (the workflow branches on an empty `Evidence link` and creates a "missing approval evidence" task instead) |
| **Human override** | Set Status back to Pending. The lock wording in the MPC is always written by a human |

> **Not automated:** writing the LOCKED wording into the MPC, and moving to the next stage. Both
> are human acts.

### A4 — Missing input overdue → reminder

| | |
|---|---|
| **Trigger** | Apps Script, daily at 08:00, over every active project's Tracker *Content Inputs* tab |
| **Action** | Rows with Status = Requested and Due Date < today: one **internal** email per owner listing overdue items by project. For P0/blocking items: create a Chirply task "Chase client: <items>" linked to the deal, with prompt **10B** in the description |
| **System** | Apps Script → Gmail / Chirply API |
| **Owner** | Project Lead |
| **Failure condition** | Sheet structure changed (missing columns). The script reports the bad sheet instead of skipping it silently |
| **Human override** | Client-facing chasers are **drafted (10B) and sent by a human** from the Chirply inbox. Automatic client reminders are optional later, per project, using Chirply sequences |

### A5 — Build complete → create QA gates

| | |
|---|---|
| **Trigger** | `deal_stage_changed` → `12 QA` |
| **Action** | Create the three QA gate tasks: Compliance (Compliance Reviewer), Strategy / UX (Independent QA Reviewer), Technical / SEO (Developer + SEO Lead). Owners come from the deal role fields. Each has a `Gate sign-off` subtask and a link to the Tracker *QA* tab, which already lists the 29 checks as Not Checked. Check-level status is not duplicated in Chirply |
| **System** | Chirply → Apps Script → Chirply API |
| **Owner** | Project Lead |
| **Failure condition** | Gate owner field empty → task assigned to the Project Lead, flagged |
| **Human override** | Gates can be marked N/A only with a comment from the Project Lead |

### A6 — Launch → baseline and 30/60/90 reviews

| | |
|---|---|
| **Trigger** | `deal_stage_changed` → `13 Launch` (moved on launch day) |
| **Action** | `create_task` × 4: "13D Capture measurement baseline" (due 0 days), "14A 30-day review" (`due_in_days` 30), "14B 60-day review" (60), "14C 90-day review" (90), each with the stage card link |
| **System** | Chirply workflow (native) |
| **Owner** | Strategist |
| **Failure condition** | Deal moved to 13 before the actual launch date, so the dates drift |
| **Human override** | Edit the due dates. If the launch slips, the Project Lead re-dates the three review tasks |

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
