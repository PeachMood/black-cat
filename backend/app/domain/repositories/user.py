from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from domain.models.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: UUID) -> Optional[User]:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: UUID) -> bool:
        pass
