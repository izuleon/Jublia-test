from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

from db.base_db import db_session

Base = declarative_base()
Base.query = db_session.query_property()


@dataclass
class BaseModel(Base):
    """Base class for all models."""

    id: int = Column(Integer, primary_key=True, autoincrement=True, name="id")
    created_at: datetime = Column(DateTime, default=datetime.now(), name="created_at")
    updated_at: datetime = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), name="updated_at"
    )
    deleted_at: datetime | None = Column(DateTime, nullable=True, name="deleted_at")

    __abstract__ = True
