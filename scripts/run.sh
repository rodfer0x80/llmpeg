#!/bin/sh

CACHE="$XDG_CACHE_HOME/llmpeg"
VENV=$CACHE/.venv
POETRY=$VENV/bin/poetry
$POETRY run main "gemma:2b" "punkt" "small" "small" "google/paligemma-3b-mix-224" run
