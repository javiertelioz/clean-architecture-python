from app.application.base_use_case import UseCase
from app.domain.exceptions.user_not_found_exception import UserNotFoundException
from app.domain.models.user_entity import UserEntity
from app.domain.services.user_service import UserService
from fastapi import Depends


class UpdateUserUseCase(UseCase[None]):
    def __init__(self, user_service: UserService = Depends()):
        self.user_service = user_service

    def execute(self, user_id: str, user_data: dict) -> UserEntity:
        try:
            return self.user_service.update(user_id, user_data).normalize()
        except UserNotFoundException as e:
            raise e
