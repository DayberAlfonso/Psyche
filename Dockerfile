# Use Python 3.12 as base image (3.14 not yet released)
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen --no-dev

# Copy application source code
COPY src/ ./src/

# Expose the default Dash port
EXPOSE 8050

# Set Python path to include the src directory
ENV PYTHONPATH=/app/src

# Run the app with gunicorn for production
# Dash apps expose their Flask WSGI app via app.server
# Change to src directory and run gunicorn with the app.server
WORKDIR /app/src

CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:8050", "--workers", "2", "--threads", "2", "--timeout", "120", "wsgi:application"]
