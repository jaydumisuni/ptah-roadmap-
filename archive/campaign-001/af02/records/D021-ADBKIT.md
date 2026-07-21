# D021 — ADBKit Archive Record

Outcome: ACCEPTED FOR ARCHIVE WITH DEVICE-AUTHORITY RESTRICTIONS — ADB client donor only

Campaign: `CAMPAIGN-001`

Formation: `AF02`

Primary Archivist: `AF02-P06`

Independent Verifier: `AF02-V06`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `DeviceFarmer/adbkit`;
- owner: DeviceFarmer organization;
- visibility: public;
- archived: false;
- default branch: `master`;
- inspected commit: `f474b57f6b1b1b41edd4abbfa1dd9bfad6420d6a`;
- inspected package: `@devicefarmer/adbkit` version `3.3.9`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root/package licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `ff328e27c624b3eac95bcdaef52c9f6454db46ed`;
- package dependencies include separate DeviceFarmer logcat/monkey packages and third-party Node libraries requiring transitive review;
- Android platform tools/ADB binary are external components with their own distribution and update obligations;
- activity state: maintained; inspected head bumps package version from 3.3.8 to 3.3.9.

## Primary evidence packet — AF02-P06

Inspected:

- `README.md` blob `71981982f5760a593115dcd90bd7f6598dd8749c`;
- `package.json` blob `24a7cb4c970823c6cfa47832bd37952f4f9972f9`;
- root `LICENSE`;
- exact current head.

Verified:

- ADBKit is a TypeScript/Node client for an existing Android Debug Bridge server;
- it is explicitly not an ADB server implementation;
- local connection may invoke the `adb` binary only to start a missing local server;
- remote server startup remains the operator's responsibility;
- supported surfaces include device listing/tracking, install, push/pull, filesystem, shell/logcat, screenshots, input events and key parsing;
- package exposes both a library and `adbkit` CLI, compiles TypeScript and runs Mocha tests;
- default ADB server endpoint is loopback port 5037 but remote hosts are supported;
- README claims broad device use but does not promise exhaustive vendor/version correctness.

Primary conclusion:

ADBKit remains a useful protocol/client donor and optional adapter for Android device Activities. It cannot grant device authorization, replace the platform ADB server, prove device ownership, normalize vendor behavior or turn command success into a valid service outcome.

## Independent verification packet — AF02-V06

Repeated checks:

- canonical identity, `master` branch and exact current head;
- Apache-2.0 root/package licence;
- package version, entry points, dependencies, compile/test scripts;
- explicit “not an ADB server” boundary;
- local/remote ADB server responsibility and broad device-control capabilities.

Challenges retained:

- ADB access is a sensitive control capability requiring explicit device/customer authorization;
- remote ADB may expose unencrypted or weakly protected transport depending on deployment;
- install, shell, pull/push, input and screenshot operations require policy, scope and Receipts;
- device identifiers, logs and filesystem contents are sensitive data;
- legacy Node engine metadata and broad Android claims require current runtime/physical-device testing;
- ADBKit success cannot replace vendor-specific evidence or Ptah Device/Activity identity.

Verifier conclusion: primary findings supported. ADBKit is an adapter/protocol donor behind Ptah authorization and audit boundaries.

## Ptah relationship

- frozen donor group: Android and physical-device donors;
- current classification: optional direct client dependency or wrapped ADB adapter;
- requirements supported: device discovery/tracking, install, shell, file transfer, logcat, screenshots, input and remote-server connection patterns;
- prohibited inheritance: ADB reachability as authorization, device serial as universal identity, command completion as final proof, unrestricted remote ADB;
- replacement/exit strategy: preserve native Ptah Device/Activity/Receipt contracts and permit alternative platform-tools or protocol adapters.

## Contradiction and supersession

- historical identity under OpenSTF is superseded by current canonical `DeviceFarmer/adbkit` ownership and package namespace;
- current source confirms active TypeScript packaging rather than the older pure-JavaScript description;
- the project still remains a client, not an ADB server or full device-farm architecture;
- frozen Ptah Android architecture is unchanged.

## Bounded outcome

`accepted for archive with device-authority restrictions` does not authorize connection to any device, remote ADB exposure, package adoption, customer-data access, Phase 0A reopening, AF03 start, ADR-0033 acceptance or Ptah runtime implementation.
