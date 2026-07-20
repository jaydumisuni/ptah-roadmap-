# Phase 0C-02 — First-slice host image and capability pin

Status: candidate for Phase 0C acceptance — runtime implementation remains unauthorized

## Purpose

Pin the exact installation source and the minimum observable Linux capability profile for the first Ptah Node without turning one kernel build, distribution package name or host tool into canonical Ptah identity.

## Selected installation source

- Distribution: Ubuntu Server 24.04.4 LTS (Noble Numbat)
- Architecture: amd64 / x86_64
- Installation image: `ubuntu-24.04.4-live-server-amd64.iso`
- SHA-256: `e907d92eeec9df64163a7e454cbc8d7755e8ddc7ed42f99dbc80c40f1a138433`
- Upstream release directory: `https://releases.ubuntu.com/noble/`
- Upstream checksum manifest: `https://releases.ubuntu.com/noble/SHA256SUMS`
- Checksum signature: `https://releases.ubuntu.com/noble/SHA256SUMS.gpg`

The ISO digest is the installation-source identity. A mirror URL, local filename or removable-media label is only a Location/Alias.

## Installation verification

Before installation:

1. retrieve `SHA256SUMS` and `SHA256SUMS.gpg` from the official Ubuntu release directory;
2. verify the checksum manifest signature using the accepted Ubuntu signing-key procedure;
3. compute SHA-256 over the exact ISO bytes;
4. reject any mismatch;
5. retain the checksum manifest, signature-verification result and ISO digest as Phase 0C evidence.

## Runtime kernel identity

The ISO pin does not authorize Ptah to assume one permanent kernel version. Security and hardware-enablement updates may change the installed kernel.

Every admitted Node generation must therefore record:

- `uname -srmv` output;
- exact kernel package name and version;
- boot ID;
- machine ID digest;
- architecture;
- OS release fields;
- cgroup mode;
- active Linux Security Module evidence;
- container runtime versions;
- capability-probe result;
- observation timestamp and Attempt identity.

A kernel or host-package change creates a new Node/Provider generation and requires the host acceptance probe to run again.

## Mandatory capability profile

The first-slice Node is admitted only when all mandatory capabilities are observed directly.

### Service and process foundation

- systemd is PID 1 and can supervise Ptah services;
- ordinary non-root service accounts are supported;
- PTY allocation and independent terminal sessions work;
- Unix-domain sockets work;
- process groups, signals and exit-status collection work;
- filesystem notifications are available;
- monotonic and wall-clock time can both be observed.

### Isolation foundation

- unified cgroups v2 is mounted and writable by the selected service boundary;
- PID, mount, UTS, IPC, user and network namespace support is observable;
- seccomp filtering is available;
- AppArmor is available and its active/enforcing state is recorded;
- overlayfs is available for the selected container snapshot path;
- no isolation downgrade may occur silently.

### Storage and durability foundation

- the selected data filesystem supports atomic rename within one filesystem;
- directory and file `fsync` behaviour is tested;
- advisory file locks are tested;
- sparse-file behaviour is observed;
- extended-attribute support is recorded;
- sufficient free space is measured before transfer, checkpoint or container operations;
- local content-addressed storage and the SQLite ledger reside on explicitly recorded Locations.

### Network foundation

- loopback networking works;
- local TCP and Unix-socket listeners work;
- outbound network use can be denied for offline proof cases;
- listener addresses and exposed ports are recorded as bounded grants, not inferred from process existence.

### Optional capabilities

The following are useful but are not required for first-slice acceptance:

- KVM acceleration;
- GPU access;
- FUSE;
- physical-device USB access;
- nested virtualization.

Their absence must be explicit negative capability evidence rather than a Node-health failure.

## Host acceptance outcomes

The capability probe produces one of:

- `accepted` — every mandatory capability passed;
- `accepted_with_optional_absence` — mandatory capabilities passed and optional capabilities are absent;
- `rejected` — one or more mandatory capabilities failed;
- `inconclusive` — the probe could not establish the required fact.

`inconclusive` never becomes `accepted` through a default or timeout.

## Update and drift policy

- automatic security updates may be enabled only when the resulting package/kernel change advances Node generation;
- no in-progress proof run may silently cross a host-generation change;
- containerd, runc, Node.js, Playwright, browser, Git, libarchive, SQLite or Rust changes require a new Provider/toolchain generation;
- an update is accepted only after the relevant WP14 positive and negative cases pass on the new exact environment;
- rollback creates another explicit generation and does not erase the failed update evidence.

## Replacement boundary

A later Ubuntu point release, Ubuntu 26.04 LTS, Debian, Fedora, another Linux distribution or a future Ptah OS image may replace this source only when:

- the same mandatory capability profile is satisfied;
- stable Ptah Node/Workspace/Object/Activity identity is preserved;
- migration and recovery proofs pass;
- backend-specific package and image identities remain Aliases/evidence;
- an implementation-selection amendment is accepted.

## Decision effect

This record closes the Phase 0C host-source selection and capability-definition work. It does not authorize deployment or runtime implementation by itself.