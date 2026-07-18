# Ptah Phase 0B WP02 — Bounded Proof-Level Registry

**Registry:** `ptah.proof-level`  
**Candidate version:** `0.1.0`  
**Status:** CANDIDATE  
**Date:** 2026-07-18

## Purpose

Define the initial proof vocabulary without creating one misleading universal ladder.

Every proof claim is scoped by:

- proof domain;
- proof level;
- exact subject references/revisions/hashes;
- producer authority class;
- observed facts and evidence;
- limitations;
- Receipt and protocol version.

A proof level never implies a level in another domain unless a later explicit protocol says so and supplies the required evidence.

---

# Request and dispatch domain

## `requested`

Meaning: a caller or control component recorded an intent/request.

Permitted authority:

- caller claim;
- Ptah control plane.

Does not imply:

- authorization;
- acceptance;
- routing;
- dispatch;
- physical execution.

## `accepted`

Meaning: the receiving authority accepted the request/command into its declared durable or runtime boundary.

Permitted authority:

- Ptah control plane;
- Ptah Node;
- Workspace Provider;
- Facility runtime;
- external provider where it owns acceptance.

Does not imply:

- routing;
- dispatch;
- work start;
- completion;
- output.

## `routed`

Meaning: a placement/route/producer destination was selected and the command was assigned for delivery.

Permitted authority:

- Ptah control plane;
- Ptah Node;
- scheduler/Provider under an accepted contract.

Does not imply:

- producer receipt;
- dispatch delivery;
- execution.

## `dispatched`

Meaning: the identified producer accepted or received the exact Attempt/nonce for execution.

Permitted authority:

- Ptah Node;
- Provider;
- Facility runtime;
- external provider where it owns dispatch acceptance.

Does not imply:

- process start;
- operation armed;
- work progress;
- completion.

---

# Runtime domain

## `process_started`

Meaning: the operating system/runtime observed a process or equivalent execution unit start.

Permitted authority:

- Ptah Node;
- Provider;
- operating system;
- Facility runtime.

Does not imply:

- interface launch;
- runtime readiness;
- intended operation execution;
- useful output.

## `interface_launched`

Meaning: an interface/application/window/browser/device surface was launched or became addressable.

Permitted authority:

- Provider;
- Facility runtime;
- operating system;
- physical device.

Does not imply:

- readiness;
- correct page/view/state;
- operation armed;
- operation completed.

## `runtime_ready`

Meaning: the runtime passed its declared readiness/read-back condition.

Permitted authority:

- Provider;
- Facility runtime;
- operating system;
- physical device;
- external provider where it owns readiness.

Does not imply:

- operation armed;
- input accepted;
- result produced.

## `operation_armed`

Meaning: the exact intended Operation was selected/configured and ready to perform under the current Attempt.

Permitted authority:

- Provider;
- Facility runtime;
- physical device;
- operating system;
- authoritative external system where applicable.

Does not imply:

- effect occurred;
- progress;
- completion.

## `progress_observed`

Meaning: bounded progress evidence was observed for the exact Attempt/Operation.

Permitted authority:

- Ptah Node;
- Provider;
- Facility runtime;
- operating system;
- physical device;
- external provider.

Does not imply:

- monotonic progress;
- eventual success;
- operation completion;
- output validity.

## `operation_completed`

Meaning: the producer reports the physical Attempt/Operation completion boundary declared by its contract.

Permitted authority:

- Provider;
- Facility runtime;
- operating system;
- physical device;
- external provider;
- authoritative external system.

Does not imply:

- intended side effect occurred correctly;
- output exists;
- output read-back/hash verification;
- independent review;
- caller acceptance.

---

# Output domain

## `output_created`

Meaning: an output Object/Artifact/location was observed to exist for the exact producing Operation/Attempt.

Permitted authority:

- Ptah Node;
- Provider;
- Facility runtime;
- operating system;
- physical device;
- external provider.

Requires:

- exact output reference/location;
- producing correlation;
- observed time.

Does not imply:

- readability;
- completeness;
- correct content;
- hash verification.

## `output_read_back`

Meaning: output was independently read from the claimed storage/device/provider boundary after creation.

Permitted authority:

- Ptah Node;
- storage Provider;
- Facility runtime;
- operating system;
- physical device;
- external provider.

Does not imply:

- expected content;
- hash match;
- semantic correctness.

## `output_hash_verified`

Meaning: read-back bytes matched the declared expected digest under a named algorithm/canonicalization.

Permitted authority:

- Ptah Node;
- storage/Artifact Facility;
- independent verifier;
- authoritative external system where it owns digest verification.

Does not imply:

- semantic correctness;
- safety;
- signature/trust;
- caller acceptance.

---

# External-result domain

## `external_result_recorded`

Meaning: Ptah recorded a result reported by an external system/device/provider.

Permitted authority:

- external provider;
- physical device;
- Facility runtime;
- human confirmation;
- Ptah control plane as recorder only.

Does not imply:

- the source has semantic authority;
- result freshness;
- signature/identity validity;
- authoritative truth.

## `authoritative_external_result`

Meaning: a result was retrieved/read back from the system/device that owns the relevant truth, with authority/freshness/integrity evidence.

Permitted authority:

- authoritative external system;
- physical device for its own state;
- external provider for provider-owned state.

Requires:

- source identity and alias;
- authority evidence;
- exact subject/result schema;
- freshness state;
- integrity/signature/attestation/read-back evidence;
- limitations.

Does not imply:

- independent review;
- caller acceptance;
- correctness beyond the source's authority domain.

---

# Review domain

## `independently_reviewed`

Meaning: an independent reviewer executed a named protocol over exact evidence/checkpoint and issued a separate Verdict.

Permitted authority:

- independent reviewer.

Requires:

- Review entity;
- exact subject refs/hashes;
- protocol revision;
- checks performed/unavailable;
- input evidence;
- Verdict reference.

Does not imply:

- PASS Verdict;
- authoritative external truth;
- caller/organization acceptance;
- future revisions remain reviewed.

---

# Cross-domain rules

1. Proof levels are partially ordered only inside a named protocol/domain.
2. A Receipt may carry several proof claims, but each claim keeps its own domain/level/subjects/limitations.
3. Higher-looking words do not permit inferred claims.
4. `operation_completed` is not `output_created`.
5. `output_created` is not `output_read_back`.
6. `output_read_back` is not `output_hash_verified`.
7. `external_result_recorded` is not `authoritative_external_result`.
8. `independently_reviewed` is not PASS, verification of a future revision, or acceptance.
9. Signature/attestation evidence belongs to provenance/integrity and does not automatically change semantic proof level.
10. Negative, partial and inconclusive claims remain first-class evidence.
11. Proof claims from stale generations/epochs may remain historical but cannot mutate current projections.
12. A proof level definition can be superseded only through a new version and migration/compatibility record.

## Conformance requirements

- reject a proof claim whose level does not belong to its declared domain;
- reject a producer authority class not permitted by the definition;
- reject missing required facts/read-back evidence;
- reject inference across domains without an explicit protocol;
- retain limitations in every presentation/export;
- preserve negative/partial/inconclusive claims;
- ensure Review/Verdict/Acceptance remain separate.

This registry defines candidate vocabulary only. It does not authorize runtime implementation or declare any real Operation proven.
