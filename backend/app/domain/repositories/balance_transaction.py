from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from domain.models.balance_transaction import BalanceTransaction


class BalanceTransactionRepository(ABC):
    @abstractmethod
    def get_by_user_id(self, user_id: UUID) -> List[BalanceTransaction]:
        pass

    @abstractmethod
    def create(self, transaction: BalanceTransaction) -> BalanceTransaction:
        pass
