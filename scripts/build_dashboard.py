#!/usr/bin/env python3
"""Build restrained GitHub-profile telemetry from public repository data.

The generated charts measure repository activity, not research quality, importance,
or validation strength. Private repositories are intentionally excluded.
"""

from __future__ import annotations

import json
import math
import os
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

OWNER = "JosephJMWalker-MBA"
REPOS = [
    "Hermeneia",
    "Proofline",
    "ChessHeat",
    "label-lens-ttb",
    "pyxis",
    "professional-provenance-publisher",
]
WEEKS = 12
API = "https://api.github.com"
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
DATA = ROOT / "data"


def api_get(path: str):
    token = os.getenv("GITHUB_TOKEN", "").strip()
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "JosephJMWalker-MBA-profile-dashboard",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    url = f"{API}{path}"
    last_error: Exception | None = None
    for attempt in range(5):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                body = response.read().decode("utf-8")
                return json.loads(body) if body else None
        except Exception as exc:  # bounded retries for transient API/network failures
            last_error = exc
            time.sleep(1 + attempt)
    raise RuntimeError(f"GitHub API request failed for {path}: {last_error}")


def week_window(now: datetime) -> tuple[datetime, list[datetime]]:
    current = now.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=now.weekday())
    oldest = current - timedelta(weeks=WEEKS - 1)
    starts = [oldest + timedelta(weeks=i) for i in range(WEEKS)]
    return oldest, starts


def parse_github_time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def collect_repo(repo: str, oldest: datetime) -> dict:
    record = {
        "repo": repo,
        "available": False,
        "weekly": [0] * WEEKS,
        "total": 0,
        "latest_commit": None,
    }

    since = urllib.parse.quote(oldest.isoformat().replace("+00:00", "Z"), safe="")

    try:
        page = 1
        while page <= 50:  # safety bound; far above the expected profile volume
            commits = api_get(f"/repos/{OWNER}/{repo}/commits?since={since}&per_page=100&page={page}")
            if not isinstance(commits, list):
                raise RuntimeError("Unexpected commits response")
            if not commits:
                break

            for item in commits:
                commit = item.get("commit", {})
                stamp = (commit.get("committer") or {}).get("date") or (commit.get("author") or {}).get("date")
                moment = parse_github_time(stamp)
                if moment is None:
                    continue

                if record["latest_commit"] is None:
                    record["latest_commit"] = stamp

                delta_days = (moment.date() - oldest.date()).days
                bucket = delta_days // 7
                if 0 <= bucket < WEEKS:
                    record["weekly"][bucket] += 1

            if len(commits) < 100:
                break
            page += 1

        record["total"] = sum(record["weekly"])
        record["available"] = True
    except Exception as exc:
        record["error"] = str(exc)

    return record


def esc(text: object) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def nice_step(value: float) -> float:
    """Return a readable chart interval close to value."""
    if value <= 0:
        return 1
    exponent = math.floor(math.log10(value))
    magnitude = 10**exponent
    fraction = value / magnitude
    if fraction <= 1:
        nice = 1
    elif fraction <= 2:
        nice = 2
    elif fraction <= 3:
        nice = 3
    elif fraction <= 5:
        nice = 5
    else:
        nice = 10
    return nice * magnitude


def fmt_number(value: float | int) -> str:
    return str(int(value)) if float(value).is_integer() else f"{value:g}"


def render_svg(snapshot: dict, *, dark: bool) -> str:
    if dark:
        bg, panel, text, muted, rule, accent = "#0d1117", "#161b22", "#f0f6fc", "#8b949e", "#30363d", "#58a6ff"
    else:
        bg, panel, text, muted, rule, accent = "#ffffff", "#f6f8fa", "#1f2328", "#656d76", "#d0d7de", "#0969da"

    repos = snapshot["repos"]
    weekly = snapshot["weekly_total"]
    labels = snapshot["week_labels"]
    starts = snapshot["week_starts"]
    total = sum(weekly)
    active = sum(1 for r in repos if r["total"] > 0)
    max_week = max(max(weekly), 1)
    max_repo = max(max((r["total"] for r in repos), default=0), 1)

    step = nice_step(max_week / 3)
    axis_max = max(step, math.ceil(max_week / step) * step)
    tick_count = int(round(axis_max / step))
    ticks = [i * step for i in range(tick_count + 1)]

    width, height = 1120, 560
    chart_x, chart_y, chart_w, chart_h = 82, 166, 622, 226
    allocation_x, allocation_y = 758, 154
    allocation_w = 306

    pieces = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Public lab activity over twelve weeks</title>',
        '<desc id="desc">Weekly commit activity and repository attention allocation across six selected public research repositories. Every weekly bar is labeled with its commit count and the vertical axis shows commits per week. The current week is partial. Commit volume measures activity, not quality or importance.</desc>',
        f'<rect width="{width}" height="{height}" rx="18" fill="{bg}"/>',
        f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="17" fill="none" stroke="{rule}"/>',
        f'<text x="54" y="60" fill="{text}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="14" letter-spacing="2">PUBLIC LAB TELEMETRY · 12 WEEKS</text>',
        f'<text x="54" y="98" fill="{text}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="28" font-weight="650">Research activity</text>',
        f'<text x="54" y="125" fill="{muted}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="14">Commit volume is activity, not evidence of quality, importance, or validation.</text>',
        f'<text x="1066" y="60" text-anchor="end" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="12">UPDATED {esc(snapshot["generated_at"][:10])}</text>',
        f'<text x="{chart_x}" y="145" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="11">COMMITS / WEEK</text>',
        f'<text x="{chart_x + chart_w}" y="145" text-anchor="end" fill="{text}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="11">{total} TOTAL</text>',
    ]

    for tick in ticks:
        y = chart_y + chart_h - (tick / axis_max) * chart_h
        pieces.append(f'<line x1="{chart_x}" y1="{y:.1f}" x2="{chart_x + chart_w}" y2="{y:.1f}" stroke="{rule}" stroke-width="1"/>')
        pieces.append(f'<text x="{chart_x - 10}" y="{y + 3:.1f}" text-anchor="end" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="9">{fmt_number(tick)}</text>')

    gap = 10
    bar_w = (chart_w - gap * (WEEKS - 1)) / WEEKS
    for i, count in enumerate(weekly):
        h = 0 if count == 0 else max(3, (count / axis_max) * chart_h)
        x = chart_x + i * (bar_w + gap)
        y = chart_y + chart_h - h
        opacity = "0.65" if i == WEEKS - 1 else "1"
        suffix = "*" if i == WEEKS - 1 else ""
        value_y = max(chart_y + 10, y - 7)
        tooltip = f'Week of {starts[i]}: {count} commits' + (' (current week partial)' if i == WEEKS - 1 else '')
        pieces.append(f'<g aria-label="{esc(tooltip)}"><title>{esc(tooltip)}</title>')
        pieces.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" rx="3" fill="{accent}" opacity="{opacity}"/>')
        pieces.append(f'<text x="{x + bar_w/2:.1f}" y="{value_y:.1f}" text-anchor="middle" fill="{text}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="9" font-weight="650">{count}{suffix}</text>')
        pieces.append('</g>')
        pieces.append(f'<text x="{x + bar_w/2:.1f}" y="{chart_y + chart_h + 24}" text-anchor="middle" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="9">{esc(labels[i])}</text>')

    pieces.extend([
        f'<line x1="730" y1="142" x2="730" y2="420" stroke="{rule}"/>',
        f'<text x="{allocation_x}" y="{allocation_y - 18}" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="11">ATTENTION ALLOCATION</text>',
    ])

    row_h = 43
    for i, repo in enumerate(repos):
        y = allocation_y + i * row_h
        label = repo["repo"]
        count = repo["total"]
        share = (count / total * 100) if total else 0
        repo_tip = f'{label}: {count} commits, {share:.1f}% of selected 12-week activity'
        pieces.append(f'<g aria-label="{esc(repo_tip)}"><title>{esc(repo_tip)}</title>')
        pieces.append(f'<text x="{allocation_x}" y="{y + 14}" fill="{text}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="13">{esc(label)}</text>')
        pieces.append(f'<text x="{allocation_x + allocation_w}" y="{y + 14}" text-anchor="end" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="11">{count}</text>')
        pieces.append(f'<rect x="{allocation_x}" y="{y + 23}" width="{allocation_w}" height="5" rx="2.5" fill="{panel}"/>')
        fill_w = 0 if count == 0 else max(3, (count / max_repo) * allocation_w)
        pieces.append(f'<rect x="{allocation_x}" y="{y + 23}" width="{fill_w:.1f}" height="5" rx="2.5" fill="{accent}"/>')
        pieces.append('</g>')

    metric_y = 474
    metrics = [
        ("12W COMMITS", str(total)),
        ("ACTIVE SYSTEMS", f"{active}/{len(repos)}"),
        ("DATA SOURCE", "GITHUB"),
    ]
    for i, (label, value) in enumerate(metrics):
        x = 54 + i * 220
        pieces.append(f'<text x="{x}" y="{metric_y}" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="10" letter-spacing="1">{label}</text>')
        pieces.append(f'<text x="{x}" y="{metric_y + 30}" fill="{text}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="22" font-weight="650">{esc(value)}</text>')

    pieces.append(f'<text x="1066" y="522" text-anchor="end" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="10">* CURRENT WEEK PARTIAL · PUBLIC REPOSITORIES ONLY</text>')
    pieces.append('</svg>')
    return "\n".join(pieces) + "\n"


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc)
    oldest, starts = week_window(now)
    repos = [collect_repo(repo, oldest) for repo in REPOS]
    weekly_total = [sum(repo["weekly"][i] for repo in repos) for i in range(WEEKS)]
    snapshot = {
        "generated_at": now.replace(microsecond=0).isoformat(),
        "scope": "selected public repositories only",
        "interpretation": "commit volume measures activity, not quality, importance, or validation strength",
        "weeks": WEEKS,
        "current_week_partial": True,
        "week_starts": [start.date().isoformat() for start in starts],
        "week_labels": [f"{start.month}/{start.day}" for start in starts],
        "weekly_total": weekly_total,
        "repos": repos,
    }

    (DATA / "public-lab-telemetry.json").write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    (ASSETS / "lab-activity-light.svg").write_text(render_svg(snapshot, dark=False), encoding="utf-8")
    (ASSETS / "lab-activity-dark.svg").write_text(render_svg(snapshot, dark=True), encoding="utf-8")


if __name__ == "__main__":
    main()
