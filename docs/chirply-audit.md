# Chirply capability audit

**Question:** can Chirply, which CosmediSites already uses, be the operational front end for the
Website OS, so that we avoid adding ClickUp or Notion?

**Date:** 2026-10-03 · **Method:** read-only inspection through Chirply's built-in MCP server.
That covers the live action catalogue (2,418 actions), live trigger/action registries, a few
read-only data calls, and Chirply's in-app knowledge base. Nothing was created, changed or sent.

---

## ⚠️ Evidence caveat: read this first

The Chirply connection available during the audit is authenticated to a workspace called
**"FM Recruitment & Provision"**. It is **not the CosmediSites workspace**, and CosmediSites is not
a client account under it (`list_accounts` returned none).

What this means:

- Findings describe **what the Chirply product can do**: its full action catalogue and the
  automation trigger/action registries, read live. They do **not** describe how the CosmediSites
  workspace is configured, or which features its plan enables.
- That workspace is on plan `scale`. It has `customObjects`, `customFields`, `pipelines`,
  `workflows`, `webhooks`, `restApi`, `forms`, `reportBuilder` and `inbox` **on**, and `appDev`
  (build your own apps) **off**: "the App Marketplace is switched off for this account by the
  agency that manages it". **The CosmediSites plan may differ.**
- Phase 2 of the [implementation plan](implementation-plan.md) therefore includes a short
  hands-on verification in the real CosmediSites workspace (tests V1–V9 below). The
  recommendation is conditional on those tests.

### Evidence labels

| Label | Meaning |
|---|---|
| **OBSERVED-live** | Seen in live data or a live registry read (trigger/action types, field definitions, report datasets) |
| **OBSERVED-catalogue** | The action exists in the live catalogue with a schema we read, but it was not exercised |
| **DOCUMENTED** | Chirply's own knowledge base / handbook (in-app articles `pipeline`, `tasks`, `navigation-projects`) |
| **INFERRED** | Likely possible by combining observed features; not proven |
| **MISSING** | Not found after targeted searching (search terms are listed at the end) |

---

## What Chirply is, in shape

Chirply is a broad CRM/marketing platform (142 feature domains). The parts relevant to us:

- **Deals + pipelines:** kanban stages you define, deal custom fields (text, textarea, number,
  date, select, multiselect, boolean, url; can be required), one owner per deal, deal templates.
- **Projects module:** separate from deals. Projects contain task lists, tasks with **subtasks**
  (`parent_id`), **multiple assignees**, start/due dates, priority, a board stage, long
  descriptions (up to 200k characters), file uploads, HTML notebooks and a per-project dashboard.
  The board columns are To do / In progress / Done.
- **Custom objects:** user-defined record types with text, number, date, select, checkbox, url,
  phone, email and `contact_link` fields. They can trigger automations on create/update.
- **Automation engine:** 86 triggers, and actions including create task, move pipeline stage,
  update custom record, send email/SMS/WhatsApp, Google Sheets, **outbound HTTP webhook**, branch
  and wait. Workflows are **contact/deal-centric**.
- **Comms:** unified two-way inbox, Gmail, templates, sequences, forms with file upload, booking
  with calendar sync, e-signature documents.
- **API:** REST (`POST /api/v1/actions/<domain>.<action>` for every action), API keys, signed
  outbound webhooks with retries, inbound workflow webhooks, Zapier.

Its strengths are the record, client communication and automation. Its weaknesses are the
structured-delivery features project tools specialise in: checklists, dependencies, gates, a
reviewer role, and task-level reporting.

---

## Requirement-by-requirement findings

### A. Project record

| Need | Finding | Evidence |
|---|---|---|
| One record per project | A **deal** in a "Website Redesign" pipeline, linked to the client company/contact | OBSERVED-catalogue (`deals_create`, `deals_link`) |
| Client, domain, target launch, Drive/Figma/GitHub links, commercial objective, priority services, status | Deal custom fields: text, url, date, select, multiselect, textarea | OBSERVED-live (12 deal custom fields exist in the audited workspace, including date/url/select) |
| Project Lead | Deal `owner_id` (a real user) | OBSERVED-catalogue |
| Strategist, Designer, Developer | **No user-type custom field.** They must be select fields listing team names, or assignees on the project tasks | MISSING (user field) → select-field workaround INFERRED |
| Project Strategy Brief, Master Project Context | URL fields pointing to the Google Docs in Drive (the documents stay in Drive) | OBSERVED-catalogue |

**Rating: AMBER.** Good enough with configuration. Team roles are labels, not user links, so you
can't filter "all projects where I'm the designer" natively.

### B. Stage workflow

| Need | Finding | Evidence |
|---|---|---|
| Create the 15 stages | A pipeline with stages 00–14 as columns; value tracking can be off ("process board") | DOCUMENTED (`pipeline` article) + OBSERVED-catalogue (`stages_create`, `pipelines_set_value_tracking`) |
| Display progress | The pipeline board shows every project's current stage. A project's task lists show per-stage progress | OBSERVED-catalogue / DOCUMENTED |
| Assign owners per stage | One project task per stage, with assignees | OBSERVED-catalogue (`projects_save_task.assignees[]`) |
| Assign reviewers | **No reviewer field.** Workaround: a "Reviewer sign-off" subtask assigned to the reviewer | MISSING → INFERRED workaround |
| Due dates per stage | `due_date` on each stage task | OBSERVED-catalogue |
| Dependencies | None on either task system | MISSING |
| Prevent progression before DoD | Cards move freely; no entry criteria on stages | MISSING |
| Flag progression | An automation on `deal_stage_changed` can create a "confirm DoD" check task | INFERRED (trigger and action OBSERVED-live) |
| Repeatable project template | Deal templates prefill fields only; no "duplicate project with tasks" action found | OBSERVED-catalogue / MISSING |
| Duplicate workflow for new clients | Scripted provisioning via REST API (`projects_create`, `projects_save_task`) from `dist/stage-config.json` | INFERRED (API OBSERVED-catalogue) |

**Rating: AMBER.** Stages, owners and dates work. Gating and dependencies don't exist, so the
gate is a human rule plus an automated flag. Duplicating a project needs a script.

### C. Definition of Done / checklists

No checklist object exists. Subtasks under each stage task (`parent_id`) can carry one DoD item each,
with open/completed status. Owner, inputs, output, template and prompts go in the stage task
description as links to the GitHub stage card.

**Rating: AMBER.** Workable, but a subtask is heavier than a tick-box. Check in the UI how
subtasks render (V2).

### D. Task assignment

| Need | CRM tasks | Project tasks |
|---|---|---|
| Named owner | ✅ `assignee_id` (single) | ✅ `assignees[]` (multiple) |
| Named reviewer | ❌ | ❌ (use a subtask) |
| Due date | ✅ `due_at` | ✅ `due_date`, `start_date` |
| Status | open / done / cancelled | open / completed + board column |
| Comments | ✅ `tasks_comment` | ❓ no API action found. Check in the UI (V3) |
| Attachments / links | ✅ media-library attachments | ✅ `projects_upload_file`; links in description |
| Dependencies | ❌ | ❌ |
| Subtasks / checklists | ❌ | ✅ subtasks |

Evidence: OBSERVED-catalogue. **Rating: AMBER.** Use **project tasks** for delivery work.

### E. Approvals

- No native approval feature for project items. MISSING.
- A **custom object "Approval Record"** can hold: Project (text or link), Decision, Status (select:
  Pending / Approved / Changes Requested / Locked / N/A), Approver (text or `contact_link` for the
  client approver), Date, Feedback (text), Decision level (select 1–5), Locked (checkbox). INFERRED;
  the field kinds are OBSERVED-catalogue.
- `custom_record_updated` can trigger on a field changing to a value (for example Status =
  Approved). OBSERVED-live (trigger registry).
- Formal client sign-off documents can use **e-signature** (`documents_send`, with audit trail).
  OBSERVED-catalogue. That suits a final Stage 9 sign-off or a launch sign-off.

**Rating: AMBER.** Configurable to the standard we need. No native approval UI.

### F. Content / input tracker

Possible as a custom object, but the tracker is a 20–60-row table per project with many columns.
Chirply has native **Google Sheets** triggers (`google_sheets_row_new`, `google_sheets_row_updated`)
and a Sheets action, so a Sheet in the project Drive folder can still drive Chirply automations.
Clients can upload inputs through **Chirply forms** (file question: images, PDF, Word, text, up to
10 MB). OBSERVED-catalogue. Do not use forms for patient imagery or consent records.

**Rating: AMBER, with Google Sheets (existing) as the companion.**

### G. Proof inventory

Custom objects lack formulas, roll-ups and relation fields. The proof inventory is evidence-heavy
and reviewed line by line, which is a spreadsheet job.

**Rating: needs companion → Google Sheets in the project Drive folder** (already in the stack; not a new tool).

### H. QA (three separate gates)

Three parent tasks in a "Stage 12 — QA" list (Compliance, Strategy/UX, Technical/SEO). Each has
one subtask per check, a gate owner, and a final "Gate sign-off" subtask. The detailed issue log
(URL, severity, fix, retest) lives in the QA sheet/doc in Drive. No enforcement. INFERRED from
OBSERVED-catalogue features.

**Rating: AMBER.**

### I. Automation

| Required automation | Possible in Chirply? | Evidence |
|---|---|---|
| Stage 3 approved → mark Positioning locked → open Stage 4 | `custom_record_updated` (Approval Record status → Approved) → create task / `move_pipeline_stage`. Marking the project task done needs an API call via `webhook` | Trigger/actions OBSERVED-live; chaining INFERRED |
| Client strategy review approved → open Production Inputs → create input tasks | Same pattern; a set of `create_task` steps, or a webhook to the provisioning script | INFERRED |
| Build complete → create three QA workstreams | `deal_stage_changed` (to Stage 12) → webhook → create 3 parent tasks + subtasks via API | INFERRED |
| Launch date set → 30/60/90 reviews | **No "date field reached" or "deal field changed" trigger.** Use `deal_stage_changed` (to Stage 13) on launch day → `create_task` with `due_in_days` 30/60/90 (relative to run time) | OBSERVED-live (`due_in_days`); MISSING (date trigger) |
| API | REST API for every action, unlimited API keys on the audited plan | OBSERVED-catalogue |
| Webhooks | Outbound (signed, retries) and inbound per workflow | OBSERVED-catalogue |
| Zapier | Native invite/recipes | OBSERVED-catalogue |
| Make / n8n | No native connector; possible via REST + webhooks | INFERRED |
| Native automations | 86 triggers; branches, waits, switches | OBSERVED-live |
| Email automation | `send_email`, `gmail_send`, sequences | OBSERVED-live |
| Internal notifications | **No team-notification action** (`notify` logs a timeline note). `create_task` says "nobody is notified". Use `send_email` to an internal address, or `webhook` to a Slack incoming webhook | OBSERVED-live / INFERRED |
| Slack | No native Slack integration found | MISSING |
| Google Drive | No native Drive integration found (Sheets and Gmail exist) | MISSING |
| Triggers on project tasks | None found (`task_completed` is CRM/contact tasks) | MISSING |

**Rating: AMBER.** The engine is strong. Because it is deal/contact-centric, project-level
automations need the deal stage as the trigger and the REST API (via `webhook`) as the actuator.

### J. Knowledge links

Deal URL fields hold project links (Drive folder, Figma, Master Project Context, deck). Stage tasks
carry links to the GitHub stage card, SOP, template and prompts in their description; the provisioning
payload (`dist/stage-config.json`) already contains every URL. Project notebooks accept HTML.
OBSERVED-catalogue. Check that description links are clickable in the UI (V4).

**Rating: AMBER, likely GREEN once V4 passes.**

### K. Client communication

Two-way unified inbox with per-contact history, Gmail integration, email/SMS/WhatsApp templates with
merge tokens, sequences, booking with Google/Outlook sync and reminders, forms with file upload,
notes and timeline, and e-signature documents. OBSERVED-catalogue.
**No client portal for project status.** Member sites gate pages; they don't show tasks.

**Rating: GREEN.** This is Chirply's strength. Use it for every client email, input request,
approval request, reminder and meeting note, rather than duplicating comms elsewhere.

### L. Dashboard

| View | Possible? |
|---|---|
| Active redesign projects, current stage, owner (lead), target launch | ✅ Pipeline board; report builder over **deals** by pipeline/stage/owner (OBSERVED-live: datasets are contacts, deals, calls, messages, appointments, revenue) |
| Upcoming approvals | ⚠️ Custom-object list filtered by Status = Pending (INFERRED) |
| Blocked projects | ⚠️ Deal select field "Health: On track / At risk / Blocked" (INFERRED) |
| Missing inputs | ⚠️ From the input Sheets, not Chirply |
| QA status | ⚠️ Per-project dashboard only (`projects_dashboard`) |
| Overdue items across projects | ❌ No tasks/projects dataset in reports; no overdue filter | MISSING |

**Rating: RED for a single native cross-project delivery dashboard. AMBER with a weekly digest**
generated through the API (see [automation map](automation-map.md), A8).

---

## Decision matrix

| Capability | Required? | Chirply native? | Via configuration? | Via API / integration? | Needs companion tool? | Unable to support? | Rating | Evidence / notes |
|---|---|---|---|---|---|---|---|---|
| Project record | Must | Partly (deal) | ✅ custom fields | – | – | Role fields aren't user links | **AMBER** | OBSERVED-live fields |
| 15 stages | Must | ✅ pipeline | – | – | – | – | **GREEN** | DOCUMENTED |
| Progress display | Must | ✅ board | ✅ task lists | – | – | – | **GREEN** | |
| Stage owner + due date | Must | – | ✅ stage tasks | – | – | – | **AMBER** | Project tasks |
| Reviewer | Must | ❌ | ✅ reviewer subtask | – | – | No reviewer field | **AMBER** | Convention |
| Dependencies | Nice | ❌ | – | – | – | ✅ | **RED** | Sequence is implicit in the stage order; acceptable |
| Gate enforcement | Must (flag) | ❌ | – | ✅ flag via automation | – | Hard prevention | **AMBER** | Human gate + automated flag |
| Repeatable template / duplication | Must | Partly | – | ✅ provisioning script | – | – | **AMBER** | Script from `stage-config.json` |
| DoD checklists | Must | ❌ | ✅ subtasks | – | – | – | **AMBER** | Verify UX (V2) |
| Task owner/due/status/attachments | Must | ✅ | – | – | – | – | **GREEN** | |
| Task comments | Should | CRM ✅ / project ❓ | – | – | – | – | **AMBER** | V3 |
| Approvals with statuses | Must | ❌ | ✅ custom object | ✅ triggers | – | – | **AMBER** | |
| Client e-sign approval | Nice | ✅ documents | – | – | – | – | **GREEN** | |
| Content / input tracker | Must | – | Possible | ✅ Sheets triggers | **Google Sheets** (existing) | – | **AMBER** | |
| Proof inventory | Must | – | Weak | – | **Google Sheets** (existing) | – | **AMBER** | |
| Three QA gates | Must | – | ✅ tasks + subtasks | – | Drive issue log | – | **AMBER** | |
| Stage-transition automations | Should | ✅ deal-stage triggers | – | ✅ webhook → API | Apps Script glue (existing Workspace) | Project-task triggers | **AMBER** | |
| Date-relative 30/60/90 | Should | ✅ `due_in_days` | – | – | – | Date-field trigger | **AMBER** | Fire on stage move |
| Internal notifications / Slack | Should | Partly (email) | – | ✅ webhook | – | Native Slack | **AMBER** | |
| Knowledge links | Must | ✅ url fields | ✅ task descriptions | – | – | – | **AMBER→GREEN** | V4 |
| Client comms, reminders, meeting notes | Must | ✅ | – | – | – | – | **GREEN** | Core strength |
| Cross-project ops dashboard | Must | Deals only | ✅ health field | ✅ weekly digest | – | Native task reporting | **RED→AMBER** | Digest closes the gap |
| Custom in-platform app | Optional | – | – | `appDev` off on audited plan | – | Unknown for CosmediSites | **unknown** | V8 |

---

## Verification tests for the CosmediSites workspace (Phase 2)

Run these by hand in the real CosmediSites Chirply workspace (about 60 minutes). Each one either
confirms the design or triggers the fallback.

| # | Test | Pass condition | If it fails |
|---|---|---|---|
| V1 | Plan check: custom fields, custom objects, pipelines, workflows, webhooks, REST API, forms, report builder | All enabled | Ask the managing agency / upgrade, or fallback |
| V2 | Create a project with a task, 5 subtasks, 2 assignees and a due date | Subtasks tick off cleanly; progress visible on the project view | **Fallback trigger** |
| V3 | Comment on a project task, and attach a link and a file | Both possible | Comments go on the deal timeline instead (acceptable) |
| V4 | Paste GitHub/Drive links into a project task description | Links clickable | Put links in deal URL fields and a project notebook |
| V5 | Pipeline with 15 stages + a `deal_stage_changed` workflow that creates a task and sends an internal email | Fires reliably | **Fallback trigger** for automation |
| V6 | Custom object "Approval Record" + `custom_record_updated` trigger on Status | Fires on change | Approvals tracked as deal fields (weaker) |
| V7 | Workflow `webhook` action calling Chirply's own REST API (`projects_save_task`) | Task created | Provisioning runs from Apps Script instead (fine) |
| V8 | Is `appDev` / App Marketplace enabled, and who is the managing agency? | Known | Informational only |
| V9 | Report builder: projects by stage and owner over the redesign pipeline | Works | Digest only |

**Fallback rule:** if **V2 or V5 fails**, Chirply can't run delivery, and we move to Option B
(see [operating architecture](operating-architecture.md#fallback-option-b)).

---

## Recommendation

**Option A: Chirply is the main operational front end, configured as specified in the
[operational stage spec](operational-stage-spec.md). The tabular trackers live in Google Sheets in
the project Drive folder.** No new platform. This is conditional on V2 and V5 passing in the
CosmediSites workspace.

Why not add ClickUp or Notion now:

- Every **must-have** has a Chirply route, native or configured, except a native cross-project
  overdue dashboard, which a weekly API digest covers.
- The things a PM tool would add (dependencies, hard gates, richer checklists) don't justify a second
  delivery system. Even in ClickUp or Notion, the DoD gate is ultimately a human decision. Here it is
  a human decision with an automated flag.
- Chirply already owns the client relationship and communications. A second tool would split
  "where is this project?" across two systems and need syncing.
- Google Sheets and Drive are already in use. Treating them as the companion for tabular
  evidence adds no software.

Full detail: [operating architecture](operating-architecture.md).

---

## Search terms used

Domain browses: projects, tasks, custom_objects, deals, automations, pipelines, proposals,
documents, stages, deal_templates, forms, dashboard, reports, team, developers, knowledge,
snapshots, members, conversations, booking.
Keyword searches: "custom field definitions for deals", "task dependency blocked by another task",
"checklist", "approval approve sign off", "add board stage column to project",
"project template duplicate project", "zapier make n8n integration webhook subscription",
"client portal customer login view their project", "form file upload question",
"email template create save", "company notes timeline add note", "google drive slack".
Knowledge base: articles `tasks`, `navigation-projects`, `pipeline`.
Live reads: `business_get_profile`, `plans_get`, `providers_connected`,
`automations_list_trigger_types`, `automations_list_action_types`, `projects_list`,
`projects_overview`, `pipelines_list`, `custom_objects_list_types`, `contacts_list_fields`,
`automations_list`, `reports_describe_catalog`.
