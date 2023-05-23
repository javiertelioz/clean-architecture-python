from fastapi import Depends
from strawberry.types import Info

from app.domain.services.user_service import UserService


# GraphQL Dependency Context
async def get_graphql_context(
    userService: UserService = Depends(),
):
    return {
        "userService": userService,
    }


def get_UserService(info: Info) -> UserService:
    return info.context["userService"]
