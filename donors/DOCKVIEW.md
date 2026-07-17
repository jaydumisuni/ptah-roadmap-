# Donor Record — Dockview

**Phase:** 0A / WP09  
**Status:** FIRST-PASS COMPLETE — LIGHTWEIGHT RESPONSIVE PANEL-LAYOUT DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/mathuo/dockview
- Default branch: `master`
- Pinned commit: `0006ab0a18a1e9168e4ae6066a7402250da1d6fc`
- Licence: MIT
- Activity: Active
- Classification: framework-neutral tabs/groups/grids/splitviews/docking layout manager
- Ptah targets: lighter desktop/tablet shell, dockable panels, layout serialization, mobile/touch support, floating groups and popout windows

## Files/components inspected

- `README.md`
- package family and framework bindings
- documented serialization, touch/mobile, floating/popout and layout features

## Verified capabilities and patterns

- Zero-dependency JavaScript core with React, Vue and Angular bindings.
- Supports tabs, groups, grids, splitviews and dockable panels.
- Serializes and deserializes complete layouts.
- Supports drag/drop, floating groups and popout windows.
- Explicitly supports touch and mobile interaction.
- Supports Shadow DOM.
- Themeable/customizable with an extensive API.
- Has high test coverage and published package provenance/build transparency.
- Can be embedded without adopting an IDE framework or extension host.

## What Dockview completes

- A lighter panel/layout option for Ptah's custom shell.
- Touch/mobile-capable docking behavior absent from many desktop IDE shells.
- Framework-neutral composition suitable for a custom Ptah Home and responsive interface.
- Saved layout and popout/floating panel patterns.
- A way to share Panel/Layout contracts between a full desktop shell and lighter presentation clients.
- An escape path from making Theia mandatory for every interface.

## Important limitations for Ptah

- Dockview only manages presentation layout; it does not own Workspace, Activity, Panel content, backend services, extensions, terminals or editors.
- Serialized layout IDs are UI-library state, not Ptah Panel identity.
- Docking interactions alone do not produce a good phone information architecture; small screens need explicit compact/navigation modes.
- Floating/popout windows can lose state or become stale after browser reload/disconnect.
- Drag/drop and touch behavior require accessibility and keyboard alternatives.
- It does not provide a plugin permission model, frontend/backend architecture or service lifecycle.
- The core can be framework-neutral, but bindings add framework-version dependencies.
- A restored layout does not restore underlying runtime Sessions or Activities.

## Must not be inherited

- Dockview panel/group IDs as canonical Ptah identity;
- free-form docking forced on small phones;
- layout serialization used as Session recovery truth;
- panels allowed to hold privileged runtime state only in browser memory;
- popout windows receiving permanent credentials or unrestricted backend access;
- drag/drop as the only way to arrange or navigate panels;
- one framework binding made part of Ptah's public contract.

## Integration decision

**ADOPT DOCKVIEW AS THE PRIMARY LIGHTWEIGHT CUSTOM-SHELL LAYOUT CANDIDATE; USE THEIA FOR THE FULL DESKTOP/IDE-COMPATIBLE SHELL.**

Recommended presentation split:

1. **Ptah Desktop Workbench** — Theia-based or Theia-composed shell for coding-heavy/full workstation use.
2. **Ptah Universal Shell** — custom responsive shell using Dockview on wide screens and explicit stacked/route-based presentation on phones.
3. Both consume the same Ptah Panel/Layout/Focus contracts.
4. The phone layout does not expose arbitrary docking; it presents one primary panel plus compact switching, drawers and Activity status.

## Native Ptah gap

Ptah must define:

- Panel and Panel Instance identity independent of Dockview;
- layout profile types: desktop, tablet, phone, kiosk and presentation;
- layout revisions and cross-client migration;
- panel visibility, focus, control and privacy state;
- compact/mobile replacement rules for docked panels;
- popout/secondary-window connection tokens;
- keyboard, screen-reader and touch alternatives;
- recovery when a popout or browser window closes;
- responsive resource limits and background panel suspension;
- Theia/Dockview projection/conformance tests.

## Exit strategy

Ptah Panel/Layout contracts can be rendered through Dockview, Theia/Lumino, native desktop views or future UI frameworks. Dockview serialization remains adapter data.

## Validation required

1. Render the same Workspace/Panel set through Theia and Dockview projections.
2. Save/migrate a layout while preserving Ptah Panel identities.
3. Switch desktop→tablet→phone without losing underlying terminal/browser/device/application Sessions.
4. Use touch, keyboard and screen-reader navigation without relying only on drag/drop.
5. Open/close popouts and reject stale connection tokens.
6. Suspend background panels under mobile resource pressure without stopping underlying Activities.
7. Replace Dockview without changing Panel/Layout records.
