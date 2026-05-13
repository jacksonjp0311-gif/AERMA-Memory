from pathlib import Path
import json


def main() -> None:
    path = Path("logs/phase2/regression_guard/latest_aerma_regression_guard.json")
    if not path.exists():
        raise SystemExit(
            "No regression guard found. Run: python -m aerma.cli.main run-suite --suite .\\tasks\\suite_v1_2.json"
        )

    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
