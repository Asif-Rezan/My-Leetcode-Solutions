#!/usr/bin/env bash
set -euo pipefail

# ===== CONFIG =====
START="2026-04-07"
END="2026-12-31"
BRANCH="$(git rev-parse --abbrev-ref HEAD)"

# ===== PROBLEMS LIST =====
PROBLEMS=(
  "Two Sum"
  "Longest Substring Without Repeating Characters"
  "Valid Parentheses"
  "Merge Two Sorted Lists"
  "Binary Search"
  "Climbing Stairs"
  "Maximum Subarray"
  "Reverse Linked List"
  "Best Time to Buy and Sell Stock"
  "Valid Anagram"
)

# ===== COMMIT TYPES =====
TYPES=("solve" "refactor" "optimize" "improve")

# ===== NEXT DAY FUNCTION (Git Bash Compatible) =====
next_day() {
  date -d "$1 + 1 day" "+%Y-%m-%d"
}

# ===== CHECK GIT REPO =====
git rev-parse --is-inside-work-tree >/dev/null

current="$START"

while [[ "$current" < "$END" || "$current" == "$END" ]]; do

  # Skip some days randomly (simulate real life)
  if (( RANDOM % 3 == 0 )); then
    current="$(next_day "$current")"
    continue
  fi

  # 1–3 commits per day
  commits=$(( RANDOM % 3 + 1 ))

  for ((i=1; i<=commits; i++)); do

    problem="${PROBLEMS[$RANDOM % ${#PROBLEMS[@]}]}"
    type="${TYPES[$RANDOM % ${#TYPES[@]}]}"

    # Time between 10 AM – 6 PM
    hh=$(printf "%02d" $(( RANDOM % 9 + 10 )))
    mm=$(printf "%02d" $(( RANDOM % 60 )))
    ss=$(printf "%02d" $(( RANDOM % 60 )))

    ts="${current} ${hh}:${mm}:${ss}"

    # Create filename
    filename=$(echo "$problem" | tr ' ' '_' | tr '[:upper:]' '[:lower:]').md

    # Write content (append so it evolves over time)
    {
      echo "# $problem"
      echo "- Practiced on $current"
      echo "- Approach: Iterative / Optimized"
      echo ""
    } >> "$filename"

    git add "$filename"

    GIT_AUTHOR_DATE="$ts" \
    GIT_COMMITTER_DATE="$ts" \
    git commit -m "$type: $problem solution"

  done

  current="$(next_day "$current")"
done

git push origin "$BRANCH"

echo "✅ Realistic LeetCode commits pushed successfully!"