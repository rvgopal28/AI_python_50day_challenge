import streamlit as st
import re

st.set_page_config(page_title="📱 Phone Number Formatter", layout="centered")
st.title("📱 Phone Number Formatter")

st.markdown("Enter a 10-digit number, and I'll format it as **(XXX) XXX-XXXX**")

# Input Field
phone_input = st.text_input("Enter 10-digit Phone Number:")

def format_phone_number(number):
    cleaned = re.sub(r'\D', '', number)  # Remove non-digit characters
    if len(cleaned) == 10:
        return f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"
    else:
        return None

if phone_input:
    formatted = format_phone_number(phone_input)
    if formatted:
        st.success(f"📞 Formatted Number: {formatted}")
    else:
        st.error("❌ Please enter a valid 10-digit phone number.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")