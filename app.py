import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Financial Fraud Analytics System",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

div[data-testid="metric-container"] {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #333333;
}

.stDataFrame {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOGIN SYSTEM
# ---------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():

    st.title("🔐 Financial Fraud Analytics Login")

    st.markdown(
        "### Secure FinTech Monitoring Platform"
    )

    st.markdown("---")

    # Demo Credentials
    st.info(
        """
        Demo Login Credentials
        
        Username: admin
        Password: admin123
        """
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    login_button = st.button("Login")

    if login_button:

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True

            st.success("✅ Login Successful!")

            st.rerun()

        else:

            st.error(
                "❌ Invalid Username or Password"
            )

# Show Login Page First
if not st.session_state.logged_in:

    login()

    st.stop()

# ---------------------------------------------------
# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = pd.read_csv("transactions.csv")

df["transaction_time"] = pd.to_datetime(
    df["transaction_time"],
    dayfirst=True
)

# ---------------------------------------------------
# FRAUD DETECTION LOGIC
# ---------------------------------------------------

def detect_fraud(row):

    risk_score = 0

    # Rule 1 - Very High Amount
    if row["transaction_amount"] > 80000:
        risk_score += 50

    # Rule 2 - Credit Card High Transaction
    if (
        row["payment_method"] == "Credit Card"
        and row["transaction_amount"] > 50000
    ):
        risk_score += 30

    # Rule 3 - Web Transactions
    if row["device_type"] == "Web":
        risk_score += 20

    # Rule 4 - Suspicious Location
    if row["location"] not in ["Bangalore", "Mysore"]:
        risk_score += 10

    # Rule 5 - Late Night Transactions
    hour = row["transaction_time"].hour

    if hour >= 1 and hour <= 4:
        risk_score += 20

    # Final Fraud Decision
    if risk_score >= 60:
        fraud_status = "Fraud"
    else:
        fraud_status = "Safe"

    return pd.Series([risk_score, fraud_status])

# Apply Fraud Detection
df[["risk_score", "fraud_status"]] = df.apply(
    detect_fraud,
    axis=1
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("💳 Fraud Analytics")

logout = st.sidebar.button("🚪 Logout")

if logout:

    st.session_state.logged_in = False

    st.rerun()

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
    "Dashboard",
    "Fraud Analysis",
    "Transaction Explorer"
]
)

payment_filter = st.sidebar.multiselect(
    "Select Payment Method",
    options=df["payment_method"].unique(),
    default=df["payment_method"].unique()
)

location_filter = st.sidebar.multiselect(
    "Select Location",
    options=df["location"].unique(),
    default=df["location"].unique()
)

# ---------------------------------------------------
# APPLY FILTERS
# ---------------------------------------------------

filtered_df = df[
    (df["payment_method"].isin(payment_filter)) &
    (df["location"].isin(location_filter))
]

# ---------------------------------------------------
# SEARCH BAR
# ---------------------------------------------------

search_term = st.sidebar.text_input(
    "🔍 Search Transactions"
)

if search_term:

    filtered_df = filtered_df[
        filtered_df["transaction_id"].astype(str).str.contains(search_term, case=False) |

        filtered_df["customer_name"].astype(str).str.contains(search_term, case=False) |

        filtered_df["mobile_number"].astype(str).str.contains(search_term, case=False)
    ]

# ---------------------------------------------------
# DASHBOARD PAGE
# ---------------------------------------------------

if page == "Dashboard":

    st.title("💳 Financial Fraud Analytics System")

    st.markdown(
        "### AI-Assisted FinTech Fraud Detection & Risk Analysis Platform"
    )

    st.markdown("---")

    # KPI Metrics

    total_transactions = len(filtered_df)

    fraud_cases = len(
        filtered_df[filtered_df["fraud_status"] == "Fraud"]
    )

    safe_cases = len(
        filtered_df[filtered_df["fraud_status"] == "Safe"]
    )

    fraud_percentage = (
        fraud_cases / total_transactions
    ) * 100

    high_risk = len(
        filtered_df[filtered_df["risk_score"] >= 60]
    )

    # KPI CARDS

    st.subheader("📊 Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Transactions",
        total_transactions
    )

    col2.metric(
        "Fraud Cases",
        fraud_cases
    )

    col3.metric(
        "High Risk Alerts",
        high_risk
    )

    col4.metric(
        "Fraud Percentage",
        f"{fraud_percentage:.2f}%"
    )

    st.markdown("---")

    # Charts

    col1, col2 = st.columns(2)

    with col1:

        fraud_chart = px.pie(
            filtered_df,
            names="fraud_status",
            title="Fraud vs Safe Transactions"
        )

        st.plotly_chart(
            fraud_chart,
            use_container_width=True
        )

    with col2:

        payment_chart = px.bar(
            filtered_df,
            x="payment_method",
            title="Transactions by Payment Method",
            color="payment_method"
        )

        st.plotly_chart(
            payment_chart,
            use_container_width=True
        )

    # Transaction Trend

    st.subheader("📈 Transaction Amount Trend")

    trend_chart = px.line(
        filtered_df.head(200),
        y="transaction_amount",
        title="Transaction Trend Analysis"
    )

    st.plotly_chart(
        trend_chart,
        use_container_width=True
    )

    # Location Analysis

    st.subheader("🌍 Fraud Analysis by Location")

    location_chart = px.histogram(
        filtered_df,
        x="location",
        color="fraud_status",
        title="Location-wise Fraud Distribution"
    )

    st.plotly_chart(
        location_chart,
        use_container_width=True
    )

# ---------------------------------------------------
# ADD TRANSACTION PAGE
# ---------------------------------------------------

# ---------------------------------------------------
# FRAUD ANALYSIS PAGE
# ---------------------------------------------------

elif page == "Fraud Analysis":

    st.title("🚨 Fraud Analysis")

    st.markdown("---")

    high_risk_df = filtered_df[
        filtered_df["risk_score"] >= 60
    ]

    st.subheader("High Risk Transactions")

    st.dataframe(
        high_risk_df,
        use_container_width=True
    )

    st.subheader("Fraud Distribution")

    fraud_location_chart = px.histogram(
        high_risk_df,
        x="location",
        color="payment_method",
        title="Fraud Transactions by Location"
    )

    st.plotly_chart(
        fraud_location_chart,
        use_container_width=True
    )

# ---------------------------------------------------
# TRANSACTION EXPLORER PAGE
# ---------------------------------------------------

elif page == "Transaction Explorer":

    st.title("📋 Transaction Explorer")

    st.markdown("---")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    csv = filtered_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Transaction Report",
        data=csv,
        file_name="fraud_analytics_report.csv",
        mime="text/csv"
    )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.success(
    "✅ Financial Fraud Analytics System Running Successfully!"
)