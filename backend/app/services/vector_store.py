import faiss
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INDEX_PATH = os.path.join(BASE_DIR, "data", "faiss_index.index")


print("Loading FAISS index...")

index = faiss.read_index(INDEX_PATH)

print("FAISS index loaded.")
