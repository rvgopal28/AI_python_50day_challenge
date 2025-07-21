import streamlit as st
import re

# -----------------------------
# NameFormatter Class
# -----------------------------
class NameFormatter:
    def __init__(self, full_name: str):
        self.original = full_name.strip()
        self.cleaned = self._clean_name(self.original)
        self.parts = self.cleaned.split()

    def _clean_name(self, name: str) -> str:
        return ' '.join(part.capitalize() for part in re.split(r'\s+', name.strip()) if part)

    def format_first_last(self) -> str:
        return ' '.join(self.parts)

    def format_last_first(self) -> str:
        if len(self.parts) >= 2:
            return f"{self.parts[-1]}, {' '.join(self.parts[:-1])}"
        return self.format_first_last()

    def get_initials(self) -> str:
        return ''.join(p[0].upper() for p in self.parts)

    def get_monogram(self) -> str:
        if len(self.parts) >= 2:
            return f"{self.parts[0][0].upper()}.{self.parts[-1][0].upper()}."
        return self.get_initials()

    def to_camel_case(self) -> str:
        return ''.join(p.capitalize() for p in self.parts)

    def to_snake_case(self) -> str:
        return '_'.join(p.lower() for p in self.parts)

    def all_formats(self) -> dict:
        return {
            "Original": self.original,
            "Cleaned": self.cleaned,
            "First Last": self.format_first_last(),
            "Last, First": self.format_last_first(),
            "Initials": self.get_initials(),
            "Monogram": self.get_monogram(),
            "CamelCase": self.to_camel_case(),
            "Snake_case": self.to_snake_case()
        }

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Name Formatter", page_icon="🧾")

st.title("🧾 Name Formatter")
st.subheader("Format any full name in multiple styles instantly.")

full_name_input = st.text_input("Enter Full Name", "")

if full_name_input:
    formatter = NameFormatter(full_name_input)
    results = formatter.all_formats()

    st.success("Formatted Results:")
    for label, value in results.items():
        st.markdown(f"**{label}**: `{value}`")
else:
    st.info("Please enter a name to see the formatted results.")

# Optional Footer
st.markdown("---")
st.markdown("Made with ❤️ by [YourName] • Powered by Streamlit")
