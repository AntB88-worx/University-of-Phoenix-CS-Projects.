#!/bin/bash

# Exit immediately if any command fails, ensuring predictable execution
set -e

echo "🚀 Starting Inventory Pipeline Setup..."

# 1. Check if Docker is installed and running
if ! command -v docker &> /dev/null; then
    echo "❌ Error: Docker is not installed or not in your PATH."
    echo "Please install Docker to proceed."
    exit 1
fi

# 2. Make sure python scripts have correct permissions
echo "🔧 Setting script permissions..."
chmod +x inventory_stream.py

# 3. Build the Docker container safely
echo "🐳 Building the Docker image (this may take a minute on first run)..."
docker build -t inventory-stream-pipeline .

echo "✅ Setup complete! You can now run the pipeline inside Docker."
echo "👉 Execute: docker run -it inventory-stream-pipeline"

