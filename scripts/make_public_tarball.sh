#!/usr/bin/env bash
set -euo pipefail
OUT="F25-NE-cybersecurity-capstone_public.tar.gz"
tar -czf "$OUT"   README.md LICENSE EvaluationLabels.json   docs   .github   scripts
echo "Wrote $OUT"
