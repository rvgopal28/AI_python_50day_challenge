import streamlit as st
import matplotlib.pyplot as plt
import random
import re

# --- Config ---
st.set_page_config(page_title="Super Vowel Counter!", page_icon="🅰️", layout="centered")

# --- Vowel Facts ---
fun_facts = [
    "🧠 Did you know? Every word in English has a vowel!",
    "🔍 'Education' has all 5 vowels in it!",
    "🗣 The letter 'E' is the most used vowel in English!",
    "🎵 Vowels help us sing and speak smoothly!",
    "🐦 'Queue' has 4 vowels in a row!"
]

# --- Quiz Questions ---
quiz_questions = [
    {"question": "Which of these is NOT a vowel?", "options": ["A", "E", "X", "U"], "answer": "X"},
    {"question": "How many vowels are there in English?", "options": ["4", "5", "6", "26"], "answer": "5"},
    {"question": "Which word contains the most vowels?", "options": ["Tree", "Education", "Sky", "Cup"], "answer": "Education"},
]

# --- Vowel Counting Function ---
def count_each_vowel(text):
    vowels = 'aeiou'
    counts = {v: 0 for v in vowels}
    for char in text.lower():
        if char in vowels:
            counts[char] += 1
    return counts

# --- Vowel Highlight ---
def highlight_vowels(text):
    return re.sub(r'([aeiouAEIOU])', r':red[\1]', text)

# --- App UI ---
st.title("🔠 Super Vowel Counter!")
st.markdown("""
👋 **Hello, Little Explorer!**  
Type any word or sentence below to find out how many **vowels** are hiding inside!  
Vowels are: 🅰️ A, 🅴 E, 🅸 I, 🅾️ O, 🆄 U  
""")

text = st.text_input("🔡 Type something fun here (like a sentence):")

# --- Process Vowels ---
if text:
    counts = count_each_vowel(text)
    total = sum(counts.values())

    st.balloons()
    st.success(f"🎉 Yay! We found **{total} vowels** in your sentence!")

    st.markdown("### 🔤 Vowel Breakdown")
    for v, c in counts.items():
        st.write(f"🔠 **{v.upper()}**: {c} time(s)")

    # --- Chart ---
    st.markdown("### 📊 Vowel Chart")
    fig, ax = plt.subplots()
    ax.bar(counts.keys(), counts.values(), color=["#FF6961", "#77DD77", "#84B6F4", "#FDFD96", "#CBAACB"])
    ax.set_title("🎨 Vowel Chart", fontsize=14)
    ax.set_xlabel("Vowels")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # --- Highlight Vowels ---
    st.markdown("### 🔍 Highlighted Text")
    st.markdown(highlight_vowels(text), unsafe_allow_html=True)

    # --- Fun Fact ---
    st.markdown("### 🧠 Fun Fact Time!")
    st.info(random.choice(fun_facts))

# --- Quiz Game ---
st.markdown("---")
st.markdown("### 🎮 Vowel Quiz Game!")
if 'quiz_index' not in st.session_state:
    st.session_state.quiz_index = 0
    st.session_state.score = 0

if st.session_state.quiz_index < len(quiz_questions):
    q = quiz_questions[st.session_state.quiz_index]
    st.subheader(f"Q{st.session_state.quiz_index + 1}: {q['question']}")
    user_answer = st.radio("Pick your answer:", q["options"])

    if st.button("Check Answer"):
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Oops! The correct answer is **{q['answer']}**.")
        st.session_state.quiz_index += 1
else:
    st.success(f"🎉 Game Over! You scored {st.session_state.score} out of {len(quiz_questions)}!")
    if st.button("🔄 Play Again"):
        st.session_state.quiz_index = 0
        st.session_state.score = 0

# --- Footer ---
st.markdown("---")
st.caption("Made with ❤️ for smart kids by Waffestry Labs")
