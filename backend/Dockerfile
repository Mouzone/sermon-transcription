# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.3
FROM python:${PYTHON_VERSION}-slim as base

# Python settings
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Create non-privileged user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Install uv (as root)
RUN pip install --no-cache-dir uv==0.1.44

# Copy dependency files first for better caching
COPY --chown=appuser:appuser pyproject.toml .

# Install dependencies (as root)
RUN uv pip install .

# Switch to non-privileged user
USER appuser

# Copy application code
COPY --chown=appuser:appuser . .

# Expose application port
EXPOSE 8000

# Run the application
CMD ["uv", "run", "main.py"]