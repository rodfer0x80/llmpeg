#!/bin/sh

CACHE=~/.cache
VENV=$CACHE/.venv
RUFF=$VENV/bin/ruff
$RUFF format --config ruff.toml --preview
$RUFF check --config ruff.toml --preview