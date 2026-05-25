import numpy as np

from app.services.embedding_service import generate_embedding
from app.services.vector_store import index
from app.services.data_loader import documents


def retrieve_context(query, top_k=4):

    query_embedding = np.array([generate_embedding(query)]).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(documents[idx])

    return "\n".join(results)
