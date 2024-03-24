from sqlalchemy import distinct

from db.base_db import get_session
from schema.recipient import Recipient


def get_all_recipient_by_event_id(id: int):
    return Recipient.query.filter(Recipient.event_id == id).all()


def get_all_event_id_registered_to_recipient():
    result = Recipient.query.with_entities(distinct(Recipient.event_id)).all()
    result = [row[0] for row in result]
    return result


def get_recipient_by_id(id: int):
    return Recipient.query.filter(Recipient.id == id).first()


def save_recipient(event_id: int, email_recipient: str):
    with get_session() as session:
        recipient = Recipient(
            event_id=event_id,
            email_recipient=email_recipient,
        )
        session.add(recipient)
        session.commit()
        session.refresh(recipient)
    return recipient.to_dict()
