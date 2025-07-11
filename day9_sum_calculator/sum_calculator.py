import streamlit as st
import matplotlib.pyplot as plt

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Streamlit app
st.title("🔢 Sum Calculator (1 to n)")
st.markdown("Enter a positive integer to calculate the sum of numbers from 1 to n using a loop.")

# User input
n = st.number_input("Enter a positive integer (n):", min_value=1, step=1, format="%d")

if st.button("Calculate Sum"):
    total_sum = calculate_sum(n)

    # Show result
    st.success(f"✅ The sum of numbers from 1 to {n} is: **{total_sum}**")

    # Prepare data for chart
    x = list(range(1, n + 1))
    y = [sum(range(1, i + 1)) for i in x]  # Cumulative sum for each step

    # Plot with matplotlib
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o', color='blue', label='Cumulative Sum')
    ax.set_title("📈 Cumulative Sum from 1 to n")
    ax.set_xlabel("Number")
    ax.set_ylabel("Sum")
    ax.grid(True)
    ax.legend()

    # Show chart
    st.pyplot(fig)
