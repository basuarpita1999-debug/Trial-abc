import streamlit as st

def add(a, b):
    return a + b

# Set a pink background using custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: none;
        background-color: #ffc0cb;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Simple Calculator - Addition")

num1 = st.number_input("Enter first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number:", value=0.0, format="%.2f")

if st.button("Add"):
    result = add(num1, num2)
    st.success(f"The sum of {num1} and {num2} is {result}")