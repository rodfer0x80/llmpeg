#!/bin/sh

python3.8 -m venv .venv
./venv/bin/pip install wheel setuptools poetry
./venv/bin/poetry install