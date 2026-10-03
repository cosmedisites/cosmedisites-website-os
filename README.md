# CosmediSites Website Operating System

The canonical, version-controlled source of how CosmediSites plans, designs, builds, launches and
measures clinic website redesigns.

**Current version:** see [`VERSION`](VERSION) · [Changelog](CHANGELOG.md)

---

## What this is

This repository is CosmediSites company IP: the methodology, the stage workflow, the templates and
the AI prompts our team uses on every redesign project. Everything else reads from it.

| System | Job |
|---|---|
| **GitHub (this repo)** | Canonical operating system. Approved, version-controlled IP. |
| **Chirply** | The team's day-to-day interface: project status, tasks, approvals, client comms. See [operating architecture](docs/operating-architecture.md). |
| **Google Drive** | Live client files, including each project's Master Project Context, trackers and artefacts. |
| **Figma** | Design. |
| **Claude / ChatGPT** | AI execution layer: research, drafting, validation. |

**This repository never holds client data.** No client projects, patient information, credentials
or analytics exports. See [SECURITY.md](SECURITY.md).

Most of the team never needs to browse this repository. The operational tool links straight to the
stage card, template or prompt you need.

## The three layers

| Layer | Question it answers | Where |
|---|---|---|
| **Playbook** | How we think | [`playbook/`](playbook/website-strategy-playbook.md) |
| **SOP** | What happens next | [`sop/`](sop/website-redesign-sop.md) + [stage cards](workflows/00-workflow-index.md) |
| **Templates / Prompts** | How we execute | [`templates/`](templates/), [`workflows/`](workflows/), [`prompts/`](prompts/) |

## The operating rule

> **Never move stage because the previous one feels approximately finished.
> Move when its Definition of Done is met.**

Every stage ends with a validator prompt that returns PASS / FAIL / BLOCKED. A named human owner
decides; the AI does not approve strategy.

## The decision hierarchy

1. Business strategy
2. Positioning
3. UX / information architecture
4. Content / proof
5. Visual expression

A lower-level preference must not silently overturn a higher-level decision. Approved decisions are
**LOCKED** and reopen only through change control ([9E](workflows/stage-09-approval/prompts.md)).

## The 15 stages

| # | Stage | Output | Gate |
|---|---|---|---|
| 00 | [Commercial Brief](workflows/stage-00-commercial-brief/README.md) | Project Strategy Brief | Client factual confirmation |
| 01 | [Evidence](workflows/stage-01-evidence/README.md) | Evidence Pack | Internal |
| 02 | [Strategic Diagnosis](workflows/stage-02-diagnosis/README.md) | Strategic Diagnosis | Internal |
| 03 | [Positioning](workflows/stage-03-positioning/README.md) | Positioning Thesis + Brand Architecture | Client strategic approval |
| 04 | [IA + SEO](workflows/stage-04-ia-seo/README.md) | Sitemap / SEO Architecture | Conditional client approval |
| 05 | [Visual Direction](workflows/stage-05-visual-direction/README.md) | Visual Direction | Client approval |
| 06 | [Page + Component System](workflows/stage-06-page-system/README.md) | Page / Component System | Internal / included in review |
| 07 | [Proof + Content + Photography](workflows/stage-07-proof-content-photography/README.md) | Proof Inventory + Photography Brief | Client supplies inputs |
| 08 | [Client Strategy Review](workflows/stage-08-client-review/README.md) | Client Strategy Deck | Review meeting |
| 09 | [Approval Gate](workflows/stage-09-approval/README.md) | Approval Record | Client sign-off |
| 10 | [Production Inputs](workflows/stage-10-production-inputs/README.md) | Content / Input Tracker | Internal gate |
| 11 | [Build](workflows/stage-11-build/README.md) | Build Handoff | Internal |
| 12 | [QA](workflows/stage-12-qa/README.md) | Compliance / Strategy / Technical QA | Internal sign-off |
| 13 | [Launch](workflows/stage-13-launch/README.md) | Launch runbook + baseline | Launch sign-off |
| 14 | [30/60/90 Measurement](workflows/stage-14-measurement/README.md) | Post-launch review + learning | Internal / client review |

## How to start a new project

1. **Create the project in Chirply** from the Website Redesign template. This creates the pipeline
   card, the stage tasks 00–14 and the links. See the [Chirply operating spec](docs/operational-stage-spec.md).
2. **Create the client's Drive folder** from the standard structure, then copy the
   [Master Project Context](workflows/00-master-project-context.md) into it as a Google Doc.
   See [Master Project Context storage](docs/master-project-context.md).
3. **Run Stage 00** from its [stage card](workflows/stage-00-commercial-brief/README.md).
4. For AI work, follow the [AI execution workflow](docs/ai-execution-workflow.md): context + one stage
   prompt + relevant files + output template. Never the whole prompt library.

New to the system? Read the [Quickstart](docs/quickstart.md) (10 minutes).

## How to improve the system

Found friction on a live project? **Don't change the SOP. Log an issue.**

```
live project → friction observed → issue logged → evidence gathered
→ change proposed (PR) → reviewed → merged → release notes
```

- [Open an issue](https://github.com/cosmedisites/cosmedisites-website-os/issues/new/choose): Bug · Improvement · Test · Documentation
- Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change
- Governance, branching and releases: [docs/governance.md](docs/governance.md)

## Repository map

```
playbook/      how we think                         (awaiting import)
sop/           what happens next                    (awaiting import)
workflows/     operating rules, context template, workflow index, 15 stage folders
               └─ stage-NN-*/README.md   stage card (generated from ops/stages.yaml)
               └─ stage-NN-*/prompts.md  stage prompts
prompts/       client communications (C01–C09), team handoffs (H01–H08), prompt-catalog.csv
templates/     17 artefact templates (interim skeletons until the Template Pack is imported)
qa/            the three Stage 12 QA gates
examples/      anonymised "what good looks like"
docs/          quickstart, architecture, Chirply audit, governance, automation map
ops/           stages.yaml: the stage registry that drives stage cards and the Chirply payload
scripts/       build.py (generate + check), safety_scan.py (blocks secrets/PII)
```

## Maintainers' quick reference

```bash
pip install pyyaml
python3 scripts/build.py           # regenerate stage cards + dist/
python3 scripts/build.py --check   # what CI runs
python3 scripts/safety_scan.py     # what CI runs
```
