import streamlit as st
from . import config
from openai import OpenAI
import os

internlm_client = OpenAI(
    api_key=config.internlm_api_key,
    base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",
)

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def chat_with_internlm(messages):
    print("messages:", messages)
    chat_rsp = internlm_client.chat.completions.create(
        model=st.session_state.model_settings["model"],
        messages=messages,
        stream=True,
        temperature=st.session_state.model_settings["temperature"],
        top_p=st.session_state.model_settings["top_p"],
    )
    
    return chat_rsp

def format_message(role, content):
    return {"role": role, "content": content} 