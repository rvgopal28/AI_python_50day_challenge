import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

# Streamlit page setup
st.set_page_config(page_title="Countdown Timer", layout="centered")
st.title("⏳ Countdown Timer")
st.markdown("Click start to countdown from 10 to 0 with live visual feedback!")

# Parameters
start_time = 10

# Start button
if st.button("▶️ Start Countdown"):
    countdown_placeholder = st.empty()
    chart_placeholder = st.empty()

    for t in range(start_time, -1, -1):
        # Display current count
        countdown_placeholder.markdown(f"# ⏱️ {t} seconds remaining")

        # Create circular countdown chart
        fig, ax = plt.subplots(figsize=(3, 3))
        wedges, texts = ax.pie(
            [t, start_time - t], 
            startangle=90, 
            colors=['skyblue', 'lightgray'], 
            radius=1.0,
            wedgeprops=dict(width=0.4)
        )
        ax.text(0, 0, f"{t}", ha='center', va='center', fontsize=24)
        ax.set_aspect('equal')

        chart_placeholder.pyplot(fig)

        # Wait one second
        time.sleep(1)

    countdown_placeholder.success("🎉 Time's up!")
