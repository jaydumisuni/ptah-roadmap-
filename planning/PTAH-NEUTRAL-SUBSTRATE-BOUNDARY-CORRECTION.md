# Ptah neutral substrate boundary correction

Status: candidate correction under review — no runtime implementation authorization

Recorded: 2026-07-22

## Existing foundation

The accepted Master Plan already establishes:

> Ptah is the world, not the thinker.

The caller provides intent, reasoning, policy, priority, judgment and acceptance criteria. Ptah provides the environment and machinery.

## Drift being corrected

Later AI Project Workspace and context-compiler wording assigned context selection, source-authority ranking, blocker selection, next-action selection, approval flow, candidate promotion and reviewer-packet construction to Ptah.

That wording contradicted the existing foundation. It did not represent an owner-approved change of architecture.

## Correct responsibility boundary

### Ptah

Ptah is a neutral Workspace and execution substrate. It provides and mechanically operates:

- Workspaces, Sessions and Activities;
- storage, Objects, Revisions and Artifacts;
- Processes, terminals, browsers, containers, Devices and other Facilities;
- configured Grants, Leases and Fences;
- Events, Receipts, logs, checkpoints and recovery;
- exact requested-record retrieval and caller-supplied query execution.

Ptah does not decide:

- what the user wants;
- which task matters;
- which source is authoritative;
- which context is relevant;
- whether a claim or result is correct;
- whether an action should be approved;
- which agent acts next;
- whether Hunter or Sergeant passed;
- what should become canonical truth.

### Hunter or another caller application

Hunter or another caller application supplies intelligence, source judgments, context selection, planning, coordination, Provider choice, next-action proposals and approval requests.

### Sergeant or another reviewer

Sergeant independently reviews a frozen candidate using Ptah resources. Sergeant selects its review evidence, performs the review and issues Sergeant's result. Ptah stores the supplied inputs and result but does not agree, approve or promote it.

### Human or calling authority

The human or calling authority owns intent, configured policy, acceptance, rejection, release and final authorization.

## Effect on accepted planning language

The accepted Master Plan remains authoritative, but ambiguous later language is corrected as follows:

- source labels and policy records may be stored and mechanically enforced by Ptah, but their meaning and assignment come from callers;
- bounded context packets are produced by Hunter or another caller-side compiler using Ptah retrieval and storage Facilities;
- Ptah returns requested records and enforces configured access; it does not rank relevance or select authority;
- handoffs are caller-generated Artifacts stored and recovered by Ptah;
- candidate promotion is performed only through an external human/application decision and recorded mechanically by Ptah;
- Sergeant review is an independent application workflow using Ptah, not a Ptah verdict.

## Public correction evidence

The public donor/profile correction was merged in `jaydumisuni/Ptah-space`:

```text
PR #15
merge: 8a8d620c5227a6508145cd4a30f4f45142bfabe9
validated exact head: 5a95c577edf366bad1d8949ee37c17b81f296254
workflow run: 29961370694
artifact: 8546091277
artifact digest: sha256:04472fd4fd546fcc2420d135cdfcb517381efbe5de8b3bc14f6971207fbde819
```

## Preserved boundaries

- no new Ptah Core entity;
- no WP01–WP14 reopening;
- Phase 0A remains frozen;
- P01 remains the active authorization work;
- ADR-0033 remains proposed;
- AF03 remains not started;
- runtime implementation remains unauthorized.
