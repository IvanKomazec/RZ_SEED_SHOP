

class CartCreationDateInvalidException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class CartNotFoundException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class CartAlreadyInDbException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code