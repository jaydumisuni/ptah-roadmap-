# Ptah Decision Amendment — 2026-08-15

This amendment is part of current recovery authority. It indexes the owner-directed host-qualification correction without rewriting the historical `DECISIONS.md` record in place.

## D-054 — Development-host qualification and Prime-native integration qualification are separate

**ACCEPTED.** The standalone exact-Ubuntu physical-host interpretation of proposed ADR-0033 no longer blocks first Ptah runtime implementation. The host proof is split into two distinct obligations:

- **P01D — physical development-host qualification:** a provider-neutral portable capability report generated on the selected real development machine, combined with independently reviewed external evidence that binds the execution to that physical machine. P01D is the Phase 0C gate that may authorize A01 after the combined evidence is accepted.
- **P01P — Prime-native integration qualification:** a later integration proof against Prime's machine Capability Interface and Workload Policy. P01P remains open after P01D and does not block A01 runtime construction.

The current selected private P01D machine and control path are recorded in `CURRENT_STATE_AMENDMENT_2026-08-15.md` and must not be copied into public Ptah source.

P01D does not require installing or booting a second operating system, creating a Ptah-specific bootable image, or creating a dedicated guest VM solely to satisfy the former Ubuntu host pin.

The original Ubuntu Server 24.04.4 / Noble GA `6.8.0-136-generic` proof kit remains historical evidence. It is not relabelled as passed and may still be used as Linux-specific diagnostic/provenance machinery.

Linux mechanisms such as cgroups, namespaces, seccomp, overlayfs and AppArmor remain real engineering obligations where Prime uses them. Their acceptance moves to P01P/Prime integration rather than acting as a Ptah distribution-identity lock.

Public Ptah remains provider- and OS-neutral. The public probe cannot claim physical-machine identity, host acceptance or runtime authorization. Private execution/control receipts remain outside the public repository and provide the machine-binding evidence for P01D review.

Runtime implementation remains **NOT AUTHORIZED** until P01D has `portable_capabilities_passed: true`, exact clean repository binding, a retained private MCP/RPC execution receipt establishing the selected physical machine, independent review of the combined evidence, and an explicit closure/authorization record.

Full decision: `decisions/ADR-0038-PRIME-HOST-DEVELOPMENT-QUALIFICATION.md`.

## Supersession order for recovery

For the host-qualification topic only:

1. `decisions/ADR-0038-PRIME-HOST-DEVELOPMENT-QUALIFICATION.md`
2. `CURRENT_STATE_AMENDMENT_2026-08-15.md`
3. this amendment
4. historical `CURRENT_STATE.md` / proposed ADR-0033 host-pin language

All unrelated accepted decisions retain their existing authority.
