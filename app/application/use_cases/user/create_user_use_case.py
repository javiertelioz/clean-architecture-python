from app.application.base_use_case import UseCase
from app.domain.exceptions.user_already_exists_exception import (
    UserAlreadyExistsException,
)
from app.domain.models.user_entity import UserEntity
from app.domain.services.user_service import UserService
from app.infrastructure.schemas.pydantic.user_schema import UserPostRequestSchema
from fastapi import Depends


class CreateUserUseCase(UseCase[None]):
    def __init__(self, user_service: UserService = Depends()):
        self.user_service = user_service

    def execute(self, user_data: UserPostRequestSchema) -> UserEntity:
        try:
            return self.user_service.create(user_data).normalize()
        except UserAlreadyExistsException as e:
            raise e
