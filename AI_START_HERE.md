# AI Start Here

> **Purpose:** reduce unnecessary orientation variance when a human or AI system enters this GitHub portfolio.

This file is a routing layer, not a project authority.

The portfolio contains many repositories with overlapping engineering vocabulary but different purposes, domains, semantics, validation rules, and units of authority. A capable model can still make a bad first move if it begins from the wrong repository, loads too much adjacent context, or treats lexical similarity as architectural identity.

The routing rule is therefore:

```text
identify task type
    ->
take the narrowest justified route
    ->
read canonical local authority
    ->
expand context only when the task requires it
```

Do not begin by reading the entire portfolio unless the task is genuinely portfolio-wide.

## Route 0 — A repository is explicitly named

If the user names a repository, start there.

1. Read that repository's canonical `README.md`.
2. Follow any repository-local authority order it defines.
3. Read only task-relevant governance, status, protocol, ADR, frozen-direction, or implementation files.
4. Use this portfolio router only if the task also requires cross-project context.

A named repository should not be reinterpreted from the portfolio summary before its own source is read.

## Route 1 — Cross-project comparison, consolidation, duplication, prior art, or portfolio strategy

Read:

1. [PORTFOLIO_ORIENTATION.md](./PORTFOLIO_ORIENTATION.md)
2. the canonical source of every named project
3. task-relevant local authority files

Required constraint:

```text
shared vocabulary
!= shared ontology
!= shared runtime
!= merger target
```

If the canonical sources do not support a confident synthesis, return **insufficient orientation**.

## Route 2 — The user describes a problem but does not name a repository

Use the branch map below to narrow candidates before reading repositories.

### Understanding, interpretation, memory, intent, continuity

Start candidates:

- Hermeneia
- Continuity Node
- Memory Lab
- Telos
- TRACE
- Pyxis

Use when the question concerns preserved understanding, memory, handoff, intent continuity, model/session replacement, or inspectable transformation.

### Evidence, provenance, governed review, public records, professional claims

Start candidates:

- Proofline
- Label Lens TTB
- Professional Provenance Publisher
- Tekmerion
- Aerial Inspections Ops

Use when the question concerns source evidence, chain of custody, review boundaries, public records, regulated review, professional evidence, agreements, or physical-asset evidence.

### Measurement, experiments, falsification, benchmarking, model evaluation

Start candidates:

- CTRT
- ChessHeat
- Crownline
- Artificial Cognitive Pathology

Use when the question concerns preregistration, measurement validity, negative results, controlled comparison, benchmarking, or falsifiable model/system behavior.

### AI architecture, interoperability, governance, multi-system coordination

Start candidates:

- Governed Intelligence Ecology
- MASI
- MASI Bus
- TunedForest
- TRACE

Use when the question concerns multi-model architecture, cross-system responsibilities, coordination, provider independence, governance, or agentic collaboration.

### Applied business, consulting, operations, commerce, enterprise systems

Start candidates:

- Masters Consulting Group
- Governed Commercial Intelligence
- SODATERU.shop
- Aerial Inspections
- Aerial Inspections Ops
- YurrMom.com
- Capital Voting

Use when the question concerns business operations, client work, process redesign, commerce, applied analytics, organizational capability, or commercial decision systems.

### Creative production, publishing, performance, music, live collaboration

Start candidates:

- Modern Movie Crew
- Performance Manuscript
- Publication Compositor
- Big Joke
- MicMap
- Collab
- MusicReviewRadio
- Hecklers & Trolls

Use when the question concerns film, authored content, performance, live events, creative collaboration, music, or production continuity.

### Hardware, missions, field systems, resilience

Start candidates:

- D.R.A.G.O.N. S.C.A.L.E.
- Hardware Continuity
- Lunar Base Resilience
- CacheWarden

Use when the question concerns hardware continuity, bounded missions, field execution, physical infrastructure, resilience, or device lifecycle.

### Public coordination, challenge, consequential decisions

Start candidates:

- Decision Point Initiative
- Decision Point Workshop

Use when the question concerns public challenge, bounded contribution, reproduction, consequential decision environments, or coordination across institutions.

If more than one branch remains plausible, do not choose arbitrarily. Read only the candidate identity entries in [PORTFOLIO_ORIENTATION.md](./PORTFOLIO_ORIENTATION.md), then narrow again.

## Route 3 — "What is current?" or "What should I work on next?"

Do not infer priority from commit counts.

Use:

- [DASHBOARD.md](./DASHBOARD.md) for selected public operational links and telemetry;
- repository-local status / next-work / roadmap files for current execution state;
- the named repository's issue and PR state when relevant.

Commit volume is not project importance, validation strength, or user priority.

## Route 4 — AI onboarding, handoff, cross-provider continuity, or reproducibility

Start with:

- [TRACE](https://github.com/JosephJMWalker-MBA/TRACE)
- TRACE `AI_ONBOARDING.md`
- TRACE `PRINCIPLES.md`
- TRACE `PROTOCOL.md`

TRACE is the protocol-level home for durable human + agent handoff. It is not the ontology for the other repositories.

## Route 5 — No branch fits

Read [PORTFOLIO_ORIENTATION.md](./PORTFOLIO_ORIENTATION.md) and identify the smallest set of candidate repositories.

Do not sweep every repository merely because the initial route is uncertain.

## Context minimization rule

The goal is not to minimize context at all costs. The goal is to eliminate **irrelevant context variance**.

A useful sequence is:

```text
minimum sufficient orientation
    ->
canonical local state
    ->
task-specific evidence
    ->
broader context only if necessary
```

This reduces the chance that unrelated repositories, historical prototypes, or recurring vocabulary bias the model toward a pattern that is not actually relevant to the user's task.

## Machine-readable routing

The companion file [`data/ai-orientation-router.json`](./data/ai-orientation-router.json) carries the same routing intent in a compact machine-readable form.

The JSON file is a navigation aid only. Repository-local canonical sources remain authoritative.

## Variability hypothesis

This router is also an experimental instrument.

Hypothesis:

> If irrelevant orientation choices are constrained before reasoning begins, repeated AI responses should show lower task-irrelevant variance while preserving legitimate model disagreement about the problem itself.

The point is not to force identical prose or identical conclusions.

The point is to reduce nuisance variance caused by:

- different repository discovery order;
- stale conversational context;
- lexical similarity between unrelated projects;
- historical artifacts loaded before current authority;
- provider-specific onboarding behavior;
- excessive context breadth;
- arbitrary first-repository selection.

TRACE contains the preregistration draft for evaluating this hypothesis across models, providers, and model versions.
