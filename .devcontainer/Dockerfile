# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.209.6/containers/python-3/.devcontainer/base.Dockerfile
# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG USERNAME=root
ARG VARIANT="3.11-bullseye"
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# Additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libsystemd-dev \
    libudev-dev \
    curl \
    gnupg \
    software-properties-common \
    unzip \
    wget \
    jq \
    sqlite3

ENV POETRY_PATH /$USERNAME/.poetry
RUN curl -sSL https://install.python-poetry.org | python - \
    && pip install -U pip setuptools

ENV PATH "$POETRY_PATH/bin:$PATH"
