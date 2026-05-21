from google import genai

from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_embedding(text):

    response = client.models.embed_content(model="text-embedding-004", contents=text)

    return response.embeddings[0].values
