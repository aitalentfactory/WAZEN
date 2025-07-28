
## Wazen - Smart Application for Expense Classifier and Analyzer & Help Family Members Achieve Financial Goals

Wazen is an AI-powered expense classification and analytics backend that empowers individuals to track their spending intelligently, categorize transactions automatically using machine learning, and visualize patterns to make informed financial decisions.

This repository provides the backend and data science pipeline for the "Wazen" application — including data preparation, model training, and integration with a mobile interface via API or Postman.

---

## 🌟 Key Features

- ✅ Automatic categorization of transactions (shopping, food, entertainment, services, etc.)
- 📊 Smart expense analysis with category-based summaries
- 📦 Python + scikit-learn + FastAPI backend
- 🔌 Connects to PostgreSQL database (cloud or local)
- 🔍 Pre-trained model on `credit_card_transactions` dataset
- 🧪 Evaluation on real-like Saudi-based generated transaction data

---

## 🧠 How it Works

1. **Data Preprocessing:**
   - Cleans transaction descriptions
   - Converts text into numerical features using TF-IDF
   - Maps categories with `LabelEncoder`

2. **Model Training:**
   - Trains Logistic Regression on `credit_card_transactions`
   - Evaluates using accuracy and F1-score

3. **Prediction:**
   - Accepts transaction descriptions via API or test file
   - Predicts and returns the category

4. **Deployment & Testing:**
   - Tested with FastAPI and Postman
   - Supports integration with mobile apps like the Wazen UI

---


## 📊 Datasets

- `credit_card_transactions.csv` – used for training
- `saudi_transactions_100k.csv` – used for testing
- `classified_saudi_transactions.csv` – output with predicted categories

---

## 📱 Frontend

Mobile UI developed in Xcode (Swift) by students team.

---

## 🤝 Contributors

- Dr. Lubna Abdelkareim Gabralla – Project Lead-Backend - MachineLearning
- PNU Students Team – Frontend 



