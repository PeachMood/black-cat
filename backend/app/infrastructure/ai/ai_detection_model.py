# import os
# from huggingface_hub import InferenceClient

from domain.models.ai_detection_model import AIDetectionResult
from domain.repositories.ai_detection_model import AIDetectionModelRepository


class Dima806AIDetectionModelRepository(AIDetectionModelRepository):
    def __init__(self):
        self._name = "dima806/ai_vs_human_generated_image_detection"
        self._prediction_cost = 1
        # Здесь будет инициализация модели
        # self._client = InferenceClient(provider="hf-inference", api_key=os.environ["HF_TOKEN"])
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def prediction_cost(self) -> int:
        return self._prediction_cost

    def predict(self, image_url: str) -> AIDetectionResult:
        # return client.image_classification(image_url, model=self._name)
        raise NotImplementedError
