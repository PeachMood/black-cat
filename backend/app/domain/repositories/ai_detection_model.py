from abc import ABC, abstractmethod

from domain.models.ai_detection_model import AIDetectionResult


class AIDetectionModelRepository(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def prediction_cost(self) -> int:
        pass

    @abstractmethod
    def predict(self, image_url: str) -> AIDetectionResult:
        pass
