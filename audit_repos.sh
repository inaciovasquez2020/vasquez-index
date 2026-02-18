#!/usr/bin/env bash

USER="inaciovasquez2020"

echo "audit: starting deep scan for $USER..."
echo "audit: looking for untagged or floating active repositories..."

gh repo list "$USER" --limit 200 --json name,description,isArchived,updatedAt,repositoryTopics \
| jq -r '
.[] |
[
  .name,
  (if .isArchived then "ARCHIVED" else "ACTIVE" end),
  (.repositoryTopics[]?.name // "NO_TOPIC"),
  .updatedAt
] | @tsv' | while read -r name status topic date; do
    if [[ "$status" == "ACTIVE" && "$topic" == "NO_TOPIC" ]]; then
        echo "WARNING: $name is ACTIVE but has NO TOPIC. Check canonicality."
    elif [[ "$status" == "ACTIVE" ]]; then
        echo "OK: $name ($topic)"
    fi
done

echo "audit: scan complete."
