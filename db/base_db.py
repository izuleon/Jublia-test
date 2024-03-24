from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from utils.constant import config as env_config

db_uri = env_config.get("DB_URI", "sqlite:///sqlite-event.sqlite")
engine = create_engine(db_uri)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


def get_engine():
    return engine


def get_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    return session
