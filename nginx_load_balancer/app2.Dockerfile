FROM python:3.10

WORKDIR /app

COPY ./app2 /app/app2

COPY ./pdm.lock /app
COPY ./pyproject.toml /app

RUN pip install pdm

RUN pdm install
