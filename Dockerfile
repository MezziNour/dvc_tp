FROM python:3.13.5-slim

WORKDIR /app

# Installer les requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code pour télécharger le modèle
COPY download_model.py .

# Utiliser les secrets pour télécharger le modèle depuis MLflow
RUN --mount=type=secret,id=MLFLOW_TRACKING_URI \
    --mount=type=secret,id=MLFLOW_TRACKING_USERNAME \
    --mount=type=secret,id=MLFLOW_TRACKING_PASSWORD \
    python download_model.py

# Copier le code de l'application FastAPI
COPY app.py .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
