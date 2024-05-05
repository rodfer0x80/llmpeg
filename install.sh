#!/bin/sh

python -m venv .venv &&\
  ./.venv/bin/pip install -r requirements.txt &&\
  ./.venv/bin/python -m playwright install
  
ollama serve & 2>1 >/dev/null
ollama pull gemma:2b
ollama pull nomic-embed-text
pkill ollama
