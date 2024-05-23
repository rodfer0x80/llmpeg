#!/bin/sh

CACHE=.
VENV=$CACHE/.venv
POETRY=$VENV/bin/poetry
$POETRY remove $1
