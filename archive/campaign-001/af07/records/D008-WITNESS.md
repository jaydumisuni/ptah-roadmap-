# D008 — Witness

Status: candidate record — paired evidence complete

Primary Archivist: `AF07-P03`

Independent Verifier: `AF07-V03`

Inspected: 2026-07-23

## Canonical source identity

- source: `in-toto/witness`;
- default branch: `main`;
- exact inspected commit: `fefddc8b9de4155cbc90ea1b21c04d3ea7a1b348`;
- root licence: Apache-2.0;
- repository role: attestation, policy and evidence collection/verification tooling;
- archived: false.

## Primary evidence packet

Witness can inform proof bundles, workload attestations, artifact provenance and policy verification.

## Independent verification packet

Attestors, keys, identities, policy files, transparency services and subject digests are separate trust surfaces. A signed statement proves signer/key relation and bytes, not correctness of the asserted external effect.

## Contradiction and supersession

Witness supports Ptah Evidence/Artifact workflows but cannot replace canonical Receipt, Claim, Evidence or acceptance authority.

## Bounded outcome

`accepted_for_archive_apache_attestation_tool_with_signer_policy_subject_and_truth_boundaries`

Allowed reuse: run or adapt pinned attestors and verification behind Ptah evidence records.

Restrictions: preserve notices; pin subjects, policies and signer identities; never equate signature validity with claim truth; keep Witness IDs and statements as backend evidence.

This outcome does not authorize implementation.