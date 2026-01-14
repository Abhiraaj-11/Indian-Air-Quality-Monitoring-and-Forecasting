import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# AQI Category Function
def aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Poor"
    elif aqi <= 300:
        return "Unhealthy"
    else:
        return "Hazardous"

# Health Advice Function
def health_advice(category):
    advice = {
        "Good": "Air quality is satisfactory. Enjoy outdoor activities.",
        "Moderate": "Sensitive individuals should limit prolonged outdoor exertion.",
        "Poor": "Avoid prolonged outdoor activities.",
        "Unhealthy": "Wear masks and avoid going outside.",
        "Hazardous": "Stay indoors and seek medical assistance."
    }
    return advice[category]

# App UI
st.set_page_config(page_title="AQI Prediction App", layout="centered")

st.title("🌍 Air Quality Index Prediction System")
st.markdown("Predict AQI based on air pollutant concentrations")

# User Inputs
so2 = st.number_input("SO₂ concentration", min_value=0.0)
no2 = st.number_input("NO₂ concentration", min_value=0.0)
rspm = st.number_input("RSPM concentration", min_value=0.0)
spm = st.number_input("SPM concentration", min_value=0.0)
pm25 = st.number_input("PM2.5 concentration", min_value=0.0)

# Prediction
if st.button("Predict AQI"):
    features = np.array([[so2, no2, rspm, spm, pm25]])
    prediction = model.predict(features)[0]

    category = aqi_category(prediction)
    advice = health_advice(category)

    st.success(f"📊 Predicted AQI: {int(prediction)}")
    st.info(f"🌫 Air Quality Category: {category}")
    st.warning(f"🩺 Health Advice: {advice}")
