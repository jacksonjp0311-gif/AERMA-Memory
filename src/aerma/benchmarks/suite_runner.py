from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

from aerma.benchmarks.benchmark_runner import BenchmarkRunner
from aerma.benchmarks.scoring import aggregate_task_metrics
from aerma.benchmarks.classifier import classify_claim
from aerma.evidence.runtime_ledger import RuntimeLedger
from aerma.evidence.evidence_package import EvidencePackageCompiler
from aerma.agent.recursive_executor_stub import RecursiveExecutorStub
from aerma.agent.reflection_evaluator_stub import ReflectionEvaluatorStub


class SuiteRunner:
    def __init__(self, root: str | Path = ".") -> None:
        self.root = Path(root).resolve()
        self.benchmark_runner = BenchmarkRunner()

    def _write_json(self, path: Path, payload: Dict[str, Any] | List[Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

    def _build_regression_guard(self, aggregate_metrics: Dict[str, float]) -> Dict[str, Any]:
        suite_score = aggregate_metrics.get("suite_score", 0.0)
        return {
            "guard_type": "AERMA-v0.1.1-regression-guard",
            "status": "baseline_locked",
            "baseline_suite_score": suite_score,
            "minimum_suite_score": max(0.0, suite_score - 0.02),
            "minimum_source_attribution_accuracy": max(0.0, aggregate_metrics.get("source_attribution_accuracy", 0.0) - 0.02),
            "minimum_fallback_correctness": max(0.0, aggregate_metrics.get("fallback_correctness", 0.0) - 0.02),
            "minimum_boundary_separation_score": max(0.0, aggregate_metrics.get("boundary_separation_score", 0.0) - 0.02),
            "minimum_abstention_correctness": max(0.0, aggregate_metrics.get("abstention_correctness", 0.0) - 0.02),
            "maximum_false_memory_frequency": aggregate_metrics.get("false_memory_frequency", 0.0),
            "claim_boundary": "Regression guard locks local scaffold evidence only; it does not prove production readiness.",
        }

    def run_suite(self, suite_path: str | Path) -> Dict[str, Any]:
        suite_path = Path(suite_path)
        suite = json.loads(suite_path.read_text(encoding="utf-8-sig"))

        run_id = "suite_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        run_dir = self.root / "runs" / run_id
        run_dir.mkdir(parents=True, exist_ok=True)

        ledger = RuntimeLedger(self.root / "ledgers" / "aerma_suite_ledger.jsonl")
        compiler = EvidencePackageCompiler()

        repeat_runs = int(suite.get("repeat_runs", 1))
        task_refs = suite.get("tasks", [])

        all_task_results: List[Dict[str, Any]] = []
        metric_records: List[Dict[str, Any]] = []
        attribution_records: List[Dict[str, Any]] = []

        for repeat_index in range(repeat_runs):
            for task_ref in task_refs:
                task_path = self.root / task_ref
                task_result = self.benchmark_runner.run_task(task_path, seed=42 + repeat_index)
                task_result["repeat_index"] = repeat_index
                task_result["task_ref"] = task_ref
                all_task_results.append(task_result)
                metric_records.append(task_result["metrics"])
                attribution_records.append(task_result["attribution"])

                task_id = task_result["task"].get("task_id", "unknown_task")
                task_out_dir = run_dir / "per_task" / task_id / f"repeat_{repeat_index}"
                task_out_dir.mkdir(parents=True, exist_ok=True)

                self._write_json(task_out_dir / "task_result.json", task_result)
                self._write_json(task_out_dir / "attribution.json", task_result["attribution"])
                self._write_json(task_out_dir / "baseline_results.json", task_result["baseline_results"])
                self._write_json(task_out_dir / "benchmark_metrics.json", task_result["metrics"])

                ledger.append("task_completed", {
                    "run_id": run_id,
                    "repeat_index": repeat_index,
                    "task_id": task_id,
                    "metrics": task_result["metrics"],
                    "decision": task_result["result"].get("decision"),
                    "selected_episode_id": task_result["result"].get("selected_episode_id"),
                })

        aggregate_metrics = aggregate_task_metrics(metric_records)

        # v0.1.1 is still a reference scaffold, not a full implementation.
        # The score is raised from 0.80 to 0.85 only because attribution and
        # regression-guard outputs now exist.
        aerma_score = 0.85

        classification = classify_claim(
            aerma_score=aerma_score,
            suite_score=aggregate_metrics["suite_score"],
            regression_frequency=aggregate_metrics["regression_frequency"],
            false_memory_frequency=aggregate_metrics["false_memory_frequency"],
            fallback_correctness=aggregate_metrics["fallback_correctness"],
            abstention_correctness=aggregate_metrics["abstention_correctness"],
            source_attribution_accuracy=aggregate_metrics["source_attribution_accuracy"],
            boundary_separation_score=aggregate_metrics["boundary_separation_score"],
        )

        recursive_stub = RecursiveExecutorStub().run()
        reflection_stub = ReflectionEvaluatorStub().evaluate()
        regression_guard = self._build_regression_guard(aggregate_metrics)

        suite_payload = {
            "run_id": run_id,
            "suite_id": suite.get("suite_id"),
            "version": suite.get("version"),
            "runtime_version": "AERMA-Memory-v0.1.1-hardening",
            "repeat_runs": repeat_runs,
            "task_count": len(task_refs),
            "aggregate_metrics": aggregate_metrics,
            "classification": classification,
            "regression_guard": regression_guard,
            "recursive_executor_stub": recursive_stub,
            "reflection_evaluator_stub": reflection_stub,
            "task_results": all_task_results,
            "attribution_records": attribution_records,
            "claim_boundary": "Suite evidence is local reference-implementation evidence, not broad agent-memory validation.",
        }

        self._write_json(run_dir / "aggregate_metrics.json", aggregate_metrics)
        self._write_json(run_dir / "suite_classification.json", classification)
        self._write_json(run_dir / "regression_guard.json", regression_guard)
        self._write_json(run_dir / "attribution_records.json", attribution_records)

        regression_dir = self.root / "logs" / "phase2" / "regression_guard"
        regression_dir.mkdir(parents=True, exist_ok=True)
        self._write_json(regression_dir / "latest_aerma_regression_guard.json", regression_guard)

        attribution_dir = self.root / "logs" / "phase2" / "attribution"
        attribution_dir.mkdir(parents=True, exist_ok=True)
        self._write_json(attribution_dir / "latest_aerma_attribution.json", attribution_records)

        evidence_path = self.root / "evidence_packages" / f"{run_id}_evidence_package.json"
        compiler.compile(evidence_path, suite_payload)

        ledger.append("suite_completed", {
            "run_id": run_id,
            "suite_score": aggregate_metrics["suite_score"],
            "classification": classification,
            "evidence_package": str(evidence_path),
            "regression_guard": str(run_dir / "regression_guard.json"),
            "attribution_records": str(run_dir / "attribution_records.json"),
        })

        return suite_payload
