#!/bin/sh

CACHE=~/.cache
VENV=$CACHE/.venv
POETRY=$VENV/bin/poetry
$POETRY add $1
