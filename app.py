import streamlit as st
import requests

# create the title for the page
st.title("🤝 Your Personal Assistant")

# add subheader
st.subheader("What can your personal assistant do?")

# create a list of what your assistant can do
st.markdown("""
            1. Answer questions on various topics.   
            2. Arrange Calendar events and meetings.  
            3. Read your emails and send replies, can even summarize them for you.
            4. Manage your tasks and to-do lists.
            5. Take quick notes for you.
            6. Track your expenses and budgeting.
            """)

# add chats subheader
st.subheader("💬 Chat with your assistant")

# create a session state for message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show the messages in chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# create a chat input box
user_message = st.chat_input()

# if user sends a message
if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)
        st.session_state.messages.append(
            {"role": "user", "content": user_message}
        )

    # send the user message to the n8n webhook
    # send the user message to the n8n webhook
# send the user message to the n8n webhook
response = requests.post(
    "http://localhost:5678/webhook/6f5d3bc0-1734-4318-b1f6-60148d289bbf",
    json={"message": user_message}
)

# get the AI response from webhook
data = response.json()

if isinstance(data, list):
    ai_response = data[0]["output"]
else:
    ai_response = data["output"]

# display the AI response in chat
with st.chat_message("assistant"):
    st.markdown(ai_response)

    # append the AI response to message history
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )