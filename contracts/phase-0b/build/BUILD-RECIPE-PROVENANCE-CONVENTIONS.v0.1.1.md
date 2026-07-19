# Phase 0B WP07 — Build Recipe and Provenance Conventions 0.1.1 Corrections

**Status:** CANDIDATE CORRECTION  
**Date:** 2026-07-19  
**Supersedes:** named clauses in `BUILD-RECIPE-PROVENANCE-CONVENTIONS.md`  
**Implementation authorization:** NONE

## Purpose

Preserve the original candidate draft while adding precision found during the overlapping contract review. All original clauses remain active except where explicitly extended below.

---

# C-001 — Backend compatibility is a separate expiring decision

A Compiled Plan does not itself prove that one backend/provider revision may execute one Recipe Revision.

`build.backend_compatibility` records a directional, target-specific result:

```text
compatible
compatible_with_declared_conversion
compatible_with_reduced_scope
incompatible
unknown
stale
```

It binds:

- exact Recipe Revision;
- target/output/platform subset;
- Facility Revision;
- Provider Revision and adapter/compiler revision;
- required versus optional capabilities;
- unsupported, altered or weakened semantics;
- Node/remote-service and environment requirements;
- proof, isolation, cache, secret and output constraints;
- evidence, evaluated-at and valid-until times.

Rules:

1. unsupported required capability blocks the affected target;
2. optional loss is operation/target scoped;
3. silent proof, isolation, output or platform weakening is forbidden;
4. backend/provider/adapter/environment revision changes expire compatibility where relevant;
5. several compatible Plans may coexist for one Recipe Revision;
6. Plan creation, compatibility, readiness and execution remain separate.

---

# C-002 — Step identity, execution projection and WP02 work remain separate

`build.step` is the stable Recipe/Run-level step identity.

`build.step_run` is one execution projection of that Step and maps to exact WP02 Operations and physical Attempts.

Rules:

- logical retries retain the Step but create new Attempts;
- backend graph/vertex/task IDs remain Aliases;
- dependency edges are frozen and explicit;
- parallel branches retain independent Activity/Operation/Attempt evidence;
- a Step projection does not replace WP02 lifecycle or proof truth.

---

# C-003 — Build Output Record is an explicit producer-to-output bridge

`build.output_record` binds one declared output to exact producer evidence and WP03 identities:

```text
output_declaration_ref
build_run_ref
build_step_ref
activity_ref
operation_ref
attempt_ref
node_provider_materialization_generations
produced_content_object_revision_refs
content_digests
artifact_and_release_refs
location_and_transfer_refs
output_state
completeness_and_finalization
proof_and_provenance_refs
limitations
```

Rules:

1. produced bytes become Content/Object Revisions before Artifact promotion;
2. output registration, Artifact promotion and Artifact Release remain separate;
3. mutable tags, paths, URLs and registry coordinates remain Aliases/Locations;
4. partial/provisional outputs survive later export/SBOM/attestation/signing failure;
5. cleanup state is explicit and receipted.

---

# C-004 — SBOM identity, generation revision and coverage are separate

`provenance.sbom` is the durable logical SBOM identity where continuity is useful.

`provenance.sbom_revision` is one immutable generation over an exact subject, platform, generator and configuration.

`provenance.sbom_coverage` records declared scope, scanned/resolved content, skipped content, unsupported regions, errors and unknown gaps.

Native generator output and SPDX/CycloneDX Views may differ and conversion is not presumed lossless.

A new generator/configuration/cataloguer set creates a new SBOM Revision even when subject bytes are unchanged.

---

# C-005 — Transparency evidence remains separately addressable

`provenance.transparency_evidence` records compact inclusion/timestamp/log-integrity facts, including:

- log or timestamp service identity/revision;
- entry/leaf/body digest;
- integrated or timestamped time;
- inclusion proof/checkpoint/tree state;
- verification protocol and trusted-root refs;
- privacy classification;
- online/offline availability and limitations.

Transparency evidence does not become signature identity, Artifact storage, Activity history, signer authorization or release acceptance.

Public identity disclosure requires explicit privacy acknowledgement. Private-log and offline-no-log policies remain valid.

---

# C-006 — Local and remote Build execution retain truthful locality

A Build Run, readiness assessment and backend compatibility record use exactly one execution-locality form.

## Node-local

Requires exact:

- Node identity and generation;
- current capability/resource snapshots;
- Provider Instance/generation and connection epoch;
- Workspace Materialization generation;
- current Dispatch Eligibility and authority.

## Remote service

Requires exact:

- approved remote-service identity/authority;
- Provider Instance/generation and connection epoch;
- current capability/readiness evidence;
- network, credential, audience, location, licence and policy checks.

Remote Builds do not fabricate Ptah Nodes or Node snapshots.

---

# C-007 — Migration and backend replacement

Migration must not:

- promote detector proposal to accepted Recipe without authority;
- use a path, Dockerfile, job ID, LLB digest or Dagger result ID as canonical Recipe/Run identity;
- omit exact source/material/tool/environment identities;
- treat process exit/backend success as universal completion;
- treat cache reuse as newly executed work or independent reproduction;
- hide volatile inputs;
- serialize raw secrets/keys/tokens;
- use OCI tags/referrer presence as Artifact identity or verification;
- treat SBOM, attestation or signature as correctness/release acceptance;
- discard partial outputs or negative proof after a later-stage failure;
- silently merge incompatible Recipe revisions or provenance graphs.

Backend replacement:

1. preserves Recipe, Object and Artifact identity;
2. creates a new Compiled Plan and compatibility decision;
3. uses new Provider/Run/Attempt generations and aliases;
4. revalidates cache portability rather than assuming it;
5. preserves all earlier outputs, Receipts, attestations, signatures, reviews and failures;
6. compares outputs under an explicit reproduction/compatibility Protocol.

---

# Additional conformance cases

1. reject remote Build records that invent Node evidence;
2. reject local Build readiness without current Node capability/resource evidence;
3. reject Compiled Plan silently weakening required proof/isolation/output semantics;
4. reject output record without exact producer Attempt and immutable digest;
5. retain different SBOM revisions for unchanged subject bytes scanned by different generator/cataloguer revisions;
6. reject transparency inclusion as signer authorization;
7. reject same-cache/same-environment rerun as independent reproduction;
8. preserve valid outputs after export/SBOM/attestation/signing failure;
9. preserve Facility/Recipe identity across BuildKit, Dagger and native backend replacement;
10. reject stale-generation backend events as proof of current Run work.

## Do-not-break rule

> Compatibility, execution locality, Step execution, output registration, SBOM coverage and transparency evidence remain explicit records. They may strengthen the Build/provenance graph but never collapse Recipe, Plan, Run, Object, proof or acceptance identity.
