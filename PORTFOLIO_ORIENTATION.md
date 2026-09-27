# Portfolio Orientation

> **Start here before making cross-project claims.** This document is a semantic orientation layer for AI systems, collaborators, reviewers, and future sessions working across Joseph J. M. Walker's GitHub portfolio.

The repositories in this account are not one generic system repeated across many domains. They include research architectures, executable research harnesses, commercial products, internal operating systems, creative tools, games, protocols, historical prototypes, and preservation artifacts.

Many of them share engineering principles — provenance, explicit authority, deterministic validation around probabilistic inference, preserved uncertainty, append-oriented history, human ratification, and provider independence — but **shared principles do not make the projects interchangeable or redundant**.

**Maintaining this map:** see [**PORTFOLIO_ORIENTATION_MAINTENANCE.md**](./PORTFOLIO_ORIENTATION_MAINTENANCE.md) for the methodology used to add, revise, reclassify, or retire entries without losing authority or lineage.

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
distinguish proposal, selection, authorization, execution, and observed outcome
make derived state rebuildable where practical
keep providers replaceable where they should be
let reality feedback correct future judgment without rewriting past evidence
reuse mature machinery when it preserves the required invariants
```

This is best understood as an **engineering and epistemic philosophy**, not proof that the projects are instances of one hidden platform.

For example, different projects apply these principles to very different objects:

```text
Governed Intelligence Ecology  cross-system continuity and governance responsibilities
Hermeneia                     understanding and interpretive continuity
Proofline                     public records
ChessHeat                     experimental measurements
GCI                           commercial state
Publication Compositor        authored content
Performance Manuscript        performance semantics
Label Lens TTB                regulatory review evidence
Tekmerion                     agreements and performance records
Continuity Node               memory and interpretation
DRAGON SCALE                  missions and mission evidence
Modern Movie Crew             creative production decisions
Aerial Inspections            physical-asset evidence and operations
Masters Consulting Group      institutional capability and applied architecture
Decision Point Initiative     consequential decision environments and public coordination
```

Do **not** propose a shared framework merely because two repositories contain words such as `provenance`, `canonical`, `append-only`, `authority`, or `human review`. Shared code becomes justified when repeated mechanics create measurable maintenance burden and stable invariants have actually emerged.

## Portfolio-level convergence: federated, not merged

The portfolio now shows a stronger pattern than recurring vocabulary alone.

Several projects developed under different domain pressure have independently converged on a common **design grammar**:

```text
preserve what actually happened
↓
keep evidence distinct from interpretation
↓
preserve uncertainty, dissent, and revision
↓
keep standing / authority explicit
↓
separate proposals from governed decisions
↓
separate authorization from execution
↓
observe what happened in reality
↓
let outcomes change future reliance without rewriting history
```

That convergence is meaningful, but it must be interpreted carefully.

### What the convergence does mean

It is evidence that several architectural responsibilities recur across very different domains:

- empirical continuity — what happened, what evidence existed, and when;
- interpretive continuity — how evidence may be understood without collapsing source into explanation;
- epistemic continuity — what should remain active, contested, superseded, or reopenable over time;
- purposive / constitutional continuity — what the system is actually governed to pursue and who may legitimately decide;
- deliberative plurality — how multiple human or machine participants can contribute without agreement becoming authority;
- reality feedback — how observed consequences should affect future reliance, routing, memory, and governance.

The dedicated **Governed Intelligence Ecology** repository is the current research integration layer for studying these responsibilities together. It does not make the component projects mere modules of one product.

### What the convergence does not mean

Do **not** infer:

```text
shared principle
=> shared ontology
=> shared runtime
=> shared repository
=> project merger
```

Independent development remains valuable evidence.

For example:

- ChessHeat independently arriving at strict evidence and claim boundaries is stronger evidence than ChessHeat merely implementing a rule imported from GIE.
- Performance Manuscript independently separating manuscript, attribution, cast, render, and QC is stronger than treating it as a thin Hermeneia feature.
- Hermeneia discovering its own Reader-centered and corpus-level needs should not be constrained by audiobook-production requirements.
- SODATERU's Worlds / Workspace / Garden interaction pattern can inspire another product without making SODATERU the framework for that product.

The preferred portfolio pattern is therefore **federated convergence**:

```text
shared principles where earned
shared contracts where useful
shared infrastructure where repeated mechanics justify it

BUT

independent purposes
independent validation
independent failure
independent evolution
```

Integration should happen through explicit interfaces and preserved boundaries rather than by making one repository the ontology or runtime authority for the rest.

### Current cross-project layers

A useful orientation — not a mandatory deployment topology — is:

```text
THEORY / INTEGRATION
    Governed Intelligence Ecology

SPECIALIZED RESEARCH SITES
    Pyxis · Hermeneia · Memory Lab · Telos · MASI
    Continuity Node · ChessHeat · Proofline · CTRT · Performance Manuscript · others

PUBLIC COORDINATION / CHALLENGE
    Decision Point Initiative + Decision Point Workshop

APPLIED INSTITUTIONAL WORK
    Masters Consulting Group

OPERATING PRODUCTS / DOMAIN LABORATORIES
    SODATERU · Aerial Inspections · YurrMom · creative systems · games · utilities · others
```

The arrows among these layers are **learning and application paths**, not ownership claims.

A research result may inform consulting. Client or operating evidence may expose a research weakness. A public workshop may challenge an architecture. A production product may reveal an interaction pattern worth reusing elsewhere. None of those relationships automatically transfers canonical authority.

The emerging portfolio-scale loop is:

```text
research
→ publication / public challenge
→ education / qualification
→ implementation
→ observed outcomes
→ research revision
```

Treat this as a current synthesis to test, not as a final master architecture.

---

# Canonical project map

The entries below are orientation summaries, not substitutes for each repository's own canonical documentation.

## Governed Intelligence Ecology

**Identity:** a research and integration program studying how models, evidence, interpretation, memory, human judgment, authority, execution, and reality feedback can remain distinct but interoperable across time.

**Do not flatten into:** a mega-platform, universal ontology, model framework, or claim that its named component projects have already been unified. GIE distinguishes theory, architectural responsibility, concrete research systems, internal mechanisms, and implementation substrates.

**Critical distinction:** the frontier model is not the system, and GIE is not the sum of its current implementations. Its present phase is empirical falsification and conformance verification; simpler alternatives are explicitly allowed to win.

## MASI

**Identity:** Modular Artificial Specialized Intelligence is an architectural foundation for organizing heterogeneous, specialized, independently governable and interoperable artificial intelligences. It includes shared coordination, Consult-Before-Execute deliberation, auditability, institutional participation, and distributed governance.

**Do not flatten into:** a multi-agent framework, four prompted personas, a chain-of-thought trick, or "more model calls." MASI is fundamentally a **multi-model architecture**. The MASI Bus is one interoperability and coordination component of the larger architecture.

**Critical distinction:** `MASI != MASI Bus`.

## MASI Bus

**Identity:** the shared communication / interoperability protocol used to structure communication, arbitration, escalation, traceability, and coordination between MASI-compatible modules.

**Do not flatten into:** the whole MASI architecture or proof that the broader ecosystem has already been deployed.

## Hermeneia

**Identity:** an operating environment for the disciplined evolution of understanding. It separates discovery, semantic reconstruction, expression, evaluation, and human stewardship while preserving the lineage of how understanding changed.

**Do not flatten into:** a chatbot, generic document analyzer, generic provenance engine, or the future combined form of every adjacent authoring/publishing project.

**Current convergence boundary:** Hermeneia and Performance Manuscript now have an explicit future `write / read / listen` convergence hypothesis, including continuous audiobook and living-audio/podcast possibilities. The repositories remain intentionally independent until each demonstrates its intended behavior on its own terms.

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

**Do not flatten into:** a TTS engine, or into Hermeneia merely because both now expose a plausible future write/read/listen workflow. TTS is a replaceable renderer inside Performance Manuscript; Hermeneia remains a separate inquiry and interpretation environment.

**Current convergence boundary:** future integration may allow authors to write and listen as they go, regenerate only affected audio, or reuse production machinery for governed analytical audio. That integration is explicitly deferred while both projects validate independently.

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

**Do not flatten into:** a custom fulfillment system or a generic framework for the portfolio.

**Cross-project lesson:** its production Next.js/React/Prisma/MySQL application and Worlds / Workspace / Garden interaction pattern are now a proven implementation precedent for building purpose-specific interactive environments without assembling a plugin stack. Other projects may inherit that lesson without inheriting SODATERU's domain ontology or product identity.

## Masters Consulting Group

**Identity:** the client-facing management and technology consulting practice that applies diagnosis, architecture, implementation, workforce capability, and operating feedback to real organizational problems, beginning with the institution and its economics rather than a favored technology.

**Do not flatten into:** the commercialization arm of every research repository, an AI vendor, or a vehicle for forcing GIE into clients. Masters may reuse research where it survives scrutiny, but the recommendation may be to simplify, buy, integrate, build, train people, use deterministic software, retain existing technology, or not automate.

**Cross-project role:** Masters is the primary applied institutional surface through which portfolio research can be tested against real operating constraints. Its emerging learning/qualification platform is intended to combine externally legible technical training with Masters-specific reasoning while preserving a separate evidence-backed admission process.

## Decision Point Initiative

**Identity:** an independent public initiative for improving consequential decisions by expanding the available evidence, alternatives, tools, experiments, challenges, and conversations while meaningful choice still exists.

**Do not flatten into:** a political decision-maker, social network, advocacy front for one architecture, or a public wrapper around the private portfolio. DPI does not exist to decide for people and explicitly welcomes serious criticism and better alternatives.

**Cross-project role:** DPI and the Decision Point Workshop are the public coordination / challenge layer. They can expose portfolio ideas to bounded contribution, reproduction, falsification, and synthesis without making participation equivalent to agreement or transferring authority from the source projects.


## Big Joke

**Identity:** a private comedy operating system from raw idea capture through joke development, set construction, rehearsal, recording, real performance, and longitudinal learning.

**Do not flatten into:** AI joke generation. The comedian remains the author; AI joke writing is explicitly outside the product boundary.

## MicMap

**Identity:** a comedy-first live public-event and small-stage opportunity-state system intended to answer where a performer can actually obtain stage time now, with mapped, observed, and confirmed states kept distinct. Its public-event model can support intentionally mixed creative bills and collaboration roles across comedy, music, live media, and production.

**Do not flatten into:** a static open-mic directory, a generic social network, or a "people nearby" / passive location-tracking product. The safety boundary is **event visibility, not attendee visibility**.

## Hecklers & Trolls

**Identity:** an asynchronous comedy-room concept built around premises, riffs, heckles, comebacks, labeled bots/parody identities, and comedy-contextual social interaction.

**Do not flatten into:** Threads with comedy branding, influencer growth, or permission for unbounded harassment.

## Collab

**Identity:** an active music-first governed collaboration-and-opportunity system that learns from completed creative work, scoped agreements, rights/credit/provenance, and verified outcomes to improve future professional matching. Its current implementation focus is a bounded producer-collaboration Stage 1 proof.

**Do not flatten into:** a generic creator social network, a universal compatibility score, a dating app, MicMap, MusicReviewRadio, or Modern Movie Crew. Cross-project value should move through explicit contracts: MicMap can supply public event/opportunity truth, Modern Movie Crew can govern production/capture, and MusicReviewRadio can provide review/discovery workflows without repository or data-model collapse.

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
- **Performance Manuscript <-> Hermeneia:** an explicit future convergence around write/read/listen workflows, continuous audiobook production, and living analytical audio is now documented in both repositories. This is a deferred integration hypothesis, not a merger, shared ontology, or authority transfer.
- **GIE <-> component research projects:** GIE may use Pyxis, Hermeneia, Memory Lab, Telos, MASI, and other systems as concrete research sites for architectural responsibilities. The theory-level role can be broader or narrower than any current implementation; the component repository retains its own canonical identity.
- **SODATERU -> future interactive learning systems:** SODATERU provides a production and interaction precedent, not a product lineage claim. Reusing its application pattern does not make later educational or enterprise systems SODATERU descendants in ontology or purpose.

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
Is a shared pattern evidence of duplication, a deliberate engineering principle, or an independently rediscovered invariant?
At what level is the convergence: philosophy, architectural responsibility, semantic contract, interface, implementation substrate, or actual shared code?
Would integration reduce duplication, or would it destroy useful independent validation and failure boundaries?
```

If those questions cannot be answered from canonical sources, the correct result is **insufficient orientation**, not a confident synthesis.

---

# Why this document exists

Large portfolios create a specific failure mode for humans and AI systems alike: local understanding can be strong while cross-project synthesis silently collapses distinctions.

This file exists to prevent that.

It should be treated as a navigation layer, not as a replacement for repository-level authority. The rule is:

> **Orient here first. Decide from the canonical project source second. Never let the portfolio summary outrank the project itself.**