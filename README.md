# llmpeg

## Requirements
````
speak [ https://github.com/espeak-ng/espeak-ng ] 
ffmpeg [ https://ffmpeg.org/ ]
nvidia-container-toolkit [ https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html ]
````

## TODO
[x] fix play audio output
[x] headless browser
[ ] pyproject proper struct
[x] upgrade to python3.11
...
[ ] dockerfile update to python3.11
[ ] containerd cluster run ollama server and llmpeg client
...
[ ] refactor into senses high abstraction layer into very basic agent for easy config
[ ] dynamic config 
[ ] basic cli with flags
[ ] install script linux/mac
...
[ ] basic gui with tk 
[ ] install gui windows
...
[ ] models in tinygrad

## Resources

````
project struct 
https://matt.sh/python-project-structure-2024
https://docs.python.org/3/library/itertools.html
https://more-itertools.readthedocs.io/en/stable/
https://boltons.readthedocs.io/en/latest/
https://grantjenks.com/docs/sortedcontainers/
https://grantjenks.com/docs/diskcache/
https://docs.peewee-orm.com/en/latest/peewee/quickstart.html#quickstart
https://github.com/ijl/orjson?tab=readme-ov-file
https://www.python-httpx.org/
````

````
docker
https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming.html
https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image
https://hub.docker.com/r/ollama/ollama
https://collabnix.com/getting-started-with-ollama-and-docker/
https://docs.coqui.ai/en/latest/inference.html
https://github.com/valiantlynx/ollama-docker
````

````
speech -> vits or openvoice 
https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md
https://github.com/myshell-ai/OpenVoice/blob/main/demo_part3.ipynb
https://huggingface.co/docs/transformers/en/model_doc/vits
listen -> wav2vec or whisper local 
https://huggingface.co/docs/transformers/en/model_doc/whisper
https://huggingface.co/docs/transformers/en/model_doc/wav2vec2
````
