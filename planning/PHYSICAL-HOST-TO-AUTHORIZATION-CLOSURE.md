# Ptah physical-host to authorization closure

Status: exact closure procedure recorded — P01 active and blocked on access to the physical proof host

Recorded: 2026-07-25

## Purpose

Define the exact remaining sequence from the current accepted planning state through physical-host proof, durable evidence acceptance, ADR-0033 acceptance and runtime implementation authorization.

This document prevents a future chat or AI from treating donor completion, plan completion, CI success or owner intent alone as authorization.

## Current prerequisite state

Complete and operative:

- Phase 0A donor and requirement closure frozen;
- WP01–WP14 contracts frozen;
- Archive Campaign 001 accepted complete;
- Phase 0C host, dependency, backend, signer, source-layout and proof-tool selections recorded;
- Apache-2.0 public/private boundary accepted;
- pinned-host proof and durable-retention tooling merged and regression-tested;
- AI Project Workspace donor/profile recorded;
- deep Workspace operations study merged in `Ptah-space`;
- Phase 0C-19 complete and ADR-0037 accepted;
- Master Plan version `1.1.0` accepted and operative;
- implementation roadmap version `1.1.0` accepted and operative;
- accepted planning authority and exact-head evidence durably bound through merge `d73a3c706e1c6cf326e67eb4e2f4247afbe0f69d`;
- current first-read handoff authority corrected through merge `15cb887f6fc47ff783e5700613cdf5ee40d0116e`;
- exact non-runtime `Ptah-space` proof candidate confirmed as `23dc4b19a0189ba55e08dfa124761efa806bd68b`.

Open:

- execution on the exact physical Ubuntu host;
- package and package-artifact acceptance;
- durable host-bundle acceptance;
- final Phase 0C consistency review;
- ADR-0033 acceptance;
- explicit runtime authorization.

## Required proof host

The machine must report:

Exact target tuple: Ubuntu Server 24.04.4 LTS | x86_64 | 6.8.0-136-generic

- Ubuntu Server `24.04.4 LTS`;
- `/etc/os-release` with `ID=ubuntu` and base `VERSION_ID=24.04`;
- architecture `x86_64`;
- kernel `6.8.0-136-generic`;
- every required capability in `Ptah-space/host/capability-profile.json`;
- exact installed `dpkg` package/version/architecture inventory;
- exact local APT binary-artifact SHA-256 metadata and source-index inventory;
- one exact clean reviewed `Ptah-space` commit before and after collection and retention.

A generic CI runner, different point release, cloud-specific kernel, dirty checkout, incomplete local APT metadata or package without exact artifact metadata is diagnostic only and cannot close the gate.

## Step 1 — planning closure package accepted

The planning closure package is complete and accepted. The operative authority includes:

- `planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md`;
- `MASTER_PLAN.md` version `1.1.0`;
- `IMPLEMENTATION_ROADMAP.md` version `1.1.0`;
- `planning/MASTER-PLAN-RECONCILIATION.md`;
- `planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md`;
- `planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md`;
- `planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-OPERATIVE-BINDING.md`;
- this closure record;
- `AI_HANDOFF.md`;
- `master-plan-index.json`;
- permanent exact-head validators and adversarial regressions.

The accepted planning closure confirms:

- the product plan is complete enough to derive implementation;
- every roadmap package maps to frozen contracts or an explicit parked/reopening rule;
- the first vertical-slice task order is preserved;
- no runtime implementation is claimed or authorized by the planning merges.

## Step 1A — complete planning load accepted

Phase 0C-19 and ADR-0037 are accepted and Master Plan/roadmap version `1.1.0` are operative. Roadmap PR #46's selected commit was re-reviewed after reconciliation and confirmed as the exact physical-proof candidate:

```text
23dc4b19a0189ba55e08dfa124761efa806bd68b
```

This completion does not itself produce or accept physical-host evidence and does not authorize runtime implementation.

## Step 2 — confirmed exact implementation-preparation commit

The exact clean `Ptah-space` commit selected for physical proof is:

```text
23dc4b19a0189ba55e08dfa124761efa806bd68b
```

Before collection:

1. clone or check out that exact commit on the physical proof host;
2. confirm `git rev-parse HEAD` equals the selected commit;
3. confirm `git status --porcelain` is empty;
4. remove any previous proof output directories;
5. do not modify, rebase or replace the selected checkout during collection or retention.

A different commit may replace it only through a separate reviewed superseding selection that updates the planning authority before collection begins. No such superseding selection currently exists.

## Step 3 — collect the pinned-host candidate

From the exact clean `Ptah-space` repository root:

```bash
python3 tools/run_pinned_host_proof.py \
  --repo-root . \
  --output evidence/phase0c/pinned-host-candidate
```

The command may exit non-zero while still producing diagnostics. Non-zero or generated files do not imply proof eligibility.

Expected source records:

- `host-identity.json`;
- `host-capabilities.json`;
- `installed-packages.json`;
- `package-artifacts.json`;
- `apt-sources.json`;
- `bundle-manifest.json`.

Every record must retain `runtime_implementation_authorized: false`.

## Step 4 — require proof eligibility

Before retention, confirm:

- `bundle-manifest.json` reports `proof_eligible: true`;
- `eligibility_failures` is empty;
- `host_identity_failures` is empty;
- `capability_failures` is empty;
- `package_artifact_failures` is empty;
- the host-capability report independently reports its own proof-eligible state;
- every installed package has one exact artifact record;
- local APT index inventory is present;
- pre/post repository state is clean and the exact `HEAD` did not change.

If any condition fails:

- preserve the result as diagnostic evidence;
- do not alter expected values merely to make the machine pass;
- correct the machine/package state or choose a newly reviewed host revision through an explicit decision;
- rerun from a clean output directory.

## Step 5 — review installed packages and artifact boundary

The owner/reviewer must inspect:

- every package name, version and architecture;
- whether each package is required, acceptable or unexpected for the first proof Node;
- exact APT artifact SHA-256 records;
- missing/conflicting metadata;
- active APT sources;
- local package-index digests;
- licence/security implications where material.

The review must not accept a manifest simply because the collector completed.

Outcomes:

- `accepted` — package boundary is suitable;
- `changes_required` — change host packages through a reviewed update and recollect;
- `rejected` — the selected host revision cannot close ADR-0033.

## Step 6 — prepare independently verified durable retention

From the same exact clean checkout:

```bash
python3 tools/retain_verified_pinned_host_evidence.py \
  --repo-root . \
  --bundle-dir evidence/phase0c/pinned-host-candidate \
  --output-dir evidence/phase0c/pinned-host-durable-candidate
```

Expected durable records:

- `durable-pinned-host-bundle.json`;
- `pinned-host-review-record.json`;
- `repository-binding.json`;
- `README.md`.

The review record must begin as pending with all acceptance fields false.

## Step 7 — commit the durable candidate

Commit the verified durable candidate to the accepted durable evidence location without changing the selected implementation-preparation commit during collection or retention.

Record:

- source bundle aggregate digest;
- durable bundle digest;
- repository-binding digest;
- selected implementation-preparation commit;
- collector and proof-runner digests;
- exact durable evidence commit and repository path.

Durable storage does not equal acceptance.

## Step 8 — explicitly accept the physical evidence

A reviewed change must update `pinned-host-review-record.json` or the accepted equivalent to record:

- physical host identity accepted;
- required capabilities accepted;
- installed package manifest accepted;
- package-artifact manifest accepted;
- APT sources/index inventory accepted;
- durable retention accepted;
- exact repository binding accepted;
- reviewer identity and date;
- `runtime_implementation_authorized: false` until the final closure merge.

## Step 9 — complete the Phase 0C closure consistency review

Review together:

- accepted Master Plan and implementation roadmap version `1.1.0`;
- frozen WP01–WP14 contracts and conformance;
- Archive Campaign 001 and Phase 0C-01 through Phase 0C-19 records;
- exact dependencies, binaries, signers and host packages;
- physical-host source and durable bundles;
- public/private and licence boundaries;
- first-slice implementation/proof map;
- current `Ptah-space` scaffold.

Require evidence that:

- no frozen identity, lifecycle, migration, privacy or proof rule was weakened;
- no runtime feature was hidden inside preparation work;
- the selected host and dependencies match the recorded plan;
- every remaining blocker is closed by exact evidence;
- the first runtime package is Programme A / A01 and no later phase is silently activated.

## Step 10 — accept ADR-0033

Change ADR-0033 from proposed to accepted only when Steps 1–9 pass.

The accepted ADR must bind:

- Master Plan and implementation roadmap versions/commits;
- exact physical host and kernel;
- installed package and package-artifact evidence;
- durable evidence bundle and repository binding;
- public licence and source layout;
- exact first Provider selections;
- first-slice task/proof map;
- limitations and reopening rules.

## Step 11 — authorize runtime implementation

In the same reviewed closure change that accepts ADR-0033:

- change `CURRENT_STATE.md` to `Runtime implementation: AUTHORIZED`;
- select `A01 — Repository, contracts and reproducible scaffold` as the first authorized runtime work package;
- update `PROGRESS.md` to show P00 and P01 complete and A01 ready;
- update `AI_HANDOFF.md` with the exact authorized branch/commit and next action;
- update `master-plan-index.json` with authorization state and evidence bindings.

Do not authorize all Programmes A–F as simultaneous active work. Authorization permits the dependency-ordered roadmap; `CURRENT_STATE.md` selects one exact active package at a time.

## Fail-closed rule

If the actual host is unavailable, the package manifest is not accepted, retention is not independently verified, the closure review finds a contract conflict, or ADR-0033 remains proposed:

```text
Runtime implementation: NOT AUTHORIZED
```

Owner intent cannot replace missing evidence because the accepted engineering process explicitly requires both owner decision and exact proof.

## Current next action

Run the proof kit on the exact physical Ubuntu host from clean confirmed `Ptah-space` commit:

```text
23dc4b19a0189ba55e08dfa124761efa806bd68b
```
