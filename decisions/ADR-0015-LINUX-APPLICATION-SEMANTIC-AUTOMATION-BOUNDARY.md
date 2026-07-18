# ADR-0015 — Linux Application Semantic Automation Boundary

**Status:** ACCEPTED FOR PHASE 0B CONTRACT DESIGN  
**Date:** 2026-07-18  
**Phase:** Phase 0A Linux semantic completion

## Context

ADR-0010 established Linux Application Providers, Application Sessions, Windows, display/visual state and visual automation, but deliberately retained one completion gap: dedicated Linux AT-SPI semantic automation.

AT-SPI2 exposes toolkit-neutral accessibility trees, roles, names, states, relations, geometry, actions, text, values, selections, tables, events and caches. It does not provide Ptah's durable identity, permissions, Application/Window correlation, event reconciliation, control leases or proof.

The gap cannot be closed by treating:

- one D-Bus object path as a stable UI element;
- one role/name/index selector as permanent identity;
- `DoAction=true` as verified completion;
- one coordinate click as semantic automation;
- one session-wide accessibility bus as safe multi-tenant access;
- Dogtail/Ponytail toolkit workarounds as universal Linux behavior.

Full composition and proof plan: `work-packages/PHASE-0A-LINUX-AT-SPI-SEMANTIC-COMPLETION.md`.

## Decision

Ptah will define a provider-neutral Linux semantic-automation contract around:

1. **Semantic Provider and generation**;
2. **Semantic Snapshot**;
3. **Accessible Node Observation**;
4. **Semantic Target and Selector Revision**;
5. **Selector Evaluation, Candidate and Ambiguity**;
6. **Semantic Event and reconciliation**;
7. **semantic coverage/availability state**;
8. **semantic action, raw input and visual-action families**;
9. **coordinate-space and visual correlation**;
10. **Application/Window control lease and permission scope**;
11. **UI Action Receipt and proof levels**.

AT-SPI2/libatspi is the primary Linux implementation donor. Dogtail, gnome-ponytail-daemon and Accerciser are completion/reference components, not Ptah identity or truth.

---

# Semantic identity

AT-SPI D-Bus application names and object paths remain adapter-local observations.

A stable Ptah Semantic Target represents the caller's intent to reacquire an element across current Snapshots using a versioned selector based on combinations of:

- Application Session/package/process and Window identity;
- accessible ID;
- role and supported interfaces;
- name, description and text;
- states and attributes;
- relations and bounded tree path;
- value, selection, table and document context;
- geometry and visual correlation.

Before mutation, Ptah reacquires the Target against a current Provider/Application/Window generation. Stale adapter references are rejected.

Zero, one and multiple selector candidates remain distinct outcomes. Multiple plausible matches are not silently resolved by choosing the first item.

---

# State model

A Semantic Snapshot is a bounded immutable observation of one Application/Window/subtree at one time.

State is built from:

1. an initial bulk/tree capture;
2. registered AT-SPI events;
3. periodic/action-triggered reconciliation;
4. full reset after Provider, bus, Application or Window generation changes.

Events update cached observations but are not complete durable truth. Event loss, cache mismatch, unsupported signatures, defunct nodes or toolkit bugs move state to partial/reconciling rather than fabricating continuity.

Coverage states include at least:

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

---

# Action and input separation

Ptah separates:

- semantic inspection/query;
- semantic Action invocation;
- focus and scroll;
- text/editable-text;
- value;
- selection/table/document operations;
- raw pointer and keyboard input;
- clipboard access;
- visual/coordinate automation;
- human takeover.

Read-only semantic inspection does not grant semantic mutation, raw input, clipboard or screenshot/video access.

X11 input and Wayland input are separate Provider capabilities. GNOME Wayland may use Ponytail/RemoteDesktop/libei, but that does not imply universal Wayland/compositor support.

Semantic actions may remain available when raw input is unavailable. Unsupported raw-input paths are reported explicitly.

---

# Coordinate and visual boundary

AT-SPI geometry can use screen, top-level Window or parent-relative coordinates. Ptah records exact coordinate source plus monitor topology, scaling, compositor/window surface and visual stream/screenshot transforms.

Geometry disagreement, stale bounds, decoration/shadow offsets or ambiguous surface mapping block raw input or require visual reacquisition. Ptah does not apply guessed universal offsets.

Semantic and visual evidence can be correlated but neither silently overwrites disagreement from the other.

Visual fallback remains an explicit fallback from ADR-0010 and is never described as semantic success.

---

# Security and control

AT-SPI is a privileged desktop-session interface capable of exposing and controlling sensitive applications.

Therefore:

- mutually untrusted Workspaces do not share one accessibility bus/desktop session;
- public clients never receive raw session-wide D-Bus authority;
- semantic tree/event access is application/window scoped;
- semantic mutation and raw input require explicit permissions and the current control lease/fencing token;
- sensitive text, clipboard and visual evidence are classified/redacted;
- application/toolkit semantic metadata is treated as an observation/claim, not inherently trusted proof.

---

# Proof boundary

Every mutating semantic/raw/visual action is a Ptah Activity attempt retaining:

- pre-action Semantic Snapshot;
- selector evaluation and ambiguity;
- Provider/Application/Window generation;
- control lease/fencing token;
- exact adapter method/action and parameters;
- command response and relevant events;
- post-action semantic read-back;
- visual evidence where permitted;
- application/domain result where available;
- limitations and disagreement.

Proof levels remain separate:

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

A semantic action boolean, input-injection acknowledgement or coordinate click does not alone prove the operation completed.

---

# Donor roles

## AT-SPI2/libatspi

- primary Linux semantic tree/state/action/event implementation;
- adapter-local D-Bus references;
- bounded cache and event reconciliation required;
- LGPL obligations apply.

## Dogtail

- high-level selector/test/automation reference and optional wrapped Facility;
- not canonical state or selector identity;
- GPL-2.0-or-later requires formal integration/distribution strategy.

## gnome-ponytail-daemon

- one GNOME-Wayland raw-input/surface-coordinate Provider;
- separate high-risk control permission;
- not universal Wayland support;
- GPL-2.0-or-later external packaging boundary.

## Accerciser

- optional specialist inspection/debug Application;
- useful event/tree/API validation donor;
- not runtime truth.

## AccessKit/Newton-style future provider

- retained as a future push-based/sandbox-aware provider replacement direction;
- not required for v1 or represented as implemented capability.

---

# Consequences

## Positive

- Linux semantic automation now fits the same Application/Window/Activity model as other platforms.
- toolkit-neutral semantics can reduce fragile coordinate automation.
- stale UI objects and ambiguous selectors are explicit.
- event-driven state gains reconciliation rather than blind cache trust.
- semantic, raw and visual control permissions remain separate.
- action results gain post-action proof.
- session-wide accessibility authority is contained.
- partial/unavailable semantics degrade honestly.
- future provider replacement preserves Ptah identities.

## Costs

- Semantic Snapshot/selector/event schemas are substantial.
- toolkit/version/compositor conformance testing is required.
- AT-SPI event/cache inconsistencies require reconciliation logic.
- coordinates must be correlated across semantic, Window, compositor and visual spaces.
- Wayland raw input remains compositor-specific.
- accessibility-session isolation adds deployment complexity.
- LGPL/GPL component boundaries require packaging/legal care.

## Do-not-break rules

> Never use an AT-SPI D-Bus object path, role/name/index selector or Dogtail node object as stable Ptah identity.

> Never treat accessibility metadata, event delivery, `DoAction=true`, focus success or injected input as application completion proof.

> Never share one privileged accessibility session across mutually untrusted Workspaces or silently turn read-only semantic access into raw input authority.

> Never describe GNOME/Ponytail support as universal Wayland automation or visual fallback as semantic success.

---

# Required proof before freeze

1. Capture semantic state from multiple Linux toolkits and retain coverage differences.
2. Reject stale objects after widget/Application/bus generation change.
3. Expose selector ambiguity rather than choosing the first candidate.
4. Detect deliberately lost events through reconciliation.
5. Perform semantic text/value/selection/focus/scroll/action operations with read-back.
6. Correlate semantic geometry and visual evidence under scaling/multi-monitor/compositor cases.
7. Keep X11, GNOME Wayland and unsupported Wayland raw-input paths distinct.
8. Prevent cross-Workspace accessibility-session access.
9. Reject stale control-lease actions.
10. Handle canvas/custom UI as partial or visual-only.
11. Preserve semantic/visual disagreement as evidence.
12. Replace AT-SPI with a mock/future Provider without changing Ptah Target, Activity or Receipt identity.
