# D005 — containerd

Status: candidate record — paired evidence complete

Primary Archivist: `AF05-P09`

Independent Verifier: `AF05-V09`

Inspected: 2026-07-23

## Canonical source identity

- source: `containerd/containerd`;
- default branch: `main`;
- exact inspected commit: `a82706307adcdc9811829727c6dc0998a64148d9`;
- root licence: Apache-2.0;
- repository role: container runtime, image, snapshot and process-management daemon;
- archived: false.

## Primary evidence packet

containerd is the selected first OCI/container backend and provides image, content, snapshot, namespace, container, task and process lifecycle patterns.

## Independent verification packet

The verifier confirmed that containerd depends on runtimes, snapshotters, CNI/networking, registries, kernel capabilities and plugins. Namespace/container/task IDs are backend aliases. Creation or start acknowledgement does not prove application success, isolation sufficiency or post-conditions.

## Contradiction and supersession

This record supports the existing locked backend while preserving replaceability and Ptah-owned identity.

## Bounded outcome

`accepted_for_archive_apache_container_runtime_backend_with_plugin_host_and_identity_boundaries`

Allowed reuse:

- use the pinned containerd backend behind the Ptah OCI Provider boundary after authorization;
- retain exact image digest, runtime, snapshotter, plugin, namespace, task and process evidence.

Restrictions:

- preserve Apache notices and review runc, snapshotters, CNI, registries and plugins separately;
- keep backend IDs as aliases and verify workload exit/post-conditions independently;
- fail closed on mutable tags, stale generations, unauthorized mounts or networks;
- do not make containerd Ptah Core or a non-replaceable identity authority.

This outcome does not authorize implementation.