import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.domain.models.base_entity import init
from app.infrastructure.metadata.tags import Tags
from app.infrastructure.configs.environment import get_environment_variables
from app.infrastructure.middleware.language import add_middleware

from app.infrastructure.routers.graphql.routers import graphql
from app.infrastructure.routers.api.v1.routers import user_router, service_router, transaction_router


env = get_environment_variables()

app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
    description=env.APP_DESCRIPTION,
)

add_middleware(app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(service_router)
app.include_router(
    graphql,
    prefix="/graphql",
    include_in_schema=False,
)


init()
