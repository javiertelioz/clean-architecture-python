from app.infrastructure.language.i18n import active_translation
from fastapi import Request


def add_middleware(app):
    @app.middleware("http")
    async def get_accept_language(request: Request, call_next):
        active_translation(request.headers.get("accept-language", None))
        response = await call_next(request)
        return response
