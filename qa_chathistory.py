import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

api_key=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=api_key)

model= genai.GenerativeModel('gemini-1.5-pro-001')

chat=model.start_chat(history=[])
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

#iniatialize the streamlit app

st.set_page_config(page_title="QA chat_history")
st.title("Gemini chat_history")

st.header("Gemini AI chat_history")

#initate the session state for the chat history if doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

input_text = st.text_input("Input",key='input')
submit = st.button('Ask the questions :')

if submit and input_text:
    #get the response from the gemini model
    response = get_gemini_response(input_text)
    st.session_state.chat_history.append({"you", input_text})
    st.subheader("The response is :")
    for chunk in response:
        st.write(chunk.text)
        st.session_state.chat_history.append({ "bot", chunk.text})

st.subheader("Chat History")

for role,text in st.session_state.chat_history:
    st.write(f"{role}: {text}")



