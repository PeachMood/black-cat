from typing import Optional, List
from uuid import UUID

from domain.models.ai_detection_task import AIDetectionTask
from domain.repositories.ai_detection_task import AIDetectionTaskRepository


class SQLAIDetectionTaskRepository(AIDetectionTaskRepository):
    def __init__(self) -> None:
        # self._db = db_connection
        pass

    def get_by_id(self, task_id: UUID) -> Optional[AIDetectionTask]:
        raise NotImplementedError

    def get_by_user_id(self, user_id: UUID) -> List[AIDetectionTask]:
        raise NotImplementedError

    def create(self, task: AIDetectionTask) -> AIDetectionTask:
        raise NotImplementedError

    def update(self, task: AIDetectionTask) -> AIDetectionTask:
        raise NotImplementedError

    def delete(self, task_id: UUID) -> bool:
        raise NotImplementedError
