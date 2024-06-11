#!/bin/sh

CACHE="$XDG_CACHE_HOME/llmpeg"
VENV=$CACHE/.venv
rm -rf $VENV ./poetry.lock
