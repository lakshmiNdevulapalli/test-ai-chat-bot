from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
import streamlit as st
from streamlit_chat import message

st.set_page_config(
    page_title='T.U.E.S.D.A.I Virtual Assistant',
    page_icon='🤖==>🌮'
)

st.subheader('TUESDAI Custom Chatbot 💡')

chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.5)

if 'messages' not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    system_message = st.text_input(label='System role')
    user_prompt = st.text_input(label='Send a message')
    
    if system_message:
        if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
            st.session_state.messages.append(SystemMessage(content=system_message))
            system_message = ""  # Reset system message
    
    st.write(st.session_state.messages)
    
    if user_prompt:
        st.session_state.messages.append(HumanMessage(content=user_prompt))
        user_prompt = ""  # Reset user message
    
    if st.session_state.messages:  # Make sure there are messages before invoking chat
        with st.spinner('🌮 is working on your request...'):
            response = chat(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

# Display messages
for msg in st.session_state.messages:
    if isinstance(msg, SystemMessage):
        st.write(f"System: {msg.content}")
    elif isinstance(msg, HumanMessage):
        st.write(f"You: {msg.content}")
    elif isinstance(msg, AIMessage):
        st.write(f"T.U.E.S.D.A.I: {msg.content}")
