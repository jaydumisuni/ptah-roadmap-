# Campaign 001 — AF01 Candidate Closure Result

Status: CANDIDATE COMPLETE — pending exact-head validation and direct review

Recorded: 2026-07-21

## Result

AF01 completed evidence collection and reconciliation for all ten assigned source obligations.

- accepted for archive: 9;
- blocked completed outcome: 1 (`D047` MiniRouter source reuse);
- remaining evidence collection: 0;
- primary packets: 10;
- independent verifier packets: 10;
- durable checkpoints: 2.

## Records

| Record | Source | Outcome |
|---|---|---|
| `D001` | OpenClaw | accepted for archive |
| `D012` | E2B | accepted for archive |
| `D016` | Playwright | accepted for archive |
| `D020` | DeviceFarmer STF | accepted with security restrictions |
| `D030` | gVisor | accepted for archive |
| `D035` | BuildKit | accepted for archive |
| `D042` | RAGFlow | accepted for archive |
| `D047` | MiniRouter | blocked for source reuse; evidence complete |
| `D051` | SparkDistill | accepted with rights/proof restrictions |
| `D058` | Strix | accepted with offensive-security restrictions |

## Formation-wide conclusions

1. Current canonical identities and exact source heads are now retained for every AF01 obligation.
2. Archive completeness did not change frozen donor architecture.
3. Implementation donors were inspected beyond README claims through licences, package/runtime entry points, source modules, tests or exact maintenance changes.
4. Security and trust limitations remain first-class evidence.
5. Root repository licences do not automatically cover models, datasets, browser/runtime binaries, provider outputs, generated artifacts or transitive services.
6. Public visibility without an explicit licence does not permit source reuse.
7. Archive acceptance does not equal dependency selection, source adoption or Ptah truth.

## Blocked record

MiniRouter is a completed archive record but remains blocked for source reuse because:

- no root `LICENSE` exists at inspected commit `6b283fed773556eb034f052a17dc0f3318f0a76b`;
- `pyproject.toml` declares no licence;
- README states adaptation from another project;
- model, benchmark and provider rights remain independent.

Research/evaluation study may continue without copying or adapting source.

## Non-effects

This result does not:

- reopen Phase 0A;
- modify WP01–WP14;
- select any donor as a default provider;
- authorize code reuse;
- start AF02;
- change P01 physical-host authorization work;
- accept ADR-0033;
- authorize Ptah runtime implementation.

## Acceptance gates

AF01 may close when exact-head proof confirms:

- all ten expected record files exist;
- all IDs, sources, branches, commits, worker pairs and outcomes match `RESULT.json`;
- nine accepted and one blocked outcome are retained;
- both checkpoints exist;
- no record remains in evidence collection;
- Phase 0A remains frozen;
- P01 remains active;
- ADR-0033 remains proposed;
- runtime implementation remains unauthorized;
- AF02 remains unauthorized until AF01 closure is merged and durably bound.
