# test.py
import streamlit as st

st.title("Hello World")
st.write("This is a test app")

# Add a button
if st.button("Click me"):
    st.write("Button clicked!")