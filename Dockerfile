FROM python:3.12.0-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev

RUN pip install poetry
RUN poetry install
