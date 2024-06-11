#!/bin/sh

CACHE="$XDG_CACHE_HOME/llmpeg"
VENV=$CACHE/.venv
POETRY=$VENV/bin/poetry
$POETRY remove $1
