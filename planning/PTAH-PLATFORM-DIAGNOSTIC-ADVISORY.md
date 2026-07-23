# Ptah Platform Diagnostic Advisory and Efficient Worker Execution

Status: accepted product clarification — runtime implementation remains unauthorized

Version: 1.0.0

Recorded: 2026-07-23

## 1. Owner direction

Ptah remains a neutral digital world and execution platform. It does not decide what work a human, Hunter, Sergeant or another application wants to perform.

The platform may, however, have two small and bounded operating capabilities:

1. diagnose its own operating condition and ask an authorized caller for an upgrade when a requested operation is degraded, incompatible or missing a required capability;
2. when a caller has already supplied a job and an execution recipe, use the Sergeant-derived ten-for-two worker pattern to finish the job faster and more efficiently through bounded parallel workers and independent checks.

Neither capability gives Ptah authority to invent the job, choose the goal, set business priority, approve the result or approve its own upgrade.

## 2. Correct boundary

```text
Caller chooses the work and supplies or selects the execution recipe
        ↓
Ptah executes the requested operation or worker formation
        ↓
Ptah observes its own platform state and exact outcomes
        ↓
Configured rules compare expected and observed state
        ↓
Ptah may emit a bounded diagnostic advisory
and may mechanically manage the caller-selected worker formation
        ↓
Human or calling application decides whether to upgrade
and whether the completed result is accepted
```

These capabilities are platform self-observation and execution mechanics, not product consciousness, business judgment or task planning.

## 3. Sergeant patterns borrowed

### 3.1 Diagnostic pattern

Ptah may borrow the following limited operating pattern from Sergeant:

- compare an explicit obligation or expected condition with observed evidence;
- retain negative and partial evidence;
- identify missing proof, capability or resource;
- challenge optimistic acknowledgements with post-condition checks;
- escalate a bounded deficiency to the responsible caller;
- state uncertainty and the evidence that would resolve it.

### 3.2 Ten-for-two worker execution pattern

For a caller-submitted job, Ptah may execute a caller-selected or caller-supplied formation recipe based on:

```text
worker capacity = max(20, human-equivalent workers × 10)
```

The ordinary two-human-equivalent formation therefore exposes twenty bounded worker slots.

Ptah may mechanically:

- instantiate the declared worker Activities, roles and independent-check lanes;
- place workers on compatible Nodes and Providers within configured Grants, Reservations, Leases and Fences;
- run independent Attempts concurrently;
- preserve worker inputs, outputs, failures, timing, Receipts and evidence;
- checkpoint after configured milestones;
- detect stalled, crashed, missing or incompatible workers;
- retry or replace a failed worker Attempt when the submitted recipe and Policy permit it;
- assemble outputs according to the submitted merge rule;
- report incomplete, conflicting or inconclusive worker results to the caller.

Ptah may not:

- invent the caller's job or goal;
- add semantic subtasks that were not supplied by the caller, Recipe, Plan or coordinating application;
- decide which conclusion is correct beyond configured deterministic checks;
- let workers silently approve their own output;
- treat worker completion as human/application acceptance;
- increase scope merely because more worker capacity exists;
- use the worker formation to choose the next business action.

Hunter, Sergeant or another caller may create the Plan, worker roles, merge logic and acceptance criteria. Ptah supplies the execution world, concurrency, isolation, scheduling evidence and recovery.

Ptah does not borrow Sergeant's review authority, verdict authority, mission selection, rank authority or final decision role.

## 4. Existing Ptah primitives used

No new Core entity is required.

The diagnostic advisory and worker formation are composed from frozen primitives:

- Node, Facility, Provider, Generation, capability, limitation and health records;
- Workspace, Activity, Operation, Attempt and Event records;
- Receipt and Evidence records;
- Claim or Finding records where the frozen contract permits the applicable category;
- Recipe, Plan, Run and Step records for caller-defined worker formations;
- Reservation, Grant, Lease and Fence records for mechanical placement and access;
- View and Artifact records for human-readable and machine-readable output;
- Package, Plugin and Provider revision records for candidate upgrade information.

A diagnostic advisory is a typed View or Artifact over exact platform evidence. A worker formation is a caller-defined Plan/Run composed of Activities and Attempts. Neither becomes a new canonical authority entity.

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
- configured support and minimum-version rules;
- declared worker count, role, independence and checkpoint requirements.

Ptah may not infer hidden user goals or invent requirements that were not supplied by the caller, contract, Recipe, Plan or configured diagnostic rule.

## 6. Diagnostic advisory contents

Each advisory must identify:

- advisory ID and exact revision;
- affected Node, Provider, Facility, Activity, Operation or worker formation;
- observed condition;
- expected condition or configured threshold;
- exact evidence and timestamps;
- detected gap or degradation;
- effect on the requested operation or formation;
- confidence and uncertainty;
- suggested upgrade class, missing capability or missing worker capacity;
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
- more storage, memory, CPU, GPU, network or worker capacity;
- a required runtime, package, plugin, toolchain or Device capability;
- replacement of a degraded Node, Provider or worker Attempt;
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

Ptah may mechanically refuse an operation or worker placement when a frozen contract, submitted Recipe/Plan or configured Policy requires a capability, compatible version, valid Grant, current Generation, Reservation, Lease, Fence, worker-independence rule or safety condition that is absent.

That refusal is not Ptah choosing what the user should do. It is enforcement of a caller- or contract-defined precondition.

Ptah may explain the missing condition and emit an upgrade or capacity advisory. The caller remains responsible for accepting, rejecting, postponing or replacing the requested path.

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

## 10. Worker-formation lifecycle

```text
caller-submitted job and formation recipe
→ worker slots reserved
→ worker Activities and independent Attempts started
→ checkpoint and conflict evidence retained
→ configured merge rule applied
→ complete / partial / failed / inconclusive result returned
→ caller or external reviewer decides acceptance
```

A worker may finish its bounded assignment without approving the whole job. The merge step may assemble deterministic outputs but may not manufacture agreement where worker evidence conflicts.

## 11. Examples

### 11.1 Missing capability

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

### 11.2 Ten-for-two execution

```text
Caller submits a repository audit and selects a ten-for-two recipe.
The recipe defines ten bounded primary checks and ten independent verifier checks.
Ptah reserves twenty worker slots, runs the declared Activities concurrently,
retains every result and checkpoint, and reports conflicts or missing workers.
The caller, Hunter or Sergeant decides what the evidence means and whether the audit passes.
```

Ptah manages the workers but does not invent the audit scope or issue the verdict.

## 12. Relationship to Hunter and Sergeant

Hunter may:

- interpret an advisory in relation to the user's goal;
- create a job Plan and select the ten-for-two execution recipe;
- define worker roles, merge rules and acceptance criteria;
- compare alternatives and recommend a response;
- submit an authorized upgrade Activity.

Sergeant may:

- supply a review formation recipe;
- independently review whether diagnostic or worker evidence supports a claim;
- challenge missing checks, worker independence or optimistic resolution claims;
- publish Sergeant's review result.

Ptah stores and executes the supplied records but does not select the winner.

## 13. Proof requirements

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
- a caller-selected ten-for-two Recipe creates twenty bounded worker slots for two human-equivalent workers;
- every worker remains a distinct Activity/Attempt evidence chain;
- configured primary/verifier independence is preserved;
- failed workers may be retried only within submitted Policy and create new Attempts;
- checkpoints and partial results survive interruption;
- conflicting worker outputs remain visible rather than being forced into agreement;
- worker completion does not equal result acceptance;
- Hunter and Sergeant can use both capabilities without gaining new Ptah authority;
- Ptah never chooses the caller's work or next business action.

## 14. Release placement

The first bounded capabilities belong in Programme A:

- A02 records Node/Provider capability, health, worker capacity and diagnostic gaps;
- A04 executes caller-defined worker Plans, correlates Attempts and emits exact Events/Receipts;
- A06 preserves worker formation state inside Workspaces and Sessions;
- A14 displays advisories, worker formation progress and caller response controls;
- A15 proves no autonomous upgrade, task-selection or result-acceptance authority exists.

Broader capacity planning, distributed worker placement and multi-Node upgrade advice may expand in Programme E after the first version is proven.

## 15. Non-effects

This clarification does not:

- make Ptah self-aware or conscious;
- turn Ptah into Hunter;
- make Ptah a reviewer or approver;
- authorize runtime implementation;
- reopen WP01–WP14;
- start AF03;
- accept ADR-0033;
- change P01 as the active implementation-authorization blocker.
