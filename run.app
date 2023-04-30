import streamlit as st
from streamlit_chat import message
import openai

st.set_page_config(page_title="Chat with SimonGPT")
st.title("Chat with SimonGPT")
st.sidebar.markdown("Developed by Mark Craddock](https://twitter.com/mcraddock)", unsafe_allow_html=True)
st.sidebar.markdown("Current Version: 0.0.2")
st.sidebar.markdown("Not optimised")
st.sidebar.markdown("May run out of OpenAI credits")

