<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/zcxGGmu/zcxGGmu/output/github-contribution-grid-snake-dark.svg?v=30026077052">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/zcxGGmu/zcxGGmu/output/github-contribution-grid-snake.svg?v=30026077052">
    <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/zcxGGmu/zcxGGmu/output/github-contribution-grid-snake.svg?v=30026077052">
  </picture>
</p>

<p align="center">
  <sub>contribution graph rendered with <a href="https://github.com/Platane/snk">Platane/snk</a></sub>
</p>

---

## Open PR Radar

_Tracks public PRs authored by [@zcxGGmu](https://github.com/pulls?q=is%3Apr+author%3AzcxGGmu), refreshed every 12 hours._

<!-- pr_activity starts -->
- **Status**: **160 PRs** across **31 projects** — 🟢 80 open · ✅ 16 merged · ⚪ 64 closed
- **Active projects**: [kvcache-ai/ktransformers](https://github.com/kvcache-ai/ktransformers) (15 open), [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) (9 open), [vllm-project/vllm](https://github.com/vllm-project/vllm) (8 open), [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) (5 open), [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) (5 open), [aaif-goose/goose](https://github.com/aaif-goose/goose) (5 open)
- **Latest PRs**:
  - 🟢 [InternLM/lmdeploy#4823](https://github.com/InternLM/lmdeploy/pull/4823) — Open — \[Docs\] Explain Ray object spilling warning
  - 🟢 [InternLM/lmdeploy#4822](https://github.com/InternLM/lmdeploy/pull/4822) — Open — \[Docs\] Clarify TurboMind engine acceleration
  - 🟢 [microsoft/onnxruntime#31633](https://github.com/microsoft/onnxruntime/pull/31633) — Open — docs: update phi-2 GenAI Python API usage
  - 🟢 [InternLM/lmdeploy#4821](https://github.com/InternLM/lmdeploy/pull/4821) — Open — \[Docs\] Explain prompt hidden states in pipeline
  - 🟢 [microsoft/onnxruntime#31631](https://github.com/microsoft/onnxruntime/pull/31631) — Open — docs: fix OpenVINO comparison labels
  - 🟢 [microsoft/onnxruntime#31630](https://github.com/microsoft/onnxruntime/pull/31630) — Open — docs: clarify OpenVINO load_config value
<!-- pr_activity ends -->

## Current Projects

- [**CodeInsights**](https://github.com/zcxGGmu/CodeInsights) — an LLM-powered multi-agent platform for open-source contribution workflows. It is built around repository understanding, issue/PR scouting, agent coordination, and turning scattered open-source work into a repeatable engineering loop.
- [**yuansheng-kit**](https://github.com/YuanshengClaw/yuansheng-kit) — an agent-oriented toolkit for RISC-V optimization knowledge extraction, pattern mining, real-hardware performance analysis, root-cause diagnosis, and code generation.
- [**ClawPerch**](https://github.com/zcxGGmu/ClawPerch) — a lightweight desktop perch for watching and managing OpenClaw / Codex-style agents. It focuses on keeping long-running agent work visible, interruptible, and operationally sane.
- [**openclaw-apex-team**](https://github.com/zcxGGmu/openclaw-apex-team) — a customizable OpenClaw engineering team framework for building, coordinating, and shipping with specialized AI agents.
- [**hermes-hip**](https://github.com/zcxGGmu/hermes-hip) — a Hermes + Whip event-to-channel notification router that bypasses gateway sessions to avoid context pollution.
- [**Ferrovisor**](https://github.com/zcxGGmu/Ferrovisor) — a memory-safe, high-performance type-1 hypervisor built in Rust.
- [**serenity-alpha-lab**](https://github.com/zcxGGmu/serenity-alpha-lab) — a research-only lab for stock, sector, and theme analysis inspired by Serenity-style reasoning. The goal is not to chase signals blindly, but to build clearer research workflows around narratives, fundamentals, and market structure.

---

**Linux Work Plan — RISC-V upstream candidates**

_Source map: [linux-riscv-docs/patch-work](https://github.com/zcxGGmu/linux-riscv-docs/tree/main/patch-work). These are snapshot-based candidates; before starting a patch, I re-check mainline, linux-next, maintainer trees, and lore._

- **KVM / G-stage memory** — build toward better RISC-V virtualization observability and lifecycle correctness: `VIRT-01` G-stage / IOMMU ptdump, `VIRT-02` lockless and reschedulable teardown, and `VIRT-04` `KVM_PRE_FAULT_MEMORY`. Sources: [ranked roadmap](https://github.com/zcxGGmu/linux-riscv-docs/blob/main/patch-work/riscv-arm-x86-gap/09-ranked-contribution-roadmap.md), [KVM 2026H1 candidates](https://github.com/zcxGGmu/linux-riscv-docs/blob/main/patch-work/kvm-riscv/analysis/kvm-2026h1-curated-candidates.md).
- **MMU / TLB / DMA correctness** — focus on high-impact memory-management gaps such as `MM-02` batched non-coherent DMA sync, `MM-06` precise `pte_needs_flush()`, and `MM-11` hot-remove range TLB batching. Source: [MMU, memory, and TLB gap analysis](https://github.com/zcxGGmu/linux-riscv-docs/blob/main/patch-work/riscv-arm-x86-gap/03-mmu-memory-tlb.md).
- **ISA-optimized kernel primitives** — land small but measurable RISC-V-specific primitives first: `ISA-01` Zbb `memcmp`, `ISA-02` Zbb `memchr`, and `ISA-03` Zvkg POLYVAL hooks. Sources: [ISA optgap overview](https://github.com/zcxGGmu/linux-riscv-docs/blob/main/patch-work/claude-4-8/riscv-isa-optgap/README.md), [string asm notes](https://github.com/zcxGGmu/linux-riscv-docs/blob/main/patch-work/claude-4-8/riscv-isa-optgap/analysis/asm_string.md), [crypto asm notes](https://github.com/zcxGGmu/linux-riscv-docs/blob/main/patch-work/claude-4-8/riscv-isa-optgap/analysis/asm_crypto.md).
- **Hardening and observability** — help unblock higher-level tooling through `CORE-01` reliable unwinder / livepatch review work, BPF stack-walk exception coverage, and `CORE-16` `ARCH_HAS_EXECMEM_ROX`. Source: [core ABI, observability, and hardening roadmap](https://github.com/zcxGGmu/linux-riscv-docs/blob/main/patch-work/riscv-arm-x86-gap/05-core-abi-observability-hardening.md).
- **Platform, ACPI, and RAS enablement** — advance system-level readiness with `PLAT-01` ACPI CPU physical hotplug, `PLAT-06` CPPC FIE / RV32 `READ_HI`, and `BOOT-01` crashkernel CMA wiring. Sources: [platform, ACPI, NUMA, power, and RAS roadmap](https://github.com/zcxGGmu/linux-riscv-docs/blob/main/patch-work/riscv-arm-x86-gap/06-platform-acpi-numa-power-ras.md), [patch-work overview](https://github.com/zcxGGmu/linux-riscv-docs/blob/main/patch-work/README.md).

## Areas of Interest

- **Linux kernel / RISC-V KVM** — I have contributed across RISC-V KVM, guest statistics, interrupt reporting, guest extension enablement, dirty memory tracking, gstage mapping, VMID / nested virtualization exploration, and related kernel paths.
- **Patch-first engineering** — I treat upstream kernel work as a long-running trail of small, reviewable patches: some land, some evolve through review, and some become the next iteration of the design.
- **Community PRs** — I also count public PR work across major communities, whether merged or not, because the engineering value is in the attempt, discussion, review, and iteration. My PR trail spans projects such as CopilotKit, OpenHands, ragflow, SWE-agent, pydantic-ai, LlamaIndex, Haystack, Dify, anything-llm, Flowise, and related AI / agent ecosystems.
- **Contribution surface** — low-level systems, open-source AI infrastructure, agent frameworks, developer tooling, and workflows that make complex repositories easier to understand and improve.

## AI Systems Philosophy

> The important layer is not the generated files. Code is the artifact; the system that produces, reviews, retries, and ships the code is the real thing to study.

My current engineering lens:

- Human value moves upward: direction, constraints, taste, judgment, and knowing what is worth building.
- Agents should not be treated as faster autocomplete. The real jump is the orchestration layer: planning, execution, review, notification, retry, and recovery.
- Good AI systems are closed loops, not one-shot prompts. They keep working when nobody is staring at the terminal.
- The bottleneck is no longer typing speed. It is problem decomposition, architectural clarity, feedback design, and the ability to distinguish signal from noise.
- The best systems amplify clear thinking. They do not replace it.

<p align="center">
  <sub>systems at the bottom · agents at the edge · orchestration in the loop</sub>
</p>

## Writing

- [**zcxGGmu's Blog**](https://zcxggmu.github.io/) — long-form notes on systems, AI, open-source work, investing, and durable workflows.

_Latest posts, refreshed with the README automation:_

<!-- blog_posts starts -->
- [Tech Rebound AI Computing Volume Growth Strategy](https://zcxggmu.github.io/2026/tech-rebound-ai-computing-volume-growth-strategy/) — 2026-08-04
- [Know And Accept Yourself Seligman Change Depth Map](https://zcxggmu.github.io/2026/know-and-accept-yourself-seligman-change-depth-map/) — 2026-08-04
- [Myside Bias Truth Polarization Public Reason](https://zcxggmu.github.io/2026/myside-bias-truth-polarization-public-reason/) — 2026-08-04
- [Anti Risk Investing Low Cost Diversification Long Term System](https://zcxggmu.github.io/2026/anti-risk-investing-low-cost-diversification-long-term-system/) — 2026-08-04
- [Software AI Application Investment Logic Agent Custom Software](https://zcxggmu.github.io/2026/software-ai-application-investment-logic-agent-custom-software/) — 2026-08-03
<!-- blog_posts ends -->

<!-- hermes_evolution starts -->
## Hermes Evolution

<p align="center">
  <img alt="Hermes evolution daily cockpit" src="./assets/hermes-evolution.svg?v=20260805060016">
</p>

<p align="center">
  <sub>Auto-refreshed daily at 06:00 CST · public memory details are privacy-redacted</sub>
</p>

- **Latest snapshot:** 2026-08-05 06:00 CST; archive date `2026-08-04`.
- **Skills:** 161 tracked / 152 active; today `+0 Δ19 -0`; activity `+407`, patches `+56`.
- **Memory:** 14 durable entries; today `+1 -1`; Memory map +1 added / +1 removed · details privacy-redacted.
- **Signal:** Δ github-contribution-triage · patch +26, use +35, view +31; Δ scheduled-pr-feedback-maintenance · patch +16, use +18, view +13
<!-- hermes_evolution ends -->

