from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# model load
model = joblib.load("model/fraud_model.pkl")

@app.get("/")
def home():
    return {"message": "Fraud Detection API is running 🚀"}

# NEW API
@app.post("/predict")
def predict(data: list):
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "Fraud Transaction 🚨"
    else:
        result = "Normal Transaction ✅"

    return {"prediction": result}