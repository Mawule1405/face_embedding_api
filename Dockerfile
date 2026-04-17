# Use a standard Python image instead of NVIDIA
#FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04
FROM python:3.10-slim

WORKDIR /app

# 1. Install SYSTEM dependencies + BUILD tools
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    # Added these for building InsightFace:
    gcc \
    g++ \
    make \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. Upgrade pip and setuptools
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 3. Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ /app/

# Copy your local model to the InsightFace directory
COPY models/buffalo_l/ /root/.insightface/models/buffalo_l/

EXPOSE 8000

# Start the API
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]