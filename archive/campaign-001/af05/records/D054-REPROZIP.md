# D054 — ReproZip

Status: candidate record — paired evidence complete

Primary Archivist: `AF05-P05`

Independent Verifier: `AF05-V05`

Inspected: 2026-07-23

## Canonical source identity

- source: `VIDA-NYU/reprozip`;
- default branch: `1.x`;
- exact inspected commit: `44687ce73efe7a889bf7a1ea982258e2d965c766`;
- root licence: BSD-3-Clause;
- repository role: Linux experiment dependency capture and reproducible execution packaging;
- archived: false.

## Primary evidence packet

ReproZip demonstrates tracing a Linux execution, collecting files and dependencies, producing a portable package and replaying through separate unpacker backends. It is useful for workload-capture and reproduction research.

## Independent verification packet

The verifier confirmed that capture completeness depends on tracing scope, kernel behaviour, external services, network, licences and data access. A packed environment does not prove semantic reproducibility, external service equivalence or safe redistribution of captured dependencies and data.

## Contradiction and supersession

ReproZip can inform Ptah Recipe, Artifact and Reproduction Run tooling, but cannot replace canonical provenance or independent Recovery Verification.

## Bounded outcome

`accepted_for_archive_bsd_reproducible_packaging_donor_with_capture_redistribution_and_semantic_replay_limits`

Allowed reuse:

- study or adapt BSD-licensed tracing, dependency inventory and pack/unpack patterns;
- retain exact capture scope, platform, files, commands, omissions and replay backend.

Restrictions:

- preserve BSD notices and review every captured file, dependency, dataset and licence before redistribution;
- do not claim complete capture of network, hardware, kernel or external-service effects;
- do not treat successful unpack or process start as semantic reproduction proof;
- do not replace Ptah Recipe, Artifact, Claim or Recovery Verification identities.

This outcome does not authorize implementation.