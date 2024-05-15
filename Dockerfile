FROM python:3.12.3-slim

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml .

RUN poetry install --only main --no-root

COPY src .

ENTRYPOINT [ "task" ]