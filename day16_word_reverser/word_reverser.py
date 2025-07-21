import streamlit as st

# -----------------------------
# Reversal Functions
# -----------------------------
def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

def reverse_sentence(sentence):
    return sentence[::-1]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Super Reverser", page_icon="🔄")
st.title("🔄 Super Reverser")
st.subheader("Reverse by Word or Sentence – Your Way!")

# Mode selection
mode = st.radio("Choose your reverse mode:", ["Reverse Words", "Reverse Sentence"])

# Input
sentence = st.text_input("Enter a sentence:")

# Output
if sentence:
    if mode == "Reverse Words":
        result = reverse_words(sentence)
        st.success("Each word reversed:")
    else:
        result = reverse_sentence(sentence)
        st.success("Entire sentence reversed:")
    st.code(result)
else:
    st.info("Type a sentence above to see the magic!")

# Examples
st.markdown("### 💡 Examples")
st.markdown("""
**Input:** `Hello Waffestry Fans!`  
- **Reverse Words:** `olleH yrts effaW !snaF`  
- **Reverse Sentence:** `!snaF yrts effaW olleH`
""")

# Footer
st.markdown("---")
st.caption("Created by Waffestry • Powered by Streamlit")
