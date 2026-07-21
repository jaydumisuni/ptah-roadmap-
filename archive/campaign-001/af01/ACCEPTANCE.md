# Campaign 001 — AF01 Accepted Closure

Status: ACCEPTED EVIDENCE RECORD

Accepted: 2026-07-21

## Candidate evidence

- candidate exact head: `f60e340cb856d50e88b4279147a933d838fce759`;
- AF01 workflow run: `29862087745`;
- accepted archive-protocol run: `29862087738`;
- Master Plan consistency run: `29862087730`;
- retained artifact: `8507695005`;
- artifact digest: `sha256:4ea6bf77131834b48b9e35ad5eb88538a87b6f376f2be4984f077eb3eeed1267`;
- validation report SHA-256: `4a8cf20f3aacf8628c1de1b774cc93018705d0aa256a65208a8abf4311edc691`;
- regression result: 24 passed — one valid state and 23 adversarial mutations;
- exact changed-file boundary: 18 durable files;
- unresolved review threads: zero;
- candidate merge: `0a35a8a904bdf235fa4989ea05b684443d5a879a`.

## Accepted-state evidence

- accepted exact head: `a66fd9287117e5ed86ff4a7e4e1adad7641e1a8e`;
- AF01 accepted-closure run: `29863993585`;
- governing archive-protocol run: `29863993448`;
- Master Plan consistency run: `29863993643`;
- AF01 accepted artifact: `8508431848`;
- AF01 accepted artifact digest: `sha256:126a95406be9a12096d35eeaa30e2fb78b20d4b0f3c1cf26aa916d58e7479d4d`;
- AF01 accepted validation report SHA-256: `dd9d8f7387474f894bd978e0efce890c5605c5575b9a8c45d5647b8753bec1d6`;
- governing archive artifact: `8508434065`;
- governing archive artifact digest: `sha256:204ff360699ae151d5b80ee928c8c00a4f6377705cc16f1bbb71fb7c78593853`;
- governing validation report SHA-256: `29d1934ec532f76366c4beb632bfa7cde5fb9fa6fcb6142d6644cd5e7236de07`;
- AF01 regression result: 27 passed;
- governing archive regression result: 25 passed;
- operative AF01 acceptance merge: `ea2424bb5bc2bdb698bfc1bf389601457abd3c89`.

## Accepted formation result

- assigned records: 10;
- reconciled records: 10;
- accepted archive records: 9;
- completed blocked outcomes: 1;
- remaining evidence collection: 0;
- Primary Archivists: 10;
- Independent Verifiers: 10;
- durable checkpoints: 2.

Accepted archive records:

- `D001` OpenClaw;
- `D012` E2B;
- `D016` Playwright;
- `D020` DeviceFarmer STF with security restrictions;
- `D030` gVisor;
- `D035` BuildKit;
- `D042` RAGFlow;
- `D051` SparkDistill with rights/proof restrictions;
- `D058` Strix with offensive-security restrictions.

Completed blocked outcome:

- `D047` MiniRouter remains blocked for source reuse. Canonical identity is resolved, but the exact inspected source has no root `LICENSE`, package metadata declares no licence and adaptation lineage remains explicit. Research may continue without copying or adapting source.

## Subsequent formation state

AF02 was started only after AF01 acceptance merged:

```text
AF01: ACCEPTED COMPLETE
AF02: ACCEPTED COMPLETE
AF02 candidate merge: 58d89dfd1d5348cc8423222e3aff256ee041dce2
AF03: READY / NOT STARTED
```

AF02 acceptance does not grant dependency adoption, alter P01 implementation authorization work or start AF03.

## Preserved boundaries

- archive acceptance does not adopt donors as Ptah architecture authority;
- Phase 0A remains frozen;
- WP01–WP14 remain unchanged;
- P01 physical-host closure remains active;
- ADR-0033 remains proposed;
- runtime implementation remains unauthorized;
- AF03 is not started.
