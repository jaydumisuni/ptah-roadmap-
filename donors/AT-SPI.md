# Donor Record — AT-SPI, libatspi, Dogtail and Wayland Input Completion

**Phase:** 0A / Linux semantic UI completion  
**Status:** FIRST-PASS COMPLETE — PRIMARY LINUX ACCESSIBILITY-TREE AND SEMANTIC-AUTOMATION DONOR  
**Inspected:** 2026-07-18

## Identity

### AT-SPI core

- Canonical upstream: https://gitlab.gnome.org/GNOME/at-spi2-core
- Inspected GitHub mirror: https://github.com/GNOME/at-spi2-core
- Mirror default branch: `main`
- Pinned mirror commit: `ae9a26ad5e1c34b1482dbbde9db59f2c094c6e7e`
- API namespace: AT-SPI 2.0
- Current documentation observed during inspection: libatspi 2.61.0
- Licence: LGPL-2.1
- Classification: Linux/Unix accessibility bus, semantic UI tree, action/text/value/selection/event and toolkit-bridge donor

### Python bindings

- Canonical upstream: https://gitlab.gnome.org/GNOME/pyatspi2
- Inspected GitHub mirror: https://github.com/GNOME/pyatspi2
- Pinned mirror commit: `a0df428cfe6713be5769e1a3d3ca9942b6b4645d`
- Package description: legacy Python bindings for AT-SPI
- Licence metadata: LGPL-2.0-or-later
- Direction: use libatspi GObject-introspection bindings for new Ptah code; pyatspi remains compatibility-only

### Dogtail

- Canonical upstream: https://gitlab.com/dogtail/dogtail
- Current release observed: `v2.0.4`, short commit `81b77508`
- Inspected GitHub mirror/source lineage: https://github.com/vhumpa/dogtail
- Mirror code pin inspected: `8fc4fcaec6a6052d0e4c85903f7a394ff61dd88c`
- Licence: GPL-2.0
- Classification: higher-level AT-SPI search/action/wait/test framework and practical GNOME/Xorg/Wayland completion donor

### GNOME Ponytail

- Canonical upstream: https://gitlab.gnome.org/ofourdan/gnome-ponytail-daemon
- Packaged version observed in Debian stable/testing lineage: `0.0.11`
- Classification: GNOME Wayland screen-cast/remote-desktop/libei input bridge used by Dogtail
- Pin status: exact upstream source commit still required before dependency approval

## Ptah targets

- Linux completion of `APP-002`;
- semantic `Screen Context`/`Application Context` equivalent for Linux;
- semantic element inventory, querying, focus and action;
- text reading/editing, value and selection control;
- UI-change Events and semantic read-back;
- Xorg and GNOME Wayland input composition;
- semantic/visual/coordinate evidence fusion;
- accessibility, automation and test reuse without making accessibility aliases canonical identity.

## Files/components inspected

### AT-SPI core

- `README.md`
- `COPYING`
- `bus/README.md`
- `bus/accessibility.conf.in`
- `xml/Accessible.xml`
- `xml/Action.xml`
- `xml/Application.xml`
- `xml/Component.xml`
- `xml/Text.xml`
- `xml/EditableText.xml`
- `xml/Selection.xml`
- `xml/Value.xml`
- `xml/Collection.xml`
- `xml/Cache.xml`
- `xml/Event.xml`
- `xml/Registry.xml`

### pyatspi

- `README.md`
- `pyproject.toml`
- current release/commit evidence

### Dogtail

- canonical current GitLab repository/release evidence;
- `README.md` and `COPYING` from inspected mirror/source lineage;
- `dogtail/tree.py` high-level tree/action/search implementation;
- Wayland/Ponytail architecture described by the current project.

## Verified AT-SPI architecture

### Accessibility bus and registry

- AT-SPI uses a dedicated accessibility D-Bus rather than ordinary session-bus traffic because the protocol is chatty.
- `at-spi-bus-launcher` manages the accessibility bus for the user session and exposes its address through `org.a11y.Bus`.
- `registryd` tracks accessible applications and event listeners.
- Accessibility may start on demand or through session accessibility settings.
- Applications register one semantic root and expose accessible descendants through D-Bus object references.
- The application interface exposes toolkit name/version and AT-SPI interface version.
- Application IDs and D-Bus names/paths are runtime/session identifiers and are explicitly not reliable long-term application identity.
- Direct application bus addresses may bypass registry proxying for communication efficiency.

### Accessible tree

- Every exposed semantic object implements the base Accessible interface.
- Core properties include localized name, description, parent, child count, locale, application-specific AccessibleId and help text.
- Standard roles normalize buttons, lists, entries, dialogs, tables, terminals, menus, text, alerts and many other controls across toolkits.
- Relations express labelled-by, controller/controlled-by, flow, embedded/subwindow, popup, description/details and error-message relationships.
- AccessibleId can improve test identification but is application-specific, may not exist and has no direct global lookup operation.
- Dynamic objects may appear/disappear and need traversal, cache or event reconciliation rather than static path assumptions.

### Bulk cache and dynamic updates

- The Cache interface can return many accessible records in one operation to avoid excessive D-Bus round trips.
- Cached records include object, application, parent, index, child count, interfaces, name, role, description and state.
- AddAccessible and RemoveAccessible signals provide incremental change information.
- Toolkit implementations differ: documented old/new cache signatures and differing parent/null behavior remain compatibility hazards.
- Cache entries are performance projections, not canonical state or durable identity.

### Query and search

- Collection queries can match descendants by states, attributes, roles and supported interfaces.
- Results can be sorted, bounded and scoped by traversal direction.
- Collection is not uniformly complete: one exposed method is documented as unimplemented in libatspi.
- Clients must support bounded traversal and fallback when Collection or bulk-cache behavior is missing or inconsistent.

### Semantic actions

- Action exposes machine-readable/localized action names, descriptions and keybindings.
- `DoAction` invokes a selected semantic action such as click/open/activate and returns a Boolean protocol result.
- Specialized interfaces provide interaction beyond generic actions.
- Component supports focus, geometry, hit-testing, scrolling and optional move/resize operations.
- Geometry can be screen-, top-level-window- or parent-relative.
- Component layer/z-order data is partial and includes documented heuristics.
- A `true` return means the application/toolkit reported method success; it does not prove the desired external state or durable side effect.

### Text and editing

- Text exposes character count, caret offset, UTF-8 ranges, character/word/sentence/line/paragraph granularity, attributes, selections and geometry-related text operations.
- Character offsets are not byte offsets.
- Locale and application segmentation affect word/sentence/line boundaries.
- EditableText can replace all text, insert, copy, cut, delete and paste.
- Clipboard operations affect shared user-session state and therefore require explicit permission/evidence.
- Password or sensitive text roles must never be treated as ordinary readable text or retained automatically.

### Selection and value

- Selection supports selected-child inventory, select/deselect, clear and select-all.
- Selected-list indices differ from ordinary child indices in several methods.
- Implementations may reject unsupported multi-select operations.
- Value exposes minimum, maximum, increment, current numeric value and human-readable text.
- CurrentValue is writable, but protocol acceptance does not prove application persistence or correctness.

### Events

- Object events cover property, bounds, state, children, visible-data, selection, active-descendant, announcements, attributes, table changes and text/caret/selection changes.
- Window events cover create, destroy, activate, deactivate, minimize, maximize, restore and related lifecycle changes.
- Historical generic event payloads reuse string, integer and variant fields whose meaning depends on event type.
- Parts of the event schema remain underdocumented and future-property support is explicitly incomplete.
- Registry listener registration can be global or limited to an application bus name.
- Event streams are notifications, not total ordering, durable replay or proof that a fresh snapshot has been read.

## Security and authority findings

- The accessibility bus uses EXTERNAL authentication but its default bus policy broadly permits sending, receiving and owning names within the session bus.
- AT-SPI is designed to let assistive technologies inspect and control the desktop session; this necessarily exposes high-value UI and input authority.
- A client with session accessibility-bus access may observe application names, semantic text, states, dialogs, errors and structure across applications.
- Mutation interfaces can trigger actions, focus, text edits, selection, value changes, clipboard changes, scrolling and window geometry requests.
- D-Bus/session identity is not Ptah authorization.
- Accessibility enablement can be session-global and may affect newly launched applications.
- A compromised semantic automation client can become a cross-application observation and control channel.
- Ptah must mediate the bus through an isolated, scoped provider process and cannot expose raw accessibility-bus access to arbitrary plugins or callers.

## libatspi and Python direction

- libatspi is the primary client library around the D-Bus interfaces.
- Modern Python can use the GObject-introspection `Atspi` namespace directly.
- pyatspi is explicitly described as a legacy wrapper retained mainly for historical compatibility and bug fixes.
- New Ptah provider work should use direct libatspi/introspection bindings or another generated binding rather than building on pyatspi's legacy object model.
- pyatspi remains useful for Dogtail 1.x and existing test compatibility only.

## Dogtail completion patterns

- Dogtail converts the raw accessibility tree into a higher-level `Node`, `Action`, predicate and search API.
- It adds bounded backoff/retry for controls that appear asynchronously.
- It adds post-action delays because real applications may continue mutating dialogs after elements first appear.
- It detects defunct nodes, inaccessible children, unsupported actions and insensitive elements, while acknowledging that toolkit state can itself be wrong.
- Search failures produce explicit exceptions and diagnostic logs.
- Child traversal is bounded to avoid unbounded large trees.
- Action wrappers record/log semantic target and action before calling AT-SPI.
- Current Dogtail 2.x is a refactor intended to reduce legacy debt and prepare for future accessibility backends.
- Dogtail remains test/automation policy and convenience, not Ptah's canonical semantic-node model or durable Activity runtime.

## Xorg and Wayland composition

- AT-SPI semantic introspection remains broadly the same under Xorg and Wayland.
- Xorg traditionally permits direct synthetic pointer/keyboard input and global screen coordinates.
- GNOME Wayland restricts ordinary synthetic input and global coordinate access.
- Dogtail's Wayland path uses GNOME Ponytail with ScreenCast/RemoteDesktop APIs, GNOME Shell window introspection and libei-backed input.
- On Wayland, AT-SPI may expose only window-local element coordinates; the input bridge maps the active/selected window to global compositor-controlled input.
- GTK4 shadows, scaling and decoration offsets can make coordinate fallback variable; Dogtail documents disabling shadows for stable testing.
- The Wayland path is GNOME/compositor-specific and does not establish a universal Wayland automation API.
- Other compositors/desktops need separate providers or may remain semantic-read-only/visual-input-degraded.

## What this donor composition completes

- A primary semantic UI tree for Linux applications.
- Cross-toolkit roles, names, relations, state and interfaces.
- Direct semantic action, text, selection and value operations.
- Element/window geometry and semantic-to-coordinate correlation.
- Bulk initial snapshots and incremental event updates.
- Practical bounded search, wait, stale-node and diagnostic patterns.
- GNOME Wayland input through a compositor-approved remote-desktop/input bridge.
- A reusable semantic testing path for GTK/GNOME and partial Qt applications.
- A clear provider boundary that complements visual remote-display and coordinate automation from WP07.

## Important limitations for Ptah

- Applications/toolkits may expose incomplete, incorrect, stale, overly large or no accessibility tree.
- Custom canvases, games, GPU surfaces, embedded browsers, Electron content, remote desktops and proprietary toolkits may be partially or entirely opaque.
- Role, state, cache and interface behavior differs across GTK versions, Qt, Java, Chromium and other bridges.
- D-Bus object paths, bus names, application IDs and child indices are ephemeral aliases.
- AccessibleId is optional and application-defined.
- Events are not durable, complete, ordered Activity history.
- Cache is not authoritative and can use different schema variants.
- Collection support is inconsistent.
- semantic action success is not read-back proof.
- UI can change between locate and act; stale references and race conditions are normal.
- coordinate systems differ across Xorg, Wayland, scale factors, decorations, shadows, multiple monitors and remote-display sessions.
- GNOME Ponytail is GNOME-specific and has a smaller maturity/deployment surface than AT-SPI itself.
- Dogtail currently carries legacy compatibility and GPL-2.0 distribution implications.
- direct libatspi bindings expose lower-level behavior requiring a Ptah-native wait/reconcile layer.
- accessibility access can expose sensitive text and control unrelated applications in the same session.
- headless sessions, locked sessions and applications outside the active user session may not expose the expected bus or input route.
- virtualization/remote display can introduce a second semantic tree or no tree at all.
- AT-SPI does not provide screenshots, visual occlusion proof, durable application checkpoint, process identity or external side-effect receipts.

## Must not be inherited

- D-Bus names, object paths, AT-SPI application IDs, AccessibleIds or child indices as canonical Ptah identities;
- raw accessibility-bus access granted to arbitrary callers/plugins;
- session-global accessibility enablement hidden as an implementation detail;
- semantic tree availability assumed for every Linux application;
- a cached node used after application/window/provider generation changes;
- event receipt interpreted as a complete/fresh semantic snapshot;
- `DoAction`, text edit, selection or value Boolean success treated as proof of intended state;
- clipboard/password/sensitive text automatically captured or retained;
- coordinate action silently substituted for semantic action as equivalent evidence;
- Xorg and Wayland input paths treated as identical;
- GNOME Ponytail presented as universal Wayland support;
- Dogtail search delays used as Ptah's durable synchronization model;
- pyatspi selected for new native provider implementation merely because Dogtail historically uses it;
- accessibility-control permissions conflated with user-session ownership;
- unsupported toolkits silently reported as automated.

## Integration decision

**ADOPT AT-SPI/LIBATSPI AS THE PRIMARY LINUX SEMANTIC UI PROVIDER FOUNDATION; ADAPT DOGTAIL'S BOUNDED SEARCH/WAIT/DIAGNOSTIC PATTERNS; USE GNOME PONYTAIL AS A GNOME-WAYLAND INPUT COMPLETION ADAPTER.**

Recommended Ptah composition:

1. one Linux Application Session owns a semantic-provider connection scoped to its user/display/session;
2. the provider uses direct libatspi/introspection bindings rather than pyatspi for new code;
3. an initial bounded Semantic Snapshot is built from Cache/Collection/traversal with source-method and completeness flags;
4. every semantic node maps to a provider-local alias under the Application Session and Window generation;
5. Ptah assigns stable snapshot/node-reference identities only for the captured revision, never for the live D-Bus object forever;
6. event listeners update/invalidate projections and trigger targeted re-read; Events never replace snapshots;
7. query criteria combine role, name, description, state, relations, interfaces, attributes, AccessibleId and ancestry;
8. action requests state their intended effect and preferred method: semantic interface, keyboard, compositor input or visual coordinate;
9. mutation is separately authorized from observation;
10. every action receives semantic and/or visual post-condition read-back before completion;
11. Xorg, GNOME Wayland and remote-display input are explicit Provider variants;
12. GNOME Ponytail/libei runs behind a dedicated process and permission boundary;
13. opaque/unsupported applications degrade to visual/coordinate automation with a visible lower semantic-confidence class;
14. accessibility source, screenshot, window, process and Activity evidence are correlated rather than collapsed;
15. sensitive roles/content are redacted or excluded according to Workspace/caller policy;
16. AT-SPI and Dogtail remain replaceable adapters behind Ptah semantic contracts.

## Native Ptah semantic contracts required

### Semantic Context

```text
semantic_context_id
application_session_id
window_id
provider_generation
backend_type
backend_version
user_and_display_session
coordinate_space
capabilities
completeness
created_at
invalidated_at
```

### Semantic Snapshot

```text
snapshot_id
semantic_context_id
source_method
captured_at
event_cursor_or_generation
root_alias
node_count
truncated_or_partial
errors_and_unsupported_interfaces
artifact_or_hash_reference
```

### Semantic Node Snapshot

```text
semantic_node_id
snapshot_id
provider_alias
application_alias
parent_node_id
child_order
role
name
description
locale
accessible_id
states
relations
interfaces
attributes
text_summary_policy
value
selection_summary
geometry
coordinate_space
sensitivity_or_privacy_class
```

### Semantic Query

```text
query_id
context_or_snapshot
scope
role_name_state_relation_interface_attribute_filters
text_or_regex
ancestor_descendant_constraints
result_limit
timeout_and_retry_policy
```

### Semantic Action Request/Result

```text
action_request_id
activity_operation_attempt
semantic_context_and_snapshot
node_reference
requested_intent
selected_backend_method
observation_or_mutation_permission
precondition
provider_call_result
postcondition_readback
visual_or_semantic_evidence
stale_or_race_status
```

## Permission model

Separate capabilities are required for:

- enumerate applications/windows;
- read semantic roles/names/states;
- read ordinary text;
- read sensitive/password/private text;
- subscribe to Events;
- request focus;
- invoke semantic actions;
- edit text/clipboard;
- change selection/value;
- synthesize keyboard/pointer input;
- capture screenshot/video;
- cross-application observation/control.

The raw accessibility bus is never the public permission surface.

## Evidence and proof rules

1. semantic snapshot proves only what the application/toolkit exposed at capture time;
2. event proves a notification was received, not that state is now known;
3. action-call success proves only provider acceptance;
4. semantic postcondition proves the accessibility tree changed as expected;
5. visual postcondition proves pixels/window changed as expected;
6. application/process/log/file/network read-back may be needed for authoritative side effects;
7. disagreement between semantic and visual evidence is retained;
8. fallback method and reduced confidence are explicit;
9. stale node or provider generation produces a new locate/read attempt, never silent reuse;
10. unsupported/opaque UI remains a negative capability result.

## Licence decision

- at-spi2-core/libatspi: LGPL-2.1; dynamic library use and any modifications/distribution require notice/source obligations review.
- pyatspi package metadata: LGPL-2.0-or-later; compatibility-only.
- Dogtail: GPL-2.0; subprocess/use for testing is different from copying/linking/embedding and must be reviewed before distribution.
- GNOME Ponytail, libei, GNOME Remote Desktop/Mutter interfaces, toolkit bridges and distribution packages require exact source pin and licence review before dependency approval.
- Ptah semantic contracts remain independently implemented and do not require copying Dogtail code.

## Exit strategy

Ptah's semantic contracts remain backend-neutral. Linux providers may use AT-SPI, future AccessKit/Newton bridges, toolkit-native automation, browser accessibility trees, visual/coordinate automation or application-specific APIs without changing Application Session, Semantic Snapshot, Action or evidence identity.

## Validation required

1. Capture equivalent semantic snapshots from GTK3, GTK4, Qt and one Electron/Chromium application and retain completeness differences.
2. Correlate AT-SPI application/window aliases with Ptah Application Session, process and Window generation.
3. Query by role/name/state/relation/interface/AccessibleId and prove bounded behavior on a large/virtualized tree.
4. Invalidate a cached node after window close/reopen and reject stale action.
5. Subscribe to child/state/text/window events, deliberately lose an event and reconcile through a fresh snapshot.
6. Invoke Action, focus, text edit, selection and value changes with semantic postcondition read-back.
7. Prove Boolean method success without matching postcondition is not reported as complete.
8. Compare Xorg and GNOME Wayland coordinate/input paths under multiple scale factors and monitors.
9. Run GNOME Ponytail in a dedicated scoped process and deny unrelated session/network/filesystem authority.
10. Deny cross-application observation/mutation when the caller is scoped to one Application Session.
11. Redact password/sensitive text and clipboard content from retained evidence.
12. Exercise an opaque/custom-canvas application and visibly degrade to visual automation without claiming semantic support.
13. Compare semantic node extents with screenshots and retain disagreement/occlusion.
14. Kill/restart the accessibility bus, application, provider and compositor input bridge and recover with new generations.
15. Run headless and remote-display sessions and record unsupported/partial paths honestly.
16. Replace Dogtail/high-level search logic with a Ptah-native implementation without changing semantic contracts.
17. Replace AT-SPI for one provider with a future backend without changing Application/Activity identities.
