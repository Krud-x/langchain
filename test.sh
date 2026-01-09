#!/usr/bin/env bash

set -euo pipefail

MODE="${1:-}"

case "$MODE" in
  base)
    make test
    ;;
  new)
    uv run --group test pytest tests/test_openai_response_parsing.py
    ;;
  *)
    echo "Usage: $0 {base|new}" >&2
    exit 1
    ;;
esac

