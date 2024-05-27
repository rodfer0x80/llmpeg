#!/bin/sh

CACHE=~/.cache
VENV=$CACHE/.venv
POETRY=$VENV/bin/poetry
$POETRY run main "llama3" "punkt" "large" "base" run
