import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from app.domain.models.base_entity import EntityMeta


class UserEntity(EntityMeta):
    """
    User model represents a user in the application.
    """

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    def normalize(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "lastname": self.lastname,
            "surname": self.surname,
            "email": self.email,
            "phone": self.phone,
        }
