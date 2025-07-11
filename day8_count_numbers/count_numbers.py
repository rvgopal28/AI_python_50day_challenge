import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🔢 Count Positive, Negative, and Zero Numbers")

st.markdown("""
Enter numbers separated by commas **OR** upload a CSV/TXT file with one number per line or column.
""")

# Option 1: Text input
user_input = st.text_area("Enter numbers (comma separated):", height=100)

# Option 2: File upload
uploaded_file = st.file_uploader("OR Upload a file (.csv or .txt)", type=["csv", "txt"])

# Extract numbers
number_list = []

def extract_numbers_from_text(text):
    try:
        return [float(num.strip()) for num in text.split(",") if num.strip() != ""]
    except ValueError:
        return None

def extract_numbers_from_file(file):
    try:
        df = pd.read_csv(file, header=None)
        flat_list = df.values.flatten()
        return [float(x) for x in flat_list if str(x).strip() != ""]
    except Exception:
        return None

# Process input
if st.button("Count"):
    if uploaded_file:
        number_list = extract_numbers_from_file(uploaded_file)
    elif user_input:
        number_list = extract_numbers_from_text(user_input)
    else:
        st.warning("Please enter numbers or upload a file.")

    if number_list is None:
        st.error("⚠️ Invalid input! Please make sure only numbers are entered.")
    elif len(number_list) == 0:
        st.warning("No numbers found.")
    else:
        # Count
        positives = sum(1 for n in number_list if n > 0)
        negatives = sum(1 for n in number_list if n < 0)
        zeros = sum(1 for n in number_list if n == 0)

        # Display results
        st.success(f"✅ Positive numbers: {positives}")
        st.error(f"❌ Negative numbers: {negatives}")
        st.info(f"🟡 Zeros: {zeros}")
        st.markdown(f"**Total numbers entered:** {len(number_list)}")

        # Bar chart
        st.markdown("### 📊 Visual Summary:")
        chart_data = pd.DataFrame({
            'Category': ['Positive', 'Negative', 'Zero'],
            'Count': [positives, negatives, zeros]
        })
        st.bar_chart(chart_data.set_index('Category'))
