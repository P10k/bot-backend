from fastapi import APIRouter

from app.services.index_service import rebuild_index

from pydantic import BaseModel

from app.services.db_service import get_courses, supabase


class CourseRequest(BaseModel):
    course: str
    duration: str
    fees: str
    campus: str


router = APIRouter(prefix="/admin", tags=["Admin"])


@router.post("/rebuild-index")
def rebuild_faiss_index():

    return rebuild_index()


@router.get("/courses")
def fetch_courses():

    return get_courses()


@router.post("/courses")
def create_course(course: CourseRequest):

    response = (
        supabase.table("courses")
        .insert(
            {
                "course": course.course,
                "duration": course.duration,
                "fees": course.fees,
                "campus": course.campus,
            }
        )
        .execute()
    )

    return response.data
