# WP11 Migration and Compatibility

**Status:** CANDIDATE

## Directional migration rules

- Local paths, container IDs, VM IDs, PIDs, pod names, sandbox IDs and scheduler job IDs migrate only to scoped Aliases.
- Legacy isolation labels migrate to an Isolation Class plus immutable Profile Revision; unknown controls remain limitations.
- Legacy placement rows require exact requirement, capacity snapshot, candidate and decision reconstruction; otherwise preserve as unverified history.
- Existing allocations migrate to Reservation only when amount, scope, holder and validity are known.
- Existing locks migrate to canonical `runtime.lease`; fence tokens cannot be invented.
- Credential values are never imported. Only credential references and delivery/cleanup evidence may migrate.
- Existing port/device/filesystem access becomes explicit expiring grant records; ambiguous scope is denied.
- Existing checkpoints remain checkpoint evidence only and require new-generation Recovery Verification.

## Backend replacement

Container, process, VM, emulator, microVM, remote sandbox and future isolation Providers may replace each other when compatibility, placement, isolation verification, new generation, new Lease/fence and recovery checks pass. Stable Workspaces, Activities, Objects and policies remain unchanged.

## Refusal cases

Migration must refuse false precision when generations, fences, resource units, secret scope, network audience, device epoch or filesystem write policy cannot be established.
