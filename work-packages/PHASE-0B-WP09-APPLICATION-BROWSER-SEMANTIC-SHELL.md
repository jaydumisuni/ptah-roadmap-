# Phase 0B WP09 — Application, Browser, Semantic UI and Human Shell

**Status:** CANDIDATE PACKAGE — FINAL CONSISTENCY REVIEW INCLUDED  
**Date:** 2026-07-19  
**Catalog:** `urn:ptah:schema-catalog:application:0.1.0`  
**Implementation authorization:** NONE

## Objective

Turn the frozen Application, Browser, semantic UI and human Workspace Shell architecture into exact backend-neutral contracts that later implementation teams can build without inventing identity, control, stale-target, recovery, privacy, accessibility or presentation/runtime boundaries.

## Accepted candidate boundary

1. Application, immutable Revision, Compatibility, Installation, Session, Process, Window, Display, Checkpoint and Recovery Verification remain separate.
2. Paths, package/bundle IDs, PIDs, window/surface handles and backend sessions remain scoped Aliases.
3. `runtime.process` remains canonical Process identity; Application/Browser records project or bind it.
4. install/uninstall acknowledgement, Window visibility, pixel streaming and functional readiness are distinct proof claims.
5. optional display or semantic loss degrades only affected scope.
6. Application/Browser checkpoint integrity and compatibility do not prove functional recovery; new generations require Recovery Verification.
7. Browser Binary/Profile may persist across Process/Context/Page generations.
8. writable Profile sharing is controlled by canonical `runtime.lease` and fencing; mutually untrusted Workspaces cannot share a writer.
9. Context isolation, storage, network and permission policy are explicit.
10. Page, Frame, Popup, Navigation, Download, Challenge and Evidence remain distinct; backend target IDs and URLs are not identity.
11. Browser downloads enter WP06 Transfer and WP03 Content/Object truth before verified completion.
12. restored cookies/profile bytes do not prove current authentication.
13. Semantic Context, Snapshot, Node, Event, Selector, Target, Target Result, Action, Attempt, Result and Visual Evidence remain separate.
14. a Selector is durable, while Target Result is fresh, generation-bound and invalidated by events/drift.
15. ambiguous or stale targets block mutation; reacquisition is mandatory.
16. every Action Attempt binds current Context/Snapshot/Target Result/Provider generation/control Lease/fence and a new WP02 Attempt.
17. provider ACK is not verified Action Result; fresh post-condition evidence is required.
18. fallback methods and reduced assurance are explicit; hidden coordinate/keyboard fallback is prohibited.
19. Shell Client, Session, Panel Type, Panel, Binding, Layout, View State, Projection, responsive projection, Client Observation and Control Transfer remain separate.
20. Shell presentation does not become runtime truth. Disconnect/panel closure/mobile backgrounding does not stop work.
21. responsive phone/tablet views derive from immutable Layout Revision without mutating desktop/global layout.
22. human/automation control transfer quiesces and fences old authority before issuing a new canonical Lease/fence.
23. accessibility, localization, safe-area and low-bandwidth behavior are conformance requirements.
24. profiles, cookies, clipboard, semantic text, screenshots, traces and client caches carry explicit privacy/redaction/retention policy.
25. backend replacement preserves stable public identity and creates new compatibility, Provider bindings, generations, snapshots and Attempts.
26. blocked, stale, ambiguous, challenged, failed and inconclusive outcomes remain immutable evidence.

## Candidate outputs

- normative WP09 conventions and entity-kind supplement;
- shared definitions;
- 51-schema offline catalog;
- 18 namespaced lifecycle machines;
- cross-machine invariants;
- directional migration and replacement rules;
- 92-case positive/negative/adversarial scenario corpus;
- consolidated safety net;
- final consistency review;
- ADR-0026.

## Catalog inventory

### Application family

- Application, Revision, Compatibility, Installation, Session;
- Window and Window Observation;
- Display Session and Display Observation;
- Application Checkpoint and Recovery Verification;
- canonical `runtime.process` reused.

### Browser family

- Binary and Binary Revision;
- Profile and Profile Revision;
- Process, Context, Page, Frame and Popup;
- Navigation, Download, Challenge and Challenge State;
- Browser Checkpoint, Recovery Verification and Evidence Bundle.

### Semantic UI family

- Context, Snapshot, Node Snapshot and Event;
- Selector, Target and Target Result;
- Action, Action Attempt, Action Result and Visual Evidence.

### Shell family

- Client, Session and Client Observation;
- Panel Type, Panel and Panel Binding;
- Layout Profile, Layout Revision and View State;
- Projection and responsive projection;
- Control Transfer using canonical `runtime.lease`.

## Required closure proofs

WP09 cannot close unless review confirms:

- 51 schema URNs and 18 lifecycle names are unique and resolve offline;
- every registered WP09 kind has one schema or explicit cross-package reuse;
- no Process/Lease/checkpoint/transfer/Object identity is duplicated;
- all generation, stale-target, control-fence, ACK/post-condition and recovery boundaries are represented;
- profile/cookie/clipboard/text/screenshot/trace privacy is explicit;
- accessibility and responsive behavior are represented in schemas and fixtures;
- the 92-case scenario suite covers Application, Browser, semantic UI, Shell, privacy, accessibility and backend replacement;
- ADR-0026 is accepted only after the final consistency review.

## Deferred implementation choices

This package does not select:

- native process/application runner or package manager;
- Playwright, CDP, WebDriver, Browser-Use or other browser backend;
- browser binary/profile pool implementation;
- RDP, VNC, Wayland, X11, WebRTC or other display backend;
- Appium, accessibility, DOM, platform UI or computer-vision semantic provider;
- editor/workbench/UI framework;
- production shell transport or state store.

Those choices occur after Phase 0C and must map to these contracts.

## Build-readiness consequence

Once accepted, implementation teams can add adapters by mapping backend IDs to Aliases, emitting exact Ptah records, respecting generations/Leases/fences, and satisfying the fixed proof suite. They must not redesign Application readiness, Browser profile isolation, semantic targeting/action verification, human takeover or Shell presentation/runtime boundaries during implementation.
