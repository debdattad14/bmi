
import streamlit as st

import streamlit as st

st.title("BMI Calculator")

# Dropdown to select height unit
height_unit = st.selectbox("Select your height unit:", ["Meters", "Centimeters", "Feet", "Inches"])

# Inputs
h = st.number_input(f"Enter the height (in {height_unit}):", format="%.2f")
w = st.number_input("Enter the weight (in kg):", format="%.2f")

# Button to calculate
if st.button("Calculate BMI"):
    if h > 0:
        # Convert the height to meters based on the selected unit
        if height_unit == "Meters":
            h_meters = h
        elif height_unit == "Centimeters":
            h_meters = h / 100
        elif height_unit == "Feet":
            h_meters = h * 0.3048
        elif height_unit == "Inches":
            h_meters = h * 0.0254

        # Calculate BMI using the converted height
        bmi = w / pow(h_meters, 2)

        # Display the result rounded to 2 decimal places
        st.write(f"**Your BMI is:** {bmi:.2f}")
    else:
        st.error("Height must be greater than zero to calculate BMI.")