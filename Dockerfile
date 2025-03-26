FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

ENV PYTHONUNBUFFERED 1
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Expose necessary ports
EXPOSE 8000 11434
