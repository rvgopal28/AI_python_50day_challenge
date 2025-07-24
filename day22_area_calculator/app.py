import streamlit as st
import math

st.set_page_config(page_title="🧮 Area Calculator", layout="centered")
st.title("🧮 Area Calculator Functions")

tab1, tab2, tab3 = st.tabs(["Circle", "Rectangle", "Triangle"])

# --- Circle Area ---
with tab1:
    st.header("🔵 Area of Circle")
    radius = st.number_input("Enter radius (r):", min_value=0.0, step=0.1)
    if st.button("Calculate Circle Area"):
        area_circle = math.pi * radius * radius
        st.success(f"Area of Circle: {area_circle:.2f}")

# --- Rectangle Area ---
with tab2:
    st.header("⬛ Area of Rectangle")
    length = st.number_input("Enter length (l):", min_value=0.0, step=0.1, key="length")
    width = st.number_input("Enter width (w):", min_value=0.0, step=0.1, key="width")
    if st.button("Calculate Rectangle Area"):
        area_rectangle = length * width
        st.success(f"Area of Rectangle: {area_rectangle:.2f}")

# --- Triangle Area ---
with tab3:
    st.header("🔺 Area of Triangle")
    base = st.number_input("Enter base (b):", min_value=0.0, step=0.1, key="base")
    height = st.number_input("Enter height (h):", min_value=0.0, step=0.1, key="height")
    if st.button("Calculate Triangle Area"):
        area_triangle = 0.5 * base * height
        st.success(f"Area of Triangle: {area_triangle:.2f}")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
