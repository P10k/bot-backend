from supabase import create_client

import os

from dotenv import load_dotenv

load_dotenv()


supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))


def get_courses():

    response = supabase.table("courses").select("*").execute()

    return response.data


def get_course_documents():

    courses = get_courses()

    documents = []

    for course in courses:
        text = f"""
        Course: {course["course"]}
        Duration: {course["duration"]}
        Fees: {course["fees"]}
        Campus: {course["campus"]}
        """

        documents.append(text)

    return documents
