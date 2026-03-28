# streamlit_app.py

import streamlit as st
import requests
import numpy as np

# 🔗 FastAPI URL (local)
API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Fraud Detection App", layout="centered")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter 30 feature values (comma separated):")

# Input box
input_data = st.text_area(
    "Example:",
    "0.1, -1.2, 2.3, 0.5, -0.8, 1.1, -2.0, 0.3, 0.7, -1.5, "
    "0.9, -0.4, 1.2, -0.6, 0.8, -1.1, 2.2, -0.9, 0.4, -0.3, "
    "1.5, -2.3, 0.6, -0.7, 1.0, -1.8, 0.2, 0.3, -0.5, 0.9"
)

# Predict button
if st.button("🔍 Predict"):

    try:
        # Convert input string → list
        values = [float(x.strip()) for x in input_data.split(",")]

        # Check length
        if len(values) != 30:
            st.error("❌ Please enter exactly 30 values")
        else:
            # API call
            response = requests.post(API_URL, json={"features": values})

            if response.status_code == 200:
                result = response.json()

                prediction = result["prediction"]
                probability = result.get("probability", None)
                status = result.get("status", "Unknown")

                # Display result
                st.subheader("Result:")

                if prediction == 1:
                    st.error(f"🚨 Fraud Transaction\nProbability: {probability:.4f}")
                else:
                    st.success(f"✅ Normal Transaction\nProbability: {probability:.4f}")

            else:
                st.error("❌ API Error")

    except Exception as e:
        st.error(f"❌ Invalid input format: {e}")