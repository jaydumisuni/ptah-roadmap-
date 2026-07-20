# Phase 0C-02 — First-slice host baseline pin

Status: candidate — runtime implementation remains unauthorized

## Decision boundary

Pin one reproducible Linux host for the first Ptah vertical slice without making Ubuntu, systemd, a kernel package name, or a machine image part of canonical Ptah identity.

## Selected installation image

- Distribution: Ubuntu Server 24.04.4 LTS (Noble Numbat)
- Architecture: amd64 / x86_64
- Image: `ubuntu-24.04.4-live-server-amd64.iso`
- SHA-256: `e907d92eeec9df64163a7e454cbc8d7755e8ddc7ed42f99dbc80c40f1a138433`
- Image role: installation material only; the installed Node receives its own Ptah Node and Node Generation identity.

The image digest is mandatory input evidence. A file with the same name and a different digest is a different material and must not be accepted silently.

## Selected kernel line

Use Noble's GA generic kernel line for the first proof image rather than the moving HWE line.

- Meta-package: `linux-image-generic`
- Candidate pinned package version: `6.8.0-136.136`
- Expected booted kernel family: `6.8.0-136-generic`

The exact installed package list, `uname -a`, kernel build string and boot ID must be captured in the host-image Receipt. A security rebase creates a new Host Image Revision and requires the host capability and first-slice proof suites to run again. Kernel upgrades may not occur silently during one exact-head proof run.

## Required capability profile

The first Node must prove all of the following before Ptah services are admitted:

1. systemd service supervision is available;
2. cgroups v2 is mounted in unified mode;
3. PID, mount, UTS, IPC, network and user namespaces are available;
4. seccomp filtering is available;
5. AppArmor is enabled or its absence is recorded as an explicit reduced-isolation limitation;
6. overlayfs is available for the selected OCI snapshot path;
7. Unix-domain sockets and ordinary loopback TCP are available;
8. PTYs support independent terminal sessions and resize events;
9. ordinary POSIX permissions, fsync, rename and advisory locking work on the selected data filesystem;
10. sufficient inotify resources exist for the first slice;
11. time is synchronized and monotonic-clock behaviour is recorded;
12. the Node can operate with network schema resolution disabled.

## Filesystem and storage baseline

- Root and Ptah data paths must use a local Linux filesystem with documented fsync and atomic-rename behaviour.
- Network filesystems, distributed filesystems and removable-media semantics are outside the first slice.
- Ptah Artifact identity is digest-based and must not depend on the host path, inode or filesystem UUID.
- SQLite database, WAL and shared-memory files must remain on the same supported local filesystem.

## Installation and update rules

- Verify the ISO SHA-256 before installation.
- Apply a recorded package snapshot or lock file when producing the proof image.
- Record every installed direct runtime package and version.
- Disable unattended upgrades for the duration of an exact-head proof run.
- Security updates are not rejected; they are admitted as a new Host Image Revision followed by the required proof rerun.
- HWE or custom kernels require a new Phase 0C/implementation decision record before becoming the first-slice authority.

## Host evidence artifact

The host preparation step must emit an immutable JSON report containing at least:

- image filename and digest;
- architecture and CPU flags relevant to virtualization;
- OS release fields;
- exact kernel package and booted kernel;
- boot ID;
- cgroup mode and controllers;
- namespace probes;
- seccomp and AppArmor state;
- overlayfs support;
- PTY and Unix-socket probes;
- filesystem type and mount options for Ptah data;
- time source and synchronization state;
- package-lock digest;
- limitations and failed probes.

## Replacement boundary

Ubuntu and the selected kernel are first implementations behind the Node and Isolation contracts. Later Debian, Fedora, custom Linux or arm64 Nodes are permitted when they satisfy the same capability declaration, migration, Receipt and WP14 proof obligations.

## Remaining blocker

The package snapshot/lock and generated host-evidence artifact must be produced in the implementation repository before ADR-0033 can be accepted.