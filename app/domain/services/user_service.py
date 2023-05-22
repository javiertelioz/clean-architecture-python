from typing import List, Optional

from fastapi import Depends

from app.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from app.domain.exceptions.user_not_found_exception import UserNotFoundException
from app.domain.models.user_entity import UserEntity
from app.infrastructure.schemas.pydantic.user_schema import UserSchema
from app.infrastructure.repository.user_repository import UserRepository


class UserService:
    userRepository: UserRepository

    def __init__(self, userRepository: UserRepository = Depends()) -> None:
        self.userRepository = userRepository

    def create(self, user_body: UserSchema) -> Optional[UserEntity]:
        """
        Create a user.

        Args:
            user_body (UserSchema): The user data.

        Returns:
            Optional[UserEntity]: The created user entity, or None if the user already exists.
        """

        exist = self.userRepository.find_by_email(user_body.email)

        if exist:
            raise UserAlreadyExistsException()

        return self.userRepository.create(
            UserEntity(
                name=user_body.name,
                lastname=user_body.lastname,
                surname=user_body.surname,
                email=user_body.email,
                phone=user_body.phone,
                password=user_body.password,
            )
        )

    def get(self, user_id: int) -> UserEntity:
        """
        Get a user by ID.

        Args:
            user_id (int): The user ID.

        Returns:
            UserEntity: The user entity.
        """
        return self.userRepository.find_by_id(user_id)

    def update(self, user_id: int, user_body: UserSchema) -> UserEntity:
        """
        Update a user.

        Args:
            user_id (int): The user ID.
            user_body (UserSchema): The updated user data.

        Returns:
            UserEntity: The updated user entity.
        """
        user = self.userRepository.find_by_id(user_id)

        if not user:
            raise UserNotFoundException()

        user.name = user_body.name
        user.lastname = user_body.lastname
        user.surname = user_body.surname
        user.email = user_body.email
        user.phone = user_body.phone
        user.password = user_body.password

        return self.userRepository.update(user)

    def delete(self, id: str) -> None:
        """
        Delete a user.

        Args:
            id (str): The user ID.
        """
        user = self.userRepository.find_by_id(id)

        if not user:
            raise UserNotFoundException()

        self.userRepository.delete(user)
