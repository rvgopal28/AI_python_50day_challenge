
# 📧 Email Username Analyzer (Streamlit App)

A beginner-friendly yet powerful Streamlit-based UI tool that analyzes email addresses and extracts useful information such as the username, domain, length of the username, presence of numbers, and special characters.

🚀 Features
✅ Extracts username (part before @)
✅ Extracts domain (part after @)
✅ Checks if username contains numbers
✅ Checks if username contains special characters
✅ Shows the length of username
✅ Handles invalid emails gracefully
✅ Streamlit UI for ease of use
✅ DataFrame compatible with Arrow (fix for serialization errors)

🧠 Example Output
Email	Username	Domain	Length	Has Numbers?	Has Special Chars?
test123@example.com	test123	example.com	7	✅	❌
user.name@site.org	user.name	site.org	9	❌	✅
invalidemail.com	❌ Invalid email	None	NaN	None	None

🛠 Tech Stack
Python 3.8+

Streamlit

NumPy

Pandas


🔧 Setup Instructions
Clone or download the project folder.

Install dependencies (preferably inside a virtual environment):

## 📦 Requirements
```bash
pip install streamlit pandas numpy
```

## ▶️ Run the App
```bash
streamlit run app.py
```

🧩 Important Fixes Included
To avoid Arrow serialization errors caused by mixing strings ('-') and integers in numeric columns:

Replaced string dashes ('-') with np.nan for missing numeric data

Used None for boolean values when the email is invalid

Ensured all columns in the DataFrame are correctly typed:

df["Length"] = pd.to_numeric(df["Length"], errors="coerce")


✅ Use Cases
Email validation tools

Classroom projects on string parsing

Entry-level Python + Streamlit projects

Teaching data typing and error handling

🙋‍♀️ Author
Built with ❤️ by the Waffestry Learning Series 🍽️