import streamlit as st
import requests
import os
import pickle
from pathlib import Path
import hashlib


def chat_page():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    user_input = st.chat_input("Digite sua mensagem...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.chat_message("user"):
            st.markdown(user_input)
        
        try:
            response = requests.post(url=f"http://agent-api:8000/api/v1/hook",
                                     json={"body": st.session_state.messages})
            
            response_content = response.json()
            
            st.session_state.messages.append({"role": "assistant", "content": response_content})
            
            with st.chat_message("assistant"):
                st.markdown(response_content)
        except Exception as e:
            st.error(f"Erro ao conectar com a API: {str(e)}")
            st.session_state.messages.pop()

def main():
    st.set_page_config(page_title="Agent Platform",
                       page_icon="💬",
                       layout="centered",
                       initial_sidebar_state="collapsed",
                       menu_items=None)
    
    st.set_option("client.toolbarMode", "minimal")

    chat_page()

if __name__ == "__main__":
    main()
