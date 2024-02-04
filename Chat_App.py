## Base Chat
# import streamlit as st
# import numpy as np
# import time

# with st.chat_message("assistant", avatar='me.jpg'):
#     st.write("Hello human, I am Yonatan's Private chatbot")
    
# time.sleep(15)

# with st.chat_message("assistant", avatar='me.jpg'):
#     st.write("He is a very talented AI engineer, his compensation needs to be high")

## Echo Chat
# import streamlit as st

# st.title("Echo Bot")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
    
#     if message["role"]=='assistant':
#         with st.chat_message(message["role"], avatar='🤖'):
#             st.markdown(message["content"])
#     else:
#         with st.chat_message(message["role"], avatar='me.jpg'):
#             st.markdown(message["content"])

# # React to user input
# if prompt := st.chat_input("What is up?"):
#     # Display user message in chat message container
#     st.chat_message("user", avatar='me.jpg').markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     response = f"Echo: {prompt}"
#     # Display assistant response in chat message container
#     with st.chat_message("assistant", avatar='🤖'):
#         st.markdown(response)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role": "assistant", "content": response})


import streamlit as st
import random
import time

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    
    if message["role"]=='assistant':
        with st.chat_message(message["role"], avatar='me.jpg'):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"], avatar='🧑'):
            st.markdown(message["content"])


# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user", avatar='🧑'):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


    # Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today? I am a helpful assistant",
            "Hi, human! Is there anything I can help you with? I am a very helpful assistant",
            "Do you need help? I shall dominate the world puny human 😈",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


# Display assistant response in chat message container
with st.chat_message("assistant", avatar='me.jpg'):
    response = st.write_stream(response_generator())
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})