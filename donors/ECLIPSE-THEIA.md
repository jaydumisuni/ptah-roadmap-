# Donor Record — Eclipse Theia

**Phase:** 0A / WP09  
**Status:** FIRST-PASS COMPLETE — PRIMARY EXTENSIBLE DESKTOP WORKSPACE-SHELL DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/eclipse-theia/theia
- Default branch: `master`
- Pinned commit: `3595b053a48a1a4c7171aea0361a25f782140af9`
- Licence: EPL-2.0, with GPL-2.0 plus Classpath Exception as an available secondary licence for qualifying source files
- Activity: Active Eclipse Foundation project
- Classification: extensible browser/desktop application framework and IDE-compatible shell donor
- Ptah targets: `UI-001`, `UI-002`, dockable panels, widget contribution, frontend/backend separation, layout persistence/migration, terminal/editor integration and extension contribution points

## Files/components inspected

- `README.md`
- `packages/core/src/browser/shell/application-shell.ts`
- `packages/core/src/browser/widget-manager.ts`
- `packages/core/src/browser/shell/shell-layout-restorer.ts`
- `packages/core/src/browser/frontend-application-contribution.ts`
- documented Theia application/plugin/VS Code extension compatibility and cloud/desktop architecture

## Verified capabilities and patterns

- Theia is a framework for building custom cloud and desktop IDE-like products rather than one fixed end-user application.
- It uses TypeScript with a browser frontend and Node.js backend.
- Products select and compose Theia packages rather than inheriting every feature.
- It supports Theia extensions and a large part of the VS Code extension ecosystem through Open VSX.
- The application shell uses Lumino widgets with main, bottom, left and right dock/side areas.
- The shell tracks active/current widgets, focus and widget creation/removal.
- Widgets are created through typed `WidgetFactory` contributions using serializable construction options.
- Widget creation may be synchronous or asynchronous and is cached/deduplicated by stable factory/options descriptions.
- Stateful widgets can store and restore inner state.
- Shell layouts are serialized, versioned and restored across sessions.
- Layout migrations and transformation contributions can update older stored layouts before restoration.
- Failed widget-state restoration can degrade one widget without necessarily destroying the whole shell.
- Frontend contributions have explicit initialize, configure, start, layout-init and stop hooks.
- Stop contributions may prevent closing when an operation or unsaved state makes shutdown unsafe.
- The shell supports secondary windows, drag/drop, tabs, split panels, side panels, status bars and toolbar contributions.

## What Theia completes

- A mature extensible desktop Workspace shell foundation.
- Typed panel/widget contribution points for terminal, editor, Object, Browser, Device, Application and Activity views.
- Dock, split, tab, side-panel and secondary-window machinery.
- Versioned layout persistence and migration.
- Frontend/backend separation suitable for remote Ptah Nodes and Workspaces.
- Existing editor, terminal, file, search, SCM and extension-host machinery that Ptah should not rebuild from scratch.
- A product-building framework that can be branded and narrowed instead of presenting as stock VS Code.

## Important limitations for Ptah

- Theia is IDE-oriented; Ptah is a broader operational Workspace for files, browsers, Devices, applications, firmware, media and evidence.
- The default desktop shell is too dense for a universal mobile interface.
- Theia widget IDs, factory IDs and serialized layout data are not Ptah Panel or Session identity.
- Theia layout restoration restores UI/widget state, not underlying Activities, terminals, Devices, applications or browser truth.
- VS Code extension compatibility can introduce broad filesystem/process/network authority and supply-chain risk.
- A frontend/backend extension may fail, block startup or expose privileged APIs if not capability-governed.
- Theia package/extension lifecycle is not Ptah's Facility lifecycle.
- Browser frontend disconnection does not prove backend Workspace/Activity failure.
- Theia's EPL/GPL-secondary licensing requires file/package-level review for direct modifications and distribution.
- Stock Theia/IDE terminology and navigation would make Ptah feel like a generic coding environment rather than its own world.
- Monaco/editor and xterm terminal surfaces are useful components but must remain views over Ptah Objects and PTY Activities.

## Must not be inherited

- stock Theia/IDE identity or product branding;
- Theia widget/layout IDs as canonical Ptah Panel/Session identity;
- every VS Code extension enabled by default;
- extension access to arbitrary host filesystem/process/network resources;
- layout restore interpreted as runtime Session recovery;
- desktop dock layout forced onto phones/tablets;
- editor/file-centric information architecture used for every Ptah domain;
- Theia backend used as the Activity Ledger, Node Protocol or Facility host truth;
- unsandboxed user extensions loaded into the core control plane;
- private THETECHGUY/Hunter integrations exposed through public Theia contributions.

## Integration decision

**ADAPT THEIA AS THE PRIMARY EXTENSIBLE DESKTOP WORKSPACE-SHELL FOUNDATION, NOT THE UNIVERSAL PTAH UI OR CORE.**

Recommended role:

1. a custom Ptah desktop/workstation shell composed from selected Theia packages;
2. Ptah-native widgets for Home, Workspaces, Objects, Activities, Browser, Devices, Applications, evidence and settings;
3. Monaco/editor, terminal and file tooling through selected existing packages;
4. optional VS Code extension compatibility in a governed extension host;
5. a separate lighter responsive/mobile shell using the same Ptah panel/session contracts;
6. Theia layout data treated as one UI adapter projection of Ptah Panel/Layout records.

## Native Ptah gap

Ptah must define:

- Shell Session, Panel, Panel Instance and Layout identities;
- panel types independent of Theia widget factories;
- panel-to-Workspace/Object/Activity/Device/Application/Browser references;
- panel capability and privacy requirements;
- desktop, tablet and phone presentation profiles;
- layout revision, migration and cross-device compatibility;
- focus/control ownership between human and automation;
- Activity/evidence status projections;
- reconnect/degraded/offline presentation;
- governed extension contribution and permission model;
- public/private contribution separation;
- accessibility, keyboard, touch and reduced-motion requirements;
- backend replacement path.

## Exit strategy

Ptah's Shell/Panel/Layout contracts remain independent. Theia, Dockview, a custom React shell, native desktop clients or future interfaces can present the same Workspace without changing underlying identities.

## Validation required

1. Compose Ptah-native Object, Activity, terminal, Browser, Device and Application panels in one Theia-based desktop shell.
2. Persist and migrate a versioned layout while retaining stable Ptah Panel identities.
3. Restore the UI after browser reload without falsely claiming runtime Activity recovery.
4. Remove or fail one panel contribution without destroying unrelated panels.
5. Run several terminals, browsers, Devices and applications concurrently without focus/input cross-talk.
6. Load a governed extension with scoped capabilities and reject an unapproved privileged extension.
7. Present the same Workspace through the lighter mobile shell without requiring Theia's desktop layout.
8. Replace Theia for one presentation client without changing Ptah Workspace, Panel or Session records.
