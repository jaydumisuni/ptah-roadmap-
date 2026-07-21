#!/usr/bin/env python3
"""Apply the guarded Phase 0C-16 master-plan control-book synchronization."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SyncError(RuntimeError):
    pass


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SyncError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.write_text(text.rstrip() + "\n", encoding="utf-8")


def update_readme() -> None:
    write(
        "README.md",
        """# Ptah Roadmap

Private canonical product plan, implementation roadmap, recovery memory, progress ledger and decision control for **Ptah Space**.

This repository answers:

1. What is Ptah meant to become?
2. What exact product and operating scope is accepted?
3. What work is dependency-ordered next?
4. What has been frozen, proven or completed?
5. What must the next chat or AI read before continuing?

## Repository boundary

- `jaydumisuni/Ptah-space` contains public implementation, public-safe technical documentation, tests and earned public progress.
- `jaydumisuni/ptah-roadmap-` contains the private Master Plan, implementation roadmap, donor recovery, decisions, progress, evidence control and durable handoff state.
- Public Ptah must not expose private consumers, company operating chains, restricted recovery knowledge, customer/device data or this private control repository.

## Mandatory recovery order

Read in this order before proposing or performing Ptah work:

1. `AI_HANDOFF.md`
2. `CURRENT_STATE.md`
3. `master-plan-index.json`
4. `MASTER_PLAN.md`
5. `IMPLEMENTATION_ROADMAP.md`
6. `planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md`
7. `planning/MASTER-PLAN-RECONCILIATION.md`
8. `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`
9. `PROGRESS.md`
10. `DECISIONS.md` and referenced ADRs
11. `MEMORY_PROTOCOL.md`
12. current source and open work in `jaydumisuni/Ptah-space`

Do not ask the owner to repeat information recoverable from these records.

## Highest rules

- Ptah is the world where work happens, not the intelligence deciding what work should happen.
- Ptah is independent and open source; private systems consume public-safe contracts.
- A Workspace persists and may host many concurrent Activities.
- Objects, Revisions, Views and Artifacts are structured and provenance-bound.
- Internet is a normal capability; local/offline restrictions are explicit.
- Active work uses capable Node-local storage; durable bytes may synchronize remotely.
- Existing internal and external work is recovered before rebuilding.
- No implementation begins merely because an idea is useful; it must be planned, ordered, selected and approved.
- Every work item follows Understand → Build → Review → Freeze → Prove → Submit/Ship.
- Substantial work is saved durably as it proceeds so another chat or AI can resume.

## Status vocabulary

- `PLANNED`
- `READY`
- `ACTIVE`
- `BLOCKED`
- `IN REVIEW`
- `FROZEN`
- `PROVEN`
- `COMPLETE`
- `PARKED`
- `REJECTED`

## Update rule

After every substantial Ptah work session:

1. save implementation/evidence checkpoints where applicable;
2. update `AI_HANDOFF.md` and `master-plan-index.json`;
3. update `PROGRESS.md` and `CURRENT_STATE.md`;
4. update `DECISIONS.md` when architecture or governance changes;
5. update donor records when donor understanding changes;
6. update `MASTER_PLAN.md` only when accepted product/operating intent changes;
7. update `IMPLEMENTATION_ROADMAP.md` when accepted sequencing, dependencies or proof gates change;
8. publish to `Ptah-space` only source and progress it has actually earned.

## Current position

Phase 0A donor closure and Phase 0B contracts are frozen. Phase 0C is active. The Master Plan and detailed implementation roadmap closure package is under review. Physical pinned-host evidence, ADR-0033 acceptance and explicit runtime authorization remain open.

**Runtime implementation is NOT AUTHORIZED.**
""",
    )


def update_memory_protocol() -> None:
    path = ROOT / "MEMORY_PROTOCOL.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        """# 1. Mandatory recovery order

Before evaluating, planning, designing, editing, or building Ptah:

1. Read `CURRENT_STATE.md`.
2. Read `MASTER_ROADMAP.md`.
3. Read `PROGRESS.md`.
4. Read `DECISIONS.md`.
5. Read `DONOR_RECOVERY.md`.
6. Inspect the current state of `jaydumisuni/Ptah-space`.
7. Inspect any donor or internal repository directly related to the selected work item.

Do not ask the user to re-explain information that can be recovered from these sources.
""",
        """# 1. Mandatory recovery order

Before evaluating, planning, designing, editing, or building Ptah:

1. Read `AI_HANDOFF.md`.
2. Read `CURRENT_STATE.md`.
3. Read `master-plan-index.json`.
4. Read `MASTER_PLAN.md`.
5. Read `IMPLEMENTATION_ROADMAP.md`.
6. Read `planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md`.
7. Read `planning/MASTER-PLAN-RECONCILIATION.md`.
8. Read `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`.
9. Read `PROGRESS.md`.
10. Read `DECISIONS.md` and the relevant ADRs.
11. Read `DONOR_RECOVERY.md` when donor or requirement context is relevant.
12. Inspect the current state of `jaydumisuni/Ptah-space`.
13. Inspect any donor or internal repository directly related to the selected work item.

Do not ask the owner to re-explain information recoverable from these sources.
""",
        "memory recovery order",
    )
    text = replace_once(
        text,
        """- present in `MASTER_ROADMAP.md`;
- ordered after its dependencies;
""",
        """- present in `MASTER_PLAN.md`;
- placed and ordered after its dependencies in `IMPLEMENTATION_ROADMAP.md`;
""",
        "work selection authority",
    )
    text = replace_once(
        text,
        """1. implementation repository source and tests;
2. implementation evidence;
3. `PROGRESS.md`;
4. `CURRENT_STATE.md`;
5. `DECISIONS.md` if architecture changed;
6. `DONOR_RECOVERY.md` if donor understanding changed;
7. `MASTER_ROADMAP.md` only when the accepted plan changed.
""",
        """1. implementation repository source and tests;
2. implementation evidence;
3. a durable intermediate checkpoint when the task is not yet finished;
4. `AI_HANDOFF.md`;
5. `master-plan-index.json`;
6. `PROGRESS.md`;
7. `CURRENT_STATE.md`;
8. `DECISIONS.md` if architecture or governance changed;
9. `DONOR_RECOVERY.md` if donor understanding changed;
10. `MASTER_PLAN.md` only when accepted product/operating intent changed;
11. `IMPLEMENTATION_ROADMAP.md` when sequencing, dependencies or proof gates changed.
""",
        "after work order",
    )
    marker = "# 5. Completion language\n"
    if marker not in text:
        raise SyncError("memory save-as-you-go marker missing")
    save_section = """# 5. Save-as-you-go checkpoint rule

Substantial work must be durably checkpointed before the full task is complete.

A checkpoint records:

- repository and branch;
- exact commit;
- completed files or work packages;
- active and incomplete work;
- failures and limitations;
- retained evidence;
- blockers;
- safest next action;
- runtime authorization state.

`AI_HANDOFF.md` is the concise recovery entry. `master-plan-index.json` is the machine-readable entry. They summarize but do not replace accepted decisions, contracts or evidence.

A chat or model may not say work is safely recoverable when these durable records are stale.

---

# 6. Completion language
"""
    text = text.replace(marker, save_section, 1)
    for number in range(6, 11):
        text = text.replace(f"# {number}. ", f"# {number + 1}. ")
    write("MEMORY_PROTOCOL.md", text)


def update_donor_recovery() -> None:
    path = ROOT / "DONOR_RECOVERY.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "**Status:** ARCHITECTURE RECOVERY COMPLETE — FINAL CONSISTENCY REVIEW ACTIVE",
        "**Status:** COMPLETE AND FROZEN — later donor additions require explicit roadmap placement",
        "donor status",
    )
    marker = "# 9. Final Phase 0A review\n"
    if marker not in text:
        raise SyncError("donor final review marker missing")
    prefix = text.split(marker, 1)[0]
    tail = """# 9. Final Phase 0A review

Result: **COMPLETE AND FROZEN** at roadmap commit `7d2dffee48f1400ba1cf88823343f09a3895ad33` through ADR-0017.

The completed review covered:

1. identity consistency across ADRs and work packages;
2. authority and permission consistency;
3. state and proof-level consistency;
4. lifecycle, deletion and recovery consistency;
5. parked, rejected and blocked gap audit;
6. Phase 0B schema, migration, conformance and proof-corpus entry requirements;
7. freeze/readiness decision.

Later donors, including the AI Project Workspace behavioural donor, may be added as non-operative studies or implementation donors only through explicit Master Plan and implementation-roadmap placement. They do not reopen Phase 0A or authorize runtime by themselves.

Runtime implementation remains governed by Phase 0C, physical-host evidence and ADR-0033.
"""
    write("DONOR_RECOVERY.md", prefix + tail)


def update_master_roadmap() -> None:
    path = ROOT / "MASTER_ROADMAP.md"
    text = path.read_text(encoding="utf-8")
    if "---" not in text:
        raise SyncError("master roadmap separator missing")
    _, body = text.split("---", 1)
    preamble = """# Ptah Space — Historical Architecture and Phase Roadmap

**Status:** retained source; superseded as primary planning authority by `MASTER_PLAN.md` and `IMPLEMENTATION_ROADMAP.md` after ADR-0034 acceptance  
**Current phase:** Phase 0C — Master Plan closure, physical-host evidence and authorization  
**Implementation:** Not authorized  
**Phase 0A frozen checkpoint:** `7d2dffee48f1400ba1cf88823343f09a3895ad33`  
**Phase 0B frozen checkpoint:** `dc2db457f1705d0cba80f17ab76e5e93f808aee0`  
**Public implementation repository:** `jaydumisuni/Ptah-space`

This file preserves the architecture laws, original phase intent and release-milestone source used to recover the complete Master Plan. It is no longer sufficient by itself as the product plan or dependency-complete implementation programme.

Use:

- `MASTER_PLAN.md` for product and operating intent;
- `IMPLEMENTATION_ROADMAP.md` for work-package sequencing and proof;
- `CURRENT_STATE.md` for the exact selected action and authorization;
- `AI_HANDOFF.md` and `master-plan-index.json` for recovery.

The body below remains historical source material and may not override newer accepted decisions or frozen contracts.

---"""
    write("MASTER_ROADMAP.md", preamble + body)


def update_decisions() -> None:
    path = ROOT / "DECISIONS.md"
    text = path.read_text(encoding="utf-8")
    if "ADR-0025-DOMAIN-FIRMWARE-DISK-DEVICE-BOUNDARY.md" in text:
        raise SyncError("decision completion section already present")
    addition = """

---

## Phase 0B completion decisions

### D-040 — Domain Pack, firmware, disk, filesystem and Device boundaries are explicit

**ACCEPTED.** WP08 preserves Domain Packs, firmware packages, Disk Images, filesystems, Devices, protocol Operations, recovery and physical mutation as separate identities and proof levels. Static analysis and write acknowledgement cannot authorize or prove physical mutation.

Full decision: `decisions/ADR-0025-DOMAIN-FIRMWARE-DISK-DEVICE-BOUNDARY.md`.

### D-041 — Application, Browser, semantic UI and human Shell boundaries are explicit

**ACCEPTED.** WP09 separates Application, Installation, Session, Process, Window and display; Browser Profile, Process, Context and Page; Semantic snapshots/targets/actions; and Shell clients, panels, layouts and control transfer. UI state cannot become runtime truth.

Full decision: `decisions/ADR-0026-APPLICATION-BROWSER-SEMANTIC-UI-SHELL-BOUNDARY.md`.

### D-042 — Knowledge, Data, Package and Plugin boundaries are explicit

**ACCEPTED.** WP10 defines neutral Knowledge Sources, revisions, indexes, queries, citations, datasets, tables, packages, releases, installations, Plugins and activations. Indexes remain derived and caller reasoning/private memory remains external.

Full decision: `decisions/ADR-0027-KNOWLEDGE-DATA-PACKAGE-PLUGIN-BOUNDARY.md`.

### D-043 — Isolation, placement, reservations, Leases and secure Grants are explicit

**ACCEPTED.** WP11 separates Isolation Class, runtime Provider, capability snapshot, placement, Reservation, Lease, Generation, Fence and secure Grants. Silent isolation or authority weakening is prohibited.

Full decision: `decisions/ADR-0028-ISOLATION-PLACEMENT-RESERVATION-LEASE-SECURE-GRANTS-BOUNDARY.md`.

### D-044 — Security Observation, Finding, Claim, Evidence and reproduction are explicit

**ACCEPTED.** WP12 separates authorization, target, plan, Observation, Finding, validation, disposition, remediation, Verification Run, Reproduction Run, bounded Claim and Evidence. Scanner output cannot become accepted truth by itself.

Full decision: `decisions/ADR-0029-SECURITY-FINDING-CLAIM-EVIDENCE-REPRODUCTION-BOUNDARY.md`.

### D-045 — Executable conformance and exact-head proof are mandatory

**ACCEPTED.** WP13 provides offline structural and semantic conformance, local URN resolution, catalog/lifecycle/fixture integrity and exact-head reports. It found and forced correction of real cross-package defects.

Full decision: `decisions/ADR-0030-EXECUTABLE-CONFORMANCE-AND-EXACT-HEAD-PROOF.md`.

### D-046 — Golden/negative corpus and proof-plan freeze are authoritative

**ACCEPTED.** WP14 freezes lawful positive, negative and adversarial fixtures, immutable expected-proof records and the first vertical-slice proof burden. A green summary without retained reports fails acceptance.

Full decision: `decisions/ADR-0031-GOLDEN-NEGATIVE-CORPUS-AND-PROOF-PLAN-FREEZE.md`.

### D-047 — Phase 0B is frozen and Phase 0C selection is active

**ACCEPTED.** WP01–WP14 are frozen at `dc2db457f1705d0cba80f17ab76e5e93f808aee0`. Runtime dependency, host, licence, source-layout and first-slice selections belong to Phase 0C.

Full decision: `decisions/ADR-0032-PHASE-0B-FREEZE-PHASE-0C-ENTRY.md`.

---

## Phase 0C accepted governance and design evidence

### D-048 — Apache-2.0 public/private boundary is operative

**ACCEPTED.** Public repository-owned Ptah source is Apache-2.0 under `John Dumisuni trading as THETECHGUY DIGITAL SOLUTIONS`. Private THETECHGUY systems, customer/device/payment data, restricted adapters, donor source and trademarks remain excluded.

Evidence: `work-packages/PHASE-0C-14-APACHE-2.0-OWNER-ACCEPTANCE.md`.

### D-049 — AI Project Workspace is a provider-independent composition profile

**ACCEPTED AS NON-OPERATIVE DESIGN EVIDENCE.** `ptah.workspace.ai_project.v1` composes existing frozen primitives. Hidden provider memory and implicit global tool access are rejected. Ptah owns durable truth and Grants; Hunter coordinates through bounded context packets.

Evidence: `work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md`.

---

## Current proposed decisions

### ADR-0033 — First vertical-slice host, licence, layout and backend selections

**PROPOSED.** Selection and tooling evidence is substantially complete, but the accepted Master Plan/roadmap, physical pinned-host result, package/retention acceptance and final closure review remain open.

### ADR-0034 — Master Plan, implementation roadmap and durable handoff authority

**PROPOSED.** Establishes separate product-plan, delivery-roadmap, current-state and recovery authorities with save-as-you-go checkpoints. It may be accepted with Phase 0C-16 after exact-head review.
"""
    write("DECISIONS.md", text + addition)


def update_progress() -> None:
    path = ROOT / "PROGRESS.md"
    text = path.read_text(encoding="utf-8")
    marker = "## Active Phase 0C closure work\n"
    if marker not in text:
        raise SyncError("progress closure marker missing")
    section = """## Master Plan and implementation roadmap closure

- [x] requirements, architecture laws, accepted decisions and known gaps recovered into one ledger;
- [x] complete product and operating Master Plan candidate written;
- [x] detailed dependency-ordered Programme P00/P01 and Programmes A–F roadmap candidate written;
- [x] WP01–WP14 and Phase 0C reconciliation completed with zero current Core extensions;
- [x] physical-host through ADR-0033 and authorization procedure recorded;
- [x] durable `AI_HANDOFF.md` and `master-plan-index.json` created;
- [x] proposed ADR-0034 and Phase 0C-16 evidence package created;
- [-] repair stale control-book records and run exact-head consistency validation;
- [ ] review and merge Phase 0C-16;
- [ ] accept ADR-0034 in the reviewed Phase 0C-16 merge.

"""
    text = text.replace(marker, section + marker, 1)
    text = replace_once(
        text,
        """## Active Phase 0C closure work

- [x] select the minimal external Rust crate/features graph;
""",
        """## Active Phase 0C closure work

- [-] review and merge the complete Master Plan and implementation roadmap closure package;
- [x] select the minimal external Rust crate/features graph;
""",
        "progress active plan blocker",
    )
    impl_marker = "# Implementation phases\n"
    if impl_marker not in text:
        raise SyncError("progress implementation marker missing")
    prefix = text.split(impl_marker, 1)[0]
    programme = """# Implementation programme

No runtime package may become READY or ACTIVE before Phase 0C authorization.

## Programme P00 — Planning and authorization

- [-] P00 — Master-plan authority closure.
- [?] P01 — Physical-host and ADR-0033 closure; blocked on the exact external host after P00 merge.

## Programme A — Online Ptah Alpha

- [ ] A01 — Repository, contracts and reproducible scaffold.
- [ ] A02 — Node identity, Generation and host truth.
- [ ] A03 — Ledger, schema versions and crash-safe migrations.
- [ ] A04 — Activity, Operation, Attempt, Event and Receipt runtime.
- [ ] A05 — Native process, PTY and multi-terminal Provider.
- [ ] A06 — Persistent Workspace, Session and authority projection.
- [ ] A07 — Object, Revision, Artifact, Location and local CAS.
- [ ] A08 — Upload and resumable download engine.
- [ ] A09 — Hardened Git Provider.
- [ ] A10 — OCI container Provider.
- [ ] A11 — Browser Provider.
- [ ] A12 — Archive decomposition Provider.
- [ ] A13 — Checkpoint, restart and verified recovery.
- [ ] A14 — Human Alpha control surface.
- [ ] A15 — Exact-head Online Ptah Alpha acceptance.

## Later programmes

- [ ] Programme B — Object World Beta.
- [ ] Programme C — Firmware and Device Beta.
- [ ] Programme D — Full Workspace Release.
- [ ] Programme E — Distributed Ptah.
- [ ] Programme F — OS-ready foundation private lane.

Detailed package dependencies, deliverables and proof gates are authoritative in `IMPLEMENTATION_ROADMAP.md`.
"""
    write("PROGRESS.md", prefix + programme)


def update_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "**Active work unit:** 0C-04 — physical pinned-host proof, durable evidence and licence closure",
        "**Active work unit:** 0C-16 — complete Master Plan, implementation roadmap and durable AI handoff closure",
        "current active work unit",
    )
    marker = "## Active Phase 0C blockers\n"
    if marker not in text:
        raise SyncError("current blocker marker missing")
    phase_section = """## Active Phase 0C-16 Master Plan closure

Planning branch:

```text
phase0c-master-plan-roadmap-closure
```

Durable candidate records:

- `planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md`;
- `MASTER_PLAN.md`;
- `IMPLEMENTATION_ROADMAP.md`;
- `planning/MASTER-PLAN-RECONCILIATION.md`;
- `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`;
- `AI_HANDOFF.md`;
- `master-plan-index.json`;
- `decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md`;
- `work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md`.

The candidate recovers the full product/operating plan, derives Programme P00/P01 and Programmes A–F, maps every frozen WP01–WP14 package and Phase 0C record, and introduces no current Core extension. It remains under review and does not authorize runtime.

---

"""
    text = text.replace(marker, phase_section + marker, 1)
    old_blockers = """Implementation remains unauthorized until all of the following are merged and reviewed:

1. a proof-eligible capability report from the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
2. the exact installed Ubuntu package manifest and package-artifact digests from that pinned host, with reviewer acceptance;
3. generation, durable commit and explicit review acceptance of that physical-host evidence bundle;
4. a Phase 0C closure review proving no frozen contract was weakened;
5. acceptance of ADR-0033;
6. explicit `Runtime implementation: AUTHORIZED` in this file in the same reviewed closure change.
"""
    new_blockers = """Implementation remains unauthorized until all of the following are merged and reviewed:

1. acceptance of the complete Master Plan, detailed implementation roadmap, reconciliation and durable handoff through Phase 0C-16 / ADR-0034;
2. a proof-eligible capability report from the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
3. the exact installed Ubuntu package manifest and package-artifact digests from that pinned host, with reviewer acceptance;
4. generation, durable commit and explicit review acceptance of that physical-host evidence bundle;
5. a Phase 0C closure review proving no frozen contract was weakened;
6. acceptance of ADR-0033;
7. explicit `Runtime implementation: AUTHORIZED` in this file in the same reviewed closure change.
"""
    text = replace_once(text, old_blockers, new_blockers, "current blockers")
    continuation = "## Immediate continuation order\n"
    if continuation not in text:
        raise SyncError("current continuation marker missing")
    prefix = text.split(continuation, 1)[0]
    tail = """## Immediate continuation order

1. Complete exact-head validation and direct review of `phase0c-master-plan-roadmap-closure`.
2. Accept ADR-0034 and merge Phase 0C-16 while retaining `Runtime implementation: NOT AUTHORIZED`.
3. Install or recover the exact Ubuntu Server 24.04.4 / `6.8.0-136-generic` proof host.
4. From the selected clean reviewed `Ptah-space` commit, run:

```bash
python3 tools/run_pinned_host_proof.py \
  --repo-root . \
  --output evidence/phase0c/pinned-host-candidate
```

5. Require `proof_eligible: true` with empty host, capability, package-artifact and repository failure sets.
6. Review and accept the complete installed package and package-artifact manifests.
7. From the same exact clean commit, run:

```bash
python3 tools/retain_verified_pinned_host_evidence.py \
  --repo-root . \
  --bundle-dir evidence/phase0c/pinned-host-candidate \
  --output-dir evidence/phase0c/pinned-host-durable-candidate
```

8. Commit and explicitly accept the durable candidate and repository binding.
9. Conduct the final Phase 0C closure consistency review.
10. Accept ADR-0033 and authorize runtime only when every blocker passes.
"""
    write("CURRENT_STATE.md", prefix + tail)


def update_adr0033() -> None:
    path = ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "Status: proposed — Rust dependencies, distributed backend artifacts, signers, host collector, physical-proof, durable-retention and Apache-2.0 governance complete; physical pinned-host result, package and retention acceptance and closure review remain open",
        "Status: proposed — dependency, backend, signer, proof, retention and licence governance complete; Master Plan acceptance, physical pinned-host result, package/retention acceptance and closure review remain open",
        "adr0033 status",
    )
    text = replace_once(
        text,
        """- `work-packages/PHASE-0C-13-DURABLE-PINNED-HOST-RETENTION-READINESS.md`;
- `work-packages/PHASE-0C-14-APACHE-2.0-OWNER-ACCEPTANCE.md`.
""",
        """- `work-packages/PHASE-0C-13-DURABLE-PINNED-HOST-RETENTION-READINESS.md`;
- `work-packages/PHASE-0C-14-APACHE-2.0-OWNER-ACCEPTANCE.md`;
- `work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md`;
- `work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md`.
""",
        "adr0033 records",
    )
    old = """This ADR remains proposed until all of the following are complete:

1. a proof-eligible capability report is produced on the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
2. the exact installed Ubuntu package manifest and package-artifact digests are recorded from that host and accepted by review;
3. that host's exact source bundle is independently verified, durably committed and explicitly accepted through its review record;
4. a Phase 0C closure review confirms no frozen contract was weakened;
5. this ADR is changed to accepted;
6. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED` in the same reviewed closure change.
"""
    new = """This ADR remains proposed until all of the following are complete:

1. the complete `MASTER_PLAN.md`, `IMPLEMENTATION_ROADMAP.md`, reconciliation and durable handoff are accepted through Phase 0C-16 and ADR-0034;
2. a proof-eligible capability report is produced on the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
3. the exact installed Ubuntu package manifest and package-artifact digests are recorded from that host and accepted by review;
4. that host's exact source bundle is independently verified, durably committed and explicitly accepted through its review record;
5. a Phase 0C closure review confirms no frozen contract was weakened;
6. this ADR is changed to accepted;
7. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED` in the same reviewed closure change.
"""
    text = replace_once(text, old, new, "adr0033 conditions")
    write(path.relative_to(ROOT).as_posix(), text)


def main() -> None:
    update_readme()
    update_memory_protocol()
    update_donor_recovery()
    update_master_roadmap()
    update_decisions()
    update_progress()
    update_current_state()
    update_adr0033()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current:
        raise SyncError("runtime non-authorization disappeared")
    if "**Runtime implementation:** AUTHORIZED" in current:
        raise SyncError("control sync attempted runtime authorization")
    adr = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    if "Status: proposed" not in adr:
        raise SyncError("ADR-0033 cannot be accepted by the planning sync")
    print("Phase 0C-16 control-book synchronization prepared successfully")


if __name__ == "__main__":
    try:
        main()
    except SyncError as exc:
        raise SystemExit(str(exc)) from exc
