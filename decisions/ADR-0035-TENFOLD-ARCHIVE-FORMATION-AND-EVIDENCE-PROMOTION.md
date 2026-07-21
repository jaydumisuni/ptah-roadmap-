# ADR-0035 — Tenfold archive formation and evidence promotion

Status: proposed — review with Phase 0C-17 archive-formation closure

Recorded: 2026-07-21

## Context

Ptah's durable recovery system is correct but still largely sequential. The project now has accepted plans, frozen WP01–WP14 contracts, extensive donor records, internal THETECHGUY sources, old chats, implementation evidence and retained workflow artifacts. Recovering and archiving these one item at a time is too slow, while using many uncoordinated agents would create duplicate summaries, correlated mistakes and false authority.

The owner directed Ptah to borrow Sergeant's existing `10 for 2` private-force rule so archival work can finish faster and still be correct.

Sergeant's accepted operational contract at commit `44c8f47f4bb50a73ef3b4d81d7b849a5aab37dfd` defines:

- a private-force multiplier of ten;
- a minimum private formation of twenty;
- `max(20, human-equivalent workers × 10)`;
- officers and privates separated from final command authority;
- evidence packets that cannot issue verdicts or escape authorized scope.

Ptah needs the same force and evidence-separation pattern for archive/recovery work, but Ptah must not import Sergeant's engineering-review verdict authority.

## Decision

Adopt `planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md` as the operating protocol for large Ptah recovery and archive campaigns.

### Formation rule

```text
private force = max(20, human-equivalent workers × 10)
```

Twenty is the minimum formation, not a ceiling.

Standard formation sizes are:

- Focused: 20;
- Component: 40+;
- Subsystem: 60+;
- System: 80–100+;
- Complex large: up to 120.

### Standard archive formation

A standard twenty-private formation normally handles at most ten ordinary records:

- ten Primary Archivists;
- ten Independent Verifiers;
- one paired lane per record.

A complex record consumes more pairs or a larger formation instead of receiving weaker review.

### Authority separation

- the owner defines objective and acceptance policy;
- an Archive Commander partitions and coordinates the campaign;
- Archive Officers reconcile bounded evidence;
- privates collect and challenge evidence;
- models and tools are replaceable capabilities;
- only the accepted review lane may promote an archive record;
- an archive acceptance does not adopt a donor, accept its claims as Ptah truth or authorize implementation.

### Archive promotion rule

A source record may be promoted only after:

1. exact source identity is recovered;
2. primary evidence is retained;
3. an independent verifier repeats critical checks;
4. contradictions and supersession are reconciled;
5. privacy and rights boundaries pass;
6. the Archive Officer records the bounded outcome;
7. a durable checkpoint and recovery index are updated.

### First campaign

Accept `archive/CAMPAIGN-001-FORMATION-MANIFEST.md` as the candidate queue for archival-completeness auditing:

- 69 external source obligations;
- 29 internal THETECHGUY source obligations;
- 98 total records;
- ten standard formations;
- 200 allocated privates;
- one primary and one verifier per obligation.

The campaign maps and validates existing records first. It does not restart Phase 0A design selection.

## Source and authority rule

The uploaded donor pool list is a queue seed and recovery source. It is not automatically current authority.

When it conflicts with accepted decisions, current state, frozen evidence or current source:

1. retain the conflict;
2. prefer the accepted truth hierarchy;
3. record supersession explicitly;
4. leave unresolved records blocked rather than guessing.

## Public/private boundary

The public roadmap may store:

- public source identities;
- public metadata and evidence references;
- public-safe classifications;
- names of internal source obligations;
- redacted progress and blockers.

Private code, customer/device/payment/employee data, restricted repair knowledge, credentials and non-public implementation evidence remain in approved private storage.

## Save-as-you-go rule

Each formation must commit:

- its mission and scope before work;
- a checkpoint after five reconciled records;
- a checkpoint after ten accepted records or formation completion;
- any blocker that changes scope or authority;
- the exact handoff before a chat/model/operator switch.

## Consequences

- Ptah can archive ten ordinary records in one independently paired formation rather than processing one source serially.
- More agents do not gain more authority.
- Duplicate work becomes an explicit verification lane instead of accidental waste.
- Complex sources automatically consume more force.
- Current donor hints are reconciled instead of blindly copied.
- Existing Phase 0A conclusions remain frozen.
- The method can later support chat, decision, evidence, repository and internal-project archive campaigns.
- The protocol remains an operating record until Ptah runtime implementation is authorized.

## Non-effects

This decision does not:

- reopen Phase 0A;
- change WP01–WP14 contracts;
- change the accepted Master Plan product scope;
- move or weaken P01 physical-host closure;
- accept ADR-0033;
- authorize runtime implementation;
- claim that 200 real concurrent runtime agents already exist.

## Acceptance conditions

ADR-0035 may be accepted when:

1. the Sergeant source rule and authority boundary are pinned;
2. the Ptah protocol defines force scaling, pairing, promotion, privacy and save points;
3. all 98 initial obligations are assigned once;
4. every obligation has one primary and one independent verifier;
5. the manifest allocates ten formations and 200 privates;
6. Phase 0A remains frozen;
7. P01 remains active;
8. ADR-0033 and runtime authorization remain false;
9. a read-only validator and adversarial regression suite pass at exact head.
