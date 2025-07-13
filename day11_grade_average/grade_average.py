import streamlit as st
import matplotlib.pyplot as plt

# App title
st.set_page_config(page_title="Grade Average Calculator", layout="centered")
st.title("📘 Grade Average Calculator")
st.markdown("Enter 5 test scores to calculate your average and see if you passed!")

# Input scores
scores = []
for i in range(1, 6):
    score = st.slider(f"Score {i}", min_value=0, max_value=100, value=50, step=1)
    scores.append(score)

# Calculate average
average = sum(scores) / len(scores)
pass_mark = 40
result = "Pass" if average >= pass_mark else "Fail"

# Show results
st.subheader("📊 Results")
st.markdown(f"**Average Score:** `{average:.2f}`")

if result == "Pass":
    st.success("🎓 You Passed! Great job!")
else:
    st.error("❌ You Failed. Keep practicing!")

# Show scores as a bar chart
st.subheader("📈 Test Score Chart")
fig, ax = plt.subplots()
test_labels = [f"Test {i}" for i in range(1, 6)]
ax.bar(test_labels, scores, color="mediumseagreen" if result == "Pass" else "salmon")
ax.set_ylabel("Score")
ax.set_ylim([0, 100])
ax.set_title("Test Scores")
st.pyplot(fig)