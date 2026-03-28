from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np

app = FastAPI()

# Load model
model = joblib.load("model/fraud_model.pkl")

# Input schema (IMPORTANT)
class InputData(BaseModel):
    data: List[float]

# Home route
@app.get("/")
def home():
    return {"message": "Fraud Detection API is running 🚀"}

# Prediction API
@app.post("/predict")
def predict(input: InputData):
    data = np.array(input.data).reshape(1, -1)

    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "Fraud Transaction 🚨"
    else:
        result = "Normal Transaction 🟩"

    return {"prediction": result}