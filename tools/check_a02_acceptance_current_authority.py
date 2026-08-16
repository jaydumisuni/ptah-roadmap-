#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

CANDIDATE = "80adcd0aefe0053b2354b26676bfc9e28d9b8ec3"
TREE = "9b477dc1bf9ab2dd466da9615dbbd0e881216ed6"
MERGE = "1603ac80b5d2c5925fde62392ec0fff4b07a1219"
RUN = 31909732507
ARTIFACT = 9253318003
ARTIFACT_DIGEST = "sha256:dbafc252ab2fb3e2eb9938de6648bca0105f698d27321be9eb2bdb1a3782ba0a"
CARGO_LOCK_SHA256 = "73bfc13e9e73a465c8271a3a26a2a688b3abf2c3734a016307aba94c4a8c5c32"
ORACLE_PAYLOAD_COMMIT = "8522f104474f404a73c74fadc3bcf9c3e81664b3"
BUNDLE_SHA256 = "04fa242442f916391c5cbc130c3ff32a6b98cde0b1149d81aa0ce9a479875671"
PHYSICAL_RECEIPT = "0000-ptah-a02-kratos-physical-proof-20260816-013450z"
SERGEANT_COMMIT = "56961f12e5cc97cde447e5150e7a00ef3a8deba8"
SERGEANT_EVIDENCE_COMMIT = "a6f2a3d216e7e4061771d76f1dead3f5c838409a"

REQUIRED_FILES = [
    "planning/A02-NODE-IDENTITY-GENERATION-HOST-TRUTH-ACCEPTANCE.md",
    "master-plan-index-amendment-2026-08-16.json",
    "planning/A01-REPOSITORY-CONTRACTS-SCAFFOLD-ACCEPTANCE.md",
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
    a01_acceptance = read(root, REQUIRED_FILES[2])
    a01_index = json.loads(read(root, REQUIRED_FILES[3]))
    start = read(root, REQUIRED_FILES[4])

    require("**Status:** ACCEPTED COMPLETE" in acceptance, "A02 acceptance status missing")
    for token in [
        CANDIDATE,
        TREE,
        MERGE,
        str(RUN),
        str(ARTIFACT),
        ARTIFACT_DIGEST,
        CARGO_LOCK_SHA256,
        ORACLE_PAYLOAD_COMMIT,
        BUNDLE_SHA256,
        PHYSICAL_RECEIPT,
        SERGEANT_COMMIT,
        SERGEANT_EVIDENCE_COMMIT,
    ]:
        require(token in acceptance, f"A02 acceptance evidence token missing: {token}")
    require("A02 is accepted complete. A03 — Ledger, schema versions and crash-safe migrations — is READY." in acceptance, "A03 readiness decision missing")
    require("81 registry packages" in acceptance and "0 Git packages" in acceptance, "frozen external Cargo universe missing")
    require("ptah-identifiers: 9 passed / 0 failed" in acceptance, "identity physical proof missing")
    require("ptah-node-agent: 17 passed / 0 failed" in acceptance, "node-agent physical proof missing")
    require("verdict: PASS" in acceptance and "blocking: 0" in acceptance and "needs_work: 0" in acceptance, "Sergeant final reconciliation missing")
    require("A03 persistence/migrations: NOT YET PROVEN" in acceptance, "A03 non-claim missing")
    require("A04 Activity execution: NOT YET PROVEN" in acceptance, "A04 non-claim missing")
    require("Prime-native deployment qualification: NOT CLAIMED" in acceptance, "Prime deployment non-claim missing")
    require("Production: NOT AUTHORIZED" in acceptance, "production non-claim missing")
    require("Release: NOT ACCEPTED" in acceptance, "release non-claim missing")

    # Preserve the accepted A01 prerequisite as historical authority.
    require("**Status:** ACCEPTED COMPLETE" in a01_acceptance, "A01 prerequisite acceptance missing")
    require(a01_index.get("a01", {}).get("status") == "accepted_complete", "A01 prerequisite machine state missing")
    require(a01_index.get("programmes", {}).get("A02") == "ready", "A01 did not historically authorize A02")

    require(index.get("status") == "operative_p01d_accepted_a01_complete_a02_complete_a03_ready", "machine authority status mismatch")
    require(index.get("supersedes_amendment") == "master-plan-index-amendment-2026-08-15.json", "machine supersession chain missing")
    require(index.get("applies_after_ptah_space_merge") == MERGE, "machine merge binding mismatch")
    require(index.get("runtime_implementation_authorized") is True, "runtime authorization was lost")
    require(index.get("active_work_unit") == "A03-ledger-schema-versions-crash-safe-migrations", "active work is not A03")
    require(index.get("authorization_blockers") == [], "unexpected authorization blockers remain")

    require(index.get("p01d", {}).get("status") == "accepted_complete", "P01D completion was lost")
    require(index.get("p01d", {}).get("physical_development_host_accepted") is True, "P01D host acceptance was lost")
    require(index.get("p01p", {}).get("status") == "open_deferred", "P01P status drifted")
    require(index.get("p01p", {}).get("blocks_programme_a") is False, "P01P incorrectly blocks Programme A")
    require(index.get("p01p", {}).get("prime_native_integration_qualified") is False, "P01P falsely claims Prime integration")

    a01 = index.get("a01")
    require(isinstance(a01, dict) and a01.get("status") == "accepted_complete", "A01 completion missing from current machine authority")
    require(a01.get("merge_commit") == "d33122c8cc625d38f2394d57fcbd2a3ef7027b08", "A01 merge binding drifted")

    a02 = index.get("a02")
    require(isinstance(a02, dict), "machine A02 acceptance record missing")
    require(a02.get("status") == "accepted_complete", "machine A02 status mismatch")
    require(a02.get("ptah_space_pr") == 24, "machine A02 PR mismatch")
    require(a02.get("candidate_exact_head") == CANDIDATE, "machine A02 candidate mismatch")
    require(a02.get("candidate_tree") == TREE, "machine A02 tree mismatch")
    require(a02.get("merge_commit") == MERGE, "machine A02 merge mismatch")
    require(a02.get("workflow_run") == RUN, "machine A02 workflow mismatch")
    require(a02.get("all_exact_head_workflows_passed") is True, "machine A02 workflow PASS missing")
    require(a02.get("exact_head_artifact_id") == ARTIFACT, "machine A02 artifact mismatch")
    require(a02.get("exact_head_artifact_digest") == ARTIFACT_DIGEST, "machine A02 artifact digest mismatch")
    require(a02.get("external_registry_package_count") == 81, "machine external registry package count mismatch")
    require(a02.get("git_dependency_count") == 0, "machine Git dependency count mismatch")
    require(a02.get("cargo_lock_sha256") == CARGO_LOCK_SHA256, "machine Cargo.lock digest mismatch")

    physical = a02.get("physical_proof")
    require(isinstance(physical, dict), "machine A02 physical proof missing")
    require(physical.get("oracle_payload_commit") == ORACLE_PAYLOAD_COMMIT, "physical payload commit mismatch")
    require(physical.get("bundle_sha256") == BUNDLE_SHA256, "physical bundle digest mismatch")
    require(physical.get("receipt_id") == PHYSICAL_RECEIPT, "physical receipt mismatch")
    require(physical.get("transport") == "oracle.live.v1", "physical transport mismatch")
    require(physical.get("github_interactive_path_used") is False, "interactive Git fallback was falsely used")
    require(physical.get("architecture") == "x86_64", "physical architecture mismatch")
    require(physical.get("identifiers_tests_passed") == 9, "physical identity test count mismatch")
    require(physical.get("node_agent_tests_passed") == 17, "physical node-agent test count mismatch")
    require(physical.get("test_failures") == 0, "physical proof contains failures")

    review = a02.get("independent_review")
    require(isinstance(review, dict), "machine A02 independent review missing")
    require(review.get("sergeant_commit") == SERGEANT_COMMIT, "Sergeant reviewer commit mismatch")
    require(review.get("evidence_commit") == SERGEANT_EVIDENCE_COMMIT, "Sergeant evidence commit mismatch")
    require(review.get("model_support_enabled") is False, "Sergeant review was not model-free")
    require(review.get("depth") == "maximum", "Sergeant review depth mismatch")
    require(review.get("verdict") == "PASS", "Sergeant verdict is not PASS")
    require(review.get("consensus") == "PASS", "Sergeant consensus is not PASS")
    require(review.get("blocking") == 0, "Sergeant blocking findings remain")
    require(review.get("needs_work") == 0, "Sergeant needs-work findings remain")

    require(a02.get("ledger_persistence_claimed") is False, "A02 falsely claims A03 persistence")
    require(a02.get("activity_runtime_claimed") is False, "A02 falsely claims A04 Activity runtime")
    require(a02.get("prime_integration_qualified") is False, "A02 falsely claims Prime integration")
    require(a02.get("production_or_release_accepted") is False, "A02 falsely claims production/release")

    programmes = index.get("programmes")
    require(isinstance(programmes, dict), "machine programme states missing")
    require(programmes.get("P01D") == "accepted_complete", "machine P01D programme state mismatch")
    require(programmes.get("A01") == "accepted_complete", "machine A01 programme state mismatch")
    require(programmes.get("A02") == "accepted_complete", "machine A02 programme state mismatch")
    require(programmes.get("A03") == "ready", "machine A03 readiness missing")
    require(programmes.get("P01P") == "open_deferred", "machine P01P programme state drifted")

    boundaries = index.get("claim_boundaries")
    require(isinstance(boundaries, dict), "claim boundaries missing")
    require(boundaries.get("node_runtime_proven") is True, "A02 Node runtime proof claim missing")
    for key in [
        "ledger_persistence_proven",
        "activity_runtime_proven",
        "prime_deployment_qualified",
        "production_authorized",
        "release_accepted",
        "historical_ubuntu_proof_passed",
        "prime_host_id_equals_ptah_node_id",
    ]:
        require(boundaries.get(key) is False, f"forbidden later claim became true: {key}")

    require("A02 — Node identity, Generation and host truth: **FROZEN / PROVEN / COMPLETE**" in start, "AI recovery entry lacks A02 completion")
    require("Active work unit: **A03 — Ledger, schema versions and crash-safe migrations**" in start, "AI recovery entry is not on A03")
    require("A03 status: **READY**" in start, "AI recovery entry lacks A03 readiness")
    require("Begin **A03 — Ledger, schema versions and crash-safe migrations**." in start, "AI recovery exact next operation is not A03")
    for token in [CANDIDATE, MERGE, str(RUN), PHYSICAL_RECEIPT, SERGEANT_COMMIT]:
        require(token in start, f"AI recovery evidence token missing: {token}")
    require("Prime Host ID != Ptah Node ID" in start, "identity separation rule missing")

    return {
        "record_type": "ptah.a02.acceptance_current_authority_validation",
        "status": "a02_accepted_complete_a03_ready",
        "a02_candidate": CANDIDATE,
        "a02_tree": TREE,
        "a02_merge": MERGE,
        "a02_workflow_run": RUN,
        "a02_artifact": ARTIFACT,
        "a02_artifact_digest": ARTIFACT_DIGEST,
        "a02_complete": True,
        "a03_ready": True,
        "runtime_implementation_authorized": True,
        "node_runtime_proven": True,
        "ledger_persistence_proven": False,
        "activity_runtime_proven": False,
        "p01p_open": True,
        "prime_deployment_qualified": False,
        "production_authorized": False,
        "release_accepted": False,
        "physical_proof_passed": True,
        "sergeant_review_passed": True,
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
