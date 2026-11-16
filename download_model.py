
import os
from pathlib import Path

import mlflow
from mlflow.artifacts import download_artifacts

# Read temporary Docker build secrets
os.environ["MLFLOW_TRACKING_URI"] = Path(
    "/run/secrets/MLFLOW_TRACKING_URI"
).read_text().strip()

os.environ["MLFLOW_TRACKING_USERNAME"] = Path(
    "/run/secrets/MLFLOW_TRACKING_USERNAME"
).read_text().strip()

os.environ["MLFLOW_TRACKING_PASSWORD"] = Path(
    "/run/secrets/MLFLOW_TRACKING_PASSWORD"
).read_text().strip()

tracking_uri = os.environ["MLFLOW_TRACKING_URI"]

mlflow.set_tracking_uri(tracking_uri)
mlflow.set_registry_uri(tracking_uri)

model_uri = "models:/random_forest_model_run_V1.0.2/1"

# Download the registered model into the Docker image
downloaded_path = download_artifacts(
    artifact_uri=model_uri,
    dst_path="model"
)

print("Model downloaded successfully:", downloaded_path)
