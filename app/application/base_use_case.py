from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class UseCase(Generic[T], ABC):
    @abstractmethod
    def execute(self, *args, **kwargs) -> T:
        pass
