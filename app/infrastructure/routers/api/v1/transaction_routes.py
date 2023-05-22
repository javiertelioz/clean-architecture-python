from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/transactions", tags=["Transaction"])


@router.post("/")
def seed() -> dict:
    return {"data": "create transcription successfully"}


@router.post("/report")
def create_report(date: str) -> dict:
    return {"data": "make report successfully"}


@router.get("/report/{date}")
def get_report(date: str) -> dict:
    return {"data": "retrieve report successfully"}
