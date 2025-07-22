import streamlit as st
import pandas as pd
import re
import math

# ----------------------------
# Utility Functions
# ----------------------------

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = re.split(r'[.!?]+', text.strip())
    return len([s for s in sentences if s.strip()])

def count_characters(text, include_spaces=True):
    return len(text) if include_spaces else len(text.replace(" ", ""))

def estimate_reading_time(word_count, wpm=200):
    minutes = word_count / wpm
    return math.ceil(minutes * 60)  # return seconds

# ----------------------------
# Streamlit UI
# ----------------------------

st.set_page_config(page_title="📊 Text Statistics", layout="centered")
st.title("📊 Text Statistics Tool")
st.markdown("Analyze a paragraph to count **words, sentences, characters**, and estimate reading time.")

user_text = st.text_area("✏️ Enter your paragraph here:", height=200)

if user_text.strip():
    words = count_words(user_text)
    sentences = count_sentences(user_text)
    chars_with_spaces = count_characters(user_text, include_spaces=True)
    chars_no_spaces = count_characters(user_text, include_spaces=False)
    read_time_seconds = estimate_reading_time(words)

    # Display in metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📝 Words", words)
        st.metric("📌 Sentences", sentences)
    with col2:
        st.metric("🔡 Chars (with spaces)", chars_with_spaces)
        st.metric("🔠 Chars (no spaces)", chars_no_spaces)

    st.success(f"🕐 Estimated Reading Time: ~{read_time_seconds} seconds")

    # Visual Chart
    st.markdown("### 📊 Text Statistics Breakdown")
    stats_data = pd.DataFrame({
        'Metric': ['Words', 'Sentences', 'Characters (with spaces)', 'Characters (no spaces)'],
        'Count': [words, sentences, chars_with_spaces, chars_no_spaces]
    })

    st.bar_chart(data=stats_data.set_index("Metric"))

    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit")

else:
    st.info("Please enter a paragraph to analyze.")
