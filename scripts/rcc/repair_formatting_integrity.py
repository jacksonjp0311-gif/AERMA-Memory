from pathlib import Path
import json
import re
import subprocess
import sys
from datetime import datetime, timezone

root = Path.cwd()

targets = [
    "README.md",
    "docs/software_architecture/README.md",
    "docs/software_architecture/aerma_rcc_echo_location_architecture_v0_1_2.md",
    "docs/context/module_index.md",
    "docs/context/validation_surface.md",
    "docs/context/drift_report.md"
]

json_targets = [
    "docs/context/repository_context_index.json"
]

minimum_line_counts = {
    "README.md": 180,
    "docs/software_architecture/README.md": 25,
    "docs/software_architecture/aerma_rcc_echo_location_architecture_v0_1_2.md": 120,
    "docs/context/module_index.md": 25,
    "docs/context/validation_surface.md": 30,
    "docs/context/drift_report.md": 25,
    "docs/context/repository_context_index.json": 20
}

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")

def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")
    print(f"[WRITE] {path.as_posix()}")

def count_lines(path: Path) -> int:
    if not path.exists():
        return 0
    text = read_text(path)
    return len(text.splitlines())

def normalize_basic(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\ufeff", "")
    return text

def repair_collapsed_markdown(text: str) -> str:
    text = normalize_basic(text)

    # Convert literal escaped newlines if a writer accidentally serialized them.
    if "\\n" in text and text.count("\n") < 20:
        text = text.replace("\\r\\n", "\n")
        text = text.replace("\\n", "\n")

    # Place headings on their own lines.
    text = re.sub(r"(?<!\n)(#{1,6}\s+)", r"\n\1", text)

    # Place RCC/HTML markers on their own lines.
    text = re.sub(r"(?<!\n)(<!--\s*[^>]+-->)", r"\n\1\n", text)

    # Place horizontal rules on their own lines.
    text = re.sub(r"(?<!\n)(---)(?!-)", r"\n\1\n", text)

    # Place common list starts on their own lines when collapsed.
    text = re.sub(r"(?<!\n)(- `)", r"\n\1", text)
    text = re.sub(r"(?<!\n)(- [A-Z][A-Za-z0-9 /_-]{1,80}:)", r"\n\1", text)
    text = re.sub(r"(?<!\n)([0-9]+\. [A-Z])", r"\n\1", text)

    # Place table header rows on their own lines when collapsed.
    text = re.sub(r"(?<!\n)(\|[^|\n]+\|[^|\n]*\|)", r"\n\1", text)

    # Clean up known phrase joins that should start paragraphs.
    starters = [
        "Current repository context:",
        "Primary source files:",
        "Primary docs and RCC files:",
        "Primary scripts:",
        "Any AI agent reading or modifying this repository must follow this order:",
        "Never claim or imply:",
        "After documentation-only RCC changes, run:",
        "After README/RCC synchronization changes, run:",
        "After source, scoring, benchmark, task, or evidence changes, run:",
        "When changing any of the following, update the root README and RCC context:",
        "Priority order:",
        "The intended RCC Echo structure is:",
        "The first real checker must validate:",
        "Expected reports:",
        "Portable components:",
        "Repo-specific components:",
        "AERMA-RCC-ECHO is weakened or rejected if:"
    ]

    for phrase in starters:
        text = text.replace(" " + phrase, "\n\n" + phrase)

    # Add blank line after headings when missing.
    text = re.sub(r"\n(#{1,6} [^\n]+)\n(?!\n)", r"\n\1\n\n", text)

    # Normalize too many blank lines.
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    return text.strip() + "\n"

def pretty_json(path: Path) -> None:
    data = json.loads(read_text(path))
    text = json.dumps(data, indent=2, sort_keys=True)
    write_text(path, text)

def run_existing_root_readme_repair() -> None:
    script = root / "scripts" / "rcc" / "repair_root_readme_format.py"
    if script.exists():
        print("[RUN] Existing root README repair generator")
        subprocess.run([sys.executable, str(script)], cwd=root, check=True)
    else:
        print("[SKIP] Existing root README repair generator not found")

def repair_markdown_files() -> dict:
    results = {}

    for rel in targets:
        path = root / rel
        if not path.exists():
            results[rel] = {
                "exists": False,
                "before_lines": 0,
                "after_lines": 0,
                "status": "missing"
            }
            print(f"[MISSING] {rel}")
            continue

        before = count_lines(path)
        text = read_text(path)
        repaired = repair_collapsed_markdown(text)
        write_text(path, repaired)
        after = count_lines(path)

        minimum = minimum_line_counts.get(rel, 1)
        status = "pass" if after >= minimum else "warn"

        results[rel] = {
            "exists": True,
            "before_lines": before,
            "after_lines": after,
            "minimum_expected_lines": minimum,
            "status": status
        }

        print(f"[FORMAT] {rel}: {before} -> {after} lines ({status})")

    return results

def repair_json_files() -> dict:
    results = {}

    for rel in json_targets:
        path = root / rel
        if not path.exists():
            results[rel] = {
                "exists": False,
                "before_lines": 0,
                "after_lines": 0,
                "status": "missing"
            }
            print(f"[MISSING] {rel}")
            continue

        before = count_lines(path)
        pretty_json(path)
        after = count_lines(path)
        minimum = minimum_line_counts.get(rel, 1)
        status = "pass" if after >= minimum else "warn"

        results[rel] = {
            "exists": True,
            "before_lines": before,
            "after_lines": after,
            "minimum_expected_lines": minimum,
            "status": status
        }

        print(f"[JSON] {rel}: {before} -> {after} lines ({status})")

    return results

def write_format_report(markdown_results: dict, json_results: dict) -> None:
    all_results = {}
    all_results.update(markdown_results)
    all_results.update(json_results)

    warnings = {
        rel: result
        for rel, result in all_results.items()
        if result.get("status") != "pass"
    }

    status = "PASS" if not warnings else "WARN"

    report = {
        "schema": "AERMA-formatting-integrity-report-v1",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "checked_files": all_results,
        "warnings": warnings,
        "claim_boundary": "Formatting integrity improves readability and agent navigation; it does not prove runtime correctness."
    }

    json_path = root / "docs" / "context" / "drift" / "latest_formatting_integrity_report.json"
    md_path = root / "docs" / "context" / "drift" / "latest_formatting_integrity_report.md"

    write_text(json_path, json.dumps(report, indent=2, sort_keys=True))

    md_lines = [
        "# Formatting Integrity Report",
        "",
        f"Status: {status}",
        "",
        f"Timestamp: {report['timestamp']}",
        "",
        "## Checked Files",
        "",
        "| File | Before lines | After lines | Minimum | Status |",
        "|---|---:|---:|---:|---|"
    ]

    for rel, result in all_results.items():
        md_lines.append(
            f"| `{rel}` | {result.get('before_lines', 0)} | {result.get('after_lines', 0)} | {result.get('minimum_expected_lines', 0)} | {result.get('status', 'unknown')} |"
        )

    md_lines.extend([
        "",
        "## Boundary",
        "",
        "Formatting integrity improves readability and agent navigation. It does not prove runtime correctness, RCC correctness, benchmark validity, or production readiness.",
        ""
    ])

    write_text(md_path, "\n".join(md_lines))

def main() -> None:
    run_existing_root_readme_repair()
    markdown_results = repair_markdown_files()
    json_results = repair_json_files()
    write_format_report(markdown_results, json_results)

    failed = []
    for rel, result in {**markdown_results, **json_results}.items():
        if not result.get("exists"):
            failed.append(rel)

    if failed:
        raise SystemExit(f"Missing formatting target files: {failed}")

    print("[FORMAT] Formatting integrity repair complete.")

if __name__ == "__main__":
    main()