from dotenv import load_dotenv 
load_dotenv()  # Loading all env variables 

import streamlit as st 
import os 
import google.generativeai as genai 
from PIL import Image 

# Load environment variables
load_dotenv()

# Configure Google Generative AI with your API key directly
#GOOGLE_API_KEY = AIzaSyAAuTYtEy6FWouv298PSgMgzhQzCpppgow
GOOGLE_API_KEY ="AIzaSyDxNdARaGB577zuKr7LyCwW-nVsA_jwfJA"# Replace this with your actual API key

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Error configuring Gemini: {str(e)}")
    st.stop()

def get_gemini_response(input, image):
    try:
        if input != "":
            response = model.generate_content([input, image])
        else:
            response = model.generate_content(image)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

## Setting up our streamlit app 

st.set_page_config(page_title="Q&A Demo") 
st.header("Gemini LLM Application")

input = st.text_input("Input Prompt: ",key="input")

uploaded_file = st.file_uploader("Choose an image..." , type=["jpg" , "jpeg" , "png"])
image = None 
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image , caption="Uploaded Image" , use_container_width=True)
    
submit = st.button("Analyze")

#
if submit: 
    if uploaded_file is None:
        st.error("Please upload an image first!")
    else:
        with st.spinner("Analyzing image..."):
            response = get_gemini_response(input , image) 
            st.subheader("The Response is")
            st.write(response)