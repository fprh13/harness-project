#!/usr/bin/env bash
set -e

echo "[verify-backend] spotlessCheck"
./gradlew spotlessCheck || { echo "[fail] spotless"; exit 1; }

echo "[verify-backend] checkstyleMain"
./gradlew checkstyleMain || { echo "[fail] checkstyle"; exit 1; }

echo "[verify-backend] test"
./gradlew test || { echo "[fail] test"; exit 1; }

echo "[verify-backend] SUCCESS"
