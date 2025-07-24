import streamlit as st
import re
import pandas as pd

st.set_page_config(page_title="📱 Phone Tools Suite", layout="centered")
st.title("📱 Phone Tools Suite")

tab1, tab2, tab3 = st.tabs(["Formatter", "Validator", "Country Code Detector"])

# --- Formatter Tab ---
with tab1:
    st.header("📞 Phone Number Formatter")
    phone_input = st.text_input("Enter 10-digit Phone Number:")

    def format_phone_number(number):
        cleaned = re.sub(r'\D', '', number)
        if len(cleaned) == 10:
            return f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"
        else:
            return None

    if phone_input:
        formatted = format_phone_number(phone_input)
        if formatted:
            st.success(f"Formatted Number: {formatted}")
        else:
            st.error("Invalid 10-digit phone number.")

# --- Validator Tab ---
with tab2:
    st.header("✔️ Phone Number Validator")
    validator_input = st.text_input("Enter Phone Number to Validate:")

    def is_valid_number(number):
        cleaned = re.sub(r'\D', '', number)
        return len(cleaned) == 10 and cleaned.isdigit()

    if validator_input:
        if is_valid_number(validator_input):
            st.success("✅ Valid 10-digit phone number!")
        else:
            st.error("❌ Invalid phone number.")

# --- Country Code Detector Tab ---
with tab3:
    st.header("🌍 Country Code Detector")
    country_input = st.text_input("Enter Full Phone Number (with country code):")

    country_codes = {
        "91": "India",
        "1": "USA/Canada",
        "44": "United Kingdom",
        "61": "Australia",
        "81": "Japan",
        "49": "Germany",
        "33": "France"
    }

    def detect_country(number):
        cleaned = re.sub(r'\D', '', number)
        for code in sorted(country_codes.keys(), key=lambda x: -len(x)):
            if cleaned.startswith(code):
                return country_codes[code]
        return "Unknown Country Code"

    if country_input:
        country = detect_country(country_input)
        st.info(f"🌐 Detected Country: {country}")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
