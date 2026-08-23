#!/usr/bin/env python3
"""Build restrained GitHub-profile telemetry from public repository data.

The generated charts measure repository activity, not research quality, importance,
or validation strength. Private repositories are intentionally excluded.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
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


def api_get(path: str, *, accept_202: bool = False):
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
    for attempt in range(6):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                status = response.status
                body = response.read().decode("utf-8")
                if status == 202 and not accept_202:
                    time.sleep(2 + attempt * 2)
                    continue
                return json.loads(body) if body else None
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code == 202:
                time.sleep(2 + attempt * 2)
                continue
            raise
        except Exception as exc:  # network/transient errors get bounded retries
            last_error = exc
            time.sleep(1 + attempt)
    raise RuntimeError(f"GitHub API did not become ready for {path}: {last_error}")


def collect_repo(repo: str) -> dict:
    record = {
        "repo": repo,
        "available": False,
        "weekly": [0] * WEEKS,
        "total": 0,
        "latest_commit": None,
    }

    try:
        activity = api_get(f"/repos/{OWNER}/{repo}/stats/commit_activity")
        if isinstance(activity, list) and activity:
            tail = activity[-WEEKS:]
            weekly = [int(item.get("total", 0)) for item in tail]
            if len(weekly) < WEEKS:
                weekly = ([0] * (WEEKS - len(weekly))) + weekly
            record["weekly"] = weekly
            record["total"] = sum(weekly)
            record["available"] = True

        commits = api_get(f"/repos/{OWNER}/{repo}/commits?per_page=1")
        if isinstance(commits, list) and commits:
            commit = commits[0].get("commit", {})
            stamp = (commit.get("committer") or {}).get("date") or (commit.get("author") or {}).get("date")
            record["latest_commit"] = stamp
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


def render_svg(snapshot: dict, *, dark: bool) -> str:
    if dark:
        bg, panel, text, muted, rule, accent = "#0d1117", "#161b22", "#f0f6fc", "#8b949e", "#30363d", "#58a6ff"
    else:
        bg, panel, text, muted, rule, accent = "#ffffff", "#f6f8fa", "#1f2328", "#656d76", "#d0d7de", "#0969da"

    repos = snapshot["repos"]
    weekly = snapshot["weekly_total"]
    total = sum(weekly)
    active = sum(1 for r in repos if r["total"] > 0)
    max_week = max(max(weekly), 1)
    max_repo = max(max((r["total"] for r in repos), default=0), 1)

    width, height = 1120, 560
    chart_x, chart_y, chart_w, chart_h = 54, 154, 650, 238
    allocation_x, allocation_y = 758, 154
    allocation_w = 306

    pieces = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Public lab activity over twelve weeks</title>',
        '<desc id="desc">Weekly commit activity and repository attention allocation across six selected public research repositories. Commit volume measures activity, not quality or importance.</desc>',
        f'<rect width="{width}" height="{height}" rx="18" fill="{bg}"/>',
        f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="17" fill="none" stroke="{rule}"/>',
        f'<text x="54" y="60" fill="{text}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="14" letter-spacing="2">PUBLIC LAB TELEMETRY · 12 WEEKS</text>',
        f'<text x="54" y="98" fill="{text}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="28" font-weight="650">Research activity</text>',
        f'<text x="54" y="125" fill="{muted}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="14">Commit volume is activity, not evidence of quality, importance, or validation.</text>',
        f'<text x="1066" y="60" text-anchor="end" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="12">UPDATED {esc(snapshot["generated_at"][:10])}</text>',
    ]

    # Weekly activity grid.
    for i in range(4):
        y = chart_y + (chart_h / 3) * i
        pieces.append(f'<line x1="{chart_x}" y1="{y:.1f}" x2="{chart_x + chart_w}" y2="{y:.1f}" stroke="{rule}" stroke-width="1"/>')

    gap = 12
    bar_w = (chart_w - gap * (WEEKS - 1)) / WEEKS
    for i, count in enumerate(weekly):
        h = 0 if count == 0 else max(3, (count / max_week) * (chart_h - 26))
        x = chart_x + i * (bar_w + gap)
        y = chart_y + chart_h - h
        pieces.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" rx="3" fill="{accent}"/>')
        pieces.append(f'<text x="{x + bar_w/2:.1f}" y="{chart_y + chart_h + 24}" text-anchor="middle" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="10">W{i+1:02d}</text>')

    pieces.extend([
        f'<text x="{chart_x}" y="{chart_y - 18}" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="11">WEEKLY COMMITS</text>',
        f'<text x="{chart_x + chart_w}" y="{chart_y - 18}" text-anchor="end" fill="{text}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="11">{total} TOTAL</text>',
        f'<line x1="730" y1="142" x2="730" y2="420" stroke="{rule}"/>',
        f'<text x="{allocation_x}" y="{allocation_y - 18}" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="11">ATTENTION ALLOCATION</text>',
    ])

    row_h = 43
    for i, repo in enumerate(repos):
        y = allocation_y + i * row_h
        label = repo["repo"]
        count = repo["total"]
        pieces.append(f'<text x="{allocation_x}" y="{y + 14}" fill="{text}" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="13">{esc(label)}</text>')
        pieces.append(f'<text x="{allocation_x + allocation_w}" y="{y + 14}" text-anchor="end" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="11">{count}</text>')
        pieces.append(f'<rect x="{allocation_x}" y="{y + 23}" width="{allocation_w}" height="5" rx="2.5" fill="{panel}"/>')
        fill_w = 0 if count == 0 else max(3, (count / max_repo) * allocation_w)
        pieces.append(f'<rect x="{allocation_x}" y="{y + 23}" width="{fill_w:.1f}" height="5" rx="2.5" fill="{accent}"/>')

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

    pieces.append(f'<text x="1066" y="522" text-anchor="end" fill="{muted}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" font-size="10">PUBLIC REPOSITORIES ONLY</text>')
    pieces.append('</svg>')
    return "\n".join(pieces) + "\n"


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)

    repos = [collect_repo(repo) for repo in REPOS]
    weekly_total = [sum(repo["weekly"][i] for repo in repos) for i in range(WEEKS)]
    snapshot = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "scope": "selected public repositories only",
        "interpretation": "commit volume measures activity, not quality, importance, or validation strength",
        "weeks": WEEKS,
        "weekly_total": weekly_total,
        "repos": repos,
    }

    (DATA / "public-lab-telemetry.json").write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    (ASSETS / "lab-activity-light.svg").write_text(render_svg(snapshot, dark=False), encoding="utf-8")
    (ASSETS / "lab-activity-dark.svg").write_text(render_svg(snapshot, dark=True), encoding="utf-8")


if __name__ == "__main__":
    main()
