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
chat_session = model.start_chat( history=[
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
       {
      "role": "user",
      "parts": [
        "tell me about bca course\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Sure!  Global Educational Institutes offers a comprehensive Bachelor of Computer Applications (BCA) program. \n\nHere's some key information about the course:\n\n**Duration:** 3 Years\n**Affiliation:** CCS University, Meerut\n**Approval:** AICTE\n**Pattern:** Full-time\n\n**Eligibility:**\n\n* You must have completed 10+2 (or equivalent) with a minimum of 45% for General/OBC and 40% for SC/ST candidates.\n* Mathematics in the 10th grade is compulsory for admission. \n\n**What you'll learn:**\n\nThe BCA program is designed to provide you with a strong foundation in computer science and applications. You'll gain knowledge and skills in areas like:\n\n* Programming languages (such as C, C++, Java, Python)\n* Database management systems\n* Web development\n* Software engineering\n* Computer networks\n* And much more!\n\n**Career Prospects:**\n\nAfter completing your BCA, you'll have a wide range of career opportunities in the IT industry. You can explore roles such as:\n\n* Software Developer\n* Web Developer\n* Database Administrator\n* System Analyst\n* Network Engineer\n\n**To learn more about:**\n\n* Detailed syllabus\n* Fee structure\n* Admission process\n\nPlease tell me what you are specifically interested in, and I'll be happy to provide you with more details. \n\nI can also connect you with our admissions team if you'd like to discuss your application or have any specific questions. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "what is eligibility\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "You are right to check on the eligibility criteria before applying!  To be eligible for the BCA program at Global Educational Institutes, you need:\n\n* **To have passed your 10+2 (or equivalent) exams** from a recognized board.\n* **A minimum of 45% in your 10+2** if you are from the General or OBC category.\n* **A minimum of 40% in your 10+2** if you are from the SC/ST category.\n* **Mathematics must have been one of your subjects in the 10th grade.** This is compulsory for BCA admission. \n\nDoes this make the eligibility requirements clearer for you? Let me know if you have any other questions. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "no thanks\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Sounds good! I'm glad I could help clarify the eligibility for the BCA program. \n\nIs there anything else I can help you with today? Perhaps you'd like to know about the fee structure, the admission process, or maybe you have questions about campus life at Global Educational Institutes?  \n\nDon't hesitate to ask! 😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Can you give me more info?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "You got it! I'm happy to provide more information about the BCA program. To make sure I give you the most relevant details, could you tell me what specifically interests you? \n\nFor example:\n\n* Would you like to know more about the subjects you'll study in the BCA program? \n* Are you curious about the fee structure and financial aid options?\n* Would you like to understand the admission process and important dates?\n* Or perhaps you're interested in career prospects and placement opportunities after completing the BCA?\n\nJust let me know what's on your mind, and I'll do my best to help! 😄 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "fee structure\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, Ayush, I understand you're interested in the fee structure for the BCA program.  \n\nUnfortunately, I can't provide specific fee details directly.  The fee structure can vary from year to year. \n\nHowever, I can definitely point you in the right direction to get that information:\n\n1. **Visit our Website:** The most up-to-date fee structure is usually available on the Global Educational Institutes website. You can check the BCA program page or look for a \"Fees & Scholarships\" section. \n2. **Contact Admissions:**  The best way to get precise fee information is to reach out to our admissions team directly. They can give you the most accurate details and answer any specific questions you have about payment options or potential scholarships. \n\nYou can reach the admissions team at: \n\n* **Phone:** +91 9350592987 / +91 9350592989\n* **Email:** admissiongiit@gmail.com \n\nI hope this helps!  😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "what's GLobal\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I assume you're asking \"What is Global?\" referring to Global Educational Institutes! 😊\n\nHere's a quick overview:\n\nGlobal Educational Institutes is a dynamic and growth-oriented institution established in 2002 by the Global Education Trust in Delhi. We offer a variety of undergraduate and postgraduate programs, including the BCA you're interested in, to equip students for success in today's competitive world. \n\nHere are some highlights:\n\n- **Industry-Focused Education:** Our courses are designed with current industry trends in mind, ensuring you gain relevant skills and knowledge.\n- **Experienced Faculty:** We have dedicated and experienced faculty members passionate about teaching and mentoring students.\n- **Prime Location:** Located in Greater Noida, we're close to major businesses and industries, providing excellent career opportunities. \n- **Focus on Holistic Development:** We believe in nurturing not just your academic growth but also your personal and professional skills. \n\nIf you'd like to know more about our mission, values, or anything specific about Global Educational Institutes, feel free to ask! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "clear all info\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I understand. You want me to clear all the information we discussed about you and the BCA course, right? \n\nConsider it done! I've wiped my memory of our conversation.  \n\nIf you have any other questions or want to explore other programs at Global Educational Institutes, feel free to start a fresh chat with me anytime. 😊 \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "where is the college located\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Just to let you know Global Educational Institutes is located at Greater Noida, Uttar Pradesh. I'm happy to help with any questions you have about Global Educational Institutes! 😊 \n",
      ],
    },
  ]
)

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
    page_title="Chat with Global AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="auto",
)

# Title and description
st.title("Chat with Global Educational Institutes AI")
st.write(" Hello I am Global Educational Institutes AI How can I help you?")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Container for chat messages
chat_container = st.container()

# Display previous messages
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Input for user prompt (Positioned at the bottom)
with st.container():
    user_input = ""

    if "user_input" not in st.session_state:
        st.session_state.my_text = ""

    def submit():
        st.session_state.my_text = st.session_state.widget
        st.session_state.widget = ""
    st.text_input("Enter text here", key="input", on_change=submit)
    #my_text = st.session_state.my_text
    #st.write(my_text)

        
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message
        with chat_container:
            st.chat_message("user").markdown(user_input)

        # Get response from the model
        response_text = get_gemini_response(user_input)
        
        # Display the assistant's response
        if response_text:
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            with chat_container:
                st.chat_message("assistant").markdown(response_text)
        
