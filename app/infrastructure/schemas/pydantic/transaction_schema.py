from pydantic import BaseModel


class TransactionPostRequestSchema(BaseModel):
    name: str


class BookSchema(TransactionPostRequestSchema):
    id: int


class TransactionUserPostRequestSchema(BaseModel):
    author_id: int
