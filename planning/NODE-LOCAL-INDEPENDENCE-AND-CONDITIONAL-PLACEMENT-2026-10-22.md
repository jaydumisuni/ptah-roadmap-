# Node-local independence and conditional placement — 2026-10-22

**Status:** Owner clarification of Ptah's existing accepted operating modes. This
clarifies sequencing and consumer routing. It is not a new programme, a new
E08 milestone, a request to reopen frozen contracts, an authorization gate or
a claim that any currently missing production feature is complete.

## Controlling execution order

1. **The Node is independently useful.** KRATOS and ATHENA each host their
   own Ptah workspace capability, state and locally available providers.
   Neither Node must be online, enrolled into the other's workflow, or
   reachable by the other for an ordinary local project to proceed. A
   persistent project/workspace remains usable across tasks, client changes,
   process restarts and ordinary disconnections within its qualified
   recovery guarantees.
2. **Select the working Node before execution.** Human, Hunter or the
   product-owning caller determines where a task is intended to run.
   Normally this is the machine on which the user is working, or the
   machine already holding the project workspace. Ptah performs actual
   technical resource/capability checks and workspace execution on that
   Node; Ptah does not second-guess the user's purpose or automatically
   transfer work simply because another Node exists.
3. **Keep execution local.** Tool development, ordinary builds, Git,
   documentation and available tests use the selected Node's local Ptah
   workspace. Cookpit retains its existing supervisors, project logic,
   worker behaviour and approved timeouts; integrating its workspace with
   Ptah must not replace healthy local execution with an E07 remote
   gateway or impose a 25/30-second limit inherited from a narrow test
   worker. WorkCell duration follows the actual task/Provider capability,
   not a generic synchronous transport wait.
4. **Identify the actual shortage.** Check missing RAM, CPU, GPU, operating
   system, dependency, installed tool, connected device or other precise
   constraint. Report `CAPABILITY_MISSING` for required current capability
   and `PLANNED_HARDWARE_DEPENDENCY` for intentionally deferred hardware
   work. These are descriptive operational dispositions, not a new
   frozen-contract enum or Ptah access denial. Do not mark an entire
   project blocked because one optional future test cannot yet run.
5. **Defer only the affected stage.** A project may be designed, built and
   ordinarily tested on existing machines while its GPU/local-model or
   special hardware test remains parked in the accepted hardware roadmap.
   In the current operating phase the AI reasoning/models are online;
   there is no demonstrated local-model compute workload that requires
   KRATOS-to-ATHENA distribution during ordinary tool building. GT502 and
   GDX Spark hardware lanes become active only when their relevant
   hardware-dependent stage is genuinely ready.
6. **Cross-Node execution is conditional.** E01–E07 identity, placement,
   transfer, compatible movement and remote proof remain supported,
   optional capabilities for a *specific* workload that genuinely needs
   another machine or target device, or for a user-selected remote
   workflow. They do not become startup prerequisites for local Ptah,
   Cookpit, Hunter or ordinary projects.
7. **No silent failover or ownership transfer.** If the chosen machine
   lacks resources, show the exact shortage and viable choices to the
   owning caller. Moving a running workload, duplicating a workspace,
   moving project authority, or restarting an uncertain effect on another
   Node requires its own explicit, qualified operation and evidence.
   Git synchronization or project continuation is distinct from remote
   compute. Offline of one Node does not stop unrelated work on another.
8. **Preserve existing product Directors.** Cookpit supervises, product
   Directors decide their own tasks and project meaning, Ptah operates
   reusable workspaces and technical Facilities, Oracle transports
   authenticated calls to machines when remote machine access is
   actually requested. Do not create duplicate planners, supervisors
   or a Ptah user-permission layer.

## Proof and sequencing consequences

- E06's local-first/recovery capabilities stand on their own, regardless
  of E07 network availability.
- E07's physical KRATOS-to-ATHENA native test remains valid **for exactly
  what it proved**: caller-mediated E01/E02/A05 via Oracle; it is not
  evidence that local jobs should run remotely, a mandatory dependency,
  or autonomous unattended cross-network forwarding.
- Current Cookpit PR #72's E07-specific short-job bridge must not be
  mistaken for the intended *general* Cookpit workspace integration.
  Its special timeout is not a Ptah WorkCell architectural limit.
  The missing generic integration is reuse of durable, Node-local Ptah
  workspaces without changing Cookpit's already-working worker semantics.
- E07 autonomous transport, if developed, is an optional distributed
  feature. It is not a release gate for an ordinary local workspace or
  a reason to recruit ATHENA into KRATOS jobs.
- Programme E still ends at **E07**, with no invented E08.
  F01–F03 remain standalone; Prime OS F04–F07 integration stays LAST.
- A qualification report should explicitly show (a) selected Node,
  (b) local workspace and provider availability, (c) unmet capability
  if any, (d) exact executed vs deferred stages, and (e) whether a
  deliberate remote execution path was used. Never infer a shortage
  merely because a stronger planned Node exists.

## Scope control

Accepted `MASTER_PLAN.md` §8.2–8.5 already describes local, hybrid,
offline/local-first and distributed operating modes. This clarification
makes their **default priority** unambiguous and supersedes any reading
of earlier E07 roaming language as a universal requirement. Historical
E07 proof records are retained unchanged. Do not modify Ptah runtime,
Cookpit runtime, physical Node configuration, Oracle, Knights, hardware
projects or user workloads merely to accept this roadmap correction.
