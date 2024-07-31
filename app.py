import streamlit as st
import google.generativeai as genai

# Configure the Generative AI Model
api_key = "AIzaSyDNKGTLr92EOMF62WWA3mIbtBIkRu_r5f8"
if api_key is None:
    st.error("API Key not found in secrets.")
    st.stop()

genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone in your answers.",
)

# Initialize chat session
chat_session = model.start_chat(history=[])

# Function to handle prompts
def get_gemini_response(question):
    try:
        response = chat_session.send_message(question)
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Sorry, I couldn't process your request."

# Streamlit page configuration
st.set_page_config(
    page_title="Chat with Google AI",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto",
)

# Title and description
st.title("Chat with Google AI")
st.write("This is a simple app to chat with Google AI using the Gemini-1.5-pro model.")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input for user prompt
user_input = st.text_input("Enter your message:", "")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from the model
    response_text = get_gemini_response(user_input)
    
    # Display the assistant's response
    if response_text:
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        with st.chat_message("assistant"):
            st.markdown(response_text)
