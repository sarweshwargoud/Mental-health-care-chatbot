# 🧠 Mental Healthcare Chatbot.

An AI-powered **Mental Healthcare Chatbot** designed to provide empathetic, supportive, and informative conversations using **Google Gemini (Generative AI)**.  
The application is built using **Python and Streamlit** and deployed on **Render**.

⚠️ This project is intended for **educational and supportive purposes only** and does **not replace professional mental health care**.

---

## 📌 Table of Contents

- About the Project
- Motivation
- Features
- Tech Stack
- Live Deployment
- Installation (Local Setup)
- Usage
- Project Structure
- How It Works
- Database Folder (`db`)
- Deployment on Render
- Environment Variables
- Future Enhancements
- Disclaimer
- License

---

## 🧾 About the Project

The **Mental Healthcare Chatbot** leverages **Google Gemini** to generate human-like, empathetic responses for mental health–related queries.  
The chatbot runs with a lightweight architecture and does **not require a full database setup** for basic operation.

A **Streamlit-based web interface** allows users to interact easily through a browser.

---

## 🎯 Motivation

Mental health resources are often difficult to access instantly. This project aims to:

- Demonstrate responsible use of Generative AI in sensitive domains
- Provide immediate, supportive conversational guidance
- Build a clean, deployable AI application for learning and portfolio use

---

## 💡 Features

- 🗣️ AI-powered mental health conversations
- 🤝 Empathetic and supportive response style
- 🌐 Interactive Streamlit web interface
- 🔐 Secure API key handling via environment variables
- 🗂️ Optional database folder for future use
- 🚀 Deployed using Render

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Programming Language | Python |
| UI Framework | Streamlit |
| LLM | Google Gemini (gemini-pro) |
| Deployment Platform | Render |
| Version Control | Git & GitHub |

---

## 🌍 Live Deployment

🔗 **Live App URL**  
```
https://mental-health-care-chatbot.onrender.com
```



---

## 🚀 Installation (Local Setup)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sarweshwargoud/Mental-health-care-chatbot.git
cd Mental-health-care-chatbot
```
## 2️⃣ Create & Activate Virtual Environment
```bash

python -m venv venv
```
Windows
---
```bash

venv\Scripts\activate
```

macOS / Linux
---
```bash

source venv/bin/activate
```
---
## 3️⃣ Install Dependencies
```bash

pip install -r requirements.txt
```
## ▶️ Usage
Run the Streamlit app locally:

```bash

streamlit run app.py
```
Open in browser:

arduino
```
http://localhost:8501
```
## 📁 Project Structure

```
Mental-health-care-chatbot/
│
├── .streamlit/
│   └── config.toml              # Streamlit configuration
│
├── app.py                       # Main Streamlit application
│
├── requirements.txt             # Python dependencies
│
├── mental_healthcare_chatbot/
│   ├── __init__.py
│   ├── chatbot.py               # Core chatbot logic using Gemini
│   └── prompts.py               # Prompt templates / system instructions
│
├── app_utils/
│   ├── __init__.py
│   └── helpers.py               # Utility/helper functions
│
├── faiss_db_raptor/             # Vector store (if RAG is enabled)
│
├── db/
│   └── .gitkeep                 # Placeholder for future database usage
│
├── assets/
│   └── screenshots/             # Screenshots / demo images (optional)
│
├── .gitignore                   # Ignored files and folders
│
├── render.yaml                  # Render deployment configuration (optional)
│
└── README.md                    # Project documentation

```
---
## 🧠 How It Works
-User enters a message in the Streamlit UI

-The input is sent to Google Gemini (gemini-pro)

-Gemini generates a context-aware and empathetic response

-The response is displayed back to the user

-The chatbot does not permanently store user data by default.
---


## ☁️ Deployment on Render
Build Command
```bash

pip install -r requirements.txt

```
```bash

streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```
Instance Type
Free tier

## 🔐 Environment Variables
Set the Gemini API key in Render:

Key	Value
GEMINI_API_KEY	Your Gemini API key

Used in code as:

python
```
import os
import google.generativeai as genai
```
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
## 🔮 Future Enhancements
## 💬 Chat history storage

-🌍 Multilingual support

-🎙️ Voice-based interaction

-📊 Usage analytics

-🧠 Emotion / sentiment detection

-🔗 RAG-based document grounding

## ⚠️ Disclaimer
This chatbot is not a medical device and does not provide diagnosis or treatment.
If you are experiencing severe mental health distress, please consult a qualified professional.

## 📜 License
This project is licensed under the MIT License.



---



