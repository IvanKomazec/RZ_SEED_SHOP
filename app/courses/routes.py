from fastapi import APIRouter

from app.courses.controller import CourseController
from app.courses.schemas import CourseSchema, CourseSchemaIn

course_router = APIRouter(prefix="/api/courses", tags=["Courses"])


@course_router.post("/create-new-course", response_model=CourseSchema)
def create_new_course(course: CourseSchemaIn):
    return CourseController.create_new_course(code=course.code, name=course.name, description=course.description)


@course_router.get("/get-all-courses", response_model=list[CourseSchema])
def get_all_courses():
    courses = CourseController.get_all_courses()
    return courses


@course_router.get("/get-course-by-id", response_model=CourseSchema)
def get_course_by_id(course_id: str):
    return CourseController.get_course_by_id(course_id)


@course_router.delete("/delete-course")
def delete_course_by_id(course_id: str):
    return CourseController.delete_course_by_id(course_id)
