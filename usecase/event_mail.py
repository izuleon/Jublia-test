from datetime import datetime

from db.base_db import db_session, get_session, init_db
from schema.event_mail import Email


def get_all_emails():
    return Email.query.all()


def get_email(id: int):
    return Email.query.filter(Email.id == id).first()


def save_emails(
    event_id: int, email_subject: str, email_content: str, sent_at: datetime
):
    with get_session() as session:
        new_email = Email(
            event_id=event_id,
            email_subject=email_subject,
            email_content=email_content,
            email_sent_at=sent_at,
        )
        session.add(new_email)
        session.commit()
        session.refresh(new_email)
    return new_email.to_dict()
