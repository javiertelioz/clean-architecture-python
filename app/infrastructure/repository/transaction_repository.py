from app.domain.contracts.repository.transaction_repository import (
    TransactionRepository as Repository,
)
from app.domain.models.transaction_entity import TransactionEntity
from app.infrastructure.configs.database import get_db_connection
from sqlalchemy.orm import Session


class TransactionRepository(Repository):
    """
    TransactionRepository provides CRUD operations for User objects using SQLAlchemy.
    """

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        """
        Initialize the TransactionRepository with a SQLAlchemy session.

        Args:
            session (Session): SQLAlchemy session object.
        """
        self.db = db

    def create(self, user: TransactionEntity) -> TransactionEntity:
        """
        Create a new user in the repository.

        Args:
            user (User): User object to create.

        Returns:
            User: Created user object.
        """
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update(self, user: TransactionEntity) -> TransactionEntity:
        """
        Update an existing user in the repository.

        Args:
            user (User): User object to update.

        Returns:
            User: Updated user object.
        """
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user: TransactionEntity):
        """
        Delete a user from the repository.

        Args:
            user (User): User object to delete.
        """
        self.session.delete(user)
        self.session.commit()

    def find_all(self) -> list:
        """
        Retrieve all users from the repository.

        Returns:
            list: List of all users.
        """
        return self.session.query(TransactionEntity).all()

    def find_by_id(self, user_id: int) -> TransactionEntity:
        """
        Retrieve a user from the repository by its ID.

        Args:
            user_id (int): ID of the user to retrieve.

        Returns:
            User: User object with the specified ID, or None if not found.
        """
        return self.session.query(TransactionEntity).filter(TransactionEntity.id == user_id).first()

    def find_one(self, criteria) -> TransactionEntity:
        """
        Retrieve a single user from the repository based on the specified criteria.

        Args:
            criteria: Criteria to search for.

        Returns:
            User: User object that matches the criteria, or None if not found.
        """
        return self.session.query(TransactionEntity).filter_by(**criteria).first()

    def find(self, criteria) -> list:
        """
        Retrieve users from the repository based on the specified criteria.

        Args:
            criteria: Criteria to search for.

        Returns:
            list: List of users that match the criteria.
        """
        return self.session.query(TransactionEntity).filter_by(**criteria).all()
