#!/usr/bin/env python3
"""Block secrets, personal data and binaries from entering the OS repository.

Usage:
    python3 scripts/safety_scan.py            # scan all tracked files
    python3 scripts/safety_scan.py FILE...    # scan specific files

A safety net, not a guarantee. See SECURITY.md.

To allow a false positive on one line, append the marker  safety-scan:allow
with a reason, and expect the reviewer to ask about it.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALLOW_MARKER = "safety-scan:allow"

BLOCKED_EXT = {
    ".docx", ".doc", ".xlsx", ".xls", ".xlsm", ".pptx", ".pdf", ".zip",
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic", ".tif", ".tiff", ".mp4", ".mov",
    ".pem", ".p12", ".pfx", ".env",
}
ALLOWED_BINARY_DIRS = ("docs/assets/",)

PATTERNS = {
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    "Google OAuth token": re.compile(r"\bya29\.[0-9A-Za-z_\-]{20,}"),
    "GitHub token": re.compile(r"\b(ghp|gho|ghu|ghs|ghr)_[0-9A-Za-z]{36}\b|\bgithub_pat_[0-9A-Za-z_]{40,}"),
    "Slack token": re.compile(r"\bxox[abprs]-[0-9A-Za-z-]{10,}"),
    "Stripe live key": re.compile(r"\b[sr]k_live_[0-9A-Za-z]{16,}"),
    "Anthropic/OpenAI key": re.compile(r"\bsk-(ant-)?[A-Za-z0-9_\-]{32,}"),
    "credential assignment": re.compile(
        r"(?i)\b(password|passwd|api[_-]?key|secret|client[_-]?secret|access[_-]?token)\b\s*[:=]\s*['\"]?[^\s'\"{}<>]{6,}"),
    "email address": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "UK phone number": re.compile(r"(?<![\d.])(?:\+44\s?7\d{3}|07\d{3})\s?\d{3}\s?\d{3}(?!\d)"),
    "NHS number pattern": re.compile(r"(?<!\d)\d{3}[ -]\d{3}[ -]\d{4}(?!\d)"),
}

# Emails that are allowed: placeholders and role addresses for the OS itself.
EMAIL_ALLOW = re.compile(r"@(example\.(com|org|co\.uk)|cosmedisites\.[a-z.]+|users\.noreply\.github\.com|anthropic\.com)$", re.I)


def tracked_files() -> list[Path]:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout
    return [ROOT / p for p in out.decode().split("\0") if p]


def scan(path: Path) -> list[str]:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "scripts/safety_scan.py":
        return []
    problems = []
    if path.suffix.lower() in BLOCKED_EXT and not rel.startswith(ALLOWED_BINARY_DIRS):
        return [f"{rel}: blocked file type {path.suffix} (attach binaries to a GitHub Release; never commit client files)"]
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, FileNotFoundError):
        return [] if not path.exists() else [f"{rel}: binary/non-UTF-8 file. Is it meant to be here?"]
    for lineno, line in enumerate(text.splitlines(), 1):
        if ALLOW_MARKER in line:
            continue
        for name, rx in PATTERNS.items():
            for m in rx.finditer(line):
                if name == "email address" and EMAIL_ALLOW.search(m.group(0)):
                    continue
                problems.append(f"{rel}:{lineno}: possible {name}: {m.group(0)[:12]}…")
    return problems


def main() -> int:
    files = [Path(a).resolve() for a in sys.argv[1:]] or tracked_files()
    problems = [p for f in files if f.is_file() or not f.exists() for p in scan(f)]
    if problems:
        print("Safety scan FAILED. This repository must not contain secrets, personal data or client files.")
        print("\n".join(problems))
        print("\nSee SECURITY.md. For a genuine false positive, add 'safety-scan:allow <reason>' to the line.")
        return 1
    print(f"Safety scan OK ({len(files)} files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
