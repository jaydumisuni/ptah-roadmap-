# Ptah Platform Diagnostic Advisory

Status: candidate product clarification — runtime implementation remains unauthorized

Version: 1.0-candidate

Recorded: 2026-07-23

## 1. Owner direction

Ptah remains a neutral digital world and execution platform. It does not decide what work a human, Hunter, Sergeant or another application wants to perform.

The platform may, however, have a small and bounded diagnostic intelligence for its own operating condition. It may detect that:

- a requested operation is not working correctly;
- a Node or Provider is degraded;
- a required capability is absent;
- an installed capability is incompatible or too old for the requested operation;
- available resources are insufficient;
- repeated attempts show the same evidenced failure pattern;
- an upgrade or additional Provider could improve or unblock the requested work.

Ptah may then present an evidence-backed advisory or ask an authorized caller for an upgrade. It may not decide the caller's work, approve its own request or install the upgrade without configured authority.

## 2. Correct boundary

```text
Caller chooses the work
        ↓
Ptah executes the requested operation
        ↓
Ptah observes its own platform state and exact outcome
        ↓
Configured diagnostic rules compare expected and observed state
        ↓
Ptah may emit a bounded diagnostic advisory
        ↓
Human or calling application decides whether to act
```

The diagnostic capability is platform self-observation, not product consciousness, business judgment or task planning.

## 3. Sergeant pattern borrowed

Ptah may borrow the following limited operating pattern from Sergeant:

- compare an explicit obligation or expected condition with observed evidence;
- retain negative and partial evidence;
- identify missing proof, capability or resource;
- challenge optimistic acknowledgements with post-condition checks;
- escalate a bounded deficiency to the responsible caller;
- state uncertainty and the evidence that would resolve it.

Ptah does not borrow Sergeant's review authority, verdict authority, mission selection, rank structure or final decision role.

## 4. Existing Ptah primitives used

No new Core entity is required.

The advisory is composed from frozen primitives:

- Node, Facility, Provider, Generation, capability, limitation and health records;
- Activity, Operation, Attempt and Event records;
- Receipt and Evidence records;
- Claim or Finding records where the frozen contract permits the applicable category;
- View and Artifact records for human-readable and machine-readable diagnostic output;
- caller-configured Policy, Grant, Lease and Fence records for mechanical access;
- Package, Plugin and Provider revision records for candidate upgrade information.

A diagnostic advisory is a typed View or Artifact over exact platform evidence. It does not become a new canonical authority entity.

## 5. Allowed diagnostic inputs

Ptah may evaluate only evidence available through configured platform records and checks, including:

- health and readiness probes;
- exact Provider revision and Generation;
- declared capabilities and limitations;
- host architecture, resources and pressure;
- dependency and protocol compatibility;
- repeated Attempt outcomes;
- post-condition verification failures;
- timeout, crash, disconnect and restart evidence;
- storage, memory, CPU, GPU, network or Device availability;
- caller-requested operation requirements;
- configured support and minimum-version rules.

Ptah may not infer hidden user goals or invent requirements that were not supplied by the caller, contract or configured diagnostic rule.

## 6. Diagnostic advisory contents

Each advisory must identify:

- advisory ID and exact revision;
- affected Node, Provider, Facility, Activity or Operation;
- observed condition;
- expected condition or configured threshold;
- exact evidence and timestamps;
- detected gap or degradation;
- effect on the requested operation;
- confidence and uncertainty;
- suggested upgrade class or missing capability;
- known compatible alternatives, when configured and evidenced;
- whether work is blocked, degraded or unaffected;
- whether unrelated Activities may continue;
- required human/application decision;
- expiry or recheck condition.

The advisory must separate observed facts from suggestions.

## 7. Upgrade request boundary

Ptah may ask for:

- an additional Provider;
- a newer compatible Provider revision;
- more storage, memory, CPU, GPU or network capacity;
- a required runtime, package, plugin, toolchain or Device capability;
- replacement of a degraded Node or Provider;
- a compatibility migration or restart;
- an operator inspection when the condition cannot be resolved automatically.

Ptah may not:

- choose a new user goal;
- reprioritize caller work;
- buy hardware or services;
- install, upgrade, remove or replace software without configured authority;
- select a vendor based on hidden preference;
- approve its own advisory;
- mark an upgrade successful without independent post-condition evidence;
- block unrelated work merely because an upgrade is available;
- convert a suggestion into an Activity unless a caller or configured automation submits it.

## 8. Mechanical enforcement versus judgment

Ptah may mechanically refuse an operation when a frozen contract or configured Policy requires a capability, compatible version, valid Grant, current Generation, Lease, Fence or safety condition that is absent.

That refusal is not Ptah choosing what the user should do. It is enforcement of a caller- or contract-defined precondition.

Ptah may explain the missing condition and emit an upgrade advisory. The caller remains responsible for accepting, rejecting, postponing or replacing the requested path.

## 9. Diagnostic lifecycle

```text
observed
→ evidence collected
→ gap or degradation detected
→ advisory emitted
→ caller acknowledged / dismissed / deferred / approved externally
→ optional caller-submitted upgrade Activity
→ post-condition recheck
→ resolved / still present / inconclusive
```

The lifecycle may be repeated when evidence or Provider Generation changes.

Dismissal does not erase the original evidence. Approval does not equal successful upgrade. Installation acknowledgement does not equal resolution.

## 10. Example

```text
Caller requests GPU-backed model execution.
Ptah observes that the selected Node has no compatible GPU Provider.
Ptah returns the failed capability check and a diagnostic advisory:
  - requested capability: CUDA-compatible GPU execution;
  - observed capability: CPU-only;
  - effect: requested acceleration unavailable;
  - alternative: continue through the available CPU Provider;
  - suggested upgrade class: compatible GPU Node or Provider;
  - decision required: caller chooses CPU continuation, another Node or upgrade.
```

Ptah does not decide which option the caller should choose.

## 11. Relationship to Hunter and Sergeant

Hunter may:

- interpret the advisory in relation to the user's goal;
- compare alternatives;
- recommend a response;
- submit an authorized upgrade Activity.

Sergeant may:

- independently review whether the diagnostic evidence supports the advisory;
- challenge missing checks or optimistic resolution claims;
- publish Sergeant's review result.

Ptah stores both results but does not select the winner.

## 12. Proof requirements

Implementation proof must demonstrate:

- a missing capability produces a bounded advisory;
- a degraded Provider produces evidence without inventing a user goal;
- repeated failures may be correlated without collapsing distinct Attempts;
- an advisory identifies evidence, expected condition, gap and uncertainty;
- unrelated Activities continue when their requirements are satisfied;
- advisory creation does not install or approve an upgrade;
- a caller-approved upgrade creates a separate Activity and new Provider/Node revision or Generation where applicable;
- acknowledgement alone cannot mark the advisory resolved;
- post-condition failure keeps the advisory open or inconclusive;
- a false-positive or stale advisory can be superseded without deleting its evidence;
- Hunter and Sergeant can use the advisory without gaining new Ptah authority;
- Ptah never chooses the caller's work or next business action.

## 13. Release placement

The first bounded capability belongs in Programme A:

- A02 records Node/Provider capability, health and diagnostic gaps;
- A04 correlates repeated Attempt failures and emits exact Events/Receipts;
- A14 displays advisories and lets a human choose a response;
- A15 proves no autonomous upgrade or task-selection authority exists.

Broader capacity planning and multi-Node upgrade advice may expand in Programme E after the first version is proven.

## 14. Non-effects

This clarification does not:

- make Ptah self-aware or conscious;
- turn Ptah into Hunter;
- make Ptah a reviewer or approver;
- authorize runtime implementation;
- reopen WP01–WP14;
- start AF03;
- accept ADR-0033;
- change P01 as the active implementation-authorization blocker.
