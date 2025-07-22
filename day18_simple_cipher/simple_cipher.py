import streamlit as st

# -----------------------------
# Cipher Logic
# -----------------------------
def shift_letter(letter, shift):
    if letter.isalpha():
        base = ord('A') if letter.isupper() else ord('a')
        return chr((ord(letter) - base + shift) % 26 + base)
    else:
        return letter

def caesar_cipher(text, shift):
    return ''.join(shift_letter(char, shift) for char in text)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Simple Cipher", page_icon="🔐")
st.title("🔐 Simple Caesar Cipher")
st.subheader("Shift each letter in a word by 1 position in the alphabet")

# Input field
text = st.text_input("Enter text to cipher:")

# Mode selector
mode = st.radio("Mode", ["Encrypt (+1 shift)", "Decrypt (-1 shift)"])

# Shift direction
shift = 1 if mode == "Encrypt (+1 shift)" else -1

# Result output
if text:
    result = caesar_cipher(text, shift)
    st.success(f"Result: `{result}`")
else:
    st.info("Type a word or sentence to encrypt or decrypt.")

# Example section
st.markdown("### 🔁 Examples")
st.markdown("""
- **Encrypt** `hello` → `ifmmp`  
- **Decrypt** `ifmmp` → `hello`  
- **Encrypt** `Zebra` → `Afcsb`
""")

# Footer
st.markdown("---")
st.caption("Waffestry Classroom Tools • Caesar Cipher • Streamlit Edition")