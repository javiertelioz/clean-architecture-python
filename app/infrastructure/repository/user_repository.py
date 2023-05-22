from typing import List

from app.domain.contracts.repository.user_repository import UserRepository as Repository
from app.domain.models.user_entity import UserEntity
from app.infrastructure.configs.database import get_db_connection
from fastapi import Depends
from sqlalchemy.orm import Session


class UserRepository(Repository):

    """
    UserRepository provides CRUD operations for User objects using SQLAlchemy.
    """

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def create(self, user: UserEntity) -> UserEntity:
        """
        Create a new user in the repository.

        Args:
            user (User): User object to create.

        Returns:
            User: Created user object.
        """
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def update(self, user: UserEntity) -> UserEntity:
        """
        Update an existing user in the repository.

        Args:
            user (User): User object to update.

        Returns:
            User: Updated user object.
        """
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: UserEntity):
        """
        Delete a user from the repository.

        Args:
            user (User): User object to delete.
        """
        self.db.delete(user)
        self.db.commit()

    def find_all(self) -> list:
        """
        Retrieve all users from the repository.

        Returns:
            list: List of all users.
        """
        return self.db.query(UserEntity).all()

    def find_by_id(self, id: str) -> UserEntity:
        """
        Retrieve a user from the repository by its ID.

        Args:
            id (str): ID of the user to retrieve.

        Returns:
            User: User object with the specified ID, or None if not found.
        """
        return self.db.query(UserEntity).filter(UserEntity.id == id).first()

    def find_by_email(self, email):
        """
        Find a user by email.

        Args:
            email (str): The email to search for.

        Returns:
            User: The found user, or None if not found.
        """
        return self.db.query(UserEntity).filter_by(email=email).first()

    def find_one(self, criteria) -> UserEntity:
        """
        Retrieve a single user from the repository based on the specified criteria.

        Args:
            criteria: Criteria to search for.

        Returns:
            User: User object that matches the criteria, or None if not found.
        """
        return self.db.query(UserEntity).filter_by(**criteria).first()

    def find(self, criteria) -> list:
        """
        Retrieve users from the repository based on the specified criteria.

        Args:
            criteria: Criteria to search for.

        Returns:
            list: List of users that match the criteria.
        """
        return self.db.query(UserEntity).filter_by(**criteria).all()
