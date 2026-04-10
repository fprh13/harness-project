#!/usr/bin/env bash
set -e

CHANGED_FILES="$(git diff --cached --name-only || true)"

# ----------------------------------------
# 백엔드 검증
# ----------------------------------------
if echo "$CHANGED_FILES" | grep -qE '^(backend/)'; then
  ./scripts/verify-backend.sh
fi

# ----------------------------------------
# 프론트엔드 검증
# ----------------------------------------

if echo "$CHANGED_FILES" | grep -qE '^(frontend/)'; then
  ./scripts/verify-frontend.sh
fi

