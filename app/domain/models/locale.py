from pydantic import BaseModel


class Locale(BaseModel):
    language: str
