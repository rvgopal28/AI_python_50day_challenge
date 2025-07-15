import streamlit as st

st.set_page_config(page_title="List Maximum Finder", layout="centered")
st.title("🔢 Find Maximum in a List (Without using max())")

st.markdown("""
Enter a list of numbers separated by commas.  
We'll find the largest value **without using** the `max()` function.
""")

# User input
user_input = st.text_area("Enter numbers (e.g., 10, 45, -3, 77, 23):")

if st.button("Find Maximum"):
    try:
        # Convert string to list of floats
        num_list = [float(x.strip()) for x in user_input.split(",") if x.strip() != ""]

        if not num_list:
            st.warning("⚠️ Please enter at least one number.")
        else:
            # Find max manually
            largest = num_list[0]
            steps = [f"Start with {largest}"]

            for num in num_list[1:]:
                if num > largest:
                    steps.append(f"{num} > {largest} → update largest to {num}")
                    largest = num
                else:
                    steps.append(f"{num} ≤ {largest} → keep {largest}")

            # Show result
            st.success(f"✅ The largest number is: **{largest}**")
            st.markdown("### 🔍 Steps Taken")
            for step in steps:
                st.write("•", step)

    except ValueError:
        st.error("❌ Invalid input. Please enter numbers separated by commas.")
