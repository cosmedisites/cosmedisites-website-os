#!/usr/bin/env python3
"""Regenerate templates/operational-tracker.md from the Operational Tracker workbook.

Usage:
    pip install openpyxl
    python3 scripts/tracker_spec.py path/to/CosmediSites_Redesign_Operational_Tracker_vX.Y.xlsx

The workbook is a GitHub Release asset (never committed). This page is its reviewable,
versioned specification: change the workbook, run this script, open a PR.
The introductory section (everything before "## Lists") is preserved from the existing page.
"""
from __future__ import annotations

import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "templates" / "operational-tracker.md"


def cell(c) -> str:
    return "" if c is None else str(c).replace("|", "\\|")


def render(xlsx: Path, intro: str) -> str:
    wb = openpyxl.load_workbook(xlsx)
    o = [intro.rstrip("\n"), ""]
    for ws in wb.worksheets:
        o += [f"## {ws.title}", ""]
        dvs = {str(d.sqref): d.formula1 for d in ws.data_validations.dataValidation}
        rows = [r for r in ws.iter_rows(values_only=True) if any(c is not None for c in r)]
        if not rows:
            continue
        if ws.title == "Lists":
            hdr = rows[0]
            o += ["| " + " | ".join(hdr) + " |", "|" + "---|" * len(hdr)]
            for r in rows[1:]:
                o.append("| " + " | ".join("" if c is None else str(c) for c in r[:len(hdr)]) + " |")
        elif ws.title == "Dashboard":
            for r in rows:
                o.append("- " + " · ".join(str(c) for c in r if c is not None).replace("|", "\\|"))
        else:
            hdr = [c for c in rows[0] if c is not None]
            o += ["| " + " | ".join(hdr) + " |", "|" + "---|" * len(hdr)]
            for r in rows[1:]:
                vals = [cell(c) for c in r[:len(hdr)]]
                if any(vals):
                    o.append("| " + " | ".join(vals) + " |")
        if dvs:
            o += ["", "Data validation:", ""] + [f"- `{k}`: {v}" for k, v in dvs.items()]
        o.append("")
    return "\n".join(o) + "\n"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    current = SPEC.read_text(encoding="utf-8")
    intro = current[: current.index("## Lists")]
    SPEC.write_text(render(Path(sys.argv[1]), intro), encoding="utf-8")
    print(f"Wrote {SPEC.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
