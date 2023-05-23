from typing import List, Optional

import strawberry
from strawberry.types import Info

from app.infrastructure.configs.graph_ql import (
    get_UserService,
)

from app.infrastructure.schemas.graphql.user.user_schema import UserSchema


@strawberry.type(description="Query all entities")
class Query:
    @strawberry.field(description="Get an User")
    def getUseByIdr(self, id: str, info: Info) -> Optional[UserSchema]:
        userService = get_UserService(info)
        return userService.get(id)

    @strawberry.field(description="List all Users")
    def users(self, info: Info) -> List[UserSchema]:
        userService = get_UserService(info)
        return userService.list()
