import json
from pathlib import Path
from typing import Dict, Any

from aerma.core.episode import AgentEpisode
from aerma.core.memory_store import AgentMemoryStore
from aerma.core.metric_manifest import MetricManifest
from aerma.core.retrieval_engine import RetrievalEngine
from aerma.drift.drift_geometry import DriftGeometryEngine
from aerma.gate.action_gate import ActionGate
from aerma.gate.source_fallback import SourceFallback
from aerma.benchmarks.baselines import default_baselines
from aerma.benchmarks.scoring import score_task


class BenchmarkRunner:
    def __init__(self, manifest: MetricManifest | None = None) -> None:
        self.manifest = manifest or MetricManifest()
        self.retrieval = RetrievalEngine()
        self.drift = DriftGeometryEngine()
        self.gate = ActionGate(self.manifest)
        self.fallback = SourceFallback()

    def load_task(self, path: str | Path) -> Dict[str, Any]:
        return json.loads(Path(path).read_text(encoding="utf-8-sig"))

    def run_task(self, task_path: str | Path, seed: int = 42) -> Dict[str, Any]:
        task = self.load_task(task_path)
        episodes = [AgentEpisode.from_dict(item) for item in task.get("episodes", [])]

        store = AgentMemoryStore()
        store.load_episodes(episodes)

        query_obj = task.get("queries", [{}])[0]
        query = query_obj.get("query", "")
        expected_behavior = query_obj.get("expected_behavior")

        candidates = self.retrieval.retrieve(query, store.all_episodes(), top_k=3)
        top = candidates[0] if candidates else None

        if top is None:
            decision = "fallback"
            selected_episode_id = None
            selected_source_ref = None
            drift_report = self.drift.compute(0.0)
            gate_decision = self.gate.decide(drift_report, source_missing=True)
        else:
            selected_episode_id = top.episode.episode_id
            selected_source_ref = top.episode.source_ref
            drift_report = self.drift.compute(top.score)
            gate_decision = self.gate.decide(
                drift_report,
                expected_behavior=expected_behavior,
                ambiguous=(expected_behavior == "fallback"),
                source_missing=(not selected_source_ref),
            )
            decision = gate_decision.decision

        if decision == "fallback":
            fallback_result = self.fallback.fallback(gate_decision.reason)
            message = fallback_result.message
        elif decision == "abstain":
            fallback_result = self.fallback.abstain(gate_decision.reason)
            message = fallback_result.message
        else:
            message = "Source-bound memory selected."

        result = {
            "task_id": task.get("task_id"),
            "task_family": task.get("task_family"),
            "query": query,
            "decision": decision,
            "gate_reason": gate_decision.reason,
            "selected_episode_id": selected_episode_id,
            "selected_source_ref": selected_source_ref,
            "retrieval_drift": drift_report.retrieval_drift,
            "omega": drift_report.omega,
            "message": message,
        }

        metrics = score_task(result, task)

        baseline_results = []
        for baseline in default_baselines():
            baseline_results.append(
                baseline.retrieve(query, store.all_episodes(), {"seed": seed})
            )

        return {
            "task": task,
            "result": result,
            "metrics": metrics,
            "baseline_results": baseline_results,
        }
