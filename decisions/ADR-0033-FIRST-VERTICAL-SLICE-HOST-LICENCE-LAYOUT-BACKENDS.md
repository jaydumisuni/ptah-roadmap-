# ADR-0033 — First vertical-slice host, licence, layout and backend selections

Status: proposed

## Context

Phase 0B is frozen and Phase 0C is active. Runtime implementation remains unauthorized until the first concrete implementation set, public licence, source layout and proof obligations are accepted.

## Proposed decision

Adopt the selections recorded in `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md` as the baseline for the first Ptah vertical slice:

- Ubuntu Server 24.04 LTS family on x86_64;
- Rust as the primary Node/control implementation language;
- `jaydumisuni/Ptah-space` as the implementation repository;
- SQLite WAL behind a repository-owned ledger interface;
- native Linux PTY/process supervision;
- OCI/containerd-compatible container adapter;
- Playwright with Chromium Browser Provider;
- hardened Git CLI adapter;
- libarchive first decomposition adapter;
- repository-owned resumable transfer and local content-addressed storage;
- Apache License 2.0 recommendation for public Ptah-owned source, excluding private THETECHGUY knowledge and data.

## Conditions before acceptance

This ADR remains proposed until:

1. the owner accepts the public licence boundary;
2. exact host image/kernel capabilities are pinned;
3. exact dependency versions and licences are recorded;
4. the implementation task graph is mapped to WP14 proof cases;
5. CI includes Rust checks, WP13 conformance and frozen proof-plan execution;
6. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED`.

## Consequences

- the first slice remains one-Node and local-first;
- distributed transport, PostgreSQL, ORAS, BuildKit and stronger isolation remain replaceable later backends;
- backend IDs remain Aliases;
- concrete implementation may not weaken any frozen Phase 0B identity, lifecycle, migration or proof boundary;
- failure of any condition leaves implementation unauthorized.
