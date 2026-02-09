from enum import StrEnum
from uuid import UUID
from base_model import BaseModel


class BalanceTransactionType(StrEnum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class BalanceTransaction(BaseModel):
    def __init__(
        self,
        user_id: UUID,
        type: BalanceTransactionType,
        amount: int,
    ) -> None:
        super().__init__()
        self._user_id = user_id
        self._type = type
        self._amount = amount

    @property
    def user_id(self) -> UUID:
        return self._user_id

    @property
    def type(self) -> BalanceTransactionType:
        return self._type

    @property
    def amount(self) -> int:
        return self._amount

    def to_dict(self) -> dict:
        return {
            "id": str(self._id),
            "user_id": str(self._user_id),
            "type": self._type.value,
            "amount": self._amount,
            "created_at": self._created_at.isoformat(),
        }
