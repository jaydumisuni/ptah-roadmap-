# Phase 0B WP04 — Node, Facility, Provider, Capability and Health Migration Compatibility

**Status:** CANDIDATE  
**Contract catalogs:** `ptah.common` 0.1.0, `ptah.activity` 0.1.1, `ptah.object` 0.1.0, `ptah.runtime` 0.1.0  
**Date:** 2026-07-19

## Purpose

Define how legacy or future Node/Facility/Provider records enter a newer Ptah contract without fabricating stable identity, trust, capability, readiness, health, capacity, generation or dispatch authority.

## Non-negotiable preservation rules

1. Stable Node identity is never derived from hostname, IP, MAC, cloud instance ID, boot ID, agent installation ID or connection ID alone.
2. Enrollment/trust is not inferred from reachability or possession of an old credential.
3. Node generation, Provider generation and connection epoch remain separate monotonic dimensions.
4. Facility contract identity is not replaced by one implementation, plugin, package or Provider.
5. Provider definition, immutable Provider Revision and running Provider Instance remain separate.
6. Capability Definition, Claim, Verification and Availability remain separate.
7. lifecycle, reachability, readiness, health, capability availability and resource pressure remain separate state dimensions.
8. old heartbeat timestamps or cached capability manifests cannot authorize new dispatch.
9. historical observations, failures, revocations and superseded revisions are retained.
10. backend aliases remain scoped aliases and cannot become canonical Ptah IDs.

## Legacy Node import

A legacy machine/worker record may become:

- one new `core.node` identity only after explicit identity reconciliation;
- one `core.node_enrollment` record with `requested`, `under_review`, `approved`, `rejected`, `revoked` or `expired` state based on evidence;
- zero or more `core.node_observation` records;
- zero or more capability/resource snapshots whose freshness and completeness are explicit.

When identity is ambiguous, create separate candidate Nodes or an unresolved identity relationship. Never merge merely because names, IPs, keys or hardware descriptions match.

Legacy `online`, `healthy`, `ready`, `worker`, `connected` or equivalent flags are imported as observations with source/time/limitations. They do not set trust, lifecycle, capability verification or dispatch eligibility.

## Generation and epoch import

- Missing Node/Provider generations start at a new migration-assigned generation and record that history before import is unavailable.
- A boot ID or process start time may support a generation boundary but cannot be the canonical generation itself.
- Missing connection epochs are assigned only for the imported connection/reconciliation event.
- Existing Attempts/Receipts without exact generations/epochs remain historical but are ineligible for proof-critical automatic correlation.
- Generation counters cannot be reset during backend replacement.

## Capability import

Legacy capability labels are imported as `core.capability_claim` records, not verified support.

A claim becomes verified only through a frozen Protocol/Activity and `core.capability_verification`. A time-bounded `core.capability_availability` may then be derived for the exact subject generation.

Unknown tool version, driver, OS, dependency, device, network or configuration information must appear as limitations. It cannot be filled from current state and attributed to the historical claim.

## Resource import

Legacy capacity/utilization values require:

- source and observation time;
- unit normalization;
- distinction among observed total, administratively allocatable, reserved, consumed, currently available and unavailable/quarantined;
- explicit pressure and overcommit policy where known.

If these dimensions cannot be separated, import a partial snapshot and block new dispatch decisions that require the missing dimension.

## Facility and Provider import

Legacy tool/service/plugin records are decomposed into:

```text
Facility
  stable neutral operation contract

Facility Revision
  immutable operation, permission, capability, dependency and proof contract

Facility Instance
  scoped logical exposure/binding

Provider
  stable implementation-family identity

Provider Revision
  immutable implementation/build/configuration compatibility record

Provider Instance
  one materialized incarnation with generation and aliases
```

One legacy record may produce all six only when evidence supports each layer. Missing layers remain explicit rather than inferred.

Package names, executable paths, process IDs, service names, URLs, sockets, container/VM IDs and module names remain aliases or implementation evidence.

## Lifecycle and observation migration

Legacy global `status` fields are split into the applicable namespaced dimensions:

- Node lifecycle;
- enrollment lifecycle;
- Facility lifecycle;
- Facility Instance lifecycle;
- Provider lifecycle;
- Provider Instance lifecycle;
- reachability;
- readiness;
- health;
- capability verification/availability;
- resource pressure.

Ambiguous values map to `unknown`, a partial observation, or manual review. They are never guessed into `active`, `ready`, `healthy` or `verified`.

## Dispatch eligibility migration

Historical scheduler/worker selection records may become `runtime.dispatch_eligibility` only when they identify:

- exact Activity and Operation;
- exact Node and Provider Instance generations;
- exact Facility Revision/operation key;
- current-at-the-time capability/resource/provider snapshots;
- authorization and policy;
- hard-constraint results;
- evaluation and expiry times.

Otherwise retain them as legacy placement/dispatch evidence, not eligibility authority.

## Compatibility direction

### Backward-compatible additions

May include optional evidence, aliases, limitations, new observation dimensions or new operation/capability references when old records remain semantically valid.

### Breaking changes

Require a new schema/state-machine/contract version when changing:

- canonical identity meaning;
- generation/epoch semantics;
- lifecycle states or transition authority;
- capability or operation semantics;
- side-effect/proof requirements;
- readiness/health meanings;
- resource quantity semantics;
- dispatch hard constraints or authorization.

Every breaking migration requires a `core.migration_definition`, a `core.migration_run`, retained source records, validation results and rollback/export strategy.

## Replacement rules

Replacing a Provider implementation/backend:

1. preserves Facility and Facility Revision identities;
2. creates or selects a Provider/Provider Revision representing the new implementation;
3. creates a new Provider Instance/generation;
4. creates new capability claims, verifications, availability and snapshots;
5. invalidates old dispatch eligibility by expiry/generation mismatch;
6. does not rewrite old Attempts, Receipts, aliases, observations or failures;
7. requires compatibility and conformance evidence before ordinary dispatch.

Replacing a Node agent or rebooting a Node preserves Node identity but advances the appropriate generation/epoch and requires fresh observations/snapshots.

## Negative migration cases

Reject or require manual review when migration attempts to:

- merge Nodes solely by hostname/IP/MAC/cloud ID;
- mark a reachable Node as approved/trusted;
- convert declared capability directly to verified/available;
- mark a running process as a ready/healthy Provider;
- reuse Provider generation after restart;
- preserve dispatch eligibility beyond snapshot expiry or generation change;
- convert total capacity directly to allocatable/available capacity;
- hide optional dependency loss behind `ready`;
- infer Facility identity from Provider package name;
- replace provider aliases with canonical entity IDs;
- discard revocation, failure, stale observation or superseded revision history.

## Validation expectation

WP13/WP14 must execute legacy-to-candidate fixtures, state mappings, generation/freshness checks, backend replacement and round-trip export. Structural JSON Schema validation alone is insufficient.