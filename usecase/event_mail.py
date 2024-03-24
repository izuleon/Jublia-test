from datetime import datetime

from flask_mail import Message

from db.base_db import get_session
from schema.event_mail import Email
from utils.config import get_mail
from utils.scheduler_init import get_scheduler


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
    scheduler = get_scheduler()
    scheduler.add_job(
        send_email_to_event,
        "date",
        run_date=sent_at,
        args=[new_email.id],
        misfire_grace_time=1800,
    )
    return new_email.to_dict()


def send_email_to_event(email_id, *args, **kwargs):
    from usecase.recipient import get_all_recipient_by_event_id
    from utils.config import get_app

    email: Email = get_email(email_id)
    recipient_list = get_all_recipient_by_event_id(email.event_id)
    recipient_list = [recipient.email_recipient for recipient in recipient_list]
    with get_app().app_context():
        for recipient in recipient_list:
            send_email(
                recipient=recipient,
                subject=email.email_subject,
                content=email.email_content,
            )


def send_email(
    recipient: str, subject: str = None, content: str = None, *args, **kwargs
):
    from utils.constant import config as env_config

    mail = get_mail()
    sender = env_config.get("MAIL_USERNAME")
    msg = Message(
        recipients=[
            recipient,
        ],
        subject=subject,
        body=content,
        sender=sender,
    )
    mail.send(message=msg)
