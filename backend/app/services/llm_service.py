import google.generativeai as genai
import os

from dotenv import load_dotenv
from app.services.conversation_memory import get_history
from app.utils.language_detector import detect_language

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(user_query, context, history):

    history_text = ""

    for msg in history:
        history_text += f"""
            {msg["role"]}: {msg["content"]}
            """

    # language = detect_language(user_query)

    # language_map = {"en": "English", "kn": "Kannada", "hi": "Hindi", "mr": "Marathi"}

    # reply_language = language_map.get(language, "English")

    prompt = f"""
You are a multilingual AI admission assistant for an institution.

Answer ONLY using provided institution data.

Conversation History:
{history_text}

Institution Data:
{context}

IMPORTANT RULES:
- Understand Kannada, Hindi, Marathi, and English
- Reply in the SAME language as the user
- NEVER ask user to speak in English
- ONLY answer from institution data
- Keep answers short and natural
- Remember previous conversation context
- Remember conversation context
- If information is unavailable, politely say it is unavailable

User Question:
{user_query}
"""

    response = model.generate_content(prompt)

    return response.text
