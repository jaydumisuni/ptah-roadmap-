# Phase 0A — Linux AT-SPI Semantic Automation Completion

**Status:** COMPLETE — CLOSED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Runtime code:** NOT STARTED

## Purpose

Close the dedicated Linux semantic-automation gap retained by WP07B and ADR-0010 without reopening the accepted Application Provider, Window, display or visual-automation architecture.

This completion defines how a Linux Application Session can expose semantic UI state and actions through AT-SPI2 while preserving:

- stable Ptah identity rather than D-Bus object identity;
- exact Application/Window/provider generations;
- event-driven state with reconciliation;
- separate semantic and raw-input permission classes;
- visual correlation and honest fallback;
- action Receipts and post-action proof;
- future replacement by a push-based accessibility provider.

## Evidence recovered

### Existing Ptah foundations

- `decisions/ADR-0010-APPLICATION-PROVIDER-WINDOW-DISPLAY-BOUNDARY.md`
- `work-packages/PHASE-0A-WP07B-APPLICATION-RUNTIME.md`
- `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`
- `decisions/ADR-0004-OPERATION-RECEIPTS-PROOF-LEVELS.md`
- `decisions/ADR-0012-HUMAN-WORKSPACE-SHELL-PANEL-CONTROL-BOUNDARY.md`
- `work-packages/PHASE-0A-WP08-BROWSER-LIVE-RESEARCH.md`

These already establish:

- Application Provider, Application Session and Window are separate identities;
- display/visual state, semantic state and control channels remain distinct;
- visual automation is an explicit fallback rather than semantic truth;
- human and automation control uses leases/fencing;
- command return, runtime state and verified result are separate proof levels;
- accessibility and mobile/desktop UI behavior are first-class.

### Completion donor

- `donors/AT-SPI2-LINUX-SEMANTIC-AUTOMATION.md`

Composite external evidence:

- AT-SPI2 Core/libatspi;
- Dogtail;
- gnome-ponytail-daemon;
- Accerciser;
- future AccessKit/Newton-style push architecture as an exit path.

## Composite direction

```text
Linux Application Session
  Window and visual/display Provider
  optional AT-SPI Semantic Provider
    initial bounded tree/cache capture
    semantic snapshots and node observations
    events and reconciliation
    semantic selectors and target reacquisition
    semantic actions/text/value/selection/focus/scroll
  optional Input Provider
    X11 input injection
    GNOME Wayland Ponytail/libei/RemoteDesktop path
    future compositor-specific providers
  visual fallback Provider
    screenshots/pixels/visual targeting
  Ptah Activity/Lease/Receipt/Proof contracts
```

No AT-SPI, Dogtail, Ponytail, toolkit or compositor identifier becomes canonical Ptah identity.

---

# 1. Semantic Provider boundary

A Linux Application Session may expose zero or more semantic Provider instances.

The Provider identifies:

```text
semantic_provider_id
application_session_id
provider_implementation
provider_version
provider_generation
application_generation
window_generation
desktop_session_id
compositor_or_display_server
atspi_bus_and_registry_instance
application_bus_name
toolkit_name_and_version
atspi_protocol_and_library_version
locale
scale_and_monitor_topology
connected_at
state
limitations
```

Provider states include:

```text
initializing
ready
partial
stale
reconciling
disconnected
permission_blocked
unsupported
failed
```

Provider generation changes after:

- accessibility bus/registry restart;
- Provider process restart;
- Application process restart;
- Window replacement that invalidates the prior semantic tree;
- explicit full reset/reconnect.

Observations from earlier generations cannot authorize current actions.

---

# 2. Semantic Snapshot and node observations

## 2.1 Snapshot

A Semantic Snapshot is an immutable bounded observation:

```text
semantic_snapshot_id
semantic_provider_id
application_session_id
provider_application_window_generation
capture_started_at
capture_completed_at
capture_method
root_references
node_count
truncation_or_budget
cache_mask
locale_scale_monitor_context
event_cursor_or_sequence
coverage_state
limitations
source_receipt
```

Capture methods may include:

- cache bulk read;
- bounded recursive traversal;
- subtree capture;
- action-targeted refresh;
- post-event reconciliation;
- post-action read-back.

## 2.2 Accessible Node Observation

```text
semantic_observation_id
semantic_snapshot_id
adapter_reference
application_and_window_context
parent_observation_or_adapter_reference
child_index_and_child_count
role_and_localized_role
name_description_help_text
accessible_id
locale
states
attributes
relations
supported_interfaces
actions_and_keybindings
text_editable_text_hypertext_metadata
value_and_selection_metadata
table_table_cell_metadata
component_geometry_coordinate_space_layer_z_order
process_and_toolkit_observations
available_defunct_or_error_state
observed_at
```

D-Bus name/object path is an adapter reference only.

## 2.3 Coverage state

```text
semantic_complete
semantic_partial
visual_only
semantic_unavailable
stale_or_defunct
provider_disconnected
permission_blocked
capture_truncated
```

Coverage is scoped to the captured application/window/subtree and time. A Provider is not labelled globally complete merely because one screen was accessible.

---

# 3. Stable Semantic Target and selector

A Semantic Target is the caller's stable intent to reacquire a UI element or semantic region across Snapshots.

```text
semantic_target_id
application_or_package_scope
window_scope
selector_revision
expected_role_or_interfaces
risk_and_action_scope
created_by
```

A selector may combine:

- Application Session/package/process/Window identity;
- accessible ID;
- role;
- name/description/localized text;
- states and attributes;
- supported interfaces/actions;
- labelled-by/controller/controlled-by/popup/embedding relations;
- ancestor/descendant path;
- text/value/table/document context;
- geometry and screenshot correlation;
- bounded child/index or nth-candidate rule.

Selector evaluation produces:

```text
selector_evaluation_id
semantic_target_id
semantic_snapshot_id
provider_generation
all_candidates
candidate_scores_and_reasons
hard_mismatches
ambiguity_state
chosen_observation_or_none
limitations
```

## 3.1 Ambiguity rule

- zero matches returns not-found/stale/coverage information;
- one validated match may proceed;
- multiple plausible matches remain ambiguous unless caller policy explicitly provides a deterministic disambiguation;
- Ptah never silently clicks the first matching name/role/index.

## 3.2 Reacquisition rule

Before mutation, Ptah reacquires the target against a current Snapshot/provider generation. A prior adapter reference cannot be reused merely because the visible label appears unchanged.

---

# 4. Event-driven state and reconciliation

## 4.1 Initial state

The Provider obtains a bounded initial tree/cache Snapshot.

## 4.2 Events

Relevant subscriptions include:

- property and attribute change;
- state/focus change;
- children add/remove;
- bounds/visible-data change;
- selection/model/table change;
- text/caret/selection change;
- active descendant;
- window create/activate/deactivate/reparent/destroy.

Each received event records:

```text
semantic_event_id
semantic_provider_id
provider_application_window_generation
source_adapter_reference
event_class_type_detail
raw_payload
received_at
sequence_or_local_cursor
correlated_observation_or_target
applied_to_cache
limitations
```

## 4.3 Reconciliation

Events are advisory state updates, not complete durable truth. Reconciliation occurs:

- periodically under a bounded budget;
- after target-affecting events;
- before high-risk actions;
- after semantic/raw-input actions;
- after suspected event loss, malformed payload or cache inconsistency;
- after window/application/bus lifecycle changes.

A lost event, unsupported cache signature or toolkit inconsistency moves the Provider/Snapshot to partial or reconciling state rather than fabricating continuity.

---

# 5. Semantic actions and input separation

## 5.1 Action families

```text
semantic_inspect
semantic_action
semantic_focus
semantic_scroll
semantic_text_read
semantic_text_edit
semantic_value
semantic_selection
semantic_table_or_document
raw_pointer
raw_keyboard
clipboard
visual_coordinate_action
human_takeover
```

## 5.2 Permission classes

Read-only semantic inspection does not grant:

- `DoAction`;
- text/value/selection mutation;
- focus/scroll mutation;
- raw keyboard/pointer;
- clipboard access;
- screenshot/video access;
- cross-application/session access.

Every control action requires the current Application Session/Window control lease and fencing token where applicable.

## 5.3 X11 and Wayland

- X11 input injection and Wayland input are distinct Provider capabilities.
- Semantic actions may work when raw coordinate input is unavailable.
- GNOME Wayland raw input may use Ponytail/RemoteDesktop/libei under the user's desktop session permissions.
- Ponytail support does not imply KDE, wlroots, Weston or universal Wayland support.
- Unsupported compositors expose explicit `raw_input_unavailable` state.
- Headless/remote sessions declare their own input and compositor profile.

## 5.4 Coordinate spaces

Geometry records exact coordinate context:

- screen/global;
- top-level Window;
- parent-relative;
- compositor surface;
- rendered stream/display coordinates;
- screenshot/pixel Artifact coordinates.

Conversions retain scaling, monitor, Window bounds, decoration/shadow and compositor source. A geometry mismatch blocks raw input or forces visual reacquisition rather than applying a guessed offset.

---

# 6. Action Activity and proof

Every mutation is a Ptah Activity/attempt.

## 6.1 Pre-action evidence

- current Application Session/Window/provider generation;
- current control lease/fencing token;
- current Semantic Snapshot;
- target selector evaluation and ambiguity state;
- relevant visual/screenshot region when permitted;
- permission and sensitive-data classification.

## 6.2 Command evidence

- exact semantic interface/action or raw-input Provider method;
- adapter reference used only for that current generation;
- parameters/coordinate space;
- command response/boolean/error;
- Provider Events and logs.

## 6.3 Post-action evidence

- relevant events;
- post-action target/subtree/full Snapshot;
- text/value/state/focus/selection/read-back;
- screenshot/visual comparison when permitted;
- application/domain result or resulting Object/Artifact where available;
- remaining ambiguity/limitations.

A boolean `DoAction=true`, input-injection acknowledgement or visual click does not alone become `operation-complete`.

Proof levels remain:

```text
command_accepted
action_invoked
ui_state_observed
visual_state_observed
application_result_observed
authoritative_external_result
reviewed
accepted
```

---

# 7. Security and session boundary

## 7.1 Session-scoped power

AT-SPI accessibility access can inspect and control sensitive applications within a desktop session. It is therefore a privileged automation interface.

## 7.2 Isolation rule

- mutually untrusted Workspaces do not share one accessibility bus/desktop session;
- the Semantic Provider runs inside or adjacent to the owning Application/desktop Provider with scoped IPC;
- public clients never receive raw session-wide D-Bus access;
- Ptah exposes only policy-filtered semantic methods/observations;
- event subscriptions and tree capture are limited to approved applications/windows;
- control actions require lease and permission;
- sensitive text, credentials and clipboard content are redacted/classified.

## 7.3 Provider trust

Application/toolkit accessibility metadata is an observation/claim. Malicious or broken applications can expose misleading roles, names, geometry, actions or events. Ptah may correlate with pixels, process/window identity and application outcomes, but never treats semantic metadata as inherently trusted proof.

---

# 8. Partial semantics and visual fallback

## 8.1 Honest degradation

When semantics are incomplete:

- retain the exposed subtree and missing-interface/coverage evidence;
- label the state `semantic_partial`;
- use semantic targeting for accessible regions only;
- use visual automation only through an explicit visual action path;
- never label coordinate/pixel interaction as semantic success.

When semantics are absent:

- label `visual_only` or `semantic_unavailable`;
- require the visual Provider and its stronger uncertainty/proof policy;
- allow human takeover where needed.

## 8.2 Correlation

Semantic and visual evidence can be correlated by:

- Window identity/generation;
- geometry and coordinate transforms;
- screenshot region;
- role/name/text versus rendered text/object;
- focus/state/event changes;
- application/domain result.

Disagreement becomes retained evidence rather than one source silently overwriting the other.

---

# 9. Accessibility testing and inspection

An accessibility/test Activity may produce:

- tree/snapshot Artifact;
- missing names/labels/actions/states/interfaces Claims;
- broken relation/role/geometry/event findings;
- selector stability findings;
- toolkit/version coverage matrix;
- screenshot/semantic overlays;
- reproduction steps and receipts.

Accerciser may run as a specialist human inspection Application. Dogtail may be wrapped as an optional test Facility. Neither becomes the canonical state/identity layer.

---

# 10. Future provider replacement

Ptah semantic contracts are provider-neutral enough to support:

- AT-SPI2/libatspi;
- future AccessKit/Newton push-based providers;
- browser accessibility trees;
- Windows UIA;
- macOS AX;
- Android UIAutomator/Accessibility;
- iOS XCUITest/accessibility;
- application-specific semantic APIs;
- visual-only providers.

The next-generation GNOME proposal is useful because it reinforces:

- per-surface trees;
- push snapshots and atomic updates;
- compositor-derived global focus/surface context;
- sandbox mediation;
- local client copies and fewer round trips.

It remains a future adapter target, not a v1 implementation dependency.

---

# 11. Requirement closure verdict

## Linux semantic Application automation — CLOSED FOR PHASE 0B CONTRACT DESIGN

Closed direction:

- AT-SPI2 is the primary Linux semantic-state/action Provider candidate;
- stable Ptah Semantic Target identity is separate from D-Bus references;
- bounded Snapshots plus events plus reconciliation form state;
- selector ambiguity and stale/defunct references are explicit;
- semantic actions, raw input and visual automation are separate capabilities/permissions;
- X11 and compositor-specific Wayland input Providers are distinct;
- action return remains separate from UI/application proof;
- accessibility bus/session access is isolated and scoped;
- partial semantics fall back honestly;
- future accessibility providers remain replaceable.

## Existing requirements extended

- `APP-002` Linux graphical/native runtime;
- `SESSION-001` Application/Window state and recovery;
- `UI-001/UI-002` operator semantic/visual projections and evidence;
- `OBS-001` semantic events and action correlation;
- `PROV-001` UI action/evidence bundles;
- `CORE-004` semantic/input Facility contributions.

No Linux semantic/runtime implementation is authorized by this closure.

---

# 12. Phase 0B contracts required

1. Semantic Provider and generation schema.
2. Semantic Snapshot and Accessible Node Observation schema.
3. Semantic Target and Selector Revision schema.
4. Selector Evaluation/Candidate/Ambiguity schema.
5. Semantic Event and reconciliation schema.
6. semantic coverage/availability state family.
7. semantic action, raw input and visual action Facility contracts.
8. coordinate-space and visual-correlation schema.
9. application/window control lease and permission schema.
10. sensitive-text/clipboard/screenshot classification schema.
11. UI Action Receipt and proof-level schema.
12. provider/toolkit/compositor conformance corpus.
13. AT-SPI-to-future-provider migration tests.

---

# 13. Required proof before freeze

1. Capture GTK3, GTK4, Qt and browser/WebKit semantic trees and retain coverage/limitations.
2. Destroy/recreate a widget and reject stale adapter references.
3. Match selectors by ID, role/name, relation path and text with ambiguity retained.
4. Apply events to a cache, deliberately lose one and detect drift through reconciliation.
5. Restart the application/accessibility bus and invalidate prior generations.
6. Invoke semantic actions and keep command response separate from UI/application outcome.
7. Exercise text, value, selection, focus and scroll interfaces with post-action read-back.
8. Correlate semantic geometry and screenshots under scaling/multi-monitor/GTK4 decoration cases.
9. Run GNOME Wayland raw input through Ponytail under a separate permission/Provider.
10. Reject unsupported compositor raw-input claims honestly.
11. Prove two mutually untrusted Workspaces cannot access one another's accessibility session.
12. Expire/revoke control lease and reject stale semantic/raw-input actions.
13. Handle custom/canvas UI as semantic-partial or visual-only.
14. Produce accessibility findings as Claims/Artifacts with reproduction evidence.
15. Replace AT-SPI with a mock/future Provider without changing Semantic Target, Activity or Receipt identity.

## Closure conclusion

Ptah now has a complete Linux Application semantic-automation direction that fits the existing Application/Window/visual architecture. AT-SPI2 supplies the semantic transport and object/action interfaces, while Ptah supplies stable identities, scoped access, event reconciliation, target reacquisition, action proof and honest visual fallback.
