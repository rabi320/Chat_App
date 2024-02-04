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


# import streamlit as st
# import random
# import time

# st.title("Simple chat")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
    
#     if message["role"]=='assistant':
#         with st.chat_message(message["role"], avatar='me.jpg'):
#             st.markdown(message["content"])
#     else:
#         with st.chat_message(message["role"], avatar='🧑'):
#             st.markdown(message["content"])


# # Accept user input
# if prompt := st.chat_input("What is up?"):
#     # Display user message in chat message container
#     with st.chat_message("user", avatar='🧑'):
#         st.markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})


#     # Streamed response emulator
# def response_generator():
#     response = random.choice(
#         [
#             "Hello there! How can I assist you today? I am a helpful assistant",
#             "Hi, human! Is there anything I can help you with? I am a very helpful assistant",
#             "Do you need help? I shall dominate the world puny human 😈",
#         ]
#     )
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)


# # Display assistant response in chat message container
# with st.chat_message("assistant", avatar='me.jpg'):
#     response = st.write_stream(response_generator())
# # Add assistant response to chat history
# st.session_state.messages.append({"role": "assistant", "content": response})


## Yonatan GPT

from openai import OpenAI
import streamlit as st

# settings

file_path = 'Yonatan_Rabinovich.txt'

with open(file_path, 'r') as file:
    sys_message = file.read()


st.title("Yonatan's GPT")

# Disclaimer
disclaimer = """
**Disclaimer:**

The information provided by this AI assistant is generated based on available data and patterns, and it may not always be accurate or up-to-date. 
Users are advised to independently verify any critical information and exercise their judgment when relying on the assistant's responses. 
The developers and creators of this AI assistant are not liable for any inaccuracies, errors, or consequences resulting from the use of the provided information.
"""

# Display the disclaimer
st.markdown(disclaimer)

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

client = OpenAI(api_key=openai_api_key)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": sys_message}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    
    if message["role"]=='assistant':
        with st.chat_message(message["role"], avatar='me.jpg'):
            st.markdown(message["content"])
    elif message["role"]=='user':
        with st.chat_message(message["role"], avatar='🧑'):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything proffesional about Yonatan"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar='🧑'):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar='me.jpg'):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            max_tokens=300,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})