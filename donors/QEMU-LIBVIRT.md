# Donor Record — QEMU and libvirt

**Phase:** 0A / WP07B  
**Status:** FIRST-PASS COMPLETE — PRIMARY VM/APPLICATION-PROVIDER MACHINERY CANDIDATE  
**Inspected:** 2026-07-17

## Identity

### QEMU

- Canonical URL: https://github.com/qemu/qemu
- Default branch: `master`
- Pinned commit: `5ef0ecc5942ee07bb581cc96a97bbfc0fdf4005c`
- Licence: GPL-2.0 overall, with component-specific licensing recorded in the source tree

### libvirt

- Canonical URL: https://github.com/libvirt/libvirt
- Default branch: `master`
- Pinned commit: `674fcf87bdd479302032fbeb331fea2aa51606ac`
- Licence: LGPL-2.1-or-later for the public C library, with GPL-covered non-library components

- Classification: virtual-machine lifecycle, hardware emulation, hypervisor abstraction and snapshot donor set
- Ptah targets: `APP-003`, Windows/Linux VM providers, isolated native application environments, checkpoints, disks, networks, displays and remote application sessions

## Files/components inspected

- QEMU `README.rst`
- QEMU QMP reference entry point
- libvirt `README.rst`
- libvirt snapshot documentation
- documented QEMU/KVM, monitor API, hypervisor and management-daemon boundaries

## Verified capabilities and patterns

### QEMU

- Emulates complete machines without hardware virtualization and can use KVM/Xen for near-native execution.
- Supports cross-architecture machine and user-space emulation.
- Exposes stable command-line and monitor APIs for higher-level managers.
- Is commonly managed indirectly through libvirt.
- Builds on Linux, macOS and Windows hosts, though production capability differs by host accelerator.
- Supplies virtual disks, networks, displays, input devices, USB devices and machine hardware models.

### libvirt

- Exposes a long-term stable management API across QEMU/KVM, Xen, LXC, bhyve, Hyper-V, VirtualBox, VMware and other providers.
- Provides a stateful management daemon with local and remote API access.
- Has bindings in several languages.
- Models domains, storage, networking, devices and lifecycle independently from one hypervisor CLI.
- Supports VM snapshots and explicitly distinguishes VM-memory snapshots, externally managed disk snapshots and caller-controlled pause/resume coordination.
- Manual snapshot mode demonstrates that hypervisor state and external storage state may require coordinated but separate proof.

## What this donor set completes

- A mature Windows VM Provider path on Linux/KVM hosts.
- Machine lifecycle, resources, disks, networking and virtual-device attachment.
- A provider-neutral virtualization API rather than hard-coding QEMU command lines into Ptah.
- VM pause, resume, snapshot and recovery foundations.
- VNC/SPICE/RDP-facing display endpoints for browser/native presentation backends.
- A route for Windows EXE/MSI workloads without requiring the Ptah control plane itself to run Windows.
- Cross-architecture and software-emulation fallbacks where performance permits.

## Important limitations for Ptah

- A VM/domain is a provider environment, not a Ptah Workspace, Application Session or Artifact identity.
- VM running state does not prove the guest OS is ready, logged in or the target application is usable.
- Memory snapshots, disk snapshots and externally managed storage snapshots have different consistency guarantees.
- A crash-consistent VM snapshot is not automatically application-consistent.
- Windows licensing, activation and redistribution remain deployment/operator responsibilities.
- GPU acceleration and passthrough require host-specific hardware, drivers, IOMMU and security proof.
- QEMU/libvirt expose powerful host/device/network capabilities and must be tightly scoped.
- GPL/LGPL boundaries require service/library packaging review; QEMU source should not be copied into Ptah Core.
- Nested virtualization and cloud-host restrictions may limit available features.
- VM images are large mutable Objects and require explicit checkpoint, backup and retention treatment.
- A display endpoint does not supply semantic Windows UI automation.

## Must not be inherited

- QEMU/libvirt domain IDs as canonical Ptah Workspace or Application Session identity.
- raw QEMU command lines exposed as the public Application Provider contract.
- arbitrary host-device, filesystem or network passthrough.
- snapshot success promoted to application-consistent recovery without guest/quiesce proof.
- VM state treated as backup or immutable Artifact truth.
- automatic restart of a VM interpreted as permission to replay application side effects.
- Windows images/keys/licences embedded in public Ptah source.
- hypervisor-specific XML/QMP schemas made canonical public Ptah schemas.

## Integration decision

**WRAP LIBVIRT AS THE PRIMARY VM-PROVIDER API, WITH QEMU/KVM AS THE INITIAL WINDOWS VM BACKEND.**

Ptah owns Workspace/Application Provider identity, VM-image Objects, Activities, checkpoints, credentials, display endpoints, Application Sessions and receipts.

Recommended provider classes:

1. QEMU/KVM Windows VM Provider on Linux Nodes;
2. QEMU/KVM Linux VM Provider for strong isolation or full OS testing;
3. future Hyper-V/VirtualBox/VMware/bhyve adapters where required;
4. direct native Windows Node as a separate provider class, not a QEMU mode.

## Native Ptah gap

Ptah must define:

- VM Provider manifest and host-accelerator capabilities;
- machine template/image Object and licence references;
- CPU/RAM/GPU/storage/network/device resource requests;
- domain/backend IDs as replaceable references;
- guest-agent/readiness and login-state receipts;
- memory/disk/application-consistent checkpoint classes;
- external storage snapshot coordination;
- display endpoint and short-lived connection-token records;
- VM/Application Session correlation;
- image clone/COW/revision and cleanup rules;
- Windows activation/licence privacy boundaries;
- migration, restart and stale-session handling;
- backend replacement and import/export tests.

## Exit strategy

Ptah's VM Provider contract remains implementable through QEMU/libvirt, Hyper-V, VMware, VirtualBox, cloud VM APIs or future microVM backends. Hypervisor/domain IDs remain adapter metadata.

## Validation required

1. Create two independent Windows VMs from one immutable base image using separate writable layers.
2. Prove booted, guest-agent-ready, user-session-ready and target-application-ready as separate states.
3. Snapshot VM memory and disks, then perform an application-consistent checkpoint with guest quiesce/read-back.
4. Restart the provider daemon and reconcile domains without changing Ptah Workspace/Application Session identity.
5. Attach an RDP/VNC display endpoint through a scoped gateway.
6. Enforce CPU/RAM/disk/network/device limits and report actual resource use.
7. Reject arbitrary host-device/filesystem passthrough.
8. Restore from a checkpoint and verify application-visible state separately from VM running state.
9. Replace QEMU/libvirt with another VM backend for one template without changing public Ptah contracts.
