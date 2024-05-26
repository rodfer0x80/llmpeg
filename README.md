# llmpeg

## Requirements
````
> running locally
espeak [ https://github.com/espeak-ng/espeak-ng ] 
ffmpeg [ https://ffmpeg.org/ ]
vlc [ https://www.videolan.org/ ]
chrome [ https://www.chromium.org/ ]
chromedriver [ https://developer.chrome.com/docs/chromedriver/downloads ]
ollama (server must be running) [ https://ollama.com/ ]
> running with docker:
nvidia-container-toolkit [ https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html ]

--
for ubuntu check ci/llmpeg.Dockerfile for all packages needed 
````

## TODO
[x] fix play audio output
[x] headless browser
[x] pyproject proper struct
[x] upgrade to python3.11
[x] dockerfile update to python3.11
[x] containerd cluster run ollama server and llmpeg client
...
[x] clipboard feature for chat browsing
[x] test nlp for chat flow and controls
[ ] sqlite db for llm chat
[ ] agent pipeline for executing actions in chaingraph of functions
[ ] chat wait feature
[ ] add regression tests
[ ] add docs
[ ] dynamic config 
...
[ ] expand web search for processing screenshots+scraping to extract intel
[ ] expand web search with rag?
...
[ ] models in tinygrad
...
[ ] basic gui web?
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
nlp llm model
https://github.com/ollama/ollama/blob/main/docs/import.md
https://huggingface.co/docs/transformers/main/en/model_doc/gpt_neo#transformers.GPTNeoForCausalLM
https://github.com/ollama/ollama/blob/main/docs/import.md#manually-converting--quantizing-models
````


````
improve
https://www.geoffreylitt.com/2023/03/25/llm-end-user-programming
https://blog.waleson.com/2024/05/the-long-long-tail-of-ai-applications.html
https://www.strangeloopcanon.com/p/what-can-llms-never-do
https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/#cluster-and-model-topics
````

````
expand websearch
https://www.youtube.com/watch?v=ZE6t9trCRnw
https://www.youtube.com/watch?v=W5XNOmyJr6I
````

````
speech -> vits or openvoice 
https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md
https://github.com/myshell-ai/OpenVoice/blob/main/demo_part3.ipynb
https://huggingface.co/docs/transformers/en/model_doc/vits
````

````
listen -> wav2vec or whisper local 
https://huggingface.co/docs/transformers/en/model_doc/whisper
https://huggingface.co/docs/transformers/en/model_doc/wav2vec2
````
