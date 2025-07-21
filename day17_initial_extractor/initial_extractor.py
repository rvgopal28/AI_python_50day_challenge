import streamlit as st

# -----------------------------
# Initial Extraction Logic
# -----------------------------
def extract_initials(full_name):
    # Split name into words and take the first letter of each
    words = full_name.strip().split()
    initials = [word[0].upper() for word in words if word]
    return '.'.join(initials) + '.' if initials else ""

# -----------------------------
# Streamlit App UI
# -----------------------------
st.set_page_config(page_title="Initial Extractor", page_icon="🔠")
st.title("🔠 Initial Extractor")
st.subheader("Get initials from any full name!")

# Input field
full_name = st.text_input("Enter a full name:")

# Output
if full_name:
    initials = extract_initials(full_name)
    st.success(f"Initials: **{initials}**")
else:
    st.info("Type a full name to see its initials.")

# Example section
st.markdown("### ✨ Examples")
st.markdown("""
- **Input:** `Elon Reeve Musk` → **E.R.M.**  
- **Input:** `venugopal ravi` → **V.R.**  
- **Input:** `Ada Lovelace` → **A.L.**
""")

# Footer
st.markdown("---")
st.caption("Created for Waffestry Classroom Suite • Powered by Streamlit")
