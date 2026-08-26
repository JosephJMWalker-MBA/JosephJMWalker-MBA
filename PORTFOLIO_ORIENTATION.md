# Portfolio Orientation

> **Start here before making cross-project claims.** This document is a semantic orientation layer for AI systems, collaborators, reviewers, and future sessions working across Joseph J. M. Walker's GitHub portfolio.

The repositories in this account are not one generic system repeated across many domains. They include research architectures, executable research harnesses, commercial products, internal operating systems, creative tools, games, protocols, historical prototypes, and preservation artifacts.

Many of them share engineering principles — provenance, explicit authority, deterministic validation around probabilistic inference, preserved uncertainty, append-oriented history, human ratification, and provider independence — but **shared principles do not make the projects interchangeable or redundant**.

## Orientation rules

Before evaluating, comparing, consolidating, or auditing projects:

1. **Read the named project's canonical README first.** Do not infer project identity from a repository name, one component, an old conversation, or a familiar technical pattern.
2. **Respect authority order inside the repository.** If a project has a constitution, authority index, accepted ADRs, frozen direction, or canonical specification, those outrank old prototypes, generated artifacts, and implementation residue.
3. **Distinguish project type.** A product, research program, research instrument, protocol, internal utility, operating system, game, and historical prototype should not be judged by the same criteria.
4. **Do not flatten a system into one component.** A message bus is not the architecture that uses it. A renderer is not the publication system around it. A model provider is not the workflow that governs its output.
5. **Do not confuse old primitives with old products.** Hashes, IRs, provenance, SQLite, append-only records, validators, event logs, and deterministic transforms are implementation mechanisms. Their prior existence does not establish that the system-level problem has already been solved.
6. **Treat lineage explicitly.** Historical prototypes may be ancestors, experiments, or preserved branches without being current authority or migration targets.
7. **Say "not sufficiently oriented" instead of guessing.** If a canonical definition is absent or contradictory, stop and resolve the ambiguity before making portfolio-level claims.
8. **Prior-art audits must operate at the actual job-to-be-done level.** The useful question is: *Could an existing mature tool replace this project end-to-end without materially losing its intended capability?*
9. **Build-versus-buy is economic as well as technical.** Existing commercial software does not automatically make a custom implementation wasteful when price, lock-in, inspectability, integration, modification rights, data ownership, or research control materially change the decision.
10. **Research apparatus is allowed to reuse known components.** A custom instrument need not be novel if ownership of the instrument is necessary to control variables, preserve evidence, modify behavior, or test a research claim.

## The recurring design vocabulary

Across many projects, the following ideas recur:

```text
preserve source
separate evidence from interpretation
keep authority explicit
make uncertainty representable
prefer deterministic validation around probabilistic inference
preserve revisions instead of silently overwriting them
allow abstention / unknown
keep human ratification visible
make derived state rebuildable where practical
keep providers replaceable where they should be
```

This is best understood as an **engineering and epistemic philosophy**, not proof that the projects are instances of one hidden platform.

For example, different projects apply these principles to very different objects:

```text
Hermeneia              understanding
Proofline              public records
ChessHeat              experimental measurements
GCI                    commercial state
Publication Compositor authored content
Performance Manuscript performance semantics
Label Lens TTB         regulatory review evidence
Tekmerion              agreements and performance records
Continuity Node        memory and interpretation
DRAGON SCALE           missions and mission evidence
Modern Movie Crew      creative production decisions
Aerial Inspections     physical-asset evidence and operations
```

Do **not** propose a shared framework merely because two repositories contain words such as `provenance`, `canonical`, `append-only`, `authority`, or `human review`. Shared code becomes justified when repeated mechanics create measurable maintenance burden and stable invariants have actually emerged.

---

# Canonical project map

The entries below are orientation summaries, not substitutes for each repository's own canonical documentation.

## MASI

**Identity:** Modular Artificial Specialized Intelligence is an architectural foundation for organizing heterogeneous, specialized, independently governable and interoperable artificial intelligences. It includes shared coordination, Consult-Before-Execute deliberation, auditability, institutional participation, and distributed governance.

**Do not flatten into:** a multi-agent framework, four prompted personas, a chain-of-thought trick, or "more model calls." MASI is fundamentally a **multi-model architecture**. The MASI Bus is one interoperability and coordination component of the larger architecture.

**Critical distinction:** `MASI != MASI Bus`.

## MASI Bus

**Identity:** the shared communication / interoperability protocol used to structure communication, arbitration, escalation, traceability, and coordination between MASI-compatible modules.

**Do not flatten into:** the whole MASI architecture or proof that the broader ecosystem has already been deployed.

## Hermeneia

**Identity:** an operating environment for the disciplined evolution of understanding. It separates discovery, semantic reconstruction, expression, evaluation, and human stewardship while preserving the lineage of how understanding changed.

**Do not flatten into:** a chatbot, generic document analyzer, or generic provenance engine.

## Pyxis

**Identity:** an evidence-first research system with an architecture-to-code/runtime spine and a bounded browser-research workflow. It preserves human intent, canonical state, generated artifacts, runtime evidence, revisions, and export boundaries while keeping proposed and observed states distinct.

**Do not flatten into:** generic browsing, RAG, or "a compiler" merely because it uses compiler-like primitives.

## TRACE

**Identity:** Transparent, Reproducible Agentic Collaboration & Experimentation — a protocol for preserving intent, review, evidence, execution, interpretation, and durable handoffs in consequential human+agent work.

**Do not flatten into:** an agent framework or orchestration engine.

## Continuity Node

**Identity:** a user-owned longitudinal memory-and-interpretation architecture in which source records remain distinct from governed interpretations, dissent and supersession preserve lineage, and derived state can be rebuilt from canonical records.

**Do not flatten into:** ordinary RAG, vector memory, semantic search, or "chat with notes."

## Telos

**Identity:** an Intent Continuity Substrate for preserving human-declared intent while models, tools, schemas, executors, interfaces, providers, machines, and custodians remain replaceable.

**Do not flatten into:** an AI memory product, agent OS, RAG system, model runner, project manager, or universal assistant. Implementation is intentionally frozen while the foundation is defined.

## Governed Commercial Intelligence

**Identity:** a research and falsification program for commercial decision intelligence in which evidence, business semantics, deterministic measures, statistical/causal claims, explanation, recommendation, human decision, and action authority remain explicitly separated.

**Do not flatten into:** BI-with-chat or an autonomous business agent.

## Proofline

**Identity:** provenance-first public-record intelligence infrastructure that turns fragmented government archives into reproducible evidence, bounded observations, reviewable relationships, and investigative questions while refusing to automate accusation.

**Do not flatten into:** generic search, OSINT summarization, or wrongdoing detection.

## CTRT

**Identity:** Content Tone & Revenue Transparency — a research workbench and measurement architecture for interchangeable content-analysis instruments, preserved evidence, uncertainty, disagreement, abstention, and reproducible evaluation.

**Do not flatten into:** censorship, moderation, one universal "tone score," or AI truth adjudication.

## ChessHeat

**Identity:** an experimental chess research system asking which spatial representations of chess consequence can actually be earned by measurement.

**Do not flatten into:** a chess GUI, an attack map, or a Stockfish replacement. Stockfish is used as a measurement instrument.

## Crownline

**Identity:** an original two-game abstract strategy game combining checker-like movement, Crownline geometry, piece identities, and mathematical scoring, with an evidence-driven rules and AI research environment.

**Do not flatten into:** a chess variant or ChessHeat.

## TunedForest

**Identity:** a concept architecture for collaborative AI ensembles with peer learning, adaptive weighting, model-health monitoring, disagreement preservation, and structured human oversight.

**Do not flatten into:** MASI. TunedForest studies adaptive ensemble learning and model-health behavior; MASI concerns the organization and governance of interoperable specialized intelligences.

## ADCP

**Identity:** Accumulated Distress Care Protocol — an experimental model-agnostic care sidecar studying how conversational posture should change as non-acute distress accumulates across time.

**Do not flatten into:** diagnosis, therapy, a suicide-risk score, or ordinary sentiment analysis.

## Civilizational Sensemaking

**Identity:** pre-implementation research into citizen inquiry, civilizational memory, provenance, reality-tested collective learning, and capture-resistant sensemaking.

**Do not flatten into:** social media, governance, surveillance, a truth engine, or a labor marketplace. Related projects are conceptual ancestors, not modules to merge.

## Hardware Continuity

**Identity:** a device x owner-intent x known-continuity-path resolver for responsible reuse of unsupported hardware.

**Do not flatten into:** a new operating system or replacement for projects such as OpenWrt, postmarketOS, OCLP, or Asahi. Those ecosystems are continuity paths the framework may reason over.

## D.R.A.G.O.N. S.C.A.L.E.

**Identity:** an experimental vehicle-agnostic architecture for translating operator-approved mission intent into bounded missions and turning UAS activity into structured, provenance-aware mission evidence.

**Do not flatten into:** a home-grown flight controller, an autonomous weapons system, or a demonstrated swarm. Planning intelligence and aircraft execution are deliberately separated.

## Lunar Base Resilience

**Identity:** a systems-sandbox game concept for stress-testing fictional lunar settlements through emergent failure cascades, resilience redesign, recovery, and causal postmortems.

**Do not flatten into:** an operational sabotage simulator or a catalog of scripted vulnerabilities.

## Publication Compositor

**Identity:** a preservation-first publication engine that carries immutable author content through canonical structure, verified construction, and multiple verified output formats.

**Do not flatten into:** another PDF renderer or typesetter. Rendering libraries are dependencies underneath the preservation problem.

## Performance Manuscript

**Identity:** a provider-neutral manuscript-to-performance production system covering structure, speaker attribution, uncertainty, casting, performance direction, human ratification, selective regeneration, QC, assembly, and packaging.

**Do not flatten into:** a TTS engine. TTS is a replaceable renderer inside the workflow.

## Modern Movie Crew

**Identity:** a distributed production operating system for generative filmmaking in which external generators produce candidate assets and accountable human production roles govern review, rights, canonical selection, and continuity.

**Do not flatten into:** a media generator itself or generic production-management software.

## Professional Provenance Publisher

**Identity:** a source-controlled publisher that turns one reviewed professional record into a resume, portfolio, links page, printable PDF, and machine-readable source.

**Do not flatten into:** a Linktree clone, career SaaS, or automatic truth-verification service.

## 729 HTML 100

**Identity:** the semantic/static publishing system for the 729 LLC public record, including deterministic intent navigation, multilingual editions, semantic reading tools, and generated narration.

**Do not flatten into:** a generic website or CMS.

## Opportunity Provenance Engine

**Identity:** a source-backed opportunity discovery, qualification, gap-analysis, and application-preparation system that maps frozen subject evidence against verified requirements.

**Do not flatten into:** a grant database or generic opportunity search. Earlier Onshoring work is historical lineage, not the canonical model.

## Aerial Inspections

**Identity:** the current WordPress/React operating-site lineage for Aerial Inspections, including leads, bookings, commerce/flight-credit tooling, weather-aware operational assistance, and scheduled business reporting.

**Do not flatten into:** Aerial Inspections Ops or DRAGON SCALE. It is the business-site operating layer.

## Aerial Inspections Ops

**Identity:** the internal dispatch, inspection, pilot, customer, evidence, and reporting platform supporting repeatable commercial aerial work and evolving toward longitudinal physical-asset continuity.

**Do not flatten into:** a generic drone booking CRM. The operating and evidentiary history around assets is part of the intended value.

## Label Lens TTB

**Identity:** a domestic-wine label prescreen and internal-review prototype where OCR can extract evidence, deterministic rules evaluate bounded checks, and human reviewers retain authority.

**Do not flatten into:** TTB, government approval/rejection, legal advice, or "AI compliance."

## Tekmerion

**Identity:** local-first lease stewardship: agreement -> confirmed obligation -> reminder -> evidence-backed performance record -> clause-linked timeline/export.

**Do not flatten into:** litigation software or an AI lawyer.

## YurrMom.com

**Identity:** a household-knowledge system where reusable routines, lists, recipes, and practical systems are the core unit, with existing shopping and delivery infrastructure connected downstream.

**Do not flatten into:** generic affiliate marketing, a retailer, or a social network.

## SODATERU.shop

**Identity:** an operating slow-fashion / wearable-art storefront where SODATERU owns editorial context, presentation, community experience, and business learning while Printful remains the fulfillment source of truth.

**Do not flatten into:** a custom fulfillment system.

## Big Joke

**Identity:** a private comedy operating system from raw idea capture through joke development, set construction, rehearsal, recording, real performance, and longitudinal learning.

**Do not flatten into:** AI joke generation. The comedian remains the author; AI joke writing is explicitly outside the product boundary.

## MicMap

**Identity:** a live open-mic opportunity-state system intended to answer where a comedian can actually obtain stage time now, with mapped, observed, and confirmed states kept distinct.

**Do not flatten into:** a static open-mic directory or another social network.

## Hecklers & Trolls

**Identity:** an asynchronous comedy-room concept built around premises, riffs, heckles, comebacks, labeled bots/parody identities, and comedy-contextual social interaction.

**Do not flatten into:** Threads with comedy branding, influencer growth, or permission for unbounded harassment.

## MusicReviewRadio

**Identity:** a creator-focused music review and discovery platform combining structured human feedback, radio/live-review workflows, host tools, community signals, content, analytics, and creator-economy mechanics.

**Do not flatten into:** a streaming service or simple review form.

## Capital Voting

**Identity:** a commerce-linked participatory-funding prototype in which qualifying purchases create proposal-linked support records and refunds can invalidate those records.

**Do not flatten into:** electoral voting, securities, ballot measures, or a cryptographically immutable ledger.

## HeadroomCalc

**Identity:** a local iOS income ledger and tax-threshold/headroom scenario planner.

**Do not flatten into:** tax preparation or authoritative tax computation. Its custom implementation can be economically rational even where professional tax-planning software exists.

## Do The Hard Thing

**Identity:** an accountability product centered on declared intention versus self-recorded follow-through over time.

**Do not flatten into:** a psychological or clinical measurement system. Its gauge is a product metaphor. The primary and redesign repositories are parallel product lineage, not independent products.

## Vital Interpreter PAi

**Identity:** a privacy-first clinical-data companion focused on better home measurement quality, review-before-persistence, longitudinal context, and better conversations with licensed clinicians.

**Do not flatten into:** diagnosis, treatment recommendation, medication advice, or automated medicine. The current architecture repository intentionally defines the product before rebuilding the native implementation.

## Safe Encounter

**Identity:** a proposed digital witness + calm co-pilot for high-stakes public encounters, evolved from an earlier multimodal MyChat/Echo Chamber prototype.

**Do not flatten into:** a currently deployed evidentiary or legal-safety system. The proposal is ahead of the executable prototype.

## CacheWarden

**Identity:** a narrow personal developer-cache maintenance utility that responds to disk pressure using explicit cleanup boundaries.

**Do not flatten into:** a flagship research project. It is a small utility and should remain proportionate to the problem.

## Decision Flipper

**Identity:** a playful low-stakes decision interaction in which AI frames two plausible choices and a coin flip supplies a commitment mechanism.

**Do not flatten into:** serious decision science or high-stakes advice.

## PHOVTY

**Identity:** a sentimental recovery placeholder preserving an attempted recovery of the first website Joseph built. It remains as a reminder to eventually reconstruct what was created there.

**Do not flatten into:** a current product, active WordPress platform, or portfolio architecture. The repository's large preserved WordPress tree is recovery material, not a canonical system definition.

---

# Important lineage boundaries

Historical adjacency does not imply replacement or equivalence.

- **ChessHeat Arena -> ChessHeat:** Arena is a preserved freeform tactical branch and is not the current ChessHeat measurement model.
- **Screenshot Claim Analysis -> CTRT:** conceptual precursor only. The earlier project exposed the weakness of generative claim/bias analysis without independent evidence; CTRT later turned the problem into governed measurement.
- **Onshoring Opportunity Matcher -> Opportunity Provenance Engine:** earlier published artifact and conceptual lineage, not OPE's canonical source or migration target.
- **Riff Machine <-> Big Joke:** related comedy tools with different AI boundaries. Riff Machine uses AI to create an external exercise and critique an attempt; Big Joke protects the comedian's authorship of the material itself.
- **PressureTrack -> Vital Interpreter family:** PressureTrack explored blood-pressure OCR/context; later Vital work broadened the problem and ultimately reset around stronger data-quality, privacy, and clinical-governance constraints.
- **Vital web / vision / early iOS prototypes -> Vital iOS Architecture:** historical implementation experiments inform the later architecture-first redesign; they do not outrank it.
- **Aerial Vite Legacy -> Aerial Inspections:** earlier marketing-site generation versus the later WordPress/React operating lineage.
- **MusicReviewRadio archive repositories -> MusicReviewRadio:** archives preserve historical states; the canonical repository is the continuation point.
- **HeadroomCalc legacy/dev repositories -> HeadroomCalc:** development lineage, not multiple independent products.
- **Do The Hard Thing Redesign <-> primary implementation:** parallel design exploration around one product lineage.
- **Grounded-AI historical MASI wording -> canonical MASI publication:** old mentions using "Multi-Agent Specialized Intelligence" do not outrank the later canonical definition of **Modular Artificial Specialized Intelligence** as a multi-model architectural foundation.

Historical experiments such as ClarityBill, DroneSafe, Geopolitical Gambit, Message Distillation, Browser Storage Toast, Commandment Companion, Grounded-AI, Call To The Faithful, the Python 4 proposal, and the As You Wish client-site prototype should remain historical unless a current repository explicitly reactivates their authority.

---

# How to conduct a fair duplication / prior-art audit

Do not ask only whether a technology already exists.

Use this sequence:

```text
1. What exact user, business, or research job is this project trying to accomplish?
2. What mature existing product/system is the closest substitute?
3. Can that substitute replace the project end-to-end?
4. What capability, control, evidence, ownership, integration, or research freedom is lost if we use it?
5. What does the existing option cost over the expected life of the need?
6. Which components are commodity and should simply be reused?
7. Is the custom implementation itself producing research evidence or strategic ownership value?
8. Is the remaining custom work worth its maintenance and compute cost?
```

The key distinction is:

```text
OLD PRIMITIVES
!= OLD ARCHITECTURE
!= OLD PRODUCT
!= OLD PROBLEM
```

A project is genuinely "Decaf-like" only when a mature accessible substitute already accomplishes substantially the same end goal, preserves the control that matters, and makes the custom implementation's opportunity cost unjustified.

---

# Cross-project reasoning standard

When a future session makes a portfolio-level claim, it should be able to answer:

```text
Which canonical project definitions support this comparison?
Which distinctions are being preserved?
Is the similarity functional, architectural, economic, historical, or merely lexical?
Could one project actually replace the other?
Is a shared pattern evidence of duplication, or evidence of a deliberate engineering principle?
```

If those questions cannot be answered from canonical sources, the correct result is **insufficient orientation**, not a confident synthesis.

---

# Why this document exists

Large portfolios create a specific failure mode for humans and AI systems alike: local understanding can be strong while cross-project synthesis silently collapses distinctions.

This file exists to prevent that.

It should be treated as a navigation layer, not as a replacement for repository-level authority. The rule is:

> **Orient here first. Decide from the canonical project source second. Never let the portfolio summary outrank the project itself.**
