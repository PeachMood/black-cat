from typing import List
from uuid import UUID

from domain.models.balance_transaction import BalanceTransaction
from domain.repositories.balance_transaction import BalanceTransactionRepository


class SQLBalanceTransactionRepository(BalanceTransactionRepository):
    def __init__(self) -> None:
        # self._db = db_connection
        pass

    def get_by_user_id(self, user_id: UUID) -> List[BalanceTransaction]:
        raise NotImplementedError
