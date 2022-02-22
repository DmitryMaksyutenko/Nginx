FROM python:3.10

WORKDIR /app

COPY ./app3 /app/app3

COPY ./pdm.lock /app
COPY ./pyproject.toml /app

RUN pip install pdm

RUN pdm install
