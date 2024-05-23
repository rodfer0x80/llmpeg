#!/bin/sh

CACHE=~/.cache
VENV=$CACHE/.venv
POETRY=$VENV/bin/poetry
$POETRY run main "gemma:2b" "punkt" "small" "tiny" run