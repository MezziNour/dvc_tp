import mlflow.pyfunc
import numpy as np

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Digits Prediction API")

# Load the model downloaded during Docker build
model = mlflow.pyfunc.load_model("model")


class PredictionInput(BaseModel):
    features: list[float] = Field(
        ...,
        min_length=64,
        max_length=64
    )


@app.post("/predict")
def predict(data: PredictionInput):
    # Convert the 64 pixel values into a NumPy array
    input_data = np.array([data.features])

    # Predict the digit
    prediction = model.predict(input_data)

    return {"prediction": int(prediction[0])}
