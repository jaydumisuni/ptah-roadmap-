# Internal Recovery Record — Sergeant

**Phase:** 0A / WP02C  
**Status:** FIRST-PASS COMPLETE  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/Sergeant`
- Visibility: Public
- Default branch: `main`
- Pinned commit: `2a5f799591ebcc9071202b5576cd8ddcf39762df`
- Version: `0.4.0`
- Licence: MIT
- Ptah relevance: evidence contracts, versioned missions, capability/permission manifests, proof bundles, caller bridge and honest verdict boundaries.

## Files inspected

- `README.md`
- `pyproject.toml`
- `main_review/v2_mission.py`
- `main_review/hardened_mission.py`
- `main_review/app_bridge.py`

## Verified implemented behavior

- Deterministic evidence and semantic reasoning are explicitly separated.
- High-severity semantic findings require supplied repository paths, valid line ranges and source support; unsupported claims are rejected.
- The review system emits explicit PASS / NEEDS WORK / BLOCK outcomes without claiming zero-defect certainty.
- A versioned `sergeant.mission.v2` request model contains source, root, mission type, mode, changed files, branch/commit/PR metadata, external evidence, human decisions, policy profile, time budget, permissions and output preferences.
- Default execution permissions are read-only with shell, network, write and untrusted-code execution disabled unless explicitly allowed.
- Mission intake is normalized before the V2 builder is invoked.
- Repository briefing detects languages, frameworks, package managers, build systems, testing/CI, risk surfaces, documentation and allowed operations.
- `WeaponManifest` describes tool ID, version, status, ownership, supported languages/frameworks/missions, officer compatibility, input/output schemas, required permissions, code/network/write behavior, expected runtime, failure behavior, tests, evidence output and maturity.
- The app bridge is a stable integration layer independent of internal module layout.
- The bridge returns normalized request, deterministic review packet, evidence consensus, learning, benchmark/graduation, squad output, V2 mission output and rendered report.
- V2 failures become structured error packets rather than erasing the rest of the review result.
- The project includes proof fixtures, battle tests, clean-clone proof, browser UI proof, package validation and checksum/artifact practices.
- Runtime API keys remain process-environment secrets and are not returned by status, stored in reports or committed.

## Strong internal patterns for Ptah

1. Versioned mission/request contracts.
2. Explicit execution permissions and time budgets.
3. Tool/Facility manifests that declare capabilities, side effects, permissions, maturity, runtime and evidence output.
4. Deterministic evidence outranks unsupported reasoning.
5. Evidence grounding and rejection are first-class operations.
6. Stable external bridge independent of internal modules.
7. Partial subsystem failure returns structured degraded output rather than destroying all results.
8. Proof fixtures and release artifacts validate claims.
9. Secrets are runtime references, not report contents.
10. Human judgment and final acceptance remain outside the machinery.

## Important limitations for Ptah

- Sergeant's mission/workflow is review-specific and must not become Ptah's universal Activity semantics.
- The Command Center intentionally enforces one active mission; Ptah requires many concurrent unrelated Activities.
- Review permissions are Sergeant defaults, while Ptah restrictions originate from caller/provider configuration rather than a universal review policy.
- Some benchmark/default metrics are synthesized by review logic and are not resource telemetry.
- Evidence/report output is review-oriented, not a universal Artifact/provenance schema.
- Sergeant does not provide durable orchestration, Node placement, event transport or Workspace Provider lifecycle.
- Its officer/weapon identities are product vocabulary, not public Ptah Facility names.

## What Ptah should reuse or adapt

- Versioned Activity and Facility contracts.
- Capability manifest fields: version, status, platforms/languages, schemas, permissions, side effects, expected runtime, failure behavior, tests, evidence type and maturity.
- Caller-supplied execution permissions and budgets.
- Evidence grounding and explicit rejection of unsupported claims.
- Stable public adapter/bridge independent of internal implementation layout.
- Structured degraded/partial failure records.
- Evidence Locker concepts for Artifacts, receipts and history.
- Proof fixture, clean-clone, UI and package validation practices.
- Credential references and redaction rules.

## What Ptah must not inherit

- Sergeant, Cpl, officer or weapon identities in neutral Ptah contracts.
- One-active-mission restriction.
- Review verdicts as generic Activity completion states.
- Deterministic review policy as universal execution policy.
- Synthetic review metrics treated as Node resource telemetry.
- A reasoning system or council inside Ptah.
- Writer/approval rules made universal rather than caller-specified.

## Classification

**ADAPT CONTRACT, MANIFEST, EVIDENCE AND PROOF PATTERNS; HOST SERGEANT AS A CALLER/WORKLOAD.**

Sergeant is strong internal evidence for `CORE-004`, `OBS-001`, `PROV-001`, `UI-002`, Facility manifests, Activity receipts and proof classification.

## Native Ptah completion required

- neutral Facility manifest naming and schemas;
- concurrent Facility and Activity execution;
- durable Object/Artifact/receipt identity;
- trace/event/Activity correlation;
- proof-critical versus operational telemetry classes;
- generalized degraded-result and evidence validation contracts;
- Node/Provider lifecycle integration;
- external review systems connected as callers rather than embedded authority.

## Validation inherited into Ptah

- reject evidence claims lacking valid source/Object references;
- preserve partial valid outputs when one Facility fails;
- prove secret redaction and connection-reference handling;
- pin Facility version, schemas, permissions and maturity;
- retain negative and rejected findings as evidence;
- reproduce proof from a clean environment;
- support many simultaneous Activities even when Sergeant itself keeps one active mission per instance.
