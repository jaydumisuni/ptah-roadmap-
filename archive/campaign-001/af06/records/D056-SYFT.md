# D056 — Syft

Status: candidate record — paired evidence complete

Primary Archivist: `AF06-P08`

Independent Verifier: `AF06-V08`

Inspected: 2026-07-23

## Canonical source identity

- source: `anchore/syft`;
- default branch: `main`;
- exact inspected commit: `c890e7f17f8db638d3f1558bf087b4cb2f3c2aad`;
- root licence: Apache-2.0;
- repository role: SBOM and package inventory generator;
- archived: false.

## Primary evidence packet

Syft can inventory packages and software metadata from container images and filesystems and emit standard SBOM formats.

## Independent verification packet

Catalogers, parsers, package databases, source scope and format output are coverage-dependent. An SBOM is an observation Artifact, not proof of absence, licence compliance or vulnerability status. Image tags must resolve to exact digests.

## Contradiction and supersession

Syft supports Ptah SBOM generation but cannot replace canonical Package, Artifact, Claim or Evidence identities.

## Bounded outcome

`accepted_for_archive_apache_sbom_workload_with_cataloger_scope_digest_and_completeness_limits`

Allowed reuse:

- run a pinned Syft workload against exact image/filesystem Revisions;
- retain cataloger configuration, source digest, output format and limitations.

Restrictions:

- preserve Apache notices and review databases/parsers separately;
- do not claim inventory completeness or licence/vulnerability conclusions from SBOM generation alone;
- bind mutable images to exact digests;
- store output as source-linked Artifact, not canonical truth.

This outcome does not authorize implementation.