# 🚨 PhishNet-AI: AI-Based Phishing URL Detection System

PhishNet-AI is an end-to-end phishing URL detection system using Machine Learning. It combines Python ML (XGBoost), Flask, Node.js, and React to detect phishing URLs in real-time with a user-friendly UI and a powerful backend.

---

## 🧠 Features

- 🔍 Real-time Phishing URL Prediction
- 🧠 ML Model (XGBoost) trained in Jupyter Notebook
- 🛠️ Flask API for ML integration
- 🌐 Node.js + Express backend
- 🎯 React frontend with a smooth interface
- 💾 Git LFS support for large datasets
- 🧹 Processed & cleaned data from OpenPhish, Alexa Top 1M, Kaggle

---

## 💻 Tech Stack

| Layer         | Technology            |
|---------------|------------------------|
| Frontend      | React.js               |
| Backend       | Node.js + Express      |
| ML API        | Flask (Python)         |
| ML Model      | XGBoost (trained in Jupyter) |
| Dataset       | Kaggle, Alexa Top 1M, OpenPhish |
| Version Ctrl  | Git & Git LFS          |

---

## 📁 Dataset Sources

- [Kaggle Phishing Dataset](https://www.kaggle.com/)
- [OpenPhish Feeds](https://openphish.com/)

The datasets were merged, cleaned, and feature engineered to train a high-accuracy XGBoost model.

---

## ⚙️ System Architecture

1. User enters a URL on the **React UI**
2. Request is sent to **Node.js backend**
3. Backend forwards it to the **Flask API**
4. Flask returns **ML model prediction**
5. Prediction is displayed back to the user

---

## 🧪 ML Model Training

- Environment: Python + Jupyter Notebook
- Model: XGBoost
- Preprocessing: URL-based features (length, special chars, domain age, etc.)
- Evaluation: Accuracy, Precision, Recall, Confusion Matrix

---

