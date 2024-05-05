#!/bin/sh
#
pkill ollama
ollama serve 2>1 >/dev/null &
./.venv/bin/python __main__.py
