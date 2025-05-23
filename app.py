import streamlit as st
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

# Inisialisasi Spark
spark = SparkSession.builder \
    .appName("student-performance") \
    .config("spark.network.timeout", "600s") \
    .getOrCreate()

st.title("Prediksi Status Mahasiswa (Random Forest - Spark)")

# Load model Spark
try:
    # model_dt = PipelineModel.load("model/dt_best_model")
    model_rf = PipelineModel.load("models/my_model")
except Exception as e:
    st.error(f"Model tidak dapat dimuat: {e}")
    st.stop()

# Fitur input (sesuaikan urutan & nama lowercase)
input_fields = [
    'marital_status', 'application_mode', 'application_order', 'course',
    'daytime_evening_attendance', 'previous_qualification', 'previous_qualification_grade',
    'nacionality', 'mothers_qualification', 'fathers_qualification',
    'mothers_occupation', 'fathers_occupation', 'admission_grade', 'displaced',
    'educational_special_needs', 'debtor', 'tuition_fees_up_to_date', 'gender',
    'scholarship_holder', 'age_at_enrollment', 'international',
    'curricular_units_1st_sem_credited', 'curricular_units_1st_sem_enrolled',
    'curricular_units_1st_sem_evaluations', 'curricular_units_1st_sem_approved',
    'curricular_units_1st_sem_grade', 'curricular_units_1st_sem_without_evaluations',
    'curricular_units_2nd_sem_credited', 'curricular_units_2nd_sem_enrolled',
    'curricular_units_2nd_sem_evaluations', 'curricular_units_2nd_sem_approved',
    'curricular_units_2nd_sem_grade', 'curricular_units_2nd_sem_without_evaluations',
    'unemployment_rate', 'inflation_rate', 'gdp'
]

label_mapping = {
    0: "Dropout",
    1: "Enrolled",
    2: "Graduate"
}

# Input user dalam dua kolom
st.subheader("Masukkan Data Mahasiswa:")
input_data = {}

for field in input_fields:
    input_data[field] = st.number_input(f"{field}", value=0.0)


# Konversi ke DataFrame
input_df = pd.DataFrame([input_data])

# Prediksi
if st.button("Prediksi"):
    try:
        # Ubah input ke Spark DataFrame
        input_df = pd.DataFrame([input_data])
        spark_df = spark.createDataFrame(input_df)

        # Prediksi Random Forest
        pred_rf = model_rf.transform(spark_df).select("prediction").collect()[0][0]

        # Mapping label hasil prediksi
        pred_label_rf = label_mapping.get(int(pred_rf), "Tidak diketahui")

        st.success(f"{pred_label_rf}")
    except Exception as e:
        st.error(f"Error prediksi: {e}")