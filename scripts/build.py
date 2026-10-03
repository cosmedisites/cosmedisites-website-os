#!/usr/bin/env python3
"""CosmediSites Website OS — build and consistency checks.

Usage:
    python3 scripts/build.py           # regenerate stage cards + dist/ release files
    python3 scripts/build.py --check   # CI mode: fail if anything is stale or inconsistent

What it does:
  1. Loads ops/stages.yaml (stage registry) and prompts/prompt-catalog.csv.
  2. Checks every catalogue prompt exists as a "## <ID> — <Name>" heading in its file,
     and every prompt heading has a catalogue row.
  3. Generates workflows/stage-*/README.md (stage cards) from the registry.
  4. Generates dist/ (git-ignored; attached to GitHub Releases):
       - ALL_PROMPTS.md          consolidated prompt library
       - prompt-catalog.json     machine-readable catalogue
       - stage-config.json       payload for the operational tool (Chirply)
  5. Checks that relative Markdown links in the repo resolve.

Only needs Python 3.9+ and PyYAML.
"""
from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "ops" / "stages.yaml"
CATALOG = ROOT / "prompts" / "prompt-catalog.csv"
DIST = ROOT / "dist"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

KIND_LABEL = {"run": "RUN", "validate": "VALIDATE", "client": "CLIENT-FACING"}
APPROVAL_LABEL = {
    "client": "Required: client approval",
    "conditional": "Conditional: client approval where the sitemap/URL changes are material",
    "client-meeting": "Required: client review meeting held",
    "client-inputs": "Client must supply inputs; no strategic sign-off at this stage",
    "internal": "Internal sign-off only",
}

errors: list[str] = []


def gh_anchor(heading: str) -> str:
    """Reproduce GitHub's heading anchor algorithm closely enough for our headings."""
    text = heading.strip().lower()
    out = []
    for ch in text:
        cat = unicodedata.category(ch)
        if ch in " -_" or cat[0] in "LN":
            out.append(ch)
    return "".join(out).replace(" ", "-")


def load_catalog() -> dict[str, dict]:
    with CATALOG.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    by_id = {}
    for row in rows:
        if row["id"] in by_id:
            errors.append(f"prompt-catalog.csv: duplicate id {row['id']}")
        by_id[row["id"]] = row
    return by_id


HEADING_RE = re.compile(r"^## ([0-9]{1,2}[A-Z]|[CH][0-9]{2}) — (.+)$", re.M)


def index_prompt_files(catalog: dict[str, dict]) -> dict[str, str]:
    """Return {prompt_id: anchor}; record consistency errors."""
    anchors: dict[str, str] = {}
    files = sorted({row["file"] for row in catalog.values()})
    for rel in files:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"prompt-catalog.csv references missing file {rel}")
            continue
        for match in HEADING_RE.finditer(path.read_text(encoding="utf-8")):
            pid, name = match.group(1), match.group(2)
            anchors[pid] = gh_anchor(f"{pid} — {name}")
            if pid not in catalog:
                errors.append(f"{rel}: prompt heading {pid} has no catalogue row")
            elif catalog[pid]["file"] != rel:
                errors.append(f"{pid}: catalogue says {catalog[pid]['file']} but heading is in {rel}")
            elif catalog[pid]["name"].strip() != name.strip():
                errors.append(f"{pid}: catalogue name '{catalog[pid]['name']}' != heading '{name}'")
    for pid in catalog:
        if pid not in anchors:
            errors.append(f"catalogue prompt {pid} not found as a heading in {catalog[pid]['file']}")
    return anchors


def blob(cfg: dict, rel: str, anchor: str | None = None) -> str:
    url = f"{cfg['repo_url']}/blob/{cfg['default_branch']}/{rel}"
    return f"{url}#{anchor}" if anchor else url


def stage_card(cfg: dict, stage: dict, nxt: dict | None, catalog: dict, anchors: dict) -> str:
    sid = stage["id"]
    prompts_rel = "prompts.md"
    lines = [
        f"# STAGE {sid} — {stage['name'].upper()}",
        "",
        "<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->",
        "",
        "> This is the stage card: what you need to work this stage. Day-to-day status lives in the",
        "> operational tool (Chirply); this card and the files it links to are the source.",
        "",
        "| Status | Owner | Reviewer | Deadline |",
        "|---|---|---|---|",
        f"| *set per project* | {stage['owner_role']} *(default role)* | {stage['reviewer_role']} *(default role)* | *set per project* |",
        "",
        "## Objective",
        "",
        stage["objective"],
        "",
        "## Inputs",
        "",
        "- Master Project Context for this project (in the project's Drive folder)",
        "- [AI Operating Rules](../00-ai-operating-rules.md)",
    ]
    seen = set()
    for p in stage["prompts"]:
        if p["kind"] != "run":
            continue
        for item in catalog[p["id"]]["inputs"].rstrip(".").split(";"):
            item = item.strip()
            if item and item.lower() not in seen:
                seen.add(item.lower())
                lines.append(f"- {item[0].upper() + item[1:]}")
    lines += ["", "## Run", "", f"Route: **{stage['route']}**", ""]

    def prompt_line(p: dict) -> str:
        row = catalog[p["id"]]
        note = f" *({p['note']})*" if p.get("note") else ""
        return (f"- **[{p['id']} — {row['name']}]({prompts_rel}#{anchors[p['id']]})**{note} — "
                f"{row['use_when']} → *{row['produces']}*")

    for p in stage["prompts"]:
        if p["kind"] in ("run", "client"):
            tag = " `CLIENT-FACING`" if p["kind"] == "client" else ""
            lines.append(prompt_line(p) + tag)
    lines += ["", "## Validate", ""]
    for p in stage["prompts"]:
        if p["kind"] == "validate":
            lines.append(prompt_line(p))
    if stage.get("no_validator_reason"):
        lines.append(stage["no_validator_reason"])
    lines += ["", "## Output", "", f"**{stage['output']}**", ""]
    for t in stage["templates"]:
        meta = cfg["templates"][t]
        lines.append(f"- Template {meta['number']} — [{meta['title']}](../../templates/{t}.md)")
    for g in stage.get("qa_gates", []):
        meta = cfg["qa_gates"][g]
        lines.append(f"- QA gate — [{meta['title']}](../../{meta['file']}) *(owner: {meta['owner_role']})*")
    lines += [
        "",
        "## Definition of Done",
        "",
        "> **Interim.** This list is compiled from this stage's validator prompt(s) in the AI Workflow",
        "> Pack v1.0. The Website Redesign SOP v1.0 Definition of Done is authoritative. Reconcile",
        "> it when the SOP is imported ([sop/](../../sop/website-redesign-sop.md)).",
        "",
    ]
    lines += [f"- [ ] {item}" for item in stage["dod"]]
    lines += [
        "",
        "Do not move stage until every item passes, or an authorised exception is recorded.",
        "",
        "## Approval",
        "",
        f"- Gate: **{stage['gate']}**",
        f"- {APPROVAL_LABEL[stage['approval']]}",
    ]
    if stage.get("locks"):
        lines.append(f"- On approval, lock: **{stage['locks']}** (add to LOCKED DECISIONS in the Master Project Context)")
    extras = []
    for h in stage.get("handoffs", []):
        extras.append(f"- [{h} — {catalog[h]['name']}](../../prompts/team-handoffs/role-handoff-prompts.md#{anchors[h]})")
    for c in stage.get("client_comms", []):
        extras.append(f"- [{c} — {catalog[c]['name']}](../../prompts/client-communications/client-communication-prompts.md#{anchors[c]})")
    if extras:
        lines += ["", "## Handoffs and client communication", ""] + extras
    lines += ["", "## Next", ""]
    if nxt:
        lines.append(f"[Stage {nxt['id']} — {nxt['name']}](../{nxt['slug']}/README.md)")
    else:
        lines.append("End of workflow. Log OS improvements found in 14E as GitHub Issues.")
    lines.append("")
    return "\n".join(lines)


def stage_config(cfg: dict, catalog: dict, anchors: dict) -> dict:
    stages = []
    for i, s in enumerate(cfg["stages"]):
        base = f"workflows/{s['slug']}"
        nxt = cfg["stages"][i + 1]["id"] if i + 1 < len(cfg["stages"]) else None
        stages.append({
            "id": s["id"],
            "name": s["name"],
            "task_name": f"S{s['id']} — {s['name']} — {s['route']}",
            "objective": s["objective"],
            "default_owner_role": s["owner_role"],
            "default_reviewer_role": s["reviewer_role"],
            "approval": s["approval"],
            "gate": s["gate"],
            "locks": s.get("locks"),
            "next_stage": nxt,
            "output": s["output"],
            "definition_of_done": s["dod"],
            "links": {
                "stage_card": blob(cfg, f"{base}/README.md"),
                "sop": blob(cfg, "sop/website-redesign-sop.md"),
                "templates": [
                    {"title": f"Template {cfg['templates'][t]['number']} — {cfg['templates'][t]['title']}",
                     "url": blob(cfg, f"templates/{t}.md")} for t in s["templates"]
                ],
                "prompts": [
                    {"id": p["id"], "kind": p["kind"], "title": f"{p['id']} — {catalog[p['id']]['name']}",
                     "url": blob(cfg, f"{base}/prompts.md", anchors[p["id"]])} for p in s["prompts"]
                ],
                "qa_gates": [
                    {"title": cfg["qa_gates"][g]["title"], "owner_role": cfg["qa_gates"][g]["owner_role"],
                     "url": blob(cfg, cfg["qa_gates"][g]["file"])} for g in s.get("qa_gates", [])
                ],
                "handoffs": [
                    {"id": h, "title": f"{h} — {catalog[h]['name']}",
                     "url": blob(cfg, "prompts/team-handoffs/role-handoff-prompts.md", anchors[h])}
                    for h in s.get("handoffs", [])
                ],
                "client_comms": [
                    {"id": c, "title": f"{c} — {catalog[c]['name']}",
                     "url": blob(cfg, "prompts/client-communications/client-communication-prompts.md", anchors[c])}
                    for c in s.get("client_comms", [])
                ],
            },
        })
    return {"os_version": VERSION, "stages": stages, "roles": cfg["roles"]}


def all_prompts(cfg: dict) -> str:
    parts = [
        f"# CosmediSites Website OS v{VERSION} — All Prompts",
        "",
        "Generated by scripts/build.py. Use with `workflows/00-ai-operating-rules.md` and the project's Master Project Context.",
        "Do not load this whole file into an AI conversation. Use the current stage's prompts only.",
        "",
    ]
    sources = [f"workflows/{s['slug']}/prompts.md" for s in cfg["stages"]]
    sources += ["prompts/client-communications/client-communication-prompts.md",
                "prompts/team-handoffs/role-handoff-prompts.md"]
    for rel in sources:
        parts += ["---", "", (ROOT / rel).read_text(encoding="utf-8").strip(), ""]
    return "\n".join(parts) + "\n"


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def check_links() -> None:
    for md in ROOT.rglob("*.md"):
        if any(part in {".git", "dist", "node_modules"} for part in md.parts):
            continue
        text = md.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in LINK_RE.findall(text):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = target.split("#", 1)[0]
            if path and not (md.parent / path).resolve().exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link -> {target}")


def main() -> int:
    check = "--check" in sys.argv
    cfg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    catalog = load_catalog()
    anchors = index_prompt_files(catalog)

    ids = [s["id"] for s in cfg["stages"]]
    if ids != [f"{i:02d}" for i in range(15)]:
        errors.append("stages.yaml: stages must be 00..14 in order")
    for s in cfg["stages"]:
        for p in s["prompts"]:
            if p["id"] not in catalog:
                errors.append(f"stage {s['id']}: unknown prompt {p['id']}")
            elif catalog[p["id"]]["stage"] != str(int(s["id"])):
                errors.append(f"stage {s['id']}: prompt {p['id']} belongs to stage {catalog[p['id']]['stage']}")
        for t in s["templates"]:
            if t not in cfg["templates"]:
                errors.append(f"stage {s['id']}: unknown template {t}")
            elif not (ROOT / "templates" / f"{t}.md").exists():
                errors.append(f"templates/{t}.md missing")
        if not any(p["kind"] == "validate" for p in s["prompts"]) and not s.get("no_validator_reason"):
            errors.append(f"stage {s['id']}: no validator prompt (add one, or set no_validator_reason)")
        for ref in s.get("handoffs", []) + s.get("client_comms", []):
            if ref not in catalog:
                errors.append(f"stage {s['id']}: unknown reference {ref}")
    staged_prompts = {p["id"] for s in cfg["stages"] for p in s["prompts"]}
    for pid, row in catalog.items():
        if row["stage"] and pid not in staged_prompts:
            errors.append(f"prompt {pid} is in the catalogue but not routed in stages.yaml")

    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        return 1

    stale = []
    for i, s in enumerate(cfg["stages"]):
        nxt = cfg["stages"][i + 1] if i + 1 < len(cfg["stages"]) else None
        card = stage_card(cfg, s, nxt, catalog, anchors)
        path = ROOT / "workflows" / s["slug"] / "README.md"
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != card:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(card, encoding="utf-8")

    check_links()
    if stale:
        errors.append("stage cards out of date (run python3 scripts/build.py): " + ", ".join(stale))
    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        return 1

    DIST.mkdir(exist_ok=True)
    (DIST / "ALL_PROMPTS.md").write_text(all_prompts(cfg), encoding="utf-8")
    (DIST / "prompt-catalog.json").write_text(
        json.dumps(list(catalog.values()), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (DIST / "stage-config.json").write_text(
        json.dumps(stage_config(cfg, catalog, anchors), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"OK: {len(cfg['stages'])} stages, {len(catalog)} prompts. dist/ written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
