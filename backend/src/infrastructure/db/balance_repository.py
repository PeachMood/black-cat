from typing import List
from uuid import UUID

from domain.models.balance import BalanceTransaction
from domain.repositories.balance_repository import BalanceRepository


class SQLBalanceRepository(BalanceRepository):
    def __init__(self) -> None:
        # self._db = db_connection
        pass

    def get_user_balance(self, user_id: UUID) -> int:
        raise NotImplementedError

    def get_user_transactions(self, user_id: UUID) -> List[BalanceTransaction]:
        raise NotImplementedError

    def update_user_balance(self, transaction: BalanceTransaction) -> bool:
        raise NotImplementedError
