import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict

st.set_page_config(page_title="Dynamic Name List App", layout="centered")

st.title("🧑‍🤝‍🧑 Name List & Length Analyzer (Dynamic Version)")

# Step 1: Select how many names to enter
name_count = st.slider("How many names would you like to enter?", 3, 20, 5)

# Step 2: Enter names
st.markdown("### ✍️ Enter Names")
name_inputs = []
for i in range(name_count):
    name = st.text_input(f"Name {i+1}", key=f"name_{i}")
    name_inputs.append(name.strip())

# Optional features
sort_by_length = st.checkbox("Sort names by length (descending)?", value=True)
min_length_filter = st.slider("Filter: Show names with at least this many characters", 0, 20, 0)

# When user clicks submit
if st.button("Analyze"):
    # Remove blanks
    valid_names = [name for name in name_inputs if name != ""]

    if len(valid_names) != name_count:
        st.error("❌ Please fill all name fields.")
    else:
        # Check for duplicates
        duplicates = [name for name in set(valid_names) if valid_names.count(name) > 1]
        if duplicates:
            st.warning(f"⚠️ Duplicate names found: {', '.join(duplicates)}")

        # Compute name lengths
        name_lengths = [(name, len(name)) for name in valid_names if len(name) >= min_length_filter]

        if sort_by_length:
            name_lengths.sort(key=lambda x: x[1], reverse=True)

        # DataFrame for export and charts
        df = pd.DataFrame(name_lengths, columns=["Name", "Length"])

        # Group by initial
        grouped = defaultdict(list)
        for name, length in name_lengths:
            initial = name[0].upper()
            grouped[initial].append((name, length))

        # Display results
        st.subheader("📋 Names and Lengths")
        for name, length in name_lengths:
            st.write(f"• **{name}** – {length} characters")

        # Summary
        total_length = sum(length for _, length in name_lengths)
        avg_length = total_length / len(name_lengths) if name_lengths else 0
        st.markdown(f"**Total characters:** {total_length}")
        st.markdown(f"**Average name length:** {avg_length:.2f}")

        # Group display
        st.subheader("🔠 Grouped by First Letter")
        for initial, items in sorted(grouped.items()):
            st.markdown(f"**{initial}**")
            for name, length in items:
                st.write(f" - {name} ({length} characters)")

        # Chart
        st.subheader("📊 Name Length Chart")
        fig, ax = plt.subplots()
        ax.barh(df["Name"], df["Length"], color="skyblue")
        ax.set_xlabel("Length (Characters)")
        ax.set_title("Name Lengths")
        st.pyplot(fig)

        # Export options
        st.subheader("📤 Export")
        export_format = st.radio("Choose export format:", ["CSV", "Text"])

        if export_format == "CSV":
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download CSV", csv, "name_lengths.csv", "text/csv")
        else:
            text = "\n".join(f"{row['Name']} – {row['Length']} characters" for _, row in df.iterrows())
            st.download_button("Download Text", text, "name_lengths.txt", "text/plain")
