# D033 — Youki

Status: candidate record — paired evidence complete

Primary Archivist: `AF05-P01`

Independent Verifier: `AF05-V01`

Inspected: 2026-07-23

## Canonical source identity

- source: `youki-dev/youki`;
- default branch: `main`;
- exact inspected commit: `59fbf00fa2fb6ccc33b5252b9ab2b2936efa3ffb`;
- root licence: Apache-2.0;
- repository role: Rust OCI runtime implementation;
- archived: false.

## Primary evidence packet

Youki is useful as a low-level OCI runtime implementation reference for namespaces, cgroups, mounts, capabilities, hooks and runtime lifecycle in Rust.

## Independent verification packet

The verifier confirmed that OCI compliance does not make backend container IDs canonical Ptah identities. Kernel, cgroup, seccomp, LSM, architecture and integration support remain exact host/runtime capability surfaces. A runtime start result does not prove workload success.

## Contradiction and supersession

Youki remains an optional runtime Provider reference, not Ptah Core or a current v1 dependency.

## Bounded outcome

`accepted_for_archive_apache_rust_oci_runtime_reference_with_host_and_identity_boundaries`

Allowed reuse:

- study or adapt Apache-2.0 OCI runtime implementation patterns;
- evaluate as a replaceable runtime Provider only after exact host proof.

Restrictions:

- preserve Apache notices and review dependencies and kernel features separately;
- do not expose backend IDs as Ptah identities;
- do not treat runtime start as workload success;
- do not make Youki mandatory or bypass containerd/runc first-slice locks.

This outcome does not authorize implementation.