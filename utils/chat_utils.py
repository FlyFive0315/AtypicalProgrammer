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
    chat_rsp = internlm_client.chat.completions.create(
        model="internlm2.5-latest",
        messages=messages,
        stream=True,
    )
    
    return chat_rsp

def format_message(role, content):
    return {"role": role, "content": content} 