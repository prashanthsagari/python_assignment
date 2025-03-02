class NegativeNumberError(Exception):
    def __init__(self, message="Only positive numbers are allowed !!!"):
        super().__init__(message)