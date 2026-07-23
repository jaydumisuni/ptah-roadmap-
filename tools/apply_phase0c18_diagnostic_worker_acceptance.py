#!/usr/bin/env python3
"""Promote the exact reviewed Phase 0C-18 candidate into accepted authority."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_HEAD = "d2608ba7c619c1c402091edd619a4b29813ee9a7"
CANDIDATE_RUN = "29986975197"
CANDIDATE_ARTIFACT = "8555395796"
CANDIDATE_ARTIFACT_DIGEST = "sha256:72025fb0aa5a969ea73abe95d7352f7cf14f1c847943955bd768a46d964a4c61"
CANDIDATE_REPORT_SHA256 = "aff3a635d37b82c15eeb36f2f6cec780f76e2c3ce320727a18053b913b8d9171"
CANDIDATE_MERGE = "fbc4ee80284a2d7ea38a44fdbfa90f0348b875ae"
ACCEPTANCE_RECORD = "planning/PTAH-DIAGNOSTIC-WORKER-AUTHORITY-ACCEPTANCE.md"


class AcceptanceError(RuntimeError):
    pass


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise AcceptanceError(f"{label}: expected one source fragment, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def accept_protocol() -> None:
    path = ROOT / "planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"
    replace_once(
        path,
        "Status: candidate product clarification — runtime implementation remains unauthorized\n\nVersion: 1.0-candidate",
        "Status: accepted product clarification — runtime implementation remains unauthorized\n\nVersion: 1.0.0",
        "protocol status",
    )


def accept_adr() -> None:
    path = ROOT / "decisions/ADR-0036-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md"
    replace_once(
        path,
        "Status: proposed — review with Phase 0C-18",
        "Status: accepted — operative diagnostic and efficient worker execution boundary",
        "ADR status",
    )
    replace_once(
        path,
        "Adopt `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md` as the candidate boundary",
        "Adopt `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md` as the operative boundary",
        "ADR operative boundary",
    )
    evidence = f"""## Acceptance evidence

- candidate exact head: `{CANDIDATE_HEAD}`;
- exact-head workflow run: `{CANDIDATE_RUN}`;
- retained artifact: `{CANDIDATE_ARTIFACT}`;
- artifact digest: `{CANDIDATE_ARTIFACT_DIGEST}`;
- validation report SHA-256: `{CANDIDATE_REPORT_SHA256}`;
- candidate merge: `{CANDIDATE_MERGE}`;
- regression cases passed: `41`;
- exact durable candidate boundary: `13` files;
- frozen primitives only, no new Core entity;
- AF03, Phase 0A, P01, ADR-0033 and runtime boundaries preserved.

"""
    replace_once(path, "## Consequences\n", evidence + "## Consequences\n", "ADR evidence")


def accept_work_package() -> None:
    path = ROOT / "work-packages/PHASE-0C-18-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md"
    replace_once(
        path,
        "Status: candidate under review — runtime implementation remains unauthorized",
        "Status: accepted and complete — product boundary only; runtime implementation remains unauthorized",
        "work package status",
    )
    replace_once(path, "- proposed ADR-0036;", "- accepted ADR-0036;", "work package ADR")
    evidence = f"""## Accepted evidence

- exact candidate head `{CANDIDATE_HEAD}`;
- workflow run `{CANDIDATE_RUN}`;
- retained artifact `{CANDIDATE_ARTIFACT}`;
- artifact digest `{CANDIDATE_ARTIFACT_DIGEST}`;
- validation report SHA-256 `{CANDIDATE_REPORT_SHA256}`;
- candidate merge `{CANDIDATE_MERGE}`;
- 41 adversarial regressions and exact-head validation passed.

"""
    replace_once(path, "## Completion effect\n", evidence + "## Completion effect\n", "work package evidence")
    replace_once(
        path,
        "When accepted, this package clarifies planned product behavior and adds future implementation proof obligations. It does not implement either capability, start AF03 or authorize runtime work.",
        "This accepted package clarifies planned product behavior and adds future implementation proof obligations. It does not implement either capability, start AF03 or authorize runtime work.",
        "work package completion",
    )


def accept_decisions() -> None:
    path = ROOT / "DECISIONS.md"
    accepted = f"""Full decision: `decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md`.

### D-052 — Ptah may diagnose its platform and efficiently execute caller-given worker formations

**ACCEPTED.** Ptah may produce evidence-backed diagnostic advisories for missing capability, degradation, incompatibility or repeated failure and may ask an authorized caller for an upgrade. For a caller-submitted job and caller-selected Recipe/Plan, Ptah may execute `max(20, human-equivalent workers × 10)` bounded workers with independent checks, checkpoints and retained conflicts. Ptah cannot choose caller work, invent semantic scope, accept the result or approve/install its own upgrade. Candidate `{CANDIDATE_HEAD}` passed 41 regressions in run `{CANDIDATE_RUN}` and merged as `{CANDIDATE_MERGE}`.

Full decision: `decisions/ADR-0036-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md`.

---

## Current proposed decisions"""
    replace_once(
        path,
        "Full decision: `decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md`.\n\n---\n\n## Current proposed decisions",
        accepted,
        "decision accepted insertion",
    )
    proposed = """

### ADR-0036 — Platform diagnostic advisory and efficient worker execution boundary

**PROPOSED.** Ptah may compare configured platform expectations with observed health, capability and execution evidence and emit a bounded upgrade or inspection advisory. For a caller-submitted job and Recipe/Plan, Ptah may apply the Sergeant-derived ten-for-two pattern to run bounded parallel workers and independent checks. Ptah may not choose caller work, invent semantic scope, approve a result or install its own upgrade.

Full decision: `decisions/ADR-0036-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md`.
"""
    replace_once(path, proposed, "\n", "remove proposed ADR block")


def accept_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    old = """## Phase 0C-18 diagnostic and efficient-worker candidate

The owner clarified that Ptah remains neutral regarding caller intent while retaining two bounded platform capabilities.

Candidate authority:

- `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md`;
- proposed ADR-0036;
- `work-packages/PHASE-0C-18-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md`.

Allowed diagnostic behavior: detect missing capability, degradation, incompatibility, resource shortage, repeated failure or failed post-condition and emit an evidence-backed advisory asking an authorized caller for an upgrade or inspection.

Allowed execution behavior: after a caller submits a job and selects a Recipe/Plan, apply `max(20, human-equivalent workers × 10)` to run bounded worker Activities, independent checks, checkpoints and configured merge/recovery mechanics.

Forbidden: choose caller work, invent semantic subtasks, reprioritize outside submitted Policy, approve a result, approve/purchase/install an upgrade, mark acknowledgement as resolution, block unrelated capable work or become Hunter/Sergeant authority.

This candidate uses frozen primitives only, does not start AF03 and does not change P01, ADR-0033 or runtime authorization.
"""
    new = f"""## Accepted Phase 0C-18 diagnostic and efficient-worker boundary

Operative authority:

- `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md` version `1.0.0`;
- ADR-0036: ACCEPTED;
- Phase 0C-18: COMPLETE;
- candidate merge: `{CANDIDATE_MERGE}`;
- acceptance evidence: `{ACCEPTANCE_RECORD}`.

Allowed diagnostic behavior: detect missing capability, degradation, incompatibility, resource shortage, repeated failure or failed post-condition and emit an evidence-backed advisory asking an authorized caller for an upgrade or inspection.

Allowed execution behavior: after a caller submits a job and selects a Recipe/Plan, apply `max(20, human-equivalent workers × 10)` to run bounded worker Activities, independent checks, checkpoints and configured merge/recovery mechanics.

Accepted evidence: exact head `{CANDIDATE_HEAD}`, run `{CANDIDATE_RUN}`, artifact `{CANDIDATE_ARTIFACT}`, digest `{CANDIDATE_ARTIFACT_DIGEST}`, validation SHA-256 `{CANDIDATE_REPORT_SHA256}`.

Forbidden: choose caller work, invent semantic subtasks, reprioritize outside submitted Policy, approve a result, approve/purchase/install an upgrade, mark acknowledgement as resolution, block unrelated capable work or become Hunter/Sergeant authority.

This accepted clarification uses frozen primitives only, does not start AF03 and does not change P01, ADR-0033 or runtime authorization.
"""
    replace_once(path, old, new, "current-state acceptance")


def accept_progress() -> None:
    path = ROOT / "PROGRESS.md"
    old = """## Diagnostic advisory and efficient worker candidate

- [x] owner boundary recovered: diagnose platform condition without deciding caller work;
- [x] owner ten-for-two boundary recovered: spread a caller-given job across bounded workers for speed and efficiency;
- [x] frozen Node/Provider health, Recipe/Plan/Run/Step, Workspace/Activity/Attempt, Reservation/Grant/Lease/Fence, Event/Receipt, Claim/Evidence and View/Artifact primitives mapped;
- [x] diagnostic advisory, upgrade-request and worker-execution boundaries written;
- [x] proposed ADR-0036 and Phase 0C-18 work package written;
- [x] Programme A02/A04/A06/A14/A15 proof placement added;
- [-] exact-head validator, adversarial tests and review pending;
- [ ] accept ADR-0036 and Phase 0C-18;
- [ ] implementation remains unauthorized.
"""
    new = f"""## Diagnostic advisory and efficient worker boundary — accepted

- [x] owner boundary recovered: diagnose platform condition without deciding caller work;
- [x] owner ten-for-two boundary recovered: spread a caller-given job across bounded workers for speed and efficiency;
- [x] frozen Node/Provider health, Recipe/Plan/Run/Step, Workspace/Activity/Attempt, Reservation/Grant/Lease/Fence, Event/Receipt, Claim/Evidence and View/Artifact primitives mapped;
- [x] diagnostic advisory, upgrade-request and worker-execution boundaries accepted as version `1.0.0`;
- [x] Programme A02/A04/A06/A14/A15 proof placement accepted;
- [x] exact head `{CANDIDATE_HEAD}` passed 41 regressions in run `{CANDIDATE_RUN}`;
- [x] retained artifact `{CANDIDATE_ARTIFACT}` with digest `{CANDIDATE_ARTIFACT_DIGEST}`;
- [x] candidate merged as `{CANDIDATE_MERGE}`;
- [x] ADR-0036 and Phase 0C-18 accepted;
- [x] implementation remains unauthorized;
- [ ] AF03 remains READY / NOT STARTED.
"""
    replace_once(path, old, new, "progress acceptance")


def accept_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    old = """## Diagnostic advisory and efficient worker candidate

Ptah remains neutral regarding caller intent. The Phase 0C-18 candidate permits two bounded platform behaviors:

```text
configured expected platform condition
→ observed health/capability/execution evidence
→ missing capability or degradation advisory
→ human/calling application chooses whether to upgrade, replace, defer or continue
```

```text
caller-submitted job and Recipe/Plan
→ max(20, human-equivalent workers × 10)
→ bounded parallel Activities, independent checks and checkpoints
→ configured merge or partial/conflicting result
→ caller or external reviewer decides acceptance
```

Read:

- `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md`;
- proposed ADR-0036;
- Phase 0C-18 work package.

Ptah may manage declared workers and ask for an upgrade, but may not choose caller work, invent semantic scope, approve a result, approve/install the upgrade or treat acknowledgement as resolution. AF03 remains READY / NOT STARTED.
"""
    new = f"""## Accepted diagnostic advisory and efficient worker boundary

```text
ADR-0036: ACCEPTED
Phase 0C-18: COMPLETE
protocol version: 1.0.0
candidate merge: {CANDIDATE_MERGE}
```

Ptah may diagnose its own platform condition and ask a caller for an upgrade. For a caller-submitted job and Recipe/Plan, Ptah may execute `max(20, human-equivalent workers × 10)` bounded workers with independent checks and checkpoints.

Ptah may not choose caller work, invent semantic scope, approve a result, approve/install its own upgrade or treat acknowledgement as resolution.

Evidence: exact head `{CANDIDATE_HEAD}`, run `{CANDIDATE_RUN}`, artifact `{CANDIDATE_ARTIFACT}`, digest `{CANDIDATE_ARTIFACT_DIGEST}`. Full record: `{ACCEPTANCE_RECORD}`.

AF03 remains READY / NOT STARTED.
"""
    replace_once(path, old, new, "handoff acceptance")


def accept_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("active_work_unit") != "P01-physical-host-and-ADR-0033-closure":
        raise AcceptanceError("P01 active work drifted")
    if data.get("runtime_implementation_authorized") is not False:
        raise AcceptanceError("runtime unexpectedly authorized")
    record = data["product_clarifications"]["platform_diagnostic_and_worker_execution"]
    if record.get("status") != "candidate_under_review":
        raise AcceptanceError("Phase 0C-18 machine state is not candidate")
    record.update({
        "status": "accepted_operational_clarification",
        "protocol_version": "1.0.0",
        "adr_0036_accepted": True,
        "phase0c_18_complete": True,
        "candidate_exact_head": CANDIDATE_HEAD,
        "candidate_workflow_run": CANDIDATE_RUN,
        "candidate_artifact_id": CANDIDATE_ARTIFACT,
        "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,
        "candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,
        "candidate_merge": CANDIDATE_MERGE,
        "acceptance_record": ACCEPTANCE_RECORD,
    })
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def accept_validator_and_tests() -> None:
    validator = ROOT / "tools/check_platform_diagnostic_advisory.py"
    replacements = (
        ('require(protocol, "Status: candidate product clarification", "protocol candidate state")',
         'require(protocol, "Status: accepted product clarification", "protocol accepted state")'),
        ('require(adr, "Status: proposed", "ADR-0036 proposed state")',
         'require(adr, "Status: accepted", "ADR-0036 accepted state")'),
        ('require(work_package, "Status: candidate under review", "Phase 0C-18 candidate state")',
         'require(work_package, "Status: accepted and complete", "Phase 0C-18 accepted state")'),
        ('require(decisions, "### ADR-0036 — Platform diagnostic advisory and efficient worker execution boundary", "decision index")\n    require(decisions, "**PROPOSED.**", "decision proposed state")',
         'require(decisions, "### D-052 — Ptah may diagnose its platform and efficiently execute caller-given worker formations", "accepted decision index")\n    require(decisions, "**ACCEPTED.**", "decision accepted state")'),
        ('require(current, "## Phase 0C-18 diagnostic and efficient-worker candidate", "current-state candidate section")',
         'require(current, "## Accepted Phase 0C-18 diagnostic and efficient-worker boundary", "current-state accepted section")'),
        ('require(progress, "## Diagnostic advisory and efficient worker candidate", "progress candidate section")',
         'require(progress, "## Diagnostic advisory and efficient worker boundary — accepted", "progress accepted section")'),
        ('require(handoff, "## Diagnostic advisory and efficient worker candidate", "handoff candidate section")',
         'require(handoff, "## Accepted diagnostic advisory and efficient worker boundary", "handoff accepted section")'),
        ('"status": "candidate_under_review",', '"status": "accepted_operational_clarification",'),
        ('"runtime_implementation_authorized": False,\n    }',
         '"runtime_implementation_authorized": False,\n        "protocol_version": "1.0.0",\n        "adr_0036_accepted": True,\n        "phase0c_18_complete": True,\n        "candidate_exact_head": CANDIDATE_HEAD,\n        "candidate_workflow_run": CANDIDATE_RUN,\n        "candidate_artifact_id": CANDIDATE_ARTIFACT,\n        "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,\n        "candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,\n        "candidate_merge": CANDIDATE_MERGE,\n        "acceptance_record": ACCEPTANCE_RECORD,\n    }'),
        ('"status": "candidate_valid_non_authorizing",', '"status": "accepted_valid_non_authorizing",'),
    )
    # Add evidence constants after imports.
    replace_once(
        validator,
        'ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")',
        'ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")\n'
        f'CANDIDATE_HEAD = "{CANDIDATE_HEAD}"\n'
        f'CANDIDATE_RUN = "{CANDIDATE_RUN}"\n'
        f'CANDIDATE_ARTIFACT = "{CANDIDATE_ARTIFACT}"\n'
        f'CANDIDATE_ARTIFACT_DIGEST = "{CANDIDATE_ARTIFACT_DIGEST}"\n'
        f'CANDIDATE_REPORT_SHA256 = "{CANDIDATE_REPORT_SHA256}"\n'
        f'CANDIDATE_MERGE = "{CANDIDATE_MERGE}"\n'
        f'ACCEPTANCE_RECORD = "{ACCEPTANCE_RECORD}"',
        "validator evidence constants",
    )
    for old, new in replacements:
        replace_once(validator, old, new, f"validator acceptance {old[:32]}")

    tests = ROOT / "tools/test_check_platform_diagnostic_advisory.py"
    replace_once(
        tests,
        'self.assertEqual(result["status"], "candidate_valid_non_authorizing")',
        'self.assertEqual(result["status"], "accepted_valid_non_authorizing")',
        "test accepted status",
    )


def main() -> int:
    accept_protocol()
    accept_adr()
    accept_work_package()
    accept_decisions()
    accept_current_state()
    accept_progress()
    accept_handoff()
    accept_index()
    accept_validator_and_tests()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    donor = (ROOT / "DONOR_RECOVERY.md").read_text(encoding="utf-8")
    adr0033 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    campaign = (ROOT / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md").read_text(encoding="utf-8")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current or "**Runtime implementation:** AUTHORIZED" in current:
        raise AcceptanceError("runtime boundary failed")
    if "**Status:** COMPLETE AND FROZEN" not in donor:
        raise AcceptanceError("Phase 0A is not frozen")
    if "Status: proposed" not in adr0033:
        raise AcceptanceError("ADR-0033 is not proposed")
    af03 = campaign.split("## AF03", 1)[1].split("## AF04", 1)[0]
    if "- status: READY / NOT STARTED" not in af03 or "- status: ACTIVE" in af03:
        raise AcceptanceError("AF03 state changed")
    print("Phase 0C-18 / ADR-0036 accepted-state transform complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
