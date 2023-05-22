from unittest.mock import Mock

from app.domain.models.user_entity import UserEntity
from app.infrastructure.repository.user_repository import UserRepository


def test_create_user():
    # Arrange
    db_mock = Mock()
    user_repository = UserRepository(db=db_mock)
    user = UserEntity()

    # Act
    result = user_repository.create(user)

    # Assert
    assert result == user
    db_mock.add.assert_called_once_with(user)
    db_mock.commit.assert_called_once()
    db_mock.refresh.assert_called_once_with(user)


def test_update_user():
    # Arrange
    db_mock = Mock()
    user_repository = UserRepository(db=db_mock)
    user = UserEntity()

    # Act
    result = user_repository.update(user)

    # Assert
    assert result == user
    db_mock.commit.assert_called_once()
    db_mock.refresh.assert_called_once_with(user)


def test_delete_user():
    # Arrange
    db_mock = Mock()
    user_repository = UserRepository(db=db_mock)
    user = UserEntity()

    # Act
    user_repository.delete(user)

    # Assert
    db_mock.delete.assert_called_once_with(user)
    db_mock.commit.assert_called_once()


def test_find_all_users():
    # Arrange
    db_mock = Mock()
    user_repository = UserRepository(db=db_mock)
    expected_result = [UserEntity(), UserEntity()]
    db_mock.query.return_value.all.return_value = expected_result

    # Act
    result = user_repository.find_all()

    # Assert
    assert result == expected_result
    db_mock.query.assert_called_once_with(UserEntity)
    db_mock.query.return_value.all.assert_called_once()


def test_find_user_by_id():
    # Arrange
    db_mock = Mock()
    user_repository = UserRepository(db=db_mock)
    user_id = "example_id"
    expected_result = UserEntity()
    db_mock.query.return_value.filter.return_value.first.return_value = expected_result

    # Act
    result = user_repository.find_by_id(user_id)

    print(result)

    # Assert
    assert result == expected_result

    db_mock.query.assert_called_once_with(UserEntity)
    # db_mock.query.return_value.filter.assert_called_once_with(
    #     UserEntity.id == user_id)
    db_mock.query.return_value.filter().first.assert_called_once()
