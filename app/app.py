from fastapi import FastAPI, Form
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("fraud_model.pkl")

@app.post("/predict")
def predict(data: str = Form(...)):
    try:
        data_list = list(map(float, data.split(",")))
        data_array = np.array(data_list).reshape(1, -1)

        pred = model.predict(data_array)

        return {"prediction": int(pred[0])}   

    except Exception as e:
        return {"error": str(e)}