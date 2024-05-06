#!/bin/sh

pkill ollama
sleep 10
ollama serve & 
./.venv/bin/python __main__.py
pkill ollama
