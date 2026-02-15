from datetime import datetime, timezone
from fastapi import APIRouter

from app.api.schemas.health import HealthCheck


router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    summary="Возвращает статус сервера для мониторинга.",
    response_model=HealthCheck,
)
async def check_health() -> HealthCheck:
    return HealthCheck(
        status="ok",
        timestamp=datetime.now(timezone.utc),
    )
