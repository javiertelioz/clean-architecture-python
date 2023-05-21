from datetime import datetime
from fastapi import HTTPException, status
from app.infrastructure.exception.date_exceptions import DateInvalidError


FORMAT_DATE = '%Y-%m-%d'


def check_valid_date(date: str) -> datetime.date:
    try:
        return datetime.strptime(date, FORMAT_DATE).date()
    except ValueError:
        raise DateInvalidError()


def get_http_exception(exception: Exception) -> HTTPException:
    status_code = exception.status_code if hasattr(
        exception, "status_code") else status.HTTP_500_INTERNAL_SERVER_ERROR
    return HTTPException(status_code=status_code, detail=str(exception))
