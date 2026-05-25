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
        You are a multilingual AI admission assistant.

        Answer ONLY from the provided institution data.
        Reply in the user's language.
        Keep responses short, natural, and conversational.
        Do not use markdown or special formatting.
        If information is unavailable, politely say so.

        Recent Conversation:
        {history_text[-300:]}

        Institution Data:
        {context}

        User Question:
        {user_query}
    """

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    return response.text
