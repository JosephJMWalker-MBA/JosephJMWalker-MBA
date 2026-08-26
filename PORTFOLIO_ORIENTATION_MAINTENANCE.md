# Portfolio Orientation Maintenance Protocol

> **Purpose:** keep `PORTFOLIO_ORIENTATION.md` accurate as repositories are added, renamed, archived, revived, split, merged, or materially redefined.

This protocol exists because portfolio orientation is a different problem from repository documentation.

A repository README should explain **that project**. The portfolio orientation layer explains **what that project means in relation to the rest of the body of work** without flattening distinct projects into a generic pattern.

The maintenance goal is therefore not to summarize every repository. It is to preserve the minimum semantic information a future human or AI needs to reason across the portfolio without inventing relationships, confusing lineage, or mistaking recurring engineering principles for duplicate products.

This methodology is intentionally written so other GitHub users can adapt it to their own portfolios.

---

## When the orientation should be reviewed

Review `PORTFOLIO_ORIENTATION.md` when any of the following occurs:

- a new repository is added;
- a repository is renamed;
- an active project is archived, parked, revived, or superseded;
- a prototype becomes the canonical implementation of a project;
- a project changes its fundamental thesis or product boundary;
- a new constitutional document, authority index, accepted ADR, or frozen product direction changes what is canonical;
- two repositories acquire an explicit lineage relationship;
- a companion implementation is created for a broader framework or publication;
- a repository that looked redundant is discovered to have a materially different job-to-be-done;
- an external evaluator or AI materially misunderstands a project;
- a portfolio-level audit reveals that the current orientation map encourages a false equivalence.

Ordinary feature work does **not** require a portfolio-orientation edit unless it changes project identity, authority, lineage, or maturity in a way that matters to cross-project reasoning.

---

# Maintenance workflow

## 1. Establish the changed scope

Do not begin by rewriting the whole portfolio from memory.

First determine what changed:

```text
new repository?
renamed repository?
new canonical README?
status change?
new authority document?
new lineage relationship?
project thesis changed?
old prototype promoted or demoted?
```

If one repository changed, begin with that repository and its immediate lineage. A full portfolio review is necessary only when the change materially affects the interpretation of several projects.

---

## 2. Read the repository's canonical source before classifying it

The default reading order is:

```text
README
  ↓
constitution / authority index / frozen direction, if present
  ↓
accepted ADRs or canonical specification
  ↓
current implementation documentation
  ↓
code and generated artifacts
  ↓
historical notes / old prototypes
```

A repository may define a different authority order. If it does, follow that order instead.

Do **not** classify a project from:

- its repository name;
- GitHub topics alone;
- one source file;
- one technical primitive;
- an old conversation;
- a historical README that has been superseded;
- a familiar architecture pattern;
- the fact that another project uses similar words.

If the repository does not contain enough canonical documentation to establish its identity, record:

```text
IDENTITY: NOT SUFFICIENTLY ORIENTED
ACTION: RESOLVE BEFORE PORTFOLIO-LEVEL JUDGMENT
```

Do not fill the gap with pattern matching.

---

## 3. Classify the project type before judging it

Determine what kind of thing the repository is.

Useful classes include:

- commercial product;
- released application;
- internal operating system or business infrastructure;
- research program;
- research apparatus / experimental harness;
- architectural framework;
- protocol or standard proposal;
- companion/reference implementation;
- game;
- creative-production tool;
- small utility;
- historical prototype;
- parallel redesign branch;
- archive;
- sentimental/preservation artifact;
- client work;
- publication or disclosure artifact.

This classification changes the questions that should be asked.

For example, a small utility may be judged primarily by whether an existing tool already solves the practical problem cheaply. A research apparatus may rationally rebuild known mechanisms because experimental control, inspectability, or variable isolation requires ownership. A historical prototype may be valuable as lineage evidence even when a modern product now does the same job better.

---

## 4. Write the canonical identity in one sentence

The identity statement should answer:

> **What is this project actually for?**

It should describe the system-level purpose, not the implementation stack.

Weak:

> A Python project using hashes, JSON, provenance, and an LLM.

Stronger:

> A system for preserving user-owned longitudinal memory while keeping source records separate from governed interpretations across replaceable inference engines.

The identity sentence should remain true if a database, model provider, UI framework, or storage engine changes.

---

## 5. Write the critical `DO NOT FLATTEN INTO` boundary

Every substantial entry should identify the most likely misleading simplification.

Examples of the pattern:

```text
MASI != MASI Bus
Performance Manuscript != TTS engine
Publication Compositor != PDF renderer
ChessHeat != attack map
historical prototype != current architecture
conceptual ancestor != module to merge
shared provenance vocabulary != same product
```

This field is not marketing language. It is a guardrail against the most plausible category error.

A useful test is:

> **If someone read only the repository name and first five technical keywords, what wrong conclusion would they be most likely to reach?**

Write the boundary that prevents that conclusion.

---

## 6. Establish authority and maturity separately

Do not infer maturity from repository size, commit count, polish, or ambitious documentation.

Record the strongest defensible state, such as:

```text
concept only
pre-implementation research
reference implementation
synthetic research foundation
active development
deployed prototype
released product
production system
historical prototype
parked concept
recovery baseline
```

Also preserve authority boundaries such as:

```text
proposal exists; runtime not implemented
schema exists; subsystem not operational
prototype executes; production claim not earned
publication defines architecture; repository implements only a subset
current branch contains post-release work; App Store binary may differ
```

**Implemented** and **proven** are different states.

---

## 7. Map lineage explicitly

For every apparent project family, determine whether the relationship is actually one of these:

```text
ancestor -> successor
prototype -> architecture-first redesign
archive -> canonical continuation
parallel branch <-> primary implementation
framework -> reference implementation
conceptual precursor -> later independent system
marketing site -> operating platform
historical experiment -> preserved lesson
```

Never infer lineage solely because two repositories address the same domain.

For each lineage relationship, state what **does not** transfer automatically.

Examples:

- old implementation behavior does not automatically define current architecture;
- conceptual influence does not imply code inheritance;
- a companion repository does not define the whole framework;
- an archive is not a second active product;
- a successor does not erase the evidentiary value of its predecessor.

---

## 8. Separate recurring principles from shared implementation

When several projects use similar ideas, ask two different questions.

### Question A — shared philosophy?

Examples:

```text
provenance
explicit authority
abstention
human ratification
deterministic validation
append-oriented history
provider independence
```

If the recurrence is conceptual, document it as engineering philosophy.

### Question B — actual duplicated mechanics?

Examples:

```text
same canonical serializer
same hashing envelope
same migration logic
same auth implementation
same bug fixed independently in several repos
same invariant implemented with near-identical code
```

Only the second category is evidence that a shared library or extracted component may reduce maintenance burden.

Do not recommend consolidation merely because the vocabulary looks similar.

---

## 9. Apply the replacement test correctly

When evaluating whether a project is unnecessary because something similar already exists, test **end-to-end substitution**, not component similarity.

Ask:

> **Could the project be deleted, replaced with an existing mature tool, and still accomplish substantially the same intended purpose?**

Then include:

```text
functional equivalence
price / licensing
ownership and modification rights
data control
inspectability
integration burden
reproducibility
vendor lock-in
research-control requirements
maintenance burden
opportunity cost
```

The existence of prior art is not itself a stop signal.

Likewise, failing to find an existing substitute is not proof of novelty. The correct statement is often:

> **No end-to-end substitute has been demonstrated in this review.**

---

## 10. Update the orientation minimally

A portfolio orientation document should be stable.

When one project changes, prefer the smallest correct edit:

- add one project entry;
- revise one identity sentence;
- change one maturity state;
- add one lineage relationship;
- correct one misleading boundary.

Do not rewrite unrelated entries merely to make the prose stylistically uniform.

The orientation layer should preserve semantic continuity over cosmetic consistency.

---

# Required entry template

A new substantial project should normally be representable with the following fields:

```markdown
## Project Name

**Identity:** one sentence describing the durable system-level purpose.

**Project type:** product / research program / apparatus / protocol / utility / historical prototype / etc.

**Do not flatten into:** the most likely misleading simplification.

**Current state:** the strongest defensible maturity description.

**Authority:** README / constitution / specification / publication / other canonical source.

**Lineage:** predecessor, successor, companion implementation, parallel branch, or standalone.
```

Not every field needs to appear verbatim in the public orientation map. The maintainer should nevertheless resolve them before writing the final entry.

---

# Consistency checks before committing

Before changing `PORTFOLIO_ORIENTATION.md`, verify:

1. Does the new summary contradict the canonical README?
2. Did an old prototype accidentally outrank a later canonical source?
3. Did a component become a stand-in for the whole architecture?
4. Did a shared implementation primitive get mistaken for project identity?
5. Did a project get classified as a product when it is actually research apparatus, or vice versa?
6. Is a maturity claim stronger than the repository supports?
7. Is a lineage relationship documented, or merely assumed?
8. Did a repository rename accidentally create a fake second project?
9. Is an archived/preserved repository being described as currently active?
10. If external prior art is mentioned, was replacement tested end-to-end including economics and control?
11. If the evidence is incomplete, does the entry say so rather than guessing?

A clean orientation update should survive all eleven questions.

---

# Repository discovery protocol

When performing a periodic full review:

1. enumerate the current repository inventory;
2. compare it against the projects already represented in `PORTFOLIO_ORIENTATION.md`;
3. identify repositories that are new, renamed, archived, or absent from the map;
4. inspect only the changed or unresolved repositories first;
5. group obvious archives and lineage repositories only after their canonical documentation establishes the relationship;
6. update the map;
7. perform a second pass looking specifically for contradictions between orientation entries and canonical README language.

Repository count is not project count.

A portfolio may contain several repositories for one product and one repository containing several distinct historical experiments. Resolve identity before counting.

---

# AI maintenance instruction

A future AI session asked to update the portfolio orientation should be given this instruction:

```text
Read PORTFOLIO_ORIENTATION.md and PORTFOLIO_ORIENTATION_MAINTENANCE.md first.

Compare the current repository inventory with the existing canonical project map.
For every repository that is new, renamed, materially changed, or missing from the map:

1. read its canonical README;
2. follow any repository-defined authority order;
3. determine project type, durable identity, maturity, and lineage;
4. identify the most likely category error and write a DO NOT FLATTEN INTO boundary;
5. do not infer equivalence from recurring technical primitives or vocabulary;
6. do not promote historical artifacts over current authority;
7. if the project cannot be confidently oriented, mark it NOT SUFFICIENTLY ORIENTED and request resolution rather than guessing;
8. make the smallest necessary changes to the portfolio orientation document;
9. report which canonical sources justified each semantic change.

Do not perform a prior-art or redundancy judgment until orientation is complete.
```

---

# Why this layer exists

Large GitHub portfolios create a retrieval problem.

A human or AI evaluator may see dozens of repositories, repeated technical vocabulary, prototypes beside successors, research instruments beside products, and old implementations beside current architecture. Without an explicit semantic map, a fast analysis can produce confident but structurally wrong conclusions.

The orientation layer establishes a simple hierarchy:

```text
GitHub profile
      ↓
portfolio orientation
      ↓
canonical project identity
      ↓
repository authority documents
      ↓
implementation and historical evidence
```

The maintenance protocol preserves that hierarchy as the portfolio changes.

The governing rule is:

> **Orient before synthesizing. Authority before inference. Similarity is not equivalence.**
