import streamlit as st
import joblib
import numpy as np

model = joblib.load("fraud_model.pkl")

st.title("💳 Credit Card Fraud Detection")

data = st.text_input("Enter 30 values (comma separated):")

if st.button("Predict"):
    try:
        data_list = list(map(float, data.split(",")))
        data_array = np.array(data_list).reshape(1, -1)

        pred = model.predict(data_array)

        if pred[0] == 1:
            st.error("⚠️ Fraud Transaction")
        else:
            st.success("✅ Normal Transaction")

    except Exception as e:
        st.error(f"Error: {e}")