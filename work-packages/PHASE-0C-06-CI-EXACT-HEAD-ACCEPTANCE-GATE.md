# Phase 0C-06 — CI and exact-head implementation acceptance gate

Status: candidate — runtime implementation remains unauthorized

## Purpose

Define the minimum CI and evidence chain required before ADR-0033 may authorize implementation and before any later implementation commit may claim first-slice acceptance.

## Workflow separation

CI must use separate jobs and reports for:

1. source and dependency integrity;
2. generated-contract integrity;
3. Rust quality and unit tests;
4. Browser Provider quality and tests;
5. WP13 roadmap conformance;
6. first-slice structural fixtures;
7. first-slice semantic/negative fixtures;
8. host capability validation where a Linux runner supports it;
9. immutable evidence packaging.

A later job may not run when a prerequisite gate fails, but failure reports from completed jobs must still be retained.

## Pre-authorization CI

The implementation repository may add the following scaffolding before runtime authorization:

- `cargo fmt --check`;
- `cargo clippy --workspace --all-targets --all-features -- -D warnings`;
- `cargo test --workspace --locked`;
- `cargo deny check` or an equivalent exact licence/advisory/source policy;
- `npm ci` against an exact lock file;
- Browser Provider lint/type/unit tests;
- generated binding reproducibility checks;
- upstream contract-lock verification;
- WP13 offline structural and semantic conformance;
- secret scanning and public/private packaging checks.

These checks prove only scaffolding integrity until runtime implementation is authorized.

## Exact-head rule

Every acceptance report must contain:

- repository and exact commit SHA;
- dirty-tree state;
- workflow definition digest;
- host image revision and capability-report digest;
- Rust, Node, dependency and browser lock digests;
- upstream roadmap freeze commit and catalog-lock digest;
- test-plan revision;
- start/end timestamps;
- result and limitation summary;
- report and Artifact digests.

Reports produced for another commit cannot authorize the current commit.

## Contract generation gate

CI must:

1. obtain frozen public catalogs from the exact locked roadmap revision or a digest-equivalent vendored source;
2. resolve all schema references offline;
3. regenerate bindings into a clean temporary tree;
4. compare generated output byte-for-byte with committed output;
5. fail on missing, changed or unexpected generated files;
6. emit a generation report with input/output digests.

No runtime package may fetch schemas dynamically from the internet.

## Dependency integrity gate

CI must verify:

- `Cargo.lock` and `package-lock.json` are present and unchanged by locked builds;
- direct binary/source archives match authoritative hashes/signatures;
- each direct and transitive dependency appears in the generated inventory;
- licence policy passes or has an explicit reviewed exception;
- denied sources, git branches and unpinned URLs are absent;
- known advisory results are retained even when risk is accepted;
- browser executable version/digest matches the Playwright lock.

## Runtime proof gate

After authorization, each implementation task from `PHASE-0C-05-WP14-IMPLEMENTATION-TASK-AND-PROOF-MAP.md` must have a stable case ID and report. The acceptance workflow must execute at least:

- Node restart/generation proof;
- ten concurrent Activity proof;
- independent multi-terminal proof;
- Workspace detach/reconnect proof;
- interrupted upload/download resume proof;
- hardened Git clone/mirror proof;
- OCI container proof;
- persistent Browser proof;
- archive decomposition proof;
- Artifact digest/provenance proof;
- checkpoint/restart/recovery proof;
- backend-replacement simulation;
- offline operation proof;
- all mandatory negative cases.

## Host-sensitive jobs

GitHub-hosted runners may prove source and many functional behaviours but are not automatically authoritative for the final Node image. Host-sensitive acceptance must run on the pinned Ptah proof image or an attested equivalent and must record:

- kernel and boot ID;
- cgroup and namespace capabilities;
- AppArmor/seccomp state;
- container runtime versions;
- filesystem and mount options;
- virtualization availability when used;
- runner identity and isolation limitations.

## Immutable evidence bundle

The final job must package without rewriting:

```text
acceptance/
  manifest.json
  host-capabilities.json
  dependency-inventory.json
  licence-report.json
  contract-generation-report.json
  wp13-report.json
  wp14-vertical-slice-report.json
  receipts/
  events/
  artifacts/
  limitations.json
  SHA256SUMS
```

`manifest.json` must bind every file by digest and the exact implementation commit. The bundle must be uploaded even on failure when safe to do so.

## Failure rules

Acceptance must fail when:

- a required report is missing;
- the workflow is green but evidence packaging failed;
- a negative case unexpectedly succeeds;
- failure evidence was deleted or redacted beyond usefulness;
- raw secrets enter logs or Artifacts;
- a stale generation/fence is accepted;
- backend acknowledgement is presented as verified success;
- the report references another commit;
- schemas were resolved over the network;
- an unreviewed dependency or licence appears.

## Branch protection candidate

Before runtime authorization, `Ptah-space/main` should require:

- pull requests for implementation changes;
- exact-head CI success;
- no force-push to protected main;
- signed or GitHub-verified commits where practical;
- review for dependency, licence, contract-lock and security-policy changes;
- retained workflow artifacts for the configured evidence period.

## Authorization blocker closed by this record

This record defines the required CI shape. The blocker remains open until the workflows exist in `Ptah-space`, execute successfully against the selected locks, and emit the required immutable reports.