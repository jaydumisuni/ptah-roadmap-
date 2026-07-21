# D001 — OpenClaw Archive Record

Outcome: ACCEPTED FOR ARCHIVE — architecture/behavior donor only; no adoption or runtime authorization

Campaign: `CAMPAIGN-001`

Formation: `AF01`

Primary Archivist: `AF01-P01`

Independent Verifier: `AF01-V01`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `openclaw/openclaw`;
- owner: OpenClaw organization/Foundation;
- visibility: public;
- archived: false;
- default branch: `main`;
- inspected commit: `4400f4ca91b2a58096353197337427d824856963`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: MIT;
- root licence evidence: `LICENSE` blob `ebaebf7c416761a32f932ad70ebe5d1d2e214f68`;
- incorporated-code notice: `THIRD_PARTY_NOTICES.md` blob `6b6721901b7590d20774ba0504d975e1be70a57a`;
- the notice records adapted Pi/pi-mono material and an MIT terminal-UI dependency;
- dependency and generated-package rights remain a later implementation review obligation;
- activity state: actively changing at the inspected head; the inspected commit includes source, tests and documentation changes for cron-list behavior.

## Primary evidence packet — AF01-P01

Inspected:

- `package.json` blob `acefdca0470182204eb0003fee31e0a8a7a939bb`;
- `openclaw.mjs` blob `2e3fbaf2849b614f9eb57a2105f67cf21b1a28d3`;
- `LICENSE`;
- `THIRD_PARTY_NOTICES.md`;
- exact head commit and changed-file evidence.

Verified:

- package identity `openclaw`, version `2026.7.2` at the inspected commit;
- declared purpose: multi-channel AI gateway with extensible messaging integrations;
- CLI entry point: `openclaw.mjs`;
- source and packaged runtime are distinct paths;
- the launcher enforces supported Node.js versions and rejects Bun runtime execution because it requires `node:sqlite`;
- packaged output includes gateway, provider, plugin, memory, browser, scheduling, concurrency, delivery and test-contract surfaces;
- repository contains a large test surface and the inspected head includes a regression test for disabled cron-job listing.

Primary conclusion:

OpenClaw remains a valid architecture and behavior donor for gateway, plugin, provider, scheduling, delivery and operational lifecycle patterns. It is not evidence that Ptah should inherit OpenClaw's object model, state authority, global scheduling authority or runtime wholesale.

## Independent verification packet — AF01-V01

Repeated checks:

- canonical owner/repository and `main` default branch;
- exact inspected head;
- MIT root licence;
- incorporated-code notice;
- actual executable entry point and runtime-version guard;
- exact head includes executable tests rather than documentation-only changes.

Challenges retained:

- repository size and rapid change make unpinned conclusions unsafe;
- root MIT licensing does not remove dependency/component review obligations;
- Node runtime and local state assumptions are implementation constraints, not Ptah requirements;
- OpenClaw's gateway and agent concepts must not become Ptah authority merely because names overlap.

Verifier conclusion: primary findings supported. No contradiction with the frozen donor register.

## Ptah relationship

- frozen donor group: Relay, Nodes, Activities and control plane;
- current classification: architecture study plus selective behavior-pattern donor;
- requirements supported: gateway/channel routing, provider/plugin lifecycle, scheduling/recovery patterns and operational test ideas;
- prohibited inheritance: donor identity model as Ptah Core, global scheduler authority, unreviewed state layout, unrestricted plugin trust, generated/provider claims as proof;
- replacement/exit strategy: implement native Ptah contracts and keep OpenClaw-specific behavior behind adapters or research workloads.

## Contradiction and supersession

- no canonical-identity contradiction found;
- current source confirms the frozen register's `openclaw/openclaw` identity;
- the current repository is materially newer than early donor summaries, so this commit supersedes unpinned version assumptions while leaving frozen Ptah decisions unchanged.

## Bounded outcome

`accepted for archive` means this record is a trustworthy retained account of the inspected source. It does not adopt OpenClaw, authorize code reuse, reopen Phase 0A, change WP01–WP14, accept ADR-0033 or authorize Ptah runtime implementation.
