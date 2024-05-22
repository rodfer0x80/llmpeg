#!/bin/sh

CACHE=.
VENV=$CACHE/.venv
POETRY=$VENV/bin/poetry
$POETRY install
$POETRY update