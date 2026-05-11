#!/usr/bin/env bash

set -euo pipefail

PROJECT_ID="${PROJECT_ID:?PROJECT_ID is required}"
REGION="${REGION:-us-central1}"
SERVICE_NAME="${SERVICE_NAME:-ai-backend}"

echo "Deploy prep started..."
echo "PROJECT_ID=$PROJECT_ID"
echo "REGION=$REGION"
echo "SERVICE_NAME=$SERVICE_NAME"
