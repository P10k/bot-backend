from app.services.embedding_service import generate_embedding
from app.services.db_service import supabase


def retrieve_context(query):

    query_embedding = generate_embedding(query)

    embedding_str = "[" + ",".join(map(str, query_embedding)) + "]"

    response = supabase.rpc(
        "match_courses", {"query_embedding": embedding_str, "match_count": 2}
    ).execute()

    results = response.data

    context = ""

    for item in results:
        context += f"""
        Course: {item["course"]}
        Duration: {item["duration"]}
        Fees: {item["fees"]}
        Campus: {item["campus"]}

        """

    return context
