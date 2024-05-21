#!/bin/sh
ruff format --config ruff.toml --preview
ruff check --config ruff.toml --preview