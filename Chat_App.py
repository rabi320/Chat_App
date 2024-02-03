import streamlit as st
import numpy as np
import time

with st.chat_message("assistant", avatar='me.jpg'):
    st.write("Hello human, I am Yonatan's Private chatbot")
    
time.sleep(15)

with st.chat_message("assistant", avatar='me.jpg'):
    st.write("He is a very talented AI engineer, his compensation needs to be high")