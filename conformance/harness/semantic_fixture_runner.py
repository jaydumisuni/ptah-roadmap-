from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from semantic_rules import evaluate


def run(root: Path) -> dict:
    results: list[dict] = []
    executed = skipped = failed = 0
    fixture_root = root / "conformance" / "fixtures" / "phase-0b"
    for path in sorted(fixture_root.rglob("*.json")):
        try:
            suite = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            failed += 1
            results.append({"path": str(path.relative_to(root)), "status": "fail", "message": f"invalid JSON: {exc}"})
            continue
        for case in suite.get("cases", []):
            rule = case.get("rule")
            payload = case.get("payload")
            if rule is None and payload is None:
                skipped += 1
                continue
            case_id = case.get("id", "<missing>")
            if not isinstance(rule, str) or not isinstance(payload, dict):
                failed += 1
                results.append({"path": str(path.relative_to(root)), "case_id": case_id, "status": "fail", "message": "semantic fixture requires string rule and object payload"})
                continue
            passed, message = evaluate(rule, payload)
            expected_valid = case.get("expected") == "valid"
            matched = passed == expected_valid
            executed += 1
            if not matched:
                failed += 1
            results.append({
                "path": str(path.relative_to(root)),
                "case_id": case_id,
                "rule": rule,
                "status": "pass" if matched else "fail",
                "rule_result": passed,
                "expected": case.get("expected"),
                "message": message,
            })
    return {"runner_version": "0.1.0", "summary": {"executed": executed, "skipped_specification_only": skipped, "failed": failed, "status": "pass" if failed == 0 else "fail"}, "results": results}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run executable semantic Ptah fixtures")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)
    report = run(args.root.resolve())
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["summary"]["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
