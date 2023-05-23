from fastapi import APIRouter

transaction_router = APIRouter(prefix="/api/v1/transactions", tags=["Transaction"])


@transaction_router.post("/")
def seed() -> dict:
    return {"data": "create transcription successfully"}


@transaction_router.post("/report")
def create_report(date: str) -> dict:
    return {"data": "make report successfully"}


@transaction_router.get("/report/{date}")
def get_report(date: str) -> dict:
    return {"data": "retrieve report successfully"}
