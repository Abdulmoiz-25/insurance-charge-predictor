import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('insurance_model.pkl')

# App title
st.title("💰 Insurance Charges Prediction App")

# Input fields
age = st.slider("Age", 18, 100, 30)
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
children = st.selectbox("Number of Children", [0, 1, 2, 3, 4, 5])
sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Preprocessing
sex_male = 1 if sex == "male" else 0
smoker_yes = 1 if smoker == "yes" else 0
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# Create input array
features = np.array([[age, bmi, children, sex_male, smoker_yes, region_northwest, region_southeast, region_southwest]])

# Predict
if st.button("Predict Charges"):
    prediction = model.predict(features)
    st.success(f"Estimated Insurance Charges: ${prediction[0]:,.2f}")
