from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Unicode

from schema.base_model import BaseModel


@dataclass
class Email(BaseModel):
    __tablename__ = "emails"
    __abstract__ = False

    event_id: int = Column(Integer, nullable=False, name="event_id")
    email_subject: str | None = Column(String, name="email_subject")
    email_content: str | None = Column(Unicode, name="email_content")
    email_sent_at: datetime = Column(DateTime, nullable=False, name="email_sent_at")

    def to_dict(cls):
        result = {
            "event_id": cls.event_id,
            "email_subject": cls.email_subject,
            "email_content": cls.email_content,
            "email_sent_at": cls.email_sent_at,
        }
        return result

    def __init__(
        self,
        event_id=None,
        email_subject=None,
        email_content=None,
        email_sent_at=None,
    ):
        self.event_id = event_id
        self.email_subject = email_subject
        self.email_content = email_content
        self.email_sent_at = email_sent_at


class Recipient(BaseModel):
    __tablename__ = "email_recipient"
    __abstract__ = False

    event_id = Column(Integer, nullable=False)
    email_recipient = Column(String, nullable=False)
