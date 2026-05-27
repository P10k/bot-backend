import faiss
import numpy as np
import os

from app.services.embedding_service import generate_embedding
from app.services.db_service import get_course_documents


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INDEX_PATH = os.path.join(BASE_DIR, "data", "faiss_index.index")


documents = get_course_documents()


print("Generating embeddings...")

embeddings = np.array([generate_embedding(doc) for doc in documents]).astype("float32")


dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)


faiss.write_index(index, INDEX_PATH)

print("FAISS index updated successfully.")
