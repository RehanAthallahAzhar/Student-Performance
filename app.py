import streamlit as st
import pandas as pd
import joblib
from sklearn.decomposition import PCA
import numpy as np

# Load model, label encoder, dan PCA components
try:
    model = joblib.load("models/rf_best_model.pkl") 
    label_encoder = joblib.load("models/label_encoder.pkl")
    pca = joblib.load("models/pca_model.pkl")  # Asumsi Anda sudah menyimpan model PCA
except Exception as e:
    st.error(f"Model tidak dapat dimuat: {e}")
    st.stop()

st.title("Prediksi Status Mahasiswa (Random Forest - Scikit-Learn)")

# Input features for PCA (17 numeric features)
pca_features = [
    'application_order', 'previous_qualification_grade', 'admission_grade',
    'age_at_enrollment', 'curricular_units_1st_sem_credited',
    'curricular_units_1st_sem_enrolled', 'curricular_units_1st_sem_evaluations',
    'curricular_units_1st_sem_approved', 'curricular_units_1st_sem_grade',
    'curricular_units_1st_sem_without_evaluations', 'curricular_units_2nd_sem_credited',
    'curricular_units_2nd_sem_enrolled', 'curricular_units_2nd_sem_evaluations',
    'curricular_units_2nd_sem_approved', 'curricular_units_2nd_sem_grade',
    'curricular_units_2nd_sem_without_evaluations', 'gdp'
]

# categorical features (doesnt use in PCA)
categorical_features = [
    'marital_status', 'application_mode', 'course', 'daytime_evening_attendance',
    'previous_qualification', 'nacionality', 'mothers_qualification',
    'fathers_qualification', 'mothers_occupation', 'fathers_occupation',
    'displaced', 'educational_special_needs', 'debtor', 'tuition_fees_up_to_date',
    'gender', 'scholarship_holder', 'international', 'unemployment_rate',
    'inflation_rate'
]

col1, col2 = st.columns(2)
input_data = {}

# Input PCA feature
for i, field in enumerate(pca_features):
    target_col = col1 if i % 2 == 0 else col2
    input_data[field] = target_col.number_input(field, value=0.0)

# Input untuk fitur kategorikal
for i, field in enumerate(categorical_features):
    target_col = col1 if i % 2 == 0 else col2
    input_data[field] = target_col.number_input(field, value=0)

# Prediksi
if st.button("Prediksi"):
    try:
        input_df = pd.DataFrame([input_data])
        
        # Retrieve only numeric features according to the training pipeline
        pca_input = input_df[pca_features] 
        
        # Direct prediction with pipeline (pipeline: scaler + pca + rf)
        prediction = model.predict(pca_input)[0]
        

        st.write(f"Hasil Prediksi: {prediction}")


    except Exception as e:
        st.error(f"Terjadi kesalahan saat prediksi: {e}")