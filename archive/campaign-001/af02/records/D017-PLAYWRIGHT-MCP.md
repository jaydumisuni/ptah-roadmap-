# D017 — Playwright MCP Archive Record

Outcome: ACCEPTED FOR ARCHIVE — MCP/browser adapter donor; no model authority or semantic-proof claim

Campaign: `CAMPAIGN-001`

Formation: `AF02`

Primary Archivist: `AF02-P05`

Independent Verifier: `AF02-V05`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `microsoft/playwright-mcp`;
- owner: Microsoft organization;
- visibility: public;
- archived: false;
- default branch: `main`;
- inspected commit: `55679f5f3d4b4f3e2534ec0ce2fc5683ba2eaf3f`;
- inspected package version: `@playwright/mcp` `0.0.78`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root and package licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `cefe596afef12e19a8e5e923f1a04c7da3188760`;
- Playwright/browser binaries, MCP clients, container images and transitive dependencies retain separate notices and distribution requirements;
- activity state: active; inspected head updates documentation/devcontainer details while the package tracks Playwright alpha builds.

## Primary evidence packet — AF02-P05

Inspected:

- `README.md` blob `b670ed5915f64eb9e2a50e5730615322d659fc4d`;
- `package.json` blob `c74c4aeaf2f835ce674385d2585ae7f0430fbfe2`;
- `cli.js` blob `f07382bfd9adf81cbb65a852fda442c86f53bdcb`;
- root `LICENSE`;
- exact current head.

Verified:

- the project exposes Playwright through a Model Context Protocol server;
- primary interaction uses structured accessibility snapshots rather than requiring screenshots/vision models;
- package requires Node.js 18 or newer and publishes the `playwright-mcp` CLI;
- CLI delegates command construction and MCP decoration to Playwright Core bundles;
- package pins matching Playwright and Playwright Core alpha versions and tests across Chrome, Firefox, WebKit and Docker configurations;
- README explicitly distinguishes MCP from CLI/skills, noting MCP's richer state/introspection but greater schema/context cost;
- normal setup uses `npx @playwright/mcp@latest`, which is convenient but unpinned and inappropriate for reproducible authority evidence.

Primary conclusion:

Playwright MCP is a valid adapter and interoperability donor for exposing Browser Facility operations to MCP clients. It is not an independent browser engine, a semantic verifier, a policy authority or proof that an LLM correctly interpreted or completed a web task.

## Independent verification packet — AF02-V05

Repeated checks:

- canonical identity, `main` branch and exact current head;
- Apache-2.0 root/package licence;
- actual CLI delegates into Playwright Core MCP tooling;
- Node and Playwright version requirements;
- executable multi-browser/Docker test scripts;
- README's MCP-vs-CLI trade-off and accessibility-tree approach.

Challenges retained:

- accessibility snapshots can omit visual/layout information and are not universal semantic truth;
- MCP clients/models may misuse powerful browser actions without Ptah policy and scope enforcement;
- `@latest` installation is non-reproducible and must be replaced with exact package/browser pins;
- persistent browser context can hold sensitive credentials/session state;
- tool-call success is not business-result, security or content-correctness proof;
- MCP server identity and model context must not become Ptah Activity/Object authority.

Verifier conclusion: primary findings supported. The donor is an optional Browser/MCP adapter behind native Ptah contracts.

## Ptah relationship

- frozen donor group: Browser and live research donors;
- current classification: optional MCP Browser adapter;
- requirements supported: structured browser-tool exposure, persistent sessions, accessibility snapshots, multi-client configuration and adapter tests;
- prohibited inheritance: MCP/model output as final truth, unpinned latest packages, unrestricted browser authority, accessibility tree as complete page semantics;
- replacement/exit strategy: keep provider-neutral Browser Facility and tool contracts; support MCP, CLI or direct Playwright adapters independently.

## Contradiction and supersession

- no canonical-identity contradiction found;
- current source confirms the repository is a thin adapter over Playwright Core rather than a separate browser runtime;
- current README explicitly narrows MCP's best-fit use cases compared with CLI/skills, superseding assumptions that MCP is always the preferred interface;
- frozen Ptah Browser architecture remains unchanged.

## Bounded outcome

`accepted for archive` retains the adapter identity, licence, current package pin and limitations. It does not authorize `@latest`, grant a model browser authority, certify task success, reopen Phase 0A, start AF03, accept ADR-0033 or authorize Ptah runtime implementation.
