# Ptah Current State

**Last updated:** 2026-10-22 (owner hardware/Node independence correction; E07 tested scope complete)
**Overall status:** E06 DONE; E07 tested native Control/Node physical E02/A05 MERGED; F01–F03 MERGED; individual KRATOS/ATHENA Nodes independent. Prime OS F04–F07 integration LAST, with only genuine planned-hardware tests deferred.
**Current phase:** Prime OS final-stage integration planning/interfaces, while each Ptah standalone tool remains usable
**Active work unit:** Prime OS interface and ordinary engineering using existing Nodes; selected GPU-intensive/specialized hardware tests deferred until planned target Node is available
**Runtime implementation:** Ptah workspace executes caller-selected available tools without independent user approval; per-operation transport and journal integrity still apply.
**Current public release:** E05 frozen 90a3ad012f0b3e15bd871e6e955dd79bbf757ded; Ptah-space E06 source main merged through eefeeafeaf89551e7d891598db20366e1aaa4939 (not a release tag)
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

## Controlling hardware-dependency and E07 scope correction — 2026-10-22

**Ptah standalone engineering is ready to move on.** E06 is DONE, E07's tested native KRATOS/ATHENA E02/A05 execution is merged and verified, and F01–F03 are merged. No present workstream or Prime OS design/integration needs an unattended distributed-computing service.

**Hardware is planned, not an emergency dependency.** Continue design, coding, integration and ordinary tests using KRATOS/ATHENA independently. Park only a specific heavy or specialized test that actually needs its designated future GT502, GDX Spark or other planned hardware; record that missing *evidence* without classifying the whole product as blocked.

Per selected task/Node, use the following operational reporting contract: `READY` (execute with available resources), `CAPABILITY_MISSING` (the current Node lacks a capability actually required for this operation), `PLANNED_HARDWARE_DEPENDENCY` (this specific test is intentionally deferred for designated future hardware). These statuses are diagnostic scheduling facts, **not** permissions, Grants or workspace-level denials. Do not automatically treat an unproven unattended cross-network mode as `PLANNED_HARDWARE_DEPENDENCY`; it would be `CAPABILITY_MISSING` **only if the caller explicitly requests that mode now**.

**E07 truth boundary:** real native E01/E02/A05 execution and post-restart journal results are proven on the tested setup; Oracle-mediated roaming worked with an active caller. Autonomous permanent cross-network packet forwarding is not proven, and is not required for independent normal Ptah use. Do not build a new relay, synthetic daemon, shared compute scheduler or third-party service to manufacture "permanence." No Knights changes. Oracle is transport.

**Next:** Prime OS integration (OS-owned F04–F07), the final planned integration stage. Start with interface/contract development on currently available machines. Defer only workload-specific tests whose documented target hardware has not arrived. Old dated E07 "blocking roaming" and "PR #157 unmerged" notes below are superseded for current decisions.

---

## E07 Oracle-carried physical native cross-host acceptance — 2026-10-21

**New physical proof (Ptah PR #157, branch head dfcda5f):** KRATOS
Control established native E01 TLS and sent E02 Reservation/Lease/Dispatch
through opaque Oracle-transported packet batches to a separate ATHENA
Windows native Node. ATHENA executed a real local A05 cmd.exe echo with
exit 0. Both physical SQLite journals passed integrity verification.
Dispatch 01a15e28-646a-7023-a574-c5b28b885826 and attempt
01a15e28-646a-7023-a574-c58a6570bc53 matched on both computers.
ATHENA completed stdout SHA-256
sha256:2344e34e044bc52acc3bc4f659ad04a8a8437db66e42b1913d7cb246b639bb6e;
independent Windows echo verification reproduced that digest.

The first test found a real E02 expiry defect: Control calculated
reservation lifetime before slow E01 negotiation. Corrected Control
starts bounded lease lifetime at actual dispatch issuance (direct
LAN unchanged; Oracle-carried 240s reservation / 210s lease), tested
including overflow. No third-party relay or new Ptah caller permission.

**Scope boundary:** native cross-host E01/E02/A05 while an existing
Oracle tool caller actively transports batches is now physically
VERIFIED. The transport adapter still depends on that live caller;
there is NO verified unattended always-on Oracle packet-forwarding
service. Do not label the stronger permanent roaming capability
complete or equate a Node ACK with independent Control-side effect
witnessing. The existing ATHENA persistent Scheduled Task, Knights,
Oracle settings and system networking were not changed. Ordinary Ptah
capabilities remain open even without native E07 forwarding.

PR #157 is tested and pushed, NOT YET MERGED. The historical
cross-phase CI checks are repository governance, not an execution
permission requirement. Earlier relay PR #155 is not the chosen path.
Prime OS integration remains LAST.

---

## E07 external-service correction — 2026-10-21

**Railway is NOT part of Ptah's required architecture.** The attempt
to provision a Railway TCP relay was not requested and must not be
treated as authorization to install a third-party service or charge
an account. KRATOS and ATHENA are already reachable by the established
Oracle machine transport on unrelated networks. Reuse and test those
existing capabilities first; any truly native E07 stream requirement
must be proven against the actual supported transport, not inferred.

Ptah PR #155 is an **unmerged, optional generic relay experiment**.
It does not authorize a Railway deployment, provider account, new
Ptah login, or an additional workspace prerequisite. Existing direct
native E07 and Oracle-assisted workflows remain available. No
cross-network native E02/A05 proof is claimed merely because Oracle
can connect to both computers. Whether a third-party Railway project
was provisioned outside Ptah is still unverified; local absence of
the Railway executable cannot prove an external resource does not
exist. Do not touch Knights, install Railway, or change host networking.

The historical relay proposal below records its technical exploration,
not a mandated deployment choice. Prime OS integration remains last.

---

## E07 roaming correction — ATHENA travels (2026-10-21)

**Binding requirement:** E07 native E02/A05 must operate when ATHENA is away
from KRATOS, on unrelated home, hotspot, work or mobile networks.
The successful seventh LAN dispatch establishes actual native execution
but is NOT cross-Internet, NAT traversal or ATHENA roaming proof.
Do not certify E07 roaming from an equal-subnet test.

**Ptah-only implementation:** [Ptah-space PR #155](https://github.com/jaydumisuni/Ptah-space/pull/155)
(commit 00083094a1f992c0f87870b540181d119e04abe7) adds a small opaque
outbound TCP rendezvous relay, outbound Control and Node sockets, and
backward-compatible direct LAN mode. Existing TLS 1.3 mutual
authentication remains strictly end-to-end; the relay cannot grant
permissions, select A05 work or forge completion evidence. ATHENA's
Node worker can be configured with a public relay endpoint instead of
a fixed private KRATOS IP. Linux/Windows native artifact build CI was
added. KRATOS complete Rust workspace tests, relay mTLS transport tests,
affected strict Clippy and A01/Phase0C checks passed locally.

**Not yet claimed:** PR #155 source has not necessarily merged; a
globally reachable TCP relay has NOT been provisioned, Windows Node
replaced or an ATHENA-off-LAN E02/A05 effect physically verified. Those
are the remaining *transport deployment/roaming acceptance* steps,
not Ptah-side login, Grants or permission gates. Normal workspace
operations remain available during an E07 relay transport outage.
Do not overwrite the working ATHENA scheduled-task config before the
new relay and Windows binary are independently reachable and verified.

**Boundaries:** Only Ptah code and Ptah roadmap changed. Knights,
Oracle configuration, ATHENA Wi-Fi and existing services untouched.
Prime OS integration LAST after the roaming requirement is met.

---

## E07 post-restart E02/A05 physical execution — VERIFIED 2026-10-21 (controlling)

**E07 source and native runtime evidence COMPLETE for the tested Ptah
configuration.** The previously missing post-restart execution has now
been observed and independently checked.

- Oracle Live verified both KRATOS and ATHENA available. Actual private-LAN
  addresses had returned to the same 192.168.238.0/24 segment; this
  supersedes the 2026-10-20 cross-subnet routing limitation.
- The latest test initially reached E01 but failed TLS with `UnknownCA`.
  Cause identified: ATHENA's Ptah Node worker used a newly installed
  certificate authority while KRATOS Control retained the previous CA.
  Existing certificate backups on ATHENA matched KRATOS's actual trusted
  CA and previously enrolled Node certificate **by exact DER SHA-256**.
  That backed-up Node certificate matched the *existing* private key.
- Updated only ATHENA's Ptah worker.json certificate file references,
  saving a rollback copy `worker.json.before-e07-reconnect-20261021`.
  Restarted only the existing Ptah-E07-Native-Node Scheduled Task.
  Worker PID changed from 30756 to **31572** and remained Running.
  No Knights, Oracle, network adapter, Wi-Fi, firewall or unrelated
  machine services were reconfigured.
- KRATOS launched the existing `ptah-e07-control-dispatch` with its
  existing enrolled Node identity and harmless A05 fixture
  `cmd.exe /C echo PTAH_E07_ATHENA_A05_REAL_20261020`.
  E01 connected and E02 reservation, lease and dispatch frames were
  sent; A05 completion acknowledgment was received. The new **fence 7**
  and dispatch/attempt IDs are independently visible in both journals.
- Control SQLite: **7** dispatches, `PRAGMA integrity_check=ok`, most
  recent phase `sent_unconfirmed` (an Ack is not an effect witness).
  ATHENA Node SQLite: **7** attempts, integrity `ok`, latest
  `completed`, exit code **0**, durable process_ref and output SHA-256.
  Dispatch, Attempt, Node, generation, connection epoch, fence and
  request digest all match exactly between the latest Control and Node
  records; ATHENA stdout SHA-256 independently matched the real Windows
  CRLF `echo` output. No fabricated confirmation was written.
- This proves a new **native E02/A05 execution AFTER the Node worker
  restarted**, closing the last previously identified E07 physical
  acceptance gap. Live use is not contingent on another Ptah user
  approval, login, Grants or release ceremony.
- E06 remains DONE; standalone F01–F03 are MERGED. Prime OS integration
  LAST. The published Programme E roadmap defines **E01–E07 only;
  there is no separately specified E08**. Do not invent or mark a
  nonexistent E08 milestone complete.

**Limit of claim:** one successful physically executed post-restart
benign A05 command under the current network/certificate configuration.
This does not assert universal production reliability, automated recovery
from every outage, or independent Control-side effect proof.

---

## Latest E07 native remote execution checkpoint — 20 October 2026 (controlling)

**Source integrated:** Ptah-space PR #153 MERGED on main as
`de6277979727cb11cb2396a4e4ce7972a26f272a`. PR #154 MERGED as
`c2c0a1dc6a2890c87605a18fc132ee37388de45a`, qualifying the exact
Windows bundled-SQLite Cargo.lock change without altering frozen A01.
Complete Rust workspace tests, native Control/Node strict Clippy and A01 /
Phase 0C scaffold checks passed. Main's protected required checks accepted
PR #153. This is a real native E02 → A05 implementation, not E01-only.

**Real cross-machine durable effects VERIFIED:** KRATOS Control and ATHENA
native Node SQLite journals, read independently over Oracle on 2026-10-20,
both passed PRAGMA integrity_check. Six of six Control dispatch identifiers
match ATHENA completed native A05 attempts exactly, including fence,
Node generation and epoch. All six Node records have exit_code 0 and output
SHA-256. Control correctly retains sent_unconfirmed (no fake independent
effect witness from an Ack); ATHENA is the actual A05 local completion source.

**Persistent worker VERIFIED:** ATHENA existing Ptah-E07-Native-Node
Scheduled Task restarted its process after the worker was forcibly
terminated. The process began at 13:36:48 local and was verified alive at
14:50 as PID 30756. The service keeps retrying absent Control without
a Ptah-side login, Task approval or Grants. Control is caller-selected and
not an indiscriminate automatic dispatch daemon.

**Precise residual transport limit:** most recent verified dispatch #6
occurred about 13:28 local, BEFORE the 13:36 unattended worker restart.
A fresh post-restart attempt listened at KRATOS 192.168.238.52:47821,
but ATHENA had changed Wi-Fi to 192.168.1.155/24 and could not reach
that old private-LAN address; it timed out before any E01 connection.
No completed dispatch #7 is claimed. The current LAN split, not a Ptah
permission gate, prevents qualifying a live dispatch AFTER restart.
Restore/establish a genuine network path before claiming that specific
further result. Never change Knights, Oracle, Wi-Fi or unrelated tools
merely to claim it passed.

**Disposition:** E07 native source MERGED; cross-machine native E02/A05
effects demonstrated and durable; unattended Windows worker restart
demonstrated; post-restart cross-subnet dispatch NOT demonstrated.
This non-global technical reachability condition must not block any
other available Ptah workspace tool. Oracle remains transport;
caller chooses work. F01–F03 remain merged. Prime OS integration LAST.

Older dated E07 no-native-execution statements below are historical and
superseded by this section.

---

## E07 physical KRATOS–ATHENA E01 link verified — 20 October 2026

**New evidence, superseding older statements that no real two-host E01
transport had been demonstrated:** Ptah-space PR #152 MERGED at
`1f39acec718acebb48b7fba3ed614762e0e91b85`. The actual Rust
`ptah-enrollment-gateway` ran on KRATOS Linux, and a new Ptah-protocol
Python 3.10 client connected from ATHENA Windows over private LAN:
mutual TLS **1.3**; canonical NodeHello/HelloAck; three heartbeats,
Close; then a second successful E01 connection with two heartbeats.
A changed canonical Node ID was rejected, and omitting the TLS client
certificate produced `TLSV13_ALERT_CERTIFICATE_REQUIRED`. The
repo-only test certificates, listener, setup files and both host test
directories were removed. No OS, Windows installation, firewall, other
services, Knights code or Prime OS settings changed. All 35 Python
client tests and 16 protected hosted PR workflows passed.

**Qualification boundary:** this is an actual physical two-host
**E01 connection/heartbeat acceptance**, using temporary test-only TLS
enrollment. It is NOT a persistent production deployment and does not
prove cross-host E02 Lease/Fence dispatch or remote A05 process effects.
`ptah-node`'s Rust CLI still has a connection-configuration placeholder;
the new client is a portable E01 wire peer. Any further production
native-execution work is a distinct *optional capability*, NEVER a
condition for Ptah workspace access, and cannot turn into a second Ptah
user login, approval, per-tool Grant or task selector. Oracle is
external machine transport. **Prime OS integration remains LAST.**

---

## Protected Ptah source closeout — VERIFIED 2026-10-20

- **E07 PR #138 MERGED** into Ptah `main` at `982210d25c15e5a1c69d9c2f2a318e096e4d9309`. Optional Control/Node native interfaces, Node-link session fix, Python client, gateway proof and verified-readback source are integrated. Protected current-head CI and Rust workspace tests passed. Native two-host production enrollment/transport demonstration is **not claimed**; E07 is optional and cannot block Oracle-backed Ptah operation.
- **Ptah shared-workspace PR #150 MERGED** at `aa413dc3140fbd8a5273c8870eb06d17be51080c`. D02 native shared workspace, D02 retrieval, D03 query, D05 package/activation and headed-browser caller choice no longer require additional Ptah per-caller enrollment, owner approval or Grants. Mechanical ledger, process, artifact and runtime integrity checks remain. The head passed the complete KRATOS Rust workspace tests, 29 Python client tests, six native bridge tests, browser routing tests (4 pass, physical-only 1 skip) and required hosted current-head integration checks.
- **Governance migration PR #151 MERGED** at `7c6080964768732b9166bbb1d7233b0ad11cae78`. The new required `ptah-current-head-integration` and `ptah-trusted-base-integrity` checks were installed and verified; the six previous baseline contexts remain required and `strict=true` remains set. Frozen historical phase workflows were not deleted, altered, or falsely called passing. Their predecessor-only failures are recorded as historical and do not bar unrelated maintenance from main.
- **Previous dated PR #138/#150 NOT MERGED notes below are SUPERSEDED.** E06 and F01–F03 were already merged. User and AI work in Ptah requires no second Ptah policy vote; an actual missing device or technical error is reported against that operation only.
- **No Knights files, repository, configurations or security code touched. Oracle remains the external transport. Prime OS integration LAST.**

---

## E07 and workspace correction — latest source and protected integration evidence (2026-10-20)

- **E07 PR #138** is pushed at `785f202b7b43a799a13330653009721f44b3d177`. The current-head A01 and Phase0C scaffold checks, exact reviewed E07 Cargo.lock reconstruction and independent PR applicability tests pass. The reconstructed historical lock digest, external registry package set and immutable original phase proofs are preserved; 18/22 hosted PR workflows pass, with four historic predecessor-bound workflows failing as nonapplicable. **Required `a11-governance-integrity` rejects changed `tools/check_current_pr_admission.py`**, despite the separately verified current-head check passing. GitHub 405 confirms **NOT MERGED**. No admission/login/Gate/Grant was added to normal Ptah workspace access; no native E07 two-host runtime was activated.
- **Workspace PR #150** is rebased through current Ptah main at `1356736a06e1c165daa7a526ffe84e508ef48dd1`, source checked on physical KRATOS. Full offline Rust workspace and six native D02 bridge tests PASS. Its merge is **NOT COMPLETE**: historical D02/D03/D05/A11 scoped CI still fails and GitHub protected merge rejects missing/failed required checks. The source fixes remain isolated on its branch, not claimed deployed.
- The **remaining release issue is repository-level governance/CI applicability**, not user/agent access. No developer shall bypass protected main, fabricate historical phase checks, reintroduce Ptah-side authorization, or touch Knights. Native E07 remains optional; Oracle transports. The real capability continues to be developed and tested irrespective of review status. F01–F03 and E06 remain merged. **Prime OS last.**

---

## E07 review-defect correction — 2026-10-20

**E07 optional native Ptah code has the three reviewed defects fixed**, pushed
to PR #138 at `b95eaac5c1d022d78ba5e66f0b1d130d193ad5eb`. The Node
journal now ties each completion receipt to the exact process identity stored
by its own spawn; a different process from the same Provider/Node generation
is rejected, and persisted identity survives reopen. New Control dispatch
journals and lockfiles are created with private Unix mode 0600. Optional
TLS enrollment expiry is checked at the actual post-handshake/Hello owner-lock
admission point, not a stale pre-accept timestamp.

Physical KRATOS: full Rust workspace test suite, 29 Python client tests and
strict Control/Node/Node-link Clippy PASS. **All three PR #138 inline review
threads are resolved**. This is not a native two-host production deployment.

**PR #138 remains open and unmerged:** GitHub rejected the merge with
"3 of 9 required status checks are failing". The historical A01/Phase0C
Cargo.lock scope and phase-exact-predecessor evidence workflows do not
currently admit this additive optional cross-phase PR. These are GitHub
repository integration checks, NOT Ptah workspace access/login rules.
Do not bypass protected main, fake a historic proof or change Knights.
Ordinary Ptah through Oracle continues unaffected. PR #150 separate caller
access cleanup also remains unmerged. The roadmap preserves **Prime OS LAST**.

---

## E07 and standalone F01–F03 verified progress — 2026-10-20

**F01–F03 DONE at standalone Ptah implementation level, merged into main:**
- Foundation profiles/preflight: PR #139 → `ef7c980`, exact-head evidence binding and output-alias safeguards
- F01 binary archive and verification: PR #141 → `a780d94`, full canonical tar verification, manifest schema, safe concurrent output
- F01 detached Ed25519 signature integrity: PR #145 → `524a654`, immutable archive/public-key snapshots, 19 passing focused tests
- F02 read-only USB inventory/rule drafting: PR #143 → `1cf04a0`, 11 tests and five actual KRATOS USB classes
- F03 bounded QEMU/KVM guest boot: PR #144 → `440aebb`, real CPU marker and host disk unchanged
- F03 COW crash rollback/restart: PR #146 → `12d31be`, real KRATOS guest process SIGKILL, byte-exact restored backing image and clean repeat boot

These are capabilities for Ptah's standalone workspace, not a second OS or an entry permission system. Physical mains-power loss and Prime OS integration were not tested and are not blockers for unrelated Ptah use.

**E07 source candidate** remains optional and independently testable. PR #138 source head `4813d82` is current-main reconciled with a session lifecycle interface fix; KRATOS full Rust workspace tests, 29 Python client tests and strict Control/Node/Node-link Clippy pass. GitHub exact-head checks and final merge still require verification, so DO NOT mark E07 merged or activated. ATHENA has Python/Git but no native Rust build tools in PATH; no persistent native service, production transport migration or second workspace authentication was installed. Oracle remains the actual host transport.

**PR #150** for removal of redundant Ptah-side secondary caller checks is separately tracked until merged. Tests or PR reviews must never be mislabeled as permission to use the workspace. No work on Knights is authorized by this checkpoint.

---

## E06 physical-host reliability completion evidence — 2026-10-20

**E06 remains DONE, with NO Ptah workspace access or other-workstream blocker.**
The two requested follow-up checks were executed on real enrolled computers
using Oracle as transport. They do not constitute a Ptah-side login,
user-authorization decision, Grants requirement, or external security change.

**1. Live authenticated transport / reconnect readback and reconciliation**
- Oracle reported both KRATOS and ATHENA ready; independent calls to the
  two hosts succeeded. Both computed SHA-256
  `51844a16014ef4a8fa2238042d4a1f838acdb3cda77ac5b7ebd066bf699d7e18`
  for the same synthetic test marker.
- KRATOS reopened a separately-created, physically persisted E06 SQLite
  journal in a *new authenticated Oracle invocation*. Intent, Node,
  contiguous origin sequence and saved reconnect references survived.
- The actual Ptah `DurableIntentJournal::observe_reconnect` implementation
  was run against the re-opened journal, with 23 entries: matching saved
  references produced the non-dispatching comparison outcome; stale E02
  fence, changed E03 object generation and uncertain prior effect yielded
  the correct distinct negative classifications. Zero observation writes
  and no change to unrelated workspace execution.

**2. Physical-host process interruption / durable recovery**
- KRATOS storage verified as **/dev/nvme0n1p2, ext4**, not RAM-only.
  Disposable test journal used SQLite WAL with synchronous FULL (2).
- 44 independent E06 CLI worker attempts; **22 explicitly SIGKILLed**
  while running and 22 completed with process receipts. One original
  bound intent plus the 22 completed workers yielded **23 persisted entries**
  after recovery, with a contiguous `1..23` Node sequence and cursor 23.
- Reopening in a later Oracle invocation: `PRAGMA integrity_check = ok`,
  23 rows, zero stored reconciliation findings and no leftover worker
  processes. No data rewrite, replay or invented authority.
- Tamper tests on disposable **copies**: deleting
  `reconciliation_findings` or corrupting the saved-generation JSON caused
  the live Ptah CLI to **fail closed**. The original journal retained
  23 entries and integrity `ok`. Corrupt copies were deleted.
- The real physical hosts, production services, Knights and any user
  workspace data were NOT rebooted, powered off, disconnected or altered.
  Only disposable E06 worker processes and files were used.

**Precise proof boundary:** this is live Oracle session continuity with
persisted reconciliation and real NVMe process-crash recovery. No deliberate
network outage or host mains-power interruption was performed, so it does
not prove such failure modes. Those are optional deployment-specific
reliability experiments, **not unfinished E06 features, security approval
steps, permissions, release gates or workspace blockers**. No automated
replay of an uncertain external effect was attempted. Existing technical
failure detection remains intact.

**Disposition: E06 closed for the tested standalone Ptah functionality.**
Continue optional E07 and standalone F01–F03. Prime OS integration LAST.

---

## E06 status correction — binding operational meaning (2026-10-20)

**E06 = DONE for source implementation:** its offline queue, durable journal recovery,
immutable reconnect references, read-only comparison and unknown-outcome
classification are implemented, tested and merged into Ptah main (PR #137
and PR #140). Normal Ptah workspace operation is NOT conditional upon
further E06 tests, release ceremonies, native multi-host proofs or any
Ptah-side caller approval.

Previously listed "live authenticated reconnect" means an **optional
real-world transport/session recovery reliability test** using existing
upstream access. It is **not** a Ptah login, enrollment, Grant, authorization
or extra user/agent acceptance procedure. "Physical recovery and final
production acceptance" means additional evidence for a particular
deployment's stronger durability/recovery claim, **not** a workspace
access gate. These checks may be performed when the relevant hardware
and deployment are available without blocking unrelated capabilities.

Ptah's only operational limitation is the actual technical state of a
requested operation: disconnected host, missing tool, corrupt data, stale
handle, resource exhaustion or unsafe unverified effect. Report the
failure of that operation truthfully; do not restrict the whole workspace
or substitute Ptah's approval judgment. Knights remains outside Ptah
implementation; Oracle transports; the caller selects the task.

**Next Ptah scope:** E07 optional native execution and F01–F03 standalone
capabilities. **Prime OS integration LAST.** Historical dated checkpoints
below retain their original evidence and are superseded where they describe
E06 tests or sign-offs as blockers to using Ptah.

---

## Ptah E06 merged source checkpoint — 2026-10-20

**Confirmed on Ptah-space main:**
- E06 durable offline queue, immutable reconciliation receipt recovery and
  versioned queued reconnect reference storage — PR #137 merged as
  `23ed17a7c71f6547aa4dba6662e2e5a3f21fe014`.
- E06-03 read-only reconnect comparison against the *stored* session, fence,
  object generation, checkpoint and host-generation facts — PR #140 merged
  as `eefeeafeaf89551e7d891598db20366e1aaa4939`.
- Earlier uncertainty from a possible external effect takes precedence over
  newly mismatched digest/fence evidence; corrupt journals cannot silently
  lose negative reconciliation receipts.
- KRATOS Rust tests, E06 strict Clippy and accepted GitHub required checks
  passed. These merges are source-level completion only, not claims of a
  live E01-E05 authenticated production replay, physical host power cut,
  E07 native two-host enrollment or final E06 release sign-off.

**Ptah correction status:** PR #147 Search and PR #148 Browser are merged.
PR #150 (D02/D03/D05 and browser-choice runtime admission refactor)
remains unmerged due Ptah repository protected CI requirements.
This is a GitHub integration gate, **not a Ptah-side permission decision**.
No Knights implementation, settings, cybersecurity, or identity system was
modified.

**Next standalone order:** E06 is DONE (extra reconnect evidence non-blocking);
continue optional E07 native capabilities, F01 package
workflow, F02 device-support and F03 VM/rollback acceptance. **Prime OS
integration comes LAST.** Ptah remains a shared workspace; Oracle only
transports caller-selected operations.

---

## Owner's binding Knights / Oracle / Ptah correction — 2026-10-19

**NO Ptah-side login, owner approval, per-agent enrollment, per-tool Grant,
browser/search permission, semantic task choice or secondary admission.**
Knights owns security/cybersecurity once implemented; currently the
development workspace is open. Trusted ingress hands Ptah an already
admitted caller. Ptah executes caller-selected tools and returns actual
results or technical errors. Oracle transports to machines, not decisions.
Keep record identity, provider process generations, transport integrity,
evidence and resource accounting mechanical; they are NOT access votes.

Verified runtime candidates (not merged production at this checkpoint):
Ptah-space PR #147 corrects agent-neutral Search access; PR #148 removes
frozen Node qualification as Browser's live launch veto; global runtime
PR #150 changes the native D02 workspace bridge and D02 reader, D03
queries, D05 package/activation path and headed browser opt-in. Exact
historical contracts are retained as data/provenance, not caller gates.
Global owner correction issue #149 is the tracking reference. If live
runtime tests or PR review have not passed, record actual status, not
imagined implementation.

The previous E06/E07 owner-login or individual native release GO/NO-GO
descriptions apply only to optional independently accepted native
distributed production; they NEVER deny normal Ptah workspace use over
Oracle. Local Ptah authorizations are not delegated security authority.

**Prime OS integration must be LAST**, following standalone E06/E07 and
F01–F03 work, and Prime owns boot, installer, OS update/rollback, encryption
and desktop rather than Ptah duplicating an operating system.

**Live Oracle update:** at this audit Oracle reports both KRATOS and ATHENA
ready; earlier "ATHENA absent" notes below are dated historical snapshots.

---

## F03 fully green exact-head update / E07 blocker distinction — 2026-10-19

Ptah-space PR #146 exact head 335e9a5487c8b6ee921c2ee648da7cda7baf0c1f
is source-qualified with 13/13 exact-head hosted workflows green and ready
for independent review. On KRATOS, all 41 conformance tests passed, two
initial live COW crash/rollback boots passed, followed by six further
two-boot SIGKILL rollback/restart cycles. The first guest's BIOS ACK
was NOT a durable disk effect in any of the six repeated crashes; the raw
baseline stayed byte-identical and the clean overlay restarted successfully.
No persistent VM processes or temporary files remain. This qualifies only
disposable QEMU process-crash rollback; F03 guest-OS boot, filesystem
durability, physical power-cut, adversarial VM isolation and independent
admission are not claimed.

A read-only attempt to use KRATOS's existing kernel for guest-OS boot
was denied by the Oracle-hosted execution environment's no-new-privileges
restriction. No host kernel permissions or services were changed.
Oracle currently shows KRATOS connected, ATHENA absent. Thus E07's
two-host native acceptance is not evidenced.

Ptah-space PR #138 E07 historical D01 and A14 CI failures are distinct
single-predecessor frozen locks: they explicitly require separate old C11
and A13 parent commits, whereas E07's real integration base is E06.
Do not alter, bypass or falsify their phase-owned acceptance. 16/18
integration-head checks passed, but optional production release remains
NO-GO until genuine independent E07 admission and owner decision.

Prime OS integration remains the FINAL step, not a Ptah duplicate of OS
boot/installation/update/desktop code.

---
## F03 crash-recovery qualification — 2026-10-19

Oracle connectivity returned for KRATOS, which is the only enrolled node
visible to the Oracle session at this checkpoint. ATHENA was not connected.
The delayed disposable COW recovery implementation now lives in Ptah PR #146
(head 335e9a5487c8b6ee921c2ee648da7cda7baf0c1f) stacked on the
F03 guest-execution PR #144, NOT merged into production mainline.

The explicit F03 process-crash runner boots an x86 BIOS test payload under
QEMU/KVM, issues a guest IDE sector-write, records its ACK, SIGKILLs only the
owned QEMU guest, classifies the post-crash effect as UNTRUSTED, discards the
COW child, and recreates a clean child against a SHA-256-verified unchanged
1 MiB base. A second disposable guest successfully starts from that image.
KRATOS: 41/41 combined local tests, two initial process recovery runs and
six subsequent repeated recovery cycles pass. In all six repeat cycles the
acknowledged pre-crash write did NOT appear reliably in the projected COW
sector, confirming it cannot be promoted to a durable execution receipt.
The original disk remains byte-identical. All temporary files removed.
The dedicated exact-head hosted workflow passed; broader CI pending at
initial publication.

**Release limits:** this is a synthetic BIOS sector, not a Linux guest,
filesystem write/fsync acceptance, multi-workload isolation, hypervisor
security, physical power interruption, or E01/E02/E05 Node admission.
F03 production acceptance remains OPEN, as do E06 authenticated owner
reconnect and optional E07 two-host native production admission. F01 real
signer and deployment, F02 physical device policy and independent review
remain open. The wider OS image, installation, OS updates/rollback and
desktop work belongs to Prime OS and stays strictly LAST.

---
## Pre-Prime-OS standalone Ptah qualification — 2026-10-19 (continuation)

Owner sequencing correction: complete Ptah E06/E07 and its standalone F01,
F02, F03 infrastructure first. Prime OS owns the OS boot image, installation,
update/rollback, encryption, selected compositor/desktop and final OS-ready
system acceptance; postpone Prime OS integration work (roadmap F04–F07)
until the Ptah standalone boundaries and acceptance are settled. Ptah
must not create a second competing operating system, authorization service
or machine transport. Oracle is the machine transport to both hosts.

F02 candidate source PR #143, branch
feat/f02-usb-safe-profile-20261019, exact head
2a5eaee56d2bae20407080ef890ef0f602d932e6. Physical KRATOS passive
USB inventory identified five vendor/product classes and collected no
serial numbers or device paths. 11 focused tests and 14/14 hosted workflows
passed. Draft device rules are inert commented examples, not installed
udev policy, service access or production-qualified drivers.

F03 candidate PR #144, branch feat/f03-bounded-kvm-boot-proof-20261019,
exact head 6e2a0c9646ca36f7b76e91546d18f8d79a2a7b58. Physical KRATOS
QEMU/KVM executed a 512-byte deterministic BIOS test sector, emitted the
expected guest debug marker, and left a disposable disk byte-identical.
No networking, guest OS, persistent VM, root escalation or Node service
installation. Combined 29 local conformance tests, A01 and Phase0C checks
passed. All 13/13 exact-head hosted CI workflows passed after the
KVM-negative test was made portable to runners without QEMU tooling.
PR #144 is ready for review, not merged or released. F03 still lacks
Linux/Windows guest OS isolation, crash recovery and independent production
admission; a boot-sector proof is not full OS-ready acceptance.

F01 PR #141 remained separately ready for review and unsigned-only. E06
PRs #137 and #140 remain candidates, not authenticated-owner reconnect
release. E07 production native approval remains independent and NO-GO.
No Prime OS work has been executed under these PRs.

---

## Engineering progress addendum — 2026-10-19

E06-03 non-authorizing reconnect comparison is now code-qualified in Ptah
PR #140, exact commit feb45001be28015e9deec4f728a9980a5c8cfc3c.
All 13 hosted workflows and the physical KRATOS full Rust workspace suite
passed. It refuses to let untrusted observations insert permanent negative
receipts; only independently verified owner evidence can settle native
E01–E05 authority. Authenticated production reconnect and final E06
review/release are still unproven.

F01 unsigned deterministic Control/Node packaging candidate is Ptah PR #141,
commit b267bf4715459255fb1543d016afd00f256cad6b. All 13 hosted
workflows and 27 combined local F tests passed. On KRATOS, both actual
Ptah executables were built, bundled and archive-verified twice; both
temporary 66,652,160-byte archives had SHA-256
254a066f54ab67ce3eb4af26229566b810c380ca65b9633015e2a77f3d65e31c.
No signature, independent two-builder provenance, installation or native
execution claim is made; the archives were cleaned afterward.

A bounded attempted F03 real kernel/guest boot was stopped by KRATOS
kernel-file read permissions at /boot, not successful guest initialization.
Do not change host permission or infer full VM admission. No production
host power cycle, deployment-owned E01 keys, owner approval or service
cutover occurred. F02–F07 implementations remain open.

---

## Superseding live evidence checkpoint — 2026-10-19

Architecture: Oracle remains authenticated machine transport for ChatGPT,
Hunter and other agents on KRATOS/ATHENA/Nodie. Ptah is the neutral shared
workspace, not a transport, planning authority, or prerequisite enrollment
gate. Supervisor/Cookpit, Hunter, Sergeant/Patrol and the owner retain their
own independent authority.

E06: Source candidate jaydumisuni/Ptah-space PR #137 at
58f11d9fda0adeb50433150884328b0c7ff22137 passed all 15 exact-head
CI workflows, including universal admission, security/licensing policy and
E06 atomic journal. KRATOS disposable SIGKILL test: 80 bounded attempts,
13 killed, 67 durable contiguous records, zero gaps, no execution authority.
E06 remains unreleased: owner-verified current E01–E05 reconnect, independent
review, and E06-07 final qualification are not proven.

E07: Optional native gateway candidate PR #138 at
5c68f2bbb73b82bf12d08f8eb023a99226d3caf7 passed relevant local
Control/Node and client tests, but D01/A14 historical predecessor CI checks
fail. Real production E01/Node certificates, E05 two-host profiles, E02
dispatch, independent A05 effects, hard-reboot recovery, Sergeant/Patrol
review and owner GO are outstanding. Ordinary Ptah workspace use through
Oracle does not depend on this native service.

Programme F: Non-activating candidate PR #139 at
d93fa2006337e6e2a03c05682140123c50aeabea adds a seven-phase profile,
21 explicit missing proof types, 19 adversarial/passive tests, and exact
head non-activating CI. F01 through F07 are NOT implemented or accepted.
KRATOS local KVM/QEMU bounded no-boot smoke and disposable QCOW2 check
passed; neither booted an OS nor proved a full guest recovery. ATHENA
has virtualization capability but no observed installed Ptah native
service, QEMU or VirtualBox.

Host caveat: KRATOS kernel observed 7.0.0-38-generic differs from
historical E05 frozen 6.8.0-136, and system storage is tight. No
silent E05 requalification, production certificate changes, Node service
activation, reboot, data-disk writes or Supervisor route changes occurred.

Use current exact branch and hosted status to resume; old text below is
retained as a historical checkpoint, not the current implementation truth.

---

## Current implementation synchronization — 2026-10-01

The Phase 0C authorization language retained later in this file is historical checkpoint evidence. It no longer describes current implementation state.

Accepted Programme E lineage:

```text
E01 merge: 18c1bb26bf074fd8146c2dd8e47838d658af8561
E02 merge: 4b745e7ee0712df0458c1adf55feafdbcc42d9d4
E03 merge: d25679c7f039d7328fe1a785af91e82bd403b44e
E04 merge: 77bbd876aaefd78fed2c0583b2b124eee428eb5f
E05 proven candidate: aa2c8b5efef87787354e41075f3d35efc573b960
E05 frozen release: 90a3ad012f0b3e15bd871e6e955dd79bbf757ded
current Ptah-space main: e11c744c4e9900c460e3c4a3fda9fe385f6e1dc9
```

E05 Task-10 release identity is exact:

- release parent 1 is accepted E04 `77bbd876...`;
- release parent 2 is proven E05 `aa2c8b5...`;
- release tree `58312f1e72dd05a28978c52e04268c5db30dd2db` is identical to the proven candidate tree;
- unchanged-candidate pull-request proof run `36847594835` passed and retained artifact `11154237301`, digest `sha256:84c0d617824a0fc90fbba512716319216a8e7cbebc9e8c75f75ea07ee5c8c8ce`;
- integration PR #107 preserved the intervening operational mainline and merged the immutable E05 release forward.

A bounded private live-consumption proof has also exercised the released E01/A02/E05/E02/A05 composition against a real consumer workload. Machine-specific and credential evidence remains outside this public roadmap repository. That proof does not claim permanent daemon installation or production credential enrollment.

**Active dependency-ordered package:** E06. Automatic Supervisor continuation opened branch `e06-intermittent-local-first` from accepted main `e11c744c4e9900c460e3c4a3fda9fe385f6e1dc9`; Cookpit micro/heavy recovery proofs PASS. No E06 implementation delta is claimed by this record.

---

## Historical Phase 0A–0C and planning record

The material below is retained for decision and proof history. Where it says runtime was not authorized, P01 was active, or Programme E had not started, read that statement as the status at that historical checkpoint; it is superseded by the current implementation synchronization above.

## Frozen checkpoints

### Phase 0A donor and requirement closure

Frozen checkpoint:

```text
7d2dffee48f1400ba1cf88823343f09a3895ad33
```

Decision:

- `decisions/ADR-0017-PHASE-0A-FREEZE-PHASE-0B-ENTRY.md`

### Phase 0B contract and proof closure

Phase 0B is frozen by:

- WP01 through WP14 candidate packages;
- exact local schema catalogs and namespaced lifecycle machines;
- directional migration and backend-replacement rules;
- positive, negative and adversarial fixtures;
- the offline WP13 structural and semantic conformance harness;
- the WP14 lawful golden/negative corpus and first vertical-slice proof plan;
- `work-packages/PHASE-0B-FREEZE-READINESS-REVIEW.md`;
- `decisions/ADR-0032-PHASE-0B-FREEZE-PHASE-0C-ENTRY.md`.

Freeze merge:

```text
dc2db457f1705d0cba80f17ab76e5e93f808aee0
```

WP13 and WP14 exact-head workflows passed unit, structural and semantic conformance before merge. Contract changes after this checkpoint require a versioned schema/lifecycle change, migration, fixtures, conformance evidence and a reopening ADR.

---

## Completed Phase 0B packages

1. WP01 — Common identity, versioning and typed families
2. WP02 — Activity, Operation, Attempt, Event, Receipt and proof
3. WP03 — Object, Revision, View, Artifact and storage
4. WP04 — Node, Facility, Provider, capability and health
5. WP05 — Workspace, Session, checkpoint, restore and recovery
6. WP06 — Transfer, synchronization, conflict, backup and restore
7. WP07 — Recipe, Build, provenance, SBOM, signature and verification
8. WP08 — Domain Pack, firmware, disk, filesystem and Device
9. WP09 — Application, Browser, semantic UI and Shell
10. WP10 — Knowledge, Data, Package and Plugin
11. WP11 — Isolation, placement, reservation, Lease and secure grants
12. WP12 — Security, Finding, Claim, Evidence, remediation and reproduction
13. WP13 — executable cross-contract conformance
14. WP14 — golden/negative corpus and proof-plan freeze

These packages define implementation boundaries. They are not evidence that the Ptah runtime already exists.

---

## Phase 0C decisions and evidence now recorded

The following records are merged:

- `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md`;
- `work-packages/PHASE-0C-02-HOST-BASELINE-PIN.md`;
- `work-packages/PHASE-0C-03-DIRECT-DEPENDENCY-LICENCE-RECORD.md`;
- `work-packages/PHASE-0C-04-SOURCE-LAYOUT-AND-BOUNDARY-ACCEPTANCE.md`;
- `work-packages/PHASE-0C-05-WP14-IMPLEMENTATION-TASK-AND-PROOF-MAP.md`;
- `work-packages/PHASE-0C-06-CI-EXACT-HEAD-ACCEPTANCE-GATE.md`;
- `work-packages/PHASE-0C-07-REAL-WORKLOAD-CANDIDATE-REGISTRY.md`;
- `work-packages/PHASE-0C-08-NONCLAIMING-SCAFFOLD-EVIDENCE-REVIEW.md`;
- `work-packages/PHASE-0C-09-IMMUTABLE-ACTION-AND-FROZEN-CONFORMANCE-EVIDENCE.md`;
- `work-packages/PHASE-0C-10-FROZEN-CATALOG-AND-GENERATED-BINDING-EVIDENCE.md`;
- `work-packages/PHASE-0C-11-RUNTIME-DEPENDENCY-BACKEND-SIGNER-AND-HOST-COLLECTOR-EVIDENCE.md`;
- `work-packages/PHASE-0C-11-EVIDENCE-MANIFEST.json`;
- `work-packages/PHASE-0C-12-PINNED-HOST-PROOF-INTEGRITY-AND-PACKAGE-ARTIFACT-READINESS.md`;
- `work-packages/PHASE-0C-13-DURABLE-PINNED-HOST-RETENTION-READINESS.md`;
- `work-packages/PHASE-0C-14-APACHE-2.0-OWNER-ACCEPTANCE.md`;
- `work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md`;
- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.

### Candidate first-slice baseline

- Ubuntu Server 24.04.4 LTS amd64 image pinned by SHA-256;
- Noble GA 6.8 generic kernel line;
- Rust `1.97.1` primary Node/control toolchain;
- SQLite `3.53.3` behind a repository-owned ledger boundary;
- native Linux PTY/process supervision;
- containerd `2.3.1` with runc `1.4.2` behind an OCI Provider boundary;
- Node.js `24.18.0`, Playwright `1.60.0` and its pinned Chromium build for the first Browser Provider;
- hardened Git `2.55.0` process adapter;
- libarchive `3.8.7` first decomposition adapter;
- repository-owned resumable transfer and local content-addressed storage;
- Apache License 2.0 accepted for repository-owned public Ptah source, with private THETECHGUY systems, data, restricted adapters and trademarks excluded.

Concrete tools remain replaceable backends. They may not redefine canonical Ptah identity, lifecycle or proof. Backend IDs remain Aliases.

---

## Merged non-claiming implementation scaffold

The initial scaffold merged at:

```text
ff26fa93d1b60781b49f33f5d1758680e1282d5f
```

Evidence hardening merged at:

```text
23fc97ff0acd2b219990411ec4fb84d8a8c0a567
```

Exact head `900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc` passed workflow run `29717942201` for source policy, Rust, Browser and frozen WP13 conformance under immutable Action pins.

The scaffold contains package boundaries, locks and CI only. It is not a Ptah runtime.

---

## Merged frozen catalog and generated binding closure

`Ptah-space` PR `#5` was tested at exact head:

```text
33043eaadb0f074d8867cb8ce999f16ea4c06a8b
```

and merged at:

```text
f45c96e3f667b463042b6a8b714066236fde703d
```

The accepted lock state is:

```text
frozen_catalogs_and_bindings_locked_runtime_dependencies_open
```

The lock records:

- fourteen frozen catalog paths, URNs and original-byte digests;
- catalog-set SHA-256 `f0668a5f5d5c68cabf623176608c627a94482faa4f4460e4f0fe0f0969d7c64d`;
- final binding generator version `0.3.0`;
- manifest SHA-256 `63fd0cb0fd4ef172271aa7a114e74bb24c0a9e70cc247faeff1db95f7a67d97d`;
- catalog-index SHA-256 `0f97e222d9baf9f90721d2a30dd2b31920b53489ae343b0430cc9089c8fdaf9c`;
- Rust-module SHA-256 `748e87f1a8cf2ed20d694aa716dd8f18b7ea4b3016372386202aeeaff687ae50`;
- output-tree SHA-256 `8f3355e0eac19715ea34e06ea227a826ac727d2e5b9ebf231a672927350c8db2`;
- fourteen catalogs, 346 canonical schemas and 99 lifecycle machines.

Exact-head workflow runs passed:

- catalog lock: `29727701958`;
- independent generated bindings: `29727701960`;
- source policy, Rust, Browser and frozen WP13 conformance: `29727701999`.

The generated crate provides metadata and lookup bindings only. It does not implement or authorize runtime behavior.

---

## Merged runtime dependency, backend signer and host-collector evidence

`Ptah-space` PR `#6` was tested at exact head:

```text
bc12885ce41844b05481628543219c3a8d3574ba
```

and squash-merged at:

```text
c2cd803b5e5c50787b3d8c2d24392d693afdbb3c
```

The accepted evidence records:

- ten exact direct Rust dependencies, 99 resolved packages, 81 crates.io packages and zero Git dependencies;
- final `Cargo.lock` SHA-256 `d68a06272d417d67049c7879570e3735607166ce1e7eff58e43df21e20c9117a`;
- passing cargo-deny advisory, ban, licence and source policy;
- nine authoritative distributed/source backend artifact identities and digests;
- Playwright `1.60.0` Chromium `148.0.7778.96`, revision `1223`, installed-tree SHA-256 `953a2e9c1fb18d1e698f0903a62c23c835264e939cdd08a85c41d57719a5de7a`;
- pinned and verified signing authorities for Node.js, runc, Git and libarchive;
- a fail-closed collector for all eighteen required host capabilities and conditional AppArmor evidence;
- realistic Ubuntu base/point-release, architecture and frozen-kernel matching;
- exact-head dependency, backend, signer, host, source, Rust, Browser, contract, binding and WP13 evidence.

All eight final workflows passed at the exact candidate head. The backend-signature lane retained a first-attempt upstream HTTP `504` as negative evidence; the unchanged lock and successful retry completed all four cryptographic checks.

The hosted collector report validates required capability observation but remains non-proof because generic runner identity does not match the frozen `6.8.0-136-generic` host. No evidence record authorizes runtime implementation.

---

## Merged pinned-host proof integrity and package-artifact readiness

The proof-integrity repair was tested in `Ptah-space` PR `#9` at exact head:

```text
4e871b2bad8c4054ef1e9a1245219fa231338458
```

and squash-merged at:

```text
b97c2defbba17d75e32cb0a02cda9bbb2b1c6649
```

The exact installed-package artifact evidence gate was tested in PR `#10` at exact head:

```text
74aef4b6a4ddebb7f2491fc0eb127d945ac05a14
```

and squash-merged at:

```text
50969c414b55460b6ff7a7d12fd7ae88f5ef5c0a
```

The merged tooling now:

- accepts only the canonical `host/scripts/collect_capabilities.py` collector;
- requires the capability report itself to pass before bundle eligibility;
- proves clean unchanged Git state before and after collection while excluding only the fresh evidence output directory;
- hashes retained hostname, machine ID and boot ID values;
- records exact installed `dpkg` package/version/architecture identities;
- resolves exact local APT binary-artifact `Filename`, `Size` and SHA-256 metadata in bounded batches;
- fails closed on malformed identities, missing or conflicting digests, absent APT release/package index evidence, capability failures or repository changes;
- emits `package-artifacts.json` and a `bundle-manifest.json` schema `0.3.0` with combined eligibility failures;
- keeps `network_used: false` and `runtime_implementation_authorized: false` in the relevant records.

All eight workflows passed at both exact heads. The final host workflow run `29811724538` checked out `74aef4b6a4ddebb7f2491fc0eb127d945ac05a14` and passed host, package-artifact and pinned-proof regression coverage.

This closes proof-tool readiness only. No physical-host bundle has yet been produced or accepted.

---

## Merged durable pinned-host retention readiness

`Ptah-space` PR `#11` was tested at exact head:

```text
f0c1aafb58b33fcc8338081244996ced9260ce5c
```

and squash-merged at:

```text
49f6035a93bf704d775dc437e8a8b25c95145ae1
```

The merged retention tooling now:

- independently re-verifies the exact six-file physical-host source bundle before retention;
- recomputes every file and aggregate digest plus host, capability, package, package-artifact, APT-index and APT-source proof conditions;
- binds the candidate to current clean exact `HEAD`, canonical collector bytes and the reviewed proof-runner digest;
- rejects malformed or authorizing records, wrong commits, collector mismatches, unexpected repository changes, symlinks, nested paths and overwrite attempts;
- preserves exact source bytes in a durable base64 bundle;
- emits a separate repository binding;
- emits a review record with `review_status: pending` and every host, package, retention, ADR and runtime acceptance field `false`;
- verifies the exact final four-file durable output and rechecks repository state after retention.

All eight workflows passed at exact head `f0c1aafb58b33fcc8338081244996ced9260ce5c`. Host workflow run `29813401728` passed the host collector, identity finalizer, package-artifact, pinned-host proof, independent retention and exact-repository-binding regression suites.

This closes durable-retention tooling readiness only. No real physical-host source bundle or durable candidate has been generated, committed or accepted.

---

## Merged Apache-2.0 public/private boundary acceptance

The non-operative boundary candidate was tested in `Ptah-space` PR `#12` at exact head:

```text
2a54093d0a7856d7b98c77ebaa78899e1626257b
```

and squash-merged at:

```text
bf846574df65061bd99d9c0e3d22a401bf9f27e2
```

The owner-acceptance change was then tested in PR `#13` at exact head:

```text
a47d418243af076b49367c4c4eccc8ef2090894c
```

and squash-merged at:

```text
3ce7d4251db0b6ba3f145385ad7ad8dc09276393
```

The accepted boundary records:

- rights holder `John Dumisuni trading as THETECHGUY DIGITAL SOLUTIONS`;
- exact official Apache License 2.0 bytes at root `LICENSE` and `LICENSES/Apache-2.0.txt`;
- licence size `11358` bytes and SHA-256 `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`;
- operative `NOTICE`, `CONTRIBUTING.md`, `SECURITY.md` and repository-wide `REUSE.toml` annotations;
- explicit private-system, customer/device/payment, restricted-adapter, donor-source and trademark exclusions;
- a reviewed third-party NOTICE boundary and mandatory re-review triggers;
- historical candidate records preserved as non-operative evidence;
- `runtime_implementation_authorized: false` in the accepted machine record and exact-head evidence.

All nine exact-head workflows passed at the acceptance head, including the new licence-acceptance lane, Rust dependency/licence policy, source/no-build, host, backend, signer, frozen-contract and generated-binding gates.

This closes the Apache-2.0 owner decision and operative public repository governance files only. It does not close the physical-host, package, durable-retention, ADR or runtime-authorization gates.

---

## Corrected AI Project Workspace behavioural donor boundary

Original donor package:

```text
PR #14 merge: d05653c5948727b58ead91088447d0b8ac4d9d9b
```

Neutral-boundary correction:

```text
PR #15 exact head: 5a95c577edf366bad1d8949ee37c17b81f296254
PR #15 merge: 8a8d620c5227a6508145cd4a30f4f45142bfabe9
```

All ten public exact-head workflows passed. Corrected Workspace run `29961370694` retained artifact `8546091277` with digest `sha256:04472fd4fd546fcc2420d135cdfcb517381efbe5de8b3bc14f6971207fbde819`. The private plan correction passed 18 regressions at `b7ab2ccad94f1cefeb4693448c2a2ca79b0b00a7` in run `29962459098`, retained artifact `8546506459` with digest `sha256:ff3e1aef59f0c847964888ef460c6177bdfed181b0a6817318cbc3d2eb9e4ccb`, and merged as `fc8ac4c42a3358da37c4866879543a5d7c4d1885`. Full merge record: `planning/PTAH-NEUTRAL-SUBSTRATE-CORRECTION-MERGE.md`.

Canonical boundary:

- Ptah is the neutral Workspace and execution substrate;
- Hunter owns intelligence, context selection, source judgments, planning and coordination;
- Sergeant independently reviews frozen candidates and issues Sergeant's result;
- humans or calling applications own intent, configured authority, approval, acceptance and release;
- Ptah stores and mechanically enforces configured records but does not select context, rank authority, review, approve, promote or choose a next action.

The donor remains application-experience study only, requires zero Core extensions and does not change ADR-0033, AF03 or runtime authorization.

---

## Accepted Phase 0C-16 Master Plan closure

The complete product/operating plan, dependency-ordered implementation roadmap, WP01–WP14/Phase 0C reconciliation and durable human/AI handoff were validated at exact candidate head:

```text
37d23449fda9a426f56ee8b09042dda91587a6d1
```

Exact-head workflow run: `29842137511`.

Retained artifact: `8499790872` with archive digest `sha256:82d6b452777e2c5e60c4d08bf88dd2c848d6b2570650b70a4eede633c8065d9f`.

Candidate squash merge:

```text
2c24f9e6b0fc98d5e03605596db75d7495796353
```

Accepted-state exact head:

```text
5860b4bfe177aa375fb2fa4305d62dbe3d2141e1
```

Permanent accepted-state workflow run: `29844040274`.

Retained accepted-state artifact: `8500540358` with archive digest `sha256:6f5229fe850d8b6f6f083b09f2c5f53189f3edbf38d4f28b9d2878ab0c78862d`.

Operative authority acceptance merge:

```text
66bd2410d4c777cd3fd3278107f40fe425e875e9
```

ADR-0034 is accepted. `MASTER_PLAN.md` and `IMPLEMENTATION_ROADMAP.md` version `1.0.0` are operative authorities. No new Core entity or current WP01–WP14 reopening was required. This closes planning authority only and does not accept the physical host, packages, retention, ADR-0033 or runtime implementation.

---

## Accepted Phase 0C-17 tenfold archive formation

Operative authority:

```text
ADR-0035: ACCEPTED
protocol: planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md version 1.0.0
campaign: archive/CAMPAIGN-001-FORMATION-MANIFEST.md
candidate merge: c4973cbf4d02a34f14a7aefa85b8e2ea7b392752
operative acceptance merge: 40ca127c6d3054bda785061090acefaefcf4cd42
```

Accepted evidence:

- candidate exact head `58b577b6793ec28de084e6d712c3c1e88bfe2d3a`;
- exact-head run `29853954659`;
- retained artifact `8504497355`;
- artifact digest `sha256:936740e8087e6f7f0a58b3d731117fcb9a4861edfd20c396fb1bb20a7d4f18f4`;
- validation report SHA-256 `de38af1e63a76e02552e4f93ad2bac2d86d05239a77dc92cc27d794a8b9b010f`;
- 21 candidate regression cases and exact-head validation passed;
- exact fifteen-file candidate boundary directly reviewed;
- accepted exact head `b96b84d17cf03e905bd0b1baf3c46b8aec09334a` passed 23 regression cases in run `29855000427`;
- retained accepted artifact `8504901567` with digest `sha256:9d96a1f299060e50ab63132d1bb1da0903d5435f73acdf4fa9e394cdcccf21d2`;
- accepted validation report SHA-256 `21d5338a7049dbc3a3af2e684efa21e19c281c52355007346291c74dfb7a1d3a`;
- operative acceptance merge `40ca127c6d3054bda785061090acefaefcf4cd42`;
- full acceptance record `planning/TENFOLD-ARCHIVE-AUTHORITY-ACCEPTANCE-MERGE.md`.

The operative rule uses minimum twenty privates for two human-equivalent workers, ten primary/verifier record pairs per ordinary formation, and adaptive escalation to 40/60/80–100/up to 120 privates for harder sources. Campaign 001 queues 98 obligations across ten formations and 200 slots.

Campaign 001 progress:

- AF01: ACCEPTED COMPLETE;
- accepted archive records: 9;
- blocked completed outcomes: 1 (`D047` MiniRouter source reuse);
- AF02: ACCEPTED COMPLETE;
- accepted archive records: 29 total;
- AF02 remaining evidence: 0;
- AF02 acceptance merge: d1d6b47e935e79790db319ad234b4abccafa4d3f;
- AF03: ACCEPTED COMPLETE;
- AF03 accepted archive records: 10;
- AF03 blocked outcomes: 0;
- AF03 remaining evidence: 0;
- AF03 candidate exact head/run/artifact: `4916f79ff3a0cbac8ee4ae53f9ac09a0065d7b7d` / `30003085272` / `8561809711`;
- AF03 candidate merge: `d86218e1127c57bacfb4d88eff15b81d326995ba`;
- AF03 mission/result/review/acceptance: `archive/campaign-001/af03/MISSION.md`, `archive/campaign-001/af03/RESULT.json`, `archive/campaign-001/af03/SERGEANT-REVIEW.md`, `archive/campaign-001/af03/ACCEPTANCE.md`;
- AF04: READY / NOT STARTED;
- AF02 mission: `archive/campaign-001/af02/MISSION.md`;
- AF01 operative acceptance merge: `ea2424bb5bc2bdb698bfc1bf389601457abd3c89`;
- AF01 candidate exact head: `f60e340cb856d50e88b4279147a933d838fce759`;
- AF01 workflow run/artifact: `29862087745` / `8507695005`;
- AF01 candidate merge: `0a35a8a904bdf235fa4989ea05b684443d5a879a`;
- AF01 acceptance record: `archive/campaign-001/af01/ACCEPTANCE.md`.

AF01, AF02 and AF03 are accepted complete. AF04 remains ready but not started. Archive acceptance does not grant unrestricted source reuse, replace P01 as the active implementation-authorization work, reopen Phase 0A, accept ADR-0033 or authorize runtime implementation.


---

## Accepted Phase 0C-18 diagnostic and efficient-worker boundary

Operative authority:

- `planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md` version `1.0.0`;
- ADR-0036: ACCEPTED;
- Phase 0C-18: COMPLETE;
- candidate merge: `fbc4ee80284a2d7ea38a44fdbfa90f0348b875ae`;
- acceptance evidence: `planning/PTAH-DIAGNOSTIC-WORKER-AUTHORITY-ACCEPTANCE.md`.

Allowed diagnostic behavior: detect missing capability, degradation, incompatibility, resource shortage, repeated failure or failed post-condition and emit an evidence-backed advisory asking an authorized caller for an upgrade or inspection.

Allowed execution behavior: after a caller submits a job and selects a Recipe/Plan, apply `max(20, human-equivalent workers × 10)` to run bounded worker Activities, independent checks, checkpoints and configured merge/recovery mechanics.

Accepted evidence: exact head `d2608ba7c619c1c402091edd619a4b29813ee9a7`, run `29986975197`, artifact `8555395796`, digest `sha256:72025fb0aa5a969ea73abe95d7352f7cf14f1c847943955bd768a46d964a4c61`, validation SHA-256 `aff3a635d37b82c15eeb36f2f6cec780f76e2c3ce320727a18053b913b8d9171`.

Forbidden: choose caller work, invent semantic subtasks, reprioritize outside submitted Policy, approve a result, approve/purchase/install an upgrade, mark acknowledgement as resolution, block unrelated capable work or become Hunter/Sergeant authority.

This accepted clarification uses frozen primitives only, does not start AF03 and does not change P01, ADR-0033 or runtime authorization.

---


## Accepted Phase 0C-19 deep Workspace reconciliation

<!-- PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION -->

- deep study source merge: `23dc4b19a0189ba55e08dfa124761efa806bd68b`;
- 22 mechanical capabilities, 28 mappings, 20 fixtures and 26 original cases;
- zero new Core entities;
- zero WP01–WP14 reopenings;
- Master Plan and roadmap candidate supplement mapped across A, B, D, E and X1–X5;
- ADR-0037: ACCEPTED;
- P01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST;
- roadmap PR #46 proof-candidate selection: CONFIRMED at `23dc4b19a0189ba55e08dfa124761efa806bd68b`;
- physical-host collection: NOT STARTED;
- ADR-0033: PROPOSED;
- runtime implementation: NOT AUTHORIZED.

Immediate order:

```text
run exact physical-host proof
→ review package and package-artifact manifests
→ retain and accept durable evidence
→ complete Phase 0C closure review
→ accept ADR-0033 and explicitly authorize runtime
```

---

## Active Phase 0C blockers

Implementation remains unauthorized until all of the following are merged and reviewed:

1. a proof-eligible capability report from the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
2. the exact installed Ubuntu package manifest and package-artifact digests from that pinned host, with reviewer acceptance;
3. generation, durable commit and explicit review acceptance of that physical-host evidence bundle;
4. a Phase 0C closure review proving no frozen contract was weakened;
5. acceptance of ADR-0033;
6. explicit `Runtime implementation: AUTHORIZED` in this file in the same reviewed closure change.

The frozen catalog, generated binding, exact Rust dependency graph, Cargo lock, cargo-deny policy, distributed backend artifact lock, Browser binary tree, signer lock, cryptographic signature, source-policy, Rust, Browser, host-collector, pinned-host proof-tool, package-artifact, durable-retention, Apache-2.0 governance and frozen-WP13 lanes are complete. They do not close the physical pinned-host result, package acceptance, actual retained-bundle acceptance or any WP14 runtime proof.

### Required first vertical slice after authorization

The first authorized slice must demonstrate, at minimum:

- one Linux Node;
- one persistent Workspace;
- canonical Object registration;
- concurrent Activities and multiple terminals;
- upload and resumable download;
- Git clone or mirror;
- one container execution path;
- one interactive Browser path;
- one decomposition adapter;
- Artifact registration;
- checkpoint, restart and reconnect;
- exact Receipts, generation evidence and negative-path retention.

---

## No-build boundary

Allowed during the remainder of Phase 0C:

- accepted licence, contribution, security and third-party-notice boundary maintenance;
- non-operative behavioural donor, Workspace-profile and Hunter-bridge maintenance;
- exact physical pinned-host and installed-package evidence;
- durable proof-location preparation and pending retention review;
- non-claiming repository and CI maintenance;
- executable proof-plan preparation;
- WP13 integration and contract-conformance maintenance;
- Phase 0C closure review.

Not yet allowed:

- claiming the Ptah runtime or UI is implemented;
- deploying production Nodes, Providers or Workspaces;
- adding runtime functionality under the name of scaffolding;
- weakening the frozen WP14 proof burden;
- bypassing WP13 conformance;
- reusing donor source outside its accepted licence and extraction boundary;
- authorizing implementation without the accepted ADR and exact evidence.

Implementation becomes authorized only when a Phase 0C acceptance ADR and an explicit `Runtime implementation: AUTHORIZED` entry are merged into this file.

---

## Immediate continuation order

1. Install or recover the exact Ubuntu Server 24.04.4 / `6.8.0-136-generic` proof host.
2. Check out confirmed `Ptah-space` commit `23dc4b19a0189ba55e08dfa124761efa806bd68b` and verify a clean tree.
3. Run:

```bash
python3 tools/run_pinned_host_proof.py \
  --repo-root . \
  --output evidence/phase0c/pinned-host-candidate
```

4. Require `proof_eligible: true` with empty host, capability, package-artifact and repository failure sets.
5. Review and accept the exact installed package and package-artifact manifests.
6. From the same exact clean commit, run:

```bash
python3 tools/retain_verified_pinned_host_evidence.py \
  --repo-root . \
  --bundle-dir evidence/phase0c/pinned-host-candidate \
  --output-dir evidence/phase0c/pinned-host-durable-candidate
```

7. Commit and explicitly accept the durable candidate and repository binding.
8. Conduct the final Phase 0C closure consistency review.
9. Accept ADR-0033 and authorize runtime only when every remaining blocker passes.
