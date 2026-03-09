from fastapi import FastAPI

from app.api.routers.health import router as health_router
from app.settings.fast_api import get_fast_api_settings

settings = get_fast_api_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION,
    debug=settings.DEBUG,
)

app.include_router(health_router)
