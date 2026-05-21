from google import genai
import os

from dotenv import load_dotenv

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_llm(user_query, context, history):

    history_text = ""

    for msg in history:
        history_text += f"""
{msg["role"]}: {msg["content"]}
"""

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
- If information is unavailable, politely say it is unavailable

User Question:
{user_query}
"""

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    return response.text
