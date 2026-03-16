from fastapi import APIRouter

router = APIRouter()

@router.get("/health/liveness")
def liveness() -> dict:

    return {"health" : "OK"}