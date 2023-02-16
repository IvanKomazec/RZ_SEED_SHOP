

class CourseExceptionCode(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class CourseNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
