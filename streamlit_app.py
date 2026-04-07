import streamlit as st
import requests
import time

# 🔗 Render FastAPI URL
API_URL = "https://credit-card-fraud-detection-6-qmw2.onrender.com/predict"

# 🎨 UI
st.set_page_config(page_title="Fraud Detection App", layout="centered")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter 29 feature values (comma separated):")

# 🧾 Input box
input_data = st.text_area(
    "Example:",
    "0.1,-1.2,0.5,1.3,-0.7,0.9,-0.2,0.4,-1.1,0.3,0.8,-0.6,1.0,-0.9,0.2,0.7,-0.3,0.6,-1.4,0.1,0.5,-0.5,1.2,-0.4,0.9,0.3,-0.2,0.7,50.0"
)

# 🔘 Predict button
if st.button("🔍 Predict"):
    try:
        # 👉 Convert string to list
        values = [float(x.strip()) for x in input_data.split(",")]

        # ✅ Check length (29 features)
        if len(values) != 29:
            st.error("❌ Please enter exactly 29 values")
        else:
            with st.spinner("⏳ Waking up server... Please wait (10–20 sec)"):

                response = None

                # 🔁 Retry logic (important for Render sleep)
                for i in range(5):
                    try:
                        response = requests.post(
                            API_URL,
                            json=values,
                            timeout=30
                        )

                        if response.status_code == 200:
                            break

                    except Exception as e:
                        print(e)

                    time.sleep(3)

            # ✅ Success case
            if response and response.status_code == 200:
                result = response.json()
                prediction = result["prediction"]

                st.subheader("Result:")

                if "Fraud" in prediction:
                    st.error(f"🚨 {prediction}")
                else:
                    st.success(f"✅ {prediction}")

            else:
                st.error(f"❌ API Error: {response.status_code if response else 'No response'}")

    except Exception as e:
        st.error(f"❌ Invalid input format: {e}")