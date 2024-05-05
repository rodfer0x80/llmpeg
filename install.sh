#!/bin/sh

python -m venv .venv &&\
  ./.venv/bin/pip install -r requirements.txt &&\
  ./.venv/bin/python -m playwright install
