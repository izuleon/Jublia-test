from sqlalchemy import Column, DateTime, Integer, String, Unicode, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    email_subject = Column(String)
    email_content = Column(Unicode)
    email_sent_at = Column(DateTime, nullable=False)


class Recipient(Base):
    __tablename__ = "email_recipient"

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    email_recipient = Column(String, nullable=False)
