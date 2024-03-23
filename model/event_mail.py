from sqlalchemy import Column, DateTime, Integer, String, Unicode

from model.base_model import BaseModel


class Email(BaseModel):
    __tablename__ = "emails"

    event_id = Column(Integer, nullable=False)
    email_subject = Column(String)
    email_content = Column(Unicode)
    email_sent_at = Column(DateTime, nullable=False)

    __abstract__ = False
    


class Recipient(BaseModel):
    __tablename__ = "email_recipient"

    event_id = Column(Integer, nullable=False)
    email_recipient = Column(String, nullable=False)

    __abstract__ = False
