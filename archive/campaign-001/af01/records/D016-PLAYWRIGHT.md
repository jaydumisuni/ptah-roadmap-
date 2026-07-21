# D016 — Playwright Archive Record

Outcome: ACCEPTED FOR ARCHIVE — Browser Facility donor; no semantic-truth or runtime-authorization claim

Campaign: `CAMPAIGN-001`

Formation: `AF01`

Primary Archivist: `AF01-P03`

Independent Verifier: `AF01-V03`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `microsoft/playwright`;
- owner: Microsoft organization;
- visibility: public;
- archived: false;
- default branch: `main`;
- inspected commit: `129717a626d6ff1c870b19f285db7771f3b33a59`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `df112373eb2e23e459bf93ec412be1764dc5a38b`;
- browser binaries and third-party components remain subject to their own notices/distribution terms;
- activity state: active; the inspected repository identifies version `1.62.0-next` and maintains broad browser, Android, Electron, MCP, installation, stress and test-runner suites.

## Primary evidence packet — AF01-P03

Inspected:

- root `package.json` blob `cd2015d4faa7dc9e30725b74078e570b015e6ebb`;
- `packages/playwright-core/src/server/browserType.ts` blob `bed4f1d3e86a4d075d2d3312812b3afe324433f7`;
- root `LICENSE`;
- exact current head.

Verified:

- repository purpose is a high-level API for browser automation;
- root engine requirement is Node.js 20 or newer;
- tests are partitioned across Chromium, Firefox, WebKit, Android, Electron, installation, stress, BiDi, MCP and Playwright Test;
- `BrowserType` validates launch options, creates isolated/persistent user-data directories, launches browser processes, records downloads/traces/artifacts, supports proxy/client-certificate handling and cleans up failed launches;
- browser connections use explicit transports and browser-specific registries;
- persistent browser contexts and custom executable paths are supported with explicit lifecycle behavior.

Primary conclusion:

Playwright remains a foundation-grade Browser Facility donor for launch, context, transport, artifact, download, trace and automation behavior. It cannot by itself establish semantic correctness, policy authority, user intent, Activity truth, durable recovery or generalized desktop automation.

## Independent verification packet — AF01-V03

Repeated checks:

- canonical identity, `main` branch and exact inspected head;
- Apache-2.0 root licence;
- actual server-side launch path rather than API documentation alone;
- broad executable test matrix;
- process, context, transport and artifact boundaries.

Challenges retained:

- Playwright-managed browser binaries and browser-specific notices need separate implementation review;
- browser automation success is not proof that an intended business result occurred;
- selectors, DOM state and screenshots are evidence inputs, not canonical Ptah Object or Activity truth;
- persistent contexts contain sensitive state and require Ptah-specific retention/deletion policy;
- remote/custom browser processes may weaken assumptions and require explicit capability/receipt evidence.

Verifier conclusion: primary findings supported. No contradiction with WP08/ADR-0011 placement.

## Ptah relationship

- frozen donor group: Browser and live research;
- current classification: direct dependency or wrapped Browser Facility candidate under the accepted Browser contract;
- requirements supported: interactive/headless browser launch, persistent contexts, transport, downloads, traces, artifacts and browser-family testing;
- prohibited inheritance: DOM/selector state as universal semantic truth, Playwright process identity as Ptah Activity identity, browser success as final proof, unrestricted persistent-profile retention;
- replacement/exit strategy: maintain provider-neutral Browser contracts and keep Playwright-specific lifecycle behind an adapter.

## Contradiction and supersession

- no canonical-identity contradiction found;
- current source confirms the frozen `microsoft/playwright` placement;
- current version/test/source evidence supersedes old unpinned assumptions without changing the accepted Browser architecture.

## Bounded outcome

`accepted for archive` retains a trustworthy source account. It does not select a final package pin for implementation, authorize browser-binary distribution, reopen Phase 0A, accept ADR-0033 or authorize Ptah runtime implementation.
