from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID, uuid4


from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID, uuid4


class BaseModel(ABC):
    def __init__(self) -> None:
        self._id: UUID = uuid4()
        self._created_at: datetime = datetime.now()
        self._updated_at: datetime = self._created_at

    def _update_timestamp(self) -> None:
        self._updated_at = datetime.now()

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    @abstractmethod
    def to_dict(self) -> dict:
        pass
