from enum import StrEnum


class AIDetectionResult(StrEnum):
    AI_GENERATED = "ai_generated"
    HUMAN_CREATED = "human_created"
