from datetime import datetime

from db.base_db import db_session, get_session, init_db
from email_scheduler.scheduler_init import get_scheduler
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
    scheduler = get_scheduler()
    scheduler.add_job(send_email, 'date', run_date=sent_at, args=[new_email.id])
    jobs = scheduler.get_jobs()
    print(jobs)
    return new_email.to_dict()

def send_email(email_id, **kwargs):
    # ... (Your email sending code using Flask-Mail or a similar library)
    scheduler = get_scheduler()
    print("email_sent")
    jobs = scheduler.get_jobs()
    print(jobs)
    email = get_email(email_id)