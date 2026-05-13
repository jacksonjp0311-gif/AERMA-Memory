from aerma.benchmarks.suite_runner import SuiteRunner
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", default="tasks/suite_v1_2.json")
    args = parser.parse_args()

    result = SuiteRunner(root=Path(".")).run_suite(args.suite)
    print(json.dumps({
        "run_id": result["run_id"],
        "aggregate_metrics": result["aggregate_metrics"],
        "classification": result["classification"]
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
