from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class FastAPISettings(BaseSettings):
    PROJECT_NAME: str = "Black Cat API"
    API_VERSION: str = "0.0.1"
    DEBUG: bool = False

    model_config = SettingsConfigDict(
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache()
def get_fast_api_settings() -> FastAPISettings:
    settings = FastAPISettings()
    return settings
