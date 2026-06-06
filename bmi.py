
import streamlit as st

st.title("BMI Calculator")

# Inputs
h = st.number_input("Enter the height:", format="%.2f")
w = st.number_input("Enter the weight:", format="%.2f")

# Button to calculate
if st.button("Calculate BMI"):
    bmi = w / pow(h, 2)
    st.write("BMI:", bmi)