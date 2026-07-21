# Ptah Current State

**Last updated:** 2026-07-21  
**Overall status:** PHASE 0B FROZEN — PHASE 0C ACTIVE  
**Current phase:** Phase 0C — implementation selection, licensing, repository layout and authorization  
**Active work unit:** 0C-16 — complete Master Plan, implementation roadmap and durable AI handoff closure  
**Runtime implementation:** NOT AUTHORIZED  
**Production dependency/backend selection:** EXACT RUST, DISTRIBUTED ARTIFACT, PROOF AND RETENTION TOOL LOCKS MERGED — APACHE-2.0 BOUNDARY ACCEPTED — PHYSICAL PINNED-HOST PROOF OPEN  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

## Frozen checkpoints

### Phase 0A donor and requirement closure

Frozen checkpoint:

```text
7d2dffee48f1400ba1cf88823343f09a3895ad33
```

Decision:

- `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`

### Phase 0B contract and proof closure

Phase 0B is frozen by:

- WP01 through WP14 candidate packages;
- exact local schema catalogs and namespaced lifecycle machines;
- directional migration and backend-replacement rules;
- positive, negative and adversarial fixtures;
- the offline WP13 structural and semantic conformance harness;
- the WP14 lawful golden/negative corpus and first vertical-slice proof plan;
- `work-packages/PHASE-0B-FREEZE-READINESS-REVIEW.md`;
- `decisions/ADR-0032-PHASE-0B-FREEZE-PHASE-0C-ENTRY.md`.

Freeze merge:

```text
dc2db457f1705d0cba80f17ab76e5e93f808aee0
```

WP13 and WP14 exact-head workflows passed unit, structural and semantic conformance before merge. Contract changes after this checkpoint require a versioned schema/lifecycle change, migration, fixtures, conformance evidence and a reopening ADR.

---

## Completed Phase 0B packages

1. WP01 — Common identity, versioning and typed families
2. WP02 — Activity, Operation, Attempt, Event, Receipt and proof
3. WP03 — Object, Revision, View, Artifact and storage
4. WP04 — Node, Facility, Provider, capability and health
5. WP05 — Workspace, Session, checkpoint, restore and recovery
6. WP06 — Transfer, synchronization, conflict, backup and restore
7. WP07 — Recipe, Build, provenance, SBOM, signature and verification
8. WP08 — Domain Pack, firmware, disk, filesystem and Device
9. WP09 — Application, Browser, semantic UI and Shell
10. WP10 — Knowledge, Data, Package and Plugin
11. WP11 — Isolation, placement, reservation, Lease and secure grants
12. WP12 — Security, Finding, Claim, Evidence, remediation and reproduction
13. WP13 — executable cross-contract conformance
14. WP14 — golden/negative corpus and proof-plan freeze

These packages define implementation boundaries. They are not evidence that the Ptah runtime already exists.

---

## Phase 0C candidate decisions and evidence now recorded

The following records are merged or awaiting this evidence-sync merge:

- `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md`;
- `work-packages/PHASE-0C-02-HOST-BASELINE-PIN.md`;
- `work-packages/PHASE-0C-03-DIRECT-DEPENDENCY-LICENCE-RECORD.md`;
- `work-packages/PHASE-0C-04-SOURCE-LAYOUT-AND-BOUNDARY-ACCEPTANCE.md`;
- `work-packages/PHASE-0C-05-WP14-IMPLEMENTATION-TASK-AND-PROOF-MAP.md`;
- `work-packages/PHASE-0C-06-CI-EXACT-HEAD-ACCEPTANCE-GATE.md`;
- `work-packages/PHASE-0C-07-REAL-WORKLOAD-CANDIDATE-REGISTRY.md`;
- `work-packages/PHASE-0C-08-NONCLAIMING-SCAFFOLD-EVIDENCE-REVIEW.md`;
- `work-packages/PHASE-0C-09-IMMUTABLE-ACTION-AND-FROZEN-CONFORMANCE-EVIDENCE.md`;
- `work-packages/PHASE-0C-10-FROZEN-CATALOG-AND-GENERATED-BINDING-EVIDENCE.md`;
- `work-packages/PHASE-0C-11-RUNTIME-DEPENDENCY-BACKEND-SIGNER-AND-HOST-COLLECTOR-EVIDENCE.md`;
- `work-packages/PHASE-0C-11-EVIDENCE-MANIFEST.json`;
- `work-packages/PHASE-0C-12-PINNED-HOST-PROOF-INTEGRITY-AND-PACKAGE-ARTIFACT-READINESS.md`;
- `work-packages/PHASE-0C-13-DURABLE-PINNED-HOST-RETENTION-READINESS.md`;
- `work-packages/PHASE-0C-14-APACHE-2.0-OWNER-ACCEPTANCE.md`;
- `work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md`;
- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.

### Candidate first-slice baseline

- Ubuntu Server 24.04.4 LTS amd64 image pinned by SHA-256;
- Noble GA 6.8 generic kernel line;
- Rust `1.97.1` primary Node/control toolchain;
- SQLite `3.53.3` behind a repository-owned ledger boundary;
- native Linux PTY/process supervision;
- containerd `2.3.1` with runc `1.4.2` behind an OCI Provider boundary;
- Node.js `24.18.0`, Playwright `1.60.0` and its pinned Chromium build for the first Browser Provider;
- hardened Git `2.55.0` process adapter;
- libarchive `3.8.7` first decomposition adapter;
- repository-owned resumable transfer and local content-addressed storage;
- Apache License 2.0 accepted for repository-owned public Ptah source, with private THETECHGUY systems, data, restricted adapters and trademarks excluded.

Concrete tools remain replaceable backends. They may not redefine canonical Ptah identity, lifecycle or proof. Backend IDs remain Aliases.

---

## Merged non-claiming implementation scaffold

The initial scaffold merged at:

```text
ff26fa93d1b60781b49f33f5d1758680e1282d5f
```

Evidence hardening merged at:

```text
23fc97ff0acd2b219990411ec4fb84d8a8c0a567
```

Exact head `900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc` passed workflow run `29717942201` for source policy, Rust, Browser and frozen WP13 conformance under immutable Action pins.

The scaffold contains package boundaries, locks and CI only. It is not a Ptah runtime.

---

## Merged frozen catalog and generated binding closure

`Ptah-space` PR `#5` was tested at exact head:

```text
33043eaadb0f074d8867cb8ce999f16ea4c06a8b
```

and merged at:

```text
f45c96e3f667b463042b6a8b714066236fde703d
```

The accepted lock state is:

```text
frozen_catalogs_and_bindings_locked_runtime_dependencies_open
```

The lock records:

- fourteen frozen catalog paths, URNs and original-byte digests;
- catalog-set SHA-256 `f0668a5f5d5c68cabf623176608c627a94482faa4f4460e4f0fe0f0969d7c64d`;
- final binding generator version `0.3.0`;
- manifest SHA-256 `63fd0cb0fd4ef172271aa7a114e74bb24c0a9e70cc247faeff1db95f7a67d97d`;
- catalog-index SHA-256 `0f97e222d9baf9f90721d2a30dd2b31920b53489ae343b0430cc9089c8fdaf9c`;
- Rust-module SHA-256 `748e87f1a8cf2ed20d694aa716dd8f18b7ea4b3016372386202aeeaff687ae50`;
- output-tree SHA-256 `8f3355e0eac19715ea34e06ea227a826ac727d2e5b9ebf231a672927350c8db2`;
- fourteen catalogs, 346 canonical schemas and 99 lifecycle machines.

Exact-head workflow runs passed:

- catalog lock: `29727701958`;
- independent generated bindings: `29727701960`;
- source policy, Rust, Browser and frozen WP13 conformance: `29727701999`.

The generated crate provides metadata and lookup bindings only. It does not implement or authorize runtime behavior.

---

## Merged runtime dependency, backend signer and host-collector evidence

`Ptah-space` PR `#6` was tested at exact head:

```text
bc12885ce41844b05481628543219c3a8d3574ba
```

and squash-merged at:

```text
c2cd803b5e5c50787b3d8c2d24392d693afdbb3c
```

The accepted evidence records:

- ten exact direct Rust dependencies, 99 resolved packages, 81 crates.io packages and zero Git dependencies;
- final `Cargo.lock` SHA-256 `d68a06272d417d67049c7879570e3735607166ce1e7eff58e43df21e20c9117a`;
- passing cargo-deny advisory, ban, licence and source policy;
- nine authoritative distributed/source backend artifact identities and digests;
- Playwright `1.60.0` Chromium `148.0.7778.96`, revision `1223`, installed-tree SHA-256 `953a2e9c1fb18d1e698f0903a62c23c835264e939cdd08a85c41d57719a5de7a`;
- pinned and verified signing authorities for Node.js, runc, Git and libarchive;
- a fail-closed collector for all eighteen required host capabilities and conditional AppArmor evidence;
- realistic Ubuntu base/point-release, architecture and frozen-kernel matching;
- exact-head dependency, backend, signer, host, source, Rust, Browser, contract, binding and WP13 evidence.

All eight final workflows passed at the exact candidate head. The backend-signature lane retained a first-attempt upstream HTTP `504` as negative evidence; the unchanged lock and successful retry completed all four cryptographic checks.

The hosted collector report validates required capability observation but remains non-proof because generic runner identity does not match the frozen `6.8.0-136-generic` host. No evidence record authorizes runtime implementation.

---

## Merged pinned-host proof integrity and package-artifact readiness

The proof-integrity repair was tested in `Ptah-space` PR `#9` at exact head:

```text
4e871b2bad8c4054ef1e9a1245219fa231338458
```

and squash-merged at:

```text
b97c2defbba17d75e32cb0a02cda9bbb2b1c6649
```

The exact installed-package artifact evidence gate was tested in PR `#10` at exact head:

```text
74aef4b6a4ddebb7f2491fc0eb127d945ac05a14
```

and squash-merged at:

```text
50969c414b55460b6ff7a7d12fd7ae88f5ef5c0a
```

The merged tooling now:

- accepts only the canonical `host/scripts/collect_capabilities.py` collector;
- requires the capability report itself to pass before bundle eligibility;
- proves clean unchanged Git state before and after collection while excluding only the fresh evidence output directory;
- hashes retained hostname, machine ID and boot ID values;
- records exact installed `dpkg` package/version/architecture identities;
- resolves exact local APT binary-artifact `Filename`, `Size` and SHA-256 metadata in bounded batches;
- fails closed on malformed identities, missing or conflicting digests, absent APT release/package index evidence, capability failures or repository changes;
- emits `package-artifacts.json` and a `bundle-manifest.json` schema `0.3.0` with combined eligibility failures;
- keeps `network_used: false` and `runtime_implementation_authorized: false` in the relevant records.

All eight workflows passed at both exact heads. The final host workflow run `29811724538` checked out `74aef4b6a4ddebb7f2491fc0eb127d945ac05a14` and passed host, package-artifact and pinned-proof regression coverage.

This closes proof-tool readiness only. No physical-host bundle has yet been produced or accepted.

---

## Merged durable pinned-host retention readiness

`Ptah-space` PR `#11` was tested at exact head:

```text
f0c1aafb58b33fcc8338081244996ced9260ce5c
```

and squash-merged at:

```text
49f6035a93bf704d775dc437e8a8b25c95145ae1
```

The merged retention tooling now:

- independently re-verifies the exact six-file physical-host source bundle before retention;
- recomputes every file and aggregate digest plus host, capability, package, package-artifact, APT-index and APT-source proof conditions;
- binds the candidate to current clean exact `HEAD`, canonical collector bytes and the reviewed proof-runner digest;
- rejects malformed or authorizing records, wrong commits, collector mismatches, unexpected repository changes, symlinks, nested paths and overwrite attempts;
- preserves exact source bytes in a durable base64 bundle;
- emits a separate repository binding;
- emits a review record with `review_status: pending` and every host, package, retention, ADR and runtime acceptance field `false`;
- verifies the exact final four-file durable output and rechecks repository state after retention.

All eight workflows passed at exact head `f0c1aafb58b33fcc8338081244996ced9260ce5c`. Host workflow run `29813401728` passed the host collector, identity finalizer, package-artifact, pinned-host proof, independent retention and exact-repository-binding regression suites.

This closes durable-retention tooling readiness only. No real physical-host source bundle or durable candidate has been generated, committed or accepted.

---

## Merged Apache-2.0 public/private boundary acceptance

The non-operative boundary candidate was tested in `Ptah-space` PR `#12` at exact head:

```text
2a54093d0a7856d7b98c77ebaa78899e1626257b
```

and squash-merged at:

```text
bf846574df65061bd99d9c0e3d22a401bf9f27e2
```

The owner-acceptance change was then tested in PR `#13` at exact head:

```text
a47d418243af076b49367c4c4eccc8ef2090894c
```

and squash-merged at:

```text
3ce7d4251db0b6ba3f145385ad7ad8dc09276393
```

The accepted boundary records:

- rights holder `John Dumisuni trading as THETECHGUY DIGITAL SOLUTIONS`;
- exact official Apache License 2.0 bytes at root `LICENSE` and `LICENSES/Apache-2.0.txt`;
- licence size `11358` bytes and SHA-256 `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`;
- operative `NOTICE`, `CONTRIBUTING.md`, `SECURITY.md` and repository-wide `REUSE.toml` annotations;
- explicit private-system, customer/device/payment, restricted-adapter, donor-source and trademark exclusions;
- a reviewed third-party NOTICE boundary and mandatory re-review triggers;
- historical candidate records preserved as non-operative evidence;
- `runtime_implementation_authorized: false` in the accepted machine record and exact-head evidence.

All nine exact-head workflows passed at the acceptance head, including the new licence-acceptance lane, Rust dependency/licence policy, source/no-build, host, backend, signer, frozen-contract and generated-binding gates.

This closes the Apache-2.0 owner decision and operative public repository governance files only. It does not close the physical-host, package, durable-retention, ADR or runtime-authorization gates.

---

## Merged AI Project Workspace behavioural donor and Hunter bridge candidate

`Ptah-space` PR `#14` was tested at exact head:

```text
2a2c28d17abd9ad52c8d850f8bbcdba57074194e
```

and squash-merged at:

```text
d05653c5948727b58ead91088447d0b8ac4d9d9b
```

The merged non-operative design package records:

- OpenAI ChatGPT Projects and Work as a public-documentation behavioural donor only;
- no OpenAI source-code reuse, proprietary implementation claim or runtime dependency;
- profile identity `ptah.workspace.ai_project.v1`;
- sixteen existing Ptah primitives composed into a human-and-agent project Workspace;
- fourteen donor behaviours: four directly covered, eight covered by profile composition, zero Core extensions and two rejected patterns;
- explicit rejection of hidden provider memory and implicit global tool access;
- a Hunter–Ptah bridge where Ptah owns durable truth and Grants while Hunter coordinates through bounded context packets;
- ten positive/negative proof fixtures for isolation, authority, provider replacement, scheduled access, handoff and Artifact lineage;
- ten fail-closed regressions and exact-head evidence under immutable Action pins;
- a corrected public README licence statement while retaining the non-claiming runtime boundary.

All ten exact-head workflows passed, including the new AI Project Workspace candidate lane, source/no-build, Rust policy, frozen contracts, generated bindings, host, licence, backend artifact, backend signature and signer-lock gates.

This candidate is a non-blocking future composition design. It neither closes nor adds an ADR-0033 acceptance condition, changes a frozen WP01–WP14 contract, implements a Workspace/context runtime or authorizes Hunter integration.

---

## Active Phase 0C-16 Master Plan closure

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

## Active Phase 0C blockers

Implementation remains unauthorized until all of the following are merged and reviewed:

1. acceptance of the complete Master Plan, detailed implementation roadmap, reconciliation and durable handoff through Phase 0C-16 / ADR-0034;
2. a proof-eligible capability report from the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
3. the exact installed Ubuntu package manifest and package-artifact digests from that pinned host, with reviewer acceptance;
4. generation, durable commit and explicit review acceptance of that physical-host evidence bundle;
5. a Phase 0C closure review proving no frozen contract was weakened;
6. acceptance of ADR-0033;
7. explicit `Runtime implementation: AUTHORIZED` in this file in the same reviewed closure change.

The frozen catalog, generated binding, exact Rust dependency graph, Cargo lock, cargo-deny policy, distributed backend artifact lock, Browser binary tree, signer lock, cryptographic signature, source-policy, Rust, Browser, host-collector, pinned-host proof-tool, package-artifact, durable-retention, Apache-2.0 governance and frozen-WP13 lanes are complete. They do not close the physical pinned-host result, package acceptance, actual retained-bundle acceptance or any WP14 runtime proof.

### Required first vertical slice after authorization

The first authorized slice must demonstrate, at minimum:

- one Linux Node;
- one persistent Workspace;
- canonical Object registration;
- concurrent Activities and multiple terminals;
- upload and resumable download;
- Git clone or mirror;
- one container execution path;
- one interactive Browser path;
- one decomposition adapter;
- Artifact registration;
- checkpoint, restart and reconnect;
- exact Receipts, generation evidence and negative-path retention.

---

## No-build boundary

Allowed during the remainder of Phase 0C:

- accepted licence, contribution, security and third-party-notice boundary maintenance;
- non-operative behavioural donor, Workspace-profile and Hunter-bridge maintenance;
- exact physical pinned-host and installed-package evidence;
- durable proof-location preparation and pending retention review;
- non-claiming repository and CI maintenance;
- executable proof-plan preparation;
- WP13 integration and contract-conformance maintenance;
- Phase 0C closure review.

Not yet allowed:

- claiming the Ptah runtime or UI is implemented;
- deploying production Nodes, Providers or Workspaces;
- adding runtime functionality under the name of scaffolding;
- weakening the frozen WP14 proof burden;
- bypassing WP13 conformance;
- reusing donor source outside its accepted licence and extraction boundary;
- authorizing implementation without the accepted ADR and exact evidence.

Implementation becomes authorized only when a Phase 0C acceptance ADR and an explicit `Runtime implementation: AUTHORIZED` entry are merged into this file.

---

## Immediate continuation order

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
