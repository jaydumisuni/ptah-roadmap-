# D032 — Firecracker

Status: candidate record — paired evidence complete

Primary Archivist: `AF03-P09`

Independent Verifier: `AF03-V09`

Inspected: 2026-07-23

## Canonical source identity

- source: `firecracker-microvm/firecracker`;
- default branch: `main`;
- exact inspected commit: `ae5bf5b68fc41927b3efeca91d220ab11e01f9dc`;
- root licence: Apache License 2.0;
- archived: false.

## Primary evidence packet

Firecracker is a minimalist virtual machine monitor that uses Linux KVM to create microVMs for container and function workloads. It exposes a host API for configuring CPU, memory, kernel, root filesystem, networking, block devices, vsock, logging, metrics and workload start.

Useful Ptah donor concepts include:

- a replaceable microVM isolation Provider;
- exact kernel, rootfs, CPU template, device and resource configuration;
- minimizing guest-facing devices and attack surface;
- a jailer process using cgroups, namespaces and privilege dropping;
- API-driven lifecycle with explicit logs, metrics and resource limits;
- capability and host-compatibility checks before workload admission.

## Independent verification packet

The verifier confirmed:

- the exact public source is Apache-2.0;
- Firecracker requires Linux KVM and hardware virtualization and therefore cannot run on every Ptah Node;
- safe multi-tenant use depends on a correctly configured host operating system, not the VMM binary alone;
- kernels, root filesystems, CPU templates, seccomp filters, jailer configuration and networking are separate artifacts and security surfaces;
- API acknowledgement that a microVM started does not prove guest workload success, isolation correctness or cleanup;
- tested platforms and limitations are narrower than a generic universal-VM claim;
- Firecracker identities and API resources are backend-specific aliases, not canonical Ptah Node, Workspace, Activity or Object identities.

## Contradiction and supersession

The donor pool classified Firecracker as an isolation backend. Current evidence supports that bounded role. It does not support making Firecracker Ptah’s universal sandbox, assuming secure multi-tenancy without host proof, or replacing container/native Providers.

No frozen Ptah Provider, identity, capability, Policy, Lease, Fence or evidence decision is superseded. Firecracker would require an optional Provider admission record tied to exact hardware and host evidence.

## Bounded outcome

`accepted_for_archive_optional_kvm_microvm_isolation_provider`

Allowed reuse:

- study or potentially integrate the Apache-2.0 VMM behind a replaceable Provider boundary;
- retain exact VMM, kernel, rootfs, CPU, host, jailer, seccomp, network, block-device, resource and Generation evidence;
- use only on Nodes whose KVM, hardware, kernel and host-security capability are proven.

Restrictions:

- preserve Apache-2.0 notices and separately review all kernels, root filesystems, tools and images;
- do not claim secure multi-tenancy from VMM presence alone;
- require exact host setup, capability, Policy, Lease/Fence, network/mount and cleanup verification;
- do not treat API start acknowledgement as guest workload success;
- do not map Firecracker VM IDs directly onto canonical Ptah identities;
- do not make Firecracker mandatory or available on incapable Nodes.

This outcome does not authorize implementation.