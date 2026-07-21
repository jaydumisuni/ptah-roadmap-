# Campaign 001 — AF01 Archive Mission

Status: ACTIVE — checkpoint 05 complete; five records remain in evidence collection

Started: 2026-07-21

Base authority commit: `856c9859e8faca959f2a38ce33d4607af33e90c1`

Protocol: `planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md` version `1.0.0`

Manifest: `archive/CAMPAIGN-001-FORMATION-MANIFEST.md`

## Objective

Reconcile and durably archive the ten AF01 external-public source obligations without reopening frozen Phase 0A, changing Ptah architecture, adopting source code, or authorizing runtime implementation.

## Formation

| Record | Source | Primary | Independent verifier | Status |
|---|---|---|---|---|
| `D001` | OpenClaw | `AF01-P01` | `AF01-V01` | accepted for archive |
| `D012` | E2B | `AF01-P02` | `AF01-V02` | accepted for archive |
| `D016` | Playwright | `AF01-P03` | `AF01-V03` | accepted for archive |
| `D020` | DeviceFarmer STF | `AF01-P04` | `AF01-V04` | accepted for archive with security restrictions |
| `D030` | gVisor | `AF01-P05` | `AF01-V05` | accepted for archive |
| `D035` | BuildKit | `AF01-P06` | `AF01-V06` | evidence collection |
| `D042` | RAGFlow | `AF01-P07` | `AF01-V07` | evidence collection |
| `D047` | MiniRouter | `AF01-P08` | `AF01-V08` | evidence collection |
| `D051` | SparkDistill | `AF01-P09` | `AF01-V09` | evidence collection |
| `D058` | Strix | `AF01-P10` | `AF01-V10` | evidence collection |

## Evidence obligations

For each source:

1. recover canonical repository identity and current default branch;
2. pin an exact inspected commit;
3. inspect repository metadata, licence and meaningful runtime/source evidence;
4. compare current source with frozen Ptah donor decisions;
5. record verified capabilities and explicit limitations;
6. retain contradictions, stale hints and supersession evidence;
7. preserve public/private and source-reuse boundaries;
8. keep primary and verification observations distinguishable;
9. assign only a bounded archive outcome;
10. update campaign status only after retained evidence exists.

## Authority boundary

Formation workers may collect and challenge evidence. They may not:

- adopt or reject a donor as Ptah architecture authority;
- modify WP01–WP14 or reopen Phase 0A;
- authorize source reuse where rights are unclear;
- claim README text as runtime proof;
- publish private THETECHGUY information;
- accept ADR-0033 or authorize runtime implementation.

## Save points

- mission start: `8dd1ff628171bc1ae75513395ea00377ffae98ec`;
- checkpoint 1: `archive/campaign-001/af01/CHECKPOINT-05.md`;
- checkpoint 2: after records `D035`, `D042`, `D047`, `D051` and `D058` are reconciled;
- formation closure: after exact-head validation and direct review.

## Current counts

- assigned records: 10
- accepted for archive: 5
- blocked: 0
- parked: 0
- superseded: 0
- in evidence collection: 5

Checkpoint 05 is durable. No remaining record is pre-accepted.
