from sqlalchemy.exc import IntegrityError

from app.courses.models import Course
from app.db import SessionLocal
from app.courses.repositories import CourseRepository
from app.courses.exceptions import CourseExceptionCode


class CourseService:

    @staticmethod
    def create_new_course(code, name, description) -> CourseExceptionCode or Course:
        try:
            with SessionLocal() as db:
                repository = CourseRepository(db)
                course = repository.read_course_by_code(code)
                if course is None:
                    return repository.create_course(code, name, description)
                raise CourseExceptionCode(message="Code already exists in database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_courses():
        try:
            with SessionLocal() as db:
                repository = CourseRepository(db)
                return repository.read_all_courses()
        except Exception as e:
            raise e

    @staticmethod
    def read_course_by_id(course_id):
        try:
            with SessionLocal() as db:
                repository = CourseRepository(db)
                return repository.read_course_by_id(course_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_course_by_id(course_id):
        try:
            with SessionLocal() as db:
                repository = CourseRepository(db)
                return repository.delete_course(course_id)
        except Exception as e:
            raise e

