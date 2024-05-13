# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.2
FROM python:${PYTHON_VERSION}-slim as base

# Set the working directory in the container
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install --no-install-recommends -y build-essential

# Install Poetry
RUN pip install poetry

# Copy the dependencies file to the working directory
COPY pyproject.toml poetry.lock* ./

# Project initialization:
RUN poetry config virtualenvs.create true && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-interaction --no-ansi

ENV PYTHONPATH=/workspace

# Copy the source code into the container.
COPY . .

ENTRYPOINT ["poetry", "run", "python", "scripts/main.py"]
