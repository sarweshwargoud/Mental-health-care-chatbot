import streamlit as st
import time
from langchain.chains import create_retrieval_chain
from langchain_core.messages import HumanMessage
from app_utils.styles import get_custom_css

def initialize_session_state():
    """
    Initialize session state variables for chat history and messages.
    """
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    
    if "chat_started" not in st.session_state:
        st.session_state["chat_started"] = False

def get_chat_history_text():
    """Convert chat history to a formatted string for download."""
    history_text = ""
    for msg in st.session_state.messages:
        role = "User" if msg["role"] == "user" else "Assistant"
        history_text += f"{role}: {msg['content']}\n\n"
    return history_text

def stream_text(text):
    """Generator function to simulate streaming text."""
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

def handle_user_query(get_conversation_chain: create_retrieval_chain, user_query: str):
    """
    Handle the user query and get the response from the conversation chain.
    """
    # Use a spinner for the "thinking" animation
    with st.spinner("Thinking..."):
        response = get_conversation_chain.invoke(
            {"input": user_query, "chat_history": st.session_state["chat_history"]}
        )

    st.session_state["chat_history"].extend(
        [HumanMessage(content=user_query), response["answer"]]
    )

    return response["answer"]

def display_landing_page():
    """Display the welcoming landing page."""
    st.markdown('<h1 class="main-title">Mental Healthcare Chatbot</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Your safe space to talk, reflect, and find balance.</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Start My Check-In", use_container_width=True):
            st.session_state["chat_started"] = True
            st.rerun()

    st.markdown("---")
    st.markdown("<h3 style='text-align: center; color: #555;'>Or start with a topic:</h3>", unsafe_allow_html=True)
    
    scol1, scol2, scol3 = st.columns(3)
    
    # Helper to start chat with a prompt
    def start_with_prompt(prompt):
        st.session_state["chat_started"] = True
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()

    with scol1:
        if st.button("Feeling overwhelmed😟", key="starter_1"):
            start_with_prompt("I'm feeling overwhelmed")
    with scol2:
        if st.button("Practice Mindfulness🧘", key="starter_2"):
            start_with_prompt("How can I practice mindfulness?")
    with scol3:
        if st.button("Anxiety Tips 🛑", key="starter_3"):
            start_with_prompt("Give me some tips to handle anxiety")

def display_chat_interface(conversation_chain: create_retrieval_chain):
    """
    Display the chat interface using Streamlit.
    """
    # Apply Custom CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)

    # Sidebar for Mood Check & Tools
    with st.sidebar:
        st.header("Daily Mood Check-In")
        mood = st.select_slider(
            "How are you feeling right now?",
            options=["😔", "😟", "😐", "🙂", "😁"],
            value="😐"
        )
        st.write(f"Current Mood: {mood}")
        
        st.markdown("---")
        st.header("Session Tools")
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.session_state.chat_started = False
            st.rerun()
            
        st.download_button(
            label="Save Chat History 📥",
            data=get_chat_history_text(),
            file_name=f"chat_history_{int(time.time())}.txt",
            mime="text/plain"
        )

    # Main Logic
    if not st.session_state["chat_started"]:
        display_landing_page()
    else:
        # Chat Header
        st.markdown('<h2 style="text-align: center; color: #00796B;">Mental HealthCare ChatBot</h2>', unsafe_allow_html=True)
        
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # React to user input
        if user_query := st.chat_input("Share your thoughts..."):
            # Display user message in chat message container
            st.chat_message("user").markdown(user_query)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_query})

            response_text = handle_user_query(conversation_chain, user_query)

            # Display assistant response with streaming effect
            with st.chat_message("assistant"):
                st.write_stream(stream_text(response_text))
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response_text})
