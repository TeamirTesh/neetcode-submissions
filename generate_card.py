#!/usr/bin/env python3
"""Generate a dark-themed NeetCode progress SVG card."""

import os
import requests

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
API_URL = "https://neetcode.io/api/problems"
OUTPUT_FILE = os.path.join(REPO_ROOT, "neetcode-card.svg")

FALLBACK_TOTALS = {"Easy": 40, "Medium": 79, "Hard": 31}
CIRCUMFERENCE = 251.33  # 2 * pi * 40


def get_solved_slugs():
    solved = set()
    for entry in os.scandir(REPO_ROOT):
        if not entry.is_dir() or entry.name.startswith("."):
            continue
        for problem in os.scandir(entry.path):
            if problem.is_dir():
                solved.add(problem.name)
    return solved


def fetch_problem_map():
    """Return (slug -> difficulty, totals-per-difficulty)."""
    try:
        resp = requests.get(API_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"Warning: NeetCode API unavailable ({e}), using fallback totals")
        return {}, dict(FALLBACK_TOTALS)

    slug_map = {}
    totals = {"Easy": 0, "Medium": 0, "Hard": 0}

    for p in data:
        slug = p.get("slug") or p.get("id") or ""
        if not slug:
            raw = p.get("name") or p.get("title") or ""
            slug = raw.lower().replace(" ", "-").replace("'", "").replace(",", "")
        difficulty = (p.get("difficulty") or "").strip().capitalize()
        if difficulty not in totals:
            difficulty = ""
        if difficulty:
            totals[difficulty] += 1
        if slug:
            slug_map[slug] = difficulty

    if not any(totals.values()):
        totals = dict(FALLBACK_TOTALS)

    return slug_map, totals


def count_by_difficulty(solved_slugs, slug_map):
    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for slug in solved_slugs:
        diff = slug_map.get(slug, "")
        if diff in counts:
            counts[diff] += 1
        # silently skip slugs not in the API
    return counts


def build_svg(easy, medium, hard, totals):
    total = easy + medium + hard
    total_max = sum(totals.values()) or 150

    def bar(val, maxv, color):
        if not maxv:
            return '<rect width="200" height="8" rx="4" fill="#21262d"/>'
        w = 200 * val / maxv
        w = max(4, w) if w > 0 else 0
        track = '<rect width="200" height="8" rx="4" fill="#21262d"/>'
        fill = f'<rect width="{w:.1f}" height="8" rx="4" fill="{color}"/>' if w else ""
        return track + fill

    arc = CIRCUMFERENCE * (total / total_max) if total_max else 0

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="380" height="220" viewBox="0 0 380 220">
  <rect width="380" height="220" rx="12" fill="#0d1117"/>
  <rect x="0.5" y="0.5" width="379" height="219" rx="11.5" fill="none" stroke="#30363d" stroke-width="1"/>

  <text x="20" y="32" font-family="Segoe UI,sans-serif" font-size="15" font-weight="600" fill="#e6edf3">NeetCode Progress</text>
  <line x1="20" y1="44" x2="360" y2="44" stroke="#21262d" stroke-width="1"/>

  <!-- Circular total progress -->
  <circle cx="68" cy="118" r="40" fill="none" stroke="#21262d" stroke-width="6"/>
  <circle cx="68" cy="118" r="40" fill="none" stroke="#58a6ff" stroke-width="6"
    stroke-linecap="round"
    stroke-dasharray="{arc:.2f} {CIRCUMFERENCE}"
    transform="rotate(-90 68 118)"/>
  <text x="68" y="114" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="28" font-weight="700" fill="#e6edf3">{total}</text>
  <text x="68" y="130" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10" fill="#6e7681">/ {total_max} solved</text>

  <!-- Easy -->
  <text x="148" y="72" font-family="Segoe UI,sans-serif" font-size="12" fill="#8b949e">Easy</text>
  <text x="355" y="72" text-anchor="end" font-family="Segoe UI,sans-serif" font-size="12" font-weight="600" fill="#3fb950">{easy}/{totals['Easy']}</text>
  <g transform="translate(148,78)">{bar(easy, totals['Easy'], '#3fb950')}</g>

  <!-- Medium -->
  <text x="148" y="110" font-family="Segoe UI,sans-serif" font-size="12" fill="#8b949e">Medium</text>
  <text x="355" y="110" text-anchor="end" font-family="Segoe UI,sans-serif" font-size="12" font-weight="600" fill="#e3b341">{medium}/{totals['Medium']}</text>
  <g transform="translate(148,116)">{bar(medium, totals['Medium'], '#e3b341')}</g>

  <!-- Hard -->
  <text x="148" y="148" font-family="Segoe UI,sans-serif" font-size="12" fill="#8b949e">Hard</text>
  <text x="355" y="148" text-anchor="end" font-family="Segoe UI,sans-serif" font-size="12" font-weight="600" fill="#f85149">{hard}/{totals['Hard']}</text>
  <g transform="translate(148,154)">{bar(hard, totals['Hard'], '#f85149')}</g>

  <text x="20" y="207" font-family="Segoe UI,sans-serif" font-size="10" fill="#484f58">auto-updated by GitHub Actions</text>
</svg>"""


def main():
    solved = get_solved_slugs()
    print(f"Solved problem folders: {len(solved)}")

    slug_map, totals = fetch_problem_map()
    print(f"API problems loaded: {len(slug_map)}, totals per difficulty: {totals}")

    counts = count_by_difficulty(solved, slug_map)
    print(f"By difficulty — Easy: {counts['Easy']}, Medium: {counts['Medium']}, Hard: {counts['Hard']}")

    svg = build_svg(counts["Easy"], counts["Medium"], counts["Hard"], totals)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Written: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
