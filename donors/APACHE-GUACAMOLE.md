# Donor Record — Apache Guacamole Server and Client

**Phase:** 0A / WP07B  
**Status:** FIRST-PASS COMPLETE — CROSS-PROTOCOL BROWSER REMOTE-DESKTOP GATEWAY DONOR  
**Inspected:** 2026-07-17

## Identity

### Server

- Canonical URL: https://github.com/apache/guacamole-server
- Default branch: `main`
- Pinned commit: `6719b20d09b767d30915c5e1c626a7a72fc75a59`
- Licence: Apache-2.0

### Client

- Canonical URL: https://github.com/apache/guacamole-client
- Default branch: `main`
- Pinned commit: `0b65b785afa3de481d08b90c44c9a748c6f5c316`
- Licence: Apache-2.0

- Classification: HTML5/browser remote-desktop protocol gateway and translation donor
- Ptah targets: `APP-002`, `APP-003`, remote desktop/display streams, RDP/VNC/SSH access, browser delivery and protocol-normalized sessions

## Files/components inspected

- `guacamole-server` README
- server licence
- `guacd`, `libguac` and protocol-library architecture
- RDP, VNC, SSH, SFTP, WebP and recording dependency boundaries
- client repository identity and web-application separation

## Verified capabilities and patterns

- `guacd` is a proxy daemon separate from the browser/web application.
- It translates binary remote-access protocols into a common Guacamole protocol designed for browser processing.
- Protocol backends include RDP, VNC, SSH and Telnet depending on compiled dependencies.
- RDP support is built over FreeRDP.
- VNC support is built over libVNCServer/client machinery.
- SFTP file transfer can complement RDP/VNC sessions.
- Audio support and WebP compression are optional capabilities.
- `guacenc` can encode session recordings through FFmpeg.
- The server and web client are separately deployable.
- `guacd` can run unprivileged and exposes explicit bind address, port, PID and logging controls.
- The architecture cleanly distinguishes remote protocol, translation daemon and browser client.

## What Guacamole completes

- One browser-facing gateway model spanning Linux VNC, Windows RDP and SSH terminal access.
- A common remote-display/input protocol independent of each underlying backend.
- A clean daemon/client split suitable for Ptah's public UI versus Node-local protocol adapter separation.
- A practical Windows Application/VM display path through RDP.
- A fallback full-desktop path for Linux providers through VNC.
- Session recording and file-transfer requirements.
- Apache-2.0 implementation patterns that are easier to adapt than GPL-heavy alternatives.

## Important limitations for Ptah

- Guacamole is a gateway, not a VM, Workspace, Device or Application Provider.
- A Guacamole connection/session ID is not Ptah Application Session identity.
- Full desktop protocols expose a broad surface rather than individual application/window semantics.
- RDP, VNC and SSH have different capabilities and proof strength despite one browser protocol.
- Clipboard, drive redirection, file transfer, audio, printing and device redirection are sensitive and backend-dependent.
- Connection success does not prove application launch, visible readiness or expected state.
- `guacd` must be protected from arbitrary target selection and credential exposure.
- The gateway does not own lease, caller authorization, recording retention or Session checkpoint policy.
- Browser display state is not a semantic UI tree.
- Recording output proves observed pixels/audio, not user intent or functional correctness.
- Backend libraries and compile-time options materially change capabilities and licences.

## Must not be inherited

- public callers allowed to choose arbitrary RDP/VNC/SSH targets;
- credentials embedded in browser-visible configuration or retained URLs;
- one `connected` flag used as application/session proof;
- clipboard/file/drive/audio/printing enabled as one generic display permission;
- Guacamole connection IDs as canonical Ptah identities;
- Guacamole's web application/database model adopted wholesale as Ptah UI or authorization;
- full-desktop transport treated as individual application semantics;
- recording presence promoted to verified completion;
- a centrally exposed `guacd` without Node/workspace scoping and network isolation.

## Integration decision

**WRAP GUACAMOLE AS THE PRIMARY CROSS-PROTOCOL BROWSER REMOTE-DESKTOP GATEWAY CANDIDATE.**

Recommended use:

1. RDP presentation for Windows VM/native Nodes;
2. VNC fallback for Linux/other graphical providers;
3. SSH terminal presentation where useful;
4. protocol-normalized browser display and input;
5. recording as an optional evidence stream.

Ptah owns the target Application/Device/Workspace Session, short-lived connection token, capability scope, credentials, streams, recordings and receipts.

## Native Ptah gap

Ptah must define:

- remote-display gateway adapter contract;
- backend protocol and capability snapshot;
- target provider/session reference rather than arbitrary host/port;
- short-lived scoped connection credentials;
- Window/Application Session mapping over full desktops;
- separate input, clipboard, files, audio, printing and recording permissions;
- first-frame and reconnect receipts;
- recording Artifact and privacy/retention metadata;
- target reachability/network isolation;
- backend library/version/compile-feature record;
- gateway restart and stale-token handling;
- semantic UI adapters independent of Guacamole pixels.

## Exit strategy

Ptah's browser-display contract remains implementable through Guacamole, Xpra HTML5, noVNC, native WebRTC/display gateways or platform-specific clients. Guacamole protocol and connection IDs remain backend metadata.

## Validation required

1. Present one Linux VNC and one Windows RDP session through the same Ptah browser-display contract.
2. Prove callers cannot use the gateway to reach an unapproved host/port.
3. Expire/revoke a short-lived session token and reject stale reconnect.
4. Permission clipboard, file transfer, audio and input independently.
5. Restart `guacd` and reconcile Session state without claiming application continuity falsely.
6. Record one session, hash the recording and link it to exact Session/Activity IDs.
7. Compare RDP and VNC capabilities and surface missing features explicitly.
8. Keep semantic automation independent from the pixel gateway.
9. Replace Guacamole with another gateway without changing public Application Session identity.
