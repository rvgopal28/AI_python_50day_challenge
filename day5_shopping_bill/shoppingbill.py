import streamlit as st

# Title
st.title("🛒 Shopping Bill Calculator")

st.markdown("Enter the base prices (without tax) of 3 items. We'll calculate the tax and show the final total.")

# Inputs for 3 items
items = []
for i in range(1, 4):
    st.subheader(f"Item {i}")
    name = st.text_input(f"Name of item {i}", key=f"name_{i}")
    price = st.number_input(f"Base Price of item {i} (₹)", min_value=0.0, key=f"price_{i}")
    quantity = st.number_input(f"Quantity of item {i}", min_value=0, step=1, key=f"qty_{i}")
    total = price * quantity
    items.append((name, price, quantity, total))

# Tax input
tax_percent = st.slider("Tax percentage", 0, 50, 18)

# When user clicks calculate
if st.button("Calculate Final Bill"):
    # Calculate subtotal and tax
    subtotal = sum(item[3] for item in items)
    tax_amount = (subtotal * tax_percent) / 100
    grand_total = subtotal + tax_amount

    # Display item details
    st.subheader("🧾 Bill Summary")
    st.markdown("### Item Breakdown")
    st.table([
        {"Item": item[0], "Base Price (₹)": f"{item[1]:.2f}", "Quantity": item[2], "Total (₹)": f"{item[3]:.2f}"}
        for item in items if item[0] and item[2] > 0
    ])

    # Display totals
    st.markdown("---")
    st.markdown(f"**Subtotal (Before Tax):** ₹{subtotal:.2f}")
    st.markdown(f"**Tax ({tax_percent}%):** ₹{tax_amount:.2f}")
    st.markdown(f"**Final Total (With Tax):** ₹{grand_total:.2f}")
