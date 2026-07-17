# Donor Record — OpenVSCode Server and code-server

**Phase:** 0A / WP09  
**Status:** FIRST-PASS COMPLETE — OPTIONAL VS CODE BROWSER COMPATIBILITY PATHS  
**Inspected:** 2026-07-18

## Identity

### OpenVSCode Server

- Canonical URL: https://github.com/gitpod-io/openvscode-server
- Default branch: `main`
- Pinned commit: `2bfb814c5215c51a10e80c2cb1b58ed91068ad8b`
- Licence: MIT
- Classification: minimal upstream-VS-Code-to-browser server distribution

### code-server

- Canonical URL: https://github.com/coder/code-server
- Default branch: `main`
- Pinned commit: `22b0a3eeabd7f34a1185839553b88f81f1718ceb`
- Pinned package version: `4.108.3`
- Licence: MIT, with bundled third-party notices
- Classification: opinionated browser-hosted VS Code distribution with authentication, proxying and mobile/PWA adaptations

- Ptah targets: optional coding-focused compatibility surface, browser-based editor/terminal, existing VS Code workflows and extension compatibility

## Files/components inspected

- OpenVSCode `README.md`
- OpenVSCode `LICENSE.txt`
- code-server `docs/README.md`
- code-server `docs/guide.md`
- code-server `LICENSE`
- product/security and extension-marketplace boundaries

## Verified capabilities and patterns

### OpenVSCode Server

- Runs the upstream open-source VS Code codebase as a browser-accessible server.
- Intentionally keeps changes minimal and upstream-compatible.
- Supports an optional connection token or token file.
- Can run in OCI/container environments.
- Offers a straightforward route for users who want familiar VS Code behavior remotely.

### code-server

- Runs VS Code in a browser with one consistent development environment on a remote machine.
- Adds integrated password authentication, proxying, service/install scripts, PWA/mobile changes and configuration.
- Uses Open VSX by default because Microsoft's extension marketplace terms are product-restricted.
- Documents that the server must never be exposed directly without authentication and encryption because terminal access can take over the machine.
- Listens on localhost by default and supports reverse-proxy/SSH/TLS deployment patterns.
- WebSockets are part of the browser/server communication path.
- Proxies application/service ports through the browser origin.
- Adds practical iPad/mobile adaptations beyond stock browser VS Code.

## What these donors complete

- Optional familiar VS Code browser experiences without requiring Ptah to recreate editor/SCM/extension UX.
- A compatibility route for coding-centric users and existing extension workflows.
- Practical deployment, authentication, WebSocket and service-port proxy lessons.
- Mobile/PWA lessons from code-server.
- A low-change upstream compatibility reference through OpenVSCode Server.
- Open VSX extension-distribution implications.

## Important limitations for Ptah

- Both products remain VS Code-centric IDE surfaces, not complete Ptah Workspaces.
- They organize around files/editors/terminals rather than Objects, Activities, Browsers, Devices, applications and proof.
- Their workspace/session/layout IDs are not Ptah identities.
- Terminal and port proxy access can grant broad machine authority.
- Extension hosts introduce supply-chain, filesystem, process and network risk.
- Marketplace compatibility and extension licences vary.
- OpenVSCode's minimal distribution lacks Ptah-native authentication, panel governance and operational status semantics.
- code-server's integrated auth is not a replacement for Ptah identity, roles, Workspace permissions or lease/fencing.
- Browser reconnect restores a client experience, not underlying Activity truth.
- Mobile changes improve VS Code usage but do not make a dense IDE the correct phone interface for Ptah.
- Port proxies can create internal-network exposure if target selection is not scoped.

## Must not be inherited

- either product used as Ptah's universal shell;
- VS Code workspace/window IDs as canonical Ptah Session/Panel identity;
- integrated code-server password auth replacing Ptah Auth;
- arbitrary port proxying or terminal access exposed to untrusted callers;
- unrestricted extension installation or Microsoft marketplace assumptions;
- coding-first navigation used for Device, firmware, media, research and evidence workflows;
- browser reconnect presented as runtime recovery;
- stock branding or extension schemas exposed as Ptah's public contract;
- one VS Code process shared across unrelated Workspaces without isolation.

## Integration decision

**SUPPORT OPENVSCODE SERVER AND CODE-SERVER AS OPTIONAL CODING-COMPATIBILITY PROVIDERS, NOT THE PRIMARY PTAH SHELL.**

Recommended roles:

1. OpenVSCode Server for minimal upstream-compatible coding sessions;
2. code-server where its deployment/PWA/mobile/proxy features are useful;
3. both hosted as Application/Workspace presentation providers behind Ptah Auth and scoped connection tokens;
4. Ptah-native Home, Activity, Object, Browser, Device, Application and evidence panels remain outside and above them;
5. extension installation is governed through Ptah Facility/plugin policy.

## Native Ptah gap

Ptah must define:

- coding-provider session and connection-token mapping;
- Workspace/Object mounts and file-authority boundaries;
- terminal/port/extension capability scopes;
- extension source, signature/licence and permission records;
- Ptah Auth/role/Workspace integration;
- safe service-port mapping rather than arbitrary proxy targets;
- editor/terminal panel embedding or linking;
- mobile handoff to a lighter Ptah shell;
- provider restart/reconnect and stale-session states;
- comparison/conformance against the Theia path.

## Exit strategy

These are optional compatibility applications. Ptah can remove or replace them with Theia, native editors, local IDE bridges or future providers without changing Workspace, Object, Activity or Panel identity.

## Validation required

1. Launch isolated OpenVSCode and code-server sessions against approved Workspace mounts.
2. Enforce Ptah Auth and short-lived scoped connection tokens outside product-local auth.
3. Reject arbitrary terminal, filesystem and port-proxy access beyond the Workspace capability scope.
4. Install one approved Open VSX extension and reject an unapproved privileged extension.
5. Disconnect/reconnect the browser and preserve honest provider/runtime state.
6. Open the same Workspace in a Ptah-native shell without relying on VS Code layout identity.
7. Use a phone/tablet and prove the lightweight Ptah shell remains usable even when the coding provider is not.
8. Remove one provider without changing Ptah Workspace/Object records.
