from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('.').resolve()
REPORT_DIR = ROOT / 'reports' / 'rcc_nexus'
DRIFT_DIR = ROOT / 'docs' / 'context' / 'drift'

def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8-sig', errors='replace')

def load_json(path: Path):
    return json.loads(read_text(path))

def clamp01(value):
    try:
        return max(0.0, min(1.0, float(value)))
    except Exception:
        return 0.0

def compute_nci(index):
    nci = index.get('nci', {})
    weights = nci.get('weights', {})
    components = nci.get('components', {})
    score = 0.0
    for name, weight in weights.items():
        score += float(weight) * clamp01(components.get(name, {}).get('score', 0.0))
    return clamp01(score)

def route_coverage(route_map):
    required = ['read_only_review', 'documentation_change', 'rcc_nexus_change', 'runtime_change', 'benchmark_task_change', 'public_claim_change']
    routes = route_map.get('task_routes', {})
    present = [name for name in required if name in routes]
    return len(present), len(required), len(present) / len(required)

def echo_coverage(index):
    nodes = index.get('nodes', [])
    total = 0
    present = 0
    for node in nodes:
        echo = node.get('echo_location_path', '')
        if not echo or '.json' in echo:
            continue
        total += 1
        file_part = echo.split('#')[0]
        path = ROOT / file_part
        if path.exists() and 'rcc nexus echo location' in read_text(path).lower():
            present += 1
    return present, total, 1.0 if total == 0 else present / total

def coordinate_coverage(index):
    nodes = index.get('nodes', [])
    total = len(nodes)
    present = 0
    for node in nodes:
        if node.get('shell') and node.get('meridians') and node.get('sector') and node.get('last_verified'):
            present += 1
    return present, total, 1.0 if total == 0 else present / total

def non_claim_lock_coverage(index):
    required = ['geometry_is_not_ai_internal_proof', 'nci_is_not_code_quality_proof', 'navigation_is_not_validation', 'context_reconstruction_is_not_correctness_proof', 'validation_remains_required']
    locks = index.get('non_claim_locks', {})
    present = [name for name in required if locks.get(name)]
    return len(present), len(required), len(present) / len(required)

def readme_format_health():
    text = read_text(ROOT / 'README.md')
    lines = text.splitlines()
    bad_patterns = ['<!-\\n-', '<!-\\r\\n-', '\\n#\\n# ', '\\n1\\n0.', '\\n1\\n1.', '\\n1\\n2.', '|\\n---\\n|', '\\x07']
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

def latest_nexus_status():
    path = DRIFT_DIR / 'latest_rcc_nexus_report.json'
    if not path.exists():
        return 'missing', None, None
    data = load_json(path)
    return data.get('status'), data.get('computed_nci'), len(data.get('findings', []))

def write_report(payload):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / 'latest_rcc_nexus_benchmark.json').write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    history_path = REPORT_DIR / 'rcc_nexus_metrics_history.jsonl'
    with history_path.open('a', encoding='utf-8') as f:
        f.write(json.dumps(payload, sort_keys=True) + '\n')

    lines = [
        '# RCC-N Benchmark Report',
        '',
        f"Timestamp: {payload['timestamp']}",
        '',
        f"Status: {payload['status']}",
        '',
        f"Computed NCI: {payload['nci']}",
        '',
        '## Metrics',
        '',
        '| Metric | Value |',
        '|---|---:|',
    ]
    for name, value in payload['metrics'].items():
        if isinstance(value, float):
            lines.append(f'| {name} | {value:.3f} |')
        else:
            lines.append(f'| {name} | {value} |')
    lines += [
        '',
        '## Boundary',
        '',
        'RCC-N benchmark reports measure repository navigation/context integrity. They do not prove code correctness, security, patch safety, AI understanding, benchmark validity, or production readiness.',
    ]
    (REPORT_DIR / 'latest_rcc_nexus_benchmark.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

    scorecard = [
        '# RCC-N Scorecard',
        '',
        f"Status: {payload['status']}",
        '',
        f"NCI: {payload['nci']}",
        '',
        f"Echo coverage: {payload['metrics']['echo_location_coverage']:.3f}",
        '',
        f"Route coverage: {payload['metrics']['route_coverage']:.3f}",
        '',
        f"Coordinate coverage: {payload['metrics']['coordinate_coverage']:.3f}",
        '',
        f"README format health: {payload['metrics']['readme_format_health']:.3f}",
        '',
        'Boundary: scorecard is diagnostic only, not correctness proof.',
    ]
    (REPORT_DIR / 'rcc_nexus_scorecard.md').write_text('\n'.join(scorecard) + '\n', encoding='utf-8')

def main():
    index = load_json(ROOT / 'docs' / 'context' / 'rcc_nexus_index.json')
    route_map = load_json(ROOT / 'rcc' / 'nexus' / 'route_map.json')
    nci = compute_nci(index)
    routes_present, routes_total, routes_score = route_coverage(route_map)
    echo_present, echo_total, echo_score = echo_coverage(index)
    coord_present, coord_total, coord_score = coordinate_coverage(index)
    locks_present, locks_total, locks_score = non_claim_lock_coverage(index)
    readme_score, readme_failures, readme_missing = readme_format_health()
    nexus_status, report_nci, finding_count = latest_nexus_status()
    metrics = {
        'node_count': len(index.get('nodes', [])),
        'route_count': routes_present,
        'route_required_count': routes_total,
        'route_coverage': routes_score,
        'echo_location_present': echo_present,
        'echo_location_required': echo_total,
        'echo_location_coverage': echo_score,
        'coordinate_present': coord_present,
        'coordinate_total': coord_total,
        'coordinate_coverage': coord_score,
        'non_claim_locks_present': locks_present,
        'non_claim_locks_total': locks_total,
        'non_claim_lock_coverage': locks_score,
        'readme_format_health': readme_score,
        'rcc_nexus_finding_count': finding_count if finding_count is not None else -1,
    }
    status = 'pass'
    if nexus_status != 'pass' or readme_score < 1.0 or nci < 0.90:
        status = 'warn'
    if routes_score < 1.0 or coord_score < 1.0 or locks_score < 1.0:
        status = 'fail'
    payload = {
        'schema': 'AERMA-RCC-N-benchmark-v1',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'status': status,
        'nci': nci,
        'nci_mode': index.get('nci', {}).get('mode'),
        'nci_components': index.get('nci', {}).get('components', {}),
        'latest_nexus_checker_status': nexus_status,
        'latest_nexus_checker_nci': report_nci,
        'metrics': metrics,
        'readme_format_failures': readme_failures,
        'readme_missing_items': readme_missing,
        'claim_boundary': 'RCC-N benchmark reports are navigation/context diagnostics, not correctness proof.'
    }
    write_report(payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if status in {'pass', 'warn'} else 1

if __name__ == '__main__':
    raise SystemExit(main())
