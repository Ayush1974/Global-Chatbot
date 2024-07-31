import streamlit as st
import google.generativeai as genai
import os

api_key = "AIzaSyDNKGTLr92EOMF62WWA3mIbtBIkRu_r5f8"
# Retrieve the API key from environment variables
GOOGLE_API_KEY = api_key

# Ensure the API key is set
if not GOOGLE_API_KEY:
    raise ValueError("Google API key not found. Please set GOOGLE_API_KEY in your environment.")

# Configure the Google AI generative model
genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model configuration and initialize the model
generation_config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    system_instruction="Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone in your answers.",
)

# Start a new chat session
chat = model.start_chat(history=[])

# Define a function to handle user prompts and get responses from the model
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit app setup
st.title("Chat with Google AI (Gemini Pro)")
st.write("Interact with the Google AI model by entering your questions below.")

# Text input for user prompt
user_input = st.text_input("Enter your prompt:")

# Display the response from the model
if user_input:
    response = get_gemini_response(user_input)
    st.write(response.text)
