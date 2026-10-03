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

SOP = ROOT / "sop" / "website-redesign-sop.md"
PLAYBOOK = ROOT / "playbook" / "website-strategy-playbook.md"

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


def doc_anchors(path: Path, pattern: str) -> dict[str, tuple[str, str]]:
    """Map a key (stage number / section number) to (heading text, anchor) for H1 headings."""
    out = {}
    for m in re.finditer(pattern, path.read_text(encoding="utf-8"), re.M):
        out[m.group("key")] = (m.group("text").strip(), gh_anchor(m.group("text")))
    return out


def sop_dods(path: Path) -> dict[str, list[str]]:
    """Return {stage number: [DoD checklist items]} for every SOP stage section that has one."""
    text = path.read_text(encoding="utf-8")
    sections = re.split(r"^# ", text, flags=re.M)
    out: dict[str, list[str]] = {}
    for sec in sections:
        m = re.match(r"Stage (\d+) — ", sec)
        if not m:
            continue
        dod = re.search(r"^## Definition of Done\s*\n(.*?)(?=^#|\Z)", sec, re.M | re.S)
        if dod:
            out[m.group(1)] = re.findall(r"^- \[ \] (.+)$", dod.group(1), re.M)
    return out


def stage_card(cfg: dict, stage: dict, nxt: dict | None, catalog: dict, anchors: dict,
               sop: dict, playbook: dict) -> str:
    sid = stage["id"]
    prompts_rel = "prompts.md"
    sop_text, sop_anchor = sop[str(stage["sop_stage"])]
    statuses = " · ".join(cfg["statuses"]["stage"])
    lines = [
        f"# STAGE {sid} — {stage['name'].upper()}",
        "",
        "<!-- GENERATED from ops/stages.yaml by scripts/build.py. Do not edit by hand. -->",
        "",
        "> This is the stage card: what you need to work this stage. Day-to-day status lives in the",
        "> operational tool (Chirply). This card and the files it links to are the source.",
        "",
        "| Status | Owner | Reviewer | Client involved | Deadline |",
        "|---|---|---|---|---|",
        f"| *set per project* | {stage['owner']} | {stage['reviewer']} | {stage['client_involved']} | *set per project* |",
        "",
        f"Status values: {statuses}.",
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
        lines.append(f"- QA gate — [{meta['title']}](../../{meta['file']}) *(owner: {meta['owner']})*")
    if stage.get("tracker_tabs"):
        tabs = ", ".join(stage["tracker_tabs"])
        lines.append(f"- Project Tracker tab(s): {tabs} ([structure](../../templates/operational-tracker.md))")
    src = stage["dod_source"]
    src_label = f"SOP v1.0, {sop_text}" if src == "SOP" else src
    lines += ["", "## Definition of Done", "", f"*Source: {src_label}*", ""]
    lines += [f"- [ ] {item}" for item in stage["dod"]]
    if stage.get("gate_checks"):
        lines += ["", "**Also required before moving stage:**", ""]
        lines += [f"- [ ] {g['check']} *({g['source']})*" for g in stage["gate_checks"]]
    lines += [
        "",
        "> Never move to the next stage because the previous one feels approximately finished.",
        "> Move when its Definition of Done has been met, or an authorised exception is recorded.",
        "",
        "## Approval",
        "",
        f"- Approval required: **{stage['approval']}**",
        f"- Gate: {stage['gate']}",
    ]
    if stage.get("locks"):
        lines.append(f"- On approval, lock: **{stage['locks']}**. Add it to LOCKED DECISIONS in the Master Project Context.")
    lines += ["", "## Method", "", f"- SOP: [{sop_text}](../../sop/website-redesign-sop.md#{sop_anchor})"]
    for n in stage.get("playbook", []):
        text, anchor = playbook[str(n)]
        lines.append(f"- Playbook: [{text}](../../playbook/website-strategy-playbook.md#{anchor})")
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
        lines.append("End of workflow. Log reusable learning from 14E as GitHub Issues.")
    lines.append("")
    return "\n".join(lines)


README = ROOT / "README.md"
TABLE_RE = re.compile(r"(<!-- stages-table:start[^>]*-->\n)(.*?)(<!-- stages-table:end -->)", re.S)


def readme_with_table(cfg: dict) -> str:
    rows = ["| # | Stage | Owner (SOP) | Output | Approval required |", "|---|---|---|---|---|"]
    for s in cfg["stages"]:
        rows.append(f"| {s['id']} | [{s['name']}](workflows/{s['slug']}/README.md) | {s['owner']} "
                    f"| {s['output']} | {s['approval']} |")
    text = README.read_text(encoding="utf-8")
    if not TABLE_RE.search(text):
        errors.append("README.md: stages-table markers missing")
        return text
    return TABLE_RE.sub(lambda m: m.group(1) + "\n".join(rows) + "\n" + m.group(3), text)


def stage_config(cfg: dict, catalog: dict, anchors: dict, sop: dict, playbook: dict) -> dict:
    stages = []
    for i, s in enumerate(cfg["stages"]):
        base = f"workflows/{s['slug']}"
        nxt = cfg["stages"][i + 1]["id"] if i + 1 < len(cfg["stages"]) else None
        sop_text, sop_anchor = sop[str(s["sop_stage"])]
        stages.append({
            "id": s["id"],
            "name": s["name"],
            "task_name": f"S{s['id']} — {s['name']} — {s['route']}",
            "objective": s["objective"],
            "owner": s["owner"],
            "reviewer": s["reviewer"],
            "client_involved": s["client_involved"],
            "approval": s["approval"],
            "approval_type": s["approval_type"],
            "gate": s["gate"],
            "locks": s.get("locks"),
            "next_stage": nxt,
            "output": s["output"],
            "definition_of_done": s["dod"],
            "definition_of_done_source": s["dod_source"],
            "gate_checks": s.get("gate_checks", []),
            "tracker_tabs": s.get("tracker_tabs", []),
            "links": {
                "stage_card": blob(cfg, f"{base}/README.md"),
                "sop": {"title": sop_text, "url": blob(cfg, "sop/website-redesign-sop.md", sop_anchor)},
                "playbook": [
                    {"title": playbook[str(n)][0], "url": blob(cfg, "playbook/website-strategy-playbook.md", playbook[str(n)][1])}
                    for n in s.get("playbook", [])
                ],
                "templates": [
                    {"title": f"Template {cfg['templates'][t]['number']} — {cfg['templates'][t]['title']}",
                     "url": blob(cfg, f"templates/{t}.md")} for t in s["templates"]
                ],
                "prompts": [
                    {"id": p["id"], "kind": p["kind"], "title": f"{p['id']} — {catalog[p['id']]['name']}",
                     "url": blob(cfg, f"{base}/prompts.md", anchors[p["id"]])} for p in s["prompts"]
                ],
                "qa_gates": [
                    {"title": cfg["qa_gates"][g]["title"], "owner": cfg["qa_gates"][g]["owner"],
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
    return {"os_version": VERSION, "statuses": cfg["statuses"], "roles": cfg["roles"], "stages": stages}


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
    sop = doc_anchors(SOP, r"^# (?P<text>Stage (?P<key>\d+) — .+)$")
    dods = sop_dods(SOP)
    playbook = doc_anchors(PLAYBOOK, r"^# (?P<text>(?P<key>\d+)\. .+)$")

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
        if str(s.get("sop_stage")) not in sop:
            errors.append(f"stage {s['id']}: SOP has no '# Stage {s.get('sop_stage')} —' heading")
        for n in s.get("playbook", []):
            if str(n) not in playbook:
                errors.append(f"stage {s['id']}: Playbook has no section {n}")
        for g in s.get("qa_gates", []):
            if g not in cfg["qa_gates"]:
                errors.append(f"stage {s['id']}: unknown QA gate {g}")
        sop_dod = dods.get(str(s.get("sop_stage")))
        if s.get("dod_source") == "SOP":
            if sop_dod is None:
                errors.append(f"stage {s['id']}: dod_source is SOP but the SOP stage has no Definition of Done")
            elif s.get("dod") != sop_dod:
                errors.append(f"stage {s['id']}: dod does not match the SOP Definition of Done verbatim")
        elif sop_dod is not None:
            errors.append(f"stage {s['id']}: the SOP now has a Definition of Done; set dod_source: SOP and copy it")
        for field in ("owner", "reviewer", "client_involved", "approval", "approval_type", "dod", "dod_source"):
            if not s.get(field):
                errors.append(f"stage {s['id']}: missing {field}")
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
        card = stage_card(cfg, s, nxt, catalog, anchors, sop, playbook)
        path = ROOT / "workflows" / s["slug"] / "README.md"
        if check:
            if not path.exists() or path.read_text(encoding="utf-8") != card:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(card, encoding="utf-8")

    readme = readme_with_table(cfg)
    if check:
        if README.read_text(encoding="utf-8") != readme:
            stale.append("README.md (stages table)")
    else:
        README.write_text(readme, encoding="utf-8")

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
        json.dumps(stage_config(cfg, catalog, anchors, sop, playbook), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"OK: {len(cfg['stages'])} stages, {len(catalog)} prompts. dist/ written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
