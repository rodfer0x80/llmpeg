#!/bin/sh

CACHE=.
VENV=$CACHE/.venv
POETRY=$VENV/bin/poetry
$POETRY run main "gemma:2b" "punkt" "small" "tiny" run