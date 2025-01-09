import streamlit as st
import joblib
import numpy as np
import bz2file as bz2

def decompress_joblib(file):
    data = bz2.BZ2File(file, 'rb')
    data = joblib.load(data)
    return data

# Load your trained model
model = decompress_joblib('random_forest_model.pkl.pbz2')

st.markdown("""
    <style>
    /* Set the background for the entire Streamlit app */
    .stApp {
        background-color: #ffd6a5 !important; /* Warm peach background */
        font-family: Arial, sans-serif;
    }

    /* Remove padding and margins at the top */
    header {
        visibility: hidden; /* Hide the header if any */
    }
    .block-container {
        padding-top: 0 !important; /* Remove padding above the content */
        margin-top: 0 !important;
    }

    .container {
        max-width: 400px;
        margin: 50px auto;
        background: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .title {
        text-align: center;
        font-weight: bold;
        font-size: 24px;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 20px;
    }

    label {
        display: block;
        margin-top: 10px;
        font-weight: bold;
    }

    input {
        width: 100%;
        padding: 8px;
        margin-top: 5px;
        margin-bottom: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
    }

    .button {
        background-color: #f08080;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px;
        width: 100%;
        cursor: pointer;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
    }

    .button:hover {
        background-color: #e57373;
    }

    .result {
        margin-top: 20px;
        font-size: 1.2em;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="container">', unsafe_allow_html=True)
# Title and subtitle
st.markdown('<div class="title">Air Prediction Level</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">WQD7006</div>', unsafe_allow_html=True)

# Form for input
with st.form("aqi_form"):
    PM25 = st.number_input("PM2.5 (µg/m³):", min_value=0.0, step=0.1)
    Wind_Direction = st.number_input("Wind Direction (°):", min_value=0.0, step=0.1)
    O3 = st.number_input("O3 (ppm):", min_value=0.0, step=0.01)
    PM10 = st.number_input("PM10 (µg/m³):", min_value=0.0, step=0.1)
    CO = st.number_input("CO (ppm):", min_value=0.0, step=0.01)
    Relative_Humidity = st.number_input("Relative Humidity (%):", min_value=0.0, max_value=100.0, step=0.1)
    Wind_Speed = st.number_input("Wind Speed (m/s):", min_value=0.0, step=0.1)
    Ambient_Temperature = st.number_input("Ambient Temperature (°C):", min_value=-30.0, step=0.1)
    NO2 = st.number_input("NO2 (ppm):", min_value=0.0, step=0.01)
    SO2 = st.number_input("SO2 (ppm):", min_value=0.0, step=0.01)

    # Submit button
    submitted = st.form_submit_button("Calculate AQI")
    if submitted:
        features = np.array([[PM25, Wind_Direction, O3, PM10, CO, Relative_Humidity, Wind_Speed, Ambient_Temperature, NO2, SO2]])
        predicted_aqi = model.predict(features)[0]

        # Determine AQI level
        if predicted_aqi <= 50:
            aqi_level = "Good"
        elif predicted_aqi <= 100:
            aqi_level = "Moderate"
        elif predicted_aqi <= 150:
            aqi_level = "Unhealthy for Sensitive Groups"
        elif predicted_aqi <= 200:
            aqi_level = "Unhealthy"
        elif predicted_aqi <= 300:
            aqi_level = "Very Unhealthy"
        else:
            aqi_level = "Hazardous"

        # Display results
        st.markdown(f'<div class="result"><strong>Predicted AQI:</strong> {predicted_aqi:.2f}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result"><strong>AQI Level:</strong> {aqi_level}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
