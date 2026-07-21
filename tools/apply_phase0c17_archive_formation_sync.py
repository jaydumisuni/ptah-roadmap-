#!/usr/bin/env python3
"""Synchronize Phase 0C-17 archive-formation candidate authority records."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SyncError(RuntimeError):
    pass


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SyncError(f"{label}: expected one source fragment, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def sync_memory_protocol() -> None:
    path = ROOT / "MEMORY_PROTOCOL.md"
    old = """A chat or model may not say work is safely recoverable when these durable records are stale.

---

# 6. Completion language
"""
    new = """A chat or model may not say work is safely recoverable when these durable records are stale.

## 5.1 Tenfold archive formation rule

Large recovery and archive campaigns use `planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md`.

The operating rule is:

```text
private force = max(20, human-equivalent workers × 10)
```

A standard twenty-private formation handles at most ten ordinary records through ten Primary Archivist / Independent Verifier pairs. Complex sources consume more pairs or escalate to 40/60/80–100/up to 120 privates rather than receiving weaker review.

Archive privates collect and challenge bounded evidence. They cannot promote truth, adopt donors, reopen frozen architecture, expand scope or authorize implementation. Archive Officers reconcile evidence; accepted review records promote only the bounded archive result.

Mandatory formation save points:

- mission and scope before evidence collection;
- after five reconciled records;
- after ten accepted records or formation completion;
- after a scope-changing blocker;
- before switching chat, model, operator or device.

`accepted for archive` does not mean a donor is adopted or that its claims become Ptah truth.

---

# 6. Completion language
"""
    replace_once(path, old, new, "MEMORY_PROTOCOL archive formation insertion")


def sync_donor_register() -> None:
    path = ROOT / "DONOR_RECOVERY.md"
    old = """Research catalogues, profiles and documentation tools use a lighter classification inspection, but can never close runtime requirements.

---

# 3. Foundation-grade donor groups
"""
    new = """Research catalogues, profiles and documentation tools use a lighter classification inspection, but can never close runtime requirements.

## 2A. Tenfold archival-completeness rule

Phase 0A remains complete and frozen. Large archival-completeness audits use:

- `planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md`;
- `archive/CAMPAIGN-001-FORMATION-MANIFEST.md`;
- `archive/ARCHIVE-RECORD-TEMPLATE.md`.

The first campaign maps 69 external and 29 internal source obligations into ten twenty-private formations. Each ordinary record receives one Primary Archivist and one Independent Verifier. The campaign reconciles existing donor records, exact current source and approved private records; it does not restart donor selection from zero.

The uploaded donor pool list is a queue seed, not current authority. Previously unresolved source hints may have been resolved by later accepted records and must be reconciled rather than copied blindly.

An archive record may be accepted as a trustworthy recovery record without adopting the donor, authorizing source reuse, changing Ptah architecture or reopening Phase 0A.

---

# 3. Foundation-grade donor groups
"""
    replace_once(path, old, new, "DONOR_RECOVERY archive formation insertion")


def sync_decisions() -> None:
    path = ROOT / "DECISIONS.md"
    old = """### ADR-0033 — First vertical-slice host, licence, layout and backend selections

**PROPOSED.** Master Plan/roadmap authority is complete. The physical pinned-host result, package and retention acceptance, final Phase 0C closure review and explicit runtime authorization remain open.
"""
    new = """### ADR-0033 — First vertical-slice host, licence, layout and backend selections

**PROPOSED.** Master Plan/roadmap authority is complete. The physical pinned-host result, package and retention acceptance, final Phase 0C closure review and explicit runtime authorization remain open.

### ADR-0035 — Tenfold archive formation and evidence promotion

**PROPOSED.** Borrows Sergeant's pinned tenfold private-force rule for Ptah recovery campaigns: minimum twenty privates, one primary/verifier pair per ordinary archive record, complexity escalation, bounded evidence packets and officer-only promotion. Phase 0A remains frozen, P01 remains active and runtime implementation remains unauthorized.

Full decision: `decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md`.
"""
    replace_once(path, old, new, "DECISIONS ADR-0035 insertion")


def sync_progress() -> None:
    path = ROOT / "PROGRESS.md"
    old = """- [x] ADR-0034 accepted; Master Plan and implementation roadmap version `1.0.0` are operative authorities.

## Active Phase 0C closure work
"""
    new = """- [x] ADR-0034 accepted; Master Plan and implementation roadmap version `1.0.0` are operative authorities.

## Tenfold archive formation candidate

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

## Active Phase 0C closure work
"""
    replace_once(path, old, new, "PROGRESS archive formation insertion")


def sync_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    old = """ADR-0034 is accepted. `MASTER_PLAN.md` and `IMPLEMENTATION_ROADMAP.md` version `1.0.0` are operative authorities. No new Core entity or current WP01–WP14 reopening was required. This closes planning authority only and does not accept the physical host, packages, retention, ADR-0033 or runtime implementation.

---

## Active Phase 0C blockers
"""
    new = """ADR-0034 is accepted. `MASTER_PLAN.md` and `IMPLEMENTATION_ROADMAP.md` version `1.0.0` are operative authorities. No new Core entity or current WP01–WP14 reopening was required. This closes planning authority only and does not accept the physical host, packages, retention, ADR-0033 or runtime implementation.

---

## Active Phase 0C-17 tenfold archive formation candidate

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

---

## Active Phase 0C blockers
"""
    replace_once(path, old, new, "CURRENT_STATE archive formation insertion")


def sync_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    old = """P00 Master-plan authority closure — COMPLETE
P01 Physical-host and ADR-0033 closure — ACTIVE / BLOCKED ON EXACT PHYSICAL HOST
Programme A Online Ptah Alpha — PLANNED / NOT AUTHORIZED
Programmes B–F — PLANNED
```

## Exact next action
"""
    new = """P00 Master-plan authority closure — COMPLETE
P01 Physical-host and ADR-0033 closure — ACTIVE / BLOCKED ON EXACT PHYSICAL HOST
Programme A Online Ptah Alpha — PLANNED / NOT AUTHORIZED
Programmes B–F — PLANNED
```

## Cross-cutting archive formation candidate

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

## Exact next action
"""
    replace_once(path, old, new, "AI_HANDOFF archive formation insertion")


def sync_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("runtime_implementation_authorized") is not False:
        raise SyncError("master-plan index unexpectedly authorizes runtime")
    if data.get("active_work_unit") != "P01-physical-host-and-ADR-0033-closure":
        raise SyncError("master-plan index active work drifted")
    recovery_order = data.get("recovery_order", [])
    protocol = "planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md"
    if protocol not in recovery_order:
        recovery_order.append(protocol)
    data["operational_protocols"] = {
        "tenfold_archive_formation": {
            "status": "candidate_under_review",
            "source_branch": "phase0c-tenfold-archive-formation",
            "pull_request": 26,
            "protocol": protocol,
            "campaign_manifest": "archive/CAMPAIGN-001-FORMATION-MANIFEST.md",
            "record_template": "archive/ARCHIVE-RECORD-TEMPLATE.md",
            "work_package": "work-packages/PHASE-0C-17-TENFOLD-ARCHIVE-FORMATION.md",
            "decision": "decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md",
            "sergeant_source_commit": "44c8f47f4bb50a73ef3b4d81d7b849a5aab37dfd",
            "private_force_multiplier": 10,
            "minimum_private_force": 20,
            "formation_count": 10,
            "allocated_private_count": 200,
            "assigned_record_count": 98,
            "phase_0a_reopened": False,
            "runtime_implementation_authorized": False,
        }
    }
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    sync_memory_protocol()
    sync_donor_register()
    sync_decisions()
    sync_progress()
    sync_current_state()
    sync_handoff()
    sync_index()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    adr0033 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    donor = (ROOT / "DONOR_RECOVERY.md").read_text(encoding="utf-8")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current:
        raise SyncError("runtime non-authorization missing")
    if "**Runtime implementation:** AUTHORIZED" in current:
        raise SyncError("runtime authorization appeared")
    if "Status: proposed" not in adr0033:
        raise SyncError("ADR-0033 is no longer proposed")
    if "**Status:** COMPLETE AND FROZEN" not in donor:
        raise SyncError("Phase 0A donor register is no longer frozen")

    print("Phase 0C-17 archive formation authority records synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
