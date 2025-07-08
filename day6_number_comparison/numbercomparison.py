import streamlit as st

# Title
st.title("🔢 Number Comparison")

# Inputs
num1 = st.number_input("Enter the first number", format="%f", key="num1")
num2 = st.number_input("Enter the second number", format="%f", key="num2")

# Button to compare
if st.button("Compare"):
    if num1 > num2:
        st.success(f"{num1} is larger than {num2}.")
    elif num1 < num2:
        st.info(f"{num1} is smaller than {num2}.")
    else:
        st.warning("Both numbers are equal.")
