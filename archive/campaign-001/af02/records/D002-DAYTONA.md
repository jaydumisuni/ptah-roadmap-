# D002 — Daytona Archive Record

Outcome: ACCEPTED FOR ARCHIVE WITH DISCONTINUATION/COPELEFT RESTRICTIONS — historical public sandbox donor only

Campaign: `CAMPAIGN-001`

Formation: `AF02`

Primary Archivist: `AF02-P03`

Independent Verifier: `AF02-V03`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `daytonaio/daytona`;
- owner: Daytona organization;
- visibility: public;
- archived flag: false;
- default branch: `main`;
- inspected commit: `ec4c21b2d597091ac09ecc278f3bcc172575a987`;
- reusable public snapshot referenced by current README: `v0.190.0`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- current root `LICENSE` file: absent at inspected `main` head;
- current README states core development moved to a private codebase in June 2026 and the public repository will receive no further updates, fixes or releases;
- the README directs public reuse to the `v0.190.0` snapshot;
- `v0.190.0` root licence: GNU Affero General Public License v3.0;
- network-service modification/deployment can trigger AGPL source-availability obligations;
- hosted Daytona services, current private code, SDK/package releases, images and third-party components are not automatically covered by the archived public snapshot licence;
- maintenance state: discontinued public core despite repository archived flag being false.

## Primary evidence packet — AF02-P03

Inspected:

- current `README.md` blob `b1f7aec5eb644b2735ac0106e6a43a0933656f49`;
- attempted current root `LICENSE` retrieval: `404 Not Found`;
- `LICENSE` at tag `v0.190.0`, blob `bae94e189e62df1b8d5bd11435d954b25bee9d7b`;
- exact current head.

Verified:

- the historical platform describes isolated sandboxes, snapshots, volumes, process/code execution, filesystem/Git operations, PTY, VNC, SSH, network controls, audit logs and OpenTelemetry;
- architecture separates interface, control and compute planes;
- client libraries span Python, TypeScript, Ruby, Go and Java;
- normal current quick-start depends on a Daytona account/API key and hosted service;
- the public repository's advertised capabilities and current commercial service must not be conflated after the private-code transition;
- the public codebase is no longer maintained even though the repository metadata does not mark it archived.

Primary conclusion:

Daytona remains a valuable historical Workspace/sandbox architecture donor and compatibility/replacement study. The reusable public implementation is the frozen AGPL `v0.190.0` snapshot, not the current private service. It should not be selected as a new foundational source dependency without explicit copyleft, maintenance, security and replacement review.

## Independent verification packet — AF02-V03

Repeated checks:

- canonical identity and `main` default branch;
- exact current head;
- public-maintenance discontinuation notice dated June 2026;
- current root licence absence;
- explicit pointer to `v0.190.0`;
- AGPL-3.0 licence at that tag;
- hosted API-key dependency and plane/SDK descriptions.

Challenges retained:

- repository visibility and non-archived metadata do not imply active maintenance;
- current documentation may describe capabilities of a private/current platform beyond the frozen public snapshot;
- AGPL obligations are material for modified network-service deployment;
- a discontinued public security surface requires independent vulnerability and dependency review;
- service/API compatibility is not Ptah lifecycle, identity, Receipt or recovery compatibility.

Verifier conclusion: primary findings supported. The donor remains useful for architecture and historical behavior, with source reuse constrained to an exact licensed snapshot.

## Ptah relationship

- frozen donor group: core architecture and Workspace/sandbox donors;
- current classification: historical architecture study and optional compatibility workload;
- requirements supported: plane separation, sandbox lifecycle, snapshots, volumes, remote access, SDK/API surfaces and operational controls;
- prohibited inheritance: current private product claims as public-source proof, AGPL code without legal acceptance, discontinued dependencies as default foundation, Daytona identity as canonical Ptah Workspace identity;
- replacement/exit strategy: preserve native Ptah Workspace contracts and evaluate maintained providers independently.

## Contradiction and supersession

- earlier donor records treated Daytona as an active open-source platform;
- current primary evidence supersedes that maintenance assumption: public core development stopped in June 2026;
- the current canonical repository remains valid, but source reuse authority is bounded to `v0.190.0` and its AGPL-3.0 terms;
- no frozen Ptah architecture decision is reopened.

## Bounded outcome

`accepted for archive with discontinuation/copyleft restrictions` preserves the historical donor and current lifecycle boundary. It does not select Daytona, authorize AGPL deployment, accept current private-service claims as public-source proof, reopen Phase 0A, start AF03, accept ADR-0033 or authorize Ptah runtime implementation.
