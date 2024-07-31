import streamlit as st
import google.generativeai as genai

# Configuration for the Generative AI Model
api_key = "AIzaSyDNKGTLr92EOMF62WWA3mIbtBIkRu_r5f8"
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

# Start a new chat session
chat_session = model.start_chat(
    history=[
        {"role": "user", "parts": ["chat prompt\n"]},
        {"role": "user", "parts": ["tell me about bca course\n"]},
        {"role": "model", "parts": [
            "Sure!  Global Educational Institutes offers a comprehensive Bachelor of Computer Applications (BCA) program. "
            "\n\nHere's some key information about the course:\n\n**Duration:** 3 Years\n**Affiliation:** CCS University, Meerut\n"
            "**Approval:** AICTE\n**Pattern:** Full-time\n\n**Eligibility:**\n\n* You must have completed 10+2 (or equivalent) with a minimum "
            "of 45% for General/OBC and 40% for SC/ST candidates.\n* Mathematics in the 10th grade is compulsory for admission. \n\n**What you'll learn:**\n\n"
            "The BCA program is designed to provide you with a strong foundation in computer science and applications. You'll gain knowledge and skills in areas like:\n\n"
            "* Programming languages (such as C, C++, Java, Python)\n* Database management systems\n* Web development\n* Software engineering\n"
            "* Computer networks\n* And much more!\n\n**Career Prospects:**\n\nAfter completing your BCA, you'll have a wide range of career opportunities in the IT industry. You can explore roles such as:\n\n"
            "* Software Developer\n* Web Developer\n* Database Administrator\n* System Analyst\n* Network Engineer\n\n**To learn more about:**\n\n"
            "* Detailed syllabus\n* Fee structure\n* Admission process\n\nPlease tell me what you are specifically interested in, and I'll be happy to provide you with more details. \n\n"
            "I can also connect you with our admissions team if you'd like to discuss your application or have any specific questions. \n"
        ]},
        {"role": "user", "parts": ["what is eligibility\n"]},
        {"role": "model", "parts": [
            "You are right to check on the eligibility criteria before applying!  To be eligible for the BCA program at Global Educational Institutes, you need:\n\n"
            "* **To have passed your 10+2 (or equivalent) exams** from a recognized board.\n* **A minimum of 45% in your 10+2** if you are from the General or OBC category.\n"
            "* **A minimum of 40% in your 10+2** if you are from the SC/ST category.\n* **Mathematics must have been one of your subjects in the 10th grade.** This is compulsory for BCA admission. \n\n"
            "Does this make the eligibility requirements clearer for you? Let me know if you have any other questions. \n"
        ]},
        {"role": "user", "parts": ["no thanks\n"]},
        {"role": "model", "parts": [
            "Sounds good! I'm glad I could help clarify the eligibility for the BCA program. \n\nIs there anything else I can help you with today? "
            "Perhaps you'd like to know about the fee structure, the admission process, or maybe you have questions about campus life at Global Educational Institutes?  \n\n"
            "Don't hesitate to ask! 😊 \n"
        ]},
        {"role": "user", "parts": ["Can you give me more info?"]}
    ]
)

st.title("Chat with Google AI")
st.write("This is a simple app to chat with Google AI using the Gemini-1.5-pro model.")

# Text input for user prompt
user_input = st.text_input("Enter your prompt:", "")

# If there is user input, get the response
if user_input:
    response = chat_session.send_message(user_input)
    st.write(response.text)
