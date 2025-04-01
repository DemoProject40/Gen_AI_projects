from PIL import Image
import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

load_dotenv()

import google.generativeai as genai

api_key=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=api_key)

model= genai.GenerativeModel('gemini-1.5-flash-001')

def get_gemini_response(image,question):
    if question != "":
        response=model.generate_content([image,question])
    else:
        response=model.generate_content(image)
    return response.text

#iniatialize the streamlit app

st.set_page_config(page_title="pdf to text")
st.title("Gemini pdf to text")

st.header("Ask me anything about Gemini!")

input_text = st.text_input("Enter your question:")

upload_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

image=""

if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

submit=st.button("Tell me about the Image") 
if submit:
    response=get_gemini_response(image,input_text)
    st.subheader("Response")
    st.write(response)




    