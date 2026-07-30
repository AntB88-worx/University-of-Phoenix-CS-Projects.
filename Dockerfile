FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir requests
COPY inventory_stream.py .
CMD ["python", "inventory_stream.py"]
