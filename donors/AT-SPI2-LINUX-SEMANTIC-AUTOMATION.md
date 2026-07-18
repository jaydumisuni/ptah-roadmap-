# Donor Record — AT-SPI2 Linux Semantic Automation Composition

**Phase:** 0A / Linux semantic completion  
**Status:** FIRST-PASS COMPLETE — PRIMARY LINUX ACCESSIBILITY TREE/ACTION DONOR WITH WAYLAND INPUT AND INSPECTION COMPLETION  
**Inspected:** 2026-07-18

## Identity

### AT-SPI2 Core

- Canonical source: https://gitlab.gnome.org/GNOME/at-spi2-core
- Official GitHub mirror: https://github.com/GNOME/at-spi2-core
- Default branch: `main`
- Pinned mirror commit: `ae9a26ad5e1c34b1482dbbde9db59f2c094c6e7e`
- API version inspected: AT-SPI 2.0
- Library version observed in current generated documentation: `2.61.0`
- Licence: LGPL-2.1-or-later for libatspi/core library material; file/component-level review remains required
- Activity: Active
- Classification: Linux/free-desktop accessibility transport, semantic object tree, actions, state/events, geometry and cache donor

### Dogtail

- Canonical source: https://gitlab.com/dogtail/dogtail
- Release pin: `v2.0.4`
- Release commit shown by canonical GitLab: `81b77508`
- Licence: GPL-2.0-or-later
- Activity: Active
- Classification: high-level AT-SPI GUI test/automation and selector convenience donor

### gnome-ponytail-daemon

- Canonical source: https://gitlab.gnome.org/ofourdan/gnome-ponytail-daemon
- Release pin: `0.0.11`
- Licence: GPL-2.0-or-later
- Classification: GNOME Wayland pointer/keyboard injection and surface-coordinate bridge donor

### Accerciser

- Canonical source: https://gitlab.gnome.org/GNOME/accerciser
- Official GitHub mirror: https://github.com/GNOME/accerciser
- Pinned mirror commit: `8062fb87b59b3f9f2445c3d9c87c4b82d5d8fb5e`
- Current release lineage inspected: `3.48.0`
- Licence: BSD-3-Clause for code, with package assets requiring file-level review
- Classification: interactive accessibility explorer, event monitor, API browser and debugging Application donor

## Ptah relevance

Ptah targets:

- completion of the Linux semantic-automation gap retained by WP07B/ADR-0010;
- Application Session semantic state and actions;
- toolkit-neutral element inspection across GTK, Qt, WebKit, browsers and compatible applications;
- semantic selectors, focus, text, value, selection, tables and actions;
- event-driven UI-state updates;
- coordinate/geometry correlation with visual evidence;
- explicit X11 versus Wayland raw-input Providers;
- accessibility/automation permission and control leases;
- honest semantic-partial and visual-fallback states;
- accessibility conformance/testing Artifacts.

## Files/components inspected

### AT-SPI2

- `README.md`
- `COPYING`
- `devel-docs/architecture.rst`
- `devel-docs/atspi-python-stack.rst`
- `xml/Accessible.xml`
- `xml/Action.xml`
- `xml/Component.xml`
- `xml/Collection.xml`
- `xml/Cache.xml`
- `xml/Event.xml`
- `xml/Registry.xml`
- current generated libatspi API documentation
- current next-generation accessibility architecture proposal

### Completion donors

- current Dogtail README, release/tag and issue/evolution evidence;
- Dogtail 2.x future-backend, GTK4, Qt, Xorg and Wayland boundaries;
- gnome-ponytail-daemon release/package and GNOME RemoteDesktop/ScreenCast integration evidence;
- Accerciser repository/product classification and current activity.

## Verified AT-SPI2 capabilities and patterns

### Toolkit-neutral accessibility architecture

- Applications and GUI toolkits expose accessibility semantics over D-Bus through AT-SPI interfaces.
- Legacy toolkit paths may use ATK and an adaptor, while modern GTK4, Qt5 and WebKit paths can implement the D-Bus interfaces directly.
- The accessibility registry tracks participating applications and event listeners within a user session.
- Assistive-technology clients such as Orca, Accerciser and Dogtail maintain a representation of accessible objects in applications.
- The protocol is toolkit-neutral: objects expose standard roles, names, states, relations, actions and interfaces rather than requiring a separate automation implementation for each toolkit.

### Accessible object model

Every accessible object can expose:

- application D-Bus name and object path;
- interface version;
- localized name and description;
- parent and child count/tree position;
- locale;
- application-specific `AccessibleId`;
- role and localized role;
- states;
- attributes;
- relations to other accessible objects;
- supported specialized interfaces.

Specialized interfaces include:

- Action;
- Collection;
- Component;
- Document;
- EditableText;
- Hypertext/Hyperlink;
- Image;
- Selection;
- Table/TableCell;
- Text;
- Value.

`AccessibleId` can improve test identification but remains application-supplied, may require tree traversal to locate and does not create a global stable identity.

### Actions and semantic mutation

- Action-capable objects enumerate available actions.
- Actions expose machine-readable name, localized name, description and keybinding.
- `DoAction` invokes an indexed semantic action and returns a boolean result.
- More specialized interfaces can set text, value, selection, focus, geometry or scrolling where supported.
- Semantic actions can avoid coordinate injection for applications that expose correct accessibility operations.
- A returned boolean is command-level evidence only; it does not prove the application reached the intended business/UI state.

### Geometry and visual correlation

The Component interface provides:

- point containment and accessible-at-point queries;
- extents, position and size;
- screen, top-level-window and parent-relative coordinate systems;
- rendering layer and selected z-order information;
- focus requests;
- move/resize methods;
- scroll-to-object and scroll-to-point methods.

Geometry enables correlation between semantic nodes and pixels/screenshots, but toolkits, scaling, shadows, compositor transforms and window decorations can create offsets or incomplete geometry.

### Query and traversal

- Tree traversal is available through parent/child operations.
- Collection can match descendants by state, attributes, roles and supported interfaces.
- Queries support sorting, traversal scope and result limits.
- Some methods are incompletely implemented across libatspi/toolkits; `GetActiveDescendant` is one documented example.
- Large trees may reject broad child-list requests or require bounded traversal.

### Cache and event model

- The Cache interface supports bulk retrieval of an application's accessible objects.
- Add/Remove signals update client caches as objects appear or disappear.
- Bulk cache reduces the otherwise chatty per-object D-Bus round trips.
- Event interfaces cover property, bounds, state, children, selection, model, active descendant, announcement, attributes, text, table and window changes.
- Clients register event interest through the Registry and may scope registrations by application.
- The event property-prefetch mechanism is currently documented as unimplemented.
- Protocol/toolkit differences remain, including older versus newer Cache signatures.
- Event loss, stale caches and toolkit bugs require periodic or action-triggered reconciliation rather than event-only trust.

### Current and future architecture

- The AT-SPI project itself identifies pull-based D-Bus chatter, legacy layers, compatibility workarounds and end-to-end test gaps.
- A proposed next-generation push-based architecture aims for sandbox support, surface-scoped trees, atomic updates, lower latency and closer visual-frame correlation.
- That proposal builds on AccessKit and anticipates an AT-SPI bridge for backward compatibility.
- The next-generation work is an important exit/adapter path, not an approved v1 dependency.

## Verified completion-donor lessons

### Dogtail

- Provides Python tree traversal, role/name/ID-oriented selectors and high-level GUI automation convenience over AT-SPI.
- Supports GNOME/GTK targets on Xorg and Wayland GNOME.
- Qt support exists through qt-at-spi but is explicitly limited/not officially maintained.
- Dogtail 2.x was refactored to reduce legacy debt and prepare for future backends such as AccessKit/Newton.
- GTK4 shadows, scaling and offsets can affect coordinate automation; Dogtail applies workarounds.
- Current issue/fix history shows selector recursion, action selection, role naming, ID matching and toolkit behavior remain fallible.
- Dogtail is useful as a test/automation reference and optional wrapped Facility, not Ptah's canonical semantic model.

### gnome-ponytail-daemon

- Bridges raw pointer/keyboard automation on GNOME Wayland.
- Uses GNOME ScreenCast, RemoteDesktop and shell/Mutter window/surface information.
- Correlates application/window-local coordinates with compositor/global surfaces.
- Uses Linux input/keyboard support such as libei and xkbcommon.
- It is GNOME/Wayland specific and does not create a universal Wayland automation path.
- Raw input injection is a stronger permission class than semantic inspection or semantic `DoAction`.

### Accerciser

- Provides interactive inspection of the accessibility tree, interfaces, events and object properties.
- Can invoke/control exposed accessibility operations for debugging.
- Supports plugins, event monitoring and API exploration.
- It is useful as a specialist inspection/debug Application and validation donor rather than a runtime dependency.

## What this composition completes

- A canonical Linux semantic-state source through AT-SPI2.
- Toolkit-neutral accessible roles, names, states, attributes, relations and interfaces.
- Semantic action invocation, text/value/selection/focus/scroll operations where applications support them.
- Bulk tree capture and event-driven updates.
- Geometry/coordinate correlation between semantic objects and rendered pixels.
- High-level selector/test patterns from Dogtail.
- GNOME-Wayland raw input completion through Ponytail.
- Human inspection and debugging through Accerciser.
- A future adapter direction toward push-based AccessKit/Newton-style trees.

## Important limitations for Ptah

- AT-SPI D-Bus names and object paths are runtime/session-local references, not stable Ptah identities.
- Accessible objects are dynamic and may be destroyed/recreated while retaining similar visible semantics.
- `AccessibleId`, role and name can be missing, duplicated, localized or changed by application/toolkit revisions.
- A cached node can become defunct even when the application/window remains alive.
- Events can be incomplete, reordered, lost or toolkit-specific.
- Cache signatures and implementation behavior vary across toolkits/versions.
- AT-SPI is chatty and can be expensive for large trees.
- Semantic coverage depends on application/toolkit accessibility quality.
- Canvas/custom-drawn/remote-rendered/game/video UIs may expose little or no useful semantic structure.
- `DoAction`/focus/text/value return values are not application outcome proof.
- Geometry can be stale or inconsistent under scaling, shadows, animations, window movement, multi-monitor and compositor transforms.
- The session accessibility bus is powerful and may expose/control many applications in a desktop session.
- Legacy AT-SPI does not provide Ptah-grade per-Workspace, per-application, per-caller object authorization.
- A shared desktop/session accessibility bus is not a safe multi-tenant boundary.
- Raw input injection can affect the wrong surface when focus/window state changes.
- Ponytail is GNOME-specific and cannot be claimed for KDE, wlroots, Weston or other compositors.
- X11 and Wayland use materially different input/control paths.
- Dogtail is GPL-2.0-or-later and its convenience code should not be copied into incompatible components without formal review.
- Dogtail coordinate/toolkit workarounds are not universal semantic truth.
- Accerciser is a human debugging tool, not a durable automation runtime.
- The proposed next-generation accessibility architecture remains evolving and cannot close v1 implementation choices.

## Must not be inherited

- D-Bus application name/object path as stable Semantic Target identity;
- role/name/index-only selectors described as permanently stable;
- `AccessibleId` assumed globally unique or immutable;
- cached accessible nodes reused after application/window/provider generation changes;
- event delivery treated as complete state truth;
- semantic action boolean treated as verified completion;
- coordinate clicking described as semantic automation;
- visual fallback described as semantic success;
- GTK4 shadow/offset hacks made universal;
- raw input authority combined with read-only semantic inspection permission;
- one session-wide AT-SPI bus shared across mutually untrusted Workspaces;
- accessibility enabled or exposed globally merely for convenience;
- Ponytail presented as universal Wayland support;
- X11 input injection silently substituted for Wayland control;
- Dogtail GPL code copied into Ptah Core without licence strategy;
- pyatspi compatibility wrappers treated as the preferred long-term binding;
- AT-SPI2 made the permanent internal Ptah semantic schema;
- future AccessKit/Newton claims presented as implemented capability.

## Integration decision

**ADAPT AT-SPI2 AS THE PRIMARY LINUX SEMANTIC-STATE/ACTION PROVIDER, WITH PTAH-NATIVE SNAPSHOT, TARGET, SELECTOR, PERMISSION, EVENT, ACTION AND PROOF CONTRACTS.**

Recommended composition:

1. each Linux Application Session can expose an optional AT-SPI Semantic Provider;
2. semantic access is scoped to an isolated desktop/session and approved application/window set;
3. initial state is captured through a bounded bulk/tree Snapshot;
4. events update the Snapshot cache and advance provider/application/window generations;
5. periodic/action-triggered reconciliation detects missed events and stale nodes;
6. AT-SPI references remain adapter-local observations beneath Ptah Semantic Target identities;
7. selectors combine application/window context, accessible ID, role, name, states, attributes, relationships, text and bounded tree path;
8. ambiguous selectors return candidates rather than silently choosing one;
9. semantic action, raw input and visual action remain separate Facility methods and permission classes;
10. every action binds to one pre-action Semantic Snapshot and produces post-action semantic/visual/read-back evidence;
11. incomplete semantic UIs degrade explicitly to semantic-partial or visual-only behavior;
12. Dogtail may be wrapped as an optional testing Facility or studied for selectors, but is not Ptah Core;
13. Ponytail is one GNOME-Wayland Input Provider with explicit compositor/session requirements;
14. Accerciser may run as an optional inspection Application;
15. future push-based accessibility providers can replace AT-SPI without changing Ptah Application Session or Semantic Target identity.

## Native Ptah completion required

### Semantic Provider and Snapshot

Ptah must define:

```text
semantic_provider_id
application_session_id
provider_generation
application_generation
window_generation
desktop_session_and_compositor
atspi_bus_and_registry_instance
provider/toolkit/atspi_versions
locale_and_scaling
snapshot_id
captured_at
event_cursor_or_sequence
coverage_state
limitations
```

### Accessible Node Observation

Each observed node needs:

```text
semantic_observation_id
snapshot_id
adapter_reference
application_and_window_context
parent_child_relationship
role
name_and_description
accessible_id
states
attributes
relations
supported_interfaces
text_value_selection_table_metadata
actions
geometry_coordinate_space_layer
observed_at
defunct_or_available_state
```

### Stable target and selector

Ptah must keep a stable Semantic Target/intent identity separate from one observation. A selector can include:

- application/package/process/window identity;
- accessible ID;
- role;
- name/description/localized text;
- states and attributes;
- interface/action support;
- relations;
- ancestor/descendant path;
- document/text/value/table context;
- geometry/visual correlation;
- bounded index/nth candidate.

The selector result records all candidates, ambiguity, confidence, snapshot and exact chosen observation.

### Coverage and availability state

At minimum:

```text
semantic_complete
semantic_partial
visual_only
semantic_unavailable
stale_or_defunct
provider_disconnected
permission_blocked
```

### Action model

Ptah must distinguish:

- inspect/query;
- semantic Action invocation;
- focus/scroll;
- text/editable-text;
- value;
- selection/table operations;
- raw pointer/keyboard injection;
- visual/coordinate automation;
- human takeover.

### Security and permission model

Ptah must define:

- semantic read scope;
- event subscription scope;
- application/window scope;
- semantic action scope;
- raw input/control scope;
- clipboard/text-secret scope;
- screenshot/video/visual evidence scope;
- control lease and fencing;
- desktop/session isolation boundary;
- compositor/RemoteDesktop permission state;
- credential/sensitive-text redaction.

### Evidence and proof

Every mutation should retain:

- pre-action Semantic Snapshot/selector result;
- exact adapter method/action and parameters;
- input/control lease and provider generation;
- command result;
- relevant AT-SPI events;
- post-action semantic Snapshot/read-back;
- screenshot/visual region when permitted;
- application/domain result where available;
- ambiguity/limitations.

## Licence decision

- AT-SPI2/libatspi LGPL-2.1-or-later permits library integration subject to LGPL obligations and file/component review.
- Dogtail GPL-2.0-or-later is best treated as architecture study, an external process/wrapped optional Facility or separately licensed component unless a formal distribution strategy approves closer reuse.
- gnome-ponytail-daemon GPL-2.0-or-later should remain a separately packaged external Provider when used.
- Accerciser BSD-3-Clause code is permissive, while included assets/data require file-level review.
- Toolkit bindings, D-Bus libraries, input libraries and compositor dependencies require separate records.

## Exit strategy

Ptah's Semantic Provider/Snapshot/Target/Action contracts remain independent of AT-SPI2. A future AccessKit/Newton provider, application-specific API, browser accessibility tree, Windows UIA, macOS AX, Android UIAutomator or visual provider can implement the same neutral contracts without changing Application Session, Activity or proof identity.

## Validation required

1. Capture bounded semantic trees from GTK3, GTK4, Qt and browser/WebKit applications and record coverage differences.
2. Recreate/destroy one widget and prove stale D-Bus object references cannot be reused as stable targets.
3. Match by accessible ID, role/name, relation path and text; expose duplicates/ambiguity honestly.
4. Bulk-load Cache state, process Add/Remove/State/Bounds/Text/Focus events and detect a deliberately dropped event through reconciliation.
5. Restart an application/accessibility bus and invalidate the prior provider/application generation.
6. Perform `DoAction` and prove command return remains separate from post-action semantic and visual outcome.
7. Perform text/value/selection/focus/scroll actions with exact permission and read-back evidence.
8. Correlate semantic extents with screenshots under scale, multi-monitor, window movement and GTK4 decoration/shadow cases.
9. Run GNOME Wayland raw input through Ponytail and keep it separate from semantic actions.
10. Run an unsupported compositor and report raw-input unavailability without claiming Wayland automation.
11. Attempt semantic access across two isolated Workspaces and prove the session bus cannot cross the boundary.
12. Revoke the control lease and reject stale semantic/raw-input actions.
13. Handle a canvas/custom-rendered app as semantic-partial or visual-only without fabricated nodes.
14. Retain accessibility conformance findings as Artifacts/Claims rather than silently correcting application semantics.
15. Replace AT-SPI2 with a mock/new semantic Provider without changing Ptah target/action/proof identities.
