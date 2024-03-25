from datetime import datetime

import pytz
from flask import Blueprint, abort, jsonify, request

event_mail_bp = Blueprint("event_mail", __name__, url_prefix="/event_mail")

from usecase import event_mail


@event_mail_bp.get("/")
def get_emails():
    result = event_mail.get_all_emails()
    return jsonify(result)


@event_mail_bp.get("/<int:id>")
def get_email(id: int):
    result = event_mail.get_email(id=id)
    if result == None:
        abort(404)
    return jsonify(result)


@event_mail_bp.post("/save_emails")
def save_emails():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing data in request body"}), 400

    # Extract data from request
    event_id = data.get("event_id")
    email_subject = data.get("email_subject")
    email_content = data.get("email_content")
    timestamp = data.get("timestamp")
    timestamp_obj = datetime.strptime(timestamp, "%d %b %Y %H:%M")
    timestamp_obj = timestamp_obj.astimezone(tz=pytz.timezone("Asia/Singapore"))
    result = event_mail.save_emails(
        event_id=event_id,
        email_subject=email_subject,
        email_content=email_content,
        sent_at=timestamp_obj,
    )
    return result
