# Phase 0C-12 — Pinned-host proof kit readiness

Status: implementation tooling complete — physical host proof still open

## Implementation evidence

Repository: `jaydumisuni/Ptah-space`

Merged pull request: `#8`

Exact tested head:

`69cb7eaec4b489b8019e6af89ff2f6da7b5465d0`

Merge commit:

`0353210ed5269a8b79baef3251873e4b66fa9642`

All eight existing exact-head workflows passed before merge:

- frozen catalog lock;
- deterministic generated bindings;
- source-policy/no-build boundary;
- Rust dependency policy;
- Browser scaffold;
- backend artifact evidence;
- backend signature evidence;
- host capability evidence.

## Added proof package

The merged implementation adds:

- `tools/run_pinned_host_proof.py`;
- `tools/test_run_pinned_host_proof.py`;
- `host/PINNED-HOST-PROOF-RUNBOOK.md`.

The runner is fail-closed and emits:

- exact Ubuntu point-release, architecture and kernel identity;
- privacy-preserving machine and boot identity;
- the existing Ptah host-capability report;
- exact installed `dpkg` package/version/architecture inventory;
- active APT sources;
- per-file SHA-256 records;
- aggregate bundle digest;
- exact clean implementation commit;
- explicit proof eligibility.

Every produced record retains:

`runtime_implementation_authorized: false`

## Proof target

The real Phase 0C host blocker can close only from a clean checkout on:

- Ubuntu Server `24.04.4 LTS`;
- `x86_64`;
- kernel `6.8.0-136-generic`;
- all required capabilities passing;
- the exact reviewed Ptah-space candidate commit;
- reviewed installed-package and APT-source evidence;
- durable retention of the produced bundle.

Generic GitHub-hosted runners remain diagnostic-only and cannot become host proof.

## Remaining ADR-0033 blockers

1. run the merged proof kit on the exact frozen host;
2. review and accept the installed package manifest;
3. retain the pinned-host bundle in a durable evidence Location;
4. accept the public Apache-2.0/private THETECHGUY boundary;
5. complete the Phase 0C closure consistency review;
6. accept ADR-0033 and explicitly authorize runtime implementation in the same reviewed change.

This record does not accept ADR-0033 and does not authorize runtime implementation.