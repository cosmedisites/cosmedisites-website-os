# Contributing to the CosmediSites Website OS

This repository is the operating system every CosmediSites redesign runs on. A change here changes
how every future project is delivered. So changes are welcome, but they have to earn their place.

## Operating principles for changes

1. **Do not change global methodology because one client dislikes something.**
   One client's preference is project feedback. It is handled in that project (9B/9E), not here.
2. **Document the problem a proposed change solves.** No problem statement, no change.
3. **Repeated cross-project friction carries more weight than a one-off preference.**
   Two or more projects showing the same friction is the normal bar for a global change.
4. **Client-specific tactics do not automatically become global SOP.** A tactic that worked once
   becomes a `TEST` issue first.
5. **Keep prompts modular.** One prompt, one job. Prompts reference the AI Operating Rules and
   Master Project Context; they do not restate them.
6. **Do not duplicate instructions already covered globally.** If a rule applies everywhere, it
   belongs in `workflows/00-ai-operating-rules.md`, once.
7. **Update the Definition of Done when a process change alters completion criteria.**
   Edit `ops/stages.yaml` (and the SOP once imported), then regenerate the stage cards.
8. **Preserve locked higher-level strategic decisions** unless new evidence genuinely changes them.
   This applies to the methodology itself as well as to client projects.
9. **Do not add unnecessary complexity.** Every new field, stage, prompt or status is admin that
   someone pays for on every project.
10. **Examples must be anonymised before entering the repository.**
    See [examples/README.md](examples/README.md).
11. **Never commit client or patient data.** See [SECURITY.md](SECURITY.md). CI blocks common
    cases, but you are responsible for the rest.

## The improvement loop

```
live project
→ friction observed
→ issue logged (BUG / IMPROVEMENT / TEST / DOCUMENTATION)
→ evidence and examples gathered (anonymised, on the issue)
→ change proposed (pull request linked to the issue)
→ reviewed (CODEOWNERS)
→ merged to main
→ CHANGELOG updated where material
→ release / tag where appropriate
```

Issue types and when to use them: [docs/governance.md#issues](docs/governance.md#issues).

## How to make a change

1. **Branch** from `main`: `improve/<short-name>`, `fix/<short-name>`, `docs/<short-name>` or `test/<short-name>`.
2. **Change** the Markdown source. Non-technical contributors can do this in the GitHub web editor:
   "Edit this file" → "Create a new branch and start a pull request".
3. If you changed `ops/stages.yaml`, a stage `prompts.md` or `prompts/prompt-catalog.csv`, run
   `python3 scripts/build.py` and commit the regenerated stage cards. CI fails if you forget.
4. **Open a pull request** using the template. Link the issue. State the change class (below).
5. **Review.** While there is one maintainer, the maintainer's own approval is the gate. With two or
   more, CODEOWNERS are requested automatically.
6. **Merge** (squash merge) once approved and checks pass.
7. **CHANGELOG.** Add a line under `## [Unreleased]` for any material change.

## Change classes

| Class | Examples | Review: single maintainer (now) | Review: 2+ maintainers | Version impact |
|---|---|---|---|---|
| **Editorial** | Typos, broken links, clarifying wording without changing meaning | Self-merge | Self-merge | none, or next release |
| **Workflow / process** | Prompt improvements, DoD wording, handoff changes, new validator checks | PR, self-approved | 1 reviewer + methodology owner | minor (v1.**1**) |
| **Tooling / additions** | New template, new prompt, new QA check, automation spec | PR, self-approved | 1 reviewer | minor (v1.**2**) |
| **Methodology** | Stage added/removed/reordered, decision hierarchy, evidence states, operating rules, Playbook principles | PR, self-approved; cite cross-project evidence | Methodology owner + one senior reviewer; cite cross-project evidence | major (v**2**.0) |

See [governance › Review model](docs/governance.md#review-model-two-phases).

When unsure, treat the change as the higher class.

## Writing rules

- British English.
- Markdown is the editable source. Do not commit DOCX/XLSX/PPTX/PDF/ZIP. Attach those to Releases.
- Prompt headings must stay in the form `## <ID> — <Name>`, and every prompt needs a row in
  `prompts/prompt-catalog.csv`. CI checks this; stable headings keep the operational tool's deep links working.
- Do not rename stage folders or prompt IDs without a methodology-class PR. Chirply links depend on them.
- Do not edit generated files (`workflows/stage-*/README.md`) by hand.
