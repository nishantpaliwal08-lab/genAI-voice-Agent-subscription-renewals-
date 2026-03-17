# app.py

# Streamlit interface for GPS renewal prototype

# This file controls:

# - simple chat interface

# - user input capture

# - bot reply rendering

# PM note:

# UI is intentionally minimal.

# The goal is not interface polish.

# The goal is fast conversational testing.
import streamlit as st
from graph import bot_reply

# ---------------- App Config ----------------

st.set_page_config(page_title="GPS Renewal Bot", page_icon="🤖")

# ---------------- Session State ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "stage" not in st.session_state:
    st.session_state.stage = "opening"

if "bot_started" not in st.session_state:
    opening_response, next_stage = bot_reply("", "opening")

    st.session_state.messages.append({
        "role": "assistant",
        "content": opening_response
    })

    st.session_state.stage = next_stage
    st.session_state.bot_started = True

# ---------------- Render Chat History ----------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- User Input ----------------

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    response, next_stage = bot_reply(user_input, st.session_state.stage)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.session_state.stage = next_stage

    with st.chat_message("assistant"):
        st.markdown(response)


# Streamlit chosen because:
# PMs can run locally without frontend engineering
# Conversation history helps test whether stage logic feels natural over multiple turns
