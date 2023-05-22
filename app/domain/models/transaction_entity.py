from sqlalchemy import Column, Integer, String

from app.domain.models.base_entity import EntityMeta


class TransactionEntity(EntityMeta):
    """
    Transaction Entity represents a transaction in the application.
    """

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column("user_id", ForeignKey("users.id"))
    transaction_type = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    datetime = Column(DateTime(timezone=True), server_default=func.now())

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "user_id": self.user_id.__str__(),
            "transaction_type": self.transaction_type.__str__(),
            "amount": self.amount.__str__(),
            "description": self.description.__str__(),
            "datetime": self.datetime.__str__(),
        }
