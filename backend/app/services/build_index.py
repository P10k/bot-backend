import faiss
import numpy as np
import json
import os

from app.services.embedding_service import generate_embedding


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "courses.json")

INDEX_PATH = os.path.join(BASE_DIR, "data", "faiss_index.index")


with open(DATA_PATH, "r", encoding="utf-8") as f:
    courses = json.load(f)


documents = []

for course in courses:
    text = f"""
Course: {course["course"]}
Duration: {course["duration"]}
Fees: {course["fees"]}
Campus: {course["campus"]}
"""

    documents.append(text)


print("Generating embeddings...")

embeddings = np.array([generate_embedding(doc) for doc in documents]).astype("float32")


dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)


faiss.write_index(index, INDEX_PATH)

print("FAISS index created successfully.")
