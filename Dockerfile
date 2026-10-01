FROM python:3.14-slim

# Prevents Python from writing .pyc files & buffers stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# libpq5 covers psycopg2-binary's runtime needs.
# build-essential + libjpeg/zlib are a safety net for Pillow and any other
# package that doesn't yet ship a prebuilt wheel for Python 3.14.
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    build-essential \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv and project dependencies first (better layer caching)
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile --dev

# Copy the rest of the project
COPY . .

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

# Default command; overridden per-service in docker-compose.yml
CMD ["gunicorn", "storefront.wsgi", "--bind", "0.0.0.0:8000"]

