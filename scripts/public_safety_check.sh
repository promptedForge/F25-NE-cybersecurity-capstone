#!/usr/bin/env bash
set -euo pipefail
echo "Listing files in public bundle:"
find . -type f -not -path "./.git/*" -print | sed 's|^\./||'

echo
echo "Scanning for sensitive patterns (NDA/secret/token/env/keys)…"
grep -RIn -E 'NDA|secret|SECRET|token|TOKEN' || true
find . -type f \( -name '*.pem' -o -name '*.key' -o -name '.env' -o -name '*.env' \) -print || true
