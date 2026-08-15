#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

PROOF_COMMIT = "f6064c98c58e369f621b1800632a0169d8fb0785"
REPORT_SHA256 = "598dbde9d5b3061ba9dfd29baf31ce2007718f0010db67ee96f2dc2b13e00083"
NEGATIVE_REPORT_SHA256 = "cc1a91ac0e19bd3c108c4a85ccd2fa54fd688975398a90eb0da41c34e261a46d"
ORACLE_RECEIPT_ID = "0000-ptah-p01d-final-kratos-proof-20260815-194730z"
ORACLE_RECEIPT_BLOB = "bf81cc24f7fce84d777da3c668b8716b475e8002"

REQUIRED_FILES = [
    "CURRENT_STATE_CLOSURE_2026-08-15.md",
    "master-plan-index-amendment-2026-08-15.json",
    "AI_START_HERE.md",
    "decisions/ADR-0038-PRIME-HOST-DEVELOPMENT-QUALIFICATION.md",
    "decisions/ADR-0039-P01D-ACCEPTANCE-A01-AUTHORIZATION.md",
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
    closure = read(root, REQUIRED_FILES[0])
    index = json.loads(read(root, REQUIRED_FILES[1]))
    start = read(root, REQUIRED_FILES[2])
    adr38 = read(root, REQUIRED_FILES[3])
    adr39 = read(root, REQUIRED_FILES[4])

    require("P01D ACCEPTED — A01 AUTHORIZED" in closure, "operative P01D/A01 closure status missing")
    require("Runtime implementation: AUTHORIZED" in closure, "runtime authorization missing from closure")
    require("A01: READY" in closure, "A01 READY state missing from closure")
    require("P01P Prime-native integration proof: OPEN / DEFERRED" in closure, "P01P deferred/open boundary missing")
    require("historical Ubuntu" in closure and "not" in closure.lower(), "historical Ubuntu non-pass boundary missing")

    for token in [PROOF_COMMIT, REPORT_SHA256, NEGATIVE_REPORT_SHA256, ORACLE_RECEIPT_ID, ORACLE_RECEIPT_BLOB]:
        require(token in closure, f"closure evidence token missing: {token}")
        require(token in adr39, f"ADR-0039 evidence token missing: {token}")

    require("action: APPROVE" in closure, "combined independent review approval missing")
    require("status: pass" in closure, "combined independent review pass status missing")
    require("required_actions: []" in closure, "combined independent review required-actions closure missing")
    require("two non-blocking heuristics" in closure.lower(), "retained Sergeant advisory notes missing")

    require("**Status:** ACCEPTED" in adr38, "ADR-0038 is not accepted")
    require("P01D — physical development-host qualification" in adr38, "ADR-0038 P01D authority missing")
    require("P01P — Prime-native integration qualification" in adr38, "ADR-0038 P01P authority missing")

    require("**Status:** ACCEPTED ON MERGE" in adr39, "ADR-0039 acceptance status missing")
    require("Accept P01D and explicitly authorize A01 runtime implementation." in adr39, "ADR-0039 authorization decision missing")
    require("P01P: OPEN / DEFERRED" in adr39, "ADR-0039 P01P boundary missing")
    require("historical Ubuntu 24.04.4" in adr39 and "claim" in adr39.lower(), "ADR-0039 historical Ubuntu non-pass boundary missing")

    require(index.get("record_type") == "ptah.master_plan_index_amendment", "machine amendment record type mismatch")
    require(index.get("status") == "operative_p01d_accepted_a01_authorized", "machine amendment status mismatch")
    require(index.get("runtime_implementation_authorized") is True, "machine runtime authorization missing")
    require(index.get("active_work_unit") == "A01-repository-contracts-and-reproducible-scaffold", "machine active work is not A01")
    require(index.get("authorization_blockers") == [], "machine authorization blockers remain")

    p01d = index.get("p01d")
    require(isinstance(p01d, dict), "machine P01D state missing")
    require(p01d.get("status") == "accepted_complete", "machine P01D acceptance missing")
    require(p01d.get("physical_development_host_accepted") is True, "machine physical host acceptance missing")
    require(p01d.get("ptah_space_proof_commit") == PROOF_COMMIT, "machine proof commit mismatch")
    require(p01d.get("public_report_sha256") == REPORT_SHA256, "machine report digest mismatch")
    require(p01d.get("oracle_live_receipt_id") == ORACLE_RECEIPT_ID, "machine Oracle receipt mismatch")
    require(p01d.get("oracle_live_receipt_blob_sha") == ORACLE_RECEIPT_BLOB, "machine Oracle receipt blob mismatch")
    require(p01d.get("negative_report_sha256") == NEGATIVE_REPORT_SHA256, "machine negative evidence digest mismatch")
    require(p01d.get("negative_evidence_retained") is True, "machine negative evidence retention missing")
    require(p01d.get("independent_review_action") == "APPROVE", "machine independent review approval missing")
    require(p01d.get("independent_review_status") == "pass", "machine independent review status mismatch")
    require(p01d.get("independent_review_required_actions") == [], "machine independent review still has required actions")
    require(p01d.get("github_interactive_path_used") is False, "Git interactive fallback incorrectly recorded")

    p01p = index.get("p01p")
    require(isinstance(p01p, dict) and p01p.get("status") == "open_deferred", "machine P01P open/deferred state missing")
    require(p01p.get("blocks_a01_start") is False, "P01P incorrectly blocks A01")
    require(p01p.get("prime_native_integration_qualified") is False, "Prime-native qualification claimed prematurely")

    adr33 = index.get("adr_0033")
    require(isinstance(adr33, dict) and adr33.get("status") == "accepted_as_amended", "machine ADR-0033 acceptance missing")
    require(adr33.get("historical_exact_ubuntu_proof_passed") is False, "historical Ubuntu proof falsely marked passed")

    boundaries = index.get("claim_boundaries")
    require(isinstance(boundaries, dict), "machine claim boundaries missing")
    for key in ["prime_deployment_qualified", "production_authorized", "release_accepted", "historical_ubuntu_proof_passed", "prime_host_id_equals_ptah_node_id"]:
        require(boundaries.get(key) is False, f"forbidden claim became true: {key}")

    require("Runtime implementation: **AUTHORIZED**" in start, "AI recovery entry does not authorize runtime")
    require("A01 status: **READY**" in start, "AI recovery entry does not mark A01 ready")
    require(PROOF_COMMIT in start and REPORT_SHA256 in start, "AI recovery entry evidence binding missing")
    require("P01P Prime-native integration proof: **OPEN / DEFERRED**" in start, "AI recovery entry P01P boundary missing")

    return {
        "record_type": "ptah.p01.closure_current_authority_validation",
        "status": "current_authority_valid_p01d_accepted_a01_authorized",
        "master_plan_version": "1.1.0",
        "implementation_roadmap_version": "1.1.0",
        "phase0c19_complete": True,
        "adr_0037_accepted": True,
        "p01_active": False,
        "p01d_accepted": True,
        "confirmed_proof_commit": PROOF_COMMIT,
        "public_report_sha256": REPORT_SHA256,
        "negative_report_sha256": NEGATIVE_REPORT_SHA256,
        "oracle_receipt_id": ORACLE_RECEIPT_ID,
        "oracle_receipt_blob_sha": ORACLE_RECEIPT_BLOB,
        "physical_host_collection_started": True,
        "physical_development_host_accepted": True,
        "adr_0033_accepted": True,
        "adr_0039_accepted": True,
        "runtime_implementation_authorized": True,
        "a01_ready": True,
        "p01p_open": True,
        "prime_native_integration_qualified": False,
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
