
def get_custom_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #FAFAFA;
            color: #333333;
        }

        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Chat Container Styling */
        .stChatInput {
            border-radius: 20px;
        }

        /* Custom Buttons */
        div.stButton > button {
            background-color: #00796B;
            color: white;
            border-radius: 25px;
            padding: 10px 24px;
            border: none;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        div.stButton > button:hover {
            background-color: #004D40;
            cursor: pointer;
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0,0,0,0.15);
        }

        /* Secondary Buttons / Starter Prompts */
        .starter-prompt > button {
            background-color: #E0F2F1;
            color: #00695C;
            border: 1px solid #B2DFDB;
        }

        .starter-prompt > button:hover {
            background-color: #B2DFDB;
            color: #004D40;
        }

        /* Chat Bubbles CSS Override */
        /* Note: Streamlit's chat elements are hard to target precisely without component inspection, 
           but we can style the markdown content or use custom HTML if needed. 
           For now, we rely on global overrides and standard components. */
        
        /* Fade in animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .stMarkdown {
            animation: fadeIn 0.5s ease-out;
        }

        /* Custom Title */
        .main-title {
            text-align: center;
            color: #004D40;
            font-weight: 700;
            font-size: 2.5rem;
            margin-bottom: 30px;
        }
        
        .sub-title {
            text-align: center;
            color: #00796B;
            font-weight: 400;
            margin-bottom: 20px;
        }

    </style>
    """
