import faiss
import numpy as np
import json

from app.services.embedding_service import generate_embedding

with open("app/data/courses.json", "r") as f:
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

embeddings = np.array([generate_embedding(doc) for doc in documents]).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)
