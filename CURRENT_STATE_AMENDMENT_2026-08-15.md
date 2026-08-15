# Ptah Current-State Amendment — 2026-08-15

**Status:** operative recovery amendment once merged  
**Applies to:** `CURRENT_STATE.md`, P01 host qualification and proposed ADR-0033  
**Authority:** owner-directed architecture correction recorded in ADR-0038

## Why this amendment exists

`CURRENT_STATE.md` still describes P01 as an exact physical Ubuntu Server 24.04.4 / `6.8.0-136-generic` host proof. That no longer matches the accepted Prime/Ptah deployment boundary.

Prime owns machine authority and Ptah remains an independent OS-neutral mechanical substrate. Ptah will be integrated with Prime through capability projection rather than hosted in a second operating system solely for Ptah.

This amendment is intentionally separate so the historical P01 evidence chain is not rewritten or falsified.

## Operative current position

- Ptah architecture: accepted planning baseline.
- Active phase: Phase 0C.
- Active work unit: **P01D — Kratos physical development-host qualification**.
- Selected physical development machine: **Kratos**.
- Kratos operating system: **use the current installed system; no replacement required for P01D**.
- Ptah-specific bootable/server OS: **not required**.
- Dedicated guest VM/server solely for Ptah: **not required**.
- Current private control path: **Oracle MCP/RPC**.
- Public proof tooling: provider-neutral; it must not expose Oracle, Kratos, private topology or private Prime integration details.
- Runtime implementation: **NOT AUTHORIZED until P01D evidence is collected and independently accepted**.
- Later Prime-native integration proof: **P01P — OPEN / DEFERRED; it does not block starting runtime implementation after P01D closes**.

## What P01D must prove

The physical Kratos run must prove the portable first-runtime prerequisites defined by ADR-0038 and the merged public development-host contract, including:

- process execution;
- temporary Workspace behavior;
- file durability call;
- atomic replacement;
- advisory locking;
- monotonic time;
- local stream sockets;
- threading;
- resource observation;
- exact clean repository binding;
- retained PASS/FAIL evidence.

Distribution/kernel identity is observed but is not an acceptance predicate for P01D.

## What moved to P01P

Prime-owned machine mechanisms are verified later against Prime's Capability Interface and Workload Policy, including:

- process/PTY substrate;
- resource accounting/enforcement;
- isolation;
- secure IPC/capability exposure;
- storage semantics and change observation;
- container/VM/remote execution backends when selected;
- recovery/restart behavior;
- Prime Host -> Ptah Node/Provider/Facility projection;
- explicit `Prime Host ID != Ptah Node ID` identity separation.

Linux implementation details such as cgroups, namespaces, seccomp, overlayfs and AppArmor remain useful lower-layer evidence when Prime uses them, but Ptah is not bound to an Ubuntu distribution identity.

## Superseded interpretation

The following interpretation is no longer operative for runtime-start authorization:

> Ptah must first install/boot an exact Ubuntu Server 24.04.4 host with kernel `6.8.0-136-generic` and close the exact APT pinned-host bundle before runtime implementation may begin.

The old tooling and records remain historical evidence. They must not be relabelled as passed.

## Resume order

1. Merge ADR-0038 recovery authority.
2. Merge the provider-neutral Ptah-space development-host probe and its CI/regression evidence.
3. Use Oracle MCP/RPC to run the exact merged probe on Kratos's current system.
4. Retain the Kratos report plus Oracle MCP/RPC execution receipt privately.
5. Independently review the physical evidence.
6. Record P01D closure and explicit A01 runtime authorization.
7. Begin A01 implementation.
8. Keep P01P open until Prime exposes the required machine Capability Interface for final integration qualification.

## Non-effects

This amendment does not:

- authorize runtime implementation by itself;
- merge Ptah semantics into Prime Core;
- change WP01-WP14 contracts;
- alter accepted licence/source/backend boundaries;
- claim Prime OS is already implemented;
- claim the old Ubuntu pinned-host proof passed;
- weaken Ptah evidence or independent-review requirements.
