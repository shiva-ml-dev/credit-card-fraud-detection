# app.py

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Initialize app
app = FastAPI(title="Credit Card Fraud Detection API")

# Load model (make sure file is in same folder)
model = joblib.load("model/fraud_model.pkl")


# Input schema (JSON format)
class InputData(BaseModel):
    features: list[float]


# Home route (for testing)
@app.get("/")
def home():
    return {"message": "Fraud Detection API is running 🚀"}


# Prediction route
@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert to numpy array
        data_array = np.array(data.features).reshape(1, -1)

        # Prediction
        prediction = model.predict(data_array)[0]

        # Optional: probability
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(data_array)[0][1]
        else:
            prob = None

        return {
            "prediction": int(prediction),
            "probability": float(prob) if prob is not None else None,
            "status": "Fraud" if prediction == 1 else "Normal"
        }

    except Exception as e:
        return {"error": str(e)}