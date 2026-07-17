# Phase 0A — WP09 Human Workspace Shell and Operator Interface Composition

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Runtime code:** NOT STARTED

## Purpose

Close Ptah's direct-human Workspace, panel/layout, Activity Centre, evidence view, responsive presentation and human/automation control boundaries without making a stock IDE or specialist product the universal shell.

## Sources inspected and saved

### External/upstream

- Eclipse Theia
- OpenVSCode Server
- code-server
- xterm.js
- Dockview

### Internal

- Hunter current UI/auth/mobile-rebuild sources
- Sergeant Command Center sources
- MIBU guided workflow sources
- THETECHGUY Device Manager interface record
- THETECHGUY website build/responsive-fix sources

Hunter Foreman is excluded from active WP09 reuse unless the owner explicitly brings it back.

Saved records:

- `donors/ECLIPSE-THEIA.md`
- `donors/OPENVSCODE-CODE-SERVER.md`
- `donors/XTERMJS.md`
- `donors/DOCKVIEW.md`
- `internal/UI-FOUNDATIONS.md`

## Composite result

```text
Ptah Shell Client
  replaceable Theia, responsive web, native, mobile or presentation client

Ptah Shell Session
  caller, selected Workspace, layout and current panel/focus state

Ptah Panel Type and Panel Instance
  stable identities bound to Objects, Activities, terminals, Browsers,
  Devices, Applications and evidence

Ptah Layout Profile and Revision
  desktop, tablet, phone, kiosk and custom logical layouts

Eclipse Theia
  primary full desktop/workbench framework

Dockview
  primary lighter responsive/wide-screen layout candidate

OpenVSCode Server / code-server
  optional coding-focused compatibility Applications

xterm.js
  primary browser terminal renderer over Ptah PTY streams

Internal UI patterns
  honest status, evidence, guided workflow, maintenance/degraded state,
  mobile reachability and manual handoff

Ptah Activity Centre
  concurrent Activity status, controls, resources, Objects and proof

Ptah Evidence Explorer
  receipts, source Objects, Artifacts, disagreements and limitations

Ptah Control Lease
  fenced human/automation input ownership and takeover/return
```

No shell framework or specialist UI is canonical Ptah runtime truth.

## Accepted architecture

Saved as `decisions/ADR-0012-HUMAN-WORKSPACE-SHELL-PANEL-CONTROL-BOUNDARY.md`.

Key decisions:

1. Shell Client, Shell Session, Panel Type, Panel Instance, Layout Profile, Layout Revision and control ownership are separate identities.
2. Eclipse Theia is the primary full desktop/workbench foundation, not the universal phone shell or Ptah Core.
3. Dockview is the primary lighter layout candidate on wide screens.
4. Phone presentation uses one primary panel, compact switching, drawers and Activity status rather than arbitrary docking.
5. OpenVSCode Server and code-server are optional coding Applications/Providers, not Ptah Home or Activity Centre.
6. xterm.js is the terminal renderer; Ptah's PTY Facility owns process, streams, replay and logs.
7. Panel state/layout restoration never implies underlying runtime Session recovery.
8. The Activity Centre projects live Activity Ledger/Event/Receipt state across unrelated concurrent work.
9. Planned, configured, available, connected, queued, running, waiting, recovering, completed, verified and accepted remain separate labels.
10. Evidence/proof is inspectable independently from progress and completion.
11. Settings is separate from live operational controls.
12. Human and automation may observe together, but controlled input uses scoped leases and fencing tokens.
13. Human takeover and return are explicit receipted transitions.
14. UI contributions call scoped Ptah Facilities rather than accessing host files/processes/credentials directly.
15. Desktop, tablet and phone clients share stable Panel/Layout records but use different projections.
16. Accessibility, keyboard, touch, safe-area, reduced-motion and low-resource behavior are first-class requirements.
17. Specialist UIs remain products/clients and are not replaced merely because Ptah gains a shared shell.
18. Runtime patch-injection and preview values are architecture debt, not accepted shell foundations.

## Requirement closure verdict

Closed for Phase 0B contract design:

- `UI-001` Human Workspace shell;
- `UI-002` Activity Centre, evidence and review interface;
- Human Workspace portions of `SESSION-001`;
- shell/panel contribution portions of `CORE-004`;
- direct-human projections of `OBS-001` and `PROV-001`;
- human-control/focus projections of Device, Application, Browser and terminal Sessions;
- responsive/mobile operator-interface requirements.

Still open elsewhere:

- final knowledge/search/data panels depend on WP10 contracts;
- distributed/placement/operator views depend on remaining scheduler/network closure;
- Linux AT-SPI semantic automation remains a platform-specific gap;
- public documentation portal remains in the later documentation/source cluster.

## Phase 0B contracts required

1. Shell Client and Shell Session schemas.
2. Panel Type and Panel Instance schemas.
3. Panel binding to Workspace/Object/Activity/Session identities.
4. Layout Profile, Layout Revision and projection/migration schemas.
5. desktop/tablet/phone presentation capability schema.
6. Activity Centre projection and command availability schema.
7. Evidence Explorer projection and disagreement/limitation schema.
8. control lease, focus, takeover and return schema.
9. panel generation/reconnect/stale-state rules.
10. Settings versus operational-control boundary.
11. UI contribution manifest, permissions and source/licence record.
12. privacy/redaction and protected-panel behavior.
13. accessibility, keyboard, touch, safe-area and reduced-motion profile.
14. background panel suspension/resource policy.
15. Theia, Dockview and alternative-client conformance mappings.

## Validation set

- one Workspace rendered through Theia and responsive shell with stable Panel identities;
- simultaneous terminal, Browser, Device and Application panels;
- desktop/tablet/phone layout switching without stopping Activities;
- layout reload with authoritative runtime re-read;
- failed panel isolation;
- exact lifecycle/proof labels from live records;
- human/automation takeover and stale-input rejection;
- keyboard/touch/screen-reader operation;
- Settings versus live control separation;
- governed extension contribution;
- shell/framework replacement without identity changes.

## Next Phase 0A group

Proceed with **WP10 — Knowledge, Data, Search and Plugin Composition**:

- RAGFlow;
- LlamaIndex;
- Dify;
- Polars;
- Deno;
- Model Context Protocol specification and server examples;
- OpenClaw/ClawHub plugin discovery/lifecycle patterns where still relevant;
- internal Hunter knowledge/memory/search/provider bridges;
- source-grounded indexing, retrieval and citations;
- structured data/table/database Activities;
- recipe/service/tool/plugin manifests;
- provider-neutral model and data interfaces;
- knowledge permissions, revisions, freshness and deletion;
- search across Objects, Activities, Artifacts, Workspaces and external sources;
- external reasoning/caller boundary without embedding an agent council into Ptah.
