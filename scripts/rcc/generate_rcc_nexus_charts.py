from __future__ import annotations

import json
from pathlib import Path

ROOT = Path('.').resolve()
REPORT = ROOT / 'reports' / 'rcc_nexus' / 'latest_rcc_nexus_benchmark.json'
HISTORY = ROOT / 'reports' / 'rcc_nexus' / 'rcc_nexus_metrics_history.jsonl'
OUT = ROOT / 'visuals' / 'rcc_nexus'

def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def svg_bar_chart(title, labels, values, path, width=900, height=420):
    OUT.mkdir(parents=True, exist_ok=True)
    maxv = max(values) if values else 1.0
    maxv = max(maxv, 1.0)
    margin_left = 220
    margin_top = 60
    bar_h = 28
    gap = 18
    chart_w = width - margin_left - 80
    rows = []
    rows.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    rows.append('<rect width="100%" height="100%" fill="white"/>')
    rows.append(f'<text x="30" y="35" font-size="24" font-family="Arial" font-weight="bold">{title}</text>')
    for i, (label, value) in enumerate(zip(labels, values)):
        y = margin_top + i * (bar_h + gap)
        bw = int(chart_w * (value / maxv))
        rows.append(f'<text x="30" y="{y + 20}" font-size="14" font-family="Arial">{label}</text>')
        rows.append(f'<rect x="{margin_left}" y="{y}" width="{bw}" height="{bar_h}" fill="#4f6bed"/>')
        rows.append(f'<text x="{margin_left + bw + 10}" y="{y + 20}" font-size="14" font-family="Arial">{value:.3f}</text>')
    rows.append('<text x="30" y="390" font-size="12" font-family="Arial" fill="#555">Boundary: RCC-N charts are diagnostics, not code correctness proof.</text>')
    rows.append('</svg>')
    path.write_text('\n'.join(rows) + '\n', encoding='utf-8')
    print(f'[WRITE] {path.as_posix()}')

def svg_trend(title, values, path, width=900, height=360):
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    rows.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    rows.append('<rect width="100%" height="100%" fill="white"/>')
    rows.append(f'<text x="30" y="35" font-size="24" font-family="Arial" font-weight="bold">{title}</text>')
    x0, y0, w, h = 70, 70, 760, 220
    rows.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="none" stroke="#333"/>')
    if not values:
        values = [0.0]
    pts = []
    n = max(1, len(values) - 1)
    for i, v in enumerate(values):
        x = x0 + (w * i / n if n else 0)
        y = y0 + h - (h * max(0.0, min(1.0, float(v))))
        pts.append((x, y))
    poly = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    rows.append(f'<polyline points="{poly}" fill="none" stroke="#4f6bed" stroke-width="3"/>')
    for x, y in pts:
        rows.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#4f6bed"/>')
    rows.append('<text x="70" y="320" font-size="12" font-family="Arial" fill="#555">Boundary: trend is report-history only, not validation proof.</text>')
    rows.append('</svg>')
    path.write_text('\n'.join(rows) + '\n', encoding='utf-8')
    print(f'[WRITE] {path.as_posix()}')

def main():
    data = load_json(REPORT)
    comps = data.get('nci_components', {})
    labels = list(comps.keys())
    values = [float(comps[k].get('score', 0.0)) for k in labels]
    svg_bar_chart('RCC-N NCI Components', labels, values, OUT / 'nci_components.svg', height=max(420, 90 + len(labels) * 46))
    metrics = data.get('metrics', {})
    cov_labels = ['route coverage', 'echo coverage', 'coordinate coverage', 'lock coverage', 'README format']
    cov_values = [
        float(metrics.get('route_coverage', 0.0)),
        float(metrics.get('echo_location_coverage', 0.0)),
        float(metrics.get('coordinate_coverage', 0.0)),
        float(metrics.get('non_claim_lock_coverage', 0.0)),
        float(metrics.get('readme_format_health', 0.0)),
    ]
    svg_bar_chart('RCC-N Coverage Surfaces', cov_labels, cov_values, OUT / 'rcc_nexus_coverage_chart.svg')
    trend = []
    if HISTORY.exists():
        for line in HISTORY.read_text(encoding='utf-8-sig').splitlines():
            if line.strip():
                try:
                    trend.append(float(json.loads(line).get('nci', 0.0)))
                except Exception:
                    pass
    svg_trend('RCC-N Health Trend', trend, OUT / 'rcc_nexus_health_trend.svg')
    surface_labels = ['nodes', 'routes', 'echo records', 'locks']
    surface_values = [
        float(metrics.get('node_count', 0.0)),
        float(metrics.get('route_count', 0.0)),
        float(metrics.get('echo_location_present', 0.0)),
        float(metrics.get('non_claim_locks_present', 0.0)),
    ]
    maxv = max(surface_values) if surface_values else 1.0
    norm = [v / maxv for v in surface_values]
    svg_bar_chart('RCC-N Surface Map', surface_labels, norm, OUT / 'rcc_nexus_surface_map.svg')

if __name__ == '__main__':
    main()
