FROM python:3.12-slim

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python3 -
# poetry workers 10

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
