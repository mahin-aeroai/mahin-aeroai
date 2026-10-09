#!/usr/bin/env python3
"""Generate the profile README stats cards as static SVGs.

Runs in GitHub Actions (see .github/workflows/profile-stats.yml) with the repo's own
token, so the cards never depend on a third-party server. Standard library only.

    GITHUB_TOKEN=... python3 scripts/gen_stats.py --user mahin-aeroai --out stats
    python3 scripts/gen_stats.py --demo --out stats     # render with sample data
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.request
from html import escape

# Theme (matches the rest of the profile README).
BG, TITLE, ICON, TEXT, MUTED, GRID = "#050d1a", "#6366f1", "#6366f1", "#7dd3fc", "#64748b", "#13203a"
FONT = "'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif"
HIDDEN_LANGS = {"Jupyter Notebook"}

QUERY = """
query($login: String!, $after: String) {
  user(login: $login) {
    name
    followers { totalCount }
    repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC,
                 first: 100, after: $after) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      restrictedContributionsCount
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def graphql(token: str, variables: dict) -> dict:
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "profile-stats"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.load(r)
    if body.get("errors"):
        raise SystemExit(f"GraphQL error: {body['errors']}")
    return body["data"]["user"]


def fetch(login: str, token: str) -> dict:
    after, stars, langs, first = None, 0, {}, None
    while True:
        user = graphql(token, {"login": login, "after": after})
        first = first or user
        repos = user["repositories"]
        for repo in repos["nodes"]:
            stars += repo["stargazerCount"]
            for e in repo["languages"]["edges"]:
                name = e["node"]["name"]
                size, color = langs.get(name, (0, None))
                langs[name] = (size + e["size"], e["node"]["color"] or color or "#94a3b8")
        if not repos["pageInfo"]["hasNextPage"]:
            break
        after = repos["pageInfo"]["endCursor"]

    cc = first["contributionsCollection"]
    days = [d for w in cc["contributionCalendar"]["weeks"] for d in w["contributionDays"]]
    return {
        "name": first["name"] or login,
        "stars": stars,
        "repos": first["repositories"]["totalCount"],
        "followers": first["followers"]["totalCount"],
        "commits": cc["totalCommitContributions"] + cc["restrictedContributionsCount"],
        "contributions": cc["contributionCalendar"]["totalContributions"],
        "languages": langs,
        "days": [(d["date"], d["contributionCount"]) for d in days],
    }


def demo_data() -> dict:
    today = dt.date(2026, 10, 9)
    days = [((today - dt.timedelta(days=i)).isoformat(), (i * 7 % 11) * (i % 3)) for i in range(370)]
    return {"name": "Mahin Nandipa", "stars": 6, "repos": 21, "followers": 12, "commits": 148,
            "contributions": 211, "days": sorted(days),
            "languages": {"Python": (420000, "#3572A5"), "HTML": (380000, "#e34c26"),
                          "C++": (60000, "#f34b7d"), "JavaScript": (90000, "#f1e05a"),
                          "TypeScript": (40000, "#3178c6"), "CMake": (3000, "#DA3434"),
                          "Shell": (2000, "#89e051"), "CSS": (15000, "#663399"),
                          "Jupyter Notebook": (900000, "#DA5B0B")}}


def card(width: int, height: int, title: str, body: str, label: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(label)}">
<title>{escape(label)}</title>
<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="6" fill="{BG}"/>
<text x="25" y="35" font-family="{FONT}" font-size="18" font-weight="600" fill="{TITLE}">{escape(title)}</text>
{body}
</svg>
"""


def overview_svg(d: dict) -> str:
    year = dt.date.fromisoformat(d["days"][-1][0]).year if d["days"] else ""
    rows = [("Total stars", d["stars"]), ("Public repos", d["repos"]),
            (f"Commits (last 12 months)", d["commits"]),
            ("Contributions (last 12 months)", d["contributions"]), ("Followers", d["followers"])]
    body = []
    for i, (label, value) in enumerate(rows):
        y = 68 + i * 24
        body.append(f'<circle cx="31" cy="{y - 5}" r="4" fill="{ICON}"/>'
                    f'<text x="45" y="{y}" font-family="{FONT}" font-size="14" fill="{TEXT}">{label}:</text>'
                    f'<text x="420" y="{y}" text-anchor="end" font-family="{FONT}" font-size="14" '
                    f'font-weight="700" fill="{TEXT}">{value:,}</text>')
    stamp = f'<text x="442" y="183" text-anchor="end" font-family="{FONT}" font-size="10" fill="{MUTED}">updated {dt.date.today().isoformat()}</text>'
    return card(467, 195, f"{d['name']}'s GitHub Stats", "\n".join(body) + stamp,
                f"GitHub stats {year}")


def languages_svg(d: dict, count: int = 8) -> str:
    items = sorted(((n, s, c) for n, (s, c) in d["languages"].items() if n not in HIDDEN_LANGS),
                   key=lambda x: -x[1])[:count]
    total = sum(s for _, s, _ in items) or 1
    x, bar = 25.0, []
    width = 300.0
    for n, s, c in items:
        w = width * s / total
        bar.append(f'<rect x="{x:.2f}" y="55" width="{max(w, 0.5):.2f}" height="8" fill="{c}"/>')
        x += w
    clip = (f'<clipPath id="bar"><rect x="25" y="55" width="{width}" height="8" rx="4"/></clipPath>'
            f'<g clip-path="url(#bar)">{"".join(bar)}</g>')
    legend = []
    for i, (n, s, c) in enumerate(items):
        col, row = i % 2, i // 2
        lx, ly = 25 + col * 150, 90 + row * 24
        legend.append(f'<circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{c}"/>'
                      f'<text x="{lx + 16}" y="{ly}" font-family="{FONT}" font-size="12" fill="{TEXT}">'
                      f'{escape(n)} {100 * s / total:.1f}%</text>')
    height = 90 + ((len(items) + 1) // 2) * 24
    return card(350, max(height, 195), "Most Used Languages", clip + "\n".join(legend),
                "Most used languages")


def activity_svg(d: dict, n_days: int = 31) -> str:
    days = d["days"][-n_days:]
    W, H, L, R, T, B = 1000, 300, 60, 25, 60, 50
    pw, ph = W - L - R, H - T - B
    peak = max([c for _, c in days] + [1])
    step = 5 if peak > 10 else 2 if peak > 4 else 1
    top = ((peak + step - 1) // step) * step
    pts = [(L + pw * i / max(len(days) - 1, 1), T + ph * (1 - c / top)) for i, (_, c) in enumerate(days)]
    grid, labels = [], []
    for v in range(0, top + 1, step):
        y = T + ph * (1 - v / top)
        grid.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W - R}" y2="{y:.1f}" stroke="{GRID}"/>')
        labels.append(f'<text x="{L - 10}" y="{y + 4:.1f}" text-anchor="end" font-family="{FONT}" '
                      f'font-size="11" fill="{MUTED}">{v}</text>')
    for i, (date, _) in enumerate(days):
        if i % 5 == 0 or i == len(days) - 1:
            x = pts[i][0]
            labels.append(f'<text x="{x:.1f}" y="{H - B + 20}" text-anchor="middle" font-family="{FONT}" '
                          f'font-size="11" fill="{MUTED}">{dt.date.fromisoformat(date).strftime("%d %b")}</text>')
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = f"{L},{T + ph} " + line + f" {W - R},{T + ph}"
    dots = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="#a5b4fc"/>' for x, y in pts)
    body = ("".join(grid) + f'<polygon points="{area}" fill="#071020" opacity="0.9"/>'
            f'<polyline points="{line}" fill="none" stroke="{TITLE}" stroke-width="2" stroke-linejoin="round"/>'
            + dots + "".join(labels))
    return card(W, H, f"{d['name']}'s Contribution Graph (last {n_days} days)", body,
                "Contribution activity graph")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default="mahin-aeroai")
    ap.add_argument("--out", default="stats")
    ap.add_argument("--demo", action="store_true", help="render sample data without the API")
    args = ap.parse_args()

    if args.demo:
        data = demo_data()
    else:
        token = os.environ.get("STATS_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if not token:
            sys.exit("set GITHUB_TOKEN (or STATS_TOKEN) to query the GitHub API")
        data = fetch(args.user, token)

    os.makedirs(args.out, exist_ok=True)
    for name, svg in (("overview.svg", overview_svg(data)), ("languages.svg", languages_svg(data)),
                      ("activity.svg", activity_svg(data))):
        with open(os.path.join(args.out, name), "w", encoding="utf-8") as f:
            f.write(svg)
    print(f"wrote {args.out}/overview.svg, languages.svg, activity.svg "
          f"(stars={data['stars']}, repos={data['repos']}, commits={data['commits']})")


if __name__ == "__main__":
    main()
