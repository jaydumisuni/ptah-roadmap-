# ADR-0002 — Composite Donor Closure Method

**Status:** ACCEPTED  
**Date:** 2026-07-17  
**Phase:** 0A requirement closure

## Context

Ptah is intended to become a more complete working environment than any single donor repository. A repository may implement one part strongly while omitting persistence, recovery, concurrency, local ownership, platform breadth, observability, proof, or an exit strategy.

Selecting one donor as the winner would cause Ptah to inherit that project's blind spots. Treating every donor as an equal dependency would create an unmaintainable collection of systems.

The correct approach is to begin from each Ptah requirement, combine the strongest compatible parts, and build only the neutral integration and missing capability that Ptah must own.

## Decision

Every Ptah requirement and subsystem must be closed through a **composite donor set**.

The donor set must identify:

1. **Internal foundation** — existing THETECHGUY work, requirements, experiments, code and proof.
2. **Primary capability donor** — the strongest inspected source for the central capability.
3. **Completion donors** — other repositories that supply important capabilities missing from the primary donor.
4. **Mature upstream machinery** — standards, engines and runtimes that should be used rather than recreated.
5. **Native Ptah layer** — contracts, integration, state and behavior Ptah must own.
6. **Fallback or exit donor** — a replacement path if the selected implementation becomes unsuitable.
7. **Validation set** — proof that the assembled Ptah subsystem covers the full requirement rather than merely reproducing one donor.

A donor can therefore be primary for one capability and only a completion donor, study source, workload or rejected path for another.

## Requirement-first inspection sequence

For every subsystem:

```text
Accepted Ptah requirement
        ↓
Recover internal work and intentional constraints
        ↓
Inspect the primary donor at source level
        ↓
List every capability and quality it does not provide
        ↓
Inspect completion donors specifically against those gaps
        ↓
Select mature upstream engines and standards
        ↓
Isolate the native Ptah contract and implementation gap
        ↓
Define an exit strategy and proof plan
        ↓
Close for design only when the complete requirement is covered
```

Repository popularity, feature count or README claims do not close a requirement.

## Completeness dimensions

Each composite donor set must be checked against the relevant dimensions:

- core engine or machinery;
- stable API or adapter boundary;
- persistence;
- concurrency;
- restart and reconnect recovery;
- cancellation and failure handling;
- logs, metrics, traces and evidence;
- local and THETECHGUY-owned deployment;
- online operation;
- future multi-node operation;
- cross-platform requirements;
- security and credential boundary;
- licence compatibility;
- maintainability and active upstream status;
- provider replacement or exit strategy;
- deterministic and live proof.

A requirement is not complete because one donor has a feature with the same name.

## OpenClaw and Daytona example

The first inspection established complementary strengths:

- OpenClaw contributes Node Protocol, gateway, presence, reconnect and terminal-session patterns.
- Daytona contributes workspace-provider lifecycle, runner separation, snapshots and environment-class patterns.

Neither is the complete Ptah runtime.

The cluster still requires inspection of:

- Coder, E2B and Dev Containers for workspace portability and long-lived human environments;
- containerd and OCI specifications for the actual owned execution foundation;
- Temporal for durable activity history and recovery;
- NATS and JetStream for live internal event transport and intermittent nodes;
- OpenTelemetry for end-to-end activity and node observability;
- native Ptah contracts joining Node, Workspace, Activity, Object and Session without collapsing them.

ADR-0001 remains valid as a boundary decision. Its donor selections are preliminary until the complete runtime donor cluster is inspected and proven.

## How the Requirement Closure Matrix changes

Every requirement record must distinguish:

- internal foundation;
- primary capability donor;
- completion donor set;
- fallback/exit donor;
- mature upstream machinery;
- native Ptah gap;
- licence decision;
- validation activity;
- closure status.

The phrase **primary donor** never means that Ptah copies the repository wholesale or stops researching its missing capabilities.

## Build rule

No implementation work is approved merely because a primary donor has been identified.

Build approval requires:

1. the primary donor's missing capabilities are explicitly recorded;
2. completion donors have been inspected against those gaps;
3. the native Ptah boundary is frozen;
4. licence and replacement decisions are recorded;
5. the validation plan proves the assembled subsystem.

## Continuous-save rule

Research and decisions must be saved as work proceeds, not reconstructed at the end.

After each meaningful inspection unit:

- update or create donor records;
- update the Requirement Closure Matrix;
- update `CURRENT_STATE.md`;
- update `PROGRESS.md`;
- create or amend an ADR when an architecture boundary changes;
- preserve unresolved gaps and rejected paths.

A future chat must be able to continue from the repository without relying on hidden conversation memory.

## Consequences

### Positive

- Ptah can exceed the completeness of individual donors.
- Missing capabilities remain visible rather than being hidden by donor selection.
- Strong existing machinery is reused without inheriting an entire product identity.
- Every subsystem retains an exit strategy.
- Internal THETECHGUY work is evaluated fairly rather than automatically replaced.

### Costs

- Phase 0A requires more disciplined source inspection.
- Some subsystem decisions remain provisional until their whole donor cluster is inspected.
- Ptah must maintain neutral contracts between several engines.

## Do-not-break rule

> Never declare a Ptah subsystem complete by selecting one repository. Close the requirement by assembling and proving the best compatible capability set, with Ptah owning the neutral contract and the missing integration.
