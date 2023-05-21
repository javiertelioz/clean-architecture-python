import uuid
import pytest

from app.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from app.domain.exceptions.user_not_found_exception import UserNotFoundException
from app.domain.models.user_entity import UserEntity
from app.infrastructure.schemas.pydantic.user_schema import UserSchema
from app.infrastructure.repository.user_repository import UserRepository
from app.domain.services.user_service import UserService


class MockUserRepository(UserRepository):
    def find_by_email(self, email):
        return None  # raise UserAlreadyExistsException()

    def create(self, instance):
        return UserEntity(
            id="09d2517b-afa9-4562-834a-af473097bb43",
            name="John",
            lastname="Doe",
            surname="Smith",
            email="johndoe@example.com",
            phone="+123456789",
            password="password")

    def find_by_id(self, id):
        return UserEntity(
            id="09d2517b-afa9-4562-834a-af473097bb43",
            name="John",
            lastname="Doe",
            surname="Smith",
            email="johndoe@example.com",
            phone="+123456789",
            password="password")

    def update(self, instance):
        return UserEntity(
            id="09d2517b-afa9-4562-834a-af473097bb43",
            name="John",
            lastname="Doe",
            surname="Smith",
            email="johndoe@example.com",
            phone="+123456789",
            password="password")

    def delete(self, instance):
        pass


@pytest.fixture
def user_service():
    return MockUserRepository()


def test_create_user(user_service):
    # Arrange
    user_body = UserSchema(
        id="09d2517b-afa9-4562-834a-af473097bb43",
        name="John",
        lastname="Doe",
        surname="Smith",
        email="johndoe@example.com",
        phone="+123456789",
        password="password",
    )

    # Act
    user_entity = user_service.create(user_body)

    # Assert
    assert isinstance(user_entity, UserEntity)

    assert user_entity.name == "John"
    assert user_entity.lastname == "Doe"
    # assert user_entity.surname == "Smith"
    assert user_entity.email == "johndoe@example.com"
    assert user_entity.phone == "+123456789"
    assert user_entity.password == "password"


# def test_create_existing_user(user_service):
#     # Arrange
#     user_body = UserSchema(
#         id="09d2517b-afa9-4562-834a-af473097bb43",
#         name="John",
#         lastname="Doe",
#         surname="Smith",
#         email="johndoe@example.com",
#         phone="+123456789",
#         password="password",
#     )

#     # Act & Assert
#     with pytest.raises(UserAlreadyExistsException):
#         user_service.create(user_body)


# def test_get_user(user_service):
#     # Arrange
#     user_id = "1"

#     # Act
#     user_entity = user_service.get(user_id)

#     # Assert
#     assert isinstance(user_entity, UserEntity)
#     assert user_entity.id == "1"


# def test_get_nonexistent_user(user_service):
#     # Arrange
#     user_id = "999"

#     # Act & Assert
#     with pytest.raises(UserNotFoundException):
#         user_service.get(user_id)


# def test_update_user(user_service):
#     # Arrange
#     user_id = "1"
#     user_body = UserSchema(
#         name="Updated Name",
#         lastname="Updated Lastname",
#         surname="Updated Surname",
#         email="updateduser@example.com",
#         phone="+987654321",
#         password="newpassword",
#     )

#     # Act
#     user_entity = user_service.update(user_id, user_body)

#     # Assert
#     assert isinstance(user_entity, UserEntity)
#     assert user_entity.name == "Updated Name"
#     assert user_entity.lastname == "Updated Lastname"
#     assert user_entity.surname == "Updated Surname"
#     assert user_entity.email == "updateduser@example.com"
#     assert user_entity.phone == "+987654321"
#     assert user_entity.password == "newpassword"


# def test_update_nonexistent_user(user_service):
#     # Arrange
#     user_id = "999"
#     user_body = UserSchema(
#         name="Updated Name",
#         lastname="Updated Lastname",
#         surname="Updated Surname",
#         email="updateduser@example.com",
#         phone="+987654321",
#         password="newpassword",
#     )

#     # Act & Assert
#     with pytest.raises(UserNotFoundException):
#         user_service.update(user_id, user_body)


# def test_delete_user(user_service):
#     # Arrange
#     user_id = "1"

#     # Act
#     user_service.delete(user_id)

#     # Assert
#     # Check if the user is deleted (implementation-specific assertion)


# def test_delete_nonexistent_user(user_service):
#     # Arrange
#     user_id = "999"

#     # Act & Assert
#     with pytest.raises(UserNotFoundException):
#         user_service.delete(user_id)
