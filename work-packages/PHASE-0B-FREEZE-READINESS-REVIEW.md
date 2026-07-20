# Phase 0B freeze readiness review

Status: candidate freeze

## Completed ordered work packages

- WP01 Common identity, versioning and typed families
- WP02 Activity, Operation, Attempt, Event, Receipt and proof
- WP03 Object, Revision, View, Artifact and storage
- WP04 Node, Facility, Provider, capability and health
- WP05 Workspace, Session, checkpoint, restore and recovery
- WP06 Transfer, synchronization, conflict, backup and restore
- WP07 Recipe, Build, provenance, SBOM, signature and verification
- WP08 Domain Pack, firmware, disk, filesystem and Device
- WP09 Application, Browser, semantic UI and Shell
- WP10 Knowledge, Data, Package and Plugin
- WP11 Isolation, placement, reservation, Lease and secure grants
- WP12 Security, Finding, Claim, Evidence, remediation and reproduction
- WP13 executable cross-contract conformance
- WP14 golden/negative corpus and proof-plan freeze

## Executable evidence

The Phase 0B conformance workflow passed on the exact WP13 and WP14 pull-request heads. It validated all discovered JSON, JSON Schema 2020-12 structures, local URNs and references, active catalogs, versioned lifecycle machines, fixture identities and executable semantic rules. Structural and semantic reports were uploaded as immutable commit-specific workflow artifacts.

WP13 also found and forced correction of real defects: malformed WP03/WP06 JSON, a missing WP08 Disk Image identity schema, lifecycle-format drift, stale catalog namespace aliases and an incomplete disposition fixture.

## Freeze findings

- Canonical identity remains backend-neutral.
- Retry, generation, epoch, Lease and fence rules are explicit.
- acknowledgement, observation, verification, review and acceptance remain distinct.
- privacy, audience, redaction and retention are present across packages.
- migration and backend replacement are explicit.
- failed, negative and inconclusive evidence is retained.
- the first implementation slice has a frozen proof burden.
- runtime implementation and dependency selection remain unauthorized until Phase 0C.

## Remaining Phase 0C decisions

1. select the Linux host baseline;
2. select the public Ptah licence;
3. approve implementation repository/source layout;
4. select exact first backends for neutral contracts;
5. approve the first vertical-slice implementation plan;
6. record implementation authorization in `CURRENT_STATE.md`.
