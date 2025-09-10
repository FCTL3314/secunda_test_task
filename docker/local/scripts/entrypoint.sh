#!/bin/sh
set -e

uv sync --locked --all-extras

uv run make apply_migrations

uv run uvicorn src.main:app --host 0.0.0.0 --port "${INTERNAL_PORT}" --reload
