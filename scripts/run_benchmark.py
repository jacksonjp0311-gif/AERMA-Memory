from aerma.benchmarks.benchmark_runner import BenchmarkRunner
import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True)
    args = parser.parse_args()

    result = BenchmarkRunner().run_task(args.task)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
