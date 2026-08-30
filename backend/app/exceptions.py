class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400, code: str = "BAD_REQUEST", field: str = None):
        self.message = message
        self.status_code = status_code
        self.code = code
        self.field = field
