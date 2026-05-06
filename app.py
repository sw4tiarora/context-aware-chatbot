import streamlit as st
from chatbot import get_response

st.title("VOX")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)
        
    response = get_response(st.session_state.messages)
    
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )
    
    with st.chat_message("assistant"):
        st.markdown(response)