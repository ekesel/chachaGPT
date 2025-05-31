# Use official Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (for layer caching)
COPY requirements.txt .

# Install system dependencies (if needed) and Python dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to start Uvicorn with your FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
