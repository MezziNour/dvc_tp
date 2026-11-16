FROM python:3.13.5-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model download script
COPY download_model.py .

# Download the registered model using temporary build secrets
RUN --mount=type=secret,id=MLFLOW_TRACKING_URI \
    --mount=type=secret,id=MLFLOW_TRACKING_USERNAME \
    --mount=type=secret,id=MLFLOW_TRACKING_PASSWORD \
    python download_model.py

# Copy the FastAPI application
COPY app.py .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
