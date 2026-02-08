from enum import StrEnum
from typing import Optional
from uuid import UUID
from base_model import BaseModel


class AIDetectionStatus(StrEnum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class AIDetectionResult(StrEnum):
    AI_GENERATED = "ai_generated"
    HUMAN_CREATED = "human_created"


class AIDetectionTask(BaseModel):
    def __init__(self, user_id: UUID, image_hash: str, image_url: str) -> None:
        super().__init__()
        self._user_id = user_id
        self._image_hash = image_hash
        self._image_url = image_url
        self._status = AIDetectionStatus.IN_PROGRESS
        self._result: Optional[AIDetectionResult] = None
        self._error: Optional[str] = None

    @property
    def user_id(self) -> UUID:
        return self._user_id

    @property
    def status(self) -> AIDetectionStatus:
        return self._status

    @property
    def result(self) -> Optional[AIDetectionResult]:
        return self._result

    @property
    def image_hashes(self) -> str:
        return self._image_hash

    @property
    def image_urls(self) -> str:
        return self._image_url

    @property
    def error(self) -> Optional[str]:
        return self._error

    def complete_prediction(self, result: AIDetectionResult) -> None:
        self._status = AIDetectionStatus.COMPLETED
        self._result = result
        self._error = None
        self._update_timestamp()

    def cancel_prediction(self) -> None:
        self._status = AIDetectionStatus.CANCELLED
        self._result = None
        self._error = None
        self._update_timestamp()

    def fail_prediction(self, error: str) -> None:
        self._status = AIDetectionStatus.FAILED
        self._result = None
        self._error = error
        self._update_timestamp()

    def to_dict(self) -> dict:
        return {
            "id": str(self._id),
            "user_id": str(self._user_id),
            "status": self._status.value,
            "result": self._result.value if self._result else None,
            "image_hash": self._image_hash,
            "image_urls": self._image_url,
            "error": self._error,
            "created_at": self._created_at.isoformat(),
            "updated_at": self._updated_at.isoformat(),
        }
