# Archive Campaign 001 — Operative Acceptance Binding

Status: OPERATIVE ACCEPTANCE MERGE BOUND — RECOVERY CONTROL STATE

Recorded: 2026-07-24

## Candidate evidence

- exact AF04–AF10 candidate head: `6eed78a9acca4614d9dd99c175681ba4ff476c8e`;
- candidate workflow run: `30076705760`;
- retained candidate artifact: `8590135926`;
- candidate artifact digest: `sha256:c7e3a9be59b5ba859b67a1b352fee32b2c43c44e774e3e70b07aaac857d8b3a7`;
- candidate validation report SHA-256: `7a53cdccfb520cbc29dfb842b952dbcbca5800f02ed1ce2a67b8a3743180d247`;
- candidate evidence merge: `ec78db9ce5b44a5d05465a1cb6271c7e6594079e`.

## Accepted-state evidence

- exact accepted-state head: `03e027b5b2898b096652688157623ad31d3c16d7`;
- accepted-state workflow run: `30078410676`;
- retained accepted-state artifact: `8590777774`;
- accepted-state artifact digest: `sha256:9a9948862f7c8af5f6551a239a19091c2e37a5565442be0ff9c90459932a2398`;
- accepted-state validation report SHA-256: `f78ebcbe2781480ce90472b5d373cc282cb13628acc3e7dcc853f8abe6ebab7f`;
- operative acceptance merge: `f7280e4af1323096196ab0534e5f76b9375fd6d7`.

## Operative campaign state

- Campaign 001: `ACCEPTED COMPLETE`;
- formations: `10 of 10 accepted complete`;
- obligations: `98 of 98 closed`;
- accepted archive records: `91`;
- completed blocked outcomes: `7`;
- remaining evidence: `0`;
- AF11: does not exist.

The completed blocks are:

1. `D047` MiniRouter — source reuse blocked by unresolved licence/source boundary;
2. `D065` amertoglu16.github.io — canonical source and licence unavailable;
3. `I018` Qualcomm DIAG — exact engine source and licence unavailable;
4. `I008` TechGuy Installer — exact source and licence unavailable;
5. `I019` SPD/Unisoc — exact engine source and licence unavailable;
6. `I024` NETUNLOCKER — canonical repository mapping unavailable;
7. `I025` ZTE generator — exact source, algorithm and licence unavailable.

Each block is a completed archive outcome with retained evidence, a safe next action and an explicit prohibition on source reuse until its missing authority is recovered.

## Preserved authority

This binding accepts archive evidence only. It does not:

- reopen Phase 0A;
- adopt or integrate a donor;
- close P01;
- accept ADR-0033;
- authorize runtime implementation;
- approve a protected device, payment, installation, unlock, deployment or customer-impacting action.

P01 remains the active physical pinned-host work. ADR-0033 remains proposed. Runtime implementation remains `NOT AUTHORIZED`.

This file and `archive/campaign-001/OPERATIVE-STATE.json` are the durable recovery authority for Campaign 001 status and supersede earlier progress-only statements that AF04 was ready or not started.