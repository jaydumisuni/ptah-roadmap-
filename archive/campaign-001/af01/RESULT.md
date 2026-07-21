# Campaign 001 — AF01 Accepted Closure Result

Status: ACCEPTED COMPLETE — exact-head evidence and direct review passed

Recorded: 2026-07-21

Accepted: 2026-07-21

## Result

AF01 completed and accepted evidence collection and reconciliation for all ten assigned source obligations.

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

## Accepted evidence

- candidate exact head: `f60e340cb856d50e88b4279147a933d838fce759`;
- AF01 workflow run: `29862087745`;
- accepted archive-protocol run: `29862087738`;
- Master Plan consistency run: `29862087730`;
- retained artifact: `8507695005`;
- artifact digest: `sha256:4ea6bf77131834b48b9e35ad5eb88538a87b6f376f2be4984f077eb3eeed1267`;
- validation report SHA-256: `4a8cf20f3aacf8628c1de1b774cc93018705d0aa256a65208a8abf4311edc691`;
- regression result: 24 passed;
- exact changed-file boundary: 18 durable files;
- candidate merge: `0a35a8a904bdf235fa4989ea05b684443d5a879a`;
- full acceptance record: `archive/campaign-001/af01/ACCEPTANCE.md`.

## Formation-wide conclusions

1. Current canonical identities and exact source heads are retained for every AF01 obligation.
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

## Next formation

```text
AF01: ACCEPTED COMPLETE
AF02: READY / NOT STARTED
```

AF02 readiness is scheduling state only. It does not start evidence collection or authorize any donor, code reuse, architecture change or runtime implementation.

## Non-effects

This accepted result does not:

- reopen Phase 0A;
- modify WP01–WP14;
- select any donor as a default provider;
- authorize code reuse;
- start AF02;
- change P01 physical-host authorization work;
- accept ADR-0033;
- authorize Ptah runtime implementation.
