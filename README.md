💳 Credit Card Fraud Detection

An end-to-end Machine Learning project to detect fraudulent credit card transactions using a trained Random Forest model. This project includes model training, API deployment using FastAPI, and a simple UI using Streamlit.

---

🚀 Live Demo

🔗 FastAPI Docs:
https://credit-card-fraud-detection-6-qmw2.onrender.com/docs

🔗 API Base URL:
https://credit-card-fraud-detection-6-qmw2.onrender.com

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

📦 Features

- 🔍 Real-time fraud prediction
- ⚡ FastAPI backend for inference
- 🌐 Deployed on cloud (Render)
- 🖥️ Streamlit UI for easy testing
- 📊 Handles imbalanced dataset

---

📡 API Usage

Endpoint:

POST "/predict"

Request Body:

{
  "data": [0.1, -1.2, 0.5, 1.3, ..., 150.0]
}

👉 Note: Input must contain 29 features

---

Response:

{
  "prediction": "Fraud Transaction"
}

OR

{
  "prediction": "Normal Transaction"
}

---

🖥️ Run Locally

git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection

pip install -r requirements.txt

uvicorn app:app --reload

Open: http://127.0.0.1:8000/docs

---

📸 Screenshots

(Add screenshots here later)

---

📌 Future Improvements

- Add model monitoring
- Add authentication
- Improve UI design
- Use Docker for deployment

---

🙌 Author

Shiva
Machine Learning Enthusiast 🚀
