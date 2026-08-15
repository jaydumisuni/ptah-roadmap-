#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

CANDIDATE = "d12feedb5b66a39d5649b1d3ffea752deb5692c6"
MERGE = "d33122c8cc625d38f2394d57fcbd2a3ef7027b08"
RUN = 31906473232
FINAL_ARTIFACT = 9252486137
FINAL_DIGEST = "sha256:0cec2c980df82a7136fb9c2869eb8ee8ad1bf343faf054b2917a1bf4a5f59c19"

REQUIRED_FILES = [
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
    start = read(root, REQUIRED_FILES[2])

    require("**Status:** ACCEPTED COMPLETE" in acceptance, "A01 acceptance status missing")
    for token in [CANDIDATE, MERGE, str(RUN), str(FINAL_ARTIFACT), FINAL_DIGEST]:
        require(token in acceptance, f"A01 acceptance evidence token missing: {token}")
    require("all 13 workflows on the exact candidate head: PASS" in acceptance, "A01 exact-head workflow closure missing")
    require("A02 — Node identity, Generation and host truth — is READY" in acceptance, "A02 readiness decision missing")
    require("Prime-native integration: NOT QUALIFIED" in acceptance, "Prime integration non-claim missing")
    require("Production: NOT AUTHORIZED" in acceptance, "production non-claim missing")
    require("Release: NOT ACCEPTED" in acceptance, "release non-claim missing")

    require(index.get("status") == "operative_p01d_accepted_a01_complete_a02_ready", "machine authority status mismatch")
    require(index.get("runtime_implementation_authorized") is True, "runtime authorization was lost")
    require(index.get("active_work_unit") == "A02-node-identity-generation-and-host-truth", "machine active work is not A02")
    require(index.get("authorization_blockers") == [], "unexpected authorization blockers remain")

    a01 = index.get("a01")
    require(isinstance(a01, dict), "machine A01 acceptance record missing")
    require(a01.get("status") == "accepted_complete", "machine A01 status mismatch")
    require(a01.get("candidate_exact_head") == CANDIDATE, "machine A01 candidate mismatch")
    require(a01.get("merge_commit") == MERGE, "machine A01 merge mismatch")
    require(a01.get("workflow_run") == RUN, "machine A01 workflow mismatch")
    require(a01.get("all_exact_head_workflows_passed") is True, "machine A01 workflow PASS missing")
    require(a01.get("final_proof_artifact_id") == FINAL_ARTIFACT, "machine A01 final artifact mismatch")
    require(a01.get("final_proof_artifact_digest") == FINAL_DIGEST, "machine A01 final artifact digest mismatch")
    require(a01.get("runtime_semantics_claimed") is False, "A01 falsely claims runtime semantics")
    require(a01.get("prime_integration_qualified") is False, "A01 falsely claims Prime integration")
    require(a01.get("production_or_release_accepted") is False, "A01 falsely claims production/release")

    programmes = index.get("programmes")
    require(isinstance(programmes, dict), "machine programme states missing")
    require(programmes.get("A01") == "accepted_complete", "machine A01 programme state mismatch")
    require(programmes.get("A02") == "ready", "machine A02 readiness missing")
    require(programmes.get("P01P") == "open_deferred", "P01P boundary drifted")

    boundaries = index.get("claim_boundaries")
    require(isinstance(boundaries, dict), "claim boundaries missing")
    for key in ["node_runtime_proven", "prime_deployment_qualified", "production_authorized", "release_accepted", "historical_ubuntu_proof_passed", "prime_host_id_equals_ptah_node_id"]:
        require(boundaries.get(key) is False, f"forbidden claim became true: {key}")

    require("A01 — Repository, contracts and reproducible scaffold: **FROZEN / PROVEN / COMPLETE**" in start, "AI recovery entry lacks A01 completion")
    require("Active work unit: **A02 — Node identity, Generation and host truth**" in start, "AI recovery entry is not on A02")
    require("A02 status: **READY**" in start, "AI recovery entry lacks A02 readiness")
    require(CANDIDATE in start and MERGE in start and str(RUN) in start, "AI recovery entry A01 evidence binding missing")

    return {
        "record_type": "ptah.a01.acceptance_current_authority_validation",
        "status": "a01_accepted_complete_a02_ready",
        "a01_candidate": CANDIDATE,
        "a01_merge": MERGE,
        "a01_workflow_run": RUN,
        "a01_final_artifact": FINAL_ARTIFACT,
        "a01_final_artifact_digest": FINAL_DIGEST,
        "a01_complete": True,
        "a02_ready": True,
        "runtime_implementation_authorized": True,
        "node_runtime_proven": False,
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
