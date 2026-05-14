from pathlib import Path
import json
import re
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

def normalize_safe(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\ufeff", "")
    text = text.replace("\x07erma", "aerma")
    text = text.replace("verified \x07erma import", "verified aerma import")
    text = text.replace("verified `\x07erma` import", "verified `aerma` import")
    text = text.replace("verified `erma` import", "verified `aerma` import")
    text = text.replace("verified erma import", "verified aerma import")
    return text

def ensure_blank_before_heading(text: str, heading: str) -> str:
    text = text.replace(" " + heading, "\n\n" + heading)
    text = text.replace("\n" + heading, "\n" + heading)
    return text

def canonicalize_readme() -> None:
    path = "README.md"
    text = normalize_safe(read(path))

    # Normalize malformed variants that may have drifted.
    variants = [
        "PART II - RCC Nexus README",
        "Part II - RCC Nexus README",
        "part ii - rcc nexus readme",
        "## PART II - RCC Nexus README",
        "### PART II - RCC Nexus README",
    ]

    # Remove duplicate noncanonical heading-only variants.
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        stripped = line.strip()
        low = stripped.lower().lstrip("#").strip()
        if low == "part ii - rcc nexus readme":
            continue
        cleaned.append(line)
    text = "\n".join(cleaned).strip() + "\n"

    # Insert exact PART II heading before RCC Nexus Identity if missing.
    if "# PART II - RCC Nexus README" not in text:
        if "## RCC Nexus Identity" in text:
            text = text.replace("## RCC Nexus Identity", "# PART II - RCC Nexus README\n\n## RCC Nexus Identity", 1)
        elif "# PART III - AI Agent README" in text:
            minimal = [
                "# PART II - RCC Nexus README",
                "",
                "## RCC Nexus Identity",
                "",
                "AERMA-Memory includes a local RCC Nexus layer based on RCC-N v1.0.",
                "",
                "RCC tells the agent what the repository means.",
                "",
                "RCC-N tells the agent where it is.",
                "",
                "Validation tells the agent whether reality agreed.",
                "",
                "## RCC Nexus Non-Claim Lock",
                "",
                "RCC-N improves navigation, traceability, maintenance discipline, and agent self-location. It does not prove code correctness, security, AI understanding, patch safety, production readiness, benchmark validity, or runtime truth.",
                "",
            ]
            text = text.replace("# PART III - AI Agent README", "\n".join(minimal) + "\n# PART III - AI Agent README", 1)
        else:
            text = text.rstrip() + "\n\n# PART II - RCC Nexus README\n\n## RCC Nexus Identity\n\nAERMA-Memory includes a local RCC Nexus layer based on RCC-N v1.0.\n"

    # Ensure PART III exact heading before AI section.
    if "# PART III - AI Agent README" not in text:
        if "## AI Version Tracking Contract" in text:
            text = text.replace("## AI Version Tracking Contract", "# PART III - AI Agent README\n\n## AI Version Tracking Contract", 1)
        else:
            text = text.rstrip() + "\n\n# PART III - AI Agent README\n\n## AI Version Tracking Contract\n"

    # Ensure PART I exact heading.
    if "# PART I - Human README" not in text:
        if "## Current Identity" in text:
            text = text.replace("## Current Identity", "# PART I - Human README\n\n## Current Identity", 1)

    # Force correct order if PART II accidentally appears after PART III.
    p1 = text.find("# PART I - Human README")
    p2 = text.find("# PART II - RCC Nexus README")
    p3 = text.find("# PART III - AI Agent README")

    if p2 != -1 and p3 != -1 and p2 > p3:
        part2 = text[p2:p3] if p3 > p2 else ""
        # Safer fallback: leave in place and checker will catch. Avoid destructive reordering.
        pass

    # Add clean spacing around exact major headings.
    for heading in [
        "# PART I - Human README",
        "# PART II - RCC Nexus README",
        "# PART III - AI Agent README",
        "## Human Director Box",
        "## RCC Nexus Identity",
        "## AI Version Tracking Contract",
    ]:
        text = ensure_blank_before_heading(text, heading)

    # Collapse excessive blanks only.
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    write(path, text)

def patch_repair_script() -> None:
    path = root / "scripts" / "rcc" / "repair_public_markdown_integrity.py"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8-sig", errors="replace")

    unsafe_lines = [
        '    text = text.replace("erma", "aerma")\n',
        '    text = text.replace("verified erma import", "verified aerma import")\n',
    ]

    for line in unsafe_lines:
        text = text.replace(line, "")

    text = text.replace(
        '    if "verified erma import" in text or "erma" in text:\n        bad.append("aerma_typo")\n',
        '    if "\\x07" in text or "verified erma import" in text or "verified `erma` import" in text:\n        bad.append("aerma_typo")\n'
    )

    path.write_text(text, encoding="utf-8")
    print("[WRITE] scripts/rcc/repair_public_markdown_integrity.py")

def patch_benchmark_script() -> None:
    path = root / "scripts" / "rcc" / "benchmark_rcc_nexus.py"
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8-sig", errors="replace")

    start = text.find("def readme_format_health():")
    if start == -1:
        return

    next_def = text.find("\ndef ", start + 1)
    if next_def == -1:
        next_def = len(text)

    new_func = '''def readme_format_health():
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
'''

    text = text[:start] + new_func + text[next_def:]
    path.write_text(text, encoding="utf-8")
    print("[WRITE] scripts/rcc/benchmark_rcc_nexus.py")

def write_markdown_integrity_report() -> None:
    def health_readme() -> dict:
        text = read("README.md")
        lines = text.splitlines()
        findings = []
        for required in [
            "# PART I - Human README",
            "# PART II - RCC Nexus README",
            "# PART III - AI Agent README",
            "<!-- RCC-AI-README:START -->",
            "<!-- RCC-AI-README:END -->",
        ]:
            if required not in text:
                findings.append("missing:" + required)
        if "\x07" in text:
            findings.append("control_char_bell")
        if len(lines) < 220:
            findings.append("line_count_below_220")
        if any(len(line) > 900 for line in lines):
            findings.append("very_long_line_over_900")
        return {
            "path": "README.md",
            "status": "pass" if not findings else "warn",
            "line_count": len(lines),
            "max_line_length": max((len(line) for line in lines), default=0),
            "findings": findings,
        }

    def health_report(path: str, min_lines: int) -> dict:
        text = read(path)
        lines = text.splitlines()
        findings = []
        if "\x07" in text:
            findings.append("control_char_bell")
        if len(lines) < min_lines:
            findings.append("line_count_below_minimum")
        if any(len(line) > 900 for line in lines):
            findings.append("very_long_line_over_900")
        return {
            "path": path,
            "status": "pass" if not findings else "warn",
            "line_count": len(lines),
            "max_line_length": max((len(line) for line in lines), default=0),
            "findings": findings,
        }

    payload = {
        "schema": "AERMA-public-markdown-integrity-v2",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "health": [
            health_readme(),
            health_report("reports/rcc_nexus/latest_validation_repair_report.md", 15),
            health_report("reports/rcc_nexus/latest_rcc_nexus_benchmark.md", 15),
            health_report("reports/rcc_nexus/rcc_nexus_scorecard.md", 10),
        ],
        "claim_boundary": "Markdown integrity improves public readability and agent navigation; it does not prove code correctness, security, patch safety, AI understanding, benchmark validity, or production readiness.",
    }

    write("reports/rcc_nexus/latest_public_markdown_integrity_report.json", json.dumps(payload, indent=2, sort_keys=True))

    md = [
        "# Public Markdown Integrity Report",
        "",
        f"Timestamp: {payload['timestamp']}",
        "",
        "## Health",
        "",
        "| File | Status | Lines | Max line length | Findings |",
        "|---|---|---:|---:|---|",
    ]

    for item in payload["health"]:
        md.append(f"| `{item['path']}` | {item['status']} | {item['line_count']} | {item['max_line_length']} | {', '.join(item['findings'])} |")

    md += [
        "",
        "## Boundary",
        "",
        "Markdown integrity improves public readability and agent navigation. It does not prove code correctness, security, patch safety, AI understanding, benchmark validity, or production readiness.",
    ]

    write("reports/rcc_nexus/latest_public_markdown_integrity_report.md", md)

def pretty_print_jsons() -> None:
    for path in [
        "reports/rcc_nexus/latest_validation_repair_report.json",
        "reports/rcc_nexus/latest_github_public_polish_report.json",
        "reports/rcc_nexus/latest_rcc_nexus_benchmark.json",
        "reports/rcc_nexus/latest_public_markdown_integrity_report.json",
        "docs/context/drift/latest_rcc_nexus_report.json",
        "docs/context/rcc_nexus_index.json",
        "rcc/nexus/route_map.json",
    ]:
        if (root / path).exists():
            save_json(path, load_json(path))

canonicalize_readme()
patch_repair_script()
patch_benchmark_script()
write_markdown_integrity_report()
pretty_print_jsons()

print("[OK] RCC-N trisection integrity patch written.")