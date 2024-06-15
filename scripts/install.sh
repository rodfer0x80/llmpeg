#!/bin/sh

CACHE="$XDG_CACHE_HOME/llmpeg"
VENV=$CACHE/.venv
PYTHON="/usr/bin/python3.12"
PIP=$VENV/bin/pip
POETRY=$VENV/bin/poetry

mkdir -p $CACHE
if [ -d $VENV ]; then
    rm -rf $VENV ./poetry.lock
fi
$PYTHON -m venv $VENV
$PIP install --upgrade pip
$PIP install wheel setuptools poetry ruff
$POETRY install