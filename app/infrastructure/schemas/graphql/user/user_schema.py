from typing import List
import strawberry


@strawberry.type(description="User Schema")
class UserSchema:
    id: str
    name: str
    lastname: str
    surname: str
    email: str
    phone: str


@strawberry.input(description="User Mutation Schema")
class UserMutationSchema:
    name: str
    lastname: str
    surname: str
    email: str
    phone: str
    password: str
