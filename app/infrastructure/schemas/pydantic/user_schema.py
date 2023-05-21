import uuid

from pydantic import BaseModel, Field


class UserPostRequestSchema(BaseModel):
    name = Field(
        "Joe",
        title='Name',
        description='The name of the user.',
    )
    lastname: str = Field(
        "Doe",
        title='Lastname',
        description='The lastname of the user.',
    )
    surname: str | None = Field(
        "Smith",
        title='Surname',
        description='The surname of the user, if available.',
    )
    email: str = Field(
        "joe_doe@mail.com",
        title='Email',
        description='The email address of the user.',
    )
    phone: str = Field(
        "+55555555555",
        title='Phone',
        description='The phone number of the user. Example: "55555555555"',
    )
    password: str = Field(
        "ApiTest_123",
        title='Password',
        description='The password of the user.',
    )


class UserSchema(UserPostRequestSchema):
    id: uuid.UUID = Field(
        title='ID',
        description='The unique identifier of the user.',
    )

    class Config:
        orm_mode = True
