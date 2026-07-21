# D013 — E2B Desktop Archive Record

Outcome: ACCEPTED FOR ARCHIVE — hosted desktop-sandbox adapter donor; no local-provider or computer-use proof claim

Campaign: `CAMPAIGN-001`

Formation: `AF02`

Primary Archivist: `AF02-P04`

Independent Verifier: `AF02-V04`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `e2b-dev/desktop`;
- owner: E2B organization;
- visibility: public;
- archived: false;
- default branch: `main`;
- inspected commit: `e4800ef873cacc0eeb91770a419b77de0ea26903`;
- inspected JavaScript package version: `@e2b/desktop` `2.3.1`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`;
- JavaScript package metadata declares MIT while the root repository licence is Apache-2.0; component packaging and notices must be reviewed per published artifact;
- E2B base service, sandbox images, desktop applications, streamed content and external agent/model examples retain separate terms;
- activity state: active; inspected head updates package dependencies.

## Primary evidence packet — AF02-P04

Inspected:

- `README.md` blob `a078507f84c874137f092cc4f3b3d4a51fd5cbe3`;
- root `package.json` blob `938108f6f1a0a4c8d5f818387f8f92779be71978`;
- `pnpm-workspace.yaml` blob `924b55f42e98721620a2206ca848eab030e6d887`;
- `packages/js-sdk/package.json` blob `9b6f3629dac4b36f282ab655ad53e37ebd4d3b26`;
- `packages/js-sdk/src/index.ts` blob `3e072a92444fc595f464abc3f788a2ffb827f411`;
- root `LICENSE`;
- exact current head.

Verified:

- repository provides Python and JavaScript SDKs for E2B-backed virtual desktops;
- normal operation requires an E2B account/API key and builds on E2B Sandbox;
- SDK examples create a sandbox, launch desktop applications, wait, stream desktop/application windows and optionally require a generated auth key;
- one stream at a time is supported, with application-specific streams closing when the application closes;
- view-only and password-protected streaming are exposed;
- the JavaScript package re-exports the base `e2b` SDK and adds a Desktop `Sandbox` class;
- package requires Node.js 20.18.1 or newer and includes test/lint/build scripts;
- root workspace is private packaging infrastructure, while published packages are separate components.

Primary conclusion:

E2B Desktop is a useful optional remote desktop/computer-use adapter donor. It extends hosted E2B lifecycle and streaming surfaces; it does not prove local/offline desktop virtualization, secure autonomous computer use, semantic UI correctness or Ptah Workspace/Activity identity.

## Independent verification packet — AF02-V04

Repeated checks:

- canonical identity, `main` branch and exact current head;
- root Apache-2.0 licence and package-level MIT declaration;
- actual package entry re-export and Desktop Sandbox addition;
- hosted API-key dependency;
- stream authentication/view-only controls and single-stream limitation;
- package/runtime requirements.

Challenges retained:

- streamed desktop URLs/auth keys are sensitive capability credentials;
- view-only mode and stream authentication do not prove tenant isolation or prevent application/data leakage;
- hosted service availability, billing and retention are external dependencies;
- application launch and visual interaction success are not business-result proof;
- root/package licence differences require artifact-specific notice review;
- E2B Desktop must not become a mandatory Ptah dependency or canonical identity source.

Verifier conclusion: primary findings supported. Placement as an optional Workspace/desktop provider adapter is correct.

## Ptah relationship

- frozen donor group: Workspace and sandbox donors;
- current classification: optional hosted desktop provider adapter;
- requirements supported: desktop sandbox creation, application launch, screen/application streaming, view-only access and auth-token patterns;
- prohibited inheritance: E2B account/API key as Ptah identity, stream URL as durable Object truth, computer-use success as semantic proof, hosted service as mandatory availability;
- replacement/exit strategy: retain provider-neutral Workspace/Desktop Facility contracts and keep E2B-specific lifecycle behind an adapter.

## Contradiction and supersession

- no canonical-identity contradiction found; the obligation resolves to `e2b-dev/desktop`;
- current source confirms this is a separate desktop layer on top of E2B, not the whole E2B infrastructure repository;
- package version/runtime evidence supersedes generic older descriptions without changing frozen Ptah architecture.

## Bounded outcome

`accepted for archive` does not select E2B Desktop as a default provider, authorize hosted credentials/data handling, certify computer-use behavior, reopen Phase 0A, start AF03, accept ADR-0033 or authorize Ptah runtime implementation.
