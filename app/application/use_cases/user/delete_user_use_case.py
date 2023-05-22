from app.application.base_use_case import UseCase
from app.domain.exceptions.user_not_found_exception import UserNotFoundException
from app.domain.services.user_service import UserService
from fastapi import Depends


class DeleteUserUseCase(UseCase[None]):
    def __init__(self, user_service: UserService = Depends()):
        self.user_service = user_service

    def execute(self, user_id: int) -> None:
        try:
            self.user_service.delete(user_id)
        except UserNotFoundException as e:
            raise e
