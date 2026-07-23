# D011 — ORAS

Status: candidate record — paired evidence complete

Primary Archivist: `AF07-P09`

Independent Verifier: `AF07-V09`

Inspected: 2026-07-23

## Canonical source identity

- source: `oras-project/oras`;
- default branch: `main`;
- exact inspected commit: `e5f2178b4079d78b68fb2a31ac88543a6ab81722`;
- root licence: Apache-2.0;
- repository role: OCI artifact client and registry interaction tool;
- archived: false.

## Primary evidence packet

ORAS can push, pull, copy, discover and relate non-container OCI Artifacts such as reports, models, SBOMs, attestations and proof bundles.

## Independent verification packet

Registries, credentials, media types, manifests, referrers and retention policies are separate trust surfaces. Mutable tags and registry acknowledgements do not prove exact content availability or durable retention; digest and read-back verification are required.

## Contradiction and supersession

ORAS is an Artifact transport/storage adapter, not Ptah's canonical Artifact identity or retention authority.

## Bounded outcome

`accepted_for_archive_apache_oci_artifact_client_with_registry_digest_credential_and_retention_boundaries`

Allowed reuse: use pinned ORAS workflows for exact-digest Artifact movement behind Ptah storage/transfer boundaries.

Restrictions: preserve notices; pin registry, manifest, media type and digest; verify destination read-back and retention independently; do not treat tags or push acknowledgement as completion; keep registry IDs as aliases.

This outcome does not authorize implementation.