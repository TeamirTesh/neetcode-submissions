#!/usr/bin/env python3
"""Generate a dark-themed NeetCode progress SVG card."""

import os

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(REPO_ROOT, "neetcode-card.svg")
CIRCUMFERENCE = 251.33  # 2 * pi * 40

# NeetCode 150 — slug to difficulty (slugs match the GitHub sync folder names)
DIFFICULTY_MAP = {
    # Arrays & Hashing
    "duplicate-integer": "Easy",
    "is-anagram": "Easy",
    "two-integer-sum": "Easy",
    "anagram-groups": "Medium",
    "top-k-elements-in-list": "Medium",
    "string-encode-and-decode": "Medium",
    "products-of-array-discluding-self": "Medium",
    "valid-sudoku": "Medium",
    "longest-consecutive-sequence": "Medium",
    # Two Pointers
    "is-palindrome": "Easy",
    "two-integer-sum-ii": "Medium",
    "three-integer-sum": "Medium",
    "max-water-container": "Medium",
    "trapping-rain-water": "Hard",
    # Sliding Window
    "buy-and-sell-crypto": "Easy",
    "longest-substring-without-duplicates": "Medium",
    "longest-repeating-substring-with-replacement": "Medium",
    "permutation-string": "Medium",
    "minimum-window-with-characters": "Hard",
    "sliding-window-maximum": "Hard",
    # Stack
    "validate-parentheses": "Easy",
    "minimum-stack": "Medium",
    "evaluate-reverse-polish-notation": "Medium",
    "generate-parentheses": "Medium",
    "daily-temperatures": "Medium",
    "car-fleet": "Medium",
    "largest-rectangle-in-histogram": "Hard",
    # Binary Search
    "binary-search": "Easy",
    "search-2d-matrix": "Medium",
    "koko-eating-bananas": "Medium",
    "find-minimum-in-rotated-sorted-array": "Medium",
    "search-in-rotated-sorted-array": "Medium",
    "time-based-key-value-store": "Medium",
    "median-of-two-sorted-arrays": "Hard",
    # Linked List
    "reverse-linked-list": "Easy",
    "merge-two-sorted-linked-lists": "Easy",
    "linked-list-cycle-detection": "Easy",
    "reorder-linked-list": "Medium",
    "remove-node-from-end-of-linked-list": "Medium",
    "find-the-duplicate-number": "Medium",
    "lru-cache": "Medium",
    "merge-k-sorted-linked-lists": "Hard",
    "reverse-nodes-in-k-group": "Hard",
    # Trees
    "invert-a-binary-tree": "Easy",
    "maximum-depth-of-binary-tree": "Easy",
    "diameter-of-binary-tree": "Easy",
    "balanced-binary-tree": "Easy",
    "same-tree": "Easy",
    "subtree-of-a-binary-tree": "Easy",
    "lowest-common-ancestor-in-binary-search-tree": "Medium",
    "binary-tree-level-order-traversal": "Medium",
    "binary-tree-right-side-view": "Medium",
    "count-good-nodes-in-binary-tree": "Medium",
    "validate-binary-search-tree": "Medium",
    "kth-smallest-integer-in-bst": "Medium",
    "construct-binary-tree-from-preorder-and-inorder-traversal": "Medium",
    "binary-tree-maximum-path-sum": "Hard",
    "serialize-and-deserialize-binary-tree": "Hard",
    # Tries
    "implement-trie-prefix-tree": "Medium",
    "design-add-and-search-words-data-structure": "Medium",
    "search-for-word": "Hard",
    # Heap / Priority Queue
    "kth-largest-element-in-a-stream": "Easy",
    "last-stone-weight": "Easy",
    "k-closest-points-to-origin": "Medium",
    "kth-largest-element-in-an-array": "Medium",
    "task-scheduler": "Medium",
    "design-twitter-feed": "Medium",
    "find-median-from-data-stream": "Hard",
    # Backtracking
    "subsets": "Medium",
    "combination-target-sum": "Medium",
    "combination-sum-ii": "Medium",
    "permutations": "Medium",
    "subsets-ii": "Medium",
    "word-search": "Medium",
    "palindrome-partitioning": "Medium",
    "letter-combinations-of-a-phone-number": "Medium",
    "n-queens": "Hard",
    # Graphs
    "number-of-islands": "Medium",
    "clone-graph": "Medium",
    "max-area-of-island": "Medium",
    "pacific-atlantic-water-flow": "Medium",
    "surrounded-regions": "Medium",
    "rotting-fruit": "Medium",
    "walls-and-gates": "Medium",
    "course-schedule": "Medium",
    "course-schedule-ii": "Medium",
    "redundant-connection": "Medium",
    "number-of-connected-components-in-graph": "Medium",
    "graph-valid-tree": "Medium",
    "word-ladder": "Hard",
    # Advanced Graphs
    "reconstruct-flight-path": "Hard",
    "min-cost-to-connect-all-points": "Medium",
    "network-delay-time": "Medium",
    "swim-in-rising-water": "Hard",
    "alien-dictionary": "Hard",
    "cheapest-flights-within-k-stops": "Medium",
    # 1D Dynamic Programming
    "climbing-stairs": "Easy",
    "min-cost-climbing-stairs": "Easy",
    "house-robber": "Medium",
    "house-robber-ii": "Medium",
    "longest-palindromic-substring": "Medium",
    "palindromic-substrings": "Medium",
    "decode-ways": "Medium",
    "coin-change": "Medium",
    "maximum-product-subarray": "Medium",
    "word-break": "Medium",
    "longest-increasing-subsequence": "Medium",
    "partition-equal-subset-sum": "Medium",
    # 2D Dynamic Programming
    "unique-paths": "Medium",
    "longest-common-subsequence": "Medium",
    "best-time-to-buy-and-sell-stock-with-cooldown": "Medium",
    "coin-change-ii": "Medium",
    "target-sum": "Medium",
    "interleaving-string": "Medium",
    "longest-increasing-path-in-matrix": "Hard",
    "distinct-subsequences": "Hard",
    "edit-distance": "Medium",
    "burst-balloons": "Hard",
    "regular-expression-matching": "Hard",
    # Greedy
    "maximum-subarray": "Medium",
    "jump-game": "Medium",
    "jump-game-ii": "Medium",
    "gas-station": "Medium",
    "hand-of-straights": "Medium",
    "merge-triplets-to-form-target": "Medium",
    "partition-labels": "Medium",
    "valid-parenthesis-string": "Medium",
    # Intervals
    "insert-new-interval": "Medium",
    "merge-intervals": "Medium",
    "non-overlapping-intervals": "Medium",
    "meeting-schedule": "Easy",
    "meeting-schedule-ii": "Medium",
    "minimum-interval-to-include-each-query": "Hard",
    # Math & Geometry
    "rotate-matrix": "Medium",
    "spiral-matrix": "Medium",
    "set-matrix-zeroes": "Medium",
    "happy-number": "Easy",
    "plus-one": "Easy",
    "power-function": "Medium",
    "multiply-strings": "Medium",
    "detect-squares": "Medium",
    # Bit Manipulation
    "single-number": "Easy",
    "number-of-1-bits": "Easy",
    "counting-bits": "Easy",
    "reverse-bits": "Easy",
    "missing-number": "Easy",
    "sum-of-two-integers": "Medium",
    "reverse-integer": "Medium",
}

TOTALS = {
    "Easy": sum(1 for d in DIFFICULTY_MAP.values() if d == "Easy"),
    "Medium": sum(1 for d in DIFFICULTY_MAP.values() if d == "Medium"),
    "Hard": sum(1 for d in DIFFICULTY_MAP.values() if d == "Hard"),
}


def get_solved_slugs():
    solved = set()
    for entry in os.scandir(REPO_ROOT):
        if not entry.is_dir() or entry.name.startswith("."):
            continue
        for problem in os.scandir(entry.path):
            if problem.is_dir():
                solved.add(problem.name)
    return solved


def count_by_difficulty(solved_slugs):
    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for slug in solved_slugs:
        diff = DIFFICULTY_MAP.get(slug)
        if diff:
            counts[diff] += 1
        # silently skip slugs not in the map
    return counts


def build_svg(easy, medium, hard):
    total = easy + medium + hard
    total_max = sum(TOTALS.values())

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

  <circle cx="68" cy="118" r="40" fill="none" stroke="#21262d" stroke-width="6"/>
  <circle cx="68" cy="118" r="40" fill="none" stroke="#58a6ff" stroke-width="6"
    stroke-linecap="round"
    stroke-dasharray="{arc:.2f} {CIRCUMFERENCE}"
    transform="rotate(-90 68 118)"/>
  <text x="68" y="114" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="28" font-weight="700" fill="#e6edf3">{total}</text>
  <text x="68" y="130" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10" fill="#6e7681">/ {total_max} solved</text>

  <text x="148" y="72" font-family="Segoe UI,sans-serif" font-size="12" fill="#8b949e">Easy</text>
  <text x="355" y="72" text-anchor="end" font-family="Segoe UI,sans-serif" font-size="12" font-weight="600" fill="#3fb950">{easy}/{TOTALS['Easy']}</text>
  <g transform="translate(148,78)">{bar(easy, TOTALS['Easy'], '#3fb950')}</g>

  <text x="148" y="110" font-family="Segoe UI,sans-serif" font-size="12" fill="#8b949e">Medium</text>
  <text x="355" y="110" text-anchor="end" font-family="Segoe UI,sans-serif" font-size="12" font-weight="600" fill="#e3b341">{medium}/{TOTALS['Medium']}</text>
  <g transform="translate(148,116)">{bar(medium, TOTALS['Medium'], '#e3b341')}</g>

  <text x="148" y="148" font-family="Segoe UI,sans-serif" font-size="12" fill="#8b949e">Hard</text>
  <text x="355" y="148" text-anchor="end" font-family="Segoe UI,sans-serif" font-size="12" font-weight="600" fill="#f85149">{hard}/{TOTALS['Hard']}</text>
  <g transform="translate(148,154)">{bar(hard, TOTALS['Hard'], '#f85149')}</g>

  <text x="20" y="207" font-family="Segoe UI,sans-serif" font-size="10" fill="#484f58">auto-updated by GitHub Actions</text>
</svg>"""


def main():
    solved = get_solved_slugs()
    print(f"Solved problem folders: {len(solved)}")

    counts = count_by_difficulty(solved)
    print(f"Easy: {counts['Easy']}, Medium: {counts['Medium']}, Hard: {counts['Hard']}")
    print(f"Map totals: {TOTALS}")

    unmatched = [s for s in solved if s not in DIFFICULTY_MAP]
    if unmatched:
        print(f"Unmatched slugs (not in map): {unmatched}")

    svg = build_svg(counts["Easy"], counts["Medium"], counts["Hard"])
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Written: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
