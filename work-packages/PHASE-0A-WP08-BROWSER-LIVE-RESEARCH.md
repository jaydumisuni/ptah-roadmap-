# Phase 0A — WP08 Browser and Live Research Composition

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-17  
**Runtime code:** NOT STARTED

## Purpose

Close Ptah's persistent browser, isolated Context, Page/Tab, rendered retrieval, downloads, evidence, authenticated profile and source-grounded live-research boundaries without embedding caller reasoning or agent identity into Ptah Core.

## Sources inspected and saved

### External/upstream

- Playwright
- Playwright MCP
- Browser-Use
- TurboWebFetch

### Internal

- Lumi browser/download handoff requirements
- Hunter credential, degradation, Activity/receipt and bridge rules
- existing Ptah Workspace, Application, Transfer, Object and provenance contracts

Saved records:

- `donors/PLAYWRIGHT.md`
- `donors/PLAYWRIGHT-MCP.md`
- `donors/BROWSER-USE.md`
- `donors/TURBOWEBFETCH.md`
- `internal/BROWSER-LIVE-RESEARCH-FOUNDATIONS.md`

## Canonical URL resolution

TurboWebFetch is resolved:

- canonical repository: `https://github.com/aza-ali/turbowebfetch`
- pinned commit: `fa18a9f9db1e1640ff6111176ec49aa88ea211f4`
- package version: `1.1.0`
- licence: MIT

It is no longer an unresolved donor.

## Composite result

```text
Ptah Browser Provider
  supervises binaries, processes, pools, local paths and resources

Ptah Browser Binary
  engine/product/version/build/platform identity

Ptah Browser Profile
  durable encrypted cookies/storage/extensions/authentication state

Ptah Browser Process
  one supervised browser backend generation

Ptah Browser Context
  isolated ephemeral, persistent, cloned or attached session

Ptah Page/Tab, Frame and Popup
  stable Ptah identities plus backend aliases/navigation epochs

Playwright
  primary process/context/page/action/download/evidence foundation

Playwright MCP
  optional external accessibility-snapshot adapter

Browser-Use
  profile reuse/cloning, persistent-loop, trajectory and scaling donor
  agent/reasoning layer excluded

TurboWebFetch
  rendered single/batch retrieval contract and extraction donor
  process-per-fetch architecture replaced by Ptah pools

Ptah Transfer/Object
  download landing, verification and finalization

Ptah Browser Evidence
  source response, DOM, accessibility, pixels, trace, video,
  console, network and storage snapshots as separate Views/Artifacts

Ptah Live Research Result
  source and citation records for external callers/reasoning systems
```

## Accepted architecture

Saved as `decisions/ADR-0011-BROWSER-PROFILE-CONTEXT-PAGE-EVIDENCE-BOUNDARY.md`.

Key decisions:

1. Browser Provider, Binary, Profile, Process, Context, Page, Frame, Popup, Download and Evidence remain separate identities.
2. Playwright is the primary Browser Facility foundation.
3. mutable Browser Profiles require exclusive lease, encryption and scoped ownership.
4. ephemeral Contexts may share a supervised process only after isolation conformance.
5. profile cloning excludes transient lock/journal files and creates a new identity/provenance chain.
6. existing personal-browser attachment requires explicit caller consent.
7. page navigation/process restart advances generation and invalidates stale locators/frames.
8. response source, raw HTML, rendered DOM, accessibility, visible text, screenshot, video, trace, console and network are separate Views.
9. browser downloads enter the existing Transfer/Object pipeline.
10. TurboWebFetch is adapted as batch rendered retrieval over pooled Contexts rather than process-per-fetch.
11. Playwright MCP is an external adapter, not Ptah's internal object model.
12. Browser-Use may run as a caller/workload; its reasoning, memory, prompts and model providers are excluded from Ptah Core.
13. live research results are claims linked to exact sources/captures, not accepted conclusions.
14. MFA, CAPTCHA, passkey, restricted access and human completion are explicit states.
15. Ptah does not claim bypass authority or permission to circumvent access controls.
16. browser crash recovery preserves safe evidence/partial results and never blindly replays non-idempotent actions.
17. browser/CDP/MCP endpoints, cookies and storage state remain protected.

## Requirement closure verdict

Closed for Phase 0B contract design:

- `BROWSE-001` Persistent interactive browser;
- `BROWSE-002` rendered extraction and live research;
- `BROWSE-003` Browser evidence;
- Browser Profile/Context/Page portions of `SESSION-001`;
- browser-panel/tab/download portions of `UI-001` and `UI-002`;
- browser download portions of `XFER-002`;
- browser trace/network/console/screenshot/video portions of `OBS-001` and `PROV-001`;
- Browser Facility portions of `CORE-004`, `CORE-005`, `OFFLINE-001` and `DIST-001`.

## Phase 0B contracts required

1. Browser Provider and binary/version capability schema.
2. Browser Profile ownership, encryption, lease and clone schema.
3. Browser Process and resource-pool schema.
4. Context types and isolation capability schema.
5. Page/Tab, Frame, Popup and navigation-epoch schemas.
6. normalized locator/selector intent and stale-reference rules.
7. navigation/action state and proof schema.
8. Download handoff and Object finalization schema.
9. Browser View and Evidence Artifact schemas.
10. Rendered Retrieval request/result and partial-batch schema.
11. Live Research Source/Claim/Citation schemas.
12. authentication/challenge/human-handoff schema.
13. profile/browser credential and privacy classes.
14. process/context/page crash/reconnect behavior.
15. MCP/CLI/SDK/UI adapter mappings.
16. cross-browser and isolation conformance suites.

## Validation set

- concurrent isolated Contexts without data leakage;
- persistent authenticated Profile lease/restart;
- safe Profile clone;
- browser crash and stale-reference rejection;
- no blind replay of non-idempotent actions;
- batch rendered retrieval with partial failures;
- source/DOM/accessibility/pixel/evidence comparison;
- browser download through Transfer/Object verification;
- human challenge handoff and resume;
- exact source/citation records;
- native SDK and MCP access without cross-Workspace leakage;
- backend/adapter replacement without identity changes.

## Next Phase 0A group

Proceed with **WP09 — Human Workspace Shell and Operator Interface Composition**:

- Theia;
- OpenVSCode Server or Code-Server as optional compatibility paths;
- internal Hunter/Foreman/Sergeant/website/device/tool interfaces;
- Ptah Home, Workspace switcher and Object views;
- multi-terminal, browser, Device and Application panels;
- Activity Centre and evidence/proof views;
- direct-human and automation coexistence;
- responsive desktop/mobile/browser UI;
- reconnect, degraded-capability and honest status presentation;
- public-safe project documentation and operator guides.
