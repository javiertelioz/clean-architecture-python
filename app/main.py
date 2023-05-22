import os

from app.domain.models.base_entity import init
from app.infrastructure.configs.environment import get_environment_variables
from app.infrastructure.metadata.tags import Tags
from app.infrastructure.middleware.language import add_middleware
from app.infrastructure.routers.api.v1.service_router import router as service_router
from app.infrastructure.routers.api.v1.transaction_routes import (
    router as transaction_router,
)
from app.infrastructure.routers.api.v1.user_router import router as user_router
from fastapi import FastAPI

env = get_environment_variables()

app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
)

add_middleware(app)

app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(service_router)


init()
