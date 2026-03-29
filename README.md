# 💳 Credit Card Fraud Detection

![Python 3. 10](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Deployment](https://img.shields.io/badge/Render-Deployed-success)

A machine learning project to detect fraudulent credit card transactions using XGBoost and Random Forest, handling class imbalance with SMOTE.

---

## 📌 Project Highlights

- End-to-end ML project (Training → Deployment)
- Real-time fraud detection API
- Deployed using FastAPI on Render
- Includes Streamlit UI for testing

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

## 🧪 API Usage

Endpoint:

POST /predict

Request Body:

{
  "data": [0.1, -1.2, 0.5, 1.3, ... ,150.0]
}

👉 Note: Input must contain 29 features

---

## 🧪 Example Inputs & Outputs

### ✅ Normal Transaction

**Input:**
```json
{
  "data": [0.1, -1.2, 0.5, 1.3, -0.7, 0.9, -0.2, 0.4, -1.1, 0.3,
           0.8, -0.6, 1.0, -0.9, 0.2, 0.7, -0.3, 0.6, -1.4, 0.1,
           0.5, -0.5, 1.2, -0.4, 0.9, 0.3, -0.2, 0.7, 50.0]
}
```

**Output:**
```json
{
  "prediction": "Normal Transaction ✅"
}
```

---

### 🚨 Fraud Transaction

**Input:**
```json
{
  "data": [-1.27, 2.46, -2.85, 2.32, -1.37,
           -0.94, -3.06, 1.16, -2.26, -4.88,
           2.25, -4.68, 0.65, -6.17, 0.59,
           -4.84, -6.53, -3.11, 1.71, 0.56,
           0.65, -0.08, -0.22, -0.52, 0.22,
           0.75, 0.63, 0.25, 0.01]
}
```

**Output:**
```json
{
  "prediction": "Fraud Transaction 🚨"
}
```
```


---

🖥️ Run Locally

git clone https://github.com/shiva-ml-dev/credit-card-fraud-detection.git
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

## 🙌 Author

Shiva  
Machine Learning Engineer (Aspiring) 🚀

---

🖥️ Run Locally

git clone https://github.com/shiva-ml-dev/credit-card-fraud-detection.git
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

## 🙌 Author

Shiva  
Machine Learning Engineer (Aspiring) 🚀
