from sqlalchemy.orm import Session
from app.domain.models.user import UserEntity
from app.domain.contracts.repository.user_repository import UserRepository as Repository


class UserRepository(Repository):
    """
    UserRepository provides CRUD operations for User objects using SQLAlchemy.
    """

    def __init__(self, session: Session):
        """
        Initialize the UserRepository with a SQLAlchemy session.

        Args:
            session (Session): SQLAlchemy session object.
        """
        self.session = session

    def create(self, user: UserEntity) -> UserEntity:
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

    def update(self, user: UserEntity) -> UserEntity:
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

    def delete(self, user: UserEntity):
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
        return self.session.query(UserEntity).all()

    def find_by_id(self, user_id: int) -> UserEntity:
        """
        Retrieve a user from the repository by its ID.

        Args:
            user_id (int): ID of the user to retrieve.

        Returns:
            User: User object with the specified ID, or None if not found.
        """
        return self.session.query(UserEntity).filter(
            UserEntity.id == user_id).first()

    def find_one(self, criteria) -> UserEntity:
        """
        Retrieve a single user from the repository based on the specified criteria.

        Args:
            criteria: Criteria to search for.

        Returns:
            User: User object that matches the criteria, or None if not found.
        """
        return self.session.query(UserEntity).filter_by(**criteria).first()

    def find(self, criteria) -> list:
        """
        Retrieve users from the repository based on the specified criteria.

        Args:
            criteria: Criteria to search for.

        Returns:
            list: List of users that match the criteria.
        """
        return self.session.query(UserEntity).filter_by(**criteria).all()
