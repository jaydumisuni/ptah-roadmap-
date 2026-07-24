#!/usr/bin/env python3
"""Validate Campaign 001 AF04-AF10 candidate evidence without promoting authority."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

EXPECTED = {
    "AF04": {"assigned": 10, "accepted": 10, "blocked": 0, "head": "ee0b78a41241a1b61a7085d6eeabf202882d2dc2"},
    "AF05": {"assigned": 10, "accepted": 9, "blocked": 1, "head": "05975c5fbf34bd52a51ccd6ec54fd13a24dac849"},
    "AF06": {"assigned": 10, "accepted": 10, "blocked": 0, "head": "388e3110435fe4664531756e6d9fc2d4e8910e2e"},
    "AF07": {"assigned": 10, "accepted": 10, "blocked": 0, "head": "50b62cd8d4870eaf1a709d719a0939651fe54d80"},
    "AF08": {"assigned": 10, "accepted": 10, "blocked": 0, "head": "e6d708798d3114b4de3230d28efb5f9a3a5733ca"},
    "AF09": {"assigned": 10, "accepted": 10, "blocked": 0, "head": "64febc773dc62ba554a7c8a64493e84ae4d8f4b0"},
    "AF10": {"assigned": 8, "accepted": 3, "blocked": 5, "head": "a2a58ae78b19cadf18b52e775301ed03a9d7ad67"},
}
EXPECTED_IDS = {
    "AF04": ["D044","D049","D053","D060","D064","D068","D004","D015","D019","D023"],
    "AF05": ["D033","D038","D045","D050","D054","D061","D065","D069","D005","D024"],
    "AF06": ["D034","D039","D046","D055","D006","D025","D040","D056","D007","D026"],
    "AF07": ["D041","D057","D008","D027","D009","D028","D010","D029","D011","I001"],
    "AF08": ["I002","I009","I013","I020","I026","I003","I010","I014","I029","I027"],
    "AF09": ["I004","I011","I015","I028","I005","I012","I016","I006","I017","I007"],
    "AF10": ["I018","I008","I019","I021","I022","I023","I024","I025"],
}

class ValidationError(RuntimeError):
    pass

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)

def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValidationError(f"cannot load {path}: {exc}") from exc

def validate(repo_root: Path) -> dict[str, Any]:
    all_ids: list[str] = []
    primaries: list[str] = []
    verifiers: list[str] = []
    accepted = blocked = assigned = 0
    formation_reports: dict[str, Any] = {}

    for formation, expected in EXPECTED.items():
        base = repo_root / "archive" / "campaign-001" / formation.lower()
        result_path = base / "RESULT.json"
        result = load_json(result_path)
        require(result.get("formation_id") == formation, f"{formation}: wrong formation_id")
        require(result.get("status") == "candidate_evidence_complete_non_authorizing", f"{formation}: wrong candidate status")
        require(result.get("assigned_record_count") == expected["assigned"], f"{formation}: assigned count mismatch")
        require(result.get("reconciled_record_count") == expected["assigned"], f"{formation}: reconciled count mismatch")
        require(result.get("accepted_archive_record_count") == expected["accepted"], f"{formation}: accepted count mismatch")
        require(result.get("blocked_record_count") == expected["blocked"], f"{formation}: blocked count mismatch")
        require(result.get("remaining_evidence_count") == 0, f"{formation}: evidence remains")
        require(result.get("sergeant_review_result") == "pass_with_mandatory_retained_restrictions", f"{formation}: independent review result mismatch")
        require(result.get("sergeant_blocking_finding_count") == 0, f"{formation}: blocking review finding")
        require(result.get("sergeant_review_target_head") == expected["head"], f"{formation}: frozen review head mismatch")
        require(result.get("phase_0a_reopened") is False, f"{formation}: Phase 0A reopened")
        require(result.get("adr_0033_accepted") is False, f"{formation}: ADR-0033 accepted prematurely")
        require(result.get("runtime_implementation_authorized") is False, f"{formation}: runtime authorized prematurely")

        records = result.get("records")
        require(isinstance(records, list) and len(records) == expected["assigned"], f"{formation}: record list mismatch")
        ids = [record.get("id") for record in records]
        require(ids == EXPECTED_IDS[formation], f"{formation}: record order or identity mismatch")
        pset = [record.get("primary") for record in records]
        vset = [record.get("verifier") for record in records]
        require(len(set(pset)) == len(pset), f"{formation}: primary worker reused")
        require(len(set(vset)) == len(vset), f"{formation}: verifier worker reused")
        require(set(pset).isdisjoint(vset), f"{formation}: primary/verifier independence collapsed")

        observed_blocked = 0
        for record in records:
            path = repo_root / str(record.get("path", ""))
            require(path.is_file(), f"{formation}/{record.get('id')}: record file missing")
            text = path.read_text(encoding="utf-8")
            require(f"Primary Archivist: `{record['primary']}`" in text, f"{record['id']}: primary packet binding missing")
            require(f"Independent Verifier: `{record['verifier']}`" in text, f"{record['id']}: verifier packet binding missing")
            require("## Bounded outcome" in text, f"{record['id']}: bounded outcome heading missing")
            require(str(record.get("outcome")) in text, f"{record['id']}: result/file outcome mismatch")
            require("does not authorize implementation" in text, f"{record['id']}: non-authorizing statement missing")
            if str(record.get("outcome", "")).startswith("blocked_"):
                observed_blocked += 1
                require("Safe next action" in text, f"{record['id']}: blocked outcome has no safe next action")
                require("prohibited" in text, f"{record['id']}: blocked source-reuse prohibition missing")
            all_ids.append(record["id"])
            primaries.append(record["primary"])
            verifiers.append(record["verifier"])
        require(observed_blocked == expected["blocked"], f"{formation}: observed blocked count mismatch")

        for required in ("MISSION.md", "CHECKPOINT-05.md", "SERGEANT-REVIEW.md", "RESULT.md"):
            require((base / required).is_file(), f"{formation}: missing {required}")
        if formation == "AF10":
            require((base / "CHECKPOINT-08.md").is_file(), "AF10: missing final checkpoint")
            require(result.get("reserve_pair_count") == 2 and result.get("reserve_pairs_used") == 0, "AF10: reserve pair state mismatch")
        else:
            require((base / "CHECKPOINT-10.md").is_file(), f"{formation}: missing checkpoint 10")

        assigned += expected["assigned"]
        accepted += expected["accepted"]
        blocked += expected["blocked"]
        formation_reports[formation] = {"records": len(records), "accepted": expected["accepted"], "blocked": expected["blocked"]}

    require(assigned == 68, "new campaign assigned total mismatch")
    require(accepted == 62, "new campaign accepted total mismatch")
    require(blocked == 6, "new campaign blocked total mismatch")
    require(len(all_ids) == 68 and len(set(all_ids)) == 68, "campaign record identities are not unique")
    require(len(primaries) == 68 and len(set(primaries)) == 68, "campaign primary worker identities are not unique")
    require(len(verifiers) == 68 and len(set(verifiers)) == 68, "campaign verifier worker identities are not unique")
    require(set(primaries).isdisjoint(verifiers), "campaign primary/verifier worker independence collapsed")

    # AF01-AF03 accepted baseline plus AF04-AF10 candidate package.
    baseline = {"AF01": (9,1), "AF02": (10,0), "AF03": (10,0)}
    for formation, counts in baseline.items():
        result = load_json(repo_root / "archive" / "campaign-001" / formation.lower() / "RESULT.json")
        require(result.get("accepted_archive_record_count") == counts[0], f"{formation}: accepted baseline drift")
        require(result.get("blocked_record_count") == counts[1], f"{formation}: blocked baseline drift")
    require(29 + accepted == 91, "full campaign accepted total mismatch")
    require(1 + blocked == 7, "full campaign blocked total mismatch")
    require(91 + 7 == 98, "full campaign obligation closure mismatch")

    current = (repo_root / "CURRENT_STATE.md").read_text(encoding="utf-8")
    proposed_adr_line = "- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`."
    require("P01" in current and "physical" in current.lower(), "P01 physical-host blocker missing")
    require(proposed_adr_line in current, "ADR-0033 proposed state missing")
    require("ADR-0033: ACCEPTED" not in current, "ADR-0033 accepted prematurely")
    require("**Runtime implementation:** NOT AUTHORIZED" in current, "runtime non-authorization field missing")
    require("**Runtime implementation:** AUTHORIZED" not in current, "runtime authorized prematurely")
    manifest = (repo_root / "archive" / "CAMPAIGN-001-FORMATION-MANIFEST.md").read_text(encoding="utf-8")
    require("AF04" in manifest and "READY / NOT STARTED" in manifest, "candidate branch promoted campaign authority prematurely")
    require(not (repo_root / "archive" / "campaign-001" / "af11").exists(), "unexpected AF11 formation exists")

    return {
        "schema_version": "1.0.0",
        "status": "af04_af10_candidate_complete_valid_non_authorizing",
        "formation_count": 7,
        "new_record_count": assigned,
        "new_accepted_archive_record_count": accepted,
        "new_blocked_record_count": blocked,
        "new_remaining_evidence_count": 0,
        "campaign_obligation_count": 98,
        "campaign_accepted_archive_record_count_if_promoted": 91,
        "campaign_blocked_record_count_if_promoted": 7,
        "campaign_completed_formation_count_if_promoted": 10,
        "sergeant_reviews_complete": True,
        "phase_0a_reopened": False,
        "p01_closed": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
        "formations": formation_reports,
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        report = validate(Path(args.repo_root).resolve())
    except ValidationError as exc:
        print(f"AF04-AF10 validation failed: {exc}")
        return 1
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
