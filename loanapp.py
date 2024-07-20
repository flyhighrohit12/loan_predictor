import streamlit as st
import requests

API_URL = "http://localhost:8005/predict/"

st.title("Personal Loan Prediction Application")

with st.form("prediction_form"):
    st.subheader("Enter your details:")
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=5)
    income = st.number_input("Annual Income (in thousands)", min_value=0, max_value=1000, value=50)
    family = st.number_input("Family size", min_value=1, max_value=10, value=3)
    ccavg = st.number_input("Average Credit Card Spending (in thousands)", min_value=0.0, max_value=20.0, step=0.1, value=1.5)
    education = st.selectbox("Education Level", options=[1, 2, 3], format_func=lambda x: {1: "Undergrad", 2: "Graduate", 3: "Professional"}[x])
    mortgage = st.number_input("Mortgage Value (in thousands)", min_value=0, max_value=1000, value=0)
    securities_account = st.radio("Do you have a securities account?", options=(1, 0), format_func=lambda x: "Yes" if x == 1 else "No")
    cd_account = st.radio("Do you have a CD account?", options=(1, 0), format_func=lambda x: "Yes" if x == 1 else "No")
    online = st.radio("Do you use online banking?", options=(1, 0), format_func=lambda x: "Yes" if x == 1 else "No")
    creditcard = st.radio("Do you have a credit card issued by the bank?", options=(1, 0), format_func=lambda x: "Yes" if x == 1 else "No")
    model_type = st.selectbox("Choose the prediction model", options=["svm", "logistic_regression", "random_forest"])
    submit_button = st.form_submit_button("Predict")

if submit_button:
    data = {
        "data": {
            "age": age,
            "experience": experience,
            "income": income,
            "family": family,
            "ccavg": ccavg,
            "education": education,
            "mortgage": mortgage,
            "securities_account": securities_account,
            "cd_account": cd_account,
            "online": online,
            "creditcard": creditcard
        },
        "model_type": model_type
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"Loan Prediction: {prediction}")
    else:
        st.error(f"Error in API call: {response.status_code}, {response.text}")

