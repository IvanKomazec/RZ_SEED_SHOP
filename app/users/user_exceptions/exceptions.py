class IdNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class LastNameNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserIdAlreadyInUseException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class InvalidCustomerIdException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
