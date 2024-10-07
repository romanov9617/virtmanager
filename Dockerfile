FROM python:3.12-slim-bullseye

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN pip install --upgrade pip \
    && python -m pip install --no-cache-dir poetry==1.8.2 \
    && poetry install --no-interaction --no-ansi

COPY . /code/
