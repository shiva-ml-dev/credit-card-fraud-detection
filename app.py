from fastapi import FastAPI
from typing import List
import joblib
import numpy as np

app = FastAPI()

model = None

@app.on_event("startup")
def load_model():
    global model
    model = joblib.load("model/fraud_model.pkl")

@app.get("/")
def home():
    return {"message": "Fraud Detection API is running 🚀"}

@app.post("/predict")
def predict(data: List[float]):
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "Fraud Transaction 🚨"
    else:
        result = "Normal Transaction ✅"

    return {"prediction": result}