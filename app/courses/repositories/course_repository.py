from app.courses.models import Course
from app.courses.exceptions import CourseNotFoundException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


class CourseRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_course(self, code: str, name: str, description: str):
        try:
            course = Course(code, name, description)
            self.db.add(course)
            self.db.commit()
            self.db.refresh(course)
            return course
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_courses(self):
        courses = self.db.query(Course).all()
        return courses

    def read_course_by_id(self, course_id: str):
        course = self.db.query(Course).filter(Course.id == course_id).first()
        if course is None:
            raise CourseNotFoundException(f"Course with provided ID: {course_id} not found.", 400)
        return course

    def delete_course(self, course_id):
        try:
            course = self.db.query(Course).filter(Course.id == course_id).first()
            if course is None:
                raise CourseNotFoundException(f"Course with provided ID: {course_id} not found.", 400)
            self.db.delete(course)
            self.db.commit()
            # self.db.refresh(course)
            return True
        except Exception as e:
            raise e

    def read_course_by_code(self, code):
        course = self.db.query(Course).filter(Course.code == code).first()
        return course
