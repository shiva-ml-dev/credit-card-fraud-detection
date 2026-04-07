💳 Credit Card Fraud Detection

A machine learning project to detect fraudulent credit card transactions using Random Forest, handling class imbalance with SMOTE.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Render](https://img.shields.io/badge/Deploy-Render-purple)

---

📌 Project Highlights

- End-to-end ML project (Training → Deployment)
- Real-time fraud detection API
- Deployed using FastAPI on Render
- Includes Streamlit UI for testing

---

🚀 Live Demo

🚀 Try the live app here:

- 🔗 FastAPI Docs: https://credit-card-fraud-detection-6-qmw2.onrender.com/docs
- 🔗 API Base URL: https://credit-card-fraud-detection-6-qmw2.onrender.com
- 🌐 Streamlit App: https://credit-card-fraud-detection-nh2nruv2xnenz8f6vhdjhn.streamlit.app

---

🧪 Try It Yourself (Live API Input)

Use this sample input in "/predict" endpoint:

✅ Normal Transaction Input

[0.1, -1.2, 0.5, 1.3, -0.7, 0.9, -0.2, 0.4, -1.1, 0.3, 0.8, -0.6, 1.0, -0.9, 0.2, 0.7, -0.3, 0.6, -1.4, 0.1, 0.5, -0.5, 1.2, -0.4, 0.9, 0.3, -0.2, 0.7, 50.0]

🚨 Fraud Transaction Input

[-1.27, 2.46, -2.85, 2.32, -1.37, -0.94, -3.06, 1.16, -2.26, -4.88, 2.25, -4.68, 0.65, -6.17, 0.59, -4.84, -6.53, -3.11, 1.71, 0.56, 0.65, -0.08, -0.22, -0.52, 0.22, 0.75, 0.63, 0.25, 0.01]

---

🧠 Model Details

- Algorithm: Random Forest Classifier
- Problem Type: Binary Classification (Fraud / Normal)
- Dataset: Highly imbalanced credit card transactions
- Features: 29 input features

---

⚙️ Tech Stack

- Python
- FastAPI
- Streamlit
- Scikit-learn
- Uvicorn
- Render (Deployment)

---

🚀 Features

- 🔍 Real-time fraud prediction
- ⚡ FastAPI backend for inference
- 🌐 Deployed on cloud (Render)
- 🖥️ Streamlit UI for easy testing
- 📊 Handles imbalanced dataset

---

## 🏗️ Architecture

User → Streamlit UI → FastAPI Backend → ML Model → Prediction Result

---

📊 Example Outputs

✅ Normal Transaction

{ "prediction": "Normal Transaction ✅" }

🚨 Fraud Transaction

{ "prediction": "Fraud Transaction 🚨" }

---

💻 Run Locally

git clone https://github.com/shiva-ml-dev/credit-card-fraud-detection.git
cd credit-card-fraud-detection

pip install -r requirements.txt

uvicorn app:app --host 0.0.0.0 --port 8000 --reload

👉 Open: http://127.0.0.1:8000/docs

---

🖥️ Streamlit UI

### 🟢 Normal Transaction Prediction

![Normal](https://raw.githubusercontent.com/shiva-ml-dev/credit-card-fraud-detection/main/assets/images/streamlit_normal.png)

### 🔴 Fraud Transaction Prediction

![Fraud](https://raw.githubusercontent.com/shiva-ml-dev/credit-card-fraud-detection/main/assets/images/streamlit_fraud.png)

---

🔮 Future Improvements

- Add model monitoring
- Add authentication
- Improve UI design
- Use Docker for deployment

---

👨‍💻 Author

Shivashankar Kakanale
Machine Learning Engineer | Open to Opportunities 🚀

- GitHub: https://github.com/shiva-ml-dev
- LinkedIn: https://www.linkedin.com/in/shivashankar-kakanale-2a337329a
- Email: kakanaleshivashankar@gmail.com

---
