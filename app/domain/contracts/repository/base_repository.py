from abc import abstractmethod

from typing import Generic, List, TypeVar

M = TypeVar("M")
K = TypeVar("K")


class RepositoryMeta(Generic[M, K]):

    @abstractmethod
    def create(self, instance: M) -> M:
        """
        Create a new instance of the Model.

        Args:
            instance (M): The instance to create.

        Returns:
            M: The created instance.
        """
        pass

    @abstractmethod
    def delete(self, id: K) -> None:
        """
        Delete an existing instance of the Model.

        Args:
            id (K): The unique ID of the instance to delete.
        """
        pass

    @abstractmethod
    def get(self, id: K) -> M:
        """
        Fetch an existing instance of the Model by its unique ID.

        Args:
            id (K): The unique ID of the instance to fetch.

        Returns:
            M: The fetched instance.
        """
        pass

    @abstractmethod
    def list(self, limit: int, start: int) -> List[M]:
        """
        List all existing instances of the Model.

        Args:
            limit (int): The maximum number of instances to return.
            start (int): The starting index of instances to return.

        Returns:
            List[M]: The list of instances.
        """
        pass

    @abstractmethod
    def update(self, id: K, instance: M) -> M:
        """
        Update an existing instance of the Model.

        Args:
            id (K): The unique ID of the instance to update.
            instance (M): The updated instance.

        Returns:
            M: The updated instance.
        """
        pass

    @abstractmethod
    def find_one(self, criteria) -> M:
        """
        Find a single instance of the Model based on the specified criteria.

        Args:
            criteria: The criteria to search for.

        Returns:
            M: The found instance, or None if not found.
        """
        pass

    @abstractmethod
    def find(self, criteria) -> List[M]:
        """
        Find instances of the Model based on the specified criteria.

        Args:
            criteria: The criteria to search for.

        Returns:
            List[M]: The list of found instances.
        """
        pass

    @abstractmethod
    def find_by_id(self, id: K) -> M:
        """
        Find an instance of the Model by its ID.

        Args:
            id (K): The ID of the instance to find.

        Returns:
            M: The found instance, or None if not found.
        """
        pass
