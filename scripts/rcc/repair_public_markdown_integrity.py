from pathlib import Path
import json
from datetime import datetime, timezone

root = Path.cwd()

def read(path: str) -> str:
    p = root / path
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8-sig", errors="replace")

def write(path: str, content) -> None:
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, list):
        text = "\n".join(content)
    else:
        text = str(content)
    p.write_text(text.rstrip() + "\n", encoding="utf-8")
    print(f"[WRITE] {path}")

def load_json(path: str):
    return json.loads(read(path))

def save_json(path: str, data) -> None:
    write(path, json.dumps(data, indent=2, sort_keys=True))

def normalize_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\ufeff", "")
    text = text.replace("\x07erma", "aerma")
    text = text.replace("erma", "aerma")
    text = text.replace("verified erma import", "verified aerma import")
    text = text.replace("verified  erma import", "verified aerma import")
    text = text.replace("verified `erma` import", "verified `aerma` import")
    text = text.replace("verified erma import", "verified aerma import")
    return text

def force_lines_before_tokens(text: str) -> str:
    text = normalize_markdown(text)

    tokens = [
        "# AERMA-Memory",
        "## Human Director Box",
        "### What is this?",
        "### What changed?",
        "### Current health snapshot",
        "### What this is not",
        "### Where do I start?",
        "### Latest RCC-N reports",
        "# PART I - Human README",
        "## Current Identity",
        "## Quick Start",
        "## What AERMA Tests",
        "## Current Hardening Layer",
        "## Regression Guard",
        "## Project Structure",
        "## Main Folders",
        "## Evidence Artifacts",
        "## Non-Claim Locks",
        "# PART II - RCC Nexus README",
        "## RCC Nexus Identity",
        "## Repository Sphere",
        "## Nexus Meridians",
        "## Nexus Sectors",
        "## Primary Nexus Files",
        "## Nexus Context Integrity",
        "## RCC Nexus Echo Location",
        "Sphere Position:",
        "Local Role:",
        "Inbound Hooks:",
        "Outbound Hooks:",
        "Evidence Surface:",
        "Validation Surface:",
        "Claim Boundary:",
        "Non-Claim Locks:",
        "Agent Route:",
        "Update Obligation:",
        "## RCC Nexus Reports and Charts",
        "## RCC Nexus Non-Claim Lock",
        "# PART III - AI Agent README",
        "## AI Version Tracking Contract",
        "## AI Operating Contract",
        "## AI File Routing Guide",
        "## AI Non-Claim Lock",
        "## Required Local Verification",
        "## README Maintenance Rule",
        "## Current Roadmap for AI Agents",
        "## Final AI Warning",
    ]

    for token in tokens:
        text = text.replace(" " + token, "\n\n" + token)
        text = text.replace("\n" + token, "\n" + token)

    bullet_tokens = [
        "- Not ",
        "- `",
        "- AERMA",
        "- RCC",
        "- NCI",
        "- Geometry",
        "- Navigation",
        "- Context",
        "- source",
        "- validation",
        "- evidence",
        "- drift",
        "- agent",
        "- safety",
        "- runtime",
        "- memory",
        "- release",
        "- federation",
        "- core",
        "- schemas",
        "- retrieval",
        "- gate",
        "- benchmark",
        "- cli",
    ]

    for token in bullet_tokens:
        text = text.replace(" " + token, "\n" + token)

    for i in range(1, 20):
        text = text.replace(f" {i}. ", f"\n{i}. ")

    table_markers = [
        "| Surface | Current result |",
        "| Tests | 15 passed |",
        "| Task | Purpose |",
        "| Guard | Threshold |",
        "| Folder | Meaning |",
        "| Shell | Name | Meaning |",
        "| Artifact | Purpose |",
        "|---|---|",
        "|---|---:|",
        "|---|---|---|",
    ]

    for marker in table_markers:
        text = text.replace(" " + marker, "\n" + marker)

    text = text.replace(" --- ", "\n\n---\n\n")
    text = text.replace("```", "")

    lines = []
    for raw in text.split("\n"):
        line = raw.rstrip()
        if line.startswith("#") and lines and lines[-1] != "":
            lines.append("")
        lines.append(line)
        if line.startswith("#"):
            lines.append("")

    cleaned = []
    last_blank = False
    for line in lines:
        blank = line.strip() == ""
        if blank and last_blank:
            continue
        cleaned.append(line)
        last_blank = blank

    return "\n".join(cleaned).strip() + "\n"

def repair_file(path: str) -> dict:
    original = read(path)
    repaired = force_lines_before_tokens(original)
    write(path, repaired)
    return {
        "path": path,
        "before_lines": len(original.splitlines()),
        "after_lines": len(repaired.splitlines()),
        "before_chars": len(original),
        "after_chars": len(repaired),
    }

def markdown_health(path: str, min_lines: int) -> dict:
    text = read(path)
    lines = text.splitlines()
    bad = []
    if "\x07" in text:
        bad.append("control_char_bell")
    if len(lines) < min_lines:
        bad.append("line_count_below_minimum")
    if any(len(line) > 900 for line in lines):
        bad.append("very_long_line_over_900_chars")
    if "verified erma import" in text or "erma" in text:
        bad.append("aerma_typo")
    if "# PART II - RCC Nexus README" not in text:
        bad.append("missing_rcc_nexus_part")
    if "# PART III - AI Agent README" not in text:
        bad.append("missing_ai_part")
    return {
        "path": path,
        "line_count": len(lines),
        "max_line_length": max((len(line) for line in lines), default=0),
        "status": "pass" if not bad else "warn",
        "findings": bad,
    }

# Repair key Markdown reports.
repair_results = []
for path in [
    "README.md",
    "reports/rcc_nexus/latest_validation_repair_report.md",
    "reports/rcc_nexus/latest_github_public_polish_report.md",
    "reports/rcc_nexus/latest_rcc_nexus_benchmark.md",
    "reports/rcc_nexus/rcc_nexus_scorecard.md",
    "docs/context/drift/latest_rcc_nexus_report.md",
]:
    if (root / path).exists():
        repair_results.append(repair_file(path))

# Pretty print key JSON.
for path in [
    "reports/rcc_nexus/latest_validation_repair_report.json",
    "reports/rcc_nexus/latest_github_public_polish_report.json",
    "reports/rcc_nexus/latest_rcc_nexus_benchmark.json",
    "docs/context/drift/latest_rcc_nexus_report.json",
    "docs/context/rcc_nexus_index.json",
    "rcc/nexus/route_map.json",
]:
    if (root / path).exists():
        save_json(path, load_json(path))

# Patch benchmark script to detect collapsed README/public markdown.
bench_path = root / "scripts/rcc/benchmark_rcc_nexus.py"
if bench_path.exists():
    text = bench_path.read_text(encoding="utf-8-sig")
    old = """def readme_format_health():
    text = read_text(ROOT / 'README.md')
    bad_patterns = ['<!-\\\\n-', '<!-\\\\r\\\\n-', '\\\\n#\\\\n# ', '\\\\n1\\\\n0.', '\\\\n1\\\\n1.', '\\\\n1\\\\n2.', '|\\\\n---\\\\n|']
    failures = [pattern for pattern in bad_patterns if pattern in text]
    required = ['# PART I - Human README', '# PART II - RCC Nexus README', '# PART III - AI Agent README', '<!-- RCC-AI-README:START -->', '<!-- RCC-AI-README:END -->']
    missing = [item for item in required if item not in text]
    score = 1.0
    if failures or missing:
        score = max(0.0, 1.0 - 0.10 * len(failures) - 0.15 * len(missing))
    return score, failures, missing
"""
    new = """def readme_format_health():
    text = read_text(ROOT / 'README.md')
    lines = text.splitlines()
    bad_patterns = ['<!-\\\\n-', '<!-\\\\r\\\\n-', '\\\\n#\\\\n# ', '\\\\n1\\\\n0.', '\\\\n1\\\\n1.', '\\\\n1\\\\n2.', '|\\\\n---\\\\n|', '\\\\x07']
    failures = [pattern for pattern in bad_patterns if pattern in text]
    required = ['# PART I - Human README', '# PART II - RCC Nexus README', '# PART III - AI Agent README', '<!-- RCC-AI-README:START -->', '<!-- RCC-AI-README:END -->']
    missing = [item for item in required if item not in text]
    if len(lines) < 220:
        failures.append('readme_line_count_below_220')
    if any(len(line) > 900 for line in lines):
        failures.append('readme_has_very_long_lines')
    score = 1.0
    if failures or missing:
        score = max(0.0, 1.0 - 0.10 * len(failures) - 0.15 * len(missing))
    return score, failures, missing
"""
    if old in text:
        text = text.replace(old, new)
    elif "readme_line_count_below_220" not in text:
        text = text.replace(
            "    score = 1.0\n    if failures or missing:",
            "    if len(lines) < 220:\n        failures.append('readme_line_count_below_220')\n    if any(len(line) > 900 for line in lines):\n        failures.append('readme_has_very_long_lines')\n    score = 1.0\n    if failures or missing:"
        )
        text = text.replace("    text = read_text(ROOT / 'README.md')\n", "    text = read_text(ROOT / 'README.md')\n    lines = text.splitlines()\n")
    bench_path.write_text(text, encoding="utf-8")
    print("[WRITE] scripts/rcc/benchmark_rcc_nexus.py")

health = {
    "schema": "AERMA-public-markdown-integrity-v1",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "repairs": repair_results,
    "health": [
        markdown_health("README.md", 220),
        markdown_health("reports/rcc_nexus/latest_validation_repair_report.md", 20),
        markdown_health("reports/rcc_nexus/latest_rcc_nexus_benchmark.md", 20),
        markdown_health("reports/rcc_nexus/rcc_nexus_scorecard.md", 10),
    ],
    "claim_boundary": "Markdown integrity improves public readability and agent navigation; it does not prove code correctness, security, patch safety, AI understanding, benchmark validity, or production readiness."
}

write("reports/rcc_nexus/latest_public_markdown_integrity_report.json", json.dumps(health, indent=2, sort_keys=True))

md = [
    "# Public Markdown Integrity Report",
    "",
    f"Timestamp: {health['timestamp']}",
    "",
    "## Health",
    "",
    "| File | Status | Lines | Max line length | Findings |",
    "|---|---|---:|---:|---|",
]

for item in health["health"]:
    md.append(
        f"| `{item['path']}` | {item['status']} | {item['line_count']} | {item['max_line_length']} | {', '.join(item['findings'])} |"
    )

md += [
    "",
    "## Boundary",
    "",
    "Markdown integrity improves public readability and agent navigation. It does not prove code correctness, security, patch safety, AI understanding, benchmark validity, or production readiness.",
]

write("reports/rcc_nexus/latest_public_markdown_integrity_report.md", md)

print("[OK] Public Markdown integrity repair complete.")