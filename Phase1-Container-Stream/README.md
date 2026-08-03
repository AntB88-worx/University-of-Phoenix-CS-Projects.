# Phase 1: Local Containerized Data Streams 🛰️

This sub-project demonstrates core competencies in Linux CLI systems, in-memory data processing, and local containerization.

### 🛠️ Architecture & Objectives
* **Refactored Data Flows:** Optimized standard file-based Python scripts to stream simulated data blocks entirely in-memory, minimizing heavy disk-I/O performance bottlenecks.
* **Declarative Containerization:** Authored a production-grade `Dockerfile` using strict, optimized image tags (`python:3.11-slim`) to guarantee platform-agnostic execution.
* **Shell Automation:** Engineered a native Bash `setup.sh` script to handle automatic file permission modifications (`chmod +x`) and trigger programmatic image compilation.

### 🚀 Local Execution
To build, verify, and run the isolated container data stream locally, execute the following terminal commands:

```bash
# 1. Grant execution rights and run the automated architecture setup harness
chmod +x setup.sh && ./setup.sh

# 2. Spin up the isolated in-memory Python data stream handler
docker run --rm -it inventory-stream-pipeline

# 3. (Optional) Run the local automated Bash testing scripts
bash scripts/run_tests.sh
```
