# Hardware Studio / Cookpit / Creative Studio — Ptah consumer-workspace mapping (2026-10-22)

**Classification:** Private consumer-integration guidance, **not** a new Ptah Programme, runtime feature, admission gate, product-owned roadmap, or separate execution supervisor.

## Why this record exists

The engineering objective is to produce an evidence-qualified TechGuy ISP Box v6.0 manufacturing package **inside a recoverable working environment**. The owner has accepted a division of responsibility between an engineering application, a visual-production application and existing workflow supervision. Ptah is the general **workspace and execution substrate** for these products, not the authority that decides their engineering work.

### Canonical project inputs

- [TTG Hardware Studio roadmap](https://github.com/jaydumisuni/TTG-Hardware-Studio/blob/main/ROADMAP.md): G0 architecture documented; C0 Cookpit intake ready **but not active**; G1 shared electro-mechanical USB-C Product Graph; G2 CAD/EDA adapters; G3 ISP Box engineering candidate; G4 manufacturer-ready release; optional parallel V1 visualization adapter; G5 physical qualification.
- [ISP Box source repository](https://github.com/jaydumisuni/isp-box-): manufacturer-submitted v6.0 schematic/package PDFs preserved, engineering source and supplier correspondence. They are **not** verified complete pin-level schematics, Gerbers or BOM. Manufacturer has supplied a framework/feasibility response and separate design-service prices, **not** a final fabrication quote.
- [TTG Creative Studio](https://github.com/jaydumisuni/ttg-creative-studio): existing Studio-owned presentation scene execution and isolated Blender-backed 3D/PBR rendering path. The ISP Box *concept* preset is **not manufacturing-accurate geometry**. A Hardware Studio -> Creative Studio authoritative geometry handoff is **not qualified**.
- [Cookpit](https://github.com/jaydumisuni/cookpit): existing registered-project control plane and five rotating supervisors; Hardware Studio is **not registered in the canonical Cookpit main registry** as of the evidence recovered for this note.

## Authority and transport

| Layer | Owns | Does not own |
| --- | --- | --- |
| **Hardware Studio / its Director** | Electrical and mechanical Product Graph; exact PCB and enclosure model; schematic, BOM, fabrication/assembly outputs; fit/electrical verification and release candidate decisions under project authority | Photoreal/cinematic renderer, generic workspace operations, or Cookpit supervision |
| **Creative Studio / its Director** | Product presentation interpretation; lighting, materials, camera, exploded views, animations; Studio scene/render job/receipts | Engineering CAD truth, part coordinates as design authority, ERC/DRC, manufacturing approval |
| **Cookpit + existing rotating supervisor** | Profile/registry onboarding, dependency frontier, bounded workers, exact-head proof and supervision of continuing Hardware Studio work | Product design authority, separate Director, unauthorized protected-main release |
| **Ptah Space** | Authorized persistent workspaces, Activities, tool/terminal/provider use, Git/source access, files, artifacts, evidence and recovery; execute exact caller-chosen work using supported installed facilities | Owner strategy, CAD/EDA domain laws, Creative renderer, job-priority decisions, product release judgment, or an extra approval for ordinary workspace use |
| **Oracle Live** | Authenticated machine transport to available workstations where invoked | Project planning, Ptah identity, CAD/EDA execution authority; permanent unattended packet forwarding without separate proof |

## Supported end-to-end intent

1. Cookpit supervises implementation work **after** Hardware Studio C0 project-specific onboarding, registry admission and actual runtime discovery; prior to that state, Hardware Studio may still undertake independent, safe G1 engineering.
2. Hardware Studio's **own Director** accepts the intended circuit/mechanical changes and produces/validates native engineering artifacts in a Ptah workspace on an available machine. Prefer KRATOS for ordinary software design/build tasks; ATHENA is an optional direct host when the actual task needs it, not a permanent KRATOS dependency. Oracle may transport cross-node execution when available. Ptah does not invent a second CAD planner.
3. When an approved revision is ready for visual presentation, Hardware Studio exports a **read-only, revision-pinned** CAD-derived snapshot (coordinate systems, units, meshes/part IDs/transforms, assembly hierarchy, and source digest through a **verified compatible format**). Do **not** assume STEP ingestion exists in Creative Studio.
4. Creative Studio's **existing Director and renderer** consume the snapshot inside an authorized workspace, create product stills/turntables/exploded animation and store visual output with source-revision identity. Visual assets **do not write back** manufacturing geometry or imply dimension/functional qualification.
5. Hardware Studio owns ERC, DRC, tolerance, fitting, assembly, source-backed BOM/Gerber/CPL/STEP release and final engineering results. Ptah retains process, source and artifact evidence; Cookpit observes exact implementation progression. The manufacturer supplies actual fabrication/components/PCBA/shipping quotation once complete Gerber and BOM are submitted.
6. When a facility/backend/machine is unavailable, Ptah reports that *specific operation's* failure without denying unrelated workspace capabilities or freezing independent local work. No new access policy, global login, hand-issued Grant, model-host coupling or paid rendering dependency is introduced.

## Evidence and qualification states

| Obligation | Status as at 2026-10-22 |
| --- | --- |
| Hardware Studio roadmap and C0/G1..G5/V1 boundaries | DOCUMENTED |
| Reusable Creative Studio 3D/presentation engine and native directed scene execution | IMPLEMENTED in Studio; proofs scoped to its own contracts |
| Cross-product CAD geometry -> Studio visual snapshot/import contract | NOT IMPLEMENTED / NOT QUALIFIED |
| Hardware Studio engineering Product Graph, PCB/CAD adapters and release candidate | NOT IMPLEMENTED / NOT QUALIFIED |
| Cookpit Hardware Studio registration, micro/heavy proof and supervisor discovery | NOT REGISTERED / NOT ACTIVE |
| Ptah task running inside generic supported workspace/terminal operations | EXISTING GENERAL CAPABILITY; **no Hardware Studio-specific end-to-end Ptah integration proven** |
| Final supplier fabrication quote, payment and physical ISP Box qualification | NOT ESTABLISHED |

### Acceptance for an eventual Ptah consumer proof

- Recover source repository/revision, workspace/Activity, machine, tool and artifact digest; no cross-project authority confusion.
- Run a bounded real G1 engineering activity in a Ptah workspace, retain stdout/stderr/checks/artifacts, and independently compare against a direct run.
- Preserve a revision-pinned visual export handed to the **existing Studio** job, check dimensions/transform fidelity separately from visual attractiveness, and verify replay/provenance.
- Cookpit's real registry entry, profile and observation are independently qualified; an unregistered repo must not be reported as already supervised.
- Show that a failed Creative render does not block valid manufacturing work; that unavailable remote compute does not block independent KRATOS work; and that presentation artifacts cannot mutate product authority.
- No special Ptah authentication or approval beyond a caller's established legitimate workspace/tool access; no manufactured progress without evidence.

## Release / sequence constraints

This mapping belongs under Ptah's **existing** AI Project Workspace (D02), Activity/Artifact/Provider/Git operation substrate and existing external transport compatibility. **Do not create a new Ptah-specific product-adapter programme, GPU/render engine, CAD kernel or per-project supervisor.** If a later actual workflow needs a missing general Ptah capability, isolate and qualify that exact neutral capability without altering Hardware Studio's own gates. Programme F04–F07 Prime OS integration remains **last**; this mapping does not advance or block E07 unattended roaming claims.

**No implementation/production activation is asserted by adding this document.**
