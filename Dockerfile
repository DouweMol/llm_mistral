FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install system dependencies (if needed, e.g. for numpy/scipy)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command (change main.py to your entrypoint if needed)
CMD ["python", "scripts/main.py"]