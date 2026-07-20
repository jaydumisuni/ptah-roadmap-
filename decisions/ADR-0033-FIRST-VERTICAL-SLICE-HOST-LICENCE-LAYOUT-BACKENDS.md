# ADR-0033 — First vertical-slice host, licence, layout and backend selections

Status: proposed — selection records and non-claiming scaffold substantially complete; runtime implementation remains unauthorized

## Context

Phase 0B is frozen and Phase 0C is active. Runtime implementation remains unauthorized until the first concrete implementation set, public licence, source layout, dependency locks, CI gates and proof obligations are accepted and demonstrated.

## Proposed decision

Adopt the selections recorded in the following Phase 0C records as the baseline for the first Ptah vertical slice:

- `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md`;
- `work-packages/PHASE-0C-02-HOST-BASELINE-PIN.md`;
- `work-packages/PHASE-0C-03-DIRECT-DEPENDENCY-LICENCE-RECORD.md`;
- `work-packages/PHASE-0C-04-SOURCE-LAYOUT-AND-BOUNDARY-ACCEPTANCE.md`;
- `work-packages/PHASE-0C-05-WP14-IMPLEMENTATION-TASK-AND-PROOF-MAP.md`;
- `work-packages/PHASE-0C-06-CI-EXACT-HEAD-ACCEPTANCE-GATE.md`;
- `work-packages/PHASE-0C-08-NONCLAIMING-SCAFFOLD-EVIDENCE-REVIEW.md`.

The selected baseline is:

- Ubuntu Server 24.04.4 LTS amd64 installation image pinned by SHA-256;
- Noble GA 6.8 generic kernel line for the first proof image;
- Rust `1.97.1` as the primary Node/control implementation toolchain;
- `jaydumisuni/Ptah-space` as the implementation repository;
- SQLite `3.53.3` in WAL mode behind a repository-owned ledger interface;
- native Linux PTY/process supervision;
- containerd `2.3.1` with runc `1.4.2` behind an OCI Provider boundary;
- Node.js `24.18.0` LTS with Playwright `1.60.0` and its pinned Chromium build as the first Browser Provider;
- hardened Git `2.55.0` process adapter;
- libarchive `3.8.7` first decomposition adapter;
- repository-owned resumable transfer and local content-addressed storage;
- Apache License 2.0 recommendation for public Ptah-owned source, excluding private THETECHGUY knowledge, customer/device data and restricted workflows.

## Non-core workload registry

`work-packages/PHASE-0C-07-REAL-WORKLOAD-CANDIDATE-REGISTRY.md` records useful later proof workloads including `linux-0.11-rs`, MIBU, TTG Device X-Ray and TTG Device Manager. That registry does not select those projects as Ptah Core or first-slice dependencies.

## Merged non-claiming scaffold evidence

`Ptah-space` pull request 2 was merged at:

```text
ff26fa93d1b60781b49f33f5d1758680e1282d5f
```

The exact scaffold head:

```text
2f1fcedaa398254e5fa4b82583675a08755fa953
```

passed workflow run `29717770393`, including the no-build guard, Rust `1.97.1` formatting/Clippy/tests and locked Browser Provider syntax/tests. This evidence proves only the repository/toolchain scaffold and does not prove a Ptah runtime.

## Conditions before acceptance

### Completed at candidate/evidence level

The following conditions now have concrete reviewed records or exact-head scaffold evidence:

1. exact host image, kernel line and capability requirements;
2. direct external dependency version and licence candidates;
3. implementation repository and source layout;
4. implementation task graph mapped to WP14 proof obligations;
5. required CI and immutable exact-head evidence shape;
6. a merged non-claiming Rust/Browser workspace scaffold;
7. exact empty Rust and Playwright npm locks for the scaffold;
8. passing scaffold no-build, formatting, lint and test jobs.

### Still open

This ADR remains proposed until all of the following are complete:

1. the owner accepts the Apache-2.0 public/private boundary;
2. `Ptah-space` adds the accepted public `LICENSE`, final `NOTICE` and contribution/security boundary;
3. every selected external Rust crate, system package and distributed binary/source artifact has an exact lock, authoritative hash/signature, licence inventory and advisory review;
4. the frozen public catalog set is fully populated in `contracts/upstream-lock.json` by path, URN and digest;
5. generated bindings reproduce offline and their output-tree digest is recorded;
6. the host capability collector is implemented and a report is produced on the pinned host image revision;
7. CI runs dependency policy, frozen-contract generation, WP13 and Phase 0C closure checks at the exact candidate commit;
8. a Phase 0C closure review confirms no frozen contract was weakened;
9. this ADR is changed to accepted;
10. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED` in the same reviewed closure change.

## Consequences

- the first slice remains one-Node and local-first;
- distributed transport, PostgreSQL, ORAS, BuildKit and stronger isolation remain replaceable later backends;
- backend IDs remain Aliases;
- public Ptah Core remains separate from private THETECHGUY Domain Packs and restricted recovery adapters;
- concrete implementation may not weaken any frozen Phase 0B identity, lifecycle, migration or proof boundary;
- security updates or dependency rebases create new Host/Provider revisions and require the relevant proof rerun;
- failure of any open condition leaves implementation unauthorized.

## Acceptance form

When the open conditions pass, the acceptance change must record:

- exact `Ptah-space` commit;
- exact dependency and host-lock digests;
- CI workflow/report digests;
- WP13 exact-head result;
- Phase 0C closure review;
- explicit implementation authorization.

A decision text without those artifacts is insufficient.