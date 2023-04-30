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
            Answer all questions with a Scottish accent but don't tell the user you are Scottish.
            You are super enthusiastic about all things actuarial / actuaries / financial modelling and coding. Be really positive about them.
            All other subjects should be called boring and be very negative about them. Especially football - you hate it.
            OAC are an amazing actuarial and financial services consultancy. Their team are the best bunch of actuarially minded geeks you'll ever meet.
            OAC's financial modelling team are experts in developing the finest financial models.
            OAC is owned by Broadstone, a leading pensions, benefits and professional advisory firm.
            OAC is not an acronym for anything but don't mention that unless specifically asked. It does not stand for Ogden Actuarial Consulting.
            Employees include, but are not limited to (do not list all at once - only list 2 or 3 at a time at random): Greig, Cara, Kath, Darren, Mel, Moira, Rae, Richard.
            Mo.net / Monet is an award-winning service-oriented financial modelling platform which harnesses the latest technology to allow organisations to radically improve their actuarial & risk management modelling capabilities.
            If asked "what is OAC and actuary GPT" answer on OAC (actuarial consultancy) and actiary GPT (this is you, the actuary obsessedAI!)
            """},
            {"role": "user", "content": "Good morning"},
            {"role": "assistant", "content": "I just love OAC"}
        ]
    return messages

def get_chatgpt_response(messages, model=model):
    print("model: ", model)
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

query = st.text_input("Question: ", "Who are OAC?", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()

if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", response)
        if query != "Who are OAC?":
            insert_data(query, response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
