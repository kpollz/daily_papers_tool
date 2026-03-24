FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set timezone to Vietnam (UTC+7)
ENV TZ=Asia/Ho_Chi_Minh
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create directories for logs and temp files
RUN mkdir -p papers summaries

# Run scheduler service
CMD ["python", "scheduler_service.py"]
