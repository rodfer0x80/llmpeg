#!/bin/sh

pkill ollama && sleep 60
ollama serve &
sleep 10
./.venv/bin/python __main__.py
pkill ollam
sleep 3
