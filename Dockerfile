FROM python:3.12-slim as base

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Europe/Moscow \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONPATH=/app \
    POETRY_VERSION=1.8.5 \
    POETRY_VIRTUALENVS_CREATE=false

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==$POETRY_VERSION"


FROM base as builder

WORKDIR /app

# Устанавливаем dev-зависимости только в builder
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    python3-dev \
    libpq-dev \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi


FROM python:3.12-slim as final  

WORKDIR /app

RUN groupadd -r appuser && useradd -d /app -r -g appuser appuser

COPY --from=builder /usr/local /usr/local
COPY . /app/

RUN chmod -R 755 /app && chown -R appuser:appuser /app

USER appuser

CMD ["python", "-m", "src.pomodoro"]
