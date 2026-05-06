import streamlit as st
from chatbot import get_response

st.title("Context-Aware Multi-Tool Chatbot")

user_input = st.text_input("You:")

if st.button("Send") and user_input:
    response = get_response(user_input)

    st.write("Bot:")
    st.write(response)