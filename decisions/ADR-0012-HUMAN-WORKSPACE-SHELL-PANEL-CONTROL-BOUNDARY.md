# ADR-0012 — Human Workspace Shell, Panel, Layout and Control Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Phase:** 0A / WP09 Human Workspace Shell closure

## Context

Ptah requires a direct-human interface that can operate the same Workspaces and Activities used by compatible systems. It must show and control many unrelated operations at once:

- Objects and files;
- terminals and processes;
- Browsers and live research;
- Devices and firmware operations;
- native/VM/mobile Applications;
- Builds, transfers and decomposition;
- Activity status, logs, receipts, evidence and proof;
- degraded, waiting, manual and recovery states.

The inspected sources solve different layers:

- Eclipse Theia supplies an extensible browser/desktop framework, typed widgets, dock/side areas, frontend/backend separation and layout migration.
- OpenVSCode Server and code-server supply optional familiar coding-focused browser applications.
- xterm.js supplies a mature browser terminal renderer, not the PTY runtime.
- Dockview supplies a lighter framework-neutral layout manager with mobile/touch support.
- Hunter supplies server-grounded shell access, explicit maintenance/degraded state and responsive/mobile lessons, while its current production interface remains under rebuild.
- Sergeant supplies full operational views, compact launchers, visible progress, evidence and history patterns.
- MIBU and Device Manager supply proof-aware guided steps, exact target state, manual handoffs and blocked-state visibility.
- THETECHGUY website sources show the need for deliberate public builds and real mobile verification, while also demonstrating the debt caused by accumulated runtime patch scripts.

No donor defines Ptah's Shell Session, Panel identity, layout, human/automation focus, Activity truth or proof model.

Hunter Foreman is excluded from active WP09 composition unless explicitly reintroduced by the owner.

## Decision

Ptah will own backend-neutral contracts for:

1. Shell Client;
2. Shell Session;
3. Workspace presentation;
4. Panel Type;
5. Panel Instance;
6. Layout Profile and Layout Revision;
7. Panel binding and View state;
8. focus and control ownership;
9. human/automation takeover and return;
10. Activity Centre;
11. evidence/proof explorer;
12. Settings and operational controls as separate surfaces;
13. contribution/extension points;
14. desktop, tablet, phone, kiosk and presentation projections.

No Theia widget, Dockview panel, VS Code editor group, browser tab or DOM element becomes canonical Ptah Panel or Layout identity.

---

# Shell Client

A Shell Client is one presentation implementation connected to Ptah.

```text
shell_client_id
client_type
client_version
platform
form_factor
capabilities
accessibility_profile
provider_or_application_reference
```

Client types include:

```text
theia_workbench
responsive_web_shell
native_desktop_shell
mobile_shell
coding_compatibility_provider
embedded_specialist_panel
read_only_presentation
```

A client is replaceable. It displays projections of underlying Ptah state rather than owning that state.

---

# Shell Session

A Shell Session is one authenticated presentation session for a caller and selected Workspace set.

```text
shell_session_id
shell_client_id
caller_reference
selected_workspace_id
accessible_workspace_ids
layout_profile_id
opened_panel_ids
focused_panel_id
control_owner_reference
started_at
last_seen_at
state
```

States include:

```text
starting
ready
degraded
reconnecting
offline_read_only
maintenance
closing
closed
failed
```

A Shell Session is not the same as a Workspace Session, Device Session, Application Session, Browser Session or terminal Session.

One shell may reconnect while underlying Activities continue. One shell may be unavailable while backend services remain healthy.

---

# Workspace presentation

The shell presents one active Workspace and may show summaries from several accessible Workspaces.

A Workspace switch changes the default scope of new panels and actions. It does not silently terminate or move existing Activities.

Every panel displays its bound Workspace, Object, Activity, Device, Application, Browser or Session context where ambiguity is possible.

---

# Panel Type

A Panel Type is a versioned UI contribution contract:

```text
panel_type_id
panel_type_version
title_and_icon_claims
supported_bindings
required_capabilities
privacy_class
minimum_presentation_size
supported_form_factors
supports_multiple_instances
supports_background_suspend
contribution_source
```

Initial native Panel Types include:

```text
ptah.home
ptah.workspace.switcher
ptah.objects
ptah.object.preview
ptah.search
ptah.activities
ptah.activity.detail
ptah.evidence
ptah.terminal
ptah.editor
ptah.browser
ptah.device
ptah.application
ptah.transfer
ptah.build
ptah.notifications
ptah.settings
ptah.help
```

Specialist products may contribute additional panels through governed adapters.

---

# Panel Instance

A Panel Instance is a user-visible view bound to exact Ptah identities.

```text
panel_id
panel_type_id
shell_session_id
workspace_id
binding_references
creation_reason
created_at
state
view_state_reference
privacy_class
focus_state
control_state
```

States include:

```text
creating
ready
loading
waiting
manual_action_required
degraded
reconnecting
suspended
closed
failed
```

Panel state is not underlying runtime truth. A terminal panel can close while the PTY Activity continues. A Device panel can reconnect while the Device Session remains alive. A layout restore can recreate a panel without restoring the underlying runtime.

---

# Panel binding

Panels bind to stable Ptah identities, for example:

- Workspace ID;
- Object or revision ID;
- Activity ID;
- terminal/PTY Session ID;
- Browser Profile/Context/Page ID;
- Device/Device Session ID;
- Application/Application Session/Window ID;
- Artifact/Receipt/Evidence ID;
- Build/Transfer/Decomposition/Firmware operation ID.

Backend-specific widget, process, window, page or stream references remain adapter metadata.

---

# Layout Profile and Revision

A Layout Profile defines presentation intent independent of one UI library.

```text
layout_profile_id
profile_type
owner_or_workspace_scope
form_factor
created_at
current_revision_id
```

Profile types include:

```text
desktop_workbench
desktop_operations
tablet_compact
phone_compact
kiosk
presentation
custom
```

A Layout Revision contains:

```text
layout_revision_id
layout_profile_id
parent_revision_id
panel_ids
logical_regions
ordering
selected_panels
sizes_and_visibility
created_at
client_projection_references
```

Logical regions may include primary, secondary, side, bottom, drawer, overlay and background.

Theia/Lumino or Dockview serialized layouts are client projections linked to a Ptah Layout Revision. They are not canonical layout truth.

Layout migrations transform old revisions explicitly. Unsupported panels are preserved as unavailable placeholders or removed through a receipted migration rather than silently lost.

---

# Presentation profiles

## Full desktop workbench

Theia is the primary candidate for coding-heavy and full workstation use.

- selected Theia packages provide shell, editor, terminal, file/search and extension-host machinery;
- stock IDE branding and navigation are replaced by Ptah-native information architecture;
- Ptah panels remain first-class beside editor/terminal views;
- VS Code compatibility is governed and optional.

## Responsive universal shell

A custom responsive web shell is required for general desktop, tablet and phone use.

- Dockview is the primary lighter layout candidate on wide screens;
- phone presentation uses one primary panel, compact switching, drawers and Activity status rather than arbitrary docking;
- tablet may use two-region split or compact dock layouts;
- background panels may be suspended visually without stopping underlying Activities;
- safe areas, touch targets, virtual keyboards and low-memory behavior are first-class.

## Coding compatibility applications

OpenVSCode Server and code-server may run as optional coding Applications/Providers. They do not replace Ptah Home, Workspace switching, Activity Centre or operational panels.

---

# Terminal surface

xterm.js is the primary browser terminal renderer.

The PTY Facility owns:

- terminal Session identity;
- process lifecycle;
- input/output streams;
- sequence and replay cursor;
- resize operations;
- retained logs and evidence.

The panel owns presentation only. Browser scrollback is not the durable log.

---

# Activity Centre

The Activity Centre is the human projection of the Activity Ledger and Event/Receipt systems.

It must show many unrelated Activities simultaneously with:

```text
activity identity and type
Workspace and caller
state and proof level
progress and current step
dependencies and blocked reason
Node/Provider/Facility
resource usage
started/updated/expected timing
retry/cancel/pause/resume availability
produced Objects/Artifacts
latest receipts/evidence
limitations and degraded capabilities
```

Lifecycle labels remain exact:

```text
planned
configured
available
connected
queued
running
waiting
manual_action_required
recovering
completed
failed
verified
accepted
```

A completed Activity is not automatically verified or accepted.

Controls are generated from the Activity contract and current permissions, not hard-coded optimistic buttons.

---

# Evidence and proof explorer

The Evidence Explorer presents:

- Receipts and proof levels;
- source Objects and produced Artifacts;
- logs, screenshots, recordings, traces and reports;
- detector or reviewer disagreements;
- stale/rejected evidence;
- static versus runtime versus physical-device proof;
- signature, attestation and review results;
- known limitations.

Preview/demo values are visually and semantically marked and cannot be promoted to live proof.

---

# Settings versus operational control

Settings is a separate surface from the Activity Centre and live Control panels.

Settings manages durable preferences and configuration such as:

- themes and accessibility;
- layout profiles;
- notifications;
- approved provider/Facility preferences;
- privacy/retention defaults;
- keyboard/touch behavior;
- feature visibility.

Operational actions such as start, stop, cancel, retry, connect, install, flash, send input or take control remain in context-specific panels or the Activity Centre.

A setting change is not proof that a runtime provider applied it; application status is shown separately.

---

# Human and automation control

Observation and control are separate.

A Control Lease contains:

```text
control_lease_id
resource_reference
shell_or_caller_reference
capability_scope
issued_at
expires_at
fencing_token
state
```

Control resources may include:

- terminal input;
- Browser Page input;
- Device input;
- Application input;
- editor mutation;
- high-impact Activity confirmation.

## Human takeover

A human may request control from automation.

Sequence:

1. request takeover;
2. current automation/caller receives a pause or control-revocation event;
3. current input operation reaches a safe boundary where possible;
4. a new fencing token is issued to the human Shell Session;
5. the panel shows human-control state;
6. return to automation is explicit and receipted.

Stale input/control tokens are rejected.

Focus in one browser window is not sufficient authority by itself.

## Shared observation

Several clients may observe one Session while only the active lease holder can send controlled input.

---

# Contribution model

A UI contribution declares:

- Panel Type and version;
- supported bindings;
- required Facility capabilities;
- privacy class;
- form-factor support;
- commands and menus;
- settings schema;
- evidence/Activity projections;
- public or private visibility;
- source/licence/signature.

UI contributions cannot access host files, processes, credentials or networks directly. They call scoped Ptah Facilities.

Theia extensions, VS Code extensions and embedded specialist interfaces are adapters to this model, not the model itself.

Private product panels remain outside public Ptah source unless deliberately released.

---

# Reconnect and degraded state

The shell distinguishes:

- client connection lost;
- panel adapter lost;
- backend Provider lost;
- underlying Activity still running;
- stale projection;
- offline cached read-only state;
- full backend outage;
- intentional maintenance.

Reconnection reloads authoritative state and advances client/panel generations. It does not replay side effects automatically.

A failed panel or contribution does not destroy unrelated panels or Activities.

---

# Accessibility and responsive behavior

Required capabilities include:

- keyboard-complete navigation;
- screen-reader landmarks and live status;
- visible focus and focus restoration;
- touch targets and gesture alternatives;
- reduced motion and animation controls;
- contrast/theme support;
- scalable text and zoom;
- safe-area handling;
- phone virtual-keyboard behavior;
- no drag/drop-only actions;
- low-resource/background panel suspension;
- status not encoded by color alone.

Accessibility settings apply across shell clients where possible.

---

# Donor decisions

- **Eclipse Theia:** primary extensible desktop/workbench foundation; not universal Ptah Core or phone shell.
- **Dockview:** primary lighter responsive layout candidate; phone uses explicit compact navigation rather than free-form docking.
- **OpenVSCode Server/code-server:** optional coding-compatibility Applications, not the Ptah shell.
- **xterm.js:** primary browser terminal renderer over Ptah PTY streams.
- **internal Hunter/Sergeant/MIBU/Device Manager/website sources:** adapt status, evidence, guided workflow, responsive and honest-claim patterns; specialist identities remain external.
- **Foreman:** excluded from active WP09 composition unless explicitly reintroduced.

---

# Consequences

## Positive

- Ptah can provide a rich workbench without forcing an IDE onto every screen.
- Desktop, tablet and phone clients share stable Panel/Layout identities.
- Many unrelated Activities remain visible and controllable concurrently.
- Human and automation can share observation while input ownership remains fenced.
- Specialist products remain usable and can contribute panels without being replaced.
- UI reload/layout restore no longer impersonates runtime recovery.
- Planned, connected, running, completed and verified claims remain honest.

## Costs

- Ptah must maintain Shell, Panel, Layout, focus/control and contribution schemas.
- Two presentation paths—full workbench and responsive shell—require conformance and design work.
- Theia and VS Code extension compatibility require strict permission governance.
- Mobile information architecture cannot be generated automatically from desktop docking.
- Accessibility and human/automation handoff require deliberate proof and testing.

## Do-not-break rule

> Never treat a shell client, widget, panel, tab, dock layout, browser focus, terminal renderer, preview value or UI reconnect as universal Ptah truth. Shell Session, Panel binding, Layout Revision, runtime Session, Activity state, proof level and control ownership have separate identities and guarantees.

---

# Required proof before freeze

1. Present one Workspace through Theia and the responsive shell with the same Ptah Panel identities.
2. Run several terminal, Browser, Device and Application panels concurrently without stream or input cross-talk.
3. Switch desktop, tablet and phone layout profiles without stopping underlying Activities.
4. Restore a layout after reload and prove runtime state is re-read rather than inferred from UI state.
5. Fail one panel/contribution and preserve unrelated panels and Activities.
6. Show planned, connected, running, completed and verified as distinct states using live records.
7. Perform human takeover and return from automation using fenced control leases.
8. Reject stale input from a closed or superseded Shell Session.
9. Navigate all critical functions by keyboard and touch without drag/drop-only dependencies.
10. Keep Settings separate from active operational controls and show whether changes were applied.
11. Load one governed extension/panel and reject an unapproved privileged contribution.
12. Replace Theia or Dockview for one client without changing Workspace, Panel, Activity or Session identity.
