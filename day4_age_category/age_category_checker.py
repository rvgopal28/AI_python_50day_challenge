# age_category_checker.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the page
st.set_page_config(page_title="👥 Age Classifier", layout="centered")
st.title("👥 Group Age Classifier")
st.write("Enter ages of multiple people to classify their life stages.")

# --- Classifier function ---
def classify_age(age):
    if age < 0:
        return "Invalid"
    elif age <= 12:
        return "Child 👶"
    elif age <= 19:
        return "Teenager 🧒"
    elif age <= 59:
        return "Adult 🧑"
    else:
        return "Senior 🧓"

# --- Input section ---
st.subheader("📋 Enter Ages")

ages_input = st.text_area("Enter ages separated by commas (e.g., 10, 25, 70)", placeholder="10, 12, 45, 67")

if st.button("Classify Group"):
    try:
        # Convert input string to list of integers
        age_list = [int(age.strip()) for age in ages_input.split(",") if age.strip().isdigit()]

        if not age_list:
            st.warning("⚠️ Please enter at least one valid age.")
        else:
            # Classify each age
            classifications = [classify_age(age) for age in age_list]

            # Create a DataFrame
            df = pd.DataFrame({
                "Age": age_list,
                "Category": classifications
            })

            st.success("✅ Classification Completed")
            st.dataframe(df)

            # Count categories
            category_counts = df["Category"].value_counts()

            # Plot a pie chart
            fig, ax = plt.subplots()
            ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
            ax.axis("equal")
            st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
