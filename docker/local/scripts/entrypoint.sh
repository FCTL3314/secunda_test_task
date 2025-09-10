#!/bin/sh
set -e

uv sync --locked

uv run make apply_migrations

uv run uvicorn src.main:app --host 0.0.0.0 --port "${INTERNAL_PORT}" --reload
