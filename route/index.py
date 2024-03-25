from datetime import datetime

import pytz
from flask import Blueprint, jsonify, request

index_bp = Blueprint("index", __name__)
from route.event_mail import event_mail


@index_bp.route("/")
def index():
    return "hello world"


@index_bp.post("/save_emails")
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
