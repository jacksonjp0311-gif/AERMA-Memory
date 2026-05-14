from pathlib import Path
import json
from datetime import datetime, timezone

root = Path.cwd()
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

def read(path: str) -> str:
    p = root / path
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8-sig")

def write(path: str, content) -> None:
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, list):
        text = "\n".join(content)
    else:
        text = str(content)
    p.write_text(text.rstrip() + "\n", encoding="utf-8")
    print(f"[WRITE] {path}")

def append_once(path: str, marker: str, block) -> None:
    text = read(path)
    block_text = "\n".join(block) if isinstance(block, list) else str(block)
    if marker in text:
        print(f"[SKIP] {path} already contains marker: {marker}")
        return
    write(path, text.rstrip() + "\n\n" + block_text.strip() + "\n")

def load_json(path: str):
    p = root / path
    return json.loads(p.read_text(encoding="utf-8-sig"))

def save_json(path: str, data) -> None:
    write(path, json.dumps(data, indent=2, sort_keys=True))

# ------------------------------------------------------------
# 1. Fix rcc/nexus meridian in Nexus index.
# Canonical meridians do not include "rcc"; rcc is a sector.
# ------------------------------------------------------------

index_path = "docs/context/rcc_nexus_index.json"
index = load_json(index_path)

for node in index.get("nodes", []):
    if node.get("path") == "rcc/nexus":
        node["meridians"] = ["source", "agent", "safety", "validation", "drift"]
        node["sector"] = "rcc"
        node["last_verified"] = TODAY
        print("[FIX] rcc/nexus meridians set to canonical values")

save_json(index_path, index)

# ------------------------------------------------------------
# 2. Fix rcc/nexus README Echo Location text to remove "rcc"
#    as a meridian while preserving rcc as sector.
# ------------------------------------------------------------

nexus_readme_path = "rcc/nexus/README.md"
nexus_readme = read(nexus_readme_path)
nexus_readme = nexus_readme.replace(
    "- Meridian(s): rcc, agent, safety, validation, drift",
    "- Meridian(s): source, agent, safety, validation, drift"
)
write(nexus_readme_path, nexus_readme)

# ------------------------------------------------------------
# 3. Add root README Echo Location block.
# ------------------------------------------------------------

root_echo = [
    "## RCC Nexus Echo Location",
    "",
    "Sphere Position:",
    "- Shell: center",
    "- Meridian(s): source, agent, safety, release",
    "- Sector: rcc",
    "- Version / TTL: RCC-N-v1.0 / 180 days",
    f"- Last Verified: {TODAY}",
    "",
    "Local Role:",
    "- Root orientation surface for humans, RCC Nexus navigation, and AI agents.",
    "",
    "Inbound Hooks:",
    "- AGENTS.md",
    "- CLAUDE.md",
    "- GitHub repository URL",
    "",
    "Outbound Hooks:",
    "- docs/context/repository_context_index.json",
    "- docs/context/rcc_nexus_index.json",
    "- docs/context/validation_surface.md",
    "- rcc/nexus/route_map.json",
    "- docs/software_architecture/",
    "",
    "Evidence Surface:",
    "- docs/context/drift/latest_rcc_nexus_report.json",
    "- docs/context/drift/latest_rcc_nexus_report.md",
    "- runs/suite_*/aggregate_metrics.json",
    "- evidence_packages/",
    "",
    "Validation Surface:",
    "- pytest -q",
    "- python -m aerma.cli.main run-suite --suite .\\tasks\\suite_v1_2.json",
    "- python scripts/run_aerma_regression_guard.py",
    "- powershell -ExecutionPolicy Bypass -File .\\scripts\\rcc\\check_rcc_drift.ps1",
    "- python scripts/rcc/check_rcc_nexus.py",
    "",
    "Claim Boundary:",
    "- README quality, RCC-N geometry, and NCI do not prove code correctness, security, patch safety, AI understanding, benchmark validity, or production readiness.",
    "",
    "Non-Claim Locks:",
    "- geometry_is_not_ai_internal_proof",
    "- nci_is_not_code_quality_proof",
    "- navigation_is_not_validation",
    "- context_reconstruction_is_not_correctness_proof",
    "- validation_remains_required",
    "",
    "Agent Route:",
    "- Read README.md, docs/context/repository_context_index.json, docs/context/rcc_nexus_index.json, rcc/nexus/route_map.json, then the target folder README before editing.",
    "",
    "Update Obligation:",
    "- Update README, RCC context, Nexus index, and route maps when project identity, validation commands, evidence paths, claim boundaries, or repository geometry changes.",
]

append_once("README.md", "## RCC Nexus Echo Location", root_echo)

# ------------------------------------------------------------
# 4. Update repository_context_index timestamp/status.
# ------------------------------------------------------------

repo_context_path = "docs/context/repository_context_index.json"
repo_context = load_json(repo_context_path)
repo_context.setdefault("rcc_nexus", {})
repo_context["rcc_nexus"]["implementation_status"] = "local_self_mode_active_repaired"
repo_context["rcc_nexus"]["last_repaired"] = datetime.now(timezone.utc).isoformat()
repo_context["rcc_nexus"]["latest_report_json"] = "docs/context/drift/latest_rcc_nexus_report.json"
repo_context["rcc_nexus"]["latest_report_md"] = "docs/context/drift/latest_rcc_nexus_report.md"
save_json(repo_context_path, repo_context)

print("[RCC-N] Repair patch written.")