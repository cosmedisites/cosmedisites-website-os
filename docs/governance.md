# Governance: branches, reviews, releases, versioning, issues

## Principle

`main` = the approved production version of the CosmediSites Website OS.
Anything not on `main` is a proposal.

```
branch → change → pull request → review → merge → changelog (if material) → release/tag (if appropriate)
```

## Branches

| Branch | Use |
|---|---|
| `main` | Approved production version. Protected. No direct pushes |
| `improve/*` | Workflow/process improvements |
| `fix/*` | Bug fixes (broken prompt behaviour, wrong links) |
| `docs/*` | Documentation-only changes |
| `test/*` | Trial versions of prompts/templates under a TEST issue (may never merge) |

Merge method: **squash merge** (one commit per change on `main`, titled after the PR).

## Review model: two phases

The aim is to **preserve history and prevent casual edits**, not to recreate enterprise governance
before the team has more than one maintainer.

### Phase 1: single maintainer (now, v1.0 → first pilot)

- `main` is production. Nobody edits `main` directly.
- **Material changes** (methodology, SOP, Playbook, master prompts, core templates, AI operating
  rules, `ops/stages.yaml`) go on a branch and through a **pull request**, even though you review it
  yourself. The PR is the audit trail: what changed, why, and which issue prompted it.
- **Your own approval is the release gate.** Merge when the `checks` CI is green and you're
  satisfied. No second approval required.
- Editorial fixes (typos, links) may also go via PR; a quick self-merged PR is fine.
- Never force-push or delete `main`.

GitHub settings for this phase (**Settings → Rules → Rulesets → New branch ruleset**, target `main`),
only if your plan enforces rulesets on private repositories (GitHub Team or above):
- ✅ Restrict deletions
- ✅ Block force pushes
- ✅ Require a pull request before merging, with **required approvals: 0**. This stops direct
  pushes but lets you merge your own PR.
- ✅ Require status checks to pass: `checks`

On GitHub Free these rules aren't enforced on a private repository, so follow them by convention.
CI still runs on every PR, and the history is still preserved.

### Phase 2: two or more maintainers (when a second reviewer joins)

Raise the ruleset to:
- required approvals: **1**, with ✅ *Require review from Code Owners*;
- ✅ *Dismiss stale approvals when new commits are pushed*;
- bypass list: repository admin only, for emergencies.

Then create the CODEOWNERS teams (below) and replace the single owner in `CODEOWNERS`.

### Always

- General → Pull Requests: allow **squash merging** only; ✅ automatically delete head branches.
- Forking disabled (already off).
- Secret scanning / push protection if your plan provides them for private repositories.
- Labels: `bug`, `improvement`, `test`, `documentation`, `triage`, `methodology`, `accepted`,
  `needs-evidence`, `wontfix`, `v1.1-candidate`.

## Who reviews what

CODEOWNERS ([`CODEOWNERS`](../CODEOWNERS)) requests reviewers automatically. Recommended teams to create:

| Team | Owns |
|---|---|
| `os-maintainers` | Everything by default; `.github/`, `scripts/`, governance |
| `methodology` | `playbook/`, `sop/`, `workflows/00-*`, `ops/stages.yaml` |
| `strategy` | Stages 00–04, 07–09 prompts and templates |
| `delivery` | Stages 05–06, 10–14 prompts, templates, `qa/` |

**Required review (Phase 2):** at least one approval for any material change. For **methodology-class** changes (see
[CONTRIBUTING](../CONTRIBUTING.md#change-classes)), approval from the methodology owner plus one other
senior reviewer, and the PR must cite cross-project evidence.

## Versioning

Kept deliberately simple: `MAJOR.MINOR` in [`VERSION`](../VERSION), tagged `vMAJOR.MINOR`.

| Version | Meaning |
|---|---|
| **v1.0** | Initial production system |
| **v1.1, v1.2, …** | Workflow/process improvements, or additional tooling/templates/prompts. Bump the minor version for any material batch of merged changes |
| **v2.0** | Material methodology/process change: a stage added, removed or reordered, decision hierarchy or evidence states changed, gates changed |

- Editorial fixes don't need a release; they go out with the next one.
- Release when there is something worth telling the team. A release roughly monthly, or after
  each pilot review, is a sensible rhythm.
- Every project records the **OS version** it started on (Chirply deal field). Running projects
  aren't forced onto new versions mid-stream.

## Releases

1. Move the `[Unreleased]` entries in `CHANGELOG.md` under a new version heading.
2. Update `VERSION`. Merge via PR.
3. Tag `main`: `git tag v1.1 && git push origin v1.1` (or create the release in the GitHub UI with a new tag).
4. `release.yml` publishes the release with `ALL_PROMPTS.md`, `prompt-catalog.json`,
   `stage-config.json` and a source zip.
5. Upload packaged DOCX/XLSX (e.g. the Quickstart DOCX, Template Pack DOCX, Operational Tracker
   XLSX) to the release by hand. **They are never committed.**
6. Post the release notes to the team.

## Issues

A lightweight loop for improving the OS. Templates are in `.github/ISSUE_TEMPLATE/`.

| Type | Use when |
|---|---|
| **BUG** | A process, prompt or template produces a **repeatable** failure |
| **IMPROVEMENT** | A **repeated** project friction could be solved by improving the system |
| **TEST** | A proposed workflow/prompt change should be **trialled** on live projects before going global |
| **DOCUMENTATION** | Something is unclear or missing |

### The loop

```
live project → friction observed → issue logged → evidence/examples gathered (anonymised)
→ change proposed (PR) → reviewed → merged → release notes
```

### Triage (fortnightly, 20 minutes, OS maintainer + methodology owner)

- **Every issue starts `triage`.** Outcomes: `accepted` · `needs-evidence` · `test` · `wontfix`.
- **One awkward client case does not change the master SOP.** An issue seen on one project gets
  `needs-evidence` and stays open while further projects add (anonymised) evidence, or it becomes a
  `TEST`.
- Accept when: the problem is clearly stated; the friction is repeated (normally 2+ projects) or the
  risk is high (compliance, migration, data); and the fix doesn't add disproportionate admin.
- Stage 14E learning capture feeds this queue at the end of every project.

### What never goes in an issue

Client names, patient information, screenshots of client sites containing personal data,
credentials, or analytics exports. Refer to projects by internal code (for example `P-014`).
