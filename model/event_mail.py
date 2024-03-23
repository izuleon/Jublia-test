from sqlalchemy import Column, DateTime, Integer, String, Unicode

from model.base_model import BaseModel


class Email(BaseModel):
    __tablename__ = "emails"
    __abstract__ = False

    event_id = Column(Integer, nullable=False)
    email_subject = Column(String)
    email_content = Column(Unicode)
    email_sent_at = Column(DateTime, nullable=False)


class Recipient(BaseModel):
    __tablename__ = "email_recipient"
    __abstract__ = False

    event_id = Column(Integer, nullable=False)
    email_recipient = Column(String, nullable=False)
