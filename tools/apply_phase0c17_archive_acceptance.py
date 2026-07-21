#!/usr/bin/env python3
"""Promote the exact reviewed Phase 0C-17 archive formation candidate."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_HEAD = "58b577b6793ec28de084e6d712c3c1e88bfe2d3a"
CANDIDATE_RUN = "29853954659"
CANDIDATE_ARTIFACT = "8504497355"
CANDIDATE_ARTIFACT_DIGEST = "sha256:936740e8087e6f7f0a58b3d731117fcb9a4861edfd20c396fb1bb20a7d4f18f4"
VALIDATION_REPORT_DIGEST = "de38af1e63a76e02552e4f93ad2bac2d86d05239a77dc92cc27d794a8b9b010f"
CANDIDATE_MERGE = "c4973cbf4d02a34f14a7aefa85b8e2ea7b392752"


class AcceptanceError(RuntimeError):
    pass


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise AcceptanceError(f"{label}: expected one source fragment, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def accept_protocol() -> None:
    path = ROOT / "planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md"
    replace_once(
        path,
        "Status: candidate operating protocol — no runtime implementation authorization\n\nVersion: 1.0-candidate",
        "Status: accepted operating protocol — no runtime implementation authorization\n\nVersion: 1.0.0",
        "protocol status",
    )


def accept_manifest() -> None:
    path = ROOT / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md"
    replace_once(
        path,
        "Status: candidate backlog — no Phase 0A reopening and no runtime authorization",
        "Status: accepted campaign backlog — no source record pre-accepted, no Phase 0A reopening and no runtime authorization",
        "manifest status",
    )


def accept_adr() -> None:
    path = ROOT / "decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md"
    replace_once(
        path,
        "Status: proposed — review with Phase 0C-17 archive-formation closure",
        "Status: accepted — tenfold archive formation is the operative large-recovery protocol",
        "ADR-0035 status",
    )
    replace_once(
        path,
        "Accept `archive/CAMPAIGN-001-FORMATION-MANIFEST.md` as the candidate queue for archival-completeness auditing:",
        "Accept `archive/CAMPAIGN-001-FORMATION-MANIFEST.md` as the operative queue for archival-completeness auditing:",
        "ADR campaign queue",
    )
    marker = "## Consequences\n"
    evidence = f"""## Acceptance evidence

- candidate exact head: `{CANDIDATE_HEAD}`;
- exact-head workflow run: `{CANDIDATE_RUN}`;
- retained artifact: `{CANDIDATE_ARTIFACT}`;
- artifact digest: `{CANDIDATE_ARTIFACT_DIGEST}`;
- validation report SHA-256: `{VALIDATION_REPORT_DIGEST}`;
- candidate merge: `{CANDIDATE_MERGE}`;
- 21 regression cases passed: one valid state and twenty adversarial mutations;
- exact fifteen-file boundary reviewed with no unresolved threads;
- Phase 0A remained frozen, P01 remained active, ADR-0033 remained proposed and runtime authorization remained false.

"""
    replace_once(path, marker, evidence + marker, "ADR acceptance evidence")


def accept_work_package() -> None:
    path = ROOT / "work-packages/PHASE-0C-17-TENFOLD-ARCHIVE-FORMATION.md"
    replace_once(
        path,
        "Status: candidate under review — runtime implementation remains unauthorized",
        "Status: accepted and complete — protocol/backlog authority only; runtime implementation remains unauthorized",
        "work package status",
    )
    replace_once(path, "- proposed ADR-0035;", "- accepted ADR-0035;", "work package ADR state")
    marker = "## Completion effect\n"
    evidence = f"""## Accepted evidence

- exact candidate head `{CANDIDATE_HEAD}`;
- workflow run `{CANDIDATE_RUN}`;
- retained artifact `{CANDIDATE_ARTIFACT}`;
- artifact digest `{CANDIDATE_ARTIFACT_DIGEST}`;
- validation report SHA-256 `{VALIDATION_REPORT_DIGEST}`;
- candidate merge `{CANDIDATE_MERGE}`;
- 21 regression cases and standalone validation passed;
- exact changed-file boundary and non-authorization directly reviewed.

"""
    replace_once(path, marker, evidence + marker, "work package evidence")
    replace_once(
        path,
        "When accepted, this package adds a reusable operating protocol and the first archive campaign backlog. It does not mark any of the 98 source records archived. Formation progress must be earned through retained per-record evidence.",
        "This accepted package adds a reusable operating protocol and the first archive campaign backlog. It does not mark any of the 98 source records archived. AF01 is the first ready formation, and progress must be earned through retained per-record evidence.",
        "work package completion effect",
    )


def accept_decision_index() -> None:
    path = ROOT / "DECISIONS.md"
    accepted_insert = f"""Full decision: `decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md`.

### D-051 — Tenfold archive formation separates parallel evidence from promotion authority

**ACCEPTED.** Large Ptah archive/recovery campaigns use `max(20, human-equivalent workers × 10)`. A normal twenty-private formation pairs ten Primary Archivists with ten Independent Verifiers for at most ten ordinary records; harder sources consume 40/60/80–100/up to 120 privates. Privates cannot issue verdicts, adopt donors, reopen Phase 0A or authorize implementation. Campaign 001 queues 98 obligations across ten formations and 200 private slots without pre-accepting any record. Candidate `{CANDIDATE_HEAD}` passed run `{CANDIDATE_RUN}` and merged as `{CANDIDATE_MERGE}`.

Full decision: `decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md`.

---

## Current proposed decisions"""
    replace_once(
        path,
        "Full decision: `decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md`.\n\n---\n\n## Current proposed decisions",
        accepted_insert,
        "decision accepted insertion",
    )
    remove = """

### ADR-0035 — Tenfold archive formation and evidence promotion

**PROPOSED.** Borrows Sergeant's pinned tenfold private-force rule for Ptah recovery campaigns: minimum twenty privates, one primary/verifier pair per ordinary archive record, complexity escalation, bounded evidence packets and officer-only promotion. Phase 0A remains frozen, P01 remains active and runtime implementation remains unauthorized.

Full decision: `decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md`.
"""
    replace_once(path, remove, "\n", "remove proposed ADR-0035 index block")


def accept_progress() -> None:
    path = ROOT / "PROGRESS.md"
    old = """## Tenfold archive formation candidate

- [x] Sergeant tenfold private-force source pinned at `44c8f47f4bb50a73ef3b4d81d7b849a5aab37dfd`;
- [x] Ptah archive authority, pairing, promotion, privacy and save-point protocol written;
- [x] 69 external and 29 internal obligations mapped into ten standard formations;
- [x] 200 private slots allocated with one primary and one independent verifier per obligation;
- [x] bounded archive-record template written;
- [x] proposed ADR-0035 and Phase 0C-17 work package written;
- [x] read-only validator and fifteen adversarial regressions added;
- [-] exact-head workflow and direct review pending final synchronized head;
- [ ] accept ADR-0035 and Phase 0C-17;
- [ ] begin AF01 only through retained per-record evidence; no source record is pre-ticked as archived.
"""
    new = f"""## Tenfold archive formation — accepted

- [x] Sergeant tenfold private-force source pinned at `44c8f47f4bb50a73ef3b4d81d7b849a5aab37dfd`;
- [x] Ptah archive authority, pairing, promotion, privacy and save-point protocol accepted as version `1.0.0`;
- [x] 69 external and 29 internal obligations mapped into ten standard formations;
- [x] 200 private slots allocated with one primary and one independent verifier per obligation;
- [x] bounded archive-record template accepted;
- [x] candidate exact head `{CANDIDATE_HEAD}` passed 21 regression cases and exact-head validation in run `{CANDIDATE_RUN}`;
- [x] retained artifact `{CANDIDATE_ARTIFACT}` with digest `{CANDIDATE_ARTIFACT_DIGEST}`;
- [x] exact fifteen-file boundary directly reviewed and candidate merged as `{CANDIDATE_MERGE}`;
- [x] ADR-0035 and Phase 0C-17 accepted;
- [ ] AF01 is READY but not started; no source record is pre-ticked as archived.
"""
    replace_once(path, old, new, "progress archive acceptance")


def accept_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    old = """## Active Phase 0C-17 tenfold archive formation candidate

Branch and PR:

```text
phase0c-tenfold-archive-formation
PR #26
```

The candidate borrows Sergeant's exact tenfold private-force rule from `jaydumisuni/Sergeant@44c8f47f4bb50a73ef3b4d81d7b849a5aab37dfd` and defines:

- minimum twenty privates for two human-equivalent workers;
- ten primary/verifier record pairs per standard formation;
- adaptive escalation to 40/60/80–100/up to 120 privates for harder sources;
- ten formations and 200 allocated privates for 98 initial archive obligations;
- bounded evidence packets and Archive Officer promotion;
- checkpoints after five and ten records;
- public/private retention boundaries;
- read-only exact-head validation and adversarial regressions.

This candidate is cross-cutting recovery governance. It does not replace P01 as the active authorization work, reopen Phase 0A, mark the 98 records archived, accept ADR-0033 or authorize runtime implementation.
"""
    new = f"""## Accepted Phase 0C-17 tenfold archive formation

Operative authority:

```text
ADR-0035: ACCEPTED
protocol: planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md version 1.0.0
campaign: archive/CAMPAIGN-001-FORMATION-MANIFEST.md
candidate merge: {CANDIDATE_MERGE}
```

Accepted evidence:

- candidate exact head `{CANDIDATE_HEAD}`;
- exact-head run `{CANDIDATE_RUN}`;
- retained artifact `{CANDIDATE_ARTIFACT}`;
- artifact digest `{CANDIDATE_ARTIFACT_DIGEST}`;
- validation report SHA-256 `{VALIDATION_REPORT_DIGEST}`;
- 21 regression cases and exact-head validation passed;
- exact fifteen-file boundary directly reviewed.

The operative rule uses minimum twenty privates for two human-equivalent workers, ten primary/verifier record pairs per ordinary formation, and adaptive escalation to 40/60/80–100/up to 120 privates for harder sources. Campaign 001 queues 98 obligations across ten formations and 200 slots.

AF01 is READY but not started. This cross-cutting recovery protocol does not replace P01 as the active authorization work, reopen Phase 0A, mark records archived, accept ADR-0033 or authorize runtime implementation.
"""
    replace_once(path, old, new, "current state archive acceptance")


def accept_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    old = """## Cross-cutting archive formation candidate

```text
branch: phase0c-tenfold-archive-formation
pull request: #26
status: candidate under review
```

Read when doing archive/recovery work:

- `planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md`;
- `archive/CAMPAIGN-001-FORMATION-MANIFEST.md`;
- `archive/ARCHIVE-RECORD-TEMPLATE.md`;
- proposed ADR-0035;
- Phase 0C-17 work package.

Campaign 001 covers 98 source obligations with ten twenty-private formations and one primary/verifier pair per obligation. It is a queue and operating protocol, not proof that records are archived or that a 200-agent runtime exists.

P01 physical-host closure remains the exact next authorization action.
"""
    new = f"""## Accepted cross-cutting archive formation

```text
ADR-0035: ACCEPTED
Phase 0C-17: COMPLETE
protocol version: 1.0.0
candidate merge: {CANDIDATE_MERGE}
AF01: READY / NOT STARTED
```

Read when doing archive/recovery work:

- `planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md`;
- `archive/CAMPAIGN-001-FORMATION-MANIFEST.md`;
- `archive/ARCHIVE-RECORD-TEMPLATE.md`;
- accepted ADR-0035;
- accepted Phase 0C-17 work package.

Evidence: exact head `{CANDIDATE_HEAD}`, run `{CANDIDATE_RUN}`, artifact `{CANDIDATE_ARTIFACT}`, digest `{CANDIDATE_ARTIFACT_DIGEST}`.

Campaign 001 covers 98 source obligations with ten twenty-private formations and one primary/verifier pair per obligation. It is an accepted queue and operating protocol, not proof that records are archived or that a 200-agent runtime exists.

P01 physical-host closure remains the exact next authorization action.
"""
    replace_once(path, old, new, "handoff archive acceptance")


def accept_machine_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("active_work_unit") != "P01-physical-host-and-ADR-0033-closure":
        raise AcceptanceError("active P01 work drifted")
    if data.get("runtime_implementation_authorized") is not False:
        raise AcceptanceError("runtime unexpectedly authorized")
    record = data["operational_protocols"]["tenfold_archive_formation"]
    if record.get("status") != "candidate_under_review":
        raise AcceptanceError("archive protocol is not in candidate state")
    record.update(
        {
            "status": "accepted_operational_protocol_af01_ready",
            "source_branch": "main",
            "protocol_version": "1.0.0",
            "candidate_exact_head": CANDIDATE_HEAD,
            "candidate_workflow_run": CANDIDATE_RUN,
            "candidate_artifact_id": CANDIDATE_ARTIFACT,
            "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,
            "validation_report_sha256": VALIDATION_REPORT_DIGEST,
            "candidate_merge": CANDIDATE_MERGE,
            "adr_0035_accepted": True,
            "phase0c_17_complete": True,
            "af01_status": "ready_not_started",
            "accepted_archive_record_count": 0,
        }
    )
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def accept_validator_and_tests() -> None:
    validator = ROOT / "tools/check_archive_formation.py"
    replacements = (
        ("require(adr, \"Status: proposed\", \"ADR-0035 proposed state\")", "require(adr, \"Status: accepted\", \"ADR-0035 accepted state\")"),
        ("require(work_package, \"Status: candidate under review\", \"Phase 0C-17 candidate state\")", "require(work_package, \"Status: accepted and complete\", \"Phase 0C-17 accepted state\")"),
        ("require(decisions, \"### ADR-0035 — Tenfold archive formation and evidence promotion\", \"decision index entry\")\n    require(decisions, \"**PROPOSED.**\", \"ADR-0035 proposed index state\")", "require(decisions, \"### D-051 — Tenfold archive formation separates parallel evidence from promotion authority\", \"accepted decision index entry\")\n    require(decisions, \"**ACCEPTED.**\", \"ADR-0035 accepted index state\")"),
        ("require(progress, \"## Tenfold archive formation candidate\", \"progress archive section\")", "require(progress, \"## Tenfold archive formation — accepted\", \"progress archive section\")"),
        ("require(progress, \"200 private slots allocated\", \"progress force count\")", "require(progress, \"200 private slots allocated\", \"progress force count\")\n    require(progress, \"AF01 is READY but not started\", \"progress AF01 state\")"),
        ("require(current_state, \"## Active Phase 0C-17 tenfold archive formation candidate\", \"current archive candidate\")\n    require(current_state, \"PR #26\", \"current archive PR\")\n    require(current_state, \"does not replace P01\", \"current P01 boundary\")", "require(current_state, \"## Accepted Phase 0C-17 tenfold archive formation\", \"current archive acceptance\")\n    require(current_state, \"ADR-0035: ACCEPTED\", \"current accepted ADR\")\n    require(current_state, \"AF01 is READY but not started\", \"current AF01 state\")\n    require(current_state, \"does not replace P01\", \"current P01 boundary\")"),
        ("require(handoff, \"## Cross-cutting archive formation candidate\", \"handoff archive candidate\")\n    require(handoff, \"pull request: #26\", \"handoff archive PR\")", "require(handoff, \"## Accepted cross-cutting archive formation\", \"handoff archive acceptance\")\n    require(handoff, \"ADR-0035: ACCEPTED\", \"handoff accepted ADR\")\n    require(handoff, \"AF01: READY / NOT STARTED\", \"handoff AF01 state\")"),
        ("\"status\": \"candidate_under_review\",\n        \"source_branch\": \"phase0c-tenfold-archive-formation\",", "\"status\": \"accepted_operational_protocol_af01_ready\",\n        \"source_branch\": \"main\","),
        ("\"runtime_implementation_authorized\": False,\n    }", f"\"runtime_implementation_authorized\": False,\n        \"protocol_version\": \"1.0.0\",\n        \"candidate_exact_head\": \"{CANDIDATE_HEAD}\",\n        \"candidate_workflow_run\": \"{CANDIDATE_RUN}\",\n        \"candidate_artifact_id\": \"{CANDIDATE_ARTIFACT}\",\n        \"candidate_artifact_digest\": \"{CANDIDATE_ARTIFACT_DIGEST}\",\n        \"validation_report_sha256\": \"{VALIDATION_REPORT_DIGEST}\",\n        \"candidate_merge\": \"{CANDIDATE_MERGE}\",\n        \"adr_0035_accepted\": True,\n        \"phase0c_17_complete\": True,\n        \"af01_status\": \"ready_not_started\",\n        \"accepted_archive_record_count\": 0,\n    }}"),
        ("\"status\": \"candidate_valid_non_authorizing\",", "\"status\": \"accepted_valid_non_authorizing\","),
    )
    for old, new in replacements:
        replace_once(validator, old, new, f"validator replacement {old[:32]}")

    tests = ROOT / "tools/test_check_archive_formation.py"
    replace_once(tests, 'self.assertEqual(result["status"], "candidate_valid_non_authorizing")', 'self.assertEqual(result["status"], "accepted_valid_non_authorizing")', "test accepted status")
    insertion = """    def test_accepted_adr0035_cannot_revert(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md"),
            "Status: accepted",
            "Status: proposed",
        )
        self.assert_invalid(root)

    def test_af01_cannot_be_precompleted(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("master-plan-index.json"),
            '"accepted_archive_record_count": 0',
            '"accepted_archive_record_count": 10',
        )
        self.assert_invalid(root)

"""
    replace_once(tests, "\n\nif __name__ == \"__main__\":", "\n\n" + insertion + 'if __name__ == "__main__":', "accepted-state tests")


def main() -> int:
    accept_protocol()
    accept_manifest()
    accept_adr()
    accept_work_package()
    accept_decision_index()
    accept_progress()
    accept_current_state()
    accept_handoff()
    accept_machine_index()
    accept_validator_and_tests()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    adr0033 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    donor = (ROOT / "DONOR_RECOVERY.md").read_text(encoding="utf-8")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current or "**Runtime implementation:** AUTHORIZED" in current:
        raise AcceptanceError("runtime non-authorization boundary failed")
    if "Status: proposed" not in adr0033:
        raise AcceptanceError("ADR-0033 is no longer proposed")
    if "**Status:** COMPLETE AND FROZEN" not in donor:
        raise AcceptanceError("Phase 0A donor register is no longer frozen")

    print("Phase 0C-17 / ADR-0035 accepted-state transform complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
