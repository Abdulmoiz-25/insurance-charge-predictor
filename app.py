import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Insurance Charges Predictor", page_icon="💰")

@st.cache_resource
def load_model():
    return joblib.load('insurance_model.pkl')

model = load_model()

st.title("💰 Insurance Charges Prediction App")

# Sidebar Inputs
st.sidebar.header("Enter Input Features")
age = st.sidebar.slider("Age", 18, 100, 30)
bmi = st.sidebar.slider("BMI", 10.0, 50.0, 25.0)
children = st.sidebar.selectbox("Number of Children", [0, 1, 2, 3, 4, 5])
sex = st.sidebar.selectbox("Sex", ["male", "female"])
smoker = st.sidebar.selectbox("Smoker", ["yes", "no"])
region = st.sidebar.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Preprocessing
sex_male = 1 if sex == "male" else 0
smoker_yes = 1 if smoker == "yes" else 0
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

features = np.array([[age, bmi, children, sex_male, smoker_yes, region_northwest, region_southeast, region_southwest]])

# Prediction Button
st.markdown("### Click Below to Predict")
if st.button("🔮 Predict Insurance Charges"):
    prediction = model.predict(features)
    st.markdown(f"<h3 style='text-align: center;'>💸 Estimated Charges: <span style='color: green;'>${prediction[0]:,.2f}</span></h3>", unsafe_allow_html=True)
