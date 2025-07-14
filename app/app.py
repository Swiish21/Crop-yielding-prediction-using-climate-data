import streamlit as st
import joblib
import numpy as np

st.title('Crop Yield Predictor')

model = joblib.load('models/crop_yield_model.pkl')

rainfall = st.number_input('Enter Rainfall (mm)', 50, 500, 120)
temperature = st.number_input('Enter Temperature (°C)', 10, 40, 25)
humidity = st.number_input('Enter Humidity (%)', 30, 90, 60)
crop_type = st.selectbox('Select Crop Type', ['Wheat', 'Rice', 'Maize'])

crop_features = [1 if crop_type == ct else 0 for ct in ['Wheat', 'Rice']] #Maize is the baseline

features = np.array([[rainfall, temperature, humidity] + crop_features])
prediction = model.predict(features)[0]

st.write(f'Predicted Yield: **{prediction:.2f} tons/hectare**')