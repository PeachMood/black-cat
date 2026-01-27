from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from domain.models.ai_detection import AIDetectionTask


class AIDetectionTaskRepository(ABC):
    @abstractmethod
    def get_by_id(self, task_id: UUID) -> Optional[AIDetectionTask]:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: UUID) -> List[AIDetectionTask]:
        pass

    @abstractmethod
    def create(self, task: AIDetectionTask) -> AIDetectionTask:
        pass

    @abstractmethod
    def update(self, task: AIDetectionTask) -> AIDetectionTask:
        pass

    @abstractmethod
    def delete(self, task_id: UUID) -> bool:
        pass
