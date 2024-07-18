import streamlit as st
from query_nerdy import generate_response_1, generate_response_2, generate_response_3

st.title("🤓🐦 Nerdy Chirpy")

# Define the options for the dropdown menu
options = ["Model developement", "Data Preprocessing", "Data Vizualization"]

# Use st.selectbox to create the dropdown menu
selected_option = st.selectbox("Select AI Task:", options)

if selected_option == "Model developement":
    if "messages" not in st.session_state.keys():
      st.session_state.messages = [{"role": "assistant", "content": "Hi I am Nerdy Chirpy. How can I help you? "}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Message Chirpy!"):
    # Display user message in chat message container
      st.chat_message("user").markdown(prompt)
    # Add user message to chat history
      st.session_state.messages.append({"role": "user", "content": prompt})

      response = generate_response_1(prompt)
    # Display assistant response in chat message container
      with st.chat_message("assistant"):
         st.markdown(response)
    # Add assistant response to chat history
      st.session_state.messages.append({"role": "assistant", "content": response})


elif selected_option == "Data Preprocessing":
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

      response = generate_response_2(prompt)
    # Display assistant response in chat message container
      with st.chat_message("assistant"):
         st.markdown(response)
    # Add assistant response to chat history
      st.session_state.messages.append({"role": "assistant", "content": response})

elif selected_option == "Data Vizualization":
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

      response = generate_response_3(prompt)
    # Display assistant response in chat message container
      with st.chat_message("assistant"):
         st.markdown(response)
    # Add assistant response to chat history
      st.session_state.messages.append({"role": "assistant", "content": response})
