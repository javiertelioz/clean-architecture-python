from datetime import date
from typing import Optional

from app.infrastructure.configs.environment import get_environment_variables
from app.infrastructure.language.get_language import get_language
from fastapi import APIRouter, Header

env = get_environment_variables()
router = APIRouter(prefix="/api/v1/services", tags=["Service"])


@router.get("/heartbeat")
def heartbeat(accept_language: Optional[str] = Header(default="en")):
    language = get_language(accept_language)
    return {"status": "success", "version": env.API_VERSION, "language": language, "releaseDate": date.today()}
