import argparse
import json
from pathlib import Path

from aerma.benchmarks.benchmark_runner import BenchmarkRunner
from aerma.benchmarks.suite_runner import SuiteRunner


def main() -> None:
    parser = argparse.ArgumentParser(prog="aerma")
    sub = parser.add_subparsers(dest="command", required=True)

    run_benchmark = sub.add_parser("run-benchmark")
    run_benchmark.add_argument("--task", required=True)

    run_suite = sub.add_parser("run-suite")
    run_suite.add_argument("--suite", required=True)

    args = parser.parse_args()

    if args.command == "run-benchmark":
        runner = BenchmarkRunner()
        result = runner.run_task(args.task)
        print(json.dumps(result["result"], indent=2, sort_keys=True))
        print(json.dumps(result["metrics"], indent=2, sort_keys=True))

    if args.command == "run-suite":
        runner = SuiteRunner(root=Path("."))
        result = runner.run_suite(args.suite)
        print(json.dumps({
            "run_id": result["run_id"],
            "suite_id": result["suite_id"],
            "aggregate_metrics": result["aggregate_metrics"],
            "classification": result["classification"],
        }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
