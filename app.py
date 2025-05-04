import streamlit as st
import requests

st.set_page_config(page_title="ConvoBot", page_icon="🤖", layout="centered")

# Custom background
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .stApp {
        background: linear-gradient(to bottom right, #a1c4fd, #c2e9fb);
        padding: 2rem;
    }
    .chat-box {
        background-color: #ffffffaa;
        padding: 1rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🤖 ConvoBot - Your AI Companion</h1>", unsafe_allow_html=True)

# Get API Key
api_key = st.secrets["openrouter_api_key"]

def ask_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://convo-bot.streamlit.app",
        "X-Title": "ConvoBot Chat"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

user_input = st.text_input("Ask ConvoBot something:")

if user_input:
    with st.spinner("ConvoBot is thinking..."):
        reply = ask_openrouter(user_input)
        st.markdown(f"<div class='chat-box'><b>You:</b> {user_input}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-box'><b>ConvoBot:</b> {reply}</div>", unsafe_allow_html=True)
