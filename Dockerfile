FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY backend_app.py .

# Create data directory
RUN mkdir -p /data

# Expose port (Gunicorn default for Railway)
EXPOSE 8080

# Health check matching Gunicorn's port
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health')" || exit 1

# Run app using Gunicorn bound cleanly to 0.0.0.0:8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "backend_app:app"]