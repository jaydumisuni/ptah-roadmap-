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
    "AI_START_HERE.md",
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
    start = read(root, REQUIRED_FILES[2])

    require("**Status:** ACCEPTED COMPLETE" in acceptance, "A02 acceptance status missing")
    for token in [CANDIDATE, MERGE, str(RUN), str(ARTIFACT), DIGEST, SERGEANT]:
        require(token in acceptance, f"A02 acceptance evidence token missing: {token}")
    require("all 13 repository workflows on the exact candidate head: PASS" in acceptance, "A02 exact-head workflow closure missing")
    require("`ptah-identifiers`: 9/9 tests" in acceptance, "Kratos identifier proof missing")
    require("`ptah-node-agent`: 17/17 tests" in acceptance, "Kratos node-agent proof missing")
    require("blocking findings: 0" in acceptance and "needs-work findings: 0" in acceptance, "Sergeant clean review missing")
    require("A03 — Ledger, schema versions and crash-safe migrations — is READY" in acceptance, "A03 readiness decision missing")
    require("Prime-native integration: NOT QUALIFIED" in acceptance, "Prime integration non-claim missing")
    require("Production: NOT AUTHORIZED" in acceptance, "production non-claim missing")
    require("Release: NOT ACCEPTED" in acceptance, "release non-claim missing")

    require(index.get("status") == "operative_p01d_accepted_a01_complete_a02_complete_a03_ready", "machine authority status mismatch")
    require(index.get("runtime_implementation_authorized") is True, "runtime authorization was lost")
    require(index.get("active_work_unit") == "A03-ledger-schema-versions-and-crash-safe-migrations", "machine active work is not A03")
    require(index.get("authorization_blockers") == [], "unexpected authorization blockers remain")

    a02 = index.get("a02")
    require(isinstance(a02, dict), "machine A02 acceptance record missing")
    require(a02.get("status") == "accepted_complete", "machine A02 status mismatch")
    require(a02.get("candidate_exact_head") == CANDIDATE, "machine A02 candidate mismatch")
    require(a02.get("merge_commit") == MERGE, "machine A02 merge mismatch")
    require(a02.get("workflow_run") == RUN, "machine A02 workflow mismatch")
    require(a02.get("all_exact_head_workflows_passed") is True, "machine A02 workflow PASS missing")
    require(a02.get("proof_artifact_id") == ARTIFACT, "machine A02 artifact mismatch")
    require(a02.get("proof_artifact_digest") == DIGEST, "machine A02 artifact digest mismatch")
    require(a02.get("kratos_identifiers_tests_passed") == a02.get("kratos_identifiers_tests_total") == 9, "Kratos identifier count mismatch")
    require(a02.get("kratos_node_agent_tests_passed") == a02.get("kratos_node_agent_tests_total") == 17, "Kratos node-agent count mismatch")
    require(a02.get("sergeant_review_commit") == SERGEANT, "Sergeant review commit mismatch")
    require(a02.get("sergeant_review_status") == "pass", "Sergeant review is not PASS")
    require(a02.get("sergeant_blocking_findings") == 0, "Sergeant blocking findings present")
    require(a02.get("sergeant_needs_work_findings") == 0, "Sergeant needs-work findings present")
    require(a02.get("a03_persistence_implemented") is False, "A02 falsely claims A03 persistence")
    require(a02.get("a04_activity_execution_implemented") is False, "A02 falsely claims A04 execution")
    require(a02.get("prime_integration_qualified") is False, "A02 falsely claims Prime integration")
    require(a02.get("production_or_release_accepted") is False, "A02 falsely claims production/release")

    programmes = index.get("programmes")
    require(isinstance(programmes, dict), "machine programme states missing")
    require(programmes.get("A01") == "accepted_complete", "A01 prerequisite drifted")
    require(programmes.get("A02") == "accepted_complete", "A02 completion missing")
    require(programmes.get("A03") == "ready", "A03 readiness missing")
    require(programmes.get("P01P") == "open_deferred", "P01P boundary drifted")

    boundaries = index.get("claim_boundaries")
    require(isinstance(boundaries, dict), "claim boundaries missing")
    require(boundaries.get("node_runtime_proven") is True, "accepted A02 Node runtime proof missing")
    for key in ["ledger_runtime_proven", "activity_runtime_proven", "prime_deployment_qualified", "production_authorized", "release_accepted", "historical_ubuntu_proof_passed", "prime_host_id_equals_ptah_node_id"]:
        require(boundaries.get(key) is False, f"forbidden claim became true: {key}")

    require("A02 — Node identity, Generation and host truth: **FROZEN / PROVEN / COMPLETE**" in start, "AI recovery entry lacks A02 completion")
    require("Active work unit: **A03 — Ledger, schema versions and crash-safe migrations**" in start, "AI recovery entry is not on A03")
    require("A03 status: **READY**" in start, "AI recovery entry lacks A03 readiness")
    for token in [CANDIDATE, MERGE, str(RUN), str(ARTIFACT), DIGEST, SERGEANT]:
        require(token in start, f"AI recovery A02 evidence missing: {token}")

    return {
        "record_type": "ptah.a02.acceptance_current_authority_validation",
        "status": "a02_accepted_complete_a03_ready",
        "a02_candidate": CANDIDATE,
        "a02_merge": MERGE,
        "a02_workflow_run": RUN,
        "a02_artifact": ARTIFACT,
        "a02_artifact_digest": DIGEST,
        "a02_complete": True,
        "a03_ready": True,
        "runtime_implementation_authorized": True,
        "node_runtime_proven": True,
        "ledger_runtime_proven": False,
        "p01p_open": True,
        "prime_deployment_qualified": False,
        "production_authorized": False,
        "release_accepted": False,
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
