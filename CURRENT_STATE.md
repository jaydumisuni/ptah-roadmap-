# Ptah Current State

**Last updated:** 2026-07-21  
**Overall status:** PHASE 0B FROZEN — PHASE 0C ACTIVE  
**Current phase:** Phase 0C — implementation selection, licensing, repository layout and authorization  
**Active work unit:** 0C-04 / P01 — physical pinned-host proof, package review, durable evidence and ADR-0033 closure  
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

## Corrected AI Project Workspace behavioural donor boundary

Original donor package:

```text
PR #14 merge: d05653c5948727b58ead91088447d0b8ac4d9d9b
```

Neutral-boundary correction:

```text
PR #15 exact head: 5a95c577edf366bad1d8949ee37c17b81f296254
PR #15 merge: 8a8d620c5227a6508145cd4a30f4f45142bfabe9
```

All ten public exact-head workflows passed. Corrected Workspace run `29961370694` retained artifact `8546091277` with digest `sha256:04472fd4fd546fcc2420d135cdfcb517381efbe5de8b3bc14f6971207fbde819`. The private plan correction passed 18 regressions at `b7ab2ccad94f1cefeb4693448c2a2ca79b0b00a7` in run `29962459098`, retained artifact `8546506459` with digest `sha256:ff3e1aef59f0c847964888ef460c6177bdfed181b0a6817318cbc3d2eb9e4ccb`, and merged as `fc8ac4c42a3358da37c4866879543a5d7c4d1885`. Full merge record: `planning/PTAH-NEUTRAL-SUBSTRATE-CORRECTION-MERGE.md`.

Canonical boundary:

- Ptah is the neutral Workspace and execution substrate;
- Hunter owns intelligence, context selection, source judgments, planning and coordination;
- Sergeant independently reviews frozen candidates and issues Sergeant's result;
- humans or calling applications own intent, configured authority, approval, acceptance and release;
- Ptah stores and mechanically enforces configured records but does not select context, rank authority, review, approve, promote or choose a next action.

The donor remains application-experience study only, requires zero Core extensions and does not change ADR-0033, AF03 or runtime authorization.

---

## Accepted Phase 0C-16 Master Plan closure

The complete product/operating plan, dependency-ordered implementation roadmap, WP01–WP14/Phase 0C reconciliation and durable human/AI handoff were validated at exact candidate head:

```text
37d23449fda9a426f56ee8b09042dda91587a6d1
```

Exact-head workflow run: `29842137511`.

Retained artifact: `8499790872` with archive digest `sha256:82d6b452777e2c5e60c4d08bf88dd2c848d6b2570650b70a4eede633c8065d9f`.

Candidate squash merge:

```text
2c24f9e6b0fc98d5e03605596db75d7495796353
```

Accepted-state exact head:

```text
5860b4bfe177aa375fb2fa4305d62dbe3d2141e1
```

Permanent accepted-state workflow run: `29844040274`.

Retained accepted-state artifact: `8500540358` with archive digest `sha256:6f5229fe850d8b6f6f083b09f2c5f53189f3edbf38d4f28b9d2878ab0c78862d`.

Operative authority acceptance merge:

```text
66bd2410d4c777cd3fd3278107f40fe425e875e9
```

ADR-0034 is accepted. `MASTER_PLAN.md` and `IMPLEMENTATION_ROADMAP.md` version `1.0.0` are operative authorities. No new Core entity or current WP01–WP14 reopening was required. This closes planning authority only and does not accept the physical host, packages, retention, ADR-0033 or runtime implementation.

---

## Accepted Phase 0C-17 tenfold archive formation

Operative authority:

```text
ADR-0035: ACCEPTED
protocol: planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md version 1.0.0
campaign: archive/CAMPAIGN-001-FORMATION-MANIFEST.md
candidate merge: c4973cbf4d02a34f14a7aefa85b8e2ea7b392752
operative acceptance merge: 40ca127c6d3054bda785061090acefaefcf4cd42
```

Accepted evidence:

- candidate exact head `58b577b6793ec28de084e6d712c3c1e88bfe2d3a`;
- exact-head run `29853954659`;
- retained artifact `8504497355`;
- artifact digest `sha256:936740e8087e6f7f0a58b3d731117fcb9a4861edfd20c396fb1bb20a7d4f18f4`;
- validation report SHA-256 `de38af1e63a76e02552e4f93ad2bac2d86d05239a77dc92cc27d794a8b9b010f`;
- 21 candidate regression cases and exact-head validation passed;
- exact fifteen-file candidate boundary directly reviewed;
- accepted exact head `b96b84d17cf03e905bd0b1baf3c46b8aec09334a` passed 23 regression cases in run `29855000427`;
- retained accepted artifact `8504901567` with digest `sha256:9d96a1f299060e50ab63132d1bb1da0903d5435f73acdf4fa9e394cdcccf21d2`;
- accepted validation report SHA-256 `21d5338a7049dbc3a3af2e684efa21e19c281c52355007346291c74dfb7a1d3a`;
- operative acceptance merge `40ca127c6d3054bda785061090acefaefcf4cd42`;
- full acceptance record `planning/TENFOLD-ARCHIVE-AUTHORITY-ACCEPTANCE-MERGE.md`.

The operative rule uses minimum twenty privates for two human-equivalent workers, ten primary/verifier record pairs per ordinary formation, and adaptive escalation to 40/60/80–100/up to 120 privates for harder sources. Campaign 001 queues 98 obligations across ten formations and 200 slots.

Campaign 001 progress:

- AF01: ACCEPTED COMPLETE;
- accepted archive records: 9;
- blocked completed outcomes: 1 (`D047` MiniRouter source reuse);
- AF02: ACCEPTED COMPLETE;
- accepted archive records: 19 total;
- AF02 remaining evidence: 0;
- AF02 acceptance merge: d1d6b47e935e79790db319ad234b4abccafa4d3f;
- AF03: READY / NOT STARTED;
- AF03 candidate package: COMPLETE / SERGEANT PASSED / NOT ACCEPTED;
- AF03 candidate outcomes: 10;
- AF03 candidate remaining evidence: 0;
- AF03 Sergeant target: `a6a1d9aa13f619c2f8ff4c1c6c0cadea331df3d6`;
- AF03 mission/result/review: `archive/campaign-001/af03/MISSION.md`, `archive/campaign-001/af03/RESULT.json`, `archive/campaign-001/af03/SERGEANT-REVIEW.md`;
- AF02 mission: `archive/campaign-001/af02/MISSION.md`;
- AF01 operative acceptance merge: `ea2424bb5bc2bdb698bfc1bf389601457abd3c89`;
- AF01 candidate exact head: `f60e340cb856d50e88b4279147a933d838fce759`;
- AF01 workflow run/artifact: `29862087745` / `8507695005`;
- AF01 candidate merge: `0a35a8a904bdf235fa4989ea05b684443d5a879a`;
- AF01 acceptance record: `archive/campaign-001/af01/ACCEPTANCE.md`.

AF02 is accepted complete. AF03 remains ready but not started; its candidate evidence package is complete, Sergeant-reviewed and not accepted. Candidate preparation does not grant source reuse, replace P01 as the active implementation-authorization work, reopen Phase 0A, accept ADR-0033 or authorize runtime implementation.


---

## Accepted Phase 0C-18 diagnostic and efficient-worker boundary

Operative authority:

- `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md` version `1.0.0`;
- ADR-0036: ACCEPTED;
- Phase 0C-18: COMPLETE;
- candidate merge: `fbc4ee80284a2d7ea38a44fdbfa90f0348b875ae`;
- acceptance evidence: `planning/PTAH-DIAGNOSTIC-WORKER-AUTHORITY-ACCEPTANCE.md`.

Allowed diagnostic behavior: detect missing capability, degradation, incompatibility, resource shortage, repeated failure or failed post-condition and emit an evidence-backed advisory asking an authorized caller for an upgrade or inspection.

Allowed execution behavior: after a caller submits a job and selects a Recipe/Plan, apply `max(20, human-equivalent workers × 10)` to run bounded worker Activities, independent checks, checkpoints and configured merge/recovery mechanics.

Accepted evidence: exact head `d2608ba7c619c1c402091edd619a4b29813ee9a7`, run `29986975197`, artifact `8555395796`, digest `sha256:72025fb0aa5a969ea73abe95d7352f7cf14f1c847943955bd768a46d964a4c61`, validation SHA-256 `aff3a635d37b82c15eeb36f2f6cec780f76e2c3ce320727a18053b913b8d9171`.

Forbidden: choose caller work, invent semantic subtasks, reprioritize outside submitted Policy, approve a result, approve/purchase/install an upgrade, mark acknowledgement as resolution, block unrelated capable work or become Hunter/Sergeant authority.

This accepted clarification uses frozen primitives only, does not start AF03 and does not change P01, ADR-0033 or runtime authorization.

---

## Active Phase 0C blockers

Implementation remains unauthorized until all of the following are merged and reviewed:

1. a proof-eligible capability report from the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
2. the exact installed Ubuntu package manifest and package-artifact digests from that pinned host, with reviewer acceptance;
3. generation, durable commit and explicit review acceptance of that physical-host evidence bundle;
4. a Phase 0C closure review proving no frozen contract was weakened;
5. acceptance of ADR-0033;
6. explicit `Runtime implementation: AUTHORIZED` in this file in the same reviewed closure change.

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

1. Install or recover the exact Ubuntu Server 24.04.4 / `6.8.0-136-generic` proof host.
2. Select and record the exact clean reviewed `Ptah-space` preparation commit.
3. Run:

```bash
python3 tools/run_pinned_host_proof.py \
  --repo-root . \
  --output evidence/phase0c/pinned-host-candidate
```

4. Require `proof_eligible: true` with empty host, capability, package-artifact and repository failure sets.
5. Review and accept the exact installed package and package-artifact manifests.
6. From the same exact clean commit, run:

```bash
python3 tools/retain_verified_pinned_host_evidence.py \
  --repo-root . \
  --bundle-dir evidence/phase0c/pinned-host-candidate \
  --output-dir evidence/phase0c/pinned-host-durable-candidate
```

7. Commit and explicitly accept the durable candidate and repository binding.
8. Conduct the final Phase 0C closure consistency review.
9. Accept ADR-0033 and authorize runtime only when every remaining blocker passes.
