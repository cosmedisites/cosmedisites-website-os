# Operating architecture and tech stack

## Recommendation: Option A, with Chirply as the operational front end

```
GITHUB  ─────────────  canonical CosmediSites operating IP (this repo)
   │                   methodology · stage cards · prompts · templates · QA gates
   │   releases → stage-config.json (links + DoD) → provisions each new project
   ▼
CHIRPLY ─────────────  team workflow · CRM · approvals · project status · client comms
   │                   deal = project record + current stage · project = stage tasks + DoD
   │                   Approval Record custom object · inbox · forms · automations
   ▼
GOOGLE DRIVE ────────  client files and project artefacts
   │                   Master Project Context (Google Doc) · filled templates
   │                   Project Tracker (Google Sheet copy of Operational Tracker v1.0):
   │                   Content Inputs · Proof Inventory · QA checks · Measurement
   │                   Apps Script = glue (Drive folder creation, sheet reminders, digest)
   ▼
FIGMA ───────────────  design
   ▼
CLAUDE / CHATGPT ────  research, strategy drafting, validation (one AI project per client)
```

This is the preferred end state from the brief, and the [Chirply audit](chirply-audit.md)
supports it, **conditional on verification tests V2 and V5** in the CosmediSites workspace.

## One home for every piece of information

Rule: **each fact has one home.** Other systems link to it rather than copying it.

| Information | Home (system of record) | Linked from |
|---|---|---|
| Methodology, SOP, DoD criteria, prompts, templates | GitHub | Chirply stage tasks, stage cards |
| Which OS version a project runs on | Chirply deal field `OS version` | – |
| Client and contacts | Chirply company / contacts | – |
| Project record (domain, team, launch date, objective, priority services) | Chirply deal | Master Project Context links back |
| **Current stage** | **Chirply deal pipeline stage** | The Master Project Context `Current stage` line is updated at each transition, for AI context only |
| Stage owner, due date, DoD progress | Chirply project: stage task + DoD subtasks | – |
| Approvals (decision, level, owner, status, date, approver, feedback class, locked) | Chirply custom object `Approval Record` (same columns as the Tracker *Approvals* tab) | Template 12 in Drive holds the narrative |
| Locked strategic decisions (the wording) | Master Project Context, LOCKED DECISIONS section | Approval Record links to it |
| Confirmed / inferred / open project facts | Master Project Context (Google Doc in Drive) | Chirply deal URL field |
| Artefacts (brief, evidence pack, positioning…) | Google Drive project folder | Chirply deal URL fields / stage tasks |
| Content inputs, proof inventory, QA checks, measurement | Project Tracker Google Sheet (tabs *Content Inputs*, *Proof Inventory*, *QA*, *Measurement*) | Deal field `Project Tracker`; Stage 07/10/12/13/14 tasks |
| Stage owners, reviewers, DoD (the definition) | GitHub (`ops/stages.yaml`, from SOP v1.0 and Tracker *Stage Tracker*) | Stage task descriptions |
| Designs | Figma | Deal URL field |
| Client emails, input requests, reminders, meeting notes | Chirply inbox / timeline | – |
| Credentials | Password manager | Never stored elsewhere |
| AI conversations | Claude / ChatGPT project per client | Approved outputs saved to Drive. The AI output is never the system of record |

## What each system does and does not do

| System | Does | Does not |
|---|---|---|
| **GitHub** | Holds and versions the OS; reviews changes; publishes releases; logs improvement issues | Hold client data; serve as the team's daily UI |
| **Chirply** | Project pipeline, stage tasks and DoD, owners and dates, approvals, client comms, reminders, automation, project-level reporting | Store long documents; hold the tabular registers (Tracker Sheet does); hold credentials |
| **Google Drive** | Client artefacts, Master Project Context, tracker sheets, restricted client assets; Apps Script glue | Track status (status lives in Chirply) |
| **Figma** | Design files, prototypes, dev handoff inspect | Approval records (Chirply) |
| **Claude / ChatGPT** | Drafting, analysis, validation against DoD | Approve anything; be the record |

## Fallback: Option B

Use this **only if** verification test V2 (project subtasks) or V5 (stage-change automation) fails
in the CosmediSites workspace.

**Chirply keeps:** CRM, client record, all client communication (inbox, templates, reminders,
forms), the deal pipeline as the top-level project status, and approvals via e-signature where needed.
The Project Tracker Sheet is used in full as the methodology designed it (all tabs live).

**One companion handles:** stage tasks, DoD checklists, owners/reviewers/due dates, QA gates and
the delivery dashboard.

**Which companion:** **Notion**. A Notion connector is already attached to this account, so it is
probably already in use. Confirm that before choosing it. It also has the database features the
gaps need (checkbox properties, relations, roll-ups, templates, filtered dashboards).
- ClickUp would be a new vendor. Choose it only if Notion isn't actually licensed.
- A MonoDesk connector is also attached, but its model (clients → projects → kanban tasks/subtasks)
  has the same gaps as Chirply's projects module, so it would not close them.
- Do not use both Notion and ClickUp.

Under Option B, Chirply's deal stage stays the "current stage" for the business. The companion
holds only delivery tasks and links back to the Chirply deal.

## Final recommended tech stack

| Layer | Tool | New spend? |
|---|---|---|
| Canonical OS | GitHub, `cosmedisites` organisation, private repo `cosmedisites-website-os` | Possibly: **GitHub Team** is needed for branch protection and required reviews on a private repo |
| Operational front end + CRM + client comms + automation | **Chirply** (existing) | No (pending plan check V1) |
| Client files, Master Project Context, Project Tracker (Operational Tracker v1.0) | **Google Drive / Sheets / Docs** (existing) | No |
| Glue scripts (Drive folders, sheet reminders, weekly digest, provisioning) | **Google Apps Script** (included with Google Workspace) | No |
| Design | **Figma** (existing) | No |
| AI execution | **Claude Projects** (one per client) and/or ChatGPT Projects | Existing |
| Optional | Chirply Zapier connector | Avoid unless Apps Script can't do the job |

**Net new tools: none.** The only potential new cost is a GitHub Team plan, plus any Chirply plan
change V1 reveals.
