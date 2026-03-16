
from fastapi import APIRouter

from src.wsfev1.health_checks.readiness_health_controller import \
    readiness_health_check

router = APIRouter()


@router.get("/wsfev1/health/readiness")
async def readiness() -> dict:

    status = await readiness_health_check()
    return status