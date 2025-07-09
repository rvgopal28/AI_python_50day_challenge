import streamlit as st
import random
import string

def check_password(password):
    min_length = 8
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"

    length_ok = len(password) >= min_length
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(char in special_characters for char in password)

    return {
        "length_ok": length_ok,
        "has_digit": has_digit,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_special": has_special
    }

def calculate_strength(checks):
    score = sum(checks.values())

    if score <= 2:
        return "Weak", "❌", "red"
    elif score == 3 or score == 4:
        return "Medium", "⚠️", "orange"
    else:
        return "Strong", "✅", "green"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Secure Password Checker with Strength Meter")

password = st.text_input("Enter your password", type="password")
confirm_password = st.text_input("Confirm your password", type="password")

if st.button("Check Password"):
    if password != confirm_password:
        st.error("❌ Passwords do not match.")
    else:
        checks = check_password(password)
        strength_label, strength_emoji, strength_color = calculate_strength(checks)

        st.markdown("### 🔍 Validation:")
        st.markdown(f"- Minimum 8 characters: {'✅' if checks['length_ok'] else '❌'}")
        st.markdown(f"- At least one digit: {'✅' if checks['has_digit'] else '❌'}")
        st.markdown(f"- At least one uppercase: {'✅' if checks['has_upper'] else '❌'}")
        st.markdown(f"- At least one lowercase: {'✅' if checks['has_lower'] else '❌'}")
        st.markdown(f"- At least one special character (!@#$...): {'✅' if checks['has_special'] else '❌'}")

        st.markdown("---")
        st.markdown(f"### 🔋 Password Strength: **:{strength_color}[{strength_label}]** {strength_emoji}")

        if strength_label != "Strong":
            st.info(f"💡 Suggested strong password: `{generate_password()}`")
        else:
            st.success("🎉 Password is strong and accepted!")
