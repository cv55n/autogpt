FROM python:3.11.10-slim-bookworm AS builder

# configura as variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN echo 'Acquire::http::Pipeline-Depth 0;\nAcquire::http::No-Cache true;\nAcquire::BrokenProxy true;\n' > /etc/apt/apt.conf.d/99fixbadproxy

RUN apt-get update --allow-releaseinfo-change --fix-missing

# instalando as dependências da build
RUN apt-get install -y build-essential 
RUN apt-get install -y libpq5
RUN apt-get install -y libz-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y postgresql-client

ENV POETRY_HOME=/opt/poetry
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH=/opt/poetry/bin:$PATH

# atualiza o pip e o setuptools para corrigir as vulnerabilidades de segurança
RUN pip3 install --upgrade pip setuptools

RUN pip3 install poetry

# copia e instala as dependências
COPY autogpt_platform/autogpt_libs /app/autogpt_platform/autogpt_libs
COPY autogpt_platform/backend/poetry.lock autogpt_platform/backend/pyproject.toml /app/autogpt_platform/backend/
WORKDIR /app/autogpt_platform/backend
RUN poetry install --no-ansi --no-root

# gera o cliente prisma
COPY autogpt_platform/backend/schema.prisma ./
RUN poetry run prisma generate

FROM python:3.11.10-slim-bookworm AS server_dependencies

WORKDIR /app

ENV POETRY_HOME=/opt/poetry \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false
ENV PATH=/opt/poetry/bin:$PATH

# atualiza o pip e o setuptools para corrigir as vulnerabilidades de segurança
RUN pip3 install --upgrade pip setuptools

# copia apenas os arquivos necessários do builder
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin

# copia os binários do prisma
COPY --from=builder /root/.cache/prisma-python/binaries /root/.cache/prisma-python/binaries

ENV PATH="/app/.venv/bin:$PATH"

RUN mkdir -p /app/autogpt_platform/autogpt_libs
RUN mkdir -p /app/autogpt_platform/backend

COPY autogpt_platform/autogpt_libs /app/autogpt_platform/autogpt_libs

COPY autogpt_platform/backend/poetry.lock autogpt_platform/backend/pyproject.toml /app/autogpt_platform/backend/

WORKDIR /app/autogpt_platform/backend

FROM server_dependencies AS server

COPY autogpt_platform/backend /app/autogpt_platform/backend
RUN poetry install --no-ansi --only-root

ENV PORT=8000

CMD ["poetry", "run", "rest"]