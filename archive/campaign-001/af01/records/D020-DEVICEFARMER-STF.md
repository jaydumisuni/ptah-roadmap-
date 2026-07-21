# D020 — DeviceFarmer STF Archive Record

Outcome: ACCEPTED FOR ARCHIVE WITH SECURITY RESTRICTIONS — architecture/workload donor only

Campaign: `CAMPAIGN-001`

Formation: `AF01`

Primary Archivist: `AF01-P04`

Independent Verifier: `AF01-V04`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `DeviceFarmer/stf`;
- owner: DeviceFarmer organization;
- visibility: public;
- archived: false;
- default branch: `master`;
- inspected commit: `36d1a3e4336f2ecdf7885e3644fe34d0a4282c87`;
- inspected release/package state: `3.7.9`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `84a051656676c80db4eac4960d7b0987ef3b2e2f`;
- package licence declaration: Apache-2.0;
- dependency/component review remains required, especially bundled/prebuilt Android tooling and old web/runtime dependencies;
- activity state: maintained but slow by the project's own status statement; inspected head is a version bump to `3.7.9`.

## Primary evidence packet — AF01-P04

Inspected:

- `README.md` blob `56c1ef46d8eb968f62b2c4e90762552c7350be7a`;
- `package.json` blob `cab60fdde8c726f2330f872544b270e13de1bf45`;
- `lib/cli/index.js` blob `ff9f3b1c39b8271de12802ff0f27838a85269915`;
- root `LICENSE`;
- exact current head.

Verified:

- STF is a browser-accessible remote smartphone/device farm;
- it supports Android remote screen/control, keyboard/touch, APK installation, shell/log access, remote ADB, device inventory and booking/partitioning;
- the CLI launches many independent services, including API, app, auth, device, provider, processor, storage, proxy and websocket processes;
- the package depends on ADBKit, minicap/minitouch, RethinkDB, ZeroMQ, Express, Socket.IO and many older Node/web dependencies;
- current documentation limits Node.js to 20.x because some dependencies do not support newer versions;
- Windows production installation is not supported by the project;
- the repository explicitly warns that there is little to no security/encryption between internal processes and that devices are not fully reset between users.

Primary conclusion:

STF is a useful Android-device-farm architecture and optional workload donor. Its device inventory, remote-control, booking and process decomposition patterns remain valuable. Its internal trust model, incomplete device reset and multi-process security assumptions must not be inherited for customer, technician or hostile multi-user use.

## Independent verification packet — AF01-V04

Repeated checks:

- canonical identity, `master` branch and exact inspected head;
- Apache-2.0 root/package licence;
- real CLI service composition;
- Android/remote-device capabilities;
- explicit security, reset and deployment limitations;
- dependency/runtime age and platform requirements.

Challenges retained:

- the project's own security warning blocks treating STF as a safe multi-tenant default;
- IMEI, account, logs, files and device-control surfaces are sensitive and require Ptah policy, audit and isolation;
- remote ADB access is powerful and cannot be exposed without explicit authorization and Receipts;
- STF's RethinkDB and service topology are donor implementation choices, not Ptah architecture requirements;
- support claims across Android versions do not replace physical-device proof for Ptah.

Verifier conclusion: primary findings supported. The frozen Android donor placement remains correct with stronger security restrictions.

## Ptah relationship

- frozen donor group: Android and physical devices;
- current classification: architecture study plus optional workload/adapter donor;
- requirements supported: device discovery/inventory, remote screen/input, ADB bridge, booking/partitioning, multi-process device service patterns;
- prohibited inheritance: internal-network trust assumptions, incomplete reset, weak inter-process security, donor database identity as Ptah truth, unrestricted ADB/device access;
- replacement/exit strategy: keep native Ptah Device/Activity/authority/Receipt contracts and use only selected adapters or an isolated workload.

## Contradiction and supersession

- no canonical-identity contradiction found;
- current `master` branch and package `3.7.9` supersede generic branch/version assumptions;
- current source confirms rather than removes the known security risk, so the restriction is retained as first-class archive evidence.

## Bounded outcome

`accepted for archive with security restrictions` does not approve STF deployment, source reuse, multi-user exposure or device access. It does not reopen Phase 0A, change WP07A, accept ADR-0033 or authorize runtime implementation.
