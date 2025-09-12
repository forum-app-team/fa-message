class AppError(Exception):
    status_code = 400
    code = "APP_ERROR"

    def __init__(self, message, *, details=None, status_code=None, code=None):
        super().__init__(message)
        if status_code:
            self.status_code = status_code
        if code:
            self.code = code
        self.details = details


class NotFoundException(AppError):
    status_code = 404
    code = "NOT_FOUND"


class DuplicateException(AppError):
    status_code = 409
    code = "DUPLICATE"
