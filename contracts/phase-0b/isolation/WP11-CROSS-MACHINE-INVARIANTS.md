# WP11 Cross-Machine Invariants

**Status:** CANDIDATE

1. Isolation Class and Profile Revision define policy; Runtime Provider and Runtime Instance prove realization.
2. Runtime/backend IDs remain scoped Aliases.
3. Placement Candidate is evidence, not a decision; Placement Decision is not Admission.
4. Capacity Snapshot expires and cannot authorize work after staleness or Provider-generation change.
5. Reservation is not Consumption; observed usage cannot rewrite the reservation ledger.
6. Overcommit must be explicit and policy-bounded.
7. Every execution mutation binds current Provider generation, Lease and fence token.
8. `runtime.lease` remains canonical authority; WP11 Lease is a typed projection only.
9. Expired, revoked, released or superseded authority blocks new mutation.
10. Preemption Decision is not Eviction execution.
11. Forced or uncertain eviction cannot become clean completion.
12. Migration creates new target generations, Attempts, Leases and fences.
13. Source shutdown occurs only after target verification and cutover authority.
14. Checkpoint integrity is not functional recovery.
15. Secure Grant contains scope and authority, never a raw secret.
16. Secret Delivery uses a credential reference and one bounded delivery act.
17. Secret cleanup requires independent post-condition verification.
18. Network exposure is explicit by direction, protocol, bind scope, audience and expiry.
19. Device access binds exact Device, connection epoch, Device Lease and allowed operations.
20. Filesystem access binds exact Location, path scope, access mode and write policy.
21. Silent isolation downgrade is prohibited.
22. Provider replacement preserves canonical Ptah identity while advancing generation and fencing stale work.
23. Negative, partial, stale, failed and inconclusive evidence remains immutable history.
24. No runtime implementation or backend selection is authorized by this contract package.
