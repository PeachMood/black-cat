from abc import ABC, abstractmethod

from domain.models.ai_detection import AIDetectionResult


class AIDetectionModelRepository(ABC):
    @property
    @abstractmethod
    def model(self) -> str:
        pass

    @property
    @abstractmethod
    def prediction_cost(self) -> int:
        pass

    @abstractmethod
    def predict(self, image_url: str) -> AIDetectionResult:
        pass
