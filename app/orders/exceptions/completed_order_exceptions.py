class CompletedOrderNotFoundException(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code

class InvalidDateException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code