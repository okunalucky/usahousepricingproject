# Import All Necessary Libraries
import joblib # type: ignore
import streamlit as st # type: ignore
import warnings
warnings.filterwarnings("ignore")
# Uploading the model
model = joblib.load("model.joblib") 
st.header("house price predictor")
col1, col2, col3, col4 = st.columns(4)
with col1:
    Avg. Area Income= st.number_input("Avg. Area Income", min_value = 17796.631190, max_value = 107701.748378) # type: ignore

with col2:
    Avg. Area House Age= st.number_input("Avg. Area House Age", min_value = 2.644304	, max_value = 9.519088) # type: ignore

with col3:
    Avg. Area Number of Rooms	= st.number_input("Avg. Area Number of Rooms", min_value = 3.236194, max_value = 10.759588) # type: ignore
 
with col4:    
    Area Population= st.number_input("Area Population", min_value = 172.610686, max_value = 69621.713378)      # type: ignore
   
if st.button("Prediction"):
    predict = model.predict([[avg_area_income, avg_area_house_age, avg_area_number_of_rooms, area_population]])# type: ignore
    st.write("Price of the House: ", predict[0])
    

