# Use an explicit, lightweight, official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Prevent Python from writing .pyc files to disk and ensure output is logged instantly
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy the local script into the container's working directory
COPY inventory_stream.py /app/

# Install dependencies if you have any (uncomment if you add a requirements.txt later)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Run the stream script as the container startup process
CMD ["python", "inventory_stream.py"]
