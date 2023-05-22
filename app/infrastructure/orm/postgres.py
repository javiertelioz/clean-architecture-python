from app.infrastructure.configs.database import Engine
from sqlalchemy.ext.declarative import declarative_base

EntityMeta = declarative_base()


def init_db():
    EntityMeta.metadata.create_all(bind=Engine)
