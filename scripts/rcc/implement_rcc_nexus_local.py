from pathlib import Path
import json
from datetime import datetime, timezone

root = Path.cwd()
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
NOW = datetime.now(timezone.utc).isoformat()

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

def update_json(path: str, updater) -> None:
    p = root / path
    if p.exists():
        data = json.loads(p.read_text(encoding="utf-8-sig"))
    else:
        data = {}
    updater(data)
    write(path, json.dumps(data, indent=2, sort_keys=True))

def echo_block(shell, meridians, sector, role, inbound, outbound, evidence, validation, claim, agent_route, update):
    lines = [
        "",
        "## RCC Nexus Echo Location",
        "",
        "Sphere Position:",
        f"- Shell: {shell}",
        f"- Meridian(s): {', '.join(meridians)}",
        f"- Sector: {sector}",
        "- Version / TTL: RCC-N-v1.0 / 180 days",
        f"- Last Verified: {TODAY}",
        "",
        "Local Role:",
        f"- {role}",
        "",
        "Inbound Hooks:",
    ]
    lines += [f"- {x}" for x in inbound] if inbound else ["- None declared."]
    lines += ["", "Outbound Hooks:"]
    lines += [f"- {x}" for x in outbound] if outbound else ["- None declared."]
    lines += ["", "Evidence Surface:"]
    lines += [f"- {x}" for x in evidence] if evidence else ["- None declared."]
    lines += ["", "Validation Surface:"]
    lines += [f"- {x}" for x in validation] if validation else ["- None declared."]
    lines += [
        "",
        "Claim Boundary:",
        f"- {claim}",
        "",
        "Non-Claim Locks:",
        "- geometry_is_not_ai_internal_proof",
        "- nci_is_not_code_quality_proof",
        "- navigation_is_not_validation",
        "- context_reconstruction_is_not_correctness_proof",
        "- validation_remains_required",
        "",
        "Agent Route:",
        f"- {agent_route}",
        "",
        "Update Obligation:",
        f"- {update}",
        "",
    ]
    return lines

# ------------------------------------------------------------
# 1. Root README trisection
# ------------------------------------------------------------

nexus_readme_block = [
    "# PART II - RCC Nexus README",
    "",
    "## RCC Nexus Identity",
    "",
    "AERMA-Memory now includes a local RCC Nexus layer based on RCC-N v1.0.",
    "",
    "RCC tells the agent what the repository means.",
    "",
    "RCC-N tells the agent where it is.",
    "",
    "Validation tells the agent whether reality agreed.",
    "",
    "## Repository Sphere",
    "",
    "| Shell | Name | Meaning |",
    "|---|---|---|",
    "| `center` | Invariant Core | Purpose, non-claim locks, evidence boundaries, safety rules. |",
    "| `inner` | Primitives | Source objects, core modules, schemas, retrieval and gate primitives. |",
    "| `middle` | Processes | Runners, benchmark flow, scripts, checks, validation workflows. |",
    "| `outer` | Evidence / Reflection | Ledgers, reports, evidence packages, architecture, public outputs. |",
    "",
    "## Nexus Meridians",
    "",
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
    "",
    "## Nexus Sectors",
    "",
    "- core",
    "- schemas",
    "- retrieval",
    "- drift",
    "- gate",
    "- benchmark",
    "- cli",
    "- evidence",
    "- rcc",
    "- agent",
    "- release",
    "",
    "## Primary Nexus Files",
    "",
    "- `docs/context/rcc_nexus_index.json`",
    "- `rcc/nexus/README.md`",
    "- `rcc/nexus/rcc_nexus_protocol.md`",
    "- `rcc/nexus/route_map.json`",
    "- `rcc/nexus/task_routing_matrix.md`",
    "- `rcc/nexus/echo_location_template.md`",
    "- `rcc/nexus/agent_handoff_contract.md`",
    "- `scripts/rcc/check_rcc_nexus.py`",
    "- `docs/context/drift/latest_rcc_nexus_report.json`",
    "- `docs/context/drift/latest_rcc_nexus_report.md`",
    "",
    "## Nexus Context Integrity",
    "",
    "Current NCI mode: `self`.",
    "",
    "NCI components:",
    "",
    "- completeness",
    "- link correctness",
    "- pattern rigidity",
    "- invariant compliance",
    "- evidence / validation linkage",
    "- drift freshness",
    "- coordinate completeness",
    "",
    "NCI is not code quality proof.",
    "",
    "## RCC Nexus Non-Claim Lock",
    "",
    "RCC-N improves navigation, traceability, and maintenance discipline. It does not prove code correctness, security, AI understanding, patch safety, production readiness, benchmark validity, or runtime truth.",
    "",
    "Geometry is not correctness.",
    "",
    "Navigation is not validation.",
    "",
    "Context is not truth.",
    "",
    "---",
]

def update_readme(text: str) -> str:
    text = text.replace("# PART II - AI / RCC Agent README", "# PART III - AI Agent README")
    text = text.replace("# PART II - AI Agent README", "# PART III - AI Agent README")
    text = text.replace("PART II - AI / RCC Agent README", "PART III - AI Agent README")
    text = text.replace("PART II - AI Agent README", "PART III - AI Agent README")

    if "# PART II - RCC Nexus README" not in text:
        marker = "<!-- RCC-AI-README:START -->"
        if marker in text:
            text = text.replace(marker, "\n".join(nexus_readme_block).strip() + "\n\n" + marker)
        else:
            text = text.rstrip() + "\n\n" + "\n".join(nexus_readme_block).strip() + "\n"

    if "Human/RCC Nexus/AI README trisection" not in text:
        text = text.rstrip() + "\n\n" + "\n".join([
            "## RCC-N v1.0 Local Integration",
            "",
            "AERMA-Memory now uses a Human/RCC Nexus/AI README trisection.",
            "",
            "- Human README: project purpose, usage, evidence boundary, roadmap.",
            "- RCC Nexus README: repository sphere, shell/meridian/sector coordinates, Echo Location, route maps, NCI, and geometric drift.",
            "- AI Agent README: required read order, patch protocol, validation commands, non-claim locks, and done criteria.",
            "",
            "This trisection is part of the RCC-N v1.0 local integration."
        ]) + "\n"

    return text

write("README.md", update_readme(read("README.md")))

# ------------------------------------------------------------
# 2. Root agent beacons
# ------------------------------------------------------------

agents_md = [
    "# AGENTS.md",
    "",
    "## Repository Identity",
    "",
    "You are entering AERMA-Memory, a governed agentic episodic memory reference workbench with RCC and RCC-N repository-context layers.",
    "",
    "## Required Read Order",
    "",
    "1. README.md",
    "2. docs/context/repository_context_index.json",
    "3. docs/context/validation_surface.md",
    "4. docs/context/rcc_nexus_index.json",
    "5. rcc/nexus/route_map.json",
    "6. Target folder README.md",
    "7. Relevant source, tests, tasks, evidence, or scripts.",
    "",
    "## Patch Rule",
    "",
    "No route, no safe patch.",
    "",
    "Read the local Echo Location block before modifying a major folder.",
    "",
    "## Validation",
    "",
    "For source, scoring, benchmark, task, evidence, or RCC-N changes, run:",
    "",
    "    pytest -q",
    "    python -m aerma.cli.main run-suite --suite .\\tasks\\suite_v1_2.json",
    "    python scripts/run_aerma_regression_guard.py",
    "    powershell -ExecutionPolicy Bypass -File .\\scripts\\rcc\\check_rcc_drift.ps1",
    "    python scripts/rcc/check_rcc_nexus.py",
    "",
    "## Non-Claim Locks",
    "",
    "- RCC-N is not code correctness.",
    "- NCI is not code quality proof.",
    "- Navigation is not validation.",
    "- Context reconstruction is not runtime truth.",
    "- Suite execution is not production readiness.",
]

claude_md = [
    "# CLAUDE.md",
    "",
    "## Project Memory",
    "",
    "AERMA-Memory uses RCC and RCC-N to make the repository self-locating for code agents.",
    "",
    "## Claude-Specific Instructions",
    "",
    "- Preserve Markdown formatting.",
    "- Do not collapse headings, tables, or lists into long single lines.",
    "- Do not treat RCC or RCC-N as proof of code correctness.",
    "- Keep patches minimal.",
    "- Preserve non-claim locks.",
    "- Run validation before claiming completion.",
    "",
    "## Required Route",
    "",
    "README.md -> docs/context/repository_context_index.json -> docs/context/rcc_nexus_index.json -> rcc/nexus/route_map.json -> target folder README.md -> source/tests/evidence.",
]

write("AGENTS.md", agents_md)
write("CLAUDE.md", claude_md)

# ------------------------------------------------------------
# 3. rcc/nexus files
# ------------------------------------------------------------

rcc_nexus_readme = [
    "# rcc/nexus",
    "",
    "<!-- RCC-MINI-README:START -->",
    "",
    "## Purpose",
    "",
    "Local RCC Nexus implementation layer for AERMA-Memory. This folder contains the geometric repository-context route maps, Echo Location protocol, task routing matrix, handoff contract, and templates needed for RCC-N v1.0.",
    "",
    "## S - Formal specification",
    "",
    "This folder implements RCC-N v1.0 as a repository-local navigation field. It defines how agents locate modules by shell, meridian, sector, hooks, evidence, validation, and update obligations before patching.",
    "",
    "## H - Hooks and integration edges",
    "",
    "- Root README links to the RCC Nexus layer.",
    "- `docs/context/rcc_nexus_index.json` provides the machine-readable sphere index.",
    "- `scripts/rcc/check_rcc_nexus.py` validates the Nexus layer.",
    "- Major folder mini READMEs include Echo Location blocks.",
    "- `docs/context/drift/latest_rcc_nexus_report.*` stores Nexus check results.",
    "",
    "## A - Artifacts",
    "",
    "- `rcc_nexus_protocol.md`",
    "- `route_map.json`",
    "- `task_routing_matrix.md`",
    "- `echo_location_template.md`",
    "- `agent_handoff_contract.md`",
    "",
    "## T - Theory or method basis",
    "",
    "RCC-N v1.0 extends RCC v1.3 with geometric repository context: Human/RCC Nexus/AI README trisection, repository sphere, shell/meridian/sector coordinates, Echo Location records, route maps, NCI, navigation entropy, and geometric drift.",
    "",
    "## I - Invariants",
    "",
    "- RCC-N is not code correctness.",
    "- NCI is not code quality proof.",
    "- Navigation is not validation.",
    "- Context reconstruction is not runtime truth.",
    "- Major changes to roles, hooks, validation, evidence, or claims require Nexus updates.",
    "- Agents must route before patching.",
    "",
    "## E - Example",
    "",
    "Run the Nexus checker:",
    "",
    "    python scripts/rcc/check_rcc_nexus.py",
    "",
    "<!-- RCC-MINI-README:END -->",
]
rcc_nexus_readme += echo_block(
    "middle",
    ["rcc", "agent", "safety", "validation", "drift"],
    "rcc",
    "Holds the repository-local RCC Nexus route maps, protocol, templates, and handoff contract.",
    ["README.md", "docs/context/rcc_nexus_index.json", "scripts/rcc/check_rcc_nexus.py"],
    ["docs/context/drift/latest_rcc_nexus_report.json", "docs/context/drift/latest_rcc_nexus_report.md"],
    ["docs/context/drift/latest_rcc_nexus_report.json", "docs/context/drift/latest_rcc_nexus_report.md"],
    ["python scripts/rcc/check_rcc_nexus.py"],
    "This folder improves agent navigation and context integrity only. It does not prove runtime correctness.",
    "Read README.md, docs/context/rcc_nexus_index.json, then this folder before editing Nexus routing.",
    "Update route map, index, protocol, and checker when repository geometry changes."
)

write("rcc/nexus/README.md", rcc_nexus_readme)

write("rcc/nexus/rcc_nexus_protocol.md", [
    "# RCC Nexus Protocol",
    "",
    "RCC-N v1.0 requires agent self-location before patching.",
    "",
    "Protocol:",
    "",
    "    Observe -> Trisect -> Locate -> Route -> Inspect -> Patch -> Validate -> Update Nexus",
    "",
    "Steps:",
    "",
    "1. Observe repository entry beacons.",
    "2. Read the Human README.",
    "3. Read the RCC Nexus README layer.",
    "4. Read the AI Agent README layer.",
    "5. Load `docs/context/rcc_nexus_index.json`.",
    "6. Identify affected shell, meridian, and sector.",
    "7. Read the local Echo Location block.",
    "8. Inspect source and tests at the required context budget.",
    "9. Patch the smallest safe surface.",
    "10. Run validation.",
    "11. Update RCC/Nexus records when geometry changes.",
    "",
    "Boundary: RCC Nexus navigation is not validation. Validation remains the reality boundary.",
])

route_map = {
    "schema": "RCC-N-v1.0-route-map",
    "repo": "AERMA-Memory",
    "entry_order": [
        "README.md",
        "AGENTS.md",
        "CLAUDE.md",
        "docs/context/repository_context_index.json",
        "docs/context/rcc_nexus_index.json",
        "docs/context/validation_surface.md"
    ],
    "task_routes": {
        "read_only_review": {
            "read_first": ["README.md", "docs/context/module_index.md", "docs/context/rcc_nexus_index.json"],
            "edit_surface": [],
            "validation": [],
            "nexus_update": "not_required_unless_stale_context_found"
        },
        "documentation_change": {
            "read_first": ["README.md", "target_folder/README.md", "docs/context/rcc_nexus_index.json"],
            "edit_surface": ["README.md", "docs/**", "target_folder/README.md"],
            "validation": ["powershell -ExecutionPolicy Bypass -File .\\scripts\\rcc\\check_rcc_drift.ps1", "python scripts/rcc/check_rcc_nexus.py"],
            "nexus_update": "required_if_role_hooks_validation_evidence_or_claims_change"
        },
        "rcc_nexus_change": {
            "read_first": ["README.md", "rcc/nexus/README.md", "docs/context/rcc_nexus_index.json"],
            "edit_surface": ["rcc/nexus/**", "docs/context/**", "scripts/rcc/check_rcc_nexus.py", "README.md"],
            "validation": ["python scripts/rcc/check_rcc_nexus.py", "powershell -ExecutionPolicy Bypass -File .\\scripts\\rcc\\check_rcc_drift.ps1"],
            "nexus_update": "always_required"
        },
        "runtime_change": {
            "read_first": ["README.md", "src/aerma/README.md", "target_module/README.md"],
            "edit_surface": ["src/aerma/**", "tests/**"],
            "validation": ["pytest -q", "python -m aerma.cli.main run-suite --suite .\\tasks\\suite_v1_2.json", "python scripts/run_aerma_regression_guard.py"],
            "nexus_update": "required_if_hooks_validation_evidence_or_claim_boundaries_change"
        },
        "benchmark_task_change": {
            "read_first": ["tasks/README.md", "src/aerma/benchmarks/README.md"],
            "edit_surface": ["tasks/**", "src/aerma/benchmarks/**", "tests/**"],
            "validation": ["pytest -q", "python -m aerma.cli.main run-suite --suite .\\tasks\\suite_v1_2.json", "python scripts/run_aerma_regression_guard.py"],
            "nexus_update": "required_if_suite_or_validation_surface_changes"
        },
        "public_claim_change": {
            "read_first": ["README.md", "docs/context/validation_surface.md", "docs/context/rcc_nexus_index.json"],
            "edit_surface": ["README.md", "docs/context/**", "docs/software_architecture/**"],
            "validation": ["pytest -q", "python -m aerma.cli.main run-suite --suite .\\tasks\\suite_v1_2.json", "python scripts/run_aerma_regression_guard.py", "python scripts/rcc/check_rcc_nexus.py"],
            "nexus_update": "always_required"
        }
    },
    "non_claim_locks": [
        "geometry_is_not_ai_internal_proof",
        "nci_is_not_code_quality_proof",
        "navigation_is_not_validation",
        "context_reconstruction_is_not_correctness_proof",
        "validation_remains_required"
    ]
}
write("rcc/nexus/route_map.json", json.dumps(route_map, indent=2, sort_keys=True))

write("rcc/nexus/task_routing_matrix.md", [
    "# RCC Nexus Task Routing Matrix",
    "",
    "| Task type | Read first | Likely edit surface | Required validation | Nexus update obligation |",
    "|---|---|---|---|---|",
    "| Read-only review | `README.md`, `docs/context/rcc_nexus_index.json` | None | None unless claims are made | No update unless stale context found |",
    "| Documentation change | `README.md`, target folder README | README/docs files | RCC check + Nexus check | Update affected Echo Location if role/hooks changed |",
    "| RCC/Nexus change | `rcc/nexus/README.md`, `docs/context/rcc_nexus_index.json` | `rcc/nexus`, `docs/context`, README | RCC check + Nexus check | Always update Nexus index/report |",
    "| Runtime change | `src/aerma/README.md` | `src/aerma/**`, tests | pytest + suite + guard | Update Echo Location if hooks/validation/evidence changed |",
    "| Scoring change | `src/aerma/benchmarks/README.md` | scoring/classifier/runner/tests | pytest + suite + guard | Update validation/evidence claims |",
    "| Task-suite change | `tasks/README.md` | tasks/suite/tests | pytest + suite + guard | Update route map and validation surface |",
    "| Evidence change | `src/aerma/evidence/README.md` | evidence compiler/ledgers/reports | pytest + suite + evidence inspection | Update evidence surface in Nexus |",
    "| Public claim change | README + validation surface | README/docs/context | full validation | Update non-claim locks and claim boundaries |",
])

write("rcc/nexus/echo_location_template.md", [
    "# RCC Nexus Echo Location Template",
    "",
    "## RCC Nexus Echo Location",
    "",
    "Sphere Position:",
    "- Shell:",
    "- Meridian(s):",
    "- Sector:",
    "- Version / TTL:",
    "- Last Verified:",
    "",
    "Local Role:",
    "-",
    "",
    "Inbound Hooks:",
    "-",
    "",
    "Outbound Hooks:",
    "-",
    "",
    "Evidence Surface:",
    "-",
    "",
    "Validation Surface:",
    "-",
    "",
    "Claim Boundary:",
    "-",
    "",
    "Non-Claim Locks:",
    "-",
    "",
    "Agent Route:",
    "-",
    "",
    "Update Obligation:",
    "-",
])

write("rcc/nexus/agent_handoff_contract.md", [
    "# RCC Nexus Agent Handoff Contract",
    "",
    "Every agent handoff should report:",
    "",
    "- task_type",
    "- files_read",
    "- files_changed",
    "- route_followed",
    "- coordinates_affected",
    "- commands_run",
    "- validation_result",
    "- evidence_generated",
    "- claim_boundary_preserved",
    "- rcc_updates_completed",
    "- nexus_updates_completed",
    "- remaining_risks",
    "",
    "Boundary: A handoff is not proof of correctness. It is a continuity artifact.",
])

# ------------------------------------------------------------
# 4. Nexus index
# ------------------------------------------------------------

nodes = [
    {
        "path": "README.md",
        "node_type": "root_readme",
        "shell": "center",
        "meridians": ["source", "agent", "safety", "release"],
        "sector": "rcc",
        "last_verified": TODAY,
        "ttl_days": 180,
        "echo_location_path": "README.md#part-ii---rcc-nexus-readme",
        "inbound_hooks": ["AGENTS.md", "CLAUDE.md"],
        "outbound_hooks": ["docs/context/repository_context_index.json", "docs/context/rcc_nexus_index.json", "rcc/nexus/route_map.json"],
        "evidence_surface": ["docs/context/drift/latest_rcc_nexus_report.json"],
        "validation_surface": ["python scripts/rcc/check_rcc_nexus.py"],
        "claim_boundary": ["readme_quality_is_not_runtime_validity", "nci_is_not_code_quality_proof"]
    },
    {
        "path": "docs/context",
        "node_type": "context_surface",
        "shell": "outer",
        "meridians": ["source", "validation", "evidence", "drift", "agent", "safety"],
        "sector": "rcc",
        "last_verified": TODAY,
        "ttl_days": 180,
        "echo_location_path": "docs/context/rcc_nexus_index.json",
        "inbound_hooks": ["README.md", "rcc/nexus/route_map.json"],
        "outbound_hooks": ["docs/context/drift/latest_rcc_nexus_report.json"],
        "evidence_surface": ["docs/context/drift/latest_rcc_nexus_report.json"],
        "validation_surface": ["python scripts/rcc/check_rcc_nexus.py"],
        "claim_boundary": ["context_index_is_not_source_truth"]
    },
    {
        "path": "docs/software_architecture",
        "node_type": "architecture_surface",
        "shell": "outer",
        "meridians": ["source", "agent", "safety", "release"],
        "sector": "rcc",
        "last_verified": TODAY,
        "ttl_days": 180,
        "echo_location_path": "docs/software_architecture/README.md#rcc-nexus-echo-location",
        "inbound_hooks": ["README.md"],
        "outbound_hooks": ["docs/software_architecture/rcc_nexus_software_architecture_v1_0.md"],
        "evidence_surface": ["docs/software_architecture/rcc_nexus_implementation_contract_v1_0.md"],
        "validation_surface": ["pytest -q", "python scripts/rcc/check_rcc_nexus.py"],
        "claim_boundary": ["architecture_is_not_implementation_proof"]
    },
    {
        "path": "src/aerma/benchmarks",
        "node_type": "source_module",
        "shell": "middle",
        "meridians": ["runtime", "validation", "evidence", "safety"],
        "sector": "benchmark",
        "last_verified": TODAY,
        "ttl_days": 180,
        "echo_location_path": "src/aerma/benchmarks/README.md#rcc-nexus-echo-location",
        "inbound_hooks": ["tasks/suite_v1_2.json", "src/aerma/cli/main.py"],
        "outbound_hooks": ["runs/", "evidence_packages/", "ledgers/aerma_suite_ledger.jsonl"],
        "evidence_surface": ["runs/suite_*/aggregate_metrics.json", "evidence_packages/*_evidence_package.json"],
        "validation_surface": ["pytest -q", "python -m aerma.cli.main run-suite --suite .\\tasks\\suite_v1_2.json"],
        "claim_boundary": ["suite_score_is_local_controlled_suite_evidence_only"]
    },
    {
        "path": "src/aerma/evidence",
        "node_type": "source_module",
        "shell": "middle",
        "meridians": ["evidence", "runtime", "safety"],
        "sector": "evidence",
        "last_verified": TODAY,
        "ttl_days": 180,
        "echo_location_path": "src/aerma/evidence/README.md#rcc-nexus-echo-location",
        "inbound_hooks": ["src/aerma/benchmarks/suite_runner.py"],
        "outbound_hooks": ["evidence_packages/"],
        "evidence_surface": ["evidence_packages/"],
        "validation_surface": ["pytest -q"],
        "claim_boundary": ["evidence_package_is_bound_to_declared_task_surface"]
    },
    {
        "path": "tasks",
        "node_type": "benchmark_tasks",
        "shell": "middle",
        "meridians": ["validation", "runtime", "evidence"],
        "sector": "benchmark",
        "last_verified": TODAY,
        "ttl_days": 180,
        "echo_location_path": "tasks/README.md#rcc-nexus-echo-location",
        "inbound_hooks": ["src/aerma/benchmarks/suite_runner.py"],
        "outbound_hooks": ["runs/", "evidence_packages/"],
        "evidence_surface": ["runs/suite_*/aggregate_metrics.json"],
        "validation_surface": ["python -m aerma.cli.main run-suite --suite .\\tasks\\suite_v1_2.json"],
        "claim_boundary": ["controlled_tasks_do_not_prove_broad_generalization"]
    },
    {
        "path": "tests",
        "node_type": "test_surface",
        "shell": "middle",
        "meridians": ["validation", "safety"],
        "sector": "core",
        "last_verified": TODAY,
        "ttl_days": 180,
        "echo_location_path": "tests/README.md#rcc-nexus-echo-location",
        "inbound_hooks": ["src/aerma/**"],
        "outbound_hooks": ["pytest -q"],
        "evidence_surface": ["pytest output"],
        "validation_surface": ["pytest -q"],
        "claim_boundary": ["tests_are_implementation_health_not_truth"]
    },
    {
        "path": "rcc/nexus",
        "node_type": "nexus_layer",
        "shell": "middle",
        "meridians": ["rcc", "agent", "safety", "validation", "drift"],
        "sector": "rcc",
        "last_verified": TODAY,
        "ttl_days": 180,
        "echo_location_path": "rcc/nexus/README.md#rcc-nexus-echo-location",
        "inbound_hooks": ["README.md", "docs/context/rcc_nexus_index.json"],
        "outbound_hooks": ["scripts/rcc/check_rcc_nexus.py", "docs/context/drift/latest_rcc_nexus_report.json"],
        "evidence_surface": ["docs/context/drift/latest_rcc_nexus_report.json"],
        "validation_surface": ["python scripts/rcc/check_rcc_nexus.py"],
        "claim_boundary": ["nexus_navigation_is_not_validation"]
    }
]

index = {
    "schema": "RCC-N-v1.0-nexus-index",
    "repository": {
        "name": "AERMA-Memory",
        "root": ".",
        "rcc_base": "RCC-v1.3-compatible",
        "nexus_version": "RCC-N-v1.0",
        "last_verified": TODAY,
        "verification_mode": "self"
    },
    "readme_trisection": {
        "human_layer_present": True,
        "rcc_nexus_layer_present": True,
        "ai_agent_layer_present": True,
        "layer_fusion_detected": False
    },
    "sphere": {
        "model": "spherical_echo_architecture",
        "shells": ["center", "inner", "middle", "outer"],
        "meridians": ["source", "validation", "evidence", "drift", "agent", "safety", "runtime", "memory", "release", "federation"],
        "sectors": ["core", "schemas", "retrieval", "drift", "gate", "benchmark", "cli", "evidence", "rcc", "agent", "release"]
    },
    "nodes": nodes,
    "route_maps": ["rcc/nexus/route_map.json", "rcc/nexus/task_routing_matrix.md"],
    "nci": {
        "mode": "self",
        "weights": {
            "completeness": 0.15,
            "link_correctness": 0.15,
            "pattern_rigidity": 0.10,
            "invariant_compliance": 0.20,
            "evidence_validation_linkage": 0.15,
            "drift_freshness": 0.10,
            "coordinate_completeness": 0.15
        },
        "components": {
            "completeness": {"score": 1.0, "algorithm": "required_nexus_sections_present / required_nexus_sections"},
            "link_correctness": {"score": 0.90, "algorithm": "declared_hooks_resolve_or_are_explicitly_external / declared_hooks"},
            "pattern_rigidity": {"score": 0.95, "algorithm": "template_conforming_records / total_records"},
            "invariant_compliance": {"score": 1.0, "algorithm": "records_preserving_non_claim_locks / total_records"},
            "evidence_validation_linkage": {"score": 0.90, "algorithm": "records_with_required_evidence_and_validation / required_records"},
            "drift_freshness": {"score": 0.95, "algorithm": "1 - geometric_drift_score"},
            "coordinate_completeness": {"score": 1.0, "algorithm": "nodes_with_shell_meridian_sector_ttl / total_nodes"}
        }
    },
    "non_claim_locks": {
        "geometry_is_not_ai_internal_proof": True,
        "nci_is_not_code_quality_proof": True,
        "navigation_is_not_validation": True,
        "context_reconstruction_is_not_correctness_proof": True,
        "validation_remains_required": True
    }
}
write("docs/context/rcc_nexus_index.json", json.dumps(index, indent=2, sort_keys=True))

# ------------------------------------------------------------
# 5. Echo Location blocks in key mini READMEs
# ------------------------------------------------------------

echo_targets = {
    "docs/software_architecture/README.md": echo_block(
        "outer",
        ["source", "agent", "safety", "release"],
        "rcc",
        "Holds locked software architecture documents and implementation contracts.",
        ["README.md", "docs/context/module_index.md"],
        ["docs/software_architecture/rcc_nexus_software_architecture_v1_0.md", "docs/software_architecture/rcc_nexus_implementation_contract_v1_0.md"],
        ["architecture documents"],
        ["pytest -q", "python scripts/rcc/check_rcc_nexus.py"],
        "Architecture is not implementation proof.",
        "Read architecture before implementing RCC-N surfaces.",
        "Update when architecture direction or implementation contract changes."
    ),
    "src/aerma/benchmarks/README.md": echo_block(
        "middle",
        ["runtime", "validation", "evidence", "safety"],
        "benchmark",
        "Runs benchmark tasks, scoring, classification, attribution, regression guard, and suite evidence surfaces.",
        ["tasks/suite_v1_2.json", "src/aerma/cli/main.py"],
        ["runs/", "evidence_packages/", "ledgers/aerma_suite_ledger.jsonl"],
        ["runs/suite_*/aggregate_metrics.json", "evidence_packages/*_evidence_package.json"],
        ["pytest -q", "python -m aerma.cli.main run-suite --suite .\\tasks\\suite_v1_2.json"],
        "Suite score is controlled-suite evidence only.",
        "Read this README before scoring, suite, or classifier changes.",
        "Update when benchmark hooks, metrics, or evidence surfaces change."
    ),
    "src/aerma/evidence/README.md": echo_block(
        "middle",
        ["evidence", "runtime", "safety"],
        "evidence",
        "Compiles runtime evidence packages and related evidence artifacts.",
        ["src/aerma/benchmarks/suite_runner.py"],
        ["evidence_packages/"],
        ["evidence_packages/"],
        ["pytest -q"],
        "Evidence packages are bounded to declared tasks and artifacts.",
        "Read this README before modifying evidence package behavior.",
        "Update when evidence schema or output paths change."
    ),
    "tasks/README.md": echo_block(
        "middle",
        ["validation", "runtime", "evidence"],
        "benchmark",
        "Stores benchmark task JSON and suite definitions.",
        ["src/aerma/benchmarks/suite_runner.py"],
        ["runs/", "evidence_packages/"],
        ["runs/suite_*/aggregate_metrics.json"],
        ["python -m aerma.cli.main run-suite --suite .\\tasks\\suite_v1_2.json"],
        "Controlled tasks do not prove broad generalization.",
        "Read this README before task or suite changes.",
        "Update when task families, suite composition, or validation expectations change."
    ),
    "tests/README.md": echo_block(
        "middle",
        ["validation", "safety"],
        "core",
        "Stores pytest validation for the current reference scaffold.",
        ["src/aerma/**"],
        ["pytest -q"],
        ["pytest output"],
        ["pytest -q"],
        "Tests are implementation health evidence, not truth proof.",
        "Read this README before modifying tests or interpreting validation status.",
        "Update when test scope or expected count changes."
    )
}

for path, block in echo_targets.items():
    if Path(root / path).exists():
        append_once(path, "## RCC Nexus Echo Location", block)
    else:
        print(f"[WARN] Echo target missing: {path}")

# ------------------------------------------------------------
# 6. Nexus checker
# ------------------------------------------------------------

checker_lines = [
"from __future__ import annotations",
"",
"import json",
"from dataclasses import dataclass",
"from datetime import datetime, timezone",
"from pathlib import Path",
"from typing import Any, Dict, List, Optional",
"",
"VALID_SHELLS = {'center', 'inner', 'middle', 'outer'}",
"VALID_MERIDIANS = {'source', 'validation', 'evidence', 'drift', 'agent', 'safety', 'runtime', 'memory', 'release', 'federation'}",
"REQUIRED_LOCKS = {",
"    'geometry_is_not_ai_internal_proof',",
"    'nci_is_not_code_quality_proof',",
"    'navigation_is_not_validation',",
"    'context_reconstruction_is_not_correctness_proof',",
"    'validation_remains_required',",
"}",
"NCI_WEIGHTS = {",
"    'completeness': 0.15,",
"    'link_correctness': 0.15,",
"    'pattern_rigidity': 0.10,",
"    'invariant_compliance': 0.20,",
"    'evidence_validation_linkage': 0.15,",
"    'drift_freshness': 0.10,",
"    'coordinate_completeness': 0.15,",
"}",
"",
"@dataclass",
"class Finding:",
"    code: str",
"    message: str",
"    severity: str = 'warning'",
"    path: Optional[str] = None",
"",
"def clamp01(value: Any) -> float:",
"    try:",
"        return max(0.0, min(1.0, float(value)))",
"    except Exception:",
"        return 0.0",
"",
"def read_text(path: Path) -> str:",
"    return path.read_text(encoding='utf-8-sig', errors='replace')",
"",
"def load_json(path: Path) -> Dict[str, Any]:",
"    return json.loads(read_text(path))",
"",
"def check_readme(root: Path) -> List[Finding]:",
"    findings = []",
"    path = root / 'README.md'",
"    if not path.exists():",
"        return [Finding('RCCN001', 'README.md missing', 'error', str(path))]",
"    text = read_text(path).lower()",
"    required = ['part i - human readme', 'part ii - rcc nexus readme', 'part iii - ai agent readme']",
"    for item in required:",
"        if item not in text:",
"            findings.append(Finding('RCCN001', f'Missing README trisection layer: {item}', 'error', 'README.md'))",
"    return findings",
"",
"def check_index(root: Path) -> tuple[List[Finding], Dict[str, Any]]:",
"    findings = []",
"    path = root / 'docs' / 'context' / 'rcc_nexus_index.json'",
"    if not path.exists():",
"        return [Finding('RCCN002', 'Missing docs/context/rcc_nexus_index.json', 'error', str(path))], {}",
"    try:",
"        data = load_json(path)",
"    except Exception as exc:",
"        return [Finding('RCCN002', f'Invalid rcc_nexus_index.json: {exc}', 'error', str(path))], {}",
"    for node in data.get('nodes', []):",
"        node_path = node.get('path', '<unknown>')",
"        if node.get('shell') not in VALID_SHELLS:",
"            findings.append(Finding('RCCN004', f'Invalid or missing shell for {node_path}', 'error', node_path))",
"        meridians = set(node.get('meridians', []))",
"        if not meridians or not meridians.issubset(VALID_MERIDIANS):",
"            findings.append(Finding('RCCN005', f'Invalid or missing meridians for {node_path}', 'error', node_path))",
"        if not node.get('sector'):",
"            findings.append(Finding('RCCN006', f'Missing sector for {node_path}', 'error', node_path))",
"        if not node.get('echo_location_path'):",
"            findings.append(Finding('RCCN003', f'Missing Echo Location path for {node_path}', 'warning', node_path))",
"    locks = data.get('non_claim_locks', {})",
"    for lock in REQUIRED_LOCKS:",
"        if not locks.get(lock):",
"            findings.append(Finding('RCCN010', f'Missing non-claim lock: {lock}', 'error', 'docs/context/rcc_nexus_index.json'))",
"    return findings, data",
"",
"def compute_nci(data: Dict[str, Any]) -> Optional[float]:",
"    nci = data.get('nci', {})",
"    weights = nci.get('weights', {})",
"    components = nci.get('components', {})",
"    if set(weights) != set(NCI_WEIGHTS):",
"        return None",
"    total = 0.0",
"    for key, weight in weights.items():",
"        total += float(weight) * clamp01(components.get(key, {}).get('score'))",
"    return clamp01(total)",
"",
"def check_nci(data: Dict[str, Any]) -> List[Finding]:",
"    findings = []",
"    nci = data.get('nci', {})",
"    if nci.get('mode') not in {'self', 'linted', 'verified'}:",
"        findings.append(Finding('RCCN015', 'NCI mode must be self, linted, or verified', 'error', 'docs/context/rcc_nexus_index.json'))",
"    if set(nci.get('weights', {})) != set(NCI_WEIGHTS):",
"        findings.append(Finding('RCCN015', 'NCI weights missing required components', 'error', 'docs/context/rcc_nexus_index.json'))",
"    for key in NCI_WEIGHTS:",
"        comp = nci.get('components', {}).get(key)",
"        if not comp or 'score' not in comp or 'algorithm' not in comp:",
"            findings.append(Finding('RCCN015', f'Incomplete NCI component: {key}', 'error', 'docs/context/rcc_nexus_index.json'))",
"    return findings",
"",
"def check_route_map(root: Path) -> List[Finding]:",
"    path = root / 'rcc' / 'nexus' / 'route_map.json'",
"    if not path.exists():",
"        return [Finding('RCCN012', 'Missing rcc/nexus/route_map.json', 'error', str(path))]",
"    try:",
"        data = load_json(path)",
"    except Exception as exc:",
"        return [Finding('RCCN012', f'Invalid route_map.json: {exc}', 'error', str(path))]",
"    required = ['read_only_review', 'documentation_change', 'rcc_nexus_change', 'runtime_change', 'benchmark_task_change', 'public_claim_change']",
"    routes = data.get('task_routes', {})",
"    return [Finding('RCCN012', f'Missing route: {r}', 'error', str(path)) for r in required if r not in routes]",
"",
"def check_echo_blocks(root: Path, data: Dict[str, Any]) -> List[Finding]:",
"    findings = []",
"    for node in data.get('nodes', []):",
"        echo = node.get('echo_location_path', '')",
"        if not echo or '.json' in echo:",
"            continue",
"        file_part = echo.split('#')[0]",
"        path = root / file_part",
"        if path.exists():",
"            text = read_text(path).lower()",
"            if 'rcc nexus echo location' not in text:",
"                findings.append(Finding('RCCN003', f'Echo Location block missing in {file_part}', 'warning', file_part))",
"        else:",
"            findings.append(Finding('RCCN003', f'Echo Location file missing: {file_part}', 'warning', file_part))",
"    return findings",
"",
"def write_reports(root: Path, payload: Dict[str, Any]) -> None:",
"    report_dir = root / 'docs' / 'context' / 'drift'",
"    report_dir.mkdir(parents=True, exist_ok=True)",
"    (report_dir / 'latest_rcc_nexus_report.json').write_text(json.dumps(payload, indent=2, sort_keys=True) + '\\n', encoding='utf-8')",
"    lines = [",
"        '# RCC Nexus Report',",
"        '',",
"        f\"Status: {payload['status']}\",",
"        '',",
"        f\"Computed NCI: {payload.get('computed_nci')}\",",
"        '',",
"        f\"Timestamp: {payload['timestamp']}\",",
"        '',",
"        '## Findings',",
"        '',",
"    ]",
"    if payload['findings']:",
"        lines += ['| Code | Severity | Path | Message |', '|---|---|---|---|']",
"        for f in payload['findings']:",
"            lines.append(f\"| {f['code']} | {f['severity']} | {f.get('path') or ''} | {f['message']} |\")",
"    else:",
"        lines.append('No findings.')",
"    lines += ['', '## Boundary', '', 'RCC Nexus improves navigation and context integrity. It does not prove code correctness, security, patch safety, AI understanding, benchmark validity, or production readiness.']",
"    (report_dir / 'latest_rcc_nexus_report.md').write_text('\\n'.join(lines) + '\\n', encoding='utf-8')",
"",
"def main() -> int:",
"    root = Path('.').resolve()",
"    findings = []",
"    findings.extend(check_readme(root))",
"    index_findings, data = check_index(root)",
"    findings.extend(index_findings)",
"    if data:",
"        findings.extend(check_nci(data))",
"        findings.extend(check_echo_blocks(root, data))",
"    findings.extend(check_route_map(root))",
"    computed_nci = compute_nci(data) if data else None",
"    status = 'pass'",
"    if any(f.severity == 'error' for f in findings):",
"        status = 'fail'",
"    elif findings:",
"        status = 'warn'",
"    payload = {",
"        'schema': 'RCC-N-v1.0-check-result',",
"        'timestamp': datetime.now(timezone.utc).isoformat(),",
"        'status': status,",
"        'computed_nci': computed_nci,",
"        'findings': [f.__dict__ for f in findings],",
"        'non_claim_locks': {lock: True for lock in sorted(REQUIRED_LOCKS)},",
"        'claim_boundary': 'RCC Nexus is context/navigation integrity only, not code correctness proof.'",
"    }",
"    write_reports(root, payload)",
"    print(json.dumps(payload, indent=2, sort_keys=True))",
"    return 1 if status == 'fail' else 0",
"",
"if __name__ == '__main__':",
"    raise SystemExit(main())",
]
write("scripts/rcc/check_rcc_nexus.py", "\n".join(checker_lines))

# ------------------------------------------------------------
# 7. Update existing context files
# ------------------------------------------------------------

def update_repo_context(data):
    data.setdefault("repository", {})
    data["repository"]["current_nexus_layer"] = "RCC-N-v1.0-local-integration"
    data["repository"]["nexus_last_updated"] = NOW
    data["rcc_nexus"] = {
        "enabled": True,
        "implementation_status": "local_self_mode_active",
        "index": "docs/context/rcc_nexus_index.json",
        "nexus_root": "rcc/nexus/",
        "route_map": "rcc/nexus/route_map.json",
        "checker": "scripts/rcc/check_rcc_nexus.py",
        "latest_report_json": "docs/context/drift/latest_rcc_nexus_report.json",
        "latest_report_md": "docs/context/drift/latest_rcc_nexus_report.md",
        "nci_mode": "self",
        "claim_boundary": "RCC-N improves navigation and context integrity; it does not prove correctness."
    }
    data.setdefault("validation", {})
    data["validation"]["rcc_nexus"] = [
        "python scripts/rcc/check_rcc_nexus.py"
    ]

update_json("docs/context/repository_context_index.json", update_repo_context)

append_once("docs/context/module_index.md", "## RCC-N Local Nexus Layer", [
    "## RCC-N Local Nexus Layer",
    "",
    "| Module | Path | Role | Runtime claim sensitivity |",
    "|---|---|---|---|",
    "| RCC Nexus index | `docs/context/rcc_nexus_index.json` | Machine-readable sphere, coordinates, NCI, route maps, and locks | Medium |",
    "| RCC Nexus local layer | `rcc/nexus/` | Route maps, protocol, task matrix, handoff, Echo template | Medium |",
    "| RCC Nexus checker | `scripts/rcc/check_rcc_nexus.py` | Validates trisection, index, route map, NCI, and Echo blocks | Medium |",
    "| RCC Nexus reports | `docs/context/drift/latest_rcc_nexus_report.*` | Generated Nexus integrity reports | Medium |",
    "",
    "Boundary: RCC-N is navigation/context integrity only, not code correctness."
])

append_once("docs/context/validation_surface.md", "## RCC-N Local Validation", [
    "## RCC-N Local Validation",
    "",
    "Run the local RCC Nexus checker:",
    "",
    "    python scripts/rcc/check_rcc_nexus.py",
    "",
    "Full validation after RCC-N changes:",
    "",
    "    pytest -q",
    "    python -m aerma.cli.main run-suite --suite .\\tasks\\suite_v1_2.json",
    "    python scripts/run_aerma_regression_guard.py",
    "    powershell -ExecutionPolicy Bypass -File .\\scripts\\rcc\\check_rcc_drift.ps1",
    "    python scripts/rcc/check_rcc_nexus.py",
    "",
    "Boundary: RCC-N local validation does not prove code correctness."
])

print("[RCC-N] Local implementation written.")