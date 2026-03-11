import streamlit as st

st.set_page_config(page_title="AI Investment Advisor", layout="centered")

st.title("💰 AI Risk-Based Investment Advisor")

st.write(
    "This AI-based fintech app suggests investment options based on your risk tolerance and financial profile."
)

# User Inputs
st.header("User Financial Information")

age = st.number_input("Enter your Age", min_value=18, max_value=70)
income = st.number_input("Monthly Income (₹)", min_value=0)
savings = st.number_input("Monthly Savings (₹)", min_value=0)

# Risk Questions
st.header("Risk Assessment Questionnaire")

horizon = st.selectbox(
    "Investment Horizon",
    ["Less than 2 years", "3–5 years", "More than 5 years"]
)

reaction = st.selectbox(
    "If your investment drops 20%, what will you do?",
    ["Sell immediately", "Wait for recovery", "Invest more"]
)

experience = st.selectbox(
    "Investment Experience",
    ["Beginner", "Moderate", "Experienced"]
)

# Button
if st.button("Get Investment Recommendation"):

    risk_score = 0

    # Horizon scoring
    if horizon == "More than 5 years":
        risk_score += 3
    elif horizon == "3–5 years":
        risk_score += 2
    else:
        risk_score += 1

    # Reaction scoring
    if reaction == "Invest more":
        risk_score += 3
    elif reaction == "Wait for recovery":
        risk_score += 2
    else:
        risk_score += 1

    # Experience scoring
    if experience == "Experienced":
        risk_score += 3
    elif experience == "Moderate":
        risk_score += 2
    else:
        risk_score += 1

    # Risk category
    if risk_score <= 4:
        investor_type = "Low Risk Investor"
        investments = [
            "Fixed Deposits",
            "Government Bonds",
            "Public Provident Fund (PPF)",
            "Debt Mutual Funds"
        ]

    elif risk_score <= 6:
        investor_type = "Moderate Risk Investor"
        investments = [
            "Index Mutual Funds",
            "Hybrid Mutual Funds",
            "Exchange Traded Funds (ETFs)",
            "Corporate Bonds"
        ]

    else:
        investor_type = "High Risk Investor"
        investments = [
            "Stocks",
            "Equity Mutual Funds",
            "Sectoral Funds",
            "Startup Investments"
        ]

    st.subheader("Investor Profile")
    st.success(investor_type)

    st.subheader("Recommended Investment Options")

    for inv in investments:
        st.write("•", inv)

    future_value = savings * 12 * 10

    st.subheader("Estimated Investment Value in 10 Years")
    st.write(f"₹ {future_value:,}")
