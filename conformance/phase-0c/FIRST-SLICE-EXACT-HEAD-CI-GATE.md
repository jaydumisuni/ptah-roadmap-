# Phase 0C — First-slice exact-head CI acceptance gate

Status: candidate CI contract — runtime implementation remains unauthorized

## Purpose

Define the CI evidence required before ADR-0033 can authorize implementation and before any first-slice commit can be accepted. The workflow is evidence-producing infrastructure, not proof merely because a green checkmark appears.

## Frozen contract source

The implementation repository must consume the frozen Phase 0B contract source from:

- repository: `jaydumisuni/ptah-roadmap-`
- frozen governance checkpoint: `dc2db457f1705d0cba80f17ab76e5e93f808aee0`
- WP14 package merge: `fef387c4f074af7fcf86f2d99f7f9b7637e91f88`

The governance checkpoint is the default contract input. Any later contract revision requires an accepted reopening/versioning ADR, migrations, fixtures and new conformance evidence.

The CI job may clone the pinned checkpoint during an online setup job, but all schema resolution and conformance execution must use the checked-out local files. The offline proof job must run with network access denied or demonstrably unused.

## Workflow jobs

## 1. `source-policy`

Required checks:

- repository contains no committed secrets or private THETECHGUY material;
- generated files declare their source catalog and generator version;
- public implementation source does not embed donor code without an accepted licence/extraction record;
- no file claims the Ptah runtime is complete before acceptance;
- no backend ID is used as a canonical identity field in test fixtures or public APIs.

Required artifact:

- `source-policy-report.json`.

## 2. `rust-toolchain`

Pinned toolchain:

- Rust `1.97.1` stable.

Required checks once scaffold exists:

- `cargo fmt --all -- --check`;
- `cargo clippy --workspace --all-targets --all-features -- -D warnings`;
- `cargo test --workspace --all-features`;
- `cargo test --workspace --doc`;
- `cargo metadata --locked --format-version 1`;
- lockfile must not change during CI;
- every package is `publish = false` until the public licence is accepted;
- unsafe code is denied by default and every exception requires a reviewed, crate-local safety record.

Required artifacts:

- Cargo metadata;
- test report;
- clippy/fmt result;
- exact Rust/Cargo versions;
- source commit.

## 3. `dependency-policy`

Required checks:

- direct and transitive dependency versions match the committed lockfiles;
- licences are accepted by an explicit allow-list;
- advisories and yanked packages are reported;
- unknown, unlicensed or git-branch dependencies fail;
- git dependencies, if exceptionally approved, must pin an exact commit;
- external binaries record version and digest;
- Node package lock is immutable;
- Playwright browser revision is exact;
- Ubuntu package inventory is retained from the proof Node.

Suggested tools may include `cargo-deny`, `cargo-audit`, `npm ci` and SPDX/SBOM generation, but their own versions must be pinned before they become acceptance dependencies.

Required artifacts:

- dependency inventory;
- licence report;
- advisory report;
- SBOM candidate;
- external-binary digest inventory.

## 4. `phase-0b-conformance`

Run the frozen WP13 harness against the locally checked-out roadmap checkpoint.

Equivalent required commands:

```text
python -m pip install ./conformance/harness
python -m unittest -v conformance/harness/test_ptah_conformance.py
ptah-conformance --root . --report conformance/reports/phase-0b-conformance.json
python conformance/harness/semantic_fixture_runner.py --root . --report conformance/reports/phase-0b-semantic.json
```

The exact invocation may be wrapped by the implementation repository, but the reports must remain semantically equivalent and contain the frozen checkpoint identity.

Required artifacts:

- `phase-0b-conformance.json`;
- `phase-0b-semantic.json`;
- harness version and source commit.

## 5. `implementation-unit-and-integration`

Required checks grow with the accepted task graph:

- identifier and contract binding tests;
- ledger transaction/migration/crash tests;
- Activity concurrency, cancellation and retry tests;
- PTY and Workspace detach/reconnect tests;
- CAS and Artifact digest tests;
- resumable transfer tests;
- hardened Git policy tests;
- container adapter tests;
- Browser generation/stale-target tests;
- decomposition budget/traversal tests;
- checkpoint/recovery tests.

Every failing test must still upload logs and partial reports.

## 6. `wp14-positive-proof`

Execute `P01` through `P15` from `PHASE-0C-03-FIRST-SLICE-TASK-GRAPH-TO-WP14-PROOFS.md`.

Each proof record must include:

- proof ID;
- exact implementation commit;
- host/Node generation;
- Provider generations;
- Activity/Operation/Attempt IDs;
- input Object/Revision/Content IDs;
- output Artifact IDs and digests;
- expected result;
- actual result;
- Receipt/Verification IDs;
- retained log/report Locations.

Required artifact:

- `wp14-positive-proof-report.json` plus referenced evidence bundle.

## 7. `wp14-negative-proof`

Execute every mandatory `N01` through `N12` case.

Rules:

- a negative proof passes only when the prohibited transition/result is rejected for the expected reason;
- process crash or test timeout is not an accepted rejection unless the case explicitly tests that uncertainty path;
- failure codes must be stable and typed;
- retained failed/inconclusive evidence is mandatory;
- a case cannot be skipped because the backend makes it inconvenient.

Required artifact:

- `wp14-negative-proof-report.json` plus referenced evidence bundle.

## 8. `offline-proof`

Run an accepted subset of the first slice with outbound network disabled.

Must prove:

- schema/catalog resolution is local;
- Node, ledger, Workspace, Activity, terminal, Object/CAS and decomposition paths start without network dependency;
- pre-cached container/browser dependencies are identified as local Artifacts and not silently downloaded;
- attempts to resolve schemas or required binaries from the network fail the job;
- reports remain complete.

Required artifact:

- `offline-proof-report.json`.

## 9. `proof-bundle`

This final job runs only after every required job completes, but it must also run in failure mode to bundle partial evidence.

Bundle contents:

- exact commit and tree identity;
- workflow/run identity;
- host image and Node generation evidence;
- dependency, licence and SBOM reports;
- structural and semantic conformance reports;
- unit/integration reports;
- WP14 positive and negative proof reports;
- offline report;
- logs and known limitations;
- bundle manifest with SHA-256 for every file.

A later signing step may sign the manifest, but unsigned evidence must never be described as signed.

## Pull-request gate

Before merge to the protected implementation branch:

- every mandatory job succeeds;
- every expected artifact exists;
- the proof-bundle manifest verifies;
- the workflow ran against the PR head, not an earlier commit;
- dependency lockfiles are unchanged after the run;
- no required case is skipped;
- human review accepts the reports.

## Failure handling

- artifacts upload with `if: always()` semantics;
- a failed job cannot delete prior failure evidence;
- rerun Attempts get new identities;
- successful rerun does not overwrite the previous failed report;
- infrastructure failure remains distinct from product failure;
- flaky classification requires retained repeated Attempts and explicit review.

## GitHub Actions supply-chain pinning

Before implementation authorization, workflow actions must be pinned to immutable commit SHAs rather than floating major tags. The accepted action commit, upstream repository and licence must be recorded in the dependency inventory.

The initial roadmap workflow currently demonstrates the required structure with `actions/checkout`, `actions/setup-python` and `actions/upload-artifact`; the implementation workflow must convert these to reviewed immutable pins.

## CI authorization condition

ADR-0033 condition 5 is closed only when this design is implemented in `jaydumisuni/Ptah-space`, runs on the exact scaffold commit and uploads verifiable reports. This document alone does not close that condition.