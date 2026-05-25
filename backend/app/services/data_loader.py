import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "courses.json")


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
