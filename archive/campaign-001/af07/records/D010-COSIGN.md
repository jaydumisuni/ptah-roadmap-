# D010 — Sigstore Cosign

Status: candidate record — paired evidence complete

Primary Archivist: `AF07-P07`

Independent Verifier: `AF07-V07`

Inspected: 2026-07-23

## Canonical source identity

- source: `sigstore/cosign`;
- default branch: `main`;
- exact inspected commit: `a3ee83c6e0326071a397b4139e875dc4f909e97b`;
- root licence: Apache-2.0;
- repository role: artifact/container/blob signing and verification client;
- archived: false.

## Primary evidence packet

Cosign supports signing and verifying containers, blobs and attestations with key-based or identity-backed workflows and transparency integrations.

## Independent verification packet

Keys, certificates, identity providers, Fulcio, Rekor, trust roots, timestamping and subject digests are separate trust surfaces. Cryptographic validity proves binding to selected identity/key and bytes, not correctness, safety or authorization.

## Contradiction and supersession

Cosign can implement signing Provider workflows but cannot replace Ptah Claim, Evidence, Policy or release authority.

## Bounded outcome

`accepted_for_archive_apache_signing_client_with_identity_trust_root_transparency_and_truth_boundaries`

Allowed reuse: sign/verify exact Ptah Artifacts through pinned Cosign-compatible workflows.

Restrictions: preserve notices; pin trust roots, identity, subject digest and transparency evidence; retain verification failures; never equate valid signature with accepted content or release approval.

This outcome does not authorize implementation.