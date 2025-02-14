import streamlit as st # type: ignore
import joblib # type: ignore
import time

model = joblib.load("model.joblib")

# Input
st.title("HOUSE PRICE PREDICTION")
avg_area_income = st.number_input("Avg. Area Income", min_value=17780, max_value=110000)# type: ignore
avg_area_house_age= st.number_input("Avg. Area House Age", min_value= 3, max_value= 10)# type: ignore
avg_area_number_of_rooms = st.number_input("Avg. Area Number of Rooms", min_value= 4, max_value= 11)# type: ignore
area_population = st.number_input("Area Population", min_value= 175, max_value= 70000)# type: ignore

# Output
if st.button("Predict"):
    result = model.predict([[avg_area_income, avg_area_house_age, avg_area_number_of_rooms, area_population]])# type: ignore
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
        time.sleep(0.01)
    st.success(result[0])

