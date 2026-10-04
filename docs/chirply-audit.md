# Chirply capability audit

**Question:** can Chirply, which CosmediSites already uses, be the operational front end for the
Website OS, so that we avoid adding ClickUp or Notion?

**Date:** 2026-10-03 (updated for Source Pack v1.0) · **Method:** read-only inspection through Chirply's built-in MCP server.
That covers the live action catalogue (2,418 actions), live trigger/action registries, a few
read-only data calls, and Chirply's in-app knowledge base. Nothing was created, changed or sent.

---

## Evidence: two rounds

1. **Desk audit (catalogue level).** Run first through a connection to an unrelated workspace
   ("FM Recruitment & Provision"). It established what the Chirply **product** can do: the full action
   catalogue, plus the automation trigger and action registries read live. The requirement findings
   A–L below come from this round, corrected where round 2 disagreed.
2. **Live verification in the CosmediSites workspace** (2026-10-03). Tests V1–V10 were run against
   the real workspace with clearly labelled `ZZ-TEST Website OS` objects. Nothing was sent to anyone,
   no keys were created and no existing record was changed. Results:
   [Verification results](#verification-results-cosmedisites-workspace). **These results override round 1.**

CosmediSites workspace facts (OBSERVED-live):
- It is a **client sub-account managed by a parent agency**, on plan `scale` ("main clients").
- Custom fields, custom objects, pipelines, workflows, webhooks, REST API, API keys, forms, report
  builder and the MCP server are **on**. `appDev` (build your own apps) and the App Marketplace are
  **off**, set by the agency.
- Current state: 2 team members, 2 pipelines, 1 project, 7 deal templates, and 8 workflows (1 active).
  Stripe and Resend are connected.

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
- A **custom object "Approval Record"** can mirror the Operational Tracker's *Approvals* tab
  column for column: Decision, Level, Owner, Status (select: Pending / Approved / Changes
  Requested / Locked / N/A, the Tracker's list), Date, Client / Approver (`contact_link` or text),
  Feedback Classification (select: Strategic / Accuracy / User / UX / Compliance / Preference /
  New Information, the Tracker's list), Notes. Add Project, Locked (checkbox) and Evidence link.
  INFERRED; the field kinds are OBSERVED-catalogue.
- `custom_record_updated` can trigger on a field changing to a value (for example Status =
  Approved). OBSERVED-live (trigger registry).
- Formal client sign-off documents can use **e-signature** (`documents_send`, with audit trail).
  OBSERVED-catalogue. That suits a final Stage 9 sign-off or a launch sign-off.

**Rating: AMBER.** Configurable to the standard we need. No native approval UI.

### F. Content / input tracker

The methodology already provides this as the **Content Inputs** tab of the Operational Tracker v1.0.
It has 9 columns, the status list Not Requested / Requested / Received / Verified / N/A, and 12 seeded
rows (see [templates/operational-tracker.md](../templates/operational-tracker.md)).

Rebuilding it in Chirply is possible as a custom object, but the tracker is a 20–60-row table per project with many columns.
Chirply has native **Google Sheets** triggers (`google_sheets_row_new`, `google_sheets_row_updated`)
and a Sheets action, so a Sheet in the project Drive folder can still drive Chirply automations.
Clients can upload inputs through **Chirply forms** (file question: images, PDF, Word, text, up to
10 MB). OBSERVED-catalogue. Do not use forms for patient imagery or consent records.

**Rating: AMBER, with Google Sheets (existing) as the companion.**

### G. Proof inventory

Custom objects lack formulas, roll-ups and relation fields. The proof inventory is evidence-heavy
and reviewed line by line, which is a spreadsheet job. The Operational Tracker already has a
**Proof Inventory** tab with exactly the required columns and validated drop-downs (Type, Applies
To, Verified?, Consent / Permission).

**Rating: needs companion → Google Sheets in the project Drive folder** (already in the stack; not a new tool).

### H. QA (three separate gates)

The check level (29 checks across the three gates, with Not Checked / Pass / Fix / N/A) already exists
as the Tracker's **QA** tab, with columns Gate, Check, Owner, Status, Issue / Fix, Sign-off / Date.
Chirply only needs the **gate level**: three parent tasks in "Stage 12 — QA" (Compliance, Strategy/UX,
Technical/SEO). Each has its SOP owner (Compliance Reviewer; Independent QA Reviewer; Developer + SEO
Lead) and a "Gate sign-off" subtask, and links to the QA tab. This keeps each check in one place.
No enforcement. INFERRED from OBSERVED-catalogue features.

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
| Project record | Must | Partly (deal) | ✅ custom fields incl. team-member type | – | – | – | **GREEN** | User fields shipped 2026-10-04 |
| 15 stages | Must | ✅ pipeline | – | – | – | – | **GREEN** | DOCUMENTED |
| Progress display | Must | ✅ pipeline board | ✅ project dashboard counts | – | – | % per stage task | **GREEN** | V2: open/completed counts per project and assignee |
| Stage owner + due date | Must | ✅ project stage tasks | – | – | – | Assignees must be project members | **GREEN** | V2 verified |
| Reviewer | Must | ✅ native reviewer + request/approve review | – | – | – | One reviewer per task | **GREEN** | Shipped 2026-10-04 |
| Dependencies | Nice | ❌ | – | – | – | ✅ | **RED** | Sequence is implicit in the stage order; acceptable |
| Gate enforcement | Must (flag) | ❌ | – | ✅ flag via automation | – | Hard prevention | **AMBER** | Human gate + automated flag |
| Repeatable template / duplication | Must | ✅ project templates; deal template auto-creates the project | – | – | – | – | **GREEN** | Shipped 2026-10-04; verify what the template copies |
| DoD checklists | Must | ❌ | ✅ subtasks | – | – | Checklist object | **AMBER** | V2 verified: subtasks tick off and are counted |
| Task owner/due/status | Must | ✅ custom board columns + tags | – | – | – | – | **GREEN** | Columns = Tracker stage statuses (shipped 2026-10-04) |
| Task attachments | Should | ✅ task files (images/PDF/AV) + task links | – | – | Drive (existing) | Docs/zips as task files | **GREEN** | Links to Drive are the norm |
| Task comments | Should | ✅ project task comments | – | – | – | – | **GREEN** | Shipped 2026-10-04; validator results go here |
| Approvals with statuses | Must | ❌ | ✅ custom object (Tracker *Approvals* columns) | ✅ triggers | – | – | **GREEN** | V6 verified: status change → automation in about 12 seconds |
| Client e-sign approval | Nice | ✅ documents | – | – | – | – | **GREEN** | |
| Content / input tracker | Must | – | Possible | ✅ Sheets triggers | **Tracker *Content Inputs* tab (Google Sheets)** | – | **AMBER** | Already part of the methodology |
| Proof inventory | Must | – | Weak | – | **Tracker *Proof Inventory* tab** | – | **AMBER** | Already part of the methodology |
| Three QA gates | Must | – | ✅ gate tasks + sign-off | – | **Tracker *QA* tab** (check level) | – | **AMBER** | One home per check |
| Stage-transition automations | Should | ✅ project-task triggers + create/update project task | – | – | Apps Script for Drive/Sheets only | Task-created trigger; reviewer/tags via workflow | **GREEN** | Shipped 2026-10-04; V5 firing still to confirm |
| Date-relative 30/60/90 | Should | ✅ `due_in_days` | – | – | – | Date-field trigger | **AMBER** | Fire on stage move |
| Internal notifications / Slack | Should | Partly (email) | – | ✅ webhook | – | Native Slack | **AMBER** | |
| Knowledge links | Must | ✅ task links + url fields | – | – | – | Rich text in descriptions | **GREEN** | `projects_add_task_link` |
| Client comms, reminders, meeting notes | Must | ✅ | – | – | – | – | **GREEN** | Core strength |
| Cross-project ops dashboard | Must | Deals only, one dimension per report | ✅ health field | ✅ weekly digest | – | Native task reporting (V9) | **AMBER** | Digest closes the gap |
| Custom in-platform app | Optional | – | – | – | – | `appDev` off by agency override | **RED** | V8. Not needed for Option A |

---

## Verification results (CosmediSites workspace)

Run 2026-10-03 in the live CosmediSites workspace. All evidence is OBSERVED-live unless stated otherwise.

| # | Test | Result | What we learned |
|---|---|---|---|
| V1 | Plan features | **PASS** | All required features are on |
| V2 | Project task with 5 subtasks, assignees, due date | **PASS (with caveats)** | Subtasks tick off and keep `completed_at`. `projects_dashboard` reports open/completed counts per project and per assignee. There is no % per parent task (it can be computed). **Only project members can be assigned.** Adding a member gives them Projects access, which the team needs anyway |
| V3 | Comment + attachment on a project task | **FAIL (comments) / PARTIAL (files)** | **Project tasks can't be commented on.** `tasks_comment` works only for CRM tasks. File upload accepts images, PDF, audio and video only, and attaches to the **project**, not the task |
| V4 | Links in task description / notebook | **PARTIAL** | Task descriptions are stored as **plain text**: markdown/HTML links won't render. Whether a bare URL is auto-linked is to be checked in the UI. Project notebooks store HTML with `<a href>` intact, so links are INFERRED clickable |
| V5 | 15-stage pipeline + stage-change workflow | **PARTIAL** | Pipeline with stages `00 Brief`…`14 Measurement` and value tracking off: **built fine**. The `deal_stage_changed` workflow scoped to that pipeline: **saved and activated fine**. **Firing not yet observed**, because creating a test deal was declined at the permission prompt. Confirm it with the pilot's first real deal |
| V6 | Approval Record custom object + status-change workflow | **PASS** | Object with all 7 fields created. `custom_record_updated` (Status → Approved) **fired within about 12 seconds** and created the task. No contact was needed |
| V7 | Workflow webhook → Chirply REST API | **NOT TESTABLE** | The webhook action supports POST + bearer auth + JSON body with merge fields, and the REST pattern is `POST /api/v1/actions/<name>`. Feasible on paper, but **it needs an API key created by a human**. Not attempted |
| V8 | appDev / managing agency | **OFF / agency-managed** | `appDev` is off by agency override. Custom in-platform apps are not available unless the agency enables them |
| V9 | Report builder | **PARTIAL** | `reports_run` works on deals, but with **one dimension per report** (stage *or* owner, not both). **No tasks/projects dataset** |
| V10 | Rename project board columns to Tracker statuses | **FAIL (API)** | Projects are fixed at To do / In progress / Done. No API to add or rename columns (UI to be checked). **Project tasks have no tags** |

Other confirmed facts:
- **No user/team-member field type**, on deals or custom objects.
- **Workflows can't create or act on project tasks.** The `create_task` action creates **CRM tasks**,
  and there are **no project-task triggers**. Project-task automation needs the REST API (V7).
- **No project template or duplicate action**, and no API delete for projects or custom object types.
- Project **chats** exist and could stand in for task comments (untested).

### What this changes in the design

| Gap | Design response |
|---|---|
| No comments on project tasks (V3) | Validator results, review notes and decisions are logged as **notes on the deal timeline** (`S03 — 3D validator: PASS — …`). Each stage's notebook holds longer notes |
| Plain-text task descriptions (V4) | Stage task descriptions use **bare URLs**, one per line. The full linked stage card goes in a **project notebook** (HTML) |
| Fixed board columns, no tags (V10) | Stage status = **deal pipeline stage** (current stage) + project task open/complete + the `✔ Reviewer sign-off` subtask (= Ready for Review → Complete) + deal **Health** field (Blocked). The board's To do / In progress / Done columns are used as-is |
| Files attach to the project, not the task (V3) | Files live in **Drive** (as designed). Tasks link to them |
| Only project members can be assigned (V2) | Add the project team as members when the project is set up |
| No project template/duplicate | Phase-1 set-up is **by hand** from the stage cards. The reference project is the pattern. Automated provisioning needs the REST API (V7) |
| Workflows create CRM tasks, not project tasks | Automations create **CRM tasks linked to the deal** for admin actions (check DoD, add a lock to the MPC, 30/60/90 reviews). Stage work stays in project tasks |
| One-dimension reports, no task dataset (V9) | Pipeline board for stage × project; the **weekly digest** for owner, overdue and inputs |

### Still to confirm (no extra risk; do during pilot set-up)

1. **V5 firing:** when the pilot deal is moved from `00` to `01`, check that the create-task workflow ran.
2. **V7:** create an API key in the UI (admin) and try one `projects.save_task` call. This is only
   needed when automating provisioning.
3. **UI checks:** whether bare URLs in task descriptions are clickable; whether the project board
   columns can be renamed in the UI; whether project chats work as task discussion.
4. **Clean-up:** delete the leftover test project **"ZZ-TEST Website OS Project"** and the custom
   object type **"ZZ-TEST Approval Records"** in the UI (the API has no delete for these).

## Platform update (2026-10-04)

After the feature requests went in, Chirply shipped most of the gaps. This was re-checked read-only
in the CosmediSites workspace on 2026-10-04 (OBSERVED-catalogue: the actions exist with the schemas
quoted; they have not been exercised yet).

| Gap (2026-10-03) | Now | What shipped |
|---|---|---|
| No comments on project tasks (V3) | **Shipped** | `projects_add_comment` / `projects_list_task_comments` / edit / delete. Notifies assignees and reviewer (in-account only) |
| Files attach to the project only (V3) | **Mostly** | `projects_attach_task_file` (task-level, 10 MB; still images/PDF/audio/video only) and `projects_add_task_link` for any URL |
| Fixed board columns, no tags (V10) | **Shipped** | `projects_create_stage` / `update_stage` / `reorder_stages` / `remove_stage` (up to 30 per project). Tags: `projects_create_tag`, `projects_set_task_tags` (replaces the list); `projects_list_items` filters by tag |
| No project template / duplicate | **Shipped** | `projects_save_as_template`, `projects_create_from_template` (optional `deal_id`), `projects_duplicate`, `projects_for_deal`. **`deal_templates_create.project_template_id`** auto-creates a linked project when a deal is made from the deal template (admin only) |
| Workflows only create CRM tasks; no project triggers | **Mostly** | Actions `create_project_task`, `update_project_task`. Triggers `project_task_completed`, `project_subtask_completed`, `project_task_moved`. Still missing: a project-task-*created* trigger; workflow actions can't set reviewer, tags or comments |
| No reviewer field | **Shipped** | Native reviewer on project tasks: `projects_set_task_reviewer`, `projects_request_review`, `projects_approve_review` (completes the task), `projects_return_review`, `projects_my_reviews`. CRM tasks also gained `reviewer_id` |
| No team-member custom field | **Shipped** | Field type `user` on **deals** and custom objects; `deals_list` filters by `member_field` + `member` |
| Reports: one dimension, no task dataset (V9) | **Unchanged** | `projects_dashboard` per project only |
| Plain-text task descriptions (V4) | **Unchanged** | Task links make this a minor issue |
| No date-reached / deal-field-changed trigger | **Unchanged** | |
| No API delete for projects / object types | **Unchanged** | `projects_delete_notebook` added. The two `ZZ-TEST` leftovers still need deleting in the UI |

Design impact: see the updated [operational stage spec](operational-stage-spec.md) and
[automation map](automation-map.md). These are configuration changes only; no SOP change.

## Recommendation

**Option A is confirmed in the live workspace.** Since the 2026-10-04 platform update, most workarounds are no longer needed. Chirply is the
main operational front end, configured as specified in the
[operational stage spec](operational-stage-spec.md). The methodology's own Operational Tracker
v1.0, as a Google Sheet per project, holds the tabular registers (Content Inputs, Proof Inventory,
QA checks, Measurement).** No new platform.

The fallback trigger (V2 or V5 failing) **did not fire**. V2 passed, and V5's pipeline and workflow
built and activated, with only the firing left to observe on the pilot's first real deal. If that firing
fails, revisit before Stage 01. Per decision D5, **Notion is not added**.

The compromises are real but bounded: no comments or statuses on project tasks, and no native project
automation. Each one has a workaround that uses Chirply features shown to work (deal notes, deal
stages, custom-object automations) or systems already in the stack (Drive, the Tracker Sheet).

Why not add ClickUp or Notion now:

- Every **must-have** has a Chirply route, native or configured, except a native cross-project
  overdue dashboard, which a weekly API digest covers.
- The things a PM tool would add (dependencies, hard gates, richer checklists) don't justify a second
  delivery system. Even in ClickUp or Notion, the DoD gate is ultimately a human decision. Here it is
  a human decision with an automated flag.
- Chirply already owns the client relationship and communications. A second tool would split
  "where is this project?" across two systems and need syncing.
- Google Sheets and Drive are already in use, and the **Operational Tracker v1.0 is already part of
  the methodology**. Using its tabular tabs as the companion adds no software and changes no method.
  Chirply takes over only the tabs it does better (stage status, approvals, dashboard). See the
  [tab split](../templates/operational-tracker.md#how-the-tracker-is-used-with-chirply).

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
