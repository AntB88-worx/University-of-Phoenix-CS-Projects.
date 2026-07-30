# Phase 1: Local Containerized Data Streams 🛰️

This sub-project demonstrates core competencies in Linux CLI systems, in-memory data processing, and local containerization.

### 🛠️ Architecture & Objectives
* **Refactored Data Flows:** Optimized standard file-based Python scripts to stream simulated data blocks entirely in-memory, minimizing heavy disk-I/O performance bottlenecks.
* **Declarative Containerization:** Authored a production-grade `Dockerfile` using strict, optimized image tags (`python:3.11-slim`) to guarantee platform-agnostic execution.
* **Shell Automation:** Engineered a native Bash `setup.sh` script to handle automatic file permission modifications (`chmod +x`) and trigger programmatic image compilation.

### 🚀 Local Execution
Execute the automated automation wrapper to launch the application isolation layer:
```bash
chmod +x setup.sh && ./setup.sh
docker run -it inventory-stream-pipeline
```
