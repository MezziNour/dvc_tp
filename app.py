
import mlflow
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Digits Prediction API")

# Load the trained model
model = mlflow.pyfunc.load_model("model")


class PredictionInput(BaseModel):
    features: list[float] = Field(
        ...,
        min_length=64,
        max_length=64
    )


@app.post("/predict")
def predict(data: PredictionInput):
    # Convert input into a DataFrame
    columns = [f"pixel_{i}" for i in range(64)]
    input_data = pd.DataFrame(
        [data.features],
        columns=columns
    )

    # Make prediction
    prediction = model.predict(input_data)

    return {"prediction": int(prediction[0])}
