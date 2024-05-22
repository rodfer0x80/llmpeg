FROM ollama/ollama:latest

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    python3-venv \
    && apt-get clean
# globally install poetry and upgrade pip things
# (NOTE: the poetry project often releases new versions over weekends, so
#        if your have auto-building services and poetry releases a new incompatible
#        version, your stuff will just break randomly on Saturday nights; so you _could_
#        pin your specific poetry version here, but also fix-as-it-breaks is valid too)
RUN pip install pip poetry setuptools wheel -U --no-cache-dir

# Copy your project definitions into the image
COPY pyproject.toml poetry.lock .

# Run the virtual env creator and dependency installer
# (NOTE: some python packages like mysqlclient require more system binary packages
#        to be installed, so you'd need to apt-get other packages as required before
#        your poetry install if needed)
RUN poetry install --without=dev --no-cache

# Copy your project package
COPY llmpeg llmpeg

# Now install the project package itself
# NOTE: Yes, we run `poetry install` TWICE due to the docker
#       caching logic because we don't want to reinstall dependencies
#       on every code update. This means the dependencies are cached
#       in the _first_ `poetry install` layer, while _this_ `poetry install`
#       layer just handles a final "script cleanup" install due to path issues.
RUN poetry install --without=dev --no-cache

# now run your command (as defined in `pyproject.toml` poetry scripts section)
CMD poetry run main --conversation_model "gemma:2b" --nlp_model "punkt" --tts_model_size "small" --stt_model_size "tiny" - run
