FROM python:3.11-slim

WORKDIR /app

<<<<<<< HEAD
# Copy requirements first
=======
# Copy requirements first (for better caching)
>>>>>>> latest_branch
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

<<<<<<< HEAD
# Copy application
=======
# Copy application code
>>>>>>> latest_branch
COPY backend_app.py .

# Create data directory
RUN mkdir -p /data

<<<<<<< HEAD
# Expose the application port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')" || exit 1

# Start Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "backend_app:app"]
=======
# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

# Run app
CMD ["python", "backend_app.py"]
>>>>>>> latest_branch
