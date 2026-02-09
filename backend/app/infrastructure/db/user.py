from typing import Optional, List
from uuid import UUID

from domain.models.user import User
from domain.repositories.user import UserRepository


class SQLUserRepository(UserRepository):
    def __init__(self) -> None:
        # self._db = db_connection
        pass

    def create(self, user: User) -> User:
        raise NotImplementedError

    def get_by_id(self, user_id: UUID) -> Optional[User]:
        raise NotImplementedError

    def update(self, user: User) -> User:
        raise NotImplementedError

    def delete(self, user_id: UUID) -> bool:
        raise NotImplementedError
