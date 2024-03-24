from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from schema.base_model import BaseModel


@dataclass
class Recipient(BaseModel):
    __tablename__ = "email_recipient"
    __abstract__ = False

    event_id: int = Column(Integer, nullable=False)
    email_recipient: str = Column(String, nullable=False)

    def to_dict(cls):
        result = {
            "event_id": cls.event_id,
            "email_recipient": cls.email_recipient,
        }
        return result

    def __init__(
        self,
        event_id=None,
        email_recipient=None,
    ):
        self.event_id = event_id
        self.email_recipient = email_recipient
