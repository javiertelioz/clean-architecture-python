import strawberry
from strawberry.types import Info

from app.infrastructure.configs.graph_ql import (
    get_UserService,
)

from app.infrastructure.schemas.graphql.user.user_schema import (
    UserMutationSchema,
    UserSchema,
)


@strawberry.type(description="Mutate all Entity")
class Mutation:
    @strawberry.field(description="Create a new user")
    def createUser(self, user: UserMutationSchema, info: Info) -> UserSchema:
        userService = get_UserService(info)
        return userService.create(user)

    @strawberry.field(description="Delete an existing user")
    def deleteUser(self, id: str, info: Info) -> None:
        userService = get_UserService(info)
        return userService.delete(id)

    @strawberry.field(description="Update an existing user")
    def updateUser(
        self,
        id: str,
        user: UserMutationSchema,
        info: Info,
    ) -> UserSchema:
        userService = get_UserService(info)

        return userService.update(id, user)
