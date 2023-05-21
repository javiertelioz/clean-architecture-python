from .base_repository import RepositoryMeta

from app.domain.models.user_entity import UserEntity


class UserRepository(RepositoryMeta[UserEntity, str]):

    def __init__(self):
        pass

    def find_by_email(self, email):
        """
        Find a user by email.

        Args:
            email (str): The email to search for.

        Returns:
            User: The found user, or None if not found.
        """
        pass
