# D038 — libarchive

Status: candidate record — paired evidence complete

Primary Archivist: `AF05-P02`

Independent Verifier: `AF05-V02`

Inspected: 2026-07-23

## Canonical source identity

- source: `libarchive/libarchive`;
- default branch: `master`;
- exact inspected commit: `f5509ae993ac30417f81acc5118f232ae3f2d27d`;
- root licence: BSD-style permissive licence;
- repository role: archive reading, writing and extraction library/tooling;
- archived: false.

## Primary evidence packet

libarchive supports broad archive and compression formats and is suitable for read-first archive inventory, streaming extraction and safe decomposition behind Ptah's Object/View/Artifact contracts.

## Independent verification packet

Format support is partial and build-dependent. Encrypted, malformed, sparse, link, traversal and decompression-bomb cases require explicit limits and coverage reporting. Successful library return is not proof that all logical content was safely materialized.

## Contradiction and supersession

libarchive is already the selected first decomposition backend; this record preserves its replaceable-adapter boundary rather than expanding its authority.

## Bounded outcome

`accepted_for_archive_permissive_archive_adapter_with_coverage_traversal_and_resource_limits`

Allowed reuse:

- use the pinned backend behind Ptah-owned decomposition identities;
- retain source digest, format detection, child coverage, skips and limitations.

Restrictions:

- preserve notices and review optional format libraries separately;
- never allow traversal, unsafe links or materialization outside the destination root;
- do not claim full coverage for malformed, encrypted, unsupported or truncated content;
- keep the source Object immutable and backend IDs as aliases.

This outcome does not authorize implementation.