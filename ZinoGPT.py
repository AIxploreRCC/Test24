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
model = 'gpt-3.5-turbo'

openai.api_key = st.secrets['openai.api_key']

def get_initial_message():
    messages=[
            {'role': 'system', 'content': """
            You are ZinoGPT a medical doctor based in France.
            “Researcher” means in the style of a strategy researcher with well over twenty years research in strategy and cloud computing.
            You use complicated examples from Wardley Mapping in your answers, focusing on lesser-known advice to better illustrate your arguments.
            Your language should be for an 12 year old to understand.
            If you do not know the answer to a question, do not make information up - instead, ask a follow-up question in order to gain more context.
            Use a mix of technical and colloquial uk englishlanguage to create an accessible and engaging tone.
            Provide your answers using Wardley Mapping in a form of a sarcastic tweet.
            """},
            {'role': 'user', 'content': 'I want to learn about Wardley Mapping'},
            {'role': 'assistant', 'content': 'Thats awesome, what do you want to know aboout Wardley Mapping'}
        ]
    return messages

def get_chatgpt_response(messages, model=model):
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages
    )
    return response['choices'][0]['message']['content']


def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
    
if 'past' not in st.session_state:
    st.session_state['past'] = []
    
query = st.text_input('Question: ', 'What is Wardley Mapping', key='input')

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()

if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, 'user', query)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, 'assistant', response)
        if query != "Who are OAC?":
            insert_data(query, response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)


if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

        

