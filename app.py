import streamlit as st

def add(a, b):
    return a + b

st.title("Simple Calculator - Addition")

num1 = st.number_input("Enter first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number:", value=0.0, format="%.2f")

if st.button("Add"):
    result = add(num1, num2)
    st.success(f"The sum of {num1} and {num2} is {result}")