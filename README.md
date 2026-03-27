# 💳 Credit Card Fraud Detection

An end-to-end machine learning system to detect 
fraudulent credit card transactions using 
Random Forest and Logistic Regression.

## 🚀 Live Demo
👉 [Click here to try the app](https://credit-card-fraud-detection-nh2nruv2xnenz8f6vhdjhn.streamlit.app)

## ✨ Features
- Multiple ML models: Random Forest, Logistic Regression
- SMOTE for handling imbalanced dataset
- Probability-based fraud detection
- FastAPI backend
- Streamlit frontend

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| ML | Scikit-learn, SMOTE |
| Backend | FastAPI |
| Frontend | Streamlit |
| Language | Python |

## ⚙️ How to Run

### Backend
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

### Frontend
```bash
streamlit run streamlit_app.py
```

## 📥 Input & Output
- **Input:** 30 numerical transaction values
- **Output:** Fraud probability + Fraud/Normal label

## 📸 Screenshots
### UI
![UI](ui.png)

### API
![API](api.png)

### Prediction
![Prediction](prediction.png)

## 👤 Author
**Shiva** | [GitHub](https://github.com/shiva-ml-dev)
