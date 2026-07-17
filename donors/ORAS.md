# Donor Record — ORAS

**Phase:** 0A / WP03  
**Status:** FIRST-PASS COMPLETE — OCI ARTIFACT RELATIONSHIP DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/oras-project/oras
- Default branch: `main`
- Pinned commit: `85da14144c4aedec48a1cd44cc34eb4904fc2ed3`
- Licence: Apache-2.0
- Activity: Active CNCF project
- Classification: OCI Artifact client, graph and referrer-relationship machinery
- Ptah targets: content-addressed Artifact transport, reports, patches, SBOMs, attestations, recordings, recipes and subject/referrer relationships

## Files/components inspected

- `README.md`
- `LICENSE`
- `cmd/oras/root/attach.go`
- OCI Image/Distribution relationships already recovered in `donors/CONTAINERD-OCI.md`

## Verified capabilities and patterns

- ORAS operates over OCI registries and OCI image layouts without restricting content to container images.
- `attach` creates a typed OCI 1.1 manifest whose `subject` points to an existing Artifact descriptor.
- Attached content carries explicit Artifact type, media types, annotations and optional custom config.
- Referrer discovery supports OCI 1.1 Referrers API and fallback tag-based schemes.
- Attach can target a platform-specific descriptor in a multi-platform index.
- Files are loaded into a content store, packed into a manifest and copied as a graph.
- Graph copy uses digest-addressed descriptors and configurable concurrency.
- Duplicate graph resolution/copy can be skipped by descriptor equality.
- Manifest export and OCI-layout targets are supported in addition to remote registries.
- JSON and template output paths make machine-readable integration possible.
- The underlying `oras-go` library is separated from the CLI.

## What ORAS completes

- A standards-based way to store and move non-image Artifacts through OCI registries.
- Subject/referrer relationships suitable for SBOMs, signatures, attestations, reports and proof bundles.
- Digest-addressed graph copying and registry interoperability.
- A bridge between local OCI layouts and remote Artifact registries.
- A mature transport rather than inventing a Ptah-specific registry protocol.

## Important limitations for Ptah

- OCI registries are not the live Ptah Workspace filesystem or universal Object store.
- Subject/referrer graphs do not contain Ptah's full Workspace, Activity, Session, proof-level or authority semantics.
- Registry retention, garbage collection and referrer support vary by implementation.
- Tags are mutable and cannot be trusted as immutable identity; digests must be retained.
- Artifact type/media-type naming requires governance and versioning.
- Registry authentication and connectivity are deployment concerns, not Ptah public identity.
- Large interactive streams and frequently mutating Workspace files are poor OCI Artifact workloads.
- Attaching a report or signature does not verify its truth or policy acceptance.
- The CLI is a transport client, not Ptah's Artifact catalogue or provenance engine.

## Must not be inherited

- OCI registry reference/tag as the only Ptah Artifact identity.
- Every Ptah Object forced into an OCI registry.
- Mutable tags used as proof of exact content.
- Referrer presence interpreted as successful verification.
- Registry credentials embedded in public recipes or retained evidence.
- ORAS command output used as the only transfer receipt.
- One registry vendor or referrer fallback scheme made mandatory.

## Integration decision

**ADOPT OCI ARTIFACT COMPATIBILITY AND WRAP ORAS/ORAS-GO AS A TRANSPORT/RELATIONSHIP BACKEND.**

Ptah should use ORAS for suitable durable, versioned and distributable Artifacts while keeping the native Object/Artifact catalogue and content-storage abstraction backend-neutral.

Typical Ptah OCI Artifact classes may include:

- build outputs and release bundles;
- SBOMs;
- attestations and signatures;
- proof bundles and reports;
- patches;
- models or recipes;
- screenshots/recordings when registry distribution is useful;
- cache or environment metadata where appropriate.

## Native Ptah gap

Ptah must define:

- Artifact ID separate from registry digest/reference;
- Object/Artifact type and version registry;
- relationship type and subject semantics;
- local/R2/S3/Drive/OCI storage-location records;
- immutable digest and mutable-alias handling;
- retention, pinning, replication and garbage-collection rules;
- provenance/receipt links to Activities, recipes, Nodes and Facilities;
- verification state distinct from uploaded/present state;
- credential references and transfer receipts;
- fallbacks for registries without full Referrers API support.

## Exit strategy

Ptah Artifact records remain valid when bytes are stored in R2/S3, local CAS, Drive exports or another registry implementation. ORAS is one backend adapter; OCI descriptors are retained as optional storage/relationship metadata.

## Validation required

1. Push one build Artifact by digest and attach an SBOM, attestation, signature and report as separate typed referrers.
2. Discover the complete relationship graph through both Referrers API and fallback path.
3. Pull into a local OCI layout and verify all descriptor digests.
4. Prove mutable tag movement does not change Ptah Artifact identity.
5. Replicate one Artifact graph between registries without duplicate blob upload where supported.
6. Record transfer attempts/receipts independently of CLI output.
7. Delete or make one registry unavailable and recover from a second Ptah storage location.
8. Prove an attached attestation remains unverified until its signature/evidence policy passes.
