from typing import Dict, Any


class RecursiveExecutorStub:
    def run(self, root_goal: str = "") -> Dict[str, Any]:
        return {
            "recursive_executor": "stub",
            "root_goal": root_goal,
            "subtasks": [],
            "max_depth": 1,
            "recursion_executed": False,
            "reason": "AERMA v1.2 includes stub only; full recursive execution is staged for a later version.",
        }
