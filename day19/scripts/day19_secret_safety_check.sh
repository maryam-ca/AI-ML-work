#!/usr/bin/env bash

echo "Checking env files..."

git ls-files | grep .env || true

echo "Done."
