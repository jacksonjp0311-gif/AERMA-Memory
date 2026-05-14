from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

VALID_SHELLS = {'center', 'inner', 'middle', 'outer'}
VALID_MERIDIANS = {'source', 'validation', 'evidence', 'drift', 'agent', 'safety', 'runtime', 'memory', 'release', 'federation'}
REQUIRED_LOCKS = {
    'geometry_is_not_ai_internal_proof',
    'nci_is_not_code_quality_proof',
    'navigation_is_not_validation',
    'context_reconstruction_is_not_correctness_proof',
    'validation_remains_required',
}
NCI_WEIGHTS = {
    'completeness': 0.15,
    'link_correctness': 0.15,
    'pattern_rigidity': 0.10,
    'invariant_compliance': 0.20,
    'evidence_validation_linkage': 0.15,
    'drift_freshness': 0.10,
    'coordinate_completeness': 0.15,
}

@dataclass
class Finding:
    code: str
    message: str
    severity: str = 'warning'
    path: Optional[str] = None

def clamp01(value: Any) -> float:
    try:
        return max(0.0, min(1.0, float(value)))
    except Exception:
        return 0.0

def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8-sig', errors='replace')

def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(read_text(path))

def check_readme(root: Path) -> List[Finding]:
    findings = []
    path = root / 'README.md'
    if not path.exists():
        return [Finding('RCCN001', 'README.md missing', 'error', str(path))]
    text = read_text(path).lower()
    required = ['part i - human readme', 'part ii - rcc nexus readme', 'part iii - ai agent readme']
    for item in required:
        if item not in text:
            findings.append(Finding('RCCN001', f'Missing README trisection layer: {item}', 'error', 'README.md'))
    return findings

def check_index(root: Path) -> tuple[List[Finding], Dict[str, Any]]:
    findings = []
    path = root / 'docs' / 'context' / 'rcc_nexus_index.json'
    if not path.exists():
        return [Finding('RCCN002', 'Missing docs/context/rcc_nexus_index.json', 'error', str(path))], {}
    try:
        data = load_json(path)
    except Exception as exc:
        return [Finding('RCCN002', f'Invalid rcc_nexus_index.json: {exc}', 'error', str(path))], {}
    for node in data.get('nodes', []):
        node_path = node.get('path', '<unknown>')
        if node.get('shell') not in VALID_SHELLS:
            findings.append(Finding('RCCN004', f'Invalid or missing shell for {node_path}', 'error', node_path))
        meridians = set(node.get('meridians', []))
        if not meridians or not meridians.issubset(VALID_MERIDIANS):
            findings.append(Finding('RCCN005', f'Invalid or missing meridians for {node_path}', 'error', node_path))
        if not node.get('sector'):
            findings.append(Finding('RCCN006', f'Missing sector for {node_path}', 'error', node_path))
        if not node.get('echo_location_path'):
            findings.append(Finding('RCCN003', f'Missing Echo Location path for {node_path}', 'warning', node_path))
    locks = data.get('non_claim_locks', {})
    for lock in REQUIRED_LOCKS:
        if not locks.get(lock):
            findings.append(Finding('RCCN010', f'Missing non-claim lock: {lock}', 'error', 'docs/context/rcc_nexus_index.json'))
    return findings, data

def compute_nci(data: Dict[str, Any]) -> Optional[float]:
    nci = data.get('nci', {})
    weights = nci.get('weights', {})
    components = nci.get('components', {})
    if set(weights) != set(NCI_WEIGHTS):
        return None
    total = 0.0
    for key, weight in weights.items():
        total += float(weight) * clamp01(components.get(key, {}).get('score'))
    return clamp01(total)

def check_nci(data: Dict[str, Any]) -> List[Finding]:
    findings = []
    nci = data.get('nci', {})
    if nci.get('mode') not in {'self', 'linted', 'verified'}:
        findings.append(Finding('RCCN015', 'NCI mode must be self, linted, or verified', 'error', 'docs/context/rcc_nexus_index.json'))
    if set(nci.get('weights', {})) != set(NCI_WEIGHTS):
        findings.append(Finding('RCCN015', 'NCI weights missing required components', 'error', 'docs/context/rcc_nexus_index.json'))
    for key in NCI_WEIGHTS:
        comp = nci.get('components', {}).get(key)
        if not comp or 'score' not in comp or 'algorithm' not in comp:
            findings.append(Finding('RCCN015', f'Incomplete NCI component: {key}', 'error', 'docs/context/rcc_nexus_index.json'))
    return findings

def check_route_map(root: Path) -> List[Finding]:
    path = root / 'rcc' / 'nexus' / 'route_map.json'
    if not path.exists():
        return [Finding('RCCN012', 'Missing rcc/nexus/route_map.json', 'error', str(path))]
    try:
        data = load_json(path)
    except Exception as exc:
        return [Finding('RCCN012', f'Invalid route_map.json: {exc}', 'error', str(path))]
    required = ['read_only_review', 'documentation_change', 'rcc_nexus_change', 'runtime_change', 'benchmark_task_change', 'public_claim_change']
    routes = data.get('task_routes', {})
    return [Finding('RCCN012', f'Missing route: {r}', 'error', str(path)) for r in required if r not in routes]

def check_echo_blocks(root: Path, data: Dict[str, Any]) -> List[Finding]:
    findings = []
    for node in data.get('nodes', []):
        echo = node.get('echo_location_path', '')
        if not echo or '.json' in echo:
            continue
        file_part = echo.split('#')[0]
        path = root / file_part
        if path.exists():
            text = read_text(path).lower()
            if 'rcc nexus echo location' not in text:
                findings.append(Finding('RCCN003', f'Echo Location block missing in {file_part}', 'warning', file_part))
        else:
            findings.append(Finding('RCCN003', f'Echo Location file missing: {file_part}', 'warning', file_part))
    return findings

def write_reports(root: Path, payload: Dict[str, Any]) -> None:
    report_dir = root / 'docs' / 'context' / 'drift'
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / 'latest_rcc_nexus_report.json').write_text(json.dumps(payload, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    lines = [
        '# RCC Nexus Report',
        '',
        f"Status: {payload['status']}",
        '',
        f"Computed NCI: {payload.get('computed_nci')}",
        '',
        f"Timestamp: {payload['timestamp']}",
        '',
        '## Findings',
        '',
    ]
    if payload['findings']:
        lines += ['| Code | Severity | Path | Message |', '|---|---|---|---|']
        for f in payload['findings']:
            lines.append(f"| {f['code']} | {f['severity']} | {f.get('path') or ''} | {f['message']} |")
    else:
        lines.append('No findings.')
    lines += ['', '## Boundary', '', 'RCC Nexus improves navigation and context integrity. It does not prove code correctness, security, patch safety, AI understanding, benchmark validity, or production readiness.']
    (report_dir / 'latest_rcc_nexus_report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

def main() -> int:
    root = Path('.').resolve()
    findings = []
    findings.extend(check_readme(root))
    index_findings, data = check_index(root)
    findings.extend(index_findings)
    if data:
        findings.extend(check_nci(data))
        findings.extend(check_echo_blocks(root, data))
    findings.extend(check_route_map(root))
    computed_nci = compute_nci(data) if data else None
    status = 'pass'
    if any(f.severity == 'error' for f in findings):
        status = 'fail'
    elif findings:
        status = 'warn'
    payload = {
        'schema': 'RCC-N-v1.0-check-result',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'status': status,
        'computed_nci': computed_nci,
        'findings': [f.__dict__ for f in findings],
        'non_claim_locks': {lock: True for lock in sorted(REQUIRED_LOCKS)},
        'claim_boundary': 'RCC Nexus is context/navigation integrity only, not code correctness proof.'
    }
    write_reports(root, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if status == 'fail' else 0

if __name__ == '__main__':
    raise SystemExit(main())
