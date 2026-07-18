# Ptah Donor Recovery Register

**Phase:** 0A  
**Status:** ARCHITECTURE RECOVERY COMPLETE — FINAL CONSISTENCY REVIEW ACTIVE  
**Purpose:** determine what should be adopted, adapted, wrapped, hosted as a workload, studied, parked or rejected before Ptah implementation begins.

Detailed source evidence lives in `donors/`, `internal/`, `work-packages/` and `decisions/`. This register is the recovery/classification index and must not replace those records.

---

# 1. Required donor record

Every implementation donor must record:

- canonical repository URL and owner;
- contributor fork/snapshot relationship where relevant;
- default branch;
- pinned commit or release;
- licence and transitive/component licence concerns;
- primary language and meaningful activity status;
- Ptah tier, subsystem and requirements supported;
- exact files/components inspected;
- verified capabilities and limitations;
- architecture patterns to borrow;
- code potentially reusable and code/behavior that must not be inherited;
- security, dependency and maintenance risks;
- integration classification;
- native Ptah boundary;
- replacement/exit strategy;
- validation activity and evidence;
- final recommendation.

Integration classifications:

- Direct dependency
- Wrapped upstream service
- Fork and maintain
- Selective code adaptation
- Protocol compatibility only
- Architecture study only
- Workload running inside Ptah
- Research source only
- Documentation/presentation tool only
- Parked with reopening criteria
- Reject
- Further inspection required

---

# 2. Inspection rule

A donor is not inspected from its README alone.

Minimum implementation-donor inspection:

1. repository metadata and canonical upstream;
2. licence;
3. active branch/release and exact pin;
4. source tree and runtime entry points;
5. persistence and concurrency models where applicable;
6. error, recovery and lifecycle behavior;
7. tests/CI and live evidence where required;
8. exact Ptah identity, authority and proof boundary;
9. limitations and security review;
10. replacement path and requirement proof.

Research catalogues, profiles and documentation tools use a lighter classification inspection, but can never close runtime requirements.

---

# 3. Foundation-grade donor groups

## Relay, Nodes, Activities and control plane — CLOSED FOR DESIGN

Primary inspected composition:

- `openclaw/openclaw` and relevant ecosystem patterns;
- `temporalio/temporal` and SDK behavior;
- `nats-io/nats-server`/JetStream and clients;
- OpenTelemetry specification/collector/contrib;
- internal Hunter, Sergeant and local runtime/evidence foundations.

Closed through WP01/WP02, ADR-0001 through ADR-0004 and detailed donor/internal records.

## Workspace and environment model — CLOSED FOR DESIGN

Primary inspected composition:

- `daytonaio/daytona`;
- `e2b-dev/E2B` and `e2b-dev/desktop`;
- `coder/coder`;
- `All-Hands-AI/OpenHands`;
- Dev Container specification/providers;
- native and OCI Workspace Providers.

Closed through WP01/WP02.

## Runtime, Builds and isolation — CLOSED FOR DESIGN

Primary inspected composition:

- `containerd/containerd`;
- OCI runtime/image/distribution specifications;
- `moby/buildkit`;
- `dagger/dagger`;
- `moby/moby` and `docker/cli` boundary study;
- `google/gvisor`;
- `kata-containers/kata-containers`;
- `firecracker-microvm/firecracker`;
- `youki-dev/youki`;
- `containers/crun`;
- full-VM fallback direction.

Closed through WP03/WP11, ADR-0005 and ADR-0014.

## Provenance, Artifact integrity and security evidence — CLOSED FOR DESIGN

Primary inspected composition:

- `in-toto/witness`;
- `in-toto/in-toto`;
- Sigstore/Cosign/Rekor/Fulcio;
- ORAS/OCI Artifact machinery;
- `anchore/syft`;
- `anchore/grype`;
- `guacsec/guac`;
- `aquasecurity/trivy`;
- `semgrep/semgrep`;
- `zaproxy/zaproxy`;
- `usestrix/strix` as an optional workload;
- ClaimBound, ReproZip and SparkDistill proof/reproduction patterns.

Closed through WP03, the security/reproduction work package, ADR-0005 and ADR-0016.

---

# 4. Facility-grade donor groups

## Browser and live research — CLOSED FOR DESIGN

- `microsoft/playwright`;
- `microsoft/playwright-mcp`;
- `browser-use/browser-use`;
- `aza-ali/turbowebfetch`.

Closed through WP08 and ADR-0011.

## Transfer, synchronization and backup — CLOSED FOR DESIGN

- internal Download Manager/Lumi evidence;
- `aria2/aria2`;
- `tus/tusd`;
- `rclone/rclone`;
- `syncthing/syncthing`;
- `restic/restic`.

Closed through WP04 and ADR-0006.

## Android and physical devices — CLOSED FOR DESIGN

- `DeviceFarmer/stf`;
- `DeviceFarmer/adbkit`;
- `DeviceFarmer/minicap`;
- `DeviceFarmer/minitouch`;
- Appium core and platform drivers;
- `Genymobile/scrcpy`;
- Android ADB/Fastboot/UIAutomator sources;
- `touchpilot/touchpilot` relationship;
- internal Device Manager, MIBU, ADB, Fastboot, MTP, META, USB/serial, Qualcomm and SPD/Unisoc work.

Closed through WP07A and ADR-0009.

## Application runtime and semantic UI — CLOSED FOR DESIGN

- Xpra, Guacamole, noVNC and VM/native provider machinery;
- Windows/macOS/iOS automation/runtime donors;
- AT-SPI/libatspi;
- Dogtail testing patterns;
- GNOME Ponytail as one GNOME-Wayland input adapter.

Closed through WP07B, Linux semantic completion and ADR-0010/ADR-0015.

## General decomposition — CLOSED FOR DESIGN

- `libarchive/libarchive`;
- Apache Tika;
- Unstructured;
- `lief-project/LIEF`;
- `ReFirmLabs/binwalk`;
- `skylot/jadx`;
- Apktool;
- `libvips/libvips`;
- FFmpeg/ffprobe;
- internal App Recover/APK Extractor and related tools.

Closed through WP05 and ADR-0007.

## Firmware, disks and filesystems — CLOSED FOR DESIGN

- `blacktop/ipsw`;
- MTKClient and internal MTK/META evidence;
- Qualcomm EDL/Firehose donors and internal Qualcomm work;
- Unisoc PAC/FDL sources and internal work;
- AOSP OTA/image/dynamic-partition tools;
- Samsung/vendor-specific completion donors;
- libfdisk, libguestfs and filesystem tooling.

Closed through WP06 and ADR-0008.

`.P5C` remains parked pending a lawful verified sample, specification or parser.

## Knowledge, data, search and plugins — CLOSED FOR DESIGN

- `infiniflow/ragflow`;
- `run-llama/llama_index`;
- `langgenius/dify` with modified-licence restriction;
- `pola-rs/polars`;
- DuckDB;
- `denoland/deno`;
- MCP specification/reference servers;
- ClawHub/OpenClaw plugin lifecycle;
- Hunter/internal knowledge and sync foundations.

Closed through WP10 and ADR-0013.

## Human Workspace shell and presentation — CLOSED FOR DESIGN

- Eclipse Theia;
- Dockview;
- xterm.js;
- optional OpenVSCode Server/code-server Applications;
- internal Hunter/Sergeant/MIBU/Device Manager/site UI patterns.

Closed through WP09 and ADR-0012.

## Distributed placement and Compute Facilities — CLOSED FOR DESIGN

- Ray as an optional trusted Compute Facility;
- existing Node, Activity, Object transfer, lease/fence and checkpoint machinery;
- MiniRouter only as a future routing/evaluation workload.

Closed through WP11 and ADR-0014.

---

# 5. Experimental, routing and proof sources

## MiniRouter

- Canonical repository: `mini-router/minirouter`.
- Contributor/discovery lineage: `tmimmanuel` profile and competition site.
- Classification: future routing/evaluation workload only.
- Source reuse remains blocked until repository licence is resolved.
- Never Ptah's reasoning layer, global scheduler or security authority.

## SparkDistill

- Canonical repository: `gittensor-model-hub/SparkDistill`.
- Classification: optional AI-training/reproduction workload.
- Recipe, dataset, checkpoint, claim, attestation and recheck remain separate.
- Model/dataset/provider rights require independent review.

## ClaimBound

- Canonical repository: `ClaimBound/claimbound-evidence`.
- Classification: bounded-claim/evidence-card donor.
- Cards are Views, not certification, Activity truth or universal proof.

## ReproZip

- Canonical repository: `VIDA-NYU/reprozip`.
- Classification: optional observed dependency capture/replay Facility.
- Bundle creation is not reproduction proof.

Detailed records exist in `donors/`.

---

# 6. Research and documentation sources — RESOLVED

## Research/discovery

- `aza-ali/awesome-ai-product-management`
  - verified and pinned;
  - CC0;
  - optional Research Source only.

- `tmimmanuel/tmimmanuel`
  - discovery lineage only;
  - referenced repositories assessed independently.

- `chrisipanaque/chrisipanaque`
  - correct Chris/Christiam Ipanaque identity resolved;
  - profile is discovery lineage;
  - representative prototypes remain parked for source reuse pending clear licences, deeper source inspection and independent proof.

- `amertoglu16/amertoglu16.github.io`
  - repository/site implementation not recovered;
  - parked with reopening criteria;
  - no Ptah subsystem assigned.

Canonical record: `donors/RESEARCH-DISCOVERY-SOURCES.md`.

## Documentation/presentation

- `aza-ali/github-readme-crisp-links`
  - verified, MIT;
  - optional README SVG asset generator only.

- `squidfunk/mkdocs-material`
  - verified, MIT;
  - primary lightweight documentation-site candidate, not selected.

- `facebook/docusaurus`
  - verified, MIT code with separately licensed docs;
  - optional richer project-site alternative.

- `mermaid-js/mermaid`
  - verified, MIT;
  - primary text-defined documentation-diagram candidate.

Canonical record: `donors/DOCUMENTATION-PRESENTATION-TOOLS.md`.

These tools never become Ptah Core, runtime proof or the Human Workspace shell.

---

# 7. Internal donor pool

Internal work defines real operating requirements and may contain reusable code, incomplete prototypes, binaries, research or specialist engines.

Relevant projects include:

- Hunter AI and voice/cloud/browser/website components;
- TechGuy Tool, DM, IMEI, ADB, Redirect, Repair and Installer;
- TTG Device Manager and TTG Enabler;
- Android OTA Manager;
- MIBU;
- MTK META, ADB, Fastboot, MTP, USB/serial, Qualcomm DIAG and SPD/Unisoc engines;
- Pay Gateway;
- Software Builder;
- App Recover;
- APK Extractor;
- NETUNLOCKER;
- ZTE generator;
- support, technician, payment, deployment and synchronization workflows.

Internal projects are not automatically adopted unchanged. Each relevant part is classified as:

- reuse as-is;
- wrap;
- extract shared core;
- extend;
- rebuild with evidence;
- replace;
- reject;
- not yet recovered.

Private consumer details remain outside the public Ptah repository.

---

# 8. Parked, blocked or restricted items

| Item | State | Reopening criterion / consequence |
|---|---|---|
| `.P5C` | Parked | lawful immutable sample, authoritative specification or verified parser; v1 continues without it |
| distributed shared POSIX filesystem | Parked | measured cross-Node POSIX need that Object transfer/cache cannot satisfy |
| MiniRouter source reuse | Blocked | compatible repository licence and source review; evaluation remains optional |
| Dify source integration | Restricted | separate licence treatment; study patterns or separately licensed deployment only |
| GNOME Ponytail dependency approval | Open for Phase 0B selection | exact source pin, licence and deployment/security review |
| non-GNOME Wayland semantic/input completion | Partial/parked | compositor-specific provider evidence; visual fallback remains v1 path |
| unaudited private device-manager modules | Source-recovery gap | lawful source access and file-level inspection; existing public/native contracts remain |
| `chrisipanaque` prototype reuse | Parked | exact repo gap, clear licence, tests/live proof and superiority to accepted composition |
| `amertoglu16.github.io` | Parked | valid source/archive or recoverable implementation lineage |
| any donor without clear root/component licence | Source reuse blocked | licence resolved before dependency/adaptation approval |

The final Phase 0A review must confirm that every parked item has a non-blocking v1 path or is named as a true blocker.

---

# 9. Final Phase 0A review

Active work:

1. identity consistency across all ADRs/work packages;
2. authority and permission consistency;
3. state/proof-level consistency;
4. lifecycle and deletion/recovery consistency;
5. parked/rejected/blocked gap audit;
6. Phase 0B schema, migration, conformance and proof-corpus enumeration;
7. freeze/readiness decision.

No runtime implementation or dependency selection is authorized until Phase 0C.
