# Ptah Progress Amendment — 2026-08-15

This amendment records work completed after the historical `PROGRESS.md` entries without rewriting earlier proof history.

Status vocabulary remains the same as `PROGRESS.md`.

## Phase 0C — P01D development-host qualification

**Status:** ACTIVE — PHYSICAL EXECUTION READY — RUNTIME IMPLEMENTATION NOT AUTHORIZED

### Host-qualification architecture correction

- [x] recovered Prime/Ptah authority boundary;
- [x] confirmed Ptah remains independent and OS-neutral;
- [x] confirmed Prime owns machine/Host authority in the intended integrated deployment;
- [x] preserved `Prime Host ID != Ptah Node ID`;
- [x] rejected the resource-wasting interpretation that Ptah requires a second bootable/server OS solely to be part of Prime;
- [x] split former P01 into P01D physical development-host qualification and later P01P Prime-native integration qualification;
- [x] selected Kratos current installed system for P01D;
- [x] selected Oracle MCP/RPC as the private P01D control boundary;
- [x] accepted ADR-0038;
- [x] architecture correction merged as `96d2b7d70f07b801982f215247ab07e8e750568b`;
- [x] runtime authorization remained false.

### Provider-neutral public P01D probe

- [x] OS-neutral development-host contract added;
- [x] portable process execution probe added;
- [x] temporary Workspace lifecycle probe added;
- [x] file durability call probe added;
- [x] atomic replacement probe added;
- [x] host-native advisory file-lock probe added;
- [x] monotonic-clock probe added;
- [x] local stream-socket round-trip probe added;
- [x] thread execution/join probe added;
- [x] OS, architecture, CPU, memory and storage observations added;
- [x] exact clean repository binding before/after collection added;
- [x] acceptance-style output required outside the repository checkout;
- [x] public report forbidden from claiming physical-machine verification, host acceptance, runtime authorization, deployment qualification or release acceptance;
- [x] public report stripped of private machine/controller/transport identity;
- [x] provider-neutral physical-proof runbook added;
- [x] Windows 2025 hosted regression passed;
- [x] Ubuntu 24.04 hosted regression passed;
- [x] all exact-head Ptah-space workflows passed before merge;
- [x] public probe merged as `d9474acaaa01bce27c0b34c951a5dc7faec75081`;
- [x] public physical-proof tracker opened as Ptah-space issue #20;
- [x] former exact-Ubuntu issue #17 closed as superseded/not-planned without claiming its proof passed.

### Ecosystem recovery synchronization

- [x] stale `TTG-progress` Phase 0A current/next/blocker state corrected;
- [x] stale `TTG-progress/ROADMAP.md` retired to an authority pointer while Git history preserves the old plan;
- [x] `TTG-progress/DONE.md` corrected to distinguish completed proof preparation from uncompleted physical acceptance;
- [x] `TTG-ecosystem/docs/PTAH_RECOVERY.md` updated to current P01D/P01P authority;
- [x] existing `TTG-decisions` Ptah architecture/memory record amended rather than duplicated;
- [x] TTG-progress synchronization merge `d8b03723c7c9cd02c347c681240a4295367cb86f`;
- [x] TTG-ecosystem synchronization merge `638a3ffa5afb3b748ec10fca10caf86e50304b1c`;
- [x] TTG-decisions synchronization merge `3f5d3369e8e1f669f3799f4a0b5c14cd70e008c7`.

### Still open — do not mark complete

- [?] execute exact merged probe `d9474acaaa01bce27c0b34c951a5dc7faec75081` on Kratos through Oracle MCP/RPC;
- [?] retain public Ptah report outside the clean checkout;
- [?] retain private Oracle MCP/RPC execution receipt binding the run to Kratos;
- [?] preserve failed/partial physical attempts if any;
- [?] independently review public mechanics evidence + exact repository binding + private physical-machine receipt;
- [ ] accept P01D only if the combined evidence passes;
- [ ] explicitly authorize A01 only after P01D acceptance;
- [ ] start A01 runtime implementation only after explicit authorization;
- [ ] complete P01P later against the real Prime machine Capability Interface / Workload Policy.

## Current exact continuation

```text
Oracle MCP/RPC
    -> Kratos
        -> exact clean Ptah-space d9474acaaa01bce27c0b34c951a5dc7faec75081
        -> run tools/run_development_host_probe.py
        -> retain public report outside checkout

private Oracle execution receipt + public Ptah report
    -> independent review
    -> P01D acceptance decision
    -> explicit A01 authorization only on PASS
```

Hosted CI is already proved as regression evidence and must not be substituted for the physical Kratos execution.
