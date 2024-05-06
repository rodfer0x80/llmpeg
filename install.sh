#!/bin/sh

# !rm -rf sakass; git clone https://github.com/rodfer0x80/sakass.git; cd ./sakass; ./install.sh

apt update; apt install python3.10-venv
curl -fsSL https://ollama.com/install.sh | sh
apt-get update; apt-get install libgstreamer-gl1.0-0 libwoff-dev gstreamer1.0-plugins-bad libharfbuzz-icu0 libenchant-2-2 libsecret-1-0 libhyphen0 libmanette-0.2-0


python -m venv .venv &&\
  ./.venv/bin/pip install --upgrade pip &&\
  ./.venv/bin/pip install -r requirements.txt &&\
  ./.venv/bin/python -m playwright install
  
ollama serve & 
sleep 10
ollama pull gemma:2b
ollama pull nomic-embed-text
pkill ollama
sleep 60
