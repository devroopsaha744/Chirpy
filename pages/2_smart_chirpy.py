import streamlit as st
from query_smart_chirpy import generate_response

st.title("💡🐦 Smart Chirpy")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Need some assistance with your backend tasks?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Message Smart Chirpy!"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = generate_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})