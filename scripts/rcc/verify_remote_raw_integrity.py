from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('.').resolve()
REPO = 'jacksonjp0311-gif/AERMA-Memory'
BRANCH = 'main'
BASE = f'https://raw.githubusercontent.com/{REPO}/{BRANCH}'

TARGETS = [
    {
        'name': 'README',
        'path': 'README.md',
        'min_lines': 220,
        'required': [
            'Repository Description',
            'Project Structure Director',
            'PART II - RCC Nexus README',
            'PART III - AI Agent README',
            'reports/rcc_nexus/latest_rcc_nexus_benchmark.md',
            'visuals/rcc_nexus/nci_components.svg',
        ],
    },
    {
        'name': 'Repo description doc',
        'path': 'docs/context/repo_description.md',
        'min_lines': 20,
        'required': ['Suggested GitHub About Description', 'Suggested Topics', 'Non-Claim Boundary'],
    },
    {
        'name': 'RCC-N benchmark report',
        'path': 'reports/rcc_nexus/latest_rcc_nexus_benchmark.md',
        'min_lines': 20,
        'required': ['RCC-N Benchmark Report', 'Status: pass', 'Computed NCI: 0.96', 'readme_format_health'],
    },
    {
        'name': 'NCI chart',
        'path': 'visuals/rcc_nexus/nci_components.svg',
        'min_lines': 5,
        'required': ['<svg', 'RCC-N NCI Components'],
    },
]

def fetch_text(path: str) -> str:
    url = f'{BASE}/{path}?cacheBust={datetime.now(timezone.utc).timestamp()}'
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read().decode('utf-8', errors='replace')

def check_target(target: dict) -> dict:
    try:
        text = fetch_text(target['path'])
    except Exception as exc:
        return {
            'name': target['name'],
            'path': target['path'],
            'status': 'fail',
            'line_count': 0,
            'max_line_length': 0,
            'missing': ['fetch_failed'],
            'error': str(exc),
        }

    lines = text.splitlines()
    missing = [item for item in target['required'] if item not in text]

    if len(lines) < int(target['min_lines']):
        missing.append('line_count_below_minimum')

    if any(len(line) > 1200 for line in lines):
        missing.append('very_long_line_over_1200')

    if '\x07' in text:
        missing.append('control_char_bell')

    return {
        'name': target['name'],
        'path': target['path'],
        'status': 'pass' if not missing else 'warn',
        'line_count': len(lines),
        'max_line_length': max((len(line) for line in lines), default=0),
        'missing': missing,
    }

def write_reports(payload: dict) -> None:
    out = ROOT / 'reports' / 'rcc_nexus'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'latest_remote_raw_integrity_report.json').write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n', encoding='utf-8')

    md = [
        '# Remote Raw Integrity Report',
        '',
        f"Timestamp: {payload['timestamp']}",
        '',
        f"Status: {payload['status']}",
        '',
        '## Targets',
        '',
        '| Target | Status | Lines | Max line length | Findings |',
        '|---|---|---:|---:|---|',
    ]

    for item in payload['targets']:
        md.append(f"| {item['name']} | {item['status']} | {item['line_count']} | {item['max_line_length']} | {', '.join(item['missing'])} |")

    md += [
        '',
        '## Boundary',
        '',
        'Remote raw integrity verifies public parseability after push. It does not prove code correctness, security, patch safety, AI understanding, benchmark validity, or production readiness.',
    ]

    (out / 'latest_remote_raw_integrity_report.md').write_text('\n'.join(md) + '\n', encoding='utf-8')

def main() -> int:
    results = [check_target(target) for target in TARGETS]
    status = 'pass'
    if any(item['status'] == 'fail' for item in results):
        status = 'fail'
    elif any(item['status'] == 'warn' for item in results):
        status = 'warn'

    payload = {
        'schema': 'AERMA-remote-raw-integrity-v1',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'repo': REPO,
        'branch': BRANCH,
        'status': status,
        'targets': results,
        'claim_boundary': 'Remote raw integrity verifies public parseability after push; it does not prove runtime correctness.',
    }

    write_reports(payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if status in {'pass', 'warn'} else 1

if __name__ == '__main__':
    raise SystemExit(main())
