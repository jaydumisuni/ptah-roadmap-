# D034 — crun

Status: candidate record — paired evidence complete

Primary Archivist: `AF06-P01`

Independent Verifier: `AF06-V01`

Inspected: 2026-07-23

## Canonical source identity

- source: `containers/crun`;
- default branch: `main`;
- exact inspected commit: `fb54bc00bf4a9139e74ba68e00da22b424b90912`;
- licences: GPL-2.0 for crun program; LGPL-2.1 for separately designated libcrun components;
- repository role: lightweight OCI runtime and library;
- archived: false.

## Primary evidence packet

crun is useful as a low-level OCI runtime and C library reference for container lifecycle, cgroups, namespaces, mounts and resource control.

## Independent verification packet

The verifier confirmed that program and library components have different copyleft terms. Build options, linked libraries, kernel features and distribution mode determine obligations. Runtime IDs and start acknowledgements remain backend evidence.

## Contradiction and supersession

crun remains optional runtime research, not the locked first-slice backend or Ptah identity source.

## Bounded outcome

`accepted_for_archive_oci_runtime_reference_with_gpl_program_lgpl_library_and_host_boundaries`

Allowed reuse:

- study crun architecture and evaluate process-separated execution;
- consider libcrun only after exact component and linking review.

Restrictions:

- do not copy or link code without component-level GPL/LGPL compliance review;
- retain exact build flags, libraries, host capabilities and distribution boundary;
- do not expose backend IDs as Ptah identities or equate start with success;
- do not replace the pinned first-slice containerd/runc backend without a reviewed Provider replacement.

This outcome does not authorize implementation.