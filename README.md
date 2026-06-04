# 💳 Financial Fraud Analytics System

## 📌 Overview

Financial Fraud Analytics System is a web-based fraud detection and risk analysis platform developed using Python and Streamlit.

The system analyzes financial transactions using rule-based fraud detection logic and classifies transactions as Safe, High Risk, or Fraud. It provides interactive dashboards, fraud hotspot analysis, transaction investigation, and downloadable reports to help monitor suspicious activities.

---

## 🚀 Live Demo

https://financial-fraud-analytics.streamlit.app/

---

## ✨ Features

- Secure Login System
- Rule-Based Fraud Detection Engine
- Risk Score Calculation
- Fraud and High-Risk Transaction Identification
- Interactive Dashboard
- Average Risk Score Gauge
- Monthly Fraud Trend Analysis
- Transaction Distribution by Location
- Fraud Hotspot Analysis
- Top Risky Merchants Analysis
- Transaction Search Functionality
- Transaction Investigation by Transaction ID
- Downloadable CSV Reports
- Interactive Filters for Payment Method and Location

---

## 🛠️ Technology Stack

### Frontend
- Streamlit

### Backend
- Python

### Data Processing
- Pandas

### Data Visualization
- Plotly Express
- Plotly Graph Objects

### Database
- MySQL

### Synthetic Data Generation
- Faker

### Version Control
- GitHub

### Deployment
- Streamlit Community Cloud

---

## 📂 Project Structure

```text
FinancialFraudAnalytics/
│
├── app.py
├── transactions.csv
├── generate_data.py
├── requirements.txt
└── README.md
```

### File Description

| File | Purpose |
|--------|----------|
| app.py | Main Streamlit application |
| transactions.csv | Transaction dataset |
| generate_data.py | Generates realistic transaction data |
| requirements.txt | Required Python libraries |
| README.md | Project documentation |

---

## 🧠 Fraud Detection Rules

The system calculates a risk score based on predefined rules:

| Rule | Risk Score |
|--------|------------|
| Transaction Amount > ₹80,000 | +50 |
| Credit Card Transaction > ₹50,000 | +30 |
| Web-Based Transaction | +20 |
| Suspicious Location | +10 |
| Late Night Transaction (1 AM - 4 AM) | +20 |

### Classification

| Risk Score | Status |
|------------|---------|
| 0 - 39 | Safe |
| 40 - 59 | High Risk |
| 60+ | Fraud |

---

## 📊 Dashboard Modules

### Dashboard
- KPI Metrics
- Fraud Percentage
- Risk Score Gauge
- Monthly Fraud Trends
- Transaction Distribution by Location
- Top Risky Merchants

### Fraud Analysis
- High Risk Transactions
- Fraud Hotspots by Location

### Transaction Explorer
- Full Transaction Dataset
- Report Download Feature

### Transaction Investigation
- Search Transaction by ID
- Detailed Transaction Information

---

## 🎯 Learning Outcomes

Through this project, I gained experience in:

- Data Analysis using Pandas
- Data Visualization using Plotly
- Streamlit Web Application Development
- Fraud Detection Concepts
- Dashboard Design
- MySQL Database Integration
- GitHub Version Control
- Cloud Deployment

---

## 👩‍💻 Author

Ramya

BCA Student

Passionate about Data Analytics, Cybersecurity, and Technology.

---
