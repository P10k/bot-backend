from app.services.db_service import get_courses, supabase

from app.services.embedding_service import generate_embedding


def sync_embeddings():

    courses = get_courses()

    for course in courses:
        text = f"""
        Course: {course["course"]}
        Duration: {course["duration"]}
        Fees: {course["fees"]}
        Campus: {course["campus"]}
        """

        embedding = generate_embedding(text)

        embedding_str = "[" + ",".join(map(str, embedding)) + "]"

        response = supabase.rpc(
            "update_course_embedding",
            {"course_id": course["id"], "embedding_value": embedding_str},
        ).execute()

    print("Embeddings synced successfully.")


sync_embeddings()
