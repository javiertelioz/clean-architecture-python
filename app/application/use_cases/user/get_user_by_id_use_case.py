from fastapi import Depends

from app.domain.models.user_entity import UserEntity
from app.domain.services.user_service import UserService
from app.domain.exceptions.user_not_found_exception import UserNotFoundException


class GetUserByIdUseCase:
    def __init__(self, user_service: UserService = Depends()):
        self.user_service = user_service

    def execute(self, user_id: int) -> UserEntity:
        try:
            return self.user_service.get(user_id).normalize()
        except UserNotFoundException as e:
            raise e
