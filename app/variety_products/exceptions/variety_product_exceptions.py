class VarietyIdNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class VarietyNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class VarietyOutOfStockException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class NoNewVarietiesException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class VarietyAlreadyInDatabaseException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

class NoDiscountVarietiesException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class InvalidDateInputException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class MatchNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code