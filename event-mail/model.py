from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Email(Base):
  __tablename__ = 'emails'

  id = Column(Integer, primary_key=True)
  event_id = Column(Integer)
  email_recipient = Column(String)
  email_subject = Column(String)
  email_content = Column(String)
  email_sent_at = Column(DateTime)