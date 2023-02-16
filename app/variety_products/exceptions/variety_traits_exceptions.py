class VarietyTraitsAlreadyExistException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class VarietyTraitsNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
