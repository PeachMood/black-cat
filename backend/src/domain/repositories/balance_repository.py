from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from domain.models.balance import BalanceTransaction


class BalanceRepository(ABC):
    @abstractmethod
    def get_user_balance(self, user_id: UUID) -> int:
        pass

    @abstractmethod
    def get_user_transactions(self, user_id: UUID) -> List[BalanceTransaction]:
        pass

    @abstractmethod
    def update_user_balance(self, transaction: BalanceTransaction) -> bool:
        pass
