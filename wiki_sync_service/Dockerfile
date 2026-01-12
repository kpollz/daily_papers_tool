FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY wiki_utils/ ./wiki_utils/
COPY wiki_sync_service.py .
COPY sync_to_wiki.py .

# Create directory for state file
RUN mkdir -p /app/data

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV STATE_FILE=/app/data/.synced_files.json

# Run the service
CMD ["python", "wiki_sync_service.py"]

