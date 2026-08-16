#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

CANDIDATE = "80adcd0aefe0053b2354b26676bfc9e28d9b8ec3"
MERGE = "1603ac80b5d2c5925fde62392ec0fff4b07a1219"
RUN = 31909732507
ARTIFACT = 9253318003
DIGEST = "sha256:dbafc252ab2fb3e2eb9938de6648bca0105f698d27321be9eb2bdb1a3782ba0a"
SERGEANT = "56961f12e5cc97cde447e5150e7a00ef3a8deba8"

REQUIRED_FILES = [
    "planning/A02-NODE-IDENTITY-GENERATION-HOST-TRUTH-ACCEPTANCE.md",
    "master-plan-index-amendment-2026-08-15.json",
]


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def read(root: Path, path: str) -> str:
    target = root / path
    require(target.is_file(), f"missing required file: {path}")
    return target.read_text(encoding="utf-8")


def validate(root: Path) -> dict:
    acceptance = read(root, REQUIRED_FILES[0])
    index = json.loads(read(root, REQUIRED_FILES[1]))

    require("**Status:** ACCEPTED COMPLETE" in acceptance, "A02 acceptance status missing")
    for token in [CANDIDATE, MERGE, str(RUN), str(ARTIFACT), DIGEST, SERGEANT]:
        require(token in acceptance, f"A02 acceptance evidence token missing: {token}")

    a02 = index.get("a02")
    require(isinstance(a02, dict), "machine A02 acceptance record missing")
    require(a02.get("status") == "accepted_complete", "machine A02 status mismatch")
    require(a02.get("candidate_exact_head") == CANDIDATE, "machine A02 candidate mismatch")
    require(a02.get("merge_commit") == MERGE, "machine A02 merge mismatch")
    require(a02.get("workflow_run") == RUN, "machine A02 workflow mismatch")
    require(a02.get("proof_artifact_id") == ARTIFACT, "machine A02 artifact mismatch")
    require(a02.get("proof_artifact_digest") == DIGEST, "machine A02 artifact digest mismatch")
    require(a02.get("sergeant_review_commit") == SERGEANT, "Sergeant review commit mismatch")
    require(a02.get("sergeant_review_status") == "pass", "Sergeant review is not PASS")
    require(a02.get("sergeant_blocking_findings") == 0, "Sergeant blocking findings present")
    require(a02.get("sergeant_needs_work_findings") == 0, "Sergeant needs-work findings present")

    require(index.get("runtime_implementation_authorized") is True, "runtime authorization was lost")
    programmes = index.get("programmes")
    require(isinstance(programmes, dict), "machine programme states missing")
    require(programmes.get("A01") == "accepted_complete", "A01 prerequisite drifted")
    require(programmes.get("A02") == "accepted_complete", "A02 completion missing")

    boundaries = index.get("claim_boundaries")
    require(isinstance(boundaries, dict), "claim boundaries missing")
    require(boundaries.get("node_runtime_proven") is True, "accepted A02 Node runtime proof missing")
    require(index.get("p01p", {}).get("status") == "open_deferred", "P01P boundary drifted")

    return {
        "record_type": "ptah.a02.acceptance_invariant_validation",
        "status": "a02_accepted_complete",
        "a02_candidate": CANDIDATE,
        "a02_merge": MERGE,
        "a02_complete": True,
        "runtime_implementation_authorized": True,
        "node_runtime_proven": True,
        "p01p_open": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    report = validate(Path(args.repo_root).resolve())
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
