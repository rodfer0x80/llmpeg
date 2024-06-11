#!/bin/sh

CACHE="$XDG_CACHE_HOME/llmpeg"
VENV=$CACHE/.venv
POETRY=$VENV/bin/poetry
$POETRY run main "gemma:2b" "punkt" "small" "small" run
