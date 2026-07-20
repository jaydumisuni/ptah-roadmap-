# ADR-0033 — First vertical-slice host, licence, layout and backend selections

Status: proposed — selection, scaffold and frozen-conformance evidence substantially complete; runtime implementation remains unauthorized

## Context

Phase 0B is frozen and Phase 0C is active. Runtime implementation remains unauthorized until the first concrete implementation set, public licence, source layout, dependency locks, generated contract bindings, host evidence, CI gates and proof obligations are accepted and demonstrated.

## Proposed decision

Adopt the selections recorded in the following Phase 0C records as the baseline for the first Ptah vertical slice:

- `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md`;
- `work-packages/PHASE-0C-02-HOST-BASELINE-PIN.md`;
- `work-packages/PHASE-0C-03-DIRECT-DEPENDENCY-LICENCE-RECORD.md`;
- `work-packages/PHASE-0C-04-SOURCE-LAYOUT-AND-BOUNDARY-ACCEPTANCE.md`;
- `work-packages/PHASE-0C-05-WP14-IMPLEMENTATION-TASK-AND-PROOF-MAP.md`;
- `work-packages/PHASE-0C-06-CI-EXACT-HEAD-ACCEPTANCE-GATE.md`;
- `work-packages/PHASE-0C-08-NONCLAIMING-SCAFFOLD-EVIDENCE-REVIEW.md`;
- `work-packages/PHASE-0C-09-IMMUTABLE-ACTION-AND-FROZEN-CONFORMANCE-EVIDENCE.md`.

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

The initial `Ptah-space` scaffold merged at:

```text
ff26fa93d1b60781b49f33f5d1758680e1282d5f
```

The initial exact head `2f1fcedaa398254e5fa4b82583675a08755fa953` passed workflow run `29717770393`, including the no-build guard, Rust `1.97.1` formatting/Clippy/tests and locked Browser Provider syntax/tests.

Evidence hardening was then tested at exact head:

```text
900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc
```

Workflow run `29717942201` passed:

- exact-head source-policy/no-build checks;
- Rust formatting, Clippy, tests and locked metadata;
- Browser locked installation, syntax, tests and dependency inventory;
- frozen WP13 harness unit, structural and semantic conformance from local files;
- retained per-lane reports under immutable GitHub Action commit pins.

The hardening merged at:

```text
23fc97ff0acd2b219990411ec4fb84d8a8c0a567
```

This evidence proves only the repository/toolchain scaffold and frozen-contract conformance gate. It does not prove a Ptah runtime.

## Conditions before acceptance

### Completed at candidate/evidence level

1. exact host image, kernel line and capability requirements;
2. direct external dependency version and licence candidates;
3. implementation repository and source layout;
4. implementation task graph mapped to WP14 proof obligations;
5. required CI and immutable exact-head evidence shape;
6. a merged non-claiming Rust/Browser workspace scaffold;
7. exact empty Rust and Playwright npm locks for the scaffold;
8. passing source-policy, Rust and Browser scaffold jobs;
9. immutable GitHub Action commit pins;
10. passing frozen WP13 unit, structural and semantic conformance from `Ptah-space`;
11. retained exact-head artifact IDs and digests.

### Still open

This ADR remains proposed until all of the following are complete:

1. the owner accepts the Apache-2.0 public/private boundary;
2. `Ptah-space` adds the accepted public `LICENSE`, final `NOTICE` and contribution/security boundary;
3. every selected external Rust crate, system package and distributed binary/source artifact has an exact lock, authoritative hash/signature, licence inventory and advisory review;
4. the frozen public catalog set is fully populated in `contracts/upstream-lock.json` by path, URN and digest;
5. generated bindings reproduce offline and their output-tree digest is recorded;
6. the host capability collector is implemented and a report is produced on the pinned host image revision;
7. CI runs dependency policy and frozen-contract generation at the exact candidate commit;
8. final accepted reports are retained in a durable proof Location beyond temporary workflow artifact expiry;
9. a Phase 0C closure review confirms no frozen contract was weakened;
10. this ADR is changed to accepted;
11. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED` in the same reviewed closure change.

## Consequences

- the first slice remains one-Node and local-first;
- distributed transport, PostgreSQL, ORAS, BuildKit and stronger isolation remain replaceable later backends;
- backend IDs remain Aliases;
- public Ptah Core remains separate from private THETECHGUY Domain Packs and restricted recovery adapters;
- concrete implementation may not weaken any frozen Phase 0B identity, lifecycle, migration or proof boundary;
- security updates or dependency rebases create new Host/Provider revisions and require the relevant proof rerun;
- the current scaffold and conformance evidence do not authorize T01 runtime work;
- failure of any open condition leaves implementation unauthorized.

## Acceptance form

When the open conditions pass, the acceptance change must record:

- exact `Ptah-space` commit;
- exact dependency and host-lock digests;
- generated binding input/output digests;
- CI workflow/report and durable evidence digests;
- WP13 exact-head result;
- Phase 0C closure review;
- explicit implementation authorization.

A decision text without those artifacts is insufficient.