import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

load_dotenv()

import google.generativeai as genai

api_key=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=api_key)

model= genai.GenerativeModel('gemini-1.5-pro-001')

def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text


#iniatialize the streamlit app

st.set_page_config(page_title="Gemini Chatbot")
st.title("Gemini Chatbot")

st.header("Ask me anything about Gemini!")

input_text = st.text_input("Enter your question:")

submit_button = st.button("Submit")

if submit_button:
    response = get_gemini_response(input_text)
    st.write("Response:")
    st.write(response)



