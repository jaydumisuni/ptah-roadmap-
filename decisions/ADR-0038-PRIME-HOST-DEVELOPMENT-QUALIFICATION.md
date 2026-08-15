# ADR-0038 — Prime-host development qualification and deferred Prime-native proof

**Status:** ACCEPTED — owner direction recovered 2026-08-15  
**Scope:** Phase 0C P01 host qualification only  
**Supersedes:** the standalone exact-Ubuntu-host requirement in proposed ADR-0033 and the host-specific interpretation of Phase 0C-02/12/13  
**Does not supersede:** WP01–WP14 contracts, Apache-2.0 boundary, source layout, backend selections, dependency locks, evidence discipline, or Ptah identity

## Context

The original Phase 0C host candidate bound runtime-start authorization to a standalone Ubuntu Server 24.04.4 LTS amd64 machine with the Noble GA `6.8.0-136-generic` kernel. That was a valid evidence design when Ptah host qualification was being treated independently.

The accepted ecosystem authority now makes the deployment boundary more exact:

- Ptah remains an independent, OS-neutral mechanical Workspace/execution substrate.
- Prime owns the machine layer, Host identity, hardware, drivers, execution backends, isolation machinery, workload policy and capability exposure.
- Ptah consumes machine capability without recreating Prime machine authority.
- A Prime deployment may integrate Ptah as a first-class subsystem, but Prime does not absorb Ptah semantics or make `Prime Host ID` equal `Ptah Node ID`.
- Ptah runtime development must not be blocked until Prime itself is complete.

Requiring a second bootable Ubuntu Server installation, guest OS or dedicated server solely to begin Ptah development would duplicate machine services, waste resources and contradict the intended Prime integration model.

## Decision

### 1. P01 is split into development-host qualification and later Prime-native qualification

The former single exact-host gate is replaced by two different proof obligations.

**P01D — physical development-host qualification** is the Phase 0C gate that may authorize A01 runtime implementation.

**P01P — Prime-native integration qualification** is a later deployment/integration gate. It is not a prerequisite for starting Ptah runtime implementation.

These two proofs must never be collapsed into one claim.

### 2. Kratos current system is the selected P01D physical development host

Kratos is the physical machine used for current Ptah development-host testing.

P01D does **not** require:

- installing or booting Ubuntu Server solely for Ptah;
- creating a Ptah-specific bootable image;
- creating a VM or guest operating system solely to host Ptah;
- replacing the operating system currently installed on Kratos;
- waiting for Prime OS implementation to finish.

A container, VM, compatibility layer or remote Provider may still be used later when an actual Ptah workload requires that backend. Such a backend is not the Ptah host identity.

### 3. P01D proves portable mechanical prerequisites, not distribution identity

P01D must prove on the real Kratos machine that the current development substrate can support the first runtime implementation and its proof loop.

The required portable baseline is:

- child-process execution and exit-code capture;
- temporary Workspace creation and cleanup;
- file write, flush and file-level `fsync`/durability call;
- atomic file replacement;
- advisory file locking using the host-native mechanism;
- monotonic clock behavior;
- local stream-socket round trip;
- thread execution/join;
- stable observation of OS, architecture, CPU count, memory and free local storage;
- clean exact repository binding for the proof tool;
- retained PASS/FAIL evidence with negative results preserved.

OS name, distribution, point release and kernel version are **observations**, not P01D acceptance predicates.

Linux-specific mechanisms such as cgroups v2, Linux namespaces, seccomp, overlayfs and AppArmor are not deleted from the engineering burden. They move to the Prime-native capability/integration proof where Prime owns those machine mechanisms.

### 4. MCP/RPC is the current private control boundary

The authorized current control path for the Kratos proof is Oracle through MCP/RPC.

The Ptah public repository must not depend on Oracle or expose private THETECHGUY topology. Therefore:

- the public Ptah development-host probe remains provider-neutral;
- the private P01D evidence must retain the Oracle MCP/RPC invocation/response receipt separately;
- MCP/RPC control evidence proves how the test was invoked and observed, not Ptah runtime correctness by itself;
- direct ad-hoc coupling to Oracle internals is not permitted.

### 5. Prime remains machine authority; Ptah remains Ptah authority

For the eventual integrated deployment:

```text
physical machine
    -> Prime Host / Prime Capability Interface / Prime Workload Policy
        -> Ptah adapter / Ptah Node / Ptah Facilities and Providers
```

Identity remains explicit:

```text
Prime Host ID != Ptah Node ID
```

Prime owns executability and machine enforcement. Ptah owns Workspace, Activity, Attempt, Environment, Facility, Provider, Node, Object, Revision, View, Artifact, Grant, Lease, Fence, Receipt, Evidence, scheduling and recovery semantics.

### 6. P01P is deferred, not waived

When Prime exposes the relevant Capability Interface, Ptah must run a separate Prime-native integration proof before the Prime deployment can be called qualified.

That proof must cover, as applicable:

- Prime Host capability projection into Ptah Node/Provider/Facility records;
- process supervision and PTY behavior;
- machine resource accounting and enforcement;
- workload isolation and no-silent-weaken policy;
- filesystem durability, atomicity, locking and change observation;
- local IPC and secure capability exposure;
- container/VM/remote-provider execution only where selected by the workload;
- Prime Workload Policy enforcement across Ptah-managed execution;
- recovery/restart behavior and retained evidence;
- distinct Prime Host and Ptah Node identities.

The exact Linux implementation mechanisms may be tested beneath Prime, but Ptah acceptance is against the Prime capability contract rather than an Ubuntu distribution label.

### 7. The old Ubuntu pinned-host kit is retained as historical evidence

`host/image-lock.json`, `host/PINNED-HOST-PROOF-RUNBOOK.md`, the exact APT artifact collector and associated retention tooling remain preserved in Git history and may remain useful as Linux diagnostic/provenance machinery.

They are no longer the operative prerequisite for authorizing A01 runtime implementation.

No old record may be rewritten to claim that its original Ubuntu physical-host proof passed.

## P01D acceptance conditions

A01 runtime implementation may be authorized only after all of the following exist:

1. a merged, provider-neutral development-host probe in `Ptah-space`;
2. a clean exact checkout of that merged proof-tool commit on Kratos;
3. a Kratos report with every required portable capability PASS and `development_host_eligible: true`;
4. a retained private Oracle MCP/RPC execution receipt tied to that test run;
5. repository binding showing the proof tool commit and clean state before/after collection;
6. independent review of the report and transport receipt;
7. a final roadmap closure record that explicitly authorizes A01 while keeping P01P open.

Until those conditions are met, runtime implementation remains unauthorized.

## Consequences

- Ptah can be developed and physically tested now without waiting for Prime or installing another server OS.
- Prime can evolve independently while exposing the machine capabilities Ptah will later consume.
- The resource-wasting second-OS interpretation is removed.
- The old exact-Ubuntu evidence work is preserved rather than falsified or silently deleted.
- Final Prime integration still carries a real proof burden.
- Public Ptah remains neutral; private machine names, Oracle topology and Prime integration policy stay in private recovery/authorization authority.

## Architecture invariants preserved

- Ptah stays independent and OS-neutral.
- Prime does not implement Ptah semantics.
- Ptah does not own boot, kernel, drivers or Prime Host identity.
- Provider/backend identifiers remain aliases, not canonical Ptah identities.
- Evidence is not acceptance.
- A development-host PASS is not a Prime-native PASS.
- No runtime authorization is inferred from this ADR alone.
