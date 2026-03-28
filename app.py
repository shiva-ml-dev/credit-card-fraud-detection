from fastapi import FastAPI
import joblib
import numpy as np
from typing import List

app = FastAPI()

# Load model
model = joblib.load("model/fraud_model.pkl")

# Home route
@app.get("/")
def home():
    return {"message": "Fraud Detection API is running 🚀"}

# Prediction API
@app.post("/predict")
def predict(data: List[float]):
    try:
        # Convert to numpy array
        data = np.array(data).reshape(1, -1)

        # Prediction
        prediction = model.predict(data)[0]

        # Result
        if prediction == 1:
            result = "Fraud Transaction 🚨"
        else:
            result = "Normal Transaction ✅"

        return {"prediction": result}

    except Exception as e:
        return {"error": str(e)}