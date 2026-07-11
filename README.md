# 💳 Financial Fraud Analytics System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Visualization-3F4F75?style=for-the-badge&logo=plotly)
![License](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

A web-based **Financial Fraud Analytics System** built with **Python** and **Streamlit** that analyzes financial transactions using a rule-based risk scoring engine. The application identifies suspicious activities, classifies transactions into **Safe**, **High Risk**, and **Fraud**, and presents insights through interactive dashboards for monitoring and investigation.

---

## 🌐 Live Demo

**Streamlit Application**

🔗 https://financial-fraud-analytics.streamlit.app/

---

# ✨ Features

- 🔐 Secure Login System
- 🧠 Rule-Based Fraud Detection Engine
- 🎯 Risk Score Calculation
- 🚨 Fraud & High-Risk Transaction Detection
- 📊 Interactive Analytics Dashboard
- 📈 Monthly Fraud Trend Analysis
- 🌍 Transaction Distribution by Location
- 🏪 Top Risky Merchants Analysis
- 🔍 Transaction Investigation by Transaction ID
- 📋 Interactive Transaction Explorer
- 📥 Downloadable CSV Reports
- 🎛️ Payment Method & Location Filters

---

# 📸 Application Screenshots

## 🔐 Login

![Login](images/login-page.png)

---

## 📊 Dashboard

![Dashboard Overview](images/dashboard-overview-1.png)

![Dashboard Analytics](images/dashboard-overview-2.png)

---

## 🚨 Fraud Analysis

![Fraud Analysis](images/fraud-analysis.png)

---

## 📋 Transaction Explorer

![Transaction Explorer](images/transaction-explorer.png)

---

## 🔎 Transaction Investigation

![Transaction Investigation](images/transaction-investigation.png)

---

# 🧠 Fraud Detection Logic

Each transaction is evaluated using predefined business rules to calculate a cumulative **Risk Score**.

| Rule | Risk Score |
|------|-----------:|
| Transaction Amount > ₹80,000 | +50 |
| Credit Card Transaction > ₹50,000 | +30 |
| Web-Based Transaction | +20 |
| Transaction Outside Trusted Locations | +10 |
| Late-Night Transaction (1 AM – 4 AM) | +20 |

### Risk Classification

| Risk Score | Status |
|------------|--------|
| 0 – 39 | ✅ Safe |
| 40 – 59 | ⚠️ High Risk |
| 60+ | 🚨 Fraud |

---

# 📊 Dashboard Modules

### 📈 Dashboard
- KPI Overview
- Fraud Percentage
- Average Risk Score Gauge
- Monthly Fraud Trend
- Transactions by Location
- Top Risky Merchants

### 🚨 Fraud Analysis
- High-Risk Transaction Table
- Fraud Hotspots by Location

### 📋 Transaction Explorer
- Searchable Transaction Dataset
- Payment & Location Filters
- CSV Report Download

### 🔎 Transaction Investigation
- Search by Transaction ID
- Detailed Transaction Information

---

# 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Framework | Streamlit |
| Data Processing | Pandas |
| Visualization | Plotly Express, Plotly Graph Objects |
| Database | MySQL |
| Data Generation | Faker |
| Version Control | Git & GitHub |
| Deployment | Streamlit Community Cloud |

---

# 📂 Project Structure

```text
FinancialFraudAnalytics/
│
├── app.py
├── generate_data.py
├── transactions.csv
├── requirements.txt
├── README.md
│
└── images/
    ├── login-page.png
    ├── dashboard-overview-1.png
    ├── dashboard-overview-2.png
    ├── fraud-analysis.png
    ├── transaction-explorer.png
    └── transaction-investigation.png
```

---

# 🚀 Run Locally

### Clone the repository

```bash
git clone https://github.com/ramya-r25/financial-fraud-analytics-system.git
```

### Navigate to the project directory

```bash
cd financial-fraud-analytics-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Launch the application

```bash
streamlit run app.py
```

---

# 💡 Highlights

This project demonstrates practical experience with:

- Data Analysis using Pandas
- Rule-Based Fraud Detection
- Interactive Dashboard Development
- Business Intelligence Visualization
- Streamlit Application Development
- MySQL Integration
- Synthetic Data Generation
- Cloud Deployment
- GitHub Version Control

---

# 🔮 Future Enhancements

- Machine Learning-Based Fraud Prediction
- Real-Time Transaction Monitoring
- Interactive Fraud Heat Maps
- Email & SMS Fraud Alerts
- User Role & Access Management
- REST API Integration
- Advanced Risk Scoring Models

---

# 👩‍💻 Author

**Ramya**

**BCA Student | Data Analytics & Business Intelligence**

Focused on building practical data-driven applications using **Python**, **SQL**, **Power BI**, and **Business Intelligence**, with an interest in **Fraud Analytics** and **Cybersecurity**.

---

## ⭐ If you found this project interesting, consider giving it a star!
