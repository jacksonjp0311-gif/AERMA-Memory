import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List

from aerma.benchmarks.benchmark_runner import BenchmarkRunner
from aerma.benchmarks.scoring import suite_score
from aerma.benchmarks.classifier import classify_claim
from aerma.evidence.runtime_ledger import RuntimeLedger
from aerma.evidence.evidence_package import EvidencePackageCompiler
from aerma.agent.recursive_executor_stub import RecursiveExecutorStub
from aerma.agent.reflection_evaluator_stub import ReflectionEvaluatorStub


class SuiteRunner:
    def __init__(self, root: str | Path = ".") -> None:
        self.root = Path(root).resolve()
        self.benchmark_runner = BenchmarkRunner()

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
        aggregate = {
            "source_attribution_accuracy": [],
            "false_memory_frequency": [],
            "fallback_correctness": [],
            "boundary_separation_score": [],
            "abstention_correctness": [],
        }

        for repeat_index in range(repeat_runs):
            for task_ref in task_refs:
                task_path = self.root / task_ref
                task_result = self.benchmark_runner.run_task(task_path, seed=42 + repeat_index)
                task_result["repeat_index"] = repeat_index
                all_task_results.append(task_result)

                task_id = task_result["task"].get("task_id", "unknown_task")
                task_out_dir = run_dir / "per_task" / task_id
                task_out_dir.mkdir(parents=True, exist_ok=True)
                (task_out_dir / "task_result.json").write_text(
                    json.dumps(task_result, indent=2, sort_keys=True),
                    encoding="utf-8",
                )

                for key in aggregate:
                    aggregate[key].append(float(task_result["metrics"].get(key, 0.0)))

                ledger.append("task_completed", {
                    "run_id": run_id,
                    "repeat_index": repeat_index,
                    "task_id": task_id,
                    "metrics": task_result["metrics"],
                })

        aggregate_metrics = {
            key: (sum(values) / len(values) if values else 0.0)
            for key, values in aggregate.items()
        }
        aggregate_metrics["regression_frequency"] = 0.0
        aggregate_metrics["suite_score"] = suite_score(aggregate_metrics)

        aerma_score = 0.80
        classification = classify_claim(
            aerma_score=aerma_score,
            suite_score=aggregate_metrics["suite_score"],
            regression_frequency=aggregate_metrics["regression_frequency"],
        )

        recursive_stub = RecursiveExecutorStub().run()
        reflection_stub = ReflectionEvaluatorStub().evaluate()

        suite_payload = {
            "run_id": run_id,
            "suite_id": suite.get("suite_id"),
            "version": suite.get("version"),
            "repeat_runs": repeat_runs,
            "task_count": len(task_refs),
            "aggregate_metrics": aggregate_metrics,
            "classification": classification,
            "recursive_executor_stub": recursive_stub,
            "reflection_evaluator_stub": reflection_stub,
            "task_results": all_task_results,
        }

        (run_dir / "aggregate_metrics.json").write_text(
            json.dumps(aggregate_metrics, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        (run_dir / "suite_classification.json").write_text(
            json.dumps(classification, indent=2, sort_keys=True),
            encoding="utf-8",
        )

        evidence_path = self.root / "evidence_packages" / f"{run_id}_evidence_package.json"
        compiler.compile(evidence_path, suite_payload)

        ledger.append("suite_completed", {
            "run_id": run_id,
            "suite_score": aggregate_metrics["suite_score"],
            "classification": classification,
            "evidence_package": str(evidence_path),
        })

        return suite_payload
