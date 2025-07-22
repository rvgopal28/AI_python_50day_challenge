import streamlit as st
import re
import numpy as np

# -----------------------------
# Helper Functions
# -----------------------------

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def extract_username(email):
    if is_valid_email(email):
        return email.split("@")[0]
    else:
        return None

def extract_domain(email):
    if is_valid_email(email):
        return email.split("@")[1]
    else:
        return None

# -----------------------------
# Streamlit UI
# -----------------------------

st.set_page_config(page_title="Email Username Extractor", page_icon="📧")
st.title("📧 Email Username Extractor")
st.subheader("Get the username and domain from any email address.")

emails_input = st.text_area(
    "Enter email address(es):",
    placeholder="e.g. hello@waffestry.com or multiple separated by commas"
)

if st.button("Extract Username(s)"):
    if not emails_input.strip():
        st.warning("Please enter at least one email address.")
    else:
        emails = [e.strip() for e in emails_input.split(",") if e.strip()]
        result_data = []

        for email in emails:
            username = extract_username(email)
            domain = extract_domain(email)
            if username:
                result_data.append({
                    "Email": email,
                    "Username": username,
                    "Domain": domain,
                    "Length": len(username),
                    "Has Numbers?": any(char.isdigit() for char in username),
                    "Has Special Chars?": any(not char.isalnum() for char in username),
                })
            else:
                result_data.append({
                    "Email": email,
                    "Username": "❌ Invalid email",
                    "Domain": None,
                    "Length": np.nan,  # 👈 Use np.nan instead of string
                    "Has Numbers?": None,
                    "Has Special Chars?": None
                })

        import pandas as pd

        df = pd.DataFrame(result_data)
        df["Length"] = pd.to_numeric(df["Length"], errors='coerce')

        st.markdown("### 🧾 Result")
        st.dataframe(result_data, use_container_width=True)

# Footer
st.markdown("---")
st.caption("Waffestry Classroom Tools • Email Username Extractor • Streamlit Edition")