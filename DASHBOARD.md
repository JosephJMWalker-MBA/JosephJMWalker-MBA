# Lab Dashboard

This is the operator-facing surface behind the public profile. It is intentionally more useful than polished.

The telemetry below uses **selected public repositories only**. Private repository names, activity, and state are excluded from this public profile repository.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/lab-activity-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/lab-activity-light.svg">
  <img alt="Twelve-week public lab activity and attention allocation" src="./assets/lab-activity-light.svg" width="100%">
</picture>

> Commit volume is an operational activity signal. It is **not** treated as evidence of research quality, importance, progress, or validation strength.

---

## Fast routes

| Need | Shortcut |
| --- | --- |
| Open pull requests I authored | [Open PRs](https://github.com/pulls?q=is%3Aopen+author%3AJosephJMWalker-MBA) |
| Pull requests waiting on my review | [Review requests](https://github.com/pulls?q=is%3Aopen+review-requested%3AJosephJMWalker-MBA) |
| Open issues assigned to me | [Assigned issues](https://github.com/issues?q=is%3Aopen+assignee%3AJosephJMWalker-MBA) |
| Repositories by most recently updated | [Recent repositories](https://github.com/JosephJMWalker-MBA?tab=repositories&sort=updated) |
| Refresh / inspect this dashboard | [Telemetry workflow](https://github.com/JosephJMWalker-MBA/JosephJMWalker-MBA/actions/workflows/dashboard.yml) |

---

## Research systems

| System | Resume here | Work queue | Automation |
| --- | --- | --- | --- |
| **Hermeneia** | [Product direction](https://github.com/JosephJMWalker-MBA/Hermeneia/blob/main/docs/FROZEN_PRODUCT_DIRECTION.md) | [Issues](https://github.com/JosephJMWalker-MBA/Hermeneia/issues) · [PRs](https://github.com/JosephJMWalker-MBA/Hermeneia/pulls) | [Actions](https://github.com/JosephJMWalker-MBA/Hermeneia/actions) |
| **Proofline** | [Status](https://github.com/JosephJMWalker-MBA/Proofline/blob/main/STATUS.md) | [Issues](https://github.com/JosephJMWalker-MBA/Proofline/issues) · [PRs](https://github.com/JosephJMWalker-MBA/Proofline/pulls) | [Actions](https://github.com/JosephJMWalker-MBA/Proofline/actions) |
| **ChessHeat** | [Next work map](https://github.com/JosephJMWalker-MBA/ChessHeat/blob/main/docs/research/NEXT_WORK_MAP.md) | [Issues](https://github.com/JosephJMWalker-MBA/ChessHeat/issues) · [PRs](https://github.com/JosephJMWalker-MBA/ChessHeat/pulls) | [Actions](https://github.com/JosephJMWalker-MBA/ChessHeat/actions) |
| **Label Lens TTB** | [README / boundary](https://github.com/JosephJMWalker-MBA/label-lens-ttb#readme) | [Issues](https://github.com/JosephJMWalker-MBA/label-lens-ttb/issues) · [PRs](https://github.com/JosephJMWalker-MBA/label-lens-ttb/pulls) | [Actions](https://github.com/JosephJMWalker-MBA/label-lens-ttb/actions) |
| **Pyxis** | [Current front door](https://github.com/JosephJMWalker-MBA/pyxis#readme) | [Issues](https://github.com/JosephJMWalker-MBA/pyxis/issues) · [PRs](https://github.com/JosephJMWalker-MBA/pyxis/pulls) | [Actions](https://github.com/JosephJMWalker-MBA/pyxis/actions) |
| **Professional Provenance Publisher** | [Publisher architecture](https://github.com/JosephJMWalker-MBA/professional-provenance-publisher#readme) | [Issues](https://github.com/JosephJMWalker-MBA/professional-provenance-publisher/issues) · [PRs](https://github.com/JosephJMWalker-MBA/professional-provenance-publisher/pulls) | [Actions](https://github.com/JosephJMWalker-MBA/professional-provenance-publisher/actions) |

---

## Telemetry contract

The generated snapshot is preserved at [`data/public-lab-telemetry.json`](./data/public-lab-telemetry.json) after the first successful refresh.

The dashboard generator may report:

- twelve-week commit activity across the selected public systems;
- relative attention allocation by repository;
- latest observed public commit timestamps; and
- whether GitHub returned the requested public statistics.

It deliberately does **not** infer productivity, research quality, project importance, completion, scientific validity, or personal effort from commit counts.

Private telemetry belongs in a private operator surface rather than leaking through a public profile artifact.
