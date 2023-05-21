from fastapi import status


class ResponseInvalidError(Exception):
    ERROR = 'El response no fue exitoso: Error: %s'

    def __init__(self, message: str):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        super().__init__(self.ERROR % message)
