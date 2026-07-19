from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from ptah_conformance_compat import Harness as CompatHarness


class Harness(CompatHarness):
    def validate_fixtures(self) -> None:
        ids: set[str] = set()
        accepted = {
            "valid", "invalid", "semantic_valid", "semantic_invalid",
            "structurally_valid_semantically_rejected_for_current_state",
            "disposition_required",
        }
        for path, doc in self.documents.items():
            if "conformance/fixtures/phase-0b" not in path.as_posix():
                continue
            if not isinstance(doc, dict) or not isinstance(doc.get("cases"), list) or not doc["cases"]:
                self.add("FIXTURE_CASES", "fail", path, "fixture suite has no cases")
                continue
            for case in doc["cases"]:
                if not isinstance(case, dict) or not isinstance(case.get("id"), str):
                    self.add("FIXTURE_ID", "fail", path, "case missing id")
                    continue
                global_id = f"{doc.get('suite_id', path)}::{case['id']}"
                if global_id in ids:
                    self.add("FIXTURE_ID_UNIQUE", "fail", path, f"duplicate {case['id']}")
                ids.add(global_id)
                expected = case.get("expected")
                if expected not in accepted:
                    self.add("FIXTURE_EXPECTED", "fail", path, f"{case['id']}: unsupported expected value {expected!r}")
                    continue
                if expected in {"invalid", "semantic_invalid", "structurally_valid_semantically_rejected_for_current_state"}:
                    if not isinstance(case.get("expected_code"), str):
                        self.add("FIXTURE_ERROR_CODE", "fail", path, f"{case['id']}: invalid case lacks expected_code")
                        continue
                if expected == "disposition_required" and not (
                    isinstance(case.get("expected_code"), str) or isinstance(case.get("expected_disposition"), str)
                ):
                    self.add("FIXTURE_DISPOSITION_CODE", "fail", path, f"{case['id']}: disposition-required case lacks typed disposition")
                    continue
                self.add("FIXTURE_CASE", "pass", path, case["id"])

    def run(self) -> dict[str, Any]:
        report = super().run()
        report["harness_version"] = "0.1.3"
        return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run offline Ptah Phase 0B contract conformance checks")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)
    report = Harness(args.root).run()
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["summary"]["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
