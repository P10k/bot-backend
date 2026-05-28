from fastapi import APIRouter

from pydantic import BaseModel

from app.services.db_service import get_courses, supabase
from app.services.embedding_service import generate_embedding


class CourseRequest(BaseModel):
    course: str
    duration: str
    fees: str
    campus: str


router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/courses")
def fetch_courses():

    return get_courses()


@router.post("/courses")
def create_course(course: CourseRequest):

    text = f"""
        Course: {course.course}
        Duration: {course.duration}
        Fees: {course.fees}
        Campus: {course.campus}
        """

    embedding = generate_embedding(text)

    embedding_str = "[" + ",".join(map(str, embedding)) + "]"

    response = (
        supabase.table("courses")
        .insert(
            {
                "course": course.course,
                "duration": course.duration,
                "fees": course.fees,
                "campus": course.campus,
                "embedding": embedding_str,
            }
        )
        .execute()
    )

    return response.data
