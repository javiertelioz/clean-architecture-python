from fastapi import Depends

from app.domain.services.user_service import UserService
from app.domain.exceptions.user_not_found_exception import UserNotFoundException


class DeleteUserUseCase:
    def __init__(self, user_service: UserService = Depends()):
        self.user_service = user_service

    def execute(self, user_id: int) -> None:
        try:
            self.user_service.delete(user_id)
        except UserNotFoundException as e:
            raise e
