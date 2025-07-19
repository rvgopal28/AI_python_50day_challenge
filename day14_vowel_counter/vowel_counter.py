import streamlit as st

# Define the vowel counting function
def count_vowels(word):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in word if char in vowels)

# Streamlit app layout
st.title("Vowel Counter")
st.write("Enter a word to count its vowels (a, e, i, o, u)")

# Input field for the word
word = st.text_input("Enter a word:", "")

# Display result when a word is entered
if word:
    vowel_count = count_vowels(word)
    st.write(f"The word **'{word}'** contains **{vowel_count}** vowel(s).")