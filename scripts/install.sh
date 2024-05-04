#!/bin/sh

VENV="$HOME/.local/share/python3-venv"
PY3="$HOME/.local/share/python3-venv/bin/python3"
PYPIP3="$HOME/.local/share/python3-venv/bin/pip3"

python3 -m venv "$VENV"
$PYPIP3 install -r requirements.txt
$PY -m playwright install
