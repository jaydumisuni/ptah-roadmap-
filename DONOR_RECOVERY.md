# Ptah Donor Recovery Register

**Phase:** 0A  
**Status:** ACTIVE  
**Purpose:** determine what should be adopted, adapted, wrapped, forked, studied, hosted as a workload, rejected, or built natively before Ptah runtime implementation begins.

This register begins from the approved external donor pool and the recovered internal repository pool. It must be expanded with file-level evidence during inspection.

---

# 1. Required donor record

Every donor must eventually record:

- repository name;
- canonical URL;
- owner or organisation;
- contributor fork or snapshot, if relevant;
- default branch;
- pinned commit SHA;
- pinned release or tag;
- licence;
- primary language;
- last meaningful update;
- activity status: Active, Maintenance, Dormant, Archived, or Unknown;
- Ptah tier and subsystem;
- requirements supported;
- verified capabilities;
- exact directories and files studied;
- architecture patterns to borrow;
- code potentially reusable;
- code or behavior that must not be inherited;
- known limitations;
- security concerns;
- dependency and maintenance risks;
- integration approach;
- licence compatibility decision;
- replacement or exit strategy;
- validation activity;
- evidence collected;
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
- Reject
- Further inspection required

---

# 2. Inspection rule

A donor is not considered inspected from its README alone.

Minimum inspection:

1. repository metadata and canonical upstream;
2. licence;
3. active branch or release;
4. source tree;
5. architecture and runtime entry points;
6. persistence model;
7. concurrency model;
8. error and recovery behavior;
9. tests and CI;
10. exact Ptah boundary;
11. proof against the relevant Ptah requirement.

---

# 3. Foundation-grade inspection order

## Relay, nodes, activities, and control plane

1. `openclaw/openclaw`
2. relevant OpenClaw organisation repositories, especially plugin, source-mirroring, MCP, Google, Git research, compatibility, and platform-control tools
3. `temporalio/temporal` and one likely Ptah SDK
4. `nats-io/nats-server`, JetStream, CLI, and likely clients
5. `open-telemetry/opentelemetry-collector`, contrib, and specification

## Workspace and environment model

6. `daytonaio/daytona`
7. `e2b-dev/E2B`
8. `e2b-dev/desktop`
9. `coder/coder`
10. `All-Hands-AI/OpenHands`
11. Dev Container specification and provider implementations
12. Eclipse Theia and optional OpenVSCode Server
13. Apache Guacamole or equivalent remote-display gateway

## Runtime, builds, and isolation

14. `containerd/containerd`
15. OCI runtime, image, and distribution specifications
16. `moby/buildkit`
17. `dagger/dagger`
18. `moby/moby` and `docker/cli` boundaries
19. `google/gvisor`
20. `kata-containers/kata-containers`
21. `firecracker-microvm/firecracker`
22. `youki-dev/youki`
23. `containers/crun`

## Provenance and artifact integrity

24. `in-toto/witness`
25. `in-toto/in-toto`
26. `sigstore/cosign`, Rekor, Fulcio, and Sigstore
27. `oras-project/oras` and `oras-go`
28. `guacsec/guac`
29. `anchore/syft`
30. `anchore/grype`
31. `aquasecurity/trivy`

---

# 4. Facility-grade inspection order

## Browser and live research

- `microsoft/playwright`
- `microsoft/playwright-mcp`
- `browser-use/browser-use`
- `aza-ali/turbowebfetch`

Primary questions:

- persistent contexts and authenticated profiles;
- concurrency and warm pools;
- interactive and headless use;
- tracing, screenshots, recording, downloads, network, and console events;
- reconnect and recovery;
- neutral browser activity contract.

## Transfer, synchronization, and backup

- internal Download Manager source when recovered;
- `aria2/aria2`;
- `tus/tusd`;
- `rclone/rclone`;
- `syncthing/syncthing`;
- `restic/restic`.

Primary questions:

- resumable transfer;
- segmented and multi-source transfer;
- queue persistence;
- partial-file recovery;
- browser handoff;
- local, R2/S3, Drive, and node transport;
- deduplication and hash verification;
- reusable engine boundary versus product UI.

## Android and physical devices

- `DeviceFarmer/stf`;
- `DeviceFarmer/adbkit`;
- `DeviceFarmer/minicap`;
- `DeviceFarmer/minitouch`;
- `appium/appium`;
- `appium/appium-uiautomator2-driver`;
- `Genymobile/scrcpy`;
- Android ADB/Fastboot source;
- Android UIAutomator source;
- `touchpilot/touchpilot` and `tmimmanuel/touchpilot` relationship;
- internal Device Manager, MIBU, ADB, Fastboot, MTP, META, USB/serial, SPD/Unisoc, and Qualcomm work.

Primary questions:

- device discovery and state;
- remote screen and input;
- semantic UI hierarchy;
- application install and operation;
- device booking/ownership state;
- unstable USB recovery;
- logs, recordings, and activity correlation;
- generic facility versus specialist repair operations.

## General decomposition

- `libarchive/libarchive`;
- Apache Tika;
- Unstructured;
- `lief-project/LIEF`;
- `ReFirmLabs/binwalk`;
- `skylot/jadx`;
- Apktool;
- `libvips/libvips`;
- FFmpeg/ffprobe;
- internal App Recover;
- internal APK Extractor.

Primary questions:

- true-type detection;
- progressive and streaming decomposition;
- recursive child objects;
- source/resource/raw separation;
- executable structures;
- embedded payloads;
- media and image derivatives;
- rebuild proof levels.

## Firmware, disks, and filesystems

- `blacktop/ipsw`;
- MTKClient and internal MTK work;
- Qualcomm EDL/Firehose donors and internal Qualcomm work;
- Android `payload.bin` extraction tools;
- Unisoc PAC/FDL parsers and internal Unisoc work;
- GPT/MBR and sparse image tools;
- Android dynamic-partition tools;
- libguestfs and filesystem-specific tools;
- embedded firmware tooling.

Required families:

- Apple IPSW/OTA/IMG4;
- MediaTek scatter/DA/preloader;
- Unisoc PAC/FDL/NV;
- Qualcomm MBN/ELF/Firehose/rawprogram/patch/content XML;
- generic Android OTA, boot images, vbmeta, sparse images, and super;
- Samsung, Huawei/Honor, LG, Sony, OPPO/Realme/OnePlus;
- embedded and router firmware;
- unknown/plugin-based formats including P5C after a real sample or verified tool is recovered.

## Knowledge, data, and application platforms

- `infiniflow/ragflow`;
- `run-llama/llama_index`;
- `langgenius/dify`;
- `pola-rs/polars`;
- `denoland/deno`;
- database and search-engine candidates.

These may supply connectors, ingestion, indexing, workflow, data, or workload patterns. They must not replace Ptah Core.

## Security workloads

- upstream `usestrix/strix` and contributor fork `josh45-source/strix`;
- `semgrep/semgrep`;
- `aquasecurity/trivy`;
- `zaproxy/zaproxy`.

These are workloads and stress tests unless a smaller neutral component is deliberately extracted.

---

# 5. Experimental, routing, and proof donors

## MiniRouter

Canonical project currently expected at `mini-router/minirouter`, with `tmimmanuel/minirouter` preserved as a contributor snapshot/fork.

Study for:

- coordinator/worker separation;
- low-cost routing;
- activity-state progression;
- worker validation;
- oracle-ceiling diagnostics;
- measurement of routing value rather than assumed value.

Do not make MiniRouter Ptah’s reasoning layer.

## SparkDistill

Canonical project currently expected at `gittensor-model-hub/SparkDistill`, with `tmimmanuel/SparkDistill` preserved as a contributor snapshot/fork.

Study for:

- pinned recipes and datasets;
- independent reproduction;
- hashes and manifests;
- immutable ledgers;
- cryptographically bound claims;
- validator workers;
- GPU capability evidence.

## NeoZorK and ClaimBound

Inspect actual ClaimBound, replay, benchmark, and simulation repositories.

Study for:

- pre-registration;
- frozen targets and gates;
- source lineage;
- honest claim boundaries;
- negative-result retention;
- replay and shadow modes.

The profile README is a discovery source, not reusable runtime code.

## ReproZip

Study for dependency capture, reproducible packaging, and workload replay.

---

# 6. Research and documentation sources

- `aza-ali/awesome-ai-product-management` — research catalogue only;
- `tmimmanuel/tmimmanuel` — discovery map only;
- Chris Ipanaque profile — unresolved until actual implementation repositories are identified;
- `amertoglu16/amertoglu16.github.io` — unresolved until source and functionality are recovered;
- `aza-ali/github-readme-crisp-links` — public documentation tooling only;
- MkDocs Material, Docusaurus, and Mermaid — documentation and diagrams.

---

# 7. Internal donor pool

Internal work defines real operating requirements and may contain reusable code, incomplete prototypes, binaries, research, or specialist engines.

Inspect at minimum:

- Hunter AI;
- TechGuy Tool;
- TechGuy DM;
- TechGuy IMEI;
- TechGuy ADB;
- TechGuy Redirect;
- TechGuy Repair;
- TechGuy Installer;
- TTG Device Manager;
- TTG Enabler;
- Android OTA Manager;
- MIBU;
- MTK META engine;
- ADB, Fastboot, MTP, USB/serial, Qualcomm DIAG, and SPD/Unisoc engines;
- Pay Gateway;
- Software Builder;
- App Recover;
- APK Extractor;
- NETUNLOCKER;
- ZTE generator;
- voice, Cloudflare worker, website assistant, support, and technician workflows where they impose Ptah requirements.

Internal projects are not automatically adopted unchanged. Classify each relevant part as:

- reuse as-is;
- wrap;
- extract shared core;
- extend;
- rebuild with evidence;
- replace;
- reject;
- not yet recovered.

---

# 8. Canonical corrections already identified

- TurboWebFetch: `aza-ali/turbowebfetch`
- Awesome AI Product Management: `aza-ali/awesome-ai-product-management`
- GitHub README Crisp Links: `aza-ali/github-readme-crisp-links`
- OpenClaw: `openclaw/openclaw`
- TouchPilot upstream: `touchpilot/touchpilot`; contributor snapshot/fork: `tmimmanuel/touchpilot`
- MiniRouter upstream: `mini-router/minirouter`; contributor snapshot/fork: `tmimmanuel/minirouter`
- SparkDistill upstream candidate: `gittensor-model-hub/SparkDistill`; contributor snapshot/fork: `tmimmanuel/SparkDistill`
- Strix upstream: `usestrix/strix`; contributor snapshot/fork: `josh45-source/strix`

These relationships must still be pinned and compared before final adoption decisions.

---

# 9. Requirement Closure Matrix template

For each Ptah v1 requirement record:

| Field | Value |
|---|---|
| Requirement ID | |
| Requirement | |
| Phase | |
| Internal evidence | |
| Primary donor | |
| Secondary/exit donor | |
| Mature upstream machinery | |
| Native Ptah gap | |
| Public/private boundary | |
| Licence decision | |
| Integration classification | |
| Validation activity | |
| Evidence | |
| Status | |

---

# 10. Phase 0A completion rule

Phase 0A is complete only when:

- every v1 requirement has a closure path;
- selected donors have canonical upstreams, pinned versions, licences, exact studied components, limitations, and exit strategies;
- internal overlap is recovered;
- code inheritance boundaries are clear;
- native Ptah gaps are isolated;
- implementation dependencies are selected by evidence rather than popularity;
- the findings are reviewed and frozen.
