from flask import Blueprint

event_mail_bp = Blueprint("event_mail", __name__)


@event_mail_bp.route("/event_mail/")
def index():
    return "event mail index"


@event_mail_bp.route("/event_mail/save_emails")
def save_emails():
    return "saving emails"
