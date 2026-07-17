# Donor Record — Witness

**Phase:** 0A / WP03  
**Status:** FIRST-PASS COMPLETE — ATTESTATION AND POLICY DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/in-toto/witness
- Default branch: `main`
- Pinned commit: `713151bb3fb1bba66fdf739b296c1911fb209569`
- Licence: Apache-2.0
- Activity: Active CNCF in-toto ecosystem project
- Classification: Attestation collection, signing, verification and policy donor
- Ptah targets: command/workload attestations, materials/products, environment/tool identity, signed proof bundles and policy-based verification

## Files/components inspected

- `README.md`
- `LICENSE`
- `docs/about/how-witness-works.md`
- `docs/concepts/attestor.md`
- documented policy, DSSE, Sigstore/SPIFFE, timestamp and Archivista integration boundaries

## Verified capabilities and patterns

- Witness wraps commands to observe execution and create an SDLC audit trail.
- Attestors are versioned interfaces with `Name`, schema `Type` and lifecycle `RunType`.
- Attestor lifecycle distinguishes pre-material, material, execute, product and post-product stages.
- Facts may describe environment, inputs, command/process execution, changed/created files and post-product metadata.
- Attestation schemas are versioned and used during policy evaluation.
- Witness compiles observations into in-toto attestations, places them in DSSE envelopes and signs them.
- Verification checks expected attestations, authorized functionaries and embedded OPA/Rego conditions.
- Integrations include cloud/CI identities, keyless Sigstore, SPIFFE/SPIRE and RFC3161 timestamp authorities.
- Attestations may be transported across air gaps and stored/discovered through Archivista.
- Witness can run in containerized or non-containerized environments without elevated privileges for normal use.
- Security documentation states that attestations are only as trustworthy as their data sources and recommends cryptographic validation evidence where possible.

## What Witness completes

- A proven typed-attestor model for collecting facts before, during and after execution.
- Versioned schemas and lifecycle stages for materials, command and products.
- DSSE-wrapped signed attestation generation.
- Policy verification over expected evidence and authorized identities.
- A bridge between execution receipts, identity/signing and independently checked claims.
- A reusable approach for non-containerized as well as containerized workloads.

## Important limitations for Ptah

- Witness is software-supply-chain oriented and does not model every Ptah Activity, Device or Session requirement.
- Command wrapping is not universal for graphical, remote, device or long-running interactive Activities.
- Attestations are only as reliable as the attestors and producer identity feeding them.
- Policy verification is caller/operator policy, not Ptah's autonomous authority.
- Witness does not replace Ptah Activity state, Object catalogue, Artifact storage or live telemetry.
- Archivista is one storage/discovery option, not mandatory Ptah infrastructure.
- Process tracing/tamper prevention is experimental.
- Attestation creation can add overhead and requires strict redaction of sensitive environment/command data.
- A signed attestation proves who signed reported facts; it does not automatically prove those facts were independently true.

## Must not be inherited

- Witness policy engine as universal Ptah policy.
- Every Activity forced through command wrapping.
- Signature existence promoted to correctness or acceptance.
- Unvalidated attestor output treated as authoritative proof.
- Environment/secrets included in attestations without redaction and explicit schema review.
- Archivista as the only attestation storage backend.
- Witness-specific predicate/schema URLs used as Ptah's only receipt vocabulary.
- Experimental process-tracing guarantees presented as stable.

## Integration decision

**ADAPT ATTESTOR/POLICY PATTERNS AND WRAP WITNESS AS A PROVENANCE FACILITY.**

Ptah should support Witness-generated in-toto/DSSE attestations for suitable Build, test, package and deployment Activities. Ptah's own Receipt schema remains broader and can reference Witness attestations as proof Artifacts.

Witness may also inspire Ptah's versioned Facility evidence plug-ins:

- pre-execution environment/identity attestors;
- input/material collectors;
- execution/command collectors;
- output/product collectors;
- post-product format-specific collectors.

## Native Ptah gap

Ptah must define:

- mapping from Activity/operation/attempt IDs to attestation subjects and predicates;
- Object/Artifact identities and hashes as materials/products;
- producer/Node/Facility identity and connection epoch;
- proof level and authority class beyond supply-chain steps;
- private/public evidence fields and redaction rules;
- long-running and interactive Activity checkpoints;
- device/firmware/application attestors;
- verification state, policy reference and verdict linkage;
- storage through ORAS/R2/local/other backends;
- backend-independent receipt and review relationships.

## Exit strategy

Ptah Receipt/Attestation interfaces remain compatible with in-toto/DSSE but are not tied to the Witness CLI. Attestations may be created by native Facility adapters, other in-toto libraries or external systems.

## Validation required

1. Run one Build Recipe with pre-material, material, execute, product and post-product attestations.
2. Verify exact source, environment, command, tool and output hashes against policy.
3. Reject an attestation signed by an unauthorized identity.
4. Reject a valid signature whose predicate facts fail policy.
5. Correlate the attestation to Ptah Activity, operation, attempt, Objects and Artifacts.
6. Store/retrieve through ORAS and an alternate Ptah storage backend.
7. Prove secrets and sensitive environment values are absent/redacted.
8. Demonstrate an attestor failure as explicit missing/degraded evidence rather than silent success.
9. Verify an air-gapped proof bundle without online services.
10. Preserve Ptah receipts and Artifact identity if Witness is replaced.
