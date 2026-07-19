# WP11 Entity-Kind Registry Completion

**Status:** CANDIDATE

## Isolation and runtime

- `isolation.class` — stable isolation-strength and trust-boundary definition.
- `isolation.profile_revision` — immutable policy/capability revision for one isolation class.
- `isolation.runtime_provider` — Provider-scoped implementation capable of realizing an isolation profile.
- `isolation.runtime_instance` — one running isolation boundary generation.
- `isolation.verification` — evidence that the realized boundary matches required isolation properties.

## Placement and capacity

- `placement.request` — workload placement intent and requirements.
- `placement.candidate` — one evaluated Node/Provider/runtime candidate.
- `placement.decision` — reviewed selected/blocked/deferred placement result.
- `resource.requirement` — requested CPU/RAM/storage/GPU/network/device quantities and constraints.
- `resource.capacity_snapshot` — expiring observation of available/allocated/reserved capacity.
- `resource.reservation` — accepted capacity hold with lifecycle, expiry and ownership.
- `resource.consumption_observation` — measured use under exact workload/runtime generation.
- `admission.decision` — explicit admit/queue/reject/preempt/defer result.
- `preemption.plan` — reviewed victims, ordering, checkpoint and safety conditions.
- `eviction.run` — execution and verification of workload eviction.
- `migration.plan` — source/target generations, compatibility, checkpoint and cutover plan.
- `migration.run` — migration execution, cutover, reconciliation and verification.

## Lease, fencing and secure authority

- `lease.request` — requested scoped ownership/control authority.
- `lease.grant` — canonical scoped Lease authority projection over `runtime.lease`.
- `lease.renewal` — explicit renewal decision and new expiry/fence.
- `lease.revocation` — explicit revocation and cleanup/fencing evidence.
- `fence.record` — immutable generation/fencing-token transition evidence.
- `secure.grant` — scoped, expiring, revocable capability/credential-access authority.
- `secure.delivery` — one secret/capability delivery attempt without raw-value persistence.
- `secure.cleanup_verification` — evidence that delivered secret material/capability state was removed or invalidated.
- `network.exposure_grant` — scoped listener/egress/ingress/public-gateway authority.
- `device.access_grant` — scoped physical/virtual Device access authority.
- `filesystem.access_grant` — scoped read/write/mount/export authority.

## Recovery

- `placement.checkpoint_bundle` — placement/migration-specific composition over WP05 Checkpoint Bundle.
- `placement.recovery_verification` — post-placement/migration workload functional verification.

## Reuse

- WP02 Activity/Operation/Attempt/Receipt remain canonical execution/proof.
- WP04 Node/Facility/Provider/generation/capability/health remain canonical runtime identity.
- `runtime.lease` remains the canonical Lease entity; WP11 defines typed requests/grants/renewals/revocations and fencing evidence, not a competing Lease root.
- WP05 Workspace/Checkpoint/Restore remain canonical persistence/recovery identity.
- WP06 Transfer remains canonical data movement.
- WP09 Application/Browser/Device control scopes remain consumers of WP11 authority.

## Non-collapse rules

1. Isolation policy, runtime implementation, runtime instance and verified isolation remain distinct.
2. Placement request, candidate and decision remain distinct.
3. Capacity observation, reservation and actual consumption remain distinct.
4. Admission, placement and execution success remain distinct.
5. Lease ownership, secure grant and secret delivery remain distinct.
6. Grant expiry/revocation fences future work; stale authority never continues silently.
7. Network port/listener existence is not exposure authority.
8. Checkpoint creation, migration cutover and functional recovery remain distinct.
9. Backend scheduler, container, VM, cloud and device IDs remain scoped Aliases.
10. No silent isolation downgrade or resource overcommit is permitted.
