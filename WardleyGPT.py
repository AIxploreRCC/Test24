# Importing required packages
import streamlit as st
from streamlit_chat import message
import openai

st.set_page_config(page_title="Chat with ZinoGPT")
st.title("Chat with ZinoGPT")
st.sidebar.markdown("Developed by Zine-Eddine KHENE](https://twitter.com/ZineEddineKhene)", unsafe_allow_html=True)
st.sidebar.markdown("Current Version: 0.1.4")
st.sidebar.markdown("Using GPT-4 API")
st.sidebar.markdown("Not optimised")
st.sidebar.markdown("May run out of OpenAI credits")


# Set OpenAI API model
model = "gpt-3.5-turbo"

def get_initial_message():
    messages=[
            {"role": "system", "content": """
            You are ZinoGPT 
        ]
    return messages
