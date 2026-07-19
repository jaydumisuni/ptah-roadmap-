# Ptah Phase 0B — Entity Kind Registry WP09 Supplement

**Registry:** `ptah.entity-kind`  
**Candidate version:** `0.1.0`  
**Status:** CANDIDATE  
**Date:** 2026-07-19

This supplement extends the common registry for WP09 without mutating earlier registry history.

## Application runtime

| Token | Meaning |
|---|---|
| `application.revision` | Immutable Application source/package/executable revision role |
| `application.compatibility` | Directional exact-context install/launch/display/semantic/checkpoint compatibility |
| `application.checkpoint` | Application-specific checkpoint component over exact Session/process/window/display/semantic generations |
| `application.recovery_verification` | Post-restore functional/application recovery result |
| `application.window_observation` | Provider observation of one Window incarnation/geometry/state |
| `application.display_observation` | Health/quality/geometry/input observation for one Display Session |

Existing kinds remain canonical:

- `application.application`;
- `application.installation`;
- `application.session`;
- `application.window`;
- `application.display_session`;
- `runtime.process`.

## Browser

| Token | Meaning |
|---|---|
| `browser.binary_revision` | Immutable Browser Binary build/package/executable revision |
| `browser.profile_revision` | Immutable policy/storage/configuration revision of one Browser Profile |
| `browser.navigation` | One Page/Frame navigation revision and resulting document identity |
| `browser.challenge_state` | Explicit authentication/MFA/captcha/consent/manual-completion state revision |
| `browser.checkpoint` | Browser Profile/Process/Context/Page checkpoint component |
| `browser.recovery_verification` | Post-restore Browser functional/navigation/authentication verification |
| `browser.evidence_bundle` | Manifest of source/DOM/accessibility/pixel/trace/network/console evidence for exact Page/navigation generations |

Existing kinds remain canonical:

- `browser.binary`;
- `browser.profile`;
- `browser.process`;
- `browser.context`;
- `browser.page`;
- `browser.frame`;
- `browser.popup`;
- `browser.download`;
- `browser.challenge`.

`browser.challenge` remains the durable challenge identity; `browser.challenge_state` is one immutable state revision.

## Semantic UI and control

| Token | Meaning |
|---|---|
| `semantic.node_snapshot` | One immutable semantic-node projection inside one Snapshot |
| `semantic.event` | Provider-origin semantic change notification under exact Context/generation |
| `semantic.target_result` | Selector result/reacquirable target binding under one Snapshot/generation |
| `semantic.action_attempt` | One physical semantic/API/raw/visual input try mapped to WP02 Attempt |
| `semantic.visual_evidence` | Captured visual region/screenshot/difference evidence for one semantic/action context |

Existing kinds remain canonical:

- `semantic.context`;
- `semantic.snapshot`;
- `semantic.target`;
- `semantic.selector`;
- `semantic.action`;
- `semantic.action_result`.

`semantic.target` is the durable reacquirable target specification where required; `semantic.target_result` records one resolved match set at one Snapshot/generation.

## Human Shell

| Token | Meaning |
|---|---|
| `shell.panel_binding` | Exact entity/runtime binding of one Panel Instance |
| `shell.projection` | Permission-filtered UI projection over canonical runtime/evidence records |
| `shell.responsive_projection` | Device-class-specific derived layout presentation over one Layout Revision |
| `shell.client_observation` | Connection/viewport/accessibility/resource observation for one Shell Client Session |

Existing kinds remain canonical:

- `shell.client`;
- `shell.session`;
- `shell.panel_type`;
- `shell.panel`;
- `shell.layout_profile`;
- `shell.layout_revision`;
- `shell.view_state`;
- `shell.control_transfer`.

## Rules

1. `runtime.process` remains the canonical supervised process identity; platform PIDs are Aliases.
2. `runtime.lease` remains the typed control-authority root; WP09 uses control Lease types and does not create a competing Shell/Semantic lease entity.
3. Application/Browser checkpoint components remain inside WP05 checkpoint bundles and do not replace them.
4. Application/Browser recovery verification remains separate from checkpoint integrity, compatibility and runtime restore.
5. Shell projection/panel/layout records never become canonical Activity/Application/Browser/Device state.
6. Registration does not authorize runtime/UI implementation or public visibility.
