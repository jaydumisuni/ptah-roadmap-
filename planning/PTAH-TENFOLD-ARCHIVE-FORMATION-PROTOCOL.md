# Ptah Tenfold Archive Formation Protocol

Status: candidate operating protocol — no runtime implementation authorization

Version: 1.0-candidate

Recorded: 2026-07-21

## 1. Purpose

Ptah has more source material than one chat or one sequential researcher can safely recover: external donors, internal THETECHGUY projects, accepted decisions, old chats, implementation evidence, workflow artifacts, research sources and recovery records.

The owner directed Ptah to borrow Sergeant's existing tenfold private-force rule so recovery can finish faster without becoming shallow, duplicated or unreviewable.

This protocol defines a bounded archive formation that:

- increases parallel archival coverage;
- preserves independent verification;
- separates evidence collection from acceptance authority;
- saves intermediate results durably;
- prevents stale source hints from replacing current repository truth;
- keeps private THETECHGUY material outside public records;
- does not reopen frozen Phase 0A or authorize Ptah runtime implementation.

## 2. Sergeant source rule being borrowed

Authoritative Sergeant source:

```text
jaydumisuni/Sergeant
commit 44c8f47f4bb50a73ef3b4d81d7b849a5aab37dfd
main_review/operational_contracts.py
```

The borrowed invariants are:

```text
private force multiplier = 10
minimum private formation = 20
private force = max(20, human-equivalent workers × 10)
```

Sergeant also preserves a strict authority boundary:

- Sergeant defines mission, gates, proof and final verdict;
- Cpl commands campaigns and council rounds;
- officers own specialist doctrine and bounded authorization;
- privates execute evidence obligations without changing authority;
- models and workspace tools have no rank;
- evidence packets cannot issue verdicts or escape authorized scope.

Ptah adopts the force and evidence-separation pattern, not Sergeant's final engineering-review authority.

## 3. Ptah archive authority boundary

### Owner

Defines the archive objective, protected boundaries and acceptance policy.

### Archive Commander

Plans formations, partitions scope, tracks dependencies and stops duplicate work. Hunter may coordinate this role when authorized, but Hunter does not manufacture archive truth.

### Archive Officers

Own one archive doctrine lane:

- Source Identity Officer;
- Licence and Rights Officer;
- Capability and Architecture Officer;
- Security and Maintenance Officer;
- Internal Boundary Officer;
- Contradiction and Supersession Officer;
- Retention and Handoff Officer.

An officer may reconcile evidence and recommend promotion. An officer may not weaken accepted ADRs, frozen contracts or privacy boundaries.

### Privates

Execute assigned, non-overlapping evidence obligations. They may:

- inspect approved sources;
- collect metadata and source references;
- identify contradictions and missing fields;
- create bounded evidence packets;
- mark uncertainty and falsifiers checked.

They may not:

- declare a donor adopted or rejected;
- change Ptah architecture;
- reopen Phase 0A;
- expand scope without escalation;
- publish private source content;
- convert a source hint into canonical truth without verification.

### Models and tools

Replaceable reasoning or retrieval capabilities only. They have no acceptance authority.

## 4. Ten-for-two formation rule

A normal archive mission is budgeted in human-equivalent workers and multiplied by ten.

| Mission difficulty | Human-equivalent need | Private formation | Normal use |
|---|---:|---:|---|
| Focused | 2 | 20 | up to ten ordinary archive records |
| Component | 4 or more | 40+ | one complex component or 10–20 linked records |
| Subsystem | 6 or more | 60+ | a subsystem with several repositories and evidence types |
| System | 8–10 or more | 80–100+ | whole product/repository-family recovery |
| Complex large | up to 12 | up to 120 | unusually large, contradictory or high-risk source set |

Twenty is the minimum, not the target ceiling.

Formation size increases when:

- source trees are large or multi-repository;
- licensing is mixed or unclear;
- current and historical records conflict;
- private/public boundaries are difficult;
- the archive includes binaries or non-text evidence;
- destructive or security-sensitive workflows are described;
- exact source lineage cannot be established;
- ten ordinary records cannot be independently verified within the standard formation.

## 5. Standard twenty-private formation

A standard formation archives at most ten ordinary records.

For each record:

- one Primary Archivist collects the first evidence packet;
- one Independent Verifier repeats the critical checks without copying the primary conclusion.

This produces ten paired lanes:

```text
P01 + V01 → record 01
P02 + V02 → record 02
...
P10 + V10 → record 10
```

The pair model provides wider coverage than assigning all twenty privates to one easy record, while retaining independent challenge.

A complex record may consume multiple pairs or the entire formation. Capacity is reduced before proof quality is reduced.

## 6. Source-diversity rule

Archive formations must avoid correlated blindness.

- adjacent primary assignments should not come from the same source family when the queue permits;
- no single repository family may occupy more than half of a standard formation without an explicit complexity reason;
- unresolved canonical identities are mixed with confirmed sources rather than grouped into one unchecked batch;
- internal and external evidence are never treated as interchangeable;
- a verifier may not reuse the primary archivist's unsupported conclusion;
- generated summaries must link back to exact source evidence.

## 7. Archive record obligation

Each accepted archive record preserves, when applicable:

- stable archive record ID;
- source class;
- canonical source identity;
- owner or organization;
- repository, document, conversation or artifact locator;
- default branch or source version;
- exact commit, release, revision or retrieval time;
- licence and rights boundary;
- last meaningful activity;
- activity/maintenance state;
- Ptah classification and subsystem;
- requirements supported;
- exact files, components, messages or evidence inspected;
- verified capabilities;
- limitations and unsupported claims;
- architecture or operating patterns that may be borrowed;
- source/code/behavior that must not be inherited;
- security and dependency risks;
- public/private classification;
- redaction and retention requirements;
- integration or usage classification;
- replacement or exit strategy;
- validation activity;
- evidence references and content digests where available;
- contradictions and supersession relationships;
- uncertainty and unresolved questions;
- final recommendation or current blocked state;
- reviewer/acceptance record.

A record is not accepted merely because all fields contain text. Claims must be supported by exact evidence.

## 8. Archive lifecycle

```text
queued
→ scoped
→ primary evidence collected
→ independently verified
→ contradiction review
→ reconciled
→ accepted for archive
→ durably retained
→ indexed for recovery
```

Alternative outcomes:

```text
blocked
parked
rejected
superseded
privacy-restricted
```

`accepted for archive` means the record is a trustworthy retained account of the source. It does not mean the source is adopted as a Ptah dependency or that its claims are accepted as Ptah truth.

## 9. Evidence packet

Each private returns a bounded packet containing:

- mission ID;
- formation ID;
- task and record IDs;
- worker role and worker ID;
- authorized scope;
- claims;
- exact evidence references;
- source/retrieval provenance;
- falsifiers checked;
- contradictions found;
- uncertainty;
- questions for the officer;
- confidence;
- completion or blocked status.

Forbidden in private evidence packets:

- final acceptance verdict;
- implementation authorization;
- architecture decision;
- owner approval;
- silent scope expansion;
- unredacted private data in public records.

## 10. Contradiction and supersession handling

When sources disagree:

1. retain both source identities;
2. distinguish source date from acceptance authority;
3. prefer accepted ADRs, current state, frozen evidence and current source over old chat summaries;
4. record the contradiction explicitly;
5. identify whether one source supersedes another;
6. leave the record blocked if authority cannot be resolved;
7. never delete the negative or stale record merely because a newer conclusion exists.

The uploaded donor list is a recovery source and queue seed. Current repository records remain the authority for whether a previously unresolved donor has since been resolved.

## 11. Save-as-you-go requirements

A formation must checkpoint before the whole campaign completes.

Mandatory save points:

- formation mission and scope committed before evidence work;
- after every five reconciled records;
- after every ten accepted records;
- immediately after a blocker changes scope or authority;
- before switching chat, model, device or operator;
- after final formation review.

Each checkpoint updates:

- formation manifest;
- per-record status;
- evidence locations;
- contradictions and blockers;
- exact branch/commit;
- next safe action;
- runtime authorization state.

## 12. Privacy and publication

Public archive records may contain public repository metadata, public source references and public-safe conclusions.

Private records may contain internal project names and bounded operational summaries, but source code, customer/device/payment/employee data, restricted recovery knowledge, credentials and private implementation details remain in approved private storage.

A public backlog may name an internal source obligation without exposing its private contents.

## 13. First archive campaign

The initial campaign audits archival completeness for:

- 69 external donor/source entries recovered in the donor pool list;
- 29 internal THETECHGUY source obligations;
- total obligations: 98;
- ten standard formations;
- minimum allocated private force: 200;
- paired primary/independent-verifier coverage for every obligation;
- escalation permitted for complex donors without changing the tenfold rule.

The campaign first maps existing donor records and frozen conclusions. It fills archival gaps and resolves stale source hints; it does not redo Phase 0A architecture selection from zero.

## 14. Acceptance gates

This protocol is acceptable only when:

- the tenfold multiplier and minimum twenty formation are explicit;
- every obligation has exactly one primary and one independent verifier in the standard backlog;
- all 98 source obligations are covered once;
- unresolved source hints cannot be promoted without current verification;
- private evidence cannot issue acceptance verdicts;
- Phase 0A remains frozen;
- P01 physical-host closure remains the active authorization blocker;
- ADR-0033 remains proposed;
- runtime implementation remains unauthorized;
- a read-only validator and adversarial tests enforce the machine-readable backlog.

## 15. Relationship to Ptah runtime

This is an operating and recovery protocol in the roadmap repository.

It does not implement the future Ptah Knowledge, Activity, Workspace, Agent, Archive, Object or Facility runtime. Later runtime support may represent the same mission, task, evidence, review and retention concepts using frozen Ptah primitives, but only after implementation authorization.
