#!/bin/sh

pkill ollama
ollama serve & 
./.venv/bin/python __main__.py
