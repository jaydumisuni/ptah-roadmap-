# Campaign 001 — AF02 Archive Mission

Status: ACTIVE — checkpoint 05 complete; five records remain in evidence collection

Started: 2026-07-21

AF01 accepted closure merge: `ea2424bb5bc2bdb698bfc1bf389601457abd3c89`

Base authority commit: `ea2424bb5bc2bdb698bfc1bf389601457abd3c89`

Protocol: `planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md` version `1.0.0`

Manifest: `archive/CAMPAIGN-001-FORMATION-MANIFEST.md`

## Objective

Reconcile and durably archive the ten AF02 external-public source obligations without reopening frozen Phase 0A, changing Ptah architecture, adopting source code without rights review, or authorizing runtime implementation.

## Formation

| Record | Source | Primary | Independent verifier | Status |
|---|---|---|---|---|
| `D062` | Awesome AI Product Management | `AF02-P01` | `AF02-V01` | accepted for archive — research only |
| `D066` | GitHub README Crisp Links | `AF02-P02` | `AF02-V02` | accepted for archive — documentation tool |
| `D002` | Daytona | `AF02-P03` | `AF02-V03` | accepted with discontinuation/copyleft restrictions |
| `D013` | E2B Desktop | `AF02-P04` | `AF02-V04` | accepted for archive — hosted adapter |
| `D017` | Playwright MCP | `AF02-P05` | `AF02-V05` | accepted for archive — MCP adapter |
| `D021` | ADBKit | `AF02-P06` | `AF02-V06` | evidence collection |
| `D031` | Kata Containers | `AF02-P07` | `AF02-V07` | evidence collection |
| `D036` | Moby | `AF02-P08` | `AF02-V08` | evidence collection |
| `D043` | LlamaIndex | `AF02-P09` | `AF02-V09` | evidence collection |
| `D048` | Ray | `AF02-P10` | `AF02-V10` | evidence collection |

## Evidence obligations

For each source:

1. recover canonical repository identity and current default branch;
2. pin an exact inspected commit;
3. inspect repository metadata, licence and meaningful source/runtime evidence;
4. compare current source with frozen Ptah donor decisions;
5. retain verified capabilities, negative evidence and explicit limitations;
6. distinguish research/documentation sources from implementation donors;
7. preserve source, model, dataset, binary and transitive-rights boundaries;
8. keep primary and independent-verifier observations distinguishable;
9. assign only a bounded archive outcome;
10. update campaign state only after retained evidence exists.

## Authority boundary

Formation workers may collect and challenge evidence. They may not:

- adopt a donor as Ptah architecture authority;
- treat curated links or README claims as executable proof;
- modify WP01–WP14 or reopen Phase 0A;
- authorize source reuse where rights are absent or unclear;
- expose device, provider, model or customer-sensitive data;
- start AF03;
- accept ADR-0033 or authorize runtime implementation.

## Save points

- mission start: `archive/campaign-001/af02/MISSION.md` at AF02 start;
- checkpoint 1: `archive/campaign-001/af02/CHECKPOINT-05.md`;
- checkpoint 2: after records `D021`, `D031`, `D036`, `D043` and `D048` are reconciled;
- formation closure: after exact-head validation and direct review.

## Current counts

- assigned records: 10
- reconciled records: 5
- accepted for archive: 5
- blocked: 0
- parked: 0
- superseded: 0
- in evidence collection: 5

Checkpoint 05 is durable. No remaining record is pre-accepted. P01 remains the active implementation-authorization work outside this archive campaign.
