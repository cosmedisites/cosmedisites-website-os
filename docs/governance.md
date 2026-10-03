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

## Branch protection for `main` (to configure)

These are set in GitHub: **Settings → Rules → Rulesets → New branch ruleset** (or Settings →
Branches → Add rule), target `main`:

- ✅ Restrict deletions
- ✅ Block force pushes
- ✅ Require a pull request before merging
  - Required approvals: **1**
  - ✅ Dismiss stale approvals when new commits are pushed
  - ✅ Require review from Code Owners
  - ✅ Require conversation resolution before merging
- ✅ Require status checks to pass: `checks`
- ✅ Require linear history (works with squash merge)
- Bypass list: **repository admin only, for emergencies**

Also in Settings:
- General → Pull Requests: allow **squash merging** only; ✅ automatically delete head branches.
- General → disable forking (already off).
- Code security: enable **secret scanning** and **push protection** if your plan includes them for
  private repositories.
- Issues → create the labels: `bug`, `improvement`, `test`, `documentation`, `triage`,
  `methodology`, `accepted`, `needs-evidence`, `wontfix`.

> **Two practical constraints, checked at set-up:**
> 1. **Plan.** On GitHub Free, branch protection and rulesets are not enforced on *private*
>    repositories. Enforcing them needs **GitHub Team** (or Enterprise). Until then, follow the
>    rules by convention.
> 2. **Reviewers.** The `cosmedisites` organisation currently has **one member** and no teams. A
>    required approval can't be met by the PR author, so add at least one more reviewer (for
>    example the Head of Strategy) before enabling "Require approvals". Until then, the admin can
>    merge via the bypass, and should still open PRs so the history is reviewable.

## Who reviews what

CODEOWNERS ([`CODEOWNERS`](../CODEOWNERS)) requests reviewers automatically. Recommended teams to create:

| Team | Owns |
|---|---|
| `os-maintainers` | Everything by default; `.github/`, `scripts/`, governance |
| `methodology` | `playbook/`, `sop/`, `workflows/00-*`, `ops/stages.yaml` |
| `strategy` | Stages 00–04, 07–09 prompts and templates |
| `delivery` | Stages 05–06, 10–14 prompts, templates, `qa/` |

**Required review:** at least one approval for any change. For **methodology-class** changes (see
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
