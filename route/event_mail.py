from flask import Blueprint

event_mail_bp = Blueprint("event_mail", __name__, url_prefix="/event_mail")
from usecase import event_mail


@event_mail_bp.get("/")
def index():
    return "event mail index"


@event_mail_bp.post("/save_emails")
def save_emails(
    self,
):
    result = event_mail.save_emails()
    return result
