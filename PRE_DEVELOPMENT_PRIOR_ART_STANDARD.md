# Pre-Development Prior-Art Standard

> **Principle:** before substantial development begins, make a serious attempt to discover whether the intended problem has already been solved well enough that building a new system would create unnecessary maintenance, compute, or opportunity cost.

This is a default development discipline, not a presumption against building.

The purpose is to distinguish three very different situations:

1. **A mature accessible system already solves the same practical job well enough.** Prefer reuse unless there is a concrete reason not to.
2. **Existing systems solve pieces of the problem but not the end-to-end job, ownership, research, or control requirement.** Reuse the commodity pieces and build the missing layer.
3. **No adequate substitute is demonstrated.** Proceed, while treating that conclusion as a search result rather than proof of novelty.

## Required pre-development question

Before committing substantial implementation effort, ask:

> **Could I delete the thing I am about to build, use an existing mature tool or combination of tools, and still accomplish substantially the same intended purpose?**

The answer must be evaluated at the actual job-to-be-done level, not by matching implementation primitives or category labels.

## Search depth

A superficial search is not enough when the development commitment is substantial.

The depth of prior-art research should scale with expected cost:

```text
small experiment / learning prototype
    -> quick category and product scan

small utility
    -> direct alternatives + operating-system/native capabilities

commercial product or significant internal tool
    -> product landscape + pricing + workflows + integration limits + user evidence

research architecture / claimed system-level contribution
    -> products + open source + academic literature + standards + patents/disclosures where relevant

large multi-month build
    -> explicit written prior-art review before architecture freezes
```

The goal is not exhaustive certainty. The goal is enough search depth that obvious mature substitutes, established research, or commodity components are unlikely to be discovered only after major implementation effort.

## What to compare

Do not stop at feature lists. Compare:

- exact user, business, or research job;
- end-to-end workflow equivalence;
- price and licensing over the expected life of the need;
- ownership and modification rights;
- data control and privacy;
- inspectability and auditability;
- interoperability and integration burden;
- reproducibility;
- vendor lock-in and continuity risk;
- research-control requirements;
- ability to preserve project-specific semantics;
- maintenance burden;
- expected compute burden;
- opportunity cost of building versus adopting.

## Reuse-first does not mean software-first

Before creating a subsystem, check whether the need is already satisfied by:

- an operating-system capability;
- a mature library;
- an open-source project;
- a hosted service or commercial product;
- an existing internal project;
- a standard/protocol;
- a deterministic script or command-line tool;
- a manual process that is already cheaper than automation at the current scale.

Commodity infrastructure should normally be reused unless control of that infrastructure is itself part of the product or experiment.

## Research and build-to-own exception

Prior art does not automatically invalidate custom development.

Building can remain rational when ownership of the system is necessary to:

- control experimental variables;
- preserve or inspect evidence;
- alter mechanisms that commercial tools hide;
- avoid prohibitive recurring pricing;
- preserve data ownership;
- avoid vendor or provider lock-in;
- integrate deeply with a unique workflow;
- create a reusable internal capability;
- test a system-level research question;
- preserve reproducibility or long-horizon continuity.

In those cases, the prior-art review should influence architecture: reuse what is commodity and keep custom work concentrated where ownership actually creates value.

## Evidence standard

Use cautious conclusions.

Preferred language:

```text
A mature substitute appears to cover the intended job end-to-end.

Existing tools cover these components, but no end-to-end substitute was demonstrated because...

No adequate substitute was found in this review.
```

Avoid:

```text
Nobody has done this before.
This is novel because I could not find it.
Existing software means this project is pointless.
```

Failure to find prior art is not proof of novelty. Finding prior art is not proof of equivalence.

## When to repeat the search

Repeat or deepen prior-art research when:

- a concept is moving from prototype to serious implementation;
- development cost increases materially;
- the project changes its job-to-be-done;
- a competitor or adjacent product appears;
- a new platform capability may eliminate custom infrastructure;
- an architecture freeze or major rewrite is being considered;
- commercialization is approaching;
- a previous search was shallow, old, or based mainly on category names.

## Relationship to portfolio orientation

This standard complements `PORTFOLIO_ORIENTATION.md` and `PORTFOLIO_ORIENTATION_MAINTENANCE.md`.

The order matters:

```text
understand the project correctly
        ↓
state its real job-to-be-done
        ↓
search deeply for substitutes and prior art
        ↓
compare end-to-end capability, economics, and control
        ↓
reuse commodity pieces
        ↓
build only the part whose ownership is justified
```

A prior-art search performed before correct orientation can be worse than no search because it may compare the project against the wrong category.

## Default instruction for future development sessions

```text
Before substantial implementation of a new project or major new subsystem, perform a prior-art and substitute search proportional to the expected development cost.

First establish the actual job-to-be-done. Then look for mature products, open-source projects, native platform capabilities, libraries, standards, and relevant research that may already solve the job or major portions of it.

Do not treat shared primitives as functional equivalence. Compare end-to-end capability, economics, ownership, data control, inspectability, integration, reproducibility, lock-in, research needs, maintenance, compute, and opportunity cost.

Prefer reuse for commodity capabilities. Build custom infrastructure only where ownership or modification materially serves the product, business, or research purpose.

If no substitute is found, report that no substitute was demonstrated in the search; do not claim novelty from absence alone.
```

The governing principle is:

> **Search before building. Reuse before reproducing. Own what needs to be owned.**
