FROM python:3.12-slim

# globally install poetry and upgrade pip things
# (NOTE: the poetry project often releases new versions over weekends, so
#        if your have auto-building services and poetry releases a new incompatible
#        version, your stuff will just break randomly on Saturday nights; so you _could_
#        pin your specific poetry version here, but also fix-as-it-breaks is valid too)
RUN pip install pip poetry setuptools wheel -U --no-cache-dir

# Copy your project definitions into the image
COPY pyproject.toml poetry.lock README.md .

# Run the virtual env creator and dependency installer
# (NOTE: some python packages like mysqlclient require more system binary packages
#        to be installed, so you'd need to apt-get other packages as required before
#        your poetry install if needed)
RUN poetry install --without=dev --no-cache

# Copy your project package
COPY hello hello

# Now install the project package itself
# NOTE: Yes, we run `poetry install` TWICE due to the docker
#       caching logic because we don't want to reinstall dependencies
#       on every code update. This means the dependencies are cached
#       in the _first_ `poetry install` layer, while _this_ `poetry install`
#       layer just handles a final "script cleanup" install due to path issues.
RUN poetry install --without=dev --no-cache

# now run your command (as defined in `pyproject.toml` poetry scripts section)
CMD poetry run hello-command extra-args
